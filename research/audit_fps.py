"""Per-scenario FP attribution audit.

Loads each scenario's labels.csv + detections.csv, applies the
viz `user_visible_fps` definition (inferred_class == 'user_behavior'
AND no GT-label overlap on the same sensor — labels of ANY class
shield), then aggregates the FP chain rows by (sensor, detector,
inferred_type) so we can see where the FP budget is spent.

Run from anomaly-detection/:  python research/audit_fps.py
"""
from __future__ import annotations
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from run_research_eval import SCENARIOS  # type: ignore

SYNTH_OUT = ROOT.parent / "synthetic-generator" / "out"
DET_OUT = ROOT / "out"


def load(scenario_tuple):
    suite, name, events_dir, _cfg, _boot = scenario_tuple
    labels_path = SYNTH_OUT / events_dir / "labels.csv"
    dets_path = DET_OUT / f"{name}_detections.csv"
    labels = pd.read_csv(labels_path, parse_dates=["start", "end"])
    dets = pd.read_csv(dets_path,
                       parse_dates=["start", "end", "first_fire_ts"])
    return suite, name, labels, dets


def fp_chains(labels, dets):
    """Chains with inferred_class=user_behavior AND no overlap with any
    GT label on the same sensor. Mirrors viz selection.user_visible_fps
    AND eval _count_class_fps_no_overlap(klass='user_behavior')."""
    by_sensor = {}
    for _, lab in labels.iterrows():
        by_sensor.setdefault(lab["sensor_id"], []).append((lab["start"], lab["end"]))

    def is_fp(row):
        if row.get("inferred_class") != "user_behavior":
            return False
        for s, e in by_sensor.get(row["sensor_id"], []):
            if row["start"] <= e and row["end"] >= s:
                return False
        return True

    return dets[dets.apply(is_fp, axis=1)].copy()


def tp_attribution(labels, dets):
    """For each label, find which (detector, sensor) combos overlap it.
    Returns rows: (label_sensor, label_anomaly_type, detector, n_chains).
    """
    out = []
    for _, lab in labels.iterrows():
        if lab.get("label_class") != "user_behavior":
            continue
        same = dets[dets["sensor_id"] == lab["sensor_id"]]
        ovl = same[(same["start"] <= lab["end"]) & (same["end"] >= lab["start"])]
        for det, c in ovl.groupby("detector").size().items():
            out.append((lab["sensor_id"], lab["anomaly_type"], det, int(c)))
    return out


