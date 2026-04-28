# Pipeline internals — technical reference (temp)

Math-heavy companion to `pipeline.md` / `pipeline_visuals.md`. Every
formula and threshold below is grounded in source; line refs in
parentheses. Defaults are the values shipped in `profiles.py` /
detector `__init__`.

Notation:
- `t` = current tick timestamp; `Δt` = seconds between two ticks.
- `v(t)` = signal value at tick.
- `μ̂`, `σ̂`, `MAD` = bootstrap-fit median, std, median-absolute-deviation.
- `||·||` = absolute value.

---

## §1 Adapters — per-archetype resampling

All three adapters expose the same contract: `ingest(event)` buffers raw
events, `emit_ready(now)` yields `(tick, feat_dict)` aligned to a fixed
60-s grid via `_align_up`. A gap of `5·expected_interval_sec` flags the
tick as `dropout` (NaN value).

### 1.1 ContinuousAdapter (`adapter.py:30-69`)

Linear interpolation between the two enclosing events `(a_ts, a_val)`
and `(b_ts, b_val)`:

```
frac  = (t − a_ts) / (b_ts − a_ts)
v(t)  = a_val + (b_val − a_val) · frac        if (b_ts − a_ts) ≤ max_gap
      = NaN                                    otherwise
```

Single-point case (only `a_ts` ≤ `t`): zero-order hold if
`(t − a_ts) ≤ max_gap`, else `NaN`. `max_gap = 5 · expected_interval_sec`
(`core.py:38`).

### 1.2 BurstyAdapter (`adapter.py:72-150`)

Per-event value retained verbatim (or `Δ/Δt` rate if `cumulative`).
**State assignment** uses bootstrap-fit 2-means:

```
fit_state_model:
  v ← bootstrap values, drop NaN
  c₀, c₁ ← percentile(v, 10), percentile(v, 90)             # init
  for _ in 1..20:
      labels[i] = argmin_k |v[i] − cₖ|
      c'ₖ      = mean(v[labels==k])  (else cₖ)
      if ||c' − c|| < ε: break
      c ← c'
  centers ← sort(c)                                         # 0 = off, 1 = on
```

Live: `state(t) = argmin_k |centers[k] − v(t)|`. `time_in_state(t) = t − last_state_change_ts` (resets on transition).

### 1.3 BinaryAdapter (`adapter.py:153-212`)

State machine with rolling 1 h / 24 h history deques.

```
duty_1h(t)   = (1/|H₁|) · Σ_{(τ,s)∈H₁} s          # mean state over last 1 h
duty_24h(t)  = (1/|H₂₄|) · Σ_{(τ,s)∈H₂₄} s
transitions_per_hour(t) = |T ∩ [t−1h, t]|
```

`pending_triggers` accumulates only when `state: 0→1` AND
`deterministic_trigger=true` is set on the sensor config.

---

## §2 Feature engineering (`features.py`)

For every numeric feature `k` in the tick (excluding `dropout`,
`trigger`, bools), maintain three rolling means at windows
`w ∈ {1 h, 24 h, 7 d}` and one diff feature, **per state** (BURSTY) or
state 0 (CONT/BINARY).

Buffer length per `(state, feature, w)` cell:

```
W_w = ⌈w / tick_sec⌉ + 1               # tick_sec = 60 s by default
W_1h = 61,  W_24h = 1441,  W_7d = 10081 floats
```

**O(1) running mean update** (`features.py:53-62`):

```
on tick (state s, feature k, window w):
  if |buf| == W_w:                           # full → evict oldest
      sum -= buf[0]
      buf.popleft()
  buf.append(v); sum += v
  v_roll_w(t) = sum / |buf|
```

**Diff feature:** `v_diff = v(t) − last(state, k)`, with `0` on first
observation. Calendar features (`hour`, `dow`, `is_weekend`, `month`)
are derived directly from the tick timestamp.

---

## §3 Detector math

### 3.1 DataQualityGate — SHORT-band, per raw event (`detectors.py:32-199`)

Each rule fires iff `predicate(ev) ∧ ts > last_fire + cooldown`.

