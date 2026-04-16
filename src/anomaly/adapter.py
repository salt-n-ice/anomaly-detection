from __future__ import annotations
from collections import deque
from typing import Iterator
import math
import numpy as np
import pandas as pd
from .core import Event, Archetype, SensorConfig


class Adapter:
    archetype: Archetype
    def __init__(self, config: SensorConfig):
        self.config = config
        self._tick_sec = config.granularity_sec
        self._next_tick: pd.Timestamp | None = None

    def ingest(self, ev: Event) -> None: raise NotImplementedError
    def emit_ready(self, now: pd.Timestamp) -> Iterator[tuple[pd.Timestamp, dict]]:
        raise NotImplementedError

    def relabel(self, feat: dict) -> dict:
        return dict(feat)

    def _align_up(self, ts: pd.Timestamp) -> pd.Timestamp:
        sec = ts.value // 10**9
        aligned = ((sec + self._tick_sec - 1) // self._tick_sec) * self._tick_sec
        return pd.Timestamp(aligned * 10**9, tz="UTC")


class ContinuousAdapter(Adapter):
    archetype = Archetype.CONTINUOUS

    def __init__(self, config: SensorConfig):
        super().__init__(config)
        self._pts: list[tuple[pd.Timestamp, float]] = []

    def ingest(self, ev: Event) -> None:
        self._pts.append((ev.timestamp, float(ev.value)))

    def emit_ready(self, now: pd.Timestamp) -> Iterator[tuple[pd.Timestamp, dict]]:
        if not self._pts: return
        if self._next_tick is None:
            self._next_tick = self._align_up(self._pts[0][0])
        step = pd.Timedelta(seconds=self._tick_sec)
        max_gap = pd.Timedelta(seconds=self.config.max_gap_sec)
        while self._next_tick <= now:
            tick = self._next_tick
            # trim: keep at most one point with ts <= tick, plus later points
            while len(self._pts) >= 2 and self._pts[1][0] <= tick:
                self._pts.pop(0)
            if not self._pts or self._pts[0][0] > tick:
                return
            a_ts, a_val = self._pts[0]
            if len(self._pts) < 2:
                # only one point ≤ tick; ZOH, NaN if too stale
                if (tick - a_ts) > max_gap:
                    value, dropout = math.nan, True
                else:
                    value, dropout = a_val, False
            else:
                b_ts, b_val = self._pts[1]
                if b_ts - a_ts > max_gap:
                    value, dropout = math.nan, True
                else:
                    frac = (tick - a_ts).total_seconds() / (b_ts - a_ts).total_seconds()
                    value = a_val + (b_val - a_val) * frac
                    dropout = False
            yield tick, {"value": float(value), "dropout": dropout}
            self._next_tick = tick + step


class BurstyAdapter(Adapter):
    archetype = Archetype.BURSTY

    def __init__(self, config: SensorConfig):
        super().__init__(config)
        self._pts: list[tuple[pd.Timestamp, float]] = []
        self._state_centers: np.ndarray | None = None
        self._state: int = 0
        self._state_entered: pd.Timestamp | None = None
        self._bootstrap_values: list[float] = []

    def ingest(self, ev: Event) -> None:
        self._pts.append((ev.timestamp, float(ev.value)))

    def fit_state_model(self) -> None:
        vs = np.asarray(self._bootstrap_values, dtype=float)
        vs = vs[~np.isnan(vs)]
        if vs.size < 4:
            self._state_centers = np.array([float(vs.mean()) if vs.size else 0.0])
            return
        lo, hi = np.percentile(vs, [10, 90])
        centers = np.array([lo, hi], dtype=float)
        for _ in range(20):
            d = np.abs(vs[:, None] - centers[None, :])
            labels = d.argmin(axis=1)
            new = np.array([vs[labels == k].mean() if (labels == k).any() else centers[k]
                            for k in range(2)])
            if np.allclose(new, centers): break
            centers = new
        self._state_centers = np.sort(centers)

    def _assign_state(self, value: float) -> int:
        if self._state_centers is None or math.isnan(value):
            return 0
        return int(np.argmin(np.abs(self._state_centers - value)))

    def relabel(self, feat: dict) -> dict:
        g = dict(feat)
        v = g.get("value")
        if v is not None and not (isinstance(v, float) and math.isnan(v)):
            g["state"] = self._assign_state(float(v))
        return g

    def _value_at_tick(self, tick: pd.Timestamp, max_gap: pd.Timedelta) -> tuple[float, bool]:
        a_ts, a_val = self._pts[0]
        if tick - a_ts > max_gap:
            return math.nan, True
        if not self.config.cumulative:
            return float(a_val), False
        # cumulative counter → Δvalue/Δt as per-tick rate
        if len(self._pts) < 2:
            return 0.0, False
        b_ts, b_val = self._pts[1]
        dt = (b_ts - a_ts).total_seconds()
        if dt <= 0: return 0.0, False
        return float((b_val - a_val) * (self._tick_sec / dt)), False

    def emit_ready(self, now: pd.Timestamp) -> Iterator[tuple[pd.Timestamp, dict]]:
        if not self._pts: return
        if self._next_tick is None:
            self._next_tick = self._align_up(self._pts[0][0])
        step = pd.Timedelta(seconds=self._tick_sec)
        max_gap = pd.Timedelta(seconds=self.config.max_gap_sec)
        while self._next_tick <= now:
            tick = self._next_tick
            while len(self._pts) >= 2 and self._pts[1][0] <= tick:
                self._pts.pop(0)
            if not self._pts or self._pts[0][0] > tick:
                return
            value, dropout = self._value_at_tick(tick, max_gap)
            self._bootstrap_values.append(value)
            new_state = self._assign_state(value)
            if new_state != self._state or self._state_entered is None:
                self._state = new_state
                self._state_entered = tick
            tis = (tick - self._state_entered).total_seconds()
            yield tick, {"value": value, "state": new_state,
                         "time_in_state": tis, "dropout": dropout}
            self._next_tick = tick + step


class BinaryAdapter(Adapter):
    archetype = Archetype.BINARY

    def __init__(self, config: SensorConfig):
        super().__init__(config)
        self._pts: list[tuple[pd.Timestamp, int]] = []
        self._transitions: deque[pd.Timestamp] = deque()
        self._history_1h: deque[tuple[pd.Timestamp, int]] = deque()
        self._history_24h: deque[tuple[pd.Timestamp, int]] = deque()
        self._last_transition: pd.Timestamp | None = None
        self._pending_triggers: list[pd.Timestamp] = []

    def ingest(self, ev: Event) -> None:
        self._pts.append((ev.timestamp, int(round(float(ev.value)))))

    def emit_ready(self, now: pd.Timestamp) -> Iterator[tuple[pd.Timestamp, dict]]:
        if not self._pts: return
        if self._next_tick is None:
            self._next_tick = self._align_up(self._pts[0][0])
        step = pd.Timedelta(seconds=self._tick_sec)
        h1 = pd.Timedelta(hours=1); h24 = pd.Timedelta(hours=24)
        while self._next_tick <= now:
            tick = self._next_tick
            # advance pts, record transitions as we pass them
            while len(self._pts) >= 2 and self._pts[1][0] <= tick:
                _, sp = self._pts[0]
                tn, sn = self._pts[1]
                if sn != sp:
                    self._transitions.append(tn)
                    self._last_transition = tn
                    if sn == 1 and self.config.deterministic_trigger:
                        self._pending_triggers.append(tn)
                self._pts.pop(0)
            if not self._pts or self._pts[0][0] > tick:
                return
            s = self._pts[0][1]
            # roll deques
            self._history_1h.append((tick, s))
            self._history_24h.append((tick, s))
            while self._history_1h and (tick - self._history_1h[0][0]) > h1:
                self._history_1h.popleft()
            while self._history_24h and (tick - self._history_24h[0][0]) > h24:
                self._history_24h.popleft()
            while self._transitions and (tick - self._transitions[0]) > h1:
                self._transitions.popleft()
            duty1 = sum(x for _, x in self._history_1h) / max(1, len(self._history_1h))
            duty24 = sum(x for _, x in self._history_24h) / max(1, len(self._history_24h))
            tslt = (tick - self._last_transition).total_seconds() if self._last_transition else 0.0
            feat = {"state": s,
                    "time_since_last_transition": tslt,
                    "transitions_per_hour": float(len(self._transitions)),
                    "duty_cycle_1h": duty1, "duty_cycle_24h": duty24,
                    "dropout": False}
            if self._pending_triggers:
                fired = any(t <= tick for t in self._pending_triggers)
                if fired:
                    feat["trigger"] = True
                    self._pending_triggers = [t for t in self._pending_triggers if t > tick]
            yield tick, feat
            self._next_tick = tick + step


ADAPTER_REGISTRY: dict[Archetype, type[Adapter]] = {
    Archetype.CONTINUOUS: ContinuousAdapter,
    Archetype.BURSTY: BurstyAdapter,
    Archetype.BINARY: BinaryAdapter,
}


def make_adapter(config: SensorConfig) -> Adapter:
    return ADAPTER_REGISTRY[config.archetype](config)
