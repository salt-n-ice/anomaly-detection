from __future__ import annotations
from typing import Protocol
import pandas as pd
from .core import Alert, SensorConfig


class CorroborationRule(Protocol):
    def accepts(self, alerts: list[Alert]) -> bool: ...


class AcceptAll:
    """Trivial corroboration rule: every assembled chain emits."""
    def accepts(self, alerts: list[Alert]) -> bool:
        return True


def group_alerts(alerts: list[Alert]) -> Alert:
    top = max(alerts, key=lambda a: a.score)
    w0 = min((a.window_start or a.timestamp) for a in alerts)
    w1 = max((a.window_end or a.timestamp) for a in alerts)
    first_fire = min(a.timestamp for a in alerts)
    fire_ticks = tuple(sorted(a.timestamp for a in alerts))
    names = "+".join(sorted({a.detector for a in alerts}))
    ctx: list[dict] = []
    for a in alerts:
        if a.context:
            ctx.extend(a.context)
    return Alert(top.sensor_id, top.capability, top.timestamp, names,
                 top.score, top.threshold, top.anomaly_type, top.raw_value,
                 top.state, w0, w1, ctx or None, first_fire, fire_ticks)


class DefaultAlertFuser:
    """Per-sensor alert fuser.

    Immediate alerts (state_transition, DQG non-dropout) pass through on ingest.
    Statistical alerts (and DQG `dropout`) buffer in a pending chain that
    flushes when (1) the gap to the newest pending alert exceeds `gap` or
    (2) the chain span exceeds `max_span`. On flush, if `corroboration.accepts`
    passes, emits one grouped alert via `group_alerts`.
    """
    def __init__(self, cfg: SensorConfig, *, gap: int, max_span: int,
                 corroboration: CorroborationRule):
        self.cfg = cfg
        self.gap = pd.Timedelta(seconds=gap)
        self.max_span = pd.Timedelta(seconds=max_span)
        self.rule = corroboration
        self._pending: list[Alert] = []
        self._newest_ts: pd.Timestamp | None = None

    @staticmethod
    def _is_immediate(a: Alert) -> bool:
        if a.detector == "state_transition": return True
        if a.detector == "data_quality_gate":
            return a.anomaly_type != "dropout"
        return False

    def _flush(self) -> list[Alert]:
        if not self._pending:
            return []
        emitted: list[Alert] = []
        if self.rule.accepts(self._pending):
            emitted.append(group_alerts(self._pending))
        self._pending = []
        self._newest_ts = None
        return emitted

    def ingest(self, fresh: list[Alert]) -> list[Alert]:
        out: list[Alert] = []
        for a in fresh:
            if self._is_immediate(a):
                out.append(a)
                continue
            if self._pending:
                gap_exceeded = (self._newest_ts is not None
                                and a.timestamp - self._newest_ts > self.gap)
                span_exceeded = (a.timestamp - self._pending[0].timestamp) > self.max_span
                if gap_exceeded or span_exceeded:
                    out.extend(self._flush())
            self._pending.append(a)
            if self._newest_ts is None or a.timestamp > self._newest_ts:
                self._newest_ts = a.timestamp
        return out

    def finalize(self) -> list[Alert]:
        return self._flush()
