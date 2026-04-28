"""Run the anomaly pipeline across all production scenarios and report the
BEHAVIOR headline (sensor_fault block is computed but not printed —
immediate-trigger DQG detectors rarely move iter-to-iter).

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
    b = m["behavior"]
    if b.get("n_labels", 0) == 0:
        print("  behavior     (no labels)")
    else:
        ta = b.get("type_acc")
        ta_s = "  -" if ta is None else f"{ta:.3f}"
        ot = b.get("on_time_rate")
        ot_s = "    -" if ot is None else f"{ot * 100:.1f}%"
        print(f"  {'behavior':<12} n={b['n_labels']:>3d}  incR={b['incident_recall']:.3f}  "
              f"evt_F1={b['evt_f1']:.3f}  fpur={b['fire_purity']:.3f}  "
              f"tyAcc={ta_s}  uvfp/d={b['user_visible_fps_per_day']:.2f}  "
              f"onTime%={ot_s}")
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
# BEHAVIOR-only — sensor_fault is computed and stored on each result row
# (`r["sensor_fault"]`) for archaeology, but no summary section is
# printed. Immediate-trigger DQG detectors don't shift across iters and
# the row was costing console real estate without informing tuning.
print("\n\n=== SUMMARY (BEHAVIOR) ===")
print(f"{'scenario':<24} {'n_lbl':>5} {'incR':>6} {'evt_F1':>7} "
      f"{'fpur':>6} {'tyAcc':>6} {'uvfp/d':>7} {'onTime%':>8}")
for r in results:
    b = r["behavior"]
    if b.get("n_labels", 0) == 0:
        continue
    ta = b.get("type_acc"); ta_s = "     -" if ta is None else f"{ta:>6.3f}"
    ot = b.get("on_time_rate")
    ot_s = "       -" if ot is None else f"{ot * 100:>7.1f}%"
    print(f"{r['scenario']:<24} {b['n_labels']:>5d} "
          f"{b['incident_recall']:>6.3f} {b['evt_f1']:>7.3f} "
          f"{b['fire_purity']:>6.3f} {ta_s} "
          f"{b['user_visible_fps_per_day']:>7.2f} {ot_s}")
