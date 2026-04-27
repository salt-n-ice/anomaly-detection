"""Canonical anomaly-type vocabulary and class mapping.

Mirrors the synthetic-generator/labels.py vocabulary so the inferred type
is directly comparable to ground truth. Kept here so the anomaly-detection
package stays decoupled from sensorgen.
"""
from __future__ import annotations


USER_BEHAVIOR_TYPES: frozenset[str] = frozenset({
    "spike", "dip", "level_shift", "trend", "degradation_trajectory",
    "frequency_change", "seasonality_loss", "time_of_day",
    "weekend_anomaly", "month_shift", "seasonal_mismatch",
    "water_leak_sustained",
})


SENSOR_FAULT_TYPES: frozenset[str] = frozenset({
    "out_of_range", "saturation", "noise_burst", "noise_floor_up",
    "stuck_at", "calibration_drift", "dropout", "duplicate_stale",
    "reporting_rate_change", "clock_drift", "batch_arrival",
})


def type_to_class(anomaly_type: str) -> str:
    """Map an anomaly_type string to its label class.

    Returns:
        "user_behavior" — occupancy/routine/appliance-shift semantics
        "sensor_fault"  — infrastructure signal-quality issues
        "unknown"       — detector-combo string or unmapped type
    """
    if anomaly_type in USER_BEHAVIOR_TYPES:
        return "user_behavior"
    if anomaly_type in SENSOR_FAULT_TYPES:
        return "sensor_fault"
    return "unknown"
