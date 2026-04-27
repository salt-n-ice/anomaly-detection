from __future__ import annotations
from dataclasses import dataclass
import pandas as pd


@dataclass(frozen=True)
class Interval:
    sensor_id: str
    start: pd.Timestamp
    end: pd.Timestamp
    anomaly_type: str = ""


def _load(df: pd.DataFrame) -> list[Interval]:
    out = []
    for r in df.itertuples(index=False):
        out.append(Interval(r.sensor_id,
                            pd.Timestamp(r.start, tz="UTC") if not isinstance(r.start, pd.Timestamp) else r.start,
                            pd.Timestamp(r.end, tz="UTC") if not isinstance(r.end, pd.Timestamp) else r.end,
                            getattr(r, "anomaly_type", "")))
    return out


def _overlaps(a: Interval, b: Interval) -> bool:
    return a.sensor_id == b.sensor_id and a.start < b.end and b.start < a.end


def interval_match(gt_df: pd.DataFrame, det_df: pd.DataFrame):
    gt = _load(gt_df); det = _load(det_df)
    tp, fp, fn = [], [], []
    matched = set()
    for g in gt:
        hit = False
        for i, d in enumerate(det):
            if i in matched: continue
            if _overlaps(g, d):
                tp.append(g); matched.add(i); hit = True; break
        if not hit: fn.append(g)
    for i, d in enumerate(det):
        if i not in matched: fp.append(d)
    return tp, fp, fn


def compute_metrics(gt_df: pd.DataFrame, det_df: pd.DataFrame) -> dict:
    tp, fp, fn = interval_match(gt_df, det_df)
    ntp, nfp, nfn = len(tp), len(fp), len(fn)
    prec = ntp / (ntp + nfp) if ntp + nfp else 0.0
    rec = ntp / (ntp + nfn) if ntp + nfn else 0.0
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
    return {"tp": ntp, "fp": nfp, "fn": nfn,
            "precision": prec, "recall": rec, "f1": f1}


def pointwise_match(gt_df: pd.DataFrame, det_df: pd.DataFrame):
    """Each GT that has ANY overlapping detection is TP. Each det with ANY overlapping
    GT is TP; otherwise FP. No 1:1 consumption constraint."""
    gt = _load(gt_df); det = _load(det_df)
    tp_gt = [g for g in gt if any(_overlaps(g, d) for d in det)]
    fn = [g for g in gt if not any(_overlaps(g, d) for d in det)]
    tp_det = [d for d in det if any(_overlaps(g, d) for g in gt)]
    fp = [d for d in det if not any(_overlaps(g, d) for g in gt)]
    return tp_gt, fp, fn  # note: tp_gt length = recall-numerator


def compute_metrics_pointwise(gt_df: pd.DataFrame, det_df: pd.DataFrame) -> dict:
    tp_gt, fp, fn = pointwise_match(gt_df, det_df)
    # recall: fraction of GT covered by any det
    n_gt = len(tp_gt) + len(fn)
    # precision: fraction of det matching any GT (compute separately)
    gt = _load(gt_df); det = _load(det_df)
    n_det = len(det)
    tp_det = sum(1 for d in det if any(_overlaps(g, d) for g in gt))
    prec = tp_det / n_det if n_det else 0.0
    rec = len(tp_gt) / n_gt if n_gt else 0.0
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
    return {"tp": len(tp_gt), "fp": len(fp), "fn": len(fn),
            "precision": prec, "recall": rec, "f1": f1}


def _merge_events(ivs: list[Interval], gap: pd.Timedelta = pd.Timedelta(hours=1)) -> list[Interval]:
    """Merge per-sensor overlapping or near-adjacent intervals into event clusters.
    Fusion caps individual alerts at 96h max_span, which fragments a single sustained
    anomaly into many chunks; the user-visible alert is one event, not N chunks."""
    by_sensor: dict[str, list[Interval]] = {}
    for iv in ivs:
        by_sensor.setdefault(iv.sensor_id, []).append(iv)
    out: list[Interval] = []
    for sid, group in by_sensor.items():
        group.sort(key=lambda x: x.start)
        cur_s, cur_e, cur_t = group[0].start, group[0].end, group[0].anomaly_type
        for iv in group[1:]:
            if iv.start <= cur_e + gap:
                cur_e = max(cur_e, iv.end)
                if iv.anomaly_type and iv.anomaly_type != cur_t:
                    cur_t = f"{cur_t}|{iv.anomaly_type}" if cur_t else iv.anomaly_type
            else:
                out.append(Interval(sid, cur_s, cur_e, cur_t))
                cur_s, cur_e, cur_t = iv.start, iv.end, iv.anomaly_type
        out.append(Interval(sid, cur_s, cur_e, cur_t))
    return out


