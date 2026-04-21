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

## Iter 004 — C4: extend {temporal_profile} margin filter to BURSTY+BINARY 2026-04-21

**Hypothesis:** Adding the same `{temporal_profile}` `score ≥ 1.2×threshold`
branch to `PassThroughCorroboration.accepts` will drop the 2 FP fridge_power
singletons on outlet_short_60d (BURSTY, scores 4.29 / 4.78) and the 10 FP
leak_basement singletons on waterleak_120d (BINARY, all 4.272) without TP
loss, because no BURSTY/BINARY temporal_profile singleton in any detection
CSV corresponds to a matching label.
**Reasoning:** Iter 003 pre-audit identified exactly these as the remaining
sub-4.8 singletons outside CONTINUOUS. The risk profile matches Iter 003
(L1): singleton-removal preserves evt_tp counts per-label while pulling
`evt_fp` and `n_events` down together — the combination that actually raises
`evt_precision` instead of regressing it via the iter-002 artifact.
**Target scenarios:** outlet_short_60d + waterleak_120d primary.
**Expected direction:** outlet_short_60d Δ evt_f1 ≈ +0.03; waterleak_120d
Δ evt_f1 ≈ +0.03-0.05; others neutral.
**Band:** LONG.

**Change:**
- `src/anomaly/fusion.py` : `PassThroughCorroboration.accepts` — add the same
  `dets == {"temporal_profile"}` margin branch that Iter 003 put in
  `ContinuousCorroboration.accepts`. Now 2 lines are duplicated; kept
  duplicated rather than abstracted (single rule, two rule classes).

**Baseline (from research/BASELINE.json):**
| suite / scenario          | evt F1 | time F1 | incR  | fp_h/d |
|---------------------------|:------:|:-------:|:-----:|:------:|
| 60d  mean                 | 0.844  | 0.648   | 0.846 | 13.05  |
| 120d mean                 | 0.899  | 0.392   | 0.883 | 23.56  |
| outlet_60d                | 0.927  | 0.758   | 0.864 | 12.73  |
| outlet_tv_60d             | 0.753  | 0.769   | 0.909 | 12.40  |
| outlet_kettle_60d         | 0.952  | 0.767   | 0.909 | 12.73  |
| waterleak_60d             | 0.824  | 0.324   | 0.700 | 26.73  |
| outlet_short_60d          | 0.763  | 0.622   | 0.850 |  0.66  |
| outlet_120d               | 0.960  | 0.559   | 0.923 | 24.61  |
| waterleak_120d            | 0.838  | 0.225   | 0.842 | 22.50  |

**Result (research/runs/20260421T154137Z.json):**
| suite / scenario          | Δ evt F1 | Δ time F1 | Δ incR | Δ fp_h/d |
|---------------------------|:--------:|:---------:|:------:|:--------:|
| 60d  mean                 | +0.010   | +0.000    | +0.000 | +0.00    |
| 120d mean                 | +0.029   | +0.000    | +0.000 | −0.04    |
| outlet_60d                | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_tv_60d             | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_kettle_60d         | +0.000   | +0.000    | +0.000 | +0.00    |
| waterleak_60d             | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_short_60d          | **+0.052** | +0.000  | +0.000 | +0.00    |
| outlet_120d               | +0.000   | +0.000    | +0.000 | +0.00    |
| waterleak_120d            | **+0.059** | +0.000  | +0.000 | −0.08    |

**Plots inspected:** none — pre-run audit (Iter 003's cross-scenario
detection-CSV scan) enumerated exactly the 12 singletons that would drop,
all confirmed as unmatched-to-label. Post-run event-count drops
(outlet_short 25 → 23, waterleak_120d 81 → 71) matched the audit within 1
event; fp_h/d moved the expected direction on waterleak_120d (−0.08).

**Verdict:** ACCEPT.
**Reason:** Two scenarios improved substantially (+0.052 / +0.059 evt_f1),
zero regressions, no floor crossed. Aggregate 60d mean +0.010, 120d mean
+0.029 — largest single-iteration gain so far in this session.
**Follow-ups:**
- outlet_tv_60d stays at evt_f1 0.753, untouched. Its 5 evt_FPs (precision
  0.643) are the largest remaining event-level gap on any scenario; next
  iteration should target them. Spawn C5 (investigate outlet_tv_60d FP
  bucket composition) in HYPOTHESES.md.
- waterleak_120d time_f1 stays at 0.225 (coverage problem, not alert-count),
  untouched by this iteration — still a 120d time_f1 target.
- The 1.2× constant is a magic number. If future iterations want to revisit
  the tightness, it deserves promotion to a module-level or per-archetype
  kwarg. Keeping the literal in place until a second use case appears.

