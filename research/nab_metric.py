"""NAB-style metric with event-level + type matching.

FP definition matches the viz layer's `user_visible_fps`
(`src/anomaly/viz/selection.py`): a chain is a false positive iff its
`inferred_class` is compatible with the scoring block (block itself or
"unknown") AND its `[start, end]` window has no overlap with ANY
ground-truth label (any class) on the same sensor. This is the same
rule the user-facing PDF report uses to count "user-visible false
alarms", so the eval and the report agree by construction.

Per GT label L of type T on sensor S, window [L.start, L.end]:
  - Define TP credit window: [L.start, L.start + semantics[T].tp_window_sec],
    clipped to L.end. For emergencies (water_leak_sustained), the credit
    window is the full label window — every fire is a TP.
  - Find detections on S whose predicted type (ml_inferred_type or
    inferred_type) matches T AND whose first_fire_ts falls in the credit
    window. Take the earliest such detection -> primary TP, scored by
    NAB sigmoid (higher weight earlier in the window).
  - If no matching detection exists in the credit window: FN.

For any non-TP-primary detection D on sensor S:
  - If D's [start, end] overlaps ANY GT label on S (any class) ->
    "covered" (no credit, no penalty). This collapses the previous
    `FP_wrong_type`, `exempt_permanent`, `exempt_fault_overlap`, and
    `TP_redundant` sub-categories into one neutral bucket. From the
    user's perspective the chain coincided with something real on the
    sensor — not a false alarm.
  - Otherwise -> FP (the user-visible-FP definition).

Scoring (reward_low_FP profile): TP weight scales with sigmoid position
within credit window (1.0 at window start, ~0 at window end). FP penalty
= -0.22 per. FN penalty contributes via absence of TP. Final score per
block (user_behavior / sensor_fault) =
    sum(TP weights) + sum(FP penalties)
normalized by number of block labels and scaled so a perfect detector
scores 100 and a null detector scores 0.

Inputs:
  - labels_df:  labels.csv (start, end, anomaly_type, label_class, ...)
  - det_df:     detections.csv (sensor_id, capability, start, end,
                first_fire_ts, inferred_type, ml_inferred_type [optional],
                inferred_class)

Output: per-block dict with score, TP/FP/FN/covered counts.
"""
from __future__ import annotations
import math
from dataclasses import dataclass

import pandas as pd

from anomaly_semantics import (
    semantics_for, is_user_behavior, is_sensor_fault,
)

# NAB reward_low_FP profile weights.
TP_WEIGHT = 1.0
FP_WEIGHT = -0.22
FN_WEIGHT = -1.0


def _sigmoid_score(t: pd.Timestamp, window_start: pd.Timestamp,
                   window_end: pd.Timestamp) -> float:
    """NAB-style sigmoid: 1.0 at window_start, ~0 at window_end."""
    total = max(1.0, (window_end - window_start).total_seconds())
    elapsed = max(0.0, (t - window_start).total_seconds())
    # Map [0, total] to [-5, +5] for the sigmoid argument — reverse sign
    # so early firings are rewarded high.
    x = -5.0 + 10.0 * elapsed / total
    return 2.0 / (1.0 + math.exp(x)) - 1.0 + TP_WEIGHT  # peak 1.0 at x=-5


def _pred_type(det_row) -> str:
    ml = det_row.get("ml_inferred_type")
    if isinstance(ml, str) and ml:
        return ml
    it = det_row.get("inferred_type")
    if isinstance(it, str) and it:
        return it
    return "statistical_anomaly"


@dataclass
class _LabelInfo:
    sensor_id: str
    capability: str
    start: pd.Timestamp
    end: pd.Timestamp
    atype: str
    window_start: pd.Timestamp
    window_end: pd.Timestamp  # credit window end (min(end, start + tp_window))


def _prepare_labels(labels_df: pd.DataFrame) -> list[_LabelInfo]:
    labels = []
    for _, r in labels_df.iterrows():
        s = pd.Timestamp(r["start"])
        e = pd.Timestamp(r["end"])
        atype = str(r["anomaly_type"])
        sem = semantics_for(atype)
        if sem.is_emergency:
            credit_end = e  # full label window
        else:
            credit_end = min(e, s + pd.Timedelta(seconds=sem.tp_window_sec))
        labels.append(_LabelInfo(
            sensor_id=str(r["sensor_id"]),
            capability=str(r["capability"]),
            start=s, end=e, atype=atype,
            window_start=s, window_end=credit_end))
    return labels


def _build_label_intervals(labels_df: pd.DataFrame
                            ) -> dict[str, list[tuple[pd.Timestamp, pd.Timestamp]]]:
    """Per-sensor list of (start, end) intervals across ALL labels (any
    class). Used for the viz-aligned FP overlap check."""
    out: dict[str, list[tuple[pd.Timestamp, pd.Timestamp]]] = {}
    for _, lab in labels_df.iterrows():
        s = pd.Timestamp(lab["start"]); e = pd.Timestamp(lab["end"])
        out.setdefault(str(lab["sensor_id"]), []).append((s, e))
    return out


