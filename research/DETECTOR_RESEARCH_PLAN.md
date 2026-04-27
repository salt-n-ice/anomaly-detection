# Detector Research Plan — SUPERSEDED

> **This plan is superseded by `PIPELINE_REDESIGN.md`.**
>
> This document assumed the current detector stack as a starting point
> and proposed replacements within it. The redesign flips that
> premise: start from an empty pipeline and add components on the
> ladder. Candidate detectors previously enumerated here
> (`BinaryWindowShift`, `LeakPersistenceDetector`, `RecentShift` on
> CONT, `StateConditionalShift`) now live in `HYPOTHESES.md` under
> the Stage they fit, or as ladder candidates in `PIPELINE_REDESIGN.md`.
>
> Kept for archival reference only. Do not drive iterations from this
> file.

---

This is the next research phase: stop spending most iterations on small
threshold nudges and start testing detector replacements more directly.

The process does **not** change. We still use the existing research loop:

`read state -> pick one detector hypothesis -> minimal change -> run -> accept/reject -> log/revert`

What changes is the unit of work. The unit is now:

- one detector family
- one archetype/capability slice
- one clear accept/reject verdict

## Why This Phase Exists

The current stack is:

- SHORT: `DataQualityGate`, `StateTransition`
- MEDIUM: `CUSUM`, `SubPCA`, `MultivariatePCA`
- LONG: `TemporalProfile`, `DefaultAlertFuser`

The current frozen baseline is still structurally bad for the task:

- worst behavior `time_F1`: `leak_30d = 0.0788`
- mean behavior `time_F1`: `0.416`
- mean behavior `fp_h_per_day`: `25.97`
- worst behavior `nondqg_latency_p95`: `1395s`

Recent iterations taught us something stronger than "keep tuning":

- detector-state changes can create real gains
- the current stack often trades FP-tail reduction against household latency
- the same families keep failing in the same way on BINARY motion

That means the bottleneck is not just parameter choice. It is detector fit to
the task.

## Current Failure Map

These are the live problems this phase should attack.

### BINARY motion / occupancy

Current dominant FP buckets are long max-span chains on motion sensors:

- `household_60d bedroom_motion {cusum,mvpca,temp}` ≈ `669 fp_h`
- `household_120d bedroom_motion {cusum,mvpca,temp}` ≈ `341 fp_h`
- `leak_30d utility_motion {cusum,mvpca,temp}` ≈ `96 fp_h`

What we already learned:

- earlier BINARY adaptation (`K=2`) improves overclaim but blows hh120d latency
- BINARY CUSUM cooldown also improves overclaim but blows hh60d/hh120d latency
- the existing post-mvpca `{cusum,mvpca}` gate helped, but the core tail remains

Interpretation:

- `CUSUM` on BINARY motion is likely carrying both useful onset sensitivity and
  destructive tail persistence
- a better detector here probably needs built-in decay / hysteresis rather than
  raw cumulative drift

### BINARY water

Live tail:

- `leak_30d basement_leak {cusum,mvpca}` ≈ `91.5 fp_h`

What we already learned:

- `TemporalProfile` was unsound on BINARY water and was removed successfully
- `StateTransition` already preserves incident recall for real leak onset

Interpretation:

- BINARY water may not need generic `CUSUM` at all
- a leak-specific persistence detector may be better than a generic drift detector

### CONTINUOUS

Live tails:

- `household_60d mains_voltage {cusum,mvpca,sub_pca,temp}` ≈ `345 fp_h`
- `household_120d mains_voltage {cusum,mvpca,sub_pca,temp}` ≈ `395 fp_h`
- `leak_30d basement_temp {cusum,mvpca,sub_pca,temp}` ≈ `66.5 fp_h`

What we already learned:

- the adapt-to-recent line is real and valuable
- CONT is the latency-sensitive archetype when adapt gets too eager
- `TemporalProfile` and `CUSUM` often stay active long after the label ends

Interpretation:

