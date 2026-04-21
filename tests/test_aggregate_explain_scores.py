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


from aggregate_explain_scores import (  # noqa: E402
    build_snapshot, diff, main,
)


def _scores_file(path: Path, rows: list[dict]) -> None:
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n")


def _cases_file(path: Path, n: int) -> None:
    rows = [{"case_id": f"c#{i:03d}", "scenario": "x", "suite": "60d"}
            for i in range(n)]
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n")


def _scenario_dir(run_dir: Path, scen: str, suite: str,
                  scores: list[dict]) -> None:
    _cases_file(run_dir / f"{scen}_cases.jsonl", len(scores))
    _scores_file(run_dir / f"{scen}_scores.jsonl", scores)
    # Record suite in a tiny manifest-lookalike so the aggregator can find it.
    manifest_path = run_dir / "manifest.json"
    mani = (json.loads(manifest_path.read_text()) if manifest_path.exists()
            else {"scenarios": []})
    mani["scenarios"].append({"name": scen, "suite": suite,
                              "skipped": False, "n_cases": len(scores)})
    manifest_path.write_text(json.dumps(mani, indent=2))


def test_build_snapshot_aggregates_all_scenarios(tmp_path):
    run_dir = tmp_path / "run_ts"; run_dir.mkdir()
    _scenario_dir(run_dir, "a_60d", "60d", [
        _tp_score({"type_identifiability": 5, "magnitude_fidelity": 5,
                   "temporal_fidelity": 5, "detector_evidence_usefulness": 5,
                   "no_misleading_content": 5}),
    ])
    _scenario_dir(run_dir, "b_120d", "120d", [
        _tp_score({"type_identifiability": 3, "magnitude_fidelity": 3,
                   "temporal_fidelity": 3, "detector_evidence_usefulness": 3,
                   "no_misleading_content": 3}),
        _fp_score({"self_weakness_signal": 4, "evidence_coherence": 4,
                   "no_false_confidence": 4}),
    ])
    snap = build_snapshot(run_dir)
    assert snap["aggregate"]["all"]["n"] == 2
    assert snap["aggregate"]["60d"]["mean_tp_mean"] == 5.0
    assert snap["aggregate"]["120d"]["mean_tp_mean"] == 3.0
    assert snap["aggregate"]["120d"]["mean_fp_mean"] == 4.0
    assert snap["missing_scores"] == []


def test_build_snapshot_lists_missing_scores(tmp_path):
    run_dir = tmp_path / "run_ts"; run_dir.mkdir()
    _cases_file(run_dir / "ghost_60d_cases.jsonl", 3)
    mani = {"scenarios": [{"name": "ghost_60d", "suite": "60d",
                           "skipped": False, "n_cases": 3}]}
    (run_dir / "manifest.json").write_text(json.dumps(mani))
    snap = build_snapshot(run_dir)
    assert "ghost_60d" in snap["missing_scores"]
    assert snap["aggregate"]["all"]["n"] == 0


def test_diff_flags_regression_over_tol():
    old = {"scenarios": [{
        "name": "a_60d", "suite": "60d",
        "tp_mean": 4.0, "fp_mean": 3.0,
        "dim_tp_means": {d: 4.0 for d in [
            "type_identifiability", "magnitude_fidelity",
            "temporal_fidelity", "detector_evidence_usefulness",
            "no_misleading_content"]},
        "dim_fp_means": {d: 3.0 for d in [
            "self_weakness_signal", "evidence_coherence",
            "no_false_confidence"]},
    }], "aggregate": {"all": {"mean_tp_mean": 4.0, "mean_fp_mean": 3.0}}}
    new = {"scenarios": [{
        "name": "a_60d", "suite": "60d",
        "tp_mean": 3.5, "fp_mean": 3.0,
        "dim_tp_means": {**old["scenarios"][0]["dim_tp_means"],
                          "type_identifiability": 3.5},
        "dim_fp_means": dict(old["scenarios"][0]["dim_fp_means"]),
    }], "aggregate": {"all": {"mean_tp_mean": 3.5, "mean_fp_mean": 3.0}}}
    d = diff(old, new, tol=0.2)
    assert any(r["name"] == "a_60d" for r in d["regressions"])


def test_diff_ignores_drop_within_tol():
    old = {"scenarios": [{
        "name": "a_60d", "suite": "60d",
        "tp_mean": 4.0, "fp_mean": 3.0,
        "dim_tp_means": {d: 4.0 for d in [
            "type_identifiability", "magnitude_fidelity",
            "temporal_fidelity", "detector_evidence_usefulness",
            "no_misleading_content"]},
        "dim_fp_means": {d: 3.0 for d in [
            "self_weakness_signal", "evidence_coherence",
            "no_false_confidence"]},
    }], "aggregate": {"all": {"mean_tp_mean": 4.0, "mean_fp_mean": 3.0}}}
    new = {"scenarios": [{
        "name": "a_60d", "suite": "60d",
        "tp_mean": 3.9, "fp_mean": 3.0,
        "dim_tp_means": dict(old["scenarios"][0]["dim_tp_means"]),
        "dim_fp_means": dict(old["scenarios"][0]["dim_fp_means"]),
    }], "aggregate": {"all": {"mean_tp_mean": 3.9, "mean_fp_mean": 3.0}}}
    d = diff(old, new, tol=0.2)
    assert d["regressions"] == []


def test_main_writes_summary_and_latest(tmp_path, monkeypatch):
    import aggregate_explain_scores as mod
    run_dir = tmp_path / "run_ts"; run_dir.mkdir()
    _scenario_dir(run_dir, "a_60d", "60d", [
        _tp_score({"type_identifiability": 5, "magnitude_fidelity": 5,
                   "temporal_fidelity": 5, "detector_evidence_usefulness": 5,
                   "no_misleading_content": 5}),
    ])
    monkeypatch.setattr(mod, "RUNS", tmp_path)
    (tmp_path / "latest.txt").write_text("run_ts")
    rc = main(["--run", "latest"])
    assert rc == 0
    assert (run_dir / "summary.json").exists()
    assert (tmp_path / "latest.json").exists()
