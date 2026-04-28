# Smart Home Sensor Anomaly Detection

## Install

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .[dev]
```

Requires Python 3.11+. Expects the companion `synthetic-generator\` as a sibling directory; override with `$env:SENSORGEN_OUT = "..."`.

## Generate a scenario

```powershell
cd ..\synthetic-generator
sensorgen run scenarios\household_60d.yaml --out out\household_60d
cd ..\anomaly-detection
```

Available scenarios: `household_60d`, `household_120d`, `household_dense_90d`, `household_sparse_60d`, `leak_30d`, `holdout_household_45d`.

## Run the pipeline

```powershell
python -m anomaly run `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --config configs\household.yaml `
  --out out\household_60d_detections.csv `
  --bootstrap-days 14
```

Use `--bootstrap-days 7` for `leak_30d`.

## Evaluate

```powershell
python -m anomaly eval `
  --detections out\household_60d_detections.csv `
  --labels ..\synthetic-generator\out\household_60d\labels.csv `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --config configs\household.yaml
```

## Run the full suite

```powershell
python scripts\run_all_scenarios.py
```

Runs the pipeline + headline eval across all six scenarios.

## Latency report (demo metric)

```powershell
python scripts\latency_report.py
```

Reports on-time rate + median absolute latency per type. Reads `out\<scenario>_detections.csv` from the suite run above.

## Visualize

```powershell
python -m anomaly viz `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --labels ..\synthetic-generator\out\household_60d\labels.csv `
  --detections out\household_60d_detections.csv `
  --out out\household_60d_viz.pdf

python -m anomaly viz-long `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --labels ..\synthetic-generator\out\household_60d\labels.csv `
  --detections out\household_60d_detections.csv `
  --out out\household_60d_viz_long.pdf `
  --min-hours 24
```

## Explain (LLM-ready bundles)

```powershell
python -m anomaly explain `
  --events ..\synthetic-generator\out\household_60d\events.csv `
  --detections out\household_60d_detections.csv `
  --out out\household_60d_bundles.jsonl
```

## Replay (HTML animation)

```powershell
python scripts\replay_demo.py --scenario household_120d
```

Writes `out\replay_household_120d.html`. Pass `--duration-sec 90` to slow down playback.

## Tests

```powershell
pytest -v
```

## Reference

- `pipeline.md` — full design spec
- `docs\METRICS.md` — eval metric reading guide
- `CHANGES.md` — tuning-session log
- `configs\` — sensor configurations (`household.yaml`, `leak_30d.yaml`)
