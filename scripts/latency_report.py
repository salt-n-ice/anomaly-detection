"""Per-label-type latency report — demo metric.

For each scenario's BEHAVIOR block, computes:

  - correctly-typed-detected labels: those with at least one overlapping
    chain where chain.inferred_type == label.anomaly_type AND
    chain.inferred_class is user_behavior / unknown.
  - per-label alert time: earliest correctly-typed overlapping chain's
    `end` (chain emit / window_end). For deployed real-time the user
    sees the alert at chain emit; immediate detectors (DQG, ST) emit
    at first_fire so end ≈ first_fire there. For fused detectors
    (recent_shift, DCS, RMP) end is the last fire's analysis-window
    end; the 4h fuser inactivity gap on top is uniform and not
    included here (would shift every fused-detector number by +4h).
  - absolute latency = max(0, alert_ts - label.start), in hours.
  - on_time = abs_latency <= MET(anomaly_type).

MET (minimum-evidence-time) per type is the floor below which a
detector physically can't have gathered enough evidence to confidently
classify the type. See discussion in chat for derivation.
"""
from __future__ import annotations
from pathlib import Path
import os, sys
import pandas as pd
import yaml

MET_HOURS: dict[str, float] = {
    # Immediate-trigger types — detector fires on a single tick / event.
    "spike":                    0.5,
    "dropout":                  0.5,
    "extreme_value":            0.5,
    "water_leak_sustained":     0.5,
    "dip":                      1.0,   # CONT recent_shift has 1h analysis window
    # Short-window step-change types.
    "level_shift":              6.0,
    "frequency_change":        12.0,
    # Slow-drift / day-level types — rolling baseline + multi-day evidence.
    "usage_anomaly":           24.0,
    "trend":                   24.0,
    "month_shift":             24.0,
    "calibration_drift":       24.0,
    "degradation_trajectory":  48.0,
    # Calendar-pattern types — need cross-day evidence.
    "weekend_anomaly":         48.0,   # need most of one weekend
    "time_of_day":             72.0,   # need cross-day repetition
    # Defaults.
    "temporal_pattern":        24.0,
    "statistical_anomaly":     12.0,
}

ROOT = Path(__file__).resolve().parent.parent
GEN  = Path(os.environ.get("SENSORGEN_OUT", ROOT.parent / "synthetic-generator" / "out"))
CFG  = ROOT / "configs"
OUT  = ROOT / "out"

SCENARIOS = [
    ("household_60d",         "household.yaml"),
    ("household_120d",        "household.yaml"),
    ("household_dense_90d",   "household.yaml"),
    ("household_sparse_60d",  "household.yaml"),
    ("leak_30d",              "leak_30d.yaml"),
    ("holdout_household_45d", "household.yaml"),
]


def _config_sensors(cfg_path: Path) -> set[tuple[str, str]]:
    cfg = yaml.safe_load(Path(cfg_path).read_text())
    return {(s["id"], s["capability"]) for s in cfg["sensors"]}


def _scenario_records(scen: str, cfg_name: str) -> list[dict]:
    det_csv = OUT / f"{scen}_detections.csv"
    lab_csv = GEN / scen / "labels.csv"
    if not det_csv.exists() or not lab_csv.exists():
        return []
    det = pd.read_csv(det_csv)
    lab = pd.read_csv(lab_csv)
    sensors = _config_sensors(CFG / cfg_name)
    lab = lab[lab.apply(
        lambda r: (r["sensor_id"], r["capability"]) in sensors, axis=1)
    ].reset_index(drop=True)
    for df in (det, lab):
        df["start_dt"] = pd.to_datetime(df["start"], utc=True, format="ISO8601")
        df["end_dt"]   = pd.to_datetime(df["end"],   utc=True, format="ISO8601")
    gt = lab[lab["label_class"] == "user_behavior"].copy()
    cls_ok = (det["inferred_class"] == "user_behavior") | \
             (det["inferred_class"] == "unknown") | \
             det["inferred_class"].isna()
    beh_det = det[cls_ok]
    out = []
    for _, lbl in gt.iterrows():
        sid = lbl["sensor_id"]
        atype = lbl["anomaly_type"]
        ls, le = lbl["start_dt"], lbl["end_dt"]
        cands = beh_det[
            (beh_det["sensor_id"] == sid) &
            (beh_det["inferred_type"] == atype) &
            (beh_det["end_dt"]   >= ls) &
            (beh_det["start_dt"] <= le)
        ]
        if len(cands) == 0:
            continue
        # Earliest chain emit (`end` column).
        earliest_end = cands["end_dt"].min()
        abs_lat_h = max(0.0, (earliest_end - ls).total_seconds() / 3600.0)
        met = MET_HOURS.get(atype, 24.0)
        out.append({
            "scenario":     scen,
            "sensor_id":    sid,
            "anomaly_type": atype,
            "abs_lat_h":    abs_lat_h,
            "met_h":        met,
            "on_time":      abs_lat_h <= met,
            "label_start":  ls,
            "alert_ts":     earliest_end,
            "label_dur_h":  (le - ls).total_seconds() / 3600.0,
        })
    return out


def main() -> int:
    rows = []
    for scen, cfg in SCENARIOS:
        rows.extend(_scenario_records(scen, cfg))
    df = pd.DataFrame(rows)
    if df.empty:
        print("No correctly-typed-detected labels found.", file=sys.stderr)
        return 1

    # Per-scenario block.
    print("=== PER-SCENARIO (BEHAVIOR, correctly-typed-detected only) ===")
    print(f"{'scenario':<25} {'n':>4} {'on_time%':>9} {'median_h':>9} {'max_h':>9}")
    for scen, _ in SCENARIOS:
        sub = df[df["scenario"] == scen]
        if sub.empty:
            print(f"{scen:<25} (no correctly-typed labels)")
            continue
        n = len(sub)
        ot = sub["on_time"].mean() * 100
        med = sub["abs_lat_h"].median()
        mx  = sub["abs_lat_h"].max()
        print(f"{scen:<25} {n:>4d} {ot:>8.1f}% {med:>8.2f}h {mx:>8.2f}h")

    # Per-type aggregation.
    print("\n=== PER-TYPE (across all scenarios) ===")
    print(f"{'anomaly_type':<25} {'MET_h':>6} {'n':>4} {'on_time%':>9} {'median_h':>9} {'max_h':>9}")
    for atype in sorted(df["anomaly_type"].unique()):
        sub = df[df["anomaly_type"] == atype]
        budget = MET_HOURS.get(atype, 24.0)
        n = len(sub)
        ot = sub["on_time"].mean() * 100
        med = sub["abs_lat_h"].median()
        mx  = sub["abs_lat_h"].max()
        print(f"{atype:<25} {budget:>6.1f} {n:>4d} {ot:>8.1f}% {med:>8.2f}h {mx:>8.2f}h")

    # Headline.
    print("\n=== HEADLINE ===")
    print(f"correctly-typed-detected labels: {len(df)}")
    print(f"on-time rate:    {df['on_time'].mean()*100:.1f}%")
    print(f"median latency:  {df['abs_lat_h'].median():.2f}h")
    print(f"max latency:     {df['abs_lat_h'].max():.2f}h")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
