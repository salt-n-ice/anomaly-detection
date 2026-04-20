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
