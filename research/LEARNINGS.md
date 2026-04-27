# Pipeline Learnings

Distilled, mechanism-level guidance. Loaded at the start of every
research session. `ITERATIONS.md` remains the per-iter log for human
audit — **it is NOT read at session start.**

## Real mechanisms (survive across scenarios)

These insights arise from detector / pipeline physics, not from
data-specific pattern matching. They generalize.

### 1. CUSUM ZOH variance collapse
Long-cadence sensors (e.g., basement_leak 6h heartbeat, basement_temp
burst mode) emit hold-the-value ticks on every observation. A naive
`arr.std()` on bootstrap data collapses to near-zero because half the
ticks are repeats. The resulting CUSUM sigma is too tight → fires on
normal post-bootstrap noise. **Fix:** deduplicate consecutive repeats
before computing std (applied in `CUSUM.fit`). Same logic applies to
`CUSUM.adapt_to_recent`.

### 2. Post-shift wind-down requires detector-state adaptation
When a level_shift ends, CUSUM's `sp/sn` accumulators keep firing
against the pre-shift bootstrap mean indefinitely. MvPCA residuals
keep scoring high against bootstrap P. Symptom: chains fire for weeks
after the anomaly ends. **Fix:** `adapt_to_recent` re-fits `mu`,
`sigma`, and threshold after a K-consecutive max_span streak, with a
sensitivity floor so sigma can only grow (prevents over-fire trap on
narrow recent variance).

**§2a Cooldown-spaced fast-fire detectors need detector-internal adapt.**
The pipeline.py K=3 max_span streak hook only counts chain-flushes whose
span ≥ 0.9 × `fuser.max_span`. For detectors whose `cooldown_s > fuser.gap`
(e.g., RollingMedianPeakShift cooldown=6h, BURSTY fuser gap=1h), every fire
is a singleton chain (audit: max chain span 0.93h, p95 0.04h on iter 020
hh60d) — the streak never reaches K. Wind-down sustains at the cooldown
rate (3-4 fires/day for ~40 days on hh60d fridge). **Fix:** count
consecutive cooldown-spaced fires inside the detector with a quiet-reset
(gap > `adapt_quiet_s` — default 24h — resets the streak counter to 1).
Self-adapt at K=3 by re-fitting boot stats from the detector's own
`_adapt_peaks` / `_adapt_history` deque (longer than the rolling fire
window). Same MAD-only-grow / sigma-only-grow floor applies.

### 3. DQG-resilient state trackers
`DefaultAlertFuser._last_emit_dets` gets reset to
`{"data_quality_gate"}` on every DQG alert. On sensors with chatty
DQGs (outlet_tv_power out_of_range bursts), any cross-chain filter
that depends on `_last_emit_dets` is effectively disabled. **Fix:**
separate `_last_fused_emit_dets` that ONLY updates on fused-chain
emits. Use the fused-only tracker for cross-chain rules (wind-down
filters, between-trend gaps).

### 4. StateTransition needs non-zero window for overlap matching
`StateTransition` fires 0-duration alerts at the trigger tick. The
metric's strict-`<` overlap check (`ts < ts` is False) fails on
0-duration alerts at the exact label start tick. **Fix:** default
to 1-minute window (`ts` → `ts + 1min`) in `_write_detections` when
window is None.

