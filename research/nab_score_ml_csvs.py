"""Score NAB on the `_ml.csv` files produced by merge_classified.py.

These CSVs already carry `ml_inferred_type` from the subagent classifier,
so no sklearn / API classifier step is needed. Straight-to-NAB.

Usage:
    python research/nab_score_ml_csvs.py --label "iter2_llm"
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "research"))

from nab_metric import compute_nab  # noqa: E402
from run_research_eval import SCENARIOS, GEN, OUT  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="run")
    args = ap.parse_args()

    rows = []
    for suite, name, events_dir, _cfg, _b in SCENARIOS:
        det_path = OUT / f"{name}_detections_ml.csv"
        lb_path = GEN / events_dir / "labels.csv"
        if not det_path.exists() or not lb_path.exists():
            print(f"skip {name}: missing csv")
            continue
        det = pd.read_csv(det_path)
        labels = pd.read_csv(lb_path)
        nab = compute_nab(labels, det)
        rows.append({"scenario": name, "suite": suite,
                      "nab_behavior": nab["user_behavior"]["score"],
                      "nab_fault":    nab["sensor_fault"]["score"],
                      "n_lbl": nab["user_behavior"]["n_labels"],
                      "tp":       nab["user_behavior"]["tp"],
                      "fp":       nab["user_behavior"]["fp"],
                      "covered":  nab["user_behavior"]["covered"],
                      "fn":       nab["user_behavior"]["fn"]})

    df = pd.DataFrame(rows)
    print(f"\n=== NAB SCORES ({args.label}) ===")
    print(df.to_string(index=False))
    prod = df[df["suite"] == "production"]
    hld  = df[df["suite"] == "holdout"]
    print()
    if len(prod):
        print(f"[production] n={len(prod)}  mean NAB_behavior={prod['nab_behavior'].mean():.2f}")
    if len(hld):
        print(f"[holdout]    n={len(hld)}  mean NAB_behavior={hld['nab_behavior'].mean():.2f}")


if __name__ == "__main__":
    main()
