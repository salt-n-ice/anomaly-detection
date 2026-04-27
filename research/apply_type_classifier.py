"""Apply the trained type classifier to a detections CSV.

Reads a detections CSV produced by the pipeline (columns: sensor_id,
capability, window_start, window_end, first_fire_ts, anomaly_type,
inferred_type, inferred_class, detector, score, ...), augments each row
with features from the alert's detector-set string + timing info, and
predicts `ml_inferred_type`.

For rows where `inferred_type` is already a real anomaly type (DQG or
state_transition output), pass through — no ML inference needed. The
classifier only runs on fused-detector-chain rows where
`inferred_type` is `statistical_anomaly` or a duration-based guess.

Usage:
    python research/apply_type_classifier.py \
        --detections out/household_60d_detections.csv \
        --out out/household_60d_detections_ml.csv
"""
from __future__ import annotations
import argparse
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "research" / "type_classifier.joblib"

# Types that are already confidently produced by DQG/state_transition —
# don't override with ML classifier (they're explicit and correct).
EXPLICIT_TYPES = frozenset({
    "out_of_range", "saturation", "stuck_at", "dropout", "clock_drift",
    "batch_arrival", "duplicate_stale", "reporting_rate_change",
    "extreme_value",
    "water_leak_sustained", "unusual_occupancy",
})

ARCHETYPE_BY_CAPABILITY = {
    "voltage": "continuous",
    "temperature": "continuous",
    "power": "bursty",
    "motion": "binary",
    "water": "binary",
}
_CAPABILITY_CODE = {"power": 0, "voltage": 1, "motion": 2, "water": 3,
                    "temperature": 4}
_SENSOR_CODE = {
    "outlet_fridge_power": 0, "outlet_kettle_power": 1,
    "outlet_tv_power": 2, "mains_voltage": 3,
    "basement_temp": 4, "basement_leak": 5,
    "bedroom_motion": 6, "utility_motion": 7,
}


def _featurize_row(row: pd.Series, feature_cols: list[str],
                    arch_codes: dict) -> dict:
    det_str = str(row.get("detector", ""))
    dets = set(det_str.split("+")) if det_str else set()
    w0 = pd.Timestamp(row["window_start"]) if pd.notna(row.get("window_start")) else None
    w1 = pd.Timestamp(row["window_end"]) if pd.notna(row.get("window_end")) else None
    ff = pd.Timestamp(row["first_fire_ts"]) if pd.notna(row.get("first_fire_ts")) else w0
    dur = max(0.0, (w1 - w0).total_seconds()) if (w0 and w1) else 0.0
    capability = str(row.get("capability", ""))
    archetype = ARCHETYPE_BY_CAPABILITY.get(capability, "continuous")
    score = float(row.get("score", 0.0))
    # No direct access to threshold/context at CSV level — use score only
    # as a proxy for score_over_thresh (reasonable since CSV strips
    # detector context). This is a known limitation; features that use
    # context (cusum_sp_over_sigma, pca_err_over_thr, temporal_z) will
    # be set to 0 at apply time — classifier was trained on full context
    # but will fall back to non-context features at inference.
    feats = {
        "capability_code": _CAPABILITY_CODE.get(capability, -1),
        "sensor_code":     _SENSOR_CODE.get(str(row.get("sensor_id", "")), -1),
        "det_cusum":            int("cusum" in dets),
        "det_sub_pca":          int("sub_pca" in dets),
        "det_multivariate_pca": int("multivariate_pca" in dets),
        "det_temporal_profile": int("temporal_profile" in dets),
        "det_recent_shift":     int("recent_shift" in dets),
        "det_data_quality_gate": int("data_quality_gate" in dets),
        "det_state_transition": int("state_transition" in dets),
        "duration_log": float(np.log1p(dur)),
        "hour":         ff.hour if ff else 0,
        "dow":          ff.dayofweek if ff else 0,
        "is_weekend":   int(ff.dayofweek >= 5) if ff else 0,
        "month":        ff.month if ff else 0,
        "drift_dir":    0,
        "cusum_sp_over_sigma": 0.0,
        "cusum_sn_over_sigma": 0.0,
        "pca_err_over_thr": 0.0,
        "temporal_z": 0.0,
        "score_over_thresh": score,
        "arch_code": arch_codes.get(archetype, -1),
    }
    return feats


def apply_classifier(det_df: pd.DataFrame, model_bundle: dict) -> pd.DataFrame:
    model = model_bundle["model"]
    feature_cols = model_bundle["feature_cols"]
    arch_codes = model_bundle["archetype_codes"]

    out = det_df.copy()
    ml_types = []
    for _, row in out.iterrows():
        itype = str(row.get("inferred_type", ""))
        # If DQG/state_transition explicitly typed, pass through.
        if itype in EXPLICIT_TYPES:
            ml_types.append(itype)
            continue
        feats = _featurize_row(row, feature_cols, arch_codes)
        X = np.array([[feats[c] for c in feature_cols]], dtype=np.float64)
        X = np.nan_to_num(X, nan=0.0, posinf=1e6, neginf=-1e6)
        X = np.clip(X, -1e6, 1e6)
        pred = model.predict(X)[0]
        ml_types.append(str(pred))
    out["ml_inferred_type"] = ml_types
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--detections", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--model", type=Path, default=MODEL_PATH)
    args = ap.parse_args()
    bundle = joblib.load(args.model)
    df = pd.read_csv(args.detections)
    out = apply_classifier(df, bundle)
    out.to_csv(args.out, index=False)
    print(f"wrote {len(out)} rows to {args.out}")
    if "ml_inferred_type" in out.columns:
        print("\nml_inferred_type distribution:")
        print(out["ml_inferred_type"].value_counts().to_string())


if __name__ == "__main__":
    main()
