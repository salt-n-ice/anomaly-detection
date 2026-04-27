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


# ----------------------------- build_payload -----------------------------


@pytest.fixture
def tmp_scenario(tmp_path):
    """Write three minimal CSVs and return their paths."""
    events = pd.DataFrame({
        "timestamp": pd.to_datetime([
            "2026-02-01T00:00:00Z", "2026-02-10T00:00:00Z", "2026-02-20T00:00:00Z",
        ]),
        "sensor_id": ["kettle", "kettle", "fridge"],
        "capability": ["power", "power", "power"],
        "value": [100.0, 200.0, 50.0],
        "unit": ["W", "W", "W"],
    })
    labels = pd.DataFrame([
        _label("kettle", "2026-02-05", "2026-02-08", "level_shift"),
    ])
    detections = pd.DataFrame([
        # TP on kettle
        {**_chain("kettle", "2026-02-06", "2026-02-06T01:00", "level_shift"),
         "anomaly_type": "duty_cycle_shift_6h", "inferred_class": "user_behavior",
         "detector": "duty_cycle_shift_6h", "threshold": 3.0, "fire_ticks": ""},
        # FP on fridge
        {**_chain("fridge", "2026-02-15", "2026-02-15T01:00", "trend"),
         "anomaly_type": "duty_cycle_shift_6h", "inferred_class": "user_behavior",
         "detector": "cusum", "threshold": 3.0, "fire_ticks": ""},
    ])
    e = tmp_path / "events.csv"; events.to_csv(e, index=False)
    l = tmp_path / "labels.csv"; labels.to_csv(l, index=False)
    d = tmp_path / "detections.csv"; detections.to_csv(d, index=False)
    return e, l, d


def test_payload_top_level_keys(tmp_scenario):
    e, l, d = tmp_scenario
    p = rd.build_payload(e, l, d, "test_scenario", 60)
    assert set(p.keys()) >= {"scenario", "duration_sec", "timeline_start_ms",
                              "timeline_end_ms", "sensors", "labels", "chains"}
    assert p["scenario"] == "test_scenario"
    assert p["duration_sec"] == 60


def test_payload_timeline_bounds_from_events(tmp_scenario):
    e, l, d = tmp_scenario
    p = rd.build_payload(e, l, d, "test_scenario", 60)
    # 2026-02-01T00:00:00Z = 1769904000000 ms
    assert p["timeline_start_ms"] == 1769904000000
    # 2026-02-20T00:00:00Z = 1771545600000 ms
    assert p["timeline_end_ms"]   == 1771545600000


def test_payload_sensors_ordered_by_chain_count_desc(tmp_scenario):
    e, l, d = tmp_scenario
    p = rd.build_payload(e, l, d, "test_scenario", 60)
    # Both sensors have 1 chain each; alphabetical tiebreak -> fridge before kettle
    assert [s["id"] for s in p["sensors"]] == ["fridge", "kettle"]
    assert all("chain_count" in s for s in p["sensors"])


def test_payload_sensors_excludes_zero_chain_sensors(tmp_path):
    # Three sensors in events, only one has a chain
    events = pd.DataFrame({
        "timestamp": pd.to_datetime(["2026-02-01T00:00:00Z", "2026-02-02T00:00:00Z", "2026-02-03T00:00:00Z"]),
        "sensor_id": ["a", "b", "c"], "capability": ["power"]*3,
        "value": [1.0, 2.0, 3.0], "unit": ["W"]*3,
    })
    labels = pd.DataFrame(columns=["sensor_id", "capability", "start", "end",
                                    "anomaly_type", "label_class", "detector_hint", "params_json"])
    detections = pd.DataFrame([
        {**_chain("b", "2026-02-02", "2026-02-02T01:00", "level_shift"),
         "anomaly_type": "x", "inferred_class": "user_behavior",
         "detector": "x", "threshold": 1.0, "fire_ticks": ""},
    ])
    e = tmp_path / "events.csv"; events.to_csv(e, index=False)
    l = tmp_path / "labels.csv"; labels.to_csv(l, index=False)
    d = tmp_path / "detections.csv"; detections.to_csv(d, index=False)
    p = rd.build_payload(e, l, d, "x", 60)
    assert [s["id"] for s in p["sensors"]] == ["b"]


def test_payload_chains_have_classification_and_fire_ts_ms(tmp_scenario):
    e, l, d = tmp_scenario
    p = rd.build_payload(e, l, d, "test_scenario", 60)
    chains = sorted(p["chains"], key=lambda c: c["fire_ts_ms"])
    assert chains[0]["sensor_id"] == "kettle"
    assert chains[0]["classification"] == "tp"
    assert chains[0]["inferred_type"] == "level_shift"
    assert chains[1]["classification"] == "fp"
    assert all(isinstance(c["fire_ts_ms"], int) for c in chains)
    assert all("score" in c for c in chains)


def test_payload_labels_have_ms_bounds_per_sensor(tmp_scenario):
    e, l, d = tmp_scenario
    p = rd.build_payload(e, l, d, "test_scenario", 60)
    assert len(p["labels"]) == 1
    lbl = p["labels"][0]
    assert lbl["sensor_id"] == "kettle"
    assert lbl["anomaly_type"] == "level_shift"
    assert lbl["start_ms"] < lbl["end_ms"]
