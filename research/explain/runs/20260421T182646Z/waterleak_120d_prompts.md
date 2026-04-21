# waterleak_120d — explain cases (run 20260421T182646Z)

## Case waterleak_120d#000  —  TP  —  GT: out_of_range

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Feb 14 2026 09:00 UTC -> Sat Feb 14 2026 09:01 UTC (duration 1.0m).

**Magnitude:** baseline 22.06 (source: prewindow_median), peak -999, delta -1021 (-4627.67%).

**Calendar context:** Saturday, hour 9 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -999 (threshold 0).

---

## Case waterleak_120d#001  —  TP  —  GT: water_leak_sustained

# Anomaly on sensor leak_basement (capability: water)

**When:** Wed Feb 18 2026 03:00 UTC -> Wed Feb 18 2026 03:00 UTC (duration 0s).

**Magnitude:** baseline 0 (source: prewindow_median), peak 1, delta +1 (+nan%).

**Calendar context:** Wednesday, hour 3 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** state_transition.

**Score:** 1 (threshold 0).

---

## Case waterleak_120d#002  —  TP  —  GT: calibration_drift

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

## Case waterleak_120d#003  —  FP  —  GT: (none)

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

## Case waterleak_120d#004  —  TP  —  GT: calibration_drift

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

## Case waterleak_120d#005  —  FP  —  GT: (none)

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

## Case waterleak_120d#006  —  TP  —  GT: calibration_drift

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

## Case waterleak_120d#007  —  TP  —  GT: unusual_occupancy

# Anomaly on sensor leak_basement (capability: water)

**When:** Sun Mar 01 2026 02:00 UTC -> Sun Mar 01 2026 02:00 UTC (duration 0s).

