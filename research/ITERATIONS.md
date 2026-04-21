# Research Iterations

Append-only log of research iterations. Each iteration tests **one** hypothesis,
records the metric delta on every scenario in both the 60d and 120d suites,
and ends with a binary verdict (ACCEPT / REJECT / PARTIAL).

- **Primary metric:** event F1, averaged across the whole suite.
- **Hard floors (any single scenario, enforced by `run_research_eval.py --diff-baseline`):**
  - `evt_f1` drop > 0.005 → REGRESSION.
  - `incident_recall` drop > 0.005 → REGRESSION.
  - `time_f1` drop > 0.02 → REGRESSION. *Long-horizon guardrail*: evt_f1
    treats a 4h detection on a 30d GT as a perfect TP, so without a time-based
    floor, hypotheses that improve event count while sacrificing long-anomaly
    coverage would silently pass.
  Any single floor crossed is auto-REJECT regardless of aggregate gain.
- **Secondary metrics:** fp_h_per_day, events_per_incident — treated
  as tiebreakers when primary moves within ±0.002.

Every entry uses the template below. Do not squash iterations; keep a full record
so regressions can be traced back.

---

## Iteration template

```
## Iter NNN — <short name>                                              <YYYY-MM-DD>

**Hypothesis:** one sentence, falsifiable.
**Reasoning:** why we think this will help; what prior evidence (plot page, memory
note, or iteration) motivated it.
**Target scenarios:** e.g. "outlet_120d + waterleak_120d (long-horizon drift)"
**Expected direction:** e.g. "evt F1 ↑ on 120d outlet; fp_h/d ↓ on long voltage bands;
no change on 60d outlet_short."
**Band:** SHORT / MEDIUM / LONG / orchestration — where the change lives (see README.md).

**Change:**
- `src/anomaly/<file>.py` : <one-line description of edit>
  (keep this list short; if more than ~2 files change, split the hypothesis)

**Baseline (from research/BASELINE.json):**
| suite / scenario          | evt F1 | time F1 | incR  | fp_h/d |
|---------------------------|:------:|:-------:|:-----:|:------:|
| 60d  mean                 |        |         |       |        |
| 120d mean                 |        |         |       |        |
| outlet_60d                |        |         |       |        |
| outlet_tv_60d             |        |         |       |        |
| outlet_kettle_60d         |        |         |       |        |
| waterleak_60d             |        |         |       |        |
| outlet_short_60d          |        |         |       |        |
| outlet_120d               |        |         |       |        |
| waterleak_120d            |        |         |       |        |

**Result:**
| suite / scenario          | Δ evt F1 | Δ time F1 | Δ incR | Δ fp_h/d |
|---------------------------|:--------:|:---------:|:------:|:--------:|
| 60d  mean                 |          |           |        |          |
| 120d mean                 |          |           |        |          |
| (per-scenario rows)       |          |           |        |          |

**Plots inspected:**
- `out/<scenario>_viz.pdf` p.<N> — <what the plot confirmed or refuted>
- `out/<scenario>_viz_long.pdf` summary + p.<N> — <observation>

**Verdict:** ACCEPT / REJECT / PARTIAL
**Reason:** one sentence. If PARTIAL, state exactly which sub-change was kept and which was reverted.
**Follow-ups:** new hypotheses spawned (add to HYPOTHESES.md if worth pursuing).
```

---

## History (most recent at top)

<!-- Research session appends iterations above this line. Keep the template above unchanged. -->

_(no iterations logged yet — this file is initialized for the first research session.)_
