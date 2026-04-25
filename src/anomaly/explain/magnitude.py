"""Magnitude extraction + per-detector context synthesis.

`extract_magnitude` produces the signed excursion (baseline / peak / delta /
delta_pct) for an alert, preferring CUSUM's tracked mu when available and
falling back through 2h / 24h / 7d pre-window medians. `_synth_detector_context`
rebuilds best-effort per-detector context dicts when the live ones were
stripped (CSV roundtrip path).
"""
from __future__ import annotations
import pandas as pd

from ..core import Alert


def _find_ctx(alert: Alert, detector: str) -> dict | None:
    """Return the first context dict for ``detector`` (or None)."""
    if not alert.context:
        return None
    for ctx in alert.context:
        if ctx.get("detector") == detector:
            return ctx
    return None


def extract_magnitude(alert: Alert, events: pd.DataFrame) -> dict:
    """Signed magnitude of the anomalous excursion relative to a baseline.

    Prefers ``cusum.mu`` when present (detector-native reference). Falls back to
    the median of the 2h pre-window for the alert's sensor.

    Contract: ``events["timestamp"]`` MUST already be UTC datetime64. The
    parse is lifted to ``bundle._ensure_utc_timestamps`` so the batch CSV
    path doesn't pay it 3× per alert.
    """
    w0 = alert.window_start or alert.timestamp
    w1 = alert.window_end or alert.timestamp
    sub = events[events["sensor_id"] == alert.sensor_id]

    cusum = _find_ctx(alert, "cusum")
    if cusum and "mu" in cusum:
        baseline = float(cusum["mu"])
        source = "cusum_mu"
    else:
        # Sparse / event-driven sensors (battery, state-change) routinely
        # have empty 2h pre-windows. Widen to 24h, then 7d before giving up —
        # a sparse baseline beats a NaN one as long as the source label is
        # surfaced so downstream consumers can weight it accordingly.
        baseline = float("nan")
        source = "prewindow_unavailable"
        for hours, label in ((2, "prewindow_2h"),
                             (24, "prewindow_24h"),
                             (7 * 24, "prewindow_7d")):
            pre = sub[(sub["timestamp"] >= w0 - pd.Timedelta(hours=hours))
                      & (sub["timestamp"] < w0)]
            if len(pre):
                baseline = float(pre["value"].median())
                source = label
                break

    during = sub[(sub["timestamp"] >= w0) & (sub["timestamp"] <= w1)]
    # baseline != baseline is the standard NaN check — happens when the 2h
    # pre-window has no events and the median fallback resolves to NaN.
    if len(during) == 0 or baseline != baseline:
        peak = float("nan"); delta = float("nan")
    else:
        deltas = (during["value"].astype(float) - baseline).dropna()
        if len(deltas) == 0:
            peak = float("nan"); delta = float("nan")
        else:
            # The "peak" is the value with the largest |delta| during the window.
            peak_idx = deltas.abs().idxmax()
            peak = float(during.loc[peak_idx, "value"])
            delta = float(peak - baseline)

    pct = (delta / baseline * 100.0) if baseline and baseline != 0 else float("nan")
    return {
        "baseline": baseline,
        "baseline_source": source,
        "peak": peak,
        "delta": delta,
        "delta_pct": pct,
    }


def _synth_detector_context(alert: Alert, events: pd.DataFrame,
                            mag: dict) -> list[dict]:
    """Rebuild best-effort per-detector context when the live dicts are absent.

    The batch/CSV path strips ``alert.context`` because the detections CSV
    doesn't carry detector-native diagnostics — bundles end up with
    ``detector_context = []`` and the prompt renders "(per-detector context
    dicts unavailable)". This function derives the stats a reader actually
    uses to interpret each detector (cusum direction + mu/sigma,
    temporal_profile same-hour z, DQG raw value + anomaly_type) from the
    events frame, so bundles from the batch path carry equivalent signal.

    Contract: ``events["timestamp"]`` MUST already be UTC datetime64. The
    parse is lifted to ``bundle._ensure_utc_timestamps`` so the batch CSV
    path doesn't pay it 3× per alert.
    """
    dets = sorted(alert.detector.split("+"))
    w0 = alert.window_start or alert.timestamp
    w1 = alert.window_end or alert.timestamp

    sub = events[events["sensor_id"] == alert.sensor_id]
    pre = sub[(sub["timestamp"] >= w0 - pd.Timedelta(hours=2))
              & (sub["timestamp"] < w0)]
    pre_median = float(pre["value"].median()) if len(pre) else float("nan")
    pre_std = float(pre["value"].std()) if len(pre) > 1 else float("nan")

    peak = mag.get("peak")
    delta = mag.get("delta")
    delta_val = float(delta) if delta is not None and delta == delta else 0.0
    if delta_val > 0:
        direction = "+"
    elif delta_val < 0:
        direction = "-"
    else:
        direction = "0"

    ctxs: list[dict] = []
    for det in dets:
        if det == "cusum":
            ctxs.append({
                "detector": "cusum",
                "mu": pre_median,
                "sigma": pre_std,
                "direction": direction,
                "delta": delta,
                "source": "derived_from_prewindow",
            })
        elif det in ("sub_pca", "multivariate_pca"):
            approx_z = (abs(delta_val) / pre_std
                        if pre_std and pre_std > 0 and pre_std == pre_std
                        else float("nan"))
            ctxs.append({
                "detector": det,
                "approx_residual_z": approx_z,
                "baseline": pre_median,
                "source": "derived_from_prewindow",
            })
        elif det == "data_quality_gate":
            ctxs.append({
                "detector": "data_quality_gate",
                "anomaly_type": alert.anomaly_type,
                "value": peak,
                "score": float(alert.score),
            })
        elif det == "temporal_profile":
            hr = int(w0.hour)
            hour_prior = sub[(sub["timestamp"] < w0)
                             & (sub["timestamp"].dt.hour == hr)]
            hour_median = (float(hour_prior["value"].median())
                           if len(hour_prior) else float("nan"))
            hour_std = (float(hour_prior["value"].std())
                        if len(hour_prior) > 1 else float("nan"))
            if (peak is not None and peak == peak
                    and hour_std and hour_std > 0 and hour_std == hour_std):
                approx_hour_z = (float(peak) - hour_median) / hour_std
            else:
                approx_hour_z = float("nan")
            ctxs.append({
                "detector": "temporal_profile",
                "hour_of_day": hr,
                "same_hour_median": hour_median,
                "approx_hour_z": approx_hour_z,
                "source": "derived_from_same_hour_history",
            })
        elif det == "state_transition":
            ctxs.append({
                "detector": "state_transition",
                "anomaly_type": alert.anomaly_type,
                "raw_value": peak,
            })
        else:
            ctxs.append({"detector": det, "source": "derived_no_model"})
    return ctxs
