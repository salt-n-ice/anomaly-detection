# Baseline

This file documents the frozen baseline — the metrics the research
loop must not silently regress. The machine-readable snapshot is
`BASELINE.json`; this file is the human-facing narrative.

**Headline metrics:** `behavior.incident_recall` (catch every real
anomaly) and `behavior.user_visible_fps_per_day` (chains classified
`user_behavior` that fire outside any GT label — same definition as
the viz layer's `user_visible_fps`, so the iter loop and the PDF
report agree by construction). `time_F1` is kept as a continuity
metric but is dominated by long labels.

## What "user_behavior" means

The pipeline summarizes **household behavior anomalies** to a
non-technical user via an LLM. Behavior anomalies are things the user
wants to be told about:
- "your fridge has been using more power for two weeks"
- "you went on vacation Mar 7-13"
- "you've shifted to working from home"
- "the basement has had three short leaks in the past two weeks"

Not:
- "the temperature sensor's calibration drifted by 1.5°C"
- "the kettle outlet's reporting rate slowed for a day"
- "the fridge sensor went offline for 45 minutes"

The first list is `label_class = user_behavior`; the second is
`label_class = sensor_fault`. Mapping lives in
`synthetic-generator/src/sensorgen/labels.py:USER_BEHAVIOR_TYPES` /
`SENSOR_FAULT_TYPES`.

Sensor_fault labels exist in the dataset for realism but are
*infrastructure*: the user-facing pipeline should suppress them from
LLM summaries, and we explicitly do NOT optimize for them. They are
kept in the eval table for visibility only.

## Scoring

`research/run_research_eval.py --diff-baseline` applies floors on the
BEHAVIOR block per scenario. Any single scenario crossing any floor →
REJECT.

### Aggregate floors (pipeline-wide on each scenario)

- **behavior.incident_recall** — drop > `--tol` (default 0.005).
  Hard floor: every user-behavior label MUST be covered by ≥1
  compatible-class detection. Missing a real anomaly is the worst UX.
- **behavior.time_f1** — drop > `--time-tol` (default 0.02).
  Length-weighted coverage metric (kept for continuity; dominated by
  long labels — see per-bucket floors below).
- **behavior.user_visible_fps_per_day** — rise > `--fp-rise-tol-rel`
  (default 0.10 = +10% relative). Counts chains classified
  `user_behavior` that fire outside any GT label on the same sensor —
  matches the viz layer's `user_visible_fps`, so this is the chain
  the user actually gets a notification for. When the old baseline
  has uv_fp/d < 0.5 and `--fp-abs-budget` is set, an absolute budget
  applies instead (covers the Stage 0 → Stage 1 transition where
  relative rise is undefined).
- **behavior.nondqg_latency_p95_s** — rise > `--lat-tol-s`
  (default 600s = 10min). Kept for continuity; the per-bucket
  fractional latency is the primary latency gate.

### Per-bucket floors (short / medium / long GT labels)

GT labels are bucketed by duration: **short** (< 1h), **medium**
(1h–24h), **long** (> 24h). This prevents length-weighted aggregates
from masking a regression on short-duration anomalies behind a gain
on long ones.

- **bucket.incident_recall** — drop > `--bucket-incR-tol`
  (default 0.005). Any bucket's recall can't regress.
- **bucket.time_recall** — drop > `--bucket-time-rec-tol`
  (default 0.05). Fraction of the bucket's GT-time covered.
- **bucket.lat_frac_p95** — rise above `--bucket-lat-frac-ceil`
  (default 0.10 = 10% of GT duration). A 30-min leak with a 5-min
  lag is 16.7% (fails); a 28-day shift with a 2-hour lag is 0.30%
  (passes). Replaces the flat 600s floor that over-penalized long
  and under-penalized short.

### Type-class filter (sensor attribution × claim correctness)

Each detection row carries an `inferred_class` column
(`user_behavior` | `sensor_fault` | `unknown`). The user_behavior
block only credits detections whose inferred class is `user_behavior`
or `unknown`; `sensor_fault`-class detections (DQG dropouts,
calibration_drift claims) are excluded. This prevents a DQG dropout
on `basement_leak` from being credited as TP against a
`water_leak_sustained` GT on the same sensor — a detection has to
hit the right sensor AND claim a compatible reason.

### Informational only

- `evt_f1` — chain-merge / chain-suppression changes routinely swing
  it ±0.05-0.10 without changing detection-time quality.
- `sensor_fault` block — infrastructure plumbing, never gates.
- Flat `nondqg_latency_p95_s` — dominated by long labels; kept for
  continuity but the per-bucket fractional latency is primary.

## Scenarios

Production (floor-gated):

| Scenario        | Source dir                                  | Timeline | #behavior | #fault |
|-----------------|---------------------------------------------|---------:|----------:|-------:|
| household_60d   | synthetic-generator/out/household_60d       |     60d  |        16 |      3 |
| household_120d  | synthetic-generator/out/household_120d      |    120d  |        31 |      4 |
| leak_30d        | synthetic-generator/out/leak_30d            |     30d  |         9 |      1 |

