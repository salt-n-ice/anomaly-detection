from __future__ import annotations
from collections import deque
from typing import Protocol
import math
import numpy as np
import pandas as pd
from .core import Event, Alert, SensorConfig, Archetype


class Detector(Protocol):
    name: str
    live: bool
    def fit(self, rows: list[tuple[pd.Timestamp, dict]]) -> None: ...
    def update(self, ts: pd.Timestamp, feat: dict) -> list[Alert]: ...


class EventDetector(Protocol):
    """SHORT-band pre-adapter raw-event detector. DataQualityGate is the
    canonical impl — out_of_range, saturation, duplicate_stale, clock_drift,
    dropout, batch_arrival per raw event."""
    name: str
    def check(self, ev: Event) -> list[Alert]: ...


def _alert(cfg: SensorConfig, ts, detector, score, threshold, atype, raw, state=None,
           w0=None, w1=None, context=None) -> Alert:
    return Alert(cfg.sensor_id, cfg.capability, ts, detector, float(score),
                 float(threshold), atype, raw, state, w0, w1,
                 [context] if context is not None else None)


class DataQualityGate:
    name = "data_quality_gate"
    live = True

    _OOR_COOLDOWN = pd.Timedelta(minutes=30)     # suppress repeat OOR alerts within this window (oscillation during noise_burst / frequency_change crosses boundaries many times)
    _DROPOUT_COOLDOWN = pd.Timedelta(minutes=30) # suppress repeat dropout alerts (reporting_rate_change floods)
    _BATCH_COOLDOWN = pd.Timedelta(minutes=30)   # suppress repeat batch_arrival alerts (generator batches release many events, tripping the burst detector every 12 events)
    _CLOCK_DRIFT_COOLDOWN = pd.Timedelta(minutes=5)
    _CLOCK_DRIFT_TICK_RATIO = 0.005   # per-tick delta threshold as fraction of expected_interval (floor 3s)
    _CLOCK_DRIFT_PERSISTENCE = 3      # consecutive drifted ticks required before firing
    _EXTREME_CAL_SAMPLES = 100        # events to observe before the extreme_value branch arms
    _EXTREME_RATIO_BURSTY = 3.0       # BURSTY cycles ON/OFF with natural peaks ~2x OFF-state median, so anything lower than 3x tripped during normal ON windows
    _EXTREME_RATIO_CONT = 1.7         # CONTINUOUS sensors have narrow natural variance around a stable mean, so a tighter ratio is safe and catches leak_temperature's 1.78x spike
    _EXTREME_COOLDOWN = pd.Timedelta(hours=1)

    def __init__(self, config: SensorConfig):
        self.config = config
        self._last_ts: pd.Timestamp | None = None
        self._last_val: float | None = None
        self._sat_run = 0
        self._burst: deque[pd.Timestamp] = deque(maxlen=12)
        self._last_min_fire: pd.Timestamp | None = None
        self._last_max_fire: pd.Timestamp | None = None
        self._last_dropout_fire: pd.Timestamp | None = None
        self._last_batch_fire: pd.Timestamp | None = None
        self._clock_drift_count: int = 0   # consecutive-tick counter; decays on normal-cadence ticks
        self._last_clock_drift_fire: pd.Timestamp | None = None
        self._extreme_seen = 0             # calibration-phase sample counter
        self._extreme_ref_max: float = -math.inf  # expanding max; updates on every event and on every fire
        self._last_extreme_fire: pd.Timestamp | None = None
        self._extreme_ratio = (self._EXTREME_RATIO_CONT
                               if config.archetype == Archetype.CONTINUOUS
                               else self._EXTREME_RATIO_BURSTY)

    def fit(self, rows): pass
    def update(self, ts, feat): return []

    def check(self, ev: Event) -> list[Alert]:
        cfg = self.config
        out: list[Alert] = []
        # out-of-range: fire on entry, then cool down to suppress oscillation around threshold
        if cfg.min_value is not None and ev.value < cfg.min_value:
            if self._last_min_fire is None or (ev.timestamp - self._last_min_fire) >= self._OOR_COOLDOWN:
                out.append(_alert(cfg, ev.timestamp, self.name, ev.value, cfg.min_value,
                                  "out_of_range", ev.value,
                                  context={"detector": self.name, "reason": "out_of_range",
                                           "side": "min", "value": ev.value, "limit": cfg.min_value}))
                self._last_min_fire = ev.timestamp
        if cfg.max_value is not None and ev.value > cfg.max_value:
            if self._last_max_fire is None or (ev.timestamp - self._last_max_fire) >= self._OOR_COOLDOWN:
                out.append(_alert(cfg, ev.timestamp, self.name, ev.value, cfg.max_value,
                                  "out_of_range", ev.value,
                                  context={"detector": self.name, "reason": "out_of_range",
                                           "side": "max", "value": ev.value, "limit": cfg.max_value}))
                self._last_max_fire = ev.timestamp
        # extreme_value: pre-bootstrap spike catcher. After N calibration events the
        # running max is frozen-by-default; a new value > max * RATIO fires and updates
        # the max so sustained high values re-calibrate upward (saturation/OOR
        # regions don't produce a fire stream). Monotonic max update means natural
        # post-bootstrap peaks reset the threshold to keep pace with level shifts.
        if self._extreme_seen < self._EXTREME_CAL_SAMPLES:
            if ev.value > self._extreme_ref_max:
                self._extreme_ref_max = ev.value
            self._extreme_seen += 1
        elif self._extreme_ref_max > 0:
            thr = self._extreme_ref_max * self._extreme_ratio
            if ev.value > thr:
                if (self._last_extreme_fire is None
                        or (ev.timestamp - self._last_extreme_fire) >= self._EXTREME_COOLDOWN):
                    out.append(_alert(cfg, ev.timestamp, self.name, ev.value, thr,
                                      "extreme_value", ev.value,
                                      context={"detector": self.name, "reason": "extreme_value",
                                               "value": ev.value, "ref_max": self._extreme_ref_max,
                                               "ratio": self._extreme_ratio}))
                    self._last_extreme_fire = ev.timestamp
                    self._extreme_ref_max = ev.value
        # saturation (10+ consecutive at max)
        if cfg.max_value is not None and ev.value >= cfg.max_value:
            self._sat_run += 1
            if self._sat_run == 10:
                out.append(_alert(cfg, ev.timestamp, self.name, ev.value, cfg.max_value,
                                  "saturation", ev.value,
                                  context={"detector": self.name, "reason": "saturation",
                                           "value": ev.value, "max": cfg.max_value,
                                           "consecutive_at_max": self._sat_run}))
        else:
            self._sat_run = 0
        # duplicate / stale
        if self._last_ts is not None and ev.timestamp == self._last_ts and ev.value == self._last_val:
            out.append(_alert(cfg, ev.timestamp, self.name, 0, 0, "duplicate_stale", ev.value,
                              context={"detector": self.name, "reason": "duplicate_stale",
                                       "value": ev.value,
                                       "repeats_ts": self._last_ts.isoformat()}))
        # clock drift: per-tick deviation from expected cadence, persistence-gated.
        # Only meaningful on CONTINUOUS sensors with sub-hourly heartbeat — bursty
        # cadence is event-driven and battery-cadence sensors are too slow for a
        # stable per-tick interval baseline. Gaps outside [0.5x, 1.5x] expected are
        # excluded (handled by dropout/batch detectors). A counter grows on ticks
        # whose deviation exceeds `max(3s, 0.5% * expected_interval)` and decays
        # by one on normal ticks, so isolated boundary perturbations (e.g. a
        # single short gap where a neighboring anomaly window starts) don't fire
        # — only N-consecutive drifted ticks do.
        if (cfg.archetype == Archetype.CONTINUOUS
                and cfg.expected_interval_sec <= 3600
                and self._last_ts is not None):
            gap = (ev.timestamp - self._last_ts).total_seconds()
            if 0.5 * cfg.expected_interval_sec <= gap <= 1.5 * cfg.expected_interval_sec:
                delta_tick = gap - cfg.expected_interval_sec
                thr_tick = max(3.0, self._CLOCK_DRIFT_TICK_RATIO * cfg.expected_interval_sec)
                if abs(delta_tick) > thr_tick:
                    # Cap at PERSISTENCE so a single post-drift normal tick drops
                    # below the fire threshold — avoids 5h+ of post-GT clock_drift
                    # alerts after the drift window ends.
                    self._clock_drift_count = min(self._clock_drift_count + 1,
                                                  self._CLOCK_DRIFT_PERSISTENCE)
                else:
                    self._clock_drift_count = max(0, self._clock_drift_count - 1)
                if self._clock_drift_count >= self._CLOCK_DRIFT_PERSISTENCE:
                    if (self._last_clock_drift_fire is None
                            or (ev.timestamp - self._last_clock_drift_fire) >= self._CLOCK_DRIFT_COOLDOWN):
                        out.append(_alert(cfg, ev.timestamp, self.name, delta_tick,
                                          thr_tick, "clock_drift", ev.value,
                                          context={"detector": self.name, "reason": "clock_drift",
                                                   "delta_sec": float(delta_tick),
                                                   "threshold_sec": float(thr_tick),
                                                   "expected_interval_sec": cfg.expected_interval_sec}))
                        self._last_clock_drift_fire = ev.timestamp
            else:
                # Out-of-window gap: the sensor is not in its configured cadence regime
                # (burst-mode, dropout-adjacent, or batch). Decay the counter so drift
                # persistence only counts N-consecutive IN-WINDOW drifted ticks — not
                # drift state carried indefinitely across non-cadence stretches.
                self._clock_drift_count = max(0, self._clock_drift_count - 1)
        # dropout (cooldown mirrors OOR — reporting_rate_change floods with tiny-gap events)
        if self._last_ts is not None:
            gap = (ev.timestamp - self._last_ts).total_seconds()
            if gap > cfg.max_gap_sec:
                if (self._last_dropout_fire is None
                        or (ev.timestamp - self._last_dropout_fire) >= self._DROPOUT_COOLDOWN):
                    # Window the alert over the dropout span (last valid event → current)
                    # so interval metrics line up with the GT dropout window. Without
                    # this, the alert is an instant fire at ev.timestamp and misses the
                    # GT window by one tick (detection is always post-dropout).
                    out.append(_alert(cfg, ev.timestamp, self.name, gap, cfg.max_gap_sec,
                                      "dropout", ev.value,
                                      w0=self._last_ts, w1=ev.timestamp,
                                      context={"detector": self.name, "reason": "dropout",
                                               "gap_sec": float(gap),
                                               "max_gap_sec": float(cfg.max_gap_sec)}))
                    self._last_dropout_fire = ev.timestamp
        # batch arrival: many events in <1s. Cooldown prevents a single batch-release
        # from generator firing 10+ times (every 12 rapid events would otherwise trip).
        self._burst.append(ev.timestamp)
        if len(self._burst) == self._burst.maxlen:
            span = (self._burst[-1] - self._burst[0]).total_seconds()
            if span < 1.0:
                if (self._last_batch_fire is None
                        or (ev.timestamp - self._last_batch_fire) >= self._BATCH_COOLDOWN):
                    out.append(_alert(cfg, ev.timestamp, self.name, len(self._burst), 1.0,
                                      "batch_arrival", ev.value,
                                      context={"detector": self.name, "reason": "batch_arrival",
                                               "burst_size": len(self._burst),
                                               "span_sec": float(span)}))
                    self._last_batch_fire = ev.timestamp
                self._burst.clear()
        self._last_ts = ev.timestamp
        self._last_val = ev.value
        return out


