# Explain-layer research workspace

This directory is the research workspace for evaluating and improving
the **explain layer** at `src/anomaly/explain/`.

## Entry point

For the loop mechanics, verdict rules, and logging conventions, see
[`START_EXPLAIN_RESEARCH.md`](START_EXPLAIN_RESEARCH.md).

## What's in scope

- The bundle returned by `anomaly.explain.explain(alert, events)`:
  what fields it contains, how downstream consumers read them.
- The prompt rendered by `anomaly.explain.build_prompt(bundle)`:
  what it tells an LLM consumer.
- The deterministic classifier `anomaly.explain.classify_type(alert)`:
  how its predicted type compares to ground-truth labels.

## What's out of scope

- Detector code at `src/anomaly/detectors.py`.
- Detection metric at `src/anomaly/metrics.py`.
- The detection-side eval harness at `research/run_research_eval.py`.

If a hypothesis can only land via changes to those, escalate to the
user — that's a separate workstream.

## Files

- `START_EXPLAIN_RESEARCH.md` — auto-research operations manual.
- `EXPLAIN_BASELINE.json` — frozen reference numbers (created on the
  first iter via the bootstrap in §2 of START).
- `EXPLAIN_ITERATIONS.md` — append-only iter log.
- `EXPLAIN_HYPOTHESES.md` — forward-looking candidate backlog.
- `run_explain_eval.py` — case generator.
- `runs/<timestamp>/` — generated case data per scenario per run.
