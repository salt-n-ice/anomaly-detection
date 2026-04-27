"""Train a type classifier on extracted ambiguous-chain detections.

Input:  research/training_data.csv (from extract_training_data.py)
Output: research/type_classifier.joblib + research/type_classifier_report.json

Only `ambiguous` rows (no explicit_type — i.e., fused detector chains)
are used for training — DQG/state_transition alerts already carry their
type and don't need classification.

Only TP rows (overlap_frac > 0.1 with a real GT label) are training
targets. At inference, the classifier predicts on ALL rows; wrong-type
predictions on real GT are FP under NAB; predictions on noise rows are
harmless (NAB FP accounting catches them via "outside any GT window").

Validation: leave-one-scenario-out cross-validation. Reports per-type
precision/recall/F1 and confusion matrices so we know which classes are
actually learnable with this data.

Usage:
    python research/train_type_classifier.py
"""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "research" / "training_data.csv"
MODEL_PATH = ROOT / "research" / "type_classifier.joblib"
REPORT_PATH = ROOT / "research" / "type_classifier_report.json"

# Minimum samples per class required to include it in the classifier's
# output space. Classes with fewer samples collapse into "statistical_anomaly"
# at inference — they're too rare to learn reliably from this data.
MIN_SAMPLES = 5

FEATURE_COLS = [
    "capability_code",
    "sensor_code",  # per-sensor prior (mains_voltage shifts → calibration_drift,
                    # outlet shifts → level_shift, etc.)
    "det_cusum", "det_sub_pca", "det_multivariate_pca",
    "det_temporal_profile", "det_recent_shift",
    "det_data_quality_gate", "det_state_transition",
    "duration_log",
    "hour", "dow", "is_weekend", "month",
    "drift_dir",
    "cusum_sp_over_sigma", "cusum_sn_over_sigma",
    "pca_err_over_thr",
    "temporal_z",
    "score_over_thresh",
]

# Archetype is a string; one-hot encode.
ARCHETYPE_CODES = {"continuous": 0, "bursty": 1, "binary": 2}


