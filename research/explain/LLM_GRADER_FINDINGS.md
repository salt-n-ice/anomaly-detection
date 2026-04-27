# LLM-Grader Findings — run 20260425T154716Z

7 subagents, one per scenario, each acting as a smart-home product reviewer.
For each TP user_behavior label they (a) wrote the household notification a
good production LLM would produce from the prompt, then (b) scored it against
the GT on accuracy / actionability / clarity / calibration (1-5 each).

## Scoreboard

| scenario                  | n  | acc  | act  | clr  | cal  | overall |
|---------------------------|---:|-----:|-----:|-----:|-----:|--------:|
| **leak_30d**              |  6 | **5.00** | 4.67 | 5.00 | **5.00** | **4.92** |
| holdout_household_45d     | 10 | 3.80 | 4.20 | 5.00 | 4.20 | 4.30    |
| household_60d             | 12 | 3.75 | 4.17 | 4.92 | 4.25 | 4.27    |
| household_sparse_60d      |  4 | 4.00 | 3.75 | 5.00 | 4.25 | 4.25    |
| household_120d            | 23 | 3.48 | 4.00 | 5.00 | 4.04 | 4.13    |
| household_dense_90d       | 14 | 3.50 | 3.93 | 4.93 | 4.07 | 4.11    |
| single_outlet_fridge_30d  |  3 | 2.33 | 3.67 | 4.67 | 3.33 | 3.50    |

**Headline:** Mean accuracy across 72 labels = 3.78. Clarity is uniformly
high (~5.0) — the prompts read well; jargon hygiene is solid. The gap is
in *accuracy* (does the summary land on the actual anomaly?) — clusters
in two scenarios (hh120d, dense_90d) where DQG-suppression framing
dominates the highest-score chain.

**super_match overstates user-facing quality.** The metric optimized in
iters 001-004 hit 0.958 production / 1.000 holdout because it credits a
label if ANY overlapping chain matches super-class. The production LLM
sees ONE prompt per incident — almost always the highest-score chain.
For DQG-pre-typed labels, that's still a `presentation: infrastructure`
prompt telling the LLM to suppress, even though *another* chain on the
same label correctly classifies (and gets the super_match credit).

## Three concrete failure modes (15 flagged labels with accuracy < 3)

### 1. DQG infrastructure framing leaking through to the user-shown chain (~8 labels)

Despite iters 002-004 adding DQG override branches for `extreme_value`
and `out_of_range` on appliance caps, some chains don't match the
override conditions and retain the `presentation: infrastructure` banner
that explicitly tells the LLM to suppress.

Reproducer signatures from the grader critiques:
- `dropout` pre-type (not covered by either override) — `single_outlet_fridge_30d#041`
- `out_of_range` with `shwz=NaN` (peer history insufficient — early-scenario or rare-hour) — multiple hh120d level_shifts
- `out_of_range` with strong negative delta but `|shwz| < 3` AND `|delta_pct| < 3` (falls between H6.2 and H7v2 thresholds) — kettle/fridge level_shift cases

**The user sees:** "*We saw an unusual reading from the fridge outlet on
Friday afternoon that looks like a sensor or connection hiccup rather
than appliance behavior — no action needed.*" When in reality the fridge
behavior had genuinely level-shifted.

### 2. Single-fire bundles can't convey multi-day patterns (~5 labels)

`weekend_anomaly`, `trend`, `degradation_trajectory` GTs fundamentally
need cross-time context. The bundle gives `same_hour_weekday_z` (a single
peer baseline), but no "spans 14 days" or "fired 11× this week vs typical
3" signal.

Failure shape:
- `weekend_anomaly` GT, single Wednesday-evening chain emit → LLM writes
  "TV usage unusual on Wednesday evening" (correct for the chain,
  misses the weekend pattern entirely).
- `trend` / `degradation_trajectory` GT spanning weeks, single 1-min
  duty-cycle fire → LLM has no slope/drift evidence to surface.

### 3. `frequency_change` has no rate-of-events evidence in the prompt body (~2 labels)

Iters 003-004 fixed the *classification* (override OOR → frequency_change)
but the prompt body still just says "data_quality_gate: out_of_range".
The LLM has no way to know "this is one of 11 OOR fires this morning vs
typical 3 per morning" — i.e., the actual rate change.

The classification line says "Heuristic classifier: suggests
**frequency_change**", but with no body evidence, a calibrated LLM
defaults to "could be a sensor glitch" rather than "your kettle is
cycling more than usual".

## What works well (for future regression-test floor)

- **leak_30d** (4.92 overall, perfect accuracy + calibration on 6 labels):
  BINARY state transitions are unambiguous, the bundle gives sensor +
  location + transition direction, and the LLM produces specific
  action-oriented alerts without false certainty. Same shape applies to
  the dip cases (basement_temp), which leveraged the iter-001 direction
  fix and `same_hour_weekday_z` for calibrated magnitude.
- **Clarity is uniformly ~5.0** across the suite — no jargon leaking,
  prompt rendering is readable.
- **Calibration is ~4.0+** outside the DQG-suppression failure mode —
  the LLM gracefully equivocates when the bundle is genuinely ambiguous.

## Recommended next iters (consumer-IoT relevant)

- **P0: Promote DQG override coverage.** Add override paths for `dropout`
  pre-type and softer `delta_pct` thresholds (or fall back to magnitude-
  free reclassification on `power` capability when shwz is NaN).
  Expected impact: lift hh120d / dense_90d accuracy from ~3.5 to ~4.0+.
- **P0: Add cross-chain context signals to bundle.** A "this sensor fired
  N times in the last K hours / days" field would let the LLM detect
  weekend_anomaly, trend, frequency_change patterns the current per-
  chain bundle can't surface. Note: this is the cross-chain extension
  flagged in iter 004's follow-ups — out of scope for the explain layer
  as currently bounded.
- **P1: Emit explicit rate evidence in the prompt body for OOR
  frequency_change overrides.** When the iter-004 path fires, also
  surface "DQG fired N times in the last hour" so the LLM has body
  evidence to back the heuristic-classifier hint.
- **P2: Re-evaluate the per-label "best chain" selection rule.** Current
  highest-`bundle.score` rule favored DQG chains because their score is
  always 1.0. A user-facing notification system should likely favor a
  chain with `presentation: user_visible` if any exists, falling back
  to score-rank.

## Methodology caveats

- 72 labels / 7 scenarios, all synthetic — real-household data would
  surface different failure modes (noisier baselines, household-specific
  patterns, multi-appliance interference).
- Single-pass grader: each subagent both produced the summary AND scored
  it. Some self-flattery bias possible; the *flagged-label critiques*
  (where the grader explicitly called out "the prompt is the limiter")
  are the most signal-rich part of the output, not the absolute scores.
- "Best chain" selection picks highest `bundle.score`, which biases
  toward DQG (always score 1.0) over signal-driven chains (variable
  score). A different chain-selection rule could move scores
  substantially.
