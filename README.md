# Smart Home Sensor Anomaly Detection

Compact Python pipeline for detecting anomalies in smart-home sensor streams (power, voltage, temperature, water leak, battery, switch state, etc.). Filter-and-escalate architecture — a sensor-aware adapter layer plus six sensor-agnostic detectors. Full design spec in `pipeline.md`.

## Quickstart (with the companion synthetic generator)

End-to-end on the canonical `household_60d` scenario (60-day smart-home
timeline, 19 labeled anomalies). PowerShell shown below; bash/zsh users
replace the trailing `` ` `` (PowerShell line-continuation) with `\`
and `\` path separators with `/`.

```powershell
# 1. Generate a labeled scenario (companion project)
cd ..\synthetic-generator
sensorgen run scenarios\household_60d.yaml --out out\household_60d
#   writes out\household_60d\events.csv and out\household_60d\labels.csv

# 2. Detection pipeline
cd ..\anomaly-detection
python -m anomaly run `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --config configs\household.yaml `
  --out out\household_60d_detections.csv `
  --bootstrap-days 14
#   writes out\household_60d_detections.csv (with first_fire_ts column)

# 3. Research eval — the full metrics suite the tuning loop uses
python research\run_research_eval.py --suite 60d
#   prints BEHAVIOR + FAULT blocks per scenario plus an onset-timing
#   audit; also writes a JSON snapshot under research\runs\

# 4a. Viz — per-day tiled PDF (best for short/mixed anomalies)
python -m anomaly viz `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --labels ..\synthetic-generator\out\household_60d\labels.csv `
  --detections out\household_60d_detections.csv `
  --out out\household_60d_viz.pdf `
  --window 1d

# 4b. Viz — one detail page per long (>=24h) label
python -m anomaly viz-long `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --labels ..\synthetic-generator\out\household_60d\labels.csv `
  --detections out\household_60d_detections.csv `
  --out out\household_60d_viz_long.pdf `
  --min-hours 24

# 5. Explain — one LLM-ready bundle per detection
python -m anomaly explain `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --detections out\household_60d_detections.csv `
  --out out\household_60d_bundles.jsonl
```

Run the full 3-scenario suite (`household_60d` + `household_120d` +
`leak_30d`) through the research scorer:
```powershell
python research\run_research_eval.py --suite all
python research\run_research_eval.py --suite all --diff-baseline   # regression check
python research\run_research_eval.py --suite all --save-baseline   # freeze BASELINE.json
```

The scorer expects `synthetic-generator\` as a sibling of this project;
override with the `SENSORGEN_OUT` env var.

Session-by-session tuning log lives in `CHANGES.md`; the frozen baseline
narrative + ratchet history is in `research\BASELINE.md`.

## Install

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1         # macOS/Linux: source .venv/bin/activate
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

Each sensor declares its archetype (`continuous` / `bursty` / `binary`) plus physical bounds. Bundled configs:

- `configs/household.yaml` — fridge + kettle + tv (bursty power) · mains_voltage (continuous) · basement_leak + bedroom_motion (binary). Used by the `household_60d` and `household_120d` scenarios.
- `configs/leak_30d.yaml` — basement_leak (binary water) · basement_temp (continuous) · utility_motion (binary).

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
```powershell
python -m anomaly run `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --config configs\household.yaml `
  --out out\household_60d_detections.csv `
  --bootstrap-days 14
```

Writes `detections.csv` with columns `sensor_id, capability, start, end, first_fire_ts, anomaly_type, detector, score`.

- `start` / `end` — the analysis-window extent of the fused chain (used by coverage metrics).
- `first_fire_ts` — the earliest component tick in the chain (used by latency / onset metrics). Added 2026-04-24; see `research\BASELINE.md`.
- `--bootstrap-days` — how long the pipeline learns the sensor's baseline before statistical detectors activate. Use 7 days for `leak_30d`, 14 days for household scenarios. Bootstrap data should be representative normal behavior; anomalies falling inside the bootstrap window silently train the models against themselves and are unlikely to be detected.

### Evaluate against ground truth

**Headline eval (built-in)** — prints the BEHAVIOR + sensor_fault block for one scenario. Runs from a fresh clone (no `research/` needed). Pass `--config` to mirror the pipeline's sensor filter (drops GT for sensors not in scope) and `--events` so the user-visible FP rate normalizes to the actual events span.

```powershell
python -m anomaly eval `
  --detections out\household_60d_detections.csv `
  --labels ..\synthetic-generator\out\household_60d\labels.csv `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --config configs\household.yaml

