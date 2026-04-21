# waterleak_60d — explain cases (run 20260421T182646Z)

## Case waterleak_60d#000  —  TP  —  GT: out_of_range

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Feb 14 2026 09:00 UTC -> Sat Feb 14 2026 09:01 UTC (duration 1.0m).

**Magnitude:** baseline 22.06 (source: prewindow_median), peak -999, delta -1021 (-4627.67%).

**Calendar context:** Saturday, hour 9 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -999 (threshold 0).

---

## Case waterleak_60d#001  —  TP  —  GT: water_leak_sustained

# Anomaly on sensor leak_basement (capability: water)

**When:** Wed Feb 18 2026 03:00 UTC -> Wed Feb 18 2026 03:00 UTC (duration 0s).

**Magnitude:** baseline 0 (source: prewindow_median), peak 1, delta +1 (+nan%).

**Calendar context:** Wednesday, hour 3 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** state_transition.

**Score:** 1 (threshold 0).

---

## Case waterleak_60d#002  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Thu Feb 19 2026 23:55 UTC -> Sat Feb 21 2026 08:05 UTC (duration 1.34d).
**Long-duration framing:** spans 1.3 days; covers 1 weekend day(s).

**Magnitude:** baseline 18.35 (source: prewindow_median), peak 27.01, delta +8.662 (+47.22%).

**Calendar context:** Thursday, hour 23 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, temporal_profile.

**Score:** 59.1 (threshold 0).

---

## Case waterleak_60d#003  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri Feb 20 2026 00:02 UTC -> Sat Feb 21 2026 06:42 UTC (duration 1.28d).
**Long-duration framing:** spans 1.3 days; covers 1 weekend day(s).

**Magnitude:** baseline 80.98 (source: prewindow_median), peak 79.8, delta -1.179 (-1.46%).

**Calendar context:** Friday, hour 0 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 25.6 (threshold 0).

---

## Case waterleak_60d#004  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Feb 21 2026 09:11 UTC -> Tue Feb 24 2026 12:06 UTC (duration 3.12d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 25.2 (source: prewindow_median), peak 20.24, delta -4.953 (-19.66%).

**Calendar context:** Saturday, hour 9 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.5 (threshold 0).

---

## Case waterleak_60d#005  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat Feb 21 2026 06:44 UTC -> Wed Feb 25 2026 06:44 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 79.8 (source: prewindow_median), peak 75.72, delta -4.084 (-5.12%).

**Calendar context:** Saturday, hour 6 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum.

**Score:** 33.8 (threshold 0).

---

## Case waterleak_60d#006  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Feb 24 2026 12:17 UTC -> Sat Feb 28 2026 08:02 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.37 (source: prewindow_median), peak 20.14, delta -7.227 (-26.41%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.8 (threshold 0).

---

## Case waterleak_60d#007  —  TP  —  GT: unusual_occupancy

# Anomaly on sensor leak_basement (capability: water)

**When:** Sun Mar 01 2026 02:00 UTC -> Sun Mar 01 2026 02:00 UTC (duration 0s).

