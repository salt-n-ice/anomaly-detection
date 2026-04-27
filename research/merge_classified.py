"""Merge the subagent's classification output into detection CSVs as a new
`ml_inferred_type` column. Explicit-type rows (DQG, state_transition) are
passed through — they keep their `inferred_type` as `ml_inferred_type`.

Input:
  research/ambiguous_classified.json  (from the subagent)

Output:
  out/<scenario>_detections_ml.csv  (augmented per-scenario CSVs)

Usage:
    python research/merge_classified.py
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "research"))

from llm_classifier import EXPLICIT_TYPES  # noqa: E402
from run_research_eval import SCENARIOS, OUT  # noqa: E402

CLASSIFIED_PATH = ROOT / "research" / "ambiguous_classified.json"


def main():
    classified = json.loads(CLASSIFIED_PATH.read_text())
    # Build per-scenario lookup: {(scenario, row_idx): {type, confidence}}
    lookup: dict[tuple[str, int], dict] = {}
    for r in classified:
        lookup[(r["scenario"], int(r["row_idx"]))] = r

    for _suite, name, _ed, _cfg, _b in SCENARIOS:
        det_path = OUT / f"{name}_detections.csv"
        if not det_path.exists():
            continue
        det = pd.read_csv(det_path)
        types: list[str] = []
        confs: list[float] = []
        n_amb = n_exp = 0
        for idx, row in det.iterrows():
            itype = str(row.get("inferred_type", ""))
            if itype in EXPLICIT_TYPES:
                types.append(itype)
                confs.append(1.0)
                n_exp += 1
                continue
            key = (name, int(idx))
            match = lookup.get(key)
            if match is None:
                types.append("statistical_anomaly")
                confs.append(0.0)
            else:
                types.append(str(match["type"]))
                confs.append(float(match.get("confidence", 0.0)))
                n_amb += 1
        det["ml_inferred_type"] = types
        det["ml_confidence"] = confs
        out_path = OUT / f"{name}_detections_ml.csv"
        det.to_csv(out_path, index=False)
        print(f"{name}: {len(det)} rows  (explicit={n_exp}, amb_matched={n_amb})  -> {out_path.name}")


if __name__ == "__main__":
    main()
