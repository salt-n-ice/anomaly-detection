"""Top-level bundle composer.

`explain` produces the structured bundle dict consumed by `prompt.build_prompt`
and the batch JSONL writer in `csv.explain_detections_csv`.
"""
from __future__ import annotations
import pandas as pd

from ..core import Alert
from .classify import classify_type
from .magnitude import extract_magnitude, _synth_detector_context
from .temporal import temporal_framing, _same_hour_weekday_stats


def explain(alert: Alert, events: pd.DataFrame) -> dict:
    """Top-level composer. Returns a structured bundle ready for an LLM prompt."""
    w0 = alert.window_start or alert.timestamp
    w1 = alert.window_end or alert.timestamp
    mag = extract_magnitude(alert, events)
    ctx = list(alert.context) if alert.context else _synth_detector_context(alert, events, mag)
    temporal = temporal_framing(alert)
    temporal.update(_same_hour_weekday_stats(alert, events, mag.get("peak")))
    return {
        "alert_id": f"{alert.sensor_id}|{alert.capability}|{w0.isoformat()}",
        "sensor": alert.sensor_id,
        "capability": alert.capability,
        "window": {"start": w0.isoformat(), "end": w1.isoformat(),
                   "duration_sec": float((w1 - w0).total_seconds())},
        "inferred_type": classify_type(alert),
        "magnitude": mag,
        "temporal": temporal,
        "detectors": sorted(alert.detector.split("+")),
        "detector_context": ctx,
        "score": float(alert.score),
        "threshold": float(alert.threshold),
    }
