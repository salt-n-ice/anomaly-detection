"""Explain-quality metric — type-classification accuracy.

Headline: `super_match_rate` — fraction of TP user_behavior labels whose
super-class matches at least one overlapping chain's
`bundle.classification.type` super-class. Aggregated per scenario.

Auxiliaries:
- `strict_match_rate` — same as headline but with exact-type equality
  instead of super-class equivalence (informational).
- `class_match_rate` — fraction of TP labels whose `label_class`
  (user_behavior / sensor_fault) matches the overlapping chain's
  `bundle.classification.class`. Gates TP credit in the detection
  metric, so it must hold.
- per-GT-type breakdown for strict + super (diagnostic).

Granularity: per LABEL (not per chain). A single label may have multiple
overlapping chains — it counts once in the denominator and is matched
if ANY overlapping chain matches.

Verdict thresholds (encoded in EXPLAIN_BASELINE.json's metric_definition):
- tol = 0.02  (per-scenario regression > 2pp on the headline → REJECT)
- noise_floor = 0.005  (changes within ±0.5pp are NULL, not improvement)

Production scenarios gate accept/reject. Holdout scenarios surface as
warnings only.

Usage
-----
    python research/explain/explain_metric.py --run latest
    python research/explain/explain_metric.py --run latest --diff-baseline
    python research/explain/explain_metric.py --run latest --save-baseline
    python research/explain/explain_metric.py --run 20260425T131617Z --diff-baseline
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "research"))

from anomaly.explain.types import (  # noqa: E402
    USER_BEHAVIOR_TYPES, SENSOR_FAULT_TYPES, type_to_class,
)
from run_research_eval import git_hash, git_dirty  # noqa: E402

RUNS = ROOT / "research" / "explain" / "runs"
BASELINE = ROOT / "research" / "explain" / "EXPLAIN_BASELINE.json"


# Super-class mapping. Conservative — only collapses pairs that need
# bundle-external context to discriminate (e.g., level_shift vs month_shift
# needs multi-week calendar context that's not in a single chain emit).
# Types not in this map default to themselves (each its own super-class).
SUPER_CLASS: dict[str, str] = {
    # Sustained value-domain shifts (need calendar context to discriminate)
    "level_shift":            "value_shift",
    "month_shift":            "value_shift",
    "trend":                  "value_shift",
    "degradation_trajectory": "value_shift",
    # Calendar-pattern shifts (need calendar context to discriminate)
    "weekend_anomaly":        "calendar_pattern",
    "time_of_day":            "calendar_pattern",
    "seasonal_mismatch":      "calendar_pattern",
    "seasonality_loss":       "calendar_pattern",
    # Impulse anomalies
    "spike":                  "impulse",
    "dip":                    "impulse",
}


def super_class(anomaly_type: str | None) -> str:
    """Map an anomaly type to its super-class (or itself if not collapsed)."""
    if anomaly_type is None:
        return "_unknown"
    return SUPER_CLASS.get(anomaly_type, anomaly_type)


def _read_jsonl(path: Path) -> list[dict]:
    return [json.loads(ln) for ln in path.read_text(encoding="utf-8").splitlines()
            if ln.strip()]


def _resolve_run_dir(run_arg: str) -> Path:
    if run_arg == "latest":
        latest_txt = RUNS / "latest.txt"
        if latest_txt.exists():
            return RUNS / latest_txt.read_text().strip()
        # Fallback: the most recent timestamped dir
        dirs = sorted([d for d in RUNS.iterdir() if d.is_dir()])
        if not dirs:
            raise FileNotFoundError(f"No runs in {RUNS}")
        return dirs[-1]
    return RUNS / run_arg


def compute_scenario(cases_path: Path) -> dict:
    """Compute metrics for one scenario from its <scen>_cases.jsonl."""
    cases = _read_jsonl(cases_path)

    # Per-label aggregation: a label is keyed by (sensor, type, start, end).
    # For each label we track (a) any overlapping chain whose type strictly
    # matches the GT.anomaly_type, (b) any overlapping chain whose super-class
    # matches the GT.anomaly_type's super-class, (c) any overlapping chain
    # whose class matches the GT's label_class.
    user_behavior_labels: dict[tuple, dict] = {}
    all_labels: dict[tuple, dict] = {}

    for case in cases:
        if not case["is_tp"]:
            continue
        bundle = case["bundle"]
        cls_block = bundle.get("classification", {})
        chain_type = cls_block.get("type")
        chain_class = cls_block.get("class")
        chain_super = super_class(chain_type)

        for gt in case["gt_labels"]:
            gt_type = gt["anomaly_type"]
            gt_class = type_to_class(gt_type)
            gt_super = super_class(gt_type)
            key = (gt["sensor_id"], gt_type, gt["start"], gt["end"])

            entry = all_labels.setdefault(key, {
                "anomaly_type": gt_type,
                "label_class": gt_class,
                "any_strict": False,
                "any_super": False,
                "any_class_match": False,
                "n_chains": 0,
            })
            entry["n_chains"] += 1
            entry["any_strict"] = entry["any_strict"] or (chain_type == gt_type)
            entry["any_super"] = entry["any_super"] or (chain_super == gt_super)
            entry["any_class_match"] = (entry["any_class_match"]
                                        or chain_class == gt_class)

            if gt_class == "user_behavior":
                user_behavior_labels[key] = entry

    n_ub = len(user_behavior_labels)
    n_all = len(all_labels)

    if n_ub:
        super_match = sum(1 for e in user_behavior_labels.values()
                          if e["any_super"]) / n_ub
        strict_match = sum(1 for e in user_behavior_labels.values()
                           if e["any_strict"]) / n_ub
    else:
        super_match = strict_match = float("nan")

    if n_all:
        class_match = sum(1 for e in all_labels.values()
                          if e["any_class_match"]) / n_all
    else:
        class_match = float("nan")

    # Per-GT-type breakdown (diagnostic)
    by_gt_type: dict[str, dict] = {}
    for entry in user_behavior_labels.values():
        bucket = by_gt_type.setdefault(entry["anomaly_type"], {
            "n": 0, "strict": 0, "super": 0,
        })
        bucket["n"] += 1
        if entry["any_strict"]:
            bucket["strict"] += 1
        if entry["any_super"]:
            bucket["super"] += 1
    by_gt_type_summary = {
        t: {"n": b["n"],
             "strict_rate": b["strict"] / b["n"],
             "super_rate":  b["super"] / b["n"]}
        for t, b in by_gt_type.items()
    }

    return {
        "n_user_behavior_tp_labels": n_ub,
        "n_all_tp_labels": n_all,
        "super_match_rate":  round(super_match, 4) if super_match == super_match else None,
        "strict_match_rate": round(strict_match, 4) if strict_match == strict_match else None,
        "class_match_rate":  round(class_match, 4) if class_match == class_match else None,
        "by_gt_type": by_gt_type_summary,
    }


# Production scenarios gate accept/reject; holdout surfaces as warnings.
PRODUCTION_SCENARIOS = {"household_60d", "household_120d", "leak_30d"}


def compute_run(run_dir: Path) -> dict:
    scenarios: dict[str, dict] = {}
    for cases_path in sorted(run_dir.glob("*_cases.jsonl")):
        scen = cases_path.stem.replace("_cases", "")
        scenarios[scen] = compute_scenario(cases_path)
        scenarios[scen]["suite"] = ("production" if scen in PRODUCTION_SCENARIOS
                                     else "holdout")
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "git_hash": git_hash(),
        "git_dirty": git_dirty(),
        "run_dir": run_dir.name,
        "metric_definition": {
            "headline": "super_match_rate — fraction of TP user_behavior "
                        "labels whose super-class matches some overlapping "
                        "chain's bundle.classification.type super-class",
            "auxiliaries": [
                "strict_match_rate — exact-type equality (informational)",
                "class_match_rate — bundle.classification.class vs "
                "GT.label_class (gates TP credit)",
                "by_gt_type — per-anomaly-type breakdown of strict + super",
            ],
            "super_class_map": SUPER_CLASS,
            "tol": 0.02,
            "noise_floor": 0.005,
        },
        "scenarios": scenarios,
    }


def print_run(snapshot: dict) -> None:
    print(f"\n=== run {snapshot['run_dir']} (git {snapshot['git_hash']}) ===")
    print(f"{'scenario':<28} {'suite':<11} {'n_ub':>4} {'super':>7} "
          f"{'strict':>7} {'class':>7}")
    for scen, m in snapshot["scenarios"].items():
        n = m["n_user_behavior_tp_labels"]
        sup = f"{m['super_match_rate']:.3f}" if m['super_match_rate'] is not None else "  -  "
        strict = f"{m['strict_match_rate']:.3f}" if m['strict_match_rate'] is not None else "  -  "
        cls = f"{m['class_match_rate']:.3f}" if m['class_match_rate'] is not None else "  -  "
        print(f"  {scen:<26} {m['suite']:<11} {n:>4} {sup:>7} {strict:>7} {cls:>7}")


def diff_baseline(snapshot: dict, baseline: dict) -> dict:
    tol = baseline["metric_definition"]["tol"]
    noise = baseline["metric_definition"]["noise_floor"]
    rows = []
    for scen, m_new in snapshot["scenarios"].items():
        m_old = baseline["scenarios"].get(scen)
        if m_old is None:
            rows.append({"name": scen, "suite": m_new["suite"],
                          "status": "new", "d_super": None, "d_strict": None,
                          "d_class": None})
            continue
        old_super = m_old.get("super_match_rate") or 0
        new_super = m_new.get("super_match_rate") or 0
        d_super = round(new_super - old_super, 4)
        old_strict = m_old.get("strict_match_rate") or 0
        new_strict = m_new.get("strict_match_rate") or 0
        d_strict = round(new_strict - old_strict, 4)
        old_class = m_old.get("class_match_rate") or 0
        new_class = m_new.get("class_match_rate") or 0
        d_class = round(new_class - old_class, 4)
        is_prod = m_new["suite"] == "production"
        if d_super < -tol and is_prod:
            status = "REGRESSION"
        elif d_super < -tol:
            status = "OVERFIT_WARNING"
        elif abs(d_super) <= noise:
            status = "NULL"
        elif d_super > noise:
            status = "IMPROVEMENT"
        else:
            status = "MINOR_REGRESSION"
        rows.append({
            "name": scen, "suite": m_new["suite"], "status": status,
            "d_super": d_super, "d_strict": d_strict, "d_class": d_class,
        })
    return {
        "tol": tol, "noise_floor": noise,
        "baseline_run": baseline.get("run_dir"),
        "new_run": snapshot["run_dir"],
        "rows": rows,
    }


def print_diff(d: dict) -> None:
    print(f"\n=== DIFF vs baseline (run {d['baseline_run']}) ===")
    print(f"(tol={d['tol']:.3f}  noise_floor={d['noise_floor']:.3f}  "
          f"production scenarios gate; holdout warns)")
    print(f"\n{'scenario':<28} {'suite':<11} {'status':<18} "
          f"{'d_super':>8} {'d_strict':>9} {'d_class':>9}")
    for r in d["rows"]:
        ds = f"{r['d_super']:+.3f}" if r["d_super"] is not None else "  -   "
        dst = f"{r['d_strict']:+.3f}" if r["d_strict"] is not None else "   -   "
        dc = f"{r['d_class']:+.3f}" if r["d_class"] is not None else "   -   "
        print(f"  {r['name']:<26} {r['suite']:<11} {r['status']:<18} "
              f"{ds:>8} {dst:>9} {dc:>9}")
    regressions = [r for r in d["rows"] if r["status"] == "REGRESSION"]
    if regressions:
        print(f"\n[REJECT] {len(regressions)} production scenario(s) "
              f"crossed -tol on headline.")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="latest",
                    help="Run dir name under research/explain/runs/, or 'latest'.")
    ap.add_argument("--diff-baseline", action="store_true",
                    help="Diff vs research/explain/EXPLAIN_BASELINE.json.")
    ap.add_argument("--save-baseline", action="store_true",
                    help="Freeze the current run as EXPLAIN_BASELINE.json.")
    args = ap.parse_args(argv)

    run_dir = _resolve_run_dir(args.run)
    if not run_dir.exists():
        print(f"run dir not found: {run_dir}", file=sys.stderr)
        return 1
    snapshot = compute_run(run_dir)
    print_run(snapshot)

    if args.save_baseline:
        BASELINE.write_text(json.dumps(snapshot, indent=2))
        print(f"\nfroze baseline -> {BASELINE}")

    if args.diff_baseline:
        if not BASELINE.exists():
            print(f"\n[no baseline at {BASELINE}; run with --save-baseline first]")
            return 0
        baseline = json.loads(BASELINE.read_text())
        d = diff_baseline(snapshot, baseline)
        print_diff(d)
        if any(r["status"] == "REGRESSION" for r in d["rows"]):
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
