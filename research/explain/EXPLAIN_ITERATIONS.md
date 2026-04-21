# Explain-quality iterations log

Template (append one block per iteration):

```
## iter-NNN — <one-line hypothesis> — <ACCEPT|REJECT|PARTIAL|NULL>

**Hypothesis:** <full statement, 1-2 sentences>
**Targets:** <dims / scenarios expected to move>
**Change:** <file + 1-line diff summary>

**Baseline before:**
- `aggregate.all.mean_tp_mean` = X.XX
- `aggregate.all.mean_fp_mean` = X.XX
- worst_tp_mean scenario = <name> X.XX

**After:**
- `aggregate.all.mean_tp_mean` = X.XX (±X.XX)
- `aggregate.all.mean_fp_mean` = X.XX (±X.XX)
- per-scenario regressions: <list or "none">

**Verdict:** <ACCEPT|REJECT|PARTIAL|NULL> because <reason>.

**Next:** <one-line next hypothesis or "revisit backlog">
```
