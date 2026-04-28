from __future__ import annotations
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
import argparse, sys
import pandas as pd
import yaml
from .core import Event, Alert, Archetype, SensorConfig
from .adapter import make_adapter, Adapter
from .features import FeatureEngineer
from .fusion import DefaultAlertFuser
from .profiles import profile_for
from .metrics import compute_metrics, compute_stratified
from .explain import classify_type, type_to_class


_ADAPT_BUFFER_TICKS_DEFAULT = 96 * 60  # 96h buffer for CONTINUOUS — a longer buffer
# on CONT (mains_voltage month_shift) absorbs mid-anomaly regime and delays subsequent
# label onset detection (tested at 120h global: +4683s hh120d nondqg_lat_p95, blows
# +600s floor). Per-archetype gate keeps CONT safe.
_ADAPT_BUFFER_TICKS_BY_ARCHETYPE = {
    Archetype.CONTINUOUS: 96 * 60,   # keep latency safety for long sustained CONT anomalies
    Archetype.BURSTY:     144 * 60,  # iter 037: sweet spot for outlet wind-down absorption
    Archetype.BINARY:     144 * 60,  # same; BINARY short-label latency is state_transition's job
}


@dataclass
class _SensorState:
    cfg: SensorConfig
    adapter: Adapter
    engineer: FeatureEngineer
    short_event: list                   # pre-adapter EventDetectors (DQG)
    short_tick: list                    # post-adapter immediate triggers (StateTransition or [])
    medium: list                        # sliding-window Detectors (RecentShift / DCS-6h / RMP)
    long_tick: list                     # reserved (currently empty)
    fuser: DefaultAlertFuser
    bootstrap_raw: list = field(default_factory=list)   # (tick, adapter_features)
    bootstrap_rows: list = field(default_factory=list)  # (tick, enriched)
    start_ts: pd.Timestamp | None = None
    fit_done: bool = False
    recent_rows: deque = field(default_factory=deque)  # size set in Pipeline.__init__ per-archetype
    consecutive_max_span: int = 0        # cross-chain streak counter for G1 adapt

    def tick_detectors(self) -> list:
        """All post-adapter detectors in emit order (short_tick -> medium -> long_tick)."""
        return self.short_tick + self.medium + self.long_tick


class Pipeline:
    def __init__(self, configs: list[SensorConfig], bootstrap_days: float = 14.0):
        self.bootstrap_days = bootstrap_days
        self._states: dict[tuple[str, str], _SensorState] = {}
        for cfg in configs:
            p = profile_for(cfg)
            buffer_ticks = _ADAPT_BUFFER_TICKS_BY_ARCHETYPE.get(
                cfg.archetype, _ADAPT_BUFFER_TICKS_DEFAULT)
            self._states[cfg.key] = _SensorState(
                cfg=cfg,
                adapter=make_adapter(cfg),
                engineer=FeatureEngineer(cfg),
                short_event=[f(cfg) for f in p.short_event],
                short_tick=[f(cfg) for f in p.short_tick],
                medium=[f(cfg) for f in p.medium],
                long_tick=[f(cfg) for f in p.long_tick],
                fuser=p.long_fuser(cfg),
                recent_rows=deque(maxlen=buffer_ticks),
            )

    def is_live(self, key) -> bool:
        st = self._states.get(key)
        return bool(st and st.fit_done and any(d.live for d in st.tick_detectors()))

    def _maybe_fit(self, st: _SensorState, now: pd.Timestamp) -> None:
        if st.fit_done or st.start_ts is None: return
        if (now - st.start_ts).total_seconds() < self.bootstrap_days * 86400: return
        # Bursty: fit state model from adapter's accumulated values.
        if st.cfg.archetype == Archetype.BURSTY:
            st.adapter.fit_state_model()
        # Enrich bootstrap rows, relabeling state where applicable; the engineer
        # ends this loop warmed with the correct per-state rolling history.
        # For BURSTY, also recompute time_in_state from the now-fit state sequence —
        # during bootstrap, the adapter emitted with state=0 fixed (no state model yet)
        # which made time_in_state grow monotonically across the full 14 days, giving
        # detectors a wildly off-distribution feature vs post-bootstrap values.
        is_bursty = st.cfg.archetype == Archetype.BURSTY
        prev_state: int | None = None
        state_entered: pd.Timestamp | None = None
        for ts, f in st.bootstrap_raw:
            g = st.adapter.relabel(dict(f))
            if is_bursty:
                s = int(g.get("state", 0))
                if prev_state is None or s != prev_state:
                    prev_state = s
                    state_entered = ts
                g["time_in_state"] = (ts - state_entered).total_seconds()
            st.bootstrap_rows.append((ts, st.engineer.enrich(ts, g)))
        for d in st.tick_detectors():
            d.fit(st.bootstrap_rows)
        st.fit_done = True

    def ingest(self, ev: Event) -> list[Alert]:
        st = self._states.get((ev.sensor_id, ev.capability))
        if st is None: return []
        if st.start_ts is None: st.start_ts = ev.timestamp
        alerts: list[Alert] = []
        # SHORT band — pre-adapter event checks (always, independent of bootstrap).
        for d in st.short_event:
            alerts.extend(d.check(ev))
        # Adapter band — normalize to uniform ticks.
        st.adapter.ingest(ev)
        for tick, feat in st.adapter.emit_ready(ev.timestamp):
            if not st.fit_done:
                st.bootstrap_raw.append((tick, dict(feat)))
                continue
            enriched = st.engineer.enrich(tick, feat)
            st.recent_rows.append((tick, enriched))
            # SHORT tick -> MEDIUM -> LONG tick (emit order preserved).
            for d in st.tick_detectors():
                alerts.extend(d.update(tick, enriched))
        self._maybe_fit(st, ev.timestamp)
        # LONG fuser — chain-level aggregation + corroboration.
        emitted = st.fuser.ingest(alerts)
        # Coordinated adaptation on consecutive max_span flushes. A single
        # max_span chain (~96h) is ambiguous — could be the legit start of a
        # multi-day anomaly OR a wind-down tail. Three consecutive max_span
        # flushes (~12d of continuous firing) is a strong wind-down signal:
        # by 12d, any active anomaly that triggered chain 1 has had its
        # onset captured (incident_recall preserved), the 1st post-onset
        # chain has had time to fire without adaptation (time_recall
        # preserved on sustained anomalies), and continued firing past
        # that is the post-shift baseline being treated as new normal.
        # Adapting once at the third flush absorbs the recent rolling
        # window into each detector's mu/centroid; subsequent ticks see
        # small deviations and the chain stops re-forming. Counter resets
        # on any non-max-span emit (chain ended naturally → not wind-down)
        # and after each adapt (require fresh streak before next adapt).
        # K=3 chosen over K=2 (iter 028) to preserve more month_shift
        # tail coverage and reduce voltage month_shift latency pressure.
        span_threshold = 0.9 * st.fuser.max_span
        for em in emitted:
            if em.window_start is None or em.window_end is None:
                continue
            if (em.window_end - em.window_start) >= span_threshold:
                st.consecutive_max_span += 1
            else:
                st.consecutive_max_span = 0
            if st.consecutive_max_span >= 3:
                rows = list(st.recent_rows)
                for d in st.medium + st.long_tick:
                    if hasattr(d, "adapt_to_recent"):
                        d.adapt_to_recent(rows)
                st.consecutive_max_span = 0
        return emitted

    def finalize(self) -> list[Alert]:
        out = []
        for st in self._states.values():
            out.extend(st.fuser.finalize())
        return out


