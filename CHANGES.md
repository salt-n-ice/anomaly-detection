# Changes

## Latency metric (2026-04-22)

`src/anomaly/metrics.py` gains `compute_metrics_latency(gt_df, det_df)`.
For each GT label covered by ≥1 overlapping detection, latency is
`max(0, earliest_overlap_det.start - label.start)` in seconds; unmatched
labels (FN) are excluded. Returns `mean / median / p95 / max` across
matched labels plus `n_tp_labels`. Unlike `compute_metrics_event`,
latency doesn't merge detections — the caller can pass a pre-filtered
`det_df` (e.g. detector ≠ `data_quality_gate`) to isolate the stats-
detector first-fire lag from the DQG fast-path.

Motivation: the existing three metrics (`_event`, `_time`, `_pointwise`)
all treat a detection the same regardless of *when* in the label window
it first fires — a detection arriving 23h into a 24h label is a perfect
TP under evt_f1. For an actionable alerting system, alert latency
matters distinctly from coverage and precision.

No floor enforcement yet; measurement-only until G-series backlog items
accumulate enough data to pick a defensible tolerance. The research
harness (`research/run_research_eval.py`, gitignored) calls this twice
per scenario (all-detectors + nondqg) and reports into the snapshot
JSON + print_table — see `research/BASELINE.md` for the current per-
scenario numbers and outliers.

---

## Explainer session (2026-04-21/22)

`src/anomaly/explain.py` enriched to carry more evidence per bundle
without adding detector dependencies:

1. **Per-detector synthetic context** — `_synth_detector_context`
   rebuilds detector-native diagnostics (cusum `mu`/`sigma`/`direction`,
   PCA `approx_residual_z`, DQG `anomaly_type` + `value`,
   temporal-profile `hour_of_day` + `approx_hour_z`,
   state_transition `anomaly_type`) from the events frame when
   `alert.context` is empty on the CSV batch path. The live pipeline
   path — where detectors attach their own context dicts — is
   unchanged (synthesis activates only when `alert.context is None`).
2. **Tiered baseline fallback** — `extract_magnitude` widens its
   pre-window search 2h → 24h → 7d with per-tier `baseline_source`
   label (`prewindow_2h` / `prewindow_24h` / `prewindow_7d` /
   `prewindow_unavailable`). Recovers baselines on sparse event-driven
   sensors (waterleak battery, waterleak temperature) where 2h windows
   are routinely empty.
3. **Same-hour-of-weekday evidence** — `explain()` attaches
   `temporal.same_hour_weekday_{median, std, n, z}` via a new
   `_same_hour_weekday_stats` helper, comparing the window peak
   against same-hour-of-week historical peers. `build_prompt` renders
   a "Same-hour-of-weekday baseline" line when the stats are
   computable (peer_n ≥ 4, σ > 0).

Design invariants preserved: bundle still omits `inferred_type` from
the rendered prompt; all derived stats are tagged
`source=derived_from_prewindow` (or similar) so downstream consumers
can weight them vs detector-native values; NaN is still surfaced
honestly when the 7d pre-window is truly empty.

`tests/test_explain.py` — one baseline-source expectation renamed from
`"prewindow_median"` to `"prewindow_2h"` to match the tiered label;
all 21 explain tests pass.

---

## Detector-tuning session (2026-04-16/17)

Brief log of the tuning session on 2026-04-16/17. Event F1 is the primary target; all four committed baselines are preserved, outlet_short improved substantially.

## Final metrics

| Scenario | evt F1 | time F1 | incident_recall | FP_h/day |
|---|---|---|---|---|
| outlet | 0.927 | 0.758 | 0.864 | 12.73 |
| outlet_tv | 0.753 | 0.769 | 0.909 | 12.40 |
| outlet_kettle | 0.952 | 0.767 | 0.909 | 12.73 |
| waterleak | 0.824 | 0.324 | 0.700 | 26.73 |
| outlet_short | 0.763 | 0.622 | 0.850 | 0.66 |

`outlet_short` went from 0.533 → 0.763 event F1 (+0.230, +43% relative) and 0.366 → 0.622 time F1.

Every long anomaly (≥24h) is caught across all scenarios. Remaining FNs are structural: pre-bootstrap labels on `fridge_power` (spike / dip / saturation Feb 5–13) and the `leak_basement` dropout on a binary sensor.

## Detector / pipeline changes

