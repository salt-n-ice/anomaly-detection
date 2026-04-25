import pandas as pd
from anomaly.core import Alert
from anomaly.explain import classify_type


def _alert(detector, duration_sec=60, atype=None, context=None):
    ts0 = pd.Timestamp("2026-03-05T10:00:00Z")
    return Alert(sensor_id="s", capability="v", timestamp=ts0,
                 detector=detector, score=1.0, threshold=0.5,
                 anomaly_type=atype,
                 window_start=ts0, window_end=ts0 + pd.Timedelta(seconds=duration_sec),
                 context=context)


def test_classify_passthrough_when_dqg_already_typed():
    a = _alert("data_quality_gate", atype="out_of_range")
    assert classify_type(a) == "out_of_range"


# Classifier tests live in tests/test_explain_classify.py — the signal-driven
# dispatch covers the iter 021 pipeline vocabulary. Legacy CUSUM/SubPCA/MvPCA
# combos are no longer in BURSTY/CONT.medium and are not classified directly
# (they fall to statistical_anomaly).


def test_classify_state_transition_is_water_leak_sustained():
    a = _alert("state_transition", atype="water_leak_sustained")
    assert classify_type(a) == "water_leak_sustained"


from anomaly.explain import extract_magnitude, temporal_framing


def _events_df(baseline=120.0, peak=124.0, baseline_hours=2, peak_minutes=10):
    """Synthetic pre/during event stream for magnitude tests."""
    rows = []
    t0 = pd.Timestamp("2026-03-05T08:00:00Z")
    # 2h of baseline (10-min cadence)
    for i in range(baseline_hours * 6):
        rows.append({"timestamp": t0 + pd.Timedelta(minutes=10 * i),
                     "sensor_id": "s", "capability": "v", "value": baseline})
    # 10 minutes of peak
    t1 = t0 + pd.Timedelta(hours=baseline_hours)
    for i in range(peak_minutes):
        rows.append({"timestamp": t1 + pd.Timedelta(minutes=i),
                     "sensor_id": "s", "capability": "v", "value": peak})
    df = pd.DataFrame(rows)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    return df, t1


def test_extract_magnitude_uses_cusum_mu_when_available():
    df, t_peak = _events_df(baseline=120.0, peak=124.0)
    alert = Alert(sensor_id="s", capability="v",
                  timestamp=t_peak + pd.Timedelta(minutes=5),
                  detector="cusum+sub_pca", score=1.0, threshold=0.5,
                  window_start=t_peak, window_end=t_peak + pd.Timedelta(minutes=10),
                  context=[{"detector": "cusum", "mu": 120.0, "sigma": 0.4,
                            "direction": "+"}])
    m = extract_magnitude(alert, df)
    assert m["baseline"] == 120.0
    assert m["peak"] == 124.0
    assert m["delta"] == 4.0
    assert m["baseline_source"] == "cusum_mu"


def test_extract_magnitude_falls_back_to_prewindow_median():
    df, t_peak = _events_df(baseline=10.0, peak=25.0)
    alert = Alert(sensor_id="s", capability="v",
                  timestamp=t_peak + pd.Timedelta(minutes=5),
                  detector="sub_pca", score=1.0, threshold=0.5,
                  window_start=t_peak, window_end=t_peak + pd.Timedelta(minutes=10),
                  context=None)
    m = extract_magnitude(alert, df)
    assert m["baseline"] == 10.0
    assert m["delta"] == 15.0
    assert m["baseline_source"] == "prewindow_2h"


def test_extract_magnitude_nan_baseline_when_no_prewindow():
    """Alert window at t0 with no prior events -> baseline is NaN; peak/delta
    must be NaN without raising (regression: .idxmax() on all-NaN deltas)."""
    t0 = pd.Timestamp("2026-03-05T10:00:00Z")
    df = pd.DataFrame([
        {"timestamp": t0, "sensor_id": "s",
         "capability": "v", "value": 42.0},
    ])
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    alert = Alert(sensor_id="s", capability="v", timestamp=t0,
                  detector="sub_pca", score=1.0, threshold=0.5,
                  window_start=t0, window_end=t0 + pd.Timedelta(minutes=1),
                  context=None)
    m = extract_magnitude(alert, df)
    assert m["baseline"] != m["baseline"]  # NaN
    assert m["peak"] != m["peak"]
    assert m["delta"] != m["delta"]


