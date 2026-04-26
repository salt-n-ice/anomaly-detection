import pandas as pd


def test_style_palette_constants_present():
    from anomaly.viz import style
    assert style.LINE == "#1a1a1a"
    assert style.TP == "#2a7f2a"
    assert style.GT == "#d62828"
    assert style.FP == "#d6a228"
    assert style.SUPPRESSED == "#888888"


def test_style_apply_runs_without_error():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from anomaly.viz import style
    style.apply()
    assert plt.rcParams["font.family"] == ["DejaVu Sans"]


def test_type_friendly_known():
    from anomaly.viz.style import type_friendly
    assert type_friendly("level_shift") == "level shift"
    assert type_friendly("water_leak_sustained") == "sustained water leak"
    assert type_friendly("trend") == "gradual drift"


def test_type_friendly_fallback():
    from anomaly.viz.style import type_friendly
    assert type_friendly("brand_new_type") == "brand new type"
    assert type_friendly("") == ""


def test_sensor_friendly_outlet():
    from anomaly.viz.style import sensor_friendly
    assert sensor_friendly("outlet_tv_power") == "TV outlet"
    assert sensor_friendly("outlet_kettle_power") == "Kettle outlet"
    assert sensor_friendly("outlet_fridge_power") == "Fridge outlet"


def test_sensor_friendly_other_prefixes():
    from anomaly.viz.style import sensor_friendly
    assert sensor_friendly("mains_voltage") == "Mains voltage"
    assert sensor_friendly("basement_leak") == "Basement leak sensor"
    assert sensor_friendly("kitchen_temperature") == "Kitchen temperature"


def test_sensor_friendly_override():
    from anomaly.viz.style import sensor_friendly
    overrides = {"outlet_tv_power": "Living-room TV"}
    assert sensor_friendly("outlet_tv_power", overrides) == "Living-room TV"
    # Unrelated sensor falls through to auto-derive
    assert sensor_friendly("outlet_kettle_power", overrides) == "Kettle outlet"


def test_sensor_friendly_unknown_pattern():
    from anomaly.viz.style import sensor_friendly
    # Unknown shape — title-case fallback
    assert sensor_friendly("weird_id_thing") == "Weird id thing"


def test_sensor_friendly_humidity_lowercase():
    """Non-outlet placement with trailing measurement word should lowercase
    the measurement (capability words like humidity / pressure are nouns,
    not appliances)."""
    from anomaly.viz.style import sensor_friendly
    assert sensor_friendly("bathroom_humidity") == "Bathroom humidity sensor"


def test_sensor_friendly_uppercase_input_fallback():
    """Fallback branch should sentence-case the output regardless of input case."""
    from anomaly.viz.style import sensor_friendly
    assert sensor_friendly("WEIRD_ID_THING") == "Weird id thing"
    assert sensor_friendly("Mixed_Case_Input") == "Mixed case input"


def test_render_summary_level_shift_up():
    from anomaly.viz.style import render_summary
    s = render_summary(
        anomaly_type="level_shift",
        sensor_friendly_name="Kettle outlet",
        is_missed=False,
        delta=120.0,
        duration_h=24.0,
        hour_str="02:00",
    )
    assert "Kettle outlet baseline shifted upward" in s
    assert "level shift" in s


def test_render_summary_level_shift_down():
    from anomaly.viz.style import render_summary
    s = render_summary(
        anomaly_type="level_shift", sensor_friendly_name="Kettle outlet",
        is_missed=False, delta=-120.0, duration_h=24.0, hour_str=None,
    )
    assert "downward" in s


def test_render_summary_water_leak_honest():
    from anomaly.viz.style import render_summary
    s = render_summary(
        anomaly_type="water_leak_sustained",
        sensor_friendly_name="Basement leak sensor",
        is_missed=False, delta=None, duration_h=4.0, hour_str=None,
    )
    # Honest template — does NOT claim observed duration
    assert "began reporting flow" in s
    assert "sustained leak based on sensor type" in s
    assert "four hours" not in s.lower()
    assert "4 hours" not in s


def test_render_summary_missed():
    from anomaly.viz.style import render_summary
    s = render_summary(
        anomaly_type="unusual_occupancy",
        sensor_friendly_name="Bedroom motion sensor",
        is_missed=True, delta=None, duration_h=1.0, hour_str=None,
    )
    assert "did not detect" in s
    assert "Bedroom motion sensor" in s
    assert "unusual occupancy" in s


