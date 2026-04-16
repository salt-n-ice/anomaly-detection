from __future__ import annotations
from collections import deque
import math
import pandas as pd
from .core import SensorConfig, Archetype


NUMERIC_SKIP = {"dropout", "trigger"}


class FeatureEngineer:
    def __init__(self, config: SensorConfig):
        self.config = config
        self._tick_sec = config.granularity_sec
        self._w1h = 3600 // self._tick_sec + 1
        self._w24h = 86400 // self._tick_sec + 1
        self._w7d = 604800 // self._tick_sec + 1
        # per-state rolling buffers + running sums + last value for diff
        self._buf: dict[tuple[int, str, int], deque[float]] = {}  # (state,feat,window)
        self._sum: dict[tuple[int, str, int], float] = {}         # O(1) rolling mean
        self._last: dict[tuple[int, str], float] = {}

    def _state_of(self, feat: dict) -> int:
        if self.config.archetype == Archetype.BURSTY:
            return int(feat.get("state", 0))
        return 0

    def _numeric_keys(self, feat: dict) -> list[str]:
        return [k for k, v in feat.items()
                if k not in NUMERIC_SKIP and isinstance(v, (int, float))
                and not isinstance(v, bool)]

    def enrich(self, ts: pd.Timestamp, feat: dict) -> dict:
        out = dict(feat)
        out["hour"] = ts.hour
        out["dow"] = ts.dayofweek
        out["is_weekend"] = 1 if ts.dayofweek >= 5 else 0
        out["month"] = ts.month
        state = self._state_of(feat)
        for k in self._numeric_keys(feat):
            v = float(feat[k])
            if math.isnan(v):
                out[f"{k}_diff"] = float("nan")
                out[f"{k}_roll_1h"] = v
                out[f"{k}_roll_24h"] = v
                out[f"{k}_roll_7d"] = v
                continue
            # diff
            prev = self._last.get((state, k))
            out[f"{k}_diff"] = 0.0 if prev is None else v - prev
            self._last[(state, k)] = v
            # rolling (incremental: O(1) per update instead of O(window_len))
            for w, wlen in (("1h", self._w1h), ("24h", self._w24h), ("7d", self._w7d)):
                key = (state, k, wlen)
                dq = self._buf.setdefault(key, deque(maxlen=wlen))
                s = self._sum.get(key, 0.0)
                if len(dq) == wlen:
                    s -= dq[0]  # subtract value about to be evicted
                dq.append(v)
                s += v
                self._sum[key] = s
                out[f"{k}_roll_{w}"] = s / len(dq)
        return out
