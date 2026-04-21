# START_EXPLAIN_RESEARCH — Auto-Research Prompt (explain quality)

You are running an autonomous research session on the explainer's bundles +
prompts. Target: raise `aggregate.all.mean_tp_mean` on the current case set
without regressing any scenario's per-dim means past `tol` (default 0.2).
Operate like an experimental scientist: hypothesise → implement minimally
→ re-run cases → re-grade → verdict → log. One hypothesis per iteration.

---

## 1 · Ground the session

1. `research/explain/EXPLAIN_BASELINE.json` — metric floors. If missing, run
   the first-time bootstrap below.
2. `research/explain/EXPLAIN_ITERATIONS.md` — prior iterations.
3. `research/explain/EXPLAIN_HYPOTHESES.md` — backlog.
4. `docs/superpowers/specs/2026-04-21-explain-eval-design.md` — rubric and
   scoring contract.
5. `src/anomaly/explain.py` — the subject of evaluation.

Report the current baseline `aggregate.all.mean_tp_mean` and `mean_fp_mean`
so the user knows you've grounded.

## 2 · First-time bootstrap

```bash
# Ensure detections are current
python research/run_research_eval.py --suite all

# Generate cases
python research/explain/run_explain_eval.py --suite all
```

In this Claude session, grade every scenario's cases to produce
`<scen>_scores.jsonl`. Then:

```bash
python research/explain/aggregate_explain_scores.py --run latest --save-baseline
```

## 3 · The loop

```
pick one hypothesis  →  modify src/anomaly/explain.py minimally  →
regenerate cases  →  regrade affected scenarios  →  aggregate  →
diff baseline  →  verdict  →  log  →  clean up
```

### 3.1 Hypothesis

Pull highest-priority from `EXPLAIN_HYPOTHESES.md`. State in chat:
- Hypothesis in one sentence.
- Which rubric dim it targets and why (cite a `notes` field from a prior
  run's scores, or a specific bundle's weakness).
- Which scenarios you expect to move.
- The minimum code change to `src/anomaly/explain.py`.

### 3.2 Implement minimally

Edit `src/anomaly/explain.py` only. Do not touch detectors, pipeline, or
the eval harness.

### 3.3 Re-run + re-grade

```bash
python research/explain/run_explain_eval.py --suite all
# grade each <scen>_cases.jsonl in this session → <scen>_scores.jsonl
python research/explain/aggregate_explain_scores.py --run latest --diff-baseline
```

### 3.4 Verdict

- Any per-scenario dim mean drops by more than `tol` → **REJECT**, revert
  `src/anomaly/explain.py`.
- All scenarios improve or neutral, aggregate rises → **ACCEPT**, commit.
  Ratchet `EXPLAIN_BASELINE.json` with `--save-baseline` only when the user
  says.
- Null result → log as such, remove the hypothesis.

### 3.5 Log

Append to `EXPLAIN_ITERATIONS.md`. Include exact baseline + new numbers, the
code diff summary, and one-line next-move.

## 4 · Guardrails

- One change per iteration.
- Revert regressions immediately.
- Never loosen `tol` to pass — if the floor is wrong, ask the user.
- No new deps.
- The judge (Claude) is the same session throughout; re-reads of the same
  case should produce the same score. If you disagree with a prior score,
  overwrite it and note why.
