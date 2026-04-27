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


# ----- Per-fire metrics + fractional latency -------------------------------

def _det_df(rows):
    """rows: list of dicts; missing fields fall back to defaults."""
    cols = ["sensor_id","start","end","first_fire_ts","fire_ticks",
            "anomaly_type","inferred_type","inferred_class","detector",
            "threshold","score"]
    return pd.DataFrame([
        {**{c: "" for c in cols}, **r} for r in rows
    ])[cols]


def test_lat_frac_bridge_chain_does_not_credit_zero():
    """A chain with one fire 1h BEFORE the label and one fire 30min INTO
    the label (label = 2h long). The chain's `first_fire_ts` is the
    pre-label fire — old-style latency would clamp to 0. The new metric
    must use the in-GT tick (30min into a 2h label = 25%).
    """
    from anomaly.metrics import compute_metrics_lat_frac
    gt = _df([("s", "2026-02-01T01:00:00Z", "2026-02-01T03:00:00Z", "level_shift")])
    # Chain bridges T-1h pre-label and T+30min in-label; first_fire_ts
    # is the earlier (pre-label) tick — the bug we're fixing.
    det = _det_df([{
        "sensor_id": "s",
        "start": "2026-02-01T00:00:00Z",
        "end":   "2026-02-01T01:31:00Z",
        "first_fire_ts": "2026-02-01T00:00:00Z",
        "fire_ticks": "2026-02-01T00:00:00Z;2026-02-01T01:30:00Z",
        "anomaly_type": "level_shift", "inferred_type": "level_shift",
        "inferred_class": "user_behavior", "detector": "rs",
        "threshold": 1.0, "score": 2.0,
    }])
    m = compute_metrics_lat_frac(gt, det)
    # 30min into a 2h label = 0.25
    assert m["n_matched"] == 1
    assert abs(m["lat_frac_p95"] - 0.25) < 1e-6, m


def test_lat_frac_multi_label_span_per_label_lag():
    """One chain bridges label A and label B. Old-style: both labels
    read the chain's `first_fire_ts` (which is in label A) — label B
    looks instantly caught. New: each label uses its own in-label fire.
    """
    from anomaly.metrics import compute_metrics_lat_frac
    gt = _df([
        ("s", "2026-02-01T00:00:00Z", "2026-02-01T01:00:00Z", "spike"),
        ("s", "2026-02-01T02:00:00Z", "2026-02-01T03:00:00Z", "dip"),
    ])
    # Chain: fires at A+5min and B+45min. Without per-fire ticks, the
    # `first_fire_ts` (A+5min) would credit B as instantly caught.
    det = _det_df([{
        "sensor_id": "s",
        "start": "2026-02-01T00:05:00Z",
        "end":   "2026-02-01T02:46:00Z",
        "first_fire_ts": "2026-02-01T00:05:00Z",
        "fire_ticks": "2026-02-01T00:05:00Z;2026-02-01T02:45:00Z",
        "anomaly_type": "spike", "inferred_type": "spike",
        "inferred_class": "user_behavior", "detector": "rs",
        "threshold": 1.0, "score": 2.0,
    }])
    m = compute_metrics_lat_frac(gt, det)
    assert m["n_matched"] == 2
    # Label A: 5min/60min = 0.0833; Label B: 45min/60min = 0.75
    # P95 must be ≈0.75, NOT ≈0.083 (which the old metric would give).
    assert abs(m["lat_frac_max"] - 0.75) < 1e-6, m
    assert abs(m["lat_frac_p50"] - 0.4167) < 1e-3, m


def test_lat_frac_pre_label_only_unmatched():
    """A chain with fires only BEFORE the label leaves the label as FN
    in the lat_frac metric (no in-GT tick → not counted)."""
    from anomaly.metrics import compute_metrics_lat_frac
    gt = _df([("s", "2026-02-01T01:00:00Z", "2026-02-01T02:00:00Z", "spike")])
    det = _det_df([{
        "sensor_id": "s",
        "start": "2026-02-01T00:00:00Z",
        "end":   "2026-02-01T00:30:00Z",
        "first_fire_ts": "2026-02-01T00:00:00Z",
        "fire_ticks": "2026-02-01T00:00:00Z;2026-02-01T00:30:00Z",
        "anomaly_type": "spike", "inferred_type": "spike",
        "inferred_class": "user_behavior", "detector": "rs",
        "threshold": 1.0, "score": 2.0,
    }])
    m = compute_metrics_lat_frac(gt, det)
    assert m["n_matched"] == 0
    assert m["lat_frac_p95"] is None


