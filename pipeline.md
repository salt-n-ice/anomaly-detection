# Smart Home Sensor Anomaly Detection — Pipeline

A streaming pipeline that turns raw sensor events into household-facing
anomaly notifications. Each event flows through six in-memory stages,
fully event-driven, ~microseconds per event.

## Data flow

```
Event(sensor_id, capability, value, timestamp)
        │
        ▼
   ┌──────────┐    Per archetype: resamples to a fixed tick rate,
   │ Adapter  │    tracks state (CONTINUOUS rolling window, BURSTY
   └────┬─────┘    on/off events, BINARY transitions). Emits a
        │         uniform tick stream + ev objects to detectors.
        ▼
   ┌──────────┐    Stateless threshold check on every raw event:
   │   DQG    │    out-of-range, dropout (gap), saturation, clock
   └────┬─────┘    drift, extreme_value. Sub-second fire path.
        │
        ▼
   ┌──────────┐    Statistical detectors fed by adapter ticks:
   │ Detectors│      CONTINUOUS  → RecentShift
   │  (per    │      BURSTY      → DutyCycleShift, RollingMedianPeak
   │ archtype)│      BINARY      → StateTransition
   └────┬─────┘    Each compares current rolling state to a frozen
        │         bootstrap baseline (median + MAD or quantiles).
        ▼
   ┌──────────┐    Per-sensor fuser. Fires within a gap window are
   │  Fuser   │    stitched into one chain so the user sees ONE
   └────┬─────┘    notification per anomaly window.
        │           CONTINUOUS gap = 15 min; BURSTY/BINARY = 4 h;
        │           max chain span = 96 h.
        ▼
   ┌──────────┐    Maps the chain's detector signature + timestamp
   │ Classify │    to a canonical anomaly_type (level_shift,
   └────┬─────┘    time_of_day, weekend_anomaly, frequency_change,
        │         spike, dip, water_leak_sustained, …) and a
        │         label_class (user_behavior | sensor_fault).
        ▼
   ┌──────────┐    Builds a structured bundle: window, magnitude,
   │ Explain  │    temporal context, detector evidence, rate
   │ (bundle) │    context, classification block. Pure post-
   └────┬─────┘    detection summarisation; no extra detection logic.
        │
        ▼
   ┌──────────┐    Renders the bundle as Markdown for an LLM
   │  Prompt  │    consumer ("# Anomaly on sensor X …"). The
   └────┬─────┘    prompt is signal-rich, verdict-light: heuristic
        │         classification surfaced as advisory hint, body
        │         dominated by raw evidence so the LLM can
        │         override based on household context.
        ▼
   Household-facing notification
```

## Components (what ships in deployment)

### Adapter (`src/anomaly/adapter.py`)
Per-sensor instance, one of three subclasses by archetype:
- **CONTINUOUS** (e.g. mains voltage, basement temp): rolling window of
  recent values, derives instantaneous + first-difference features.
- **BURSTY** (e.g. outlet power, kettle): event-segmenter — detects
  rising/falling edges, tracks the current event's peak + duration.
- **BINARY** (e.g. leak, switch): state machine, emits
  transitions and tracks time-in-state.

All adapters emit a uniform `(tick, event)` stream consumed by detectors.
Per-sensor state is bounded by the rolling window (typically minutes to
a few hours of buffered ticks).

### Detectors (`src/anomaly/detectors.py`)
Five active classes, registered per archetype in `profiles.py`:

| Detector | Archetype | What it catches |
|---|---|---|
| `DataQualityGate` | all | out_of_range, dropout, extreme_value, clock_drift, saturation, duplicate_stale (instantaneous threshold checks) |
| `RecentShift` | CONTINUOUS | sustained shifts in the rolling-mean tail (level shifts, drifts) |
| `DutyCycleShift` | BURSTY | fraction-of-time-on over a 6h window deviating from baseline |
| `RollingMedianPeakShift` | BURSTY | per-event peak magnitude vs bootstrap median+MAD |
| `StateTransition` | BINARY | 0→1 transitions on water/leak sensors |

Each detector loads frozen bootstrap stats (median, MAD, quantiles)
fitted on the first 7-14 days of normal traffic, and a small rolling
state buffer for live evaluation.

