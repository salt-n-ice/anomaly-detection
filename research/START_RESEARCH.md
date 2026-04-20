# START_RESEARCH — Auto-Research Prompt

You are running an autonomous research session on the anomaly-detection pipeline.
Target: improve event-F1 on the **60-day suite** and the **120-day suite**
without regressing any scenario past the floors in `BASELINE.md`. Operate like
an experimental scientist: hypothesise → implement minimally → measure →
verdict → log. One hypothesis per iteration. `ultrathink` every decision.

> Keep reading this file to the end before you do anything else. It is the only
> instruction you need — everything else is context linked from here.

---

## 0 · How to use this file

The user invoked this by pasting the contents of `research/START_RESEARCH.md`
into the chat (or running `cat research/START_RESEARCH.md` and sending it).
You are expected to execute the loop in section 3, continuing until the user
tells you to stop, until every HYPOTHESES.md item is exhausted, or until
3 consecutive iterations all REJECT with no new hypothesis spawned.

You have every tool you need: file IO, Bash, and this repo's CLIs
(`python -m anomaly run|eval|viz|viz-long`, `python research/run_research_eval.py`).
There is no separate "agent" to call — you *are* the research agent.

---

## 1 · Ground the session (read these in order)

Do these reads **before** proposing anything. Do not skip.

1. `research/BASELINE.md` — the metric floors you must not regress.
2. `research/BASELINE.json` — authoritative per-scenario numbers. If missing,
   **stop** and run the "first-time bootstrap" in §2.
3. `research/ITERATIONS.md` — all prior iteration history. Read every entry;
   accepted changes are landmines for anything that conflicts with them.
4. `research/HYPOTHESES.md` — backlog. The next iteration is drawn from here
   (or derived from the latest run's plots if the backlog is stale).
5. `CHANGES.md` and the memory files under
   `C:/Users/yashs/.claude/projects/C--Projects-Sensor-data-anomaly-detection-anomaly-detection/memory/`
   (`project_detector_fp_roots.md`, `project_cusum_autocorrelation.md`,
   `project_iter_gains_2026_04.md`, `project_outlet_short_scenario.md`,
   `feedback_tuning_workflow.md`) — these document past traps.
6. `pipeline.md` — the intended design, for when a tuning decision would
   contradict the baseline architecture.
7. `src/anomaly/pipeline.py` and `src/anomaly/detectors.py` — the files you
   will most often edit. Re-read them every session; they change.

State (one line) in your first response what the current `BASELINE.json` says
for the 60d-mean and 120d-mean event F1, so the user knows you've grounded.

---

## 2 · First-time bootstrap (only if BASELINE.json is missing)

```bash
# Generate 120-day datasets (one-off; ~20s each).
cd ../synthetic-generator
sensorgen run scenarios/outlet_120d.yaml    --out out/outlet_120d
sensorgen run scenarios/waterleak_120d.yaml --out out/waterleak_120d

# Freeze the current metrics as the baseline.
cd ../anomaly-detection
python research/run_research_eval.py --suite all --save-baseline
```

If either scenario can't be generated (missing anomaly type in the generator,
for example), list the affected scenarios and ask the user whether to proceed
with a 60d-only baseline or to pause while they fix the generator. Do not
silently run on a partial baseline — the whole point of this exercise is
apples-to-apples comparison.

---

## 3 · The research loop

```
repeat:
    pick one hypothesis  →  implement  →  run  →  inspect plots  →
    verdict  →  log  →  clean up
```

### 3.1 Pick one hypothesis

Pull the highest-priority (P0 > P1 > P2) item from `HYPOTHESES.md` whose risk
(`L*`) you're willing to take given the last 2 iterations' outcomes. If two
REJECTs in a row, step down one priority tier — the high-leverage items are
clearly not easy and a smaller win unblocks signal. If the backlog is empty or
obviously stale, regenerate it: run `research/run_research_eval.py --suite all`,
then read `out/*_viz.pdf` pages covering the worst remaining FPs and `out/*_viz_long.pdf`
summary pages for the worst remaining FNs. Write 2-3 fresh hypotheses into
`HYPOTHESES.md` and pick from them.

**Before implementing, write down** (in your chat reply to the user, not a
file):
- Hypothesis in one sentence.
- Why you believe it (cite the specific plot page, iteration, or memory line).
- Which scenarios you expect to move, in which direction.
- The *minimum* code change. If the minimum touches more than 2 files or
  changes more than ~30 net lines, **split** the hypothesis — a too-large
  change buries cause and effect.