def main():
    summary = []
    for sc in SCENARIOS:
        if sc[0] != "production":
            continue
        try:
            suite, name, labels, dets = load(sc)
        except FileNotFoundError as e:
            print(f"  skip {sc[1]}: {e}")
            continue
        fps = fp_chains(labels, dets)
        n = len(fps)
        if len(dets):
            days = max(1.0, (dets["end"].max() - dets["start"].min()).total_seconds() / 86400)
        else:
            days = 1.0
        print(f"\n=== {name}  total user-visible FPs = {n}  ({n/days:.2f}/d, span {days:.1f}d) ===")

        if n == 0:
            continue

        print("\n  by sensor:")
        for s, c in fps.groupby("sensor_id").size().sort_values(ascending=False).items():
            print(f"    {s:30s} {c:5d}")

        print("\n  by detector:")
        for d, c in fps.groupby("detector").size().sort_values(ascending=False).items():
            print(f"    {d:55s} {c:5d}")

        print("\n  by (sensor, detector):")
        gb = fps.groupby(["sensor_id", "detector"]).size().sort_values(ascending=False)
        for (s, d), c in gb.head(25).items():
            print(f"    {s:30s} {d:55s} {c:5d}")

        print("\n  by (sensor, inferred_type):")
        gb = fps.groupby(["sensor_id", "inferred_type"]).size().sort_values(ascending=False)
        for (s, t), c in gb.head(20).items():
            print(f"    {s:30s} {t:30s} {c:5d}")

        # TP attribution per label
        print("\n  TP attribution (label -> detectors that overlap):")
        beh_labels = labels[labels["label_class"] == "user_behavior"]
        tp_rows = tp_attribution(labels, dets)
        # Count: for how many labels did each (sensor, detector) overlap?
        from collections import defaultdict
        labels_caught = defaultdict(set)  # (sensor, detector) -> set of label_ids
        for i, lab in beh_labels.reset_index().iterrows():
            same = dets[dets["sensor_id"] == lab["sensor_id"]]
            ovl = same[(same["start"] <= lab["end"]) & (same["end"] >= lab["start"])]
            for det in ovl["detector"].unique():
                labels_caught[(lab["sensor_id"], det)].add(i)
        # also: which labels would be MISSED if we removed a particular (sensor, detector)?
        # Compute: for each (sensor, detector), how many labels are caught ONLY by this combo?
        # (i.e. not caught by any other detector on the same sensor)
        per_label_dets = {}  # i -> set of (sensor, detector) combos
        for (s, d), ids in labels_caught.items():
            for i in ids:
                per_label_dets.setdefault(i, set()).add((s, d))
        only_caught_by = defaultdict(set)
        for i, combos in per_label_dets.items():
            if len(combos) == 1:
                only_caught_by[next(iter(combos))].add(i)
        print(f"    {'sensor':30s} {'detector':45s}  caught  unique-only  fps")
        all_keys = set(labels_caught) | {(s, d) for (s, d), _ in fps.groupby(["sensor_id", "detector"])}
        for s, d in sorted(all_keys, key=lambda k: -len(labels_caught.get(k, set()))):
            ncaught = len(labels_caught.get((s, d), set()))
            nonly = len(only_caught_by.get((s, d), set()))
            nfp = int(((fps["sensor_id"] == s) & (fps["detector"] == d)).sum())
            print(f"    {s:30s} {d:45s}  {ncaught:5d}  {nonly:10d}   {nfp:5d}")
        summary.append((name, n, days, n/days))

    if summary:
        print("\n=== summary (production) ===")
        for name, n, days, rate in summary:
            print(f"  {name:30s} {n:5d} FPs / {days:6.1f}d = {rate:.3f}/d")
        total_n = sum(x[1] for x in summary)
        total_days = sum(x[2] for x in summary)
        print(f"  {'TOTAL':30s} {total_n:5d} FPs / {total_days:6.1f}d = {total_n/total_days:.3f}/d")

    # Per-label MAX-TP-score audit: for each label, find the max DCS-6h
    # firing score that overlaps it. The min over those maxes is the
    # highest z_threshold that preserves ALL TP labels.
    print("\n=== DCS-6h per-label MAX firing score (label is caught if any "
          "firing within label window exceeds z_threshold) ===")
    for sc in SCENARIOS:
        if sc[0] != "production":
            continue
        suite, name, labels, dets = load(sc)
        beh = labels[labels["label_class"] == "user_behavior"]
        dcs = dets[dets["detector"].str.contains("duty_cycle_shift_6h", na=False)]
        rows = []
        for _, lab in beh.iterrows():
            same = dcs[dcs["sensor_id"] == lab["sensor_id"]]
            ovl = same[(same["start"] <= lab["end"]) & (same["end"] >= lab["start"])]
            if len(ovl) == 0:
                continue
            rows.append((lab["sensor_id"], lab["anomaly_type"],
                          lab["end"] - lab["start"], len(ovl),
                          float(ovl["score"].max())))
        if not rows:
            continue
        print(f"\n  {name}:")
        for s, t, dur, n, mx in sorted(rows, key=lambda r: r[4]):
            print(f"    {s:25s} {t:25s} dur={dur} n_fires={n:3d} max_z={mx:.2f}")

    # Score-distribution audit: for each (sensor, detector) bucket where
    # detector == duty_cycle_shift_6h, print FP score distribution and the
    # MIN score on TPs (overlapping any label). The min-TP-score sets the
    # lower bound for how high we can lift z_threshold without losing TPs.
    print("\n=== DCS-6h score distribution (FP vs TP min) ===")
    for sc in SCENARIOS:
        if sc[0] != "production":
            continue
        suite, name, labels, dets = load(sc)
        dcs = dets[dets["detector"].str.contains("duty_cycle_shift_6h", na=False)]
        if len(dcs) == 0:
            continue
        # FP rows
        fps = fp_chains(labels, dets)
        fp_dcs = fps[fps["detector"].str.contains("duty_cycle_shift_6h", na=False)]
        # TP rows: dcs detections that overlap a behavior label on the same sensor
        beh_labels = labels[labels["label_class"] == "user_behavior"]
        def is_tp(row):
            same = beh_labels[beh_labels["sensor_id"] == row["sensor_id"]]
            return any((row["start"] <= e and row["end"] >= s)
                        for s, e in zip(same["start"], same["end"]))
        tp_dcs = dcs[dcs.apply(is_tp, axis=1)]
        print(f"\n  {name}:")
        for sensor in sorted(dcs["sensor_id"].unique()):
            s_fp = fp_dcs[fp_dcs["sensor_id"] == sensor]["score"]
            s_tp = tp_dcs[tp_dcs["sensor_id"] == sensor]["score"]
            if len(s_fp) == 0 and len(s_tp) == 0:
                continue
            fp_q = (s_fp.quantile([0.5, 0.75, 0.9, 0.95, 0.99]).values.tolist()
                     if len(s_fp) else [])
            tp_min = float(s_tp.min()) if len(s_tp) else None
            tp_max = float(s_tp.max()) if len(s_tp) else None
            print(f"    {sensor:25s} FP n={len(s_fp):4d} q50/75/90/95/99={fp_q}  "
                  f"TP n={len(s_tp):3d} min={tp_min} max={tp_max}")


if __name__ == "__main__":
    main()
