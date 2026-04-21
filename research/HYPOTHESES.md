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
- `Band:` = which of SHORT / MEDIUM / LONG the change lives in (see `README.md` architecture section).
- `Edit:` = concrete file + symbol to touch. Most hypotheses are now a one- or two-line edit in `profiles.py` or `fusion.py` — the refactor made band-level changes trivial.
- Strike with `~~...~~` and note the iteration that resolved it once tested.

---

## A. Long-horizon FPs (primary 120d-suite targets)

~~**A1 — `[120d][hot] P0 L2`** Stationary voltage CUSUM+SubPCA/MvPCA chains grow
across the extra 60 days because the `{cusum, sub_pca}`/`{cusum, temporal_profile}`
4-hour drop threshold in `ContinuousCorroboration.accepts` was tuned on 60-day data.
Hypothesis: tightening the drop threshold to 6h (or 8h) on CONTINUOUS sensors will reduce
120d fp_h/day on voltage without dropping any TP on the committed 60d baseline
(all TP voltage chains ≥ 6h already, per CHANGES.md). **Measure:** Δ fp_h/d on
outlet_120d voltage; Δ evt_F1 on every 60d scenario ≥ −0.005.~~
_(Resolved Iter 001 — null result: no chain exists in the 4-6h bucket with
these det-sets on any of the 7 scenarios; FPs ride the 4-det fall-through instead.
Spawned C3 in its place.)_

**A2 — `[120d] P1 L2`** Long-horizon CUSUM-only chain threshold (currently 90h)
may accept multi-day random-walk drifts that never had a real TP in 60 days.
Try 120h on CONTINUOUS; expect 120d FP reduction, leak_battery trend (real, 10d)
still accepted. **Measure:** Δ fp_h/d on outlet_120d & waterleak_120d; preserve
waterleak_60d battery-trend TP.
`Band:` LONG. `Edit:` `src/anomaly/fusion.py` — in `ContinuousCorroboration.accepts`,
change `pd.Timedelta(hours=90)` in the `dets == {"cusum"}` branch to `hours=120`.

