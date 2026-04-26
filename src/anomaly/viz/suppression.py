"""Suppression page: 'Quietly suppressed' header + per-sensor count bar list.

Document.py omits this page when ctx.n_suppressed < 50 and folds the count
into the cover footer line instead.
"""
from __future__ import annotations
import matplotlib.figure

from . import style
from .context import Context


def render_suppression(fig: matplotlib.figure.Figure, ctx: Context) -> None:
    style.apply()
    fig.set_facecolor(style.PAGE_BG)

    fig.text(0.06, 0.92, "Quietly suppressed",
             fontsize=18, fontweight="700", color=style.MUTED)
    fig.text(0.06, 0.81, f"{ctx.n_suppressed:,}",
             fontsize=56, fontweight="700", color=style.TEXT)
    fig.text(0.06, 0.74,
             "low-level fires filtered as sensor noise",
             fontsize=11, color=style.MUTED)

    fig.text(0.06, 0.62, "BY SENSOR",
             fontsize=9, fontweight="600", color=style.MUTED)

    top = ctx.suppression_by_sensor[:6]
    if not top:
        return
    max_c = max(c for _, c in top)
    ax = fig.add_axes([0.06, 0.30, 0.88, 0.30])
    ax.set_facecolor(style.PAGE_BG)
    sensor_labels = [ctx.sensor_friendly.get(sid, sid) for sid, _ in top]
    counts = [c for _, c in top]
    y_pos = list(range(len(top)))
    ax.barh(y_pos, counts, color="#bbbbbb", height=0.55)
    ax.invert_yaxis()
    ax.set_yticks(y_pos)
    ax.set_yticklabels(sensor_labels, fontsize=10)
    ax.set_xlim(0, max_c * 1.15)
    ax.tick_params(left=False, bottom=False, labelbottom=False)
    for s in ("top", "right", "bottom", "left"):
        ax.spines[s].set_visible(False)
    for i, c in enumerate(counts):
        ax.text(c + max_c * 0.02, i, f"{c:,}", va="center",
                fontsize=9, color=style.MUTED)

    if len(ctx.suppression_by_sensor) > 6:
        fig.text(0.06, 0.22,
                 f"+ {len(ctx.suppression_by_sensor) - 6} more sensors",
                 fontsize=10, color=style.MUTED, fontstyle="italic")
    fig.text(0.06, 0.10,
             '"None of these reach the user dashboard."',
             fontsize=11, color=style.MUTED, fontstyle="italic")
