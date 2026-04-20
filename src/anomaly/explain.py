"""Deterministic explainer layer.

Turns a detection-pipeline Alert into a structured bundle an LLM can consume.
No LLM, no persistence, no cross-sensor context (Stage 2). The pipeline keeps
its real-time contract; this module runs afterwards on whatever alerts are
emitted (streaming or batch).
"""
from __future__ import annotations
import pandas as pd
from .core import Alert


def _find_ctx(alert: Alert, detector: str) -> dict | None:
    """Return the first context dict for ``detector`` (or None)."""
    if not alert.context:
        return None
    for ctx in alert.context:
        if ctx.get("detector") == detector:
            return ctx
    return None


def classify_type(alert: Alert) -> str:
    """Decision tree: detector set x duration x drift direction -> canonical type.

    Reuses the generator's label vocabulary so the type is directly comparable
    to ground truth. Unknown combinations fall back to ``"statistical_anomaly"``.
    """
    # 1. DQG / state_transition are pre-typed -- pass through.
    if alert.anomaly_type:
        return alert.anomaly_type

    dets = set(alert.detector.split("+"))
    dur_sec = ((alert.window_end or alert.timestamp)
               - (alert.window_start or alert.timestamp)).total_seconds()
    cusum = _find_ctx(alert, "cusum")
    drift_dir = cusum.get("direction") if cusum else None

    # 2. Short + many detectors agreeing = spike/dip.
    if dur_sec < 10 * 60 and len(dets) >= 3:
        return "spike" if drift_dir == "+" else "dip"

    # 3. CUSUM-led long chain -> drift family, bucketed by duration.
    if "cusum" in dets and dur_sec > 60 * 60:
        if dur_sec > 7 * 86400:
            return "month_shift"
        if dur_sec > 86400:
            return "calibration_drift"
        # 1h-24h: distinguish level_shift (shape change, PCA fires) from drift.
        if "sub_pca" in dets or "multivariate_pca" in dets:
            return "level_shift"
        return "trend"

    # 4. Temporal-profile-only -> calendar pattern anomaly.
    if dets == {"temporal_profile"}:
        ts = alert.timestamp
        if ts.dayofweek >= 5:
            return "weekend_anomaly"
        if 2 <= ts.hour <= 6 or 22 <= ts.hour <= 23:
            return "time_of_day"
        return "temporal_pattern"

    # 5. SubPCA-led without CUSUM -> shape anomaly (frequency_change, seasonality_loss).
    if "sub_pca" in dets and "cusum" not in dets:
        return "frequency_change" if dur_sec >= 3600 else "shape_anomaly"

    return "statistical_anomaly"