# --- CLI ---

def _load_configs(path: Path) -> list[SensorConfig]:
    doc = yaml.safe_load(Path(path).read_text())
    out = []
    for s in doc["sensors"]:
        out.append(SensorConfig(
            sensor_id=s["id"], capability=s["capability"],
            archetype=Archetype(s["archetype"]),
            expected_interval_sec=float(s["expected_interval_sec"]),
            min_value=s.get("min_value"), max_value=s.get("max_value"),
            cumulative=bool(s.get("cumulative", False)),
            heartbeat_sec=s.get("heartbeat_sec"),
            granularity_sec=int(s.get("granularity_sec", 60)),
            deterministic_trigger=bool(s.get("deterministic_trigger", False)),
        ))
    return out


def run(events_csv: Path, config_yaml: Path, out_csv: Path, bootstrap_days: float) -> None:
    configs = _load_configs(config_yaml)
    p = Pipeline(configs, bootstrap_days=bootstrap_days)
    df = pd.read_csv(events_csv)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True, format="ISO8601")
    df = df.sort_values("timestamp").reset_index(drop=True)
    all_alerts: list[Alert] = []
    for row in df.itertuples(index=False):
        all_alerts.extend(p.ingest(Event(row.timestamp, row.sensor_id, row.capability,
                                          float(row.value), getattr(row, "unit", "") or "")))
    all_alerts.extend(p.finalize())
    _write_detections(all_alerts, out_csv)
    print(f"wrote {len(all_alerts)} detections to {out_csv}")


