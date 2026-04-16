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
