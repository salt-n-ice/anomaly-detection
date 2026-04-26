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


TYPE_FRIENDLY: dict[str, str] = {
    "level_shift":            "level shift",
    "weekend_anomaly":        "weekend pattern",
    "time_of_day":            "time-of-day pattern",
    "trend":                  "gradual drift",
    "water_leak_sustained":   "sustained water leak",
    "frequency_change":       "frequency change",
    "month_shift":            "long-term shift",
    "degradation_trajectory": "gradual degradation",
    "unusual_occupancy":      "unusual occupancy",
    "stuck_at":               "frozen reading",
    "dropout":                "dropout",
    "spike":                  "spike",
    "dip":                    "dip",
    "calibration_drift":      "calibration drift",
    "saturation":             "saturation",
    "noise_burst":            "noise burst",
    "noise_floor_up":         "elevated noise floor",
    "duplicate_stale":        "duplicate readings",
    "reporting_rate_change":  "reporting rate change",
    "clock_drift":            "clock drift",
    "batch_arrival":          "batched delivery",
    "out_of_range":           "out of range",
    "extreme_value":          "extreme value",
    "seasonality_loss":       "seasonality loss",
    "seasonal_mismatch":      "seasonal mismatch",
}


def type_friendly(t: str) -> str:
    """Friendly display name for an anomaly type. Title-case fallback for unknowns."""
    if t in TYPE_FRIENDLY:
        return TYPE_FRIENDLY[t]
    return t.replace("_", " ")


_PLACEMENT_PREFIXES = frozenset({
    "outlet", "mains", "basement", "bedroom", "kitchen", "livingroom", "bathroom",
})
_CAPABILITY_SUFFIXES = ("_power", "_voltage", "_leak", "_motion", "_temperature")
_ACRONYM_OVERRIDES = {"tv": "TV", "ac": "AC", "ev": "EV", "led": "LED"}
# Capability suffixes whose word denotes a sensor *purpose* (not a direct
# measurement), so we tack on " sensor" for stakeholder readability.
_NEEDS_SENSOR_SUFFIX = frozenset({"_leak", "_motion"})


def _titlecase_token(tok: str) -> str:
    return _ACRONYM_OVERRIDES.get(tok.lower(), tok.capitalize())


def sensor_friendly(sensor_id: str,
                    overrides: dict[str, str] | None = None) -> str:
    """Resolve sensor_id to a stakeholder-friendly display name.

    Algorithm: strip capability suffix, split on '_', reorder placement prefix
    to the back, title-case (preserving known acronyms). Single-placement
    tokens (e.g., 'mains_voltage') reconstruct as "Placement <capability>",
    with " sensor" appended for purpose-suffixes like _leak / _motion.

    Override via the optional `overrides` dict (sensor_id -> friendly).
    """
    if overrides and sensor_id in overrides:
        return overrides[sensor_id]
    base = sensor_id
    stripped_suffix = ""
    for suf in _CAPABILITY_SUFFIXES:
        if base.endswith(suf):
            stripped_suffix = suf
            base = base[:-len(suf)]
            break
    tokens = base.split("_")
    if not tokens or tokens == [""]:
        return sensor_id
    # Recognized placement prefix with at least one trailing appliance token
    if len(tokens) >= 2 and tokens[0] in _PLACEMENT_PREFIXES:
        placement, *rest = tokens
        appliance = " ".join(_titlecase_token(t) for t in rest)
        if placement == "outlet":
            return f"{appliance} outlet"
        return f"{_titlecase_token(placement)} {appliance} sensor"
    # Single placement token only (e.g., 'mains_voltage', 'kitchen_temperature')
    if len(tokens) == 1 and tokens[0] in _PLACEMENT_PREFIXES and stripped_suffix:
        cap_word = stripped_suffix.lstrip("_")  # "_voltage" -> "voltage"
        suffix = " sensor" if stripped_suffix in _NEEDS_SENSOR_SUFFIX else ""
        return f"{_titlecase_token(tokens[0])} {cap_word}{suffix}"
    # Fallback: no placement prefix recognized — sentence-case the whole id
    parts = sensor_id.split("_")
    if len(parts) == 1:
        return parts[0].capitalize()
    return parts[0].capitalize() + " " + " ".join(parts[1:])