### 5. Bounded onset backfill on motion
Motion labels (unusual_occupancy, month_shift start) often have
their first post-label trigger tens of minutes after label start.
Pre-label bridging via long fused chains inflates early-coverage
artifact. **Fix:** `StateTransition` backfills the first trigger
after a quiet gap (bounded cap), giving UX-acceptable onset coverage
without relying on days of pre-label bridge chains. **Caveat:** the
exact MIN_GAP/CAP numbers are scenario-sensitive (see landmine #4).

### 6. BURSTY detection splits by signal type (bimodal-vs-rate)
On bimodal BURSTY outlets (OFF at ~0W, ON at device-nominal W), per-tick
value detectors (CUSUM, MvPCA, TemporalProfile, SubPCA) and per-state
value detectors (StateConditionalShift) and per-event magnitude detectors
(EventPeakShift) **all share a failure pattern**: they either null on
OFF-dominated bootstrap (low-fire) or flood on multi-phase natural variance
(high-fire). Six single-detector iters (CUSUM/MvPCA/SubPCA/TP-z4/TP-z6/SCS/
EPS variants) confirmed this on household_60d/120d BURSTY outlets.

**Orthogonal signal: event-arrival rate.** Rising-edge ON events form an
effectively Poisson process whose daily count (μ_day ± σ_day) characterizes
normal behavior. Rate-based detectors (`EventRateShift`) surface a signal
class invisible to value-based detectors — adds real TPs on
frequency_change / trend / degradation labels where no value detector fired.
**Implication:** Stage 3 BURSTY needs both families co-present, or a single
unified detector that reads both. Rate alone catches rate-shift labels
(frequency_change / degradation); magnitude alone catches level_shift /
spike; neither covers all BURSTY user_behavior shapes.

### 7. Rolling-window rate detectors have window-floor latency
A rate detector with `recent_window_s=W` cannot fire earlier than W seconds
after an anomaly begins — it needs W seconds of shifted data to detect the
shift. Consequence: `lat_frac = W / label_duration`. With W=24h and the
10% `lat_frac` ceiling, the detector can only legitimately claim labels
with duration ≥ 10·W = 10 days. For shorter labels, the detection fires
AFTER the label ends and the match is "credit after the fact" — not
useful detection. **Fix direction:** either (a) point-detection window
(`w0 = fire_ts - 1min`) so overlap semantics exclude ended labels, or
(b) sensor-class-aware latency floors in the metric, or (c) per-bucket
gating of detector credit by label duration.

### 8. Stage 4 corroboration requires UNCORRELATED failure modes
The Stage 4 AND-corroboration premise is "two detectors with different
mechanisms filter each other's false positives." This works only if their
failure modes are UNCORRELATED. Concrete counter-example: CUSUM +
RecentShift on CONT both have ~7-12d post-level-shift wind-down (CUSUM's
`sp/sn` accumulator keeps accumulating against stale `mu`; RecentShift's
rolling baseline takes 7d to catch up). During wind-down both fire, so
corroboration passes → fused chain emits → FP. Iter 014 confirmed: adding
CUSUM alongside RecentShift REGRESSED time_F1 and nd_lat_p95 on both
hh120d and leak_30d; fuser's `anchor_on_non_cusum=True` and
`ContinuousCorroboration` rules did NOT catch the correlated-wind-down
chains because CUSUM had RecentShift as its anchor (the anchor rule
filters CUSUM-alone chains, not CUSUM+anything chains).

**Implication:** When picking Stage 4 corroboration pairs, explicitly
audit whether both detectors share a known failure interval (post-
shift wind-down, bootstrap noise, hour-of-day effects). If yes, they're
not a valid pair — their "corroboration" is actually a shared artifact.
Mechanism-diversity is REQUIRED, not just DIFFERENT algorithms.

### 9. DutyCycle is the strongest BURSTY signal class (empirical)
After 13 BURSTY single-detector iters (5-13 per-tick/per-event/rate-based
attempts; 16-18 research sprint across peak/duty/histogram variants),
rolling-window duty cycle (fraction of time in the ON state) emerged as
the strongest mechanism by a wide margin (+0.482 production mean incR
vs +0.028 to +0.268 for alternatives). Generalizes on holdout (+0.52
holdout mean incR).

Why duty cycle works where value-based variants don't:
- **Magnitude-free:** immune to multi-phase variance (defrost, startup
  surges change peak but not duty).
- **Time-integrated:** integrates over the window, smoothing natural
  event-to-event jitter.
- **Bimodal-safe:** BURSTY distributions are bimodal (OFF=0, ON=device-W),
  but duty integrates both states uniformly.
- **Orthogonal to value/rate detectors:** duty is a different projection
  of the signal than peak value (RollingMedianPeakShift) or event count
  (EventRateShift). When paired with either, a genuine Stage 4 with
  uncorrelated failure modes (§8-compliant) is possible.
- **Single-parameter-tunable:** `window_s` trades latency vs statistical
  power; `z_threshold` trades recall vs FP. Well-behaved.

Caveats: latency is `~window_s/2` for a step-shift; any BURSTY duty
detector will breach 10% `lat_frac` on labels shorter than ~5×window_s
(for window_s=6h: labels <30h will exceed ceiling). Mechanism-intrinsic
per §7.

### 10. Bootstrap-MAD collapse on bimodal-zero BURSTY → z-inflation
On chatty BURSTY outlets dominated by OFF windows during bootstrap
(TV at 14% ZOH and median inter-event 4s — but 14d bootstrap captures
mostly off windows; same for kettle which is mostly idle), the duty
distribution is bimodal-zero: many windows at 0% duty, a few at
50-90% (active periods). MAD on this distribution collapses toward
zero — the "median absolute deviation from median" is dominated by
the cluster of zero-duty windows, all near the (zero) median. The
0.005 floor in `DutyCycleShift.fit` clamps it.

Once `boot_mad` is at the floor, `z = (live_duty - 0) / 0.005`
explodes. A normal-evening 30% TV duty produces z=60 (well above
z_threshold=3); audit observed FP-side z scores clustered at q50=33
and q95=130+ on `outlet_tv_power × duty_cycle_shift_6h` (iter 023
audit: 661 of 894 production behavior FPs from this single bucket =
74%). Real anomalies and natural-variance fires both hit huge z
because the divisor is artificially tiny.

**Symptom:** a single (sensor × detector) bucket dominating the
production FP budget on chatty BURSTY outlets, with FP z-scores
clustered well above z_threshold rather than borderline.

**Half-fix (iter 023):** percentile-novelty gate that activates only
when MAD collapsed to floor — fire requires `live_duty > boot_q99`
(high) or `< boot_q01` (low) in addition to z. Cuts the FPs cleanly
(76% reduction of production behavior uv_fp/d on the 2026-04-26
baseline). **Caveat:** the gate also filters "fluke TPs" that were
caught only via z-inflation (TV 2d weekend max_z=88 with duty 0.44
within bootstrap natural-evening range — DCS catching it was an
artifact, not a magnitude-novelty detection). Per-scenario incR
drops are real metric losses but reflect filtering of statistically
spurious detections rather than mechanism degradation.

**Open mechanism gap:** time-of-usage anomalies on BURSTY outlets
(TV weekend, kettle time_of_day with similar total duty) are NOT
detectable by any pure duty-magnitude detector. `HourlyEventRateChiSq`
is the architecturally-correct complementary detector (per-hour-of-
day histogram chi-square); iter 024 attempted to add it but REJECTED
(default chi_sq_mult=2.0 unreachable on TV/kettle's sparse-event
regime; fired only on fridge as new FPs). HERS-v2 with bootstrap-
derived per-sensor params is the deferred direction.

### 10b. Percentile-novelty gate generalizes beyond collapsed-MAD (iter 029)
The bootstrap-percentile gate from §10 (require duty outside
[boot_q01, boot_q99] in addition to z>z_threshold) is independently
meaningful regardless of MAD state. iter 023 gated only when
`mad_at_floor=True`; iter 029 dropped that conditional and made the
gate always-on, with no incR/time_F1 cost across 5 scenarios and
-16% rel uv_fp/d on production (-29 FPs).

For collapsed-MAD sensors (TV/kettle bimodal-zero): z is mechanically
inflated by the floor-MAD divisor, so the gate is the primary
discriminator (already in §10).

For non-collapsed-MAD sensors (fridge dense-cycle): z is statistically
meaningful but natural-variance fires (z=3-5, q50=3.04 in audit) often
produce duty values inside the bootstrap envelope. These are
"z-anomalous but absolutely-common" — the same fluke-fire mechanism
in different guise. The gate filters them as not-actually-novel.

**Combined formulation (binding):** a DCS-6h fire requires both
z-statistic anomaly AND absolute novelty (duty outside [q01, q99]).
This is a 2-of-2 mechanism that handles both MAD regimes uniformly.

Real anomaly fires push duty far above q99 with high z (TV TPs at
duty>0.7+ with z=111-200; fridge TPs at max_z=5.36-6.91 with duty
above per-sensor q99). They pass both gates trivially. Fluke fires
pass at most one gate.

### 12. Fuser gap must exceed longest detector cooldown (iter 030)
The user-visible-FP metric counts CHAINS (one notification per chain),
not raw fires. Each `DefaultAlertFuser` chain ends after `gap` seconds
of silence. If `gap < cooldown_s` of any contributing detector, every
cooldown-period fire becomes its own chain — including sustained TPs
(N notifications for one anomaly) and paired-rhythm FPs (N FP chains
counted N times).

**Pre-iter-030 BURSTY/BINARY default:** `gap=60min`, but DCS-6h cooldown
is 2h, RMP cooldown is 2h. Every cooldown fire was its own chain.
**Post-iter-030:** `gap=4h` (> 2h cooldown). Sustained fires fuse.
Across all 7 scenarios, uv_fp dropped 0-54% (median -37%) with zero
incR change — TPs became one chain per label (still overlap → still
TP) and paired/rhythmic FPs collapsed.

**Mechanism:** the fuser parameter `gap` defines the temporal binding
unit for the user-facing metric. Cooldown-spaced detectors need the
gap to span at least one cooldown period for the metric to count
notifications correctly. Production mean uv_fp/d fell from 0.65 → 0.34;
holdout from 0.67 → 0.44.

**Generalization rule:** when adding a detector with cooldown C, ensure
the consuming fuser's `gap > C`. Audit: `BURSTY/BINARY` fuser uses 4h
which covers DCS-6h(2h) and RMP(2h). If a future detector adds cooldown
> 4h, increase `gap` accordingly.

**Caveat:** the `max_span` cap (96h) still bounds chains, so very long
sustained anomalies will still split into multiple chains — that's
correct: the 4d-95d split mirrors a "still-firing" notification cadence
that the user expects.

## Landmines (don't repeat)

### L1. Curve-fitting to "N% FP on training"
**The trap:** "Rule X rejects 94% FP by count across the 3 training
scenarios, so it's safe to add." This is sampling error, not
generalization — a rule fit to 2 training chains (both FP) will break
a legitimate TP on holdout with slightly different label shape.

**Correct question:** Is there a MECHANISM reason the detector-combo
shouldn't fire? (e.g., "cumulative drift without residual or variance
confirmation is inherently weak evidence") Not "does the ratio
currently favor rejection?"

### L2. `max_span` shortening does not reduce total chain time
Alerts that kept firing during a long post-label drift will still
keep firing after `max_span` shortens — they just get sliced into
multiple shorter chains. Total chain time stays the same (or grows
due to flush overhead). **Correct approach:** address the detector's
persistent firing (adapt_to_recent, post-fire cooldown, or deletion),
not the chain boundary.

### L3. CUSUM downsampling to event cadence discards signal
Downsampling CUSUM input to the sensor's natural event cadence (drop
ZOH ticks) reduces raw fires drastically but regresses time_F1 on
CONTINUOUS — real anomaly signal shows up in the dense-tick regime
that ZOH handles; dropping it discards the signal.

