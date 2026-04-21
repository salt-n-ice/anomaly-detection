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
