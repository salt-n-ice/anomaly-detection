from __future__ import annotations
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
import argparse, sys
import pandas as pd
import yaml
from .core import Event, Alert, Archetype, SensorConfig
from .adapter import make_adapter, Adapter
from .features import FeatureEngineer
from .fusion import DefaultAlertFuser
from .profiles import profile_for
from .batch import matrix_profile_discords
from .metrics import compute_metrics
from .explain import classify_type, type_to_class


_ADAPT_BUFFER_TICKS_DEFAULT = 96 * 60  # 96h buffer for CONTINUOUS — a longer buffer
# on CONT (mains_voltage month_shift) absorbs mid-anomaly regime and delays subsequent
# label onset detection (tested at 120h global: +4683s hh120d nondqg_lat_p95, blows
# +600s floor). Per-archetype gate keeps CONT safe.
_ADAPT_BUFFER_TICKS_BY_ARCHETYPE = {
    Archetype.CONTINUOUS: 96 * 60,   # keep latency safety for long sustained CONT anomalies
    Archetype.BURSTY:     144 * 60,  # iter 037: sweet spot for outlet wind-down absorption
    Archetype.BINARY:     144 * 60,  # same; BINARY short-label latency is state_transition's job
}


@dataclass
class _SensorState:
    cfg: SensorConfig
    adapter: Adapter
    engineer: FeatureEngineer
    short_event: list                   # pre-adapter EventDetectors (DQG)
    short_tick: list                    # post-adapter immediate triggers (StateTransition or [])
    medium: list                        # sliding-window Detectors (CUSUM, SubPCA, MvPCA)
    long_tick: list                     # calendar Detectors (TemporalProfile)
    fuser: DefaultAlertFuser
    bootstrap_raw: list = field(default_factory=list)   # (tick, adapter_features)
    bootstrap_rows: list = field(default_factory=list)  # (tick, enriched)
    raw_series: list = field(default_factory=list)
    start_ts: pd.Timestamp | None = None
    fit_done: bool = False
    recent_rows: deque = field(default_factory=deque)  # size set in Pipeline.__init__ per-archetype
    consecutive_max_span: int = 0        # cross-chain streak counter for G1 adapt

    def tick_detectors(self) -> list:
        """All post-adapter detectors in emit order (short_tick -> medium -> long_tick)."""
        return self.short_tick + self.medium + self.long_tick


