# Research loop — karpathy-style auto-research

This directory holds the tooling for an autonomous research session
aimed at improving anomaly detection on the behavior-stratified eval
suite.

**Current branch approach:** bottom-up precision-first redesign. See
`PIPELINE_REDESIGN.md`.

## Files (read order)

| File                 | Purpose                                                   |
|----------------------|-----------------------------------------------------------|
| `START_RESEARCH.md`  | Session prompt — paste into a fresh Claude session.       |
| `PIPELINE_REDESIGN.md` | Current approach + the ladder stages.                   |
| `LEARNINGS.md`       | Mechanisms that generalize + landmines + binding rules.   |
| `BASELINE.md`        | Baseline narrative + floors. Machine copy: `BASELINE.json`. |
| `HYPOTHESES.md`      | Forward-looking candidate ideas not yet on the ladder.    |
| `ITERATIONS.md`      | Append-only per-iter log. **Not loaded at session start.** |
| `run_research_eval.py` | Runner — executes pipeline on all scenarios, diffs.     |
| `runs/`              | One `<timestamp>.json` per run; `latest.json` points at the most recent. |
| `DETECTOR_RESEARCH_PLAN.md` | SUPERSEDED — archived reference only.              |

## Common commands

```bash
# From anomaly-detection/

# Iter gate — 3 production + 2 random holdout
python research/run_research_eval.py --suite iter --random-sample 2

# Full all-scenario audit (stage boundaries, pre-merge)
python research/run_research_eval.py --suite all

# Diff current run vs BASELINE.json (exit 1 on any floor breach)
python research/run_research_eval.py --suite all --diff-baseline

# Freeze the current run as the new baseline (only on clean stage completion)
python research/run_research_eval.py --suite all --save-baseline
```

## Visualization

```bash
python -m anomaly viz --events ../synthetic-generator/out/<scen>/events.csv \
                      --labels ../synthetic-generator/out/<scen>/labels.csv \
                      --detections out/<scen>_detections.csv \
                      --out out/<scen>_viz.pdf --window 1d

python -m anomaly viz-long --events ../synthetic-generator/out/<scen>/events.csv \
                           --labels ../synthetic-generator/out/<scen>/labels.csv \
                           --detections out/<scen>_detections.csv \
                           --out out/<scen>_viz_long.pdf --min-hours 24
```

## Starting a session

Paste the contents of `START_RESEARCH.md` into a fresh session. That
file is self-contained and points to `PIPELINE_REDESIGN.md` for the
current ladder stage.