def test_temporal_framing_emits_calendar_fields():
    ts0 = pd.Timestamp("2026-03-07T14:00:00Z")  # Saturday afternoon
    alert = Alert(sensor_id="s", capability="v", timestamp=ts0,
                  detector="temporal_profile", score=1.0, threshold=0.5,
                  window_start=ts0, window_end=ts0 + pd.Timedelta(minutes=10))
    t = temporal_framing(alert)
    assert t["weekday"] == "Saturday"
    assert t["hour"] == 14
    assert t["is_weekend"] is True
    assert t["month"] == "March"
    assert t["time_of_day_bucket"] == "afternoon"


import json
from pathlib import Path
from anomaly.explain import explain, explain_detections_csv


def test_explain_bundle_has_expected_keys():
    import pandas as pd
    from anomaly.core import Alert
    from anomaly.explain import explain
    ts = pd.Timestamp("2026-03-05T10:00:00Z")
    a = Alert(sensor_id="s", capability="power", timestamp=ts,
              detector="duty_cycle_shift_6h+rolling_median_peak_shift",
              score=4.0, threshold=3.0,
              window_start=ts, window_end=ts + pd.Timedelta(hours=1),
              context=[{"detector": "duty_cycle_shift_6h",
                        "duty": 0.4, "bootstrap_median": 0.1,
                        "bootstrap_mad": 0.05, "z": 5.0}])
    events = pd.DataFrame({"sensor_id": ["s"], "capability": ["power"],
                            "value": [100.0],
                            "timestamp": [ts - pd.Timedelta(hours=1)]})
    events["timestamp"] = pd.to_datetime(events["timestamp"], utc=True)
    b = explain(a, events)
    # Top-level shape
    assert set(b.keys()) >= {
        "alert_id", "sensor", "capability", "archetype", "window",
        "classification", "magnitude", "temporal", "detectors",
        "detector_context", "score",
    }
    # Classification block
    c = b["classification"]
    assert set(c.keys()) == {
        "type", "class", "presentation", "confidence", "signal_classes"
    }
    assert c["type"] == "level_shift"
    assert c["class"] == "user_behavior"
    assert c["presentation"] == "user_visible"
    assert c["confidence"] == "high"
    assert sorted(c["signal_classes"]) == ["duty", "peak"]
    # No legacy flat inferred_type at top level
    assert "inferred_type" not in b


def test_explain_detections_csv_roundtrip(tmp_path: Path):
    # Build tiny events + detections CSVs, run explain_detections_csv,
    # verify the JSONL has one bundle per detection.
    events = pd.DataFrame([
        {"timestamp": "2026-03-05T08:00:00Z", "sensor_id": "s",
         "capability": "v", "value": 120.0, "unit": "V"},
        {"timestamp": "2026-03-05T10:00:00Z", "sensor_id": "s",
         "capability": "v", "value": 124.0, "unit": "V"},
    ])
    dets = pd.DataFrame([{
        "sensor_id": "s", "capability": "v",
        "start": "2026-03-05T10:00:00Z", "end": "2026-03-05T10:30:00Z",
        "anomaly_type": "out_of_range", "detector": "data_quality_gate",
        "threshold": 0.5,
        "score": 1.0,
    }])
    ev_p = tmp_path / "events.csv"; events.to_csv(ev_p, index=False)
    det_p = tmp_path / "dets.csv";   dets.to_csv(det_p, index=False)
    out_p = tmp_path / "bundles.jsonl"
    explain_detections_csv(ev_p, det_p, out_p)
    lines = out_p.read_text().splitlines()
    assert len(lines) == 1
    bundle = json.loads(lines[0])
    # Phase B: flat inferred_type replaced by classification.type.
    assert bundle["classification"]["type"] == "out_of_range"
    assert bundle["detectors"] == ["data_quality_gate"]


from anomaly.explain import build_prompt


