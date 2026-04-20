# Hypothesis Backlog

Seed list of candidate hypotheses for the research loop. Each bullet is a
**falsifiable claim** with a specific target metric. Pick one per iteration
(highest leverage × lowest risk first); after testing, append the outcome to
`ITERATIONS.md` and either strike the hypothesis here or refine it.

When the backlog runs dry, generate new hypotheses by:
1. Re-running `research/run_research_eval.py --suite all` and re-reading
   `out/*_viz_long.pdf` + the top 3 worst pages of `out/*_viz.pdf`.
2. Bucketing remaining FPs/FNs by (detector-set, duration, sensor, label-type).
3. Asking: "What single-file change would remove the most-common FP/FN bucket
   without touching any other?"

Conventions:
- `P<n>` = priority (P0 highest). `L<n>` = estimated risk of regression (L0 lowest).
- `[60d]`, `[120d]`, `[both]` mark which suite(s) a change most directly targets.
- `[hot]` = known non-trivial problem documented in memory; worth ultrathinking.
- Strike with `~~...~~` and note the iteration that resolved it once tested.

---

## A. Long-horizon FPs (primary 120d-suite targets)

**A1 — `[120d][hot] P0 L2`** Stationary voltage CUSUM+SubPCA/MvPCA chains grow
across the extra 60 days because the `{cusum, sub_pca}`/`{cusum, temporal_profile}`
4-hour drop threshold in `_chain_corroborated` was tuned on 60-day data. Hypothesis:
tightening the drop threshold to 6h (or 8h) on CONTINUOUS sensors will reduce
120d fp_h/day on voltage without dropping any TP on the committed 60d baseline
(all TP voltage chains ≥ 6h already, per CHANGES.md). **Measure:** Δ fp_h/d on
outlet_120d voltage; Δ evt_F1 on every 60d scenario ≥ −0.005.

**A2 — `[120d] P1 L2`** Long-horizon CUSUM-only chain threshold (currently 90h)
may accept multi-day random-walk drifts that never had a real TP in 60 days.
Try 120h on CONTINUOUS; expect 120d FP reduction, leak_battery trend (real, 10d)
still accepted. **Measure:** Δ fp_h/d on outlet_120d & waterleak_120d; preserve
waterleak_60d battery-trend TP.

**A3 — `[120d] P1 L3`** Post-shift wind-down after a calibration_drift /
level_shift currently creates multi-day FP strips because detectors don't
adapt. For long horizons (120d), consider adding a "coordinated adapt"
trigger: when a fused chain closes at `max_span`, call
`adapt_to_recent()` on every detector for that sensor/state. Prior attempts
regressed outlet_demo F1 (see memory `project_iter_gains_2026_04`), but the
120d suite may tip the cost/benefit — the post-shift tail is 60+ days. Run
only the 120d suite first to confirm the gain, then re-run the 60d suite to
confirm it doesn't regress.

**A4 — `[120d] P2 L2`** SubPCA threshold (99.9th percentile of sliding-window
bootstrap errors) was tuned against a 14-day bootstrap. For 120d scenarios where
sustained drift dominates, consider evaluating whether 99.95 or 99.99 on the
sliding distribution removes solo-SubPCA chains in the second 60 days without
losing TP spike/dip detection. **Measure:** FP count for `{sub_pca}`-only chains
on outlet_120d voltage.

---

## B. Pre-bootstrap FNs (both suites, known structural gap)

**B1 — `[both][hot] P1 L3`** Pre-bootstrap spike/dip/saturation on fridge_power
(Feb 5, 7, 11) fall inside the 14-day bootstrap window and are silent. Options:
(a) shrink bootstrap to 7d and measure whether per-state detectors still have
enough data; (b) add a minimal MAD-based rolling detector that activates from
ingest 1 (short buffer, wider thresholds, no CUSUM/PCA interaction).
**Measure:** pre-bootstrap labels on outlet_60d and outlet_short_60d; ensure
post-bootstrap F1 is preserved on every scenario.

**B2 — `[both] P2 L2`** DQG saturation currently requires 10 consecutive
at-max readings. Shortening to 5 may catch the Feb 11 10-min saturation TP
that currently misses (fridge heartbeat is 5min, so 10 consecutive = 50 min).
**Measure:** whether saturation is now TP on outlet_60d; side-effect check on
waterleak (leak_battery at 100%).

---

## C. Short-cluster FPs on voltage (60d + 120d)

**C1 — `[both][hot] P0 L1`** Short `{cusum, mvpca}` chains on voltage (4 events
at 18/31/47/22 min on outlet_short). These currently pass `_chain_corroborated`
because the combo is tuned to accept duplicate_stale. Idea: require a same-sign
persistence in the raw value series during the chain (compute cum-min and
cum-max of Δvalue; if |range| < noise_floor, reject). Needs prototyping in
a helper. **Measure:** `{cusum, mvpca}` FP count on outlet_short_60d.

**C2 — `[both] P2 L1`** Single `{temporal_profile}` 0-min fires (3 FPs on
outlet_short) — drop chains whose `dets == {"temporal_profile"}` and
duration = 0 and whose raw |z| is only marginally above threshold (< 1.2 ×
z_thresh). **Measure:** Δ fp_h/d on outlet_short_60d + TP preservation elsewhere.

---

## D. Adaptation under long drift (120d sharp-focus)

**D1 — `[120d] P2 L3`** Temporal-profile buckets across a 120-day window see
each (hour, dow) bucket roughly twice as often, so bucket stats become tighter
and `|z| > z_thresh` fires more readily on natural seasonality. Hypothesis:
raising `z_thresh` to 5.0 on CONTINUOUS sensors reduces solo temporal_profile
FPs without masking real seasonal anomalies (those are caught by PCA/CUSUM
anyway). Prior attempt regressed outlet_60d — but worth re-checking in the
120d suite context.

**D2 — `[120d] P3 L2`** Monthly bucket refinement (×12 buckets) becomes usable
once ≥90d of history exists. The pipeline.md mentions this as "Month 3+".
Currently unimplemented. Adding it may cut false seasonality alerts in the
second 60-day wave of 120d scenarios. Non-trivial change; defer until simpler
wins are exhausted.

---

## E. Data-quality gate consistency (both suites)

**E1 — `[both] P2 L1`** DQG `clock_drift` persistence counter is 3. At 10-min
heartbeat voltage, 3 consecutive drifted ticks = 30 minutes before the alert
fires. For 120d scenarios with a long post-drift tail, this is fine; confirm
via viz that the Mar 10 clock_drift on outlet_60d voltage still fires within
the 6h window. If marginally late, bump to 2. Low leverage but clean.

**E2 — `[both] P3 L1`** DQG batch cooldown currently 30 min. If a generator
batches many events within a single 10-min window, the cooldown may suppress
distinct batch events. Look for 120d batch_arrival labels that miss.

---

## F. Meta-research

**F1 — `P0 L0`** After any ACCEPT, run the 60d suite again to confirm there are
no silent regressions. `run_research_eval.py --diff-baseline` enforces this.
Do not wait to hit a metric cliff before checking.

**F2 — `P1 L0`** After any REJECT, write a 2-sentence autopsy in the iteration
entry explaining the failure mode (which detector fired more, on which sensor,
during which GT window) — these are the highest-density observations in the log
and are what unlock the next iteration.

**F3 — `P1 L0`** Every 5 iterations, re-sort this backlog. Hypotheses that were
marginal at P1 may be better now that higher-priority items are done; new
observations may have spawned better hypotheses than any of the above.