def compute_metrics_time(gt_df: pd.DataFrame, det_df: pd.DataFrame) -> dict:
    """Duration-weighted confusion metric (seconds).

    Event F1 counts a 3-day FP strip the same as a 10-min FP, which hides the
    calendar cost of multi-day detector drift chains (e.g. voltage cusum+sub_pca
    fusing into 1-3 day bands on stationary noise). This metric sweeps each
    sensor timeline and accumulates elapsed time into TP/FP/FN buckets:

    - TP-sec: seconds where a GT interval and a det interval are both active
    - FP-sec: seconds where a det interval is active but no GT interval is
    - FN-sec: seconds where a GT interval is active but no det interval is

    Precision/recall/F1 are computed on these seconds, and per-sensor
    breakdowns are returned so voltage vs power strips are visible separately.
    """
    gt = _load(gt_df); det = _load(det_df)
    sensors = set(iv.sensor_id for iv in gt) | set(iv.sensor_id for iv in det)
    tp_sec = fp_sec = fn_sec = 0.0
    per_sensor: dict[str, dict[str, float]] = {}
    for s in sensors:
        gt_s = [iv for iv in gt if iv.sensor_id == s]
        det_s = [iv for iv in det if iv.sensor_id == s]
        events: list[tuple[pd.Timestamp, int, int]] = []
        for iv in gt_s:
            events.append((iv.start, 0, +1)); events.append((iv.end, 0, -1))
        for iv in det_s:
            events.append((iv.start, 1, +1)); events.append((iv.end, 1, -1))
        if not events:
            continue
        # Apply closings before openings at the same timestamp (stable counts).
        events.sort(key=lambda x: (x[0], x[2]))
        gt_open = det_open = 0
        prev_ts = events[0][0]
        s_tp = s_fp = s_fn = 0.0
        for ts, kind, delta in events:
            dt = (ts - prev_ts).total_seconds()
            if dt > 0:
                if gt_open > 0 and det_open > 0:
                    s_tp += dt
                elif det_open > 0:
                    s_fp += dt
                elif gt_open > 0:
                    s_fn += dt
            if kind == 0:
                gt_open += delta
            else:
                det_open += delta
            prev_ts = ts
        tp_sec += s_tp; fp_sec += s_fp; fn_sec += s_fn
        per_sensor[s] = {"tp_sec": s_tp, "fp_sec": s_fp, "fn_sec": s_fn}
    prec = tp_sec / (tp_sec + fp_sec) if (tp_sec + fp_sec) > 0 else 0.0
    rec = tp_sec / (tp_sec + fn_sec) if (tp_sec + fn_sec) > 0 else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
    return {"tp_sec": tp_sec, "fp_sec": fp_sec, "fn_sec": fn_sec,
            "time_precision": prec, "time_recall": rec, "time_f1": f1,
            "per_sensor": per_sensor}


def _load_with_fire_ts(df: pd.DataFrame) -> list[tuple[Interval, pd.Timestamp]]:
    """Load intervals alongside the earliest fire-tick for latency measurement.

    Reads `first_fire_ts` when present (added by `_write_detections` so the
    fused chain's earliest component tick is preserved instead of being
    collapsed into `window_start`). Falls back to `start` for legacy CSVs
    that predate the column; that fallback reproduces the old behavior.
    """
    has_ffts = "first_fire_ts" in df.columns
    out: list[tuple[Interval, pd.Timestamp]] = []
    for r in df.itertuples(index=False):
        iv = Interval(r.sensor_id,
                      pd.Timestamp(r.start, tz="UTC") if not isinstance(r.start, pd.Timestamp) else r.start,
                      pd.Timestamp(r.end, tz="UTC") if not isinstance(r.end, pd.Timestamp) else r.end,
                      getattr(r, "anomaly_type", ""))
        if has_ffts and pd.notna(r.first_fire_ts):
            fire = (pd.Timestamp(r.first_fire_ts, tz="UTC")
                    if not isinstance(r.first_fire_ts, pd.Timestamp)
                    else r.first_fire_ts)
        else:
            fire = iv.start
        out.append((iv, fire))
    return out


