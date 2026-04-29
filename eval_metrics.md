# Eval Metrics — Quick Reference

Computed by `compute_stratified` in `src/anomaly/metrics.py`. Every
metric is reported in two blocks: **`behavior`** (user-facing —
the optimization target) and **`sensor_fault`** (infrastructure —
visibility-only). The 5-scenario suite mean drives iteration
decisions; the holdout is generalization-only.

---

## Headline metrics (printed each run)

| Metric | One-liner |
|---|---|
| **incR** (`incident_recall`) | Fraction of GT labels covered by ≥1 chain. "Did we even notice?" |
| **evt_F1** | Harmonic mean of `evt_precision` and `evt_recall`. Penalizes both misses and over-firing on the same label. |
| **fpur** (`fire_purity`) | TP fires / total fires. "Of everything we fired, how much was real?" |
| **tyAcc** (`type_acc`) | Among in-GT fires, fraction whose `inferred_type` matches the GT label's `anomaly_type`. |
| **on_time_rate** | Among correctly-typed-matched labels, fraction whose alert arrived inside the per-type MET budget (see below). |
| **lat_frac_p95** | 95th percentile of `(latency_to_first_fire / label_duration)`. "How far into the label were we still silent, worst case?" |
| **uvfp/d** (`user_visible_fps_per_day`) | Suppression-survived FP chains per timeline day. The user's spam bar. |
| **n_labels** | Count of GT labels in this block (sample-size context for the rates above). |

---

## Sub-row breakdowns (reported, less commonly read)

| Metric | One-liner |
|---|---|
| `evt_precision` | TP chains / total chains. The precision side of `evt_F1`. |
| `evt_recall` | Labels with ≥1 TP chain / total labels. The recall side of `evt_F1`. |
| `time_f1` / `time_precision` / `time_recall` | Tick-level (not chain-level) coverage; useful for regression archaeology, not headline. |
| `n_fires` / `n_in_gt_fires` | Raw counts behind `fire_purity`. |
| `fp_fires_per_day` | Pre-suppression FP rate (vs. `uvfp/d` which is post-suppression). |
| `lat_frac_p50` / `lat_frac_max` | Median and worst-case fractional latency. |
| `n_typed_matched` | Denominator behind `on_time_rate` (correctly-typed-detected labels only). |
| `n_user_visible_fps` | Raw count behind `uvfp/d`. |
| `nondqg_latency_p95_s` | p95 latency in seconds, excluding DQG fires (DQG is sub-second by design and would dominate). |

---

## MET budgets (used by `on_time_rate`)

A label is "on time" iff `(alert_end − label_start) ≤ MET(anomaly_type)`.

| Anomaly type | MET (hours) |
|---|---:|
| `spike`, `dropout`, `extreme_value`, `water_leak_sustained` | 0.5 |
| `dip` | 2 |
| `level_shift`, `frequency_change` | 6 |
| `usage_anomaly`, `month_shift`, `calibration_drift` | 24 |
| `trend`, `degradation_trajectory`, `weekend_anomaly`, `time_of_day` | 48 |
| (anything unmapped) | 24 |

---

## Reading the suite output

- **Headline mean across 5 scenarios** (NOT including holdout) is what
  decides accept/reject on an iteration.
- **Holdout** is the canary — never used to drive decisions, only to
  detect overfitting after the fact.
- **`tyAcc = NaN`** means zero TP fires existed in that block — the
  classifier wasn't tested, not "perfect."
- **`on_time_rate = None`** means zero correctly-typed-matched labels
  (denominator empty); `incR` and `tyAcc` already cover that gap.
- **Past iters that report `time_F1` are NOT comparable** to current
  headline — the metric pivoted to per-fire grading on 2026-04-27.