| rule | predicate | cooldown |
|---|---|---|
| `out_of_range` | `v < min` ∨ `v > max` | 30 min |
| `saturation` | `v ≥ max` for **10** consecutive events | (latched, no cooldown) |
| `duplicate_stale` | `ts == last_ts ∧ v == last_v` | none |
| `clock_drift`* | persistence-gated drift counter ≥ 3 | 5 min |
| `dropout` | `Δt > 5·expected_interval_sec` | 30 min |
| `batch_arrival` | 12 events in < 1 s | 30 min |
| `extreme_value` | `v > ref_max · ratio` (after 100-event calibration) | 1 h |

*Clock-drift gating (CONT only, `expected_interval ≤ 3600 s`):*

```
δ = Δt − expected_interval_sec
threshold_tick = max(3 s, 0.005 · expected_interval_sec)
if 0.5·expected ≤ Δt ≤ 1.5·expected:
    if |δ| > threshold_tick: counter = min(counter + 1, 3)
    else:                    counter = max(counter − 1, 0)
else:                        counter = max(counter − 1, 0)    # outside cadence regime
fire iff counter ≥ 3
```

*Extreme-value ratchet:*

```
during calibration (first 100 events):
    ref_max ← max(ref_max, v)
after calibration:
    threshold = ref_max · ratio
    if v > threshold: fire; ref_max ← v   # ratchet up on every fire
ratio = 3.0 (BURSTY)  |  1.7 (CONTINUOUS)
```

### 3.2 RecentShift — CONT, MEDIUM (`detectors.py:202-267`)

Compares short-window value to long-window baselines.

```
short_feature        = "value_roll_1h"
baseline_features    = ("value_roll_24h", "value_roll_7d")
quantile             = 0.999
min_score            = 1.1
```

**Bootstrap fit** (per baseline `b`):

```
δ_b[i] = |value_roll_1h[i] − value_roll_b[i]|       # over all bootstrap rows
threshold[b] = max( quantile(δ_b, 0.999), 10⁻⁶ )    # noise-floor 99.9-th
```

**Live update:**

```
for b in baselines (where v_roll_b is finite):
    δ_b   = |value_roll_1h(t) − value_roll_b(t)|
    r_b   = δ_b / threshold[b]
(b*, r*) = argmax_b r_b                             # most-violated baseline
fire iff r* > min_score
score   = r*
```

The `min_score = 1.1` margin filters periodic-signal point-estimate
noise (basement_temp diurnal undersampling), keeping drift
signatures (calibration_drift / level_shift typically score 4–7).

### 3.3 DutyCycleShift — BURSTY, MEDIUM (`detectors.py:498-730`)

Z-tested rolling 6 h fraction-of-time-on, with a percentile-novelty
gate that activates when bootstrap MAD collapses.

```
window_s    = 6·3600 s
z_threshold = 3.0
cooldown_s  = 2·3600 s
on_threshold = 50 W
```

**Bootstrap fit:**

```
slide a 6h window across bootstrap, step = 3h
for each window k:
    above_sₖ = Σ Δt · 1[v_prev > on_threshold]         (interval contributions)
    total_sₖ = Σ Δt
    duty[k]  = above_sₖ / total_sₖ                       (when total_s > 0)
μ̂ = median(duty)
MAD = median(|duty − μ̂|)
σ̂ = max(MAD, 0.005)                                    # MAD floor
q01, q99 = quantile(duty, 0.01 / 0.99)
mad_at_floor = (raw MAD ≤ 0.005)                       # bimodal-zero flag
```

**Per-bucket calendar baseline:** map `(is_weekend, hour) → median(duty in bucket)`. Tertile rank over the 48 cells: `low ≤ p30`, `high ≥ p70`, else `normal`.

**Live update** (incremental running sums, amortised O(1)):

