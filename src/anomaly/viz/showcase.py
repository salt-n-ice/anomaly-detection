"""Showcase page renderer (one per curated GT label).

Layout (top to bottom):
  1. Verdict tag (CAUGHT green / MISSED red).
  2. Friendly sensor name + date range header.
  3. Hero signal trace, full page width, with label-region overlay.
  4. Best-chain pin (caught only) with verdict callout.
     Or: red dashed "no system fire" callout (missed).
  5. Plain-English summary line at the bottom.
"""
from __future__ import annotations
import matplotlib.figure
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

from . import style
from .context import Context


def _xtick_locator(label_dur_h: float):
    if label_dur_h >= 24 * 30:
        return mdates.WeekdayLocator(byweekday=0, interval=2)
    if label_dur_h >= 24:
        return mdates.DayLocator()
    return mdates.HourLocator(interval=2)


def _is_binary(values: np.ndarray) -> bool:
    uniq = set(np.unique(values).tolist())
    return uniq.issubset({0, 0.0, 1, 1.0})


def _binary_labels(capability: str) -> list[str]:
    return {
        "water":  ["no flow", "flow"],
        "motion": ["still", "motion"],
    }.get(capability, ["off", "on"])


def render_showcase(fig: matplotlib.figure.Figure, ctx: Context,
                    label: pd.Series) -> None:
    style.apply()
    fig.set_facecolor(style.PAGE_BG)
    is_missed = not bool(label["is_tp"])
    sensor_id = label["sensor_id"]
    sensor_name = ctx.sensor_friendly.get(sensor_id, sensor_id)

    # Header: verdict tag + sensor + date range
    if is_missed:
        fig.text(0.06, 0.92, "MISSED", fontsize=11, fontweight="700",
                 color="white", verticalalignment="top",
                 bbox=dict(boxstyle="round,pad=0.4",
                           facecolor=style.GT, edgecolor=style.GT,
                           linewidth=1.2))
    else:
        fig.text(0.06, 0.92, "CAUGHT", fontsize=11, fontweight="700",
                 color=style.TP, verticalalignment="top",
                 bbox=dict(boxstyle="round,pad=0.4",
                           facecolor="white", edgecolor=style.TP,
                           linewidth=1.2))
    fig.text(0.13, 0.93, sensor_name,
             fontsize=20, fontweight="700", color=style.TEXT,
             verticalalignment="top")
    date_range = style.format_date_range(label["start"], label["end"])
    fig.text(0.13, 0.89, date_range, fontsize=11, color=style.MUTED,
             verticalalignment="top")

    # Signal area
    ax = fig.add_axes([0.06, 0.20, 0.88, 0.62])
    ax.set_facecolor(style.SIGNAL_BG)
    pad_s = max(86400, min(14 * 86400,
                           (label["end"] - label["start"]).total_seconds() / 4))
    pad = pd.Timedelta(seconds=pad_s)
    x_lo = label["start"] - pad
    x_hi = label["end"] + pad

    sensor_events = ctx.events.get(sensor_id)
    if sensor_events is not None and len(sensor_events):
        m = ((sensor_events["timestamp"] >= x_lo)
             & (sensor_events["timestamp"] <= x_hi))
        sub = sensor_events.loc[m]
        if len(sub) > 2000:
            step = max(1, len(sub) // 2000)
            sub = sub.iloc[::step]
        if len(sub):
            vals = sub["value"].to_numpy(dtype=float)
            if _is_binary(vals):
                ax.step(sub["timestamp"], vals, where="post",
                        color=style.LINE, lw=1.4)
                ax.set_yticks([0, 1])
                ax.set_yticklabels(_binary_labels(ctx.sensor_capability.get(sensor_id, "")))
                ax.set_ylim(-0.2, 1.2)
            else:
                ax.plot(sub["timestamp"], vals, color=style.LINE, lw=1.0)

    # Label region overlay
    ax.axvspan(label["start"], label["end"],
               color=style.GT, alpha=style.LABEL_REGION_ALPHA, lw=0)
    ax.axvline(label["start"], color=style.GT, lw=1.2, ls="--", alpha=0.6)
    ax.axvline(label["end"],   color=style.GT, lw=1.2, ls="--", alpha=0.6)

    ax.set_xlim(x_lo, x_hi)
    ax.tick_params(labelsize=8)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    loc = _xtick_locator((label["end"] - label["start"]).total_seconds() / 3600)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(loc))

    # Best-chain pin + verdict callout (caught) OR no-fire callout (missed)
    if not is_missed and pd.notna(label.get("best_chain_idx", None)):
        chain_idx = int(label["best_chain_idx"])
        chain = ctx.detections.iloc[chain_idx]
        pin_t = chain["start"]
        # Find y of signal at pin_t for the pin's vertical position
        if sensor_events is not None and len(sensor_events):
            nearest = sensor_events.iloc[
                (sensor_events["timestamp"] - pin_t).abs().argmin()
            ]
            pin_y = float(nearest["value"])
        else:
            pin_y = 0.5
        ax.plot([pin_t], [pin_y], "o", color=style.TP, markersize=8,
                markeredgecolor="white", markeredgewidth=1.5)
        verdict_friendly = style.type_friendly(
            chain.get("inferred_type", label["anomaly_type"])
        )
        fig.text(0.65, 0.83, "SYSTEM VERDICT",
                 fontsize=9, fontweight="600", color=style.TP)
        fig.text(0.65, 0.79, verdict_friendly,
                 fontsize=14, fontweight="700", color=style.TEXT)
    elif is_missed:
        fig.text(0.65, 0.83, "NO SYSTEM FIRE",
                 fontsize=9, fontweight="600", color=style.GT)
        fig.text(0.65, 0.79, "This period was not detected.",
                 fontsize=12, fontweight="700", color=style.TEXT)

    # Plain-English summary
    delta = None
    duration_h = (label["end"] - label["start"]).total_seconds() / 3600
    summary = style.render_summary(
        anomaly_type=label["anomaly_type"],
        sensor_friendly_name=sensor_name,
        is_missed=is_missed,
        delta=delta,
        duration_h=duration_h,
        hour_str=label["start"].strftime("%H:%M"),
    )
    fig.text(0.06, 0.10, summary, fontsize=12, color=style.TEXT,
             wrap=True)
