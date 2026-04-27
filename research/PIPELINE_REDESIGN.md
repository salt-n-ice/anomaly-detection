# Pipeline Redesign: Bottom-Up Precision-First

## The problem

A top-down pipeline (every detector fires, filter rules suppress FP) has
two failure modes:

1. **Filter rules overfit.** "Rule X rejects 94% FP on the current data"
   is sampling error, not a mechanism. These rules break on holdout with
   slightly different label shapes.
2. **Detectors aren't carrying their weight.** If a detector's output
   needs to be overridden by ~15 fusion-rule branches, the detector is
   the wrong shape for the task; the rules are inventing metadata to
   discard its fires.

The anchor observation: **"start with no anomalies detected and go
from there."** A pipeline that detects nothing has precision = 1.0,
recall = 0.0, user_visible_fps_per_day = 0.0. From that anchor, every added
component must justify its existence by bringing recall UP without
dropping precision below an agreed floor.

## Core principle

> **Minimum Viable Pipeline (MVP):** the smallest set of components
> that still catches the incident_recall-critical behaviors.
> Everything else is negotiable.

Every detector, fusion rule, and corroboration rule must defend its
place against deletion. If removing it does not drop
`behavior.incident_recall` on any scenario, it's not load-bearing —
it's either inert or net-negative.

## The ladder (how to build up)

Build the pipeline in stages. At each stage, measure all scenarios
(production + holdout). A stage is accepted only if it improves recall
without breaking the precision floor.

### Stage 0: empty pipeline
- No detectors enabled.
- Expected: all labels missed, `incR = 0` everywhere.
- This is the starting precision ceiling (1.0) against which every
  addition is measured.

### Stage 1: deterministic triggers only
- `StateTransition` on BINARY water + BINARY motion (deterministic,
  high-precision-by-design).
- `DataQualityGate` on all sensors (dropout, out_of_range, stuck_at,
  clock_drift — sensor_fault class, but needed for pipeline sanity).
- **Defining test:** does `behavior.incident_recall` on
  `single_outlet_fridge_30d` stay at 0 (no motion/water sensor)?
  Does it reach 1.0 on `leak_30d` for `water_leak_sustained` labels?

### Stage 2: one CONTINUOUS detector
- Add a single CONTINUOUS detector. Candidate per
  `DETECTOR_CANDIDATE_SURVEY.md` §Selection heuristic, grounded in
  the current `WORKLOAD_FINGERPRINT.json`; pre-redesign inventory
  is reference only, not the menu.
- Measure. The one with the highest **marginal precision** wins.
- **Defining test:** does adding this detector lift
  `mains_voltage` / `basement_temp` incident_recall without crossing
  +0.20 on `user_visible_fps_per_day` from Stage 1?

### Stage 3: one BURSTY detector per archetype
- Same procedure as Stage 2, for BURSTY power outlets. Candidate
  per `DETECTOR_CANDIDATE_SURVEY.md` selection heuristic on the
  BURSTY rows of the workload fingerprint.
- Hardest targets: sustained 28-day appliance shifts. Each candidate
  must fire within the label AND not fire in the weeks after label end.

### Stage 4: corroboration (only if Stage 2/3 single-detector
precision is too low)
- Combine 2 detectors. Only fire on their agreement.
- Measure; if precision rises but recall holds, keep.

**Status (2026-04-25):** Stage 4 closed at iter 021 (commit 06ae65b)
under the OR-fire (orthogonal-coverage) interpretation rather than the
strict AND-fire interpretation. iter 021 added `RollingMedianPeakShift`
alongside the iter 017 `DutyCycleShift` in `BURSTY.medium`. Mechanism
diversity per LEARNINGS §9 (duty ⊥ peak ⊥ rate) — duty-cycle integrates
event rate via time-in-state, RollingMedianPeak captures per-event peak
magnitude. iter 022 confirmed adding `EventRateShift` as a 3rd BURSTY
detector is REDUNDANT with DutyCycleShift on this dataset (rate-shifts
also change duty), so the orthogonal triple collapses to a duty/peak
pair.