### 3.2 Implement minimally

- Edit only the files named in your plan.
- Leave comments only where a future reader would otherwise be confused by
  *why* — never what.
- Do not touch tests, configs, or the generator unless the hypothesis is
  explicitly about them.
- Before running, mentally replay: "if this code fires too often, which
  metric/scenario moves first?" If you can't answer, you don't understand
  the change well enough.

### 3.3 Run + measure

```bash
# Full evaluation. Produces research/runs/<timestamp>.json + updates latest.json.
python research/run_research_eval.py --suite all
```

If only one suite is relevant to your hypothesis (e.g. a 120d-only change):

```bash
python research/run_research_eval.py --suite 120d
# …then, if 120d looks good, always follow up with the 60d run before accepting:
python research/run_research_eval.py --suite 60d
```

Never ACCEPT a change that improves one suite without running the other.
60d regressions caused by 120d-targeted changes are the most common silent
failure mode in this pipeline.

### 3.4 Inspect the plots

Do not trust aggregate metrics alone. For every scenario whose event F1 moved
by more than ±0.01, regenerate the PDF and read the relevant pages:

```bash
# Windowed view — good for short anomalies and fine-grained FP inspection.
python -m anomaly viz \
  --events ../synthetic-generator/out/<dir>/events.csv \
  --labels ../synthetic-generator/out/<dir>/labels.csv \
  --detections out/<scenario>_detections.csv \
  --out out/<scenario>_viz_iterNN.pdf \
  --window 1d

# Long-anomaly view — one page per label ≥ 24h, with full-scenario and zoomed signal.
python -m anomaly viz-long \
  --events ../synthetic-generator/out/<dir>/events.csv \
  --labels ../synthetic-generator/out/<dir>/labels.csv \
  --detections out/<scenario>_detections.csv \
  --out out/<scenario>_viz_long_iterNN.pdf \
  --min-hours 24
```

The viz layout per page (see `src/anomaly/viz.py:render`):
- Signal trace per sensor.
- A red "truth" lane — one row per anomaly *type*; red bar spans the GT interval.
- A blue "detected" lane — one row per detector *combination*; blue bar spans the fused-chain window.

Reading the page:
- Blue bar under a red bar = TP (aligned horizontally).
- Red bar with no blue under it = FN (missed).
- Blue bar with no red above it = FP (false alarm).
- Multiple detector rows on the blue lane = multiple detector fusion fired.

For `viz-long`, page 1 is a summary table of all labels with TP/FN status and
which detectors fired. Each subsequent page covers one long label: the full
scenario signal with the GT region shaded, a zoomed view (`±max(1d, duration/3)`
context, capped at 14d), and the truth/detection strips.

**When reading the PDF, look at only the pages you need.** Page numbers that
matter:
- Every FP page (from the diff: fp_h/day increases tell you to look for new
  blue bars).
- Every FN page (incident_recall drop tells you to find the missing match).
- The viz-long summary (page 1) for a global "what got caught / missed" view.

### 3.5 Verdict

Compute the diff:

```bash
python research/run_research_eval.py --suite all --diff-baseline
```

Apply the decision tree:

1. **Any scenario crosses a floor** (evt F1 drops more than 0.02, or
   incident_recall drops more than 0.005 from baseline)? → **REJECT**.
   No exceptions. Revert the change (`git checkout -- <file>`).
2. **Aggregate 60d-mean evt F1 rises AND aggregate 120d-mean evt F1 rises,
   neither suite's incident_recall drops, and fp_h/day does not rise by more
   than +10% relative** on any single scenario? → **ACCEPT**. Commit the
   change with a message that mirrors the iteration-log entry. Update
   `BASELINE.json` via `--save-baseline` only if you want to ratchet — most
   iterations leave the baseline alone, so several small ACCEPTs can
   accumulate before the next ratchet.
3. **Mixed movement** (improves some, regresses some within floors)?
   → Decide ACCEPT or PARTIAL based on whether the regressed scenarios are
   documented known hard cases (waterleak time F1, outlet_short fp_h/day)
   or newly-introduced. If newly-introduced, REJECT. Otherwise PARTIAL —
   keep the subset of the code change that cleanly helps, revert the rest,
   and rerun the full suite to confirm.
