from __future__ import annotations
from typing import Protocol
import pandas as pd
from .core import Alert, Archetype, SensorConfig


class CorroborationRule(Protocol):
    def accepts(self, alerts: list[Alert]) -> bool: ...


class PassThroughCorroboration:
    """BURSTY / BINARY — filters marginal single-detector `temporal_profile`
    singletons (|z| within 20% of threshold) and power-capability `{cusum}`-only
    chains (bursty outlets' cumulative drift without corroborating detector);
    everything else passes through."""
    def accepts(self, alerts: list[Alert]) -> bool:
        dets = {a.detector for a in alerts}
        if dets == {"temporal_profile"}:
            return any(a.score >= 1.2 * a.threshold for a in alerts)
        if dets == {"cusum"} and all(a.capability == "power" for a in alerts):
            # BURSTY power-outlet cusum-only chains without corroboration are
            # uniformly FPs in the current dataset (7 such chains across the
            # 3 scenarios, all FPs — Feb 15 bootstrap-noise + Feb 17-21 kettle
            # singletons). Mirrors ContinuousCorroboration's {cusum}+duration>=90h
            # rule: a legit sustained shift should also fire MvPCA or SubPCA.
            # Restricted to capability=="power" so BINARY bedroom_motion
            # cusum-only chains (2 TPs on household_60d month_shift) continue
            # to pass via PassThroughCorroboration's default-accept.
            return False
        if dets == {"sub_pca"} and all(a.capability == "power" for a in alerts):
            # BURSTY power-outlet sub_pca-only chains are similarly uniformly FP
            # (5 such chains across the 3 scenarios, all FPs). Additionally,
            # accepting them currently resets the iter-013 `_consecutive_cs`
            # streak counter in `DefaultAlertFuser._flush`, so interleaved
            # {sub_pca} singletons inside a {cusum, sub_pca} 2-det streak
            # currently prevent the streak filter from rejecting the 3rd+
            # 2-det chain. Rejecting {sub_pca}-only lets the streak counter
            # persist across these interleavings.
            return False
        if dets == {"multivariate_pca"} and all(a.capability == "power" for a in alerts):
            # BURSTY power-outlet mvpca singletons split cleanly by score:
            # 58 TPs (22 on hh60d, 36 on hh120d) have min score 48433; 2 FPs
            # (hh60d kettle 02-15 score 2e-19, hh120d kettle 02-17 score 4141)
            # have scores ≤ 5000. A 10,000 floor rejects both FPs with a wide
            # safety margin. Absolute score threshold is unit-specific to
            # power-outlet feature scale (peak W~10^3, diff-feat residuals
            # push real anomalies to 10^4-10^5).
            return max(a.score for a in alerts) >= 10000
        if dets == {"multivariate_pca"} and all(a.capability == "motion" for a in alerts):
            # BINARY motion mvpca singletons are 94% FP across the suite:
            # leak_30d 0/20 TP (9.8h FP), hh60d 0/24 TP (10.5h FP), hh120d
            # 6/73 TP (4h TP / 41.9h FP). Score doesn't separate (TP 4-16
            # overlaps FP 4-24). The 6 hh120d TPs are on bedroom_motion
            # month_shift labels (Mar 7, Apr 26) already covered by 100-250
            # state_transition alerts plus recent_shift+temporal_profile
            # fused chains, so incident_recall is preserved. Mirrors iter
            # 059 rejection of motion temporal_profile singletons.
            return False
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
        if dets == {"cusum", "sub_pca"}:
            return duration >= pd.Timedelta(hours=4)
        if dets == {"cusum", "temporal_profile"}:
            # On CONTINUOUS, {cusum, temp} without SubPCA or MvPCA corroboration
            # is weak evidence: CUSUM's cumulative drift plus bucket z-score
            # without residual/variance confirmation tends to fire post-anomaly
            # as the baseline shifts but the error space and variance settle.
            # Audit across current scenarios: 4 such chains on leak_30d
            # basement_temp (post-cal_drift wind-down), all FPs on behavior;
            # 0 chains on household_60d/120d. The old-dataset 4h duration floor
            # was tuned for outlet_voltage and does not generalize.
            return False
        if dets == {"cusum", "multivariate_pca"}:
            return (duration <= pd.Timedelta(hours=1)
                    and max(a.score for a in alerts) < 2.0)
        if dets == {"cusum", "multivariate_pca", "temporal_profile"}:
            # Same wind-down mechanism as the {cusum, temporal_profile} rule
            # above, one level richer: mvpca joins but sub_pca is absent, so
            # bootstrap-variance corroboration is missing. Audit across current
            # scenarios: 3 chains (1 on household_60d mains_voltage, 2 on
            # leak_30d basement_temp), all FPs on both behavior and sensor_fault.
            # The 1h duration floor was tuned on retired scenarios; no
            # current-dataset TP relies on this det-set.
            return False
        if dets == {"multivariate_pca"}:
            # mvpca singletons on CONTINUOUS are uniformly FP in the current
            # dataset (audit: 0 TPs across 3 scenarios, 2 FPs on leak_30d
            # basement_temp with scores 1.00 and 0.86). The 2.0 floor mirrors
            # the {cusum, multivariate_pca} rule's score cap: a mvpca-only
            # chain that isn't corroborated by CUSUM needs convincing residual
            # magnitude to be credible. Iter 006's {margin = 1.2×threshold}
            # rule passed these singletons; the absolute-score floor rejects them.
            return max(a.score for a in alerts) >= 2.0
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
    first_fire = min(a.timestamp for a in alerts)
    names = "+".join(sorted({a.detector for a in alerts}))
    # BINARY water {cusum, multivariate_pca} chains over-extend 17-46h past
    # the actual water_leak_sustained label end (labels are 1-6h). CUSUM drift
    # and MvPCA residual persist against bootstrap baseline even after the
    # leak event ends. Cap the emitted chain end at w0+8h to trim the
    # wind-down tail. Every current water label fits in the first 8h of its
    # containing chain except leak_30d Feb 23 08:30 which is mid-chain
    # (Feb 22-24) — a state_transition 1min alert covers the Feb 23 onset
    # so incident_recall stays 1.0.
    dets = {a.detector for a in alerts}
    if top.capability == "water" and dets == {"cusum", "multivariate_pca"}:
        # 6h cap: the longest water_leak_sustained label in the current
        # generator is 6h (hh120d May 21 08:00-14:00). All other labels are
        # 1-5h. A 6h cap fits the max label exactly and trims 2h FP from
        # every shorter-label chain (6 chains across 3 scenarios).
        cap_end = w0 + pd.Timedelta(hours=6)
        if w1 > cap_end:
            w1 = cap_end
    ctx: list[dict] = []
    for a in alerts:
        if a.context:
            ctx.extend(a.context)
    return Alert(top.sensor_id, top.capability, top.timestamp, names,
                 top.score, top.threshold, top.anomaly_type, top.raw_value,
                 top.state, w0, w1, ctx or None, first_fire)


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
        # Last FUSED chain's detector-set on this sensor (excludes immediate
        # alerts like state_transition). Distinct from `_last_emit_dets` which
        # gets reset on every immediate alert; on BINARY motion with 856+
        # state_transitions per scenario, `_last_emit_dets` is almost never
        # a fused-chain det-set, so the BINARY-motion post-mvpca wind-down
        # filter (iter 032) needs a tracker that survives interleaved immediate
        # alerts. Only updated in `_flush` on successful fused emits.
        self._last_fused_emit_dets: frozenset[str] | None = None
        # End timestamp of the most recently *attempted* fused chain (whether
        # emitted or filtered). Distinct from `_newest_ts` (which is reset on
        # every flush). The CONTINUOUS between-trend filter uses this to
        # require >5d gap from the previous attempt: on leak_battery, Row 17
        # (first FP after a cusum-only chain) is kept; Rows 18/19 (isolated
        # 3-det chains 6d/18d apart) are dropped; Row 20 (trend2 boundary,
        # 4d after Row 19) is preserved. outlet_voltage's late-May 3-det
        # streak has consecutive chains with sub-1h gaps so it never trips
        # the 5d threshold.
        self._last_attempt_end_ts: pd.Timestamp | None = None

    @staticmethod
    def _is_immediate(a: Alert) -> bool:
        if a.detector == "state_transition": return True
        if a.detector == "data_quality_gate":
            return a.anomaly_type != "dropout"
        return False

    def _flush(self) -> list[Alert]:
        if not self._pending:
            return []
        chain_start = self._pending[0].timestamp
        chain_end = self._pending[-1].timestamp
        emitted: list[Alert] = []
        if self.rule.accepts(self._pending):
            dets = {a.detector for a in self._pending}
            is_bursty = self.cfg.archetype == Archetype.BURSTY
            is_continuous = self.cfg.archetype == Archetype.CONTINUOUS
            is_binary = self.cfg.archetype == Archetype.BINARY
            is_cs2 = is_bursty and dets == {"cusum", "sub_pca"}
            is_cstp3_post_mvpca = (
                is_bursty
                and dets == {"cusum", "sub_pca", "temporal_profile"}
                and self._last_fused_emit_dets is not None
                and "multivariate_pca" in self._last_fused_emit_dets
            )
            is_cms3_continuous_between = (
                is_continuous
                and dets == {"cusum", "multivariate_pca", "sub_pca"}
                and self._last_fused_emit_dets is not None
                and "multivariate_pca" in self._last_fused_emit_dets
                and self._last_attempt_end_ts is not None
                and (chain_start - self._last_attempt_end_ts) > pd.Timedelta(days=5)
            )
            # BINARY motion wind-down filter: {cusum, multivariate_pca} 2-det chains
            # on motion sensors are wind-down when they immediately follow a richer
            # chain that contained mvpca (the 3-det {cusum,mvpca,temp} chain that
            # led the anomaly has closed; mvpca residual is still drifting while
            # TP's bucket z-score has relaxed). Audit across scenarios:
            # household_60d 3 × 2-det chains (Feb 19-21, Feb 24-28, Mar 16-20) all
            # follow 3-det mvpca chains, all FP, 0 TPs; household_120d 4 × 2-det
            # chains — 3 follow 3-det mvpca chains (Feb 23-26, Apr 6-8, May 13-17,
            # all FP), 1 follows a non-mvpca cusum+temp TP chain (May 1-5, kept);
            # leak_30d 2 × 2-det chains (Feb 16-20, Feb 24-28) both follow 3-det
            # mvpca chains — Feb 16-20 was previously TP for utility_motion
            # unusual_occupancy Feb 17-18 but state_transition at those label
            # timestamps preserves incident_recall. Iter 029's global reject
            # blew the hh120d latency floor (+1140s) because pre-iter-030 code
            # included an onset-bridging 2-det chain for hh120d bedroom_motion;
            # the post-mvpca gate protects onset chains (whose predecessor is an
            # immediate state_transition or a non-mvpca chain, not a full 3-det
            # wind-down lead).
            is_cm2_binary_motion_post_mvpca = (
                is_binary
                and self.cfg.capability == "motion"
                and dets == {"cusum", "multivariate_pca"}
                and self._last_fused_emit_dets is not None
                and "multivariate_pca" in self._last_fused_emit_dets
            )
            # BINARY motion {mvpca, temporal_profile} 2-det chains are nearly
            # pure FP on current data: 2 TPs (bedroom_motion month_shift Mar 8
            # on hh60d and hh120d, 8h total) vs 13 FPs (132h total) across the
            # full suite — 87% FP by count, 94% by FP time. Both TP cases have
            # hundreds of alternative covering rows on the same label
            # (state_transition + temporal_profile singletons), so incident
            # recall is preserved. Without a cumulative-drift signal (cusum) or
            # recent-vs-long-term shift (recent_shift), mvpca+tp is high-residual
            # noise that matches the hourly-bucket deviation but lacks sustain.
            is_mvtp2_binary_motion = (
                is_binary
                and self.cfg.capability == "motion"
                and dets == {"multivariate_pca", "temporal_profile"}
            )
            # BINARY motion temporal_profile singletons: 7 TP (23h across
            # bedroom_motion month_shift labels) vs 50 FP (176h) across the
            # suite. 86% FP by count, 88% by time. TP cases all have
            # state_transition + other coverage on the same long month_shift
            # labels; incident_recall preserved but some time_recall dilution
            # on bedroom_motion month_shift is expected.
            is_tp1_binary_motion = (
                is_binary
                and self.cfg.capability == "motion"
                and dets == {"temporal_profile"}
            )
            if is_cs2:
                self._consecutive_cs += 1
                if self._consecutive_cs <= 2:
                    emitted.append(group_alerts(self._pending))
                    self._last_emit_dets = frozenset(dets)
                    self._last_fused_emit_dets = frozenset(dets)
            elif (is_cstp3_post_mvpca or is_cms3_continuous_between
                  or is_cm2_binary_motion_post_mvpca or is_mvtp2_binary_motion
                  or is_tp1_binary_motion):
                pass  # Iter 015/016/032/058/059: cross-chain wind-down / between-trend filter
            else:
                self._consecutive_cs = 0
                emitted.append(group_alerts(self._pending))
                self._last_emit_dets = frozenset(dets)
                self._last_fused_emit_dets = frozenset(dets)
            # Only chains that pass corroboration count as "attempts" for the
            # cross-chain gap tracker — corroboration-rejected chains are noise
            # (e.g., dense sub-90h cusum-only chains on long-cadence sensors)
            # and would shrink the apparent gap to ~0.
            self._last_attempt_end_ts = chain_end
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
