"""Tests for research/explain/aggregate_explain_scores.py."""
from __future__ import annotations
import json
import sys
from pathlib import Path
import pytest

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "research" / "explain"))
sys.path.insert(0, str(_REPO / "research"))

from aggregate_explain_scores import (  # noqa: E402
    compute_scenario_summary, _read_jsonl, _mean,
)


def _tp_score(dims, case_id="c#001"):
    return {"case_id": case_id, "is_tp": True, "gt_types": ["spike"],
            "scores": dims, "tp_mean": sum(dims.values()) / len(dims)}


def _fp_score(dims, case_id="c#002"):
    return {"case_id": case_id, "is_tp": False, "gt_types": [],
            "scores": dims, "fp_mean": sum(dims.values()) / len(dims)}


def test_compute_scenario_summary_tp_and_fp_counts():
    scores = [
        _tp_score({"type_identifiability": 5, "magnitude_fidelity": 4,
                   "temporal_fidelity": 5, "detector_evidence_usefulness": 3,
                   "no_misleading_content": 5}),
        _fp_score({"self_weakness_signal": 2, "evidence_coherence": 4,
                   "no_false_confidence": 3}),
    ]
    s = compute_scenario_summary("scen", "60d", scores)
    assert s["n_cases"] == 2
    assert s["n_tp"] == 1
    assert s["n_fp"] == 1


def test_compute_scenario_summary_dim_means_are_correct():
    scores = [
        _tp_score({"type_identifiability": 5, "magnitude_fidelity": 3,
                   "temporal_fidelity": 5, "detector_evidence_usefulness": 4,
                   "no_misleading_content": 5}, "c#001"),
        _tp_score({"type_identifiability": 3, "magnitude_fidelity": 5,
                   "temporal_fidelity": 5, "detector_evidence_usefulness": 2,
                   "no_misleading_content": 5}, "c#002"),
    ]
    s = compute_scenario_summary("scen", "60d", scores)
    assert s["dim_tp_means"]["type_identifiability"] == 4.0
    assert s["dim_tp_means"]["magnitude_fidelity"] == 4.0
    assert s["dim_tp_means"]["detector_evidence_usefulness"] == 3.0


def test_compute_scenario_summary_tp_mean_is_mean_of_tp_means():
    scores = [
        _tp_score({"type_identifiability": 5, "magnitude_fidelity": 5,
                   "temporal_fidelity": 5, "detector_evidence_usefulness": 5,
                   "no_misleading_content": 5}, "c#001"),
        _tp_score({"type_identifiability": 3, "magnitude_fidelity": 3,
                   "temporal_fidelity": 3, "detector_evidence_usefulness": 3,
                   "no_misleading_content": 3}, "c#002"),
    ]
    s = compute_scenario_summary("scen", "60d", scores)
    assert s["tp_mean"] == 4.0  # (5 + 3) / 2


def test_compute_scenario_summary_zero_tp_or_fp():
    s = compute_scenario_summary("scen", "60d", [])
    assert s["n_cases"] == 0 and s["tp_mean"] is None and s["fp_mean"] is None


def test_read_jsonl_roundtrip(tmp_path):
    p = tmp_path / "x.jsonl"
    rows = [{"a": 1}, {"b": 2}]
    p.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    assert _read_jsonl(p) == rows
