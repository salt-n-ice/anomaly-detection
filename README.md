# Smart Home Sensor Anomaly Detection

Compact Python pipeline for detecting anomalies in smart-home sensor streams (power, voltage, temperature, water leak, battery, switch state, etc.). Filter-and-escalate architecture — a sensor-aware adapter layer plus six sensor-agnostic detectors. Full design spec in `pipeline.md`.

## Quickstart (with the companion synthetic generator)

End-to-end: YAML scenario → events CSV → detections CSV → metrics + PDFs.

```bash
# 1. Generate a labeled scenario from a YAML spec
cd synthetic-generator
sensorgen run scenarios/outlet_demo.yaml --out out/outlet
#   writes out/outlet/events.csv  and  out/outlet/labels.csv

# 2. Run the detection pipeline
cd ../anomaly-detection
python -m anomaly run \
  --events ../synthetic-generator/out/outlet/events.csv \
  --config configs/outlet.yaml \
  --out out/outlet_detections.csv \
  --bootstrap-days 14
#   writes out/outlet_detections.csv

# 3. Score against ground truth
python -m anomaly eval \
  --detections out/outlet_detections.csv \
  --labels ../synthetic-generator/out/outlet/labels.csv

# 4a. Visualize (multi-page, 1-day windows — best for short/mixed anomalies)
python -m anomaly viz \
  --events ../synthetic-generator/out/outlet/events.csv \
  --labels ../synthetic-generator/out/outlet/labels.csv \
  --detections out/outlet_detections.csv \
  --out out/outlet_viz.pdf \
  --window 1d

# 4b. Visualize long-duration anomalies (one page per label ≥ 24h, with signal curves)
python -m anomaly viz-long \
  --events ../synthetic-generator/out/outlet/events.csv \
  --labels ../synthetic-generator/out/outlet/labels.csv \
  --detections out/outlet_detections.csv \
  --out out/outlet_viz_long.pdf \
  --min-hours 24
```