---

## Iter 003 — C2*: marginal-|z| filter for {temporal_profile} CONTINUOUS  2026-04-21

**Hypothesis:** Adding a margin filter to `{temporal_profile}`-only CONTINUOUS
chains — require at least one alert with `score ≥ 1.2 × threshold` — will drop
`outlet_short_60d`'s documented low-|z| FP singletons without losing any TP,
because real temporal_profile singletons either score >4.8 (outlet fridge_power
Mar 7/14: 5.4-7.1; outlet_voltage noise_floor_up: 80) or live on archetypes
that don't use ContinuousCorroboration.
**Reasoning:** Iter 002 taught that any chain-merging change triggers the
`evt_precision = 1 − evt_fp/n_events` artifact. Singleton-removal is the
opposite: it drops events *as FPs*, preserving TP counts. Cross-scenario grep
confirmed no sub-4.8 temporal_profile singleton corresponds to a label for any
CONTINUOUS sensor outside the waterleak_120d May 2-9 calibration_drift window,
which is independently covered by multi-det chains.
**Target scenarios:** outlet_short_60d primary; waterleak_120d watch.
**Expected direction:** outlet_short_60d Δ evt_f1 ≈ +0.05, others neutral.
**Band:** LONG.

**Change:**
- `src/anomaly/fusion.py` : `ContinuousCorroboration.accepts` — new branch
  before fall-through `return True`:
  ```python
  if dets == {"temporal_profile"}:
      return any(a.score >= 1.2 * a.threshold for a in alerts)
  ```

**Baseline (from research/BASELINE.json):**
| suite / scenario          | evt F1 | time F1 | incR  | fp_h/d |
|---------------------------|:------:|:-------:|:-----:|:------:|
| 60d  mean                 | 0.844  | 0.648   | 0.846 | 13.05  |
| 120d mean                 | 0.899  | 0.392   | 0.883 | 23.56  |
| outlet_60d                | 0.927  | 0.758   | 0.864 | 12.73  |
| outlet_tv_60d             | 0.753  | 0.769   | 0.909 | 12.40  |
| outlet_kettle_60d         | 0.952  | 0.767   | 0.909 | 12.73  |
| waterleak_60d             | 0.824  | 0.324   | 0.700 | 26.73  |
| outlet_short_60d          | 0.763  | 0.622   | 0.850 |  0.66  |
| outlet_120d               | 0.960  | 0.559   | 0.923 | 24.61  |
| waterleak_120d            | 0.838  | 0.225   | 0.842 | 22.50  |

**Result (research/runs/20260421T153328Z.json):**
| suite / scenario          | Δ evt F1 | Δ time F1 | Δ incR | Δ fp_h/d |
|---------------------------|:--------:|:---------:|:------:|:--------:|
| 60d  mean                 | +0.003   | +0.000    | +0.000 | +0.00    |
| 120d mean                 | +0.001   | −0.001    | +0.000 | +0.00    |
| outlet_60d                | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_tv_60d             | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_kettle_60d         | +0.000   | +0.000    | +0.000 | +0.00    |
| waterleak_60d             | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_short_60d          | **+0.017** | +0.000  | +0.000 | +0.00    |
| outlet_120d               | +0.000   | +0.000    | +0.000 | +0.00    |
| waterleak_120d            | +0.003   | −0.001    | +0.000 | +0.00    |

**Plots inspected:** none — the cross-scenario detection-CSV scan (`awk` over
`out/*_detections.csv` filtering `detector=="temporal_profile"`) gave me the
pre-run audit: every sub-4.8 singleton on a CONTINUOUS sensor was either an
outlet_short FP or a May 2-9 calibration_drift tail with multi-det coverage,
and every temporal_profile TP elsewhere clears 4.8. The run's event-count
shifts (outlet_short 26 → 25, waterleak_120d 90 → 81) matched the pre-run
audit exactly.

**Verdict:** ACCEPT.
**Reason:** Aggregate 60d evt_f1 rose (+0.003), 120d evt_f1 rose (+0.001), no
floor crossed, no incident_recall drop, no fp_h/d increase on any scenario.
Outlet_short_60d gained the documented +0.017 from removing the Feb 17 voltage
FP singleton (score 4.19, ratio 1.048). The remaining two fridge_power
singletons (BURSTY, scores 4.29 / 4.78) survived because BURSTY uses
`PassThroughCorroboration` — spawns Iter 004 to extend the filter.
**Follow-ups:** Iter 004 — extend the `{temporal_profile}` margin filter to
`PassThroughCorroboration` (hits both BURSTY and BINARY). Pre-run audit
identifies 2 FP fridge_power singletons on outlet_short_60d (another +0.03ish
evt_f1) and 10 leak_basement singletons on waterleak_120d (potentially +0.05
evt_f1 if calibration_drift coverage is independent) as the accessible wins.
Zero BURSTY/BINARY temporal_profile singleton TPs in the seven detection CSVs.

