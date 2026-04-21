"""Tests for research/explain/run_explain_eval.py."""
from __future__ import annotations
import sys
from pathlib import Path
import pandas as pd
import pytest

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "research" / "explain"))
sys.path.insert(0, str(_REPO / "research"))

from run_explain_eval import compute_overlap  # noqa: E402


def _bundle(sensor="s1", capability="v", ws="2026-03-05T10:00:00Z",
            we="2026-03-05T10:30:00Z") -> dict:
    return {
        "sensor": sensor, "capability": capability,
        "window": {"start": ws, "end": we, "duration_sec": 1800.0},
    }


def _labels_df(rows: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    if len(df):
        df["start"] = pd.to_datetime(df["start"], utc=True)
        df["end"]   = pd.to_datetime(df["end"], utc=True)
    return df


def test_overlap_same_sensor_time_intersect_returns_match():
    labels = _labels_df([{
        "sensor_id": "s1", "capability": "v",
        "start": "2026-03-05T10:15:00Z", "end": "2026-03-05T10:45:00Z",
        "anomaly_type": "spike", "detector_hint": "pca", "params_json": "{}",
    }])
    assert len(compute_overlap(_bundle(), labels)) == 1


def test_overlap_different_sensor_returns_empty():
    labels = _labels_df([{
        "sensor_id": "s2", "capability": "v",
        "start": "2026-03-05T10:15:00Z", "end": "2026-03-05T10:45:00Z",
        "anomaly_type": "spike", "detector_hint": "pca", "params_json": "{}",
    }])
    assert compute_overlap(_bundle(sensor="s1"), labels) == []


def test_overlap_different_capability_returns_empty():
    labels = _labels_df([{
        "sensor_id": "s1", "capability": "p",
        "start": "2026-03-05T10:15:00Z", "end": "2026-03-05T10:45:00Z",
        "anomaly_type": "spike", "detector_hint": "pca", "params_json": "{}",
    }])
    assert compute_overlap(_bundle(capability="v"), labels) == []


def test_overlap_disjoint_time_returns_empty():
    labels = _labels_df([{
        "sensor_id": "s1", "capability": "v",
        "start": "2026-03-05T11:00:00Z", "end": "2026-03-05T11:30:00Z",
        "anomaly_type": "spike", "detector_hint": "pca", "params_json": "{}",
    }])
    assert compute_overlap(_bundle(), labels) == []


def test_overlap_multiple_labels_all_included():
    labels = _labels_df([
        {"sensor_id": "s1", "capability": "v",
         "start": "2026-03-05T10:05:00Z", "end": "2026-03-05T10:10:00Z",
         "anomaly_type": "spike", "detector_hint": "pca", "params_json": "{}"},
        {"sensor_id": "s1", "capability": "v",
         "start": "2026-03-05T10:20:00Z", "end": "2026-03-05T10:25:00Z",
         "anomaly_type": "dip",   "detector_hint": "pca", "params_json": "{}"},
    ])
    assert len(compute_overlap(_bundle(), labels)) == 2


def test_overlap_empty_labels_returns_empty():
    assert compute_overlap(_bundle(), _labels_df([])) == []


from run_explain_eval import build_cases, _serialize_labels  # noqa: E402


def test_serialize_labels_converts_timestamps_to_iso():
    labels_in = [{
        "sensor_id": "s1", "capability": "v",
        "start": pd.Timestamp("2026-03-05T10:00:00Z"),
        "end":   pd.Timestamp("2026-03-05T10:30:00Z"),
        "anomaly_type": "spike", "detector_hint": "pca",
        "params_json": "{\"magnitude\": 600}",
    }]
    out = _serialize_labels(labels_in)
    assert out[0]["start"] == "2026-03-05T10:00:00+00:00"
    assert out[0]["end"]   == "2026-03-05T10:30:00+00:00"
    assert out[0]["anomaly_type"] == "spike"
    assert out[0]["detector_hint"] == "pca"


def test_serialize_labels_missing_optional_fields_defaults_none():
    labels_in = [{
        "sensor_id": "s1", "capability": "v",
        "start": pd.Timestamp("2026-03-05T10:00:00Z"),
        "end":   pd.Timestamp("2026-03-05T10:30:00Z"),
        "anomaly_type": "spike",
    }]
    out = _serialize_labels(labels_in)
    assert out[0]["detector_hint"] is None
    assert out[0]["params_json"] is None


def _bundles_two() -> list[dict]:
    return [
        {**_bundle(sensor="s1"),
         "detectors": ["cusum"], "inferred_type": "spike"},
        {**_bundle(sensor="s2", ws="2026-03-05T12:00:00Z",
                   we="2026-03-05T12:30:00Z"),
         "detectors": ["sub_pca"], "inferred_type": "frequency_change"},
    ]


def test_build_cases_tags_tp_when_overlap_exists():
    labels = _labels_df([{
        "sensor_id": "s1", "capability": "v",
        "start": "2026-03-05T10:15:00Z", "end": "2026-03-05T10:20:00Z",
        "anomaly_type": "spike", "detector_hint": "pca", "params_json": "{}",
    }])
    cases = build_cases("outlet_60d", "60d", _bundles_two(), labels)
    assert len(cases) == 2
    assert cases[0]["is_tp"] is True
    assert cases[0]["gt_labels"][0]["anomaly_type"] == "spike"
    assert cases[1]["is_tp"] is False
    assert cases[1]["gt_labels"] == []


def test_build_cases_case_ids_zero_padded():
    cases = build_cases("outlet_60d", "60d", _bundles_two(), _labels_df([]))
    assert cases[0]["case_id"] == "outlet_60d#000"
    assert cases[1]["case_id"] == "outlet_60d#001"


def test_build_cases_includes_prompt_and_scenario_metadata():
    cases = build_cases("outlet_60d", "60d", _bundles_two(), _labels_df([]))
    assert cases[0]["scenario"] == "outlet_60d"
    assert cases[0]["suite"] == "60d"
    assert isinstance(cases[0]["prompt"], str)
    assert "sensor s1" in cases[0]["prompt"]


from run_explain_eval import _render_prompts_md  # noqa: E402


def test_prompts_md_header_includes_scenario_and_ts():
    cases = build_cases("outlet_60d", "60d", _bundles_two(), _labels_df([]))
    md = _render_prompts_md("outlet_60d", "20260421T170000Z", cases)
    assert "# outlet_60d" in md
    assert "20260421T170000Z" in md


def test_prompts_md_tags_tp_and_fp_per_case():
    labels = _labels_df([{
        "sensor_id": "s1", "capability": "v",
        "start": "2026-03-05T10:15:00Z", "end": "2026-03-05T10:20:00Z",
        "anomaly_type": "spike", "detector_hint": "pca", "params_json": "{}",
    }])
    cases = build_cases("outlet_60d", "60d", _bundles_two(), labels)
    md = _render_prompts_md("outlet_60d", "ts", cases)
    assert "—  TP  —  GT: spike" in md
    assert "—  FP  —  GT: (none)" in md


def test_prompts_md_multiple_gt_labels_joined_by_comma():
    labels = _labels_df([
        {"sensor_id": "s1", "capability": "v",
         "start": "2026-03-05T10:05:00Z", "end": "2026-03-05T10:10:00Z",
         "anomaly_type": "spike", "detector_hint": "pca", "params_json": "{}"},
        {"sensor_id": "s1", "capability": "v",
         "start": "2026-03-05T10:20:00Z", "end": "2026-03-05T10:25:00Z",
         "anomaly_type": "dip", "detector_hint": "pca", "params_json": "{}"},
    ])
    cases = build_cases("outlet_60d", "60d", _bundles_two()[:1], labels)
    md = _render_prompts_md("outlet_60d", "ts", cases)
    assert "GT: spike, dip" in md
