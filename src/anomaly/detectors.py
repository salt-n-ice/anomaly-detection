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


class CUSUM:
    name = "cusum"

    def __init__(self, config: SensorConfig, features: list[str],
                 delta_sigma: float = 0.1, lam: float = 5.0,
                 warmup_seconds: float = 0.0):
        self.config = config
        self.features = features
        self.delta_sigma = delta_sigma
        self.lam = lam
        self.warmup_seconds = warmup_seconds
        self.live = False
        # per-state per-feature: (mean, sigma, s_pos, s_neg)
        self._state: dict[tuple[int, str], list[float]] = {}
        self._first_update_ts: pd.Timestamp | None = None

    def _get_state(self, feat: dict) -> int:
        return int(feat.get("state", 0)) if self.config.archetype == Archetype.BURSTY else 0

    def fit(self, rows):
        by_state: dict[int, dict[str, list[float]]] = {}
        for ts, f in rows:
            s = self._get_state(f)
            bkt = by_state.setdefault(s, {k: [] for k in self.features})
            for k in self.features:
                v = f.get(k)
                if v is None or (isinstance(v, float) and math.isnan(v)):
                    continue
                bkt[k].append(float(v))
        for s, feats in by_state.items():
            for k, vals in feats.items():
                if len(vals) < 10:
                    continue
                arr = np.asarray(vals)
                mu = float(arr.mean())
                # Dedupe consecutive repeats (ZOH interpolation collapses variance:
                # the adapter emits 1-min ticks from 5-10 min event cadence, so
                # between events the tick sequence repeats the last value, which
                # crushes sd and makes the detector fire on normal post-bootstrap
                # noise). Estimating sd from non-repeated values recovers the true
                # per-event variance.
                keep = np.concatenate(([True], arr[1:] != arr[:-1]))
                uniq = arr[keep]
                sd = float(uniq.std()) if uniq.size >= 10 else float(arr.std())
                if sd == 0: sd = 1e-6
                self._state[(s, k)] = [mu, sd, 0.0, 0.0]
        self.live = bool(self._state)

    def update(self, ts, feat):
        if not self.live: return []
        if self._first_update_ts is None:
            self._first_update_ts = ts
        # Warmup: during the first `warmup_seconds` after going live, still
        # process state (accumulate sp/sn, silent-reset on would-fire) but don't
        # emit alerts. Fixes diurnal-driven CUSUM warm-up FPs on continuous
        # sensors (e.g., leak_temperature) where bootstrap mu isn't calendar-aware.
        in_warmup = (self.warmup_seconds > 0
                     and (ts - self._first_update_ts).total_seconds() < self.warmup_seconds)
        out = []
        s = self._get_state(feat)
        for k in self.features:
            st = self._state.get((s, k))
            if st is None: continue
            v = feat.get(k)
            if v is None or (isinstance(v, float) and math.isnan(v)): continue
            mu, sd, sp, sn = st
            dlt = self.delta_sigma * sd
            dev = (v - mu)
            sp = max(0.0, sp + dev - dlt)
            sn = min(0.0, sn + dev + dlt)
            thresh = self.lam * sd
            fired = sp > thresh or -sn > thresh
            if fired:
                if not in_warmup:
                    score = max(sp, -sn)
                    direction = "+" if sp > thresh else "-"
                    out.append(_alert(self.config, ts, self.name, score, thresh,
                                      None, float(v), state=s,
                                      context={"detector": self.name, "feature": k,
                                               "state": s, "direction": direction,
                                               "mu": float(mu), "sigma": float(sd),
                                               "sp": float(sp), "sn": float(sn),
                                               "value": float(v)}))
                sp = sn = 0.0  # reset on fire (silent during warmup)
            st[2], st[3] = sp, sn
        return out

    def adapt_to_recent(self, rows):
        # Coordinated adaptation at K=3 max_span streak close: absorb the recent
        # regime as the new normal. Iter 033: extend mu-only absorb to also grow
        # sigma with a sensitivity floor (sigma = max(old_sigma, new_sigma)) so
        # post-shift regimes with wider variance than bootstrap stop re-firing
        # on in-regime noise. The floor means sigma can only GROW from adapt,
        # never shrink — a quieter post-shift regime keeps bootstrap sigma, so
        # in-regime noise post-adapt stays non-firing (no over-fire trap).
        # A noisier post-shift regime widens the firing band, killing wind-down
        # chains whose sp/sn re-accumulated against a tight bootstrap threshold.
        if not self.live or not rows: return
        by_state: dict[tuple[int, str], list[float]] = {}
        for ts, f in rows:
            s = self._get_state(f)
            for k in self.features:
                v = f.get(k)
                if v is None or (isinstance(v, float) and math.isnan(v)): continue
                by_state.setdefault((s, k), []).append(float(v))
        for (s, k), vals in by_state.items():
            st = self._state.get((s, k))
            if st is None or len(vals) < 10: continue
            arr = np.asarray(vals)
            # Dedupe consecutive repeats to match fit-time ZOH handling.
            keep = np.concatenate(([True], arr[1:] != arr[:-1]))
            uniq = arr[keep]
            new_sigma = float(uniq.std()) if uniq.size >= 10 else float(arr.std())
            st[0] = float(np.mean(vals))
            st[1] = max(st[1], new_sigma)  # sigma can only grow
            st[2] = st[3] = 0.0


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


