# Smart Home Sensor Anomaly Detection Pipeline

## Design Overview

The pipeline follows a **filter-and-escalate** architecture: an adapter layer normalizes any sensor into a canonical numeric stream, low-cost deterministic checks eliminate obvious data problems, lightweight statistical models handle real-time detection, and more intensive batch analysis runs periodically on accumulated data. This staged approach ensures that 95%+ of normal readings are processed in under 2 ms with minimal memory, while complex pattern anomalies are caught in scheduled batch runs.

The genericness of the pipeline lives in the **adapter layer**: it classifies each sensor into one of three archetypes (continuous numeric, bursty/multimodal numeric, binary/state) and emits a uniform regularly-sampled feature stream. The detector layer downstream is sensor-agnostic.

The core detection engine is PCA on an enriched feature vector — not raw sensor values, but adapter-emitted features augmented with calendar context, rolling statistics, and variance tracking. The key design insight: rather than using a complex model on simple features, we use a simple model on smart features. Two complementary PCA variants run in parallel:

- **Sub-PCA** (per-sensor univariate) detects unusual shapes within one sensor's recent waveform.
- **Multivariate PCA** detects unusual combinations across the enriched feature vector.

PCA ranks #1 (univariate) and #3 (multivariate) on the TSB-AD benchmark, outperforming transformers and deep learning at a fraction of the compute cost. CUSUM runs in parallel for drift-specific detection, and temporal profile z-scores handle calendar-aware comparisons.

