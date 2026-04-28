"""Run the anomaly pipeline across all production scenarios and report the
stratified BEHAVIOR / sensor_fault headline.

Expects the companion `synthetic-generator/` project to be a sibling
directory of `anomaly-detection/`, with scenarios already generated under
`synthetic-generator/out/{scenario_name}/`. Override the generator output
root via the SENSORGEN_OUT environment variable if needed.

Production scenarios (eval target): household_60d / household_120d /
household_dense_90d / household_sparse_60d / leak_30d. Holdout
(overfit-check, separate from tuning loop): holdout_household_45d.
"""
from pathlib import Path
import os, sys, time
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
import pandas as pd
from anomaly.pipeline import run
from anomaly.metrics import compute_stratified

ROOT = Path(__file__).resolve().parent.parent
GEN  = Path(os.environ.get("SENSORGEN_OUT", ROOT.parent / "synthetic-generator" / "out"))
CFG  = ROOT / "configs"
OUT  = ROOT / "out"
OUT.mkdir(exist_ok=True)

# (label, scenario_dir_name, config_yaml).
# Detection CSV is OUT/{scenario_dir_name}_detections.csv.
SCENARIOS = [
    ("household_60d",        "household_60d",        CFG / "household.yaml"),
    ("household_120d",       "household_120d",       CFG / "household.yaml"),
    ("household_dense_90d",  "household_dense_90d",  CFG / "household.yaml"),
    ("household_sparse_60d", "household_sparse_60d", CFG / "household.yaml"),
    ("leak_30d",             "leak_30d",             CFG / "leak_30d.yaml"),
    ("holdout_household_45d","holdout_household_45d",CFG / "household.yaml"),
]

results = []
for name, scenario_dir, cfg in SCENARIOS:
    events_csv = GEN / scenario_dir / "events.csv"
    labels_csv = GEN / scenario_dir / "labels.csv"
    det_csv    = OUT / f"{scenario_dir}_detections.csv"
    if not events_csv.exists() or not labels_csv.exists():
        print(f"\n=== {name} ===  SKIP (missing {events_csv} or {labels_csv})",
              flush=True)
        continue
    print(f"\n=== {name} ===", flush=True)
    t0 = time.time()
    run(events_csv, cfg, det_csv, bootstrap_days=14.0)
    elapsed = time.time() - t0
    gt = pd.read_csv(labels_csv)
    det = pd.read_csv(det_csv)
    ev_ts = pd.read_csv(events_csv, usecols=["timestamp"])["timestamp"]
    ev_ts = pd.to_datetime(ev_ts, utc=True, format="ISO8601")
    timeline_days = (ev_ts.max() - ev_ts.min()).total_seconds() / 86400 if len(ev_ts) else 0
    m = compute_stratified(gt, det, timeline_days)
    print(f"  elapsed={elapsed:.1f}s  labels={len(gt)}  dets={len(det)}  timeline={timeline_days:.1f}d")
    for block_name in ("behavior", "sensor_fault"):
        b = m[block_name]
        if b.get("n_labels", 0) == 0:
            print(f"  {block_name:<12} (no labels)")
            continue
        ta = b.get("type_acc")
        ta_s = "  -" if ta is None else f"{ta:.3f}"
        lf = b.get("lat_frac_p95")
        lf_s = "  -" if lf is None else f"{lf:.3f}"
        print(f"  {block_name:<12} n={b['n_labels']:>3d}  incR={b['incident_recall']:.3f}  "
              f"evt_F1={b['evt_f1']:.3f}  fpur={b['fire_purity']:.3f}  "
              f"tyAcc={ta_s}  uvfp/d={b['user_visible_fps_per_day']:.2f}  "
              f"lat%P95={lf_s}")
    results.append({
        "scenario": name,
        "elapsed_s": elapsed,
        "n_labels": len(gt),
        "n_detections": len(det),
        "timeline_days": timeline_days,
        "behavior": m["behavior"],
        "sensor_fault": m["sensor_fault"],
    })

# -- Summary table --------------------------------------------------------
# Grouped by block so the BEHAVIOR row vs sensor_fault row stays visually
# distinct (behavior is the optimization target; sensor_fault is the
# infrastructure side-channel).
print("\n\n=== SUMMARY (BEHAVIOR) ===")
print(f"{'scenario':<24} {'n_lbl':>5} {'incR':>6} {'evt_F1':>7} "
      f"{'fpur':>6} {'tyAcc':>6} {'uvfp/d':>7} {'lat%P95':>8}")
for r in results:
    b = r["behavior"]
    if b.get("n_labels", 0) == 0:
        continue
    ta = b.get("type_acc"); ta_s = "     -" if ta is None else f"{ta:>6.3f}"
    lf = b.get("lat_frac_p95"); lf_s = "       -" if lf is None else f"{lf:>8.3f}"
    print(f"{r['scenario']:<24} {b['n_labels']:>5d} "
          f"{b['incident_recall']:>6.3f} {b['evt_f1']:>7.3f} "
          f"{b['fire_purity']:>6.3f} {ta_s} "
          f"{b['user_visible_fps_per_day']:>7.2f} {lf_s}")

print("\n=== SUMMARY (SENSOR_FAULT) ===")
print(f"{'scenario':<24} {'n_lbl':>5} {'incR':>6} {'evt_F1':>7} "
      f"{'fpur':>6} {'tyAcc':>6} {'uvfp/d':>7} {'lat%P95':>8}")
for r in results:
    b = r["sensor_fault"]
    if b.get("n_labels", 0) == 0:
        continue
    ta = b.get("type_acc"); ta_s = "     -" if ta is None else f"{ta:>6.3f}"
    lf = b.get("lat_frac_p95"); lf_s = "       -" if lf is None else f"{lf:>8.3f}"
    print(f"{r['scenario']:<24} {b['n_labels']:>5d} "
          f"{b['incident_recall']:>6.3f} {b['evt_f1']:>7.3f} "
          f"{b['fire_purity']:>6.3f} {ta_s} "
          f"{b['user_visible_fps_per_day']:>7.2f} {lf_s}")
