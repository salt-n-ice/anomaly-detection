# Smart Home Sensor Anomaly Detection — Pipeline

A streaming, in-memory pipeline that turns raw sensor events into
household-facing anomaly notifications. Single-process Python,
microseconds per event, ~15–20 MB resident per sensor.

## Real-time data flow

```
Event(sensor_id, capability, value, timestamp)
          │
          ▼
   ┌──────────────┐  SHORT-band check on every raw event. Threshold
   │ DataQuality  │  + cadence checks vs config (min/max, expected
   │   Gate       │  interval). Fires sub-second; bypasses bootstrap.
   └──────┬───────┘
          │
          ▼
   ┌──────────────┐  Per-archetype resampler — aligns events to a
   │  Adapter     │  fixed 60 s tick:
   │              │    CONTINUOUS  → linear interpolation
   │              │    BURSTY      → k-means state (off/on) assignment
   │              │    BINARY      → state hold + transition tracking
   └──────┬───────┘  Gaps > 5 × expected_interval mark the tick as
          │         dropout.
          ▼
   ┌──────────────┐  Adds rolling means (1 h / 24 h / 7 d) per
   │ Feature      │  (state, feature) to each tick via O(1) running
   │ Engineer     │  sums.
   └──────┬───────┘
          │
          ▼
   ┌──────────────┐  MEDIUM-band statistical detectors:
   │  Detectors   │    CONTINUOUS  → RecentShift
   │              │    BURSTY      → DutyCycleShift,
   │              │                  RollingMedianPeakShift
   │              │    BINARY      → StateTransition (immediate)
   └──────┬───────┘  Compare live rolling state to the per-sensor
          │         baseline fit during bootstrap.
          ▼
   ┌──────────────┐  Per-sensor chain assembler. Co-fires within
   │  Fuser       │  `gap` stitch into one chain so the user sees
   │              │  one notification per anomaly window.
   │              │    CONTINUOUS  gap = 15 min
   │              │    BURSTY/BIN  gap = 4 h
   │              │    max_span    = 96 h
   └──────┬───────┘
          │
          ▼
   ┌──────────────┐  Walks a decision tree on (detector signature,
   │  Classify    │  direction, calendar position, magnitude) →
   │              │  (anomaly_type, label_class). Pre-typed alerts
   └──────┬───────┘  (DQG, StateTransition) pass through.
          │
          ▼
   ┌──────────────┐  bundle.explain → prompt.build_prompt produces
   │  Explain     │  Markdown for the LLM consumer. Signal-rich,
   │              │  verdict-light: the heuristic class is advisory;
   └──────┬───────┘  the LLM can override with household context.
          │
          ▼
   Household-facing notification
```

## What each detector does

Per-sensor instances. SHORT-band runs per raw event; MEDIUM-band runs
per 60 s tick after the 14-day bootstrap.

| Detector | Archetype | Mechanism | Catches |
|---|---|---|---|
| **DataQualityGate** | all | Per-event threshold checks against `min_value` / `max_value` / `expected_interval`, with per-rule cooldowns to suppress oscillation around boundaries. | out_of_range, dropout, saturation, extreme_value, clock_drift, duplicate_stale, batch_arrival |
| **RecentShift** | CONTINUOUS | `value_roll_1h` vs `value_roll_24h` / `_7d`; fires when ❘delta❘ exceeds the bootstrap-quantile threshold × `min_score`. | level_shift, calibration_drift, month_shift on continuous signals |
| **DutyCycleShift** | BURSTY | Rolling 6 h fraction-of-time-on vs bootstrap median ± MAD (z-score). Percentile-novelty gate engages when MAD collapses to its floor on bimodal-zero sensors. Per-(weekend, hour) bucket map disambiguates calendar patterns. | frequency_change, time_of_day, weekend_anomaly, level_shift on outlets |
| **RollingMedianPeakShift** | BURSTY | Median of last 5 event peaks vs bootstrap peak median ± MAD (z-score). Magnitude-based, orthogonal to DCS. | trend, degradation_trajectory, level_shift on outlet peaks |
| **StateTransition** | BINARY | Fires immediately on 0→1 transitions, only for sensors marked `deterministic_trigger: true`. | water_leak_sustained |

## Bootstrap and continuous adaptation

**Bootstrap (14 days per sensor, one-time per cold start).** Medium-band
detectors are silent. Each sensor accumulates ticks, then `fit()`
computes its baseline:

- `RecentShift` — quantile of |short − baseline| deltas
- `DutyCycleShift` — median / MAD / q01 / q99 over sliding 6 h windows
  + per-(weekend, hour) bucket calendar baseline
- `RollingMedianPeakShift` — median + MAD of per-event peaks
- `BurstyAdapter` — k-means state centers (off / on)

DQG and StateTransition do not bootstrap; they fire from event 1.

**The system does NOT freeze after bootstrap.** Three independent
adaptation mechanisms keep baselines current:

