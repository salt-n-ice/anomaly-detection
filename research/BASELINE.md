# Baseline

This file documents the frozen baseline — the metrics the research loop must
not silently regress. The machine-readable snapshot is `BASELINE.json`; this
file is the human-facing narrative (how it was taken and what it means).

The research loop compares every new run to `BASELINE.json` via
`research/run_research_eval.py --diff-baseline`. To move the baseline, use
`--save-baseline` **only** after an iteration ACCEPTs and you're ready to ratchet.

## How to take / refresh the baseline

```bash
# 1. Generate 120-day scenarios if you haven't yet (one-off).
cd ../synthetic-generator
sensorgen run scenarios/outlet_120d.yaml    --out out/outlet_120d
sensorgen run scenarios/waterleak_120d.yaml --out out/waterleak_120d

# 2. Run the full evaluation and freeze the result as the baseline.
cd ../anomaly-detection
python research/run_research_eval.py --suite all --save-baseline
```

That writes `research/BASELINE.json` and `research/runs/<timestamp>.json`. The
`BASELINE.json` never changes automatically — it's only overwritten by an
explicit `--save-baseline` invocation.

## How to check a candidate against the baseline

```bash
python research/run_research_eval.py --suite all --diff-baseline
# exit code 0 = no regression; 1 = at least one scenario regressed
```

The diff applies two floors per scenario:
- **evt F1:** drop > 0.02 is a regression.
- **incident_recall:** drop > 0.005 is a regression.

These floors are intentionally tighter than the aggregate "mean improvement"
target — they catch regressions that the aggregate average would hide.

## Scenarios included

| Suite | Scenario         | Source                                      | Timeline |
|:-----:|------------------|---------------------------------------------|---------:|
| 60d   | outlet_60d       | synthetic-generator/out/outlet               |     60d |
| 60d   | outlet_tv_60d    | synthetic-generator/out/outlet_tv            |     60d |
| 60d   | outlet_kettle_60d| synthetic-generator/out/outlet_kettle        |     60d |
| 60d   | waterleak_60d    | synthetic-generator/out/leak                 |     60d |
| 60d   | outlet_short_60d | synthetic-generator/out/outlet_short         |     60d |
| 120d  | outlet_120d      | synthetic-generator/out/outlet_120d          |    120d |
| 120d  | waterleak_120d   | synthetic-generator/out/waterleak_120d       |    120d |

## Baseline values (as of 2026-04-20, both suites)

| Scenario         | evt F1 | time F1 | incR  | fp_h/d | ev/inc |
|------------------|:------:|:-------:|:-----:|:------:|:------:|
| **60d suite**    |        |         |       |        |        |
| outlet_60d       | 0.927  | 0.758   | 0.864 | 12.73  | 0.77   |
| outlet_tv_60d    | 0.753  | 0.769   | 0.909 | 12.40  | 0.64   |
| outlet_kettle_60d| 0.952  | 0.767   | 0.909 | 12.73  | 0.27   |
| waterleak_60d    | 0.824  | 0.324   | 0.700 | 26.73  | 0.70   |
| outlet_short_60d | 0.763  | 0.622   | 0.850 |  0.66  | 1.30   |
| **60d mean**     | 0.844  | 0.648   | 0.846 | 13.05  | —      |
| **120d suite**   |        |         |       |        |        |
| outlet_120d      | 0.960  | 0.559   | 0.923 | 24.61  | 0.49   |
| waterleak_120d   | 0.838  | 0.225   | 0.842 | 22.50  | 4.74   |
| **120d mean**    | 0.899  | 0.392   | 0.882 | 23.56  | —      |

Authoritative values live in `BASELINE.json`. This table is a snapshot of
the state captured at baseline-freeze time; it will drift if the baseline is
ratcheted. Don't rely on the markdown table for diffs — always run the
script.

### First-look notes on the 120d baseline

- **outlet_120d evt F1 (0.960) > outlet_60d (0.927)** because the second
  60-day wave adds more "easy" short-event labels that dilute the 3
  pre-bootstrap FNs. Event F1 here is a weak signal — the time F1 drop
  (0.758 → 0.559) tells the honest story: sustained FP bands on stationary
  voltage and post-shift wind-down accumulate linearly with scenario length.
- **waterleak_120d events_per_incident = 4.74** — 90 detector events for
  19 labels — is the single worst alert-burden number in the suite. The
  second `trend` on battery is probably triggering fresh CUSUM chains
  beyond the existing 90h drop threshold. High-leverage 120d-only target.
- **Both 120d scenarios worst-incident-recall ≥ 0.842**, better than the
  60d waterleak (0.700) — indicating recall scales fine, it's the
  precision / fp_h/d side where 120d adds pain.