def _write_detections(alerts: list[Alert], path: Path) -> None:
    # Pre-pass: flag DQG out_of_range fires that recur on the same sensor
    # within a 6h sliding window. Sustained-OOR is the level-shift
    # signature on power-capability sensors — synth-gen's
    # ``level_shift offset=-N`` drives the off-state below the configured
    # min, producing OOR every cooldown for the label duration. Iter 1
    # gated this on a behavior-detector co-fire (within ±12h) as a
    # defensive guard against post-label OOR drift, but the synth-gen
    # bound (94ab893) made offsets stop at the label end, so the guard is
    # no longer needed and was costing ~700 misclassified fires across
    # the suite (TV/kettle level_shift labels with no DCS co-fire).
    SUSTAINED_OOR_WINDOW = pd.Timedelta(hours=6)
    SUSTAINED_OOR_COUNT = 3
    # Iter 4: cross-chain DCS hour-spread → level_shift override.
    # A long-running level_shift on an always-on power appliance (e.g.,
    # +150W offset on the kettle) doesn't push it below the OOR floor
    # (so the sustained-OOR override doesn't fire), but it does drive
    # DCS to fire roughly every cooldown across the label window. The
    # cooldown is decoupled from 24h, so successive fires drift through
    # all hours of the day — and the per-chain classifier sees each as
    # a short calendar pattern (time_of_day / weekend_anomaly). True
    # calendar anomalies cluster DCS fires at a tight band of hours
    # (kettle 10-12 time_of_day produces chains all near hour 10-12).
    # Two conditions separate them in a 14d window:
    #   - DISTINCT_HOURS ≥ 4: the firing positions span the day.
    #   - MAX_HOUR_PCT  < 0.35: no single hour dominates (else it's
    #     a concentrated calendar pattern with noise on the side).
    # Iter 8: lowered from 5 → 4. The dense_90d 30d kettle level_shift
    # produces 8 chains drifting through hours every 4d, so the FIRST
    # two chains only see 4 prior chains in the symmetric 14d window
    # — threshold 5 missed them and they fell through to time_of_day.
    # Concentration ceiling (0.35) blocks holdout's multi-anomaly
    # contamination case at the lower threshold (concentration there
    # is 0.44 → still gated).
    SUSTAINED_DCS_WINDOW = pd.Timedelta(days=14)
    SUSTAINED_DCS_DISTINCT_HOURS = 4
    SUSTAINED_DCS_MAX_HOUR_PCT = 0.35
    # Iter 10: post-label return-transient suppression. After a sustained
    # DCS run ends (level_shift / time_of_day label expires), synth-gen
    # snaps the offset back to baseline at the label boundary. The DCS
    # detector sees that step as a duty-cycle shift in the OPPOSITE
    # direction and emits a short reversal chain just past the label —
    # which has no GT label and counts as a user_visible FP. The fuser's
    # 4h gap absorbs reversals within 4h, so anything we can suppress here
    # sits in the 4h-24h range. Sustained-prev gate (≥3 same-direction
    # chains, prev included) keeps the rule from firing on incidental
    # back-to-back reversals; the 24h gap caps it to immediately-after
    # transients so genuine multi-day behavior reversals (≥1d apart)
    # are unaffected.
    RETURN_TRANSIENT_GAP = pd.Timedelta(hours=72)
    RETURN_TRANSIENT_PRIOR_COUNT = 3
    # Iter 14: recent_shift on CONTINUOUS sensors (mains_voltage,
    # basement_temp) fires post-label recovery chains differently from
    # DCS — instead of multiple short chains it produces ONE huge chain
    # with thousands of fire-ticks (continuous tick-level firing as the
    # rolling baseline slowly adapts). The iter 11 "≥2 prior chains"
    # sustained-run gate can't recognise this because the in-label firing
    # is a single chain with no priors. Add a size-based disjunct:
    # prev_n_ticks ≥ 100 is also "sustained." Detected on hh120d's
    # post-calibration_drift Mar 21-27 window where 5 monster chains
    # contributed 96.8% of all wholly-FP behavior ticks (6869 of 7093).
    # MIN_GAP = 1h on the recent_shift rule prevents the metric quirk
    # where the detector's 1h analysis-window back-pads first_fire's
    # window_start into the prior label, causing a metric-TP overlap
    # the eval would credit (saw on holdout Feb 22 00:39, gap 49min).
    RECENT_SHIFT_MIN_GAP = pd.Timedelta(hours=1)
    RECENT_SHIFT_PREV_TICK_THRESHOLD = 100
    # Iter 15: extend iter 14's cascade walk to SKIP past same-direction
    # chains instead of breaking on them. Iter 14 catches the post-
    # recovery transient when the immediate next chain after a sustained
    # head is opposite-direction (hh120d's Mar 19 "+" head followed by
    # Mar 21 "-" recovery, gap 61h). But synth-gen's calibration_drift
    # bias is applied gradually, so the in-label firing on holdout
    # (12 small "+" chains over 2 days during a 0.8V drift) precedes the
    # actual "-" recovery cascade. Iter 14 breaks at the first "+"
    # continuation chain and never reaches the "-" recovery — leaving
    # 13 mv user_visible FPs on holdout.
    #
    # Mechanism: when walking opposite-direction recovery from a
    # sustained head, treat same-direction chains as transparent
    # fillers — skip without breaking and without updating the anchor.
    # The 72h gap is still measured from the LAST opposite-direction
    # chain's lf (or the head's lf if none seen yet), so an unrelated
    # event much later (gap >72h via the anchor) still ends the
    # cascade. This preserves the iter 14 invariant that protects
    # hh120d's mixed-direction month_shift label firing (chain 8 "-"
    # head's anchor stays at Apr 21 00:22; chain 24 "+" at May 1 has
    # gap 240h > 72h → break, TPs preserved).
    #
    # Applies uniformly across all recent_shift detectors — the
    # extension still requires an OPPOSITE-direction recovery chain
    # to suppress anything; only the path to find that chain is
    # widened. Verified safe on basement_temp dip clusters in leak_30d
    # (no direction-mixed sustained heads followed by opposite-dir
    # recovery pattern).
    _DCS_DETECTORS = frozenset({
        "duty_cycle_shift_1h", "duty_cycle_shift_3h",
        "duty_cycle_shift_6h", "duty_cycle_shift_12h",
    })
    _RECENT_SHIFT_DETECTORS = frozenset({"recent_shift"})
    _RMP_DETECTORS = frozenset({"rolling_median_peak_shift"})
    # Iter 18: opposite-direction RMP cascade walk. RMP detector's
    # adapt mechanism re-fits boot_median upward during a sustained
    # in-label "+" run; once the label ends and value reverts to
    # natural baseline, roll_median falls below the (now elevated)
    # boot_median → RMP fires "-" direction for several hours. That's
    # the post-recovery cascade we want to suppress. Mirrors
    # iter 14/15/16 (opposite-dir + iter 15 same-dir skip).
    #
    # Two extra gates vs iter 16 to keep this safe:
    #   1. RMP_CASCADE_GAP = 72h (matches iter 11's RETURN_TRANSIENT_GAP)
    #   2. RMP_CASCADE_PRIOR_GAP = 24h: head qualifies only if its
    #      LATEST same-direction prior is within 24h. This protects
    #      hh60d fridge: a "loose" head with priors 50h+ apart is
    #      sporadic post-label noise, NOT a sustained trend cluster;
    #      its forward walk would otherwise reach the next label's
    #      in-window TP fires.
    # Solo RMP chains only (combo chains route through different
    # classifiers and aren't the post-trend-cluster FP target).
    RMP_CASCADE_GAP = pd.Timedelta(hours=72)
    RMP_CASCADE_PRIOR_GAP = pd.Timedelta(hours=24)

    def _dcs_direction(a: Alert) -> str | None:
        """Extract +/- from any DCS context dict on the alert."""
        if not a.context:
            return None
        for ctx in a.context:
            d = ctx.get("direction")
            if d in ("+", "-"):
                return d
            if d == "high":
                return "+"
            if d == "low":
                return "-"
        return None

    def _rs_direction(a: Alert) -> str | None:
        """Extract +/- for recent_shift chains. Uses explicit `direction`
        if present, else derives from short_value vs baseline_value."""
        if not a.context:
            return None
        for ctx in a.context:
            d = ctx.get("direction")
            if d in ("+", "-"):
                return d
            sv = ctx.get("short_value")
            bv = ctx.get("baseline_value")
            if sv is not None and bv is not None:
                return "+" if sv > bv else "-"
        return None

    def _rmp_direction(a: Alert) -> str | None:
        """RMP detector emits direction='high'/'low' on the alert
        context (z > 0 vs z < 0 against bootstrap median). Map to +/-."""
        if not a.context:
            return None
        for ctx in a.context:
            d = ctx.get("direction")
            if d in ("+", "-"):
                return d
            if d == "high":
                return "+"
            if d == "low":
                return "-"
        return None

    oor_ts_by_sensor: dict[str, list[pd.Timestamp]] = {}
    dcs_ts_by_sensor: dict[str, list[pd.Timestamp]] = {}
    # (first_fire, last_fire, direction) per DCS chain — needed by iter 10
    # return-transient gate. Kept alongside the timestamp-only index above
    # so iter 4/8/9 helpers that only need the hour distribution stay
    # untouched.
    dcs_chains_by_sensor: dict[
        str, list[tuple[pd.Timestamp, pd.Timestamp, str | None]]
    ] = {}
    # Iter 14: recent_shift chains tracked separately with `n_ticks` so
    # the size-based sustained disjunct can recognise mono-chain
    # in-label firing patterns. RMP intentionally excluded (iter 12d
    # showed RMP suppression hurts hh60d via in-label off-pattern noise
    # chains the metric counts as TPs).
    rs_chains_by_sensor: dict[
        str, list[tuple[pd.Timestamp, pd.Timestamp, str | None, int]]
    ] = {}
    # Iter 18: solo-RMP chains only (combo chains like DCS+RMP route
    # through different classifiers and are not the post-trend-cluster
    # FP target).
    rmp_chains_by_sensor: dict[
        str, list[tuple[pd.Timestamp, pd.Timestamp, str | None]]
    ] = {}
    for a in alerts:
        detectors = set((a.detector or "").split("+"))
        if (a.anomaly_type == "out_of_range"
                and a.capability == "power"
                and "data_quality_gate" in detectors):
            oor_ts_by_sensor.setdefault(a.sensor_id, []).append(a.timestamp)
        if detectors & _DCS_DETECTORS:
            # Iter 8: index DCS chains by first_fire_ts (earliest tick
            # in the chain). a.timestamp uses the LAST tick of the
            # fused chain, which for DCS_6h means all chains land
            # ~6h after their start — so two chains starting at hours
            # 0 and 2 both end at hours 6 and 8. The last-tick hour
            # collapses the natural cooldown drift, hurting the
            # distinct-hour count. first_fire_ts preserves the
            # actual chain-start drift.
            ff = a.first_fire_ts or a.timestamp
            dcs_ts_by_sensor.setdefault(a.sensor_id, []).append(ff)
            dcs_chains_by_sensor.setdefault(a.sensor_id, []).append(
                (ff, a.timestamp, _dcs_direction(a)))
        if detectors & _RECENT_SHIFT_DETECTORS:
            ff = a.first_fire_ts or a.timestamp
            n_ticks = len(a.fire_ticks) if a.fire_ticks else 1
            rs_chains_by_sensor.setdefault(a.sensor_id, []).append(
                (ff, a.timestamp, _rs_direction(a), n_ticks))
        if detectors == _RMP_DETECTORS:
            ff = a.first_fire_ts or a.timestamp
            rmp_chains_by_sensor.setdefault(a.sensor_id, []).append(
                (ff, a.timestamp, _rmp_direction(a)))
    for v in oor_ts_by_sensor.values():
        v.sort()
    for v in dcs_ts_by_sensor.values():
        v.sort()
    for v in dcs_chains_by_sensor.values():
        v.sort(key=lambda t: t[0])
    for v in rs_chains_by_sensor.values():
        v.sort(key=lambda t: t[0])
    for v in rmp_chains_by_sensor.values():
        v.sort(key=lambda t: t[0])
    import bisect
    def _is_sustained_oor(a: Alert) -> bool:
        sid = a.sensor_id
        ts_list = oor_ts_by_sensor.get(sid)
        if not ts_list:
            return False
        ts = a.timestamp
        lo = ts - SUSTAINED_OOR_WINDOW
        hi = ts + SUSTAINED_OOR_WINDOW
        l = bisect.bisect_left(ts_list, lo)
        r = bisect.bisect_right(ts_list, hi)
        return (r - l) >= SUSTAINED_OOR_COUNT
    def _is_sustained_dcs(a: Alert) -> bool:
        sid = a.sensor_id
        ts_list = dcs_ts_by_sensor.get(sid)
        if not ts_list:
            return False
        ts = a.first_fire_ts or a.timestamp
        lo = ts - SUSTAINED_DCS_WINDOW
        hi = ts + SUSTAINED_DCS_WINDOW
        l = bisect.bisect_left(ts_list, lo)
        r = bisect.bisect_right(ts_list, hi)
        n = r - l
        if n < SUSTAINED_DCS_DISTINCT_HOURS:
            return False
        hour_counts: dict[int, int] = {}
        for i in range(l, r):
            h = ts_list[i].hour
            hour_counts[h] = hour_counts.get(h, 0) + 1
        if len(hour_counts) < SUSTAINED_DCS_DISTINCT_HOURS:
            return False
        return max(hour_counts.values()) / n < SUSTAINED_DCS_MAX_HOUR_PCT

    def _is_return_transient(a: Alert) -> bool:
        # Iter 10: a DCS chain whose direction reverses the immediately
        # preceding chain on the same sensor — within 24h of that prior
        # chain ending — and where the prior chain was part of a sustained
        # run (≥3 same-direction chains in its 14d window, itself
        # included). Pattern signature: synth-gen snaps the level_shift
        # offset off at label end, and the duty cycle steps back to
        # baseline. The detector correctly fires, but no GT label covers
        # the boundary, so it's a user_visible FP.
        detectors = set((a.detector or "").split("+"))
        if not (detectors & _DCS_DETECTORS):
            return False
        sid = a.sensor_id
        chains = dcs_chains_by_sensor.get(sid, [])
        if len(chains) < 2:
            return False
        cur_ff = a.first_fire_ts or a.timestamp
        cur_dir = _dcs_direction(a)
        if cur_dir is None:
            return False
        prev = None
        for ch in chains:
            if ch[0] >= cur_ff:
                break
            prev = ch
        if prev is None:
            return False
        prev_ff, prev_lf, prev_dir = prev
        if prev_dir is None or prev_dir == cur_dir:
            return False
        gap = cur_ff - prev_lf
        if gap < pd.Timedelta(0) or gap > RETURN_TRANSIENT_GAP:
            return False
        prior_lo = prev_ff - SUSTAINED_DCS_WINDOW
        same_dir_priors = sum(
            1 for ch in chains
            if prior_lo <= ch[0] < prev_ff and ch[2] == prev_dir
        )
        return same_dir_priors >= (RETURN_TRANSIENT_PRIOR_COUNT - 1)

    # Iter 14: pre-compute the recent_shift recovery cascade. After a
    # sustained recent_shift chain (≥100 ticks) ends, all subsequent
    # opposite-direction chains within RETURN_TRANSIENT_GAP (72h) of
    # the cascade's last fire are post-recovery noise. The cascade
    # extends with each suppression: chain N's last_fire becomes the
    # new anchor for chain N+1's gap check. Breaks when:
    #   - gap > 72h (recovery has run its course)
    #   - direction switches back (a real new anomaly)
    rs_suppressed_keys: set[tuple[str, pd.Timestamp]] = set()
    for sid, chains in rs_chains_by_sensor.items():
        for i, ch in enumerate(chains):
            prev_ff, prev_lf, prev_dir, prev_n_ticks = ch
            if prev_dir is None:
                continue
            if prev_n_ticks < RECENT_SHIFT_PREV_TICK_THRESHOLD:
                continue
            opp_dir = "-" if prev_dir == "+" else "+"
            anchor_lf = prev_lf
            for j in range(i + 1, len(chains)):
                ff_j, lf_j, dir_j, _ = chains[j]
                # Iter 15: skip same-direction (and unknown-direction)
                # chains without breaking — anchor stays put so the gap
                # check below is still measured from the last
                # opposite-direction chain (or head's lf). Lets the
                # cascade find an opposite-direction recovery cluster
                # that's separated from the head by in-label same-dir
                # continuation chains.
                if dir_j != opp_dir:
                    continue
                gap = ff_j - anchor_lf
                if gap < RECENT_SHIFT_MIN_GAP:
                    continue
                if gap > RETURN_TRANSIENT_GAP:
                    break
                rs_suppressed_keys.add((sid, ff_j))
                anchor_lf = lf_j

    def _is_rs_return_transient(a: Alert) -> bool:
        # Iter 14 / 15: the cascade walk built `rs_suppressed_keys`
        # above; this hook is a membership check. Iter 15 widened the
        # walk to skip past same-direction continuation chains, so a
        # head's opposite-direction recovery cascade is reachable even
        # when the head is followed by in-label same-direction firing
        # before the recovery starts (the holdout / hh60d cal_drift
        # pattern).
        detectors = set((a.detector or "").split("+"))
        if not (detectors & _RECENT_SHIFT_DETECTORS):
            return False
        cur_ff = a.first_fire_ts or a.timestamp
        return (a.sensor_id, cur_ff) in rs_suppressed_keys

    # Iter 16: parallel cascade-walk for DCS chains. Iter 11
    # (`_is_return_transient`) catches only the FIRST reversal after a
    # sustained DCS run — subsequent chains slip through because their
    # immediate prev is the just-suppressed reversal (now same-direction
    # as cur), so the per-chain gate fails. This pre-pass mirrors iter
    # 14 / 15: from each sustained head (≥3 same-direction chains in
    # 14d, == iter 11 priors gate), walk forward and suppress every
    # opposite-direction chain within RETURN_TRANSIENT_GAP (72h) of the
    # running anchor; the anchor extends per suppression. Iter 15-style
    # skip-same-dir keeps the cascade reachable past in-label
    # same-direction continuations.
    #
    # Same gate as iter 11 (RETURN_TRANSIENT_PRIOR_COUNT) so chains iter
    # 11 wouldn't have called sustained heads aren't promoted. The two
    # mechanisms are complementary: iter 11 catches the first reversal
    # via per-chain check; iter 16 catches the rest via cascade.
    dcs_cascade_suppressed_keys: set[tuple[str, pd.Timestamp]] = set()
    for sid, chains in dcs_chains_by_sensor.items():
        for i, ch in enumerate(chains):
            prev_ff, prev_lf, prev_dir = ch
            if prev_dir is None:
                continue
            prior_lo = prev_ff - SUSTAINED_DCS_WINDOW
            same_dir_priors = sum(
                1 for c in chains
                if prior_lo <= c[0] < prev_ff and c[2] == prev_dir
            )
            if same_dir_priors < (RETURN_TRANSIENT_PRIOR_COUNT - 1):
                continue
            opp_dir = "-" if prev_dir == "+" else "+"
            anchor_lf = prev_lf
            for j in range(i + 1, len(chains)):
                ff_j, lf_j, dir_j = chains[j]
                if dir_j != opp_dir:
                    continue
                gap = ff_j - anchor_lf
                if gap < pd.Timedelta(0):
                    continue
                if gap > RETURN_TRANSIENT_GAP:
                    break
                dcs_cascade_suppressed_keys.add((sid, ff_j))
                anchor_lf = lf_j

    def _is_dcs_cascade_suppressed(a: Alert) -> bool:
        # Iter 16: membership check against the pre-computed cascade
        # suppression set built above. Sustained head + cascade walk
        # generalises iter 11 from "first reversal only" to "all
        # opposite-direction recovery chains within 72h of the running
        # anchor."
        detectors = set((a.detector or "").split("+"))
        if not (detectors & _DCS_DETECTORS):
            return False
        cur_ff = a.first_fire_ts or a.timestamp
        return (a.sensor_id, cur_ff) in dcs_cascade_suppressed_keys

    # Iter 18: solo-RMP opposite-direction cascade walk. After a
    # sustained head (≥3 same-direction solo RMP chains in 14d, latest
    # prior within 24h of head — a TIGHT cluster), suppress every
    # opposite-direction solo RMP chain within 72h of the running
    # anchor. Anchor extends per suppression. Iter 15-style skip-same
    # for in-label same-direction continuations between head and the
    # opp-direction recovery cluster.
    rmp_cascade_suppressed_keys: set[tuple[str, pd.Timestamp]] = set()
    for sid, chains in rmp_chains_by_sensor.items():
        for i, ch in enumerate(chains):
            prev_ff, prev_lf, prev_dir = ch
            if prev_dir is None:
                continue
            prior_lo = prev_ff - SUSTAINED_DCS_WINDOW
            same_dir_priors = [c for c in chains
                               if prior_lo <= c[0] < prev_ff and c[2] == prev_dir]
            if len(same_dir_priors) < (RETURN_TRANSIENT_PRIOR_COUNT - 1):
                continue
            # Tightness gate: latest same-direction prior must be
            # within 24h of head. Distinguishes a true sustained run
            # (priors clustered near head) from sporadic post-label
            # noise (priors spread over multiple days).
            latest_prior_ff = max(c[0] for c in same_dir_priors)
            if (prev_ff - latest_prior_ff) > RMP_CASCADE_PRIOR_GAP:
                continue
            opp_dir = "-" if prev_dir == "+" else "+"
            anchor_lf = prev_lf
            for j in range(i + 1, len(chains)):
                ff_j, lf_j, dir_j = chains[j]
                # Iter 15-style: skip same-direction (and unknown)
                # without breaking — anchor stays put.
                if dir_j != opp_dir:
                    continue
                gap = ff_j - anchor_lf
                if gap < pd.Timedelta(0):
                    continue
                if gap > RMP_CASCADE_GAP:
                    break
                rmp_cascade_suppressed_keys.add((sid, ff_j))
                anchor_lf = lf_j

    def _is_rmp_cascade_suppressed(a: Alert) -> bool:
        # Iter 18: membership check. Only solo RMP (single-detector
        # rolling_median_peak_shift chain) is in the cascade index.
        detectors = set((a.detector or "").split("+"))
        if detectors != _RMP_DETECTORS:
            return False
        cur_ff = a.first_fire_ts or a.timestamp
        return (a.sensor_id, cur_ff) in rmp_cascade_suppressed_keys

    def _is_time_of_day_pattern(a: Alert) -> bool:
        # Iter 9: chain hour-of-day appears on BOTH weekdays and
        # weekends in the 14d window — that's a daily calendar
        # pattern (kettle 10-12 daily) which fires DCS every day at
        # the same hour. The chain itself might be a weekend day
        # within a multi-week label, so the per-chain
        # `is_weekend` check would route to weekend_anomaly. The
        # cross-day hour-of-day signature corrects that to
        # time_of_day.
        sid = a.sensor_id
        ts_list = dcs_ts_by_sensor.get(sid)
        if not ts_list:
            return False
        ts = a.first_fire_ts or a.timestamp
        target_hour = ts.hour
        lo = ts - SUSTAINED_DCS_WINDOW
        hi = ts + SUSTAINED_DCS_WINDOW
        l = bisect.bisect_left(ts_list, lo)
        r = bisect.bisect_right(ts_list, hi)
        weekday_count = 0
        weekend_count = 0
        for i in range(l, r):
            t = ts_list[i]
            # ±1h band to absorb cooldown jitter on the same daily peak
            if abs(t.hour - target_hour) > 1:
                # also handle 23 ↔ 0 wrap
                if not (target_hour == 0 and t.hour == 23) and \
                   not (target_hour == 23 and t.hour == 0):
                    continue
            if t.dayofweek >= 5:
                weekend_count += 1
            else:
                weekday_count += 1
        return weekday_count >= 2 and weekend_count >= 1

    rows = []
    for a in alerts:
        # Iter 10/14/16: skip post-label return-transient chains entirely.
        # iter 11 (`_is_return_transient`) catches the first reversal of
        # a sustained DCS head; iter 14/15 (`_is_rs_return_transient`)
        # the recent_shift cascade; iter 16 the rest of the DCS cascade.
        if (_is_return_transient(a)
                or _is_rs_return_transient(a)
                or _is_dcs_cascade_suppressed(a)
                or _is_rmp_cascade_suppressed(a)):
            continue
        start = a.window_start or a.timestamp
        end = a.window_end or (a.timestamp + pd.Timedelta(minutes=1))
        # first_fire_ts: earliest component tick in a fused chain; immediate
        # (unfused) alerts fall back to a.timestamp. Latency/onset metrics
        # read this column instead of `start` so sliding-window and cross-
        # chain artifacts don't back-date the reported alert fire time.
        first_fire = a.first_fire_ts or a.timestamp
        # fire_ticks: every component fire tick in the chain (semicolon-
        # joined ISO). Per-fire metrics grade each tick against GT
        # containment independently, so a fuser-bridged chain whose only
        # in-label fire was at 75% elapsed can't pretend it was caught
        # at the chain's earliest pre-label tick. Immediate alerts have
        # no fused components, so we fall back to (timestamp,).
        ticks = a.fire_ticks or (a.timestamp,)
        fire_ticks_iso = ";".join(t.isoformat() for t in ticks)
        # inferred_type: explainer-derived canonical type (pre-typed alerts
        # from DQG / state_transition pass through; detector-combo chains
        # get a best-guess label via classify_type). inferred_class maps
        # the type to {user_behavior, sensor_fault, unknown} so the eval
        # harness can prevent a DQG `dropout` claim from being credited
        # as TP against a `water_leak_sustained` GT label on the same
        # sensor (and vice versa).
        sustained_oor = (a.anomaly_type == "out_of_range"
                         and _is_sustained_oor(a))
        detectors = set((a.detector or "").split("+"))
        is_dcs = bool(detectors & _DCS_DETECTORS)
        sustained_dcs = is_dcs and _is_sustained_dcs(a)
        time_of_day_pattern = is_dcs and _is_time_of_day_pattern(a)
        inferred_type = classify_type(a, sustained_oor=sustained_oor,
                                       sustained_dcs=sustained_dcs,
                                       time_of_day_pattern=time_of_day_pattern)
        inferred_class = type_to_class(inferred_type)
        rows.append({"sensor_id": a.sensor_id, "capability": a.capability,
                     "start": start.isoformat(), "end": end.isoformat(),
                     "first_fire_ts": first_fire.isoformat(),
                     "fire_ticks": fire_ticks_iso,
                     "anomaly_type": a.anomaly_type or a.detector,
                     "inferred_type": inferred_type,
                     "inferred_class": inferred_class,
                     "detector": a.detector,
                     "threshold": float(a.threshold),
                     "score": a.score})
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows, columns=["sensor_id","capability","start","end",
                                 "first_fire_ts","fire_ticks","anomaly_type",
                                 "inferred_type","inferred_class",
                                 "detector","threshold","score"]).to_csv(path, index=False)


