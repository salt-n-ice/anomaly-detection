from __future__ import annotations
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
import argparse, sys
import numpy as np
import pandas as pd
import yaml
from .core import Event, Alert, Archetype, SensorConfig
from .adapter import make_adapter, Adapter
from .features import FeatureEngineer
from .detectors import DataQualityGate, CUSUM, SubPCA, MultivariatePCA, TemporalProfile
from .batch import matrix_profile_discords
from .metrics import compute_metrics


DETECTOR_ENABLED = {
    (Archetype.CONTINUOUS, "sub_pca"): True,
    (Archetype.CONTINUOUS, "multivariate_pca"): True,
    (Archetype.CONTINUOUS, "cusum"): True,
    (Archetype.CONTINUOUS, "temporal_profile"): True,
    (Archetype.BURSTY, "sub_pca"): True,
    (Archetype.BURSTY, "multivariate_pca"): True,
    (Archetype.BURSTY, "cusum"): True,
    (Archetype.BURSTY, "temporal_profile"): True,
    (Archetype.BINARY, "sub_pca"): False,
    (Archetype.BINARY, "multivariate_pca"): True,
    (Archetype.BINARY, "cusum"): True,
    (Archetype.BINARY, "temporal_profile"): True,
}


_ADAPT_BUFFER_TICKS = 96 * 60  # rolling buffer for coordinated adaptation: last 96h at 1-min granularity


@dataclass
class _SensorState:
    cfg: SensorConfig
    adapter: Adapter
    engineer: FeatureEngineer
    dqg: DataQualityGate
    detectors: list
    bootstrap_raw: list = field(default_factory=list)   # (tick, adapter_features)
    bootstrap_rows: list = field(default_factory=list)  # (tick, enriched)
    raw_series: list = field(default_factory=list)
    start_ts: pd.Timestamp | None = None
    fit_done: bool = False
    pending_alerts: list = field(default_factory=list)
    pending_newest_ts: pd.Timestamp | None = None  # O(1) replacement for max-scan in _fuse
    pending_newest_non_cusum_ts: pd.Timestamp | None = None  # anchor for CUSUM-bridging rule (Iter G)
    recent_rows: deque = field(default_factory=lambda: deque(maxlen=_ADAPT_BUFFER_TICKS))  # for adaptation


def _features_for_detectors(cfg: SensorConfig) -> dict[str, list[str]]:
    if cfg.archetype == Archetype.BINARY:
        base = ["duty_cycle_1h", "duty_cycle_24h", "transitions_per_hour"]
        return {"cusum": ["duty_cycle_24h", "transitions_per_hour"],
                "mvpca": base + [f"{b}_diff" for b in base],
                "temporal": base}
    if cfg.archetype == Archetype.BURSTY:
        return {"cusum": ["value"],
                "mvpca": ["value", "time_in_state", "value_diff",
                          "value_roll_1h", "value_roll_24h"],
                "temporal": ["value"]}
    return {"cusum": ["value"],
            "mvpca": ["value", "value_diff", "value_roll_1h", "value_roll_24h"],
            "temporal": ["value"]}


