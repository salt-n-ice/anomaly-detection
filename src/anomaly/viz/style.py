"""Color palette, matplotlib defaults, friendly mappings, and plain-English
templates. All visual constants used by the viz package live here so a future
re-skin is a one-file change.
"""
from __future__ import annotations
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

LINE = "#1a1a1a"
TP = "#2a7f2a"
GT = "#d62828"
FP = "#d6a228"
SUPPRESSED = "#888888"
GRID = "#f0f0f0"
TEXT = "#1a1a1a"
MUTED = "#888888"
PAGE_BG = "white"
SIGNAL_BG = "#fcfcfc"
LABEL_REGION_ALPHA = 0.10


def apply() -> None:
    """Apply plot rcParams used across all renderers."""
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "figure.facecolor": PAGE_BG,
        "axes.facecolor": PAGE_BG,
        "axes.edgecolor": "#cccccc",
        "axes.linewidth": 0.6,
        "axes.labelcolor": TEXT,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
    })
