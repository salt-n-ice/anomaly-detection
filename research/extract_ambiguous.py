"""Extract all ambiguous detections across scenarios into one JSON file
ready to feed to a subagent classifier.

Ambiguous = a fused-detector-chain detection whose `inferred_type` is
`statistical_anomaly` (the current rule-based fallback when the
classifier can't confidently pick a type). Explicit-typed DQG and
state_transition rows are skipped.

Output: research/ambiguous_batch.json with:
    [
      {"scenario": "...", "row_idx": <csv row>, "bundle": {...}},
      ...
    ]

Usage:
    python research/extract_ambiguous.py
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "research"))

from llm_classifier import EXPLICIT_TYPES, _stable_bundle  # noqa: E402
from run_research_eval import SCENARIOS, OUT  # noqa: E402

BATCH_PATH = ROOT / "research" / "ambiguous_batch.json"


def main():
    out = []
    for _suite, name, _ed, _cfg, _b in SCENARIOS:
        det_path = OUT / f"{name}_detections.csv"
        if not det_path.exists():
            continue
        det = pd.read_csv(det_path)
        for idx, row in det.iterrows():
            itype = str(row.get("inferred_type", ""))
            if itype in EXPLICIT_TYPES:
                continue
            bundle = _stable_bundle(row)
            out.append({
                "scenario": name,
                "row_idx":  int(idx),
                "current_inferred_type": itype,
                "bundle":   bundle,
            })
    BATCH_PATH.write_text(json.dumps(out, indent=2))
    print(f"wrote {len(out)} ambiguous rows to {BATCH_PATH}")
    # Small summary
    by_scen = {}
    for r in out:
        by_scen[r["scenario"]] = by_scen.get(r["scenario"], 0) + 1
    for s, n in sorted(by_scen.items()):
        print(f"  {s}: {n}")


if __name__ == "__main__":
    main()
