"""Color palette, matplotlib defaults, friendly mappings, and plain-English
templates. All visual constants used by the viz package live here so a future
re-skin is a one-file change.
"""
from __future__ import annotations
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

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
    "outlet", "mains", "basement", "kitchen", "livingroom", "bathroom",
})
_CAPABILITY_SUFFIXES = ("_power", "_voltage", "_leak", "_temperature")
_ACRONYM_OVERRIDES = {"tv": "TV", "ac": "AC", "ev": "EV", "led": "LED"}
# Capability suffixes whose word denotes a sensor *purpose* (not a direct
# measurement), so we tack on " sensor" for stakeholder readability.
_NEEDS_SENSOR_SUFFIX = frozenset({"_leak"})


def _titlecase_token(tok: str) -> str:
    return _ACRONYM_OVERRIDES.get(tok.lower(), tok.capitalize())


def sensor_friendly(sensor_id: str,
                    overrides: dict[str, str] | None = None) -> str:
    """Resolve sensor_id to a stakeholder-friendly display name.

    Algorithm: strip capability suffix, split on '_', reorder placement prefix
    to the back, title-case (preserving known acronyms). Single-placement
    tokens (e.g., 'mains_voltage') reconstruct as "Placement <capability>",
    with " sensor" appended for purpose-suffixes like _leak.

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
        if placement == "outlet":
            appliance = " ".join(_titlecase_token(t) for t in rest)
            return f"{appliance} outlet"
        # Non-outlet placement: trailing tokens are usually measurement nouns
        # (humidity, pressure, etc.). Lowercase them.
        rest_lower = " ".join(t.lower() for t in rest)
        return f"{_titlecase_token(placement)} {rest_lower} sensor"
    # Single placement token only (e.g., 'mains_voltage', 'kitchen_temperature')
    if len(tokens) == 1 and tokens[0] in _PLACEMENT_PREFIXES and stripped_suffix:
        cap_word = stripped_suffix.lstrip("_")  # "_voltage" -> "voltage"
        suffix = " sensor" if stripped_suffix in _NEEDS_SENSOR_SUFFIX else ""
        return f"{_titlecase_token(tokens[0])} {cap_word}{suffix}"
    # Fallback: no placement prefix recognized — sentence-case the whole id
    parts = sensor_id.split("_")
    if len(parts) == 1:
        return parts[0].capitalize()
    return parts[0].capitalize() + " " + " ".join(p.lower() for p in parts[1:])


PLAIN_ENGLISH: dict[str, str] = {
    "level_shift":            "{sensor} baseline shifted {direction_word} at the start of this period. Flagged as a level shift.",
    "weekend_anomaly":        "{sensor} ran heavily during this weekend. Flagged as a weekend pattern.",
    "time_of_day":            "{sensor} fired at {hour_str} — outside its typical hours. Flagged as a time-of-day pattern.",
    "trend":                  "{sensor} began drifting {direction_word} early in this period. Flagged as a gradual drift.",
    "water_leak_sustained":   "{sensor} began reporting flow. Flagged as a sustained leak based on sensor type.",
    "frequency_change":       "{sensor} cycled at a different rate than usual. Flagged as a frequency change.",
    "month_shift":            "{sensor} {direction_word_long} at the start of this period. Flagged as a long-term shift.",
    "degradation_trajectory": "{sensor} began showing gradual degradation. Flagged as a gradual degradation.",
    "spike":                  "{sensor} jumped sharply. Flagged as a spike.",
    "dip":                    "{sensor} dropped sharply. Flagged as a dip.",
    "dropout":                "{sensor} lost reading. Flagged as a dropout.",
    "calibration_drift":      "{sensor} drifted from its baseline. Flagged as a calibration drift.",
}

_GENERIC_TEMPLATE = "{sensor} produced an event the system flagged as a {friendly_type}."
_MISSED_TEMPLATE = (
    "The system did not detect this period. {sensor} anomalies of type "
    "'{friendly_type}' rely on detectors not currently active for this sensor."
)


def _direction_word(delta: float | None) -> str:
    if delta is None or delta != delta or delta == 0:
        return ""
    return "upward" if delta > 0 else "downward"


def _direction_word_long(delta: float | None) -> str:
    if delta is None or delta != delta or delta == 0:
        return "shifted"
    return "rose" if delta > 0 else "dropped"


def render_summary(*, anomaly_type: str, sensor_friendly_name: str,
                   is_missed: bool, delta: float | None,
                   duration_h: float, hour_str: str | None) -> str:
    """Render the plain-English summary line for a showcase page.

    Templates describe what the system saw at fire time, NOT what the GT
    label claims about duration. Caller passes in the friendly name (resolved
    upstream via `sensor_friendly`) and the anomaly type (canonical, not yet
    friendly-mapped here).
    """
    friendly = type_friendly(anomaly_type)
    if is_missed:
        return _MISSED_TEMPLATE.format(
            sensor=sensor_friendly_name, friendly_type=friendly,
        )
    tmpl = PLAIN_ENGLISH.get(anomaly_type, _GENERIC_TEMPLATE)
    return tmpl.format(
        sensor=sensor_friendly_name,
        friendly_type=friendly,
        direction_word=_direction_word(delta) or "in some direction",
        direction_word_long=_direction_word_long(delta),
        hour_str=hour_str or "",
    )


def _day_no_pad(ts: pd.Timestamp) -> str:
    """Return the day of month as a string with no leading zero.

    Platform-safe: avoids the `%-d` strftime token which is not supported
    on Windows (it would produce e.g. `'%-d'` literal or fail).
    """
    return str(ts.day)


def format_duration(seconds: float) -> str:
    """Friendly duration: '45s', '1 minute', '23 hours', '7 days'."""
    if seconds < 60:
        return f"{seconds:.0f}s"
    if seconds < 3600:
        n = int(round(seconds / 60))
        return f"{n} minute{'s' if n != 1 else ''}"
    if seconds < 86400:
        n = int(round(seconds / 3600))
        return f"{n} hour{'s' if n != 1 else ''}"
    n = int(round(seconds / 86400))
    return f"{n} day{'s' if n != 1 else ''}"


def format_date_range(start: pd.Timestamp, end: pd.Timestamp) -> str:
    """Friendly date range. Multi-day uses weekday-first long format; intraday
    shows weekday + date + clock times. Duration is rendered in hours so
    multi-day spans surface their concrete length (e.g., '48 hours').
    """
    duration_s = (end - start).total_seconds()
    hours = int(round(duration_s / 3600))
    duration_str = f"{hours} hour{'s' if hours != 1 else ''}"
    if duration_s >= 86400:
        return (f"{start.strftime('%A %b')} {_day_no_pad(start)} — "
                f"{end.strftime('%A %b')} {_day_no_pad(end)}, "
                f"{end.strftime('%Y')} · "
                f"{duration_str}")
    return (f"{start.strftime('%A %b')} {_day_no_pad(start)}, "
            f"{start.strftime('%Y')} · "
            f"{start.strftime('%H:%M')} — {end.strftime('%H:%M')} · "
            f"{duration_str}")


def format_eyebrow(start: pd.Timestamp, end: pd.Timestamp,
                   scenario_name: str | None) -> str:
    """Cover eyebrow line: 'N DAYS · SCENARIO_CLASS_UPPER'."""
    days = max(1, int(round((end - start).total_seconds() / 86400)))
    name_part = ""
    if scenario_name:
        # Trim trailing _Nd / _Nh suffix; uppercase the remainder.
        import re as _re
        cleaned = _re.sub(r"_\d+[dhmw]?$", "", scenario_name)
        name_part = " · " + cleaned.upper().replace("_", " ")
    return f"{days} DAYS{name_part}"