Holdout (info-only, surface overfit):

| Scenario                     | #behavior | Purpose                                   |
|------------------------------|----------:|-------------------------------------------|
| holdout_household_45d        | varies    | diff seed + diff label shapes vs prod     |
| single_outlet_fridge_30d     |         3 | minimal-config (single sensor)            |
| household_sparse_60d         |         6 | low-activity quiet household (fp should be LOW) |
| household_dense_90d          |        19 | dense/overlapping anomalies               |

## Baseline status

Re-anchored 2026-04-27 after iter 030 (default fuser gap 60min → 4h —
see ITERATIONS.md / LEARNINGS §12). Cooldown-rhythm fires that
previously emitted as separate user-visible chains now fuse into one
chain per anomaly window. **Every incR unchanged across all 7 scenarios;
production mean uv_fp/d 0.65 → 0.34 (-48%); holdout 0.67 → 0.44 (-34%).**

Prior anchor (iter 029, 6820938) had production uv_fp/d 0.65 / holdout
0.67. Prior to iter 029 (iter 023, 29bf2bb): 0.77 / 1.88. Prior to
iter 023 (fc4def9): 3.18 / various — those numbers reflected ~74%
z-inflation FPs from `outlet_tv_power × duty_cycle_shift_6h` on
bimodal-zero MAD-collapsed bootstrap.

**Production headline numbers (iter 030 at 9bd799f):**

| Scenario        | incR  | uv_fp/d | uv_fp | evt_F1 |
|-----------------|------:|--------:|------:|-------:|
| household_60d   | 0.917 |    0.48 |    29 |    n/a |
| household_120d  | 0.913 |    0.48 |    57 |    n/a |
| leak_30d        | 0.857 |    0.07 |     2 |    n/a |

Production mean: incR = **0.896**, uv_fp/d = **0.34**.

**Holdout headline numbers:**

| Scenario                 | incR  | uv_fp/d | uv_fp |
|--------------------------|------:|--------:|------:|
| holdout_household_45d    | 0.900 |    0.69 |    31 |
| single_outlet_fridge_30d | 1.000 |    0.07 |     2 |
| household_sparse_60d     | 0.750 |    0.57 |    34 |
| household_dense_90d      | 0.714 |    0.43 |    39 |

Holdout mean: incR = 0.841, uv_fp/d = 0.44.

**What this tells you:** the pipeline now emits **about 1 user-visible
false alarm every 3 days on production** (0.34/day) — comfortably below
deployable thresholds. The chain-merging mechanism (iter 030) is
LEARNINGS §12: the fuser's `gap` parameter must exceed each contributing
detector's `cooldown_s` for the user-visible-FP metric to count
notifications correctly. Pre-iter-030, every cooldown-period DCS-6h
fire was its own chain; post-iter-030, sustained fires fuse into one
notification per anomaly.

**Open mechanism gap:** time-of-usage anomalies on BURSTY outlets
(TV weekend_anomaly with similar total duty but shifted hours;
kettle time_of_day with similar magnitude but rare shifts) are NOT
detectable by any pure duty-magnitude detector. The labels lost on
hh60d (TV 2d weekend) and holdout_household_45d (TV 1d weekend) are
of this shape. `HourlyEventRateChiSq` (already implemented but
absent from BURSTY profile as of 2026-04-26) is the architecturally
correct complementary detector. Adding it is the natural Stage 5
candidate.

`leak_30d` and `single_outlet_fridge_30d` are unchanged from the prior
baseline — narrow-domain detectors with tight event semantics keep
FPs near zero with no DCS involvement.

**Deployment posture:** prod uv_fp/d 0.77 is a defensible household-
notification budget; the binding incR misses are mechanism-bounded
(time-of-usage shifts that no current detector can capture). Adding
HERS to BURSTY would lift incR back without re-introducing the
z-inflation FPs.

## How to read the baseline numbers

- **`incident_recall`** is the floor that matters most. If any
  behavior label goes uncovered, that's the worst possible UX.
- **`time_precision`** is historically the bleeding wound. The
  pre-redesign pipeline flagged "anomaly" over 65-97% of the time on
  non-anomalous stretches. Precision-first is the redesign's whole
  point.
- **`time_recall`** is easy to hit with a loose pipeline; it's
  meaningful only in conjunction with time_precision via `time_F1`.
- **`evt_F1`** looks good (0.78-0.98) even with bad time_precision
  because its 1h merge-gap collapses multi-day FP streaks into single
  "events." Do not use as a quality indicator.
- **`user_visible_fps_per_day`** is the count of user-visible
  user_behavior chains per day — the chain the user gets a
  notification for. Matches the PDF report's "user-visible false
  alarms" headline by construction (same definition: classified
  `user_behavior`, no overlap with any GT label on the same sensor).
  Replaces the prior `fp_h_per_day` time-weighted metric, which
  hid notification volume behind hour-integrals (a 28-day fake drift
  dominated; five short noisy chains barely registered).
