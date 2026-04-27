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


_DQG_SPIKE_OVERRIDE_CAPS = frozenset({"power", "voltage", "temperature"})

# H6.2 (iter 003) and H7v2 (iter 004) thresholds for DQG out_of_range
# overrides on power capability. The shwz axis splits "sustained" (large
# z, level_shift) from "transient/cyclic" (small z, frequency_change);
# the delta_pct floor on frequency_change rules out null-magnitude trips.
_DQG_LEVEL_SHIFT_SHWZ_THRESHOLD = 3.0
_DQG_FREQ_CHANGE_DELTA_PCT_THRESHOLD = 3.0

# Iter 006: a DQG dropout co-firing with one of these duty-cycle detectors
# is corroborating evidence that the appliance's time-in-state shifted
# before readings stopped — read as behavioral level_shift, not sensor
# fault.
_DUTY_CYCLE_DETECTORS = frozenset({
    "duty_cycle_shift_1h", "duty_cycle_shift_3h",
    "duty_cycle_shift_6h", "duty_cycle_shift_12h",
})

# Iter 007: when DQG dropout fires alone (no duty co-fire), peer-baseline
# or magnitude evidence can still corroborate behavioral level_shift.
# |shwz| floor is 2.5 — lower than iter-003's 3.0 for OOR because dropout
# chains have peak/baseline at the off-marker (e.g., -1400 on a kettle
# in the synth dataset) and the shwz signal is less noisy than for OOR
# value excursions. |delta_pct| floor is 100 — same as iter-002 spike,
# captures cases where the post-recovery reading is clearly off without
# peer baseline evidence.
_DQG_DROPOUT_NO_DUTY_SHWZ_THRESHOLD = 2.5
_DQG_DROPOUT_NO_DUTY_DELTA_PCT_THRESHOLD = 100.0
_DQG_DROPOUT_DUR_FLOOR_S = 3600.0


def _maybe_dqg_oor_override(alert: Alert, mag: dict | None,
                            temporal: dict | None) -> str | None:
    """Re-classify a DQG ``out_of_range`` pre-typed alert on a power-
    capability sensor based on the bundle's same-hour-of-week z-score.

    DQG out_of_range is a static-threshold trip; on power (wide
    legitimate dynamic range), the pre-typed `sensor_fault` label is
    rarely correct. We can split the override into two regimes using
    `temporal.same_hour_weekday_z`:

      - ``|shwz| >= 3``  →  ``level_shift``. The value is sustainedly off
        the same-hour-of-week median: appliance unplugged or left on
        permanently. Direction not encoded — `value_shift` super covers
        both signs.
      - ``|shwz| < 3`` AND ``|mag.delta_pct| >= 3`` AND ``delta != 0``
        →  ``frequency_change``. The value is genuinely different from
        the immediate pre-window baseline (cycle in or out of phase) but
        not strongly off historical norm at this hour-of-week — the
        appliance is firing/idling more or less often than usual.

    Below both thresholds the OOR is a small noise-floor trip with no
    behavioral signal; fall through to the pre-typed sensor_fault label.

    Returns the inferred type, or ``None`` to fall through.
    """
    if alert.anomaly_type != "out_of_range":
        return None
    if alert.capability != "power":
        return None
    if "data_quality_gate" not in alert.detector.split("+"):
        return None
    if not temporal:
        return None
    shwz = temporal.get("same_hour_weekday_z")
    if shwz is None or shwz != shwz:
        return None
    if abs(shwz) >= _DQG_LEVEL_SHIFT_SHWZ_THRESHOLD:
        return "level_shift"
    if not mag:
        return None
    delta = mag.get("delta")
    dp = mag.get("delta_pct")
    if delta is None or delta != delta or delta == 0:
        return None
    if dp is None or dp != dp or abs(dp) < _DQG_FREQ_CHANGE_DELTA_PCT_THRESHOLD:
        return None
    return "frequency_change"


