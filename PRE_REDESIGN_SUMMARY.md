# Anomaly Detection Pipeline — Pre-Redesign Progression

## Dataset change — from OLD single-sensor scenarios to realistic households

The OLD scenarios were single-sensor synthetic test beds (one outlet, one leak sensor) that stressed one anomaly class at a time. Three problems became blocking:

- **Unrealistic.** A real household runs many sensor types together, and the fusion logic couldn't be tested against cross-sensor interactions.
- **No separation between user-facing anomalies and sensor faults.** "The fridge is misbehaving" and "a clock drift / a dropout" were scored identically, so gains on one could mask regressions on the other.
- **`evt_F1` artifacts.** Chain-merging made small changes look large in confusing directions.

The new suite (`household_60d`, `household_120d`, `leak_30d`) is full multi-sensor households. GT labels are tagged `user_behavior` vs `sensor_fault`, and the headline metric became `behavior.time_F1` — literally "how well we catch what the household actually cares about." Sensor faults stayed in the pipeline for realism but got demoted to an "infrastructure" block that's reported but not optimized.

---

## Progression — 5 phases, tracked by `hh60d time_F1`

### 1. Early filter rules (OLD dataset)

First-pass margin filters on weak solo-detector alerts (a statistical detector firing alone without any corroborating detector is suppressed), plus cross-chain wind-down filters that stop detectors from "ringing" after a real anomaly ends.

*`hh60d time_F1` not directly comparable — OLD was single-sensor scenarios.*

### 2. Dataset migration + fusion/DQG rebuild

Switched to realistic multi-sensor households with behavior-stratified labels, and simultaneously rebuilt the alert-combining logic and data-quality gate (the fixes were interdependent, so they shipped together).

**`hh60d time_F1` landed at 0.492** — first measurement on the new dataset.

### 3. Warmup + adapt-to-recent baseline

Fast-event sensors now stay silent for a 12h calibration window after bootstrap. Any detector that fires non-stop for ~12 days re-centers its baseline to treat the new level as normal. Three aggressiveness levels were tested; the most conservative was the only one that didn't kill genuine multi-day anomalies.

**`hh60d time_F1`: 0.492 → 0.498 (+0.006).**

### 4. Fused-only tracker + full-refit adapt + per-sensor-type buffers

- **Tracker bug fix.** The data-quality gate was resetting the motion cross-chain filter every tick, so the filter almost never triggered. Built a separate tracker that only real fused alerts update.
- **Full-model re-centering.** The baseline re-centering was upgraded to re-fit the full statistical model (mean + PCA projection + threshold) with a safety floor preventing over-sensitivity.
- **Per-sensor-type buffers.** Tuned how much recent history each sensor type absorbs (4 days for continuous signals, 6 days for bursty/binary).

**`hh60d time_F1`: 0.498 → 0.571 (+0.073)** — the biggest single ladder of gains in the whole pre-redesign run.

### 5. Motion tuning + DQG-resilient filters, then overfit revert

Motion-sensor timing refinements (extend the idle-gap threshold before trusting the first motion alert, shorten the backfill window), plus a filter rewrite so the earlier cross-chain rules actually trigger even when the data-quality gate is chatty.

**`hh60d time_F1`: 0.571 → 0.632 (+0.061).**

A subsequent batch of narrower filters (scenario-specific chain caps, detector-combo singleton rejects) briefly landed then was flagged as curve-fitting to training false-positive counts and reverted wholesale. This triggered the **`pipeline-redesign` pivot** — the "start with nothing detected, prove each addition" framework.

The redesign reset **`hh60d time_F1` to 0.024** (Stage 0, empty-pipeline anchor, current baseline).

---

## Summary table

| Phase                                            | `hh60d time_F1` | Δ        |
| ------------------------------------------------ | --------------: | -------: |
| OLD dataset                                      | not comparable  |    —     |
| Dataset migration + fusion/DQG rebuild           | 0.492           | baseline |
| Warmup + adapt-to-recent baseline                | 0.498           | +0.006   |
| Fused-only tracker + full-refit adapt + buffers  | 0.571           | +0.073   |
| Motion tuning + DQG-resilient filters            | 0.632           | +0.061   |
| **Redesign pivot — Stage 0 empty-pipeline anchor** | **0.024**     | **reset** |