Strict AND-fire variant not pursued: detector audit on iter 021 showed
~6+ labels caught by single-detector chains (e.g., fridge degradation
duty-only, fridge frequency_change peak-only, kettle weekend duty-only).
AND-fire would lose those TPs. The OR-fire pipeline retains coverage
while still providing chain-tag-level discrimination signal:
`{duty}` chains → rate-class behaviors; `{peak}` chains → magnitude-class;
`{duty + peak}` chains → combined level_shift. Discrimination at the
explain-layer level (HYPOTHESES.md EX1) is the natural follow-on.

**Stage 4 result vs Stage 0 anchor (production):**
- Mean incR: 0.476 → 0.938 (+0.462)
- Mean fp_h/d: 2.37 → 0.61 *(historical, old metric)*
- Holdout mean incR: 0.964 (4 scenarios)

**Note (2026-04-26):** the FP gate metric was switched from
`fp_h_per_day` (time-weighted) to `user_visible_fps_per_day` (chain
count, matches viz `user_visible_fps`). Pre-2026-04-26 fp_h/d numbers
above are not directly comparable to current uv_fp/d numbers. New
production baseline at fc4def9: mean incR 0.938 unchanged, mean
uv_fp/d **3.18** (hh120d 5.39, hh60d 4.08, leak 0.07). The same
chains are firing — the metric just stopped collapsing them into
small hour-integrals. See `BASELINE.md` §"Baseline status".

**Note (2026-04-26 later):** Stage 4 closure re-anchored at iter 023
after a one-day audit showed 74% of production behavior FPs came from
`outlet_tv_power × duty_cycle_shift_6h` via bootstrap-MAD-collapse
z-inflation (LEARNINGS §10). DCS now applies a percentile-novelty
gate when boot_mad collapsed — fires only when live duty falls
outside the bootstrap [q01, q99] envelope. New production baseline:
mean incR **0.896** / mean uv_fp/d **0.77** (a -0.04 incR change
that reflects filtering of statistical-fluke "TPs" along with the
FPs they masked). See `BASELINE.md` §"Baseline status" (re-anchored
2026-04-26) and `ITERATIONS.md` iter 023 (ACCEPT, re-framed). The
deferred mechanism gap — time-of-usage anomalies on BURSTY outlets
that no duty-magnitude detector can capture — moves to Stage 5.

**Stage 4 follow-up: detector-internal self-adapt mechanism (LEARNINGS §2a).**
RollingMedianPeak's cooldown (6h) > BURSTY fuser gap (1h), so each fire
is a singleton chain — the pipeline.py K=3 max_span streak adapt hook
never triggers. Detector-internal counter (3 consecutive cooldown-spaced
fires with 24h-quiet reset) is the architectural analog. Reusable for
any future cooldown-spaced fast-fire detector.

### Stage 5: cross-sensor detector (the big hypothesis)
- A new detector that fires on **correlated** changes across multiple
  sensors: vacation (low kettle + low tv + low motion for >24h),
  shift-work (motion at unusual hour + kettle at unusual hour on the
  same day), etc.
- This is a NEW component, not a tune of existing ones.
- Expected to be the single largest behavior-recall lift if it works.

### Stage 6: filter rules (last, not first)
- Add corroboration rules or detector-combo rejections ONLY if
  Stages 1-5 have a stable precision/recall Pareto front and some
  specific, identified FP bucket remains. Never start here.

## Methodology per stage

For each candidate addition:

1. **Ablation run:** measure all scenarios WITH and WITHOUT the
   component.
2. **Marginal contribution:** compute deltas on:
   - `incident_recall` per bucket (short/medium/long)
   - `time_recall` per bucket
   - `lat_frac_p95` per bucket (fractional latency, 10% ceiling)
   - `user_visible_fps_per_day` (absolute budget during Stage 0 → 1,
     relative rise thereafter)
