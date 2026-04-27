"""Signal extraction from Alert objects.

A `Signals` instance is the single input to the classifier dispatch in
`classify.py`. Coarsens a fired-detector set into a small vocabulary of
signal classes (duty / peak / rate / magnitude / calendar / dqg / state),
flattens calendar context, surfaces drift direction from any per-detector
context dict that carries one. The classifier reads only `Signals`, never
the raw Alert — keeps the dispatch table testable in isolation.
"""
from __future__ import annotations
from dataclasses import dataclass

from ..core import Alert


# Map detector name → coarse signal class. Unknown detectors are silently
# dropped from the classes set; the dispatch still works on the remaining
# known classes. A detector renamed (e.g., new duty-cycle window variant)
# only needs a row here — no rule edits required.
DETECTOR_CLASSES: dict[str, str] = {
    # DQG and StateTransition are pre-typed; classify_type short-circuits
    # to alert.anomaly_type before ever consulting Signals, but the table
    # entry is here for completeness/audit.
    "data_quality_gate":           "dqg",
    "state_transition":            "state",
    # Magnitude-domain (CONTINUOUS detectors)
    "cusum":                       "magnitude",
    "recent_shift":                "magnitude",
    "sub_pca":                     "magnitude",
    "multivariate_pca":            "magnitude",
    "bocpd":                       "magnitude",
    "state_conditional_shift":     "magnitude",
    # Duty-cycle (BURSTY time-in-state)
    "duty_cycle_shift_1h":         "duty",
    "duty_cycle_shift_3h":         "duty",
    "duty_cycle_shift_6h":         "duty",
    "duty_cycle_shift_12h":        "duty",
    # Per-event peak magnitude (BURSTY)
    "rolling_median_peak_shift":   "peak",
    "event_peak_shift":            "peak",
    # Event arrival rate (BURSTY)
    "event_rate_shift":            "rate",
    "hourly_event_rate_chi_sq":    "rate",
    # Calendar (hour/weekday bucketed)
    "temporal_profile":            "calendar",
}


# Capability → archetype heuristic. Pipeline Alerts don't carry archetype
# directly; the inference covers the cases in the current configs (water →
# BINARY, voltage/temperature → CONTINUOUS, power → BURSTY).
_ARCHETYPE_BY_CAPABILITY: dict[str, str] = {
    "water":       "BINARY",
    "voltage":     "CONTINUOUS",
    "temperature": "CONTINUOUS",
    "power":       "BURSTY",
}


_OFF_HOURS_RANGES = ((22, 24), (0, 7))  # 22:00-23:59 and 00:00-06:59


def _is_off_hours(hour: int) -> bool:
    return any(lo <= hour < hi for lo, hi in _OFF_HOURS_RANGES)


def _bucket_typical_from_context(context: list[dict] | None) -> str | None:
    """Walk per-detector context dicts looking for a bucket-typical marker.

    Emitted by DutyCycleShift; carries the calendar-position percentile
    rank of the firing window's (is_weekend, hour) bucket relative to all
    bootstrap buckets ("low" / "normal" / "high"). Used by the duty-branch
    classifier to disambiguate calendar-pattern anomalies from level
    shifts.
    """
    if not context:
        return None
    for ctx in context:
        bt = ctx.get("bucket_typical")
        if bt:
            return bt
    return None


def _direction_from_context(context: list[dict] | None,
                            mag: dict | None = None) -> str | None:
    """Walk per-detector context dicts looking for a direction signal.

    Sources, in order of preference:
      - cusum.direction          ("+" or "-")
      - recent_shift.direction   (set by the detector if available)
      - recent_shift.short_value vs baseline_value (compute "+" or "-")
      - rolling_median_peak_shift.direction ("high"/"low" → "+"/"-")
      - duty_cycle_shift_*.direction         ("high"/"low" → "+"/"-")
      - magnitude.delta sign (final fallback — covers the CSV-replay path
        where alert.context is None and no synthesized dict carries a
        direction marker for the firing detectors)
    """
    if context:
        for ctx in context:
            det = ctx.get("detector", "")
            d = ctx.get("direction")
            if d in ("+", "-"):
                return d
            if d == "high":
                return "+"
            if d == "low":
                return "-"
            if det == "recent_shift":
                sv = ctx.get("short_value")
                bv = ctx.get("baseline_value")
                if sv is not None and bv is not None:
                    return "+" if sv > bv else "-"
    if mag:
        delta = mag.get("delta")
        if delta is not None and delta == delta and delta != 0:
            return "+" if delta > 0 else "-"
    return None


@dataclass(frozen=True)
class Signals:
    detectors: frozenset[str]
    classes: frozenset[str]
    duration_sec: float
    capability: str
    archetype: str
    direction: str | None
    hour: int
    is_weekend: bool
    is_off_hours: bool
    pre_typed: str | None
    bucket_typical: str | None  # "low" / "normal" / "high" / None (no DCS context)

    @classmethod
    def from_alert(cls, alert: Alert, mag: dict | None = None) -> "Signals":
        detectors = frozenset(alert.detector.split("+"))
        classes = frozenset(
            DETECTOR_CLASSES[d] for d in detectors if d in DETECTOR_CLASSES
        )
        w0 = alert.window_start or alert.timestamp
        w1 = alert.window_end or alert.timestamp
        duration_sec = (w1 - w0).total_seconds()
        ts = alert.timestamp
        archetype = _ARCHETYPE_BY_CAPABILITY.get(alert.capability, "UNKNOWN")
        return cls(
            detectors=detectors,
            classes=classes,
            duration_sec=float(duration_sec),
            capability=alert.capability,
            archetype=archetype,
            direction=_direction_from_context(alert.context, mag),
            hour=int(ts.hour),
            is_weekend=bool(ts.dayofweek >= 5),
            is_off_hours=_is_off_hours(int(ts.hour)),
            pre_typed=alert.anomaly_type,
            bucket_typical=_bucket_typical_from_context(alert.context),
        )