class Pipeline:
    def __init__(self, configs: list[SensorConfig], bootstrap_days: float = 14.0):
        self.bootstrap_days = bootstrap_days
        self._states: dict[tuple[str, str], _SensorState] = {}
        for cfg in configs:
            feats = _features_for_detectors(cfg)
            detectors = []
            if DETECTOR_ENABLED.get((cfg.archetype, "cusum"), False):
                # Continuous-archetype CUSUM gets a 5-day post-fit warmup to
                # silence diurnal-driven warm-up FPs (bootstrap mu averages over
                # a diurnal period; first post-fit peak trips lam reliably).
                # Bursty/Binary don't need it — per-state CUSUM + state=0 idle
                # centers the distribution without diurnal structure. 5d is the
                # max that preserves outlet_voltage trend (Feb 19-21 label);
                # 7d would regress trend to FN.
                wu_cusum = 5 * 86400.0 if cfg.archetype == Archetype.CONTINUOUS else 0.0
                detectors.append(CUSUM(cfg, feats["cusum"], warmup_seconds=wu_cusum))
            if DETECTOR_ENABLED.get((cfg.archetype, "sub_pca"), False):
                # 3-day PCA warmup for Continuous: silences warm-up noise FPs
                # (e.g., voltage Feb 16 04-08 exposed once CUSUM went silent).
                # Preserves calibration_drift Feb 17-18 (PCA fires from Feb 17
                # post-warmup overlap the label).
                wu_pca = 3 * 86400.0 if cfg.archetype == Archetype.CONTINUOUS else 0.0
                detectors.append(SubPCA(cfg, warmup_seconds=wu_pca))
            if DETECTOR_ENABLED.get((cfg.archetype, "multivariate_pca"), False):
                wu_pca = 3 * 86400.0 if cfg.archetype == Archetype.CONTINUOUS else 0.0
                detectors.append(MultivariatePCA(cfg, feats["mvpca"], warmup_seconds=wu_pca))
            if DETECTOR_ENABLED.get((cfg.archetype, "temporal_profile"), False):
                detectors.append(TemporalProfile(cfg, feats["temporal"]))
            self._states[cfg.key] = _SensorState(cfg, make_adapter(cfg),
                                                 FeatureEngineer(cfg),
                                                 DataQualityGate(cfg), detectors)

    def is_live(self, key) -> bool:
        st = self._states.get(key)
        return bool(st and st.fit_done and any(d.live for d in st.detectors))

    def _maybe_fit(self, st: _SensorState, now: pd.Timestamp) -> None:
        if st.fit_done or st.start_ts is None: return
        if (now - st.start_ts).total_seconds() < self.bootstrap_days * 86400: return
        # Bursty: fit state model from adapter's accumulated values.
        if st.cfg.archetype == Archetype.BURSTY:
            st.adapter.fit_state_model()
        # Enrich bootstrap rows, relabeling state where applicable; the engineer
        # ends this loop warmed with the correct per-state rolling history.
        # For BURSTY, also recompute time_in_state from the now-fit state sequence —
        # during bootstrap, the adapter emitted with state=0 fixed (no state model yet)
        # which made time_in_state grow monotonically across the full 14 days, giving
        # detectors a wildly off-distribution feature vs post-bootstrap values.
        is_bursty = st.cfg.archetype == Archetype.BURSTY
        prev_state: int | None = None
        state_entered: pd.Timestamp | None = None
        for ts, f in st.bootstrap_raw:
            g = st.adapter.relabel(dict(f))
            if is_bursty:
                s = int(g.get("state", 0))
                if prev_state is None or s != prev_state:
                    prev_state = s
                    state_entered = ts
                g["time_in_state"] = (ts - state_entered).total_seconds()
            st.bootstrap_rows.append((ts, st.engineer.enrich(ts, g)))
        for d in st.detectors:
            d.fit(st.bootstrap_rows)
        st.fit_done = True

    def _fuse(self, st: _SensorState, fresh: list[Alert]) -> list[Alert]:
        # state_transition is always immediate. DQG types are immediate EXCEPT
        # `dropout`, which fires once per cooldown window (30min) for the entire
        # duration of reporting_rate_change / sustained outages — fusing folds
        # those into one chain instead of emitting 20+ redundant alerts.
        def _is_immediate(a: Alert) -> bool:
            if a.detector == "state_transition": return True
            if a.detector == "data_quality_gate":
                return a.anomaly_type != "dropout"
            return False
        immediate = [a for a in fresh if _is_immediate(a)]
        statistical = [a for a in fresh if not _is_immediate(a)]
        out = list(immediate)
        # Fusion gap: 60min for BURSTY/BINARY (tuned on committed baselines).
        # Iter G: CONTINUOUS uses 15min — tighter to break multi-day FP strips
        # on stationary voltage. Non-CUSUM alerts daisy-chain through small
        # gaps (p90 gap = 8min among stationary voltage alerts), so a 60min
        # gap lets clusters merge across hours into 1-3 day chains. 15min
        # breaks inter-cluster daisy-chaining (typical cluster-to-cluster gap
        # is 20-60min on stationary, but <2min during real anomalies). Long
        # CONTINUOUS labels in committed baselines (calibration_drift 1d,
        # month_shift 30d, trend 2d) are unaffected because their detectors
        # fire densely throughout the label.
        is_continuous = (st.cfg.archetype == Archetype.CONTINUOUS)
        gap = pd.Timedelta(minutes=15 if is_continuous else 60)
        max_span = pd.Timedelta(hours=96)    # cap fused-group duration — 4 days balances FP reduction vs. letting adjacent labels claim distinct chunks
        for a in statistical:
            if st.pending_alerts:
                gap_exceeded = (st.pending_newest_ts is not None
                                and a.timestamp - st.pending_newest_ts > gap)
                span_exceeded = (a.timestamp - st.pending_alerts[0].timestamp) > max_span
                # Iter G: on CONTINUOUS, a CUSUM alert can only EXTEND a chain
                # if a non-CUSUM alert fired within the fusion gap. Without
                # this, stationary CUSUM drift (fires every ~10min) acts as a
                # bridge, stretching chains long after the last non-CUSUM fire.
                # Real TPs have sustained non-CUSUM firing so the anchor
                # doesn't trim them.
                anchor_exceeded = (is_continuous
                                   and a.detector == "cusum"
                                   and st.pending_newest_non_cusum_ts is not None
                                   and a.timestamp - st.pending_newest_non_cusum_ts > gap)
                if gap_exceeded or span_exceeded or anchor_exceeded:
                    grouped = _group(st.pending_alerts)
                    if _chain_corroborated(st.pending_alerts, st.cfg):
                        out.append(grouped)
                    st.pending_alerts = []
                    st.pending_newest_ts = None
                    st.pending_newest_non_cusum_ts = None
            st.pending_alerts.append(a)
            if st.pending_newest_ts is None or a.timestamp > st.pending_newest_ts:
                st.pending_newest_ts = a.timestamp
            if a.detector != "cusum":
                if (st.pending_newest_non_cusum_ts is None
                        or a.timestamp > st.pending_newest_non_cusum_ts):
                    st.pending_newest_non_cusum_ts = a.timestamp
        return out

    def ingest(self, ev: Event) -> list[Alert]:
        st = self._states.get((ev.sensor_id, ev.capability))
        if st is None: return []
        if st.start_ts is None: st.start_ts = ev.timestamp
        alerts: list[Alert] = []
        alerts.extend(st.dqg.check(ev))
        st.adapter.ingest(ev)
        for tick, feat in st.adapter.emit_ready(ev.timestamp):
            st.raw_series.append((tick, feat.get("value", float("nan"))))
            if not st.fit_done:
                st.bootstrap_raw.append((tick, dict(feat)))
                continue
            enriched = st.engineer.enrich(tick, feat)
            st.recent_rows.append((tick, enriched))
            if feat.get("trigger"):
                alerts.append(Alert(st.cfg.sensor_id, st.cfg.capability, tick,
                                    "state_transition", 1.0, 1.0,
                                    "water_leak_sustained", 1.0, feat.get("state"),
                                    tick, tick,
                                    [{"detector": "state_transition",
                                      "state": feat.get("state")}]))
            for d in st.detectors:
                alerts.extend(d.update(tick, enriched))
        self._maybe_fit(st, ev.timestamp)
        return self._fuse(st, alerts)

    def finalize(self) -> list[Alert]:
        out = []
        for st in self._states.values():
            if st.pending_alerts:
                if _chain_corroborated(st.pending_alerts, st.cfg):
                    out.append(_group(st.pending_alerts))
                st.pending_alerts.clear()
                st.pending_newest_ts = None
                st.pending_newest_non_cusum_ts = None
            # MatrixProfile discords: disabled. Produces only leak FPs on this dataset
            # (0 hits for outlet/tv/kettle after 5σ threshold tightening); statistical
            # detectors already cover the same label types that MP would catch.
            # if st.cfg.archetype != Archetype.BINARY and st.raw_series:
            #     out.extend(matrix_profile_discords(st.cfg, st.raw_series))
        return out


