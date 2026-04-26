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


def test_classify_labels_marks_tp_fn():
    from anomaly.viz import selection
    from conftest import _minimal_viz_scenario
    events, labels, detections = _minimal_viz_scenario()
    labels["start"] = pd.to_datetime(labels["start"], utc=True)
    labels["end"] = pd.to_datetime(labels["end"], utc=True)
    detections["start"] = pd.to_datetime(detections["start"], utc=True)
    detections["end"] = pd.to_datetime(detections["end"], utc=True)
    out = selection.classify_labels(labels, detections)
    tp_rows = out[out["is_tp"]]
    fn_rows = out[~out["is_tp"]]
    assert set(tp_rows["sensor_id"]) == {"outlet_tv_power"}
    assert set(fn_rows["sensor_id"]) == {"bedroom_motion"}


def test_attach_best_chain_picks_user_visible():
    from anomaly.viz import selection
    from conftest import _minimal_viz_scenario
    events, labels, detections = _minimal_viz_scenario()
    labels["start"] = pd.to_datetime(labels["start"], utc=True)
    labels["end"] = pd.to_datetime(labels["end"], utc=True)
    detections["start"] = pd.to_datetime(detections["start"], utc=True)
    detections["end"] = pd.to_datetime(detections["end"], utc=True)
    labels = selection.classify_labels(labels, detections)
    labels = selection.attach_best_chain(labels, detections)
    tp = labels[labels["is_tp"]].iloc[0]
    assert tp["best_chain_idx"] is not None and tp["best_chain_idx"] >= 0
    # The picked chain should be the user-visible one (TV outlet TP)
    assert detections.iloc[int(tp["best_chain_idx"])]["inferred_class"] == "user_behavior"


def test_compute_buckets():
    from anomaly.viz import selection
    from conftest import _minimal_viz_scenario
    events, labels, detections = _minimal_viz_scenario()
    labels["start"] = pd.to_datetime(labels["start"], utc=True)
    labels["end"] = pd.to_datetime(labels["end"], utc=True)
    detections["start"] = pd.to_datetime(detections["start"], utc=True)
    detections["end"] = pd.to_datetime(detections["end"], utc=True)
    labels = selection.classify_labels(labels, detections)
    n_user_fps, n_suppressed, by_sensor = selection.compute_buckets(labels, detections)
    assert n_user_fps == 1
    assert n_suppressed == 1
    assert by_sensor[0][0] == "outlet_tv_power"
    assert by_sensor[0][1] == 1


def test_select_showcases_curation():
    from anomaly.viz import selection
    import pandas as _pd
    # Construct a labels df spanning multiple types and durations
    labels = _pd.DataFrame({
        "sensor_id": ["s1", "s2", "s3", "s4", "s5"],
        "capability": ["power"]*5,
        "start": _pd.to_datetime([
            "2026-01-01", "2026-01-05", "2026-01-10",
            "2026-01-12", "2026-01-15"], utc=True),
        "end": _pd.to_datetime([
            "2026-01-08", "2026-01-06", "2026-01-30",
            "2026-01-13", "2026-01-16"], utc=True),
        "anomaly_type": ["level_shift", "level_shift", "trend",
                         "weekend_anomaly", "weekend_anomaly"],
        "is_tp": [True, True, True, True, True],
        "best_chain_idx": [0, 1, 2, 3, 4],
    })
    picked = selection.select_showcases(labels, max_n=8)
    # One per type: longest level_shift (s1, 7d), longest trend (s3, 20d),
    # longest weekend_anomaly (s4, 1d).
    assert len(picked) == 3
    types = [r["anomaly_type"] for _, r in picked.iterrows()]
    assert set(types) == {"level_shift", "trend", "weekend_anomaly"}


