"""Per-anomaly-type semantics used by the NAB-style metric.

- `tp_window_sec`: time after GT onset where a correctly-typed detection
  counts as TP with sigmoid weight. Past this window but still inside
  the GT label, detections become FPs (detector should have adapted by
  now or signal should have returned to baseline).
- `is_permanent`: True for anomalies whose signal effect persists past
  the labeled `end` (`calibration_drift`, `level_shift` — see
  `../synthetic-generator/src/sensorgen/anomalies/drift.py`). Correctly-
  typed detections occurring outside the GT window but after the onset
  of a permanent anomaly on the same sensor are exempted from FP (they
  are a reaffirmation of an ongoing known condition, not a new event).
- `is_emergency`: True for anomalies where repeat firings are desired
  (household needs escalating alerts until resolved). `tp_window_sec`
  is effectively the full label duration — every fire is a TP.

Values derived from onset-sharpness reasoning in the session autopsy:
step onsets (spike, dip, out_of_range, level_shift, calibration_drift,
stuck_at, dropout, clock_drift) fire within 1-2 ticks; pattern onsets
(frequency_change, seasonality_loss, time_of_day, weekend_anomaly,
month_shift) need 1-2 cycles; slow drifts (trend, degradation_trajectory)
are physics-limited (time_to_threshold ≈ sqrt(2·λ·σ/(slope·Δt))·Δt,
~3h for typical voltage/power slopes → 12h cap with 4× margin).
"""
from __future__ import annotations
from dataclasses import dataclass

from anomaly.explain import SENSOR_FAULT_TYPES, USER_BEHAVIOR_TYPES


@dataclass(frozen=True)
class AnomalySemantics:
    tp_window_sec: int
    is_permanent: bool = False
    is_emergency: bool = False


_SEMANTICS: dict[str, AnomalySemantics] = {
    # Step onset — fire within 30 min
    "spike":               AnomalySemantics(tp_window_sec=30 * 60),
    "dip":                 AnomalySemantics(tp_window_sec=30 * 60),
    "out_of_range":        AnomalySemantics(tp_window_sec=30 * 60),
    "saturation":          AnomalySemantics(tp_window_sec=30 * 60),
    "stuck_at":            AnomalySemantics(tp_window_sec=60 * 60),
    "dropout":             AnomalySemantics(tp_window_sec=30 * 60),
    "duplicate_stale":     AnomalySemantics(tp_window_sec=30 * 60),
    "clock_drift":         AnomalySemantics(tp_window_sec=30 * 60),
    "batch_arrival":       AnomalySemantics(tp_window_sec=30 * 60),
    "reporting_rate_change": AnomalySemantics(tp_window_sec=30 * 60),
    "noise_burst":         AnomalySemantics(tp_window_sec=60 * 60),
    "noise_floor_up":      AnomalySemantics(tp_window_sec=60 * 60),
    "unusual_occupancy":   AnomalySemantics(tp_window_sec=60 * 60),
    # Pattern onset — 1-2 cycles
    "frequency_change":    AnomalySemantics(tp_window_sec=2 * 3600),
    "seasonality_loss":    AnomalySemantics(tp_window_sec=2 * 3600),
    "seasonal_mismatch":   AnomalySemantics(tp_window_sec=2 * 3600),
    "time_of_day":         AnomalySemantics(tp_window_sec=2 * 3600),
    "weekend_anomaly":     AnomalySemantics(tp_window_sec=2 * 3600),
    "month_shift":         AnomalySemantics(tp_window_sec=6 * 3600),
    # Slow drift — physics-limited
    "trend":               AnomalySemantics(tp_window_sec=12 * 3600),
    "degradation_trajectory": AnomalySemantics(tp_window_sec=48 * 3600),
    # Permanent — signal persists past label end; fire-once-at-onset;
    # past-label detections of same type exempted from FP.
    "calibration_drift":   AnomalySemantics(tp_window_sec=4 * 3600,
                                             is_permanent=True),
    "level_shift":         AnomalySemantics(tp_window_sec=4 * 3600,
                                             is_permanent=True),
    # Emergency — keep firing until resolved.
    "water_leak_sustained": AnomalySemantics(tp_window_sec=1,
                                              is_emergency=True),
}

# Default when a type isn't in the table (unrecognized / unknown types).
_DEFAULT = AnomalySemantics(tp_window_sec=2 * 3600)


def semantics_for(anomaly_type: str) -> AnomalySemantics:
    return _SEMANTICS.get(anomaly_type, _DEFAULT)


def is_user_behavior(anomaly_type: str) -> bool:
    return anomaly_type in USER_BEHAVIOR_TYPES


def is_sensor_fault(anomaly_type: str) -> bool:
    return anomaly_type in SENSOR_FAULT_TYPES