```
on tick (ts, above):
    Δt = ts − ts_prev
    total_s += Δt;  if above_prev: above_s += Δt
    window.append((ts, above))
    while window[0].ts < ts − window_s:                    # evict
        Δt_old = window[1].ts − window[0].ts
        total_s -= Δt_old
        if window[0].above: above_s -= Δt_old
        window.popleft()
    duty = above_s / total_s
    z    = (duty − μ̂) / σ̂
    fire iff |z| > z_threshold
         AND (ts − last_fire) ≥ cooldown_s
         AND (z > 0 ⇒ duty > q99) AND (z < 0 ⇒ duty < q01)   # percentile gate
```

Score = `|z|`, direction = `sgn(z)` mapped to `high`/`low`,
`bucket_typical` = bucket map at `(is_weekend(t), hour(t))`.

### 3.4 RollingMedianPeakShift — BURSTY, MEDIUM (`detectors.py:294-495`)

Robust median-of-recent-peaks z-test. Self-adapts on sustained firing.

```
on_threshold      = 50 W      (event-segmenter)
min_event_ticks   = 3
rolling_n         = 5
min_bootstrap_evs = 30
z_threshold       = 3.0
cooldown_s        = 6·3600 s
adapt_K           = 3
adapt_quiet_s     = 24·3600 s
adapt_history_n   = 20
```

**Event-peak segmenter:**

```
prev_above = false; peak = ∅; ticks = 0
on tick v:
    above = v > on_threshold
    if above and not prev_above:    peak ← v;          ticks ← 1
    elif above:                     peak ← max(peak,v); ticks += 1
    elif prev_above and ticks ≥ 3:  emit(peak)
    prev_above ← above
```

**Bootstrap fit** (require ≥ 30 emitted peaks):

```
peaks[1..N]
μ̂   = median(peaks)
MAD = median(|peaks − μ̂|)
σ̂   = max(MAD, |μ̂|·0.01, 1.0)                         # multi-floor
```

**Live update** (on each event close):

```
push peak → recent_peaks (deque maxlen 5)
push peak → adapt_peaks  (deque maxlen 20)
if |recent_peaks| == 5:
    roll_median = median(recent_peaks)
    z = (roll_median − μ̂) / σ̂
    if |z| > z_threshold AND (ts − last_fire) ≥ cooldown_s:
        fire(score=|z|, direction=sgn(z))
        if last_fire is None or (ts − last_fire) > adapt_quiet_s:
            consec_fires = 1
        else:
            consec_fires += 1
        last_fire = ts
        if consec_fires ≥ adapt_K:                      # self-adapt
            μ̂   ← median(adapt_peaks)
            σ̂_new = median(|adapt_peaks − μ̂|)
            σ̂   ← max(σ̂, σ̂_new, |μ̂|·0.01, 1.0)         # MAD-only-grow
            consec_fires = 0
```

The MAD-only-grow floor prevents "over-fire trap": after adapting up
to a high regime, a quieter post-adapt period can't tighten the band.

### 3.5 StateTransition — BINARY, immediate (`detectors.py:733-760`)

Trivial: fires when `feat["trigger"]` is truthy (set by BinaryAdapter
only on `state: 0→1` AND `deterministic_trigger=true`). Emits
`anomaly_type = "water_leak_sustained"` for water capability,
`score = threshold = 1.0`.

---

## §4 Fuser math (`fusion.py`)

Per-sensor chain assembly. **Immediate alerts** (DQG non-`dropout`,
StateTransition) bypass the buffer and are returned on ingest.
**Statistical alerts** (medium-band + DQG `dropout`) buffer in
`pending`; flush on either `gap` or `max_span` violation.

```
on alert a with timestamp t:
    if pending non-empty:
        gap_exceeded  = (t − newest(pending)) > gap
        span_exceeded = (t − oldest(pending)) > max_span
        if gap_exceeded ∨ span_exceeded: flush()
    pending.append(a)

flush:
    if rule.accepts(pending):     # AcceptAll → always true today
        emit group_alerts(pending)
    pending ← []
```

**`group_alerts`** (`fusion.py:17-30`):

```
top         = argmax_a a.score
w0          = min_a (a.window_start ∨ a.timestamp)
w1          = max_a (a.window_end   ∨ a.timestamp)
first_fire  = min_a a.timestamp
fire_ticks  = sorted unique a.timestamp
detectors   = "+".join(sorted unique a.detector)
context     = concat(a.context for a in pending)
score       = top.score
```