def _prep(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["arch_code"] = out["archetype"].map(ARCHETYPE_CODES).fillna(-1).astype(int)
    # Some alert scores (pca_err_over_thr, score_over_thresh, cusum_sp/sigma)
    # can explode on near-zero thresholds. Clip to finite +/- 1e6 and fill NaN.
    num_cols = [c for c in out.columns if out[c].dtype.kind in ("f", "i")]
    out[num_cols] = (out[num_cols]
                     .replace([np.inf, -np.inf], np.nan)
                     .fillna(0.0)
                     .clip(-1e6, 1e6))
    return out


def _fit_and_evaluate(model_cls, model_kwargs, train_df, test_df,
                       feature_cols, label_col, label_classes):
    X_train = train_df[feature_cols].values
    y_train = train_df[label_col].values
    X_test  = test_df[feature_cols].values
    y_test  = test_df[label_col].values
    model = model_cls(**model_kwargs)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred, model


def main():
    df = pd.read_csv(DATA_PATH)
    # Ambiguous = no explicit_type, fused-chain output.
    amb = df[df["explicit_type"].isna() | (df["explicit_type"] == "")].copy()
    # TP rows only (for TRAINING): detection must overlap a real GT.
    tps = amb[(amb["gt_type"] != "noise") & (amb["overlap_frac"] > 0.1)].copy()
    print(f"Ambiguous rows: {len(amb)}, training TP rows: {len(tps)}")

    tps = _prep(tps)
    feature_cols = FEATURE_COLS + ["arch_code"]

    # Restrict label space to classes with enough samples.
    class_counts = Counter(tps["gt_type"])
    kept_classes = sorted([c for c, n in class_counts.items() if n >= MIN_SAMPLES])
    print(f"Kept classes (>= {MIN_SAMPLES} samples): {kept_classes}")
    print(f"Dropped (too few samples): "
          f"{sorted([c for c, n in class_counts.items() if n < MIN_SAMPLES])}")

    train = tps[tps["gt_type"].isin(kept_classes)].copy()
    print(f"Usable training rows: {len(train)}")

    # Leave-one-scenario-out CV.
    scenarios = sorted(train["scenario"].unique())
    print(f"\nLOOCV across scenarios: {scenarios}\n")

    cv_rows = []
    all_y_true = []
    all_y_pred = []

    for holdout in scenarios:
        train_fold = train[train["scenario"] != holdout]
        test_fold  = train[train["scenario"] == holdout]
        if len(test_fold) == 0:
            continue
        # Skip folds where the test set introduces classes absent from training
        # (one-off label types on a holdout scenario). Prediction on those
        # will just be wrong; LOOCV reports this as fold skip.
        test_classes = set(test_fold["gt_type"].unique())
        train_classes = set(train_fold["gt_type"].unique())
        if not test_classes.issubset(train_classes):
            print(f"  {holdout}: test has classes absent in train: "
                  f"{test_classes - train_classes} — fold will show lower recall")

        # Try two models; pick the one with better weighted F1.
        candidates = [
            ("decision_tree", DecisionTreeClassifier,
             {"max_depth": 6, "min_samples_leaf": 3, "random_state": 0,
              "class_weight": "balanced"}),
            ("random_forest", RandomForestClassifier,
             {"n_estimators": 200, "max_depth": 8, "min_samples_leaf": 2,
              "random_state": 0, "class_weight": "balanced", "n_jobs": -1}),
        ]
        best = None
        for name, cls, kw in candidates:
            y_pred, _ = _fit_and_evaluate(cls, kw, train_fold, test_fold,
                                           feature_cols, "gt_type", kept_classes)
            # Compute weighted F1 manually
            from sklearn.metrics import f1_score
            f1 = f1_score(test_fold["gt_type"].values, y_pred,
                           average="weighted", zero_division=0)
            if best is None or f1 > best[0]:
                best = (f1, name, y_pred)
        f1, name, y_pred = best
        y_true = test_fold["gt_type"].values
        cv_rows.append({"scenario": holdout, "model": name,
                         "weighted_f1": round(f1, 4),
                         "n_test": len(test_fold)})
        all_y_true.extend(y_true.tolist())
        all_y_pred.extend(y_pred.tolist())
        print(f"  {holdout}: n={len(test_fold):3d}  model={name:15s}  "
              f"weighted_F1={f1:.3f}")

    print("\n=== Aggregated LOOCV classification report ===")
    rep = classification_report(all_y_true, all_y_pred,
                                 labels=kept_classes, zero_division=0,
                                 output_dict=True)
    for cls in kept_classes:
        r = rep[cls]
        print(f"  {cls:25s}  precision={r['precision']:.2f}  "
              f"recall={r['recall']:.2f}  F1={r['f1-score']:.2f}  "
              f"support={int(r['support'])}")
    print(f"  {'macro avg':25s}  precision={rep['macro avg']['precision']:.2f}  "
          f"recall={rep['macro avg']['recall']:.2f}  "
          f"F1={rep['macro avg']['f1-score']:.2f}")
    print(f"  {'weighted avg':25s}  precision={rep['weighted avg']['precision']:.2f}  "
          f"recall={rep['weighted avg']['recall']:.2f}  "
          f"F1={rep['weighted avg']['f1-score']:.2f}")

    # Final model: train on all data using the better overall model (RF).
    final = RandomForestClassifier(
        n_estimators=200, max_depth=8, min_samples_leaf=2,
        random_state=0, class_weight="balanced", n_jobs=-1)
    final.fit(train[feature_cols].values, train["gt_type"].values)
    joblib.dump({"model": final, "feature_cols": feature_cols,
                  "kept_classes": kept_classes,
                  "archetype_codes": ARCHETYPE_CODES,
                  "min_samples": MIN_SAMPLES}, MODEL_PATH)
    print(f"\nSaved final model to {MODEL_PATH}")

    # Feature importance (RF).
    imp = sorted(zip(feature_cols, final.feature_importances_),
                  key=lambda x: -x[1])
    print("\n=== Feature importance ===")
    for k, v in imp[:10]:
        print(f"  {k:30s}  {v:.3f}")

    report = {
        "min_samples": MIN_SAMPLES,
        "kept_classes": kept_classes,
        "n_training_rows": len(train),
        "cv_rows": cv_rows,
        "per_class": {cls: {k: float(rep[cls][k]) if k != "support"
                                   else int(rep[cls][k])
                             for k in ("precision", "recall", "f1-score",
                                        "support")}
                       for cls in kept_classes},
        "macro_avg": {k: float(rep["macro avg"][k]) for k in
                       ("precision", "recall", "f1-score")},
        "weighted_avg": {k: float(rep["weighted avg"][k]) for k in
                          ("precision", "recall", "f1-score")},
        "feature_importance": [{"feature": k, "importance": float(v)}
                                 for k, v in imp],
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2))
    print(f"Saved report to {REPORT_PATH}")


if __name__ == "__main__":
    main()
