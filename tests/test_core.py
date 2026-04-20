from anomaly.core import Event, Alert, Archetype, SensorConfig
import pandas as pd

def test_archetype_values():
    assert Archetype.CONTINUOUS.value == "continuous"
    assert Archetype.BURSTY.value == "bursty"
    assert Archetype.BINARY.value == "binary"

def test_event_roundtrip():
    ev = Event(pd.Timestamp("2026-02-01T00:00:00Z"), "s", "power", 41.5, "W")
    assert ev.value == 41.5
    assert ev.capability == "power"

def test_sensor_config_defaults():
    c = SensorConfig("s", "power", Archetype.BURSTY, expected_interval_sec=300)
    assert c.granularity_sec == 60
    assert c.cumulative is False
    assert c.deterministic_trigger is False

def test_alert_fields():
    a = Alert("s", "power", pd.Timestamp("2026-02-01T00:00:00Z"), "cusum",
              1.0, 0.5, None, 100.0, 1, None, None)
    assert a.detector == "cusum"

def test_alert_carries_context_list():
    a = Alert(
        sensor_id="s", capability="v", timestamp=pd.Timestamp("2026-01-01", tz="UTC"),
        detector="cusum", score=1.0, threshold=0.5,
        context=[{"detector": "cusum", "mu": 10.0, "sigma": 1.0}],
    )
    assert a.context == [{"detector": "cusum", "mu": 10.0, "sigma": 1.0}]

def test_alert_context_defaults_to_none():
    a = Alert(sensor_id="s", capability="v",
              timestamp=pd.Timestamp("2026-01-01", tz="UTC"),
              detector="d", score=0.0, threshold=0.0)
    assert a.context is None