def _maybe_dqg_dropout_override(alert: Alert,
                                mag: dict | None = None,
                                temporal: dict | None = None
                                ) -> str | None:
    """Re-classify a DQG ``dropout`` pre-typed alert on a power-capability
    sensor as ``level_shift`` when sustained AND corroborated by any of
    three signals.

    A real sensor dropout (hardware failure, comm loss) on a power
    appliance is typically short-lived and lacks corroboration from
    behavior-driven detectors or peer-baseline z-scores. A *sustained*
    dropout (at least an hour) accompanied by ANY of the following is
    much more likely a behavioral level_shift (kettle unplugged,
    appliance left off):

      - **Duty-cycle co-fire** (iter 006). ``duty_cycle_shift_*h`` fires
        on the binarized time-in-state; a real dropout would register
        as ``off``, not as a *shift*. Co-fire indicates the appliance's
        time-in-state pattern measurably shifted before the reading
        stream stopped.
      - **|same_hour_weekday_z| >= 2.5** (iter 007). Mirrors iter-003's
        OOR shwz threshold; lowered slightly because dropout chains
        sit at the off-marker (constant value during the window),
        making the peer-baseline signal less noisy than for OOR value
        excursions.
      - **|delta_pct| >= 100** (iter 007). Captures cases where the
        post-recovery reading is clearly off baseline without peer
        evidence. Same threshold as iter-002 spike.

    The 1-hour duration floor blocks short comm hiccups whose timing
    coincidentally aligned with a duty boundary or peer-baseline noise.

    Confidence is "low" because the dropout itself carries no in-window
    magnitude evidence (sparse / no readings); we lean on the
    corroborator. signal_classes ``["dqg", "duty"]`` is shared across
    all three branches — the duty signal class covers both the duty
    co-fire path and the time-in-state interpretation that the other
    two paths land in.

    Returns the inferred type, or ``None`` to fall through to the normal
    pre-typed short-circuit (``dropout`` / sensor_fault).
    """
    if alert.anomaly_type != "dropout":
        return None
    if alert.capability != "power":
        return None
    detectors = set(alert.detector.split("+"))
    if "data_quality_gate" not in detectors:
        return None
    w0 = alert.window_start or alert.timestamp
    w1 = alert.window_end or alert.timestamp
    if (w1 - w0).total_seconds() < _DQG_DROPOUT_DUR_FLOOR_S:
        return None
    if detectors & _DUTY_CYCLE_DETECTORS:
        return "level_shift"
    if temporal:
        shwz = temporal.get("same_hour_weekday_z")
        if (shwz is not None and shwz == shwz
                and abs(shwz) >= _DQG_DROPOUT_NO_DUTY_SHWZ_THRESHOLD):
            return "level_shift"
    if mag:
        dp = mag.get("delta_pct")
        if (dp is not None and dp == dp
                and abs(dp) >= _DQG_DROPOUT_NO_DUTY_DELTA_PCT_THRESHOLD):
            return "level_shift"
    return None


def _maybe_dqg_oor_sustained_override(alert: Alert) -> str | None:
    """Re-classify a DQG ``out_of_range`` pre-typed alert as ``level_shift``
    when the pipeline flags it as sustained — i.e., multiple OOR fires on
    the same sensor within a 6h sliding window.

    A real OOR sensor fault is typically transient (calibration glitch,
    momentary overload, single noise burst). A sustained OOR pattern
    across hours is much more likely a behavioral level shift — synth-gen's
    ``level_shift offset=-N`` on power sensors drives the off-state below
    the configured min, producing a stream of OOR fires every cooldown.
    The pipeline path pre-computes the sustained flag from the alert
    sequence (DQG fires bypass the fuser, so this can't be derived
    chain-side); the bundle explain path falls back to shwz-based override.

    Returns the inferred type, or ``None`` to fall through to the normal
    pre-typed short-circuit.
    """
    if alert.anomaly_type != "out_of_range":
        return None
    if alert.capability != "power":
        return None
    if "data_quality_gate" not in alert.detector.split("+"):
        return None
    return "level_shift"