- CONT likely needs a detector that compares short-vs-long recent regime more
  directly, instead of accumulating indefinitely against a bootstrap-only mean

### BURSTY power

Live tails:

- `household_60d outlet_kettle_power {cusum,mvpca,sub_pca}` ≈ `234 fp_h`
- `household_60d outlet_tv_power {cusum,sub_pca,temp}` ≈ `192 fp_h`
- `household_120d outlet_fridge_power {cusum,mvpca,sub_pca}` ≈ `333 fp_h`
- `household_120d outlet_fridge_power {cusum,sub_pca}` ≈ `312 fp_h`

What we already learned:

- the old cross-chain BURSTY filters are helpful but not sufficient
- per-archetype adapt buffers helped BURSTY a lot, which means post-shift tails
  are still fundamentally a detector-state problem

Interpretation:

- BURSTY likely wants a state-conditional shift detector more than another
  generic PCA/cumulative-drift stack

## Rules For This Phase

- Test one detector idea at a time.
- Prefer one-file or two-file edits.
- Start with detector disable/replace audits before adding brand-new classes.
- If a detector family crosses a floor twice for the same mechanism, park it.
- Do not add a new detection band. Stay within SHORT / MEDIUM / LONG.
- Any hypothesis with `time_F1` movement under `0.002` on all scenarios is null.

## Experiment Ladder

Each lane below is meant to be run as a small chain of accept/reject experiments.

### Lane 1: BINARY motion replacement

This is the highest-priority lane.

#### 1A. Detector necessity audit

Hypothesis:

- `CUSUM` is net-negative on BINARY motion and should be removed or replaced there.

Minimal change:

- `src/anomaly/profiles.py`
- disable `CUSUM` for BINARY `capability=="motion"` only

Why first:

- cheapest way to measure dependency
- tells us whether `CUSUM` is essential for incident recall on motion labels

Acceptance signal:

- `leak_30d` or household motion tails shrink materially
- `incident_recall` stays intact
- `nondqg_latency_p95` does not worsen

Interpretation:

- if this works, replacement is easier than coexistence
- if recall drops, we need a new motion-specific onset detector before removal

#### 1B. Add a motion-specific dual-window detector

Candidate detector:

- `BinaryWindowShift`

Idea:

- compare recent `1h` / `6h` occupancy features against a trailing `24h` / `7d`
  baseline
- fire on large ratio or difference changes in `duty_cycle_1h`,
  `duty_cycle_24h`, and `transitions_per_hour`
- decay naturally once the short window converges to the long window

Why it fits the task:

- user_behavior labels on motion are occupancy / routine shifts
- this detector is explicitly about occupancy regime change, not cumulative drift

Minimum edit shape:

- `src/anomaly/detectors.py`: new class
- `src/anomaly/profiles.py`: register for BINARY motion

Acceptance signal:

- beats BINARY CUSUM disable on recall
- keeps the leak/household tail gains without the +921s latency trap

#### 1C. If needed, add hysteresis/refractory inside the new detector

Only do this if 1B improves headline but leaves short repeated chains.

### Lane 2: BINARY water simplification

This is the second-highest-priority lane because `StateTransition` already
gives us a strong onset anchor.

#### 2A. Detector necessity audit

Hypothesis:

- `CUSUM` is net-negative on BINARY water and can be disabled.

Minimal change:

- `src/anomaly/profiles.py`
- disable `CUSUM` for BINARY `capability=="water"`

Acceptance signal:

- `leak_30d basement_leak` tails collapse
- no incident-recall loss because `StateTransition` still covers onset

#### 2B. If 2A loses too much recall, add a leak-specific persistence detector

Candidate detector:

- `LeakPersistenceDetector`

Idea:

- fire when ON-state persistence or rolling duty cycle exceeds a leak-like
  threshold over a short wall-clock window
- do not use indefinite cumulative drift

Why it fits the task:

- leak labels are persistence events, not generic binary drift

### Lane 3: CONT replacement

This is the highest-upside structural lane after BINARY motion.

