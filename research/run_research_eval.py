"""Research-loop eval harness — behavior-focused successor.

Runs the household + leak scenarios, prints a compact table, and writes a JSON
snapshot. Headline metric is **behavior-stratified** evt_F1 + incident_recall —
sensor_fault labels (DQG-flavored: dropout, calibration_drift, stuck_at, etc)
are kept in the dataset for realism but excluded from the user-facing
optimization target. The user-facing pipeline summarizes user_behavior labels
to the household via LLM; sensor_fault labels are infrastructure plumbing.

Usage
-----
    python research/run_research_eval.py --suite all
    python research/run_research_eval.py --suite all --diff-baseline
    python research/run_research_eval.py --suite all --save-baseline

Outputs
-------
    research/runs/<timestamp>.json      one JSON per run
    research/runs/latest.json           pointer to the latest
    research/BASELINE.json              frozen baseline (only with --save-baseline)
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
import yaml  # noqa: E402
from anomaly.pipeline import run  # noqa: E402
from anomaly.metrics import (  # noqa: E402
    compute_metrics,
    compute_metrics_pointwise,
    compute_metrics_event,
    compute_metrics_time,
    compute_metrics_latency,
    compute_metrics_onset_timing,
    compute_metrics_by_bucket,
    DURATION_BUCKETS,
)

GEN = Path(os.environ.get("SENSORGEN_OUT", ROOT.parent / "synthetic-generator" / "out"))
CFG = ROOT / "configs"
OUT = ROOT / "out"
RESEARCH_OUT = ROOT / "research" / "runs"
BASELINE_PATH = ROOT / "research" / "BASELINE.json"


# (suite, name, events_dir_name, config_filename, bootstrap_days)
# Three suites:
#   "production" — the three frozen training scenarios that --diff-baseline
#     checks floors against.
#   "holdout" — diverse real-ish scenarios that probe overfit. Floor
#     CROSSINGS on holdout surface as `[OVERFIT WARNING]` in the diff
#     output but never block an accept. Every iter should run at least
#     2 holdout scenarios (--random-sample 2) alongside the production
#     suite to catch regressions on out-of-distribution data.
SCENARIOS: list[tuple[str, str, str, str, float]] = [
    # Production (floors apply, gating)
    ("production", "household_60d",  "household_60d",  "household.yaml", 14.0),
    ("production", "household_120d", "household_120d", "household.yaml", 14.0),
    ("production", "leak_30d",       "leak_30d",       "leak_30d.yaml",  7.0),
    # Holdout (info-only; no gating)
    ("holdout", "holdout_household_45d",   "holdout_household_45d",
     "household.yaml", 14.0),
    ("holdout", "single_outlet_fridge_30d", "single_outlet_fridge_30d",
     "single_outlet_fridge.yaml", 7.0),
    ("holdout", "household_sparse_60d",    "household_sparse_60d",
     "household.yaml", 14.0),
    ("holdout", "household_dense_90d",     "household_dense_90d",
     "household.yaml", 14.0),
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


def _stratify_gt(gt: pd.DataFrame, klass: str) -> pd.DataFrame:
    """Return only the GT labels of a given label_class (user_behavior | sensor_fault).
    Falls back to all labels if the column is missing (legacy datasets)."""
    if "label_class" not in gt.columns:
        return gt
    return gt[gt["label_class"] == klass].reset_index(drop=True)


def _restrict_det_to_sensors(det: pd.DataFrame, gt_subset: pd.DataFrame) -> pd.DataFrame:
    """For per-class precision: a detection is only an FP for THIS class if it
    fired on a sensor that has at least one GT label of THIS class. Otherwise
    a detection on a sensor whose GT labels are all the other class would
    falsely count as a class-FP."""
    sensors = set(gt_subset["sensor_id"].unique())
    if not sensors:
        return det.iloc[0:0]
    return det[det["sensor_id"].isin(sensors)]


def _filter_det_by_class(det: pd.DataFrame, klass: str) -> pd.DataFrame:
    """Keep detections whose claimed class is compatible with `klass`.

    Compatibility: a detection's `inferred_class` must be either `klass`
    itself or `"unknown"` (detector-combo chains that didn't classify
    cleanly). A detection that confidently claims the OTHER class is
    dropped — e.g., a DQG `dropout` claim doesn't count as TP against
    a `water_leak_sustained` GT on the same sensor.

    Falls back to passing everything through when `inferred_class` is
    missing (legacy detection CSVs predate the column)."""
    if "inferred_class" not in det.columns:
        return det
    return det[(det["inferred_class"] == klass)
               | (det["inferred_class"] == "unknown")
               | det["inferred_class"].isna()]


def _count_class_fps_no_overlap(det: pd.DataFrame, all_labels: pd.DataFrame,
                                  klass: str) -> int:
    """Chains classified `klass` with no overlap with any GT label
    (any class) on the same sensor. For klass='user_behavior' this is
    exactly viz selection.user_visible_fps — i.e. the user-visible
    false alarm count rendered in the PDF report.
    """
    if "inferred_class" not in det.columns or len(det) == 0:
        return 0
    cls_chains = det[det["inferred_class"] == klass]
    if len(cls_chains) == 0:
        return 0
    label_intervals: dict[str, list[tuple[pd.Timestamp, pd.Timestamp]]] = {}
    for _, lab in all_labels.iterrows():
        s = pd.Timestamp(lab["start"]); e = pd.Timestamp(lab["end"])
        label_intervals.setdefault(str(lab["sensor_id"]), []).append((s, e))
    n = 0
    for _, row in cls_chains.iterrows():
        sensor = str(row["sensor_id"])
        s = pd.Timestamp(row["start"]); e = pd.Timestamp(row["end"])
        overlaps = False
        for ls, le in label_intervals.get(sensor, []):
            if s <= le and e >= ls:
                overlaps = True
                break
        if not overlaps:
            n += 1
    return n


def _stratified_block(gt: pd.DataFrame, det: pd.DataFrame, klass: str,
                       timeline_days: float) -> dict:
    sub_gt = _stratify_gt(gt, klass)
    sub_det = _restrict_det_to_sensors(det, sub_gt)
    # Type compatibility: a DQG `dropout` claim on the same sensor as a
    # water_leak_sustained GT should NOT count as a TP for the user_behavior
    # block. Filter detections whose inferred_class confidently disagrees
    # with this block's class. Unknown-class detector-combo chains
    # (cusum+mvpca, etc.) stay in both blocks.
    sub_det = _filter_det_by_class(sub_det, klass)
    if sub_gt.empty:
        return {"n_labels": 0}
    mev = compute_metrics_event(sub_gt, sub_det)
    mpw = compute_metrics_pointwise(sub_gt, sub_det)
    mtm = compute_metrics_time(sub_gt, sub_det)
    mlat = compute_metrics_latency(sub_gt, sub_det)
    sub_det_nondqg = sub_det[sub_det["detector"] != "data_quality_gate"]
    mlat_nd = compute_metrics_latency(sub_gt, sub_det_nondqg)
    monset = compute_metrics_onset_timing(sub_gt, sub_det_nondqg)
    # Duration-stratified (short / medium / long) — uses non-DQG detections
    # for latency consistency with the global nondqg_* numbers. Recall numbers
    # use the full detection set so DQG can still "cover" a label.
    by_bucket = compute_metrics_by_bucket(sub_gt, sub_det)
    by_bucket_nd = compute_metrics_by_bucket(sub_gt, sub_det_nondqg)
    # User-visible FP count — chains classified `klass` (untouched by sensor
    # restriction or DQG filter, full detection set) with no overlap with ANY
    # GT label on same sensor. Uses unstratified `gt` so the overlap check
    # honors any-class labels (matches viz user_visible_fps semantics).
    n_uv = _count_class_fps_no_overlap(det, gt, klass)
    fn_h = mtm["fn_sec"] / 3600
    return {
        "n_labels": int(len(sub_gt)),
        "evt_f1": round(float(mev["f1"]), 4),
        "evt_precision": round(float(mev["precision"]), 4),
        "evt_recall": round(float(mev["recall"]), 4),
        "evt_tp": int(mev["tp"]),
        "evt_fp": int(mev["fp"]),
        "evt_fn": int(mev["fn"]),
        "n_events": int(mev["n_events"]),
        "time_f1": round(float(mtm["time_f1"]), 4),
        "time_precision": round(float(mtm["time_precision"]), 4),
        "time_recall": round(float(mtm["time_recall"]), 4),
        "fn_h": round(float(fn_h), 2),
        "n_user_visible_fps": int(n_uv),
        "user_visible_fps_per_day": round(float(n_uv / max(1e-6, timeline_days)), 3),
        "incident_recall": round(float(mpw["recall"]), 4),
        "events_per_incident": round(float(mev["n_events"] / max(1, len(sub_gt))), 3),
        "latency_mean_s": _round_or_none(mlat["latency_mean_s"], 1),
        "latency_p95_s": _round_or_none(mlat["latency_p95_s"], 1),
        "latency_max_s": _round_or_none(mlat["latency_max_s"], 1),
        "nondqg_latency_mean_s": _round_or_none(mlat_nd["latency_mean_s"], 1),
        "nondqg_latency_p95_s": _round_or_none(mlat_nd["latency_p95_s"], 1),
        "nondqg_latency_max_s": _round_or_none(mlat_nd["latency_max_s"], 1),
        "onset_matched_labels": int(monset["n_matched_labels"]),
        "onset_missed_labels": int(monset["n_missed_labels"]),
        "onset_early_labels": int(monset["n_early_labels"]),
        "onset_late_labels": int(monset["n_late_labels"]),
        "onset_early_lead_mean_s": _round_or_none(monset["early_lead_mean_s"], 1),
        "onset_early_lead_p95_s": _round_or_none(monset["early_lead_p95_s"], 1),
        "onset_early_lead_max_s": _round_or_none(monset["early_lead_max_s"], 1),
        "onset_late_start_mean_s": _round_or_none(monset["late_start_mean_s"], 1),
        "onset_late_start_p95_s": _round_or_none(monset["late_start_p95_s"], 1),
        "onset_late_start_max_s": _round_or_none(monset["late_start_max_s"], 1),
        # Per-bucket recall + fractional-latency (short / medium / long).
        # `by_bucket` uses all detections (DQG-inclusive) for recall; the
        # `_nondqg` copy mirrors `nondqg_latency_p95_s` semantics.
        "by_bucket": by_bucket,
        "by_bucket_nondqg": by_bucket_nd,
    }


def score_one(name: str, events_csv: Path, cfg_yaml: Path, labels_csv: Path,
              det_csv: Path, bootstrap_days: float) -> dict:
    t0 = time.time()
    run(events_csv, cfg_yaml, det_csv, bootstrap_days=bootstrap_days)
    elapsed = time.time() - t0

    gt = pd.read_csv(labels_csv)
    # Drop GT labels for sensors not currently configured in cfg_yaml — this
    # mirrors the pipeline's own sensor filter (events on unknown sensors are
    # ignored by `Pipeline.ingest`) and avoids counting those labels as FN
    # when the scenario's config has intentionally disabled a sensor family
    # (e.g., motion disabled for baseline work; re-added later).
    cfg_doc = yaml.safe_load(Path(cfg_yaml).read_text())
    cfg_sensors = {(s["id"], s["capability"]) for s in cfg_doc["sensors"]}
    gt = gt[gt.apply(lambda r: (r["sensor_id"], r["capability"]) in cfg_sensors,
                     axis=1)].reset_index(drop=True)
    det = pd.read_csv(det_csv)
    # Overall (legacy) metrics — kept as a sanity check, but NOT the headline.
    mev = compute_metrics_event(gt, det)
    mpw = compute_metrics_pointwise(gt, det)
    mtm = compute_metrics_time(gt, det)

    ev_ts = pd.to_datetime(
        pd.read_csv(events_csv, usecols=["timestamp"])["timestamp"],
        utc=True, format="ISO8601")
    timeline_days = ((ev_ts.max() - ev_ts.min()).total_seconds() / 86400
                     if len(ev_ts) else 0.0)

    behavior = _stratified_block(gt, det, "user_behavior", timeline_days)
    fault = _stratified_block(gt, det, "sensor_fault", timeline_days)

    return {
        "name": name,
        "elapsed_s": round(elapsed, 2),
        "n_labels": int(len(gt)),
        "n_detections": int(len(det)),
        "n_events": int(mev["n_events"]),
        "timeline_days": round(float(timeline_days), 2),
        # === HEADLINE: user_behavior block (the user-facing alert quality) ===
        "behavior": behavior,
        # === Sensor_fault block (infrastructure: kept for visibility, not optimized) ===
        "sensor_fault": fault,
        # === Overall (all labels mixed) — legacy, NOT the optimization target ===
        "overall_evt_f1": round(float(mev["f1"]), 4),
        "overall_time_f1": round(float(mtm["time_f1"]), 4),
        "overall_incident_recall": round(float(mpw["recall"]), 4),
        "overall_fp_h": round(float(mtm["fp_sec"] / 3600), 2),
        "overall_fp_h_per_day": round(float(
            (mtm["fp_sec"] / 3600) / max(1e-6, timeline_days)), 3),
    }


def _round_or_none(x, ndigits: int):
    return None if x is None else round(float(x), ndigits)


def filter_suite(suite: str, random_sample: int = 0
                 ) -> list[tuple[str, str, str, str, float]]:
    """Pick the scenarios for a run.

    - 'all'        : every scenario (production + holdout)
    - 'production' : only the 3 production scenarios
    - 'holdout'    : only the 4 holdout scenarios
    - 'iter'       : production + `random_sample` random holdout scenarios
                     (this is the default for a tuning iter — keeps total
                     runtime < 6 min while still sampling out-of-distribution
                     data each iter to catch overfit early).
    - Named suite  : legacy single-name match (e.g., '60d', 'holdout')
    """
    import random
    if suite == "all":
        return SCENARIOS
    if suite == "production":
        return [s for s in SCENARIOS if s[0] != "holdout"]
    if suite == "iter":
        prod = [s for s in SCENARIOS if s[0] != "holdout"]
        held = [s for s in SCENARIOS if s[0] == "holdout"]
        n = max(0, min(random_sample, len(held)))
        sampled = random.sample(held, n) if n > 0 else []
        return prod + sampled
    return [s for s in SCENARIOS if s[0] == suite]


def aggregate(results: list[dict]) -> dict:
    """Aggregate across scenarios, focused on the user_behavior block.
    Sensor_fault block is summarized separately for visibility only."""

    def _safe_mean(vals):
        vals = [v for v in vals if v is not None]
        return round(sum(vals) / len(vals), 4) if vals else None

    def _safe_max(vals):
        vals = [v for v in vals if v is not None]
        return round(max(vals), 1) if vals else None

    def _safe_min(vals):
        vals = [v for v in vals if v is not None]
        return round(min(vals), 4) if vals else None

    def _agg(subset: list[dict]) -> dict:
        if not subset:
            return {}
        beh = [r["behavior"] for r in subset if r["behavior"].get("n_labels", 0) > 0]
        flt = [r["sensor_fault"] for r in subset if r["sensor_fault"].get("n_labels", 0) > 0]
        return {
            "n": len(subset),
            # USER_BEHAVIOR (headline)
            "behavior_mean_evt_f1": _safe_mean([b["evt_f1"] for b in beh]),
            "behavior_mean_time_f1": _safe_mean([b["time_f1"] for b in beh]),
            "behavior_mean_incident_recall": _safe_mean([b["incident_recall"] for b in beh]),
            "behavior_mean_user_visible_fps_per_day":
                _safe_mean([b["user_visible_fps_per_day"] for b in beh]),
            "behavior_total_n_user_visible_fps":
                int(sum(b["n_user_visible_fps"] for b in beh)),
            "behavior_worst_evt_f1": _safe_min([b["evt_f1"] for b in beh]),
            "behavior_worst_incident_recall": _safe_min([b["incident_recall"] for b in beh]),
            "behavior_worst_nondqg_latency_p95_s":
                _safe_max([b["nondqg_latency_p95_s"] for b in beh]),
            "behavior_mean_nondqg_latency_mean_s":
                _safe_mean([b["nondqg_latency_mean_s"] for b in beh]),
            "behavior_mean_onset_early_labels":
                _safe_mean([b["onset_early_labels"] for b in beh]),
            "behavior_mean_onset_late_labels":
                _safe_mean([b["onset_late_labels"] for b in beh]),
            "behavior_worst_onset_early_lead_p95_s":
                _safe_max([b["onset_early_lead_p95_s"] for b in beh]),
            "behavior_worst_onset_late_start_p95_s":
                _safe_max([b["onset_late_start_p95_s"] for b in beh]),
            # SENSOR_FAULT (visibility only)
            "fault_mean_evt_f1": _safe_mean([f["evt_f1"] for f in flt]),
            "fault_mean_incident_recall": _safe_mean([f["incident_recall"] for f in flt]),
        }
    by_suite: dict[str, list[dict]] = {}
    for r in results:
        by_suite.setdefault(r["suite"], []).append(r)
    agg = {"all": _agg(results)}
    for suite, subset in by_suite.items():
        agg[suite] = _agg(subset)
    return agg


def run_suite(suite: str, random_sample: int = 0) -> dict:
    OUT.mkdir(exist_ok=True)
    RESEARCH_OUT.mkdir(parents=True, exist_ok=True)
    results: list[dict] = []
    skipped: list[dict] = []
    for suite_tag, name, events_dir, cfg_name, bootstrap_days in filter_suite(suite, random_sample):
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
        b = r["behavior"]
        f = r["sensor_fault"]
        print(f"  BEHAVIOR  evt_F1={b.get('evt_f1', 0):.3f}  time_F1={b.get('time_f1', 0):.3f}  "
              f"incR={b.get('incident_recall', 0):.3f}  "
              f"uv_fp/d={b.get('user_visible_fps_per_day', 0):.2f}  "
              f"uv_fp={b.get('n_user_visible_fps', 0)}  "
              f"nd_lat_p95={(b.get('nondqg_latency_p95_s') or 0):.0f}s")
        print(f"            onset early={b.get('onset_early_labels', 0)}/{b.get('onset_matched_labels', 0)}  "
              f"early_p95={(b.get('onset_early_lead_p95_s') or 0):.0f}s  "
              f"late={b.get('onset_late_labels', 0)}/{b.get('onset_matched_labels', 0)}  "
              f"late_p95={(b.get('onset_late_start_p95_s') or 0):.0f}s")
        if f.get("n_labels", 0):
            print(f"  FAULT     evt_F1={f.get('evt_f1', 0):.3f}  incR={f.get('incident_recall', 0):.3f}  "
                  f"sf_fp/d={f.get('user_visible_fps_per_day', 0):.2f}  "
                  f"(infrastructure — not optimized)")
        print(f"  elapsed={r['elapsed_s']:.1f}s")

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
    print("\n=== USER-BEHAVIOR HEADLINE (the user-facing alert quality) ===")
    hdr = (f"{'scenario':<22} {'evt F1':>7} {'time F1':>8} {'incR':>6} "
           f"{'uv_fp/d':>8} {'uv_fp':>6} {'nd_lat_p95':>11} {'#labels':>8}")
    print(hdr); print("-" * len(hdr))
    for r in snapshot["scenarios"]:
        b = r["behavior"]
        if not b.get("n_labels"):
            continue
        print(f"{r['name']:<22} {b['evt_f1']:>7.3f} {b['time_f1']:>8.3f} "
              f"{b['incident_recall']:>6.3f} "
              f"{b['user_visible_fps_per_day']:>8.2f} "
              f"{b['n_user_visible_fps']:>6} "
              f"{(b.get('nondqg_latency_p95_s') or 0):>10.0f}s "
              f"{b['n_labels']:>8}")

    print("\n=== DURATION-STRATIFIED BEHAVIOR (short / medium / long GT labels) ===")
    bhdr = (f"{'scenario':<22} {'bucket':<8} {'#lbl':>5} {'incR':>6} "
            f"{'t_rec':>6} {'lat_frac_p95':>13}")
    print(bhdr); print("-" * len(bhdr))
    for r in snapshot["scenarios"]:
        bb = (r.get("behavior") or {}).get("by_bucket", {}) or {}
        if not bb:
            continue
        for bname, _, _ in DURATION_BUCKETS:
            b = bb.get(bname) or {}
            if not b.get("n_labels"):
                continue
            print(f"{r['name']:<22} {bname:<8} {b['n_labels']:>5} "
                  f"{(b.get('incident_recall') or 0):>6.3f} "
                  f"{(b.get('time_recall') or 0):>6.3f} "
                  f"{(b.get('lat_frac_p95') or 0):>12.2%}")

    print("\n=== SENSOR_FAULT block (infrastructure — kept for visibility, not optimized) ===")
    print("\n=== ONSET TIMING AUDIT (nondqg detections only) ===")
    ohdr = (f"{'scenario':<22} {'early':>11} {'early_p95':>11} "
            f"{'late':>10} {'late_p95':>10} {'miss':>6}")
    print(ohdr); print("-" * len(ohdr))
    for r in snapshot["scenarios"]:
        b = r["behavior"]
        if not b.get("n_labels"):
            continue
        matched = b.get("onset_matched_labels", 0)
        print(f"{r['name']:<22} "
              f"{b.get('onset_early_labels', 0):>3}/{matched:<7} "
              f"{(b.get('onset_early_lead_p95_s') or 0):>10.0f}s "
              f"{b.get('onset_late_labels', 0):>3}/{matched:<6} "
              f"{(b.get('onset_late_start_p95_s') or 0):>9.0f}s "
              f"{b.get('onset_missed_labels', 0):>6}")

    fhdr = (f"{'scenario':<22} {'evt F1':>7} {'incR':>6} {'sf_fp/d':>8} {'sf_fp':>6} {'#labels':>8}")
    print(fhdr); print("-" * len(fhdr))
    for r in snapshot["scenarios"]:
        f = r["sensor_fault"]
        if not f.get("n_labels"):
            continue
        print(f"{r['name']:<22} {f['evt_f1']:>7.3f} {f['incident_recall']:>6.3f} "
              f"{f['user_visible_fps_per_day']:>8.2f} "
              f"{f['n_user_visible_fps']:>6} {f['n_labels']:>8}")

    for suite_tag, agg in snapshot["aggregate"].items():
        if not agg: continue
        print(f"\n[{suite_tag}] n={agg['n']}  "
              f"BEHAVIOR mean evt_F1={(agg.get('behavior_mean_evt_f1') or 0):.3f}  "
              f"mean incR={(agg.get('behavior_mean_incident_recall') or 0):.3f}  "
              f"mean time_F1={(agg.get('behavior_mean_time_f1') or 0):.3f}  "
              f"worst evt_F1={(agg.get('behavior_worst_evt_f1') or 0):.3f}  "
              f"worst incR={(agg.get('behavior_worst_incident_recall') or 0):.3f}  "
              f"worst nd_lat_p95={(agg.get('behavior_worst_nondqg_latency_p95_s') or 0):.0f}s  "
              f"mean uv_fp/d={(agg.get('behavior_mean_user_visible_fps_per_day') or 0):.2f}  "
              f"total uv_fp={agg.get('behavior_total_n_user_visible_fps') or 0}")


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
         time_tol: float = 0.02, lat_tol_s: float = 600.0,
         fp_rise_tol_rel: float = 0.10,
         fp_abs_budget: float | None = None,
         bucket_incR_tol: float = 0.005,
         bucket_time_rec_tol: float = 0.05,
         bucket_lat_frac_ceil: float = 0.10) -> dict:
    """Per-scenario delta on the BEHAVIOR block (the optimization target).

    A scenario is a REGRESSION if any of:
      AGGREGATE floors (pipeline-wide):
      - behavior.incident_recall drops by more than `tol` (default 0.005).
      - behavior.time_f1 drops by more than `time_tol` (default 0.02).
      - behavior.nondqg_latency_p95_s rises by more than `lat_tol_s`
        (default 600s = 10min).
      - behavior.user_visible_fps_per_day rises by more than `fp_rise_tol_rel`
        relative (default +10%). If `fp_abs_budget` is set and the old
        baseline has uv_fp/d near 0 (< 0.5), an ABSOLUTE budget applies
        instead of the relative one — this handles the Stage 0 → Stage 1
        transition where relative rise is undefined.

      PER-BUCKET floors (short / medium / long anomaly durations):
      - any bucket's incident_recall drops by more than `bucket_incR_tol`
        (default 0.005) — short anomalies can't be starved.
      - any bucket's time_recall drops by more than `bucket_time_rec_tol`
        (default 0.05) — coverage-fraction regression on any band fails.
      - any bucket's lat_frac_p95 rises above `bucket_lat_frac_ceil`
        (default 0.10 = 10% of the GT label elapsed before first alert).
        This replaces the flat 600s latency floor, which was lethal on
        short labels (600s = 33% of a 30-min leak) and trivial on long
        ones (600s = 0.03% of a 28-day shift).

    `evt_f1` is reported (as `d_evt_f1`) but is NOT a regression criterion:
    chain-merge / chain-suppression changes routinely swing it ±0.05-0.10
    via the 1h merge-gap artifact.

    Sensor_fault metrics are reported in the diff for visibility but do NOT
    trigger a regression — they're infrastructure plumbing.
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
        ob = old_map[name]["behavior"]
        nb = new_map[name]["behavior"]
        if not ob.get("n_labels") or not nb.get("n_labels"):
            continue  # nothing to diff
        d_evt = round(nb["evt_f1"] - ob["evt_f1"], 4)
        d_time = round(nb["time_f1"] - ob["time_f1"], 4)
        d_incR = round(nb["incident_recall"] - ob["incident_recall"], 4)
        old_fp = ob["user_visible_fps_per_day"]
        new_fp = nb["user_visible_fps_per_day"]
        d_fp = round(new_fp - old_fp, 3)
        # Relative fp rise: protects against scenarios where a small absolute
        # uv_fp/d rise (e.g., +0.2/d) is actually >10% relative on a low-FP
        # scenario.
        fp_rise_rel = (new_fp - old_fp) / max(old_fp, 1e-6) if old_fp > 0 else 0.0
        d_uv_fp_count = int(nb["n_user_visible_fps"]) - int(ob["n_user_visible_fps"])
        old_lat = ob.get("nondqg_latency_p95_s") or 0
        new_lat = nb.get("nondqg_latency_p95_s") or 0
        d_lat = round(new_lat - old_lat, 1)
        row = {
            "name": name,
            "suite": new_map[name]["suite"],
            "d_evt_f1": d_evt, "d_time_f1": d_time, "d_incR": d_incR,
            "d_uv_fp_d": d_fp, "fp_rise_rel": round(fp_rise_rel, 3),
            "d_uv_fp_count": d_uv_fp_count,
            "d_nondqg_lat_p95_s": d_lat,
        }
        # Per-bucket floors (short / medium / long).
        bucket_violations: list[str] = []
        ob_bkt = ob.get("by_bucket", {}) or {}
        nb_bkt = nb.get("by_bucket", {}) or {}
        for bname in ("short", "medium", "long"):
            ob_b = ob_bkt.get(bname, {}) or {}
            nb_b = nb_bkt.get(bname, {}) or {}
            if not nb_b.get("n_labels") or not ob_b.get("n_labels"):
                continue
            d_bincR = (nb_b.get("incident_recall") or 0) - (ob_b.get("incident_recall") or 0)
            d_btrec = (nb_b.get("time_recall") or 0) - (ob_b.get("time_recall") or 0)
            nb_lf = nb_b.get("lat_frac_p95") or 0
            if d_bincR < -bucket_incR_tol:
                bucket_violations.append(f"{bname}.incR{d_bincR:+.3f}")
            if d_btrec < -bucket_time_rec_tol:
                bucket_violations.append(f"{bname}.time_rec{d_btrec:+.3f}")
            if nb_lf > bucket_lat_frac_ceil:
                bucket_violations.append(f"{bname}.lat_frac={nb_lf:.2%}")
        row["bucket_violations"] = bucket_violations

        # FP budget: relative rise by default; absolute budget if old baseline
        # is near-zero (Stage 0 → Stage 1 transition).
        if fp_abs_budget is not None and old_fp < 0.5:
            fp_violation = new_fp > fp_abs_budget
            row["fp_mode"] = f"abs(<={fp_abs_budget})"
        else:
            fp_violation = fp_rise_rel > fp_rise_tol_rel
            row["fp_mode"] = "rel"

        is_holdout = new_map[name]["suite"] == "holdout"
        floor_hit = (d_incR < -tol or d_time < -time_tol or d_lat > lat_tol_s
                     or fp_violation or bool(bucket_violations))
        if floor_hit and not is_holdout:
            # Only production scenarios gate the accept/reject decision.
            regressions.append(row)
        elif floor_hit and is_holdout:
            # Holdout floor hit is a WARNING, not a regression — surfaces
            # overfit but does not block acceptance (the rule still has
            # to prove itself on production metrics, and holdout is
            # diagnostic).
            row["holdout_warning"] = True
            neutral.append(row)
        elif d_time > time_tol or fp_rise_rel < -fp_rise_tol_rel or d_lat < -lat_tol_s:
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
    print("\n=== DIFF vs baseline (BEHAVIOR block) ===")
    print("(agg floors: incR -0.005, time_F1 -0.02, uv_fp/d +10% rel, nd_lat_p95 +600s)")
    print("(bucket floors: incR -0.005, time_recall -0.05, lat_frac_p95 < 0.10)")
    # Surface holdout floor crossings in their own section — they're
    # warnings, not gates, but they need visibility.
    holdout_warnings = [r for r in d["neutral"] if r.get("holdout_warning")]
    if holdout_warnings:
        print(f"\n[OVERFIT WARNINGS] ({len(holdout_warnings)}) — holdout "
              f"scenario crossed a floor that would have regressed on production")
        for r in holdout_warnings:
            print(f"  {r['name']:<28} d_time_F1={r['d_time_f1']:+.3f}  "
                  f"d_incR={r['d_incR']:+.3f}  fp_rise={r['fp_rise_rel']:+.1%}  "
                  f"d_uv_fp_count={r['d_uv_fp_count']:+d}  "
                  f"d_nd_lat_p95={r['d_nondqg_lat_p95_s']:+.0f}s")
    for group, rows in [("REGRESSIONS", d["regressions"]),
                        ("IMPROVEMENTS", d["improvements"]),
                        ("NEUTRAL",     d["neutral"])]:
        if group == "NEUTRAL":
            rows = [r for r in rows if not r.get("holdout_warning")]
        print(f"\n[{group}] ({len(rows)})")
        for r in rows:
            suite_tag = ""
            if r.get("suite") == "holdout":
                suite_tag = " [holdout]"
            viols = r.get("bucket_violations") or []
            viol_tag = f"  buckets={','.join(viols)}" if viols else ""
            print(f"  {r['name']:<28}{suite_tag} d_time_F1={r['d_time_f1']:+.3f}  "
                  f"d_incR={r['d_incR']:+.3f}  fp_rise={r['fp_rise_rel']:+.1%}  "
                  f"d_uv_fp_count={r['d_uv_fp_count']:+d}  "
                  f"d_nd_lat_p95={r['d_nondqg_lat_p95_s']:+.0f}s  "
                  f"(d_evt_F1={r['d_evt_f1']:+.3f}){viol_tag}")
    if d["new_only"]:
        print(f"\n[NEW_ONLY] {d['new_only']}")
    if d["dropped"]:
        print(f"[DROPPED]  {d['dropped']}")


