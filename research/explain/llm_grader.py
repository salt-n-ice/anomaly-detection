"""LLM-grader pipeline for explain prompts.

Two-step flow: (1) ``prepare`` extracts grading inputs from the latest run,
one JSON per scenario under ``runs/<ts>/grading_inputs/``. (2) Subagent
graders (dispatched from a Claude Code session) read each input file and
write a sibling ``<scen>_grades.json`` with structured scores. (3)
``aggregate`` consolidates and prints a scoreboard.

Per-label, not per-chain: a label may be matched by many overlapping
chains; we pick the chain with the highest ``bundle.score`` (tie-break
by case_id) since that's what the production LLM would most likely be
shown for the label's user-facing notification.

Granularity rationale: production summaries are emitted per-incident, not
per-chain — the user sees one notification, the metric should reflect
that. Multiple TP user_behavior labels per scenario give us a sample.

Usage
-----
    python research/explain/llm_grader.py prepare --run latest
    # ...dispatch graders out-of-band, write <scen>_grades.json siblings...
    python research/explain/llm_grader.py aggregate --run latest
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "research"))

from anomaly.explain.types import type_to_class  # noqa: E402

RUNS = ROOT / "research" / "explain" / "runs"


def _resolve_run_dir(run_arg: str) -> Path:
    if run_arg == "latest":
        latest_txt = RUNS / "latest.txt"
        if latest_txt.exists():
            return RUNS / latest_txt.read_text().strip()
        dirs = sorted(d for d in RUNS.iterdir() if d.is_dir())
        if not dirs:
            raise FileNotFoundError(f"No runs in {RUNS}")
        return dirs[-1]
    return RUNS / run_arg


def _load_cases(cases_path: Path) -> list[dict]:
    return [json.loads(ln) for ln in cases_path.read_text(encoding="utf-8").splitlines()
            if ln.strip()]


def _label_key(L: dict) -> tuple:
    return (L["sensor_id"], L["anomaly_type"], L["start"], L["end"])


def _select_best_per_label(cases: list[dict]) -> dict:
    """For each TP user_behavior label, return the case with the highest
    bundle.score among overlapping chains. Tie-break by case_id."""
    best: dict[tuple, dict] = {}
    for c in cases:
        if not c["is_tp"]:
            continue
        for L in c["gt_labels"]:
            if type_to_class(L["anomaly_type"]) != "user_behavior":
                continue
            key = _label_key(L)
            score = float(c["bundle"].get("score") or 0)
            cur = best.get(key)
            cur_score = float(cur["bundle"]["score"]) if cur else float("-inf")
            if (cur is None or score > cur_score
                    or (score == cur_score and c["case_id"] < cur["case_id"])):
                best[key] = c
    return best


def prepare(run_dir: Path) -> int:
    """Build per-scenario grading-input JSONs under
    ``run_dir/grading_inputs/<scen>.json``. Each file lists
    ``{label_key, gt_type, gt_class, prompt, classification}`` per label."""
    inputs_dir = run_dir / "grading_inputs"
    inputs_dir.mkdir(exist_ok=True)
    n_total = 0
    for cases_path in sorted(run_dir.glob("*_cases.jsonl")):
        scen = cases_path.stem.replace("_cases", "")
        cases = _load_cases(cases_path)
        per_label = _select_best_per_label(cases)
        items = []
        for key, c in per_label.items():
            items.append({
                "label_key": "|".join(str(x) for x in key),
                "sensor_id": key[0],
                "gt_type":   key[1],
                "gt_start":  key[2],
                "gt_end":    key[3],
                "gt_class":  type_to_class(key[1]),
                "case_id":   c["case_id"],
                "classification": c["bundle"]["classification"],
                "prompt":    c["prompt"],
            })
        out = inputs_dir / f"{scen}.json"
        out.write_text(json.dumps({"scenario": scen, "n_labels": len(items),
                                   "items": items}, indent=2),
                       encoding="utf-8")
        print(f"  {scen:<26}  n_labels={len(items):>3}  -> {out.relative_to(ROOT)}")
        n_total += len(items)
    print(f"\nprepared {n_total} labels across {len(list(inputs_dir.iterdir()))} scenarios")
    return 0


def aggregate(run_dir: Path) -> int:
    """Read sibling ``<scen>_grades.json`` files written by graders and
    print a scoreboard. Output is also written to
    ``run_dir/llm_grades.json``."""
    inputs_dir = run_dir / "grading_inputs"
    if not inputs_dir.exists():
        print(f"no grading_inputs dir at {inputs_dir}", file=sys.stderr)
        return 1
    all_grades: dict[str, list[dict]] = {}
    for inp_path in sorted(inputs_dir.glob("*.json")):
        scen = inp_path.stem
        if scen.endswith("_grades"):
            continue  # skip the grader output files when iterating inputs
        grades_path = inputs_dir / f"{scen}_grades.json"
        if not grades_path.exists():
            print(f"  [skip] {scen}: no grades file at {grades_path.name}")
            continue
        all_grades[scen] = json.loads(grades_path.read_text(encoding="utf-8"))
    if not all_grades:
        print("no grades files found")
        return 1

    summary = {"scenarios": {}}
    print(f"\n=== LLM-grader scoreboard (run {run_dir.name}) ===")
    print(f"{'scenario':<28} {'n':>3} {'acc':>5} {'act':>5} {'clr':>5} {'cal':>5} {'avg':>5}")
    for scen, grades in all_grades.items():
        if not grades:
            continue
        avg_acc = sum(g["accuracy"] for g in grades) / len(grades)
        avg_act = sum(g["actionability"] for g in grades) / len(grades)
        avg_clr = sum(g["clarity"] for g in grades) / len(grades)
        avg_cal = sum(g["calibration"] for g in grades) / len(grades)
        avg_all = (avg_acc + avg_act + avg_clr + avg_cal) / 4
        summary["scenarios"][scen] = {
            "n": len(grades),
            "accuracy": round(avg_acc, 2),
            "actionability": round(avg_act, 2),
            "clarity": round(avg_clr, 2),
            "calibration": round(avg_cal, 2),
            "overall": round(avg_all, 2),
            "labels": grades,
        }
        print(f"  {scen:<26} {len(grades):>3} "
              f"{avg_acc:>5.2f} {avg_act:>5.2f} {avg_clr:>5.2f} {avg_cal:>5.2f} "
              f"{avg_all:>5.2f}")

    # Worst-of: anything with accuracy < 3
    flagged = []
    for scen, grades in all_grades.items():
        for g in grades:
            if g.get("accuracy", 5) < 3:
                flagged.append((scen, g))
    if flagged:
        print(f"\n=== {len(flagged)} flagged labels (accuracy < 3) ===")
        for scen, g in flagged:
            print(f"  [{scen}] {g.get('label_key', '?')}")
            print(f"    summary: {g.get('summary', '')[:120]}")
            print(f"    critique: {g.get('critique', '')[:200]}")

    out_path = run_dir / "llm_grades.json"
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\nwrote {out_path.relative_to(ROOT)}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["prepare", "aggregate"])
    ap.add_argument("--run", default="latest")
    args = ap.parse_args(argv)
    run_dir = _resolve_run_dir(args.run)
    if not run_dir.exists():
        print(f"run dir not found: {run_dir}", file=sys.stderr)
        return 1
    if args.cmd == "prepare":
        return prepare(run_dir)
    return aggregate(run_dir)


if __name__ == "__main__":
    raise SystemExit(main())
