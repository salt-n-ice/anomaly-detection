# START_EXPLAIN_RESEARCH — Auto-Research Prompt (explain quality)

You are running an autonomous research session on the explain layer at
`src/anomaly/explain/`. The pipeline + detection metric are out of scope
and frozen by upstream work — you are evaluating and improving the
post-detection bundle/prompt pipeline only.

Operate like an experimental scientist: hypothesise → implement minimally
→ re-run cases → re-measure → verdict → log. One hypothesis per iteration.

---

## 1 · Read state (once at session start)

1. **`src/anomaly/explain/`** — skim every submodule (`signals.py`,
   `classify.py`, `bundle.py`, `prompt.py`, `magnitude.py`, `temporal.py`,
   `csv.py`, `types.py`). You need to know what the bundle and prompt
   look like before you can reason about quality.
2. **`research/explain/EXPLAIN_BASELINE.json`** — frozen reference
   numbers + metric definition. Already established (see §2).
3. **`research/explain/EXPLAIN_ITERATIONS.md`** — append-only iter log.
   Read only the most recent 1–2 iters to know what was just tried.
4. **`research/explain/EXPLAIN_HYPOTHESES.md`** — backlog of candidate
   ideas. Pull from this when picking the next iter.

State the current baseline numbers in one chat line so the user knows
you've grounded.

---

## 2 · The metric (fixed — do not redesign without escalation)

**Headline (per scenario):** `super_match_rate` — fraction of TP
user_behavior labels whose super-class matches at least one overlapping
chain's `bundle.classification.type` super-class.

**Auxiliaries (per scenario):**
- `strict_match_rate` — exact-type equality (informational; if super
  goes up but strict goes down, the change is collapsing categories
  rather than resolving them).
- `class_match_rate` — bundle's `classification.class` vs GT's
  `label_class` (gates TP credit in the detection metric, so it must
  hold).
- `by_gt_type` — strict + super per GT anomaly_type (diagnostic; catches
  aggregate-masking on rare types).

**Super-class map** (in `research/explain/explain_metric.py::SUPER_CLASS`):

```
{level_shift, month_shift, trend, degradation_trajectory}
    → value_shift
{weekend_anomaly, time_of_day, seasonal_mismatch, seasonality_loss}
    → calendar_pattern
{spike, dip}
    → impulse
frequency_change   → rate_shift           (alone — distinct mechanism)
water_leak_sustained → water_leak_sustained (alone — pre-typed)
unusual_occupancy  → unusual_occupancy    (alone)
sensor_fault types → each its own super-class
```

Rationale: many strict-type misses are *intrinsically undecidable* from
a single chain emit (level_shift vs month_shift needs multi-week calendar
context not in the bundle). Penalizing the classifier for not getting
`month_shift` rewards guessing; rewarding super-class match incentivizes
mechanism-honest classification at the resolution physically achievable
from the bundle.

**Granularity:** per LABEL, not per chain. A single label may have many
overlapping chains — it counts once in the denominator and is matched
if ANY overlapping chain matches.

**Baseline (commit `181afa9`, 2026-04-25), production scenarios:**

| scenario        | n_ub | super | strict | class |
|-----------------|-----:|------:|-------:|------:|
| household_60d   |   12 | 0.833 | 0.750  | 0.929 |
| household_120d  |   23 | 0.783 | 0.696  | 0.885 |
| leak_30d        |    6 | 0.833 | 0.833  | 0.857 |

**Verdict thresholds:**
- `tol = 0.02` per scenario on the headline (`super_match_rate`).
- `noise_floor = 0.005` (changes within ±0.5pp on headline are NULL).
- Production scenarios gate ACCEPT/REJECT. Holdout regressions surface
  as warnings only (do not block).

If you find the metric mis-specified mid-loop (the headline goes up
while user-perceived quality clearly degrades, or it's stuck at ceiling
for trivial reasons), **stop and escalate** (§4) — don't silently swap
metrics, the iter log must remain comparable.

---

## 3 · The loop

```
pick one hypothesis  →  modify src/anomaly/explain/ minimally  →
regenerate cases  →  re-measure  →  diff baseline  →  verdict  →
log  →  commit-or-revert
```

### 3.1 Hypothesis

