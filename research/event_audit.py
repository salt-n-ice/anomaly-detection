"""Per-event TP/FP audit.

Merges detections within a 1-hour gap (mirroring the event-F1 metric), then
flags each merged event TP (overlaps any same-sensor label) or FP. Handy when
`run_research_eval.py --diff-baseline` calls out a scenario and you want the
exact list of FP events with detector fingerprint + duration.

    python research/event_audit.py outlet_tv_60d waterleak_120d
"""
import pandas as pd
import sys
from pathlib import Path


# Scenario → synthetic-generator out-dir, mirrored from run_research_eval.py.
_LBL_DIR = {
    "outlet_60d": "outlet",
    "outlet_tv_60d": "outlet_tv",
    "outlet_kettle_60d": "outlet_kettle",
    "waterleak_60d": "leak",
    "outlet_short_60d": "outlet_short",
    "outlet_120d": "outlet_120d",
    "waterleak_120d": "waterleak_120d",
}


def _merge_events(det: pd.DataFrame, gap_hours: float = 1.0) -> pd.DataFrame:
    """Collapse per-sensor detections whose inter-row gap is <= gap_hours."""
    rows = []
    for sid, g in det.groupby("sensor_id"):
        g = g.sort_values("start").reset_index(drop=True)
        cur_s = cur_e = None
        cur_det: list[str] = []
        for _, r in g.iterrows():
            if cur_s is None or (r["start"] - cur_e) > pd.Timedelta(hours=gap_hours):
                if cur_s is not None:
                    rows.append((sid, cur_s, cur_e, "+".join(sorted(set(cur_det)))))
                cur_s, cur_e, cur_det = r["start"], r["end"], [r["detector"]]
            else:
                cur_e = max(cur_e, r["end"])
                cur_det.append(r["detector"])
        if cur_s is not None:
            rows.append((sid, cur_s, cur_e, "+".join(sorted(set(cur_det)))))
    return pd.DataFrame(rows, columns=["sensor", "start", "end", "dets"])


def audit(scenario: str) -> None:
    det = pd.read_csv(f"out/{scenario}_detections.csv")
    det["start"] = pd.to_datetime(det["start"], utc=True, format="ISO8601")
    det["end"] = pd.to_datetime(det["end"], utc=True, format="ISO8601")
    lbl = pd.read_csv(f"../synthetic-generator/out/{_LBL_DIR[scenario]}/labels.csv")
    lbl["start"] = pd.to_datetime(lbl["start"], utc=True, format="ISO8601")
    lbl["end"] = pd.to_datetime(lbl["end"], utc=True, format="ISO8601")

    ev = _merge_events(det)
    out = []
    for _, e in ev.iterrows():
        overlap = lbl[(lbl["sensor_id"] == e["sensor"])
                      & (lbl["end"] >= e["start"])
                      & (lbl["start"] <= e["end"])]
        status = ("TP:" + ",".join(sorted(overlap["anomaly_type"].unique()))
                  if len(overlap) else "FP")
        out.append({
            "sensor": e["sensor"],
            "start": str(e["start"]),
            "end": str(e["end"]),
            "dur_h": round((e["end"] - e["start"]).total_seconds() / 3600, 1),
            "dets": e["dets"][:60],
            "status": status,
        })
    df = pd.DataFrame(out).sort_values("start")
    fps = df[df["status"] == "FP"]
    print(f"=== {scenario} — {len(df)} events ({len(fps)} FP) ===")
    with pd.option_context("display.max_rows", None, "display.width", 240,
                           "display.max_colwidth", 70):
        print(fps.to_string(index=False) if len(fps) else "(no FPs)")


if __name__ == "__main__":
    if not sys.argv[1:]:
        print("usage: python research/event_audit.py <scenario> [<scenario> ...]",
              file=sys.stderr)
        print(f"scenarios: {', '.join(_LBL_DIR)}", file=sys.stderr)
        sys.exit(2)
    for name in sys.argv[1:]:
        audit(name)
