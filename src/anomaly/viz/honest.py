"""Honest accounting page: missed labels + user-visible false alarms.

Layout: Two tinted sections, each a 3-column mini-multiples grid.
- Top section: 'WHAT WE MISSED' — pink-tinted FN tiles.
- Bottom section: 'FALSE ALARMS' — amber-tinted user-visible FP tiles.
Page is omitted by document.py when both lists are empty.
"""
from __future__ import annotations
import matplotlib.figure
import matplotlib.colors as _mc
import pandas as pd

from . import style
from .context import Context


def _user_visible_fps(ctx: Context) -> pd.DataFrame:
    """Return rows of detections where inferred_class == 'user_behavior'
    and there is no overlapping GT label."""
    label_intervals: dict[str, list[tuple[pd.Timestamp, pd.Timestamp]]] = {}
    for _, lab in ctx.labels.iterrows():
        label_intervals.setdefault(lab["sensor_id"], []).append(
            (lab["start"], lab["end"]))

    def _is_fp(row) -> bool:
        if row.get("inferred_class") != "user_behavior":
            return False
        for s, e in label_intervals.get(row["sensor_id"], []):
            if row["start"] <= e and row["end"] >= s:
                return False
        return True

    return ctx.detections[ctx.detections.apply(_is_fp, axis=1)]


def _draw_tile(fig, x, y, w, h, *, sensor_id, friendly_type, ts, color, ctx):
    ax = fig.add_axes([x, y, w, h])
    ax.set_facecolor(_mc.to_rgba(color, alpha=0.10))
    for s in ("top", "right", "bottom", "left"):
        ax.spines[s].set_color(color)
        ax.spines[s].set_alpha(0.4)
    sensor_events = ctx.events.get(sensor_id)
    if sensor_events is not None and len(sensor_events):
        ax.plot(sensor_events["timestamp"], sensor_events["value"],
                color=style.LINE, lw=0.6)
    ax.tick_params(left=False, bottom=False,
                   labelleft=False, labelbottom=False)
    ax.set_title("")
    sensor_friendly = ctx.sensor_friendly.get(sensor_id, sensor_id)
    fig.text(x + 0.005, y - 0.025, sensor_friendly,
             fontsize=9, fontweight="600", color=style.TEXT)
    fig.text(x + 0.005, y - 0.045,
             f"{friendly_type} · {ts.strftime('%b %d')}",
             fontsize=8, color=style.MUTED)


def render_honest(fig: matplotlib.figure.Figure, ctx: Context) -> None:
    style.apply()
    fig.set_facecolor(style.PAGE_BG)

    fig.text(0.06, 0.93, "What we missed · what we got wrong",
             fontsize=16, fontweight="700", color=style.GT)

    # MISSED section
    fns = ctx.labels[~ctx.labels["is_tp"]]
    fig.text(0.06, 0.86, "MISSED", fontsize=10, fontweight="600",
             color=style.MUTED)
    cols = 3
    tile_w = 0.27; tile_h = 0.18
    x0 = 0.06; y0 = 0.62
    for i, (_, fn) in enumerate(fns.iterrows()):
        if i >= 6:
            break
        col = i % cols; row = i // cols
        _draw_tile(fig, x0 + col * (tile_w + 0.02), y0 - row * (tile_h + 0.07),
                   tile_w, tile_h,
                   sensor_id=fn["sensor_id"],
                   friendly_type=style.type_friendly(fn["anomaly_type"]),
                   ts=fn["start"], color=style.GT, ctx=ctx)
    if len(fns) > 6:
        fig.text(0.06, 0.50, f"+ {len(fns) - 6} more",
                 fontsize=10, color=style.MUTED, fontstyle="italic")

    # FALSE ALARMS section
    fps = _user_visible_fps(ctx)
    fig.text(0.06, 0.42, "FALSE ALARMS (user-visible)",
             fontsize=10, fontweight="600", color=style.MUTED)
    y0 = 0.20
    for i, (_, fp) in enumerate(fps.iterrows()):
        if i >= 6:
            break
        col = i % cols; row = i // cols
        _draw_tile(fig, x0 + col * (tile_w + 0.02), y0 - row * (tile_h + 0.07),
                   tile_w, tile_h,
                   sensor_id=fp["sensor_id"],
                   friendly_type=style.type_friendly(fp.get("inferred_type", "")),
                   ts=fp["start"], color=style.FP, ctx=ctx)
