"""Classify ambiguous anomaly detection events per domain priors."""
import json
from pathlib import Path
from datetime import datetime

IN_PATH = Path(r"C:\Projects\Sensor-data-anomaly-detection\anomaly-detection\research\ambiguous_batch.json")
OUT_PATH = Path(r"C:\Projects\Sensor-data-anomaly-detection\anomaly-detection\research\ambiguous_classified.json")


def _parse_iso(s: str) -> datetime:
    # Python stdlib fromisoformat handles +00:00
    return datetime.fromisoformat(s)


def classify(bundle: dict) -> tuple[str, float, str]:
    sensor = bundle.get("sensor_id", "")
    cap = bundle.get("capability", "")
    dur = float(bundle.get("duration_hours", 0.0))
    first_fire_ts = bundle.get("first_fire_ts", "")
    first_fire_month = int(bundle.get("first_fire_month", 0))

    # Parse date for day-of-month near boundary check
    ts = None
    try:
        ts = _parse_iso(first_fire_ts)
    except Exception:
        ts = None
    day = ts.day if ts is not None else None

    # ---- mains_voltage (voltage) ----
    if sensor == "mains_voltage" or cap == "voltage":
        # Default strong prior: calibration_drift (sensor_fault).
        # Month-shift only if detection begins near month boundary AND we have
        # evidence of modest shift. Score is relative to detector threshold; we
        # do not have the actual delta-volts, so we cannot robustly check "~1-2 V".
        # Prior explicitly says: default strongly toward calibration_drift for
        # mains_voltage. We use month_shift only when the date is right on a
        # boundary (day <= 2 or >= 29) AND duration is short-ish (< 24h),
        # which is the typical shape of a month rollover artifact.
        near_month_boundary = day is not None and (day <= 2 or day >= 29)
        if near_month_boundary and dur < 12:
            return (
                "month_shift",
                0.55,
                f"mains_voltage shift firing on day {day} (near month boundary) with duration {dur:.2f}h; treating as month_shift per boundary prior, though calibration_drift is a close alternative.",
            )
        # Otherwise calibration_drift — sustained voltage shifts are almost
        # always sensor drift on this dataset.
        if dur >= 24:
            return (
                "calibration_drift",
                0.85,
                f"mains_voltage sustained shift ({dur:.2f}h >= 24h) on recent_shift — voltage sensor sustained deviation is almost always calibration_drift.",
            )
        # Short-duration voltage shift (<24h) — still calibration_drift per
        # "default strongly toward" prior, but confidence is lower because
        # short bounces can also be line-voltage events.
        return (
            "calibration_drift",
            0.70,
            f"mains_voltage brief shift ({dur:.2f}h) on recent_shift — voltage shifts default to calibration_drift on this dataset.",
        )

    # ---- basement_temp (temperature) ----
    if sensor == "basement_temp" or cap == "temperature":
        # Brief dip (<24h): dip (user behavior — cold exposure). The bundle
        # does not carry sign-of-shift; prior says brief temperature deviations
        # in the basement are dips (cold/open window) rather than spikes, since
        # a hot basement is not a common user event. Default to dip.
        if dur < 24:
            return (
                "dip",
                0.70,
                f"basement_temp brief deviation ({dur:.2f}h < 24h) — user-behavior brief cold exposure per temperature prior.",
            )
        # Sustained >=24h: calibration_drift (sensor fault).
        return (
            "calibration_drift",
            0.80,
            f"basement_temp sustained deviation ({dur:.2f}h >= 24h) — sensor fault per temperature prior.",
        )

    # ---- Fallback (should not trigger for this batch) ----
    return (
        "statistical_anomaly",
        0.40,
        f"Unhandled sensor/capability combo ({sensor}/{cap}); falling back to statistical_anomaly.",
    )


def main() -> None:
    rows = json.loads(IN_PATH.read_text(encoding="utf-8"))
    out = []
    for r in rows:
        bundle = r.get("bundle", {}) or {}
        typ, conf, reason = classify(bundle)
        out.append(
            {
                "scenario": r.get("scenario"),
                "row_idx": r.get("row_idx"),
                "type": typ,
                "confidence": conf,
                "reasoning": reason,
            }
        )
    OUT_PATH.write_text(json.dumps(out, indent=2), encoding="utf-8")

    # Summary ---------------------------------------------------------------
    from collections import Counter

    total = len(out)
    type_dist = Counter(r["type"] for r in out)
    low_conf = [r for r in out if r["confidence"] < 0.6]

    print(f"Total rows classified: {total}")
    print("Type distribution:")
    for t, c in type_dist.most_common():
        print(f"  {t}: {c}")
    print(f"Low-confidence rows (<0.6): {len(low_conf)}")
    for r in low_conf:
        print(
            f"  [{r['scenario']} row {r['row_idx']}] type={r['type']} conf={r['confidence']:.2f} :: {r['reasoning']}"
        )


if __name__ == "__main__":
    main()
