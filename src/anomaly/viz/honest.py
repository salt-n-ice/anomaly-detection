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
from . import selection
from .context import Context


def _draw_tile(fig, x, y, w, h, *, sensor_id, friendly_type, ts, color, ctx,
               event_start=None, event_end=None):
    """Draw one mini-multiple tile.

    `event_start`/`event_end` (when provided) window the signal to a
    +/- few-day region around the GT/FP event so tile-scale plots stay
    legible. Without windowing, long-history sensors render as illegible
    smears.
    """
    import pandas as _pd
    ax = fig.add_axes([x, y, w, h])
    ax.set_facecolor(_mc.to_rgba(color, alpha=0.10))
    for s in ("top", "right", "bottom", "left"):
        ax.spines[s].set_color(color)
        ax.spines[s].set_alpha(0.4)
    sensor_events = ctx.events.get(sensor_id)
    if sensor_events is not None and len(sensor_events):
        sub = sensor_events
        if event_start is not None and event_end is not None:
            ev_dur = (event_end - event_start).total_seconds()
            pad_s = max(86400, min(7 * 86400, ev_dur / 2))
            pad = _pd.Timedelta(seconds=pad_s)
            x_lo = event_start - pad
            x_hi = event_end + pad
            m = ((sub["timestamp"] >= x_lo) & (sub["timestamp"] <= x_hi))
            sub = sub.loc[m]
            # Tinted band over the event interval
            ax.axvspan(event_start, event_end, color=color, alpha=0.20, lw=0)
        if len(sub) > 500:
            sub = sub.iloc[::max(1, len(sub) // 500)]
        if len(sub):
            ax.plot(sub["timestamp"], sub["value"],
                    color=style.LINE, lw=0.6)
    ax.tick_params(left=False, bottom=False,
                   labelleft=False, labelbottom=False)
    ax.set_title("")
    sensor_friendly = ctx.sensor_friendly.get(sensor_id, sensor_id)
    fig.text(x + 0.005, y - 0.025, sensor_friendly,
             fontsize=9, fontweight="600", color=style.TEXT)
    caption = (f"{friendly_type} · {ts.strftime('%b %d')}"
               if friendly_type else ts.strftime('%b %d'))
    fig.text(x + 0.005, y - 0.045, caption,
             fontsize=8, color=style.MUTED)


def render_honest(fig: matplotlib.figure.Figure, ctx: Context) -> None:
    style.apply()
    fig.set_facecolor(style.PAGE_BG)

    fig.text(0.06, 0.93, "What we missed · what we got wrong",
             fontsize=16, fontweight="700", color=style.GT)

    cols = 3
    tile_w = 0.27
    tile_h = 0.18

    # MISSED section. Header is only drawn when there are FNs to show; an
    # empty header above blank space looks like a layout bug.
    fns = ctx.labels[~ctx.labels["is_tp"]]
    x0 = 0.06
    fn_y0 = 0.62
    if len(fns):
        fig.text(0.06, 0.86, "MISSED", fontsize=10, fontweight="600",
                 color=style.MUTED)
    for i, (_, fn) in enumerate(fns.iterrows()):
        if i >= 6:
            break
        col = i % cols; row = i // cols
        _draw_tile(fig, x0 + col * (tile_w + 0.02),
                   fn_y0 - row * (tile_h + 0.07),
                   tile_w, tile_h,
                   sensor_id=fn["sensor_id"],
                   friendly_type=style.type_friendly(fn["anomaly_type"]),
                   ts=fn["start"], color=style.GT, ctx=ctx,
                   event_start=fn["start"], event_end=fn["end"])
    if len(fns) > 6:
        fig.text(0.06, 0.50, f"+ {len(fns) - 6} more",
                 fontsize=10, color=style.MUTED, fontstyle="italic")

    # FALSE ALARMS section. Header is conditional on having FPs, mirroring
    # the MISSED section.
    fps = selection.user_visible_fps(ctx.labels, ctx.detections)
    if len(fps):
        fig.text(0.06, 0.42, "FALSE ALARMS (user-visible)",
                 fontsize=10, fontweight="600", color=style.MUTED)
    fp_y0 = 0.20
    for i, (_, fp) in enumerate(fps.iterrows()):
        if i >= 6:
            break
        col = i % cols; row = i // cols
        _draw_tile(fig, x0 + col * (tile_w + 0.02),
                   fp_y0 - row * (tile_h + 0.07),
                   tile_w, tile_h,
                   sensor_id=fp["sensor_id"],
                   friendly_type=style.type_friendly(fp.get("inferred_type", "")),
                   ts=fp["start"], color=style.FP, ctx=ctx,
                   event_start=fp["start"], event_end=fp["end"])
    if len(fps) > 6:
        fig.text(0.06, 0.06, f"+ {len(fps) - 6} more false alarms",
                 fontsize=10, color=style.MUTED, fontstyle="italic")
