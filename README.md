# Smart Home Sensor Anomaly Detection

Compact Python pipeline for detecting anomalies in smart-home sensor streams (power, voltage, temperature, water leak, battery, switch state, etc.). Filter-and-escalate architecture — a sensor-aware adapter layer plus six sensor-agnostic detectors. Full design spec in `pipeline.md`.

## Quickstart (with the companion synthetic generator)

```bash
# 1. Generate a labeled scenario
cd synthetic-generator
sensorgen run scenarios/outlet_demo.yaml --out out/outlet

# 2. Run the pipeline
cd ../anomaly-detection
python -m anomaly run \
  --events ../synthetic-generator/out/outlet/events.csv \
  --config configs/outlet.yaml \
  --out out/outlet_detections.csv \
  --bootstrap-days 14

# 3. Score against ground truth
python -m anomaly eval \
  --detections out/outlet_detections.csv \
  --labels ../synthetic-generator/out/outlet/labels.csv
```

To sweep all 4 bundled scenarios (outlet / outlet-tv / outlet-kettle / waterleak) and compare both metrics:
```bash
python scripts/run_all_scenarios.py
```

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

Prints `{tp, fp, fn, precision, recall, f1}` using **1:1** interval-overlap matching (each label can match at most one detection, greedy by label order). A pointwise variant — where any detection overlapping any label counts as TP — is available via `compute_metrics_pointwise` in `anomaly.metrics`. For long-duration anomalies (day/week-scale drifts, month shifts), pointwise is the more faithful picture of detector quality; 1:1 over-counts as FP the redundant chunks that sit on a single long label.

To run on multiple scenarios and compare both metrics side-by-side, see `scripts/run_all_scenarios.py`.

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

## Project structure

```
src/anomaly/
  core.py        Event, Alert, Archetype, SensorConfig
  adapter.py     per-archetype resampling + state modeling
  features.py    calendar + rolling + first-diff enrichment
  detectors.py   DQG + CUSUM + SubPCA + MultivariatePCA + TemporalProfile
  batch.py       MatrixProfile (offline)
  pipeline.py    orchestrator, fusion, staggered bootstrap, CLI
  metrics.py     interval-overlap + pointwise matching
  viz.py         PDF visualization
configs/                     sample sensor configurations (outlet / tv / kettle / waterleak)
scripts/run_all_scenarios.py runs the pipeline on all bundled scenarios, reports 1:1 + pointwise metrics
tests/                       41 unit + integration tests
pipeline.md                  full design spec (algorithms, suppression matrix, bootstrap phases)
```

## Tests

```bash
pytest -v
```

41 tests — all pure unit/integration tests using in-memory fixtures. No external data required.

Some optional integration tests (if present) look for generated synthetic scenarios under the companion `synthetic-generator/` project's `out/` directory (e.g. `outlet7`, `leak7`). They auto-skip if the data isn't present, so the core suite runs everywhere.

## Adding a new sensor archetype

1. Add a subclass to `src/anomaly/adapter.py` (see `ContinuousAdapter` for template).
2. Register it in `ADAPTER_REGISTRY`.
3. Enable relevant detectors in `DETECTOR_ENABLED` in `src/anomaly/pipeline.py`.

Downstream code is archetype-agnostic — detectors consume the uniform feature dict produced by the adapter.
