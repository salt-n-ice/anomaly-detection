# Backlog

Items deferred from in-flight iterations. Pick up when the current iter
loop closes or when a related lever becomes the bottleneck.

## Pipeline runtime optimization

**Symptom**: `pipeline.run()` takes ~3 min on hh60d (60d, ~200k events, 5
sensors) and ~10 min on hh120d. Full 6-scenario suite is ~30 min sequential
or ~10 min parallel (gated on the longest scenario).

**Suspected hotspots** (unprofiled):
- `Pipeline.ingest()` per-event overhead — called ~1M times on hh120d
  (events × sensors). Each call walks DQG event checks → adapter →
  engineer → every live detector → fuser.
- `DutyCycleShift.update()` walks its sliding-window deque every tick.
  6h window at 1-min granularity = ~360 entries per call, ~720M deque
  iterations per scenario per sensor.
- `pd.read_csv` + `df.itertuples` is slow; `pyarrow.csv.read_csv` +
  numpy iteration is typically 2–5× faster on this shape of data.

**Suggested approach**:
1. Profile (cProfile or py-spy) on a 60-sec hh60d slice; dump top-20
   callers. Most likely the per-tick deque scans dominate.
2. Cache rolling sums incrementally instead of re-summing the deque
   each tick (keep `(above_s, total_s)` running totals; subtract the
   evicted entry, add the new entry).
3. Swap `pd.read_csv` for `pyarrow.csv.read_csv` if the CSV-read step
   is non-trivial.
4. Vectorize bootstrap fit once per scenario and compute features as
   pandas/numpy batch ops; iterate per-tick only over already-enriched
   arrays. Removes `engineer.enrich` from the per-event hot path.

**Expected payoff**: targeting 2–4× wall-time reduction. Worth it if
iteration cadence is gated on suite runtime.
