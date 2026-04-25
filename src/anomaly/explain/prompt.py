"""LLM-prompt rendering for explain bundles.

`build_prompt(bundle)` returns the natural-language prompt for the LLM
consumer. Phase A keeps the existing semantics — Phase C revises this
under the "signal-rich, verdict-light" principle.
"""
from __future__ import annotations
import pandas as pd


def _human_duration(s: float) -> str:
    if s < 60:
        return f"{s:.0f}s"
    if s < 3600:
        return f"{s/60:.1f}m"
    if s < 86400:
        return f"{s/3600:.2f}h"
    return f"{s/86400:.2f}d"


def _human_ts(iso: str) -> str:
    try:
        return pd.Timestamp(iso).strftime("%a %b %d %Y %H:%M UTC")
    except (ValueError, TypeError):
        return str(iso)


def _weekend_day_count(start_iso: str, end_iso: str) -> int:
    s = pd.Timestamp(start_iso)
    e = pd.Timestamp(end_iso)
    days = pd.date_range(s.normalize(), e.normalize(), freq="D")
    return sum(1 for d in days if d.dayofweek >= 5)


def _format_detector_context(ctx: dict) -> str:
    det = ctx.get("detector", "unknown")
    rest = {k: v for k, v in ctx.items() if k != "detector"}
    if not rest:
        return det
    kvs = ", ".join(f"{k}={v}" for k, v in rest.items())
    return f"{det}: {kvs}"


def _sensor_profile_line(bundle: dict) -> str | None:
    """Render a one-line sensor profile from bootstrap stats in detector_context.

    Format: "Sensor profile: <archetype> <capability> — typical peak ~X
    when on; bootstrap window 14d." Drawn from per-detector context dicts;
    returns None when contexts are empty so we don't render a fake number.
    """
    archetype = bundle.get("archetype", "UNKNOWN")
    capability = bundle.get("capability", "")
    ctx = bundle.get("detector_context") or []
    if not ctx:
        return None
    peak_median = None
    for c in ctx:
        if c.get("detector", "").startswith("rolling_median_peak_shift"):
            peak_median = c.get("bootstrap_median")
            break
        if c.get("detector") == "cusum":
            peak_median = c.get("mu")
    if peak_median is None or peak_median != peak_median:  # NaN check
        # Still emit the archetype + capability line even without peak —
        # better than no profile at all.
        return f"**Sensor profile:** {archetype} {capability}."
    return (f"**Sensor profile:** {archetype} {capability} — "
            f"baseline ~{peak_median:.4g} during typical samples.")


def _presentation_banner(bundle: dict) -> str | None:
    """Single-line banner when the classifier flagged this as infrastructure.

    The LLM is told this is sensor-fault; downstream household-facing
    summaries should typically suppress unless correlated with behavior.
    """
    presentation = bundle.get("classification", {}).get("presentation")
    if presentation != "infrastructure":
        return None
    return ("⚠ **Infrastructure signal** (not a household behavior change). "
            "Household-facing summary should generally suppress unless "
            "correlated with a behavior issue.")


_SIGNAL_CLASS_LABELS: dict[str, str] = {
    "duty":      "time-in-state (duty cycle)",
    "peak":      "per-event peak magnitude",
    "rate":      "event-arrival rate",
    "magnitude": "value-domain magnitude",
    "calendar":  "hour/weekday calendar bucket",
    "dqg":       "data-quality gate",
    "state":     "BINARY state transition",
}


def _signal_class_narrative(bundle: dict) -> str | None:
    """Auto-generated bridge: \"Signals fired: time-in-state and per-event peak
    magnitude both deviated from bootstrap.\" Returns None for pre-typed alerts
    (no signal_classes recorded)."""
    classes = bundle.get("classification", {}).get("signal_classes") or []
    labels = [_SIGNAL_CLASS_LABELS.get(c, c) for c in classes]
    if not labels:
        return None
    if len(labels) == 1:
        return f"**Signals fired:** {labels[0]} deviated from bootstrap."
    if len(labels) == 2:
        return (f"**Signals fired:** {labels[0]} and {labels[1]} both deviated "
                f"from bootstrap.")
    return (f"**Signals fired:** {', '.join(labels[:-1])}, and {labels[-1]} "
            f"all deviated from bootstrap.")


