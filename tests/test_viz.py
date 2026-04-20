import pandas as pd
from anomaly.viz import _windows, _classify
from anomaly.metrics import Interval

def ts(s):
    s = s.rstrip("Z")
    if "T" not in s:
        s += "T00:00:00"
    return pd.Timestamp(s + "+00:00")

def test_windows_splits_by_width():
    ws = list(_windows(ts("2026-02-01Z"), ts("2026-02-04Z"), pd.Timedelta("1d")))
    assert len(ws) == 3
    assert ws[0] == (ts("2026-02-01Z"), ts("2026-02-02Z"))
    assert ws[-1] == (ts("2026-02-03Z"), ts("2026-02-04Z"))

def test_windows_partial_last():
    ws = list(_windows(ts("2026-02-01T00:00:00Z"),
                       ts("2026-02-02T12:00:00Z"), pd.Timedelta("1d")))
    assert len(ws) == 2
    assert ws[1][1] == ts("2026-02-02T12:00:00Z")

def test_classify_tp_fn_fp():
    gt = [Interval("s", ts("2026-02-01Z"), ts("2026-02-01T01:00:00Z"), "a"),
          Interval("s", ts("2026-02-03Z"), ts("2026-02-03T01:00:00Z"), "b")]
    det = [Interval("s", ts("2026-02-01T00:30:00Z"),
                   ts("2026-02-01T02:00:00Z"), "x"),
           Interval("s", ts("2026-02-05Z"),
                   ts("2026-02-05T01:00:00Z"), "y")]
    tp_gt, fn, fp = _classify(gt, det)
    assert len(tp_gt) == 1 and len(fn) == 1 and len(fp) == 1

def test_render_smoke(tmp_path):
    from anomaly.viz import render
    events = pd.DataFrame({
        "timestamp": pd.to_datetime(["2026-02-01T00:00:00Z", "2026-02-01T12:00:00Z",
                                     "2026-02-02T00:00:00Z", "2026-02-02T12:00:00Z"]),
        "sensor_id": ["s","s","s","s"], "capability": ["v","v","v","v"],
        "value": [10.0, 20.0, 10.0, 15.0], "unit": ["","","",""]
    })
    labels = pd.DataFrame({
        "sensor_id": ["s"], "capability": ["v"],
        "start": pd.to_datetime(["2026-02-01T11:00:00Z"]),
        "end": pd.to_datetime(["2026-02-01T13:00:00Z"]),
        "anomaly_type": ["spike"]
    })
    det = pd.DataFrame({
        "sensor_id": ["s"], "capability": ["v"],
        "start": pd.to_datetime(["2026-02-01T11:30:00Z"]),
        "end": pd.to_datetime(["2026-02-01T11:45:00Z"]),
        "anomaly_type": ["pca"], "detector": ["sub_pca"], "score": [1.0]
    })
    out = tmp_path / "viz.pdf"
    render(events, labels, det, out, window="1d")
    assert out.exists() and out.stat().st_size > 0


def test_render_explain_relabels_detections(tmp_path, monkeypatch):
    """With explain=True, detection intervals are regrouped under the
    classifier's inferred_type rather than the raw detector string."""
    from anomaly.viz import render, _load
    import anomaly.viz as viz_mod
    events = pd.DataFrame({
        "timestamp": pd.to_datetime(["2026-02-01T00:00:00Z", "2026-02-01T12:00:00Z",
                                     "2026-02-02T00:00:00Z", "2026-02-02T12:00:00Z"]),
        "sensor_id": ["s","s","s","s"], "capability": ["v","v","v","v"],
        "value": [10.0, 20.0, 10.0, 15.0], "unit": ["","","",""]
    })
    labels = pd.DataFrame({
        "sensor_id": ["s"], "capability": ["v"],
        "start": pd.to_datetime(["2026-02-01T11:00:00Z"]),
        "end": pd.to_datetime(["2026-02-01T13:00:00Z"]),
        "anomaly_type": ["spike"]
    })
    # A statistical fused detection where anomaly_type falls back to the detector
    # string (matches pipeline._write_detections behavior).
    det = pd.DataFrame({
        "sensor_id": ["s"], "capability": ["v"],
        "start": pd.to_datetime(["2026-02-01T11:30:00Z"]),
        "end": pd.to_datetime(["2026-02-01T11:45:00Z"]),
        "anomaly_type": ["cusum+sub_pca"], "detector": ["cusum+sub_pca"],
        "score": [1.0]
    })
    # Spy on _gantt calls to inspect the anomaly_type values the detected lane sees.
    seen_det_types: list[list[str]] = []
    orig_gantt = viz_mod._gantt
    def _spy(ax, intervals, w0, w1, color, empty_label, max_rows=8):
        # Only record the blue (detected) lane.
        if color == viz_mod._DETECT:
            seen_det_types.append([iv.anomaly_type for iv in intervals])
        return orig_gantt(ax, intervals, w0, w1, color, empty_label, max_rows)
    monkeypatch.setattr(viz_mod, "_gantt", _spy)
    out = tmp_path / "viz_explain.pdf"
    render(events, labels, det, out, window="1d", explain=True)
    assert out.exists() and out.stat().st_size > 0
    # The detection was re-labeled. It's no longer "cusum+sub_pca"; it's whatever
    # classify_type decided (e.g. "shape_anomaly", "level_shift", etc.).
    all_seen = [t for page in seen_det_types for t in page]
    assert all_seen, "expected at least one detection to be passed to _gantt"
    assert "cusum+sub_pca" not in all_seen