class RecentShift:
    name = "recent_shift"

    def __init__(self, config: SensorConfig, short_feature: str = "value_roll_1h",
                 baseline_features: tuple[str, ...] = ("value_roll_24h", "value_roll_7d"),
                 quantile: float = 0.999, min_score: float = 1.1):
        # min_score: multiplicative margin above the bootstrap-quantile threshold
        # required to emit. Periodic signals (e.g. basement_temp diurnal) have
        # a point-estimate tail that the 7-day bootstrap undersamples — day-to-
        # day peak-amplitude variance produces fires at score 1.00-1.05 that
        # are noise, not signal. Drift signals (calibration_drift, level_shift)
        # sustain >24% above threshold; the 10% margin separates them cleanly.
        self.config = config
        self.short_feature = short_feature
        self.baseline_features = baseline_features
        self.quantile = quantile
        self.min_score = min_score
        self.live = False
        self._thresholds: dict[str, float] = {}

    def fit(self, rows):
        by_feature = {k: [] for k in self.baseline_features}
        for _, feat in rows:
            short_v = feat.get(self.short_feature)
            if short_v is None or (isinstance(short_v, float) and math.isnan(short_v)):
                continue
            short_v = float(short_v)
            for base_k in self.baseline_features:
                base_v = feat.get(base_k)
                if base_v is None or (isinstance(base_v, float) and math.isnan(base_v)):
                    continue
                by_feature[base_k].append(abs(short_v - float(base_v)))
        for base_k, vals in by_feature.items():
            if len(vals) < 20:
                continue
            self._thresholds[base_k] = max(float(np.quantile(vals, self.quantile)), 1e-6)
        self.live = bool(self._thresholds)

    def update(self, ts, feat):
        if not self.live:
            return []
        short_v = feat.get(self.short_feature)
        if short_v is None or (isinstance(short_v, float) and math.isnan(short_v)):
            return []
        short_v = float(short_v)
        best: tuple[str, float, float, float] | None = None
        for base_k, thr in self._thresholds.items():
            base_v = feat.get(base_k)
            if base_v is None or (isinstance(base_v, float) and math.isnan(base_v)):
                continue
            delta = abs(short_v - float(base_v))
            ratio = delta / thr if thr > 0 else 0.0
            if best is None or ratio > best[1]:
                best = (base_k, ratio, delta, thr)
        if best is None or best[1] <= self.min_score:
            return []
        base_k, ratio, delta, thr = best
        return [_alert(self.config, ts, self.name, ratio, 1.0, None, short_v,
                       w0=ts - pd.Timedelta(hours=1), w1=ts,
                       context={"detector": self.name,
                                "short_feature": self.short_feature,
                                "baseline_feature": base_k,
                                "delta": float(delta),
                                "delta_threshold": float(thr),
                                "short_value": float(short_v),
                                "baseline_value": float(feat.get(base_k))})]