def evaluate(detections_csv: Path, labels_csv: Path,
             events_csv: Path | None = None,
             config_yaml: Path | None = None) -> dict:
    """Print the stratified BEHAVIOR / sensor_fault headline block and
    return the structured dict.

    Timeline span (used to normalize `user_visible_fps_per_day`) is read
    from `events_csv` when provided, else derived from the labels'
    min/max range. Pass `--events` for the most accurate rate.

    If `config_yaml` is provided, GT labels for sensors not in the
    config are dropped — mirroring the pipeline's own sensor filter so
    OOS labels don't count as FN. Pass the same `--config` you used
    with `python -m anomaly run` to get research-matching numbers.
    """
    gt = pd.read_csv(labels_csv)
    if config_yaml is not None:
        cfg = yaml.safe_load(Path(config_yaml).read_text())
        cfg_sensors = {(s["id"], s["capability"]) for s in cfg["sensors"]}
        gt = gt[gt.apply(
            lambda r: (r["sensor_id"], r["capability"]) in cfg_sensors,
            axis=1)].reset_index(drop=True)
    det = pd.read_csv(detections_csv)
    if events_csv is not None:
        ts = pd.to_datetime(pd.read_csv(events_csv, usecols=["timestamp"])
                            ["timestamp"], utc=True, format="ISO8601")
        timeline_days = float((ts.max() - ts.min()).total_seconds() / 86400)
    else:
        ls = pd.to_datetime(gt["start"], utc=True, format="ISO8601")
        le = pd.to_datetime(gt["end"], utc=True, format="ISO8601")
        timeline_days = float((le.max() - ls.min()).total_seconds() / 86400)
    m = compute_stratified(gt, det, timeline_days)
    print(f"\n=== Headline (timeline {timeline_days:.1f}d) ===")
    # Per-fire grading: each pre-fusion component tick = one LLM call.
    # `fire_purity` = fires landing in any GT / total fires.
    # `type_acc`    = of in-GT fires, fraction with correct inferred_type.
    # `onTime%`     = correctly-typed-detected labels with earliest-typed
    #                 chain-end within MET budget, %. Reflects user-visible
    #                 alert latency at fuser flush; budgets per type live in
    #                 metrics.MET_HOURS. Denominator is correctly-typed-
    #                 detected labels only (not all labels).
    # `uvfp/d`      = chains classified user_behavior with no GT overlap,
    #                 per day (the user-visible LLM-spam rate).
    print(f"{'block':<14} {'n_lbl':>5} {'incR':>6} {'evt_F1':>7} "
          f"{'fpur':>6} {'tyAcc':>6} {'uvfp/d':>7} {'onTime%':>8}")
    for block_name in ("behavior", "sensor_fault"):
        b = m[block_name]
        if b.get("n_labels", 0) == 0:
            print(f"  {block_name:<12} (no labels)")
            continue
        ta = b.get("type_acc")
        ta_s = "     -" if ta is None else f"{ta:>6.3f}"
        ot = b.get("on_time_rate")
        ot_s = "       -" if ot is None else f"{ot * 100:>7.1f}%"
        print(f"  {block_name:<12} {b['n_labels']:>5d} "
              f"{b['incident_recall']:>6.3f} {b['evt_f1']:>7.3f} "
              f"{b['fire_purity']:>6.3f} {ta_s} "
              f"{b['user_visible_fps_per_day']:>7.2f} {ot_s}")
    return m


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    ap = argparse.ArgumentParser(prog="anomaly")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--events", required=True, type=Path)
    r.add_argument("--config", required=True, type=Path)
    r.add_argument("--out", required=True, type=Path)
    r.add_argument("--bootstrap-days", type=float, default=14.0)
    e = sub.add_parser("eval")
    e.add_argument("--detections", required=True, type=Path)
    e.add_argument("--labels", required=True, type=Path)
    e.add_argument("--events", type=Path, default=None,
                   help="optional; events.csv used to derive the timeline span "
                        "for user_visible_fps_per_day. Falls back to label "
                        "min/max range when omitted.")
    e.add_argument("--config", type=Path, default=None,
                   help="optional; same sensor config used with `run`. When "
                        "provided, GT labels for sensors not in the config "
                        "are dropped (mirrors pipeline's sensor filter).")
    v = sub.add_parser("viz")
    v.add_argument("--events", required=True, type=Path)
    v.add_argument("--labels", required=True, type=Path)
    v.add_argument("--detections", required=True, type=Path)
    v.add_argument("--out", required=True, type=Path)
    v.add_argument("--sensor-names", type=Path, default=None,
                   help="JSON file mapping sensor_id to friendly display name")
    v.add_argument("--max-showcases", type=int, default=8,
                   help="cap on the number of curated showcase pages")
    v.add_argument("--exclude-sensors", default="",
                   help="comma-separated sensor_ids to drop from the report")
    v.add_argument("--title", default=None,
                   help="document title; default auto-derived from events.csv path")
    vl = sub.add_parser("viz-long")
    vl.add_argument("--events", required=True, type=Path)
    vl.add_argument("--labels", required=True, type=Path)
    vl.add_argument("--detections", type=Path, default=None)
    vl.add_argument("--out", required=True, type=Path)
    vl.add_argument("--min-hours", type=float, default=24.0,
                    help="minimum label duration to get its own detail page")
    ex = sub.add_parser("explain")
    ex.add_argument("--events", required=True, type=Path)
    ex.add_argument("--detections", required=True, type=Path)
    ex.add_argument("--out", required=True, type=Path,
                    help="JSONL path - one bundle per detection")
    args = ap.parse_args(argv)
    if args.cmd == "run":
        run(args.events, args.config, args.out, args.bootstrap_days); return 0
    if args.cmd == "eval":
        evaluate(args.detections, args.labels, args.events, args.config); return 0
    if args.cmd == "viz":
        import json as _json
        from .viz import render
        ev = pd.read_csv(args.events)
        lb = pd.read_csv(args.labels)
        dt = pd.read_csv(args.detections)
        sn = _json.loads(args.sensor_names.read_text()) if args.sensor_names else {}
        excluded = frozenset(s.strip() for s in args.exclude_sensors.split(",") if s.strip())
        render(ev, lb, dt, args.out,
               sensor_names=sn,
               max_showcases=args.max_showcases,
               excluded_sensors=excluded,
               title=args.title)
        print(f"wrote {args.out}")
        return 0
    if args.cmd == "viz-long":
        from .viz import render_long
        ev = pd.read_csv(args.events)
        lb = pd.read_csv(args.labels)
        dt = pd.read_csv(args.detections) if args.detections else None
        render_long(ev, lb, dt, args.out, min_hours=args.min_hours)
        print(f"wrote {args.out}")
        return 0
    if args.cmd == "explain":
        from .explain import explain_detections_csv
        n = explain_detections_csv(args.events, args.detections, args.out)
        print(f"wrote {n} bundles to {args.out}")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