def test_attach_best_chain_defensive_against_sparse_index():
    """Direct callers may pass a filtered (sparse-index) detections frame.
    attach_best_chain should still produce positional best_chain_idx values
    that are valid for .iloc indexing on the (also-resetted) detections."""
    from anomaly.viz import selection
    import pandas as _pd
    labels = _pd.DataFrame({
        "sensor_id": ["s1"],
        "start": _pd.to_datetime(["2026-01-01T00:00:00Z"]),
        "end":   _pd.to_datetime(["2026-01-02T00:00:00Z"]),
        "anomaly_type": ["level_shift"],
        "is_tp": [True],
    })
    # Simulate a filter result: original index has gaps [10, 20, 30]
    full = _pd.DataFrame({
        "sensor_id": ["x", "s1", "y", "s1", "z", "s1"],
        "start": _pd.to_datetime([
            "2026-01-01", "2026-01-01T01:00:00", "2026-01-01",
            "2026-01-01T12:00:00", "2026-01-01", "2026-01-01T23:00:00"],
            utc=True, format="mixed"),
        "end":   _pd.to_datetime([
            "2026-01-01T01:00:00", "2026-01-01T01:01:00", "2026-01-01T01:00:00",
            "2026-01-01T12:01:00", "2026-01-01T01:00:00", "2026-01-01T23:01:00"],
            utc=True, format="mixed"),
        "inferred_class": ["sensor_fault","user_behavior","sensor_fault",
                           "user_behavior","sensor_fault","user_behavior"],
        "score": [1.0, 5.0, 1.0, 9.0, 1.0, 3.0],
    })
    detections_sparse = full[full["sensor_id"] == "s1"]
    # Confirm we have a sparse index
    assert list(detections_sparse.index) == [1, 3, 5]
    out = selection.attach_best_chain(labels, detections_sparse)
    chain_idx = int(out.iloc[0]["best_chain_idx"])
    # The picked chain must be valid against the (internally-reset) detections
    inner = detections_sparse.reset_index(drop=True)
    assert 0 <= chain_idx < len(inner)
    # The highest-score user_visible was the s1 chain at original index 3 (score 9.0)
    assert inner.iloc[chain_idx]["score"] == 9.0


def test_render_cover_smoke():
    from anomaly.viz import cover
    from anomaly.viz.context import Context
    from conftest import _minimal_viz_scenario, _render_one_page_to_text
    events, labels, detections = _minimal_viz_scenario()
    ctx = Context.build(events, labels, detections,
                        sensor_names={}, excluded_sensors=frozenset(),
                        title="test scenario")
    text = _render_one_page_to_text(cover.render_cover, ctx)
    # Hero metric
    assert "1" in text and "of 2" in text
    # Friendly cover narrative
    assert "anomalies caught" in text.lower() or "caught" in text.lower()
    # Eyebrow
    assert "DAYS" in text
    # Suppression footer
    assert "suppressed" in text.lower() or "filtered" in text.lower() or "noise" in text.lower()


def test_render_cover_zero_tp_uses_red_hero():
    """Spec §13: zero-TP scenarios render the hero metric in red, not the
    default text color."""
    from anomaly.viz import cover, style
    from anomaly.viz.context import Context
    from conftest import _minimal_viz_scenario
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    events, labels, detections = _minimal_viz_scenario()
    # Force zero TPs by passing detections with no chains overlapping any GT
    empty_dets = detections.iloc[0:0].copy()
    ctx = Context.build(events, labels, empty_dets,
                        sensor_names={}, excluded_sensors=frozenset(),
                        title=None)
    assert ctx.n_tp == 0  # sanity

    fig = plt.figure(figsize=(13, 7))
    cover.render_cover(fig, ctx)
    # The hero "0" text should be the GT (red) color, not TEXT (dark grey).
    # Walk the figure's text artists to find the largest fontsize text and
    # check its color.
    texts = [t for t in fig.findobj(match=lambda o: hasattr(o, "get_fontsize") and hasattr(o, "get_color"))]
    # Filter to figure-level texts (not axes ticks): largest fontsize and text == "0"
    hero = [t for t in texts if t.get_text() == "0"]
    assert hero, "expected to find a hero text artist with text '0'"
    # Find the one with fontsize >= 50 (the large hero numeral)
    big = [t for t in hero if t.get_fontsize() >= 50]
    assert big, "expected a large-fontsize '0' for the hero metric"
    color = matplotlib.colors.to_hex(big[0].get_color())
    expected = matplotlib.colors.to_hex(style.GT)
    assert color.lower() == expected.lower(), \
        f"expected hero color {expected}, got {color}"
    plt.close(fig)


