# Detector Candidate Survey

The redesign picks detectors by matching detector properties to anomaly
and sensor properties — not by picking from the pre-redesign inventory.
This doc is the reference palette + the workload-grounding protocol.
`PIPELINE_REDESIGN.md` is the strategy; `LEARNINGS.md` is the binding
mechanism + anti-overfit rules (R1–R5 still apply here).

## Workload Fingerprint Protocol

Run **once per stage boundary**, before proposing the next stage's
candidate. Caches to `research/WORKLOAD_FINGERPRINT.json` so subsequent
iters within the stage read it instead of recomputing. Re-run when
scenarios are added or label vocabulary changes.

Output schema:

```json
{
  "timestamp": "...",
  "scenarios_included": ["household_60d", ...],
  "anomaly_types": {
    "<anomaly_type>": {
      "count": int,
      "label_class_breakdown": {"user_behavior": N, "sensor_fault": N},
      "duration_buckets": {"short": N, "medium": N, "long": N},
      "archetypes_seen": ["CONTINUOUS", "BURSTY", "BINARY"],
      "sensors_seen": [...]
    }
  },
  "sensor_physics": {
    "<sensor_id>": {
      "archetype": "...", "capability": "...",
      "expected_interval_s": int,
      "median_inter_event_s": float,
      "zoh_fraction": float,    // consecutive value-equal ticks / total ticks
      "heartbeat_s": int|null,
      "n_events": int
    }
  },
  "shape_distribution": {
    // rough hand-categorized buckets per archetype, derived from
    // anomaly_type x duration_bucket cross-tab. Categories:
    //   "spike_dip" (short impulse), "level_shift" (sustained step),
    //   "drift" (gradual trend), "regime" (state-machine change),
    //   "seasonal" (time-of-day / weekend deviation),
    //   "rate_change" (event-arrival rate shift on BURSTY/BINARY)
    "CONTINUOUS": {"spike_dip": N, "level_shift": N, "drift": N, ...},
    "BURSTY": {...},
    "BINARY": {...}
  }
}
```

Implementation: a small script (e.g., `research/audit_workload.py`) that
walks `SCENARIOS` from `run_research_eval.py`, reads each scenario's
`labels.csv` + `events.csv`, aggregates the above. ZOH-fraction = count
of (`value[i] == value[i-1]`) / total. Anomaly-shape categorization is a
fixed mapping — `spike|dip → spike_dip`; `level_shift|month_shift →
level_shift`; `trend|degradation_trajectory|calibration_drift → drift`;
`frequency_change|seasonality_loss → regime`; `time_of_day|weekend_anomaly|
seasonal_mismatch → seasonal`; `unusual_occupancy → rate_change` for
BINARY motion, otherwise `regime`; `water_leak_sustained → level_shift`.

## Detector Family Taxonomy

Survey of candidates beyond the pre-redesign inventory. Each entry is
one mechanism — the implementation may need a ZOH-aware or sensor-cadence
variant (per L1).

1. **CUSUM / EWMA** — Cumulative deviation from running mean; threshold
   on sum or weighted recent error.
   *Fits:* sustained level shifts on stationary continuous signals; slow
   drift detection. *Misses:* spikes (no impulse response), multi-modal
   regimes. *Failure modes:* ZOH variance collapse (L1); post-shift
   wind-down lag absent `adapt_to_recent` (L2). *Complexity:* low.

2. **Bayesian Online Change Point Detection (BOCPD)** — Online posterior
   over run-length under a piecewise-stationary prior; alarm on posterior
   collapse to short run-lengths.
   *Fits:* discrete regime changes with unknown shift magnitude; handles
   heteroscedastic noise better than CUSUM. *Misses:* very gradual drift
   (run-length grows monotonically). *Failure modes:* prior misspec on
   hazard rate; quadratic-per-tick under naive impl (use streaming
   approximation). *Complexity:* medium.

3. **STL / seasonal decomposition + residual z-score** — Decompose into
   trend + seasonal + residual; threshold on residual.
   *Fits:* seasonal anomalies (time-of-day, weekend); spikes against
   periodic baselines. *Misses:* non-periodic regime changes; needs ≥2
   full periods of bootstrap. *Failure modes:* trend leakage on level
   shifts (residual stays small); period misspec on irregular cadences.
   *Complexity:* medium (statsmodels).

4. **Matrix Profile discord** — Distance-to-nearest-neighbor over
   fixed-length subsequences; large distance = novel shape.
   *Fits:* shape anomalies, model-free (peaks, dips, irregular bursts).
   *Misses:* gradual shifts where every subsequence still has a near
   neighbor; multivariate without bespoke distance. *Failure modes:*
   subsequence-length sensitivity; compute cost (use SCRIMP/LeftSTAMP
   for online). *Complexity:* medium (stumpy).

5. **Robust PCA / online subspace tracking (GROUSE, OR-PCA)** — Online
   low-rank + sparse decomposition; sparse component flags outliers.
   *Fits:* multivariate sensors with correlated structure; tolerates
   outliers in fit window. *Misses:* univariate signals (degenerates to
   z-score); slow regime change (low-rank absorbs it). *Failure modes:*
   rank misspec; centroid drift on long-running streams. *Complexity:*
   medium-high.

