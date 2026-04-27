from anomaly.core import SensorConfig, Archetype
from anomaly.detectors import (DataQualityGate, RecentShift, RollingMedianPeakShift,
                                DutyCycleShift, StateTransition)
from anomaly.fusion import DefaultAlertFuser
from anomaly.profiles import PROFILES


def _cfg(arch):
    return SensorConfig("s", "v", arch, expected_interval_sec=60,
                        min_value=0, max_value=100)


def test_profiles_has_three_archetypes():
    assert set(PROFILES.keys()) == {Archetype.CONTINUOUS, Archetype.BURSTY, Archetype.BINARY}


def test_continuous_profile_shape():
    p = PROFILES[Archetype.CONTINUOUS]
    cfg = _cfg(Archetype.CONTINUOUS)
    assert len(p.short_event) == 1
    assert isinstance(p.short_event[0](cfg), DataQualityGate)
    assert p.short_tick == []
    medium_types = [type(f(cfg)) for f in p.medium]
    assert medium_types == [RecentShift]
    assert p.long_tick == []
    assert isinstance(p.long_fuser(cfg), DefaultAlertFuser)


def test_bursty_profile_shape():
    p = PROFILES[Archetype.BURSTY]
    cfg = _cfg(Archetype.BURSTY)
    assert len(p.short_event) == 1
    assert isinstance(p.short_event[0](cfg), DataQualityGate)
    assert p.short_tick == []
    medium_types = [type(f(cfg)) for f in p.medium]
    assert medium_types == [DutyCycleShift, RollingMedianPeakShift]
    assert p.long_tick == []
    assert isinstance(p.long_fuser(cfg), DefaultAlertFuser)


def test_binary_profile_shape():
    p = PROFILES[Archetype.BINARY]
    cfg = _cfg(Archetype.BINARY)
    assert len(p.short_event) == 1
    assert isinstance(p.short_event[0](cfg), DataQualityGate)
    assert len(p.short_tick) == 1
    assert isinstance(p.short_tick[0](cfg), StateTransition)
    assert p.medium == []
    assert p.long_tick == []
    assert isinstance(p.long_fuser(cfg), DefaultAlertFuser)
