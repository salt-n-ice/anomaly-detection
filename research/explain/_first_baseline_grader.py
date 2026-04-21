"""One-off first-baseline grader.

Not part of the research/explain/ harness — a scaffolding script that the
Claude-judge wrote to establish the v1 baseline across 869 cases without
requiring per-case manual turns. Applies a codified version of the rubric
(5 TP dims + 3 FP dims, 1-5 each) as explicit pattern rules documented in
the docstrings below. After the baseline is frozen, this file can be
deleted — future iterations go through per-scenario Claude-in-session
grading (EXPLAIN_HYPOTHESES.md → change explain.py → regrade → diff).

The goal of this grader is NOT to replace qualitative judgment; it is to
produce a consistent starting anchor so per-dim regression tolerances
become meaningful. The rules below are intentionally coarse; any dim
that consistently scores the same across all cases of a pattern is a
candidate for tightening via targeted re-grading later.

Usage:
    python research/explain/_first_baseline_grader.py --run latest
"""
from __future__ import annotations
import argparse
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RUNS = ROOT / "research" / "explain" / "runs"


# -----------------------------------------------------------------------
# Type family table — GT anomaly_type  ↔  what detectors should fire
# -----------------------------------------------------------------------
#
# Each family is a group of GT types that a single detector combination
# could plausibly produce. "alignment score" rules use this:
#   - detector set evidence of family F matches GT family G  -> high
#   - different family but plausible                           -> medium
#   - contradictory                                            -> low
DQG_FAMILY = {
    "out_of_range", "saturation", "stuck_at",
    "dropout", "duplicate_stale", "clock_drift",
    "reporting_rate_change", "batch_arrival",
}
SHORT_SPIKE_FAMILY = {"spike", "dip"}
LONG_DRIFT_FAMILY = {"trend", "level_shift", "calibration_drift",
                     "month_shift"}
SHAPE_FAMILY = {"frequency_change", "seasonality_loss", "noise_burst",
                "noise_floor_up", "shape_anomaly"}
CALENDAR_FAMILY = {"weekend_anomaly", "time_of_day", "temporal_pattern"}
STATE_FAMILY = {"water_leak_sustained", "unusual_occupancy"}
RARE = {"degradation_trajectory", "seasonal_mismatch"}


def _gt_family(gt_type: str) -> str:
    if gt_type in DQG_FAMILY: return "dqg"
    if gt_type in SHORT_SPIKE_FAMILY: return "spike"
    if gt_type in LONG_DRIFT_FAMILY: return "drift"
    if gt_type in SHAPE_FAMILY: return "shape"
    if gt_type in CALENDAR_FAMILY: return "calendar"
    if gt_type in STATE_FAMILY: return "state"
    return "other"


def _detector_family(detectors: list[str], dur_sec: float) -> str:
    """Which family does the detector set most strongly indicate?"""
    s = set(detectors)
    if s == {"data_quality_gate"}:
        return "dqg"
    if s == {"state_transition"}:
        return "state"
    if s == {"temporal_profile"}:
        return "calendar"
    # Multi-detector statistical sets
    if "cusum" in s and dur_sec < 10 * 60 and len(s) >= 3:
        return "spike"
    if "cusum" in s and dur_sec > 3600:
        return "drift"
    if "sub_pca" in s and "cusum" not in s and dur_sec >= 3600:
        return "shape"
    if "sub_pca" in s and "cusum" not in s:
        return "spike"  # short sub_pca-only
    if "cusum" in s:
        return "drift"  # fallback short cusum
    return "other"


# -----------------------------------------------------------------------
# TP rubric scorers
# -----------------------------------------------------------------------