def test_per_fire_purity_and_type_acc():
    """Two chains, four fires:
      - Chain 1: 2 fires inside label A, type matches → 2 in_gt + 2 type_correct
      - Chain 2: 1 fire inside label A, type MISMATCH → 1 in_gt + 0 type_correct
                 1 fire after label A ends → fp
    Expected: total=4, in_gt=3, type_correct=2 → fp=1
              fire_purity = 0.75, type_acc = 2/3 = 0.6667
    """
    from anomaly.metrics import compute_metrics_per_fire
    gt = _df([("s", "2026-02-01T01:00:00Z", "2026-02-01T02:00:00Z", "level_shift")])
    det = _det_df([
        {"sensor_id": "s",
         "start": "2026-02-01T01:10:00Z",
         "end":   "2026-02-01T01:50:00Z",
         "first_fire_ts": "2026-02-01T01:10:00Z",
         "fire_ticks": "2026-02-01T01:10:00Z;2026-02-01T01:30:00Z",
         "anomaly_type": "level_shift", "inferred_type": "level_shift",
         "inferred_class": "user_behavior", "detector": "rs",
         "threshold": 1.0, "score": 2.0},
        {"sensor_id": "s",
         "start": "2026-02-01T01:40:00Z",
         "end":   "2026-02-01T03:31:00Z",
         "first_fire_ts": "2026-02-01T01:40:00Z",
         "fire_ticks": "2026-02-01T01:40:00Z;2026-02-01T03:30:00Z",
         "anomaly_type": "spike", "inferred_type": "spike",
         "inferred_class": "user_behavior", "detector": "dcs",
         "threshold": 1.0, "score": 2.0},
    ])
    m = compute_metrics_per_fire(gt, det, timeline_days=1.0)
    assert m["n_fires"] == 4
    assert m["n_in_gt"] == 3
    assert m["n_type_correct"] == 2
    assert m["n_fp_fires"] == 1
    assert abs(m["fire_purity"] - 0.75) < 1e-6
    assert abs(m["type_acc"] - 2/3) < 1e-3
    assert abs(m["fp_fires_per_day"] - 1.0) < 1e-6


def test_per_fire_legacy_csv_no_fire_ticks_column():
    """Legacy detection CSVs (pre-`fire_ticks`) must still grade — falls
    back to one fire per chain at `first_fire_ts`."""
    from anomaly.metrics import compute_metrics_per_fire
    gt = _df([("s", "2026-02-01T01:00:00Z", "2026-02-01T02:00:00Z", "spike")])
    # Build det without the fire_ticks column entirely.
    det = pd.DataFrame([{
        "sensor_id": "s",
        "start": "2026-02-01T01:10:00Z",
        "end":   "2026-02-01T01:50:00Z",
        "first_fire_ts": "2026-02-01T01:30:00Z",
        "anomaly_type": "spike", "inferred_type": "spike",
        "inferred_class": "user_behavior", "detector": "rs",
        "threshold": 1.0, "score": 2.0,
    }])
    m = compute_metrics_per_fire(gt, det, timeline_days=1.0)
    assert m["n_fires"] == 1
    assert m["n_in_gt"] == 1
    assert m["fire_purity"] == 1.0


def test_per_fire_no_in_gt_fires_type_acc_is_none():
    """Detector fires only OUTSIDE any GT — type_acc is undefined
    (None), not 1.0 by default."""
    from anomaly.metrics import compute_metrics_per_fire
    gt = _df([("s", "2026-02-01T01:00:00Z", "2026-02-01T02:00:00Z", "spike")])
    det = _det_df([{
        "sensor_id": "s",
        "start": "2026-02-01T03:00:00Z",
        "end":   "2026-02-01T03:01:00Z",
        "first_fire_ts": "2026-02-01T03:00:00Z",
        "fire_ticks": "2026-02-01T03:00:00Z",
        "anomaly_type": "spike", "inferred_type": "spike",
        "inferred_class": "user_behavior", "detector": "rs",
        "threshold": 1.0, "score": 2.0,
    }])
    m = compute_metrics_per_fire(gt, det, timeline_days=1.0)
    assert m["n_fires"] == 1
    assert m["n_in_gt"] == 0
    assert m["fire_purity"] == 0.0
    assert m["type_acc"] is None
