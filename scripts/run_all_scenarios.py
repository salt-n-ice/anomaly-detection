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
from anomaly.metrics import (compute_metrics, compute_metrics_pointwise,
                             compute_metrics_event, compute_metrics_time)

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
    ("outlet_short (fridge+voltage, clean)", GEN / "outlet_short" / "events.csv", CFG / "outlet.yaml", OUT / "outlet_short_detections.csv", GEN / "outlet_short" / "labels.csv"),
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
    mev = compute_metrics_event(gt, det)
    mtm = compute_metrics_time(gt, det)
    # Timeline duration from the events CSV (for FP_h/day normalization).
    ev_ts = pd.read_csv(events_csv, usecols=["timestamp"])["timestamp"]
    ev_ts = pd.to_datetime(ev_ts, utc=True, format="ISO8601")
    timeline_days = (ev_ts.max() - ev_ts.min()).total_seconds() / 86400 if len(ev_ts) else 0
    fp_h_per_day = (mtm["fp_sec"] / 3600) / max(1e-6, timeline_days)
    # incident_recall = fraction of GT labels covered by any detection (pointwise recall).
    incident_recall = mpw["recall"]
    # events_per_incident = detector events emitted per labeled incident (alert burden).
    events_per_incident = mev["n_events"] / max(1, len(gt))
    burden = (len(det) - mpw['fp']) / max(1, mpw['tp']) if mpw['tp'] else 0
    results.append({
        "scenario": name,
        "elapsed_s": elapsed,
        "n_labels": len(gt),
        "n_detections": len(det),
        "n_events": mev["n_events"],
        "timeline_days": timeline_days,
        "tp_1to1": m11["tp"], "fp_1to1": m11["fp"], "fn_1to1": m11["fn"],
        "prec_1to1": m11["precision"], "recall_1to1": m11["recall"], "f1_1to1": m11["f1"],
        "tp_ev": mev["tp"], "fp_ev": mev["fp"], "fn_ev": mev["fn"],
        "prec_ev": mev["precision"], "recall_ev": mev["recall"], "f1_ev": mev["f1"],
        "tp_pw": mpw["tp"], "fp_pw": mpw["fp"], "fn_pw": mpw["fn"],
        "prec_pw": mpw["precision"], "recall_pw": mpw["recall"], "f1_pw": mpw["f1"],
        "fp_h": mtm["fp_sec"] / 3600, "fn_h": mtm["fn_sec"] / 3600,
        "time_f1": mtm["time_f1"],
        "incident_recall": incident_recall,
        "fp_h_per_day": fp_h_per_day,
        "events_per_incident": events_per_incident,
        "alerts_per_incident": burden,
    })
    print(f"  elapsed={elapsed:.1f}s  labels={len(gt)}  dets={len(det)}  events={mev['n_events']}  timeline={timeline_days:.1f}d")
    print(f"  1:1   TP={m11['tp']:>3} FP={m11['fp']:>4} FN={m11['fn']:>2}  P={m11['precision']:.3f} R={m11['recall']:.3f} F1={m11['f1']:.3f}")
    print(f"  evt   TP={mev['tp']:>3} FP={mev['fp']:>4} FN={mev['fn']:>2}  P={mev['precision']:.3f} R={mev['recall']:.3f} F1={mev['f1']:.3f}")
    print(f"  pw    TP={mpw['tp']:>3} FP={mpw['fp']:>4} FN={mpw['fn']:>2}  P={mpw['precision']:.3f} R={mpw['recall']:.3f} F1={mpw['f1']:.3f}")
    print(f"  time  FP_h={mtm['fp_sec']/3600:>6.1f} FN_h={mtm['fn_sec']/3600:>5.1f}  P={mtm['time_precision']:.3f} R={mtm['time_recall']:.3f} F1={mtm['time_f1']:.3f}")
    print(f"  incident_recall={incident_recall:.3f}  FP_h/day={fp_h_per_day:.2f}  events/incident={events_per_incident:.2f}  alerts/incident={burden:.2f}")

print("\n\n=== SUMMARY ===")
print(f"{'scenario':<40} {'dets':>5} {'evts':>5} {'evt F1':>7} {'time F1':>8} {'incR':>5} {'fp_h/d':>7} {'ev/inc':>7}")
for r in results:
    print(f"{r['scenario']:<40} {r['n_detections']:>5} {r['n_events']:>5} {r['f1_ev']:>7.3f} {r['time_f1']:>8.3f} {r['incident_recall']:>5.3f} {r['fp_h_per_day']:>7.2f} {r['events_per_incident']:>7.2f}")