def compute_metrics_latency(gt_df: pd.DataFrame, det_df: pd.DataFrame) -> dict:
    """Per-label first-alert latency, in seconds.

    For each GT label matched by at least one overlapping detection, latency is
    `max(0, earliest_overlap_fire - label.start)` where `fire` is the
    detector's first-fire tick (`first_fire_ts` column; falls back to
    `start` on legacy CSVs without the column). Using the fire tick instead
    of `window_start` avoids collapsing real post-onset firing delay to
    zero when (a) sliding-window detectors back-date their `window_start`
    by the window length and (b) cross-label fused chains inherit an
    earlier component's `window_start`.

    Clamp-at-zero preserves the "alert available at or before label start
    = zero latency" reading; negative leading edges (detection fires
    slightly before label) aren't a virtue we reward and they aren't a cost
    we penalize.

    Unmatched GT labels (FN) are excluded — latency is undefined for misses, and
    `incident_recall` / `evt_recall` already account for them.

    The caller can restrict the detector set (e.g. to filter out DQG) by passing
    a pre-filtered `det_df`. This keeps the function signature narrow and lets us
    measure multiple latency breakdowns in the same evaluation pass without
    coupling the function to detector-name taxonomy.
    """
    gt = _load(gt_df); det_pairs = _load_with_fire_ts(det_df)
    lags: list[float] = []
    for g in gt:
        overlaps = [(d, fire) for d, fire in det_pairs if _overlaps(g, d)]
        if not overlaps:
            continue
        first_fire = min(fire for _, fire in overlaps)
        lags.append(max(0.0, (first_fire - g.start).total_seconds()))
    if not lags:
        return {"n_tp_labels": 0, "latency_mean_s": None,
                "latency_median_s": None, "latency_p95_s": None,
                "latency_max_s": None}
    s = pd.Series(lags)
    return {
        "n_tp_labels": int(s.shape[0]),
        "latency_mean_s": float(s.mean()),
        "latency_median_s": float(s.median()),
        "latency_p95_s": float(s.quantile(0.95)),
        "latency_max_s": float(s.max()),
    }


def compute_metrics_onset_timing(gt_df: pd.DataFrame, det_df: pd.DataFrame) -> dict:
    """Per-label timing split into early lead and late start.

    `compute_metrics_latency()` collapses every matched label whose first
    overlapping detection fires before the label into `0s`. That is useful for
    "was an alert already present by label start?" but it hides long pre-label
    bridge chains. This helper keeps the two directions separate:

    - early_lead_*: how far before label start the first overlapping detection
      fires (0 if it fires at/after the label)
    - late_start_*: how far after label start the first overlapping detection
      fires (0 if it fires at/before the label)

    Both are reported across matched labels, so zeros remain part of the
    distribution. Counts of early/late labels are included for interpretation.

    Uses `first_fire_ts` when present (earliest component tick in a fused
    chain) — same rationale as `compute_metrics_latency`.
    """
    gt = _load(gt_df); det_pairs = _load_with_fire_ts(det_df)
    early_leads: list[float] = []
    late_starts: list[float] = []
    n_missed = 0
    for g in gt:
        overlaps = [(d, fire) for d, fire in det_pairs if _overlaps(g, d)]
        if not overlaps:
            n_missed += 1
            continue
        first_fire = min(fire for _, fire in overlaps)
        early_leads.append(max(0.0, (g.start - first_fire).total_seconds()))
        late_starts.append(max(0.0, (first_fire - g.start).total_seconds()))
    if not early_leads:
        return {
            "n_matched_labels": 0,
            "n_missed_labels": int(n_missed),
            "n_early_labels": 0,
            "n_late_labels": 0,
            "early_lead_mean_s": None,
            "early_lead_p95_s": None,
            "early_lead_max_s": None,
            "late_start_mean_s": None,
            "late_start_p95_s": None,
            "late_start_max_s": None,
        }
    early = pd.Series(early_leads)
    late = pd.Series(late_starts)
    return {
        "n_matched_labels": int(len(early_leads)),
        "n_missed_labels": int(n_missed),
        "n_early_labels": int(sum(x > 0 for x in early_leads)),
        "n_late_labels": int(sum(x > 0 for x in late_starts)),
        "early_lead_mean_s": float(early.mean()),
        "early_lead_p95_s": float(early.quantile(0.95)),
        "early_lead_max_s": float(early.max()),
        "late_start_mean_s": float(late.mean()),
        "late_start_p95_s": float(late.quantile(0.95)),
        "late_start_max_s": float(late.max()),
    }


