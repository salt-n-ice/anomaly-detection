"""Extract (feature, gt_type) training pairs from pipeline detections.

Runs the pipeline with the pre-redesign full-detector profile on each
scenario, collects the fused Alerts with their context dicts, joins with
GT labels by (sensor, time overlap), and writes a training CSV.

Output: research/training_data.csv with columns:
    scenario, sensor_id, capability, archetype,
    det_cusum, det_sub_pca, det_multivariate_pca, det_temporal_profile,
    det_recent_shift, det_data_quality_gate, det_state_transition,
    duration_sec, hour, dow, is_weekend, month, drift_dir,
    cusum_sp_over_sigma, cusum_sn_over_sigma, cusum_dir_plus,
    pca_err_over_thr, temporal_z,
    score_over_thresh, capability_code,
    gt_type, gt_class, overlap_frac

Usage:
    python research/extract_training_data.py
"""
from __future__ import annotations
import json
import sys
from functools import partial
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "research"))

from anomaly import profiles as profiles_module  # noqa: E402
from anomaly import pipeline as pipeline_module  # noqa: E402
from anomaly.core import Archetype, Event, SensorConfig  # noqa: E402
from anomaly.detectors import (  # noqa: E402
    CUSUM, MultivariatePCA, RecentShift, SubPCA, TemporalProfile,
    DataQualityGate, StateTransition,
)
from anomaly.fusion import DefaultAlertFuser  # noqa: E402
from anomaly.profiles import ArchetypeProfile  # noqa: E402
from anomaly.pipeline import Pipeline, _load_configs  # noqa: E402

from run_research_eval import SCENARIOS, GEN, CFG  # noqa: E402

OUT_PATH = ROOT / "research" / "training_data.csv"

# Additional training-only scenarios — rich in rare-class anomalies. Not part
# of evaluation. Their sensor configs mirror household.yaml / leak_30d.yaml
# but include motion sensors (so the classifier learns motion types too, for
# eventual re-introduction). Eval pipeline's motion filter still applies at
# scoring time; these CSVs are consumed ONLY by the extractor.
TRAINING_EXTRA: list[tuple[str, str, str, str, float]] = [
    ("training", "training_rich_60d",     "training_rich_60d",
     "household_full.yaml", 14.0),
    ("training", "training_patterns_60d", "training_patterns_60d",
     "household_full.yaml", 14.0),
]

_BINARY_BASE = ["duty_cycle_1h", "duty_cycle_24h", "transitions_per_hour"]
_BINARY_FEATS = {
    "cusum":    ["duty_cycle_24h", "transitions_per_hour"],
    "mvpca":    _BINARY_BASE + [f"{b}_diff" for b in _BINARY_BASE],
    "temporal": _BINARY_BASE,
}
_BURSTY_FEATS = {
    "cusum":    ["value"],
    "mvpca":    ["value", "time_in_state", "value_diff",
                 "value_roll_1h", "value_roll_24h"],
    "temporal": ["value"],
}
_CONT_FEATS = {
    "cusum":    ["value"],
    "mvpca":    ["value", "value_diff", "value_roll_1h", "value_roll_24h"],
    "temporal": ["value"],
}


def _full_profiles():
    """Pre-redesign PROFILES: every statistical detector enabled. Used only
    by the training-data extractor — not wired into the main pipeline."""
    from anomaly.fusion import (ContinuousCorroboration,
                                 PassThroughCorroboration)

    def cont_fuser(cfg):
        return DefaultAlertFuser(cfg, gap=15*60, max_span=96*3600,
                                  anchor_on_non_cusum=True,
                                  corroboration=ContinuousCorroboration())

    def default_fuser(cfg):
        return DefaultAlertFuser(cfg, gap=60*60, max_span=96*3600,
                                  anchor_on_non_cusum=False,
                                  corroboration=PassThroughCorroboration())

    return {
        Archetype.CONTINUOUS: ArchetypeProfile(
            short_event=[DataQualityGate],
            short_tick=[],
            medium=[
                partial(CUSUM, features=_CONT_FEATS["cusum"],
                         warmup_seconds=5*86400),
                partial(SubPCA, warmup_seconds=3*86400),
                partial(MultivariatePCA, features=_CONT_FEATS["mvpca"],
                         warmup_seconds=5*86400),
                # Also include RecentShift on CONT so the classifier trains
                # on the (recent_shift, continuous, voltage/temperature)
                # combinations that Stage 2+ iters actually use. Without this,
                # the pre-redesign training set only has recent_shift on
                # motion, and the classifier over-generalizes
                # "recent_shift → unusual_occupancy".
                partial(RecentShift),
            ],
            long_tick=[partial(TemporalProfile,
                                features=_CONT_FEATS["temporal"])],
            long_fuser=cont_fuser,
        ),
        Archetype.BURSTY: ArchetypeProfile(
            short_event=[DataQualityGate],
            short_tick=[],
            medium=[
                partial(CUSUM, features=_BURSTY_FEATS["cusum"],
                         warmup_seconds=12*3600),
                partial(SubPCA, warmup_seconds=12*3600),
                partial(MultivariatePCA, features=_BURSTY_FEATS["mvpca"],
                         warmup_seconds=12*3600),
            ],
            long_tick=[partial(TemporalProfile,
                                features=_BURSTY_FEATS["temporal"])],
            long_fuser=default_fuser,
        ),
        Archetype.BINARY: ArchetypeProfile(
            short_event=[DataQualityGate],
            short_tick=[StateTransition],
            medium=[
                partial(CUSUM, features=_BINARY_FEATS["cusum"]),
                partial(MultivariatePCA, features=_BINARY_FEATS["mvpca"]),
            ],
            long_tick=[partial(TemporalProfile,
                                features=_BINARY_FEATS["temporal"])],
            long_fuser=default_fuser,
        ),
    }


