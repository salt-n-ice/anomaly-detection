import pandas as pd, numpy as np
from anomaly.core import Event, SensorConfig, Archetype
from anomaly.pipeline import Pipeline

def ts(s): return pd.Timestamp(s, tz="UTC")

def _continuous_cfg():
    return SensorConfig("s", "v", Archetype.CONTINUOUS, expected_interval_sec=60,
                        min_value=0, max_value=1000)

def test_pipeline_dqg_alerts_immediately():
    p = Pipeline([_continuous_cfg()], bootstrap_days=1)
    alerts = p.ingest(Event(ts("2026-02-01T00:00:00Z"), "s", "v", 9999, ""))
    assert any(a.anomaly_type == "out_of_range" for a in alerts)

def test_pipeline_bootstraps_and_goes_live():
    cfg = _continuous_cfg()
    p = Pipeline([cfg], bootstrap_days=1)
    base = ts("2026-02-01T00:00:00Z")
    rng = np.random.default_rng(0)
    # 2 days of normal data → ~2880 events (1/min)
    for i in range(2880):
        p.ingest(Event(base + pd.Timedelta(seconds=60*i), "s", "v",
                       50.0 + rng.normal(), ""))
    # Inject a spike-like pattern: 5 ticks at v=500
    for i in range(5):
        p.ingest(Event(base + pd.Timedelta(seconds=60*(2880+i)), "s", "v", 500, ""))
    final = p.finalize()
    # pipeline state should report at least one detector live
    assert p.is_live(cfg.key)

def test_pipeline_dqg_out_of_range_cooldown():
    # DQG out_of_range fires once on entry then cools down — oscillating values
    # around a threshold (e.g. noise_burst crossing 0) must not flood the output.
    cfg = _continuous_cfg()
    p = Pipeline([cfg], bootstrap_days=1)
    base = ts("2026-02-01T00:00:00Z")
    a1 = p.ingest(Event(base, "s", "v", 9999, ""))
    a2 = p.ingest(Event(base + pd.Timedelta(seconds=30), "s", "v", 9999, ""))
    a3 = p.ingest(Event(base + pd.Timedelta(minutes=31), "s", "v", 9999, ""))
    assert any(a.anomaly_type == "out_of_range" for a in a1)            # first fires
    assert not any(a.anomaly_type == "out_of_range" for a in a2)        # cooldown suppresses
    assert any(a.anomaly_type == "out_of_range" for a in a3)            # beyond 30-min cooldown, fires again


def test_write_detections_includes_threshold_column(tmp_path):
    """Detection CSV carries the alert.threshold so downstream consumers
    (explain layer, eval) don't have to hardcode threshold=0.0."""
    import pandas as pd
    from anomaly.core import Alert
    from anomaly.pipeline import _write_detections

    ts = pd.Timestamp("2026-03-05T10:00:00Z")
    alerts = [
        Alert(sensor_id="s", capability="power", timestamp=ts,
              detector="duty_cycle_shift_6h", score=4.5, threshold=3.0,
              anomaly_type=None,
              window_start=ts, window_end=ts + pd.Timedelta(minutes=1)),
    ]
    out = tmp_path / "det.csv"
    _write_detections(alerts, out)
    df = pd.read_csv(out)
    assert "threshold" in df.columns
    assert df.iloc[0]["threshold"] == 3.0