def _sample_bundle(dur_sec=600.0, ctx=None, detectors=None):
    ws = pd.Timestamp("2026-03-05T10:00:00+00:00")
    we = ws + pd.Timedelta(seconds=dur_sec)
    return {
        "alert_id": "s|v|2026-03-05T10:00:00+00:00",
        "sensor": "s", "capability": "v",
        "archetype": "BURSTY",
        "classification": {"type": "statistical_anomaly", "class": "unknown",
                            "presentation": "user_visible",
                            "confidence": "low",
                            "signal_classes": []},
        "window": {"start": ws.isoformat(), "end": we.isoformat(),
                   "duration_sec": dur_sec},
        "magnitude": {"baseline": 120.0, "baseline_source": "cusum_mu",
                      "peak": 124.0, "delta": 4.0, "delta_pct": 3.33},
        "temporal": {"timestamp": ws.isoformat(),
                     "weekday": "Thursday", "hour": 10, "is_weekend": False,
                     "month": "March", "time_of_day_bucket": "morning"},
        "detectors": detectors if detectors is not None
                     else ["cusum", "sub_pca"],
        "detector_context": ctx if ctx is not None else [],
        "score": 3.2, "threshold": 0.5,
    }


def test_build_prompt_includes_sensor_capability_and_time():
    bundle = {
        "sensor": "outlet_kettle_power", "capability": "power",
        "archetype": "BURSTY",
        "window": {"start": "2026-03-05T10:00:00+00:00",
                   "end":   "2026-03-05T10:05:00+00:00",
                   "duration_sec": 300.0},
        "classification": {"type": "spike", "class": "user_behavior",
                            "presentation": "user_visible",
                            "confidence": "high",
                            "signal_classes": ["peak"]},
        "magnitude": {}, "temporal": {}, "detectors": ["rolling_median_peak_shift"],
        "detector_context": [], "score": 5.0,
    }
    p = build_prompt(bundle)
    assert "outlet_kettle_power" in p
    assert "power" in p
    assert "BURSTY" in p


def test_build_prompt_renders_heuristic_hint_as_advisory():
    bundle = {
        "sensor": "s", "capability": "power", "archetype": "BURSTY",
        "window": {"start": "2026-03-05T10:00:00+00:00",
                   "end":   "2026-03-05T11:00:00+00:00",
                   "duration_sec": 3600.0},
        "classification": {"type": "level_shift", "class": "user_behavior",
                            "presentation": "user_visible",
                            "confidence": "high",
                            "signal_classes": ["duty", "peak"]},
        "magnitude": {}, "temporal": {}, "detectors": [], "detector_context": [],
        "score": 7.0,
    }
    p = build_prompt(bundle)
    assert "level_shift" in p
    assert "starting point" in p.lower() or "refine" in p.lower()


def test_build_prompt_adds_long_duration_framing():
    p = build_prompt(_sample_bundle(dur_sec=4 * 86400))  # 4 days
    assert "Long-duration framing" in p
    assert "4.0 days" in p
    assert "weekend day" in p


def test_build_prompt_renders_detector_context_dicts():
    ctx = [
        {"detector": "cusum", "direction": "+", "mu": 120.0,
         "sigma": 0.4, "sp": 3.2, "sn": 0.0, "value": 124.0},
        {"detector": "sub_pca", "err": 0.15, "thr": 0.05, "feature": "x"},
    ]
    p = build_prompt(_sample_bundle(ctx=ctx))
    assert "cusum:" in p
    assert "mu=120.0" in p
    assert "direction=+" in p
    assert "sub_pca: err=0.15" in p


def test_build_prompt_falls_back_gracefully_when_context_empty():
    p = build_prompt(_sample_bundle(ctx=[]))
    assert "per-detector context dicts unavailable" in p
    assert "Detectors fired:" in p and "cusum, sub_pca" in p


def test_detections_to_alerts_strips_detector_string_fallback():
    """pipeline._write_detections writes `anomaly_type or detector` so statistical
    fused alerts land in the CSV with anomaly_type == detector. The loader must
    strip that fallback, otherwise classify_type short-circuits on rule 1 and
    returns the detector string as the inferred type."""
    from anomaly.explain import _detections_to_alerts, classify_type
    dets = pd.DataFrame([
        # Statistical fused: anomaly_type matches the detector string.
        {"sensor_id": "s", "capability": "v",
         "start": "2026-03-05T10:00:00Z", "end": "2026-03-05T12:00:00Z",
         "anomaly_type": "cusum+sub_pca", "detector": "cusum+sub_pca", "score": 1.0},
        # DQG: anomaly_type is the actual type.
        {"sensor_id": "s", "capability": "v",
         "start": "2026-03-05T14:00:00Z", "end": "2026-03-05T14:01:00Z",
         "anomaly_type": "out_of_range", "detector": "data_quality_gate", "score": 1.0},
    ])
    alerts = _detections_to_alerts(dets)
    assert alerts[0].anomaly_type is None     # detector-string fallback stripped
    assert alerts[1].anomaly_type == "out_of_range"
    # And the classifier now runs the decision tree on the statistical row.
    assert classify_type(alerts[0]) != "cusum+sub_pca"


