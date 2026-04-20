# Research loop — Karpathy-style auto-research

This directory holds the tooling for an autonomous research session aimed at
improving anomaly detection on the **60-day** and **120-day** scenario suites.

The loop is: pick one hypothesis → implement the minimum change → run the full
eval → inspect the plots → ACCEPT or REJECT against hard metric floors → append
to the iteration log. `ultrathink` every step.

## Files

| File               | Purpose                                                                                |
|--------------------|----------------------------------------------------------------------------------------|
| `START_RESEARCH.md`| The prompt that bootstraps a session. Hit this (send its contents to a fresh session). |
| `HYPOTHESES.md`    | Ranked backlog of candidate hypotheses. Draw one per iteration.                        |
| `ITERATIONS.md`    | Append-only log of everything tried, with exact metric deltas and verdicts.            |
| `BASELINE.md`      | Human-facing notes on what the frozen baseline means and how to refresh it.            |
| `BASELINE.json`    | Machine-readable baseline — the bar every candidate run is diffed against.             |
| `run_research_eval.py` | Runner: executes the pipeline on all scenarios, writes JSON, does baseline diffs.  |
| `runs/`            | One `<timestamp>.json` per run; `latest.json` points at the most recent.               |

## Suites

### 60d (5 scenarios — pre-existing)

- `outlet_60d`, `outlet_tv_60d`, `outlet_kettle_60d`, `waterleak_60d`, `outlet_short_60d`
- Drawn from `../synthetic-generator/out/{outlet,outlet_tv,outlet_kettle,leak,outlet_short}/`.

### 120d (2 scenarios — new)

- `outlet_120d`, `waterleak_120d`
- Scenario specs: `../synthetic-generator/scenarios/outlet_120d.yaml`,
  `../synthetic-generator/scenarios/waterleak_120d.yaml`
- Generate: `sensorgen run scenarios/outlet_120d.yaml --out out/outlet_120d`
  (and same for waterleak_120d) from the `synthetic-generator/` directory.

## Common commands

```bash
# From anomaly-detection/

# Measure only (no baseline comparison)
python research/run_research_eval.py --suite all

# Measure + diff against BASELINE.json (exit 1 on any floor breach)
python research/run_research_eval.py --suite all --diff-baseline

# Freeze current run as the new baseline (only after an ACCEPT you want to ratchet)
python research/run_research_eval.py --suite all --save-baseline

# Visualize a scenario post-run
python -m anomaly viz --events ../synthetic-generator/out/outlet_120d/events.csv \
                      --labels ../synthetic-generator/out/outlet_120d/labels.csv \
                      --detections out/outlet_120d_detections.csv \
                      --out out/outlet_120d_viz.pdf --window 1d

python -m anomaly viz-long --events ../synthetic-generator/out/outlet_120d/events.csv \
                           --labels ../synthetic-generator/out/outlet_120d/labels.csv \
                           --detections out/outlet_120d_detections.csv \
                           --out out/outlet_120d_viz_long.pdf --min-hours 24
```

## Start a session

Copy the contents of `START_RESEARCH.md` into a fresh Claude session.
That file is self-contained — it instructs the agent to ground on the baseline,
pick a hypothesis, run the loop, and log results.
