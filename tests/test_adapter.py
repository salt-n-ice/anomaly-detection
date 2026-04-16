import pandas as pd
from anomaly.core import Event, Archetype, SensorConfig
from anomaly.adapter import make_adapter

def ts(s): return pd.Timestamp(s, tz="UTC")

def _cfg(arch, **kw):
    defaults = dict(sensor_id="s", capability="v", archetype=arch,
                    expected_interval_sec=60, granularity_sec=60)
    defaults.update(kw)
    return SensorConfig(**defaults)

def _ev(t, v, cfg):
    return Event(ts(t), cfg.sensor_id, cfg.capability, v, "")

def test_continuous_regular_passthrough():
    cfg = _cfg(Archetype.CONTINUOUS)
    ad = make_adapter(cfg)
    ad.ingest(_ev("2026-02-01T00:00:00Z", 10.0, cfg))
    ad.ingest(_ev("2026-02-01T00:01:00Z", 12.0, cfg))
    ticks = list(ad.emit_ready(ts("2026-02-01T00:01:00Z")))
    assert [t.strftime("%M:%S") for t, _ in ticks] == ["00:00", "01:00"]
    assert ticks[0][1]["value"] == 10.0
    assert ticks[1][1]["value"] == 12.0

def test_continuous_interpolation():
    cfg = _cfg(Archetype.CONTINUOUS, expected_interval_sec=120)
    ad = make_adapter(cfg)
    ad.ingest(_ev("2026-02-01T00:00:00Z", 0.0, cfg))
    ad.ingest(_ev("2026-02-01T00:02:00Z", 20.0, cfg))
    ticks = list(ad.emit_ready(ts("2026-02-01T00:02:00Z")))
    values = [round(f["value"], 3) for _, f in ticks]
    assert values == [0.0, 10.0, 20.0]

def test_continuous_gap_emits_nan_and_flag():
    cfg = _cfg(Archetype.CONTINUOUS, expected_interval_sec=60)  # max_gap=300s
    ad = make_adapter(cfg)
    ad.ingest(_ev("2026-02-01T00:00:00Z", 10.0, cfg))
    ad.ingest(_ev("2026-02-01T00:10:00Z", 10.0, cfg))  # 600s gap > 300s
    ticks = list(ad.emit_ready(ts("2026-02-01T00:10:00Z")))
    nan_ticks = [f for _, f in ticks if pd.isna(f["value"])]
    assert len(nan_ticks) >= 5  # interior ticks are NaN
    assert any(f.get("dropout") for _, f in ticks)

import numpy as np

def test_bursty_zero_order_hold_and_state():
    cfg = _cfg(Archetype.BURSTY, expected_interval_sec=60)
    ad = make_adapter(cfg)
    # bootstrap: bimodal stream, 5 off @ 2W, 5 on @ 100W
    pts = [(0, 2), (60, 2), (120, 2), (180, 2), (240, 2),
           (300, 100), (360, 100), (420, 100), (480, 100), (540, 100)]
    base = ts("2026-02-01T00:00:00Z")
    for sec, v in pts:
        ad.ingest(_ev((base + pd.Timedelta(seconds=sec)).isoformat(), v, cfg))
    list(ad.emit_ready(base + pd.Timedelta(seconds=540)))
    ad.fit_state_model()
    # next tick should have a state assigned
    ad.ingest(_ev((base + pd.Timedelta(seconds=600)).isoformat(), 100, cfg))
    ticks = list(ad.emit_ready(base + pd.Timedelta(seconds=600)))
    assert ticks, "expected at least one tick"
    last = ticks[-1][1]
    assert last["state"] in (0, 1)
    assert "time_in_state" in last

def test_bursty_cumulative_differencing():
    import math as _math
    cfg = _cfg(Archetype.BURSTY, expected_interval_sec=60, cumulative=True)
    ad = make_adapter(cfg)
    base = ts("2026-02-01T00:00:00Z")
    # Counter grows by 5 per minute. Rate should emerge as ~5 per tick.
    for i, v in enumerate([0.0, 5.0, 10.0, 15.0]):
        ad.ingest(_ev((base + pd.Timedelta(seconds=60*i)).isoformat(), v, cfg))
    ticks = list(ad.emit_ready(base + pd.Timedelta(seconds=180)))
    rates = [f["value"] for _, f in ticks if not _math.isnan(f["value"])]
    assert any(abs(r - 5.0) < 1e-6 for r in rates), rates

def test_binary_derived_features():
    cfg = _cfg(Archetype.BINARY, expected_interval_sec=600)
    ad = make_adapter(cfg)
    base = ts("2026-02-01T00:00:00Z")
    # 0, 1, 0 pattern every 30 min over 2h
    evs = [(0, 0), (30*60, 1), (60*60, 0), (90*60, 1), (120*60, 0)]
    for sec, v in evs:
        ad.ingest(_ev((base + pd.Timedelta(seconds=sec)).isoformat(), v, cfg))
    ticks = list(ad.emit_ready(base + pd.Timedelta(seconds=120*60)))
    last = ticks[-1][1]
    assert "transitions_per_hour" in last
    assert "duty_cycle_1h" in last
    assert "duty_cycle_24h" in last
    # 4 transitions in 2h → last hour saw 2 transitions
    assert last["transitions_per_hour"] >= 1

def test_binary_deterministic_trigger():
    cfg = _cfg(Archetype.BINARY, expected_interval_sec=600, deterministic_trigger=True)
    ad = make_adapter(cfg)
    base = ts("2026-02-01T00:00:00Z")
    ad.ingest(_ev(base.isoformat(), 0, cfg))
    ad.ingest(_ev((base + pd.Timedelta(seconds=60)).isoformat(), 1, cfg))
    ticks = list(ad.emit_ready(base + pd.Timedelta(seconds=60)))
    transitions = [f for _, f in ticks if f.get("trigger")]
    assert transitions, "expected deterministic trigger flag on 0->1"
