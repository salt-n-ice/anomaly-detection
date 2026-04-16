import math, pandas as pd
from anomaly.core import SensorConfig, Archetype
from anomaly.features import FeatureEngineer

def ts(s): return pd.Timestamp(s, tz="UTC")

def _cfg(arch=Archetype.CONTINUOUS, gran=60):
    return SensorConfig("s", "v", arch, expected_interval_sec=60, granularity_sec=gran)

def test_calendar_added():
    fe = FeatureEngineer(_cfg())
    out = fe.enrich(ts("2026-02-02T14:30:00Z"), {"value": 1.0})
    assert out["hour"] == 14
    assert out["dow"] == 0  # Monday
    assert out["is_weekend"] == 0
    assert out["month"] == 2

def test_first_diff():
    fe = FeatureEngineer(_cfg())
    fe.enrich(ts("2026-02-02T00:00:00Z"), {"value": 10.0})
    out = fe.enrich(ts("2026-02-02T00:01:00Z"), {"value": 13.0})
    assert out["value_diff"] == 3.0

def test_rolling_mean_1h_window():
    fe = FeatureEngineer(_cfg())
    # fill 60 ticks of 10.0
    for i in range(60):
        fe.enrich(ts("2026-02-02T00:00:00Z") + pd.Timedelta(minutes=i), {"value": 10.0})
    out = fe.enrich(ts("2026-02-02T01:00:00Z"), {"value": 20.0})
    assert abs(out["value_roll_1h"] - (60*10 + 20) / 61) < 1e-6

def test_bursty_per_state_rolling():
    fe = FeatureEngineer(_cfg(Archetype.BURSTY))
    base = ts("2026-02-02T00:00:00Z")
    for i in range(5):
        fe.enrich(base + pd.Timedelta(minutes=i), {"value": 10.0, "state": 0})
    out = fe.enrich(base + pd.Timedelta(minutes=5), {"value": 100.0, "state": 1})
    # state 1 has only one sample, so diff = 0 (first sample in state)
    assert out["value_diff"] == 0.0
