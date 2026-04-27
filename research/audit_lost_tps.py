"""Identify which behavior labels became FN under the iter-023 percentile gate.

Reads current detection CSVs (iter-023 state, not reverted yet in CSVs)
and labels CSV; lists labels that are NOT overlapped by any detection on
the same sensor — those are the FN labels under iter-023.
"""
from __future__ import annotations
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from run_research_eval import SCENARIOS  # type: ignore

SYNTH_OUT = ROOT.parent / "synthetic-generator" / "out"
DET_OUT = ROOT / "out"


for sc in SCENARIOS:
    suite, name, events_dir, _cfg, _boot = sc
    if name not in ("household_60d", "household_120d", "household_sparse_60d",
                     "holdout_household_45d", "household_dense_90d",
                     "single_outlet_fridge_30d", "leak_30d"):
        continue
    labels = pd.read_csv(SYNTH_OUT / events_dir / "labels.csv",
                         parse_dates=["start", "end"])
    dets = pd.read_csv(DET_OUT / f"{name}_detections.csv",
                       parse_dates=["start", "end"])
    beh = labels[labels["label_class"] == "user_behavior"]
    # Filter to behavior-compatible detections (matches eval semantics).
    # DQG dropouts/out_of_range with inferred_class=sensor_fault don't
    # count as TP for behavior labels (LEARNINGS L11).
    dets_beh = dets[(dets["inferred_class"] == "user_behavior")
                    | (dets["inferred_class"] == "unknown")
                    | dets["inferred_class"].isna()]
    print(f"\n=== {name} ({suite}) ===")
    for _, lab in beh.iterrows():
        same = dets_beh[dets_beh["sensor_id"] == lab["sensor_id"]]
        ovl = same[(same["start"] <= lab["end"]) & (same["end"] >= lab["start"])]
        if len(ovl) == 0:
            dur = lab["end"] - lab["start"]
            print(f"  FN: {lab['sensor_id']:25s} {lab['anomaly_type']:25s} "
                  f"dur={dur} start={lab['start']}")
        else:
            # what dets hit?
            tags = sorted(set(ovl["detector"].unique()))
            dur = lab["end"] - lab["start"]
            print(f"  TP: {lab['sensor_id']:25s} {lab['anomaly_type']:25s} "
                  f"dur={dur} dets={tags}")
