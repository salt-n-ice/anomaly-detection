"""Cover page renderer.

Layout (top to bottom):
  1. Eyebrow line (small caps duration + scenario name).
  2. Hero metric (large numerator + smaller denominator + 'caught' subline).
  3. Caught-by-type bar chart (top 6 types + 'and N more').
  4. Scenario timeline strip with caught/missed markers per GT label.
  5. Suppression footer line.
"""
from __future__ import annotations
import matplotlib.figure
import matplotlib.dates as mdates
from collections import Counter

from . import style
from .context import Context


def render_cover(fig: matplotlib.figure.Figure, ctx: Context) -> None:
    style.apply()
    fig.set_facecolor(style.PAGE_BG)

    # 1. Eyebrow
    fig.text(0.06, 0.92, ctx.eyebrow,
             fontsize=11, fontweight="600", color=style.MUTED)
    date_range = (f"{ctx.scenario_start.strftime('%b %d, %Y')} - "
                  f"{ctx.scenario_end.strftime('%b %d, %Y')}")
    fig.text(0.06, 0.89, date_range, fontsize=9, color=style.MUTED)

    # 2. Hero metric
    hero_color = style.GT if ctx.n_tp == 0 else style.TEXT
    fig.text(0.06, 0.76, str(ctx.n_tp),
             fontsize=72, fontweight="700", color=hero_color)
    # Approximate offset for the "of N" small text alongside the big numeral.
    offset_x = 0.06 + 0.013 * len(str(ctx.n_tp)) + 0.04
    fig.text(offset_x, 0.78, f"of {ctx.n_total_labels}",
             fontsize=22, color=style.MUTED)
    fig.text(0.06, 0.71, "anomalies caught",
             fontsize=14, color=style.TEXT)

    # 3. Caught-by-type bar chart
    tp_labels = ctx.labels[ctx.labels["is_tp"]]
    type_counts = Counter(tp_labels["anomaly_type"])
    top = type_counts.most_common(6)
    if len(type_counts) > 6:
        rest = sum(c for _, c in type_counts.most_common()[6:])
        top.append(("... and others", rest))
    if top:
        ax_bar = fig.add_axes([0.06, 0.34, 0.40, 0.28])
        ax_bar.set_facecolor(style.PAGE_BG)
        types = [style.type_friendly(t) if not t.startswith("...") else t
                 for t, _ in top]
        counts = [c for _, c in top]
        y_pos = list(range(len(types)))
        max_c = max(counts) if counts else 1
        palette = ["#1565c0", "#3b82c4", "#5fa1d6", "#7eb3df",
                   "#9cc4e7", "#bcd5ee", "#dde6ef"]
        bar_colors = [palette[i % len(palette)] for i in range(len(types))]
        ax_bar.barh(y_pos, counts, height=0.55, color=bar_colors)
        ax_bar.set_yticks(y_pos)
        ax_bar.set_yticklabels(types, fontsize=10, color=style.TEXT)
        ax_bar.invert_yaxis()
        ax_bar.set_xlim(0, max_c * 1.15)
        ax_bar.tick_params(left=False, bottom=False, labelbottom=False)
        for s in ("top", "right", "bottom"):
            ax_bar.spines[s].set_visible(False)
        ax_bar.spines["left"].set_visible(False)
        for i, c in enumerate(counts):
            ax_bar.text(c + max_c * 0.02, i, str(c), va="center",
                        fontsize=9, color=style.MUTED)
        fig.text(0.06, 0.64, "CAUGHT BY TYPE",
                 fontsize=9, fontweight="600", color=style.MUTED)

    # 4. Scenario timeline strip
    ax_tl = fig.add_axes([0.50, 0.40, 0.44, 0.20])
    ax_tl.set_facecolor(style.PAGE_BG)
    ax_tl.set_xlim(ctx.scenario_start, ctx.scenario_end)
    ax_tl.set_ylim(-1, 1)
    ax_tl.axhline(0, color="#d0d0d0", lw=0.6)
    for _, lab in ctx.labels.iterrows():
        x = mdates.date2num(lab["start"])
        if lab["is_tp"]:
            ax_tl.plot([x], [0], "o", color=style.TP, markersize=8)
        else:
            ax_tl.plot([x], [0], "x", color=style.GT, markersize=10,
                       markeredgewidth=2.0)
    ax_tl.tick_params(left=False, labelleft=False, labelsize=8)
    for s in ("top", "right", "left"):
        ax_tl.spines[s].set_visible(False)
    ax_tl.spines["bottom"].set_color("#d0d0d0")
    loc = mdates.AutoDateLocator(maxticks=8)
    ax_tl.xaxis.set_major_locator(loc)
    ax_tl.xaxis.set_major_formatter(mdates.ConciseDateFormatter(loc))
    fig.text(0.50, 0.62, "SCENARIO TIMELINE",
             fontsize=9, fontweight="600", color=style.MUTED)
    # Legend
    fig.text(0.50, 0.36, f"●  caught ({ctx.n_tp})",
             fontsize=9, color=style.TP)
    fig.text(0.60, 0.36, f"×  missed ({ctx.n_fn})",
             fontsize=9, color=style.GT)

    # 5. Suppression footer
    if ctx.n_suppressed:
        total_fires = ctx.n_suppressed + ctx.n_user_visible_fps + ctx.n_tp
        pct = 100.0 * ctx.n_suppressed / max(1, total_fires)
        footer = (f"~{pct:.0f}% of fires ({ctx.n_suppressed:,} of "
                  f"{total_fires:,}) were filtered as sensor noise - "
                  f"never reached the user.")
        fig.text(0.06, 0.06, footer, fontsize=10, color=style.MUTED,
                 fontstyle="italic")
