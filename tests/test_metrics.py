import pandas as pd
from anomaly.metrics import interval_match, compute_metrics

def _df(rows):
    return pd.DataFrame(rows, columns=["sensor_id","start","end","anomaly_type"])

def test_interval_match_basic():
    gt = _df([("s","2026-02-01T00:00:00Z","2026-02-01T00:10:00Z","spike")])
    det = _df([("s","2026-02-01T00:05:00Z","2026-02-01T00:15:00Z","spike")])
    tp, fp, fn = interval_match(gt, det)
    assert len(tp) == 1 and len(fp) == 0 and len(fn) == 0

def test_interval_match_no_overlap():
    gt = _df([("s","2026-02-01T00:00:00Z","2026-02-01T00:10:00Z","spike")])
    det = _df([("s","2026-02-01T01:00:00Z","2026-02-01T01:10:00Z","spike")])
    tp, fp, fn = interval_match(gt, det)
    assert len(tp) == 0 and len(fp) == 1 and len(fn) == 1

def test_compute_metrics():
    gt = _df([("s","2026-02-01T00:00:00Z","2026-02-01T00:10:00Z","spike"),
              ("s","2026-02-01T02:00:00Z","2026-02-01T02:10:00Z","dip")])
    det = _df([("s","2026-02-01T00:05:00Z","2026-02-01T00:15:00Z","spike")])
    m = compute_metrics(gt, det)
    assert m["tp"] == 1 and m["fp"] == 0 and m["fn"] == 1
    assert abs(m["recall"] - 0.5) < 1e-9
    assert abs(m["precision"] - 1.0) < 1e-9


def test_pointwise_match_one_det_matches_two_gt():
    from anomaly.metrics import pointwise_match, compute_metrics_pointwise
    gt = _df([("s","2026-02-01T00:00:00Z","2026-02-01T00:10:00Z","a"),
              ("s","2026-02-01T00:05:00Z","2026-02-01T00:15:00Z","b")])
    det = _df([("s","2026-02-01T00:00:00Z","2026-02-01T00:30:00Z","x")])
    tp, fp, fn = pointwise_match(gt, det)
    assert len(tp) == 2 and len(fp) == 0 and len(fn) == 0
    m = compute_metrics_pointwise(gt, det)
    assert m["recall"] == 1.0
