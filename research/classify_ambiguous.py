"""Classify ambiguous detections into anomaly types using domain priors.

Priors (from task instructions + CLAUDE.md):
- mains_voltage (voltage): default `calibration_drift`. `month_shift` only if
  first_fire_ts is within day 28-31 or 1-3 AND duration < 6h.
- basement_temp (temperature): brief (<24h) → `dip`; sustained (>=24h) → `calibration_drift`.
  (Spike direction is not inferable from bundle fields, and dip is the stated default
  for brief temperature events per instructions.)

No direction/signal data is present in bundles, so we rely on duration + timestamp
+ sensor_id + detector_set to choose types. Confidence calibration:
- 0.85: clean match to a strong prior (e.g. long-duration mains_voltage =
  calibration_drift; brief basement_temp = dip).
- 0.75: prior applies but with mild ambiguity (short mains_voltage far from
  month boundary — still calibration_drift, but recent_shift alone is weak evidence).
- 0.65: month-boundary mains_voltage short bundle → month_shift (tie between
  month_shift and calibration_drift; instructions say month_shift qualifies).
- 0.55: residual ambiguity flagged; still choose per prior.
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

IN_PATH = Path(r"C:\Projects\Sensor-data-anomaly-detection\anomaly-detection\research\ambiguous_batch.json")
OUT_PATH = Path(r"C:\Projects\Sensor-data-anomaly-detection\anomaly-detection\research\ambiguous_classified.json")


def classify(row: dict) -> dict:
    b = row["bundle"]
    sensor = b["sensor_id"]
    dur_h = float(b["duration_hours"])
    ts = datetime.fromisoformat(b["first_fire_ts"])
    day = ts.day

    if sensor == "mains_voltage":
        near_month_boundary = day <= 3 or day >= 28
        if near_month_boundary and dur_h < 6.0:
            # Per instructions: month_shift requires BOTH month-boundary AND short duration.
            return {
                "type": "month_shift",
                "confidence": 0.65,
                "reasoning": (
                    f"mains_voltage brief event ({dur_h:.2f}h) on day {day} "
                    f"(month-boundary window); month_shift prior applies over calibration_drift."
                ),
            }
        if dur_h >= 24.0:
            return {
                "type": "calibration_drift",
                "confidence": 0.88,
                "reasoning": (
                    f"mains_voltage sustained shift ({dur_h:.2f}h) — strong sensor_fault "
                    f"calibration_drift signature per voltage prior."
                ),
            }
        # Short duration, not at month boundary: instructions say default STRONGLY to calibration_drift.
        return {
            "type": "calibration_drift",
            "confidence": 0.80,
            "reasoning": (
                f"mains_voltage shift ({dur_h:.2f}h) on day {day}; voltage sensor shifts "
                f"default to calibration_drift per prior."
            ),
        }

    if sensor == "basement_temp":
        if dur_h >= 24.0:
            return {
                "type": "calibration_drift",
                "confidence": 0.80,
                "reasoning": (
                    f"basement_temp sustained shift ({dur_h:.2f}h ≥ 24h) → "
                    f"sensor_fault calibration_drift per temperature prior."
                ),
            }
        return {
            "type": "dip",
            "confidence": 0.78,
            "reasoning": (
                f"basement_temp brief event ({dur_h:.2f}h < 24h) on recent_shift — "
                f"user_behavior dip per temperature prior (direction not encoded; "
                f"dip is the stated default)."
            ),
        }

    # Fallback: genuinely ambiguous / unexpected sensor.
    return {
        "type": "statistical_anomaly",
        "confidence": 0.50,
        "reasoning": (
            f"Unknown sensor {sensor!r} outside voltage/temperature priors; fall back to "
            f"statistical_anomaly."
        ),
    }


def main() -> None:
    rows = json.loads(IN_PATH.read_text(encoding="utf-8"))
    out = []
    for r in rows:
        c = classify(r)
        out.append(
            {
                "scenario": r["scenario"],
                "row_idx": r["row_idx"],
                "type": c["type"],
                "confidence": c["confidence"],
                "reasoning": c["reasoning"],
            }
        )

    OUT_PATH.write_text(json.dumps(out, indent=2), encoding="utf-8")

    total = len(out)
    # Type distribution
    type_counts: dict[str, int] = {}
    for o in out:
        type_counts[o["type"]] = type_counts.get(o["type"], 0) + 1

    low_conf = [o for o in out if o["confidence"] < 0.6]

    print(f"Total rows classified: {total}")
    print("Type distribution:")
    for t, n in sorted(type_counts.items(), key=lambda kv: -kv[1]):
        print(f"  {t}: {n}")
    print(f"Rows with confidence < 0.6: {len(low_conf)}")
    for o in low_conf:
        print(
            f"  scenario={o['scenario']} row_idx={o['row_idx']} "
            f"type={o['type']} conf={o['confidence']:.2f}"
        )


if __name__ == "__main__":
    main()
