"""Research-loop eval harness — machine-parseable successor to scripts/run_all_scenarios.py.

Runs one or more scenarios across the 60d and 120d suites, prints a compact table,
and writes a JSON snapshot (with timestamp, git hash, per-scenario metrics, and
aggregate stats) that downstream diffing logic can consume.

Usage
-----
    # run everything available (60d + 120d if generated)
    python research/run_research_eval.py --suite all

    # only the 60d suite (same scenarios as scripts/run_all_scenarios.py)
    python research/run_research_eval.py --suite 60d

    # freeze the current metrics as the baseline to beat
    python research/run_research_eval.py --suite all --save-baseline

    # diff the latest run against the frozen baseline and exit non-zero on regression
    python research/run_research_eval.py --suite all --diff-baseline

Outputs
-------
    research/runs/<timestamp>.json        one JSON per run
    research/runs/latest.json             symlink-ish pointer (copy) to the latest
    research/BASELINE.json                frozen baseline (only written with --save-baseline)

The JSON schema is documented in research/START_RESEARCH.md.
"""
from __future__ import annotations
import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd  # noqa: E402
from anomaly.pipeline import run  # noqa: E402
from anomaly.metrics import (  # noqa: E402
    compute_metrics,
    compute_metrics_pointwise,
    compute_metrics_event,
    compute_metrics_time,
)

GEN = Path(os.environ.get("SENSORGEN_OUT", ROOT.parent / "synthetic-generator" / "out"))
CFG = ROOT / "configs"
OUT = ROOT / "out"
RESEARCH_OUT = ROOT / "research" / "runs"
BASELINE_PATH = ROOT / "research" / "BASELINE.json"


# (suite, name, events_dir_name, config_filename, bootstrap_days)
# events_dir_name points to {SENSORGEN_OUT}/<name>/events.csv + labels.csv
SCENARIOS: list[tuple[str, str, str, str, float]] = [
    ("60d", "outlet_60d",        "outlet",        "outlet.yaml",        14.0),
    ("60d", "outlet_tv_60d",     "outlet_tv",     "outlet_tv.yaml",     14.0),
    ("60d", "outlet_kettle_60d", "outlet_kettle", "outlet_kettle.yaml", 14.0),
    ("60d", "waterleak_60d",     "leak",          "waterleak.yaml",     14.0),
    ("60d", "outlet_short_60d",  "outlet_short",  "outlet.yaml",        14.0),
    ("120d", "outlet_120d",      "outlet_120d",   "outlet.yaml",        14.0),
    ("120d", "waterleak_120d",   "waterleak_120d","waterleak.yaml",     14.0),
]


def git_hash() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except Exception:
        return "unknown"


def git_dirty() -> bool:
    try:
        out = subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True)
        return bool(out.strip())
    except Exception:
        return False


def score_one(name: str, events_csv: Path, cfg_yaml: Path, labels_csv: Path,
              det_csv: Path, bootstrap_days: float) -> dict:
    t0 = time.time()
    run(events_csv, cfg_yaml, det_csv, bootstrap_days=bootstrap_days)
    elapsed = time.time() - t0

    gt = pd.read_csv(labels_csv)
    det = pd.read_csv(det_csv)
    m11 = compute_metrics(gt, det)
    mpw = compute_metrics_pointwise(gt, det)
    mev = compute_metrics_event(gt, det)
    mtm = compute_metrics_time(gt, det)

    ev_ts = pd.to_datetime(
        pd.read_csv(events_csv, usecols=["timestamp"])["timestamp"],
        utc=True, format="ISO8601")
    timeline_days = ((ev_ts.max() - ev_ts.min()).total_seconds() / 86400
                     if len(ev_ts) else 0.0)
    fp_h = mtm["fp_sec"] / 3600
    fn_h = mtm["fn_sec"] / 3600
    fp_h_per_day = fp_h / max(1e-6, timeline_days)
    events_per_incident = mev["n_events"] / max(1, len(gt))

    return {
        "name": name,
        "elapsed_s": round(elapsed, 2),
        "n_labels": int(len(gt)),
        "n_detections": int(len(det)),
        "n_events": int(mev["n_events"]),
        "timeline_days": round(float(timeline_days), 2),
        "evt_f1": round(float(mev["f1"]), 4),
        "evt_precision": round(float(mev["precision"]), 4),
        "evt_recall": round(float(mev["recall"]), 4),
        "evt_tp": int(mev["tp"]),
        "evt_fp": int(mev["fp"]),
        "evt_fn": int(mev["fn"]),
        "time_f1": round(float(mtm["time_f1"]), 4),
        "time_precision": round(float(mtm["time_precision"]), 4),
        "time_recall": round(float(mtm["time_recall"]), 4),
        "fp_h": round(float(fp_h), 2),
        "fn_h": round(float(fn_h), 2),
        "fp_h_per_day": round(float(fp_h_per_day), 3),
        "incident_recall": round(float(mpw["recall"]), 4),
        "events_per_incident": round(float(events_per_incident), 3),
        "f1_1to1": round(float(m11["f1"]), 4),
        "f1_pw": round(float(mpw["f1"]), 4),
    }


