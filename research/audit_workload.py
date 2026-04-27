"""Workload fingerprint builder.

Run once per stage boundary to cache what the current scenarios actually
contain — anomaly-type/archetype breakdowns, sensor physics (ZOH fraction,
cadence), and a rough anomaly-shape tally. Used by Stage-N candidate
selection so proposals are grounded in the real workload, not the
pre-redesign detector inventory.

Usage:
    python research/audit_workload.py

Writes: research/WORKLOAD_FINGERPRINT.json
"""
from __future__ import annotations
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "research"))

from run_research_eval import SCENARIOS, GEN, CFG  # noqa: E402

OUT_PATH = ROOT / "research" / "WORKLOAD_FINGERPRINT.json"

# Duration-bucket thresholds (seconds) — must match metrics.DURATION_BUCKETS.
BUCKETS = [("short", 0.0, 3600.0),
           ("medium", 3600.0, 86400.0),
           ("long", 86400.0, float("inf"))]

# Anomaly-type → shape_distribution category, per survey spec.
SHAPE_MAP = {
    "spike": "spike_dip", "dip": "spike_dip",
    "level_shift": "level_shift", "month_shift": "level_shift",
    "water_leak_sustained": "level_shift",
    "trend": "drift", "degradation_trajectory": "drift",
    "calibration_drift": "drift",
    "frequency_change": "regime", "seasonality_loss": "regime",
    "time_of_day": "seasonal", "weekend_anomaly": "seasonal",
    "seasonal_mismatch": "seasonal",
    # unusual_occupancy is handled case-wise below
}


def _bucket(d_s: float) -> str:
    for name, lo, hi in BUCKETS:
        if lo <= d_s < hi:
            return name
    return "long"


def _shape_for(atype: str, archetype: str) -> str:
    if atype == "unusual_occupancy":
        return "rate_change" if archetype == "BINARY" else "regime"
    return SHAPE_MAP.get(atype, "other")


def _load_config(cfg_file: str) -> dict[str, dict]:
    path = CFG / cfg_file
    with path.open("r") as fh:
        raw = yaml.safe_load(fh)
    out = {}
    for s in raw["sensors"]:
        out[s["id"]] = {
            "archetype": s["archetype"].upper(),
            "capability": s["capability"],
            "expected_interval_s": int(s["expected_interval_sec"]),
            "heartbeat_s": int(s["heartbeat_sec"]) if s.get("heartbeat_sec") else None,
        }
    return out


def _sensor_physics(events: pd.DataFrame, sensor_id: str, meta: dict) -> dict:
    sub = events[events["sensor_id"] == sensor_id].sort_values("timestamp")
    if sub.empty:
        return {**meta, "median_inter_event_s": None, "zoh_fraction": None, "n_events": 0}
    ts = pd.to_datetime(sub["timestamp"]).reset_index(drop=True)
    vals = sub["value"].reset_index(drop=True)
    inters = ts.diff().dropna().dt.total_seconds()
    median_int = float(inters.median()) if not inters.empty else None
    if len(vals) > 1:
        eq = (vals.iloc[1:].to_numpy() == vals.iloc[:-1].to_numpy()).sum()
        zoh = float(eq) / float(len(vals) - 1)
    else:
        zoh = 0.0
    return {
        **meta,
        "median_inter_event_s": median_int,
        "zoh_fraction": round(zoh, 4),
        "n_events": int(len(sub)),
    }


def main() -> None:
    scen_names = []
    # Per-anomaly-type accumulators
    at_count: Counter = Counter()
    at_class: dict[str, Counter] = defaultdict(Counter)
    at_bucket: dict[str, Counter] = defaultdict(Counter)
    at_arch: dict[str, set] = defaultdict(set)
    at_sensors: dict[str, set] = defaultdict(set)
    # Shape distribution per archetype
    shape_dist: dict[str, Counter] = defaultdict(Counter)
    # Sensor physics aggregated across scenarios
    sensor_phys: dict[str, dict] = {}

    for suite, name, events_dir, cfg_file, _boot in SCENARIOS:
        ev_path = GEN / events_dir / "events.csv"
        lb_path = GEN / events_dir / "labels.csv"
        if not ev_path.exists() or not lb_path.exists():
            print(f"skip {name} (missing csv)")
            continue
        scen_names.append(name)
        sensors = _load_config(cfg_file)
        events = pd.read_csv(ev_path)
        labels = pd.read_csv(lb_path)
        labels["start"] = pd.to_datetime(labels["start"])
        labels["end"] = pd.to_datetime(labels["end"])

        for _, row in labels.iterrows():
            atype = str(row["anomaly_type"])
            klass = str(row.get("label_class") or "unknown")
            sid = str(row["sensor_id"])
            arch = sensors.get(sid, {}).get("archetype", "UNKNOWN")
            dur = (row["end"] - row["start"]).total_seconds()
            bkt = _bucket(dur)
            at_count[atype] += 1
            at_class[atype][klass] += 1
            at_bucket[atype][bkt] += 1
            at_arch[atype].add(arch)
            at_sensors[atype].add(sid)
            shape = _shape_for(atype, arch)
            shape_dist[arch][shape] += 1

        for sid, meta in sensors.items():
            key = f"{name}:{sid}"
            sensor_phys[key] = _sensor_physics(events, sid, meta)

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "scenarios_included": scen_names,
        "anomaly_types": {
            at: {
                "count": at_count[at],
                "label_class_breakdown": dict(at_class[at]),
                "duration_buckets": dict(at_bucket[at]),
                "archetypes_seen": sorted(at_arch[at]),
                "sensors_seen": sorted(at_sensors[at]),
            }
            for at in sorted(at_count)
        },
        "sensor_physics": sensor_phys,
        "shape_distribution": {
            arch: dict(shape_dist[arch]) for arch in sorted(shape_dist)
        },
    }
    OUT_PATH.write_text(json.dumps(out, indent=2))
    print(f"wrote {OUT_PATH}")
    print(f"  anomaly_types: {len(out['anomaly_types'])}")
    print(f"  sensors: {len(sensor_phys)}")
    print(f"  shape_distribution: "
          f"{ {a: sum(d.values()) for a, d in shape_dist.items()} }")


if __name__ == "__main__":
    main()
