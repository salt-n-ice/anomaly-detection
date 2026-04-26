"""Appendix table: every GT label with caught/missed verdict.

Yields one matplotlib.Figure per page. Pagination occurs at ~40 rows per page.
"""
from __future__ import annotations
import matplotlib.figure
import matplotlib.pyplot as plt
from typing import Iterator

from . import style
from .context import Context

_ROWS_PER_PAGE = 40


def iter_appendix_figures(ctx: Context) -> Iterator[matplotlib.figure.Figure]:
    style.apply()
    rows = []
    for _, lab in ctx.labels.sort_values(by=["is_tp", "start"],
                                          ascending=[False, True]).iterrows():
        rows.append({
            "sensor": ctx.sensor_friendly.get(lab["sensor_id"], lab["sensor_id"]),
            "type":   style.type_friendly(lab["anomaly_type"]),
            "when":   lab["start"].strftime("%b %d"),
            "duration": style.format_duration(
                (lab["end"] - lab["start"]).total_seconds()),
            "result": ("✓ caught" if lab["is_tp"] else "× missed"),
            "color":  style.TP if lab["is_tp"] else style.GT,
        })
    if not rows:
        return
    n_pages = max(1, (len(rows) + _ROWS_PER_PAGE - 1) // _ROWS_PER_PAGE)
    for p in range(n_pages):
        chunk = rows[p * _ROWS_PER_PAGE : (p + 1) * _ROWS_PER_PAGE]
        fig = plt.figure(figsize=(13, 7))
        fig.set_facecolor(style.PAGE_BG)
        title = "All incidents" + (f" · page {p+1} of {n_pages}"
                                    if n_pages > 1 else "")
        fig.text(0.06, 0.93, title, fontsize=16, fontweight="700",
                 color=style.TEXT)
        fig.text(0.06, 0.89,
                 f"{ctx.n_total_labels} rows total — "
                 f"{ctx.n_tp} caught, {ctx.n_fn} missed",
                 fontsize=10, color=style.MUTED, fontstyle="italic")
        # Header
        col_x = [0.06, 0.30, 0.50, 0.62, 0.80]
        headers = ["SENSOR", "TYPE", "WHEN", "DURATION", "RESULT"]
        for x, h in zip(col_x, headers):
            fig.text(x, 0.83, h, fontsize=9, fontweight="600",
                     color=style.MUTED)
        # Rows
        y = 0.79
        row_h = 0.018
        for r in chunk:
            for x, key in zip(col_x, ["sensor", "type", "when",
                                       "duration", "result"]):
                if key == "result":
                    color = r["color"]
                elif r["result"].startswith("×"):  # missed row -> muted
                    color = style.MUTED
                else:
                    color = style.TEXT
                fig.text(x, y, r[key], fontsize=9, color=color)
            y -= row_h
            if y < 0.05:
                break
        yield fig
