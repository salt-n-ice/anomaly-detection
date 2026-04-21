# Explain-quality hypotheses backlog

Each entry: Priority (P0/P1/P2), Risk (L1/L2/L3), brief.

## P0

- **H1 — Include `sub_types` tally in the rendered prompt.** L1.
  Current `build_prompt` omits `n_sub_alerts` / `sub_types`; the LLM can't
  tell a 34-tick clock_drift burst from a single OOR spike. Predict:
  `type_identifiability` up on DQG-heavy scenarios (outlet_short clock_drift).

- **H2 — Surface score-to-threshold ratio in the prompt.** L1.
  Bundles currently show raw `score` + `threshold` but not the ratio.
  Predict: `self_weakness_signal` (FP rubric) up because a reader can more
  easily flag "barely above threshold" FPs.

## P1

- **H3 — Add `window_range_ratio` to the magnitude block.** L2.
  delta / peak doesn't distinguish "real excursion within known range" from
  "ZOH artefact near sensor ceiling". Needs a `sensor_range` lookup from
  config.

- **H4 — Render detector context dicts even when empty.** L1.
  When `detector_context == []` the prompt says
  "(per-detector context dicts unavailable)" — negative signal. Try
  "no per-detector diagnostics available for this fused chain" wording
  to see if it changes judge scoring (meta-check on prompt wording).

## P2

- **H5 — Add nearest-neighbour calendar comparison.** L3.
  "last week at this hour the sensor showed X" would strengthen
  `temporal_fidelity` for time-of-day / weekend anomalies. Requires
  pulling the events DataFrame ±7 days around the window.