For batch analysis, the baseline uses MatrixProfile (training-free, parameter-free), with a future upgrade path to TSPulse (1M parameters, GPU-free, #1 on TSB-AD).

A **suppression layer** disables detectors that are degenerate for a given archetype (e.g., MatrixProfile on a binary stream, FFT on near-constant data), so the same pipeline runs cleanly across heterogeneous sensors.

### References

1. **Liu & Paparrizos (NeurIPS 2024)** — *"The Elephant in the Room: Towards A Reliable Time-Series Anomaly Detection Benchmark"* — TSB-AD benchmark evaluating 40 algorithms across 1,070 time series. PCA and statistical methods consistently outperform deep learning. VUS-PR established as the reliable evaluation metric.
2. **Ekambaram et al. (2025)** — *"TSPulse"* — IBM's 1M-parameter foundation model, #1 on both TSB-AD leaderboards with GPU-free inference. Dual-space (time + frequency) masked reconstruction.
3. **Reis et al. (Future Internet, 2025)** — *"Edge AI for Real-Time Anomaly Detection in Smart Homes"* — Benchmarked Isolation Forest (22 ms) and LSTM-AE (35 ms) on Raspberry Pi 4. Validated hybrid statistical + neural pipeline on edge hardware at 4.2 W.
4. **Liu & Paparrizos (PVLDB, 2025)** — *"TSB-AutoAD"* — Evaluated 70 automated AD solutions; over half don't outperform random model selection. Selective ensembling (SENSE) validates our staged approach.
5. **Fährmann et al. (IEEE Access, 2024)** — *"Anomaly Detection in Smart Environments: A Comprehensive Survey"* — Heterogeneous mixed-type data is the core smart home challenge. Recommends methods that handle continuous + binary + intermittent signals without strong distributional assumptions.

---

## Baseline System

8 components. Covers the majority of anomaly types with zero ML training complexity and minimal per-sensor configuration. The adapter layer is the only place per-sensor knowledge lives — everything downstream is generic.

> **Granularity:** the adapter resamples each sensor to a canonical rate. Default is 1 sample/min for continuous and bursty archetypes, 1 sample/min on derived features for binary archetypes. All buffer sizes, window counts, and MatrixProfile parameters assume this. Granularity is a per-archetype runtime parameter — see Configuration Parameters below.

**Total real-time cost:** < 1.5 ms, < 4 MB RAM.

### Pipeline Flow

```
                       ┌─────────────────┐
                       │ Incoming Event   │
                       └────────┬────────┘
                                │
                       ┌────────▼────────┐
                       │ Adapter Layer   │  classify archetype, resample,
                       │                 │  difference counters, emit features
                       └────────┬────────┘
                                │
                       ┌────────▼────────┐
                       │ Data Quality    │──── Reject ────┐
                       │ Gate            │                 │
                       └────────┬────────┘                 │
                                │ Pass                     │
                       ┌────────▼────────┐                 │
                       │ Feature         │                 │
                       │ Engineering     │                 │
                       └────────┬────────┘                 │
                                │
                       ┌────────▼────────┐                 │
                       │ Suppression     │  drop detectors degenerate
                       │ (per archetype) │  for this archetype
                       └──┬───┬───┬───┬──┘                 │
                          │   │   │   │                    │
              ┌───────────┘   │   │   └───────────┐        │
              │         ┌─────┘   └─────┐         │        │
     ┌────────▼──┐ ┌────▼─────┐ ┌───────▼──┐ ┌───▼──────┐ │
     │ Sub-PCA   │ │Multivar. │ │ CUSUM    │ │ Temporal │ │
     │           │ │PCA       │ │          │ │ Profiles │ │
     └────────┬──┘ └────┬─────┘ └───────┬──┘ └───┬──────┘ │
              │         │               │         │        │
              └────┬────┘               └────┬────┘        │
                   │                         │             │
                   └───────────┬─────────────┘             │
                               │                           │
                      ┌────────▼────────┐                  │
                      │  Alert Fusion   │                  │
                      └────────┬────────┘                  │
                               │                           │
  ┌──────────────────┐         │         ┌─────────────────▼──┐
  │ Accumulated Data │    ┌────▼─────┐   │                    │
  └────────┬─────────┘    │  Alert   │◄──┘                    │
           │              │  Output  │                        │
  ┌────────▼─────────┐    └──────────┘                        │
  │ MatrixProfile    │────────▲                               │
  │ (Batch)          │        └───────────────────────────────┘
  └──────────────────┘
```

| Block | What It Does |
|---|---|
| Adapter Layer | Classifies sensor archetype, resamples to fixed rate, differences counters, emits canonical numeric features |
| Data Quality Gate | Rejects impossible values, duplicates, and timing faults (operates on raw events) |
| Feature Engineering | Adds calendar context, rolling means, and first differences to adapter output |
| Suppression | Disables detectors that are degenerate for the sensor's archetype |
| Sub-PCA | Flags unusual shapes within a single sensor's recent waveform |
| Multivariate PCA | Flags unusual combinations across the enriched feature vector |
| CUSUM | Accumulates evidence of slow drift or level shifts |
| Temporal Profiles | Compares each reading against its time-of-week historical norm |
| MatrixProfile (Batch) | Discovers anomalous subsequences in stored history |
| Alert Fusion | Groups concurrent detector firings into a single alert event |

---

### Adapter Layer

The adapter is the only component with per-sensor awareness. It accepts the raw event stream and emits a uniform regularly-sampled vector of canonical numeric features. Every downstream component sees the same shape regardless of sensor type.

Each sensor is declared as one of three **archetypes**. The archetype is set at registration time (one line of config per sensor) and determines which canonical features the adapter emits and which detectors the suppression layer enables.

#### Archetype A — Continuous Numeric
*Examples: temperature, voltage, humidity, ambient light, indoor pressure.*

The "easy case." Reading is a real-valued physical quantity that varies smoothly.

- **Resampling:** linear interpolation to the canonical rate, with `max_gap` (default 5× expected interval). Gaps exceeding `max_gap` emit `NaN` and trigger a dropout alert via the data quality gate; downstream features handle `NaN` by skipping the update.
- **Canonical features emitted per timestep:**
  - `value` — the resampled reading.
- **Suppression:** none. All detectors active.

#### Archetype B — Bursty / Multimodal Numeric
*Examples: outlet power (W), water flow rate, network throughput.*

Real-valued but heavily multimodal — typically a near-zero idle mode plus one or more active modes. PCA on the raw value is poorly conditioned because residuals are non-Gaussian.

- **Resampling:** zero-order hold (forward-fill) to the canonical rate, since events are threshold-reported and the value is assumed constant between events. `max_gap` applies as for Archetype A.
- **Cumulative counters** (e.g., `energy` kWh): differenced before emission. The adapter stores the last cumulative value and emits `Δvalue / Δt` per canonical timestep. This is non-negotiable — raw counters destroy CUSUM and PCA.
- **State channel:** a 2-component GMM (or a simple bimodal threshold during cold start) is fit during bootstrap on the resampled value. The adapter emits a discrete `state ∈ {0, 1, …}` label per timestep. PCA models are then trained **per state** rather than globally.
- **Canonical features emitted per timestep:**
  - `value` — resampled reading (or differenced rate, for counters).
  - `state` — discrete mode index.
  - `time_in_state` — seconds since last state transition.
- **Suppression:** FFT/spectral features disabled in the off-state. Sub-PCA, Multivariate PCA, CUSUM, and temporal profiles run **conditioned on `state`** — separate models per state.

#### Archetype C — Binary / State
*Examples: switch on/off, water leak wet/dry, motion detected, contact open/closed.*

Two-valued state stream. The "interesting" signal is not the value but the **timing and frequency** of transitions.

- **Resampling:** the binary value itself is forward-filled, but the adapter's primary job is to emit derived numeric features over a sliding window.
- **Canonical features emitted per timestep:**
  - `state` — 0 or 1, forward-filled.
  - `time_since_last_transition` — seconds.
  - `transitions_per_hour` — count over trailing 1 h window.
  - `duty_cycle_1h` — fraction of trailing 1 h spent in state 1.
  - `duty_cycle_24h` — fraction of trailing 24 h spent in state 1.
- **Suppression:** Sub-PCA disabled (the raw binary waveform has no learnable shape). MatrixProfile disabled (z-normalization on near-constant series produces garbage discords). FFT/spectral features disabled. Multivariate PCA, CUSUM, and temporal profiles operate on the **derived numeric features**, not on the raw binary.
- **Special handling:** for sensors where the positive state is itself the alert (e.g., water leak `wet`), the adapter forwards the state transition directly to alert output as a deterministic event. Statistical detectors then operate only on the derived features for health/trend monitoring.

#### Suppression Matrix

| Detector | Continuous | Bursty | Binary |
|---|---|---|---|
| Data Quality Gate | ✓ | ✓ | ✓ |
| Sub-PCA | ✓ | ✓ (per state) | ✗ |
| Multivariate PCA | ✓ | ✓ (per state) | ✓ (on derived features) |
| CUSUM | ✓ | ✓ (per state) | ✓ (on derived features) |
| Temporal Profiles | ✓ | ✓ (per state) | ✓ (on derived features) |
| MatrixProfile | ✓ | ✓ | ✗ |
| Spectral / FFT (future) | ✓ | ✓ (active states only) | ✗ |

**Cost of adapter:** < 0.2 ms per event, < 2 KB state per sensor.

---

### Data Quality Gate

Rule-based filter on every incoming raw event (runs before the adapter, since some quality faults — duplicates, future timestamps — are detectable on the raw stream). Hard min/max bounds per sensor type reject physically impossible values. Tracks inter-arrival time per sensor to detect dropouts (gap > `max_gap`, set by archetype) and batch arrivals. Flags exact timestamp+value duplicates and timestamps that are in the future or stale by > 5 minutes.

For binary sensors, dropout is detected from the device's `checkInterval` heartbeat rather than from data inter-arrival time, since long quiet periods are normal.

**Cost:** < 0.1 ms, rule-based.

### Feature Engineering

Operates on the adapter's canonical feature stream. Appends three groups before PCA:

- **Calendar:** hour, day-of-week, is_weekend, month (4 values).
- **Rolling means:** mean of each adapter feature over 1 h, 24 h, 7 d windows.
- **First differences:** current − previous value per adapter feature.

For Bursty archetype, rolling means and first differences are computed **per state** so that an OFF→ON transition does not look like a feature jump.

**Cost:** < 0.5 ms, circular buffers.

### Sub-PCA (Per-Sensor, Univariate)

TSB-AD-U rank #1. Operates on a single canonical numeric feature stream. Takes a sliding window of recent values (default **m = 125 points**; at 1 sample/min ≈ 2 hours), treats that window as a vector, and projects it onto the principal subspace learned from normal windows during training. High reconstruction error = the current window's shape is unlike any normal shape seen before.

For Bursty archetype, separate Sub-PCA models are trained per `state`; the active model is selected by the current `state` value. Disabled entirely for Binary archetype.

**Window size guidance:** m = 125 is the TSB-AD benchmark default. Tune m to match the shortest anomaly duration you care about. At 1/min: m = 60 covers 1 h, m = 125 covers ~2 h, m = 360 covers 6 h.

**Training:** non-overlapping windows from the bootstrap period (minimum 14 days of normal data). Reconstruction error threshold = 99th percentile of training-period errors. Retrain every 30 days.

**Cost:** < 0.5 ms, < 1 KB model.

### Multivariate PCA (Cross-Sensor)

TSB-AD-M rank #3. Operates on the full enriched feature vector at each timestep. Projects onto the principal subspace of normal feature relationships. High reconstruction error = the combination of features at this moment is unusual.

With one sensor, this still captures calendar context and temporal dynamics, so "unusual value for a Tuesday morning" is detectable. Each additional sensor adds its adapter-emitted features with no architectural change.

For Bursty archetype, separate Multivariate PCA models are trained per `state`.

**Why both Sub-PCA and Multivariate PCA:** Sub-PCA detects unusual shapes within one sensor over time. Multivariate PCA detects unusual combinations across features at one moment. Complementary, not redundant.

**Training:** enriched feature matrix from bootstrap. 99th percentile reconstruction error threshold. Retrain every 30 days, excluding readings flagged as anomalous.

**Cost:** < 0.5 ms, < 1 KB model.

### CUSUM (Page-Hinkley)

Per-feature cumulative sum of deviations from a reference mean. Accumulates small shifts that are individually below PCA's threshold. The only component purpose-built for slow drift.

**Reference mean:** sample mean over the bootstrap period. For Bursty archetype, a separate reference mean is maintained per state, and CUSUM only accumulates while the corresponding state is active.

For Binary archetype, CUSUM runs on `duty_cycle_24h` and `transitions_per_hour` — catches gradual usage shifts (e.g., a leak sensor's host pipe slowly changing usage pattern) and battery decline.

**Parameters:**
- **δ (drift sensitivity):** `0.1 × σ_training`. Smaller δ = more sensitive but more false positives.
- **λ (detection threshold):** `5.0` accumulated drift units.

**Reset:** zero on confirmed anomaly alert or user acknowledgment. Never reset silently.

**Cost:** < 0.1 ms, few bytes/feature.

### Temporal Profiles

Lookup table of (mean, std) per feature per temporal bucket. Each adapter-emitted feature is z-scored against its matching bucket. Updated incrementally via Welford's algorithm.

**Default bucket definition:** `hour_of_day (24) × day_of_week (7) = 168 buckets`. ~24 bytes/bucket. Monthly refinement (×12) added once history allows.

For Binary archetype, profiles operate on derived features (`transitions_per_hour`, `duty_cycle_1h`), not the raw state.

**Z-score threshold:** `|z| > 3.0`. Tune up if alert fatigue is a problem.

**Cold start suppression:** require `n ≥ 5` per bucket; skip silently otherwise.

**Cost:** < 0.1 ms, ~4 KB table per sensor.

### MatrixProfile (Batch)

Computes the z-normalized nearest-neighbor distance for every subsequence in stored history. Discords = most anomalous subsequences. Training-free, parameter-free beyond window size m.

Operates on the canonical numeric feature stream from the adapter. Disabled for Binary archetype (z-normalization on near-constant series is undefined/degenerate).

**Default window size:** `m = 360` points. At 1/min = 6 hours.

**Discord threshold:** Top-3 discords per batch, filtered to MP score > `mean(MP) + 3 × std(MP)`.

**Cost:** Batch only, ~50 MB peak.

---

### Configuration Parameters

Values are derived from the adapter's `GRANULARITY_SEC` (default 60), the sensor's `ARCHETYPE`, and `NUM_SENSORS`.

| Parameter | Formula | Default (1 min, 1 sensor) |
|---|---|---|
| 1h buffer size | `3600 / GRANULARITY_SEC` | 60 points |
| 24h buffer size | `86400 / GRANULARITY_SEC` | 1,440 points |
| 7d buffer size | `604800 / GRANULARITY_SEC` | 10,080 points |
| Sub-PCA window m | `125` (TSB-AD default) | 125 points ≈ 2 h |
| MatrixProfile window m | `360` | 360 points = 6 h |
| Adapter `max_gap` | `5 × expected_interval` (per sensor) | sensor-specific |
| Bursty state model | 2-component GMM, refit every 30 d | — |
| Binary derived windows | 1 h / 24 h | fixed |
| CUSUM δ | `0.1 × σ_training` per feature per state | bootstrap |
| CUSUM λ | `5.0` | 5.0 |
| PCA error threshold | 99th pct of training-period errors per model | bootstrap |
| z-score threshold | `3.0` | 3.0 |
| MP discord threshold | Top-3 per batch + MP > mean + 3×std | — |

These are starting defaults, expected to be tuned after the first few weeks of deployment.

---

### Bootstrap / Cold Start

| Day Range | Active Detectors | Notes |
|---|---|---|
| Days 0–13 | Adapter, data quality gate, CUSUM | Raw events buffered. Bursty state model fit on accumulated data at end of period. |
| Day 14 | Sub-PCA + Multivariate PCA activate | Train per archetype: Continuous = global model; Bursty = one model per discovered state; Binary = on derived features. |
| Day 7+ | Temporal profiles become useful | Apply z-score alerts only to buckets with ≥ 5 samples. |
| Week 4+ | MatrixProfile batch activates | Continuous and Bursty only. First batch on Day 28 over 14-day window. |
| Month 3+ | Monthly temporal bucket refinement | Needs ≥ 3 prior months per bucket. |

**Binary archetype bootstrap caveat:** if zero positive transitions occur during bootstrap (e.g., a leak sensor that never goes wet), CUSUM and temporal profile baselines for transition-based features remain at zero, which is correct — any transition then registers as a strong anomaly. The deterministic state-transition forward to alert output handles the primary detection path regardless.

PCA retraining: retrain every 30 days using the most recent 14 days of data, excluding anomaly-flagged readings. Log model version and training window.

---

### Alert Output Schema

```json
{
  "sensor_id": "string",
  "archetype": "continuous | bursty | binary",
  "timestamp": "ISO-8601",
  "detector": "data_quality_gate | sub_pca | multivariate_pca | cusum | temporal_profile | matrix_profile | state_transition",
  "score": 0.0,
  "threshold": 0.0,
  "anomaly_type": "string or null",
  "raw_value": 0.0,
  "state": "integer or null",
  "window_start": "ISO-8601 or null",
  "window_end": "ISO-8601 or null"
}
```

`anomaly_type` is populated deterministically for data quality gate and state-transition alerts. It is `null` for statistical detectors at baseline.

### Multi-Detector Alert Fusion

When multiple detectors fire on the same sensor within a 5-minute window, they are grouped into a single alert event with the union of time windows and `severity = max(...)`. Data quality gate and state-transition alerts are never fused — they emit immediately and independently.

---

### Coverage by Archetype

The Coverage table below applies to each archetype. An anomaly type marked `—` is structurally inapplicable for that archetype.

| # | Anomaly | Continuous | Bursty | Binary |
|---|---|---|---|---|
| A1 | Spike | ✓ PCA | ✓ PCA per state | — |
| A2 | Dip | ✓ PCA | ✓ PCA per state | — |
| A3 | Out-of-range | ✓ DQG | ✓ DQG | — |
| A4 | Noise burst | ⚠ batch (rolling variance in future) | ⚠ batch | — |
| B1 | Stuck-at | ⚠ deferred (stuck-at detector) | ⚠ deferred | ⚠ via dropout |
| B2 | Calibration drift | ✓ CUSUM | ✓ CUSUM per state | — |
| B3 | Increased noise floor | ⚠ batch | ⚠ batch | — |
| B4 | Intermittent dropout | ✓ DQG | ✓ DQG | ✓ heartbeat |
| B5 | Sensor saturation | ✓ DQG | ✓ DQG | — |
| B6 | Duplicate / stale | ✓ DQG | ✓ DQG | ✓ DQG |
| C1 | Trend | ✓ CUSUM | ✓ CUSUM per state | ✓ CUSUM on duty cycle |
| C2 | Level shift | ✓ CUSUM + PCA | ✓ via state model | ✓ on duty cycle |
| C3 | Frequency change | ⚠ batch (TSPulse later) | ⚠ batch | ✓ transitions/hr |
| C5 | Seasonality disappearance | ⚠ batch | ⚠ batch | ✓ duty_cycle_24h |
| D1 | Time-of-day | ✓ profiles | ✓ profiles per state | ✓ on derived features |
| D2 | Weekend vs weekend | ✓ profiles | ✓ profiles | ✓ |
| D3 | Month vs month | ✓ profiles | ✓ profiles | ✓ |
| D4 | Holiday | deferred | deferred | deferred |
| D5 | Seasonal mismatch | ✓ profiles | ✓ profiles | ✓ |
| E* | Cross-sensor | requires ≥2 sensors | requires ≥2 sensors | requires ≥2 sensors |
| F1 | Unusual occupancy | ✓ profiles + batch | ✓ via state pattern | ✓ via duty cycle |
| F3 | Water leak (sustained) | ✓ CUSUM | ✓ CUSUM | ✓ state_transition (deterministic) |
| F4 | Unusual event sequence | deferred | deferred | deferred |
| G1 | Reporting rate change | ✓ DQG | ✓ DQG | ✓ DQG |
| G2 | Clock drift | ✓ DQG | ✓ DQG | ✓ DQG |
| G3 | Batch arrival | ✓ DQG | ✓ DQG | ✓ DQG |
| H1 | Concept drift | deferred (dual-model PCA) | deferred | deferred |
| H2 | Degradation trajectory | ✓ CUSUM long window | ✓ CUSUM | ✓ on duty cycle |

Cross-sensor types (E1–E4, F2) become detectable as soon as a second sensor of any archetype is present.

---

## Future Improvements

Improvements are grouped by what they unlock. Add them based on observed need.

### When to Add What

| Trigger | Addition |
|---|---|
| Sensors start producing flatline readings | Stuck-at detector (Continuous/Bursty only) |
| Need frequency/seasonality detection or missing-data handling | TSPulse replaces MatrixProfile |
| Noise or volatility anomalies matter | Rolling variance + spectral features (Continuous/Bursty only) |
| Need "HVAC on but not cooling" type detection | Event sequence rules |
| False positives on holidays | Holiday calendar |
| Subtle sensor pair decorrelation matters | Cross-sensor correlation monitor |
| Alert fatigue from legitimate behavioral changes | Dual-model PCA |
| Bursty state model drifts | Online GMM refitting |

---

### Close Sensor Gaps

**Stuck-at Detector** *(Continuous, Bursty)* — Counts consecutive identical readings (within ±ε). Tracks rolling min−max range. Zero variance = sensor fault. Skipped for Binary (constant state is normal). *Closes B1 for numeric archetypes.*

**TSPulse (replaces MatrixProfile)** *(Continuous, Bursty)* — IBM's 1M-parameter foundation model. Dual-space (time + frequency) masked reconstruction. GPU-free inference. Handles missing data via imputation. *+16% VUS-PR over MatrixProfile. Upgrades C3, C5 for numeric archetypes.*

**Rolling Variance Features** *(Continuous, Bursty)* — Per-feature rolling variance at 1h/24h/7d appended to the feature vector. Makes PCA sensitive to volatility changes. *Closes A4, B3, C6.*

**Spectral Features** *(Continuous, Bursty active states)* — Dominant frequency and spectral centroid from rolling 256-point FFT, appended to feature vector. *Real-time C3, C5.* Skipped for Binary; skipped in off-state for Bursty.

**CUSUM on Variance** *(Continuous, Bursty)* — Same Page-Hinkley applied to rolling variance.

**After these additions:** < 2.5 ms, < 5 MB RAM. The 256-point FFT adds ~0.5–1 ms on RPi 4.

---

### Cross-Sensor Intelligence

**Cross-Sensor Correlation Monitor** — Running Pearson correlation over a sliding window for configured sensor pairs. Coefficients appended to multivariate PCA feature vector. Direct alert if a historically strong correlation drops below a floor. Works across archetypes since correlation is computed on adapter-emitted numeric features. *Closes E1, E4. Strengthens E2.*

**Event Sequence Rules** — Lightweight state machine on `state_transition` events (which all archetypes can emit — Bursty via state index, Binary natively, Continuous via threshold-crossing rules). Per-deployment domain configuration. *Closes E3, F4.*

**Holiday Calendar** — Holiday flag added to calendar encoding. Holiday-specific temporal profile buckets. *Closes D4.*

**After these additions:** < 2 ms, < 6 MB RAM.

---

### Adaptation and Interpretability

**Dual-Model PCA** — Stable (30-day) + recent (7-day) models. When recent says normal but stable flags anomaly for 14+ consecutive days, reclassify as concept drift. Per-state for Bursty. *Closes H1.*

**Interpretability Layer** — Decision tree over which detectors fired → anomaly type label. PCA contribution decomposition identifies the responsible feature. Output: sensor name, anomaly type, duration, confidence, suggested action.

**Online GMM Refit** *(Bursty)* — Detects when the bursty state model itself has drifted (new appliance behavior, additional load mode). Triggers PCA per-state retraining with the new state set.

---

## How References Support the Pipeline

| Design Decision | Reference | What It Proves |
|---|---|---|
| PCA as core real-time detector | [1] TSB-AD (NeurIPS 2024) | PCA #1 univariate, #3 multivariate across 40 algorithms / 1,070 series. |
| TSPulse for batch; spectral features | [2] TSPulse (2025) | #1 on both TSB-AD leaderboards, GPU-free. Dual-space validates frequency features. |
| Edge-class compute budget | [3] Edge AI for Smart Homes (2025) | 22 ms (IF) / 35 ms (LSTM-AE) on RPi 4. Our < 2 ms is well within budget. |
| Suppression layer over flat ensemble | [4] TSB-AutoAD (PVLDB 2025) | Selective ensembling beats running every detector. |
| Adapter layer with archetype classification | [5] Smart Environments Survey (IEEE Access 2024) | Mixed-type data (continuous + binary + intermittent) is the core challenge. Per-type handling is the recommended response. |

---

## Appendix: Applying to SmartThings Outlet & Water Leak Sensor

### Outlet (`switch`, `power`, `energy`, `voltage`)

The outlet exposes multiple capabilities; each registers as its own logical sensor.

| Capability | Archetype | Adapter notes |
|---|---|---|
| `switch` | Binary | Native binary; emits derived features. |
| `power` | Bursty | 2-component GMM splits idle vs active. PCA per state. |
| `energy` | Bursty | **Differenced** to Wh/min before resampling. Treated as a derived rate, not a counter. |
| `voltage` | Continuous | Should be ~constant; CUSUM + DQG dominate. |

### Water Leak Sensor (`water`, `temperature`, `battery`)

| Capability | Archetype | Adapter notes |
|---|---|---|
| `water` | Binary | `wet` transition forwarded directly to alert output (deterministic). Statistical detectors run on derived features (transitions/hr, duty cycle) for usage trends. |
| `temperature` | Continuous | Standard pipeline. |
| `battery` | Continuous | CUSUM dominates (slow monotonic decline); PCA contributes little but costs nothing. |

For both devices, dropout detection uses the SmartThings `checkInterval` heartbeat rather than data inter-arrival timing.