def test_render_showcase_caught():
    from anomaly.viz import showcase
    from anomaly.viz.context import Context
    from conftest import _minimal_viz_scenario, _render_one_page_to_text
    events, labels, detections = _minimal_viz_scenario()
    ctx = Context.build(events, labels, detections,
                        sensor_names={}, excluded_sensors=frozenset(),
                        title=None)
    tp_label = ctx.labels[ctx.labels["is_tp"]].iloc[0]
    text = _render_one_page_to_text(showcase.render_showcase, ctx, tp_label)
    assert "CAUGHT" in text
    assert "TV outlet" in text
    assert "weekend pattern" in text.lower()
    # Honest plain-English: doesn't claim observed duration in seconds/days
    assert "weekend" in text.lower()


def test_render_showcase_missed():
    from anomaly.viz import showcase
    from anomaly.viz.context import Context
    from conftest import _minimal_viz_scenario, _render_one_page_to_text
    events, labels, detections = _minimal_viz_scenario()
    ctx = Context.build(events, labels, detections,
                        sensor_names={}, excluded_sensors=frozenset(),
                        title=None)
    fn_label = ctx.labels[~ctx.labels["is_tp"]].iloc[0]
    text = _render_one_page_to_text(showcase.render_showcase, ctx, fn_label)
    assert "MISSED" in text
    assert "Bedroom motion sensor" in text
    assert "did not detect" in text.lower()


def test_render_honest_smoke():
    from anomaly.viz import honest
    from anomaly.viz.context import Context
    from conftest import _minimal_viz_scenario, _render_one_page_to_text
    events, labels, detections = _minimal_viz_scenario()
    ctx = Context.build(events, labels, detections,
                        sensor_names={}, excluded_sensors=frozenset(),
                        title=None)
    text = _render_one_page_to_text(honest.render_honest, ctx)
    assert "MISSED" in text or "missed" in text.lower()
    assert "FALSE ALARM" in text or "false alarm" in text.lower()
    assert "Bedroom motion sensor" in text  # FN tile


def test_render_honest_fp_overflow_indicator():
    """When >6 user-visible FPs exist, render_honest must show a
    '+ N more false alarms' overflow indicator (mirrors the FN side)."""
    from anomaly.viz import honest
    from anomaly.viz.context import Context
    from conftest import _minimal_viz_scenario, _render_one_page_to_text
    import pandas as _pd
    events, labels, detections = _minimal_viz_scenario()
    # Synthesize 8 user-visible FPs on outlet_tv_power
    extra_fps = _pd.DataFrame({
        "sensor_id": ["outlet_tv_power"] * 8,
        "capability": ["power"] * 8,
        "start": _pd.to_datetime([
            "2026-02-19T01:00:00Z", "2026-02-19T02:00:00Z",
            "2026-02-19T03:00:00Z", "2026-02-19T04:00:00Z",
            "2026-02-19T05:00:00Z", "2026-02-19T06:00:00Z",
            "2026-02-19T07:00:00Z", "2026-02-19T08:00:00Z",
        ]),
        "end": _pd.to_datetime([
            "2026-02-19T01:01:00Z", "2026-02-19T02:01:00Z",
            "2026-02-19T03:01:00Z", "2026-02-19T04:01:00Z",
            "2026-02-19T05:01:00Z", "2026-02-19T06:01:00Z",
            "2026-02-19T07:01:00Z", "2026-02-19T08:01:00Z",
        ]),
        "first_fire_ts": _pd.to_datetime([
            "2026-02-19T01:01:00Z"] * 8),
        "anomaly_type": ["duty_cycle_shift_6h"] * 8,
        "inferred_type": ["level_shift"] * 8,
        "inferred_class": ["user_behavior"] * 8,
        "detector": ["duty_cycle_shift_6h"] * 8,
        "threshold": [3.0] * 8,
        "score": [3.0] * 8,
    })
    detections = _pd.concat([detections, extra_fps], ignore_index=True)
    ctx = Context.build(events, labels, detections,
                        sensor_names={}, excluded_sensors=frozenset(),
                        title=None)
    text = _render_one_page_to_text(honest.render_honest, ctx)
    # We have at least 9 user-visible FPs: 1 original + 8 extra.
    # 6 fit on page; 3+ should be reported as overflow.
    assert "more false alarms" in text.lower()
