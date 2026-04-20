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


def test_classify_short_composite_positive_is_spike():
    a = _alert("cusum+multivariate_pca+sub_pca+temporal_profile", duration_sec=120,
               context=[{"detector": "cusum", "direction": "+"}])
    assert classify_type(a) == "spike"


def test_classify_short_composite_negative_is_dip():
    a = _alert("cusum+multivariate_pca+sub_pca+temporal_profile", duration_sec=120,
               context=[{"detector": "cusum", "direction": "-"}])
    assert classify_type(a) == "dip"


def test_classify_cusum_plus_pca_short_is_level_shift():
    a = _alert("cusum+sub_pca+temporal_profile", duration_sec=4*3600,
               context=[{"detector": "cusum", "direction": "+"}])
    assert classify_type(a) == "level_shift"


def test_classify_multiday_cusum_led_is_calibration_drift():
    a = _alert("cusum+sub_pca", duration_sec=2*86400,
               context=[{"detector": "cusum", "direction": "+"}])
    assert classify_type(a) == "calibration_drift"


def test_classify_multi_day_is_month_shift():
    a = _alert("cusum+sub_pca", duration_sec=8*86400,
               context=[{"detector": "cusum", "direction": "+"}])
    assert classify_type(a) == "month_shift"


def test_classify_temporal_only_weekend_is_weekend_anomaly():
    ts0 = pd.Timestamp("2026-03-07T14:00:00Z")  # Saturday
    a = Alert(sensor_id="s", capability="v", timestamp=ts0,
              detector="temporal_profile", score=1.0, threshold=0.5,
              window_start=ts0, window_end=ts0 + pd.Timedelta(minutes=15),
              context=[{"detector": "temporal_profile"}])
    assert classify_type(a) == "weekend_anomaly"


def test_classify_sub_pca_only_long_is_frequency_change():
    a = _alert("sub_pca", duration_sec=2*3600)
    assert classify_type(a) == "frequency_change"


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
    assert m["baseline_source"] == "prewindow_median"


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
    df, t_peak = _events_df(baseline=120.0, peak=124.0)
    alert = Alert(sensor_id="s", capability="v",
                  timestamp=t_peak + pd.Timedelta(minutes=5),
                  detector="cusum+sub_pca", score=1.0, threshold=0.5,
                  window_start=t_peak, window_end=t_peak + pd.Timedelta(minutes=10),
                  context=[{"detector": "cusum", "mu": 120.0, "sigma": 0.4,
                            "direction": "+"}])
    b = explain(alert, df)
    assert b["sensor"] == "s"
    assert b["inferred_type"] in ("level_shift", "statistical_anomaly",
                                   "calibration_drift", "spike")
    assert "magnitude" in b and b["magnitude"]["delta"] == 4.0
    assert "temporal" in b and b["temporal"]["hour"] == t_peak.hour + 5 // 60
    assert b["detectors"] == ["cusum", "sub_pca"]
    assert b["detector_context"][0]["detector"] == "cusum"


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
        "score": 1.0,
    }])
    ev_p = tmp_path / "events.csv"; events.to_csv(ev_p, index=False)
    det_p = tmp_path / "dets.csv";   dets.to_csv(det_p, index=False)
    out_p = tmp_path / "bundles.jsonl"
    explain_detections_csv(ev_p, det_p, out_p)
    lines = out_p.read_text().splitlines()
    assert len(lines) == 1
    bundle = json.loads(lines[0])
    assert bundle["inferred_type"] == "out_of_range"
    assert bundle["detectors"] == ["data_quality_gate"]
