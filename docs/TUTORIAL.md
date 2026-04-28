# Deployment Tutorial

How the anomaly-detection pipeline is meant to be deployed and
operated. Detection only — the output is a Markdown prompt per
detected anomaly that a downstream LLM consumes.

For internal design, see `pipeline.md`. For metric definitions, see
`docs/METRICS.md`. For setup commands, see `README.md`.

---

## 1. End-to-end picture

```
events.csv                   per-sensor stream of raw readings (input)
        │
        ▼
  Pipeline                   per sensor:
    ├ adapter                  resample to uniform 1-min ticks
    ├ DataQualityGate          rule-based pre-adapter checks (always on)
    ├ statistical detectors    fire on shifts/peaks/duty-cycle/state changes
    └ fuser                    group overlapping fires into one Alert
        │
        ▼
  classify + explain         per Alert:
    ├ inferred_type            canonical anomaly type (level_shift, etc.)
    ├ inferred_class           user_behavior | sensor_fault | unknown
    └ build_prompt             Markdown for the LLM
        │
        ▼
detections.csv (one row per Alert) + bundles.jsonl (one JSON bundle per Alert)
```

Two output shapes leave the pipeline:

- `detections.csv` — flat one-row-per-Alert table consumed by metrics
  / viz / replay tools.
- `bundles.jsonl` — one structured bundle per Alert. Each bundle
  renders to a Markdown prompt the deployment hands to the LLM.

---

## 2. Sensor archetypes

Every sensor must be declared as one of three archetypes. The
archetype fixes the adapter + detector roster.

| Archetype       | Examples                          | Adapter                                                   | Detectors fired                                       |
|-----------------|-----------------------------------|-----------------------------------------------------------|-------------------------------------------------------|
| **CONTINUOUS**  | voltage, temperature              | linear interp to 1/min ticks; NaN on gaps                 | `DataQualityGate` + `RecentShift`                     |
| **BURSTY**      | outlet power, water flow rate     | zero-order hold + 2-mode state model (idle/active)        | `DataQualityGate` + `DutyCycleShift` + `RollingMedianPeakShift` |
| **BINARY**      | water leak, contact switch        | forward-fill + duty-cycle + transition counters           | `DataQualityGate` + `StateTransition`                 |

`DataQualityGate` runs pre-adapter and is always on (no bootstrap
needed). It fires on out-of-range, extreme-value, dropout, saturation,
clock-drift, duplicate, and batch-arrival rule violations.

Statistical detectors run post-adapter and need a bootstrap window
(default 14 days) of representative normal data before they activate.

---

## 3. Sensor configuration (`configs/*.yaml`)

```yaml
sensors:
  - id: outlet_fridge_power
    capability: power
    archetype: bursty             # continuous | bursty | binary
    expected_interval_sec: 300    # nominal cadence; max_gap = 5×
    min_value: 0
    max_value: 3000
    cumulative: false             # BURSTY only: counter-style? (rare)
    granularity_sec: 60           # tick rate

  - id: mains_voltage
    capability: voltage
    archetype: continuous
    expected_interval_sec: 600
    min_value: 80
    max_value: 140

  - id: basement_leak
    capability: water
    archetype: binary
    expected_interval_sec: 7200
    heartbeat_sec: 7200           # BINARY only: liveness expectation
    deterministic_trigger: true   # BINARY: state→1 fires immediately
```

The pipeline keys on `(sensor_id, capability)`. A single device
publishing two streams (e.g., a smart plug emitting both power and
energy) needs two entries.

`min_value` / `max_value` are physical bounds; `DataQualityGate` fires
on crossings. They should reflect the sensor spec, not data
distribution.

Bundled examples: `configs/household.yaml`, `configs/leak_30d.yaml`.

---

## 4. Input — `events.csv`

```
timestamp,sensor_id,capability,value,unit
2026-02-01T00:00:00+00:00,outlet_fridge_power,power,41.5,W
2026-02-01T00:00:00+00:00,mains_voltage,voltage,122.47,V
```