def compute_metrics_event(gt_df: pd.DataFrame, det_df: pd.DataFrame,
                          merge_gap: pd.Timedelta = pd.Timedelta(hours=1)) -> dict:
    """Event-level F1: merge overlapping/near-adjacent detections into event clusters
    (the user-facing unit — one sustained alert is one event regardless of internal
    chunking), then TP/FP/FN over events vs GT. This is the honest number when long
    labels cause the pipeline to fuse into multiple bounded chunks."""
    gt = _load(gt_df)
    det_events = _merge_events(_load(det_df), merge_gap)
    tp_gt = [g for g in gt if any(_overlaps(g, e) for e in det_events)]
    fn = [g for g in gt if g not in tp_gt]
    tp_events = [e for e in det_events if any(_overlaps(g, e) for g in gt)]
    fp = [e for e in det_events if e not in tp_events]
    ntp, nfp, nfn = len(tp_gt), len(fp), len(fn)
    # precision uses detection-events as the denominator, not GTs
    n_events = len(det_events)
    prec = len(tp_events) / n_events if n_events else 0.0
    rec = ntp / (ntp + nfn) if ntp + nfn else 0.0
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
    return {"tp": ntp, "fp": nfp, "fn": nfn,
            "precision": prec, "recall": rec, "f1": f1,
            "n_events": n_events}


# ----- Duration-stratified metrics ------------------------------------------
#
# Length-weighted aggregates (time_F1, latency_p95) bias toward long anomalies:
# a 28-day level_shift contributes ~4000x more seconds than a 30-min water leak,
# so the aggregate "rewards" any pipeline that covers long labels even if it
# completely misses short ones. Flat latency floors (e.g. 600s) are lethal for
# short labels (33% elapsed before alert) and trivial for long ones (<0.03%).
#
# These helpers bucket GT labels by duration and report metrics per bucket, so
# a regression on any one band is visible instead of being averaged out.

DURATION_BUCKETS: list[tuple[str, float, float]] = [
    # (name, min_seconds_inclusive, max_seconds_exclusive)
    ("short",  0.0,       3600.0),          # < 1h     — leaks, dips
    ("medium", 3600.0,    86400.0),         # 1h–24h   — weekend anomaly, occupancy
    ("long",   86400.0,   float("inf")),    # > 24h    — level_shift, WFH, month_shift
]


def _bucket_of(duration_s: float) -> str:
    for name, lo, hi in DURATION_BUCKETS:
        if lo <= duration_s < hi:
            return name
    return DURATION_BUCKETS[-1][0]


