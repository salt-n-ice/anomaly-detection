from __future__ import annotations
from dataclasses import dataclass
from functools import partial
from typing import Callable
from .core import Archetype, SensorConfig
from .detectors import (Detector, EventDetector, DataQualityGate,
                         CUSUM, RecentShift, SubPCA, MultivariatePCA,
                         TemporalProfile, StateTransition)
from .fusion import (DefaultAlertFuser, PassThroughCorroboration,
                      ContinuousCorroboration)


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


# per-archetype feature maps (from the old _features_for_detectors)
_BINARY_BASE   = ["duty_cycle_1h", "duty_cycle_24h", "transitions_per_hour"]
_BINARY_FEATS  = {
    "cusum":    ["duty_cycle_24h", "transitions_per_hour"],
    "mvpca":    _BINARY_BASE + [f"{b}_diff" for b in _BINARY_BASE],
    "temporal": _BINARY_BASE,
}
_BURSTY_FEATS = {
    "cusum":    ["value"],
    "mvpca":    ["value", "time_in_state", "value_diff",
                 "value_roll_1h", "value_roll_24h"],
    "temporal": ["value"],
}
_CONT_FEATS   = {
    "cusum":    ["value"],
    "mvpca":    ["value", "value_diff", "value_roll_1h", "value_roll_24h"],
    "temporal": ["value"],
}


def _continuous_fuser(cfg):
    # CONTINUOUS: 15-min gap + CUSUM anchor-on-non-cusum — breaks stationary-voltage
    # drift chains; ContinuousCorroboration drops unsupported cusum-only artifacts.
    return DefaultAlertFuser(cfg, gap=15*60, max_span=96*3600,
                              anchor_on_non_cusum=True,
                              corroboration=ContinuousCorroboration())


def _default_fuser(cfg):
    # BURSTY / BINARY: 60-min gap, no anchor rule, no corroboration filtering.
    return DefaultAlertFuser(cfg, gap=60*60, max_span=96*3600,
                              anchor_on_non_cusum=False,
                              corroboration=PassThroughCorroboration())


# Stage 0: empty-pipeline anchor. Only DataQualityGate (sensor-fault events)
# and StateTransition (BINARY immediate triggers) remain. Every statistical
# detector (CUSUM / SubPCA / MultivariatePCA / RecentShift / TemporalProfile)
# is disabled so the precision ceiling can be measured. Stage 2+ re-adds one
# detector at a time and checks marginal contribution (PIPELINE_REDESIGN.md).
# Imports and feature maps are kept in place so Stage-2 re-introduction is a
# list-edit rather than a re-plumbing.
PROFILES: dict[Archetype, ArchetypeProfile] = {
    Archetype.CONTINUOUS: ArchetypeProfile(
        short_event=[DataQualityGate],
        short_tick=[],
        medium=[],
        long_tick=[],
        long_fuser=_continuous_fuser,
    ),
    Archetype.BURSTY: ArchetypeProfile(
        short_event=[DataQualityGate],
        short_tick=[],
        medium=[],
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
    # Stage 0: no motion-specific override (RecentShift + MvPCA are both
    # statistical detectors, disabled at this stage). Re-introduce the
    # override when Stage 2 adds a motion detector back.
    return PROFILES[cfg.archetype]
