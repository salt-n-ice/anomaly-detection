"""Batch CSV → JSONL bundle writer.

`explain_detections_csv` reads the pipeline's events.csv + detections.csv,
materializes Alert objects via `_detections_to_alerts`, and writes one
bundle per detection to a JSONL file.
"""
from __future__ import annotations
import pandas as pd

from ..core import Alert
from .bundle import explain


def _detections_to_alerts(det_df: pd.DataFrame) -> list[Alert]:
    out: list[Alert] = []
    for r in det_df.itertuples(index=False):
        w0 = pd.Timestamp(r.start) if not isinstance(r.start, pd.Timestamp) else r.start
        w1 = pd.Timestamp(r.end)   if not isinstance(r.end,   pd.Timestamp) else r.end
        det_str = str(r.detector)
        atype_raw = str(getattr(r, "anomaly_type", "")) or None
        # pipeline._write_detections stores `anomaly_type or detector` in the
        # CSV's anomaly_type column; for statistical fused alerts the value is
        # the detector string. Strip that fallback so classify_type walks the
        # decision tree instead of short-circuiting on the pre-typed branch.
        anomaly_type = None if atype_raw == det_str else atype_raw
        # Threshold lands in the CSV via pipeline._write_detections (Phase B).
        # Old CSVs (pre-Phase-B research/explain runs) lack the column, so
        # fall back to 0.0 — getattr handles the missing-attr case for namedtuples.
        threshold = float(getattr(r, "threshold", 0.0)) if hasattr(r, "threshold") else 0.0
        out.append(Alert(
            sensor_id=str(r.sensor_id), capability=str(r.capability),
            timestamp=w0, detector=det_str,
            score=float(getattr(r, "score", 0.0)), threshold=threshold,
            anomaly_type=anomaly_type,
            raw_value=None, state=None, window_start=w0, window_end=w1,
            context=None,
        ))
    return out


def explain_detections_csv(events_csv, detections_csv, out_jsonl) -> int:
    """Batch explainer: CSV in, JSONL out. Returns the number of bundles written.

    Performance: events are pre-grouped by `sensor_id` once so the magnitude/
    temporal/synth helpers don't repeat the full-frame `events[events.sensor_id
    == ...]` filter on every detection. ~2x speedup on the full 7-scenario
    suite (~25 min → ~12 min); the inner timestamp-window filters are still
    the dominant cost on large scenarios.
    """
    import json as _json
    from pathlib import Path as _P
    events = pd.read_csv(events_csv)
    events["timestamp"] = pd.to_datetime(events["timestamp"], utc=True, format="ISO8601")
    # Pre-group: one filter per sensor up front, then index lookups per alert.
    events_by_sensor: dict[str, pd.DataFrame] = {
        sid: g.reset_index(drop=True) for sid, g in events.groupby("sensor_id")
    }
    empty_events = events.iloc[0:0]
    dets = pd.read_csv(detections_csv)
    alerts = _detections_to_alerts(dets)
    path = _P(out_jsonl); path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        n = 0
        for a in alerts:
            sensor_events = events_by_sensor.get(a.sensor_id, empty_events)
            f.write(_json.dumps(explain(a, sensor_events), default=str) + "\n")
            n += 1
    return n