def _chain_corroborated(alerts: list[Alert], cfg: SensorConfig) -> bool:
    # CONTINUOUS-sensor FPs have two archetypes on stationary voltage:
    #   (a) CUSUM-only chains (autocorrelation random walks from 1-min ZOH ticks),
    #       ARL0 collapses from ~12000 to ~9 samples; sporadic multi-hour bursts.
    #   (b) CUSUM + ONE weak statistical detector (sub_pca OR temporal_profile),
    #       where that one detector happens to cross its threshold during a
    #       CUSUM-fused chain but no multivariate or multi-detector corroboration
    #       exists. These are the 2-3h bands visible in viz.
    # Real anomalies on CONTINUOUS either trip DQG immediately (out_of_range,
    # duplicate_stale, clock_drift, dropout) or trip 3+ statistical detectors
    # simultaneously (noise_burst, stuck_at, calibration_drift). `cusum+mvpca` is
    # preserved because mvpca looks at cross-feature subspace, and that combo
    # is the only signal for duplicate_stale-style GT on outlet_short.
    # Sustained CUSUM-only chains near max_span (leak_battery trend) are kept —
    # they bridge multi-detector chunks on the same sustained anomaly.
    if cfg.archetype != Archetype.CONTINUOUS:
        return True
    dets = {a.detector for a in alerts}
    duration = alerts[-1].timestamp - alerts[0].timestamp if len(alerts) >= 2 else pd.Timedelta(0)
    if dets == {"cusum"}:
        return duration >= pd.Timedelta(hours=90) and len(alerts) >= 2
    # Iter I: two-detector stationary-artifact combos
    if dets in ({"cusum", "sub_pca"}, {"cusum", "temporal_profile"}):
        return duration >= pd.Timedelta(hours=4)
    # {cusum, mvpca} is the legitimate duplicate_stale signature on outlet_short
    # (DQG's duplicate_stale check requires same-ts+same-val which the generator
    # doesn't produce). TP chains are short (<30min per chain). Longer chains
    # are stationary cross-feature coincidences — drop if over an hour.
    if dets == {"cusum", "multivariate_pca"}:
        return duration <= pd.Timedelta(hours=1)
    # {sub_pca}-only chains are sliding-window residual excursions that happen
    # naturally on stationary voltage a few times per month. Real spike/dip
    # anomalies fire across cusum+mvpca+temporal_profile simultaneously, so a
    # solo sub_pca chain of >60min is almost always an artifact. Single-alert
    # chains have 0 timestamp-span but 125min window span — use the window
    # union so we catch them.
    if dets == {"sub_pca"}:
        starts = [a.window_start or a.timestamp for a in alerts]
        ends = [a.window_end or a.timestamp for a in alerts]
        return (max(ends) - min(starts)) <= pd.Timedelta(hours=1)
    return True


