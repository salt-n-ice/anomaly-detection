# Eval Metrics — Reading Guide

The eval splits ground-truth labels into two blocks and computes the
same metrics on each:

- **behavior** — `user_behavior` labels.
- **sensor_fault** — infrastructure faults (`dropout`,
  `calibration_drift`, etc.).

Detections are filtered per-block by `inferred_class`: a chain
claiming to be `user_behavior` is only credited against
`user_behavior` GT, never `sensor_fault` GT (and vice versa). Chains
with `inferred_class == unknown` count for both.

All metrics below come from `compute_stratified` in
`src/anomaly/metrics.py`. Latency comes from
`scripts/latency_report.py`.

---

## `incident_recall` (`incR`)

Fraction of GT labels with **at least one matching detection**. One
fire inside the label window counts the label as caught.

- `1.000` — every GT label was caught at least once.
- `0.500` — half the labels were missed entirely.

---

## `evt_F1`

Harmonic mean of event-level precision and event-level recall.
Combines "did we catch each label" with "did we fire too many extra
chains" into one number.

- `1.000` — every label caught, no extra chains.
- `0.700` — meaningful alerts with a noticeable FP tail.

---

## `fire_purity` (`fpur`)

Fraction of **fire ticks** (not chains) that land inside any GT
label. A chain has many fire ticks (one per detector emit); per-fire
grading rewards chains that fire densely inside a label more than
chains that bridge briefly.

- `1.000` — every fire tick was in-GT.
- `0.500` — half of fires were outside any GT.

If `fpur` drops while `evt_F1` holds steady, in-label fires are being
suppressed without removing FPs.

---

## `type_acc` (`tyAcc`)

Of fire ticks that landed in-GT, the fraction whose `inferred_type`
matches the GT `anomaly_type` exactly.

- `1.000` — every in-GT fire correctly typed.
- `0.800` — 20% of correctly-located fires got the wrong type.

A misclassified TP still counts as caught for `incR`, but the LLM
downstream sees the wrong type.

---

## `user_visible_fps_per_day` (`uvfp/d`)

Chains classified `user_behavior` that **don't overlap any GT label**
(any class) on the same sensor, normalized by scenario timeline in
days. Any-class overlap exempts: a `user_behavior` chain hitting a
`sensor_fault` GT label is not counted as a user-visible FP.

- `0.00` — no false alerts visible to the user.
- `0.50` — about one false alert every two days.
- `5.00` — five false alerts a day.

---

## On-time rate + median absolute latency

From `scripts/latency_report.py`. Two numbers per block:

1. **on-time rate** — fraction of *correctly-typed-detected* labels
   where the alert fires within `MET(label_type)` of label start.
2. **median absolute latency (h)** — typical time-to-alert, in hours.

A label is correctly-typed-detected if at least one chain overlaps
it AND that chain's `inferred_type` matches the label's
`anomaly_type`. Per label, the EARLIEST matching chain's `end`
(chain emit / `window_end`) is the alert time.

`MET` is the **user-expectation budget** — the latest the alert can
arrive and still be useful to a human:

| anomaly_type             | MET   | rationale                                                            |
|--------------------------|-------|----------------------------------------------------------------------|
| `spike`                  | 0.5h  | instant trigger, single tick                                         |
| `dropout`                | 0.5h  | heartbeat lapse                                                      |
| `extreme_value`          | 0.5h  | DQG threshold breach                                                 |
| `water_leak_sustained`   | 0.5h  | "stop the leak now"                                                  |
| `dip`                    | 2h    | 1h analysis window + fuser emit slack                                |
| `level_shift`            | 6h    | bias is instant; CONT detector should catch within window            |
| `frequency_change`       | 6h    | within-label catch (labels span 2-8h)                                |
| `usage_anomaly`          | 24h   | day-level outlier, alert next morning                                |
| `trend`                  | 48h   | gentle slopes need 24-48h of accumulation                            |
| `month_shift`            | 24h   | sustained shift, classifier needs ~1d                                |
| `calibration_drift`      | 24h   | detect by label midpoint                                             |
| `degradation_trajectory` | 48h   | slow slope, multi-day                                                |
| `weekend_anomaly`        | 48h   | alert by end of weekend, or by mid-week for weekday-pattern          |
| `time_of_day`            | 72h   | physical floor — needs Sat + Mon + Tue (cross-day evidence)          |

Most rows are user-expectation budgets. `time_of_day` 72h is also a
physical floor: the classifier rule structurally needs three days
(weekday + weekend evidence) before it can route a chain to that
type.