### Fuser (`src/anomaly/fusion.py::DefaultAlertFuser`)
Per-sensor instance. Holds the most recent unflushed alerts and chains
co-fires within a gap window. Emits one chain per anomaly window with
`window_start`, `window_end`, `first_fire_ts`, `score`, and the
detector union.

### Classifier (`src/anomaly/explain/classify.py::classify`)
Stateless function: takes a fused chain + magnitude + temporal context
and returns `(type, class, confidence, signal_classes)`. Pre-typed
alerts (DQG, StateTransition) pass through; detector-combo chains walk
a decision tree based on which signals fired and the calendar context
of the chain.

### Explain layer (`src/anomaly/explain/`)
- **`bundle.explain(alert, events_df)`** — assembles the structured
  bundle dict from the alert + recent events.
- **`prompt.build_prompt(bundle)`** — renders the bundle as the
  Markdown prompt the LLM consumer reads.

## Sensor config

YAML, one entry per sensor:

```yaml
sensors:
  - id: outlet_kettle_power
    capability: power
    archetype: bursty
    expected_interval_sec: 300
    min_value: 0
    max_value: 3000
```

`min_value` / `max_value` drive `DataQualityGate.out_of_range`;
`expected_interval_sec` drives the `dropout` / `clock_drift` checks.
Sensors not in the config are silently dropped by `Pipeline.ingest`.

## Bootstrap

Detectors are silent on a sensor for its first 7-14 days
(`--bootstrap-days`). During that window they fit their baseline stats
(median, MAD, quantiles) and freeze them. After bootstrap there is no
online retraining — `RollingMedianPeakShift` updates its peak median
additively but the alert thresholds stay locked.

## State / storage in production

In-memory, per sensor:

| Component | State | Footprint |
|---|---|---|
| Adapter | rolling tick window + state vars | few KB |
| DataQualityGate | scalar counters + last-fire timestamps | ~16 floats |
| RecentShift | bootstrap quantiles + rolling summary | ~10 floats |
| DutyCycleShift | bootstrap median/MAD/q01/q99 + 6h rolling deque of `(ts, on/off)` pairs | ~few KB |
| RollingMedianPeakShift | bootstrap median+MAD + 5-event peak deque | ~10 floats |
| StateTransition | last trigger ts | 1 timestamp |
| Fuser | last-emit ts, chain span tracker | ~5 floats |

**Constant per sensor**, no growth over runtime, no external store.
A 1k-sensor fleet fits in a few MB of pipeline RAM.

## Latency budget

- Per-event compute through `Pipeline.ingest`: **microseconds**
  (in-memory scalar ops over 3-4 detectors + fuser).
- Time from anomaly onset to first chain emit:
  - DQG-pre-typed (sensor faults): **sub-second**.
  - Behavioral chains (DutyCycle / RollingMedianPeak / RecentShift /
    StateTransition): governed by detector tick interval + fuser gap.
    Typical user-visible p95 is **15 min – several hours** for
    sustained behavioural anomalies.
- Bootstrap: detectors silent for the first 7-14 days per sensor (one-time).

## Output

`Pipeline.ingest(event)` returns a list of zero or more `Alert`
objects. Each fully-fused chain comes through with:

```python
Alert(
  sensor_id, capability, timestamp, detector,    # detector union as "+"-joined string
  score, threshold, anomaly_type, window_start,
  window_end, first_fire_ts, context,
)
```

The deployment consumer calls `bundle.explain(alert, events_df)` →
`prompt.build_prompt(bundle)` to get the LLM-ready Markdown for the
household notification.

## What's NOT in deployment

- **CSV-replay path** (`python -m anomaly run / eval / explain`) —
  research/offline only. Reads `events.csv` upfront, replays through
  `Pipeline.ingest`, writes detections at end. Not a streaming
  pattern.
- **Bundle JSONL writer** (`csv.explain_detections_csv`) — also
  CSV-replay only. Production callers invoke `bundle.explain()` per
  alert directly; no CSV round-trip.
- **Research harness** (`research/run_research_eval.py`,
  `research/explain/*`) — gitignored, local-only. Headline metric
  evaluation against ground truth, baselines, iteration logs.
- **MatrixProfile, CUSUM, PCA, BOCPD, TemporalProfile, etc.** —
  removed in `bf6adbc` (chore: prune dead detectors). The current
  five-detector set is the deployment surface; ~1970 LOC of legacy
  detectors was pruned with byte-identical detection CSVs across all
  scenarios (zero behaviour change).
