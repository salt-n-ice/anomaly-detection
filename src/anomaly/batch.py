from __future__ import annotations
import numpy as np
import pandas as pd
from .core import SensorConfig, Archetype, Alert


def _znorm(W: np.ndarray) -> np.ndarray:
    mu = W.mean(axis=1, keepdims=True)
    sd = W.std(axis=1, keepdims=True)
    sd = np.where(sd < 1e-8, 1.0, sd)
    return (W - mu) / sd


def _matrix_profile(x: np.ndarray, m: int) -> np.ndarray:
    n = x.size - m + 1
    if n <= 1: return np.zeros(n)
    idx = np.arange(m)[None, :] + np.arange(n)[:, None]
    W = x[idx]
    Wn = _znorm(W).astype(np.float32)
    G = Wn @ Wn.T                                   # (n, n) gram matrix
    D2 = 2.0 * m - 2.0 * G                          # squared distances
    ez = max(1, m // 4)
    for i in range(n):
        lo = max(0, i - ez); hi = min(n, i + ez + 1)
        D2[i, lo:hi] = np.inf
    return np.sqrt(np.maximum(D2.min(axis=1), 0.0))


_MAX_MP_POINTS = 15_000  # ~10.4 days at 1-min granularity; caps gram matrix at ~800 MB


def matrix_profile_discords(config: SensorConfig, series: list[tuple[pd.Timestamp, float]],
                             window: int = 360, top_k: int = 3) -> list[Alert]:
    if config.archetype == Archetype.BINARY:
        return []
    ts_arr = [t for t, _ in series]
    vals = np.asarray([v for _, v in series], dtype=float)
    vals = np.where(np.isnan(vals), np.nanmean(vals) if np.isfinite(np.nanmean(vals)) else 0.0, vals)
    if vals.size > _MAX_MP_POINTS:
        ts_arr = ts_arr[-_MAX_MP_POINTS:]
        vals = vals[-_MAX_MP_POINTS:]
    if vals.size < window * 3:
        return []
    mp = _matrix_profile(vals, window)
    thr = mp.mean() + 5 * mp.std()  # tightened from 3 — leak scenario produced 4 unmatched MP FPs at 3*std
    idx_sorted = np.argsort(mp)[::-1]
    out: list[Alert] = []
    used_ez = window
    last_idxs: list[int] = []
    for i in idx_sorted:
        if mp[i] <= thr: break
        if any(abs(i - j) < used_ez for j in last_idxs): continue
        last_idxs.append(int(i))
        if len(last_idxs) > top_k: break
        w0 = ts_arr[int(i)]
        w1 = ts_arr[min(len(ts_arr) - 1, int(i) + window - 1)]
        out.append(Alert(config.sensor_id, config.capability, w0, "matrix_profile",
                         float(mp[i]), float(thr), None, float(vals[int(i)]), None, w0, w1))
    return out