def compute_metrics_by_bucket(gt_df: pd.DataFrame, det_df: pd.DataFrame) -> dict:
    """Per-bucket recall + fractional-latency, keyed by GT label duration.

    Returned dict structure:
        {
          "short":  {"n_labels": N, "incident_recall": r, "time_recall": r,
                     "lat_frac_p95": f, "lat_frac_max": f, "n_matched": m},
          "medium": {...},
          "long":   {...},
        }

    Precision-side metrics (time_precision, fp_h_per_day) are NOT bucketed
    because an FP is by definition "detection outside any GT" and has no
    natural bucket assignment. Those remain global in the caller.

    `lat_frac` = latency_seconds / label_duration_seconds — fraction of the
    GT label elapsed before first-fire. `lat_frac_p95 = 0.10` means "the 95th
    percentile label had 10% of its duration pass before any alert". Flat-
    seconds floors don't capture this; a 600s lag on a 30-min leak is 33%,
    on a 28-day shift it's 0.025%.
    """
    gt = _load(gt_df)
    det_pairs = _load_with_fire_ts(det_df)

    out: dict[str, dict] = {}
    for name, lo, hi in DURATION_BUCKETS:
        bucket_gt = [g for g in gt
                     if lo <= (g.end - g.start).total_seconds() < hi]
        n_labels = len(bucket_gt)
        if n_labels == 0:
            out[name] = {"n_labels": 0, "incident_recall": None,
                         "time_recall": None, "lat_frac_p95": None,
                         "lat_frac_max": None, "n_matched": 0}
            continue

        # Incident recall: each GT in bucket is TP if ANY det overlaps.
        n_matched = 0
        fractional_lags: list[float] = []
        tp_sec = 0.0
        gt_sec = 0.0
        for g in bucket_gt:
            duration = (g.end - g.start).total_seconds()
            gt_sec += duration
            overlaps = [(d, fire) for d, fire in det_pairs if _overlaps(g, d)]
            if not overlaps:
                continue
            n_matched += 1
            first_fire = min(fire for _, fire in overlaps)
            lag = max(0.0, (first_fire - g.start).total_seconds())
            fractional_lags.append(lag / duration if duration > 0 else 0.0)

            # TP-sec for this label: intersected seconds across all overlapping dets.
            events: list[tuple[pd.Timestamp, int]] = []
            events.append((g.start, +1)); events.append((g.end, -1))
            for d, _ in overlaps:
                events.append((max(d.start, g.start), +2))
                events.append((min(d.end, g.end), -2))
            events.sort(key=lambda x: (x[0], x[1]))
            gt_open = det_open = 0
            prev_ts = events[0][0]
            for ts, delta in events:
                dt = (ts - prev_ts).total_seconds()
                if dt > 0 and gt_open > 0 and det_open > 0:
                    tp_sec += dt
                if abs(delta) == 1:
                    gt_open += (1 if delta > 0 else -1)
                else:
                    det_open += (1 if delta > 0 else -1)
                prev_ts = ts

        incR = n_matched / n_labels
        time_rec = tp_sec / gt_sec if gt_sec > 0 else 0.0

        if fractional_lags:
            s = pd.Series(fractional_lags)
            lat_p95 = float(s.quantile(0.95))
            lat_max = float(s.max())
        else:
            lat_p95 = lat_max = None

        out[name] = {
            "n_labels": int(n_labels),
            "n_matched": int(n_matched),
            "incident_recall": round(float(incR), 4),
            "time_recall": round(float(time_rec), 4),
            "lat_frac_p95": None if lat_p95 is None else round(lat_p95, 4),
            "lat_frac_max": None if lat_max is None else round(lat_max, 4),
        }
    return out


# ---------------------------------------------------------------------------
# Stratified evaluation — BEHAVIOR (user-facing) vs sensor_fault.
#
# The headline numbers reported in the README + research log come from
# splitting GT by `label_class` (column on labels.csv), restricting
# detections to the GT-bearing sensors, then computing the standard
# metrics on each block. `user_visible_fps_per_day` counts chains the
# pipeline classified `user_behavior` that don't overlap ANY GT label
# (any class) on the same sensor — i.e. the user-visible false-alarm
# count the production LLM would get pinged for.
# ---------------------------------------------------------------------------


def _stratify_gt(gt: pd.DataFrame, klass: str) -> pd.DataFrame:
    """Return GT labels of one class. Falls back to all labels when the
    `label_class` column is absent (legacy datasets)."""
    if "label_class" not in gt.columns:
        return gt
    return gt[gt["label_class"] == klass].reset_index(drop=True)


def _restrict_det_to_sensors(det: pd.DataFrame,
                             gt_subset: pd.DataFrame) -> pd.DataFrame:
    """A detection only counts as an FP for THIS class if it fired on a
    sensor that actually carries GT of THIS class. Otherwise a detection
    on a sensor whose GT labels are all the other class would count as
    a class-FP unfairly."""
    sensors = set(gt_subset["sensor_id"].unique())
    if not sensors:
        return det.iloc[0:0]
    return det[det["sensor_id"].isin(sensors)]