def _fit_pca(X: np.ndarray, var_ratio: float = 0.95):
    mu = X.mean(axis=0)
    Xc = X - mu
    _, S, VT = np.linalg.svd(Xc, full_matrices=False)
    total = (S ** 2).sum()
    if total == 0.0:
        # Degenerate: constant data; keep 1 component so reconstruction is
        # partial and any deviation from the training constant is detectable.
        k = 1
    else:
        cum = np.cumsum(S ** 2) / total
        k = max(1, int(np.searchsorted(cum, var_ratio) + 1))
        k = min(k, len(S))  # guard: searchsorted may return len(S)
    P = VT[:k].T  # projection d×k
    return mu, P


def _pca_error(x: np.ndarray, mu: np.ndarray, P: np.ndarray) -> float:
    xc = x - mu
    rec = xc @ P @ P.T
    d = xc - rec
    return float(d @ d)


class RollingMedianPeakShift:
    """Rolling median of last N event peaks vs bootstrap per-event peak
    distribution. Fires on sustained shift in the median peak.

    Mechanism fit (vs EventPeakShift iter 10/10b/10c REJECT):
    - Single-event peak comparison (EventPeakShift) fires on natural
      multi-phase variance: fridge has compressor-on, defrost, startup,
      door-open peaks legitimately distributed over a wide range.
    - Rolling MEDIAN of last N event peaks is robust to natural phase
      variance: even if 2 of the 5 recent events are defrost / startup
      outliers, the median picks the typical-phase peak. A sustained
      level_shift / trend / degradation drives the median of EVERY
      recent event up or down, not just occasional outliers.
    - Bootstrap stats = median + MAD (median absolute deviation) across
      all bootstrap events; compare recent-median to bootstrap-median
      in units of MAD. Z-threshold gate.

    Expected label fit: level_shift, trend, degradation_trajectory
    (the 11 value-based BURSTY long labels). NOT a fit for time-based
    labels (time_of_day, weekend_anomaly) — median peak doesn't move
    when events just shift in time.
    """
    name = "rolling_median_peak_shift"

    def __init__(self, config: SensorConfig, on_threshold: float = 50.0,
                 min_event_ticks: int = 3, rolling_n: int = 5,
                 min_bootstrap_events: int = 30, z_threshold: float = 3.0,
                 cooldown_s: int = 6 * 3600, feature: str = "value",
                 adapt_K: int = 3, adapt_quiet_s: int = 24 * 3600,
                 adapt_history_n: int = 20):
        # rolling_n=5: median of last 5 event peaks. On kettle (~3 events/day),
        # this is a ~1.7-day rolling horizon. On fridge (~100 events/day),
        # this is ~1h. For LONG labels (14-28d), lat_frac ≈ 6-12% — near
        # 10% ceiling; smaller rolling_n = faster but noisier.
        # z_threshold=3.0 on MAD-normalized deviation of median.
        # cooldown_s=6h: typical shift sustains; one fire per 6h window.
        # adapt_K=3: after 3 consecutive cooldown-spaced fires (~18h sustained
        # high-|z|), absorb the new regime into boot_median (LEARNINGS §2
        # equivalent for cooldown>gap detectors — the chain-flush hook in
        # pipeline.py never triggers because each fire is a singleton chain,
        # so the adapt has to be detector-internal). adapt_quiet_s=24h: a
        # gap >24h between fires resets the streak, so sporadic single fires
        # don't accumulate toward adapt.
        self.config = config
        self.on_threshold = on_threshold
        self.min_event_ticks = min_event_ticks
        self.rolling_n = rolling_n
        self.min_bootstrap_events = min_bootstrap_events
        self.z_threshold = z_threshold
        self.cooldown_s = cooldown_s
        self.feature = feature
        self.adapt_K = adapt_K
        self.adapt_quiet_s = adapt_quiet_s
        self.live = False
        self._boot_median: float = 0.0
        self._boot_mad: float = 1.0
        self._recent_peaks: deque = deque(maxlen=rolling_n)
        # Longer event-peak history for self-adapt re-fit (more stable median
        # than the 5-event rolling deque). Maxlen 20 ≈ ~5h on fridge,
        # ~6.7d on kettle; in either case enough samples for a stable median.
        self._adapt_peaks: deque = deque(maxlen=adapt_history_n)
        self._event_peak: float | None = None
        self._event_ticks: int = 0
        self._event_start_ts: pd.Timestamp | None = None
        self._prev_above = False
        self._last_fire_ts: pd.Timestamp | None = None
        self._consecutive_fires: int = 0

    def _scan_peaks(self, rows):
        prev_above = False
        cur_peak: float | None = None
        cur_ticks = 0
        for _ts, f in rows:
            v = f.get(self.feature)
            if v is None or (isinstance(v, float) and math.isnan(v)):
                continue
            v = float(v)
            above = v > self.on_threshold
            if above:
                if not prev_above:
                    cur_peak = v
                    cur_ticks = 1
                else:
                    cur_peak = max(cur_peak or v, v)
                    cur_ticks += 1
            else:
                if prev_above and cur_ticks >= self.min_event_ticks and cur_peak is not None:
                    yield cur_peak
                cur_peak = None
                cur_ticks = 0
            prev_above = above

    def fit(self, rows):
        peaks = list(self._scan_peaks(rows))
        if len(peaks) < self.min_bootstrap_events:
            return
        arr = np.asarray(peaks)
        self._boot_median = float(np.median(arr))
        # MAD = median absolute deviation; floor at 1e-3 of boot_median to
        # avoid zero for perfectly uniform bootstrap peaks.
        mad = float(np.median(np.abs(arr - self._boot_median)))
        self._boot_mad = max(mad, abs(self._boot_median) * 0.01, 1.0)
        self.live = True

    def adapt_to_recent(self, rows):
        # LEARNINGS §2: Pipeline-hook variant (called by pipeline.py at
        # K=3 max_span streak). Used by detectors whose chains naturally
        # span max_span. RollingMedianPeak has cooldown(6h)>fuser_gap(1h)
        # so each fire is a singleton chain — the streak hook does not
        # trigger for this detector. Implementation kept for completeness
        # and for any future fuser-gap revision that lets these chains
        # extend (e.g., fast cooldown variants).
        if not self.live or not rows:
            return
        peaks = list(self._scan_peaks(rows))
        if len(peaks) < 5:
            return
        arr = np.asarray(peaks)
        new_median = float(np.median(arr))
        new_mad = float(np.median(np.abs(arr - new_median)))
        self._boot_median = new_median
        self._boot_mad = max(self._boot_mad, new_mad,
                             abs(new_median) * 0.01, 1.0)

    def _self_adapt(self):
        # LEARNINGS §2: detector-internal adapt. Triggered when
        # _consecutive_fires reaches adapt_K with no quiet gap > adapt_quiet_s.
        # Re-fits boot_median + boot_mad from _adapt_peaks (last ~20 event
        # peaks). MAD-only-grow floor: a quieter post-shift regime keeps
        # the original firing band rather than tightening → no over-fire
        # trap on in-regime noise.
        if len(self._adapt_peaks) < 5:
            return
        arr = np.asarray(self._adapt_peaks)
        new_median = float(np.median(arr))
        new_mad = float(np.median(np.abs(arr - new_median)))
        self._boot_median = new_median
        self._boot_mad = max(self._boot_mad, new_mad,
                             abs(new_median) * 0.01, 1.0)

    def update(self, ts, feat):
        if not self.live:
            return []
        v = feat.get(self.feature)
        if v is None or (isinstance(v, float) and math.isnan(v)):
            return []
        v = float(v)
        above = v > self.on_threshold
        alerts: list = []
        if above:
            if not self._prev_above:
                self._event_peak = v
                self._event_ticks = 1
                self._event_start_ts = ts
            else:
                self._event_peak = max(self._event_peak or v, v)
                self._event_ticks += 1
        else:
            if (self._prev_above and self._event_ticks >= self.min_event_ticks
                    and self._event_peak is not None):
                self._recent_peaks.append(self._event_peak)
                self._adapt_peaks.append(self._event_peak)
                if len(self._recent_peaks) >= self.rolling_n:
                    roll_median = float(np.median(list(self._recent_peaks)))
                    z = (roll_median - self._boot_median) / self._boot_mad
                    cooldown_ok = (self._last_fire_ts is None
                                   or (ts - self._last_fire_ts).total_seconds()
                                      >= self.cooldown_s)
                    if abs(z) > self.z_threshold and cooldown_ok:
                        # Streak counter for self-adapt: increment on each
                        # cooldown-spaced fire; reset to 1 if the gap from
                        # the previous fire exceeds adapt_quiet_s (sporadic
                        # firing isn't sustained-shift signal).
                        if self._last_fire_ts is None:
                            self._consecutive_fires = 1
                        else:
                            gap_s = (ts - self._last_fire_ts).total_seconds()
                            if gap_s > self.adapt_quiet_s:
                                self._consecutive_fires = 1
                            else:
                                self._consecutive_fires += 1
                        self._last_fire_ts = ts
                        direction = "high" if z > 0 else "low"
                        score = abs(z)
                        alerts.append(_alert(self.config, ts, self.name, score,
                                              self.z_threshold, None, float(roll_median),
                                              w0=ts - pd.Timedelta(minutes=1), w1=ts,
                                              context={"detector": self.name,
                                                       "roll_median": roll_median,
                                                       "bootstrap_median": self._boot_median,
                                                       "bootstrap_mad": self._boot_mad,
                                                       "z": float(z),
                                                       "direction": direction,
                                                       "rolling_n": self.rolling_n}))
                        if self._consecutive_fires >= self.adapt_K:
                            self._self_adapt()
                            self._consecutive_fires = 0
                self._event_peak = None
                self._event_ticks = 0
                self._event_start_ts = None
        self._prev_above = above
        return alerts