### L4. Per-scenario numeric thresholds are brittle
Absolute thresholds (`cap=6h`, `score<10000`, `MIN_GAP=45m`) tuned to
exact label durations / score distributions in 3 training scenarios
clip legitimate signal on a new scenario with slightly different
numbers (e.g., holdout 8h water label vs training 6h max).
**Correct approach:** express constraints as RATIOS or
RELATIVE-TO-LABEL-DURATION (if inferrable), not absolute numbers.

### L5. Streak-count K=1 orphans legitimate TPs
Rejecting the 2nd (or 1st) `{cusum, sub_pca}` BURSTY chain in a
streak kills real anomaly coverage that starts with a single chain.
K=2 (accept first 2, reject 3+) is the lower bound. K=3 has been
observed too lenient on some shapes.

### L6. Naive "N within M days" cross-chain rules
Time-window rules that don't anchor on a specific prior event reject
legit TPs inside active anomaly bouts. The streak-count pattern
works because it resets on any non-matching emit — cross-chain state
without that anchor doesn't.

### L7. `max_span` re-start at overlap
On CONTINUOUS with `max_span=96h`, consecutive chains can show
"-2h gap" in detection CSV — the fuser flushes one alert before the
alert that triggered the span-exceeded. Gap-based cross-chain rules
should be aware; interpret negative gaps as "same underlying bout
fragmented by max_span."

