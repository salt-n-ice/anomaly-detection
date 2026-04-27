# Explain-quality hypotheses backlog

Forward-looking candidate ideas that don't yet fit a specific iter.
Add to it when an idea appears mid-iter that's out of scope; pull from
it when picking the next iter.

## Convention

- `P<n>` = priority (P0 highest).
- `L<n>` = estimated risk of regression (L0 lowest).
- `Edit:` = concrete file + symbol to touch.
- **No iteration numbers. No past-trial diff tables.** Use
  `EXPLAIN_ITERATIONS.md` for history.

---

## P0 (LLM-grader-derived, see LLM_GRADER_FINDINGS.md)

These items come from the LLM-grader pass run after iter 004. They are
**structurally insensitive to the headline `super_match_rate` metric**
(at ceiling: 0.958 prod, 1.000 holdout) — both the per-label rule
(any-chain match) and the per-best-chain rule (LLM-grader inputs)
apply, but only the latter is moveable. Verification on these iters
requires running the LLM-grader (`python research/explain/llm_grader.py
prepare --run latest`, dispatch graders, then `aggregate`) — the iter
loop's headline gate alone is insufficient to ACCEPT or REJECT.

- **Sub-1-hour dropout level_shift override** (L3 — risky). Post iter
  007 there are still 2 hh120d/hh60d outlet_fridge_power level_shift
  labels whose best chain is DQG `dropout` with duration just under
  1 hour (2977s and 3000s). The iter-006 / iter-007 1-hour floor
  protects against the fridge_30d#041 sensor_fault trap; lowering it
  would re-expose that trap. Possible alternative: a much higher
  magnitude floor (|delta_pct| ≥ 500) for sub-1h dropouts. Risky and
  needs a careful FP audit. Edit: `classify.py`.

- **Lower iter-003 OOR shwz threshold to 2.5 for power capability**
  (L2). 1 dense_90d outlet_kettle_power level_shift label has best
  chain `out_of_range` with shwz=-2.77 — just barely outside iter-003's
  |shwz|≥3 threshold. Audit candidates: any OOR-on-power chain where
  2.5 ≤ |shwz| < 3. Risk: regresses cases where the OOR is a noise-
  floor trip with marginal peer evidence. Edit: lower
  `_DQG_LEVEL_SHIFT_SHWZ_THRESHOLD` from 3.0 to 2.5 — mirrors iter-007's
  dropout threshold. (Note: iter 003's commentary says 3.0 was chosen
  conservatively because OOR value excursions have noisier shwz than
  dropout cases at the off-marker; lowering needs evidence the noise
  floor is actually higher.)

- **Robust typical-rate** (L1, follow-up to iter 009). Iter 009 ships
  scenario-mean typical_dqg_fires_per_24h, which contaminates with the
  anomaly window itself on sensors where the burst is a large fraction
  of total DQG fires (e.g., outlet_kettle_power on hh120d: typical
  33.73 vs recent 48 = 1.4x; uncontaminated typical probably ~5-10/day
  → 5-10x contrast). Compute typical from the bootstrap window (first
  14d) or exclude ±24h around the alert. Higher leverage on rate-shift
  cases that iter 009 only weakly resolved.

- **Change per-label "best chain" selection rule in production**
  (L0 — outside explain-layer code). The current `bundle.score`-rank
  rule biases toward DQG chains (always score 1.0) over signal-driven
  chains. A user-facing notification system should prefer
  `presentation: user_visible` chains when one exists, falling back to
  score-rank. Not an explain-layer change per se; flagged here because
  it changes which prompt the LLM sees and therefore the LLM-grader
  scoreboard substantially.

## P1

- **Add per-detector direction synth in `_synth_detector_context`**
  (L1). The mag.delta fallback shipped in iter 001 fixes _classification_
  but bundles still render
  `(per-detector context dicts unavailable on this alert; …)` for
  recent_shift / sub_pca / multivariate_pca / bocpd in the CSV path. A
  follow-up pass would synth a per-detector dict (mirroring the cusum
  case) so the prompt's "Detector evidence" block carries the same signal
  as the live pipeline path. _Not_ a metric move on its own (mag.delta
  fallback already drives classify) — quality lift comes from richer
  prompt body, which the headline metric does not measure.
  Edit: `src/anomaly/explain/magnitude.py::_synth_detector_context` —
  add elif branches for `recent_shift`, `sub_pca`, `multivariate_pca`.

## P2 (escalation — bundle structure changes)

- **Add cross-chain context signals to the bundle** (L4 — needs design
  discussion). Per-chain bundles fundamentally cannot convey multi-day
  patterns. weekend_anomaly / trend / degradation_trajectory GTs are
  unreachable from a single 1-minute chain emit (~5 LLM-grader-flagged
  labels). Possible fields: "fired N times in last K hours / days",
  "weekday-vs-weekend baseline split when both sides have ≥4 samples",
  "duration of label-coverage by overlapping chains". This is the
  metric ceiling without it. Out of current explain-layer scope per
  START doc §4 — escalate before working.

## Completed / retired

