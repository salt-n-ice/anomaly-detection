import pandas as pd
from anomaly.core import Event, SensorConfig, Archetype
from anomaly.detectors import DataQualityGate

def ts(s): return pd.Timestamp(s, tz="UTC")

def _cfg(**kw):
    d = dict(sensor_id="s", capability="v", archetype=Archetype.CONTINUOUS,
             expected_interval_sec=60, min_value=0, max_value=100)
    d.update(kw)
    return SensorConfig(**d)

def test_dqg_out_of_range():
    dqg = DataQualityGate(_cfg())
    alerts = dqg.check(Event(ts("2026-02-01T00:00:00Z"), "s", "v", 999, ""))
    assert any(a.anomaly_type == "out_of_range" for a in alerts)

def test_dqg_saturation_repeat_at_max():
    cfg = _cfg(max_value=50)
    dqg = DataQualityGate(cfg)
    alerts = []
    base = ts("2026-02-01T00:00:00Z")
    for i in range(12):
        alerts += dqg.check(Event(base + pd.Timedelta(seconds=60*i), "s", "v", 50, ""))
    assert any(a.anomaly_type == "saturation" for a in alerts)

def test_dqg_duplicate_stale():
    dqg = DataQualityGate(_cfg())
    base = ts("2026-02-01T00:00:00Z")
    dqg.check(Event(base, "s", "v", 10.0, ""))
    alerts = dqg.check(Event(base, "s", "v", 10.0, ""))
    assert any(a.anomaly_type == "duplicate_stale" for a in alerts)

def test_dqg_clock_drift_ewma():
    # New clock_drift semantics: EWMA of (actual_gap - expected_interval) on
    # CONTINUOUS sensors. Seed with on-cadence events, then stretch intervals
    # to simulate drift; expect clock_drift within a few drifted events.
    cfg = _cfg(expected_interval_sec=60)
    dqg = DataQualityGate(cfg)
    base = ts("2026-02-01T00:00:00Z")
    alerts = []
    for i in range(3):
        alerts += dqg.check(Event(base + pd.Timedelta(seconds=60 * i), "s", "v", 10.0, ""))
    # Drift: each subsequent event 75s after previous (delta_tick = +15s).
    t = base + pd.Timedelta(seconds=60 * 2)
    for _ in range(10):
        t = t + pd.Timedelta(seconds=75)
        alerts += dqg.check(Event(t, "s", "v", 10.0, ""))
    assert any(a.anomaly_type == "clock_drift" for a in alerts)

def test_dqg_no_clock_drift_on_cadence():
    # Stationary sensor at exact cadence should never fire clock_drift.
    cfg = _cfg(expected_interval_sec=60)
    dqg = DataQualityGate(cfg)
    base = ts("2026-02-01T00:00:00Z")
    alerts = []
    for i in range(200):
        alerts += dqg.check(Event(base + pd.Timedelta(seconds=60 * i), "s", "v", 10.0, ""))
    assert not any(a.anomaly_type == "clock_drift" for a in alerts)

def test_dqg_dropout():
    cfg = _cfg(expected_interval_sec=60)  # max_gap=300s
    dqg = DataQualityGate(cfg)
    base = ts("2026-02-01T00:00:00Z")
    dqg.check(Event(base, "s", "v", 10.0, ""))
    alerts = dqg.check(Event(base + pd.Timedelta(seconds=600), "s", "v", 10.0, ""))
    assert any(a.anomaly_type == "dropout" for a in alerts)

def test_dqg_batch_arrival():
    dqg = DataQualityGate(_cfg())
    base = ts("2026-02-01T00:00:00Z")
    alerts = []
    for i in range(15):
        alerts += dqg.check(Event(base + pd.Timedelta(milliseconds=i), "s", "v", 10.0+i, ""))
    assert any(a.anomaly_type == "batch_arrival" for a in alerts)


def test_dqg_context_populated_on_fire():
    dqg = DataQualityGate(_cfg())
    a = dqg.check(Event(ts("2026-02-01T00:00:00Z"), "s", "v", 999, ""))
    oor = next(x for x in a if x.anomaly_type == "out_of_range")
    assert oor.context is not None
    assert oor.context[0]["detector"] == "data_quality_gate"
    assert oor.context[0]["reason"] == "out_of_range"
    assert oor.context[0]["value"] == 999
    assert oor.context[0]["limit"] == 100

from anomaly.detectors import StateTransition


def test_state_transition_fires_on_trigger():
    cfg = SensorConfig("leak", "water", Archetype.BINARY,
                       expected_interval_sec=3600, deterministic_trigger=True)
    d = StateTransition(cfg)
    d.fit([])
    assert d.live is True
    t = ts("2026-02-01T00:00:00Z")
    out = d.update(t, {"trigger": True, "state": 1})
    assert len(out) == 1
    assert out[0].detector == "state_transition"
    assert out[0].anomaly_type == "water_leak_sustained"
    assert out[0].state == 1


def test_state_transition_silent_without_trigger():
    cfg = SensorConfig("leak", "water", Archetype.BINARY,
                       expected_interval_sec=3600)
    d = StateTransition(cfg)
    d.fit([])
    t = ts("2026-02-01T00:00:00Z")
    assert d.update(t, {"state": 0}) == []
    assert d.update(t, {"trigger": False, "state": 1}) == []