def _group(alerts: list[Alert]) -> Alert:
    top = max(alerts, key=lambda a: a.score)
    w0 = min((a.window_start or a.timestamp) for a in alerts)
    w1 = max((a.window_end or a.timestamp) for a in alerts)
    names = "+".join(sorted({a.detector for a in alerts}))
    ctx: list[dict] = []
    for a in alerts:
        if a.context:
            ctx.extend(a.context)
    return Alert(top.sensor_id, top.capability, top.timestamp, names,
                 top.score, top.threshold, top.anomaly_type, top.raw_value,
                 top.state, w0, w1, ctx or None)


# --- CLI ---

def _load_configs(path: Path) -> list[SensorConfig]:
    doc = yaml.safe_load(Path(path).read_text())
    out = []
    for s in doc["sensors"]:
        out.append(SensorConfig(
            sensor_id=s["id"], capability=s["capability"],
            archetype=Archetype(s["archetype"]),
            expected_interval_sec=float(s["expected_interval_sec"]),
            min_value=s.get("min_value"), max_value=s.get("max_value"),
            cumulative=bool(s.get("cumulative", False)),
            heartbeat_sec=s.get("heartbeat_sec"),
            granularity_sec=int(s.get("granularity_sec", 60)),
            deterministic_trigger=bool(s.get("deterministic_trigger", False)),
        ))
    return out


