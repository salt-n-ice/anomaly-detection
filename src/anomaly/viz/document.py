"""Public render() entry point and per-scenario page sequencing.

Page order (per spec section 3, with omission rules):
  1. Cover (always).
  2. Curated showcases (one per type, up to max_showcases).
  3. Honest accounting (omitted if zero FNs and zero user-visible FPs).
  4. Suppression (omitted if n_suppressed < 50; folds into cover footer).
  5. Appendix (always, auto-paginates).
"""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from . import style
from . import cover as cover_mod
from . import showcase as showcase_mod
from . import honest as honest_mod
from . import suppression as suppression_mod
from . import appendix as appendix_mod
from . import selection
from .context import Context

_SUPPRESSION_THRESHOLD = 50


def render(events: pd.DataFrame, labels: pd.DataFrame,
           detections: pd.DataFrame, out_path: Path | str, *,
           sensor_names: dict[str, str] | None = None,
           max_showcases: int = 8,
           excluded_sensors: frozenset[str] = frozenset(),
           title: str | None = None) -> None:
    """Render the per-scenario stakeholder PDF to `out_path`.

    Builds a Context once, then sequences pages and writes via PdfPages.
    """
    style.apply()
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    ctx = Context.build(
        events, labels, detections,
        sensor_names=sensor_names,
        excluded_sensors=excluded_sensors,
        title=title,
    )

    showcases = selection.select_showcases(ctx.labels, max_n=max_showcases)
    has_honest_content = (ctx.n_fn > 0) or (ctx.n_user_visible_fps > 0)
    show_suppression_page = ctx.n_suppressed >= _SUPPRESSION_THRESHOLD

    with PdfPages(out_path) as pdf:
        # 1. Cover
        fig = plt.figure(figsize=(13, 7))
        cover_mod.render_cover(fig, ctx)
        pdf.savefig(fig, facecolor="white"); plt.close(fig)

        # 2. Curated showcases
        for _, lab in showcases.iterrows():
            fig = plt.figure(figsize=(13, 7))
            showcase_mod.render_showcase(fig, ctx, lab)
            pdf.savefig(fig, facecolor="white"); plt.close(fig)

        # 3. Honest accounting
        if has_honest_content:
            fig = plt.figure(figsize=(13, 7))
            honest_mod.render_honest(fig, ctx)
            pdf.savefig(fig, facecolor="white"); plt.close(fig)

        # 4. Suppression
        if show_suppression_page:
            fig = plt.figure(figsize=(13, 7))
            suppression_mod.render_suppression(fig, ctx)
            pdf.savefig(fig, facecolor="white"); plt.close(fig)

        # 5. Appendix (auto-paginates)
        for fig in appendix_mod.iter_appendix_figures(ctx):
            pdf.savefig(fig, facecolor="white"); plt.close(fig)
