from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


def _ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


@dataclass(frozen=True)
class Interval:
    sensor_id: str
    capability: str
    start: datetime
    end: datetime
    anomaly_type: str
    detector: str
    # Earliest fire-tick; falls back to `start` on legacy CSVs without the
    # `first_fire_ts` column. Latency and onset timing use this instead of
    # `start` so sliding-window and cross-chain artifacts don't back-date
    # the reported alert fire moment.
    first_fire_ts: datetime | None = None

    @property
    def fire(self) -> datetime:
        return self.first_fire_ts or self.start


def _load_labels(path: Path, label_class: str | None) -> list[Interval]:
    rows: list[Interval] = []
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if label_class is not None and row.get("label_class") != label_class:
                continue
            rows.append(Interval(
                sensor_id=row["sensor_id"],
                capability=row["capability"],
                start=_ts(row["start"]),
                end=_ts(row["end"]),
                anomaly_type=row.get("anomaly_type", ""),
                detector=row.get("detector_hint", ""),
            ))
    return rows


def _load_detections(path: Path, exclude_detector: str | None) -> list[Interval]:
    rows: list[Interval] = []
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if exclude_detector is not None and row.get("detector") == exclude_detector:
                continue
            first_fire_raw = row.get("first_fire_ts") or ""
            first_fire = _ts(first_fire_raw) if first_fire_raw else None
            rows.append(Interval(
                sensor_id=row["sensor_id"],
                capability=row["capability"],
                start=_ts(row["start"]),
                end=_ts(row["end"]),
                anomaly_type=row.get("anomaly_type", ""),
                detector=row.get("detector", ""),
                first_fire_ts=first_fire,
            ))
    return rows


def _overlaps(a: Interval, b: Interval) -> bool:
    return a.sensor_id == b.sensor_id and a.start < b.end and b.start < a.end


def _quantile(sorted_vals: list[float], q: float) -> float | None:
    if not sorted_vals:
        return None
    if len(sorted_vals) == 1:
        return sorted_vals[0]
    pos = (len(sorted_vals) - 1) * q
    lo = int(pos)
    hi = min(len(sorted_vals) - 1, lo + 1)
    frac = pos - lo
    return sorted_vals[lo] * (1.0 - frac) + sorted_vals[hi] * frac


def _fmt_seconds(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.1f}s"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--labels", required=True, type=Path)
    ap.add_argument("--detections", required=True, type=Path)
    ap.add_argument("--label-class", default="user_behavior")
    ap.add_argument("--exclude-detector", default="data_quality_gate")
    ap.add_argument("--sensor-id", default=None)
    ap.add_argument("--top-k", type=int, default=12)
    args = ap.parse_args()

    labels = _load_labels(args.labels, args.label_class)
    detections = _load_detections(args.detections, args.exclude_detector)
    if args.sensor_id is not None:
        labels = [x for x in labels if x.sensor_id == args.sensor_id]
        detections = [x for x in detections if x.sensor_id == args.sensor_id]

    rows: list[dict] = []
    for label in labels:
        overlaps = [det for det in detections if _overlaps(label, det)]
        if not overlaps:
            rows.append({
                "label": label,
                "first": None,
                "lead_s": None,
                "late_s": None,
            })
            continue
        first = min(overlaps, key=lambda det: det.fire)
        rows.append({
            "label": label,
            "first": first,
            "lead_s": max(0.0, (label.start - first.fire).total_seconds()),
            "late_s": max(0.0, (first.fire - label.start).total_seconds()),
        })

    matched = [r for r in rows if r["first"] is not None]
    lead_vals = sorted(r["lead_s"] for r in matched if r["lead_s"] is not None)
    late_vals = sorted(r["late_s"] for r in matched if r["late_s"] is not None)
    n_early = sum(1 for r in matched if (r["lead_s"] or 0.0) > 0)
    n_late = sum(1 for r in matched if (r["late_s"] or 0.0) > 0)

    print("=== Onset Timing Audit ===")
    print(f"labels={len(labels)} matched={len(matched)} misses={len(labels) - len(matched)}")
    print(
        "lead: "
        f"early_labels={n_early} "
        f"mean={_fmt_seconds(sum(lead_vals) / len(lead_vals) if lead_vals else None)} "
        f"p95={_fmt_seconds(_quantile(lead_vals, 0.95))} "
        f"max={_fmt_seconds(max(lead_vals) if lead_vals else None)}"
    )
    print(
        "late: "
        f"late_labels={n_late} "
        f"mean={_fmt_seconds(sum(late_vals) / len(late_vals) if late_vals else None)} "
        f"p95={_fmt_seconds(_quantile(late_vals, 0.95))} "
        f"max={_fmt_seconds(max(late_vals) if late_vals else None)}"
    )

    print("\nTop Early Labels")
    early_rows = sorted(
        (r for r in matched if (r["lead_s"] or 0.0) > 0),
        key=lambda r: (r["lead_s"], r["label"].start),
        reverse=True,
    )[: args.top_k]
    for row in early_rows:
        label = row["label"]
        first = row["first"]
        print(
            f"{int(row['lead_s']):>7}s early  "
            f"{label.sensor_id:<20} {label.anomaly_type:<22} "
            f"label={label.start.isoformat()} first_fire={first.fire.isoformat()} det={first.detector}"
        )

    print("\nTop Late Labels")
    late_rows = sorted(
        (r for r in matched if (r["late_s"] or 0.0) > 0),
        key=lambda r: (r["late_s"], r["label"].start),
        reverse=True,
    )[: args.top_k]
    for row in late_rows:
        label = row["label"]
        first = row["first"]
        print(
            f"{int(row['late_s']):>7}s late   "
            f"{label.sensor_id:<20} {label.anomaly_type:<22} "
            f"label={label.start.isoformat()} first_fire={first.fire.isoformat()} det={first.detector}"
        )

    if len(labels) != len(matched):
        print("\nMissed Labels")
        misses = [r for r in rows if r["first"] is None][: args.top_k]
        for row in misses:
            label = row["label"]
            print(
                f"MISS          {label.sensor_id:<20} {label.anomaly_type:<22} "
                f"label={label.start.isoformat()}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