def _full_profile_for(cfg):
    p = profiles_module.PROFILES[cfg.archetype]
    if cfg.archetype == Archetype.BINARY and cfg.capability == "motion":
        return ArchetypeProfile(
            short_event=p.short_event,
            short_tick=p.short_tick,
            medium=[
                partial(RecentShift,
                        short_feature="duty_cycle_1h",
                        baseline_features=("duty_cycle_24h",
                                            "duty_cycle_24h_roll_7d")),
                partial(MultivariatePCA, features=_BINARY_FEATS["mvpca"]),
            ],
            long_tick=p.long_tick,
            long_fuser=p.long_fuser,
        )
    return p


_CAPABILITY_CODE = {"power": 0, "voltage": 1, "motion": 2, "water": 3,
                    "temperature": 4}

# Sensor-id codes. The classifier can learn per-sensor priors this way:
# mains_voltage shifts on CONT are almost always calibration_drift; outlet_power
# shifts are almost always level_shift / appliance behavior. Capability alone
# (voltage vs power) doesn't capture that two different outlets have similar
# signature but different label distributions (fridge level_shift vs kettle
# trend). Unknown sensors get -1 (classifier treats them as no prior).
_SENSOR_CODE = {
    "outlet_fridge_power": 0,
    "outlet_kettle_power": 1,
    "outlet_tv_power":     2,
    "mains_voltage":       3,
    "basement_temp":       4,
    "basement_leak":       5,
    "bedroom_motion":      6,
    "utility_motion":      7,
}


def _find_ctx(alert, detector):
    if not alert.context:
        return None
    for ctx in alert.context:
        if ctx.get("detector") == detector:
            return ctx
    return None


def _features_from_alert(alert, cfg: SensorConfig) -> dict:
    dets = set(alert.detector.split("+"))
    w0 = alert.window_start or alert.timestamp
    w1 = alert.window_end or alert.timestamp
    duration_sec = max(0.0, (w1 - w0).total_seconds())
    ts = alert.first_fire_ts or alert.timestamp
    cusum = _find_ctx(alert, "cusum")
    pca = _find_ctx(alert, "multivariate_pca") or _find_ctx(alert, "sub_pca")
    temp = _find_ctx(alert, "temporal_profile")

    drift_dir = 0
    cusum_sp = cusum_sn = 0.0
    if cusum:
        d = cusum.get("direction")
        drift_dir = 1 if d == "+" else (-1 if d == "-" else 0)
        sigma = float(cusum.get("sigma", 1e-6)) or 1e-6
        cusum_sp = float(cusum.get("sp", 0.0)) / sigma
        cusum_sn = float(cusum.get("sn", 0.0)) / sigma

    pca_ratio = 0.0
    if pca:
        thr = float(pca.get("thr", 1.0)) or 1.0
        pca_ratio = float(pca.get("err", 0.0)) / thr

    temporal_z = float(temp.get("z", 0.0)) if temp else 0.0

    return {
        "sensor_id": cfg.sensor_id,
        "capability": cfg.capability,
        "archetype": cfg.archetype.value,
        "capability_code": _CAPABILITY_CODE.get(cfg.capability, -1),
        "sensor_code":     _SENSOR_CODE.get(cfg.sensor_id, -1),
        "det_cusum":            int("cusum" in dets),
        "det_sub_pca":          int("sub_pca" in dets),
        "det_multivariate_pca": int("multivariate_pca" in dets),
        "det_temporal_profile": int("temporal_profile" in dets),
        "det_recent_shift":     int("recent_shift" in dets),
        "det_data_quality_gate": int("data_quality_gate" in dets),
        "det_state_transition": int("state_transition" in dets),
        "duration_sec":    duration_sec,
        "duration_log":    float(np.log1p(duration_sec)),
        "hour":            ts.hour,
        "dow":             ts.dayofweek,
        "is_weekend":      int(ts.dayofweek >= 5),
        "month":           ts.month,
        "drift_dir":       drift_dir,
        "cusum_sp_over_sigma": cusum_sp,
        "cusum_sn_over_sigma": cusum_sn,
        "pca_err_over_thr":    pca_ratio,
        "temporal_z":          temporal_z,
        "score":            float(alert.score),
        "threshold":        float(alert.threshold),
        "score_over_thresh": (float(alert.score) /
                               float(alert.threshold) if alert.threshold else 0.0),
        "explicit_type":    alert.anomaly_type or "",
        "window_start":     w0.isoformat(),
        "window_end":       w1.isoformat(),
        "first_fire_ts":    ts.isoformat(),
    }