def filter_suite(suite: str) -> list[tuple[str, str, str, str, float]]:
    if suite == "all":
        return SCENARIOS
    return [s for s in SCENARIOS if s[0] == suite]


def aggregate(results: list[dict]) -> dict:
    def _agg(subset: list[dict]) -> dict:
        if not subset:
            return {}
        return {
            "n": len(subset),
            "mean_evt_f1": round(sum(r["evt_f1"] for r in subset) / len(subset), 4),
            "mean_time_f1": round(sum(r["time_f1"] for r in subset) / len(subset), 4),
            "mean_incident_recall": round(
                sum(r["incident_recall"] for r in subset) / len(subset), 4),
            "mean_fp_h_per_day": round(
                sum(r["fp_h_per_day"] for r in subset) / len(subset), 3),
            "worst_evt_f1": round(min(r["evt_f1"] for r in subset), 4),
            "worst_time_f1": round(min(r["time_f1"] for r in subset), 4),
            "worst_incident_recall": round(
                min(r["incident_recall"] for r in subset), 4),
        }
    by_suite: dict[str, list[dict]] = {}
    for r in results:
        by_suite.setdefault(r["suite"], []).append(r)
    agg = {"all": _agg(results)}
    for suite, subset in by_suite.items():
        agg[suite] = _agg(subset)
    return agg


def run_suite(suite: str) -> dict:
    OUT.mkdir(exist_ok=True)
    RESEARCH_OUT.mkdir(parents=True, exist_ok=True)
    results: list[dict] = []
    skipped: list[dict] = []
    for suite_tag, name, events_dir, cfg_name, bootstrap_days in filter_suite(suite):
        events_csv = GEN / events_dir / "events.csv"
        labels_csv = GEN / events_dir / "labels.csv"
        cfg_yaml = CFG / cfg_name
        if not events_csv.exists() or not labels_csv.exists():
            print(f"  [skip] {name}: missing {events_csv} or {labels_csv}")
            skipped.append({"name": name, "suite": suite_tag,
                            "reason": "generator output not found",
                            "expected_path": str(events_csv)})
            continue
        det_csv = OUT / f"{name}_detections.csv"
        print(f"\n=== {name} ({suite_tag}) ===", flush=True)
        r = score_one(name, events_csv, cfg_yaml, labels_csv, det_csv, bootstrap_days)
        r["suite"] = suite_tag
        r["events_csv"] = str(events_csv)
        r["labels_csv"] = str(labels_csv)
        r["detections_csv"] = str(det_csv)
        r["config"] = str(cfg_yaml)
        results.append(r)
        print(f"  evt_F1={r['evt_f1']:.3f}  time_F1={r['time_f1']:.3f}  "
              f"incR={r['incident_recall']:.3f}  fp_h/d={r['fp_h_per_day']:.2f}  "
              f"ev/inc={r['events_per_incident']:.2f}  elapsed={r['elapsed_s']:.1f}s")

    snapshot = {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "git_hash": git_hash(),
        "git_dirty": git_dirty(),
        "suite_filter": suite,
        "scenarios": results,
        "skipped": skipped,
        "aggregate": aggregate(results),
    }
    return snapshot


def print_table(snapshot: dict) -> None:
    print("\n=== SUMMARY ===")
    hdr = f"{'scenario':<22} {'suite':<5} {'evt F1':>7} {'time F1':>8} {'incR':>6} {'fp_h/d':>7} {'ev/inc':>7} {'dets':>5} {'evts':>5}"
    print(hdr)
    print("-" * len(hdr))
    for r in snapshot["scenarios"]:
        print(f"{r['name']:<22} {r['suite']:<5} {r['evt_f1']:>7.3f} {r['time_f1']:>8.3f} "
              f"{r['incident_recall']:>6.3f} {r['fp_h_per_day']:>7.2f} "
              f"{r['events_per_incident']:>7.2f} {r['n_detections']:>5} {r['n_events']:>5}")
    for suite_tag, agg in snapshot["aggregate"].items():
        if not agg: continue
        print(f"\n[{suite_tag}] n={agg['n']}  mean evt F1={agg['mean_evt_f1']:.3f}  "
              f"mean time F1={agg['mean_time_f1']:.3f}  worst evt F1={agg['worst_evt_f1']:.3f}  "
              f"worst incR={agg['worst_incident_recall']:.3f}  "
              f"mean fp_h/d={agg['mean_fp_h_per_day']:.2f}")


def save_snapshot(snapshot: dict) -> Path:
    ts = snapshot["timestamp"].replace(":", "").replace("-", "").replace("+0000", "Z")
    path = RESEARCH_OUT / f"{ts}.json"
    path.write_text(json.dumps(snapshot, indent=2))
    (RESEARCH_OUT / "latest.json").write_text(json.dumps(snapshot, indent=2))
    return path