# === Headline (timeline 60.0d) ===
# block          n_labels  time_F1   incR  evt_F1  uvfp/d   latP95s
#   behavior           12    0.372  0.917   0.753    0.48     71190
#   sensor_fault        2    0.030  0.500   0.500   28.67       -
```

The headline block is the user-facing optimization target; the `sensor_fault` row is reported for visibility, not optimized against.

**Research suite (multi-scenario sweep)** — the scorer the tuning loop uses. Runs the pipeline across all 7 scenarios, writes a JSON snapshot, supports `--diff-baseline` regression checks. The `research/` directory is gitignored, so this path is local-only after clone.

```powershell
python research\run_research_eval.py --suite all           # household_60d + household_120d + leak_30d
python research\run_research_eval.py --suite 60d           # just household_60d
python research\run_research_eval.py --suite all --diff-baseline    # regression check vs BASELINE.json
python research\run_research_eval.py --suite all --save-baseline    # freeze current as BASELINE.json
```

Per-scenario metrics tracked in research (BEHAVIOR block — the user-facing optimization target):

| Metric                        | Role         | Semantics                                                                                           |
|-------------------------------|:------------:|-----------------------------------------------------------------------------------------------------|
| `time_f1`                     | **headline** | Duration-weighted F1 over label-seconds vs detection-seconds. Penalises over-claim AND missed coverage. |
| `incident_recall`             | **floor**    | Fraction of labels covered by any detection. The tuning loop never allows this to drop.             |
| `fp_h_per_day`                | secondary    | FP detection-hours per calendar day. Direct over-claim proxy.                                       |
| `nondqg_latency_p95_s`        | secondary    | 95th-%ile delay from label start to first chain fire. Reads the `first_fire_ts` column.             |
| `evt_f1`                      | visibility   | Event-level F1 with a 1h merge-gap. Reported but **not** a regression criterion (merge-gap artifact). |
| `onset_early_labels` / `_late_labels` | diagnostic | How many labels had the first chain fire before / after label start.                          |
| `onset_early_lead_p95_s` / `onset_late_start_p95_s` | diagnostic | Distribution of those leads / delays.                                              |

Regression floors (`--diff-baseline` defaults): `incident_recall` drop >0.005, `time_f1` drop >0.02, `fp_h_per_day` rise >10% relative, `nondqg_latency_p95_s` rise >600s. Any scenario tripping any floor → REJECT.

The `sensor_fault` block is reported for visibility only — infrastructure anomalies are not user-facing and we do not optimise for them. `label_class` slicing lives in `synthetic-generator/src/sensorgen/labels.py`.

All F1 flavors live in `anomaly.metrics`:
- `compute_metrics_time` — **primary**. TP/FP/FN in seconds via per-sensor interval sweep.
- `compute_metrics_event` — event-level F1 (1h merge-gap); what `evt_f1` reports.
- `compute_metrics_pointwise` — any-overlap set semantics; recall = `incident_recall`.
- `compute_metrics` — legacy 1:1 greedy matching; printed by `python -m anomaly eval`.
- `compute_metrics_latency` / `compute_metrics_onset_timing` — read `first_fire_ts` when present, fall back to `start` on legacy CSVs.

### Visualize
```powershell
python -m anomaly viz `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --labels ..\synthetic-generator\out\household_60d\labels.csv `
  --detections out\household_60d_detections.csv `
  --out out\household_60d_viz.pdf `
  --window 1d
```

Produces a multi-page PDF (one page per time window). Each sensor has three lanes per page:
1. Clean signal (no shading)
2. **truth** timeline — one row per anomaly type (red)
3. **detected** timeline — one row per detector (blue)

Vertical alignment between a red row and a blue row = caught. Unmatched red = missed. Unmatched blue = false alarm.

`--window` accepts any pandas Timedelta string: `1h`, `6h`, `12h`, `1d`, `2d`, etc.

### Long-anomaly viz (`viz-long`)

For scenarios with day- or week-scale anomalies, strip markers across 30+ days don't communicate much. `viz-long` produces a per-label interpretive PDF:

```powershell
python -m anomaly viz-long `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --labels ..\synthetic-generator\out\household_60d\labels.csv `
  --detections out\household_60d_detections.csv `
  --out out\household_60d_viz_long.pdf `
  --min-hours 24
```

Page 1 is a summary table of every label with duration, TP/FN, and detector mix. Each following page is one GT label whose duration >= `--min-hours`, showing the full scenario signal with the label region highlighted, a zoomed signal with padded context (`max(1d, duration/3)`, capped at 14d), and aligned truth/detection strips. Short (<24h) labels are listed on the summary page but don't get a detail page — use the per-day `viz` above for those.

## Explain (`anomaly.explain`)

The pipeline emits `Alert` objects (see `core.Alert`). For LLM
summarisation you can convert each alert into a structured bundle +
markdown prompt. Available as a **CLI subcommand** for batch use, or
as a **library** for in-process streaming.

### CLI: events CSV + detections CSV → bundles JSONL

After running `python -m anomaly run ...` to produce
`out\household_60d_detections.csv`, generate one bundle per detected alert:

```powershell
python -m anomaly explain `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --detections out\household_60d_detections.csv `
  --out out\household_60d_bundles.jsonl
