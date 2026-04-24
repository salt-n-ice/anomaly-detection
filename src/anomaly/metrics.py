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


def compute_metrics_latency(gt_df: pd.DataFrame, det_df: pd.DataFrame) -> dict:
    """Per-label first-alert latency, in seconds.

    For each GT label matched by at least one overlapping detection, latency is
    `max(0, earliest_overlap_det.start - label.start)`. Clamp-at-zero preserves
    the "alert available at or before label start = zero latency" reading;
    negative leading edges (detection fires slightly before label) aren't a
    virtue we reward and they aren't a cost we penalize.

    Unmatched GT labels (FN) are excluded — latency is undefined for misses, and
    `incident_recall` / `evt_recall` already account for them.

    The caller can restrict the detector set (e.g. to filter out DQG) by passing
    a pre-filtered `det_df`. This keeps the function signature narrow and lets us
    measure multiple latency breakdowns in the same evaluation pass without
    coupling the function to detector-name taxonomy.
    """
    gt = _load(gt_df); det = _load(det_df)
    lags: list[float] = []
    for g in gt:
        overlaps = [d for d in det if _overlaps(g, d)]
        if not overlaps:
            continue
        first_start = min(d.start for d in overlaps)
        lags.append(max(0.0, (first_start - g.start).total_seconds()))
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
    overlapping detection starts before the label into `0s`. That is useful for
    "was an alert already present by label start?" but it hides long pre-label
    bridge chains. This helper keeps the two directions separate:

    - early_lead_*: how far before label start the first overlapping detection
      begins (0 if it starts at/after the label)
    - late_start_*: how far after label start the first overlapping detection
      begins (0 if it starts at/before the label)

    Both are reported across matched labels, so zeros remain part of the
    distribution. Counts of early/late labels are included for interpretation.
    """
    gt = _load(gt_df); det = _load(det_df)
    early_leads: list[float] = []
    late_starts: list[float] = []
    n_missed = 0
    for g in gt:
        overlaps = [d for d in det if _overlaps(g, d)]
        if not overlaps:
            n_missed += 1
            continue
        first_start = min(d.start for d in overlaps)
        early_leads.append(max(0.0, (g.start - first_start).total_seconds()))
        late_starts.append(max(0.0, (first_start - g.start).total_seconds()))
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