### L8. `evt_precision = 1 - evt_fp/n_events` penalizes TP merging
Changes that consolidate multiple TP-adjacent chains into one fused
chain reduce `evt_fp` AND `n_events` — sometimes by the same amount
— so `evt_precision` drops even though detection quality improved.
**Use per-bucket `time_recall` and `incR` as primary signals;
`evt_F1` is informational only.**

### L9. Length-weighted aggregates mask short-anomaly regressions
Aggregate `time_F1` is dominated by long labels (a 28-day shift is
~4000× heavier than a 30-min leak in seconds). A pipeline that helps
long-shift coverage but trashes short-leak coverage can LOOK like an
improvement on aggregate `time_F1` while breaking the short-label
UX. Per-bucket metrics (short/medium/long) catch this.

### L10. Flat latency floors are scale-wrong
A 600s latency floor is 33% of a 30-min leak (lethal) and 0.03% of a
28-day shift (trivial). Use fractional latency (`lag / duration`)
with a 10% ceiling instead of absolute seconds.

### L11. Sensor match without type match over-counts
A detection on the right sensor at the right time can be an FP in
meaning even if it's a TP in coverage: a DQG `dropout` claim on
`basement_leak` during a real `water_leak_sustained` label shouldn't
get credit for catching a leak. The metric requires the detection's
`inferred_class` to be compatible with the GT's `label_class`.
Unknown-class detector-combo chains (`cusum+mvpca` etc.) stay
compatible with both classes; only confidently-wrong-class claims
are rejected.