def _match_gt(feature_row: dict, gt: pd.DataFrame) -> tuple[str, str, float]:
    """Find the GT label that this detection's window most overlaps."""
    sub = gt[(gt["sensor_id"] == feature_row["sensor_id"])
             & (gt["capability"] == feature_row["capability"])]
    if sub.empty:
        return "noise", "unknown", 0.0
    w0 = pd.Timestamp(feature_row["window_start"])
    w1 = pd.Timestamp(feature_row["window_end"])
    best = ("noise", "unknown", 0.0)
    for _, r in sub.iterrows():
        g0 = pd.Timestamp(r["start"])
        g1 = pd.Timestamp(r["end"])
        overlap = max(0.0, (min(w1, g1) - max(w0, g0)).total_seconds())
        total = max(1.0, (w1 - w0).total_seconds())
        frac = overlap / total
        if frac > best[2]:
            best = (r["anomaly_type"], r.get("label_class", "unknown"), frac)
    return best


def _run_scenario(name, events_dir, cfg_file, bootstrap_days):
    ev_path = GEN / events_dir / "events.csv"
    lb_path = GEN / events_dir / "labels.csv"
    if not ev_path.exists() or not lb_path.exists():
        print(f"  skip {name}: missing csv")
        return []
    configs = _load_configs(CFG / cfg_file)
    pipe = Pipeline(configs, bootstrap_days=bootstrap_days)
    df = pd.read_csv(ev_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True,
                                      format="ISO8601")
    df = df.sort_values("timestamp").reset_index(drop=True)
    alerts = []
    cfg_by_key = {c.key: c for c in configs}
    for row in df.itertuples(index=False):
        emitted = pipe.ingest(Event(row.timestamp, row.sensor_id,
                                     row.capability, float(row.value),
                                     getattr(row, "unit", "") or ""))
        alerts.extend(emitted)
    alerts.extend(pipe.finalize())

    gt = pd.read_csv(lb_path)
    gt["start"] = pd.to_datetime(gt["start"])
    gt["end"] = pd.to_datetime(gt["end"])

    rows = []
    for a in alerts:
        cfg = cfg_by_key.get((a.sensor_id, a.capability))
        if cfg is None:
            continue
        feat = _features_from_alert(a, cfg)
        gt_type, gt_class, frac = _match_gt(feat, gt)
        feat["scenario"] = name
        feat["gt_type"] = gt_type
        feat["gt_class"] = gt_class
        feat["overlap_frac"] = frac
        rows.append(feat)
    return rows


def main():
    # Monkey-patch PROFILES to full-detector config for training extraction.
    # Pipeline.__init__ imports `profile_for` by name into pipeline_module, so
    # patch both the source module AND the bound reference in pipeline.
    profiles_module.PROFILES = _full_profiles()
    profiles_module.profile_for = _full_profile_for
    pipeline_module.profile_for = _full_profile_for

    all_rows = []
    # For extraction, swap household.yaml → household_full.yaml on the eval
    # scenarios so training data also covers motion + basement_temp labels.
    # Production eval still uses the motion-disabled household.yaml.
    for suite, name, events_dir, cfg_file, boot in SCENARIOS + TRAINING_EXTRA:
        train_cfg = "household_full.yaml" if cfg_file == "household.yaml" else cfg_file
        print(f"run {name} ({suite}) cfg={train_cfg}...")
        rows = _run_scenario(name, events_dir, train_cfg, boot)
        print(f"  {len(rows)} detections")
        all_rows.extend(rows)

    df = pd.DataFrame(all_rows)
    # Drop columns that are noisy / high-cardinality for training (keep in CSV
    # as audit info but separate the feature set in the training script).
    df.to_csv(OUT_PATH, index=False)
    print(f"\nwrote {len(df)} rows to {OUT_PATH}")
    print("\ngt_type distribution:")
    print(df["gt_type"].value_counts().to_string())
    print("\nscenario x gt_type (truncated):")
    print(df.groupby(["scenario", "gt_type"]).size().head(30).to_string())


if __name__ == "__main__":
    main()