# -> wrote N bundles to out\household_60d_bundles.jsonl
```

Equivalent from Python (useful if you want the return value or are
driving this from another process):

```python
from anomaly.explain import explain_detections_csv
n = explain_detections_csv(
    events_csv     = '../synthetic-generator/out/household_60d/events.csv',
    detections_csv = 'out/household_60d_detections.csv',
    out_jsonl      = 'out/household_60d_bundles.jsonl',
)
```

`out\household_60d_bundles.jsonl` is one JSON bundle per line:

```json
{
  "alert_id": "outlet_fridge_power|power|2026-02-09T11:00:00+00:00",
  "sensor": "outlet_fridge_power", "capability": "power",
  "window": {"start": "...", "end": "...", "duration_sec": 60.0},
  "inferred_type": "out_of_range",
  "magnitude": {"baseline": 1.5, "baseline_source": "prewindow_2h",
                "peak": 9999.0, "delta": 9997.5, "delta_pct": 666500.0},
  "temporal": {"weekday": "Monday", "hour": 11, "is_weekend": false,
               "same_hour_weekday_z": 3.2, "same_hour_weekday_n": 8, ...},
  "detectors": ["data_quality_gate"],
  "detector_context": [{"detector": "data_quality_gate",
                        "anomaly_type": "out_of_range",
                        "value": 9999.0, "score": 9999.0}],
  "score": 9999.0, "threshold": 0.0
}
```

### Analyze: render one bundle as markdown

```powershell
python -c "import json; from anomaly.explain import build_prompt; print(build_prompt(json.loads(open('out/household_60d_bundles.jsonl').readline())))"
```

Produces an LLM-ready markdown block:

```
# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 09 2026 11:00 UTC -> Mon Feb 09 2026 11:01 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 9999,
               delta +9998 (+666500.00%).

**Calendar context:** Monday, hour 11 (morning), weekday, February.
**Same-hour-of-weekday baseline:** peak is +3.20σ vs. the median of
  8 prior Monday 11:00 samples (peer median 1.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=9999, score=9999

**Detectors fired:** data_quality_gate.
**Score:** 1e+04 (threshold 0).
```

### Per-alert (live pipeline path)

If you're driving the pipeline directly in Python (`Pipeline.ingest`
returns `Alert` objects), skip the CSV round-trip:

```python
from anomaly.explain import explain, build_prompt

for alert in alerts:                         # Alert stream from the pipeline
    bundle = explain(alert, events_df)       # events_df: pandas DataFrame
    print(build_prompt(bundle))
```

The live path carries detector-native context on `alert.context`; the
CSV batch path reconstructs it from the events frame
(`_synth_detector_context`). Either way the bundle schema is the same.

### What the bundle carries

- **`window`** — start / end / duration_sec (from the alert's firing
  window).
- **`magnitude`** — baseline / peak / delta / delta_pct, with
  `baseline_source` labeling the tier: `cusum_mu` (detector-native) >
  `prewindow_2h` > `prewindow_24h` > `prewindow_7d` > `prewindow_unavailable`.
- **`temporal`** — weekday, hour, is_weekend, month, time-of-day
  bucket, plus same-hour-of-weekday z-score when ≥4 peer samples exist.
- **`detectors`** — sorted list of firing detector names.
- **`detector_context`** — per-detector diagnostic dict (`cusum`:
  mu/sigma/direction, `sub_pca`/`multivariate_pca`: approx_residual_z,
  `data_quality_gate`: anomaly_type + value, `temporal_profile`:
  hour_of_day + approx_hour_z, `state_transition`: anomaly_type).
- **`score`** / **`threshold`** — raw detector output.

`build_prompt` deliberately **omits** the classifier's
`inferred_type` — the LLM is expected to reason from the rendered
evidence. See `CHANGES.md` for the evidence extensions and their
rationale.

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
configs/                          sample sensor configurations (household / leak_30d)
research/run_research_eval.py     canonical scorer — behavior-stratified metrics, JSON snapshots, BASELINE.json diff
research/BASELINE.md              frozen baseline narrative + ratchet history
scripts/run_all_scenarios.py      legacy sweep over old scenarios (outlet / tv / kettle / waterleak)
tests/                            unit + integration tests
pipeline.md                       full design spec (algorithms, suppression matrix, bootstrap phases)
CHANGES.md                        tuning-session log (detector / fusion / metric evolution)
```

## Tests

```powershell
pytest -v
```

All pure unit/integration tests using in-memory fixtures. No external data required.

Some optional integration tests look for generated synthetic scenarios under the companion `synthetic-generator/` project's `out/` directory. They auto-skip if the data isn't present, so the core suite runs everywhere.

## Adding a new sensor archetype

1. Add a subclass to `src/anomaly/adapter.py` (see `ContinuousAdapter` for template).
2. Register it in `ADAPTER_REGISTRY`.
3. Enable relevant detectors in `DETECTOR_ENABLED` in `src/anomaly/pipeline.py`.

Downstream code is archetype-agnostic — detectors consume the uniform feature dict produced by the adapter.
