import pandas as pd
import pytest
from anomaly.core import Alert
from anomaly.explain.classify import classify_type


def _alert(detector, ts="2026-03-05T10:00:00Z", duration_sec=60,
           atype=None, capability="power", context=None):
    ts0 = pd.Timestamp(ts)
    return Alert(sensor_id="s", capability=capability, timestamp=ts0,
                 detector=detector, score=1.0, threshold=0.5,
                 anomaly_type=atype,
                 window_start=ts0,
                 window_end=ts0 + pd.Timedelta(seconds=duration_sec),
                 context=context)


# --- Pre-typed passthrough (DQG / StateTransition) ---

def test_pretyped_dqg_passes_through():
    a = _alert("data_quality_gate", atype="dropout")
    assert classify_type(a) == "dropout"


def test_pretyped_state_transition_passes_through():
    a = _alert("state_transition", atype="water_leak_sustained")
    assert classify_type(a) == "water_leak_sustained"


# --- State (BINARY water/motion when not pre-typed) ---

def test_state_water_returns_water_leak_sustained():
    a = _alert("state_transition", capability="water")  # not pre-typed
    assert classify_type(a) == "water_leak_sustained"


def test_state_motion_returns_unusual_occupancy():
    a = _alert("state_transition", capability="motion")
    assert classify_type(a) == "unusual_occupancy"


# --- Continuous magnitude (RecentShift / CUSUM / BOCPD) ---

def test_magnitude_voltage_long_is_month_shift():
    a = _alert("recent_shift", duration_sec=24*3600, capability="voltage",
               context=[{"detector": "recent_shift",
                         "short_value": 230, "baseline_value": 220}])
    assert classify_type(a) == "month_shift"


def test_magnitude_voltage_short_up_is_spike():
    a = _alert("recent_shift", duration_sec=300, capability="voltage",
               context=[{"detector": "recent_shift",
                         "short_value": 240, "baseline_value": 220}])
    assert classify_type(a) == "spike"


def test_magnitude_voltage_short_down_is_dip():
    a = _alert("recent_shift", duration_sec=300, capability="voltage",
               context=[{"detector": "recent_shift",
                         "short_value": 200, "baseline_value": 220}])
    assert classify_type(a) == "dip"


def test_magnitude_temperature_short_down_is_dip():
    a = _alert("recent_shift", duration_sec=3600, capability="temperature",
               context=[{"detector": "recent_shift",
                         "short_value": 18, "baseline_value": 22}])
    assert classify_type(a) == "dip"


def test_magnitude_temperature_long_is_calibration_drift():
    a = _alert("recent_shift", duration_sec=2*86400, capability="temperature",
               context=[{"detector": "recent_shift",
                         "short_value": 25, "baseline_value": 22}])
    assert classify_type(a) == "calibration_drift"


# --- Duty cycle (BURSTY) ---

def test_duty_alone_weekday_normal_hour_is_level_shift():
    # Wednesday 10am (not weekend, not off-hours).
    # Per WORKLOAD_FINGERPRINT priors (16 level_shift vs 6 frequency_change
    # in BURSTY), level_shift is the prior winner for duty-alone weekday
    # normal-hour chains.
    a = _alert("duty_cycle_shift_6h", ts="2026-03-04T10:00:00Z",
               duration_sec=3600)
    assert classify_type(a) == "level_shift"


def test_duty_alone_off_hours_is_time_of_day():
    a = _alert("duty_cycle_shift_6h", ts="2026-03-04T03:00:00Z",
               duration_sec=3600)
    assert classify_type(a) == "time_of_day"


def test_duty_alone_weekend_is_weekend_anomaly():
    a = _alert("duty_cycle_shift_6h", ts="2026-03-07T14:00:00Z",
               duration_sec=3600)  # Saturday 2 PM
    assert classify_type(a) == "weekend_anomaly"


def test_duty_alone_long_is_degradation_trajectory():
    a = _alert("duty_cycle_shift_6h", ts="2026-03-04T10:00:00Z",
               duration_sec=10*86400)
    assert classify_type(a) == "degradation_trajectory"


def test_duty_plus_peak_is_level_shift():
    # The iter-021 critical rule: combined duty+peak chain.
    a = _alert("duty_cycle_shift_6h+rolling_median_peak_shift",
               ts="2026-03-04T10:00:00Z", duration_sec=3600)
    assert classify_type(a) == "level_shift"


