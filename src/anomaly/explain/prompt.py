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


def build_prompt(bundle: dict) -> str:
    """Render an explainer bundle as an LLM-ready natural-language prompt.

    Deliberately omits ``inferred_type`` from the text: the classifier's
    heuristics are noisy on mixed-detector events and pushing an opinionated
    label ahead of the evidence biases the LLM. The LLM gets the raw signal
    (detectors fired, magnitude, per-detector context dicts when available,
    temporal framing) and reasons about the type itself.

    Duration framing adapts: short events get ``Xh``; events >= 24h get a
    ``Long-duration framing`` line with day span and weekend-day count.
    """
    sensor = bundle["sensor"]
    cap = bundle["capability"]
    w = bundle["window"]
    mag = bundle.get("magnitude") or {}
    temp = bundle.get("temporal") or {}
    dets = bundle.get("detectors") or []
    dctx = bundle.get("detector_context") or []
    score = bundle.get("score")
    threshold = bundle.get("threshold")

    lines: list[str] = [f"# Anomaly on sensor {sensor} (capability: {cap})", ""]

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

    lines.append(f"**Detectors fired:** {', '.join(dets) if dets else 'none'}.")
    lines.append("")

    if score is not None and threshold is not None:
        lines.append(f"**Score:** {score:.3g} (threshold {threshold:.3g}).")

    return "\n".join(lines).rstrip()
