import numpy as np, pandas as pd
from anomaly.batch import matrix_profile_discords
from anomaly.core import SensorConfig, Archetype

def ts(s): return pd.Timestamp(s, tz="UTC")

def test_matrix_profile_finds_injected_discord():
    cfg = SensorConfig("s","v", Archetype.CONTINUOUS, 60)
    # 500 points of clean sine, with a sharp square wave inserted at 200..240
    t = np.linspace(0, 50, 500)
    y = np.sin(t)
    y[200:240] = 3.0
    base = ts("2026-02-01T00:00:00Z")
    series = [(base + pd.Timedelta(seconds=60*i), float(y[i])) for i in range(500)]
    alerts = matrix_profile_discords(cfg, series, window_sec=40*60)  # 40 ticks at 60s tick rate
    assert alerts, "expected at least one discord"
    # discord should span around index 200..240
    hits = [a for a in alerts if 200 <= ((a.window_start - base).total_seconds()/60) <= 250]
    assert hits, f"expected a discord covering the injected region, got {alerts}"