**A3 — `[120d] P1 L3`** Post-shift wind-down after a calibration_drift /
level_shift currently creates multi-day FP strips because detectors don't
adapt. For long horizons (120d), consider adding a "coordinated adapt"
trigger: when a fused chain closes at `max_span`, call
`adapt_to_recent()` on every detector for that sensor/state. Prior attempts
regressed outlet_demo F1 (see memory `project_iter_gains_2026_04`), but the
120d suite may tip the cost/benefit — the post-shift tail is 60+ days. Run
only the 120d suite first to confirm the gain, then re-run the 60d suite to
confirm it doesn't regress.
`Band:` LONG. `Edit:` cross-module — `src/anomaly/fusion.py` (`DefaultAlertFuser._flush`
needs to signal back to the pipeline state with the closed chain) + `src/anomaly/pipeline.py`
(wire `st.recent_rows` into each tick detector's `adapt_to_recent`). This is the
rare multi-file hypothesis; consider whether adding an optional `on_flush` callback
to `DefaultAlertFuser.__init__` (profile-wired) keeps the pipeline dispatcher thin.

**A4 — `[120d] P2 L2`** SubPCA threshold (99.9th percentile of sliding-window
bootstrap errors) was tuned against a 14-day bootstrap. For 120d scenarios where
sustained drift dominates, consider evaluating whether 99.95 or 99.99 on the
sliding distribution removes solo-SubPCA chains in the second 60 days without
losing TP spike/dip detection. **Measure:** FP count for `{sub_pca}`-only chains
on outlet_120d voltage.
`Band:` MEDIUM. `Edit:` `src/anomaly/detectors.py` — in `SubPCA.fit`, change the
`np.quantile(errs, 0.999)` literal (or promote it to a constructor kwarg and set
per-archetype in `profiles.py`).

---

## B. Pre-bootstrap FNs (both suites, known structural gap)

**B1 — `[both][hot] P1 L3`** Pre-bootstrap spike/dip/saturation on fridge_power
(Feb 5, 7, 11) fall inside the 14-day bootstrap window and are silent. Options:
(a) shrink bootstrap to 7d and measure whether per-state detectors still have
enough data; (b) add a minimal MAD-based rolling detector that activates from
ingest 1 (short buffer, wider thresholds, no CUSUM/PCA interaction).
**Measure:** pre-bootstrap labels on outlet_60d and outlet_short_60d; ensure
post-bootstrap F1 is preserved on every scenario.
`Band:` (a) orchestration — `Pipeline(configs, bootstrap_days=7.0)` at construction
sites (tests / CLI) or change the default in `src/anomaly/pipeline.py`.
(b) SHORT — new class in `src/anomaly/detectors.py` implementing `Detector`
(fit=pass, update=MAD-based threshold), register in `short_tick` for CONTINUOUS
+ BURSTY profiles in `src/anomaly/profiles.py`.

**B2 — `[both] P2 L2`** DQG saturation currently requires 10 consecutive
at-max readings. Shortening to 5 may catch the Feb 11 10-min saturation TP
that currently misses (fridge heartbeat is 5min, so 10 consecutive = 50 min).
**Measure:** whether saturation is now TP on outlet_60d; side-effect check on
waterleak (leak_battery at 100%).
`Band:` SHORT. `Edit:` `src/anomaly/detectors.py` — in `DataQualityGate.check`,
change the `self._sat_run == 10` literal to `== 5`.

---

## C. Short-cluster FPs on voltage (60d + 120d)

**C1 — `[both][hot] P0 L1`** Short `{cusum, mvpca}` chains on voltage (4 events
at 18/31/47/22 min on outlet_short). These currently pass
`ContinuousCorroboration.accepts` because the combo is tuned to accept
duplicate_stale. Idea: require a same-sign persistence in the raw value series
during the chain (compute cum-min and cum-max of Δvalue; if |range| <
noise_floor, reject). **Measure:** `{cusum, mvpca}` FP count on outlet_short_60d.
`Band:` LONG. `Edit:` `src/anomaly/fusion.py` — extend the
`dets == {"cusum", "multivariate_pca"}` branch in `ContinuousCorroboration.accepts`
to inspect `alert.context` entries for per-sample value deltas and reject when
|range| below a noise-floor constant.

~~**C2 — `[both] P2 L1`** Single `{temporal_profile}` 0-min fires (3 FPs on
outlet_short) — drop chains whose `dets == {"temporal_profile"}` and
duration = 0 and whose raw |z| is only marginally above threshold (< 1.2 ×
z_thresh). **Measure:** Δ fp_h/d on outlet_short_60d + TP preservation elsewhere.~~
_(Resolved Iter 003 — ACCEPT. Implemented as `score >= 1.2 * threshold` margin
check on `{temporal_profile}` only in ContinuousCorroboration. outlet_short_60d
evt_f1 0.763 → 0.780 (+0.017). Only the CONTINUOUS (voltage) singleton was
affected; the BURSTY (fridge_power) singletons remain — handed off to Iter 004
follow-up C4 below.)_

~~**C4 — `[both] P1 L1`** Extend the `{temporal_profile}` 1.2×threshold margin
filter to `PassThroughCorroboration` (BURSTY + BINARY). Pre-audit shows
2 FP singletons on outlet_short_60d fridge_power (scores 4.29/4.78) and
10 identical-score (4.272) FP singletons on waterleak_120d leak_basement;
no BURSTY/BINARY singleton TPs in any detection CSV. **Measure:** Δ evt_f1
on outlet_short_60d and waterleak_120d; no regression anywhere else.~~
_(Resolved Iter 004 — ACCEPT. outlet_short_60d 0.780 → 0.815 (+0.052 from
original baseline), waterleak_120d 0.838 → 0.897 (+0.059). No regression.)_

**C5 — `[60d] P2 L3`** outlet_tv_60d remains the weakest scenario at
evt_f1 = 0.753 (5 evt_FPs). Session 2026-04-21 audit (via
`research/event_audit.py outlet_tv_60d`) shows all 5 FP events are on
outlet_tv_power (BURSTY) after the weekend_anomaly ends 2026-03-16:
four `{cusum, sub_pca}`-only chains (12h / 52h / 63h / 220h / 21h) and one
`{cusum, sub_pca, temporal_profile}` (12h). **Structural:** this is
post-shift wind-down on a permanent level_shift — detectors keep firing
against the old baseline, and the same det-sets appear as TPs on other
scenarios (outlet_60d & outlet_120d fridge_power and outlet_kettle_60d
kettle_power have many `{cusum, sub_pca}`-only chains event-merged into TPs).
No clean local-corroboration signal separates them. Fix requires either
adaptation (prior session memory: all coordinated-adaptation attempts
regressed other scenarios) or a cross-chain bridge rule in `DefaultAlertFuser`
(tracking "did a non-cusum chain close within N days on this sensor"),
which is multi-file and needs its own session.
`Band:` orchestration / cross-chain state. Deferred.

**L4 — `[120d] P2 L3`** waterleak_120d has 3 remaining evt_FPs, all on
leak_battery with `{cusum, mvpca, sub_pca}` combo, all between the Mar 5-15
and May 15-29 trend labels (Apr 6-7, Apr 13-15, May 3-7). Same combo
produces TPs inside both trend windows, and event-merges aren't bridging the
between-trend chains with trend-chain events (gaps > 1h). Score/duration
signatures overlap between TPs and FPs — no local rule separates them.
Fix likely needs "last non-cusum emission on this sensor within 14 days"
state in the fuser. Deferred; note this is the **same structural shape** as
C5 (the event-merge gap isolates legitimately "between-event" FPs).
`Band:` orchestration. Deferred alongside C5.

**C6 — `[outlet_short] P3 L2`** 2 remaining FPs on outlet_short_60d voltage
survive all session 2026-04-21 filters: (a) mvpca singleton Feb 19 03:01
score 0.056 (ratio above 1.2×threshold, so margin filter doesn't trip —
iter 006 rejected); (b) Mar 10 11:51 `{cusum, mvpca, temporal_profile}` 22min
score 4.83. Both sit in early-post-bootstrap territory where MvPCA
reconstruction is still noisy. Could address via longer MvPCA warmup
(5d instead of 3d) as a targeted profile change, but risk is masking real
early-scenario anomalies; measure against outlet_60d's Feb 20+ TP chain
first. P3 because outlet_short_60d is already at 0.874.

---

## D. Adaptation under long drift (120d sharp-focus)

**D1 — `[120d] P2 L3`** Temporal-profile buckets across a 120-day window see
each (hour, dow) bucket roughly twice as often, so bucket stats become tighter
and `|z| > z_thresh` fires more readily on natural seasonality. Hypothesis:
raising `z_thresh` to 5.0 on CONTINUOUS sensors reduces solo temporal_profile
FPs without masking real seasonal anomalies (those are caught by PCA/CUSUM
anyway). Prior attempt regressed outlet_60d — but worth re-checking in the
120d suite context.
`Band:` LONG. `Edit:` `src/anomaly/profiles.py` — in CONTINUOUS profile,
change `partial(TemporalProfile, features=_CONT_FEATS["temporal"])` to
`partial(TemporalProfile, features=_CONT_FEATS["temporal"], z_thresh=5.0)`.

**D2 — `[120d] P3 L2`** Monthly bucket refinement (×12 buckets) becomes usable
once ≥90d of history exists. The pipeline.md mentions this as "Month 3+".
Currently unimplemented. Adding it may cut false seasonality alerts in the
second 60-day wave of 120d scenarios. Non-trivial change; defer until simpler
wins are exhausted.
`Band:` LONG. `Edit:` `src/anomaly/detectors.py` — extend `TemporalProfile._bucket`
to add `ts.month` when sample count justifies it; thread through `fit` and `update`.
No `profiles.py` change needed (same Protocol).

---

## E. Data-quality gate consistency (both suites)

**E1 — `[both] P2 L1`** DQG `clock_drift` persistence counter is 3. At 10-min
heartbeat voltage, 3 consecutive drifted ticks = 30 minutes before the alert
fires. For 120d scenarios with a long post-drift tail, this is fine; confirm
via viz that the Mar 10 clock_drift on outlet_60d voltage still fires within
the 6h window. If marginally late, bump to 2. Low leverage but clean.
`Band:` SHORT. `Edit:` `src/anomaly/detectors.py` — change the
`_CLOCK_DRIFT_PERSISTENCE = 3` class constant in `DataQualityGate`.

**E2 — `[both] P3 L1`** DQG batch cooldown currently 30 min. If a generator
batches many events within a single 10-min window, the cooldown may suppress
distinct batch events. Look for 120d batch_arrival labels that miss.
`Band:` SHORT. `Edit:` `src/anomaly/detectors.py` — change the
`_BATCH_COOLDOWN = pd.Timedelta(minutes=30)` class constant in `DataQualityGate`.

---

## L. Long-anomaly coverage (120d time_f1 targets)

The research gate now enforces `time_f1 drop > 0.02` as a REGRESSION floor
(see `BASELINE.md`), because evt_f1 treats a 4h detection on a 30d GT as a
perfect TP. These hypotheses specifically target coverage / fragmentation on
sustained anomalies — improving `time_f1` without regressing `evt_f1`.

~~**L1 — `[120d][hot] P0 L2`** Fuser `max_span=96h` fragments any GT longer
than 4 days into chunks separated by silence (whenever detectors go quiet
between re-fires). On `outlet_120d`, this shows up as multi-day FN bands
inside `calibration_drift` / `month_shift` labels where the fused chain
closed and nothing reopened it. Hypothesis: raise `max_span` to 192h (8d)
on CONTINUOUS only; long FP strips would lengthen too, but
ContinuousCorroboration already filters single-detector-combo chains, so
genuine sustained multi-detector TPs gain coverage while stationary
voltage FPs stay gated. **Measure:** Δ time_f1 on outlet_120d and
waterleak_120d (expect ↑); Δ fp_h/d (watch carefully — this is where the
risk is).~~
_(Resolved Iter 002 — REJECT. time_f1 did improve (+0.035 waterleak_120d,
+0.002 outlet_120d) but evt_f1 regressed on waterleak_120d (−0.013) via the
metric artifact `evt_precision = 1 − evt_fp/n_events`: TP-event consolidation
mechanically lowers precision whenever FPs don't collapse at the same rate.
outlet_120d saw essentially zero movement, disconfirming the "fragmentation
is the bottleneck" framing — outlet_120d's time_f1 deficit is a precision
problem (post-shift wind-down tails), not a recall problem.)_

**L2 — `[120d] P1 L2`** Chain re-open: when a fused chain closes and the
*same* detector combo fires again on the *same* sensor within one fusion
`gap`, reopen the chain rather than starting a new one. This bridges
brief silences during sustained anomalies (detectors momentarily stop
crossing threshold) without extending FP chains, because the re-open
requires the same combo (FPs tend to have drifting combos). **Measure:**
Δ time_f1 on both 120d scenarios (expect ↑); Δ events_per_incident
(expect ↓ — fragmentation reduces).
`Band:` LONG. `Edit:` `src/anomaly/fusion.py` — add to `DefaultAlertFuser`
a `_last_closed: tuple[frozenset[str], pd.Timestamp] | None` field; in
`ingest`, before pushing a fresh alert onto `self._pending`, check if
`_last_closed` exists, has matching detector set, and is within `self.gap`
— if so, restore it as the new `self._pending` head.

**L3 — `[120d] P2 L3`** During sustained drift, CUSUM-only re-fires during
chain-silence are currently rejected by `ContinuousCorroboration`
(`dets == {"cusum"}` only accepted at ≥90h duration). But on an already-
corroborated multi-detector TP chain, a CUSUM-only continuation is
legitimate bridging. Hypothesis: if the *immediately preceding* fused
emission for this sensor had non-CUSUM corroboration within the last 48h,
accept a CUSUM-only chain as a continuation regardless of the 90h rule.
Requires state that crosses fused-chain boundaries (same sensor's last
emit), so it's more than a local corroboration rule. **Measure:** Δ time_f1
on outlet_120d (voltage-drift tail); Δ evt_f1 ≥ 0 on all 60d.
`Band:` LONG. `Edit:` `src/anomaly/fusion.py` — `ContinuousCorroboration`
needs a "last non-CUSUM emission timestamp" held by `DefaultAlertFuser`
and passed into `accepts`; this breaks the stateless-rule contract
slightly, so consider refactoring `CorroborationRule` to receive a
context object rather than just the alerts list.

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