1. **Pipeline-level adapt** (`pipeline.py:140`) — after three
   consecutive max-span chains (~12 days of continuous firing) on a
   sensor, the pipeline calls `detector.adapt_to_recent()` with the
   last 144 h of feature rows; detectors re-fit baselines from that
   window. The streak resets on any non-max-span emit (chain ended
   naturally) and after each adapt.
2. **RMP self-adapt** (`detectors.py:418`) — after three
   cooldown-spaced fires (~18 h sustained high-|z|) inside a 24 h-quiet
   window, `RollingMedianPeakShift` re-fits `boot_median`/`boot_mad`
   from its last 20 event peaks, with a MAD-only-grow floor.
3. **DQG `extreme_value` ratchet** (`detectors.py:92`) — the reference
   max updates on every event during calibration (first 100 events),
   then on every fire. Sustained high values continuously re-anchor
   the threshold upward.

Adaptation is intentionally conservative: gated on sustained firing,
sized in days. **Silent drift (regime change below the firing
threshold) does not trigger adapt** — the system stays calibrated to
its bootstrap until something fires.

## Per-sensor state in production

In-memory, per sensor, post-bootstrap:

| Component | State | Footprint |
|---|---|---|
| Adapter | 1–2 buffered raw points; k-means centers (BURSTY); 1 h / 24 h history (BINARY) | < 100 KB |
| DataQualityGate | scalar counters + last-fire timestamps + 12-event burst deque | < 1 KB |
| **FeatureEngineer rolling buffers** | per (state × feature × window) deques — 1 h / 24 h / **7 d** sized in ticks; e.g. 4 features × 3 windows × 2 states for BURSTY | **~2 MB** |
| RecentShift | bootstrap quantile threshold per baseline feature | < 1 KB |
| DutyCycleShift | bootstrap stats + 6 h rolling `(ts, on/off)` deque + 48-cell bucket map | ~10 KB |
| RollingMedianPeakShift | bootstrap median + MAD + 5-event + 20-event peak deques | < 1 KB |
| StateTransition | last trigger ts | 1 timestamp |
| Fuser | pending alert chain + last-newest ts | < 1 KB |
| **Pipeline `recent_rows` ring** | 144 h × 60 enriched feature dicts; held so `adapt_to_recent` has a re-fit window when the K=3 max-span streak fires | **~5–10 MB** |

**Total ~15–20 MB per sensor in Python.** A 5-sensor home is ~100 MB;
a 1000-sensor fleet is ~15 GB at single-process scale — shard by
household / tenant for fleets.

**Bootstrap memory spike** (one-time, cold start): `bootstrap_raw`
accumulates 14 days of adapter output (~10 MB / sensor) before `fit()`
runs, then is released. Could be made streaming-online but isn't
currently.

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

- `min_value` / `max_value` drive `DataQualityGate.out_of_range`.
- `expected_interval_sec` drives `dropout` (gap > 5 × expected) and
  `clock_drift` (per-tick deviation > 0.5 %) checks.
- `archetype` selects which medium-band detectors load.
- Sensors not in the config are silently dropped by `Pipeline.ingest`.

## Latency budget

- **Per-event compute** through `Pipeline.ingest`: microseconds —
  in-memory scalar ops over the adapter, feature engineer, 3–4
  detectors, and the fuser.
- **Onset → first chain emit**:
  - DQG / StateTransition (sensor faults, water leak): sub-second.
  - DCS / RMP / RecentShift: detector cooldown + fuser gap. Median
    observed latency across the eval suite is 2.6 h; on-time rate
    against per-type MET budgets is 76 %.
- **Bootstrap silence**: 14 days per sensor, one-time per cold start.
- **Adaptation**: triggers after ~12 days of sustained firing
  (pipeline-level) or ~18 h (RMP self-adapt).

## Output

`Pipeline.ingest(event)` returns zero or more `Alert` objects. Each
chain carries:

```python
Alert(
  sensor_id, capability, timestamp,
  detector,         # "+"-joined union of detectors fused into the chain
  score, threshold,
  anomaly_type,     # post-classify canonical label
  window_start, window_end,
  first_fire_ts,    # earliest component fire tick (latency reference)
  fire_ticks,       # all component fire ticks (per-fire grading)
  context,          # detector evidence dicts
)
```

Deployment consumer:

```python
bundle = explain(alert, events_df)
prompt = build_prompt(bundle)   # → LLM input
```

## What's NOT in deployment

- **CSV replay path** (`python -m anomaly run / eval / explain`) —
  research/offline only. Reads `events.csv` upfront, replays through
  `Pipeline.ingest`, writes detections at end. Not a streaming pattern.
- **Bundle JSONL writer** (`csv.explain_detections_csv`) — research
  only; production calls `bundle.explain()` per alert directly.
- **Research harness** (`research/`, `scripts/run_all_scenarios.py`,
  `scripts/latency_report.py`) — dev-only. Headline metrics, latency
  reports, baselines, iteration logs.
- **Cross-sensor correlation** ("kettle + TV co-fire → guests") —
  not implemented; each sensor is analyzed independently.
- **CUSUM, PCA, MatrixProfile, BOCPD, TemporalProfile, …** — pruned.
  The five-detector set above is the entire deployment surface.
