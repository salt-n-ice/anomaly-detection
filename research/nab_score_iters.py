"""Run NAB scoring on each scenario's current detection CSV.

For each scenario in SCENARIOS:
  - Load labels.csv and detections.csv.
  - Apply a type classifier — prefers LLM (Claude, via `llm_classifier.py`)
    when `ANTHROPIC_API_KEY` is set, falls back to the sklearn classifier
    (via `apply_type_classifier.py`) otherwise. Writes `ml_inferred_type`.
  - Compute NAB_behavior and NAB_fault.
  - Print per-scenario + aggregate summary.

Use after `run_research_eval.py` has populated out/<scen>_detections.csv
for the pipeline state you want to score.

Usage:
    python research/nab_score_iters.py
    python research/nab_score_iters.py --label "stage0" --classifier llm
    python research/nab_score_iters.py --label "stage0" --classifier sklearn
"""
from __future__ import annotations
import argparse
import os
import sys
from pathlib import Path

import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "research"))

from apply_type_classifier import apply_classifier, MODEL_PATH  # noqa: E402
from nab_metric import compute_nab  # noqa: E402
from run_research_eval import SCENARIOS, GEN, OUT  # noqa: E402


def _pick_classifier(arg_choice: str) -> str:
    """Resolve 'auto' → 'llm' if ANTHROPIC_API_KEY is set, else 'sklearn'."""
    if arg_choice != "auto":
        return arg_choice
    return "llm" if os.environ.get("ANTHROPIC_API_KEY") else "sklearn"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="run", help="tag for this NAB run")
    ap.add_argument("--classifier", choices=["auto", "llm", "sklearn"],
                     default="auto",
                     help="auto = LLM when ANTHROPIC_API_KEY is set, else sklearn")
    args = ap.parse_args()

    which = _pick_classifier(args.classifier)
    print(f"Using classifier: {which}")

    if which == "sklearn":
        model = joblib.load(MODEL_PATH)

        def classify(det_df, scenario_name):
            return apply_classifier(det_df, model)
    else:
        from llm_classifier import apply_llm_classifier

        def classify(det_df, scenario_name):
            out = apply_llm_classifier(det_df, scenario_name=scenario_name)
            # NAB reads `ml_inferred_type`; LLM writes `llm_inferred_type`.
            # Bridge the column name so downstream doesn't need to know.
            out["ml_inferred_type"] = out["llm_inferred_type"]
            return out

    rows = []
    for suite, name, events_dir, cfg_file, _boot in SCENARIOS:
        det_path = OUT / f"{name}_detections.csv"
        lb_path = GEN / events_dir / "labels.csv"
        if not det_path.exists():
            print(f"skip {name}: no detections CSV")
            continue
        if not lb_path.exists():
            print(f"skip {name}: no labels CSV")
            continue

        print(f"classify {name} ({suite})...")
        det = pd.read_csv(det_path)
        det_ml = classify(det, name)
        labels = pd.read_csv(lb_path)

        nab = compute_nab(labels, det_ml)
        rows.append({"scenario": name, "suite": suite,
                      "nab_behavior": nab["user_behavior"]["score"],
                      "nab_fault":    nab["sensor_fault"]["score"],
                      "n_behavior_labels": nab["user_behavior"]["n_labels"],
                      "tp":       nab["user_behavior"]["tp"],
                      "fp":       nab["user_behavior"]["fp"],
                      "covered":  nab["user_behavior"]["covered"],
                      "fn":       nab["user_behavior"]["fn"]})

    df = pd.DataFrame(rows)
    print(f"\n=== NAB SCORES ({args.label}) ===")
    print(df.to_string(index=False))
    print()
    prod = df[df["suite"] == "production"]
    hld = df[df["suite"] == "holdout"]
    if len(prod):
        print(f"[production] n={len(prod)}  mean NAB_behavior={prod['nab_behavior'].mean():.2f}"
              f"  mean NAB_fault={prod['nab_fault'].mean():.2f}")
    if len(hld):
        print(f"[holdout]    n={len(hld)}  mean NAB_behavior={hld['nab_behavior'].mean():.2f}"
              f"  mean NAB_fault={hld['nab_fault'].mean():.2f}")


if __name__ == "__main__":
    main()
