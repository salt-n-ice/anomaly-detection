"""Temporal framing helpers.

`temporal_framing` produces the calendar context block (weekday, hour,
weekend flag, time-of-day bucket). `_same_hour_weekday_stats` adds the
peer-z block when there's enough same-hour-of-weekday history.
"""
from __future__ import annotations
import pandas as pd

from ..core import Alert


_TIME_BUCKETS = [(0, 6, "night"), (6, 12, "morning"),
                 (12, 18, "afternoon"), (18, 24, "evening")]


def temporal_framing(alert: Alert) -> dict:
    ts = alert.timestamp
    bucket = next((name for lo, hi, name in _TIME_BUCKETS if lo <= ts.hour < hi),
                  "unknown")
    return {
        "timestamp": ts.isoformat(),
        "weekday": ts.day_name(),
        "hour": int(ts.hour),
        "is_weekend": bool(ts.dayofweek >= 5),
        "month": ts.month_name(),
        "time_of_day_bucket": bucket,
    }


def _same_hour_weekday_stats(alert: Alert, events: pd.DataFrame,
                             peak: float | None) -> dict:
    """Compare the alert's peak against same-hour-of-weekday history.

    A large |z| means the value is unusual for this sensor at this
    hour-of-day on this day-of-week — positive evidence for calendar-family
    anomalies (time_of_day, weekend_anomaly, temporal_pattern) even when the
    firing detectors are statistical rather than `temporal_profile`.
    Returns ``{}`` if there's too little peer history (< 4 points) or peak
    is not finite.
    """
    if peak is None or peak != peak:
        return {}
    ts = alert.timestamp
    w0 = alert.window_start or ts
    if "timestamp" in events.columns and events["timestamp"].dtype != "datetime64[ns, UTC]":
        events = events.copy()
        events["timestamp"] = pd.to_datetime(events["timestamp"], utc=True, format="ISO8601")
    sub = events[events["sensor_id"] == alert.sensor_id]
    peers = sub[(sub["timestamp"] < w0)
                & (sub["timestamp"].dt.hour == ts.hour)
                & (sub["timestamp"].dt.dayofweek == ts.dayofweek)]
    if len(peers) < 4:
        return {}
    peer_median = float(peers["value"].median())
    peer_std = float(peers["value"].std())
    if not (peer_std and peer_std > 0 and peer_std == peer_std):
        return {}
    return {
        "same_hour_weekday_median": peer_median,
        "same_hour_weekday_std": peer_std,
        "same_hour_weekday_n": int(len(peers)),
        "same_hour_weekday_z": float((peak - peer_median) / peer_std),
    }
