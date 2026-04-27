# Backlog

Items deferred from in-flight iterations. Pick up when the current iter
loop closes or when a related lever becomes the bottleneck.

## Resolved

- **DCS update incremental running sums** (2026-04-27). cProfile showed
  `DutyCycleShift.update` at 65% of hh60d runtime (155s of 237s) —
  every tick re-walked the 6h window deque to recompute duty. Replaced
  with O(1) running-sum maintenance: append adds the new (prev → cur)
  interval, evict subtracts the (old → next-after-old) interval. hh60d
  solo 174s → 37s (5×); parallel 6-scenario suite ~600s → 96s (6×).
  Bit-exact metric parity verified across all 6 scenarios.

## Open

- **Profile remaining hotspots.** Post-DCS-fix the suite is ~96s wall
  parallel; if iter cadence demands faster, profile again. Likely
  next-largest items: `adapter.emit_ready` (was 36s of 237s pre-fix),
  `features.enrich` (20s pre-fix), `pd.read_csv` (untimed but candidate
  for `pyarrow.csv.read_csv` 2–5× swap).
- **Vectorize bootstrap fit.** `_compute_bootstrap_windows` is 2.5s per
  sensor (one-shot at fit). Could batch-vectorize via pandas rolling
  ops if it becomes a budget item.
