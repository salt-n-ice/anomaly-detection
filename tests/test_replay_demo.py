"""Tests for scripts/replay_demo.py - pure-logic functions only.

The HTML render is verified manually in a browser (see plan Task 5).
"""
import sys
from pathlib import Path
import pandas as pd
import pytest

# Make scripts/ importable
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import replay_demo as rd


def _label(sensor, start, end, anomaly_type, params_json="{}"):
    return {
        "sensor_id": sensor,
        "capability": "power",
        "start": pd.Timestamp(start, tz="UTC"),
        "end":   pd.Timestamp(end, tz="UTC"),
        "anomaly_type": anomaly_type,
        "label_class": "user_behavior",
        "detector_hint": "",
        "params_json": params_json,
    }


def _chain(sensor, start, end, inferred_type):
    return {
        "sensor_id": sensor,
        "capability": "power",
        "start": pd.Timestamp(start, tz="UTC"),
        "end":   pd.Timestamp(end, tz="UTC"),
        "first_fire_ts": pd.Timestamp(start, tz="UTC"),
        "inferred_type": inferred_type,
        "score": 5.0,
    }


# ----------------------------- classify_chain -----------------------------


def test_classify_no_overlap_is_fp():
    labels = pd.DataFrame([_label("kettle", "2026-03-01", "2026-03-02", "level_shift")])
    chain = _chain("kettle", "2026-04-10", "2026-04-10T01:00", "level_shift")
    assert rd.classify_chain(chain, labels) == "fp"


def test_classify_other_sensor_overlap_is_fp():
    labels = pd.DataFrame([_label("kettle", "2026-03-01", "2026-03-05", "level_shift")])
    chain = _chain("fridge", "2026-03-02", "2026-03-03", "level_shift")
    assert rd.classify_chain(chain, labels) == "fp"


def test_classify_exact_type_match_is_tp():
    labels = pd.DataFrame([_label("kettle", "2026-03-01", "2026-03-05", "level_shift")])
    chain = _chain("kettle", "2026-03-02", "2026-03-03", "level_shift")
    assert rd.classify_chain(chain, labels) == "tp"


def test_classify_overlap_type_mismatch_is_ambiguous():
    labels = pd.DataFrame([_label("kettle", "2026-03-01", "2026-03-05", "trend")])
    chain = _chain("kettle", "2026-03-02", "2026-03-03", "level_shift")
    assert rd.classify_chain(chain, labels) == "ambiguous"


def test_classify_synonym_weekend_target_weekday_is_tp():
    """time_of_day GT with target=weekday should match weekend_anomaly verdict."""
    labels = pd.DataFrame([_label(
        "kettle", "2026-03-01", "2026-03-15", "time_of_day",
        params_json='{"target": "weekday", "magnitude": 700}',
    )])
    chain = _chain("kettle", "2026-03-05", "2026-03-06", "weekend_anomaly")
    assert rd.classify_chain(chain, labels) == "tp"


def test_classify_synonym_time_of_day_no_target_is_ambiguous():
    """time_of_day without target=weekday does NOT match weekend_anomaly."""
    labels = pd.DataFrame([_label(
        "kettle", "2026-03-01", "2026-03-15", "time_of_day",
        params_json='{"hour_start": 10, "hour_end": 12}',
    )])
    chain = _chain("kettle", "2026-03-05", "2026-03-06", "weekend_anomaly")
    assert rd.classify_chain(chain, labels) == "ambiguous"


def test_classify_synonym_month_shift_is_tp_for_level_shift():
    labels = pd.DataFrame([_label("kettle", "2026-03-01", "2026-03-30", "level_shift")])
    chain = _chain("kettle", "2026-03-15", "2026-03-16", "month_shift")
    assert rd.classify_chain(chain, labels) == "tp"


def test_classify_synonym_calibration_drift_is_tp_for_trend():
    labels = pd.DataFrame([_label("kettle", "2026-03-01", "2026-03-15", "trend")])
    chain = _chain("kettle", "2026-03-05", "2026-03-06", "calibration_drift")
    assert rd.classify_chain(chain, labels) == "tp"


def test_classify_multi_label_picks_first_match():
    """Chain overlapping multiple labels: TP if ANY label's type matches."""
    labels = pd.DataFrame([
        _label("kettle", "2026-03-01", "2026-03-10", "trend"),
        _label("kettle", "2026-03-05", "2026-03-12", "level_shift"),
    ])
    chain = _chain("kettle", "2026-03-06", "2026-03-07", "level_shift")
    assert rd.classify_chain(chain, labels) == "tp"
