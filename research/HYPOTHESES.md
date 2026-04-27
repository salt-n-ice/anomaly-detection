# Hypothesis Backlog (redesign branch)

Under the bottom-up redesign (`PIPELINE_REDESIGN.md`), the next
hypothesis is dictated by the **current Stage**, not by a pre-ranked
backlog. The ladder is the hypothesis queue.

This file holds **forward-looking candidate ideas** that don't yet fit
a specific stage — detector designs, cross-sensor signal ideas, eval
scenarios to build. When you pick one up, promote it into the ladder
of `PIPELINE_REDESIGN.md` or open a plan for it.

## Convention

- `P<n>` = priority (P0 highest).
- `L<n>` = estimated risk of regression (L0 lowest).
- `[stage N]` = the ladder stage this belongs in if accepted.
- `Edit:` = concrete file + symbol to touch.
- **No iteration numbers. No past-trial diff tables.** Use
  `ITERATIONS.md` for history and `LEARNINGS.md` for mechanism
  insights that already survived.

## Candidate detectors (for Stage 2, 3, 5)

### CD1 — `RecentShift` on CONTINUOUS  `[stage 2] P1 L2`
Compare a short recent window against a trailing baseline window for
`value` (and optionally `value_roll_1h`). Score by normalized mean
shift and/or variance shift. Built-in expiry: the short and long
windows eventually converge, so post-shift wind-down self-terminates.
- **Mechanism fit:** `mains_voltage month_shift` and `basement_temp`
  dip clusters are recent-regime problems, not "keep accumulating
  against day-0 mean" problems.
- `Edit:` `src/anomaly/detectors.py` (new class),
  `src/anomaly/profiles.py` (register for CONT MEDIUM band).

### CD2 — `BinaryWindowShift` for motion  `[stage 3] P1 L2`
Compare recent 1h / 6h occupancy features against a trailing 24h / 7d
baseline. Fire on large ratio or difference changes in `duty_cycle_1h`,
`duty_cycle_24h`, `transitions_per_hour`. Decay once the short window
converges to the long window.
- **Mechanism fit:** motion labels are occupancy/routine shifts, not
  cumulative drift.

### CD3 — `LeakPersistenceDetector`  `[stage 1 or 3] P2 L1`
Fire when ON-state persistence or rolling duty cycle exceeds a
leak-like threshold over a short wall-clock window. No indefinite
cumulative drift.
- **Mechanism fit:** leak labels are persistence events, not generic
  binary drift. Only needed if `StateTransition` alone under-covers
  `water_leak_sustained`.

### CD4 — `StateConditionalShift` for BURSTY power  `[stage 3] P2 L2`
Compare current value / time-in-state against recent same-state
history. Fire on persistent state-level mean changes. Expire when new
state history stabilizes.
- **Mechanism fit:** BURSTY appliance behavior is state-based
  (kettle/fridge/tv ON-states vs idle).

## Cross-sensor ideas (Stage 5)

### XS1 — Vacation detector  `P1 L3`
Fires on simultaneous low activity across kettle + tv + motion for
>24h. Requires new `HouseholdDetector` protocol that consumes multiple
sensor streams. Expected largest single recall lift for the
"went on vacation" behavior class.

### XS2 — Shift-work detector  `P2 L3`
Fires on motion-at-unusual-hour + kettle-at-unusual-hour on the same
day (correlated off-hour activity). Needs temporal co-occurrence
across sensors.

## Eval scenarios to build

### EV1 — Low-activity household  `P1 L0`
Existing `household_sparse_60d` is the prototype. If holdout shows
precision problems on quiet households, expand into a multi-week quiet
scenario so FP regression is visible earlier.

### EV2 — Overlapping anomalies  `P1 L0`
Existing `household_dense_90d`. May need denser variants to stress-test
event-merge behavior specifically.

### EV3 — Single-sensor minimal config  `P0 L0`
Existing `single_outlet_fridge_30d`. Verify it regresses correctly when
the ladder adds a detector that needs cross-sensor corroboration.

## Explain-layer hooks (downstream, not in the ladder)

### EX1 — `inferred_type` column on detections  `P2 L1`
Add `inferred_type` from `explain.classify_type(alert)` in
`_write_detections`. Then add a `behavior_type_accuracy` metric to the
eval: fraction of user_behavior TPs where ≥1 overlapping detection has
a matching inferred type. Makes "detected but with wrong reason"
failures visible.

### EX2 — `presentation_class` suppression tag  `P2 L0`
When `classify_type(alert)` returns a sensor-fault type, tag the
bundle with `presentation_class = "infrastructure"` so the LLM prompt
suppresses it from household-facing summaries.

## Meta

- After any ACCEPT, run `--suite all --diff-baseline` to confirm zero
  regressions across production scenarios.
- After any REJECT, write a 2-sentence autopsy in the iteration entry
  of `ITERATIONS.md`. These are the highest-density observations in
  the log.
- When the list runs dry, generate fresh candidates by auditing the
  worst-time_F1 scenario: bucket FPs by (sensor, det-set, duration),
  identify uncovered behavior labels, and ask *"what single
  architectural change — not numeric threshold — would address the
  dominant bucket?"*
