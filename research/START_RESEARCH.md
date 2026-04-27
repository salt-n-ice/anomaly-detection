# START_RESEARCH

You are working on the `pipeline-redesign` branch. The approach is
**bottom-up, precision-first**, defined in `PIPELINE_REDESIGN.md`.

## Read state (once at start)

- `PIPELINE_REDESIGN.md` — which Stage you're on and what the
  stage's defining test is. If you don't know the Stage, go back
  and establish Stage 0 first.
- `LEARNINGS.md` — mechanisms that generalize, landmines to avoid,
  binding anti-overfit rules R1-R5.
- `DETECTOR_CANDIDATE_SURVEY.md` — detector-family palette +
  workload fingerprint protocol. Read when proposing a candidate;
  do NOT default to the pre-redesign inventory.
- `BASELINE.json` — numeric reference for the current pipeline.
  Until Stage 0 is frozen, this reflects the pre-redesign pipeline;
  treat as reference only.

Do **not** read `ITERATIONS.md` at session start — it's the per-iter
audit log, not context for the next iter.

## The loop

```
pick ladder stage → propose one candidate component → 
  ablate (run with + without) → decide keep/delete → log/commit/revert
```

### Before every iter, state (one line in chat):

1. **Current Stage** from `PIPELINE_REDESIGN.md`.
2. **Candidate** you're about to add or remove.
3. **Candidate discovery** — name the anomaly shapes this stage
   targets (from `WORKLOAD_FINGERPRINT.json`); consult
   `DETECTOR_CANDIDATE_SURVEY.md` §Selection heuristic; list the
   2–3 candidate families considered and why this one wins. If
   this is the first iter in a new stage, run the workload
   fingerprint protocol first and save the output.
4. **Mechanism hypothesis** — what signal does this component
   capture, and what failure mode does its absence cause? (If you
   can't name the mechanism, you're not ready to propose the
   change.)
5. **Expected direction** per scenario.
6. **What would make you REJECT** — a specific metric delta
   threshold that would flip the decision.

Anti-patterns (stop and course-correct if you see yourself doing this):
- "This detector-combo is N% FP on training" → `LEARNINGS.md` R1.
- "A shorter `max_span`/cap will fix it" → `LEARNINGS.md` L2 and L4.
- "We need to reject chain X because it's a wind-down" — ask first:
  **why is the detector firing during wind-down?** Fix the detector's
  wind-down behavior rather than filtering out the chain
  (`LEARNINGS.md` R4).

### Run the eval

```bash
# Default for any tuning iter — production + 2 random holdout.
python research/run_research_eval.py --suite iter --random-sample 2

# Full all-scenario audit (slower — ~10 min — run at stage
# boundaries and before merging).
python research/run_research_eval.py --suite all

# Freeze a new baseline (only when a stage completes cleanly).
python research/run_research_eval.py --suite all --save-baseline
```

### Verdict rules

- **ACCEPT:** all 5 scenarios pass floors AND the component pulls
  its weight (Stage-defined).
- **OVERFIT WARNING:** production passes, holdout floor hit. This is
  surfaced explicitly in `[OVERFIT WARNINGS]` block. Does NOT block
  the commit but demands a written one-paragraph analysis of WHY
  the holdout broke. If the cause is "holdout has a label shape
  we didn't anticipate," either (a) revise the component to handle
  that shape or (b) revert. Not both "accept and ignore."
- **REJECT (regression):** any production floor crossed.
- **REJECT (null):** no metric moves > 0.002.

### Log per iter

Append to `ITERATIONS.md` with:
- Stage + candidate component
- Mechanism hypothesis
- Result table (5 scenarios minimum)
- Verdict with reasoning
- Follow-ups

### Commit

- ACCEPT → commit (message starts with `stage(N):`).
- REJECT → `git checkout -- <files>` and verify clean with the full
  eval again.

## Stop and report when

1. **A Stage is complete** — freeze baseline, write up the stage
   summary in `PIPELINE_REDESIGN.md`, consult before starting the
   next Stage.
2. **Any OVERFIT WARNING** — don't automatically accept; produce the
   autopsy first.
3. **A component proposal requires a new `Detector` protocol or
   cross-sensor signal handling** — that's an architecture
   decision, escalate.
4. **The eval harness errors** or a new scenario fails to generate.

## Eval scenarios (current inventory)

Production (floor-gated):
- `household_60d` — 6 sensors, 60 days, 16 behavior labels
- `household_120d` — 6 sensors, 120 days, 31 behavior labels
- `leak_30d` — 3 sensors, 30 days, 9 behavior labels

Holdout (info-only):
- `holdout_household_45d` — 6 sensors, 45 days, diff seed + diff
  label shapes than production (tests overfit)
- `single_outlet_fridge_30d` — 1 sensor, 30 days, 3 labels
  (tests minimal-config)
- `household_sparse_60d` — 6 sensors, 60 days, 6 labels
  (tests low-activity quiet household; uv_fp/d should be LOW)
- `household_dense_90d` — 6 sensors, 90 days, 19 labels
  (tests dense/overlapping anomalies)

Add new holdout scenarios whenever a real-world behavior shape
isn't represented. Do NOT tune against holdout — it's diagnostic.

## Begin

Start at Stage 0. Read `PIPELINE_REDESIGN.md` §"Next concrete step"
and establish the empty-pipeline baseline before proposing any
additions.