**Magnitude:** baseline 0 (source: prewindow_median), peak 1, delta +1 (+nan%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** state_transition.

**Score:** 1 (threshold 0).

---

## Case waterleak_60d#008  —  TP  —  GT: water_leak_sustained

# Anomaly on sensor leak_basement (capability: water)

**When:** Wed Feb 18 2026 03:00 UTC -> Thu Feb 19 2026 04:00 UTC (duration 1.04d).
**Long-duration framing:** spans 1.0 days; covers 0 weekend day(s).

**Magnitude:** baseline 0 (source: prewindow_median), peak 1, delta +1 (+nan%).

**Calendar context:** Wednesday, hour 3 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca.

**Score:** 5 (threshold 0).

---

## Case waterleak_60d#009  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed Feb 25 2026 06:46 UTC -> Sun Mar 01 2026 06:46 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 75.72 (source: prewindow_median), peak 71.69, delta -4.031 (-5.32%).

**Calendar context:** Wednesday, hour 6 (morning), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum.

**Score:** 40.4 (threshold 0).

---

## Case waterleak_60d#010  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Feb 28 2026 08:52 UTC -> Tue Mar 03 2026 12:05 UTC (duration 3.13d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 25.09 (source: prewindow_median), peak 20.28, delta -4.808 (-19.16%).

**Calendar context:** Saturday, hour 8 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.5 (threshold 0).

---

## Case waterleak_60d#011  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun Mar 01 2026 06:47 UTC -> Thu Mar 05 2026 06:47 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 71.69 (source: prewindow_median), peak 67.71, delta -3.978 (-5.55%).

**Calendar context:** Sunday, hour 6 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum.

**Score:** 24.9 (threshold 0).

---

## Case waterleak_60d#012  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu Mar 05 2026 05:21 UTC -> Thu Mar 05 2026 13:15 UTC (duration 7.90h).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Thursday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 25.4 (threshold 0).

---

## Case waterleak_60d#013  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu Mar 05 2026 13:16 UTC -> Sat Mar 07 2026 00:36 UTC (duration 1.47d).
**Long-duration framing:** spans 1.5 days; covers 1 weekend day(s).

**Magnitude:** baseline 67.24 (source: prewindow_median), peak 65.06, delta -2.18 (-3.24%).

**Calendar context:** Thursday, hour 13 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 27.6 (threshold 0).

---

## Case waterleak_60d#014  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Mar 03 2026 12:16 UTC -> Sat Mar 07 2026 08:01 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.31 (source: prewindow_median), peak 20.21, delta -7.101 (-26.00%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.5 (threshold 0).

---

## Case waterleak_60d#015  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat Mar 07 2026 00:37 UTC -> Sat Mar 07 2026 18:30 UTC (duration 17.88h).

**Magnitude:** baseline 65.06 (source: prewindow_median), peak 63.93, delta -1.13 (-1.74%).

**Calendar context:** Saturday, hour 0 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 28.7 (threshold 0).

---

## Case waterleak_60d#016  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat Mar 07 2026 18:31 UTC -> Mon Mar 09 2026 12:54 UTC (duration 1.77d).
**Long-duration framing:** spans 1.8 days; covers 2 weekend day(s).

**Magnitude:** baseline 63.93 (source: prewindow_median), peak 61.39, delta -2.545 (-3.98%).

**Calendar context:** Saturday, hour 18 (evening), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 31.2 (threshold 0).

---

## Case waterleak_60d#017  —  TP  —  GT: stuck_at

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Mar 07 2026 09:07 UTC -> Tue Mar 10 2026 12:13 UTC (duration 3.13d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 25.02 (source: prewindow_median), peak 20.35, delta -4.671 (-18.67%).

**Calendar context:** Saturday, hour 9 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.4 (threshold 0).

---

## Case waterleak_60d#018  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon Mar 09 2026 12:55 UTC -> Wed Mar 11 2026 01:12 UTC (duration 1.51d).
**Long-duration framing:** spans 1.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 61.39 (source: prewindow_median), peak 59.31, delta -2.082 (-3.39%).

**Calendar context:** Monday, hour 12 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 33.4 (threshold 0).

---

## Case waterleak_60d#019  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed Mar 11 2026 01:13 UTC -> Thu Mar 12 2026 01:12 UTC (duration 23.98h).

**Magnitude:** baseline 59.31 (source: prewindow_median), peak 57.89, delta -1.414 (-2.38%).

**Calendar context:** Wednesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 34.8 (threshold 0).

---

## Case waterleak_60d#020  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu Mar 12 2026 01:13 UTC -> Fri Mar 13 2026 12:49 UTC (duration 1.48d).
**Long-duration framing:** spans 1.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 57.89 (source: prewindow_median), peak 55.8, delta -2.096 (-3.62%).

**Calendar context:** Thursday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 36.9 (threshold 0).

---

## Case waterleak_60d#021  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Mar 10 2026 12:23 UTC -> Sat Mar 14 2026 08:00 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.29 (source: prewindow_median), peak 20.41, delta -6.879 (-25.21%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.5 (threshold 0).

---

## Case waterleak_60d#022  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri Mar 13 2026 12:50 UTC -> Sun Mar 15 2026 20:43 UTC (duration 2.33d).
**Long-duration framing:** spans 2.3 days; covers 2 weekend day(s).

**Magnitude:** baseline 55.8 (source: prewindow_median), peak 58.05, delta +2.258 (+4.05%).

**Calendar context:** Friday, hour 12 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 38.6 (threshold 0).

---

## Case waterleak_60d#023  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Mar 14 2026 08:51 UTC -> Tue Mar 17 2026 12:10 UTC (duration 3.14d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 24.96 (source: prewindow_median), peak 20.38, delta -4.576 (-18.34%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.5 (threshold 0).

---

## Case waterleak_60d#024  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun Mar 15 2026 20:44 UTC -> Thu Mar 19 2026 20:44 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 1 weekend day(s).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Sunday, hour 20 (evening), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum.

**Score:** 39.5 (threshold 0).

---

## Case waterleak_60d#025  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Mar 17 2026 12:20 UTC -> Fri Mar 20 2026 01:20 UTC (duration 2.54d).
**Long-duration framing:** spans 2.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 27.27 (source: prewindow_median), peak 20.7, delta -6.567 (-24.08%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.6 (threshold 0).

---

## Case waterleak_60d#026  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 01:20 UTC -> Fri Mar 20 2026 03:50 UTC (duration 2.50h).

**Magnitude:** baseline 21.07 (source: prewindow_median), peak 22, delta +0.9231 (+4.38%).

**Calendar context:** Friday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 6.6e+03 (threshold 0).

---

## Case waterleak_60d#027  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 03:50 UTC -> Fri Mar 20 2026 05:10 UTC (duration 1.33h).

**Magnitude:** baseline 21.75 (source: prewindow_median), peak 23.1, delta +1.358 (+6.24%).

**Calendar context:** Friday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 3.6e+03 (threshold 0).

---

## Case waterleak_60d#028  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 05:10 UTC -> Fri Mar 20 2026 08:20 UTC (duration 3.17h).

**Magnitude:** baseline 22 (source: prewindow_median), peak 25.36, delta +3.366 (+15.30%).

**Calendar context:** Friday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 1.02e+04 (threshold 0).

---

## Case waterleak_60d#029  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 08:20 UTC -> Fri Mar 20 2026 14:40 UTC (duration 6.33h).

**Magnitude:** baseline 25.26 (source: prewindow_median), peak 26.22, delta +0.9671 (+3.83%).

**Calendar context:** Friday, hour 8 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 2.28e+04 (threshold 0).

---

## Case waterleak_60d#030  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 14:40 UTC -> Fri Mar 20 2026 16:30 UTC (duration 1.83h).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Friday, hour 14 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 6.6e+03 (threshold 0).

---

## Case waterleak_60d#031  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 16:30 UTC -> Fri Mar 20 2026 18:40 UTC (duration 2.17h).

**Magnitude:** baseline 26.22 (source: prewindow_median), peak 23.27, delta -2.948 (-11.24%).

**Calendar context:** Friday, hour 16 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 7.2e+03 (threshold 0).

---

## Case waterleak_60d#032  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 18:40 UTC -> Fri Mar 20 2026 22:20 UTC (duration 3.67h).

**Magnitude:** baseline 23.59 (source: prewindow_median), peak 21.09, delta -2.498 (-10.59%).

**Calendar context:** Friday, hour 18 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 1.02e+04 (threshold 0).

---

## Case waterleak_60d#033  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 22:20 UTC -> Sat Mar 21 2026 08:01 UTC (duration 9.68h).

**Magnitude:** baseline 21.38 (source: prewindow_median), peak 25.11, delta +3.732 (+17.46%).

**Calendar context:** Friday, hour 22 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 6e+03 (threshold 0).

---

## Case waterleak_60d#034  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu Mar 19 2026 20:45 UTC -> Mon Mar 23 2026 20:45 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Thursday, hour 20 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum.

**Score:** 43.6 (threshold 0).

---

## Case waterleak_60d#035  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Mar 21 2026 08:35 UTC -> Tue Mar 24 2026 12:08 UTC (duration 3.15d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 24.69 (source: prewindow_median), peak 20.36, delta -4.333 (-17.54%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.3 (threshold 0).

---

## Case waterleak_60d#036  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon Mar 23 2026 20:46 UTC -> Fri Mar 27 2026 20:46 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 0 weekend day(s).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Monday, hour 20 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 47.4 (threshold 0).

---

## Case waterleak_60d#037  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri Mar 27 2026 18:42 UTC -> Sat Mar 28 2026 01:56 UTC (duration 7.23h).

**Magnitude:** baseline 45.22 (source: prewindow_median), peak 45.14, delta -0.08024 (-0.18%).

**Calendar context:** Friday, hour 18 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 47.6 (threshold 0).

---

## Case waterleak_60d#038  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Mar 24 2026 12:19 UTC -> Sat Mar 28 2026 08:06 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.11 (source: prewindow_median), peak 20.29, delta -6.818 (-25.15%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.7 (threshold 0).

---

## Case waterleak_60d#039  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Mar 28 2026 08:57 UTC -> Tue Mar 31 2026 12:10 UTC (duration 3.13d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 24.81 (source: prewindow_median), peak 20.21, delta -4.6 (-18.54%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.8 (threshold 0).

---

## Case waterleak_60d#040  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat Mar 28 2026 01:57 UTC -> Wed Apr 01 2026 01:57 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 45.14 (source: prewindow_median), peak 40.97, delta -4.165 (-9.23%).

**Calendar context:** Saturday, hour 1 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum.

**Score:** 51.7 (threshold 0).

---

## Case waterleak_60d#041  —  TP  —  GT: unusual_occupancy

# Anomaly on sensor leak_basement (capability: water)

**When:** Sun Mar 01 2026 02:00 UTC -> Mon Mar 02 2026 02:10 UTC (duration 1.01d).
**Long-duration framing:** spans 1.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 0 (source: prewindow_median), peak 1, delta +1 (+nan%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca.

**Score:** 5 (threshold 0).

---

## Case waterleak_60d#042  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Mar 31 2026 12:20 UTC -> Wed Apr 01 2026 23:50 UTC (duration 1.48d).
**Long-duration framing:** spans 1.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 27.31 (source: prewindow_median), peak 21.28, delta -6.035 (-22.10%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.8 (threshold 0).

---
