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

The diff applies three floors per scenario:
- **evt F1:** drop > `--tol` (default 0.005) is a regression.
- **incident_recall:** drop > `--tol` (default 0.005) is a regression.
- **time F1:** drop > `--time-tol` (default 0.02) is a regression. *This is
  the long-horizon guardrail*: evt_f1 treats a 4h detection on a 30d GT as a
  perfect TP, so without a time-based floor, hypotheses that improve event
  count while sacrificing long-anomaly coverage or generating multi-day FP
  strips would silently pass. time_f1 is duration-weighted, so it catches
  both failure modes; the 0.02 floor is looser than evt_f1's because
  seconds-based F1 is intrinsically noisier.

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

## Baseline values (as of 2026-04-21, both suites — ratcheted after Iters 003-005)

| Scenario         | evt F1 | time F1 | incR  | fp_h/d | ev/inc |
|------------------|:------:|:-------:|:-----:|:------:|:------:|
| **60d suite**    |        |         |       |        |        |
| outlet_60d       | 0.927  | 0.758   | 0.864 | 12.73  | 0.77   |
| outlet_tv_60d    | 0.753  | 0.769   | 0.909 | 12.40  | 0.64   |
| outlet_kettle_60d| 0.952  | 0.767   | 0.909 | 12.73  | 0.27   |
| waterleak_60d    | 0.824  | 0.324   | 0.700 | 26.73  | 0.70   |
| outlet_short_60d | 0.874  | 0.629   | 0.850 |  0.63  | 1.00   |
| **60d mean**     | 0.866  | 0.649   | 0.846 | 13.05  | —      |
| **120d suite**   |        |         |       |        |        |
| outlet_120d      | 0.960  | 0.559   | 0.923 | 24.61  | 0.49   |
| waterleak_120d   | 0.896  | 0.225   | 0.842 | 22.42  | 3.74   |
| **120d mean**    | 0.928  | 0.392   | 0.882 | 23.52  | —      |

Authoritative values live in `BASELINE.json`. This table is a snapshot of
the state captured at baseline-freeze time; it will drift if the baseline is
ratcheted. Don't rely on the markdown table for diffs — always run the
script.

### Ratchet history

- **2026-04-20** — initial freeze (all mean evt F1 = 0.860).
- **2026-04-21** — ratcheted after session `research/evt-f1-round-2` iters
  003-005 (margin filter on `{temporal_profile}` singletons in both
  corroboration classes + score ceiling on `{cusum, multivariate_pca}`).
  outlet_short_60d +0.111, waterleak_120d +0.058, others unchanged.
  60d-mean evt F1 0.844 → 0.866, 120d-mean 0.899 → 0.928.

### Remaining structural gaps (as of 2026-04-21 ratchet)

- **outlet_tv_60d evt F1 = 0.753** stays the weakest. All 5 evt_FPs are
  post-weekend_anomaly wind-down on `outlet_tv_power` (BURSTY). Same det-sets
  are TPs on other scenarios. Fix needs cross-chain fuser state or adaptation.
- **waterleak_120d time F1 = 0.225** — coverage, not fragmentation. 3 evt_FPs
  are `{cusum, mvpca, sub_pca}` chains on leak_battery *between* the two
  trend labels; same shape as outlet_tv's wind-down problem (event-merge gap
  isolates them from bridging TPs).
- **waterleak_60d time F1 = 0.324** — post-cal-drift tail on leak_temperature.
  Coverage is 99% but time_precision is 19% because detection windows extend
  past permanent-shift labels with no reset. Adaptation-flavored problem.
- **outlet_120d time_precision = 0.391** — same post-shift-tail mechanism
  as waterleak_60d time F1; all 36 evt_TPs at 100% precision, but time-weighted
  the tails dominate.
- Pre-bootstrap FNs (fridge_power spike/dip/saturation Feb 5-13) persist on
  outlet_60d / outlet_short_60d / outlet_120d. Backlog item B1.