---

## Iter 002 — L1: raise CONTINUOUS max_span 96h → 192h                    2026-04-21

**Hypothesis:** Raising `max_span` on the CONTINUOUS fuser from 96h (4d) to
192h (8d) will lift `time_f1` on `outlet_120d` + `waterleak_120d` by stitching
multi-day detector firing that force-closes every 4 days, without regressing any
60d scenario past the 0.02 time_f1 floor.
**Reasoning:** `max_span` only matters for chains that actually reach it —
sustained firing across 4+ days with <15 min gaps, i.e. long-GT labels and
post-shift wind-down tails. Memory `project_iter_gains_2026_04`: "max_span 96h → 168h
was net wash" on 60d, so the 60d downside was bounded. Iter 001 already ruled out the
2-det bucket; the FP time must ride sustained chains.
**Target scenarios:** outlet_120d + waterleak_120d primary; 60d scenarios for safety.
**Expected direction:** Δ time_f1 ↑ on 120d; Δ evt_F1 ~0 everywhere per chunking
invariance of evt metrics; Δ fp_h/d may ↑ or ↓.
**Band:** LONG.

**Change:**
- `src/anomaly/profiles.py` : `_continuous_fuser` — `max_span=96*3600` → `max_span=192*3600`.

**Baseline (from research/BASELINE.json):**
| suite / scenario          | evt F1 | time F1 | incR  | fp_h/d |
|---------------------------|:------:|:-------:|:-----:|:------:|
| 60d  mean                 | 0.844  | 0.648   | 0.846 | 13.05  |
| 120d mean                 | 0.899  | 0.392   | 0.883 | 23.56  |
| outlet_60d                | 0.927  | 0.758   | 0.864 | 12.73  |
| outlet_tv_60d             | 0.753  | 0.769   | 0.909 | 12.40  |
| outlet_kettle_60d         | 0.952  | 0.767   | 0.909 | 12.73  |
| waterleak_60d             | 0.824  | 0.324   | 0.700 | 26.73  |
| outlet_short_60d          | 0.763  | 0.622   | 0.850 |  0.66  |
| outlet_120d               | 0.960  | 0.559   | 0.923 | 24.61  |
| waterleak_120d            | 0.838  | 0.225   | 0.842 | 22.50  |

**Result (research/runs/20260421T151952Z.json):**
| suite / scenario          | Δ evt F1 | Δ time F1 | Δ incR | Δ fp_h/d |
|---------------------------|:--------:|:---------:|:------:|:--------:|
| 60d  mean                 | +0.000   | −0.000    | +0.000 | +0.05    |
| 120d mean                 | −0.006   | +0.019    | +0.000 | +0.40    |
| outlet_60d                | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_tv_60d             | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_kettle_60d         | +0.000   | +0.000    | +0.000 | +0.00    |
| waterleak_60d             | +0.000   | −0.002    | +0.000 | +0.27    |
| outlet_short_60d          | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_120d               | +0.000   | +0.002    | +0.000 | +0.00    |
| waterleak_120d            | **−0.013** | +0.035  | +0.000 | +0.80    |

**Plots inspected:**
- `out/waterleak_120d_viz_long_iter002.pdf` summary + battery pages — confirms
  the Feb 21 → Mar 1 `cusum`-only 192h chain on `leak_battery` (8d exactly,
  max_span-capped). Under 96h this was two 4d chains. Both cases are FP
  (no GT label until Mar 5). Merging two FPs into one saved 1 evt_FP.
- Metrics JSON for waterleak_120d: `evt_tp=16` (unchanged from baseline),
  `evt_fn=3` (unchanged), `evt_fp` 15 → 14, `n_events` 90 → 73.

**Verdict:** REJECT.
**Reason (autopsy):** `waterleak_120d` evt_F1 −0.013 crosses the −0.005 floor.
Mechanism is a metric artifact, not a quality loss: `evt_precision =
1 − evt_fp/n_events`, so collapsing 17 TP-matching events into fewer chains
while only dropping 1 FP mechanically lowers precision. TP/FN counts were
unchanged, and time_f1 actually improved (+0.035 on waterleak_120d, +0.002 on
outlet_120d). This is a structural blocker: **any change that merges TP events
faster than FP events will regress `evt_f1` via this artifact**, regardless of
whether detection quality improved. On `outlet_120d` the movement was nearly
zero (+0.002 time_f1) because the long-GT labels don't have the sustained
4+ day alert-streams I predicted — their FP time comes from post-shift
wind-down tails, a different structural phenomenon. L1 was the wrong
diagnosis for outlet_120d; for waterleak_120d it was a win on quality but a
loss on the metric. Backlog L1 struck.
**Follow-ups:** Pivot away from anything that merges chains — focus on drops
that remove FP events without affecting TP events. C2 (drop marginal-|z|
temporal_profile singletons on CONTINUOUS) fits this profile and targets 3
documented FPs on outlet_short_60d. Also spawn L1b (a smaller max_span step
like 120h) into HYPOTHESES.md only if a later iteration ratchets the baseline
in a way that changes the mechanics.