To sweep all 5 bundled scenarios (outlet / outlet-tv / outlet-kettle / waterleak / outlet_short) and compare all metrics side-by-side:
```bash
python scripts/run_all_scenarios.py
```
(expects the generator's `out/` directory to be a sibling of this project — set `SENSORGEN_OUT` to override)

A session-by-session tuning log lives in `CHANGES.md`.

## Install

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -e .[dev]
```

Requires Python 3.11+. Dependencies: numpy, pandas, pyyaml, matplotlib.

## Data format

Input is two CSVs. `events.csv` is required; `labels.csv` is optional (needed only for evaluation / viz).

**events.csv**
```
timestamp,sensor_id,capability,value,unit
2026-02-01T00:00:00+00:00,outlet_fridge_power,power,41.5,W
2026-02-01T00:00:00+00:00,outlet_voltage,voltage,122.47,V
```

**labels.csv** (ground-truth intervals)
```
sensor_id,capability,start,end,anomaly_type,detector_hint,params_json
outlet_fridge_power,power,2026-02-05T14:00:00Z,2026-02-05T14:02:00Z,spike,pca,"{""magnitude"": 600}"
```

## Sensor config

Each sensor declares its archetype (`continuous` / `bursty` / `binary`) plus physical bounds. Sample configs:

- `configs/outlet.yaml` — fridge (bursty) + voltage (continuous)
- `configs/outlet_tv.yaml` — TV (bursty) + voltage
- `configs/outlet_kettle.yaml` — kettle (bursty, high-wattage) + voltage
- `configs/waterleak.yaml` — water leak (binary) + temperature + battery

```yaml
sensors:
  - id: outlet_fridge_power
    capability: power
    archetype: bursty
    expected_interval_sec: 300
    min_value: 0
    max_value: 3000
  - id: outlet_voltage
    capability: voltage
    archetype: continuous
    expected_interval_sec: 600
    min_value: 80
    max_value: 140
```

## CLI

### Run the pipeline
```bash
python -m anomaly run \
  --events events.csv \
  --config configs/outlet.yaml \
  --out detections.csv \
  --bootstrap-days 14
```

Writes `detections.csv` with columns `sensor_id, capability, start, end, anomaly_type, detector, score`.

`--bootstrap-days` is how long the pipeline learns the sensor's baseline before statistical detectors activate. Use ~2 days for a 7-day scenario, ~14 days for 60-day evaluations. Bootstrap data should be representative normal behavior — anomalies falling inside the bootstrap window will silently train the models against themselves and are unlikely to be detected.

### Evaluate against ground truth
```bash
python -m anomaly eval \
  --detections detections.csv \
  --labels labels.csv
```

Prints `{tp, fp, fn, precision, recall, f1}` using **1:1** interval-overlap matching. Four F1 flavors are implemented in `anomaly.metrics`:

- `compute_metrics` — **1:1** greedy matching (legacy). Penalizes multi-chunk detection of long labels.
- `compute_metrics_pointwise` — any-overlap set semantics. Recall equals `incident_recall`.
- `compute_metrics_event` — **event-level F1** (primary target). Detections within a 1h gap are merged into "events" before matching; one sustained alert is one event regardless of internal chunking.
- `compute_metrics_time` — **duration-weighted**. TP/FP/FN in seconds via per-sensor interval sweep. Surfaces multi-day FP strips that event F1 collapses into a single event.

To run on multiple scenarios and compare all metrics side-by-side, see `scripts/run_all_scenarios.py`. It also reports `incident_recall`, `fp_h_per_day`, and `events_per_incident` (alert burden).

### Visualize
```bash
python -m anomaly viz \
  --events events.csv \
  --labels labels.csv \
  --detections detections.csv \
  --out viz.pdf \
  --window 1d
```

Produces a multi-page PDF (one page per time window). Each sensor has three lanes per page:
1. Clean signal (no shading)
2. **truth** timeline — one row per anomaly type (red)
3. **detected** timeline — one row per detector (blue)

Vertical alignment between a red row and a blue row = caught. Unmatched red = missed. Unmatched blue = false alarm.

`--window` accepts any pandas Timedelta string: `1h`, `6h`, `12h`, `1d`, `2d`, etc.

### Long-anomaly viz (`viz-long`)

For scenarios with day- or week-scale anomalies, strip markers across 30 days don't communicate much. `viz-long` produces a per-label interpretive PDF:

```bash
python -m anomaly viz-long \
  --events events.csv \
  --labels labels.csv \
  --detections detections.csv \
  --out viz_long.pdf \
  --min-hours 24
```

Page 1 is a summary table of every label with duration, TP/FN, and detector mix. Each following page is one GT label whose duration ≥ `--min-hours`, showing the full 60-day signal with the label region highlighted, a zoomed signal with padded context (`max(1d, duration/3)`, capped at 14d), and aligned truth/detection strips.

## Programmatic explainer (`anomaly.explain`)

The pipeline emits `Alert` objects (see `core.Alert`). For LLM
summarisation you can convert each alert into a structured bundle +
markdown prompt:

```python
from anomaly.explain import explain, build_prompt, explain_detections_csv

# Per-alert (live pipeline path — alert.context carries detector-native dicts)
bundle = explain(alert, events_df)          # dict: window / magnitude / temporal / detectors / detector_context / ...
prompt = build_prompt(bundle)               # markdown string the LLM reads

# Batch (post-hoc from a detections CSV)
explain_detections_csv(events_csv, detections_csv, out_jsonl)
```

The bundle carries derivable per-detector context (cusum
mu/sigma/direction, PCA residual z, DQG anomaly_type + value,
temporal-profile same-hour z), a tiered baseline (`prewindow_2h` /
`prewindow_24h` / `prewindow_7d`), and same-hour-of-weekday peer
statistics. `build_prompt` renders a human- and LLM-readable markdown
block and deliberately omits the classifier's inferred type so the
reader reasons from the evidence. See `CHANGES.md` for the evidence
extensions and their rationale.

## Project structure

```
src/anomaly/
  core.py        Event, Alert, Archetype, SensorConfig
  adapter.py     per-archetype resampling + state modeling
  features.py    calendar + rolling + first-diff enrichment
  detectors.py   DQG + CUSUM + SubPCA + MultivariatePCA + TemporalProfile
  batch.py       MatrixProfile (offline)
  fusion.py      per-sensor alert fuser (chain + corroboration rules)
  profiles.py    per-archetype detector/fuser factory registry
  pipeline.py    orchestrator, fusion, staggered bootstrap, CLI
  metrics.py     interval-overlap + pointwise + event + time-weighted
  explain.py     structured bundle + LLM-ready markdown prompt per alert
  viz.py         PDF visualization
configs/                     sample sensor configurations (outlet / tv / kettle / waterleak)
scripts/run_all_scenarios.py runs the pipeline on all 5 bundled scenarios, reports 1:1 / event / pointwise / time-weighted metrics
tests/                       unit + integration tests
pipeline.md                  full design spec (algorithms, suppression matrix, bootstrap phases)
CHANGES.md                   tuning-session log (detector / fusion / metric evolution)
```

## Tests

```bash
pytest -v
```

All pure unit/integration tests using in-memory fixtures. No external data required.

Some optional integration tests (if present) look for generated synthetic scenarios under the companion `synthetic-generator/` project's `out/` directory (e.g. `outlet7`, `leak7`). They auto-skip if the data isn't present, so the core suite runs everywhere.

## Adding a new sensor archetype

1. Add a subclass to `src/anomaly/adapter.py` (see `ContinuousAdapter` for template).
2. Register it in `ADAPTER_REGISTRY`.
3. Enable relevant detectors in `DETECTOR_ENABLED` in `src/anomaly/pipeline.py`.

Downstream code is archetype-agnostic — detectors consume the uniform feature dict produced by the adapter.