- **iter 001 — mag.delta-sign fallback for CONT direction.** ACCEPT.
  Lifted leak_30d super 0.833 → 1.000.
- **iter 002 — DQG extreme_value → spike/dip on appliance caps with
  |shwz|≥6 + |delta_pct|≥100.** ACCEPT. Lifted hh120d super
  0.783 → 0.826 (+0.043), dense_90d super 0.786 → 0.857 (+0.071).
- **iter 003 — DQG out_of_range → level_shift on power with |shwz|≥3.**
  ACCEPT. Lifted holdout_45d 0.900 → 1.000 (+0.100), dense_90d
  0.857 → 0.929 (+0.071). Production NULL (kettle level_shift labels
  already matched via duty/peak chains).
- **iter 004 — DQG out_of_range → frequency_change on power |shwz|<3
  + |delta_pct|≥3.** ACCEPT. Lifted hh60d 0.833 → 0.917 (+0.083),
  hh120d 0.826 → 0.957 (+0.130), dense_90d 0.929 → 1.000 (+0.071),
  fridge_30d 0.667 → 1.000 (+0.333). Cumulative diff vs 9ccbbc9:
  mean prod super 0.816 → 0.958, mean holdout super 0.838 → 1.000.
- **iter 005 — NaN-shwz OOR-on-power magnitude fallback.** NULL,
  REVERTED. Eval ran clean (no super_match regression); deterministic
  diff of LLM-grader inputs returned 0/72 best-chain changes because
  every NaN-shwz chain has an iter-003-matched valid-shwz sibling that
  wins the per-label case_id tie-break. Mechanism is sound; the metric
  it would have moved (per-label best-chain framing) is not visible to
  super_match_rate. See EXPLAIN_ITERATIONS.md.
- **iter 006 — DQG dropout + duty co-fire + duration≥1h → level_shift
  on power.** ACCEPT. No super_match movement (already-ceiling); no
  class_match regression (the 1-hour duration floor blocks the false
  fridge_30d#041 discriminator); +1 best-chain framing flip on
  dense_90d outlet_kettle_power (dropout/infrastructure → level_shift/
  user_visible/low). LLM-grader rescore on dense_90d: that label's
  accuracy lifts 2 → 4 (+2). Production gate clean.
- **iter 007 — DQG dropout + dur≥1h + (|shwz|≥2.5 OR |delta_pct|≥100)
  on power (no-duty corroborator path).** ACCEPT. Same gate clean
  pattern as iter 006; +1 additional best-chain framing flip on
  hh120d outlet_kettle_power level_shift (dropout/infrastructure →
  level_shift/user_visible/low). LLM-grader: that label's accuracy
  lifts 2 → 4 (+2). Same dur≥1h floor protects against the dropout-
  GT trap on shorter fridge_30d-style cases.
- **iter 008 — Rate-of-events context in DQG-pre-typed prompts.**
  ACCEPT. Pure prompt-body enrichment (csv.py + prompt.py); no
  classifier change, no structural trap. Adds "DQG fired N times in
  last 1h / 24h" line to all DQG-pre-typed bundles. Production gate
  NULL (no classification change). LLM-grader cross-scenario
  validation: hh120d +0.35 mean accuracy (7 items up, 0 down vs iter
  007), dense_90d +0.21 mean accuracy (4 up, 1 down — drop is grader
  noise). Standout: hh120d#6152 frequency_change rises 1→3 even
  though the classifier still labels it out_of_range with
  infrastructure banner — body evidence rescues quality on top of
  unchanged framing. Cumulative session (iters 005-008): 0 super
  movement (ceiling), 2 best-chain framing flips (iters 006/007), 1
  scenario-wide quality lift (iter 008), 0 class_match regressions.
- **iter 009 — Typical-rate baseline alongside recent rate counts.**
  ACCEPT. Pure prompt-body enrichment (csv.py + prompt.py). Computes
  scenario-wide `typical_dqg_fires_per_24h` from events span and
  renders alongside iter-008's recent counts. Production gate clean
  (headline mathematically unchanged). Detection-set drift since
  iter 008 invalidated direct grader comparison, so a clean A/B was
  run (iter008-state on current detection set vs iter009-state on
  same): hh120d acc +0.130 (4 up, 1 down, 18 same), dense_90d acc
  +0.083 (1 up by +2, 1 down, 10 same). All 4 axes positive on
  hh120d (clarity +0.435, calibration +0.174). Standout
  dense_90d#1725 frequency_change 2→4 — typical anchor lifted
  rate-shift framing over default sensor-fault hedging.

## Tried and rejected (do not re-attempt without new evidence)

- **Short-window-duty-alone non-weekend non-off-hours → time_of_day.**
  Pre-flight sim regressed hh120d −17pp because duty_cycle_shift_6h-alone
  fires repeatedly inside multi-day level_shift chains (kettle/tv/fridge),
  and reclassifying flips matched value_shift labels to mismatched
  calendar_pattern. Mechanism for time_of_day vs level_shift on duty-alone
  is bundle-external and cannot be resolved per-chain.
