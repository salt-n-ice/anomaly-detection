from anomaly.core import SensorConfig, Archetype
from anomaly.detectors import (DataQualityGate, CUSUM, SubPCA, MultivariatePCA,
                                TemporalProfile, StateTransition)
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
    assert p.short_tick == []  # no trigger for continuous
    medium_types = [type(f(cfg)) for f in p.medium]
    assert medium_types == [CUSUM, SubPCA, MultivariatePCA]
    long_types = [type(f(cfg)) for f in p.long_tick]
    assert long_types == [TemporalProfile]
    assert isinstance(p.long_fuser(cfg), DefaultAlertFuser)


def test_bursty_profile_shape():
    p = PROFILES[Archetype.BURSTY]
    cfg = _cfg(Archetype.BURSTY)
    assert p.short_tick == []
    assert len(p.medium) == 3
    assert len(p.long_tick) == 1


def test_binary_profile_has_state_transition_and_drops_sub_pca():
    p = PROFILES[Archetype.BINARY]
    cfg = _cfg(Archetype.BINARY)
    assert len(p.short_tick) == 1
    assert isinstance(p.short_tick[0](cfg), StateTransition)
    medium_types = [type(f(cfg)) for f in p.medium]
    assert SubPCA not in medium_types
    assert CUSUM in medium_types
    assert MultivariatePCA in medium_types


def test_continuous_cusum_has_5d_warmup():
    p = PROFILES[Archetype.CONTINUOUS]
    cfg = _cfg(Archetype.CONTINUOUS)
    cusum = p.medium[0](cfg)
    assert cusum.warmup_seconds == 5 * 86400


def test_bursty_cusum_has_no_warmup():
    p = PROFILES[Archetype.BURSTY]
    cfg = _cfg(Archetype.BURSTY)
    cusum = p.medium[0](cfg)
    assert cusum.warmup_seconds == 0
