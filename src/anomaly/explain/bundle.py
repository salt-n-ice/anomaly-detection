"""Top-level bundle composer.

`explain` produces the structured bundle dict consumed by `prompt.build_prompt`
and the batch JSONL writer in `csv.explain_detections_csv`.
"""
from __future__ import annotations
import pandas as pd

from ..core import Alert
from .signals import Signals
from .classify import classify
from .types import type_to_class
from .magnitude import extract_magnitude, _synth_detector_context
from .temporal import temporal_framing, _same_hour_weekday_stats


def _ensure_utc_timestamps(events: pd.DataFrame) -> pd.DataFrame:
    """Return ``events`` with a UTC-typed timestamp column.

    The batch CSV path lands here with object-dtype strings; per-event
    helpers (`extract_magnitude`, `_synth_detector_context`,
    `_same_hour_weekday_stats`) all assume already-UTC timestamps and
    skip the parse. Lifting the parse to the top of `explain` cuts
    triple parsing per alert in the batch path.
    """
    if "timestamp" not in events.columns:
        return events
    if events["timestamp"].dtype == "datetime64[ns, UTC]":
        return events
    events = events.copy()
    events["timestamp"] = pd.to_datetime(events["timestamp"], utc=True,
                                         format="ISO8601")
    return events


def explain(alert: Alert, events: pd.DataFrame) -> dict:
    """Top-level composer. Returns a structured bundle ready for an LLM prompt."""
    w0 = alert.window_start or alert.timestamp
    w1 = alert.window_end or alert.timestamp
    events = _ensure_utc_timestamps(events)
    mag = extract_magnitude(alert, events)
    ctx = list(alert.context) if alert.context else _synth_detector_context(alert, events, mag)
    s = Signals.from_alert(alert)
    cls = classify(alert)
    type_class = type_to_class(cls.type)
    presentation = "user_visible" if type_class == "user_behavior" else "infrastructure"
    if type_class == "unknown":
        presentation = "user_visible"  # err on the side of showing
    temporal = temporal_framing(alert)
    temporal.update(_same_hour_weekday_stats(alert, events, mag.get("peak")))
    return {
        "alert_id": f"{alert.sensor_id}|{alert.capability}|{w0.isoformat()}",
        "sensor": alert.sensor_id,
        "capability": alert.capability,
        "archetype": s.archetype,
        "window": {"start": w0.isoformat(), "end": w1.isoformat(),
                   "duration_sec": float((w1 - w0).total_seconds())},
        "classification": {
            "type":           cls.type,
            "class":          type_class,
            "presentation":   presentation,
            "confidence":     cls.confidence,
            "signal_classes": cls.signal_classes,
        },
        "magnitude": mag,
        "temporal": temporal,
        "detectors": sorted(alert.detector.split("+")),
        "detector_context": ctx,
        "score": float(alert.score),
    }
