"""Deterministic explainer layer.

Turns a detection-pipeline Alert into a structured bundle an LLM can consume.
No LLM, no persistence, no cross-sensor context (Stage 2). The pipeline keeps
its real-time contract; this module runs afterwards on whatever alerts are
emitted (streaming or batch).
"""
from __future__ import annotations
import pandas as pd
from .core import Alert


# Canonical label vocabulary (mirrors synthetic-generator/labels.py). Kept
# local so the anomaly-detection package stays decoupled from sensorgen.
USER_BEHAVIOR_TYPES: frozenset[str] = frozenset({
    "spike", "dip", "level_shift", "trend", "degradation_trajectory",
    "frequency_change", "seasonality_loss", "time_of_day",
    "weekend_anomaly", "month_shift", "seasonal_mismatch",
    "water_leak_sustained", "unusual_occupancy",
})
SENSOR_FAULT_TYPES: frozenset[str] = frozenset({
    "out_of_range", "saturation", "noise_burst", "noise_floor_up",
    "stuck_at", "calibration_drift", "dropout", "duplicate_stale",
    "reporting_rate_change", "clock_drift", "batch_arrival",
})


def type_to_class(anomaly_type: str) -> str:
    """Map an anomaly_type string to its label class.

    Returns:
        "user_behavior" — occupancy/routine/appliance-shift semantics
        "sensor_fault"  — infrastructure signal-quality issues
        "unknown"       — detector-combo string or unmapped type

    Used by the eval harness to prevent a DQG `dropout` claim from
    being counted as TP against a `water_leak_sustained` label on the
    same sensor, and vice versa.
    """
    if anomaly_type in USER_BEHAVIOR_TYPES:
        return "user_behavior"
    if anomaly_type in SENSOR_FAULT_TYPES:
        return "sensor_fault"
    return "unknown"


def _find_ctx(alert: Alert, detector: str) -> dict | None:
    """Return the first context dict for ``detector`` (or None)."""
    if not alert.context:
        return None
    for ctx in alert.context:
        if ctx.get("detector") == detector:
            return ctx
    return None


def classify_type(alert: Alert) -> str:
    """Decision tree: detector set x duration x drift direction -> canonical type.

    Reuses the generator's label vocabulary so the type is directly comparable
    to ground truth. Unknown combinations fall back to ``"statistical_anomaly"``.
    """
    # 1. DQG / state_transition are pre-typed -- pass through.
    if alert.anomaly_type:
        return alert.anomaly_type

    dets = set(alert.detector.split("+"))
    dur_sec = ((alert.window_end or alert.timestamp)
               - (alert.window_start or alert.timestamp)).total_seconds()
    cusum = _find_ctx(alert, "cusum")
    drift_dir = cusum.get("direction") if cusum else None

    # 2. Short + many detectors agreeing = spike/dip.
    if dur_sec < 10 * 60 and len(dets) >= 3:
        return "spike" if drift_dir == "+" else "dip"

    # 3. CUSUM-led long chain -> drift family, bucketed by duration.
    if "cusum" in dets and dur_sec > 60 * 60:
        if dur_sec > 7 * 86400:
            return "month_shift"
        if dur_sec > 86400:
            return "calibration_drift"
        # 1h-24h: distinguish level_shift (shape change, PCA fires) from drift.
        if "sub_pca" in dets or "multivariate_pca" in dets:
            return "level_shift"
        return "trend"

    # 4. Temporal-profile-only -> calendar pattern anomaly.
    if dets == {"temporal_profile"}:
        ts = alert.timestamp
        if ts.dayofweek >= 5:
            return "weekend_anomaly"
        if 2 <= ts.hour <= 6 or 22 <= ts.hour <= 23:
            return "time_of_day"
        return "temporal_pattern"

    # 5. SubPCA-led without CUSUM -> shape anomaly (frequency_change, seasonality_loss).
    if "sub_pca" in dets and "cusum" not in dets:
        return "frequency_change" if dur_sec >= 3600 else "shape_anomaly"

    return "statistical_anomaly"


_TIME_BUCKETS = [(0, 6, "night"), (6, 12, "morning"),
                 (12, 18, "afternoon"), (18, 24, "evening")]