- `timestamp` — ISO-8601 UTC.
- `sensor_id` / `capability` — must match a row in the sensor config.
- `value` — float.
- `unit` — informational; not parsed.

Events for sensors not in the config are silently skipped.

---

## 5. Output — `detections.csv`

One row per emitted Alert.

| Column           | Meaning                                                                           |
|------------------|-----------------------------------------------------------------------------------|
| `sensor_id`      | Sensor that fired.                                                                |
| `capability`     | `power` / `voltage` / `temperature` / `water` / etc.                              |
| `start`          | Analysis-window start (used by coverage metrics).                                 |
| `end`            | Analysis-window end / chain emit time.                                            |
| `first_fire_ts`  | Earliest component tick in the chain (used by latency).                          |
| `fire_ticks`     | Semicolon-joined ISO timestamps of every component fire tick in the chain.        |
| `anomaly_type`   | Pre-typed label from DQG / state_transition; falls back to detector name on statistical chains. |
| `inferred_type`  | Canonical type assigned by the explainer (see §7).                                |
| `inferred_class` | `user_behavior` / `sensor_fault` / `unknown` — surfaces whether this row should reach the household-facing LLM. |
| `detector`       | Detector name; fused chains use `"a+b+c"`.                                        |
| `threshold`      | Detector threshold at fire time.                                                  |
| `score`          | Raw detector score.                                                               |

The deployment-relevant filter is `inferred_class`: rows with
`inferred_class == sensor_fault` are infrastructure signals (sensor
calibration, dropouts) and typically suppressed from user-facing
notifications.

---

## 6. Output — `bundles.jsonl` (LLM input)

One JSON bundle per Alert. Schema:

```jsonc
{
  "alert_id":   "<sensor>|<capability>|<window_start>",
  "sensor":     "outlet_fridge_power",
  "capability": "power",
  "archetype":  "BURSTY",
  "window":     { "start": "...", "end": "...", "duration_sec": 60.0 },
  "classification": {
    "type":           "level_shift",
    "class":          "user_behavior",
    "presentation":   "user_visible",
    "confidence":     "high",
    "signal_classes": ["duty", "peak"]
  },
  "magnitude":  { "baseline": 1.5,  "baseline_source": "prewindow_2h",
                  "peak":     9999, "delta":           9997.5,
                  "delta_pct": 666500.0 },
  "temporal":   { "weekday": "Monday", "hour": 11, "is_weekend": false,
                  "month": "February",  "time_of_day_bucket": "morning",
                  "same_hour_weekday_z": 3.2,
                  "same_hour_weekday_n": 8 },
  "detectors":         ["data_quality_gate"],
  "detector_context":  [{"detector":"data_quality_gate", ...}],
  "score": 9999.0
}
```

Pass each bundle to `build_prompt(bundle)` to render Markdown:

```python
from anomaly.explain import build_prompt
prompt = build_prompt(bundle)
# hand `prompt` to the LLM along with whatever household / device
# context the deployment maintains externally
```

The prompt is signal-rich and verdict-light: it lays out the magnitude,
calendar context, signal classes, and detector evidence, then ends
with the heuristic classification as an advisory hint that the LLM
can override.

---

## 7. The anomaly-type vocabulary

`inferred_type` is one of these canonical strings (mirrors the
ground-truth vocabulary the synthetic-generator emits).
`type_to_class(inferred_type)` maps to the class column; anything
outside both sets resolves to `unknown`.

### user_behavior — what the household gets

