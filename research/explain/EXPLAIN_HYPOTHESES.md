# Explain-quality hypotheses backlog

Each entry: Priority (P0/P1/P2), Risk (L1/L2/L3), brief.

## P0

- **H9 — detector firing density over the detection period.** L1-L2.
  Bundles show a single fused chain's window, but don't signal how
  "dense" the firing was (1 tick vs 34 ticks fused into the chain). A
  `firing_density_per_min` field from the detections frame could let the
  grader differentiate sustained evidence from transient fires, raising
  `no_false_confidence` for dense-FP cases.


## P1

- **H3 — Add `window_range_ratio` to the magnitude block.** L2.
  delta / peak doesn't distinguish "real excursion within known range" from
  "ZOH artefact near sensor ceiling". Needs a `sensor_range` lookup from
  config.

- **H4 — Render detector context dicts even when empty.** L1.
  Largely subsumed by iter-002 — synthetic dicts now populate empty context.
  What remains: tighter wording / adding a "context source: derived" banner
  at the prompt level (currently only a per-dict `source` field).

## P2

- **H5 — Add nearest-neighbour calendar comparison.** L3.
  "last week at this hour the sensor showed X" would strengthen
  `temporal_fidelity` for time-of-day / weekend anomalies. Requires
  pulling the events DataFrame ±7 days around the window.

## Blocked

- **H2 — Surface score-to-threshold ratio in the prompt.** L1.
  **Blocked:** every bundle has `threshold = 0.0` because
  `_detections_to_alerts` in `explain.py` hardcodes it — the detections CSV
  has no threshold column. Unblocking requires adding a threshold column at
  pipeline write-time, which is out of scope for the explain loop.

## Completed / retired

- ~~H10 — loosen calendar-evidence gate below |z|=2.~~ (iter-008, ACCEPT,
  +0.028 agg on top of iter-005.) Threshold 2.0 → 1.5 unlocked ~40
  moderate-z cases (mostly in outlet_tv_60d) without regressing any
  non-calendar scenarios.

- ~~H8 — state-signal for cusum-sees-state waterleak TPs.~~ (iter-007,
  ACCEPT, +0.016 agg.) Implemented as a grader-only `drift → state`
  promotion when `|baseline| < 0.1` and `0.5 ≤ |delta| ≤ 2.0` (binary
  on/off signature). Delta cap at 2.0 prevents kettle-power-swing
  false-positive promotion.

- ~~H7 — same-hour-of-weekday baseline.~~ (iter-004, ACCEPT, +0.09 agg.)
  Implemented as `bundle.temporal.same_hour_weekday_z` with peer-group by
  weekday+hour. Grader rewards calendar-GT cases where |z|≥2 and peer_n≥4
  even when firing detectors aren't `temporal_profile`. Lifted type_id and
  no_misleading across all four outlet scenarios.

- ~~H1 — `sub_types` tally in the rendered prompt.~~ (iter-001, NULL.)
  Premise wrong: `sub_types` / `n_sub_alerts` don't exist as bundle fields —
  detections.csv is one row per detection and the fuser's group_alerts context
  doesn't round-trip through the CSV. Reframed as a sibling-detections tally
  computed from the detections frame at explain time, but the rule never
  fires: DQG-only detector sets with shape-family GT have n≈0 neighbors
  because DQG fires on range violations, not shape changes. The ≥10-neighbor
  clusters that DO exist are fused statistical chains (cusum+sub_pca+…), so
  `base_fam != 'dqg'` and the rule short-circuits. The DQG↔shape mismatch
  isn't recoverable from the explainer — the signal isn't in the detections.
  See `EXPLAIN_ITERATIONS.md` iter-001 for full data.

## P1

- **H3 — Add `window_range_ratio` to the magnitude block.** L2.
  delta / peak doesn't distinguish "real excursion within known range" from
  "ZOH artefact near sensor ceiling". Needs a `sensor_range` lookup from
  config.

- **H4 — Render detector context dicts even when empty.** L1.
  When `detector_context == []` the prompt says
  "(per-detector context dicts unavailable)" — negative signal. Try
  "no per-detector diagnostics available for this fused chain" wording
  to see if it changes judge scoring (meta-check on prompt wording).

## P2

- **H5 — Add nearest-neighbour calendar comparison.** L3.
  "last week at this hour the sensor showed X" would strengthen
  `temporal_fidelity` for time-of-day / weekend anomalies. Requires
  pulling the events DataFrame ±7 days around the window.