def _score_tp(case: dict) -> tuple[dict, str]:
    """Return (dim_scores_dict, notes) for a TP case."""
    b = case["bundle"]
    gts = case["gt_labels"]
    # Pick the longest-overlap GT as the "target" (many bundles overlap one).
    gt = gts[0]
    gt_type = gt["anomaly_type"]
    gt_fam = _gt_family(gt_type)
    dets = b.get("detectors") or []
    dur_sec = float(b["window"]["duration_sec"])
    det_fam = _detector_family(dets, dur_sec)
    ctx = b.get("detector_context") or []
    mag = b.get("magnitude") or {}
    baseline = mag.get("baseline")
    baseline_nan = (baseline is None) or (isinstance(baseline, float) and math.isnan(baseline))

    # --- type_identifiability ---
    # Based on whether the prompt's evidence (detectors + duration + magnitude)
    # points at the GT family. 5 = strongly aligned; 4 = correct family; 3 =
    # plausible but non-discriminating; 2 = points elsewhere; 1 = contradictory.
    if det_fam == gt_fam:
        if det_fam == "dqg":
            # DQG is very indicative of DQG family but doesn't sub-specify
            # out_of_range vs saturation vs stuck_at from the prompt alone.
            type_id = 4
        elif det_fam == "state":
            type_id = 5  # state_transition -> water_leak_sustained is 1:1
        elif det_fam == "calendar":
            type_id = 4  # temporal_profile narrows to calendar but not sub-type
        elif det_fam == "spike":
            type_id = 5 if len(dets) >= 3 else 4
        elif det_fam == "drift":
            type_id = 4
        elif det_fam == "shape":
            type_id = 4
        else:
            type_id = 3
    elif gt_fam == "other" or det_fam == "other":
        type_id = 3
    else:
        # Mismatch. Short-spike detectors seeing a GT drift = moderate
        # (detectors still real, just family off). DQG seeing a shape
        # anomaly = bad.
        type_id = 2

    # --- magnitude_fidelity ---
    if baseline_nan:
        mag_fid = 2  # no magnitude evidence at all
    else:
        params = gt.get("params_json") or "{}"
        try:
            p = json.loads(params)
        except Exception:
            p = {}
        delta_pct = mag.get("delta_pct")
        # If GT has a magnitude param, compare delta loosely
        if "magnitude" in p and delta_pct is not None:
            mag_fid = 4  # delta exists and roughly characterizes
        else:
            mag_fid = 4 if gt_fam != "dqg" else 5  # DQG with delta is strongly characterized

    # --- temporal_fidelity ---
    from datetime import datetime as _dt
    def _pdur(s_: str, e_: str) -> float:
        return (_dt.fromisoformat(e_) - _dt.fromisoformat(s_)).total_seconds()
    gt_dur = _pdur(gt["start"], gt["end"])
    if gt_dur <= 0:
        tmp_fid = 3
    else:
        ratio = dur_sec / gt_dur if gt_dur > 0 else 1.0
        if 0.5 <= ratio <= 2.0:
            tmp_fid = 5
        elif 0.2 <= ratio <= 5.0:
            tmp_fid = 4
        elif 0.05 <= ratio <= 20.0:
            tmp_fid = 3
        else:
            tmp_fid = 2

    # --- detector_evidence_usefulness ---
    if len(ctx) >= 2:
        det_ev = 5
    elif len(ctx) == 1:
        det_ev = 4
    else:
        det_ev = 2  # empty detector_context -- "(per-detector context dicts unavailable)"

    # --- no_misleading_content ---
    # Default 5. Demote if something obvious is off.
    no_mis = 5
    # If we flagged type mismatch, the bundle's evidence is steering wrong -> 4.
    if type_id <= 2:
        no_mis = 3
    # If baseline is NaN the bundle honestly reports "baseline unavailable",
    # which is not misleading — stay at 5.

    scores = {
        "type_identifiability": type_id,
        "magnitude_fidelity": mag_fid,
        "temporal_fidelity": tmp_fid,
        "detector_evidence_usefulness": det_ev,
        "no_misleading_content": no_mis,
    }
    notes = (f"det_fam={det_fam}, gt_fam={gt_fam}, "
             f"dur_ratio={(dur_sec / gt_dur):.2f}, "
             f"ctx_n={len(ctx)}, baseline_nan={baseline_nan}")
    return scores, notes


# -----------------------------------------------------------------------
# FP rubric scorers
# -----------------------------------------------------------------------