3. **Go/no-go:**
   - If any bucket's `d_incR > +0.05` on a critical scenario AND no
     bucket regresses AND `uv_fp/d` stays within budget: **keep**.
   - If `d_incR ≤ +0.02` across every bucket on every scenario:
     **delete** (component isn't pulling weight).
   - Otherwise: investigate whether the component needs a filter to
     be useful. A component needing 3 filter rules is probably the
     wrong component.
4. **Write a one-paragraph mechanism justification.** "This fires on X
   because Y." No statistical claims about training-set FP rates
   (see `LEARNINGS.md` R1).

**Key metric properties (see `BASELINE.md` §Scoring):**

- Metrics are stratified by GT label duration (short/medium/long).
  A change that helps long-shift recall but trashes short-leak
  recall fails on the short bucket instead of washing out in the
  aggregate.
- Each detection's `inferred_class` (user_behavior / sensor_fault /
  unknown) must be compatible with the block's class. DQG dropout
  claims don't get credit for water_leak_sustained TPs.
- Latency is measured as a fraction of the GT label duration, not
  absolute seconds. A 5-minute lag on a 30-min leak is 16.7% (bad);
  a 2-hour lag on a 28-day shift is 0.30% (fine).

## Evaluation harness

```
python research/run_research_eval.py --suite iter --random-sample 2
```

This runs 3 production scenarios (floors apply; regression = REJECT)
plus 2 random holdout scenarios (surface overfit as warning). Every
proposed addition must pass on all 5. At stage boundaries, run
`--suite all` to confirm all 7 scenarios.

## Pre-redesign inventory (reference, not the candidate menu)

This table lists what the pipeline had before the redesign. It is
**not** the menu to pick from at each stage — see
`DETECTOR_CANDIDATE_SURVEY.md` for the full palette + selection
heuristic. A pre-redesign component re-enters the pipeline only if
its property profile wins the selection heuristic against the
broader survey on the current workload fingerprint.

| Component | Band | Archetypes | Purpose |
|---|---|---|---|
| DataQualityGate | SHORT-event | all | DQG (fault detection) |
| StateTransition | SHORT-tick | BINARY | deterministic trigger |
| CUSUM | MEDIUM-tick | BURSTY, BINARY water, CONT | drift |
| RecentShift | MEDIUM-tick | BINARY motion | short-vs-long shift |
| SubPCA | MEDIUM-tick | BURSTY, CONT | per-state PCA |
| MultivariatePCA | MEDIUM-tick | all | multi-feature PCA |
| TemporalProfile | LONG-tick | all | hourly-bucket z-score |
| DefaultAlertFuser | orchestration | all | chain fusion |
| ContinuousCorroboration | filter | CONT | reject weak combos |
| PassThroughCorroboration | filter | BURSTY/BINARY | reject weak combos |

Any component absent from the accepted ladder at stage completion
should be removed from `profiles.py`.

## Open questions (resolve during stage builds)

1. **Which detector family gives the most CONTINUOUS recall per unit
   FP?** Run the workload fingerprint protocol; apply
   `DETECTOR_CANDIDATE_SURVEY.md` §Selection heuristic to the
   CONTINUOUS rows; ablate the top 2–3 candidate families (not
   limited to the pre-redesign inventory).
2. **Can TemporalProfile be eliminated entirely?** If it's not
   load-bearing for any label's incident_recall, delete the detector.
3. **Should CUSUM be split per sensor-cadence?** ZOH variance collapse
   (see `LEARNINGS.md` §1) may not generalize across sensors with
   different heartbeat intervals.
4. **What would a cross-sensor household detector look like?** It
   needs to consume features from multiple sensors simultaneously —
   the current `Detector` protocol is per-sensor. Likely a new
   component type (`HouseholdDetector`?).

## Next concrete step

Before any Stage 1 work, establish the empty-pipeline baseline.
Disable all detectors except `DataQualityGate` and `StateTransition`
(so the pipeline still runs without errors) and measure all
scenarios. Those numbers become the Stage-0 anchor. Every subsequent
stage compares to that.