def score_block(labels_df: pd.DataFrame, det_df: pd.DataFrame,
                block: str) -> dict:
    """block in {'user_behavior', 'sensor_fault'}.

    Two-tier class filter, matching the viz layer's split:

    - TP candidate pool: `inferred_class in {block, "unknown"}`. Unknown
      (detector-combo chains that didn't classify cleanly) can still
      credit a TP if it happens to type-match a block label in the
      credit window.
    - FP candidate pool: `inferred_class == block` only. This mirrors
      viz `user_visible_fps`, which counts only chains classified as
      `user_behavior` as user-visible FPs (unknown chains are neither
      surfaced as FP nor as suppressed in the report).

    No sensor restriction — viz doesn't restrict either, so a chain on
    a sensor with no block labels still counts as FP if it has no
    label overlap.
    """
    # Filter labels to block (for TP/FN)
    if "label_class" in labels_df.columns:
        block_labels = labels_df[labels_df["label_class"] == block]
    else:
        # Legacy: classify by anomaly type
        pick = is_user_behavior if block == "user_behavior" else is_sensor_fault
        block_labels = labels_df[labels_df["anomaly_type"].apply(pick)]

    # All-label intervals for the viz-aligned overlap check.
    all_label_intervals = _build_label_intervals(labels_df)

    # TP candidate pool: block class or unknown
    if "inferred_class" in det_df.columns:
        det = det_df[(det_df["inferred_class"] == block)
                      | (det_df["inferred_class"] == "unknown")
                      | det_df["inferred_class"].isna()].copy()
    else:
        det = det_df.copy()

    n_labels = len(block_labels)
    if n_labels == 0:
        return {"n_labels": 0, "tp": 0, "fp": 0, "covered": 0, "fn": 0,
                "tp_weight_sum": 0.0, "fp_weight_sum": 0.0,
                "raw_score": 0.0, "raw_max": 1.0, "score": 100.0}

    # Parse detection timestamps
    for col in ("start", "end", "first_fire_ts"):
        if col in det.columns:
            det[col] = pd.to_datetime(det[col])
    labels = _prepare_labels(block_labels)

    det_list = list(det.itertuples())
    det_types = [_pred_type(d._asdict()) for d in det_list]

    # Pass 1: assign TP primary per block label (type-matching, in credit window).
    tp_assignments: dict[int, int] = {}
    det_status: dict[int, str] = {}
    tp_weight_sum = 0.0
    fn_count = 0

    for li, L in enumerate(labels):
        best = None
        for di, d in enumerate(det_list):
            if d.sensor_id != L.sensor_id:
                continue
            t_fire = (d.first_fire_ts
                      if hasattr(d, "first_fire_ts") and pd.notna(d.first_fire_ts)
                      else d.start)
            if t_fire < L.window_start or t_fire > L.window_end:
                continue
            if det_types[di] != L.atype:
                continue
            if best is None or t_fire < best[1]:
                best = (di, t_fire)
        if best is None:
            fn_count += 1
            continue
        di, t_fire = best
        tp_assignments[li] = di
        weight = _sigmoid_score(t_fire, L.window_start, L.window_end)
        tp_weight_sum += weight
        det_status[di] = "TP"

    # Pass 2: viz-aligned categorization for the rest. FP pool is the
    # block class only (unknown is excluded — viz also doesn't surface
    # unknown chains as user-visible FPs).
    fp_count = 0
    fp_weight_sum = 0.0
    covered_count = 0
    for di, d in enumerate(det_list):
        if di in det_status:
            continue
        d_class = getattr(d, "inferred_class", None)
        if d_class != block:
            # Unknown/null-class chain that didn't credit a TP — neither
            # FP nor covered. Skip from scoring entirely.
            continue
        sensor = d.sensor_id
        d_start = d.start
        d_end = d.end
        overlaps = False
        for s, e in all_label_intervals.get(sensor, []):
            if d_start <= e and d_end >= s:
                overlaps = True
                break
        if overlaps:
            det_status[di] = "covered"
            covered_count += 1
        else:
            det_status[di] = "FP"
            fp_count += 1
            fp_weight_sum += FP_WEIGHT

    raw_max = TP_WEIGHT * n_labels
    raw = tp_weight_sum + fp_weight_sum
    score_0_100 = 100.0 * raw / max(1e-6, raw_max)

    return {
        "n_labels": n_labels,
        "tp": sum(1 for v in det_status.values() if v == "TP"),
        "fp": fp_count,
        "covered": covered_count,
        "fn": fn_count,
        "tp_weight_sum": round(tp_weight_sum, 3),
        "fp_weight_sum": round(fp_weight_sum, 3),
        "raw_score": round(raw, 3),
        "raw_max": round(raw_max, 3),
        "score": round(score_0_100, 2),
    }


def compute_nab(labels_df: pd.DataFrame, det_df: pd.DataFrame) -> dict:
    return {
        "user_behavior": score_block(labels_df, det_df, "user_behavior"),
        "sensor_fault":  score_block(labels_df, det_df, "sensor_fault"),
    }
