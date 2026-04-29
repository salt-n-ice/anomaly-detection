# Eval Metrics — household_120d (iter 21, commit `134c916`)

n_labels = 27.

| Metric | Value | One-liner |
|---|---:|---|
| incR | 1.000 | Every GT label was caught. |
| **evt_F1** ← headline | 0.792 | Per-fire precision/recall balance — ~79 % effective. |
| fpur | 0.993 | 99 % of fires sit inside a GT label; almost no false alarms. |
| tyAcc | 0.811 | When a fire is in-GT, type is named correctly ~81 % of the time. |
| on_time_rate | 0.625 | ~63 % of correctly-typed alerts arrived inside MET budget. |
| lat_frac_p95 | 0.465 | Worst case, silent through ~47 % of the label before first fire. |
| uvfp/d | 0.37 | ≈ 1 user-visible FP every ~3 days. |