def extract_magnitude(alert: Alert, events: pd.DataFrame) -> dict:
    """Signed magnitude of the anomalous excursion relative to a baseline.

    Prefers ``cusum.mu`` when present (detector-native reference). Falls back to
    the median of the 2h pre-window for the alert's sensor.
    """
    w0 = alert.window_start or alert.timestamp
    w1 = alert.window_end or alert.timestamp
    if "timestamp" in events.columns and events["timestamp"].dtype != "datetime64[ns, UTC]":
        events = events.copy()
        events["timestamp"] = pd.to_datetime(events["timestamp"], utc=True, format="ISO8601")
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
    """
    dets = sorted(alert.detector.split("+"))
    w0 = alert.window_start or alert.timestamp
    w1 = alert.window_end or alert.timestamp

    if "timestamp" in events.columns and events["timestamp"].dtype != "datetime64[ns, UTC]":
        events = events.copy()
        events["timestamp"] = pd.to_datetime(events["timestamp"], utc=True, format="ISO8601")
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


def temporal_framing(alert: Alert) -> dict:
    ts = alert.timestamp
    bucket = next((name for lo, hi, name in _TIME_BUCKETS if lo <= ts.hour < hi),
                  "unknown")
    return {
        "timestamp": ts.isoformat(),
        "weekday": ts.day_name(),
        "hour": int(ts.hour),
        "is_weekend": bool(ts.dayofweek >= 5),
        "month": ts.month_name(),
        "time_of_day_bucket": bucket,
    }


def _same_hour_weekday_stats(alert: Alert, events: pd.DataFrame,
                             peak: float | None) -> dict:
    """Compare the alert's peak against same-hour-of-weekday history.

    A large |z| means the value is unusual for this sensor at this
    hour-of-day on this day-of-week — positive evidence for calendar-family
    anomalies (time_of_day, weekend_anomaly, temporal_pattern) even when the
    firing detectors are statistical rather than `temporal_profile`.
    Returns ``{}`` if there's too little peer history (< 4 points) or peak
    is not finite.
    """
    if peak is None or peak != peak:
        return {}
    ts = alert.timestamp
    w0 = alert.window_start or ts
    if "timestamp" in events.columns and events["timestamp"].dtype != "datetime64[ns, UTC]":
        events = events.copy()
        events["timestamp"] = pd.to_datetime(events["timestamp"], utc=True, format="ISO8601")
    sub = events[events["sensor_id"] == alert.sensor_id]
    peers = sub[(sub["timestamp"] < w0)
                & (sub["timestamp"].dt.hour == ts.hour)
                & (sub["timestamp"].dt.dayofweek == ts.dayofweek)]
    if len(peers) < 4:
        return {}
    peer_median = float(peers["value"].median())
    peer_std = float(peers["value"].std())
    if not (peer_std and peer_std > 0 and peer_std == peer_std):
        return {}
    return {
        "same_hour_weekday_median": peer_median,
        "same_hour_weekday_std": peer_std,
        "same_hour_weekday_n": int(len(peers)),
        "same_hour_weekday_z": float((peak - peer_median) / peer_std),
    }


def explain(alert: Alert, events: pd.DataFrame) -> dict:
    """Top-level composer. Returns a structured bundle ready for an LLM prompt."""
    w0 = alert.window_start or alert.timestamp
    w1 = alert.window_end or alert.timestamp
    mag = extract_magnitude(alert, events)
    ctx = list(alert.context) if alert.context else _synth_detector_context(alert, events, mag)
    temporal = temporal_framing(alert)
    temporal.update(_same_hour_weekday_stats(alert, events, mag.get("peak")))
    return {
        "alert_id": f"{alert.sensor_id}|{alert.capability}|{w0.isoformat()}",
        "sensor": alert.sensor_id,
        "capability": alert.capability,
        "window": {"start": w0.isoformat(), "end": w1.isoformat(),
                   "duration_sec": float((w1 - w0).total_seconds())},
        "inferred_type": classify_type(alert),
        "magnitude": mag,
        "temporal": temporal,
        "detectors": sorted(alert.detector.split("+")),
        "detector_context": ctx,
        "score": float(alert.score),
        "threshold": float(alert.threshold),
    }


def _human_duration(s: float) -> str:
    if s < 60:
        return f"{s:.0f}s"
    if s < 3600:
        return f"{s/60:.1f}m"
    if s < 86400:
        return f"{s/3600:.2f}h"
    return f"{s/86400:.2f}d"


def _human_ts(iso: str) -> str:
    try:
        return pd.Timestamp(iso).strftime("%a %b %d %Y %H:%M UTC")
    except (ValueError, TypeError):
        return str(iso)


def _weekend_day_count(start_iso: str, end_iso: str) -> int:
    s = pd.Timestamp(start_iso)
    e = pd.Timestamp(end_iso)
    days = pd.date_range(s.normalize(), e.normalize(), freq="D")
    return sum(1 for d in days if d.dayofweek >= 5)


def _format_detector_context(ctx: dict) -> str:
    det = ctx.get("detector", "unknown")
    rest = {k: v for k, v in ctx.items() if k != "detector"}
    if not rest:
        return det
    kvs = ", ".join(f"{k}={v}" for k, v in rest.items())
    return f"{det}: {kvs}"


def build_prompt(bundle: dict) -> str:
    """Render an explainer bundle as an LLM-ready natural-language prompt.

    Deliberately omits ``inferred_type`` from the text: the classifier's
    heuristics are noisy on mixed-detector events and pushing an opinionated
    label ahead of the evidence biases the LLM. The LLM gets the raw signal
    (detectors fired, magnitude, per-detector context dicts when available,
    temporal framing) and reasons about the type itself.

    Duration framing adapts: short events get ``Xh``; events >= 24h get a
    ``Long-duration framing`` line with day span and weekend-day count.
    """
    sensor = bundle["sensor"]
    cap = bundle["capability"]
    w = bundle["window"]
    mag = bundle.get("magnitude") or {}
    temp = bundle.get("temporal") or {}
    dets = bundle.get("detectors") or []
    dctx = bundle.get("detector_context") or []
    score = bundle.get("score")
    threshold = bundle.get("threshold")

    lines: list[str] = [f"# Anomaly on sensor {sensor} (capability: {cap})", ""]

    dur_sec = float(w.get("duration_sec", 0))
    lines.append(
        f"**When:** {_human_ts(w['start'])} -> {_human_ts(w['end'])} "
        f"(duration {_human_duration(dur_sec)})."
    )
    if dur_sec >= 86400:
        n_days = dur_sec / 86400
        n_weekends = _weekend_day_count(w["start"], w["end"])
        lines.append(
            f"**Long-duration framing:** spans {n_days:.1f} days; "
            f"covers {n_weekends} weekend day(s)."
        )
    lines.append("")

    baseline = mag.get("baseline")
    if baseline is not None and baseline == baseline:
        lines.append(
            f"**Magnitude:** baseline {baseline:.4g} "
            f"(source: {mag.get('baseline_source', 'unknown')}), "
            f"peak {mag.get('peak'):.4g}, "
            f"delta {mag.get('delta'):+.4g} "
            f"({mag.get('delta_pct'):+.2f}%)."
        )
    else:
        lines.append("**Magnitude:** baseline unavailable (no pre-window data).")
    lines.append("")

    lines.append(
        f"**Calendar context:** {temp.get('weekday', '?')}, "
        f"hour {temp.get('hour', '?')} ({temp.get('time_of_day_bucket', '?')}), "
        f"{'weekend' if temp.get('is_weekend') else 'weekday'}, "
        f"{temp.get('month', '?')}."
    )
    shwz = temp.get("same_hour_weekday_z")
    if shwz is not None and shwz == shwz:
        lines.append(
            f"**Same-hour-of-weekday baseline:** peak is "
            f"{shwz:+.2f}σ vs. the median of {temp.get('same_hour_weekday_n', 0)} "
            f"prior {temp.get('weekday', '?')} {temp.get('hour', '?')}:00 samples "
            f"(peer median {temp.get('same_hour_weekday_median'):.4g})."
        )
    lines.append("")

    lines.append("**Detector evidence:**")
    if dctx:
        for ctx in dctx:
            lines.append(f"- {_format_detector_context(ctx)}")
    else:
        lines.append(
            "- (per-detector context dicts unavailable on this alert; "
            "see detectors list below)"
        )
    lines.append("")

    lines.append(f"**Detectors fired:** {', '.join(dets) if dets else 'none'}.")
    lines.append("")

    if score is not None and threshold is not None:
        lines.append(f"**Score:** {score:.3g} (threshold {threshold:.3g}).")

    return "\n".join(lines).rstrip()


def _detections_to_alerts(det_df: pd.DataFrame) -> list[Alert]:
    out: list[Alert] = []
    for r in det_df.itertuples(index=False):
        w0 = pd.Timestamp(r.start) if not isinstance(r.start, pd.Timestamp) else r.start
        w1 = pd.Timestamp(r.end)   if not isinstance(r.end,   pd.Timestamp) else r.end
        det_str = str(r.detector)
        atype_raw = str(getattr(r, "anomaly_type", "")) or None
        # pipeline._write_detections stores `anomaly_type or detector` in the
        # CSV's anomaly_type column; for statistical fused alerts the value is
        # the detector string. Strip that fallback so classify_type walks the
        # decision tree instead of short-circuiting on the pre-typed branch.
        anomaly_type = None if atype_raw == det_str else atype_raw
        out.append(Alert(
            sensor_id=str(r.sensor_id), capability=str(r.capability),
            timestamp=w0, detector=det_str,
            score=float(getattr(r, "score", 0.0)), threshold=0.0,
            anomaly_type=anomaly_type,
            raw_value=None, state=None, window_start=w0, window_end=w1,
            context=None,
        ))
    return out


def explain_detections_csv(events_csv, detections_csv, out_jsonl) -> int:
    """Batch explainer: CSV in, JSONL out. Returns the number of bundles written."""
    import json as _json
    from pathlib import Path as _P
    events = pd.read_csv(events_csv)
    events["timestamp"] = pd.to_datetime(events["timestamp"], utc=True, format="ISO8601")
    dets = pd.read_csv(detections_csv)
    alerts = _detections_to_alerts(dets)
    path = _P(out_jsonl); path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        n = 0
        for a in alerts:
            f.write(_json.dumps(explain(a, events), default=str) + "\n")
            n += 1
    return n
