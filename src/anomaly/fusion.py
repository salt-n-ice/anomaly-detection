from __future__ import annotations
from typing import Protocol
import pandas as pd
from .core import Alert, Archetype, SensorConfig


class CorroborationRule(Protocol):
    def accepts(self, alerts: list[Alert]) -> bool: ...


class PassThroughCorroboration:
    """BURSTY / BINARY — only filters marginal single-detector `temporal_profile`
    singletons (|z| within 20% of threshold); everything else passes through."""
    def accepts(self, alerts: list[Alert]) -> bool:
        dets = {a.detector for a in alerts}
        if dets == {"temporal_profile"}:
            return any(a.score >= 1.2 * a.threshold for a in alerts)
        return True


class ContinuousCorroboration:
    """CONTINUOUS sensors — filter FP chains from autocorrelation, stationary
    PCA residuals, and stuck-sub_pca artifacts. Ported verbatim from the
    previous `_chain_corroborated` in pipeline.py."""
    def accepts(self, alerts: list[Alert]) -> bool:
        dets = {a.detector for a in alerts}
        duration = alerts[-1].timestamp - alerts[0].timestamp if len(alerts) >= 2 else pd.Timedelta(0)
        if dets == {"cusum"}:
            return duration >= pd.Timedelta(hours=90) and len(alerts) >= 2
        if dets in ({"cusum", "sub_pca"}, {"cusum", "temporal_profile"}):
            return duration >= pd.Timedelta(hours=4)
        if dets == {"cusum", "multivariate_pca"}:
            return (duration <= pd.Timedelta(hours=1)
                    and max(a.score for a in alerts) < 2.0)
        if dets == {"cusum", "multivariate_pca", "temporal_profile"}:
            return duration >= pd.Timedelta(hours=1)
        if dets == {"sub_pca"}:
            starts = [a.window_start or a.timestamp for a in alerts]
            ends = [a.window_end or a.timestamp for a in alerts]
            return (max(ends) - min(starts)) <= pd.Timedelta(hours=1)
        if dets == {"temporal_profile"}:
            return any(a.score >= 1.2 * a.threshold for a in alerts)
        return True


def group_alerts(alerts: list[Alert]) -> Alert:
    top = max(alerts, key=lambda a: a.score)
    w0 = min((a.window_start or a.timestamp) for a in alerts)
    w1 = max((a.window_end or a.timestamp) for a in alerts)
    names = "+".join(sorted({a.detector for a in alerts}))
    ctx: list[dict] = []
    for a in alerts:
        if a.context:
            ctx.extend(a.context)
    return Alert(top.sensor_id, top.capability, top.timestamp, names,
                 top.score, top.threshold, top.anomaly_type, top.raw_value,
                 top.state, w0, w1, ctx or None)


class DefaultAlertFuser:
    """Per-sensor alert fuser.

    Immediate alerts (state_transition, DQG non-dropout) pass through on ingest.
    Statistical alerts (and DQG `dropout`) buffer in a pending chain that
    flushes when: (1) gap to newest pending > `gap`, (2) chain span > `max_span`,
    or (3) `anchor_on_non_cusum` and a CUSUM alert arrives with no non-CUSUM
    alert within `gap`. On flush, if `corroboration.accepts` passes, emits one
    grouped alert via `group_alerts`.
    """
    def __init__(self, cfg: SensorConfig, *, gap: int, max_span: int,
                 anchor_on_non_cusum: bool,
                 corroboration: CorroborationRule):
        self.cfg = cfg
        self.gap = pd.Timedelta(seconds=gap)
        self.max_span = pd.Timedelta(seconds=max_span)
        self.anchor = anchor_on_non_cusum
        self.rule = corroboration
        self._pending: list[Alert] = []
        self._newest_ts: pd.Timestamp | None = None
        self._newest_non_cusum_ts: pd.Timestamp | None = None
        # Cross-chain wind-down filter on BURSTY sensors: count consecutive
        # {cusum, sub_pca} 2-det fused emissions since the last "richer" emission
        # (immediate alert, or a fused chain whose det-set isn't {cusum, sub_pca}).
        # The 3rd+ consecutive 2-det chain is dropped — without this, post-shift
        # absorption keeps CUSUM+SubPCA cycling indefinitely on BURSTY power
        # sensors after the anomaly ends (outlet_tv weekend_anomaly wind-down).
        self._consecutive_cs: int = 0
        # Last emission's detector-set on this sensor (immediate or fused). Used
        # by the post-mvpca wind-down-lead filter: a {cusum, sub_pca,
        # temporal_profile} 3-det BURSTY chain whose immediately preceding
        # emission contained mvpca is the wind-down lead chain — TPs that share
        # this 3-det signature have non-mvpca predecessors (they occur while
        # MvPCA hasn't yet fired for the active anomaly bout).
        self._last_emit_dets: frozenset[str] | None = None

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
            dets = {a.detector for a in self._pending}
            is_bursty = self.cfg.archetype == Archetype.BURSTY
            is_cs2 = is_bursty and dets == {"cusum", "sub_pca"}
            is_cstp3_post_mvpca = (
                is_bursty
                and dets == {"cusum", "sub_pca", "temporal_profile"}
                and self._last_emit_dets is not None
                and "multivariate_pca" in self._last_emit_dets
            )
            if is_cs2:
                self._consecutive_cs += 1
                if self._consecutive_cs <= 2:
                    emitted.append(group_alerts(self._pending))
                    self._last_emit_dets = frozenset(dets)
            elif is_cstp3_post_mvpca:
                pass  # Iter 015: wind-down lead chain — drop
            else:
                self._consecutive_cs = 0
                emitted.append(group_alerts(self._pending))
                self._last_emit_dets = frozenset(dets)
        self._pending = []
        self._newest_ts = None
        self._newest_non_cusum_ts = None
        return emitted

    def ingest(self, fresh: list[Alert]) -> list[Alert]:
        out: list[Alert] = []
        for a in fresh:
            if self._is_immediate(a):
                out.append(a)
                self._consecutive_cs = 0
                self._last_emit_dets = frozenset({a.detector})
                continue
            if self._pending:
                gap_exceeded = (self._newest_ts is not None
                                and a.timestamp - self._newest_ts > self.gap)
                span_exceeded = (a.timestamp - self._pending[0].timestamp) > self.max_span
                anchor_exceeded = (self.anchor
                                   and a.detector == "cusum"
                                   and self._newest_non_cusum_ts is not None
                                   and a.timestamp - self._newest_non_cusum_ts > self.gap)
                if gap_exceeded or span_exceeded or anchor_exceeded:
                    out.extend(self._flush())
            self._pending.append(a)
            if self._newest_ts is None or a.timestamp > self._newest_ts:
                self._newest_ts = a.timestamp
            if a.detector != "cusum":
                if (self._newest_non_cusum_ts is None
                        or a.timestamp > self._newest_non_cusum_ts):
                    self._newest_non_cusum_ts = a.timestamp
        return out

    def finalize(self) -> list[Alert]:
        return self._flush()
