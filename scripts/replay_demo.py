"""Deployment-style replay animation for a scenario's detection chains.

Reads:
  synthetic-generator/out/<scenario>/events.csv  (timeline bounds only)
  synthetic-generator/out/<scenario>/labels.csv  (GT band overlays)
  out/<scenario>_detections.csv                  (chain stream -> pins)

Writes:
  out/replay_<scenario>.html  (self-contained, ~150-250 KB)

Default scenario is `household_120d`. Override the synth-gen output root via
the SENSORGEN_OUT environment variable (matches scripts/run_all_scenarios.py).
"""
from __future__ import annotations
import argparse, json, os, sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
GEN_ROOT = Path(os.environ.get("SENSORGEN_OUT", ROOT.parent / "synthetic-generator" / "out"))
OUT = ROOT / "out"


# ---------------------------- classification ----------------------------

# Synonym map: system inferred_type -> set of GT anomaly_types it can match.
# Encodes that the system's verdict and the GT label may use different
# vocabulary for the same underlying phenomenon (see spec section 5).
SYNONYMS = {
    "month_shift": {"level_shift", "month_shift"},
    "calibration_drift": {"trend", "calibration_drift"},
    # weekend_anomaly only matches time_of_day if GT target=weekday - handled
    # in code below because it depends on params_json content.
}


def _types_match(inferred: str, gt_type: str, gt_params_json: str) -> bool:
    if inferred == gt_type:
        return True
    if inferred in SYNONYMS and gt_type in SYNONYMS[inferred]:
        return True
    if inferred == "weekend_anomaly" and gt_type == "time_of_day":
        try:
            p = json.loads(gt_params_json) if gt_params_json else {}
        except (ValueError, TypeError):
            p = {}
        return p.get("target") == "weekday"
    return False


def classify_chain(chain, labels_df) -> str:
    """Return 'tp', 'ambiguous', or 'fp' for one chain against all labels.

    chain: dict-like with sensor_id, start, end, inferred_type.
    labels_df: DataFrame with sensor_id, start, end, anomaly_type, params_json.
    """
    same_sensor = labels_df[labels_df["sensor_id"] == chain["sensor_id"]]
    if same_sensor.empty:
        return "fp"
    overlapping = same_sensor[(same_sensor["start"] < chain["end"]) &
                              (same_sensor["end"] > chain["start"])]
    if overlapping.empty:
        return "fp"
    for _, lbl in overlapping.iterrows():
        if _types_match(chain["inferred_type"], lbl["anomaly_type"], lbl.get("params_json", "{}")):
            return "tp"
    return "ambiguous"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--scenario", default="household_120d")
    p.add_argument("--out", type=Path, default=None,
                   help="HTML output path (default: out/replay_<scenario>.html)")
    p.add_argument("--duration-sec", type=int, default=60,
                   help="Wall-clock seconds for full timeline at 1x speed")
    args = p.parse_args()

    events_csv = GEN_ROOT / args.scenario / "events.csv"
    labels_csv = GEN_ROOT / args.scenario / "labels.csv"
    det_csv    = OUT / f"{args.scenario}_detections.csv"
    for f in (events_csv, labels_csv, det_csv):
        if not f.exists():
            print(f"ERROR: missing {f}", file=sys.stderr)
            return 1

    out_path = args.out or OUT / f"replay_{args.scenario}.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    payload = build_payload(events_csv, labels_csv, det_csv, args.scenario, args.duration_sec)
    html = render_html(payload)
    out_path.write_text(html, encoding="utf-8")
    print(f"wrote {out_path} ({out_path.stat().st_size // 1024} KB, {len(payload['chains'])} chains)")
    return 0


def build_payload(events_csv, labels_csv, det_csv, scenario, duration_sec):
    raise NotImplementedError("Task 3")


def render_html(payload):
    raise NotImplementedError("Task 4")


if __name__ == "__main__":
    sys.exit(main())