| archetype | gap | max_span |
|---|---|---|
| CONTINUOUS | 15 min | 96 h |
| BURSTY / BINARY | 4 h | 96 h |

---

## §5 Classify dispatch (`explain/classify.py`)

Inputs: an `Alert` + bundle-derived `mag` and `temporal` blocks + three
boolean flags pre-computed in `pipeline._write_detections`
(`sustained_oor`, `sustained_dcs`, `time_of_day_pattern`). Output is a
`ClassificationResult{type, confidence, signal_classes}`.

### 5.1 Override chain (return on first match)

```
1. _maybe_dqg_dropout_override        (capability=power, dur ≥ 1 h, dropout)
2. _maybe_dqg_oor_sustained_override  (sustained_oor flag set)
3. _maybe_dqg_spike_override          (extreme_value, large excursion + shwz)
4. _maybe_dqg_oor_override            (capability=power, OOR not sustained)
5. pre-typed short-circuit            (alert.anomaly_type set)
6. time_of_day_pattern flag + duty + direction='+'  → time_of_day
7. sustained_dcs flag    + duty + direction='+'     → level_shift / weekend_anomaly
8. _dispatch(Signals)                 (general path)
```

**Override predicates** (`classify.py:64-248`):

```
DQG dropout → level_shift   iff   duty co-fire
                             OR    |shwz| ≥ 2.5
                             OR    |delta_pct| ≥ 100

DQG sustained_oor → level_shift   (always, given the flag)

DQG extreme_value → spike|dip   iff   capability ∈ {power,voltage,temperature}
                                  AND |delta_pct| ≥ 100
                                  AND |shwz|      ≥ 6
                                  AND delta ≠ 0
                                  (spike if delta>0, dip if <0)

DQG OOR  → level_shift          iff   |shwz| ≥ 3
                                else if |delta_pct| ≥ 3 AND delta ≠ 0
                                                        → frequency_change
```

### 5.2 Signals construction (`explain/signals.py`)

```
detectors = set(alert.detector.split("+"))
classes   = { DETECTOR_CLASSES[d] | d ∈ detectors, d known }
duration  = (window_end − window_start).total_seconds()
direction = first non-None among:
              ctx.direction,                          # cusum/dcs/rmp emit "+"/"-"
              ctx.short_value vs ctx.baseline_value,  # recent_shift derived
              sgn(mag.delta)                          # final fallback
chain_weekday_only = ∀ d in [w0..w1]: d.dayofweek < 5
score   = alert.score        # detector-specific magnitude
bucket_typical = ctx.bucket_typical (DCS-emitted: low/normal/high)
```

`DETECTOR_CLASSES` map (`signals.py:21-47`): coarsens fired detectors
into `{dqg, state, magnitude, duty, peak, rate, calendar}`.

### 5.3 General dispatch (`_dispatch`, `classify.py:381-395`)

```
if classes == {state}:        _classify_state(s)
if classes == {magnitude}:    _classify_continuous(s)
if "duty"   in classes:       _classify_duty(s)
if "peak"   in classes:       _classify_peak(s)
if "rate"   in classes:       "frequency_change"
if "calendar" in classes:     _classify_calendar(s)
else:                         "statistical_anomaly"     # → confidence=low
```

### 5.4 Sub-classifier trees

**`_classify_state`:** water capability → `water_leak_sustained`, else `statistical_anomaly`.

**`_classify_continuous`** (`classify.py:404-436`):

```
if capability == "voltage":
    if dur ≥ 12 h:
        return "calibration_drift" if score ≥ 4 else "month_shift"
    if dur ≥ 1 h:    return "level_shift"
    return "spike" if direction == "+" else "dip"
if capability == "temperature":
    if dur < 2 h or direction == "-":  return "dip"
    return "calibration_drift"
# generic CONT
if dur ≥ 7 d:    return "month_shift"
if dur ≥ 1 h:    return "level_shift"
return "spike" if direction == "+" else "dip"
```