def _maybe_dqg_spike_override(alert: Alert, mag: dict | None,
                              temporal: dict | None) -> str | None:
    """Re-classify a DQG ``extreme_value`` pre-typed alert as ``spike`` /
    ``dip`` when the bundle context unambiguously indicates a transient
    user-behavior excursion rather than a sensor max-rated trip.

    Triggered only when ALL of:
      - DQG ``extreme_value`` pre-type
      - Capability is appliance-style (power / voltage / temperature) —
        these have wide legitimate dynamic range, so a single threshold
        crossing is more often behavior than fault.
      - ``mag.delta`` is non-zero (rules out null-magnitude trips)
      - ``|mag.delta_pct| >= 100`` (excursion is at least 1× baseline —
        a transient, not a baseline drift)
      - ``|temporal.same_hour_weekday_z| >= 6`` (value is >=6σ off the
        same-hour-of-week historical median; sensor faults that recur
        do not get this strong against their own history)

    Returns the inferred type, or ``None`` to fall through to the normal
    pre-typed short-circuit. The 6σ threshold is intentionally
    conservative — picks up textbook spikes (delta_pct in hundreds of
    percent on appliances), avoids re-classifying merely-large excursions
    that could be early-stage faults.
    """
    if alert.anomaly_type != "extreme_value":
        return None
    if alert.capability not in _DQG_SPIKE_OVERRIDE_CAPS:
        return None
    if "data_quality_gate" not in alert.detector.split("+"):
        return None
    if not mag or not temporal:
        return None
    delta = mag.get("delta")
    dp = mag.get("delta_pct")
    shwz = temporal.get("same_hour_weekday_z")
    if delta is None or delta != delta or delta == 0:
        return None
    if dp is None or dp != dp or abs(dp) < 100:
        return None
    if shwz is None or shwz != shwz or abs(shwz) < 6:
        return None
    return "spike" if delta > 0 else "dip"