def test_duty_plus_peak_short_weekend_is_weekend_anomaly():
    # 2-day duty+peak on a Saturday → weekend_anomaly takes precedence
    # over level_shift since duration is short and falls on weekend.
    a = _alert("duty_cycle_shift_6h+rolling_median_peak_shift",
               ts="2026-03-07T14:00:00Z", duration_sec=2*86400)
    assert classify_type(a) == "weekend_anomaly"


def test_duty_plus_rate_is_frequency_change():
    a = _alert("duty_cycle_shift_6h+event_rate_shift",
               ts="2026-03-04T10:00:00Z", duration_sec=3600)
    assert classify_type(a) == "frequency_change"


def test_duty_plus_peak_plus_rate_is_level_shift():
    a = _alert("duty_cycle_shift_6h+rolling_median_peak_shift+event_rate_shift",
               ts="2026-03-04T10:00:00Z", duration_sec=3600)
    assert classify_type(a) == "level_shift"


# --- Peak alone (BURSTY) ---

def test_peak_alone_default_is_trend():
    # Peak-alone singleton chains (RollingMedianPeak emits 1-min windows)
    # default to trend per WORKLOAD_FINGERPRINT priors. True spikes fire
    # DQG's extreme_value branch and are pre-typed.
    a = _alert("rolling_median_peak_shift", duration_sec=300)
    assert classify_type(a) == "trend"


def test_peak_long_is_degradation_trajectory():
    a = _alert("rolling_median_peak_shift", duration_sec=10*86400)
    assert classify_type(a) == "degradation_trajectory"


def test_peak_medium_is_trend():
    a = _alert("rolling_median_peak_shift", duration_sec=2*86400)
    assert classify_type(a) == "trend"


def test_peak_plus_rate_is_trend():
    a = _alert("rolling_median_peak_shift+event_rate_shift",
               duration_sec=3600)
    assert classify_type(a) == "trend"


# --- Rate alone (BURSTY) ---

def test_rate_alone_is_frequency_change():
    a = _alert("event_rate_shift", duration_sec=3600)
    assert classify_type(a) == "frequency_change"


# --- Calendar (TemporalProfile) ---

def test_calendar_alone_weekend_is_weekend_anomaly():
    a = _alert("temporal_profile", ts="2026-03-07T14:00:00Z",
               duration_sec=900)
    assert classify_type(a) == "weekend_anomaly"


def test_calendar_alone_off_hours_is_time_of_day():
    a = _alert("temporal_profile", ts="2026-03-04T03:00:00Z",
               duration_sec=900)
    assert classify_type(a) == "time_of_day"


def test_calendar_alone_default_is_temporal_pattern():
    a = _alert("temporal_profile", ts="2026-03-04T10:00:00Z",
               duration_sec=900)
    assert classify_type(a) == "temporal_pattern"


# --- Fallthrough ---

def test_unknown_detector_returns_statistical_anomaly():
    a = _alert("brand_new_detector_xyz", duration_sec=3600)
    assert classify_type(a) == "statistical_anomaly"


# --- Phase B: classify(alert) returning ClassificationResult ---

from anomaly.explain.classify import classify, ClassificationResult


def test_classify_returns_result_with_type_and_confidence():
    a = _alert("duty_cycle_shift_6h+rolling_median_peak_shift",
               ts="2026-03-04T10:00:00Z", duration_sec=3600)
    r = classify(a)
    assert isinstance(r, ClassificationResult)
    assert r.type == "level_shift"
    assert r.confidence == "high"
    assert r.signal_classes == ["duty", "peak"]


def test_classify_low_confidence_for_statistical_anomaly():
    a = _alert("brand_new_detector_xyz", duration_sec=3600)
    r = classify(a)
    assert r.type == "statistical_anomaly"
    assert r.confidence == "low"
    assert r.signal_classes == []


def test_classify_high_confidence_for_specific_signal_class():
    # Peak-alone defaults to trend per WORKLOAD_FINGERPRINT priors
    # (see test_peak_alone_default_is_trend). The point of this test
    # is that a recognized signal class yields confidence="high" with
    # the corresponding class surfaced in signal_classes.
    a = _alert("rolling_median_peak_shift", duration_sec=300)
    r = classify(a)
    assert r.type == "trend"
    assert r.confidence == "high"
    assert r.signal_classes == ["peak"]


def test_classify_type_still_returns_string():
    a = _alert("duty_cycle_shift_6h+rolling_median_peak_shift",
               ts="2026-03-04T10:00:00Z", duration_sec=3600)
    assert classify_type(a) == "level_shift"  # str-returning facade