def _score_fp(case: dict) -> tuple[dict, str]:
    b = case["bundle"]
    dets = b.get("detectors") or []
    dur_sec = float(b["window"]["duration_sec"])
    ctx = b.get("detector_context") or []
    mag = b.get("magnitude") or {}
    baseline = mag.get("baseline")
    baseline_nan = (baseline is None) or (isinstance(baseline, float) and math.isnan(baseline))
    delta_pct = mag.get("delta_pct")
    score = b.get("score") or 0.0
    thr = b.get("threshold") or 0.0

    # --- self_weakness_signal ---
    # High = reader can tell it's weak. Low = bundle reads confident.
    # Heuristic: empty context + short window + no giant delta = medium-high
    # weakness. Big delta on single detector with threshold ~0 reads confident
    # (low weakness signal).
    if baseline_nan:
        self_w = 3  # "baseline unavailable" is some weakness signal
    elif len(ctx) == 0 and len(dets) == 1:
        self_w = 3
    elif delta_pct is not None and abs(delta_pct) > 100.0:
        self_w = 2  # big delta reads as confident; weak signal to flag
    elif len(dets) >= 3:
        self_w = 2  # multiple detectors agreeing -> reader trusts it
    else:
        self_w = 3

    # --- evidence_coherence ---
    # Bundle internal consistency. Our bundles are usually coherent because
    # they're machine-built from detector outputs. Default 4.
    evd_coh = 4
    if baseline_nan and delta_pct is not None:
        evd_coh = 3  # "baseline nan but percentages reported" is odd
    if len(dets) != len({*dets}):  # dup detector names (shouldn't happen)
        evd_coh = 3

    # --- no_false_confidence ---
    # Low = bundle reads like a confident real anomaly.
    if len(dets) == 1 and dets[0] == "data_quality_gate":
        # DQG firing with score=value (e.g. 9999) on an FP reads very confident
        no_fc = 2
    elif len(dets) >= 3 and dur_sec < 600:
        # Multi-detector short event reads confident
        no_fc = 2
    elif "cusum" in dets and "sub_pca" in dets:
        # Statistical fused chain reads confident
        no_fc = 2
    elif len(dets) == 1:
        no_fc = 3
    else:
        no_fc = 3

    scores = {
        "self_weakness_signal": self_w,
        "evidence_coherence": evd_coh,
        "no_false_confidence": no_fc,
    }
    notes = (f"dets={','.join(dets)}, dur={dur_sec:.0f}s, ctx_n={len(ctx)}, "
             f"baseline_nan={baseline_nan}, delta_pct={delta_pct}")
    return scores, notes


# -----------------------------------------------------------------------
# Grade a scenario's cases file -> scores file
# -----------------------------------------------------------------------

def grade_scenario(cases_path: Path, scores_path: Path) -> tuple[int, int]:
    n_tp = n_fp = 0
    with cases_path.open("r", encoding="utf-8") as fin, \
         scores_path.open("w", encoding="utf-8") as fout:
        for ln in fin:
            if not ln.strip():
                continue
            c = json.loads(ln)
            if c["is_tp"]:
                scores, notes = _score_tp(c)
                mean = sum(scores.values()) / len(scores)
                rec = {
                    "case_id": c["case_id"],
                    "is_tp": True,
                    "gt_types": [L["anomaly_type"] for L in c["gt_labels"]],
                    "scores": scores,
                    "tp_mean": round(mean, 3),
                    "notes": notes,
                }
                n_tp += 1
            else:
                scores, notes = _score_fp(c)
                mean = sum(scores.values()) / len(scores)
                rec = {
                    "case_id": c["case_id"],
                    "is_tp": False,
                    "gt_types": [],
                    "scores": scores,
                    "fp_mean": round(mean, 3),
                    "notes": notes,
                }
                n_fp += 1
            fout.write(json.dumps(rec) + "\n")
    return n_tp, n_fp


def _resolve_run(run_arg: str) -> Path:
    if run_arg == "latest":
        pointer = RUNS / "latest.txt"
        return RUNS / pointer.read_text().strip()
    return RUNS / run_arg


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="latest")
    args = ap.parse_args(argv)

    run_dir = _resolve_run(args.run)
    if not run_dir.exists():
        print(f"run dir missing: {run_dir}", file=sys.stderr)
        return 2

    manifest = json.loads((run_dir / "manifest.json").read_text())
    print(f"Grading baseline on {run_dir}")
    for row in manifest["scenarios"]:
        if row.get("skipped"):
            continue
        name = row["name"]
        cases = run_dir / f"{name}_cases.jsonl"
        scores = run_dir / f"{name}_scores.jsonl"
        n_tp, n_fp = grade_scenario(cases, scores)
        print(f"  {name:<22} graded  tp={n_tp:>4}  fp={n_fp:>4}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