**`_classify_duty`** (`classify.py:439-536`) — the longest tree:

```
has_peak = "peak" in classes
has_rate = "rate" in classes
if has_peak ∧ has_rate:                   return "level_shift"
if has_peak:
    if dur < 24 h:
        if is_weekend:    return "weekend_anomaly"
        if is_off_hours:  return "time_of_day"
        return "time_of_day"
    if is_weekend ∧ dur < 3 d:            return "weekend_anomaly"
    return "level_shift"
if has_rate:                              return "frequency_change"

# duty alone — bucket-aware
bt = bucket_typical or "normal"
if bt == "low" ∧ direction == "+":        # busy when typically quiet
    if is_off_hours:  return "time_of_day"
    if dur < 6 h:     return "time_of_day"
    return "weekend_anomaly"
if bt == "high" ∧ direction == "-":       # quiet when typically busy
    if is_weekend ∧ dur < 3 d:            return "weekend_anomaly"
    return "level_shift"

# bucket weak → fall back to duration / calendar
if direction == "+" ∧ dur < 12 h:
    if is_off_hours:  return "time_of_day"
    if is_weekend:    return "weekend_anomaly"
    return "time_of_day"
if 12 h < dur < 7 d ∧ direction == "+" ∧ chain_weekday_only:
    return "weekend_anomaly"              # target=weekday signature
if is_weekend:                            return "weekend_anomaly"
if is_off_hours:                          return "time_of_day"
if dur ≥ 7 d:                             return "degradation_trajectory"
return "level_shift"
```

**`_classify_peak`:** `rate` co-fire → `trend`, else `dur ≥ 7 d → degradation_trajectory`, else `trend`.

**`_classify_calendar`:** `is_weekend → weekend_anomaly`, `is_off_hours → time_of_day`, else `temporal_pattern`.

### 5.5 Confidence

```
pre-typed (DQG/StateTransition short-circuit) → "high",   signal_classes = []
"statistical_anomaly" fallthrough              → "low"
direction-None spike/dip in _classify_continuous → "low"  (spike-vs-dip arbitrary)
DQG dropout override                           → "low"   (no in-window magnitude)
all other dispatched types                     → "high"
```

---

## §6 LLM-ready prompt

`bundle.explain(alert, events) → dict` (`bundle.py`), then
`build_prompt(bundle) → str` (`prompt.py`).

### 6.1 Bundle dict

```
{
  alert_id:        "{sensor}|{capability}|{w0_iso}",
  sensor, capability, archetype,
  window:          {start, end, duration_sec},
  classification:  {type, class, presentation, confidence, signal_classes},
  magnitude:       {baseline, baseline_source, peak, delta, delta_pct},
  temporal:        {timestamp, weekday, hour, is_weekend, month,
                    time_of_day_bucket,
                    same_hour_weekday_{median,std,n,z}},     # added when peer history ≥ 4
  detectors:       sorted list of detector names,
  detector_context: list of dicts (one per detector, with native diagnostics
                    or synthesized from events when context stripped),
  score:           top-scorer's score
}
```

`presentation`:
```
"infrastructure" if class == "sensor_fault"
"user_visible"   otherwise (including "unknown")
```

### 6.2 Magnitude block (`magnitude.py`)

```
baseline source preference:
    cusum.mu (when cusum context present)
    median(events in [w0 − 2 h, w0))     # prewindow_2h
    median(events in [w0 − 24 h, w0))    # prewindow_24h
    median(events in [w0 − 7 d, w0))     # prewindow_7d
    NaN                                   # prewindow_unavailable

peak  = events[i*].value where i* = argmax_{i ∈ [w0,w1]} |value − baseline|
delta = peak − baseline
delta_pct = 100 · delta / baseline          (NaN if baseline == 0)
```

### 6.3 Same-hour-of-weekday peer baseline (`temporal.py`)

Only computed when ≥ 4 prior events match `(hour=hour(t), dow=dow(t))`:

```
peers       = events with ts < w0 ∧ ts.hour == h ∧ ts.dayofweek == dow
peer_median = median(peers.value)
peer_std    = std(peers.value)               (must be > 0)
shwz        = (peak − peer_median) / peer_std
```

