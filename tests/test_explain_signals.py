import pandas as pd
import pytest
from anomaly.core import Alert
from anomaly.explain.signals import Signals, DETECTOR_CLASSES


def _alert(detector, ts="2026-03-05T10:00:00Z", duration_sec=60,
           atype=None, capability="power", context=None):
    ts0 = pd.Timestamp(ts)
    return Alert(sensor_id="s", capability=capability, timestamp=ts0,
                 detector=detector, score=1.0, threshold=0.5,
                 anomaly_type=atype,
                 window_start=ts0,
                 window_end=ts0 + pd.Timedelta(seconds=duration_sec),
                 context=context)


def test_signals_from_alert_splits_detector_string_on_plus():
    a = _alert("duty_cycle_shift_6h+rolling_median_peak_shift")
    s = Signals.from_alert(a)
    assert s.detectors == frozenset({"duty_cycle_shift_6h",
                                     "rolling_median_peak_shift"})


def test_signals_classes_coarsens_detectors_via_table():
    a = _alert("duty_cycle_shift_6h+rolling_median_peak_shift")
    s = Signals.from_alert(a)
    assert s.classes == frozenset({"duty", "peak"})


def test_signals_classes_drops_unknown_detector_silently():
    a = _alert("duty_cycle_shift_6h+brand_new_detector_xyz")
    s = Signals.from_alert(a)
    assert s.classes == frozenset({"duty"})  # unknown dropped


def test_signals_duration_sec_from_window():
    a = _alert("data_quality_gate", duration_sec=3600)
    s = Signals.from_alert(a)
    assert s.duration_sec == pytest.approx(3600.0)


def test_signals_capability_passes_through():
    a = _alert("recent_shift", capability="voltage")
    s = Signals.from_alert(a)
    assert s.capability == "voltage"


def test_signals_direction_from_cusum_context():
    a = _alert("cusum+sub_pca",
               context=[{"detector": "cusum", "direction": "+"},
                        {"detector": "sub_pca"}])
    s = Signals.from_alert(a)
    assert s.direction == "+"


def test_signals_direction_from_recent_shift_context_short_baseline():
    a = _alert("recent_shift",
               context=[{"detector": "recent_shift",
                         "short_value": 130.0, "baseline_value": 120.0}])
    s = Signals.from_alert(a)
    assert s.direction == "+"


def test_signals_direction_none_when_no_context():
    a = _alert("recent_shift", context=None)
    s = Signals.from_alert(a)
    assert s.direction is None


def test_signals_calendar_off_hours_at_3am():
    a = _alert("duty_cycle_shift_6h", ts="2026-03-05T03:30:00Z")  # Thursday 3:30 AM
    s = Signals.from_alert(a)
    assert s.is_off_hours is True
    assert s.is_weekend is False


def test_signals_calendar_weekend_saturday_afternoon():
    a = _alert("duty_cycle_shift_6h", ts="2026-03-07T14:00:00Z")  # Saturday 2 PM
    s = Signals.from_alert(a)
    assert s.is_weekend is True
    assert s.is_off_hours is False


def test_signals_pre_typed_passes_through():
    a = _alert("data_quality_gate", atype="dropout")
    s = Signals.from_alert(a)
    assert s.pre_typed == "dropout"


def test_signals_detector_classes_table_covers_pipeline_detectors():
    # Every detector currently registered in src/anomaly/profiles.py must be
    # in the DETECTOR_CLASSES table or the dispatch falls through silently.
    assert "data_quality_gate" in DETECTOR_CLASSES
    assert "state_transition" in DETECTOR_CLASSES
    assert "recent_shift" in DETECTOR_CLASSES
    assert "duty_cycle_shift_6h" in DETECTOR_CLASSES
    assert "rolling_median_peak_shift" in DETECTOR_CLASSES


def test_signals_archetype_inferred_from_capability_water():
    a = _alert("state_transition", capability="water")
    s = Signals.from_alert(a)
    assert s.archetype == "BINARY"


def test_signals_archetype_inferred_from_capability_voltage():
    a = _alert("recent_shift", capability="voltage")
    s = Signals.from_alert(a)
    assert s.archetype == "CONTINUOUS"


def test_signals_archetype_inferred_from_capability_temperature():
    a = _alert("recent_shift", capability="temperature")
    s = Signals.from_alert(a)
    assert s.archetype == "CONTINUOUS"


def test_signals_archetype_inferred_from_capability_power():
    a = _alert("duty_cycle_shift_6h", capability="power")
    s = Signals.from_alert(a)
    assert s.archetype == "BURSTY"