---

## Iter 001 — A1: tighten 2-det 4h floor to 6h                            2026-04-21

**Hypothesis:** Raising the `{cusum, sub_pca}` / `{cusum, temporal_profile}`
CONTINUOUS duration floor from 4h to 6h will reduce `fp_h/d` on `outlet_120d`
(stationary voltage FP bands that accumulate into the 4-6h bucket over 120 days)
without regressing evt_F1 / incident_recall on any committed scenario.
**Reasoning:** Memory `project_iter_gains_2026_04` Iter I notes the 4h floor was tuned
on 60d data and targets "1-3h bands"; `BASELINE.md` first-look notes call out 120d
voltage FP-band linear accumulation.
**Target scenarios:** outlet_120d primary; watch all 60d for recall regressions.
**Expected direction:** Δ fp_h/d ↓ on outlet_120d; Δ evt_F1 ≥ −0.005 everywhere.
**Band:** LONG.

**Change:**
- `src/anomaly/fusion.py` : `ContinuousCorroboration.accepts` — `hours=4` → `hours=6`
  on the `{cusum, sub_pca}` / `{cusum, temporal_profile}` branch.

**Baseline (from research/BASELINE.json):**
| suite / scenario          | evt F1 | time F1 | incR  | fp_h/d |
|---------------------------|:------:|:-------:|:-----:|:------:|
| 60d  mean                 | 0.844  | 0.648   | 0.846 | 13.05  |
| 120d mean                 | 0.899  | 0.392   | 0.883 | 23.56  |
| outlet_60d                | 0.927  | 0.758   | 0.864 | 12.73  |
| outlet_tv_60d             | 0.753  | 0.769   | 0.909 | 12.40  |
| outlet_kettle_60d         | 0.952  | 0.767   | 0.909 | 12.73  |
| waterleak_60d             | 0.824  | 0.324   | 0.700 | 26.73  |
| outlet_short_60d          | 0.763  | 0.622   | 0.850 |  0.66  |
| outlet_120d               | 0.960  | 0.559   | 0.923 | 24.61  |
| waterleak_120d            | 0.838  | 0.225   | 0.842 | 22.50  |

**Result (research/runs/20260421T151142Z.json):**
| suite / scenario          | Δ evt F1 | Δ time F1 | Δ incR | Δ fp_h/d |
|---------------------------|:--------:|:---------:|:------:|:--------:|
| 60d  mean                 | +0.000   | +0.000    | +0.000 | +0.00    |
| 120d mean                 | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_60d                | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_tv_60d             | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_kettle_60d         | +0.000   | +0.000    | +0.000 | +0.00    |
| waterleak_60d             | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_short_60d          | +0.000   | +0.000    | +0.000 | +0.00    |
| outlet_120d               | +0.000   | +0.000    | +0.000 | +0.00    |
| waterleak_120d            | +0.000   | +0.000    | +0.000 | +0.00    |

**Plots inspected:** none — null result on every metric made plot inspection
unproductive. Aggregate diff (§3.5 path 4) is self-explanatory: the
`{cusum, sub_pca}` / `{cusum, temporal_profile}` chain bucket between 4h and
6h is empty across all seven scenarios; these det-sets either stay under 4h
(already dropped) or already clear 6h.

**Verdict:** REJECT (null result).
**Reason:** No metric moved. 120d stationary-voltage FPs must ride the
4-detector fall-through branch (`return True`) in `ContinuousCorroboration.accepts`
or be ≥6h already — not the 2-det bucket. Strike A1 from backlog.
**Follow-ups:** Reorient 120d FP hypotheses toward either (a) extending the
CONTINUOUS fuser's `max_span` so long-GT chains stop fragmenting (L1), or
(b) adding a corroboration rule for the 4-detector `{cusum, sub_pca,
multivariate_pca, temporal_profile}` combo in `ContinuousCorroboration.accepts`
— currently it is unconditionally accepted via the `return True` fall-through.
Adding the latter is a new hypothesis, spawned as `C3` in HYPOTHESES.md.

---