`shwz` is consumed by the DQG-override branches (§5.1).

### 6.4 Rendered prompt skeleton

```
# Anomaly on sensor {sensor} (capability: {cap}, archetype: {archetype})

[**Sensor profile:** {archetype} {capability} — baseline ~{boot_median}
  during typical samples.]                     # only when bootstrap stats present

[⚠ **Infrastructure signal** ...]              # only when presentation=infrastructure

**When:** {start_human} -> {end_human} (duration {humanised}).
[**Long-duration framing:** spans {N} days; covers {M} weekend day(s).]

**Magnitude:** baseline {b:.4g} (source: {src}), peak {p:.4g},
               delta {±d:.4g} ({±pct:.2f}%).
   ↳ OR: **Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** {weekday}, hour {h} ({bucket}), {weekend|weekday},
                       {month}.
[**Same-hour-of-weekday baseline:** peak is {z:+.2f}σ vs. the median of
  {n} prior {weekday} {hour}:00 samples (peer median {m:.4g}).]
[**Rate context:** data_quality_gate has fired {n1h} time(s) in the last
  1 hour and {n24h} time(s) in the last 24 hours on this sensor;
  typical is {x:g} fire(s) per 24h on this sensor.]

[**Signals fired:** {label₁}, {label₂}, … all deviated from bootstrap.]

**Detector evidence:**
- {det₁}: k₁=v₁, k₂=v₂, …
- {det₂}: …

**Detectors fired:** {d₁}, {d₂}, ….

**Score:** {score:.3g}.

**Heuristic classifier:** suggests **{type}** (confidence: {conf}).
  Use as a starting point; refine based on signals above and any
  context outside this bundle.
```

### 6.5 Design principle: signal-rich, verdict-light

The deterministic classifier appears **once**, at the bottom, framed as
advisory. The body is dominated by raw evidence (magnitude, calendar
context, peer-baseline, per-detector dicts) so an LLM consumer can
override the heuristic using context this bundle doesn't have
(household state, cross-sensor correlation, device knowledge). The
`presentation: infrastructure` banner explicitly tells the LLM to
suppress sensor-fault chains from household-facing output unless
correlated with behaviour.

---

## Appendix — quick-reference defaults

| stage | parameter | value |
|---|---|---|
| Adapter | tick | 60 s |
| Adapter | dropout threshold | 5 × `expected_interval_sec` |
| Adapter | bootstrap | 14 d (`--bootstrap-days`) |
| FeatureEngineer | rolling windows | 1 h / 24 h / 7 d |
| DQG | OOR / dropout / batch cooldown | 30 min |
| DQG | clock-drift cooldown / persistence | 5 min / 3 ticks |
| DQG | extreme-value cooldown | 1 h |
| DQG | extreme-value ratio | 3.0 BURSTY / 1.7 CONT |
| DQG | calibration samples | 100 |
| RecentShift | quantile / min-score | 0.999 / 1.1 |
| DCS | window / z / cooldown | 6 h / 3.0 / 2 h |
| DCS | MAD floor | 0.005 |
| RMP | rolling_n / z / cooldown | 5 / 3.0 / 6 h |
| RMP | adapt_K / adapt_quiet / history | 3 / 24 h / 20 |
| Fuser | gap (CONT) | 15 min |
| Fuser | gap (BURSTY/BIN) | 4 h |
| Fuser | max_span | 96 h |
| Pipeline adapt | K consecutive max-span | 3 |
| Pipeline adapt | recent-rows ring | 96 h (CONT) / 144 h (BURSTY/BIN) |
| Classify | DQG OOR shwz threshold | 3.0 |
| Classify | DQG dropout shwz threshold | 2.5 |
| Classify | DQG dropout duration floor | 1 h |
| Classify | DQG spike shwz / delta_pct | 6.0 / 100 |
| Classify | voltage `calibration_drift` score | ≥ 4 |
| Bundle | shwz min peer count | 4 |
| Bundle | baseline pre-window fallback | 2 h → 24 h → 7 d |
