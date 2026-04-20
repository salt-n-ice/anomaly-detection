from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
import pandas as pd

class Archetype(str, Enum):
    CONTINUOUS = "continuous"
    BURSTY = "bursty"
    BINARY = "binary"

@dataclass(frozen=True)
class Event:
    timestamp: pd.Timestamp
    sensor_id: str
    capability: str
    value: float
    unit: str = ""

@dataclass
class SensorConfig:
    sensor_id: str
    capability: str
    archetype: Archetype
    expected_interval_sec: float
    min_value: float | None = None
    max_value: float | None = None
    cumulative: bool = False
    heartbeat_sec: float | None = None
    granularity_sec: int = 60
    deterministic_trigger: bool = False

    @property
    def key(self) -> tuple[str, str]:
        return (self.sensor_id, self.capability)

    @property
    def max_gap_sec(self) -> float:
        return 5.0 * self.expected_interval_sec

@dataclass(frozen=True)
class Alert:
    sensor_id: str
    capability: str
    timestamp: pd.Timestamp
    detector: str
    score: float
    threshold: float
    anomaly_type: str | None = None
    raw_value: float | None = None
    state: int | None = None
    window_start: pd.Timestamp | None = None
    window_end: pd.Timestamp | None = None
    context: list[dict] | None = None