class DutyCycleShift:
    """Rolling 6h duty cycle (fraction of time in ON state) vs bootstrap
    per-6h-window distribution. Fires on sustained duty-cycle deviations.

    Mechanism fit:
    - Kettle normally has ~5-10% duty cycle. frequency_change anomalies
      multiply event rate → duty cycle shifts proportionally.
    - DutyCycle is a MAGNITUDE-free signal: it doesn't care about peak
      value, only time-in-ON-state. Orthogonal to RollingMedianPeakShift.
    - Bootstrap: sliding 6h windows across bootstrap span give a
      distribution of duty values; compute median + MAD.
    - Live: rolling tick counter maintains time-in-ON over last 6h.
      Fire when current 6h duty crosses z_threshold × MAD.

    Expected label fit: frequency_change (6 labels), reporting_rate_change
    (but that's sensor_fault). time_of_day / weekend may shift total
    6h-window duty slightly but not strongly.
    """
    name = "duty_cycle_shift"

    def __init__(self, config: SensorConfig, on_threshold: float = 50.0,
                 window_s: int = 6 * 3600, z_threshold: float = 3.0,
                 min_bootstrap_windows: int = 30, cooldown_s: int = 2 * 3600,
                 feature: str = "value"):
        # window_s=6h: compromise between latency and statistical power.
        # A frequency shift detectable in 6h covers medium+long labels.
        # cooldown_s=2h: shift sustains across multiple 6h windows; one fire
        # per 2h keeps the chain dense without spam.
        self.config = config
        self.on_threshold = on_threshold
        self.window_s = window_s
        self.z_threshold = z_threshold
        self.min_bootstrap_windows = min_bootstrap_windows
        self.cooldown_s = cooldown_s
        self.feature = feature
        self.live = False
        # Instance-specific name so multiple window-size instances emit
        # distinct detector tags (e.g., duty_cycle_shift_1h vs _6h). The
        # fuser treats them as separate detectors — a multi-window stack
        # can corroborate or OR-combine without colliding.
        self.name = f"duty_cycle_shift_{window_s // 3600}h"
        self._boot_median: float = 0.0
        self._boot_mad: float = 0.01
        # Bootstrap-percentile novelty gate (used only when boot_mad
        # collapses to its floor; see fit() / update()).
        self._boot_q01: float = 0.0
        self._boot_q99: float = 1.0
        self._mad_at_floor: bool = False
        # Per-bucket calendar baseline (populated by fit). Empty until fit
        # runs; classify falls back to "normal" for unfitted instances.
        self._bucket_typical: dict[tuple[bool, int], str] = {}
        # Live: (ts, above) pairs in rolling window. Duty over the window
        # is maintained incrementally via running sums — appending a tick
        # adds the (prev → current) interval; evicting an old tick subtracts
        # the (old → next-oldest) interval. Cuts per-tick cost from O(N)
        # window scan to O(1) (modulo eviction loops, amortized O(1) too).
        self._window: deque = deque()
        self._above_s_running: float = 0.0
        self._total_s_running: float = 0.0
        self._last_fire_ts: pd.Timestamp | None = None

    def _compute_bootstrap_windows(self, rows):
        """Slide a `window_s` window across bootstrap rows; compute duty per window.

        Returns list of (window_end_ts, duty) tuples. Window-end timestamp
        anchors each duty sample to the same calendar position the live
        update() will use at fire time, so per-bucket baselines computed here
        line up with live bucket lookups in update().
        """
        if not rows:
            return []
        duties_with_ts: list[tuple[pd.Timestamp, float]] = []
        # Bin rows by sliding window start, stepped by window_s/2 for overlap
        step = self.window_s // 2
        first_ts = rows[0][0]
        last_ts = rows[-1][0]
        w_start_ts = first_ts
        while w_start_ts + pd.Timedelta(seconds=self.window_s) <= last_ts:
            w_end_ts = w_start_ts + pd.Timedelta(seconds=self.window_s)
            above_s = 0.0
            total_s = 0.0
            prev_ts = None
            prev_above = False
            for ts, f in rows:
                if ts < w_start_ts or ts > w_end_ts:
                    continue
                v = f.get(self.feature)
                if v is None or (isinstance(v, float) and math.isnan(v)):
                    continue
                above = float(v) > self.on_threshold
                if prev_ts is not None:
                    dt = (ts - prev_ts).total_seconds()
                    total_s += dt
                    if prev_above:
                        above_s += dt
                prev_ts = ts
                prev_above = above
            if total_s > 0:
                duties_with_ts.append((w_end_ts, above_s / total_s))
            w_start_ts += pd.Timedelta(seconds=step)
        return duties_with_ts

    def fit(self, rows):
        duties_with_ts = self._compute_bootstrap_windows(rows)
        if len(duties_with_ts) < self.min_bootstrap_windows:
            return
        duties = [d for _, d in duties_with_ts]
        arr = np.asarray(duties)
        self._boot_median = float(np.median(arr))
        mad = float(np.median(np.abs(arr - self._boot_median)))
        # MAD floor stays at 0.005 so the existing z scaling is preserved
        # for sensors with meaningful natural variance. Track whether the
        # raw MAD hit the floor — bimodal-zero distributions on chatty
        # BURSTY outlets (TV 14% ZOH, kettle 35% ZOH with mostly-off
        # bootstrap windows) collapse MAD to ~0, then z = duty/0.005
        # explodes for any non-zero live duty. The percentile-novelty
        # gate in update() activates only in that regime.
        self._boot_mad = max(mad, 0.005)
        self._boot_q01 = float(np.quantile(arr, 0.01))
        self._boot_q99 = float(np.quantile(arr, 0.99))
        self._mad_at_floor = (mad <= 0.005)

        # Per-bucket calendar baseline. Buckets are (is_weekend, hour) → 48
        # cells. Each bootstrap window is assigned to the bucket of its
        # window-end timestamp; per-bucket median is then split into
        # low/normal/high tertiles by percentile rank across bucket medians.
        # The classifier reads bucket_typical to disambiguate:
        #   - "low" + direction "+" → behavior elevated in typically-quiet
        #     time → calendar-pattern anomaly (target=weekend on weekday,
        #     time_of_day at unusual hour).
        #   - "high" + direction "-" → behavior depressed in typically-busy
        #     time → calendar-pattern anomaly (target=weekday on weekend).
        # Falls back to "normal" for buckets with too few bootstrap samples
        # or when the global classification can't be computed (< 6 buckets).
        bucket_duties: dict[tuple[bool, int], list[float]] = {}
        for ts, d in duties_with_ts:
            key = (bool(ts.dayofweek >= 5), int(ts.hour))
            bucket_duties.setdefault(key, []).append(d)
        bucket_medians: dict[tuple[bool, int], float] = {}
        for key, vals in bucket_duties.items():
            if len(vals) >= 3:
                bucket_medians[key] = float(np.median(vals))
        self._bucket_typical: dict[tuple[bool, int], str] = {}
        if len(bucket_medians) >= 6:
            sorted_medians = sorted(bucket_medians.values())
            n = len(sorted_medians)
            p30_idx = max(0, int(n * 0.3) - 1)
            p70_idx = min(n - 1, int(n * 0.7))
            p30 = sorted_medians[p30_idx]
            p70 = sorted_medians[p70_idx]
            for key, m in bucket_medians.items():
                if m <= p30:
                    self._bucket_typical[key] = "low"
                elif m >= p70:
                    self._bucket_typical[key] = "high"
                else:
                    self._bucket_typical[key] = "normal"

        self.live = True

    def update(self, ts, feat):
        if not self.live:
            return []
        v = feat.get(self.feature)
        if v is None or (isinstance(v, float) and math.isnan(v)):
            return []
        above = float(v) > self.on_threshold
        # Incremental running-sum update: the new tick closes the interval
        # from the previous tick to itself, contributing prev_above × dt
        # to above_s and dt to total_s. Eviction below subtracts the
        # symmetric contribution from the oldest interval.
        if self._window:
            ts_prev, above_prev = self._window[-1]
            dt = (ts - ts_prev).total_seconds()
            self._total_s_running += dt
            if above_prev:
                self._above_s_running += dt
        self._window.append((ts, above))
        cutoff = ts - pd.Timedelta(seconds=self.window_s)
        while self._window and self._window[0][0] < cutoff:
            ts_old, above_old = self._window.popleft()
            if self._window:
                ts_next = self._window[0][0]
                dt_old = (ts_next - ts_old).total_seconds()
                self._total_s_running -= dt_old
                if above_old:
                    self._above_s_running -= dt_old
            else:
                # Window emptied; reset running sums to clean zero (avoid
                # accumulated float drift across many evictions).
                self._above_s_running = 0.0
                self._total_s_running = 0.0
        if len(self._window) < 10:
            return []
        if self._total_s_running <= 0:
            return []
        duty = self._above_s_running / self._total_s_running
        z = (duty - self._boot_median) / self._boot_mad
        cooldown_ok = (self._last_fire_ts is None
                       or (ts - self._last_fire_ts).total_seconds() >= self.cooldown_s)
        if abs(z) > self.z_threshold and cooldown_ok:
            # Percentile-novelty gate (only when bootstrap MAD collapsed):
            # require live duty to fall outside the bootstrap [q01, q99]
            # range. Suppresses z-inflation FPs from chatty BURSTY outlets
            # whose bootstrap is dominated by zero-duty windows. Real
            # magnitude-novel anomalies push duty into a regime never
            # seen during bootstrap; natural-variance fires (and
            # z-inflation "fluke TPs" — see iter 023 ITERATIONS.md)
            # stay within it.
            # Trial A: percentile gate ALWAYS applied (not just when
            # mad_at_floor). Tests whether fridge low-z FPs at duty values
            # inside the bootstrap envelope can be filtered cleanly.
            if z > 0 and duty <= self._boot_q99:
                return []
            if z < 0 and duty >= self._boot_q01:
                return []
            self._last_fire_ts = ts
            direction = "high" if z > 0 else "low"
            score = abs(z)
            bucket_key = (bool(ts.dayofweek >= 5), int(ts.hour))
            bucket_typical = self._bucket_typical.get(bucket_key, "normal")
            return [_alert(self.config, ts, self.name, score, self.z_threshold,
                           None, float(duty),
                           w0=ts - pd.Timedelta(minutes=1), w1=ts,
                           context={"detector": self.name,
                                    "duty": duty,
                                    "bootstrap_median": self._boot_median,
                                    "bootstrap_mad": self._boot_mad,
                                    "z": float(z),
                                    "direction": direction,
                                    "window_s": self.window_s,
                                    "bucket_typical": bucket_typical})]
        return []


class StateTransition:
    """Tick-level trigger for deterministic binary events (e.g. water leak
    sustain). Emits a `state_transition` alert when `feat['trigger']` is
    truthy. Extracted from inline code in pipeline.py."""
    name = "state_transition"
    live = True

    def __init__(self, config: SensorConfig):
        self.config = config

    def fit(self, rows): pass

    def update(self, ts, feat):
        if not feat.get("trigger"):
            return []
        # window_start/window_end left as None so `_write_detections` applies
        # the default 1-minute window_end — a 0-duration alert at the label's
        # exact start fails `_overlaps`' strict-less-than check (`ts < ts` is
        # False) and would not count as overlapping a label that starts at
        # the same tick. The 1-minute tail makes overlap semantically correct.
        if self.config.capability == "water":
            atype = "water_leak_sustained"
        else:
            atype = self.name  # fallback — shouldn't occur at this stage
        return [Alert(self.config.sensor_id, self.config.capability, ts,
                      self.name, 1.0, 1.0, atype, 1.0,
                      feat.get("state"), None, None,
                      [{"detector": self.name, "state": feat.get("state")}])]