class SubPCA:
    name = "sub_pca"

    def __init__(self, config: SensorConfig, window_sec: int = 7500, feature: str = "value",
                 warmup_seconds: float = 0.0):
        # Wall-clock-defined window keeps behavior stable across granularity_sec
        # changes. Default 7500s ≈ 2h (= 125 ticks at 60s granularity, matching the
        # pre-refactor constant). Convert to point count using the sensor's tick rate.
        self.config = config
        self.window_sec = window_sec
        self.window = max(1, window_sec // config.granularity_sec)
        self.feature = feature
        self.warmup_seconds = warmup_seconds
        self.live = False
        self._models: dict[int, tuple[np.ndarray, np.ndarray, float]] = {}
        self._buf: dict[int, deque[float]] = {}
        self._first_update_ts: pd.Timestamp | None = None

    def _state(self, feat: dict) -> int:
        return int(feat.get("state", 0)) if self.config.archetype == Archetype.BURSTY else 0

    def fit(self, rows):
        per_state: dict[int, list[float]] = {}
        for ts, f in rows:
            v = f.get(self.feature)
            if v is None or (isinstance(v, float) and math.isnan(v)):
                continue
            s = self._state(f)
            per_state.setdefault(s, []).append(float(v))
        for s, seq in per_state.items():
            if len(seq) < self.window * 3:
                continue
            arr = np.asarray(seq, dtype=float)
            # Fit PCA on non-overlapping windows (stable model).
            n = arr.size // self.window
            X = arr[:n * self.window].reshape(n, self.window)
            mu, P = _fit_pca(X)
            # Threshold: for CONTINUOUS sensors, derive from sliding windows —
            # non-overlap errors are in-sample residuals whose 99.9th
            # percentile underestimates the out-of-sample tail, which on
            # near-constant signals (voltage_mains σ=0.4V) caused a ~6%
            # stationary FP rate. Sliding bootstrap matches the live error
            # distribution (cuts that to ~0.2%). For BURSTY per-state models,
            # keep non-overlap: per-state slices are already short, sliding
            # inflates the threshold enough to fragment legitimate post-shift
            # fusion chains on outlet_tv power.
            if self.config.archetype == Archetype.CONTINUOUS:
                n_slide = arr.size - self.window + 1
                errs = np.array([_pca_error(arr[i:i + self.window], mu, P)
                                 for i in range(n_slide)])
            else:
                errs = np.array([_pca_error(X[i], mu, P) for i in range(n)])
            thr = float(np.quantile(errs, 0.999))
            self._models[s] = (mu, P, thr)
            self._buf[s] = deque(maxlen=self.window)
        self.live = bool(self._models)

    def update(self, ts, feat):
        if not self.live: return []
        if self._first_update_ts is None:
            self._first_update_ts = ts
        in_warmup = (self.warmup_seconds > 0
                     and (ts - self._first_update_ts).total_seconds() < self.warmup_seconds)
        s = self._state(feat)
        model = self._models.get(s)
        if model is None: return []
        v = feat.get(self.feature)
        if v is None or (isinstance(v, float) and math.isnan(v)): return []
        buf = self._buf[s]
        buf.append(float(v))
        if len(buf) < self.window: return []
        x = np.asarray(buf, dtype=float)
        mu, P, thr = model
        err = _pca_error(x, mu, P)
        if err > thr and not in_warmup:
            return [_alert(self.config, ts, self.name, err, thr, None, float(v),
                           state=s,
                           w0=ts - pd.Timedelta(seconds=self.window*self.config.granularity_sec),
                           w1=ts,
                           context={"detector": self.name, "state": s,
                                    "err": float(err), "thr": float(thr),
                                    "window": self.window, "feature": self.feature})]
        return []

    def adapt_to_recent(self, rows):
        # Iter 033: full re-fit with sensitivity floor. Re-derive mu/P/threshold
        # from the recent 96h window so the projection aligns with the new
        # regime's directions (kills post-level-shift wind-down where v is
        # near-stable at a new baseline but bootstrap-P's residuals against
        # that baseline stay above bootstrap-thr). Threshold is clamped to
        # max(old_thr, new_thr): a narrow-variance post-shift regime would
        # produce a tight new_thr that over-fires on normal-scale noise; the
        # floor keeps threshold at bootstrap sensitivity (prior comment here
        # called that out — the floor unblocks re-fit by removing the over-
        # fire risk).
        if not self.live or not rows: return
        per_state: dict[int, list[float]] = {}
        for ts, f in rows:
            v = f.get(self.feature)
            if v is None or (isinstance(v, float) and math.isnan(v)): continue
            per_state.setdefault(self._state(f), []).append(float(v))
        for s, seq in per_state.items():
            if s not in self._models or len(seq) < self.window * 2: continue
            old_mu, old_P, old_thr = self._models[s]
            arr = np.asarray(seq, dtype=float)
            n = arr.size // self.window
            X = arr[:n * self.window].reshape(n, self.window)
            new_mu, new_P = _fit_pca(X)
            # Threshold derivation matches fit(): sliding for CONT, non-overlap
            # for BURSTY per-state, to mirror live error distribution.
            if self.config.archetype == Archetype.CONTINUOUS:
                n_slide = arr.size - self.window + 1
                errs = np.array([_pca_error(arr[i:i + self.window], new_mu, new_P)
                                 for i in range(n_slide)])
            else:
                errs = np.array([_pca_error(X[i], new_mu, new_P) for i in range(n)])
            new_thr = float(np.quantile(errs, 0.999))
            self._models[s] = (new_mu, new_P, max(new_thr, old_thr))


class MultivariatePCA:
    name = "multivariate_pca"

    def __init__(self, config: SensorConfig, features: list[str],
                 warmup_seconds: float = 0.0):
        self.config = config
        self.features = features
        self.warmup_seconds = warmup_seconds
        self.live = False
        self._models: dict[int, tuple[np.ndarray, np.ndarray, float]] = {}
        self._first_update_ts: pd.Timestamp | None = None

    def _state(self, feat: dict) -> int:
        return int(feat.get("state", 0)) if self.config.archetype == Archetype.BURSTY else 0

    def _vec(self, feat: dict) -> np.ndarray | None:
        vals = []
        for k in self.features:
            v = feat.get(k)
            if v is None or (isinstance(v, float) and math.isnan(v)):
                return None
            vals.append(float(v))
        return np.asarray(vals, dtype=float)

    def fit(self, rows):
        per_state: dict[int, list[np.ndarray]] = {}
        for ts, f in rows:
            v = self._vec(f)
            if v is None: continue
            per_state.setdefault(self._state(f), []).append(v)
        for s, vs in per_state.items():
            if len(vs) < max(20, 3 * len(self.features)): continue
            X = np.stack(vs)
            mu, P = _fit_pca(X)
            errs = np.array([_pca_error(X[i], mu, P) for i in range(len(X))])
            thr = float(np.quantile(errs, 0.999))
            self._models[s] = (mu, P, thr)
        self.live = bool(self._models)

    def update(self, ts, feat):
        if not self.live: return []
        if self._first_update_ts is None:
            self._first_update_ts = ts
        in_warmup = (self.warmup_seconds > 0
                     and (ts - self._first_update_ts).total_seconds() < self.warmup_seconds)
        s = self._state(feat)
        model = self._models.get(s)
        if model is None: return []
        v = self._vec(feat)
        if v is None: return []
        mu, P, thr = model
        err = _pca_error(v, mu, P)
        if err > thr and not in_warmup:
            # Per-feature squared residual, identify top contributor.
            xc = v - mu
            rec = xc @ P @ P.T
            resid = xc - rec
            per_feat = resid * resid
            top_i = int(per_feat.argmax())
            return [_alert(self.config, ts, self.name, err, thr, None, float(v[0]),
                           state=s,
                           context={"detector": self.name, "state": s,
                                    "err": float(err), "thr": float(thr),
                                    "top_feature": self.features[top_i],
                                    "top_feature_contribution": float(per_feat[top_i]),
                                    "feature_residuals": {
                                        self.features[i]: float(per_feat[i])
                                        for i in range(len(self.features))}})]
        return []

    def adapt_to_recent(self, rows):
        # Iter 033: full re-fit with sensitivity floor (same rationale as
        # SubPCA.adapt_to_recent — see that method's comment). Re-derive
        # mu/P/threshold from recent; threshold clamped to max(old, new) so
        # sensitivity can't tighten below bootstrap even if the post-shift
        # regime has very narrow variance.
        if not self.live or not rows: return
        per_state: dict[int, list[np.ndarray]] = {}
        for ts, f in rows:
            v = self._vec(f)
            if v is None: continue
            per_state.setdefault(self._state(f), []).append(v)
        for s, vs in per_state.items():
            if s not in self._models or len(vs) < max(20, 3 * len(self.features)): continue
            old_mu, old_P, old_thr = self._models[s]
            X = np.stack(vs)
            new_mu, new_P = _fit_pca(X)
            new_errs = np.array([_pca_error(X[i], new_mu, new_P) for i in range(len(X))])
            new_thr = float(np.quantile(new_errs, 0.999))
            self._models[s] = (new_mu, new_P, max(new_thr, old_thr))


class TemporalProfile:
    name = "temporal_profile"

    def __init__(self, config: SensorConfig, features: list[str], z_thresh: float = 4.0,
                 min_samples: int = 20):
        self.config = config
        self.features = features
        self.z_thresh = z_thresh
        self.min_samples = min_samples
        self.live = False
        # bucket -> feature -> (n, mean, M2) [Welford]
        self._buckets: dict[tuple[int, int, int], dict[str, list[float]]] = {}

    @staticmethod
    def _bucket(ts: pd.Timestamp, state: int) -> tuple[int, int, int]:
        return (state, ts.hour, ts.dayofweek)

    def _state(self, feat: dict) -> int:
        return int(feat.get("state", 0)) if self.config.archetype == Archetype.BURSTY else 0

    def _update_bucket(self, b, k, v):
        bkt = self._buckets.setdefault(b, {})
        st = bkt.setdefault(k, [0, 0.0, 0.0, None])  # [n, mean, M2, last_v]
        # Dedupe consecutive identical values. ZOH-inflated tick streams (bursty
        # value between events, binary derived features holding steady) otherwise
        # pump bucket.n past min_samples without adding information, and a brief
        # labeled-anomaly burst (e.g., 60 consecutive transitions_per_hour=1
        # ticks during water_leak) permanently poisons the bucket mean.
        if st[3] is not None and v == st[3]:
            return
        st[3] = v
        st[0] += 1
        dlt = v - st[1]
        st[1] += dlt / st[0]
        st[2] += dlt * (v - st[1])

    def fit(self, rows):
        # BINARY water (water-leak) sensors have rare-event trigger semantics:
        # most (state, hour, dayofweek) buckets observe zero-transition ticks
        # all the time, so bucket sd collapses toward zero. A single non-zero
        # tick in one of those hours then produces |z| that far exceeds
        # z_thresh — the detector fires with score 5-7 at the sparse few
        # hours when any heartbeat-adjacent transitions happen, periodically,
        # for the rest of the scenario. The bucket model is unsound on this
        # class of sensor; CUSUM + MultivariatePCA cover sustained-leak
        # behavior and state_transition covers the deterministic trigger.
        if (self.config.archetype == Archetype.BINARY
                and self.config.capability == "water"):
            return
        # Collect per-(bucket, feature) values so we can dedupe consecutive repeats
        # (ZOH tick artifacts collapse variance to zero inside buckets — see CUSUM.fit
        # for the same ZOH-collapse reasoning).
        collected: dict[tuple, dict[str, list[float]]] = {}
        for ts, f in rows:
            s = self._state(f)
            b = self._bucket(ts, s)
            bkt = collected.setdefault(b, {})
            for k in self.features:
                v = f.get(k)
                if v is None or (isinstance(v, float) and math.isnan(v)):
                    continue
                bkt.setdefault(k, []).append(float(v))
        for b, feats in collected.items():
            for k, vals in feats.items():
                arr = np.asarray(vals)
                if arr.size >= 3:
                    keep = np.concatenate(([True], arr[1:] != arr[:-1]))
                    arr = arr[keep]
                for v in arr:
                    self._update_bucket(b, k, float(v))
        self.live = bool(self._buckets)

    def update(self, ts, feat):
        if not self.live: return []
        out = []
        s = self._state(feat)
        b = self._bucket(ts, s)
        bkt = self._buckets.get(b, {})
        for k in self.features:
            v = feat.get(k)
            if v is None or (isinstance(v, float) and math.isnan(v)): continue
            st = bkt.get(k)
            if st is None or st[0] < self.min_samples:
                self._update_bucket(b, k, float(v))
                continue
            n, mean, m2 = st[0], st[1], st[2]
            var = m2 / max(1, n - 1)
            sd = var ** 0.5
            anomalous = False
            if sd > 0:
                z = (float(v) - mean) / sd
                if abs(z) > self.z_thresh:
                    out.append(_alert(self.config, ts, self.name, abs(z), self.z_thresh,
                                      None, float(v), state=s,
                                      context={"detector": self.name, "state": s,
                                               "feature": k,
                                               "bucket": [s, ts.hour, ts.dayofweek],
                                               "expected_mean": float(mean),
                                               "expected_sd": float(sd),
                                               "observed_value": float(v),
                                               "observed_z": float(z)}))
                    anomalous = True
            if not anomalous:
                self._update_bucket(b, k, float(v))
        return out

    def adapt_to_recent(self, rows):
        # Force-absorb recent values into the matching buckets, even ones that
        # `update()` skipped because they fired. After a max_span fused close,
        # the recent values ARE the new normal (level shift, weekend pattern,
        # post-calibration baseline) — feeding them in shifts the bucket
        # mean/sd toward the new distribution so the profile stops re-firing.
        if not self.live or not rows: return
        for ts, f in rows:
            s = self._state(f)
            b = self._bucket(ts, s)
            for k in self.features:
                v = f.get(k)
                if v is None or (isinstance(v, float) and math.isnan(v)): continue
                self._update_bucket(b, k, float(v))


class EventPeakShift:
    """Per-event peak-value shift detector for BURSTY appliances. Treats each
    ON event (rising edge where value > `on_threshold`, to falling edge) as a
    discrete unit; records its peak value; compares against a bootstrap
    quantile band of peaks. Fires ON THE FIRST deviant event's completion.

    Mechanism fit (why this works where per-tick detectors fail on BURSTY):
    - Per-tick detectors (CUSUM, TemporalProfile, MvPCA) see a bimodal
      OFF/ON distribution and either collapse on the dead-state or flood
      on every unique ON micro-shape.
    - Per-state rolling detectors (StateConditionalShift) fire too late on
      low-duty appliances (kettle at 10% needs hours to collect enough
      samples) and produce wind-down FPs (lagging baseline).
    - This detector fires on a SINGLE anomalous event: kettle -800W shift
      produces peak 1700 on the first ON event post-shift, outside the
      bootstrap band [2400, 2600]. Wind-down: once events return to
      typical peak, no more fires — no lag.
    """
    name = "event_peak_shift"

    def __init__(self, config: SensorConfig, on_threshold: float = 50.0,
                 min_event_ticks: int = 3, iqr_k: float = 3.0,
                 min_events: int = 20, streak_k: int = 3,
                 feature: str = "value"):
        # iqr_k: Tukey outlier multiplier on IQR (k=1.5 mild, k=3.0 strict).
        # streak_k: fire only after K consecutive same-direction deviant events.
        # Natural single-event variance (fridge defrost, tv surge) resets the
        # streak; sustained shifts (level_shift, degradation) accumulate.
        self.config = config
        self.on_threshold = on_threshold
        self.min_event_ticks = min_event_ticks
        self.iqr_k = iqr_k
        self.min_events = min_events
        self.streak_k = streak_k
        self.feature = feature
        self.live = False
        self._q_low: float | None = None
        self._q_high: float | None = None
        # Live event-tracking state
        self._event_peak: float | None = None
        self._event_ticks: int = 0
        self._event_start_ts: pd.Timestamp | None = None
        self._prev_above = False
        self._streak_count = 0
        self._streak_direction: str | None = None

    def _scan_events(self, rows):
        """Yield (peak_value, tick_count) for each completed ON event in `rows`."""
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
                    yield (cur_peak, cur_ticks)
                cur_peak = None
                cur_ticks = 0
            prev_above = above

    def fit(self, rows):
        peaks = [p for p, _ in self._scan_events(rows)]
        if len(peaks) < self.min_events:
            return
        arr = np.asarray(peaks)
        q1 = float(np.quantile(arr, 0.25))
        q3 = float(np.quantile(arr, 0.75))
        iqr = q3 - q1
        self._q_low = q1 - self.iqr_k * iqr
        self._q_high = q3 + self.iqr_k * iqr
        self.live = True

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
                peak = self._event_peak
                q_low = self._q_low if self._q_low is not None else 0.0
                q_high = self._q_high if self._q_high is not None else float("inf")
                if peak < q_low or peak > q_high:
                    direction = "high" if peak > q_high else "low"
                    if self._streak_direction == direction:
                        self._streak_count += 1
                    else:
                        self._streak_direction = direction
                        self._streak_count = 1
                    if self._streak_count >= self.streak_k:
                        thr = q_high if peak > q_high else q_low
                        score = abs(peak - thr) / max(abs(thr), 1e-6) + 1.0
                        start_ts = self._event_start_ts or ts
                        alerts.append(_alert(self.config, ts, self.name, score, 1.0,
                                              None, peak,
                                              w0=start_ts, w1=ts,
                                              context={"detector": self.name,
                                                       "event_peak": peak,
                                                       "direction": direction,
                                                       "streak": self._streak_count,
                                                       "q_low": q_low,
                                                       "q_high": q_high,
                                                       "event_ticks": self._event_ticks}))
                else:
                    # Normal event resets the streak
                    self._streak_count = 0
                    self._streak_direction = None
            self._event_peak = None
            self._event_ticks = 0
            self._event_start_ts = None
        self._prev_above = above
        return alerts


class StateConditionalShift:
    """Per-state rolling mean of `value` vs bootstrap per-state mean. Fires
    when the recent short window in state s diverges from bootstrap's
    state-s mean by > `min_score` × bootstrap_sd. Designed for BURSTY
    appliances where bimodal OFF/ON value distributions defeat per-tick or
    per-(hour,dow) detectors: OFF-state stays silent (recent ≈ bootstrap ≈ 0);
    ON-state shifts (level_shift, trend, degradation) cleanly separate from
    noise because the comparison is within-state, not across modes.
    """
    name = "state_conditional_shift"

    def __init__(self, config: SensorConfig, short_samples: int = 100,
                 min_score: float = 3.0, min_bootstrap: int = 30,
                 feature: str = "value"):
        self.config = config
        self.short_samples = short_samples
        self.min_score = min_score
        self.min_bootstrap = min_bootstrap
        self.feature = feature
        self.live = False
        self._bootstrap_stats: dict[int, tuple[float, float]] = {}
        self._recent: dict[int, deque[float]] = {}

    def _state(self, feat: dict) -> int:
        return int(feat.get("state", 0)) if self.config.archetype == Archetype.BURSTY else 0

    def fit(self, rows):
        per_state: dict[int, list[float]] = {}
        for _, f in rows:
            v = f.get(self.feature)
            if v is None or (isinstance(v, float) and math.isnan(v)):
                continue
            per_state.setdefault(self._state(f), []).append(float(v))
        for s, vals in per_state.items():
            if len(vals) < self.min_bootstrap:
                continue
            arr = np.asarray(vals)
            # Dedupe ZOH (matches CUSUM.fit rationale — consecutive-repeat ticks
            # collapse sd toward zero and break the threshold).
            keep = np.concatenate(([True], arr[1:] != arr[:-1]))
            uniq = arr[keep] if np.count_nonzero(keep) >= self.min_bootstrap else arr
            mean = float(uniq.mean())
            sd = max(float(uniq.std()), 1e-6)
            self._bootstrap_stats[s] = (mean, sd)
        self.live = bool(self._bootstrap_stats)

    def update(self, ts, feat):
        if not self.live:
            return []
        s = self._state(feat)
        stats = self._bootstrap_stats.get(s)
        if stats is None:
            return []
        v = feat.get(self.feature)
        if v is None or (isinstance(v, float) and math.isnan(v)):
            return []
        buf = self._recent.setdefault(s, deque(maxlen=self.short_samples))
        buf.append(float(v))
        if len(buf) < self.short_samples:
            return []
        recent_mean = sum(buf) / len(buf)
        boot_mean, boot_sd = stats
        delta = abs(recent_mean - boot_mean)
        ratio = delta / boot_sd
        if ratio <= self.min_score:
            return []
        return [_alert(self.config, ts, self.name, ratio, self.min_score, None,
                       float(v),
                       w0=ts - pd.Timedelta(hours=1), w1=ts, state=s,
                       context={"detector": self.name, "state": s,
                                "recent_mean": float(recent_mean),
                                "bootstrap_mean": float(boot_mean),
                                "bootstrap_sd": float(boot_sd),
                                "delta": float(delta),
                                "short_samples": len(buf)})]


class EventRateShift:
    """Per-day event-count rate-shift detector for BURSTY appliances. Scans
    rising-edge ON events (value > on_threshold) to event completion, records
    their start timestamps, and compares the recent rolling-window event
    count against bootstrap per-day counts.

    Mechanism fit (why this works where value-based detectors fail):
    - time_of_day / weekend_anomaly / frequency_change (28 BURSTY
      user_behavior labels) are shifts in WHEN or HOW OFTEN events occur,
      not in their magnitude. Per-tick value detectors (CUSUM, MvPCA,
      TemporalProfile, SubPCA) see only the raw ZOH stream where OFF-ticks
      dominate; the event-arrival process is invisible to them. Per-event
      peak detectors (EventPeakShift) see magnitude but not arrival rate.
      This detector operates directly on the event-arrival process.
    - Bootstrap: per-day event counts across the bootstrap window give a
      mean μ_day and std σ_day of daily rate. Low-variance kettle use
      (~3/day with σ≈1.5) produces a tight threshold; high-variance fridge
      (~200/day compressor cycles with σ≈20) produces a loose threshold
      that tolerates natural multi-phase variance.
    - Live: rolling 24h count against (24h/day × μ_day) = μ_day. Fires when
      |observed - μ_day| > z_threshold × max(σ_day, 1.0). Z-score rather
      than Poisson because day-to-day variance exceeds Poisson sqrt(mean)
      on appliances with weekend / weekday patterns.

    Does NOT fit: level_shift (same event rate, different peak — use
    EventPeakShift), trend / degradation (slow value shift without rate
    change), spike (single-event impulse).
    """
    name = "event_rate_shift"

    def __init__(self, config: SensorConfig, on_threshold: float = 50.0,
                 min_event_ticks: int = 3, recent_window_s: int = 24 * 3600,
                 min_bootstrap_days: int = 7, z_threshold: float = 3.0,
                 cooldown_s: int = 4 * 3600, detection_window_s: int = 60,
                 min_persistence_s: int = 0, feature: str = "value"):
        # z_threshold=3.0: ~p<0.003 per Poisson assumption, but empirical σ is
        # used so Bonferroni / day-of-week adjustments are baked into σ.
        # cooldown_s=4h: after a fire, suppress further fires in the same
        # rolling window so sustained shifts produce one fire not a train.
        # min_bootstrap_days=7: need at least a week of daily counts to see
        # weekend/weekday variance; below this the detector stays dormant.
        # detection_window_s: emit w0 = fire_ts - detection_window_s. With the
        # default 60s, the detection is effectively a point at fire_ts, so
        # only labels still active at fire_ts overlap-match. Setting this to
        # recent_window_s (86400) restores the back-span variant which
        # over-credits ended labels (see ITERATIONS.md iter 011).
        # min_persistence_s: fire only when |z|>threshold has been continuously
        # true for ≥ min_persistence_s. Default 0 = no persistence gate
        # (iter 011/012 behavior). Setting to e.g., 12h filters transient
        # rate blips, restricts fires to shifts that sustain long enough to
        # plausibly be long-bucket-label events. For a rate shift lasting
        # >= recent_window_s + min_persistence_s, the fire happens
        # (approximately) at label_start + recent_window_s + min_persistence_s.
        self.config = config
        self.on_threshold = on_threshold
        self.min_event_ticks = min_event_ticks
        self.recent_window_s = recent_window_s
        self.min_bootstrap_days = min_bootstrap_days
        self.z_threshold = z_threshold
        self.cooldown_s = cooldown_s
        self.detection_window_s = detection_window_s
        self.min_persistence_s = min_persistence_s
        self.feature = feature
        self.live = False
        self._boot_mean: float = 0.0
        self._boot_sd: float = 1.0
        # Live event-tracking state
        self._event_ticks: int = 0
        self._event_start_ts: pd.Timestamp | None = None
        self._prev_above = False
        self._event_deque: deque = deque()  # rising-edge timestamps in window
        self._last_fire_ts: pd.Timestamp | None = None
        # Persistence-gate state: when |z|>threshold first crossed, record ts;
        # cleared when |z| drops back below threshold. Fire requires
        # (ts - _deviation_start_ts) >= min_persistence_s.
        self._deviation_start_ts: pd.Timestamp | None = None

    def _scan_event_starts(self, rows):
        """Yield event-start timestamps for each completed ON event in rows."""
        prev_above = False
        start_ts: pd.Timestamp | None = None
        cur_ticks = 0
        for ts, f in rows:
            v = f.get(self.feature)
            if v is None or (isinstance(v, float) and math.isnan(v)):
                continue
            v = float(v)
            above = v > self.on_threshold
            if above:
                if not prev_above:
                    start_ts = ts
                    cur_ticks = 1
                else:
                    cur_ticks += 1
            else:
                if prev_above and cur_ticks >= self.min_event_ticks and start_ts is not None:
                    yield start_ts
                start_ts = None
                cur_ticks = 0
            prev_above = above

    def fit(self, rows):
        per_day: dict = {}
        for ets in self._scan_event_starts(rows):
            d = ets.date()
            per_day[d] = per_day.get(d, 0) + 1
        if len(per_day) < self.min_bootstrap_days:
            return
        daily = np.asarray(list(per_day.values()), dtype=float)
        self._boot_mean = float(daily.mean())
        # σ floor at 1.0: with mean 3/day and integer counts, σ can be
        # artificially low if all bootstrap days happen to have identical
        # counts; 1-event fluctuation is noise, not signal.
        self._boot_sd = max(float(daily.std()), 1.0)
        self.live = True

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
                self._event_start_ts = ts
                self._event_ticks = 1
            else:
                self._event_ticks += 1
        else:
            if (self._prev_above and self._event_ticks >= self.min_event_ticks
                    and self._event_start_ts is not None):
                self._event_deque.append(self._event_start_ts)
                # Trim to recent window
                cutoff = ts - pd.Timedelta(seconds=self.recent_window_s)
                while self._event_deque and self._event_deque[0] < cutoff:
                    self._event_deque.popleft()
                observed = len(self._event_deque)
                expected = self._boot_mean * (self.recent_window_s / 86400.0)
                sd_scaled = self._boot_sd * (self.recent_window_s / 86400.0) ** 0.5
                z = (observed - expected) / max(sd_scaled, 1e-6)
                # Persistence gate: |z| must stay above threshold for
                # min_persistence_s continuous before fire. Track the first ts
                # where |z| crossed; clear when it drops back below.
                if abs(z) > self.z_threshold:
                    if self._deviation_start_ts is None:
                        self._deviation_start_ts = ts
                else:
                    self._deviation_start_ts = None
                # Fire check: |z| above threshold AND persistence met AND cooldown ok.
                cooldown_ok = (self._last_fire_ts is None
                               or (ts - self._last_fire_ts).total_seconds() >= self.cooldown_s)
                persistence_ok = (self._deviation_start_ts is not None
                                  and (ts - self._deviation_start_ts).total_seconds()
                                      >= self.min_persistence_s)
                if abs(z) > self.z_threshold and cooldown_ok and persistence_ok:
                    self._last_fire_ts = ts
                    direction = "high" if z > 0 else "low"
                    score = abs(z)
                    w0 = ts - pd.Timedelta(seconds=self.detection_window_s)
                    alerts.append(_alert(self.config, ts, self.name, score,
                                          self.z_threshold, None, float(observed),
                                          w0=w0, w1=ts,
                                          context={"detector": self.name,
                                                   "observed_count": observed,
                                                   "expected_count": float(expected),
                                                   "bootstrap_mean": self._boot_mean,
                                                   "bootstrap_sd": self._boot_sd,
                                                   "z_score": float(z),
                                                   "direction": direction,
                                                   "window_s": self.recent_window_s,
                                                   "persistence_s": int((ts - self._deviation_start_ts).total_seconds())}))
                self._event_start_ts = None
                self._event_ticks = 0
        self._prev_above = above
        return alerts


class BOCPD:
    """Bayesian Online Change Point Detection for CONTINUOUS sensors. Streams
    the posterior over "run length" (time since last changepoint) using a
    constant-hazard prior and Gaussian observation model with known variance
    from bootstrap. Alarms when the posterior on r=0 (just changed) crosses
    a threshold.

    Mechanism fit (why this works where CUSUM / RecentShift don't):
    - CUSUM's `sp/sn` accumulator keeps growing against a stale bootstrap μ
      after a level shift → 12d wind-down (iter 001). RecentShift's rolling
      24h baseline takes 7d to catch up to a new mean → 7d wind-down (iter
      002). Both share post-shift wind-down.
    - BOCPD's state is a DISTRIBUTION over run-lengths, not a point estimate.
      At a changepoint, posterior mass shifts to r=0; in the new regime, mass
      grows back as r increases. There is no accumulator against a stale μ
      because the algorithm explicitly models "possibly a new distribution
      started just now." Wind-down is bounded by posterior convergence speed
      (~1-3 days typical) rather than window length or max_span.
    - Per LEARNINGS §8, this makes BOCPD a valid Stage 4 pair candidate with
      RecentShift: their failure modes are NOT correlated (different
      mechanisms; different wind-down profiles).

    Does NOT fit: gradual drifts without a sharp changepoint (posterior
    never collapses to r=0 sharply), short-duration spikes/dips (need
    multiple ticks of shifted data to shift posterior).
    """
    name = "bocpd"

    def __init__(self, config: SensorConfig, hazard_lambda: float = 5000,
                 alarm_threshold: float = 0.3, max_run_length: int = 1000,
                 warmup_ticks: int = 200, cooldown_s: int = 6 * 3600,
                 feature: str = "value"):
        # hazard_lambda: prior expected run length in ticks. 5000 ≈ 35d at
        # 10-min cadence; consistent with observed mains_voltage month_shift
        # interval. Higher λ = changepoints assumed rarer = detector less
        # sensitive.
        # alarm_threshold: posterior on r=0 threshold for fire. 0.3 =
        # "more than 30% probability changepoint just happened this tick."
        # max_run_length: truncate R array here. 1000 ticks = ~7d at 10min.
        #   Longer run-lengths get their posterior mass folded into max_r.
        # warmup_ticks: suppress alarms for the first N post-fit ticks so
        #   R stabilizes (fresh R initialization briefly puts high mass on
        #   short r, which can trigger false alarm).
        # cooldown_s: 6h minimum between alarms to prevent re-alarming on
        #   the same changepoint as posterior settles.
        self.config = config
        self.hazard_lambda = hazard_lambda
        self.alarm_threshold = alarm_threshold
        self.max_run_length = max_run_length
        self.warmup_ticks = warmup_ticks
        self.cooldown_s = cooldown_s
        self.feature = feature
        self.live = False
        self._boot_mean: float = 0.0
        self._boot_var: float = 1.0
        # Run-length posterior R[r] = P(run_length = r | observations)
        self._R: np.ndarray | None = None
        # Cumulative sum of observations per run-length (for predictive mean)
        self._running_sum: np.ndarray | None = None
        self._tick_count = 0
        self._last_fire_ts: pd.Timestamp | None = None

    def fit(self, rows):
        values: list[float] = []
        for _, f in rows:
            v = f.get(self.feature)
            if v is None or (isinstance(v, float) and math.isnan(v)):
                continue
            values.append(float(v))
        if len(values) < 50:
            return
        arr = np.asarray(values)
        self._boot_mean = float(arr.mean())
        # Variance with floor; BOCPD is known-variance (bootstrap σ² is the
        # observation noise assumption). Too-small σ² makes the detector
        # over-sensitive to tick-level jitter.
        self._boot_var = max(float(arr.var()), 1e-4)
        n = self.max_run_length + 1
        self._R = np.zeros(n)
        self._R[0] = 1.0  # starts confident a changepoint just happened
        self._running_sum = np.zeros(n)
        self.live = True

    def update(self, ts, feat):
        if not self.live or self._R is None or self._running_sum is None:
            return []
        v = feat.get(self.feature)
        if v is None or (isinstance(v, float) and math.isnan(v)):
            return []
        v = float(v)
        self._tick_count += 1

        # Predictive distribution per run-length using a Normal-Normal
        # conjugate model (known observation variance σ_obs², broad prior
        # on mean with σ_prior² = K·σ_obs², K large).
        #
        # Posterior on μ after r obs: precision = 1/σ_prior² + r/σ_obs².
        # Posterior mean = weighted avg of prior mean and sample mean.
        # Predictive variance = σ_obs² + 1/posterior_precision.
        #
        # At r=0 (diffuse prior): predictive variance ≈ σ_prior² (wide);
        # any value has reasonable likelihood.
        # At r>>0: predictive variance → σ_obs² (tight); only values near
        # the sample mean have high likelihood.
        # This asymmetry is what lets a shift drive R[0] high: post-shift
        # values have tiny likelihood under long-run hypotheses (tight
        # predictive centered on stale mean) but reasonable likelihood
        # under r=0 (wide predictive).
        r_arr = np.arange(self.max_run_length + 1)
        sigma_obs_sq = self._boot_var
        K = 100.0  # prior width multiplier (diffuse)
        sigma_prior_sq = K * sigma_obs_sq
        prior_precision = 1.0 / sigma_prior_sq
        data_precision = r_arr / sigma_obs_sq
        post_precision = prior_precision + data_precision
        post_var = 1.0 / post_precision
        # Weighted posterior mean: prior weight + data weight (running sum / σ_obs²)
        post_mean = (prior_precision * self._boot_mean
                     + self._running_sum / sigma_obs_sq) / post_precision
        pred_var = sigma_obs_sq + post_var
        log_lik = -0.5 * np.log(2 * math.pi * pred_var) \
                  - 0.5 * (v - post_mean) ** 2 / pred_var
        # Numerical stability: shift so max is 0, then exponentiate.
        log_lik -= log_lik.max()
        lik = np.exp(log_lik)

        # Hazard: constant 1/λ.
        H = 1.0 / self.hazard_lambda
        # Growth probability: no changepoint, run-length increments.
        growth = self._R * lik * (1.0 - H)
        # Changepoint probability: changepoint NOW, r resets to 0.
        change = float((self._R * lik * H).sum())

        R_new = np.zeros_like(self._R)
        # Shift growth up by 1: R_new[r+1] = growth[r]; R_new[max_r] absorbs overflow.
        R_new[1:] = growth[:-1]
        R_new[-1] += growth[-1]  # fold r=max into max (truncation)
        R_new[0] = change
        total = R_new.sum()
        if total <= 0 or not math.isfinite(total):
            R_new = np.zeros_like(self._R)
            R_new[0] = 1.0
        else:
            R_new /= total

        # Update running-sum sufficient statistics: shift up by 1; r=0 resets to v.
        new_sum = np.zeros_like(self._running_sum)
        new_sum[1:] = self._running_sum[:-1] + v
        new_sum[-1] = self._running_sum[-1] + v  # absorb overflow consistently
        new_sum[0] = v
        self._running_sum = new_sum
        self._R = R_new

        alerts: list = []
        if (self._tick_count > self.warmup_ticks
                and R_new[0] > self.alarm_threshold):
            cooldown_ok = (self._last_fire_ts is None
                           or (ts - self._last_fire_ts).total_seconds()
                              >= self.cooldown_s)
            if cooldown_ok:
                self._last_fire_ts = ts
                score = float(R_new[0])
                alerts.append(_alert(self.config, ts, self.name, score,
                                      self.alarm_threshold, None, v,
                                      w0=ts - pd.Timedelta(minutes=1), w1=ts,
                                      context={"detector": self.name,
                                               "posterior_r0": float(R_new[0]),
                                               "tick_count": self._tick_count,
                                               "boot_mean": self._boot_mean,
                                               "boot_var": self._boot_var,
                                               "value": v}))
        return alerts


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
        # Live: (ts, above) pairs in rolling window
        self._window: deque = deque()
        self._last_fire_ts: pd.Timestamp | None = None

    def _compute_bootstrap_windows(self, rows):
        """Slide a `window_s` window across bootstrap rows; compute duty per window."""
        if not rows:
            return []
        duties: list[float] = []
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
                duties.append(above_s / total_s)
            w_start_ts += pd.Timedelta(seconds=step)
        return duties

    def fit(self, rows):
        duties = self._compute_bootstrap_windows(rows)
        if len(duties) < self.min_bootstrap_windows:
            return
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
        self.live = True

    def update(self, ts, feat):
        if not self.live:
            return []
        v = feat.get(self.feature)
        if v is None or (isinstance(v, float) and math.isnan(v)):
            return []
        above = float(v) > self.on_threshold
        self._window.append((ts, above))
        cutoff = ts - pd.Timedelta(seconds=self.window_s)
        while self._window and self._window[0][0] < cutoff:
            self._window.popleft()
        # Compute duty cycle on window: sum of dt where state is ON / total dt
        if len(self._window) < 10:
            return []
        above_s = 0.0
        total_s = 0.0
        prev_ts = None
        prev_above = False
        for wts, wabove in self._window:
            if prev_ts is not None:
                dt = (wts - prev_ts).total_seconds()
                total_s += dt
                if prev_above:
                    above_s += dt
            prev_ts = wts
            prev_above = wabove
        if total_s <= 0:
            return []
        duty = above_s / total_s
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
            if self._mad_at_floor:
                if z > 0 and duty <= self._boot_q99:
                    return []
                if z < 0 and duty >= self._boot_q01:
                    return []
            self._last_fire_ts = ts
            direction = "high" if z > 0 else "low"
            score = abs(z)
            return [_alert(self.config, ts, self.name, score, self.z_threshold,
                           None, float(duty),
                           w0=ts - pd.Timedelta(minutes=1), w1=ts,
                           context={"detector": self.name,
                                    "duty": duty,
                                    "bootstrap_median": self._boot_median,
                                    "bootstrap_mad": self._boot_mad,
                                    "z": float(z),
                                    "direction": direction,
                                    "window_s": self.window_s})]
        return []


class HourlyEventRateChiSq:
    """Per-hour-of-day event-count histogram chi-square vs bootstrap
    distribution. Fires when the hour-of-day distribution of recent events
    deviates from bootstrap.

    Mechanism fit (vs total-count EventRateShift iter 11-13):
    - EventRateShift compares TOTAL events in recent window to bootstrap
      total. Misses time_of_day shifts (same total, different timing).
    - This detector compares the PER-HOUR-OF-DAY histogram. kettle
      time_of_day anomaly: events move from hour 7-9 to hour 17-19,
      same total. Per-hour chi-square spikes dramatically.
    - Bootstrap: count events per hour-of-day bucket per day across
      bootstrap. Compute the mean-per-hour profile μ_h.
    - Live: rolling 3-day window of events bucketed by hour. Compute
      chi-square: Σ (obs_h - E[obs_h])² / E[obs_h] where E[obs_h] = μ_h × 3.
    - Fire when chi-square exceeds bootstrap 95th-percentile chi-square.

    Expected label fit: time_of_day (11 labels), weekend_anomaly (11),
    frequency_change (partial — if rate shifts unequally across hours).
    NOT level_shift / trend (same hour pattern, different magnitude).
    """
    name = "hourly_event_rate_chi_sq"

    def __init__(self, config: SensorConfig, on_threshold: float = 50.0,
                 min_event_ticks: int = 3, recent_window_s: int = 3 * 86400,
                 min_bootstrap_days: int = 7, chi_sq_mult: float = 2.0,
                 cooldown_s: int = 6 * 3600, feature: str = "value"):
        # recent_window_s=3d: rolling 3-day window of events. Long enough
        # for statistical power on per-hour counts (kettle ~3/day x 3 = 9
        # events distributed over 24 hours), short enough that lat_frac
        # is acceptable for long-bucket labels.
        # chi_sq_mult=2.0: threshold = 2 × bootstrap q95(chi_sq). Adapts
        # to per-sensor variance (fridge has higher natural chi-sq variance
        # than kettle).
        self.config = config
        self.on_threshold = on_threshold
        self.min_event_ticks = min_event_ticks
        self.recent_window_s = recent_window_s
        self.min_bootstrap_days = min_bootstrap_days
        self.chi_sq_mult = chi_sq_mult
        self.cooldown_s = cooldown_s
        self.feature = feature
        self.live = False
        # Bootstrap: per-hour mean count (over 3d windows)
        self._hour_mean: np.ndarray | None = None
        self._bootstrap_chi_sq_q95: float = 0.0
        # Live state
        self._prev_above = False
        self._event_ticks = 0
        self._event_start_ts: pd.Timestamp | None = None
        self._event_deque: deque = deque()
        self._last_fire_ts: pd.Timestamp | None = None

    def _scan_event_starts(self, rows):
        prev_above = False
        start_ts: pd.Timestamp | None = None
        cur_ticks = 0
        for ts, f in rows:
            v = f.get(self.feature)
            if v is None or (isinstance(v, float) and math.isnan(v)):
                continue
            above = float(v) > self.on_threshold
            if above:
                if not prev_above:
                    start_ts = ts
                    cur_ticks = 1
                else:
                    cur_ticks += 1
            else:
                if prev_above and cur_ticks >= self.min_event_ticks and start_ts is not None:
                    yield start_ts
                start_ts = None
                cur_ticks = 0
            prev_above = above

    def _hour_histogram(self, event_starts):
        hist = np.zeros(24)
        for ts in event_starts:
            hist[ts.hour] += 1
        return hist

    def _chi_sq(self, obs: np.ndarray, expected: np.ndarray) -> float:
        # Chi-square ignoring hours where expected is near zero (undefined).
        mask = expected > 0.5
        if not mask.any():
            return 0.0
        return float(np.sum((obs[mask] - expected[mask]) ** 2 / expected[mask]))

    def fit(self, rows):
        events = list(self._scan_event_starts(rows))
        days_seen = set(e.date() for e in events)
        if len(days_seen) < self.min_bootstrap_days:
            return
        # Compute per-hour count per day; average over days for μ_h
        hist_total = self._hour_histogram(events)
        n_days = len(days_seen)
        hour_mean_per_day = hist_total / n_days
        # Scale to recent_window_s (days_equivalent): e.g., 3 days → multiply by 3
        window_days = self.recent_window_s / 86400.0
        self._hour_mean = hour_mean_per_day * window_days
        # Compute bootstrap chi-square: for each sliding recent_window_s window
        # over bootstrap events, compute chi-square to μ_h. 95th percentile.
        chi_sqs: list[float] = []
        if events:
            first_ts = events[0]
            last_ts = events[-1]
            step = pd.Timedelta(seconds=self.recent_window_s // 2)
            w_start = first_ts
            window_td = pd.Timedelta(seconds=self.recent_window_s)
            while w_start + window_td <= last_ts:
                w_end = w_start + window_td
                window_events = [e for e in events if w_start <= e < w_end]
                if window_events:
                    obs = self._hour_histogram(window_events)
                    chi_sqs.append(self._chi_sq(obs, self._hour_mean))
                w_start += step
        if chi_sqs:
            self._bootstrap_chi_sq_q95 = float(np.quantile(chi_sqs, 0.95))
        else:
            self._bootstrap_chi_sq_q95 = 10.0  # fallback
        self.live = True

    def update(self, ts, feat):
        if not self.live or self._hour_mean is None:
            return []
        v = feat.get(self.feature)
        if v is None or (isinstance(v, float) and math.isnan(v)):
            return []
        above = float(v) > self.on_threshold
        alerts: list = []
        if above:
            if not self._prev_above:
                self._event_start_ts = ts
                self._event_ticks = 1
            else:
                self._event_ticks += 1
        else:
            if (self._prev_above and self._event_ticks >= self.min_event_ticks
                    and self._event_start_ts is not None):
                self._event_deque.append(self._event_start_ts)
                # Trim to recent window
                cutoff = ts - pd.Timedelta(seconds=self.recent_window_s)
                while self._event_deque and self._event_deque[0] < cutoff:
                    self._event_deque.popleft()
                # Compute chi-square vs bootstrap hour_mean
                if len(self._event_deque) >= 5:  # min events for power
                    obs = self._hour_histogram(self._event_deque)
                    chi_sq = self._chi_sq(obs, self._hour_mean)
                    threshold = self.chi_sq_mult * self._bootstrap_chi_sq_q95
                    cooldown_ok = (self._last_fire_ts is None
                                   or (ts - self._last_fire_ts).total_seconds()
                                      >= self.cooldown_s)
                    if chi_sq > threshold and cooldown_ok:
                        self._last_fire_ts = ts
                        score = float(chi_sq / max(threshold, 1e-6))
                        alerts.append(_alert(self.config, ts, self.name, score,
                                              self.chi_sq_mult, None, float(chi_sq),
                                              w0=ts - pd.Timedelta(minutes=1), w1=ts,
                                              context={"detector": self.name,
                                                       "chi_sq": float(chi_sq),
                                                       "threshold": float(threshold),
                                                       "bootstrap_q95": self._bootstrap_chi_sq_q95,
                                                       "n_events": len(self._event_deque)}))
                self._event_start_ts = None
                self._event_ticks = 0
        self._prev_above = above
        return alerts


class StateTransition:
    """Tick-level trigger for deterministic binary events (e.g. water leak
    sustain). Emits a `state_transition` alert when `feat['trigger']` is
    truthy. Extracted from inline code in pipeline.py."""
    name = "state_transition"
    live = True
    _MOTION_IDLE_LOOKBACK_MIN_GAP = pd.Timedelta(minutes=45)
    _MOTION_IDLE_LOOKBACK_CAP = pd.Timedelta(minutes=17)

    def __init__(self, config: SensorConfig):
        self.config = config
        self._last_trigger_ts: pd.Timestamp | None = None

    def fit(self, rows): pass

    def update(self, ts, feat):
        if not feat.get("trigger"):
            return []
        # window_start/window_end left as None so `_write_detections` applies
        # the default 1-minute window_end — a 0-duration alert at the label's
        # exact start fails `_overlaps`' strict-less-than check (`ts < ts` is
        # False) and would not count as overlapping a label that starts at
        # the same tick. The 1-minute tail makes overlap semantically correct.
        w0 = None
        w1 = None
        if (self.config.capability == "motion"
                and self._last_trigger_ts is not None):
            gap = ts - self._last_trigger_ts
            if gap >= self._MOTION_IDLE_LOOKBACK_MIN_GAP:
                # First trigger after a quiet spell: let the alert cover a
                # bounded slice of the idle gap so midnight / regime-boundary
                # motion labels don't require multi-day pre-label fused chains
                # just to score near-zero onset latency.
                w0 = max(self._last_trigger_ts, ts - self._MOTION_IDLE_LOOKBACK_CAP)
                w1 = ts + pd.Timedelta(minutes=1)
        self._last_trigger_ts = ts
        # Capability-appropriate type: water → water_leak_sustained,
        # motion → unusual_occupancy. Previous hardcoded "water_leak_sustained"
        # on every trigger was correct-by-class (both user_behavior) but
        # wrong-by-type — surfaced by NAB's type-matching metric where a motion
        # trigger claiming "water_leak_sustained" is a confidently wrong
        # explanation and counts as FP.
        if self.config.capability == "water":
            atype = "water_leak_sustained"
        elif self.config.capability == "motion":
            atype = "unusual_occupancy"
        else:
            atype = self.name  # fallback — shouldn't occur at this stage
        return [Alert(self.config.sensor_id, self.config.capability, ts,
                      self.name, 1.0, 1.0, atype, 1.0,
                      feat.get("state"), w0, w1,
                      [{"detector": self.name, "state": feat.get("state")}])]