def _heuristic_hint(bundle: dict) -> str | None:
    """Final advisory line. Tells the LLM what our deterministic classifier
    suggests AND that it can override based on context outside this bundle.
    Wording invites override, doesn't assert authority.
    """
    cls = bundle.get("classification", {})
    type_ = cls.get("type")
    confidence = cls.get("confidence", "low")
    if type_ is None or type_ == "statistical_anomaly":
        return ("**Heuristic classifier:** type uncertain — detector signals "
                "don't fit a canonical pattern. Reason from the evidence above.")
    return (f"**Heuristic classifier:** suggests **{type_}** (confidence: "
            f"{confidence}). Use as a starting point; refine based on "
            f"signals above and any context outside this bundle.")


def build_prompt(bundle: dict) -> str:
    """Render an explainer bundle as an LLM-ready natural-language prompt.

    Principle: signal-rich, verdict-light. The LLM combines our bundle with
    external context (household state, cross-sensor patterns, device
    knowledge) the pipeline doesn't have. Heuristic classification is
    surfaced as an advisory hint at the end, explicitly invitable to
    override; the body is dominated by raw signal evidence.
    """
    sensor = bundle["sensor"]
    cap = bundle["capability"]
    archetype = bundle.get("archetype", "UNKNOWN")
    w = bundle["window"]
    mag = bundle.get("magnitude") or {}
    temp = bundle.get("temporal") or {}
    dets = bundle.get("detectors") or []
    dctx = bundle.get("detector_context") or []
    score = bundle.get("score")

    lines: list[str] = [
        f"# Anomaly on sensor {sensor} (capability: {cap}, archetype: {archetype})",
        "",
    ]

    # Sensor profile (optional — only when bootstrap stats available)
    profile = _sensor_profile_line(bundle)
    if profile:
        lines.append(profile)
        lines.append("")

    # Presentation banner (only when sensor_fault)
    banner = _presentation_banner(bundle)
    if banner:
        lines.append(banner)
        lines.append("")

    # When
    dur_sec = float(w.get("duration_sec", 0))
    lines.append(
        f"**When:** {_human_ts(w['start'])} -> {_human_ts(w['end'])} "
        f"(duration {_human_duration(dur_sec)})."
    )
    if dur_sec >= 86400:
        n_days = dur_sec / 86400
        n_weekends = _weekend_day_count(w["start"], w["end"])
        lines.append(
            f"**Long-duration framing:** spans {n_days:.1f} days; "
            f"covers {n_weekends} weekend day(s)."
        )
    lines.append("")

    # Magnitude
    baseline = mag.get("baseline")
    if baseline is not None and baseline == baseline:
        lines.append(
            f"**Magnitude:** baseline {baseline:.4g} "
            f"(source: {mag.get('baseline_source', 'unknown')}), "
            f"peak {mag.get('peak'):.4g}, "
            f"delta {mag.get('delta'):+.4g} "
            f"({mag.get('delta_pct'):+.2f}%)."
        )
    else:
        lines.append("**Magnitude:** baseline unavailable (no pre-window data).")
    lines.append("")

    # Calendar context
    lines.append(
        f"**Calendar context:** {temp.get('weekday', '?')}, "
        f"hour {temp.get('hour', '?')} ({temp.get('time_of_day_bucket', '?')}), "
        f"{'weekend' if temp.get('is_weekend') else 'weekday'}, "
        f"{temp.get('month', '?')}."
    )
    shwz = temp.get("same_hour_weekday_z")
    if shwz is not None and shwz == shwz:
        lines.append(
            f"**Same-hour-of-weekday baseline:** peak is "
            f"{shwz:+.2f}σ vs. the median of {temp.get('same_hour_weekday_n', 0)} "
            f"prior {temp.get('weekday', '?')} {temp.get('hour', '?')}:00 samples "
            f"(peer median {temp.get('same_hour_weekday_median'):.4g})."
        )
    lines.append("")

    # Signal-class narrative bridge (NEW)
    bridge = _signal_class_narrative(bundle)
    if bridge:
        lines.append(bridge)
        lines.append("")

    # Detector evidence (rich, full fidelity)
    lines.append("**Detector evidence:**")
    if dctx:
        for ctx in dctx:
            lines.append(f"- {_format_detector_context(ctx)}")
    else:
        lines.append(
            "- (per-detector context dicts unavailable on this alert; "
            "see detectors list below)"
        )
    lines.append("")

    # Detectors fired
    lines.append(f"**Detectors fired:** {', '.join(dets) if dets else 'none'}.")
    lines.append("")

    # Score (threshold dropped from bundle in Phase B)
    if score is not None:
        lines.append(f"**Score:** {score:.3g}.")
        lines.append("")

    # Heuristic hint (advisory; LAST)
    hint = _heuristic_hint(bundle)
    if hint:
        lines.append(hint)

    return "\n".join(lines).rstrip()