# ------------------------------- DIFF LOGIC -------------------------------

def _flatten(snapshot: dict) -> dict[str, dict]:
    return {r["name"]: r for r in snapshot["scenarios"]}


def diff(old: dict, new: dict, tol: float = 0.005,
         time_tol: float = 0.02) -> dict:
    """Per-scenario delta on evt_f1, time_f1, incident_recall, fp_h_per_day.

    A scenario is a REGRESSION if any of:
      - evt_f1 drops by more than `tol`   (default 0.005)
      - incident_recall drops by more than `tol`
      - time_f1 drops by more than `time_tol` (default 0.02 — noisier metric,
        protects against long-horizon coverage / FP-bleed degradation that
        evt_f1 hides)

    Returns a structured summary with regressions / improvements / neutral lists.
    """
    old_map = _flatten(old)
    new_map = _flatten(new)
    regressions: list[dict] = []
    improvements: list[dict] = []
    neutral: list[dict] = []
    new_only: list[str] = []
    dropped: list[str] = []

    for name in new_map:
        if name not in old_map:
            new_only.append(name); continue
        o, n = old_map[name], new_map[name]
        row = {
            "name": name,
            "suite": n["suite"],
            "evt_f1_old": o["evt_f1"], "evt_f1_new": n["evt_f1"],
            "d_evt_f1": round(n["evt_f1"] - o["evt_f1"], 4),
            "time_f1_old": o["time_f1"], "time_f1_new": n["time_f1"],
            "d_time_f1": round(n["time_f1"] - o["time_f1"], 4),
            "incR_old": o["incident_recall"], "incR_new": n["incident_recall"],
            "d_incR": round(n["incident_recall"] - o["incident_recall"], 4),
            "fp_h_d_old": o["fp_h_per_day"], "fp_h_d_new": n["fp_h_per_day"],
            "d_fp_h_d": round(n["fp_h_per_day"] - o["fp_h_per_day"], 3),
        }
        if (row["d_evt_f1"] < -tol
                or row["d_incR"] < -tol
                or row["d_time_f1"] < -time_tol):
            regressions.append(row)
        elif row["d_evt_f1"] > tol or row["d_time_f1"] > tol:
            improvements.append(row)
        else:
            neutral.append(row)
    for name in old_map:
        if name not in new_map:
            dropped.append(name)

    return {
        "regressions": regressions,
        "improvements": improvements,
        "neutral": neutral,
        "new_only": new_only,
        "dropped": dropped,
    }


def print_diff(d: dict) -> None:
    print("\n=== DIFF vs baseline ===")
    for group, rows in [("REGRESSIONS", d["regressions"]),
                        ("IMPROVEMENTS", d["improvements"]),
                        ("NEUTRAL",     d["neutral"])]:
        print(f"\n[{group}] ({len(rows)})")
        for r in rows:
            print(f"  {r['name']:<22} d_evt_F1={r['d_evt_f1']:+.3f}  "
                  f"d_time_F1={r['d_time_f1']:+.3f}  d_incR={r['d_incR']:+.3f}  "
                  f"d_fp_h/d={r['d_fp_h_d']:+.2f}")
    if d["new_only"]:
        print(f"\n[NEW_ONLY] {d['new_only']}")
    if d["dropped"]:
        print(f"[DROPPED]  {d['dropped']}")


# ------------------------------- CLI -------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", choices=["all", "60d", "120d"], default="all")
    ap.add_argument("--save-baseline", action="store_true",
                    help="Freeze the current run as research/BASELINE.json (the bar to beat).")
    ap.add_argument("--diff-baseline", action="store_true",
                    help="After running, diff against research/BASELINE.json and exit 1 if any regression.")
    ap.add_argument("--tol", type=float, default=0.005,
                    help="Tolerance for evt_f1 and incident_recall regressions (default 0.005).")
    ap.add_argument("--time-tol", type=float, default=0.02,
                    help="Tolerance for time_f1 regressions (default 0.02 — looser "
                         "because seconds-based F1 is noisier than event F1).")
    args = ap.parse_args(argv)

    snap = run_suite(args.suite)
    print_table(snap)
    path = save_snapshot(snap)
    print(f"\nwrote {path}")

    if args.save_baseline:
        BASELINE_PATH.write_text(json.dumps(snap, indent=2))
        print(f"froze baseline -> {BASELINE_PATH}")

    if args.diff_baseline:
        if not BASELINE_PATH.exists():
            print("no BASELINE.json yet — run with --save-baseline first", file=sys.stderr)
            return 2
        old = json.loads(BASELINE_PATH.read_text())
        d = diff(old, snap, tol=args.tol, time_tol=args.time_tol)
        print_diff(d)
        return 1 if d["regressions"] else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
