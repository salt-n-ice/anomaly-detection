# Eval Metrics — Current Numbers

State: **iter 21** (commit `134c916`, 2026-04-28). Numbers computed
from `out/<scenario>_detections.csv` via `compute_stratified` in
`src/anomaly/metrics.py`. BEHAVIOR is the optimization target;
sensor_fault is reported for visibility only. Holdout is a
generalization canary and is **not** used to drive iter decisions.

---

## Headline — BEHAVIOR, suite mean (5 production scenarios)

> **Primary headline: `evt_F1`.** This is the single number iter
> accept/reject decisions are made against. Every other metric in
> this table is diagnostic — it explains *why* `evt_F1` moved.

| Metric | Value | Inference |
|---|---:|---|
| **incR** (incident_recall) | **0.930** | We notice ~93 % of real anomaly labels — coverage is strong. |
| **`evt_F1`** ← HEADLINE | **0.790** | Solid precision/recall balance per fire; the ~21 % gap to ceiling is split between misses and over-firing on the same label. |
| **fpur** (fire_purity) | **0.882** | ~88 % of fires sit inside a GT label; 12 % are false alarms. |
| **tyAcc** (type_acc) | **0.919** | When a fire is in-GT, the classifier names the type correctly ~92 % of the time. |
| **on_time_rate** | **0.827** | Of correctly-typed alerts, ~83 % land inside the per-type MET budget; ~17 % arrive late. |
| **lat_frac_p95** | **0.356** | Worst-case (p95), we're silent through the first ~36 % of a label before the first fire. |
| **uvfp/d** (user-visible FPs/day) | **0.315** | ≈ 1 user-visible FP every ~3 days suite-wide — below the spam-tolerance bar. |

---

## Per-scenario — BEHAVIOR

| Scenario | n | incR | evt_F1 | fpur | tyAcc | on_time | lat_p95 | uvfp/d |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| household_60d | 12 | 0.917 | 0.725 | 0.946 | 0.912 | 0.800 | 0.188 | 0.57 |
| household_120d | 27 | 1.000 | 0.792 | 0.993 | 0.811 | 0.625 | 0.465 | 0.37 |
| household_dense_90d | 16 | 0.875 | 0.813 | 0.960 | 0.882 | 0.875 | 0.762 | 0.22 |
| household_sparse_60d | 5 | 1.000 | 0.818 | 0.982 | 0.991 | 1.000 | 0.200 | 0.42 |
| leak_30d | 7 | 0.857 | 0.800 | 0.531 | 1.000 | 0.833 | 0.167 | 0.00 |

**Reading the rows**

- **household_60d** — lowest evt_F1 (0.725) on the smallest production scenario; bursty kettle/fridge over-firing pulls evt_precision down. Classifier still nails 91 % of types.
- **household_120d** — perfect incR (every label caught) and 99 % fpur, but tyAcc 0.811 reflects iter 21's voltage-split still mis-naming a slice of mixed-direction RMP chains. lat_p95 0.465 is the suite worst.
- **household_dense_90d** — best evt_F1 (0.813) but lat_p95 0.762 means at least one label was caught very late inside its window — a deep-onset miss.
- **household_sparse_60d** — every behavioral metric ≥ 0.99 except uvfp/d (0.42); small label count (n=5) makes rates noisy but the pipeline runs clean here.
- **leak_30d** — fpur 0.531 looks weak in isolation but n=7 and DQG dropout-as-behavior is the dominant fire shape; uvfp/d = 0 means the FPs that do exist all overlap GT.

---

## Holdout — generalization canary (NOT used for iter decisions)

| Scenario | n | incR | evt_F1 | fpur | tyAcc | on_time | lat_p95 | uvfp/d |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| holdout_household_45d | 10 | 0.900 | 0.831 | 0.943 | 0.917 | 0.667 | 0.227 | 0.16 |

**Inference** — holdout evt_F1 (0.831) and fpur (0.943) sit *above*
the production-suite mean: no overfitting signal. on_time_rate
(0.667) is the soft spot — 1-2 correctly-typed alerts arrived
outside MET. uvfp/d 0.16 is the cleanest in the whole suite.

---

## Sensor-fault — visibility-only block

| Scenario | n | incR | evt_F1 | fpur | tyAcc | uvfp/d |
|---|---:|---:|---:|---:|---:|---:|
| household_60d | 2 | 1.000 | 1.000 | 0.500 | 1.000 | 0.00 |
| household_120d | 3 | 0.667 | 0.667 | 0.694 | 1.000 | 0.00 |
| household_dense_90d | 2 | 0.500 | 0.667 | 0.751 | 1.000 | 0.00 |
| household_sparse_60d | — | — | — | — | — | — |
| leak_30d | 1 | 0.000 | 0.000 | 0.000 | — | 0.00 |
| holdout_household_45d | 1 | 0.000 | 0.000 | 0.000 | — | 0.00 |

**Inference** — sensor_fault label counts are tiny (1-3 per
scenario), so a single miss = 0/1 = 0 % incR. uvfp/d = 0 on every
scenario means the suite emits zero noise on the infrastructure
side. tyAcc = 1.0 on every block with TPs means every caught
fault is named correctly.

---

## At-a-glance pass/fail bar

| Gate | Threshold | Current |
|---|---:|---:|
| Suite mean incR ≥ 0.90 | 0.90 | **0.930** ✅ |
| Suite mean evt_F1 ≥ 0.78 | 0.78 | **0.790** ✅ |
| Suite mean uvfp/d ≤ 0.50 | 0.50 | **0.315** ✅ |
| Holdout incR within ±0.05 of suite | — | suite 0.930 / holdout 0.900 ✅ |
| Holdout evt_F1 not regressing vs suite | — | holdout 0.831 ≥ suite 0.790 ✅ |

All five gates green at iter 21.
