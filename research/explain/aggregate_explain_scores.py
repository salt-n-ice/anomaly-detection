"""Explain-quality aggregator — rolls per-scenario scores into a snapshot.

Reads every <scenario>_scores.jsonl under a run directory, computes per-
scenario TP/FP means + per-dim means, builds a summary.json, and optionally
diffs against research/explain/EXPLAIN_BASELINE.json.

Usage
-----
    python research/explain/aggregate_explain_scores.py --run latest
    python research/explain/aggregate_explain_scores.py --run 20260421T170000Z \
        --diff-baseline
    python research/explain/aggregate_explain_scores.py --run latest \
        --save-baseline
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "research"))

from run_research_eval import git_hash, git_dirty  # noqa: E402

RUNS = ROOT / "research" / "explain" / "runs"
BASELINE = ROOT / "research" / "explain" / "EXPLAIN_BASELINE.json"

TP_DIMS = [
    "type_identifiability", "magnitude_fidelity", "temporal_fidelity",
    "detector_evidence_usefulness", "no_misleading_content",
]
FP_DIMS = ["self_weakness_signal", "evidence_coherence", "no_false_confidence"]


def _read_jsonl(path: Path) -> list[dict]:
    return [json.loads(ln) for ln in path.read_text(encoding="utf-8").splitlines()
            if ln.strip()]


def _mean(vals: list[float]) -> float | None:
    return round(sum(vals) / len(vals), 3) if vals else None


def compute_scenario_summary(scenario: str, suite: str,
                             scores: list[dict]) -> dict:
    """Per-scenario: n_tp, n_fp, tp_mean, fp_mean, dim_*_means."""
    tp = [s for s in scores if s["is_tp"]]
    fp = [s for s in scores if not s["is_tp"]]
    dim_tp = {d: _mean([s["scores"][d] for s in tp if d in s["scores"]])
              for d in TP_DIMS}
    dim_fp = {d: _mean([s["scores"][d] for s in fp if d in s["scores"]])
              for d in FP_DIMS}
    tp_mean = _mean([s["tp_mean"] for s in tp if "tp_mean" in s])
    fp_mean = _mean([s["fp_mean"] for s in fp if "fp_mean" in s])
    return {
        "name": scenario, "suite": suite,
        "n_cases": len(scores), "n_tp": len(tp), "n_fp": len(fp),
        "tp_mean": tp_mean, "fp_mean": fp_mean,
        "dim_tp_means": dim_tp, "dim_fp_means": dim_fp,
    }