| type                     | what the alert tells the household                                                   |
|--------------------------|--------------------------------------------------------------------------------------|
| `spike`                  | brief over-power surge — faulty appliance, pre-breaker / pre-fire signal             |
| `dip`                    | voltage dip = grid or wiring fault; fridge temp dip = door left open / seal broken   |
| `level_shift`            | appliance unplugged, replaced, or left running — equipment-state visibility          |
| `trend`                  | gradual motor / compressor wear — service the appliance before it fails              |
| `degradation_trajectory` | multi-week decline (HVAC filter clogging, fridge dying) — pre-failure replacement    |
| `frequency_change`       | cadence shifted — guest staying, newborn, work-from-home onset                       |
| `seasonality_loss`       | expected daily pattern missing — homeowner traveled or appliance silently broken     |
| `time_of_day`            | usage at off-hours — vampire loads, hidden leaks, late-night activity                |
| `weekend_anomaly`        | weekend-vs-weekday split — WFH transition, vacation mode, lifestyle change           |
| `month_shift`            | sustained shift over weeks — utility-grid adjustment or appliance running constantly |
| `seasonal_mismatch`      | AC in winter / heater in summer — broken thermostat or HVAC misconfiguration         |
| `water_leak_sustained`   | minutes-not-hours alert; prevents thousands in water damage                          |
| `usage_anomaly`          | day with markedly elevated activity — party, sick day, unattended appliance          |

### sensor_fault — what operations gets

| type                    | what the alert tells the deployer                                                |
|-------------------------|----------------------------------------------------------------------------------|
| `out_of_range`          | reading beyond physical bounds — wiring or hardware fault; data not trustworthy  |
| `saturation`            | pinned at min/max — broken transducer or disconnected wire; replace sensor       |
| `noise_burst`           | short-burst noise — EMI source or impending hardware failure                     |
| `noise_floor_up`        | baseline noise rising — sensor degrading toward failure                          |
| `stuck_at`              | value frozen — sensor halted; physical inspection needed                         |
| `calibration_drift`     | gradual offset — schedule recalibration before readings mislead                  |
| `dropout`               | reads stopped — dead battery, network loss, or sensor failure                    |
| `duplicate_stale`       | same reading repeated — upstream cache stuck or sensor halt                      |
| `reporting_rate_change` | cadence shifted — firmware change, network throttling, or pre-failure signal     |
| `clock_drift`           | timestamps drifting — NTP / RTC issue; cross-sensor correlation at risk          |
| `batch_arrival`         | many events landing at once — network buffering or connectivity problem          |

---

## 8. Bootstrap

Every statistical detector needs `bootstrap_days` of data before it
activates. Default is 14 days (use 7 for very short scenarios).

