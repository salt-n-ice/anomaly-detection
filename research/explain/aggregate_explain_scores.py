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


def _resolve_run(run_arg: str) -> Path:
    if run_arg == "latest":
        pointer = RUNS / "latest.txt"
        if not pointer.exists():
            raise FileNotFoundError(
                f"{pointer} missing — run run_explain_eval.py first")
        return RUNS / pointer.read_text().strip()
    return RUNS / run_arg


def build_snapshot(run_dir: Path) -> dict:
    manifest_path = run_dir / "manifest.json"
    manifest = (json.loads(manifest_path.read_text())
                if manifest_path.exists()
                else {"scenarios": []})
    scenarios_out: list[dict] = []
    missing: list[str] = []
    for row in manifest["scenarios"]:
        if row.get("skipped"):
            continue
        name = row["name"]; suite = row["suite"]
        scores_path = run_dir / f"{name}_scores.jsonl"
        if not scores_path.exists():
            missing.append(name); continue
        scores = _read_jsonl(scores_path)
        scenarios_out.append(compute_scenario_summary(name, suite, scores))

    def _agg(subset: list[dict]) -> dict:
        if not subset:
            return {"n": 0}
        tp_means = [s["tp_mean"] for s in subset if s.get("tp_mean") is not None]
        fp_means = [s["fp_mean"] for s in subset if s.get("fp_mean") is not None]
        return {
            "n": len(subset),
            "mean_tp_mean": _mean(tp_means),
            "mean_fp_mean": _mean(fp_means),
            "worst_tp_mean": round(min(tp_means), 3) if tp_means else None,
            "worst_fp_mean": round(min(fp_means), 3) if fp_means else None,
        }

    by_suite: dict[str, list[dict]] = {}
    for s in scenarios_out:
        by_suite.setdefault(s["suite"], []).append(s)

    return {
        "timestamp": manifest.get("timestamp"),
        "git_hash": git_hash(),
        "git_dirty": git_dirty(),
        "run_dir": str(run_dir),
        "scenarios": scenarios_out,
        "aggregate": {"all": _agg(scenarios_out),
                      **{k: _agg(v) for k, v in by_suite.items()}},
        "missing_scores": missing,
    }


def diff(old: dict, new: dict, tol: float = 0.2) -> dict:
    old_map = {s["name"]: s for s in old.get("scenarios", [])}
    new_map = {s["name"]: s for s in new.get("scenarios", [])}
    regressions: list[dict] = []
    improvements: list[dict] = []
    neutral: list[dict] = []
    for name, n in new_map.items():
        if name not in old_map:
            continue
        o = old_map[name]
        worst_drop = 0.0
        worst_dim = None
        for d in TP_DIMS:
            ov = (o.get("dim_tp_means") or {}).get(d)
            nv = (n.get("dim_tp_means") or {}).get(d)
            if ov is None or nv is None: continue
            drop = ov - nv
            if drop > worst_drop:
                worst_drop = drop; worst_dim = f"tp.{d}"
        for d in FP_DIMS:
            ov = (o.get("dim_fp_means") or {}).get(d)
            nv = (n.get("dim_fp_means") or {}).get(d)
            if ov is None or nv is None: continue
            drop = ov - nv
            if drop > worst_drop:
                worst_drop = drop; worst_dim = f"fp.{d}"
        d_tp = (n.get("tp_mean") or 0) - (o.get("tp_mean") or 0)
        d_fp = (n.get("fp_mean") or 0) - (o.get("fp_mean") or 0)
        row = {"name": name, "suite": n["suite"],
               "d_tp_mean": round(d_tp, 3), "d_fp_mean": round(d_fp, 3),
               "worst_drop": round(worst_drop, 3), "worst_dim": worst_dim}
        if worst_drop > tol or d_tp < -tol or d_fp < -tol:
            regressions.append(row)
        elif d_tp > tol or d_fp > tol:
            improvements.append(row)
        else:
            neutral.append(row)
    return {"regressions": regressions, "improvements": improvements,
            "neutral": neutral}


def _print_diff(d: dict) -> None:
    print("\n=== DIFF vs baseline ===")
    for group, rows in (("REGRESSIONS", d["regressions"]),
                        ("IMPROVEMENTS", d["improvements"]),
                        ("NEUTRAL", d["neutral"])):
        print(f"\n[{group}] ({len(rows)})")
        for r in rows:
            print(f"  {r['name']:<22} d_tp={r['d_tp_mean']:+.2f}  "
                  f"d_fp={r['d_fp_mean']:+.2f}  worst={r['worst_dim']}({-r['worst_drop']:+.2f})")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="latest",
                    help="run-directory name under research/explain/runs/ (or 'latest')")
    ap.add_argument("--save-baseline", action="store_true")
    ap.add_argument("--diff-baseline", action="store_true")
    ap.add_argument("--tol", type=float, default=0.2)
    args = ap.parse_args(argv)

    run_dir = _resolve_run(args.run)
    if not run_dir.exists():
        print(f"run dir missing: {run_dir}", file=sys.stderr); return 2

    snap = build_snapshot(run_dir)
    summary_path = run_dir / "summary.json"
    summary_path.write_text(json.dumps(snap, indent=2))
    (RUNS / "latest.json").write_text(json.dumps(snap, indent=2))
    print(f"wrote {summary_path}")

    if snap["missing_scores"]:
        print(f"  (missing scores for: {', '.join(snap['missing_scores'])})")

    if args.save_baseline:
        BASELINE.write_text(json.dumps(snap, indent=2))
        print(f"froze baseline -> {BASELINE}")

    if args.diff_baseline:
        if not BASELINE.exists():
            print("no EXPLAIN_BASELINE.json — run with --save-baseline first",
                  file=sys.stderr)
            return 2
        d = diff(json.loads(BASELINE.read_text()), snap, tol=args.tol)
        _print_diff(d)
        return 1 if d["regressions"] else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