Pull highest-priority from `EXPLAIN_HYPOTHESES.md`, or generate one by
auditing the worst-scoring scenario from the last baseline. State in
chat (one line each):

- Hypothesis.
- Which metric you expect to move and by how much.
- Which scenarios should move; which should stay neutral.
- The minimum code change to `src/anomaly/explain/`.
- A specific delta threshold that would flip you to REJECT.

### 3.2 Implement minimally

Edit only `src/anomaly/explain/`. Do not touch detectors, pipeline,
or the detection-side eval harness. If a hypothesis can only land via
metric-side or pipeline-side changes, escalate (§4) — that's a
separate workstream.

### 3.3 Re-run + re-measure

```bash
# Regenerate cases (~12 min full suite, dominated by hh120d + dense_90d):
python research/explain/run_explain_eval.py --suite all

# Compute metrics + diff vs baseline:
python research/explain/explain_metric.py --run latest --diff-baseline
```

### 3.4 Verdict

The metric script's `print_diff` prints a status per scenario:
- `IMPROVEMENT` — `d_super > noise_floor`, scenario's super lifted.
- `NULL` — `|d_super| <= noise_floor`.
- `MINOR_REGRESSION` — within `[-tol, -noise_floor]` band.
- `REGRESSION` — `d_super < -tol` on a production scenario; this
  flips ACCEPT → REJECT.
- `OVERFIT_WARNING` — same on a holdout scenario; warns but doesn't
  block.

Decide:
- **ACCEPT:** no production REGRESSION; aggregate moves the right way.
  Commit (`explain(iter NNN): <title>`). Optionally ratchet
  `EXPLAIN_BASELINE.json` (run `explain_metric.py --save-baseline`)
  only when the user confirms the new floor.
- **REJECT (regression):** at least one production REGRESSION.
  `git checkout -- src/anomaly/explain/` and verify the working tree
  is clean.
- **NULL:** no scenario moves > noise_floor. Log as null; remove the
  hypothesis from the backlog (or note why it didn't move).

### 3.5 Log

Append to `EXPLAIN_ITERATIONS.md` per the template at the top of that
file: iter number + date + title, hypothesis, change, baseline + new +
diff per scenario, verdict, follow-ups.

---

## 4 · Stop-and-report criteria

Pause and report to the user when:

1. **Headline metric mis-specified** — an iter exposes that the
   headline doesn't capture something quality-relevant. Don't silently
   swap; escalate.
2. **Five consecutive REJECTs / NULLs** on hypotheses pulled from the
   backlog — the obvious moves are exhausted; pause for direction.
3. **Out-of-scope changes required** — anything in `src/anomaly/
   detectors.py`, `src/anomaly/pipeline.py`, or
   `src/anomaly/metrics.py` is escalation-only.
4. **Harness errors or scenario fails to generate** — debug or
   escalate; don't silently skip.

---

## 5 · Guardrails

- **One change per iter.** Bundling multiple hypotheses makes the
  diff uninterpretable.
- **Revert regressions immediately.** No partial work carried.
- **No new dependencies.** The explain layer stays pure-Python on
  `pandas` + `numpy`.
- **Don't curve-fit.** A change that "fixes 3 known-bad cases on
  hh120d" is overfitting to your audit sample, not a generalizable
  mechanism. State the mechanism reason a change should help.
- **Document mechanism, not data.** The iter log explains WHY the
  change moves the metric in terms of bundle/prompt design, not
  "rule X rejects N% on the current data."

---

## 6 · Working units

- `research/explain/` — this directory. Iter log + baseline + backlog
  + metric script live here. Gitignored at the project level.
- `src/anomaly/explain/` — code under test. Commit prefix
  `explain(iter NNN):` for traceability.
- `research/explain/runs/<timestamp>/` — generated case data per
  scenario per run. The latest is what you measure against;
  `runs/latest.txt` points to the most recent timestamp.

---

## 7 · One-line invocation

The auto-research entry point is a single instruction:

> *Read research/explain/START_EXPLAIN_RESEARCH and continue iterations
> on the explain layer.*

That's it. The session reads §1 (state), checks `EXPLAIN_BASELINE.json`
(present — established), and begins §3 (the loop). No further user
input required to bootstrap.