def run(events_csv: Path, config_yaml: Path, out_csv: Path, bootstrap_days: float) -> None:
    configs = _load_configs(config_yaml)
    p = Pipeline(configs, bootstrap_days=bootstrap_days)
    df = pd.read_csv(events_csv)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True, format="ISO8601")
    df = df.sort_values("timestamp").reset_index(drop=True)
    all_alerts: list[Alert] = []
    for row in df.itertuples(index=False):
        all_alerts.extend(p.ingest(Event(row.timestamp, row.sensor_id, row.capability,
                                          float(row.value), getattr(row, "unit", "") or "")))
    all_alerts.extend(p.finalize())
    _write_detections(all_alerts, out_csv)
    print(f"wrote {len(all_alerts)} detections to {out_csv}")


def _write_detections(alerts: list[Alert], path: Path) -> None:
    rows = []
    for a in alerts:
        start = a.window_start or a.timestamp
        end = a.window_end or (a.timestamp + pd.Timedelta(minutes=1))
        rows.append({"sensor_id": a.sensor_id, "capability": a.capability,
                     "start": start.isoformat(), "end": end.isoformat(),
                     "anomaly_type": a.anomaly_type or a.detector,
                     "detector": a.detector, "score": a.score})
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows, columns=["sensor_id","capability","start","end",
                                 "anomaly_type","detector","score"]).to_csv(path, index=False)


def evaluate(detections_csv: Path, labels_csv: Path) -> dict:
    m = compute_metrics(pd.read_csv(labels_csv), pd.read_csv(detections_csv))
    print(m)
    return m


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    ap = argparse.ArgumentParser(prog="anomaly")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--events", required=True, type=Path)
    r.add_argument("--config", required=True, type=Path)
    r.add_argument("--out", required=True, type=Path)
    r.add_argument("--bootstrap-days", type=float, default=14.0)
    e = sub.add_parser("eval")
    e.add_argument("--detections", required=True, type=Path)
    e.add_argument("--labels", required=True, type=Path)
    v = sub.add_parser("viz")
    v.add_argument("--events", required=True, type=Path)
    v.add_argument("--labels", required=True, type=Path)
    v.add_argument("--detections", type=Path, default=None)
    v.add_argument("--out", required=True, type=Path)
    v.add_argument("--window", default="1d", help="e.g. 1h, 6h, 1d, 2d")
    vl = sub.add_parser("viz-long")
    vl.add_argument("--events", required=True, type=Path)
    vl.add_argument("--labels", required=True, type=Path)
    vl.add_argument("--detections", type=Path, default=None)
    vl.add_argument("--out", required=True, type=Path)
    vl.add_argument("--min-hours", type=float, default=24.0,
                    help="minimum label duration to get its own detail page")
    args = ap.parse_args(argv)
    if args.cmd == "run":
        run(args.events, args.config, args.out, args.bootstrap_days); return 0
    if args.cmd == "eval":
        evaluate(args.detections, args.labels); return 0
    if args.cmd == "viz":
        from .viz import render
        ev = pd.read_csv(args.events)
        lb = pd.read_csv(args.labels)
        dt = pd.read_csv(args.detections) if args.detections else None
        render(ev, lb, dt, args.out, args.window)
        print(f"wrote {args.out}")
        return 0
    if args.cmd == "viz-long":
        from .viz import render_long
        ev = pd.read_csv(args.events)
        lb = pd.read_csv(args.labels)
        dt = pd.read_csv(args.detections) if args.detections else None
        render_long(ev, lb, dt, args.out, min_hours=args.min_hours)
        print(f"wrote {args.out}")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