During bootstrap on a given sensor:
- `DataQualityGate` still fires (it's rule-based, no fit needed).
- All other detectors are silent — they're collecting data.

After bootstrap:
- BURSTY adapters fit a 2-means state model (idle vs active).
- The feature engineer warms its rolling buffers.
- Each detector calls `fit()` on the buffered bootstrap rows and
  flips `live=True` if it has enough signal.

**Bootstrap data must be representative normal behavior.** Anomalies
that occur during bootstrap silently train the models against
themselves and become invisible afterward. If a sensor is being
onboarded onto a known-anomalous installation, hold the deployment
back until you have a clean window — or pre-fit and ship the fitted
state.

The window is wall-clock from the sensor's first event, **not**
calendar time. A sensor with sparse cadence may take longer than
14 calendar days to accumulate 14 bootstrap-equivalent days of data.

---

## 9. Bootstrap and ongoing operation timeline

```
day 0       sensor first event
day 0-14    DQG only fires; statistical detectors silent
day 14      _maybe_fit runs; detectors flip live
day 14+     full pipeline live; alerts emit on chain close
```

Two adaptive behaviors run automatically post-bootstrap:

- **Fuser chain max_span = 96h.** Any fused chain that runs longer
  than 96h closes and emits regardless of activity. A long sustained
  anomaly produces a sequence of 96h chunks rather than one indefinite
  chain.

- **Consecutive-max-span detector adapt.** After three consecutive
  max-span chains on a sensor (≈12 days of continuous firing), the
  pipeline calls each detector's `adapt_to_recent(rows)` to refit its
  baseline from the recent rolling buffer. This stops the chain from
  re-forming forever when an anomaly has effectively become the new
  normal — important for behavior changes (lifestyle shifts) the user
  doesn't want to be alerted on after the first ~2 weeks.

---

## 10. Fuser configuration

| Archetype  | Inactivity gap | Max span | Why                                                                |
|------------|---------------:|---------:|--------------------------------------------------------------------|
| CONTINUOUS | 15 min         | 96 h     | tight gap — CONT detectors fire densely on real shifts             |
| BURSTY     | 4 h            | 96 h     | must absorb DCS-6h's 2h cooldown + RMP's 6h cooldown into one chain|
| BINARY     | 4 h            | 96 h     | event-driven; a single chain per occupancy/leak episode            |

The fuser receives all alerts from a tick and accumulates them into
`_pending`. When the gap or max_span condition trips, the pending
chain is collapsed into one Alert (top-scorer's metadata, joined
detector list, union of windows, earliest first_fire, concatenated
context). One Alert = one downstream LLM call.

`DataQualityGate` non-dropout fires (out_of_range, saturation, etc.)
and `StateTransition` fires bypass the fuser entirely — they emit
immediately, one alert per tick.

---

## 11. CLI

```powershell
# Run the pipeline
python -m anomaly run `
  --events  ..\synthetic-generator\out\household_60d\events.csv `
  --config  configs\household.yaml `
  --out     out\household_60d_detections.csv `
  --bootstrap-days 14

# Render bundles + prompts (LLM input)
python -m anomaly explain `
  --events     ..\synthetic-generator\out\household_60d\events.csv `
  --detections out\household_60d_detections.csv `
  --out        out\household_60d_bundles.jsonl
```

Pythonic alternative — drive the live path in-process for streaming
deployments:

```python
from anomaly.pipeline import Pipeline
from anomaly.explain import explain, build_prompt

pipe = Pipeline(configs, bootstrap_days=14.0)
for ev in event_stream:
    for alert in pipe.ingest(ev):
        bundle = explain(alert, events_df)
        prompt = build_prompt(bundle)
        send_to_llm(prompt, bundle["classification"])
```

The live path preserves detector-native context that the CSV
roundtrip strips. For batch deployments either path produces the same
bundle schema.

---

## 12. Operational notes

**Multi-tenancy.** Each `(sensor_id, capability)` has its own
independent state. Different households are separated only at the
input level — feed each tenant's events through a separate `Pipeline`
instance.

**Sparse sensors.** A leak sensor publishing once an hour will accept
the same 14-day bootstrap clock but takes longer to accumulate enough
post-bootstrap signal for tight statistics. The `RecentShift` /
`DutyCycleShift` activations gate on minimum sample counts in `fit()`,
so a quiet sensor stays effectively in DQG-only mode until enough
data lands.

**Onboarding a new sensor archetype.** Subclass `Adapter` in
`src/anomaly/adapter.py`, register it in `ADAPTER_REGISTRY`, and add
a profile entry in `src/anomaly/profiles.py`. Downstream code is
archetype-agnostic — detectors consume whatever feature dict the
adapter emits.

**Onboarding a new anomaly type.** Add the canonical name to
`USER_BEHAVIOR_TYPES` or `SENSOR_FAULT_TYPES` in
`src/anomaly/explain/types.py`. If the existing classifier dispatch
in `src/anomaly/explain/classify.py` doesn't route it correctly, add
a branch there.

**Suppressing sensor_fault alerts from user-facing notifications.**
Filter `detections.csv` (or the live alert stream) on
`inferred_class == "user_behavior"` before invoking the LLM.
`unknown` rows are typically detector-combo strings on chains the
classifier couldn't confidently route; treat them as low-priority.

**Pre-fitting in production.** For deployments that can't tolerate a
14-day silent bootstrap, the `Pipeline` exposes the per-sensor
`_SensorState` dict; you can serialize fitted detectors from a
training run and deserialize at deploy time. There's no first-class
API for this yet — it's done by pickling `_states`.