6. **Isolation Forest / Random Cut Forest** — Tree-based unsupervised;
   isolation depth ~ outlier-ness.
   *Fits:* multivariate point outliers; no distribution assumption.
   *Misses:* temporal context (each point scored independently). *Failure
   modes:* needs upstream feature engineering on raw series; ZOH-heavy
   features inflate near-duplicates' scores. *Complexity:* low (sklearn /
   rrcf).

7. **Autoencoder / LSTM reconstruction error** — Train low-dim manifold
   on bootstrap; reconstruction error fires on novelty.
   *Fits:* complex multi-feature sensors with learnable structure.
   *Misses:* short bootstrap (overfits); silently re-fits to anomalous
   regime if not gated. *Failure modes:* train/test distribution drift;
   opaque debugging. *Complexity:* high.

8. **HDP-HMM / state-switching** — Bayesian nonparametric HMM with
   unbounded state count; alarm when new state instantiated or transition
   prob collapses.
   *Fits:* appliance regime detection (off/on/standby), occupancy state
   changes. *Misses:* continuous-valued anomalies without discrete
   structure. *Failure modes:* state explosion under noise; expensive
   inference. *Complexity:* high.

9. **HTM / sequence-memory (Numenta-style)** — Sparse distributed
   representations + temporal pooling; anomaly score from prediction
   error.
   *Fits:* streaming continuous learning, no retrain. *Misses:* requires
   custom encoder per capability; thin academic foundations vs. classical
   methods. *Failure modes:* hyperparameter brittleness; library
   maturity. *Complexity:* high.

10. **Hidden semi-Markov / Poisson rate-change** — Event-arrival rate
    model with state-dependent hold times; alarm on rate-state change.
    *Fits:* motion event sequences, water-flow counts, BINARY
    transition-rate shifts. *Misses:* continuous-valued sensors (need
    discretization). *Failure modes:* state-count misspec; sparse-event
    sensors yield low-power estimates. *Complexity:* medium.

11. **Quantile regression residual / conditional CDF** — Fit conditional
    quantiles of `value | covariates` (hour-of-day, prior-tick); alarm on
    extreme percentile.
    *Fits:* asymmetric noise (voltage spikes), hour-conditional
    thresholds, distributional shifts. *Misses:* shape change without
    quantile shift. *Failure modes:* covariate misspec; slow to adapt to
    legitimate baseline drift. *Complexity:* medium.

12. **Seasonal-Hybrid ESD (S-H-ESD, Twitter)** — STL + generalized ESD on
    residual; multi-spike detection.
    *Fits:* spike-in-seasonal (one-off bursts during a typical day).
    *Misses:* level shifts (same trend-leakage as STL alone). *Failure
    modes:* ESD over-flags when `max_anoms` is set too liberally.
    *Complexity:* medium.

## Selection heuristic

| Anomaly shape (per fingerprint) | Sensor character | First-pick families | Second-pick |
|---|---|---|---|
| Sustained level shift | CONTINUOUS, low ZOH | CUSUM (ZOH-aware), BOCPD | Robust PCA |
| Sustained level shift | CONTINUOUS, high ZOH | BOCPD | STL residual |
| Spike / dip | any | Matrix Profile, Quantile residual | S-H-ESD |
| Time-of-day / weekend | seasonal sensor | STL residual, Quantile (hr-conditional) | S-H-ESD |
| Rate change | BURSTY power, BINARY motion | Hidden semi-Markov / Poisson | BOCPD on duty cycle |
| Regime change (appliance state) | BURSTY multi-state | HDP-HMM, Subspace tracking | BOCPD on multivariate |
| Multivariate drift | CONTINUOUS w/ correlated feats | Robust PCA, Subspace tracking | Autoencoder |

Heuristic rules:
- **Lower complexity first.** Don't propose autoencoder/HDP-HMM/HTM until
  the low-complexity families (CUSUM, BOCPD, STL, MP, Quantile,
  Poisson-rate) have been ablated and shown insufficient.
- **Mechanism-explainable preferred.** A mechanism you can name in one
  sentence is debuggable; a learned model is not. Pick the explainable
  family unless the workload fingerprint shows shape complexity that
  classical methods provably cannot capture.
- **ZOH-aware variants always.** Per L1, any family operating on raw
  ticks must dedupe consecutive repeats before computing variance.
- **Multivariate only when fingerprint shows correlated structure.**
  Univariate problems on multivariate detectors degenerate to noisy
  z-scores.

## Anti-patterns

- **R1–R5 still bind.** No "N% FP on current data" justification (R1).
  Holdout incR drop is a hard stop (R5).
- **Don't pick from the pre-redesign inventory by default.** That set
  was assembled top-down; the redesign is bottom-up.
- **Don't escalate complexity prematurely.** If the workload fingerprint
  shows mostly level shifts and seasonal deviations, autoencoder is the
  wrong answer regardless of how impressive it sounds.
- **Don't skip the fingerprint and propose from intuition.** The
  fingerprint exists so the proposal is grounded in what's actually in
  the labels and sensor data, not a generic claim about "household
  anomalies."