#### 3A. Add a recent-shift detector

Candidate detector:

- `RecentShift`

Idea:

- compare a short recent window against a trailing baseline window for `value`
  and maybe `value_roll_1h`
- score by normalized mean shift and/or variance shift
- built-in expiry because the short and long windows eventually match

Why it fits:

- mains voltage month_shift and basement_temp dip clusters are recent-regime
  problems, not "keep accumulating forever against day-0 mean" problems

Minimum edit shape:

- `src/anomaly/detectors.py`: new class
- `src/anomaly/profiles.py`: add to CONT medium band

Acceptance signal:

- better `time_F1` on hh120d/leak_30d without large latency penalty
- reduction in long `{cusum,mvpca,sub_pca,temp}` chains

#### 3B. If 3A works, test replacing CONT `CUSUM`

Do not stack too many detectors immediately.

Sequence:

- first add `RecentShift`
- if positive, disable CONT `CUSUM`
- rerun full suite

Goal:

- find out whether `RecentShift` is a better core detector than `CUSUM` for CONT

### Lane 4: BURSTY power replacement

This is the last lane because BURSTY already benefited most from accepted
adapt work, so the risk/reward is lower than BINARY/CONT replacement.

#### 4A. Add a state-conditional shift detector

Candidate detector:

- `StateConditionalShift`

Idea:

- compare current value / time-in-state against recent same-state history
- fire on persistent state-level mean changes
- expire when the new state history stabilizes

Why it fits:

- BURSTY appliance behavior is explicitly state-based
- this is closer to the semantics of kettle/fridge/tv behavior shifts than
  PCA residuals alone

#### 4B. If 4A works, test replacing BURSTY `TemporalProfile`

Reason:

- several live BURSTY FP buckets still include `TemporalProfile`
- it may be adding tail confirmation more than real onset value

## What To Stop Doing

Park these families unless a very narrow sensor-specific version emerges:

- BINARY earlier adapt trigger (`K=2`): rejected on hh120d latency
- BINARY `CUSUM` cooldown: rejected twice, same latency failure
- broad cross-sensor detector suppression without a capability gate

## Execution Order

Run the lanes in this order:

1. BINARY motion `CUSUM` disable audit
2. BINARY water `CUSUM` disable audit
3. `BinaryWindowShift` for motion
4. `LeakPersistenceDetector` if needed
5. `RecentShift` for CONT
6. CONT `CUSUM` replacement test
7. BURSTY `StateConditionalShift`
8. BURSTY `TemporalProfile` replacement test

## Per-Iteration Run Protocol

For each detector hypothesis:

1. State the hypothesis in chat.
2. State the expected direction per scenario.
3. Make the minimum code change.
4. Run the most relevant fast gate first:

   - BINARY motion: `--suite 120d` first
   - BINARY water or leak-specific: `--suite 30d` first
   - CONT: `--suite 120d` first, then `30d`
   - BURSTY: `--suite 60d` first, then `120d`

5. If the gate is promising and does not cross floors, run `--suite all --diff-baseline`.
6. ACCEPT / REJECT / PARTIAL using the same floors as `START_RESEARCH.md`.
7. Append to `research/ITERATIONS.md`.
8. If rejected, revert code and confirm baseline-zero diff.

## Acceptance Standard For A Detector

A detector idea is worth keeping only if it does at least one of these:

- becomes the new best detector for an archetype/capability slice
- enables removal of a weaker detector without hurting floors
- improves `behavior.time_F1` meaningfully on its target scenario and survives full-suite validation

A detector idea should be retired if:

- it crosses a floor twice for the same mechanism
- it only helps one scenario but repeatedly breaks another
- it needs large orchestration hacks just to behave

## Recommended First Iteration

Start with:

- disable `CUSUM` on BINARY motion only

Reason:

- it is the cheapest clean test of whether the worst current detector family
  is worth keeping on the slice that hurts the most
- it will immediately tell us whether the right next move is "replace" or
  "augment"
