"""Explain-quality research harness — case generator.

Produces per-scenario <scenario>_cases.jsonl + <scenario>_prompts.md under
research/explain/runs/<timestamp>/. Each case bundles the explainer output,
the rendered prompt, and the overlapping ground-truth labels. A Claude-in-
session judge then reads cases.jsonl and writes <scenario>_scores.jsonl
(see docs/superpowers/specs/2026-04-21-explain-eval-design.md).

Usage
-----
    python research/explain/run_explain_eval.py --suite all
    python research/explain/run_explain_eval.py --suite 60d
"""
from __future__ import annotations
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "research"))

import pandas as pd  # noqa: E402

from anomaly.explain import explain_detections_csv, build_prompt  # noqa: E402
from run_research_eval import SCENARIOS, GEN, git_hash, git_dirty  # noqa: E402


RUNS = ROOT / "research" / "explain" / "runs"
OUT = ROOT / "out"


def compute_overlap(bundle: dict, labels: pd.DataFrame) -> list[dict]:
    """Return the subset of `labels` overlapping `bundle` by sensor+cap+time.

    `labels` must have columns sensor_id, capability, start, end,
    anomaly_type, and optionally detector_hint / params_json. start / end
    must already be parsed to UTC-aware pd.Timestamp.
    """
    if len(labels) == 0:
        return []
    ws = pd.Timestamp(bundle["window"]["start"])
    we = pd.Timestamp(bundle["window"]["end"])
    mask = (
        (labels["sensor_id"] == bundle["sensor"])
        & (labels["capability"] == bundle["capability"])
        & (labels["start"] <= we)
        & (labels["end"] >= ws)
    )
    return labels[mask].to_dict(orient="records")