**Magnitude:** baseline 0 (source: prewindow_median), peak 1, delta +1 (+nan%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** state_transition.

**Score:** 1 (threshold 0).

---

## Case waterleak_120d#008  —  TP  —  GT: water_leak_sustained

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

## Case waterleak_120d#009  —  FP  —  GT: (none)

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

## Case waterleak_120d#010  —  FP  —  GT: (none)

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

## Case waterleak_120d#011  —  TP  —  GT: trend

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

## Case waterleak_120d#012  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu Mar 05 2026 05:21 UTC -> Thu Mar 05 2026 13:15 UTC (duration 7.90h).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Thursday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 25.4 (threshold 0).

---

## Case waterleak_120d#013  —  TP  —  GT: trend

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

## Case waterleak_120d#014  —  FP  —  GT: (none)

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

## Case waterleak_120d#015  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat Mar 07 2026 00:37 UTC -> Sat Mar 07 2026 18:30 UTC (duration 17.88h).

**Magnitude:** baseline 65.06 (source: prewindow_median), peak 63.93, delta -1.13 (-1.74%).

**Calendar context:** Saturday, hour 0 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 28.7 (threshold 0).

---

## Case waterleak_120d#016  —  TP  —  GT: trend

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

## Case waterleak_120d#017  —  TP  —  GT: stuck_at

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

## Case waterleak_120d#018  —  TP  —  GT: trend

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

## Case waterleak_120d#019  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed Mar 11 2026 01:13 UTC -> Thu Mar 12 2026 01:12 UTC (duration 23.98h).

**Magnitude:** baseline 59.31 (source: prewindow_median), peak 57.89, delta -1.414 (-2.38%).

**Calendar context:** Wednesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 34.8 (threshold 0).

---

## Case waterleak_120d#020  —  TP  —  GT: trend

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

## Case waterleak_120d#021  —  FP  —  GT: (none)

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

## Case waterleak_120d#022  —  TP  —  GT: trend

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

## Case waterleak_120d#023  —  FP  —  GT: (none)

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

## Case waterleak_120d#024  —  FP  —  GT: (none)

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

## Case waterleak_120d#025  —  TP  —  GT: reporting_rate_change

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

## Case waterleak_120d#026  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 01:20 UTC -> Fri Mar 20 2026 03:50 UTC (duration 2.50h).

**Magnitude:** baseline 21.07 (source: prewindow_median), peak 22, delta +0.9231 (+4.38%).

**Calendar context:** Friday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 6.6e+03 (threshold 0).

---

## Case waterleak_120d#027  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 03:50 UTC -> Fri Mar 20 2026 05:10 UTC (duration 1.33h).

**Magnitude:** baseline 21.75 (source: prewindow_median), peak 23.1, delta +1.358 (+6.24%).

**Calendar context:** Friday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 3.6e+03 (threshold 0).

---

## Case waterleak_120d#028  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 05:10 UTC -> Fri Mar 20 2026 08:20 UTC (duration 3.17h).

**Magnitude:** baseline 22 (source: prewindow_median), peak 25.36, delta +3.366 (+15.30%).

**Calendar context:** Friday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 1.02e+04 (threshold 0).

---

## Case waterleak_120d#029  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 08:20 UTC -> Fri Mar 20 2026 14:40 UTC (duration 6.33h).

**Magnitude:** baseline 25.26 (source: prewindow_median), peak 26.22, delta +0.9671 (+3.83%).

**Calendar context:** Friday, hour 8 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 2.28e+04 (threshold 0).

---

## Case waterleak_120d#030  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 14:40 UTC -> Fri Mar 20 2026 16:30 UTC (duration 1.83h).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Friday, hour 14 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 6.6e+03 (threshold 0).

---

## Case waterleak_120d#031  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 16:30 UTC -> Fri Mar 20 2026 18:40 UTC (duration 2.17h).

**Magnitude:** baseline 26.22 (source: prewindow_median), peak 23.27, delta -2.948 (-11.24%).

**Calendar context:** Friday, hour 16 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 7.2e+03 (threshold 0).

---

## Case waterleak_120d#032  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 18:40 UTC -> Fri Mar 20 2026 22:20 UTC (duration 3.67h).

**Magnitude:** baseline 23.59 (source: prewindow_median), peak 21.09, delta -2.498 (-10.59%).

**Calendar context:** Friday, hour 18 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 1.02e+04 (threshold 0).

---

## Case waterleak_120d#033  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 22:20 UTC -> Sat Mar 21 2026 08:01 UTC (duration 9.68h).

**Magnitude:** baseline 21.38 (source: prewindow_median), peak 25.11, delta +3.732 (+17.46%).

**Calendar context:** Friday, hour 22 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 6e+03 (threshold 0).

---

## Case waterleak_120d#034  —  FP  —  GT: (none)

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

## Case waterleak_120d#035  —  FP  —  GT: (none)

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

## Case waterleak_120d#036  —  FP  —  GT: (none)

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

## Case waterleak_120d#037  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri Mar 27 2026 18:42 UTC -> Sat Mar 28 2026 01:56 UTC (duration 7.23h).

**Magnitude:** baseline 45.22 (source: prewindow_median), peak 45.14, delta -0.08024 (-0.18%).

**Calendar context:** Friday, hour 18 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 47.6 (threshold 0).

---

## Case waterleak_120d#038  —  FP  —  GT: (none)

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

## Case waterleak_120d#039  —  FP  —  GT: (none)

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

## Case waterleak_120d#040  —  FP  —  GT: (none)

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

## Case waterleak_120d#041  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Mar 31 2026 12:20 UTC -> Sat Apr 04 2026 08:03 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.31 (source: prewindow_median), peak 20.43, delta -6.881 (-25.19%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.8 (threshold 0).

---

## Case waterleak_120d#042  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon Apr 06 2026 01:16 UTC -> Tue Apr 07 2026 09:53 UTC (duration 1.36d).
**Long-duration framing:** spans 1.4 days; covers 0 weekend day(s).

**Magnitude:** baseline 36.07 (source: prewindow_median), peak 34.85, delta -1.218 (-3.38%).

**Calendar context:** Monday, hour 1 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 58 (threshold 0).

---

## Case waterleak_120d#043  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Apr 04 2026 08:53 UTC -> Tue Apr 07 2026 12:14 UTC (duration 3.14d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 24.92 (source: prewindow_median), peak 20.34, delta -4.583 (-18.39%).

**Calendar context:** Saturday, hour 8 (morning), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.4 (threshold 0).

---

## Case waterleak_120d#044  —  TP  —  GT: spike

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Apr 07 2026 12:24 UTC -> Sat Apr 11 2026 08:00 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.42 (source: prewindow_median), peak 45.71, delta +18.29 (+66.68%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 180 (threshold 0).

---

## Case waterleak_120d#045  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Apr 11 2026 08:50 UTC -> Tue Apr 14 2026 12:07 UTC (duration 3.14d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 24.89 (source: prewindow_median), peak 20.37, delta -4.519 (-18.16%).

**Calendar context:** Saturday, hour 8 (morning), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.5 (threshold 0).

---

## Case waterleak_120d#046  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon Apr 13 2026 14:51 UTC -> Wed Apr 15 2026 16:44 UTC (duration 2.08d).
**Long-duration framing:** spans 2.1 days; covers 0 weekend day(s).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Monday, hour 14 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 66.3 (threshold 0).

---

## Case waterleak_120d#047  —  TP  —  GT: dip

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Apr 14 2026 12:18 UTC -> Sat Apr 18 2026 08:03 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.31 (source: prewindow_median), peak 12.56, delta -14.74 (-54.00%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.7 (threshold 0).

---

## Case waterleak_120d#048  —  TP  —  GT: water_leak_sustained

# Anomaly on sensor leak_basement (capability: water)

**When:** Mon Apr 20 2026 02:00 UTC -> Mon Apr 20 2026 02:00 UTC (duration 0s).

**Magnitude:** baseline 0 (source: prewindow_median), peak 1, delta +1 (+nan%).

**Calendar context:** Monday, hour 2 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** state_transition.

**Score:** 1 (threshold 0).

---

## Case waterleak_120d#049  —  TP  —  GT: unusual_occupancy

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

## Case waterleak_120d#050  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Apr 18 2026 08:54 UTC -> Tue Apr 21 2026 12:10 UTC (duration 3.14d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 24.91 (source: prewindow_median), peak 20.35, delta -4.561 (-18.31%).

**Calendar context:** Saturday, hour 8 (morning), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.8 (threshold 0).

---

## Case waterleak_120d#051  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Apr 21 2026 12:21 UTC -> Sat Apr 25 2026 08:05 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.27 (source: prewindow_median), peak 20.31, delta -6.957 (-25.51%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.6 (threshold 0).

---

## Case waterleak_120d#052  —  TP  —  GT: water_leak_sustained

# Anomaly on sensor leak_basement (capability: water)

**When:** Mon Apr 20 2026 02:00 UTC -> Tue Apr 21 2026 04:00 UTC (duration 1.08d).
**Long-duration framing:** spans 1.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 0 (source: prewindow_median), peak 1, delta +1 (+nan%).

**Calendar context:** Monday, hour 2 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca.

**Score:** 2.01 (threshold 0).

---

## Case waterleak_120d#053  —  TP  —  GT: noise_burst

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Apr 25 2026 09:14 UTC -> Tue Apr 28 2026 12:10 UTC (duration 3.12d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 25.59 (source: prewindow_median), peak 31.53, delta +5.936 (+23.19%).

**Calendar context:** Saturday, hour 9 (morning), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.4 (threshold 0).

---

## Case waterleak_120d#054  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Apr 28 2026 12:20 UTC -> Fri May 01 2026 23:57 UTC (duration 3.48d).
**Long-duration framing:** spans 3.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 27.27 (source: prewindow_median), peak 20.57, delta -6.697 (-24.56%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.8 (threshold 0).

---

## Case waterleak_120d#055  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Mon May 04 2026 21:00 UTC -> Mon May 04 2026 21:08 UTC (duration 8.0m).

**Magnitude:** baseline 20.17 (source: prewindow_median), peak 19.67, delta -0.4924 (-2.44%).

**Calendar context:** Monday, hour 21 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 6.91 (threshold 0).

---

## Case waterleak_120d#056  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 05 2026 20:06 UTC -> Tue May 05 2026 20:14 UTC (duration 8.0m).

**Magnitude:** baseline 21.24 (source: prewindow_median), peak 20.81, delta -0.4305 (-2.03%).

**Calendar context:** Tuesday, hour 20 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 5.14 (threshold 0).

---

## Case waterleak_120d#057  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Wed May 06 2026 21:00 UTC -> Wed May 06 2026 21:35 UTC (duration 35.0m).

**Magnitude:** baseline 20.49 (source: prewindow_median), peak 19.71, delta -0.7777 (-3.80%).

**Calendar context:** Wednesday, hour 21 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 6.23 (threshold 0).

---

## Case waterleak_120d#058  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Wed May 06 2026 22:00 UTC -> Wed May 06 2026 22:06 UTC (duration 6.0m).

**Magnitude:** baseline 19.87 (source: prewindow_median), peak 19.51, delta -0.3562 (-1.79%).

**Calendar context:** Wednesday, hour 22 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 5.38 (threshold 0).

---

## Case waterleak_120d#059  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 03 2026 17:32 UTC -> Thu May 07 2026 17:32 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 1 weekend day(s).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Sunday, hour 17 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 88.3 (threshold 0).

---

## Case waterleak_120d#060  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Thu May 07 2026 18:00 UTC -> Thu May 07 2026 18:06 UTC (duration 6.0m).

**Magnitude:** baseline 22.64 (source: prewindow_median), peak 21.91, delta -0.7248 (-3.20%).

**Calendar context:** Thursday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 5.13 (threshold 0).

---

## Case waterleak_120d#061  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Thu May 07 2026 21:00 UTC -> Thu May 07 2026 21:05 UTC (duration 5.0m).

**Magnitude:** baseline 20.26 (source: prewindow_median), peak 19.74, delta -0.5206 (-2.57%).

**Calendar context:** Thursday, hour 21 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 5.53 (threshold 0).

---

## Case waterleak_120d#062  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Thu May 07 2026 22:00 UTC -> Thu May 07 2026 22:09 UTC (duration 9.0m).

**Magnitude:** baseline 19.57 (source: prewindow_median), peak 19.18, delta -0.3918 (-2.00%).

**Calendar context:** Thursday, hour 22 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 5.81 (threshold 0).

---

## Case waterleak_120d#063  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri May 08 2026 21:00 UTC -> Fri May 08 2026 21:13 UTC (duration 13.0m).

**Magnitude:** baseline 19.83 (source: prewindow_median), peak 19.13, delta -0.6938 (-3.50%).

**Calendar context:** Friday, hour 21 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 5.63 (threshold 0).

---

## Case waterleak_120d#064  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 15 2026 06:00 UTC -> Fri May 15 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Friday, hour 6 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.13 (threshold 0).

---

## Case waterleak_120d#065  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 15 2026 12:00 UTC -> Fri May 15 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Friday, hour 12 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.259 (threshold 0).

---

## Case waterleak_120d#066  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 15 2026 18:00 UTC -> Fri May 15 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Friday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.389 (threshold 0).

---

## Case waterleak_120d#067  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 11 2026 17:34 UTC -> Fri May 15 2026 17:34 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 0 weekend day(s).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Monday, hour 17 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 93 (threshold 0).

---

## Case waterleak_120d#068  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 16 2026 00:00 UTC -> Sat May 16 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Saturday, hour 0 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.518 (threshold 0).

---

## Case waterleak_120d#069  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 16 2026 06:00 UTC -> Sat May 16 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Saturday, hour 6 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.648 (threshold 0).

---

## Case waterleak_120d#070  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 16 2026 12:00 UTC -> Sat May 16 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Saturday, hour 12 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.778 (threshold 0).

---

## Case waterleak_120d#071  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 16 2026 18:00 UTC -> Sat May 16 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Saturday, hour 18 (evening), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.907 (threshold 0).

---

## Case waterleak_120d#072  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 17 2026 00:00 UTC -> Sun May 17 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Sunday, hour 0 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.04 (threshold 0).

---

## Case waterleak_120d#073  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 17 2026 06:00 UTC -> Sun May 17 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Sunday, hour 6 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.17 (threshold 0).

---

## Case waterleak_120d#074  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 17 2026 12:00 UTC -> Sun May 17 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Sunday, hour 12 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.3 (threshold 0).

---

## Case waterleak_120d#075  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 17 2026 18:00 UTC -> Sun May 17 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Sunday, hour 18 (evening), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.43 (threshold 0).

---

## Case waterleak_120d#076  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 18 2026 00:00 UTC -> Mon May 18 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Monday, hour 0 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.56 (threshold 0).

---

## Case waterleak_120d#077  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 18 2026 06:00 UTC -> Mon May 18 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Monday, hour 6 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.68 (threshold 0).

---

## Case waterleak_120d#078  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 18 2026 12:00 UTC -> Mon May 18 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Monday, hour 12 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.81 (threshold 0).

---

## Case waterleak_120d#079  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 18 2026 18:00 UTC -> Mon May 18 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Monday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.94 (threshold 0).

---

## Case waterleak_120d#080  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 19 2026 00:00 UTC -> Tue May 19 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Tuesday, hour 0 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.07 (threshold 0).

---

## Case waterleak_120d#081  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 19 2026 06:00 UTC -> Tue May 19 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Tuesday, hour 6 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.2 (threshold 0).

---

## Case waterleak_120d#082  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 19 2026 12:00 UTC -> Tue May 19 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.33 (threshold 0).

---

## Case waterleak_120d#083  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 19 2026 18:00 UTC -> Tue May 19 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Tuesday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.46 (threshold 0).

---

## Case waterleak_120d#084  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 20 2026 00:00 UTC -> Wed May 20 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Wednesday, hour 0 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.59 (threshold 0).

---

## Case waterleak_120d#085  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 20 2026 06:00 UTC -> Wed May 20 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Wednesday, hour 6 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.72 (threshold 0).

---

## Case waterleak_120d#086  —  TP  —  GT: dropout

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Wed May 20 2026 02:50 UTC -> Wed May 20 2026 05:00 UTC (duration 2.17h).

**Magnitude:** baseline 19.3 (source: prewindow_median), peak 21.51, delta +2.204 (+11.42%).

**Calendar context:** Wednesday, hour 2 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 7.8e+03 (threshold 0).

---

## Case waterleak_120d#087  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 20 2026 12:00 UTC -> Wed May 20 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Wednesday, hour 12 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.85 (threshold 0).

---

## Case waterleak_120d#088  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 20 2026 18:00 UTC -> Wed May 20 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Wednesday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.98 (threshold 0).

---

## Case waterleak_120d#089  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 21 2026 00:00 UTC -> Thu May 21 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Thursday, hour 0 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -3.11 (threshold 0).

---

## Case waterleak_120d#090  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 21 2026 06:00 UTC -> Thu May 21 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Thursday, hour 6 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -3.24 (threshold 0).

---

## Case waterleak_120d#091  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 21 2026 12:00 UTC -> Thu May 21 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Thursday, hour 12 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -3.37 (threshold 0).

---

## Case waterleak_120d#092  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 21 2026 18:00 UTC -> Thu May 21 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Thursday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -3.5 (threshold 0).

---

## Case waterleak_120d#093  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 22 2026 00:00 UTC -> Fri May 22 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Friday, hour 0 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -3.63 (threshold 0).

---

## Case waterleak_120d#094  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 22 2026 06:00 UTC -> Fri May 22 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Friday, hour 6 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -3.76 (threshold 0).

---

## Case waterleak_120d#095  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 22 2026 12:00 UTC -> Fri May 22 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Friday, hour 12 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -3.89 (threshold 0).

---

## Case waterleak_120d#096  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 22 2026 18:00 UTC -> Fri May 22 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Friday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -4.02 (threshold 0).

---

## Case waterleak_120d#097  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 23 2026 00:00 UTC -> Sat May 23 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Saturday, hour 0 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -4.15 (threshold 0).

---

## Case waterleak_120d#098  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 23 2026 06:00 UTC -> Sat May 23 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Saturday, hour 6 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -4.28 (threshold 0).

---

## Case waterleak_120d#099  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 23 2026 12:00 UTC -> Sat May 23 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Saturday, hour 12 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -4.41 (threshold 0).

---

## Case waterleak_120d#100  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 23 2026 18:00 UTC -> Sat May 23 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Saturday, hour 18 (evening), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -4.54 (threshold 0).

---

## Case waterleak_120d#101  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 24 2026 00:00 UTC -> Sun May 24 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Sunday, hour 0 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -4.67 (threshold 0).

---

## Case waterleak_120d#102  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 24 2026 06:00 UTC -> Sun May 24 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Sunday, hour 6 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -4.8 (threshold 0).

---

## Case waterleak_120d#103  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 24 2026 12:00 UTC -> Sun May 24 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Sunday, hour 12 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -4.92 (threshold 0).

---

## Case waterleak_120d#104  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 24 2026 18:00 UTC -> Sun May 24 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Sunday, hour 18 (evening), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -5.05 (threshold 0).

---

## Case waterleak_120d#105  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 25 2026 00:00 UTC -> Mon May 25 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Monday, hour 0 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -5.18 (threshold 0).

---

## Case waterleak_120d#106  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 25 2026 06:00 UTC -> Mon May 25 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Monday, hour 6 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -5.31 (threshold 0).

---

## Case waterleak_120d#107  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 25 2026 12:00 UTC -> Mon May 25 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Monday, hour 12 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -5.44 (threshold 0).

---

## Case waterleak_120d#108  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 25 2026 18:00 UTC -> Mon May 25 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Monday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -5.57 (threshold 0).

---

## Case waterleak_120d#109  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 26 2026 00:00 UTC -> Tue May 26 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Tuesday, hour 0 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -5.7 (threshold 0).

---

## Case waterleak_120d#110  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Mon May 25 2026 23:50 UTC -> Tue May 26 2026 01:20 UTC (duration 1.50h).

**Magnitude:** baseline 18.67 (source: prewindow_median), peak 18.42, delta -0.2535 (-1.36%).

**Calendar context:** Monday, hour 23 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 5.4e+03 (threshold 0).

---

## Case waterleak_120d#111  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 02:00 UTC -> Tue May 26 2026 04:50 UTC (duration 2.83h).

**Magnitude:** baseline 19.13 (source: prewindow_median), peak 21.14, delta +2.01 (+10.50%).

**Calendar context:** Tuesday, hour 2 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 1.02e+04 (threshold 0).

---

## Case waterleak_120d#112  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 26 2026 06:00 UTC -> Tue May 26 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Tuesday, hour 6 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -5.83 (threshold 0).

---

## Case waterleak_120d#113  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 04:50 UTC -> Tue May 26 2026 05:50 UTC (duration 1.00h).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Tuesday, hour 4 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 3.6e+03 (threshold 0).

---

## Case waterleak_120d#114  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 07:10 UTC -> Tue May 26 2026 09:40 UTC (duration 2.50h).

**Magnitude:** baseline 21.58 (source: prewindow_median), peak 24.44, delta +2.862 (+13.26%).

**Calendar context:** Tuesday, hour 7 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate.

**Score:** 8.4e+03 (threshold 0).

---

## Case waterleak_120d#115  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 09:40 UTC -> Tue May 26 2026 11:10 UTC (duration 1.50h).

**Magnitude:** baseline 24.03 (source: prewindow_median), peak 24.82, delta +0.7961 (+3.31%).

**Calendar context:** Tuesday, hour 9 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 5.4e+03 (threshold 0).

---

## Case waterleak_120d#116  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 26 2026 12:00 UTC -> Tue May 26 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -5.96 (threshold 0).

---

## Case waterleak_120d#117  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 11:40 UTC -> Tue May 26 2026 14:40 UTC (duration 3.00h).

**Magnitude:** baseline 24.82 (source: prewindow_median), peak 23.84, delta -0.9821 (-3.96%).

**Calendar context:** Tuesday, hour 11 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 1.08e+04 (threshold 0).

---

## Case waterleak_120d#118  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 14:40 UTC -> Tue May 26 2026 15:50 UTC (duration 1.17h).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Tuesday, hour 14 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 4.2e+03 (threshold 0).

---

## Case waterleak_120d#119  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 26 2026 18:00 UTC -> Tue May 26 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Tuesday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -6.09 (threshold 0).

---

## Case waterleak_120d#120  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 15:50 UTC -> Tue May 26 2026 17:00 UTC (duration 1.17h).

**Magnitude:** baseline 23.84 (source: prewindow_median), peak 22.63, delta -1.214 (-5.09%).

**Calendar context:** Tuesday, hour 15 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 4.2e+03 (threshold 0).

---

## Case waterleak_120d#121  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 17:00 UTC -> Tue May 26 2026 19:40 UTC (duration 2.67h).

**Magnitude:** baseline 23.33 (source: prewindow_median), peak 20.59, delta -2.742 (-11.75%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 9.6e+03 (threshold 0).

---

## Case waterleak_120d#122  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 19:40 UTC -> Tue May 26 2026 21:50 UTC (duration 2.17h).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Tuesday, hour 19 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 7.8e+03 (threshold 0).

---

## Case waterleak_120d#123  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 27 2026 00:00 UTC -> Wed May 27 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Wednesday, hour 0 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -6.22 (threshold 0).

---

## Case waterleak_120d#124  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 27 2026 06:00 UTC -> Wed May 27 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Wednesday, hour 6 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -6.35 (threshold 0).

---

## Case waterleak_120d#125  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 27 2026 12:00 UTC -> Wed May 27 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Wednesday, hour 12 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -6.48 (threshold 0).

---

## Case waterleak_120d#126  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 27 2026 18:00 UTC -> Wed May 27 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Wednesday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -6.61 (threshold 0).

---

## Case waterleak_120d#127  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 28 2026 00:00 UTC -> Thu May 28 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Thursday, hour 0 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -6.74 (threshold 0).

---

## Case waterleak_120d#128  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 28 2026 06:00 UTC -> Thu May 28 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Thursday, hour 6 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -6.87 (threshold 0).

---

## Case waterleak_120d#129  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 28 2026 12:00 UTC -> Thu May 28 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Thursday, hour 12 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -7 (threshold 0).

---

## Case waterleak_120d#130  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 28 2026 18:00 UTC -> Thu May 28 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Thursday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -7.13 (threshold 0).

---

## Case waterleak_120d#131  —  TP  —  GT: unusual_occupancy

# Anomaly on sensor leak_basement (capability: water)

**When:** Fri May 29 2026 03:00 UTC -> Fri May 29 2026 03:00 UTC (duration 0s).

**Magnitude:** baseline 0 (source: prewindow_median), peak 1, delta +1 (+nan%).

**Calendar context:** Friday, hour 3 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** state_transition.

**Score:** 1 (threshold 0).

---

## Case waterleak_120d#132  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 27 2026 17:38 UTC -> Sun May 31 2026 17:38 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Wednesday, hour 17 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 99.7 (threshold 0).

---

## Case waterleak_120d#133  —  TP  —  GT: unusual_occupancy

# Anomaly on sensor leak_basement (capability: water)

**When:** Fri May 29 2026 03:00 UTC -> Sat May 30 2026 03:05 UTC (duration 1.00d).
**Long-duration framing:** spans 1.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 0 (source: prewindow_median), peak 1, delta +1 (+nan%).

**Calendar context:** Friday, hour 3 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca.

**Score:** 5 (threshold 0).

---

## Case waterleak_120d#134  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 31 2026 15:34 UTC -> Sun May 31 2026 18:00 UTC (duration 2.43h).

**Magnitude:** baseline unavailable (no pre-window data).

**Calendar context:** Sunday, hour 15 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 92.6 (threshold 0).

---