class Pipeline:
    def __init__(self, configs: list[SensorConfig], bootstrap_days: float = 14.0):
        self.bootstrap_days = bootstrap_days
        self._states: dict[tuple[str, str], _SensorState] = {}
        for cfg in configs:
            p = profile_for(cfg)
            buffer_ticks = _ADAPT_BUFFER_TICKS_BY_ARCHETYPE.get(
                cfg.archetype, _ADAPT_BUFFER_TICKS_DEFAULT)
            self._states[cfg.key] = _SensorState(
                cfg=cfg,
                adapter=make_adapter(cfg),
                engineer=FeatureEngineer(cfg),
                short_event=[f(cfg) for f in p.short_event],
                short_tick=[f(cfg) for f in p.short_tick],
                medium=[f(cfg) for f in p.medium],
                long_tick=[f(cfg) for f in p.long_tick],
                fuser=p.long_fuser(cfg),
                recent_rows=deque(maxlen=buffer_ticks),
            )

    def is_live(self, key) -> bool:
        st = self._states.get(key)
        return bool(st and st.fit_done and any(d.live for d in st.tick_detectors()))

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
        for d in st.tick_detectors():
            d.fit(st.bootstrap_rows)
        st.fit_done = True

    def ingest(self, ev: Event) -> list[Alert]:
        st = self._states.get((ev.sensor_id, ev.capability))
        if st is None: return []
        if st.start_ts is None: st.start_ts = ev.timestamp
        alerts: list[Alert] = []
        # SHORT band — pre-adapter event checks (always, independent of bootstrap).
        for d in st.short_event:
            alerts.extend(d.check(ev))
        # Adapter band — normalize to uniform ticks.
        st.adapter.ingest(ev)
        for tick, feat in st.adapter.emit_ready(ev.timestamp):
            st.raw_series.append((tick, feat.get("value", float("nan"))))
            if not st.fit_done:
                st.bootstrap_raw.append((tick, dict(feat)))
                continue
            enriched = st.engineer.enrich(tick, feat)
            st.recent_rows.append((tick, enriched))
            # SHORT tick -> MEDIUM -> LONG tick (emit order preserved).
            for d in st.tick_detectors():
                alerts.extend(d.update(tick, enriched))
        self._maybe_fit(st, ev.timestamp)
        # LONG fuser — chain-level aggregation + corroboration.
        emitted = st.fuser.ingest(alerts)
        # Coordinated adaptation on consecutive max_span flushes. A single
        # max_span chain (~96h) is ambiguous — could be the legit start of a
        # multi-day anomaly OR a wind-down tail. Three consecutive max_span
        # flushes (~12d of continuous firing) is a strong wind-down signal:
        # by 12d, any active anomaly that triggered chain 1 has had its
        # onset captured (incident_recall preserved), the 1st post-onset
        # chain has had time to fire without adaptation (time_recall
        # preserved on sustained anomalies), and continued firing past
        # that is the post-shift baseline being treated as new normal.
        # Adapting once at the third flush absorbs the recent rolling
        # window into each detector's mu/centroid; subsequent ticks see
        # small deviations and the chain stops re-forming. Counter resets
        # on any non-max-span emit (chain ended naturally → not wind-down)
        # and after each adapt (require fresh streak before next adapt).
        # K=3 chosen over K=2 (iter 028) to preserve more of hh60d
        # bedroom_motion month_shift tail coverage and reduce hh120d
        # voltage month_shift latency pressure.
        span_threshold = 0.9 * st.fuser.max_span
        for em in emitted:
            if em.window_start is None or em.window_end is None:
                continue
            if (em.window_end - em.window_start) >= span_threshold:
                st.consecutive_max_span += 1
            else:
                st.consecutive_max_span = 0
            if st.consecutive_max_span >= 3:
                rows = list(st.recent_rows)
                for d in st.medium + st.long_tick:
                    if hasattr(d, "adapt_to_recent"):
                        d.adapt_to_recent(rows)
                st.consecutive_max_span = 0
        return emitted

    def finalize(self) -> list[Alert]:
        out = []
        for st in self._states.values():
            out.extend(st.fuser.finalize())
            # MatrixProfile discords: disabled. Produces only leak FPs on this dataset
            # (0 hits for outlet/tv/kettle after 5σ threshold tightening); statistical
            # detectors already cover the same label types that MP would catch.
            # if st.cfg.archetype != Archetype.BINARY and st.raw_series:
            #     out.extend(matrix_profile_discords(st.cfg, st.raw_series))
        return out


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
        # first_fire_ts: earliest component tick in a fused chain; immediate
        # (unfused) alerts fall back to a.timestamp. Latency/onset metrics
        # read this column instead of `start` so sliding-window and cross-
        # chain artifacts don't back-date the reported alert fire time.
        first_fire = a.first_fire_ts or a.timestamp
        # inferred_type: explainer-derived canonical type (pre-typed alerts
        # from DQG / state_transition pass through; detector-combo chains
        # get a best-guess label via classify_type). inferred_class maps
        # the type to {user_behavior, sensor_fault, unknown} so the eval
        # harness can prevent a DQG `dropout` claim from being credited
        # as TP against a `water_leak_sustained` GT label on the same
        # sensor (and vice versa).
        inferred_type = classify_type(a)
        inferred_class = type_to_class(inferred_type)
        rows.append({"sensor_id": a.sensor_id, "capability": a.capability,
                     "start": start.isoformat(), "end": end.isoformat(),
                     "first_fire_ts": first_fire.isoformat(),
                     "anomaly_type": a.anomaly_type or a.detector,
                     "inferred_type": inferred_type,
                     "inferred_class": inferred_class,
                     "detector": a.detector,
                     "threshold": float(a.threshold),
                     "score": a.score})
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows, columns=["sensor_id","capability","start","end",
                                 "first_fire_ts","anomaly_type",
                                 "inferred_type","inferred_class",
                                 "detector","threshold","score"]).to_csv(path, index=False)


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
    v.add_argument("--detections", required=True, type=Path)
    v.add_argument("--out", required=True, type=Path)
    v.add_argument("--sensor-names", type=Path, default=None,
                   help="JSON file mapping sensor_id to friendly display name")
    v.add_argument("--max-showcases", type=int, default=8,
                   help="cap on the number of curated showcase pages")
    v.add_argument("--exclude-sensors", default="",
                   help="comma-separated sensor_ids to drop from the report")
    v.add_argument("--title", default=None,
                   help="document title; default auto-derived from events.csv path")
    vl = sub.add_parser("viz-long")
    vl.add_argument("--events", required=True, type=Path)
    vl.add_argument("--labels", required=True, type=Path)
    vl.add_argument("--detections", type=Path, default=None)
    vl.add_argument("--out", required=True, type=Path)
    vl.add_argument("--min-hours", type=float, default=24.0,
                    help="minimum label duration to get its own detail page")
    ex = sub.add_parser("explain")
    ex.add_argument("--events", required=True, type=Path)
    ex.add_argument("--detections", required=True, type=Path)
    ex.add_argument("--out", required=True, type=Path,
                    help="JSONL path - one bundle per detection")
    args = ap.parse_args(argv)
    if args.cmd == "run":
        run(args.events, args.config, args.out, args.bootstrap_days); return 0
    if args.cmd == "eval":
        evaluate(args.detections, args.labels); return 0
    if args.cmd == "viz":
        import json as _json
        from .viz import render
        ev = pd.read_csv(args.events)
        lb = pd.read_csv(args.labels)
        dt = pd.read_csv(args.detections)
        sn = _json.loads(args.sensor_names.read_text()) if args.sensor_names else {}
        excluded = frozenset(s.strip() for s in args.exclude_sensors.split(",") if s.strip())
        render(ev, lb, dt, args.out,
               sensor_names=sn,
               max_showcases=args.max_showcases,
               excluded_sensors=excluded,
               title=args.title)
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
    if args.cmd == "explain":
        from .explain import explain_detections_csv
        n = explain_detections_csv(args.events, args.detections, args.out)
        print(f"wrote {n} bundles to {args.out}")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
