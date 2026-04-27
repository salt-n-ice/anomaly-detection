from __future__ import annotations
from dataclasses import dataclass
from typing import Callable
from .core import Archetype, SensorConfig
from .detectors import (Detector, EventDetector, DataQualityGate, RecentShift,
                         StateTransition, RollingMedianPeakShift, DutyCycleShift)
from .fusion import DefaultAlertFuser, AcceptAll


DetectorFactory = Callable[[SensorConfig], Detector]
EventFactory    = Callable[[SensorConfig], EventDetector]
FuserFactory    = Callable[[SensorConfig], DefaultAlertFuser]


@dataclass(frozen=True)
class ArchetypeProfile:
    short_event: list[EventFactory]
    short_tick:  list[DetectorFactory]
    medium:      list[DetectorFactory]
    long_tick:   list[DetectorFactory]
    long_fuser:  FuserFactory


def _continuous_fuser(cfg):
    return DefaultAlertFuser(cfg, gap=15*60, max_span=96*3600,
                              corroboration=AcceptAll())


def _default_fuser(cfg):
    # BURSTY / BINARY: 4h gap. Bursty detectors (DCS-6h, RMP) have 2h
    # cooldown — at smaller gaps every cooldown-period fire is its own
    # chain. At 4h gap, sustained anomalies fuse into one chain (one
    # notification per anomaly window).
    return DefaultAlertFuser(cfg, gap=4*3600, max_span=96*3600,
                              corroboration=AcceptAll())


PROFILES: dict[Archetype, ArchetypeProfile] = {
    Archetype.CONTINUOUS: ArchetypeProfile(
        short_event=[DataQualityGate],
        short_tick=[],
        medium=[RecentShift],
        long_tick=[],
        long_fuser=_continuous_fuser,
    ),
    Archetype.BURSTY: ArchetypeProfile(
        short_event=[DataQualityGate],
        short_tick=[],
        medium=[DutyCycleShift, RollingMedianPeakShift],
        long_tick=[],
        long_fuser=_default_fuser,
    ),
    Archetype.BINARY: ArchetypeProfile(
        short_event=[DataQualityGate],
        short_tick=[StateTransition],
        medium=[],
        long_tick=[],
        long_fuser=_default_fuser,
    ),
}


def profile_for(cfg: SensorConfig) -> ArchetypeProfile:
    return PROFILES[cfg.archetype]