# ------------------------------- CLI -------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", choices=["all", "iter", "production",
                                         "holdout", "60d", "120d", "30d"],
                    default="iter",
                    help="'iter' (default): production + N random holdout "
                         "scenarios (set N via --random-sample). Use this "
                         "for every tuning iter. 'production' = 60d+120d"
                         "+30d only. 'holdout' = all 4 holdout scenarios. "
                         "'all' = production + all holdout.")
    ap.add_argument("--random-sample", type=int, default=2,
                    help="When --suite=iter, number of holdout scenarios "
                         "to randomly sample (default 2). 0 disables "
                         "holdout sampling (legacy 3-scenario behavior).")
    ap.add_argument("--save-baseline", action="store_true",
                    help="Freeze the current run as research/BASELINE.json.")
    ap.add_argument("--diff-baseline", action="store_true",
                    help="After running, diff against research/BASELINE.json and exit 1 on regression.")
    ap.add_argument("--tol", type=float, default=0.005,
                    help="Tolerance for incident_recall regressions on BEHAVIOR "
                         "block (default 0.005). Recall loss is real quality "
                         "loss; this floor stays tight.")
    ap.add_argument("--time-tol", type=float, default=0.02,
                    help="Tolerance for time_f1 regressions (default 0.02).")
    ap.add_argument("--lat-tol-s", type=float, default=600.0,
                    help="Tolerance for nondqg_latency_p95 increases on BEHAVIOR "
                         "block (default 600s = 10min).")
    ap.add_argument("--fp-rise-tol-rel", type=float, default=0.10,
                    help="Tolerance for user_visible_fps_per_day RELATIVE "
                         "rise on BEHAVIOR block (default 0.10 = +10%%). "
                         "Protects against silent user-notification "
                         "volume worsening.")
    ap.add_argument("--fp-abs-budget", type=float, default=None,
                    help="Absolute uv_fp/d budget. Applied instead of the "
                         "relative rise when the old baseline has uv_fp/d "
                         "near 0 (< 0.5) — covers Stage 0 → Stage 1 "
                         "where relative rise is undefined. e.g. "
                         "--fp-abs-budget 1.0 means 'new pipeline must "
                         "stay under 1 user-visible FP per day'.")
    ap.add_argument("--bucket-incR-tol", type=float, default=0.005,
                    help="Per-bucket incident_recall floor (default 0.005). "
                         "Any single duration bucket (short/medium/long) "
                         "whose incR drops by more than this fails.")
    ap.add_argument("--bucket-time-rec-tol", type=float, default=0.05,
                    help="Per-bucket time_recall floor (default 0.05). "
                         "Any bucket whose coverage fraction drops by "
                         "more than this fails.")
    ap.add_argument("--bucket-lat-frac-ceil", type=float, default=0.10,
                    help="Per-bucket fractional latency ceiling "
                         "(default 0.10 = 10%% of GT duration). Replaces "
                         "the flat 600s floor which over-penalized long "
                         "labels and under-penalized short ones.")
    args = ap.parse_args(argv)

    snap = run_suite(args.suite, random_sample=args.random_sample)
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
        d = diff(old, snap, tol=args.tol, time_tol=args.time_tol,
                 lat_tol_s=args.lat_tol_s,
                 fp_rise_tol_rel=args.fp_rise_tol_rel,
                 fp_abs_budget=args.fp_abs_budget,
                 bucket_incR_tol=args.bucket_incR_tol,
                 bucket_time_rec_tol=args.bucket_time_rec_tol,
                 bucket_lat_frac_ceil=args.bucket_lat_frac_ceil)
        print_diff(d)
        return 1 if d["regressions"] else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