def test_detections_to_alerts_reads_threshold_from_csv():
    """Phase B: pipeline._write_detections now writes a threshold column;
    _detections_to_alerts should round-trip it onto the Alert. Old CSVs
    without the column fall back to 0.0 (backwards-compat)."""
    from anomaly.explain import _detections_to_alerts
    # New CSV with threshold column → preserved on Alert.
    dets_with = pd.DataFrame([{
        "sensor_id": "s", "capability": "v",
        "start": "2026-03-05T10:00:00Z", "end": "2026-03-05T12:00:00Z",
        "anomaly_type": "out_of_range", "detector": "data_quality_gate",
        "threshold": 2.5, "score": 4.0,
    }])
    alerts = _detections_to_alerts(dets_with)
    assert alerts[0].threshold == 2.5
    # Old CSV without threshold column → falls back to 0.0.
    dets_without = pd.DataFrame([{
        "sensor_id": "s", "capability": "v",
        "start": "2026-03-05T10:00:00Z", "end": "2026-03-05T12:00:00Z",
        "anomaly_type": "out_of_range", "detector": "data_quality_gate",
        "score": 4.0,
    }])
    alerts = _detections_to_alerts(dets_without)
    assert alerts[0].threshold == 0.0


def test_sensor_profile_line_from_bursty_bundle():
    from anomaly.explain.prompt import _sensor_profile_line
    bundle = {
        "archetype": "BURSTY",
        "capability": "power",
        "detector_context": [
            {"detector": "duty_cycle_shift_6h",
             "bootstrap_median": 0.08, "bootstrap_mad": 0.03},
            {"detector": "rolling_median_peak_shift",
             "bootstrap_median": 1450.0, "bootstrap_mad": 30.0},
        ],
    }
    line = _sensor_profile_line(bundle)
    assert line is not None
    assert "BURSTY" in line
    assert "power" in line
    assert "1450" in line  # peak baseline rendered


def test_sensor_profile_line_returns_none_when_context_empty():
    from anomaly.explain.prompt import _sensor_profile_line
    bundle = {"archetype": "BURSTY", "capability": "power",
              "detector_context": []}
    assert _sensor_profile_line(bundle) is None


def test_presentation_banner_for_sensor_fault():
    from anomaly.explain.prompt import _presentation_banner
    bundle = {"classification": {"presentation": "infrastructure"}}
    line = _presentation_banner(bundle)
    assert line is not None
    assert "Infrastructure" in line


def test_presentation_banner_none_for_user_visible():
    from anomaly.explain.prompt import _presentation_banner
    bundle = {"classification": {"presentation": "user_visible"}}
    assert _presentation_banner(bundle) is None


def test_signal_class_narrative_duty_plus_peak():
    from anomaly.explain.prompt import _signal_class_narrative
    bundle = {"classification": {"signal_classes": ["duty", "peak"]}}
    line = _signal_class_narrative(bundle)
    assert "duty" in line.lower() or "time-in-state" in line.lower()
    assert "peak" in line.lower()


def test_signal_class_narrative_empty_for_pretyped():
    from anomaly.explain.prompt import _signal_class_narrative
    bundle = {"classification": {"signal_classes": []}}
    assert _signal_class_narrative(bundle) is None


def test_heuristic_hint_includes_type_and_confidence():
    from anomaly.explain.prompt import _heuristic_hint
    bundle = {"classification": {
        "type": "level_shift", "confidence": "high",
        "signal_classes": ["duty", "peak"],
    }}
    line = _heuristic_hint(bundle)
    assert "level_shift" in line
    assert "high" in line.lower()
    assert "starting point" in line.lower() or "refine" in line.lower()