def classify(alert: Alert, mag: dict | None = None,
             temporal: dict | None = None,
             sustained_oor: bool = False,
             sustained_dcs: bool = False) -> ClassificationResult:
    """Rich classifier result. `bundle.explain` feeds this into the
    structured `classification` block; `classify_type` wraps it.

    The optional ``mag`` parameter (the magnitude block already computed
    by ``bundle.explain``) is forwarded to ``Signals.from_alert`` so that
    direction can be inferred from ``mag.delta`` sign in the CSV-replay
    path where ``alert.context`` is None.

    The optional ``temporal`` parameter (the temporal block, including
    ``same_hour_weekday_z``) drives the DQG-override branch — see
    ``_maybe_dqg_spike_override``.

    The optional ``sustained_oor`` flag (pre-computed by
    ``pipeline._write_detections`` from the alert sequence) routes
    repeated DQG ``out_of_range`` fires on the same sensor to the
    ``level_shift`` override; a sustained OOR pattern is the level-shift
    signature when synth-gen's offset drives the off-state below the
    configured min.

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
    overridden = _maybe_dqg_dropout_override(alert, mag=mag, temporal=temporal)
    if overridden is not None:
        return ClassificationResult(
            type=overridden,
            confidence="low",
            signal_classes=["dqg", "duty"],
        )
    if sustained_oor:
        overridden = _maybe_dqg_oor_sustained_override(alert)
        if overridden is not None:
            return ClassificationResult(
                type=overridden,
                confidence="high",
                signal_classes=["dqg", "duty"],
            )
    overridden = _maybe_dqg_spike_override(alert, mag, temporal)
    if overridden is not None:
        return ClassificationResult(
            type=overridden,
            confidence="high",
            signal_classes=["dqg", "magnitude"],
        )
    overridden = _maybe_dqg_oor_override(alert, mag, temporal)
    if overridden is not None:
        # signal_classes naming reflects the discriminating bundle
        # signal: shwz (calendar / hour-of-week peer baseline) for the
        # level_shift branch, magnitude (delta_pct vs immediate
        # pre-window) for the frequency_change branch.
        sig = ["dqg", "calendar"] if overridden == "level_shift" \
              else ["dqg", "magnitude"]
        return ClassificationResult(
            type=overridden,
            confidence="high",
            signal_classes=sig,
        )
    if alert.anomaly_type:
        return ClassificationResult(
            type=alert.anomaly_type,
            confidence="high",
            signal_classes=[],
        )
    s = Signals.from_alert(alert, mag=mag)
    if sustained_dcs and "duty" in s.classes and s.direction == "+":
        # Iter 4: cross-chain hour-spread says DCS is firing across many
        # hours-of-day on this sensor in a 14d window — that's a sustained
        # behavioral anomaly, not a per-day calendar pattern.
        # Iter 6: a multi-day fused chain confined to weekdays is the
        # synth-gen `weekend_anomaly target=weekday` signature (magnitude
        # added Mon-Fri only); a chain that crosses Sat/Sun is the
        # always-on level_shift signature.
        if (s.chain_weekday_only
                and s.duration_sec > 12 * 3600):
            sustained_type = "weekend_anomaly"
        else:
            sustained_type = "level_shift"
        return ClassificationResult(
            type=sustained_type,
            confidence="high",
            signal_classes=sorted(s.classes | {"sustained"}),
        )
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


def classify_type(alert: Alert, mag: dict | None = None,
                  temporal: dict | None = None,
                  sustained_oor: bool = False,
                  sustained_dcs: bool = False) -> str:
    return classify(alert, mag=mag, temporal=temporal,
                    sustained_oor=sustained_oor,
                    sustained_dcs=sustained_dcs).type


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
    """BURSTY duty-cycle. Branches on peak/rate co-presence + calendar.

    The duty-alone branch consults DutyCycleShift's per-bucket calendar
    baseline (``s.bucket_typical``) to disambiguate calendar-pattern
    anomalies from sustained level shifts. Synth-gen's weekend_anomaly
    and time_of_day labels can land on weekday or weekend timestamps
    independent of which calendar pattern they're injecting:
      - ``target=weekend`` injects weekend-shape on weekdays — fires
        carry weekday timestamps with direction "+" in a typically-low
        bucket.
      - ``target=weekday`` injects weekday-shape on weekends — fires
        carry weekend timestamps with direction "-" in a typically-high
        bucket.
    Raw-timestamp ``is_weekend`` / ``is_off_hours`` cannot tell those
    apart from a sustained level shift; ``bucket_typical`` × direction
    can.
    """
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
    # Duty alone: bucket-typical × direction routes calendar patterns.
    bt = s.bucket_typical or "normal"
    if bt == "low" and s.direction == "+":
        # Behavior elevated during a typically-quiet calendar position.
        # Off-hours and short hour-specific chains route to time_of_day;
        # multi-hour daytime chains route to weekend_anomaly (target=
        # weekend on weekday signature: TV-style afternoon/evening
        # behavior on weekday).
        if s.is_off_hours:
            return "time_of_day"
        if s.duration_sec < 6 * 3600:
            return "time_of_day"
        return "weekend_anomaly"
    if bt == "high" and s.direction == "-":
        # Behavior depressed during a typically-busy calendar position.
        # Weekend-positioned short chains are target=weekday on weekend;
        # longer chains and weekday-positioned ones are level shifts
        # (e.g. vacation, kettle replaced).
        if s.is_weekend and s.duration_sec < 3 * 86400:
            return "weekend_anomaly"
        return "level_shift"
    # Bucket signal weak (bt=normal or direction mismatch) — bucket
    # percentile rank can be uninformative when the bootstrap is
    # noisy across hours (e.g., dense_90d kettle, where event density
    # smears each hour's duty). Fall back to chain-duration:
    #   - A direction-up chain bounded under ~12h cannot be a sustained
    #     level_shift, which would extend across the DCS 6h window
    #     repeatedly and span at least a day. Most synth-gen short
    #     direction-up signatures are calendar patterns (time_of_day at
    #     specific hours, weekend_anomaly per-day chunks).
    if s.direction == "+" and s.duration_sec < 12 * 3600:
        if s.is_off_hours:
            return "time_of_day"
        if s.is_weekend:
            return "weekend_anomaly"
        # Weekday daytime short chain — defaults to time_of_day per
        # synth-gen prior (kettle 10-12 / 14-18 daily injections are
        # the dominant pattern in this signature).
        return "time_of_day"
    # Iter 6: multi-day chain confined to weekdays → weekend_anomaly
    # target=weekday. Synth-gen weekend_anomaly target=weekday adds
    # magnitude on Mon-Fri only, so weekend duty returns to baseline
    # and the fuser splits the chain at Sat/Sun. A multi-day fused
    # chain that never crosses a weekend day is the signature.
    if (s.duration_sec > 12 * 3600
            and s.duration_sec < 7 * 86400
            and s.direction == "+"
            and s.chain_weekday_only):
        return "weekend_anomaly"
    # Existing fall-through for "normal" buckets and non-matching directions.
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
