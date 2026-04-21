# Explain-quality research loop

Parallel harness to `research/` that grades `src/anomaly/explain.py`'s bundles
and prompts against ground-truth labels.

## Flow

```
detections + labels + events ─> run_explain_eval.py ─> runs/<ts>/<scen>_cases.jsonl + _prompts.md
                                                              │
                                            [Claude-in-session judge]
                                                              │
                                          runs/<ts>/<scen>_scores.jsonl
                                                              │
                                            aggregate_explain_scores.py
                                                              │
                                 runs/<ts>/summary.json  ──> diff vs EXPLAIN_BASELINE.json
```

## Files

| File                           | Purpose                                                                 |
|--------------------------------|-------------------------------------------------------------------------|
| `run_explain_eval.py`          | Generate per-scenario cases + prompts.md from detections + labels.      |
| `aggregate_explain_scores.py`  | Roll per-scenario scores into a snapshot; save / diff baseline.         |
| `EXPLAIN_BASELINE.json`        | Frozen baseline (created via `--save-baseline`).                        |
| `EXPLAIN_ITERATIONS.md`        | Append-only iteration log.                                              |
| `EXPLAIN_HYPOTHESES.md`        | Ranked backlog of explain-quality hypotheses.                           |
| `START_EXPLAIN_RESEARCH.md`    | Session-bootstrap prompt (paste into a fresh Claude session).           |
| `runs/<ts>/`                   | One directory per run: cases, prompts, scores, summary.                 |
| `runs/latest.txt`              | Plain text pointer — the latest `<ts>`.                                 |
| `runs/latest.json`             | Copy of the latest `summary.json`.                                      |

## Commands

```bash
# Precondition: detections exist under out/<scenario>_detections.csv
python research/run_research_eval.py --suite all   # refresh detections if needed

# Generate cases for all scenarios
python research/explain/run_explain_eval.py --suite all

# In this Claude session:
#   user: "grade explain runs/<ts> outlet_60d"
#   Claude reads <scen>_cases.jsonl, writes <scen>_scores.jsonl
# Repeat per scenario.

# Aggregate + diff
python research/explain/aggregate_explain_scores.py --run latest --diff-baseline

# Freeze a new baseline after an ACCEPT you want to ratchet
python research/explain/aggregate_explain_scores.py --run latest --save-baseline
```

## Rubric (1-5 per dim)

**TP rubric:** `type_identifiability`, `magnitude_fidelity`, `temporal_fidelity`,
`detector_evidence_usefulness`, `no_misleading_content`.

**FP rubric:** `self_weakness_signal`, `evidence_coherence`,
`no_false_confidence`.

Score schema and decision tree — see `docs/superpowers/specs/2026-04-21-explain-eval-design.md`.
