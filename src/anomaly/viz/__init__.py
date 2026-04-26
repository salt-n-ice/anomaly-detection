"""Stakeholder-facing PDF renderer for anomaly detection runs.

Per the 2026-04-26 design: per-scenario PDF with cover + curated showcases +
honest accounting + suppression footnote + appendix table. Replaces the
monolithic per-day-window viz.

The legacy `render_long` (per-incident long-form PDF) is preserved unchanged
as `viz.long.render_long` and re-exported here.
"""
from __future__ import annotations
from .long import render_long

__all__ = ["render_long"]
# Note: `render` re-export is added in Task 14, after document.py is implemented.
# Keeping the temporary single-export form during scaffolding lets render_long
# import without depending on stub modules.
