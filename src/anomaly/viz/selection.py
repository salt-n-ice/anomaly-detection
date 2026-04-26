"""TP/FN classification, best-chain selection, and bucket counts.

Lifted from the explain-layer's grader logic (per the 2026-04-26 spec) so it
becomes production rendering logic, not research-only.
"""
from __future__ import annotations
import pandas as pd
import numpy as np


def classify_labels(labels: pd.DataFrame,
                    detections: pd.DataFrame) -> pd.DataFrame:
    """Add `is_tp` boolean column. A label is TP iff at least one detection
    on the same sensor overlaps its [start, end] interval.
    """
    labels = labels.copy().reset_index(drop=True)
    is_tp = np.zeros(len(labels), dtype=bool)
    for pos, (_, lab) in enumerate(labels.iterrows()):
        same_sensor = detections[detections["sensor_id"] == lab["sensor_id"]]
        if len(same_sensor) == 0:
            continue
        overlap = ((same_sensor["start"] <= lab["end"])
                   & (same_sensor["end"] >= lab["start"]))
        is_tp[pos] = bool(overlap.any())
    labels["is_tp"] = is_tp
    return labels


def attach_best_chain(labels: pd.DataFrame,
                      detections: pd.DataFrame) -> pd.DataFrame:
    """Add `best_chain_idx` column. For each TP label, pick the highest-score
    overlapping chain. Prefer user-visible (`inferred_class == 'user_behavior'`)
    chains; fall back to sensor-fault if no user-visible overlap exists.
    For FN labels, leave as None (pd.NA).
    """
    labels = labels.copy()
    best_idx: list[object] = []
    for _, lab in labels.iterrows():
        if not lab["is_tp"]:
            best_idx.append(None)
            continue
        same_sensor = detections[detections["sensor_id"] == lab["sensor_id"]]
        overlap_mask = ((same_sensor["start"] <= lab["end"])
                        & (same_sensor["end"] >= lab["start"]))
        overlapping = same_sensor[overlap_mask]
        if len(overlapping) == 0:
            best_idx.append(None)
            continue
        user_visible = overlapping[overlapping["inferred_class"] == "user_behavior"]
        pool = user_visible if len(user_visible) else overlapping
        # Highest score, tie-break by earliest start
        pool = pool.sort_values(by=["score", "start"],
                                ascending=[False, True])
        best_idx.append(int(pool.index[0]))
    labels["best_chain_idx"] = best_idx
    return labels


def compute_buckets(labels: pd.DataFrame, detections: pd.DataFrame
                    ) -> tuple[int, int, list[tuple[str, int]]]:
    """Count user-visible FPs (chains with `inferred_class == 'user_behavior'`
    that don't overlap any GT label), sensor-fault suppressed chains, and
    sensor-fault counts grouped by sensor (descending).
    Returns (n_user_visible_fps, n_suppressed, suppression_by_sensor).
    """
    # Build per-sensor label intervals for fast overlap test
    label_intervals: dict[str, list[tuple[pd.Timestamp, pd.Timestamp]]] = {}
    for _, lab in labels.iterrows():
        label_intervals.setdefault(lab["sensor_id"], []).append(
            (lab["start"], lab["end"]))

    def _overlaps_any_label(row) -> bool:
        ivs = label_intervals.get(row["sensor_id"], [])
        for (s, e) in ivs:
            if row["start"] <= e and row["end"] >= s:
                return True
        return False

    n_user_fps = 0
    n_suppressed = 0
    by_sensor: dict[str, int] = {}
    for _, row in detections.iterrows():
        cls = row.get("inferred_class", "")
        if cls == "sensor_fault":
            n_suppressed += 1
            by_sensor[row["sensor_id"]] = by_sensor.get(row["sensor_id"], 0) + 1
        elif cls == "user_behavior":
            if not _overlaps_any_label(row):
                n_user_fps += 1
    suppression_sorted = sorted(by_sensor.items(),
                                key=lambda kv: -kv[1])
    return n_user_fps, n_suppressed, suppression_sorted


def select_showcases(labels: pd.DataFrame, *, max_n: int = 8) -> pd.DataFrame:
    """Curate which GT labels become showcase pages.

    1. Group labels by anomaly_type.
    2. Within each type, pick the longest-duration label.
    3. Sort candidates: TP first (caught), then duration desc, then start asc.
    4. Always include at least one FN if any FN exists.
    5. Cap at max_n.
    """
    if len(labels) == 0:
        return labels.iloc[0:0]
    df = labels.copy()
    df["_dur"] = (df["end"] - df["start"]).dt.total_seconds()
    # Pick longest per type
    candidates = (df.sort_values(by="_dur", ascending=False)
                    .groupby("anomaly_type", as_index=False).head(1))
    # TP-first ordering
    candidates = candidates.sort_values(
        by=["is_tp", "_dur", "start"],
        ascending=[False, False, True],
    )
    picks = candidates.head(max_n)
    # Force-include longest FN if any FN exists and not already in picks
    has_fn = (~df["is_tp"]).any()
    if has_fn and not (~picks["is_tp"]).any():
        longest_fn = (df[~df["is_tp"]]
                      .sort_values(by="_dur", ascending=False)
                      .head(1))
        picks = pd.concat([longest_fn, picks.head(max_n - 1)],
                          ignore_index=True)
    return picks.drop(columns=["_dur"]).reset_index(drop=True)