## Anti-overfit rules (binding)

### R1. No rule whose justification is "N% FP on current data"
Rejection rules must cite a MECHANISM reason why the detector-combo
shouldn't fire. "100% FP across 3 scenarios" is 3 data points; it's
not evidence of anything.

### R2. Every accepted rule must hold on 2+ holdout scenarios
`research/run_research_eval.py --suite iter --random-sample 2` runs
production + 2 random holdout scenarios. If the iter CROSSES a floor
on a holdout scenario (OVERFIT WARNING in diff output), the rule
must be re-examined — if it holds on production but breaks holdout,
it's overfit.

### R3. Prefer relative thresholds over absolute ones
Use `max_chain_duration > 3 × label_upper_bound`, not
`max_chain_duration > 24h`. Use `score > k × threshold`, not
`score > 10000`. If the underlying value has a natural scale, encode
that scale into the rule.

### R4. Architectural changes > filter changes
Detector-state changes (e.g., `adapt_to_recent`) address root causes
and generalize. Filter rules yield small gains and are brittle. When
a filter iter rejects, consider whether the need indicates a
detector-state bug instead.

### R5. Holdout incR drop is a hard stop
If any iter drops incident_recall on any holdout scenario (not just
production), stop and re-examine. Missed labels on holdout mean the
rule is over-restrictive for some real-world data shape.
