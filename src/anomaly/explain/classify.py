"""Signal-driven classifier dispatch.

`classify_type(alert) -> str` returns the canonical anomaly type. The
dispatch is a flat 7-branch chain over `Signals.classes`; each branch
calls a small specialized helper. No fall-through except the explicit
final `"statistical_anomaly"`.

Acceptance: on the production scenarios (household_60d, household_120d,
leak_30d) the per-scenario `behavior_type_accuracy` (TP cases where any
overlapping chain's inferred_type ∈ gt_labels.anomaly_type) must be >=
the pre-rewrite baseline. iter 021's missing `{duty, peak}` rule lifts
hh60d and hh120d specifically.
"""
from __future__ import annotations
from ..core import Alert
from .signals import Signals


def classify_type(alert: Alert) -> str:
    if alert.anomaly_type:
        # DQG and StateTransition pre-type their alerts; pass through.
        return alert.anomaly_type
    return _dispatch(Signals.from_alert(alert))


def _dispatch(s: Signals) -> str:
    classes = s.classes
    if classes == frozenset({"state"}):
        return _classify_state(s)
    if classes == frozenset({"magnitude"}):
        return _classify_continuous(s)
    if "duty" in classes:
        return _classify_duty(s)
    if "peak" in classes:
        return _classify_peak(s)
    if "rate" in classes:
        return "frequency_change"
    if "calendar" in classes:
        return _classify_calendar(s)
    return "statistical_anomaly"


def _classify_state(s: Signals) -> str:
    if s.capability == "water":
        return "water_leak_sustained"
    if s.capability == "motion":
        return "unusual_occupancy"
    return "statistical_anomaly"


def _classify_continuous(s: Signals) -> str:
    """CONT magnitude detectors: RecentShift / CUSUM / BOCPD / SubPCA / MvPCA.

    Capability-specific rules dominate. Defaults handle generic CONT.
    """
    if s.capability == "voltage":
        if s.duration_sec >= 12 * 3600:
            return "month_shift"
        if s.duration_sec >= 3600:
            return "level_shift"
        return "spike" if s.direction == "+" else "dip"
    if s.capability == "temperature":
        if s.duration_sec < 2 * 3600 or s.direction == "-":
            return "dip"
        return "calibration_drift"
    # Generic CONT (power, etc.)
    if s.duration_sec >= 7 * 86400:
        return "month_shift"
    if s.duration_sec >= 3600:
        return "level_shift"
    return "spike" if s.direction == "+" else "dip"


def _classify_duty(s: Signals) -> str:
    """BURSTY duty-cycle. Branches on peak/rate co-presence + calendar."""
    has_peak = "peak" in s.classes
    has_rate = "rate" in s.classes
    if has_peak and has_rate:
        return "level_shift"
    if has_peak:
        # Combined duty + peak: classic level_shift signature. But a
        # short weekend hit is more plausibly a weekend behavior change.
        if s.is_weekend and s.duration_sec < 3 * 86400:
            return "weekend_anomaly"
        return "level_shift"
    if has_rate:
        return "frequency_change"
    # Duty alone: either calendar-type or rate-class.
    if s.is_weekend:
        return "weekend_anomaly"
    if s.is_off_hours:
        return "time_of_day"
    if s.duration_sec >= 7 * 86400:
        return "degradation_trajectory"
    return "frequency_change"


def _classify_peak(s: Signals) -> str:
    """BURSTY per-event peak magnitude. Branches on rate co-presence."""
    if "rate" in s.classes:
        return "trend"
    if s.duration_sec < 600:
        return "spike"
    if s.duration_sec >= 7 * 86400:
        return "degradation_trajectory"
    return "trend"


def _classify_calendar(s: Signals) -> str:
    if s.is_weekend:
        return "weekend_anomaly"
    if s.is_off_hours:
        return "time_of_day"
    return "temporal_pattern"
