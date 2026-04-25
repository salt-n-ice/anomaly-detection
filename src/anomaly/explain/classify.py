"""Signal-driven classifier dispatch.

`classify_type(alert) -> str` returns the canonical anomaly type. The
dispatch is a flat 7-branch chain over `Signals.classes`; each branch
calls a small specialized helper. No fall-through except the explicit
final `"statistical_anomaly"`.

`classify(alert) -> ClassificationResult` returns a richer value with
type, confidence ("high" | "low"), and the sorted Signals.classes that
contributed to the dispatch. The bundle in `bundle.explain` consumes
the rich result; `classify_type` is kept as a thin string facade so
external callers (pipeline._write_detections) compile unchanged.

Acceptance: on the production scenarios (household_60d, household_120d,
leak_30d) the per-scenario `behavior_type_accuracy` (TP cases where any
overlapping chain's inferred_type ∈ gt_labels.anomaly_type) must be >=
the pre-rewrite baseline. iter 021's missing `{duty, peak}` rule lifts
hh60d and hh120d specifically.
"""
from __future__ import annotations
from dataclasses import dataclass
from ..core import Alert
from .signals import Signals


@dataclass(frozen=True)
class ClassificationResult:
    type: str
    confidence: str           # "high" | "low"
    signal_classes: list[str] # sorted list of Signals.classes that contributed


def classify(alert: Alert, mag: dict | None = None) -> ClassificationResult:
    """Rich classifier result. `bundle.explain` feeds this into the
    structured `classification` block; `classify_type` wraps it.

    The optional ``mag`` parameter (the magnitude block already computed
    by ``bundle.explain``) is forwarded to ``Signals.from_alert`` so that
    direction can be inferred from ``mag.delta`` sign in the CSV-replay
    path where ``alert.context`` is None.

    Confidence rules:
      - Pre-typed alerts (DQG, StateTransition) → "high"; signal_classes []
        because the detector signal didn't drive the dispatch.
      - "statistical_anomaly" fallthrough → "low" (the dispatcher couldn't
        identify a recognizable signal class).
      - All other dispatched types → "high".
      - Direction-None CONT branches that would have used direction
        (spike/dip) → downgrade to "low" so downstream consumers know the
        spike-vs-dip choice was arbitrary. The type stays whatever the
        helper returned (no point in re-running the dispatch); the
        confidence flag carries the caveat.
    """
    if alert.anomaly_type:
        return ClassificationResult(
            type=alert.anomaly_type,
            confidence="high",
            signal_classes=[],
        )
    s = Signals.from_alert(alert, mag=mag)
    type_ = _dispatch(s)
    confidence = "low" if type_ == "statistical_anomaly" else "high"
    if type_ in ("spike", "dip") and s.direction is None:
        # _classify_continuous defaults to "dip" when direction is None;
        # the caller has no real evidence for spike-vs-dip, so flag low.
        confidence = "low"
    signal_classes = sorted(s.classes)
    return ClassificationResult(
        type=type_, confidence=confidence, signal_classes=signal_classes,
    )


def classify_type(alert: Alert, mag: dict | None = None) -> str:
    return classify(alert, mag=mag).type


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
    return "level_shift"


def _classify_peak(s: Signals) -> str:
    """BURSTY per-event peak magnitude. Branches on rate co-presence.

    Peak chains are typically singleton 1-min emits (cooldown > fuser gap
    per LEARNINGS §2a), so chain duration_sec is not a useful discriminator.
    Default to `trend` (the WORKLOAD_FINGERPRINT prior winner among magnitude-
    only BURSTY labels: trend 6 + level_shift 16 + degradation_trajectory 2 vs
    spike 1). True spikes typically fire data_quality_gate (extreme_value),
    which is pre-typed and short-circuits before reaching this helper.
    """
    if "rate" in s.classes:
        return "trend"
    if s.duration_sec >= 7 * 86400:
        return "degradation_trajectory"
    return "trend"


def _classify_calendar(s: Signals) -> str:
    if s.is_weekend:
        return "weekend_anomaly"
    if s.is_off_hours:
        return "time_of_day"
    return "temporal_pattern"