4. **No movement outside ±0.002 on any metric**? → REJECT and note as "null
   result" in the iteration log. Null results are valuable — they eliminate
   a hypothesis from the backlog.

### 3.6 Log

Append to `research/ITERATIONS.md` using the template at the top of that file.
Copy the exact baseline numbers from `BASELINE.json` and the result numbers
from the latest run JSON under `research/runs/`. No rounding beyond 3 decimals.

List every plot you actually opened in "Plots inspected". If you didn't open
any plots, that iteration was done on faith and must be marked as such in
the verdict note — it is a weaker conclusion.

### 3.7 Clean up

- On ACCEPT: leave `research/runs/latest.json` as the new de-facto metric.
  Do **not** auto-ratchet `BASELINE.json`; the user will say when.
- On REJECT: `git checkout -- <files>` on everything you touched. Confirm
  with `python research/run_research_eval.py --suite all --diff-baseline` —
  the diff output must show zero regressions (you reverted cleanly).
- Delete `out/<scenario>_viz_iterNN.pdf` outputs older than the last 2
  iterations if the `out/` dir is getting crowded.

---

## 4 · Workflow guardrails

These are hard rules — violating any is a bug, not a style choice.

- **One change per iteration.** If in §3.1 you wrote a hypothesis that
  requires two unrelated edits, you have two hypotheses; split them. Prior
  tuning history shows interactions between detectors + fusion are the
  single biggest source of confused outcomes.
- **Revert regressions immediately.** Don't leave a regressing change in
  hoping a later iteration compensates. Unwind *now*, learn *now*.
- **Never tune to a single number.** If outlet_60d event F1 moves by +0.02,
  either waterleak_60d or outlet_short_60d is almost certainly moving too.
  Always read the full table.
- **Ultrathink before every code change.** Prior session feedback from the
  user is emphatic: "ultrathink on each iteration". Concretely: before
  touching code, write out the hypothesis → expected direction → minimum
  change → rollback plan in the response.
- **Never bypass a regression by loosening a floor.** If the floor is wrong,
  say so and ask the user. Do not edit `BASELINE.md` in the same commit as
  a code change.
- **No new dependencies.** The pipeline is numpy + pandas + matplotlib + pyyaml.
  A hypothesis that needs scikit-learn is a research detour, not a tuning
  iteration — file it in HYPOTHESES.md and keep going.

---

## 5 · Escape hatches

Stop the loop and report to the user when any of the following occurs:

- You need to add or rename a detector (larger than a tuning step).
- You need to change metrics or the evaluation script itself — the research
  loop depends on metric continuity.
- Three consecutive iterations REJECT with no new hypothesis spawned; the
  backlog has run dry and the plots no longer suggest next moves.
- A scenario fails to generate, a pipeline run errors, or `run_research_eval.py`
  crashes on a scenario — investigate and report; do not paper over.
- A regression crosses a floor that the user specifically said was
  negotiable in a previous turn and you're unsure.

Always exit cleanly: make sure `git status` has no surprise files beyond the
research/* outputs after a stop.

---

## 6 · The exact commands you will run most often

```bash
# Full eval, no diff — just measure.
python research/run_research_eval.py --suite all

# Full eval, diff vs frozen baseline (exits 1 on regression).
python research/run_research_eval.py --suite all --diff-baseline

# Freeze current metrics as the new baseline (only after an ACCEPT you want to ratchet).
python research/run_research_eval.py --suite all --save-baseline

# Visualize a single scenario post-run.
python -m anomaly viz \
  --events ../synthetic-generator/out/<gen_dir>/events.csv \
  --labels ../synthetic-generator/out/<gen_dir>/labels.csv \
  --detections out/<scen>_detections.csv \
  --out out/<scen>_viz_iterNN.pdf --window 1d

python -m anomaly viz-long \
  --events ../synthetic-generator/out/<gen_dir>/events.csv \
  --labels ../synthetic-generator/out/<gen_dir>/labels.csv \
  --detections out/<scen>_detections.csv \
  --out out/<scen>_viz_long_iterNN.pdf --min-hours 24

# Revert the working tree for a specific file (after a REJECT).
git checkout -- src/anomaly/<file>.py
```

---

## 7 · Begin

1. Do §1 reads. Report 60d-mean and 120d-mean evt F1 from the baseline.
2. If BASELINE.json is missing, do §2 bootstrap.
3. Pick the first hypothesis and state it in the chat.
4. Start the loop. Keep going.

`ultrathink`.