def test_render_summary_unknown_type_fallback():
    from anomaly.viz.style import render_summary
    s = render_summary(
        anomaly_type="brand_new_type",
        sensor_friendly_name="Some sensor",
        is_missed=False, delta=None, duration_h=1.0, hour_str=None,
    )
    assert "Some sensor" in s
    assert "brand new type" in s


def test_format_duration_short():
    from anomaly.viz.style import format_duration
    assert format_duration(45.0) == "45s"
    assert format_duration(60.0) == "1 minute"
    assert format_duration(120.0) == "2 minutes"


def test_format_duration_hours():
    from anomaly.viz.style import format_duration
    assert format_duration(3600.0) == "1 hour"
    assert format_duration(7200.0) == "2 hours"
    assert format_duration(3600.0 * 4) == "4 hours"


def test_format_duration_days():
    from anomaly.viz.style import format_duration
    assert format_duration(86400.0) == "1 day"
    assert format_duration(86400.0 * 2) == "2 days"
    assert format_duration(86400.0 * 23) == "23 days"


def test_format_date_range_multiday():
    from anomaly.viz.style import format_date_range
    from conftest import ts
    s = format_date_range(ts("2026-02-16T00:00:00"), ts("2026-02-18T00:00:00"))
    assert "Monday Feb 16" in s
    assert "Wednesday Feb 18, 2026" in s
    assert "48 hours" in s


def test_format_date_range_intraday():
    from anomaly.viz.style import format_date_range
    from conftest import ts
    s = format_date_range(ts("2026-04-03T14:00:00"), ts("2026-04-03T18:00:00"))
    assert "Friday Apr 3, 2026" in s
    assert "14:00" in s and "18:00" in s
    assert "4 hours" in s


def test_format_eyebrow():
    from anomaly.viz.style import format_eyebrow
    from conftest import ts
    s = format_eyebrow(ts("2026-02-15"), ts("2026-06-15"), "household_120d")
    assert "120 DAYS" in s
    assert "HOUSEHOLD" in s


def test_context_build_basic_fields():
    from anomaly.viz.context import Context
    from conftest import _minimal_viz_scenario
    events, labels, detections = _minimal_viz_scenario()
    ctx = Context.build(events, labels, detections,
                        sensor_names={}, excluded_sensors=frozenset(),
                        title=None)
    assert ctx.n_total_labels == 2
    assert ctx.n_tp == 1
    assert ctx.n_fn == 1
    assert ctx.n_user_visible_fps == 1
    assert ctx.n_suppressed == 1
    assert "outlet_tv_power" in ctx.sensor_friendly
    assert ctx.sensor_friendly["outlet_tv_power"] == "TV outlet"
    assert "outlet_tv_power" in ctx.events  # grouped by sensor


def test_context_build_excluded_sensors():
    from anomaly.viz.context import Context
    from conftest import _minimal_viz_scenario
    events, labels, detections = _minimal_viz_scenario()
    ctx = Context.build(events, labels, detections,
                        sensor_names={}, excluded_sensors=frozenset({"bedroom_motion"}),
                        title=None)
    # Motion label dropped -> no FN
    assert ctx.n_fn == 0
    assert ctx.n_total_labels == 1
    assert "bedroom_motion" not in ctx.events


def test_context_best_chain_idx_valid_under_exclusion():
    """When excluded_sensors filters detections, best_chain_idx values must
    correctly index into the surviving detections (positional, not original
    sparse index from the source frame)."""
    from anomaly.viz.context import Context
    from conftest import _minimal_viz_scenario
    events, labels, detections = _minimal_viz_scenario()
    # Exclude a sensor (none in the fixture have detections, so pretend
    # we exclude bedroom_motion; what matters is reset_index runs on
    # detections regardless).
    ctx = Context.build(events, labels, detections,
                        sensor_names={}, excluded_sensors=frozenset({"bedroom_motion"}),
                        title=None)
    tp = ctx.labels[ctx.labels["is_tp"]].iloc[0]
    chain_idx = tp["best_chain_idx"]
    assert chain_idx is not None and not pd.isna(chain_idx), \
        "best_chain_idx should be set for TP labels"
    chain_idx = int(chain_idx)
    # The picked chain should be valid: indexable via .iloc and a user_visible chain
    assert 0 <= chain_idx < len(ctx.detections)
    chain = ctx.detections.iloc[chain_idx]
    assert chain["sensor_id"] == tp["sensor_id"]