1. **DQG cooldowns tuned.** `_OOR_COOLDOWN` 5min → 30min, `_DROPOUT_COOLDOWN` 30min, `_BATCH_COOLDOWN` 30min. Collapses oscillation alerts during noise_burst / frequency_change / reporting_rate_change.
2. **DQG `dropout` is fusable** (pipeline `_fuse`). Collapses reporting_rate_change dropout floods.
3. **DQG dropout alert windowed.** Alert spans `[last_valid_event, current_event]` instead of being an instant point, so it overlaps the GT dropout window instead of landing one tick past it.
4. **DQG clock_drift via cadence-persistence counter.** Replaces the dormant wall-clock `now` path. A consecutive-tick counter increments when `|gap − expected_interval| > max(3s, 0.5% × expected_interval)` and decays on normal ticks; fires when the counter reaches 3, 5-min cooldown, capped at the threshold so post-drift exit is clean. Gated to CONTINUOUS sensors with `expected_interval_sec ≤ 3600`.
5. **MatrixProfile disabled** in `Pipeline.finalize` (0 outlet hits, 2–4 leak FPs).
6. **CUSUM dedupe on bootstrap sigma** — ZOH-interpolated 1-min ticks crush σ; dedupe before computing `std()` so CUSUM uses the true per-event variance.
7. **CUSUM 5-day warmup on CONTINUOUS.** State accumulates and silent-resets during warmup; no alerts emitted. Kills diurnal-driven warm-up FPs on leak_temperature and voltage.
8. **SubPCA / MultivariatePCA 3-day warmup on CONTINUOUS.** Same pattern.
9. **SubPCA sliding-bootstrap threshold on CONTINUOUS** — 99.9-percentile computed from sliding windows (not non-overlap), so the threshold reflects out-of-sample tail. Cuts stationary voltage FP rate ~30×.
10. **TemporalProfile `min_samples` 5 → 20** and **bucket update dedupe** (mirrors CUSUM's fit-time dedupe). Prevents ZOH-inflated tick streams from poisoning bucket stats.
11. **Pipeline fusion — CUSUM-only chain filter.** `_chain_corroborated` drops CONTINUOUS chains containing only CUSUM alerts unless duration ≥ 90h. CUSUM's ARL0 collapses ~35× on autocorrelated ticks; sustained chains (leak_battery trend) are kept, short artifacts dropped.
12. **Pipeline fusion — CONTINUOUS tightening.** Fusion gap 60min → 15min on CONTINUOUS; CUSUM can only *extend* a chain if a non-CUSUM alert fired within the gap. Breaks inter-cluster daisy-chaining on stationary voltage.
13. **Pipeline fusion — two-detector-combo filter.** Drops CONTINUOUS chains whose detector set is `{cusum, sub_pca}` or `{cusum, temporal_profile}` with duration < 4h, and `{cusum, multivariate_pca}` chains over 60min, and `{sub_pca}`-alone chains whose window-union span exceeds 60min. Based on per-event analysis showing TP anomalies fire ≥3 detectors or an immediate DQG alert, while FP anomalies are almost all exactly `{cusum + one-other}`.

## Metrics

- Added `compute_metrics_event` — merges detections within a 1h gap into event clusters; this is the user-facing "how many real alerts" number.
- Added `compute_metrics_time` — duration-weighted TP/FP/FN seconds via per-sensor interval sweep. Surfaces multi-day FP strips that event F1 collapses into a single event.
- `scripts/run_all_scenarios.py` now also reports `incident_recall`, `fp_h_per_day`, `events_per_incident`.
- `scripts/run_all_scenarios.py` includes `outlet_short` as a 5th scenario (clean 60d dataset of short-only anomalies, uses `configs/outlet.yaml`).

## Visualization

- New `viz-long` CLI subcommand (`python -m anomaly viz-long …`). Produces a per-long-anomaly interpretive PDF: one page per GT label of duration ≥ `--min-hours` (default 24), showing the full scenario signal with the GT region highlighted, a zoomed signal with padded context, and aligned truth / detection strips. First page is a summary table of all labels with TP/FN status and detectors fired.
- Existing `viz` (multi-page 1-day / 6-hour windows) unchanged.

## Tests

- `test_dqg_future_timestamp` replaced with `test_dqg_clock_drift_ewma` + `test_dqg_no_clock_drift_on_cadence` covering the new persistence-counter clock-drift semantics.
- `test_pipeline_dqg_out_of_range_cooldown` updated to match the 30-min OOR cooldown.

## Files touched

```
src/anomaly/detectors.py          DQG, CUSUM, SubPCA, MultivariatePCA, TemporalProfile
src/anomaly/pipeline.py           fuse gap, chain corroboration, warmups, viz-long CLI
src/anomaly/metrics.py            event + time-weighted metrics
src/anomaly/viz.py                render_long()
scripts/run_all_scenarios.py      +outlet_short, +3 metrics
tests/test_detectors.py           clock_drift tests
tests/test_pipeline.py            oor-cooldown window
```
