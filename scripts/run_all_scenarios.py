"""Run the anomaly pipeline across all bundled scenarios and report both metrics.

Expects the companion `synthetic-generator/` project to be a sibling directory of
`anomaly-detection/`, with scenarios already generated under
`synthetic-generator/out/{outlet,outlet_tv,outlet_kettle,leak}/`. Override the
generator output root via the SENSORGEN_OUT environment variable if needed.
"""
from pathlib import Path
import os, sys, time
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
import pandas as pd
from anomaly.pipeline import run
from anomaly.metrics import compute_metrics, compute_metrics_pointwise

ROOT = Path(__file__).resolve().parent.parent
GEN  = Path(os.environ.get("SENSORGEN_OUT", ROOT.parent / "synthetic-generator" / "out"))
CFG  = ROOT / "configs"
OUT  = ROOT / "out"
OUT.mkdir(exist_ok=True)

SCENARIOS = [
    ("outlet (fridge+voltage)",  GEN / "outlet" / "events.csv",        CFG / "outlet.yaml",        OUT / "outlet60_detections.csv",   GEN / "outlet" / "labels.csv"),
    ("outlet-tv (tv+voltage)",   GEN / "outlet_tv" / "events.csv",     CFG / "outlet_tv.yaml",     OUT / "outlet_tv_detections.csv",  GEN / "outlet_tv" / "labels.csv"),
    ("outlet-kettle (kettle+voltage)", GEN / "outlet_kettle" / "events.csv", CFG / "outlet_kettle.yaml", OUT / "outlet_kettle_detections.csv", GEN / "outlet_kettle" / "labels.csv"),
    ("waterleak (water+temp+battery)", GEN / "leak" / "events.csv",    CFG / "waterleak.yaml",     OUT / "leak60_detections.csv",     GEN / "leak" / "labels.csv"),
]

results = []
for name, events_csv, cfg, det_csv, labels_csv in SCENARIOS:
    print(f"\n=== {name} ===", flush=True)
    t0 = time.time()
    run(events_csv, cfg, det_csv, bootstrap_days=14.0)
    elapsed = time.time() - t0
    gt = pd.read_csv(labels_csv)
    det = pd.read_csv(det_csv)
    m11 = compute_metrics(gt, det)
    mpw = compute_metrics_pointwise(gt, det)
    burden = (len(det) - mpw['fp']) / max(1, mpw['tp']) if mpw['tp'] else 0
    results.append({
        "scenario": name,
        "elapsed_s": elapsed,
        "n_labels": len(gt),
        "n_detections": len(det),
        "tp_1to1": m11["tp"], "fp_1to1": m11["fp"], "fn_1to1": m11["fn"],
        "prec_1to1": m11["precision"], "recall_1to1": m11["recall"], "f1_1to1": m11["f1"],
        "tp_pw": mpw["tp"], "fp_pw": mpw["fp"], "fn_pw": mpw["fn"],
        "prec_pw": mpw["precision"], "recall_pw": mpw["recall"], "f1_pw": mpw["f1"],
        "alerts_per_incident": burden,
    })
    print(f"  elapsed={elapsed:.1f}s  labels={len(gt)}  dets={len(det)}")
    print(f"  1:1   TP={m11['tp']:>3} FP={m11['fp']:>4} FN={m11['fn']:>2}  P={m11['precision']:.3f} R={m11['recall']:.3f} F1={m11['f1']:.3f}")
    print(f"  pw    TP={mpw['tp']:>3} FP={mpw['fp']:>4} FN={mpw['fn']:>2}  P={mpw['precision']:.3f} R={mpw['recall']:.3f} F1={mpw['f1']:.3f}")
    print(f"  alerts/incident = {burden:.2f}")

print("\n\n=== SUMMARY ===")
print(f"{'scenario':<40} {'dets':>5} {'1:1 F1':>7} {'pw F1':>7} {'pw P':>6} {'pw R':>6} {'burd':>5}")
for r in results:
    print(f"{r['scenario']:<40} {r['n_detections']:>5} {r['f1_1to1']:>7.3f} {r['f1_pw']:>7.3f} {r['prec_pw']:>6.3f} {r['recall_pw']:>6.3f} {r['alerts_per_incident']:>5.2f}")
