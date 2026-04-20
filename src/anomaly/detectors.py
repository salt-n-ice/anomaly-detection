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
        # Coordinated adaptation: when a fused chunk closes due to prolonged firing,
        # absorb the recent baseline into mu so we stop firing on the new normal.
        # Sigma is preserved (anomalous data inflates variance — keeping the bootstrap
        # sigma maintains sensitivity for the next genuine deviation).
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
            st[0] = float(np.mean(vals))
            st[2] = st[3] = 0.0


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

    def __init__(self, config: SensorConfig, window: int = 125, feature: str = "value",
                 warmup_seconds: float = 0.0):
        self.config = config
        self.window = window
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
        # Shift mu (the window centroid) to the recent baseline, but KEEP the
        # projection P and threshold from bootstrap. This recenters the model
        # on the new normal without re-deriving sensitivity — refitting P/thr
        # on narrow recent variance creates tight thresholds that over-fire.
        if not self.live or not rows: return
        per_state: dict[int, list[float]] = {}
        for ts, f in rows:
            v = f.get(self.feature)
            if v is None or (isinstance(v, float) and math.isnan(v)): continue
            per_state.setdefault(self._state(f), []).append(float(v))
        for s, seq in per_state.items():
            if s not in self._models or len(seq) < self.window * 2: continue
            _, P, thr = self._models[s]
            arr = np.asarray(seq, dtype=float)
            n = arr.size // self.window
            X = arr[:n * self.window].reshape(n, self.window)
            new_mu = X.mean(axis=0)
            self._models[s] = (new_mu, P, thr)


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
        # Shift centroid mu to the recent mean, but KEEP P and threshold —
        # same rationale as SubPCA.adapt_to_recent above.
        if not self.live or not rows: return
        per_state: dict[int, list[np.ndarray]] = {}
        for ts, f in rows:
            v = self._vec(f)
            if v is None: continue
            per_state.setdefault(self._state(f), []).append(v)
        for s, vs in per_state.items():
            if s not in self._models or len(vs) < max(20, 3 * len(self.features)): continue
            _, P, thr = self._models[s]
            new_mu = np.mean(np.stack(vs), axis=0)
            self._models[s] = (new_mu, P, thr)


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