def _filter_det_by_class(det: pd.DataFrame, klass: str) -> pd.DataFrame:
    """Keep detections whose `inferred_class` is `klass` or `unknown`/NaN.
    A confidently-other-class chain is dropped (e.g. a DQG `dropout`
    claim doesn't TP a `water_leak_sustained` GT). Falls back to passing
    everything through when the column is missing."""
    if "inferred_class" not in det.columns:
        return det
    return det[(det["inferred_class"] == klass)
               | (det["inferred_class"] == "unknown")
               | det["inferred_class"].isna()]


def _count_class_fps_no_overlap(det: pd.DataFrame, all_labels: pd.DataFrame,
                                klass: str) -> int:
    """Chains classified `klass` that don't overlap any GT label on the
    same sensor (any-class overlap exempts)."""
    if "inferred_class" not in det.columns or len(det) == 0:
        return 0
    cls_chains = det[det["inferred_class"] == klass]
    if len(cls_chains) == 0:
        return 0
    label_intervals: dict[str, list[tuple[pd.Timestamp, pd.Timestamp]]] = {}
    for _, lab in all_labels.iterrows():
        s = pd.Timestamp(lab["start"]); e = pd.Timestamp(lab["end"])
        label_intervals.setdefault(str(lab["sensor_id"]), []).append((s, e))
    n = 0
    for _, row in cls_chains.iterrows():
        sensor = str(row["sensor_id"])
        s = pd.Timestamp(row["start"]); e = pd.Timestamp(row["end"])
        if not any(s <= le and e >= ls
                    for ls, le in label_intervals.get(sensor, [])):
            n += 1
    return n


def _round_or_none(x, ndigits: int):
    return None if x is None or pd.isna(x) else round(float(x), ndigits)


def _stratified_block(gt: pd.DataFrame, det: pd.DataFrame, klass: str,
                       timeline_days: float) -> dict:
    sub_gt = _stratify_gt(gt, klass)
    sub_det = _restrict_det_to_sensors(det, sub_gt)
    sub_det = _filter_det_by_class(sub_det, klass)
    if sub_gt.empty:
        return {"n_labels": 0}
    mev = compute_metrics_event(sub_gt, sub_det)
    mpw = compute_metrics_pointwise(sub_gt, sub_det)
    mtm = compute_metrics_time(sub_gt, sub_det)
    sub_det_nondqg = sub_det[sub_det["detector"] != "data_quality_gate"]
    mlat_nd = compute_metrics_latency(sub_gt, sub_det_nondqg)
    n_uv = _count_class_fps_no_overlap(det, gt, klass)
    return {
        "n_labels": int(len(sub_gt)),
        "evt_f1": round(float(mev["f1"]), 4),
        "evt_precision": round(float(mev["precision"]), 4),
        "evt_recall": round(float(mev["recall"]), 4),
        "time_f1": round(float(mtm["time_f1"]), 4),
        "time_precision": round(float(mtm["time_precision"]), 4),
        "time_recall": round(float(mtm["time_recall"]), 4),
        "incident_recall": round(float(mpw["recall"]), 4),
        "n_user_visible_fps": int(n_uv),
        "user_visible_fps_per_day": round(
            float(n_uv / max(1e-6, timeline_days)), 3),
        "nondqg_latency_p95_s": _round_or_none(mlat_nd["latency_p95_s"], 1),
    }


def compute_stratified(gt_df: pd.DataFrame, det_df: pd.DataFrame,
                       timeline_days: float) -> dict:
    """Headline-metrics dict with `behavior` + `sensor_fault` blocks.

    `timeline_days` is the scenario span used to normalize the
    user-visible FP rate; pass `(events.timestamp.max() -
    events.timestamp.min()).days` (or label-derived if events isn't
    available).

    BEHAVIOR is the user-facing optimization target; the FAULT block is
    reported for visibility but isn't gated. See README §"Evaluate
    against ground truth" for the metric semantics.
    """
    return {
        "behavior":     _stratified_block(gt_df, det_df, "user_behavior",
                                          timeline_days),
        "sensor_fault": _stratified_block(gt_df, det_df, "sensor_fault",
                                          timeline_days),
        "timeline_days": round(float(timeline_days), 3),
    }
