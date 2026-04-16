from __future__ import annotations
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
                detectors.append(CUSUM(cfg, feats["cusum"]))
            if DETECTOR_ENABLED.get((cfg.archetype, "sub_pca"), False):
                detectors.append(SubPCA(cfg))
            if DETECTOR_ENABLED.get((cfg.archetype, "multivariate_pca"), False):
                detectors.append(MultivariatePCA(cfg, feats["mvpca"]))
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
        bypass = ("data_quality_gate", "state_transition")
        immediate = [a for a in fresh if a.detector in bypass]
        statistical = [a for a in fresh if a.detector not in bypass]
        out = list(immediate)
        gap = pd.Timedelta(minutes=60)       # merge alert chains from repeated CUSUM/PCA trips
        max_span = pd.Timedelta(hours=96)    # cap fused-group duration — 4 days balances FP reduction vs. letting adjacent labels claim distinct chunks
        for a in statistical:
            if st.pending_alerts:
                gap_exceeded = (st.pending_newest_ts is not None
                                and a.timestamp - st.pending_newest_ts > gap)
                span_exceeded = (a.timestamp - st.pending_alerts[0].timestamp) > max_span
                if gap_exceeded or span_exceeded:
                    out.append(_group(st.pending_alerts))
                    st.pending_alerts = []
                    st.pending_newest_ts = None
            st.pending_alerts.append(a)
            if st.pending_newest_ts is None or a.timestamp > st.pending_newest_ts:
                st.pending_newest_ts = a.timestamp
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
            if feat.get("trigger"):
                alerts.append(Alert(st.cfg.sensor_id, st.cfg.capability, tick,
                                    "state_transition", 1.0, 1.0,
                                    "water_leak_sustained", 1.0, feat.get("state"),
                                    tick, tick))
            for d in st.detectors:
                alerts.extend(d.update(tick, enriched))
        self._maybe_fit(st, ev.timestamp)
        return self._fuse(st, alerts)

    def finalize(self) -> list[Alert]:
        out = []
        for st in self._states.values():
            if st.pending_alerts:
                out.append(_group(st.pending_alerts))
                st.pending_alerts.clear()
                st.pending_newest_ts = None
            if st.cfg.archetype != Archetype.BINARY and st.raw_series:
                out.extend(matrix_profile_discords(st.cfg, st.raw_series))
        return out


def _group(alerts: list[Alert]) -> Alert:
    top = max(alerts, key=lambda a: a.score)
    w0 = min((a.window_start or a.timestamp) for a in alerts)
    w1 = max((a.window_end or a.timestamp) for a in alerts)
    names = "+".join(sorted({a.detector for a in alerts}))
    return Alert(top.sensor_id, top.capability, top.timestamp, names,
                 top.score, top.threshold, top.anomaly_type, top.raw_value,
                 top.state, w0, w1)


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
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
