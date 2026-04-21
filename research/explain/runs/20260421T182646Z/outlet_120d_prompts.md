# outlet_120d — explain cases (run 20260421T182646Z)

## Case outlet_120d#000  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 09 2026 11:00 UTC -> Mon Feb 09 2026 11:01 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_median), peak 9999, delta +9998 (+666500.00%).

**Calendar context:** Monday, hour 11 (morning), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 1e+04 (threshold 0).

---

## Case outlet_120d#001  —  TP  —  GT: noise_burst

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Feb 13 2026 12:00 UTC -> Fri Feb 13 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_median), peak -56.11, delta -57.61 (-3840.68%).

**Calendar context:** Friday, hour 12 (afternoon), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -13.8 (threshold 0).

---

## Case outlet_120d#002  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 10:30 UTC -> Sun Feb 15 2026 10:31 UTC (duration 1.0m).

**Magnitude:** baseline 120.2 (source: prewindow_median), peak 141.1, delta +20.96 (+17.44%).

**Calendar context:** Sunday, hour 10 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 141 (threshold 0).

---

## Case outlet_120d#003  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 11:12 UTC -> Sun Feb 15 2026 11:13 UTC (duration 1.0m).

**Magnitude:** baseline 120.1 (source: prewindow_median), peak 140.9, delta +20.88 (+17.39%).

**Calendar context:** Sunday, hour 11 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 141 (threshold 0).

---

## Case outlet_120d#004  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 10:00 UTC -> Sun Feb 15 2026 12:01 UTC (duration 2.02h).

**Magnitude:** baseline 120 (source: prewindow_median), peak 96.77, delta -23.26 (-19.38%).

**Calendar context:** Sunday, hour 10 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 80.1 (threshold 0).

---

## Case outlet_120d#005  —  TP  —  GT: calibration_drift, trend

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Feb 17 2026 00:00 UTC -> Sat Feb 21 2026 00:00 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 120 (source: prewindow_median), peak 127.9, delta +7.908 (+6.59%).

**Calendar context:** Tuesday, hour 0 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 91.1 (threshold 0).

---

## Case outlet_120d#006  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Feb 20 2026 21:57 UTC -> Sat Feb 21 2026 14:39 UTC (duration 16.70h).

**Magnitude:** baseline 1.5 (source: prewindow_median), peak 116.7, delta +115.2 (+7683.21%).

**Calendar context:** Friday, hour 21 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#007  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Feb 21 2026 13:41 UTC -> Sat Feb 21 2026 18:05 UTC (duration 4.40h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 113.4, delta +96.88 (+587.15%).

**Calendar context:** Saturday, hour 13 (afternoon), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#008  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 00:10 UTC -> Mon Feb 23 2026 00:11 UTC (duration 1.0m).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak -2.912, delta -19.41 (-117.65%).

**Calendar context:** Monday, hour 0 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.91 (threshold 0).

---

## Case outlet_120d#009  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 00:43 UTC -> Mon Feb 23 2026 00:44 UTC (duration 1.0m).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak -2.912, delta -19.41 (-117.65%).

**Calendar context:** Monday, hour 0 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.91 (threshold 0).

---

## Case outlet_120d#010  —  TP  —  GT: level_shift, frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Feb 21 2026 17:51 UTC -> Mon Feb 23 2026 01:14 UTC (duration 1.31d).
**Long-duration framing:** spans 1.3 days; covers 2 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 117.4, delta +100.9 (+611.33%).

**Calendar context:** Saturday, hour 17 (afternoon), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 6.32e+04 (threshold 0).

---

## Case outlet_120d#011  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 03:01 UTC -> Mon Feb 23 2026 03:02 UTC (duration 1.0m).

**Magnitude:** baseline 103.7 (source: prewindow_median), peak -2.912, delta -106.7 (-102.81%).

**Calendar context:** Monday, hour 3 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.91 (threshold 0).

---

## Case outlet_120d#012  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 03:34 UTC -> Mon Feb 23 2026 03:35 UTC (duration 1.0m).

**Magnitude:** baseline 89.97 (source: prewindow_median), peak -2.912, delta -92.88 (-103.24%).

**Calendar context:** Monday, hour 3 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.91 (threshold 0).

---

## Case outlet_120d#013  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 04:06 UTC -> Mon Feb 23 2026 04:07 UTC (duration 1.0m).

**Magnitude:** baseline 44.02 (source: prewindow_median), peak -13.38, delta -57.41 (-130.40%).

**Calendar context:** Monday, hour 4 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -13.4 (threshold 0).

---

## Case outlet_120d#014  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 04:36 UTC -> Mon Feb 23 2026 04:37 UTC (duration 1.0m).

**Magnitude:** baseline 30.79 (source: prewindow_median), peak -1.286, delta -32.07 (-104.18%).

**Calendar context:** Monday, hour 4 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.29 (threshold 0).

---

## Case outlet_120d#015  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 05:10 UTC -> Mon Feb 23 2026 05:11 UTC (duration 1.0m).

**Magnitude:** baseline 28.06 (source: prewindow_median), peak -1.286, delta -29.35 (-104.58%).

**Calendar context:** Monday, hour 5 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.29 (threshold 0).

---

## Case outlet_120d#016  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 05:48 UTC -> Mon Feb 23 2026 05:49 UTC (duration 1.0m).

**Magnitude:** baseline 29.1 (source: prewindow_median), peak -2.331, delta -31.43 (-108.01%).

**Calendar context:** Monday, hour 5 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.33 (threshold 0).

---

## Case outlet_120d#017  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 00:43 UTC -> Mon Feb 23 2026 13:26 UTC (duration 12.72h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 145.4, delta +128.9 (+780.95%).

**Calendar context:** Monday, hour 0 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 8.97e+04 (threshold 0).

---

## Case outlet_120d#018  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 12:39 UTC -> Tue Feb 24 2026 00:04 UTC (duration 11.42h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 114.7, delta +98.18 (+595.04%).

**Calendar context:** Monday, hour 12 (afternoon), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#019  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 23:02 UTC -> Tue Feb 24 2026 16:38 UTC (duration 17.60h).

**Magnitude:** baseline 103.7 (source: prewindow_median), peak 16.5, delta -87.21 (-84.09%).

**Calendar context:** Monday, hour 23 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#020  —  TP  —  GT: trend

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Fri Feb 20 2026 21:56 UTC -> Wed Feb 25 2026 00:01 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 127.1 (source: prewindow_median), peak 122.8, delta -4.35 (-3.42%).

**Calendar context:** Friday, hour 21 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 66.5 (threshold 0).

---

## Case outlet_120d#021  —  TP  —  GT: seasonality_loss, time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Feb 24 2026 15:52 UTC -> Fri Feb 27 2026 03:44 UTC (duration 2.49d).
**Long-duration framing:** spans 2.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 186.2, delta +169.7 (+1028.77%).

**Calendar context:** Tuesday, hour 15 (afternoon), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 1.88e+05 (threshold 0).

---

## Case outlet_120d#022  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Feb 27 2026 02:55 UTC -> Fri Feb 27 2026 06:22 UTC (duration 3.45h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 186.2, delta +169.7 (+1028.77%).

**Calendar context:** Friday, hour 2 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#023  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Feb 27 2026 05:32 UTC -> Sat Feb 28 2026 02:59 UTC (duration 21.45h).

**Magnitude:** baseline 96.5 (source: prewindow_median), peak 16.5, delta -80 (-82.90%).

**Calendar context:** Friday, hour 5 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#024  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Feb 28 2026 03:21 UTC -> Sat Feb 28 2026 21:31 UTC (duration 18.17h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 192.1, delta +175.6 (+1064.26%).

**Calendar context:** Saturday, hour 3 (night), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#025  —  TP  —  GT: month_shift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Feb 24 2026 21:57 UTC -> Sun Mar 01 2026 00:02 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 124 (source: prewindow_median), peak 126.1, delta +2.092 (+1.69%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 47 (threshold 0).

---

## Case outlet_120d#026  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Feb 28 2026 20:52 UTC -> Sat Feb 28 2026 23:24 UTC (duration 2.53h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 110.7, delta +94.16 (+570.67%).

**Calendar context:** Saturday, hour 20 (evening), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#027  —  TP  —  GT: time_of_day, weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 01 2026 00:05 UTC -> Mon Mar 02 2026 06:35 UTC (duration 1.27d).
**Long-duration framing:** spans 1.3 days; covers 1 weekend day(s).

**Magnitude:** baseline 104 (source: prewindow_median), peak 16.5, delta -87.46 (-84.13%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 7.96e+05 (threshold 0).

---

## Case outlet_120d#028  —  TP  —  GT: month_shift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat Feb 28 2026 21:58 UTC -> Thu Mar 05 2026 00:03 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 124.1 (source: prewindow_median), peak 127.2, delta +3.186 (+2.57%).

**Calendar context:** Saturday, hour 21 (evening), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 79.8 (threshold 0).

---

## Case outlet_120d#029  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Mar 02 2026 06:58 UTC -> Thu Mar 05 2026 06:34 UTC (duration 2.98d).
**Long-duration framing:** spans 3.0 days; covers 0 weekend day(s).

**Magnitude:** baseline 58.18 (source: prewindow_median), peak 116.4, delta +58.23 (+100.08%).

**Calendar context:** Monday, hour 6 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#030  —  TP  —  GT: weekend_anomaly, dropout

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 05 2026 05:36 UTC -> Thu Mar 05 2026 13:41 UTC (duration 8.08h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 111.4, delta +94.86 (+574.92%).

**Calendar context:** Thursday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#031  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 05 2026 13:25 UTC -> Thu Mar 05 2026 19:39 UTC (duration 6.23h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 114.8, delta +98.31 (+595.81%).

**Calendar context:** Thursday, hour 13 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#032  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 05 2026 19:26 UTC -> Thu Mar 05 2026 21:50 UTC (duration 2.40h).

**Magnitude:** baseline 101.1 (source: prewindow_median), peak 16.5, delta -84.63 (-83.68%).

**Calendar context:** Thursday, hour 19 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#033  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 05 2026 20:58 UTC -> Fri Mar 06 2026 21:44 UTC (duration 1.03d).
**Long-duration framing:** spans 1.0 days; covers 0 weekend day(s).

**Magnitude:** baseline 100.1 (source: prewindow_median), peak 16.5, delta -83.63 (-83.52%).

**Calendar context:** Thursday, hour 20 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#034  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 06 2026 20:57 UTC -> Fri Mar 06 2026 23:59 UTC (duration 3.03h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 116, delta +99.52 (+603.17%).

**Calendar context:** Friday, hour 20 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#035  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 01:00 UTC -> Sat Mar 07 2026 01:59 UTC (duration 59.0m).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 147.2, delta +90.74 (+160.60%).

**Calendar context:** Saturday, hour 1 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 5.5 (threshold 0).

---

## Case outlet_120d#036  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 05:00 UTC -> Sat Mar 07 2026 06:59 UTC (duration 1.98h).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 148.6, delta +92.11 (+163.03%).

**Calendar context:** Saturday, hour 5 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 7.07 (threshold 0).

---

## Case outlet_120d#037  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 08:00 UTC -> Sat Mar 07 2026 08:59 UTC (duration 59.0m).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 151.8, delta +95.29 (+168.66%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 6.45 (threshold 0).

---

## Case outlet_120d#038  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 11:03 UTC -> Sat Mar 07 2026 11:03 UTC (duration 0s).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak nan, delta +nan (+nan%).

**Calendar context:** Saturday, hour 11 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** multivariate_pca.

**Score:** 3.25e+04 (threshold 0).

---

## Case outlet_120d#039  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 12:55 UTC -> Sat Mar 07 2026 15:03 UTC (duration 2.13h).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 153.2, delta +96.68 (+171.12%).

**Calendar context:** Saturday, hour 12 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** multivariate_pca.

**Score:** 3.73e+04 (threshold 0).

---

## Case outlet_120d#040  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 17:00 UTC -> Sun Mar 08 2026 02:16 UTC (duration 9.27h).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 151.3, delta +94.75 (+167.71%).

**Calendar context:** Saturday, hour 17 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 6.98e+04 (threshold 0).

---

## Case outlet_120d#041  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 02:31 UTC -> Sun Mar 08 2026 09:01 UTC (duration 6.51h).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 153.3, delta +96.84 (+171.40%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, temporal_profile.

**Score:** 4.59e+03 (threshold 0).

---

## Case outlet_120d#042  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 09:01 UTC -> Sun Mar 08 2026 13:59 UTC (duration 4.95h).

**Magnitude:** baseline 150.2 (source: prewindow_median), peak 56.5, delta -93.74 (-62.39%).

**Calendar context:** Sunday, hour 9 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, temporal_profile.

**Score:** 5.25e+03 (threshold 0).

---

## Case outlet_120d#043  —  TP  —  GT: month_shift, duplicate_stale

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Wed Mar 04 2026 21:59 UTC -> Mon Mar 09 2026 00:04 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 126 (source: prewindow_median), peak 127, delta +1.08 (+0.86%).

**Calendar context:** Wednesday, hour 21 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 92 (threshold 0).

---

## Case outlet_120d#044  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:30 UTC -> Tue Mar 10 2026 00:31 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_median), peak 126.3, delta +0.3413 (+0.27%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#045  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:40 UTC -> Tue Mar 10 2026 00:41 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126, delta -0.05924 (-0.05%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#046  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:51 UTC -> Tue Mar 10 2026 00:52 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.9, delta -0.1839 (-0.15%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#047  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:01 UTC -> Tue Mar 10 2026 01:02 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.6, delta -0.4125 (-0.33%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#048  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:11 UTC -> Tue Mar 10 2026 01:12 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.9, delta -0.07685 (-0.06%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#049  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:21 UTC -> Tue Mar 10 2026 01:22 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_median), peak 126, delta +0.07243 (+0.06%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#050  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:31 UTC -> Tue Mar 10 2026 01:32 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.2, delta +0.1755 (+0.14%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#051  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:42 UTC -> Tue Mar 10 2026 01:43 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.7, delta -0.2747 (-0.22%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#052  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:52 UTC -> Tue Mar 10 2026 01:53 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.5, delta +0.5505 (+0.44%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#053  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:02 UTC -> Tue Mar 10 2026 02:03 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.3, delta +0.2887 (+0.23%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#054  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:12 UTC -> Tue Mar 10 2026 02:13 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.2, delta +0.1948 (+0.15%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#055  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:22 UTC -> Tue Mar 10 2026 02:23 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.5, delta +0.5245 (+0.42%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#056  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:33 UTC -> Tue Mar 10 2026 02:34 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.1, delta +0.09375 (+0.07%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#057  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:43 UTC -> Tue Mar 10 2026 02:44 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 125.9, delta -0.1808 (-0.14%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#058  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:53 UTC -> Tue Mar 10 2026 02:54 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.3, delta +0.2345 (+0.19%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#059  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:03 UTC -> Tue Mar 10 2026 03:04 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.4, delta -0.7105 (-0.56%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#060  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:13 UTC -> Tue Mar 10 2026 03:14 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 126.3, delta +0.1019 (+0.08%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#061  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:24 UTC -> Tue Mar 10 2026 03:25 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.8, delta -0.4178 (-0.33%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#062  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:34 UTC -> Tue Mar 10 2026 03:35 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.4, delta -0.7889 (-0.63%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#063  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:44 UTC -> Tue Mar 10 2026 03:45 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.8, delta -0.3544 (-0.28%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#064  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:54 UTC -> Tue Mar 10 2026 03:55 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.1, delta -0.01955 (-0.02%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#065  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:04 UTC -> Tue Mar 10 2026 04:05 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.3, delta +0.2701 (+0.21%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#066  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:15 UTC -> Tue Mar 10 2026 04:16 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.1, delta +0.07486 (+0.06%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#067  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:25 UTC -> Tue Mar 10 2026 04:26 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 125.5, delta -0.5175 (-0.41%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#068  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:35 UTC -> Tue Mar 10 2026 04:36 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_median), peak 126.3, delta +0.3651 (+0.29%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#069  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:45 UTC -> Tue Mar 10 2026 04:46 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126, delta -0.02427 (-0.02%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#070  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:55 UTC -> Tue Mar 10 2026 04:56 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.3, delta +0.2418 (+0.19%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#071  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:06 UTC -> Tue Mar 10 2026 05:07 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 125.2, delta -0.8694 (-0.69%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#072  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:16 UTC -> Tue Mar 10 2026 05:17 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.2, delta +0.2109 (+0.17%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#073  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:26 UTC -> Tue Mar 10 2026 05:27 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.2, delta +0.1845 (+0.15%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#074  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:36 UTC -> Tue Mar 10 2026 05:37 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.5, delta +0.3431 (+0.27%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#075  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:46 UTC -> Tue Mar 10 2026 05:47 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 126.1, delta -0.1849 (-0.15%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#076  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:57 UTC -> Tue Mar 10 2026 05:58 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.4, delta -0.8825 (-0.70%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#077  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 14:09 UTC -> Tue Mar 10 2026 05:27 UTC (duration 1.64d).
**Long-duration framing:** spans 1.6 days; covers 1 weekend day(s).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 150.3, delta +93.78 (+165.98%).

**Calendar context:** Sunday, hour 14 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#078  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 10 2026 04:29 UTC -> Tue Mar 10 2026 18:24 UTC (duration 13.92h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 114.4, delta +97.88 (+593.23%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#079  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 10 2026 17:47 UTC -> Wed Mar 11 2026 10:38 UTC (duration 16.85h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 117.1, delta +100.6 (+609.54%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#080  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 11 2026 09:59 UTC -> Wed Mar 11 2026 23:42 UTC (duration 13.72h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 114.6, delta +98.14 (+594.81%).

**Calendar context:** Wednesday, hour 9 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#081  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 103.2 (source: prewindow_median), peak 16.5, delta -86.69 (-84.01%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#082  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 103.2 (source: prewindow_median), peak 16.5, delta -86.69 (-84.01%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#083  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 103.2 (source: prewindow_median), peak 16.5, delta -86.69 (-84.01%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#084  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 103.2 (source: prewindow_median), peak 16.5, delta -86.69 (-84.01%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#085  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 11 2026 23:00 UTC -> Thu Mar 12 2026 14:12 UTC (duration 15.20h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 114.7, delta +98.18 (+595.03%).

**Calendar context:** Wednesday, hour 23 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#086  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Mar 08 2026 22:00 UTC -> Fri Mar 13 2026 00:05 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 124.9, delta -1.287 (-1.02%).

**Calendar context:** Sunday, hour 22 (evening), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 85.1 (threshold 0).

---

## Case outlet_120d#087  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 13:21 UTC -> Fri Mar 13 2026 07:36 UTC (duration 18.25h).

**Magnitude:** baseline 102.1 (source: prewindow_median), peak 16.5, delta -85.56 (-83.83%).

**Calendar context:** Thursday, hour 13 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#088  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 13 2026 07:04 UTC -> Fri Mar 13 2026 20:57 UTC (duration 13.88h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 116.6, delta +100.1 (+606.55%).

**Calendar context:** Friday, hour 7 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#089  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 13 2026 20:05 UTC -> Fri Mar 13 2026 23:59 UTC (duration 3.90h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 110.9, delta +94.41 (+572.17%).

**Calendar context:** Friday, hour 20 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#090  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 01:00 UTC -> Sat Mar 14 2026 02:37 UTC (duration 1.62h).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 149.3, delta +92.77 (+164.20%).

**Calendar context:** Saturday, hour 1 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, temporal_profile.

**Score:** 1.3e+03 (threshold 0).

---

## Case outlet_120d#091  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 05:00 UTC -> Sat Mar 14 2026 06:59 UTC (duration 1.98h).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 151.4, delta +94.86 (+167.89%).

**Calendar context:** Saturday, hour 5 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 7.12 (threshold 0).

---

## Case outlet_120d#092  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 08:00 UTC -> Sat Mar 14 2026 08:59 UTC (duration 59.0m).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 143.3, delta +86.76 (+153.56%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 5.42 (threshold 0).

---

## Case outlet_120d#093  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 11:59 UTC -> Sat Mar 14 2026 11:59 UTC (duration 0s).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak nan, delta +nan (+nan%).

**Calendar context:** Saturday, hour 11 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum.

**Score:** 1.29e+03 (threshold 0).

---

## Case outlet_120d#094  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 13:55 UTC -> Sat Mar 14 2026 14:15 UTC (duration 20.0m).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 150.1, delta +93.56 (+165.58%).

**Calendar context:** Saturday, hour 13 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** multivariate_pca.

**Score:** 3.96e+04 (threshold 0).

---

## Case outlet_120d#095  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 15:35 UTC -> Mon Mar 16 2026 09:32 UTC (duration 1.75d).
**Long-duration framing:** spans 1.7 days; covers 2 weekend day(s).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 160.1, delta +103.6 (+183.33%).

**Calendar context:** Saturday, hour 15 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.1e+05 (threshold 0).

---

## Case outlet_120d#096  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Mar 16 2026 08:31 UTC -> Mon Mar 16 2026 15:26 UTC (duration 6.92h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 116.3, delta +99.77 (+604.66%).

**Calendar context:** Monday, hour 8 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#097  —  TP  —  GT: month_shift, stuck_at

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 12 2026 22:01 UTC -> Tue Mar 17 2026 00:06 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 124.8, delta -1.366 (-1.08%).

**Calendar context:** Thursday, hour 22 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 85.8 (threshold 0).

---

## Case outlet_120d#098  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Mar 16 2026 14:36 UTC -> Wed Mar 18 2026 02:28 UTC (duration 1.49d).
**Long-duration framing:** spans 1.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 115.6, delta +99.12 (+600.72%).

**Calendar context:** Monday, hour 14 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#099  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 18 2026 01:41 UTC -> Fri Mar 20 2026 18:04 UTC (duration 2.68d).
**Long-duration framing:** spans 2.7 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 115.3, delta +98.78 (+598.69%).

**Calendar context:** Wednesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#100  —  TP  —  GT: month_shift, stuck_at, degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Mon Mar 16 2026 22:02 UTC -> Sat Mar 21 2026 00:07 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 124.9, delta -1.207 (-0.96%).

**Calendar context:** Monday, hour 22 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 82.4 (threshold 0).

---

## Case outlet_120d#101  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 20 2026 17:02 UTC -> Sat Mar 21 2026 02:09 UTC (duration 9.12h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 115.2, delta +98.67 (+597.98%).

**Calendar context:** Friday, hour 17 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#102  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 21 2026 01:11 UTC -> Tue Mar 24 2026 15:11 UTC (duration 3.58d).
**Long-duration framing:** spans 3.6 days; covers 2 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 117.7, delta +101.2 (+613.56%).

**Calendar context:** Saturday, hour 1 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#103  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 24 2026 14:43 UTC -> Tue Mar 24 2026 21:01 UTC (duration 6.30h).

**Magnitude:** baseline 93.16 (source: prewindow_median), peak 16.5, delta -76.66 (-82.29%).

**Calendar context:** Tuesday, hour 14 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#104  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 24 2026 20:03 UTC -> Tue Mar 24 2026 22:22 UTC (duration 2.32h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 110, delta +93.5 (+566.67%).

**Calendar context:** Tuesday, hour 20 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#105  —  TP  —  GT: month_shift, degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Fri Mar 20 2026 22:03 UTC -> Wed Mar 25 2026 00:08 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 125.8 (source: prewindow_median), peak 127.4, delta +1.588 (+1.26%).

**Calendar context:** Friday, hour 22 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 86.1 (threshold 0).

---

## Case outlet_120d#106  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 24 2026 21:21 UTC -> Wed Mar 25 2026 10:08 UTC (duration 12.78h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 113, delta +96.46 (+584.61%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#107  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 25 2026 09:32 UTC -> Wed Mar 25 2026 11:54 UTC (duration 2.37h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 109.1, delta +92.6 (+561.18%).

**Calendar context:** Wednesday, hour 9 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#108  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 25 2026 11:02 UTC -> Fri Mar 27 2026 05:12 UTC (duration 1.76d).
**Long-duration framing:** spans 1.8 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 117.9, delta +101.4 (+614.46%).

**Calendar context:** Wednesday, hour 11 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#109  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 27 2026 04:25 UTC -> Fri Mar 27 2026 06:37 UTC (duration 2.20h).

**Magnitude:** baseline 103.5 (source: prewindow_median), peak 16.5, delta -86.99 (-84.06%).

**Calendar context:** Friday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#110  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 27 2026 06:06 UTC -> Fri Mar 27 2026 08:57 UTC (duration 2.85h).

**Magnitude:** baseline 100.2 (source: prewindow_median), peak 16.5, delta -83.69 (-83.53%).

**Calendar context:** Friday, hour 6 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#111  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 27 2026 08:15 UTC -> Fri Mar 27 2026 15:05 UTC (duration 6.83h).

**Magnitude:** baseline 104.6 (source: prewindow_median), peak 16.5, delta -88.13 (-84.23%).

**Calendar context:** Friday, hour 8 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#112  —  TP  —  GT: month_shift, degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 24 2026 22:04 UTC -> Sun Mar 29 2026 00:09 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 126.6 (source: prewindow_median), peak 128.2, delta +1.605 (+1.27%).

**Calendar context:** Tuesday, hour 22 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 97.3 (threshold 0).

---

## Case outlet_120d#113  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 27 2026 14:07 UTC -> Tue Mar 31 2026 14:10 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 115.9, delta +99.4 (+602.40%).

**Calendar context:** Friday, hour 14 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#114  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 13:32 UTC -> Tue Mar 31 2026 18:59 UTC (duration 5.45h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 113.7, delta +97.22 (+589.21%).

**Calendar context:** Tuesday, hour 13 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#115  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 17:55 UTC -> Tue Mar 31 2026 22:29 UTC (duration 4.57h).

**Magnitude:** baseline 98.56 (source: prewindow_median), peak 16.5, delta -82.06 (-83.26%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#116  —  TP  —  GT: month_shift, degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat Mar 28 2026 22:05 UTC -> Thu Apr 02 2026 00:10 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 126.8 (source: prewindow_median), peak 122.9, delta -3.896 (-3.07%).

**Calendar context:** Saturday, hour 22 (evening), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 97.8 (threshold 0).

---

## Case outlet_120d#117  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 21:29 UTC -> Thu Apr 02 2026 00:19 UTC (duration 1.12d).
**Long-duration framing:** spans 1.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 118.3, delta +101.8 (+616.85%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#118  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Apr 02 2026 00:11 UTC -> Fri Apr 03 2026 10:15 UTC (duration 1.42d).
**Long-duration framing:** spans 1.4 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 117.2, delta +100.7 (+610.42%).

**Calendar context:** Thursday, hour 0 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#119  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Apr 03 2026 09:31 UTC -> Sat Apr 04 2026 01:21 UTC (duration 15.83h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 115.7, delta +99.17 (+601.06%).

**Calendar context:** Friday, hour 9 (morning), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#120  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Wed Apr 01 2026 22:06 UTC -> Mon Apr 06 2026 00:11 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 124.3 (source: prewindow_median), peak 122.8, delta -1.45 (-1.17%).

**Calendar context:** Wednesday, hour 22 (evening), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 45.9 (threshold 0).

---

## Case outlet_120d#121  —  TP  —  GT: spike

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Apr 04 2026 00:17 UTC -> Mon Apr 06 2026 03:08 UTC (duration 2.12d).
**Long-duration framing:** spans 2.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 656.4, delta +639.9 (+3878.35%).

**Calendar context:** Saturday, hour 0 (night), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 6.72e+05 (threshold 0).

---

## Case outlet_120d#122  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Apr 06 2026 02:25 UTC -> Tue Apr 07 2026 12:24 UTC (duration 1.42d).
**Long-duration framing:** spans 1.4 days; covers 0 weekend day(s).

**Magnitude:** baseline 103.4 (source: prewindow_median), peak 16.5, delta -86.95 (-84.05%).

**Calendar context:** Monday, hour 2 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#123  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 07 2026 11:24 UTC -> Tue Apr 07 2026 21:33 UTC (duration 10.15h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 115.1, delta +98.64 (+597.83%).

**Calendar context:** Tuesday, hour 11 (morning), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#124  —  TP  —  GT: dip

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 08 2026 09:00 UTC -> Wed Apr 08 2026 09:01 UTC (duration 1.0m).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak -68.5, delta -85 (-515.15%).

**Calendar context:** Wednesday, hour 9 (morning), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -68.5 (threshold 0).

---

## Case outlet_120d#125  —  TP  —  GT: dip

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 07 2026 21:10 UTC -> Wed Apr 08 2026 15:38 UTC (duration 18.47h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 118.1, delta +101.6 (+615.48%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 5.15e+04 (threshold 0).

---

## Case outlet_120d#126  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 08 2026 14:42 UTC -> Thu Apr 09 2026 06:04 UTC (duration 15.37h).

**Magnitude:** baseline 57.78 (source: prewindow_median), peak 115.8, delta +57.97 (+100.33%).

**Calendar context:** Wednesday, hour 14 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#127  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Apr 05 2026 22:07 UTC -> Fri Apr 10 2026 00:12 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 124.2 (source: prewindow_median), peak 122.8, delta -1.392 (-1.12%).

**Calendar context:** Sunday, hour 22 (evening), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 46 (threshold 0).

---

## Case outlet_120d#128  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Apr 09 2026 05:20 UTC -> Fri Apr 10 2026 01:17 UTC (duration 19.95h).

**Magnitude:** baseline 98.63 (source: prewindow_median), peak 16.5, delta -82.13 (-83.27%).

**Calendar context:** Thursday, hour 5 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#129  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Apr 10 2026 00:40 UTC -> Fri Apr 10 2026 22:04 UTC (duration 21.40h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 118.1, delta +101.6 (+615.60%).

**Calendar context:** Friday, hour 0 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#130  —  TP  —  GT: noise_burst

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Apr 11 2026 12:00 UTC -> Sat Apr 11 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak -48.58, delta -65.08 (-394.44%).

**Calendar context:** Saturday, hour 12 (afternoon), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -22.6 (threshold 0).

---

## Case outlet_120d#131  —  TP  —  GT: noise_burst

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Apr 10 2026 21:01 UTC -> Sat Apr 11 2026 18:50 UTC (duration 21.82h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 194, delta +177.5 (+1075.50%).

**Calendar context:** Friday, hour 21 (evening), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 3.02e+04 (threshold 0).

---

## Case outlet_120d#132  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Apr 11 2026 17:53 UTC -> Sun Apr 12 2026 17:56 UTC (duration 1.00d).
**Long-duration framing:** spans 1.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 114.4, delta +97.91 (+593.41%).

**Calendar context:** Saturday, hour 17 (afternoon), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#133  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Apr 12 2026 16:53 UTC -> Mon Apr 13 2026 04:34 UTC (duration 11.68h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 115.1, delta +98.61 (+597.64%).

**Calendar context:** Sunday, hour 16 (afternoon), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#134  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Apr 09 2026 22:08 UTC -> Tue Apr 14 2026 00:13 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 124 (source: prewindow_median), peak 125.4, delta +1.411 (+1.14%).

**Calendar context:** Thursday, hour 22 (evening), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 44.4 (threshold 0).

---

## Case outlet_120d#135  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Apr 13 2026 03:41 UTC -> Tue Apr 14 2026 02:26 UTC (duration 22.75h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 116.4, delta +99.9 (+605.46%).

**Calendar context:** Monday, hour 3 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#136  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Apr 14 2026 14:00 UTC -> Tue Apr 14 2026 14:01 UTC (duration 1.0m).

**Magnitude:** baseline 124.1 (source: prewindow_median), peak 180, delta +55.89 (+45.04%).

**Calendar context:** Tuesday, hour 14 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 180 (threshold 0).

---

## Case outlet_120d#137  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 14 2026 01:57 UTC -> Tue Apr 14 2026 13:21 UTC (duration 11.40h).

**Magnitude:** baseline 100.6 (source: prewindow_median), peak 16.5, delta -84.11 (-83.60%).

**Calendar context:** Tuesday, hour 1 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#138  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 14 2026 12:57 UTC -> Thu Apr 16 2026 09:23 UTC (duration 1.85d).
**Long-duration framing:** spans 1.9 days; covers 0 weekend day(s).

**Magnitude:** baseline 59.23 (source: prewindow_median), peak 115.7, delta +56.52 (+95.42%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#139  —  TP  —  GT: out_of_range, calibration_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Mon Apr 13 2026 22:09 UTC -> Sat Apr 18 2026 00:14 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 123.8 (source: prewindow_median), peak 180, delta +56.17 (+45.36%).

**Calendar context:** Monday, hour 22 (evening), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 5.76e+03 (threshold 0).

---

## Case outlet_120d#140  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Apr 16 2026 08:25 UTC -> Sat Apr 18 2026 00:18 UTC (duration 1.66d).
**Long-duration framing:** spans 1.7 days; covers 1 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 116.7, delta +100.2 (+607.32%).

**Calendar context:** Thursday, hour 8 (morning), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#141  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Apr 17 2026 23:16 UTC -> Sat Apr 18 2026 03:01 UTC (duration 3.75h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 115.8, delta +99.35 (+602.10%).

**Calendar context:** Friday, hour 23 (evening), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#142  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Apr 18 2026 01:58 UTC -> Sat Apr 18 2026 11:53 UTC (duration 9.92h).

**Magnitude:** baseline 103.4 (source: prewindow_median), peak 16.5, delta -86.89 (-84.04%).

**Calendar context:** Saturday, hour 1 (night), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#143  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Apr 18 2026 10:53 UTC -> Tue Apr 21 2026 03:34 UTC (duration 2.70d).
**Long-duration framing:** spans 2.7 days; covers 2 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 115.8, delta +99.27 (+601.61%).

**Calendar context:** Saturday, hour 10 (morning), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#144  —  TP  —  GT: calibration_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Fri Apr 17 2026 22:10 UTC -> Wed Apr 22 2026 00:15 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 123.9 (source: prewindow_median), peak 119.9, delta -3.958 (-3.19%).

**Calendar context:** Friday, hour 22 (evening), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 23.1 (threshold 0).

---

## Case outlet_120d#145  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 21 2026 02:34 UTC -> Wed Apr 22 2026 09:48 UTC (duration 1.30d).
**Long-duration framing:** spans 1.3 days; covers 0 weekend day(s).

**Magnitude:** baseline 94.16 (source: prewindow_median), peak 16.5, delta -77.66 (-82.48%).

**Calendar context:** Tuesday, hour 2 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#146  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 22 2026 09:02 UTC -> Wed Apr 22 2026 11:53 UTC (duration 2.85h).

**Magnitude:** baseline 102.1 (source: prewindow_median), peak 16.5, delta -85.63 (-83.84%).

**Calendar context:** Wednesday, hour 9 (morning), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#147  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 22 2026 11:15 UTC -> Thu Apr 23 2026 05:08 UTC (duration 17.88h).

**Magnitude:** baseline 104.5 (source: prewindow_median), peak 16.5, delta -87.99 (-84.21%).

**Calendar context:** Wednesday, hour 11 (morning), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#148  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Apr 23 2026 04:15 UTC -> Fri Apr 24 2026 16:30 UTC (duration 1.51d).
**Long-duration framing:** spans 1.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 119.9, delta +103.4 (+626.72%).

**Calendar context:** Thursday, hour 4 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#149  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Apr 24 2026 16:18 UTC -> Sat Apr 25 2026 14:20 UTC (duration 22.03h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 117.6, delta +101.1 (+612.78%).

**Calendar context:** Friday, hour 16 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#150  —  TP  —  GT: trend

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Apr 21 2026 23:13 UTC -> Sun Apr 26 2026 00:16 UTC (duration 4.04d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 120.9 (source: prewindow_median), peak 119.3, delta -1.555 (-1.29%).

**Calendar context:** Tuesday, hour 23 (evening), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 12.6 (threshold 0).

---

## Case outlet_120d#151  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Apr 25 2026 14:01 UTC -> Mon Apr 27 2026 18:29 UTC (duration 2.19d).
**Long-duration framing:** spans 2.2 days; covers 2 weekend day(s).

**Magnitude:** baseline 104.1 (source: prewindow_median), peak 16.5, delta -87.57 (-84.14%).

**Calendar context:** Saturday, hour 14 (afternoon), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#152  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Apr 27 2026 17:59 UTC -> Tue Apr 28 2026 04:30 UTC (duration 10.52h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 116, delta +99.53 (+603.19%).

**Calendar context:** Monday, hour 17 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#153  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 28 2026 03:40 UTC -> Tue Apr 28 2026 21:47 UTC (duration 18.12h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 117.6, delta +101.1 (+612.87%).

**Calendar context:** Tuesday, hour 3 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#154  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 28 2026 20:46 UTC -> Wed Apr 29 2026 01:28 UTC (duration 4.70h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 112, delta +95.49 (+578.72%).

**Calendar context:** Tuesday, hour 20 (evening), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#155  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 29 2026 00:55 UTC -> Wed Apr 29 2026 14:56 UTC (duration 14.02h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 117.1, delta +100.6 (+609.56%).

**Calendar context:** Wednesday, hour 0 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#156  —  TP  —  GT: trend

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Apr 26 2026 21:41 UTC -> Wed Apr 29 2026 16:02 UTC (duration 2.76d).
**Long-duration framing:** spans 2.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 119.3 (source: prewindow_median), peak 121.9, delta +2.588 (+2.17%).

**Calendar context:** Sunday, hour 21 (evening), weekend, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 21.3 (threshold 0).

---

## Case outlet_120d#157  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 29 2026 13:56 UTC -> Wed Apr 29 2026 21:08 UTC (duration 7.20h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 114.7, delta +98.21 (+595.21%).

**Calendar context:** Wednesday, hour 13 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#158  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 29 2026 20:15 UTC -> Fri May 01 2026 12:57 UTC (duration 1.70d).
**Long-duration framing:** spans 1.7 days; covers 0 weekend day(s).

**Magnitude:** baseline 55.93 (source: prewindow_median), peak 114, delta +58.08 (+103.84%).

**Calendar context:** Wednesday, hour 20 (evening), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#159  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 01 2026 12:00 UTC -> Fri May 01 2026 19:21 UTC (duration 7.35h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 101.1, delta +94.56 (+1454.72%).

**Calendar context:** Friday, hour 12 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#160  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 01 2026 18:21 UTC -> Fri May 01 2026 23:55 UTC (duration 5.57h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 100.1, delta +93.58 (+1439.64%).

**Calendar context:** Friday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#161  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 01 2026 23:23 UTC -> Sat May 02 2026 05:13 UTC (duration 5.83h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 103.8, delta +97.3 (+1496.93%).

**Calendar context:** Friday, hour 23 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#162  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 02 2026 04:21 UTC -> Sun May 03 2026 07:29 UTC (duration 1.13d).
**Long-duration framing:** spans 1.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 103.8, delta +97.3 (+1496.93%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#163  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Wed Apr 29 2026 17:55 UTC -> Sun May 03 2026 17:55 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 121.1 (source: prewindow_median), peak 119.8, delta -1.333 (-1.10%).

**Calendar context:** Wednesday, hour 17 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 9.55 (threshold 0).

---

## Case outlet_120d#164  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun May 03 2026 06:33 UTC -> Sun May 03 2026 20:51 UTC (duration 14.30h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 104.8, delta +98.29 (+1512.15%).

**Calendar context:** Sunday, hour 6 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#165  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun May 03 2026 19:58 UTC -> Mon May 04 2026 02:54 UTC (duration 6.93h).

**Magnitude:** baseline 94.58 (source: prewindow_median), peak 6.5, delta -88.08 (-93.13%).

**Calendar context:** Sunday, hour 19 (evening), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca, temporal_profile.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#166  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 04 2026 01:55 UTC -> Mon May 04 2026 22:49 UTC (duration 20.90h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 167.8, delta +161.3 (+2481.22%).

**Calendar context:** Monday, hour 1 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#167  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 04 2026 21:54 UTC -> Thu May 07 2026 00:04 UTC (duration 2.09d).
**Long-duration framing:** spans 2.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 169.9, delta +163.4 (+2514.01%).

**Calendar context:** Monday, hour 21 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca, temporal_profile.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#168  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun May 03 2026 16:19 UTC -> Thu May 07 2026 17:56 UTC (duration 4.07d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 121 (source: prewindow_median), peak 122.4, delta +1.428 (+1.18%).

**Calendar context:** Sunday, hour 16 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 9.16 (threshold 0).

---

## Case outlet_120d#169  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed May 06 2026 23:10 UTC -> Fri May 08 2026 03:40 UTC (duration 1.19d).
**Long-duration framing:** spans 1.2 days; covers 0 weekend day(s).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 106.8, delta +100.3 (+1543.64%).

**Calendar context:** Wednesday, hour 23 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca, temporal_profile.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#170  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 08 2026 02:38 UTC -> Fri May 08 2026 12:27 UTC (duration 9.82h).

**Magnitude:** baseline 87.85 (source: prewindow_median), peak 6.5, delta -81.35 (-92.60%).

**Calendar context:** Friday, hour 2 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#171  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 02:21 UTC -> Sat May 09 2026 02:22 UTC (duration 1.0m).

**Magnitude:** baseline 88.47 (source: prewindow_median), peak -9.436, delta -97.91 (-110.66%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -9.44 (threshold 0).

---

## Case outlet_120d#172  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 02:55 UTC -> Sat May 09 2026 02:56 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak -9.192, delta -15.69 (-241.42%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -9.19 (threshold 0).

---

## Case outlet_120d#173  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 03:28 UTC -> Sat May 09 2026 03:29 UTC (duration 1.0m).

**Magnitude:** baseline 14.82 (source: prewindow_median), peak -10.38, delta -25.2 (-170.06%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -10.4 (threshold 0).

---

## Case outlet_120d#174  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 04:01 UTC -> Sat May 09 2026 04:02 UTC (duration 1.0m).

**Magnitude:** baseline 14.82 (source: prewindow_median), peak -10.38, delta -25.2 (-170.06%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -10.4 (threshold 0).

---

## Case outlet_120d#175  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 04:59 UTC -> Sat May 09 2026 05:00 UTC (duration 1.0m).

**Magnitude:** baseline 19.63 (source: prewindow_median), peak -5.544, delta -25.17 (-128.24%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -5.54 (threshold 0).

---

## Case outlet_120d#176  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 05:33 UTC -> Sat May 09 2026 05:34 UTC (duration 1.0m).

**Magnitude:** baseline 19.63 (source: prewindow_median), peak -5.544, delta -25.17 (-128.24%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -5.54 (threshold 0).

---

## Case outlet_120d#177  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 06:06 UTC -> Sat May 09 2026 06:07 UTC (duration 1.0m).

**Magnitude:** baseline 19.63 (source: prewindow_median), peak -0.6255, delta -20.25 (-103.19%).

**Calendar context:** Saturday, hour 6 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.625 (threshold 0).

---

## Case outlet_120d#178  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 06:39 UTC -> Sat May 09 2026 06:40 UTC (duration 1.0m).

**Magnitude:** baseline 14.52 (source: prewindow_median), peak -0.6255, delta -15.15 (-104.31%).

**Calendar context:** Saturday, hour 6 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.625 (threshold 0).

---

## Case outlet_120d#179  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 07:12 UTC -> Sat May 09 2026 07:13 UTC (duration 1.0m).

**Magnitude:** baseline 9.633 (source: prewindow_median), peak -0.6255, delta -10.26 (-106.49%).

**Calendar context:** Saturday, hour 7 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.625 (threshold 0).

---

## Case outlet_120d#180  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 07:46 UTC -> Sat May 09 2026 07:47 UTC (duration 1.0m).

**Magnitude:** baseline 14.52 (source: prewindow_median), peak -0.6255, delta -15.15 (-104.31%).

**Calendar context:** Saturday, hour 7 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.625 (threshold 0).

---

## Case outlet_120d#181  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 08 2026 11:31 UTC -> Sat May 09 2026 07:57 UTC (duration 20.43h).

**Magnitude:** baseline 86.51 (source: prewindow_median), peak -15.7, delta -102.2 (-118.15%).

**Calendar context:** Friday, hour 11 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 4.33e+04 (threshold 0).

---

## Case outlet_120d#182  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 07:11 UTC -> Sat May 09 2026 15:00 UTC (duration 7.82h).

**Magnitude:** baseline 9.633 (source: prewindow_median), peak 111.3, delta +101.7 (+1055.22%).

**Calendar context:** Saturday, hour 7 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 4.16e+04 (threshold 0).

---

## Case outlet_120d#183  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 14:04 UTC -> Mon May 11 2026 06:11 UTC (duration 1.67d).
**Long-duration framing:** spans 1.7 days; covers 2 weekend day(s).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 105.2, delta +98.65 (+1517.73%).

**Calendar context:** Saturday, hour 14 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#184  —  TP  —  GT: degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu May 07 2026 17:57 UTC -> Mon May 11 2026 17:57 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 121 (source: prewindow_median), peak 122.8, delta +1.798 (+1.49%).

**Calendar context:** Thursday, hour 17 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 21.2 (threshold 0).

---

## Case outlet_120d#185  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 11 2026 06:17 UTC -> Tue May 12 2026 02:09 UTC (duration 19.87h).

**Magnitude:** baseline 87.93 (source: prewindow_median), peak 6.5, delta -81.43 (-92.61%).

**Calendar context:** Monday, hour 6 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#186  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue May 12 2026 01:12 UTC -> Tue May 12 2026 18:44 UTC (duration 17.53h).

**Magnitude:** baseline 92.83 (source: prewindow_median), peak 6.5, delta -86.33 (-93.00%).

**Calendar context:** Tuesday, hour 1 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#187  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue May 12 2026 17:55 UTC -> Tue May 12 2026 21:43 UTC (duration 3.80h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 102.1, delta +95.6 (+1470.76%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#188  —  TP  —  GT: seasonality_loss

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue May 12 2026 20:39 UTC -> Thu May 14 2026 12:50 UTC (duration 1.67d).
**Long-duration framing:** spans 1.7 days; covers 0 weekend day(s).

**Magnitude:** baseline 93.51 (source: prewindow_median), peak 6.5, delta -87.01 (-93.05%).

**Calendar context:** Tuesday, hour 20 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 1.36e+05 (threshold 0).

---

## Case outlet_120d#189  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu May 14 2026 11:47 UTC -> Fri May 15 2026 11:23 UTC (duration 23.60h).

**Magnitude:** baseline 91.19 (source: prewindow_median), peak 6.5, delta -84.69 (-92.87%).

**Calendar context:** Thursday, hour 11 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#190  —  TP  —  GT: degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Mon May 11 2026 16:00 UTC -> Fri May 15 2026 17:58 UTC (duration 4.08d).
**Long-duration framing:** spans 4.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 121 (source: prewindow_median), peak 122.4, delta +1.423 (+1.18%).

**Calendar context:** Monday, hour 16 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 11.1 (threshold 0).

---

## Case outlet_120d#191  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 15 2026 10:24 UTC -> Sat May 16 2026 02:25 UTC (duration 16.02h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 109.2, delta +102.7 (+1579.26%).

**Calendar context:** Friday, hour 10 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#192  —  TP  —  GT: dropout

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 16 2026 01:32 UTC -> Sat May 16 2026 11:44 UTC (duration 10.20h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 104.6, delta +98.09 (+1509.03%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.17e+03 (threshold 0).

---

## Case outlet_120d#193  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 16 2026 10:50 UTC -> Sat May 16 2026 19:10 UTC (duration 8.33h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 104, delta +97.46 (+1499.40%).

**Calendar context:** Saturday, hour 10 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#194  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 16 2026 18:08 UTC -> Sun May 17 2026 13:19 UTC (duration 19.18h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 108.4, delta +101.9 (+1568.29%).

**Calendar context:** Saturday, hour 18 (evening), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#195  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun May 17 2026 12:17 UTC -> Mon May 18 2026 20:37 UTC (duration 1.35d).
**Long-duration framing:** spans 1.3 days; covers 1 weekend day(s).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 104.2, delta +97.68 (+1502.77%).

**Calendar context:** Sunday, hour 12 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#196  —  TP  —  GT: degradation_trajectory, duplicate_stale

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Fri May 15 2026 16:40 UTC -> Tue May 19 2026 17:59 UTC (duration 4.05d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 121.2 (source: prewindow_median), peak 122.9, delta +1.716 (+1.42%).

**Calendar context:** Friday, hour 16 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#197  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 18 2026 19:40 UTC -> Tue May 19 2026 18:24 UTC (duration 22.73h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 105.6, delta +99.11 (+1524.76%).

**Calendar context:** Monday, hour 19 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#198  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue May 19 2026 17:28 UTC -> Wed May 20 2026 01:00 UTC (duration 7.53h).

**Magnitude:** baseline 91.27 (source: prewindow_median), peak 6.5, delta -84.77 (-92.88%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#199  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed May 20 2026 00:39 UTC -> Wed May 20 2026 08:35 UTC (duration 7.93h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 105.2, delta +98.68 (+1518.08%).

**Calendar context:** Wednesday, hour 0 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#200  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed May 20 2026 07:36 UTC -> Thu May 21 2026 00:47 UTC (duration 17.18h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 104.8, delta +98.27 (+1511.78%).

**Calendar context:** Wednesday, hour 7 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#201  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed May 20 2026 23:45 UTC -> Thu May 21 2026 15:18 UTC (duration 15.55h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 107.6, delta +101.1 (+1554.93%).

**Calendar context:** Wednesday, hour 23 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#202  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu May 21 2026 14:23 UTC -> Thu May 21 2026 18:46 UTC (duration 4.38h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 104.3, delta +97.78 (+1504.37%).

**Calendar context:** Thursday, hour 14 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#203  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu May 21 2026 17:52 UTC -> Fri May 22 2026 00:47 UTC (duration 6.92h).

**Magnitude:** baseline 48.25 (source: prewindow_median), peak 105.4, delta +57.1 (+118.34%).

**Calendar context:** Thursday, hour 17 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#204  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 00:06 UTC -> Fri May 22 2026 02:55 UTC (duration 2.82h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 100.1, delta +93.62 (+1440.38%).

**Calendar context:** Friday, hour 0 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#205  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#206  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#207  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#208  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#209  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#210  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#211  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#212  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 00:51 UTC -> Fri May 22 2026 17:05 UTC (duration 16.23h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 104.3, delta +97.84 (+1505.27%).

**Calendar context:** Friday, hour 0 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.85e+03 (threshold 0).

---

## Case outlet_120d#213  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 16:38 UTC -> Sat May 23 2026 09:24 UTC (duration 16.77h).

**Magnitude:** baseline 91.4 (source: prewindow_median), peak 6.5, delta -84.9 (-92.89%).

**Calendar context:** Friday, hour 16 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#214  —  TP  —  GT: degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue May 19 2026 15:55 UTC -> Sat May 23 2026 18:00 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 121.9 (source: prewindow_median), peak 123.2, delta +1.282 (+1.05%).

**Calendar context:** Tuesday, hour 15 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 17.9 (threshold 0).

---

## Case outlet_120d#215  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 23 2026 09:28 UTC -> Sun May 24 2026 18:05 UTC (duration 1.36d).
**Long-duration framing:** spans 1.4 days; covers 2 weekend day(s).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 105.8, delta +99.25 (+1526.98%).

**Calendar context:** Saturday, hour 9 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#216  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun May 24 2026 17:03 UTC -> Mon May 25 2026 00:28 UTC (duration 7.43h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 102.7, delta +96.19 (+1479.87%).

**Calendar context:** Sunday, hour 17 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#217  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun May 24 2026 22:24 UTC -> Mon May 25 2026 03:23 UTC (duration 5.00h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 99.28, delta +92.78 (+1427.41%).

**Calendar context:** Sunday, hour 22 (evening), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 4.74e+03 (threshold 0).

---

## Case outlet_120d#218  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 02:49 UTC -> Mon May 25 2026 05:25 UTC (duration 2.61h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 99.28, delta +92.78 (+1427.41%).

**Calendar context:** Monday, hour 2 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate, sub_pca.

**Score:** 3.95e+03 (threshold 0).

---

## Case outlet_120d#219  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 05:36 UTC -> Mon May 25 2026 06:30 UTC (duration 54.5m).

**Magnitude:** baseline 84.18 (source: prewindow_median), peak 94.44, delta +10.25 (+12.18%).

**Calendar context:** Monday, hour 5 (night), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 3.27e+03 (threshold 0).

---

## Case outlet_120d#220  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 07:06 UTC -> Mon May 25 2026 08:05 UTC (duration 59.6m).

**Magnitude:** baseline 94.44 (source: prewindow_median), peak 99.11, delta +4.671 (+4.95%).

**Calendar context:** Monday, hour 7 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 3.58e+03 (threshold 0).

---

## Case outlet_120d#221  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 08:35 UTC -> Mon May 25 2026 10:42 UTC (duration 2.12h).

**Magnitude:** baseline 95.26 (source: prewindow_median), peak 6.5, delta -88.76 (-93.18%).

**Calendar context:** Monday, hour 8 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 7.62e+03 (threshold 0).

---

## Case outlet_120d#222  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 08:38 UTC -> Mon May 25 2026 11:44 UTC (duration 3.10h).

**Magnitude:** baseline 95.55 (source: prewindow_median), peak 6.5, delta -89.05 (-93.20%).

**Calendar context:** Monday, hour 8 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.68e+03 (threshold 0).

---

## Case outlet_120d#223  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 09:56 UTC -> Mon May 25 2026 14:48 UTC (duration 4.88h).

**Magnitude:** baseline 93.67 (source: prewindow_median), peak 6.5, delta -87.17 (-93.06%).

**Calendar context:** Monday, hour 9 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.15e+03 (threshold 0).

---

## Case outlet_120d#224  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 13:29 UTC -> Mon May 25 2026 16:53 UTC (duration 3.40h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 104.2, delta +97.71 (+1503.19%).

**Calendar context:** Monday, hour 13 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#225  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 16:11 UTC -> Mon May 25 2026 19:35 UTC (duration 3.40h).

**Magnitude:** baseline 92.59 (source: prewindow_median), peak 6.5, delta -86.09 (-92.98%).

**Calendar context:** Monday, hour 16 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.27e+03 (threshold 0).

---

## Case outlet_120d#226  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 17:57 UTC -> Mon May 25 2026 20:41 UTC (duration 2.74h).

**Magnitude:** baseline 94.38 (source: prewindow_median), peak 6.5, delta -87.88 (-93.11%).

**Calendar context:** Monday, hour 17 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#227  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 18:37 UTC -> Tue May 26 2026 11:37 UTC (duration 17.00h).

**Magnitude:** baseline 45.89 (source: prewindow_median), peak 102.8, delta +56.95 (+124.11%).

**Calendar context:** Monday, hour 18 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 4.57e+03 (threshold 0).

---

## Case outlet_120d#228  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue May 26 2026 10:52 UTC -> Tue May 26 2026 18:09 UTC (duration 7.28h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 106.8, delta +100.3 (+1543.29%).

**Calendar context:** Tuesday, hour 10 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#229  —  TP  —  GT: degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 23 2026 15:56 UTC -> Wed May 27 2026 18:01 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 121.8 (source: prewindow_median), peak 119.7, delta -2.118 (-1.74%).

**Calendar context:** Saturday, hour 15 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 14 (threshold 0).

---

## Case outlet_120d#230  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue May 26 2026 17:10 UTC -> Thu May 28 2026 23:14 UTC (duration 2.25d).
**Long-duration framing:** spans 2.3 days; covers 0 weekend day(s).

**Magnitude:** baseline 88.18 (source: prewindow_median), peak 6.5, delta -81.68 (-92.63%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#231  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu May 28 2026 22:30 UTC -> Fri May 29 2026 10:17 UTC (duration 11.78h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 106.7, delta +100.2 (+1542.24%).

**Calendar context:** Thursday, hour 22 (evening), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#232  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 00:30 UTC -> Sat May 30 2026 00:31 UTC (duration 1.0m).

**Magnitude:** baseline 121 (source: prewindow_median), peak 120.7, delta -0.2459 (-0.20%).

**Calendar context:** Saturday, hour 0 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#233  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 00:40 UTC -> Sat May 30 2026 00:41 UTC (duration 1.0m).

**Magnitude:** baseline 120.9 (source: prewindow_median), peak 120.8, delta -0.06738 (-0.06%).

**Calendar context:** Saturday, hour 0 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#234  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 00:51 UTC -> Sat May 30 2026 00:52 UTC (duration 1.0m).

**Magnitude:** baseline 120.9 (source: prewindow_median), peak 120.8, delta -0.03882 (-0.03%).

**Calendar context:** Saturday, hour 0 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#235  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 01:01 UTC -> Sat May 30 2026 01:02 UTC (duration 1.0m).

**Magnitude:** baseline 120.8 (source: prewindow_median), peak 121.9, delta +1.034 (+0.86%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#236  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 01:11 UTC -> Sat May 30 2026 01:12 UTC (duration 1.0m).

**Magnitude:** baseline 120.8 (source: prewindow_median), peak 121.1, delta +0.2401 (+0.20%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#237  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 01:21 UTC -> Sat May 30 2026 01:22 UTC (duration 1.0m).

**Magnitude:** baseline 120.9 (source: prewindow_median), peak 120.5, delta -0.3687 (-0.31%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#238  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 01:32 UTC -> Sat May 30 2026 01:33 UTC (duration 1.0m).

**Magnitude:** baseline 120.8 (source: prewindow_median), peak 120.7, delta -0.1372 (-0.11%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#239  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 01:42 UTC -> Sat May 30 2026 01:43 UTC (duration 1.0m).

**Magnitude:** baseline 120.8 (source: prewindow_median), peak 120.9, delta +0.08084 (+0.07%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#240  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 01:52 UTC -> Sat May 30 2026 01:53 UTC (duration 1.0m).

**Magnitude:** baseline 120.8 (source: prewindow_median), peak 121.5, delta +0.6448 (+0.53%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#241  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 02:02 UTC -> Sat May 30 2026 02:03 UTC (duration 1.0m).

**Magnitude:** baseline 120.9 (source: prewindow_median), peak 121.2, delta +0.3612 (+0.30%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#242  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 02:13 UTC -> Sat May 30 2026 02:14 UTC (duration 1.0m).

**Magnitude:** baseline 120.9 (source: prewindow_median), peak 120.6, delta -0.2661 (-0.22%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#243  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 02:23 UTC -> Sat May 30 2026 02:24 UTC (duration 1.0m).

**Magnitude:** baseline 120.8 (source: prewindow_median), peak 121.2, delta +0.3911 (+0.32%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#244  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 02:33 UTC -> Sat May 30 2026 02:34 UTC (duration 1.0m).

**Magnitude:** baseline 120.9 (source: prewindow_median), peak 121.2, delta +0.2926 (+0.24%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#245  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 02:43 UTC -> Sat May 30 2026 02:44 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_median), peak 121.2, delta +0.1354 (+0.11%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#246  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 02:54 UTC -> Sat May 30 2026 02:55 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_median), peak 120.9, delta -0.2864 (-0.24%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#247  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 03:04 UTC -> Sat May 30 2026 03:05 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_median), peak 121.6, delta +0.5119 (+0.42%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#248  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 03:14 UTC -> Sat May 30 2026 03:15 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_median), peak 121.3, delta +0.09767 (+0.08%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#249  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 03:24 UTC -> Sat May 30 2026 03:25 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_median), peak 121.1, delta -0.1181 (-0.10%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#250  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 03:35 UTC -> Sat May 30 2026 03:36 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_median), peak 121.7, delta +0.4544 (+0.37%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#251  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 03:45 UTC -> Sat May 30 2026 03:46 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_median), peak 120.6, delta -0.6532 (-0.54%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#252  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 03:55 UTC -> Sat May 30 2026 03:56 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_median), peak 121, delta -0.2479 (-0.20%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#253  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 04:05 UTC -> Sat May 30 2026 04:06 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_median), peak 121.2, delta -0.01197 (-0.01%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#254  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 04:16 UTC -> Sat May 30 2026 04:17 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_median), peak 121.6, delta +0.4291 (+0.35%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#255  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 04:26 UTC -> Sat May 30 2026 04:27 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_median), peak 120.5, delta -0.7395 (-0.61%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#256  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 04:36 UTC -> Sat May 30 2026 04:37 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_median), peak 121, delta -0.2297 (-0.19%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#257  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 04:46 UTC -> Sat May 30 2026 04:47 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_median), peak 120.8, delta -0.3065 (-0.25%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#258  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 04:57 UTC -> Sat May 30 2026 04:58 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_median), peak 121.1, delta -0.02178 (-0.02%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#259  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 05:07 UTC -> Sat May 30 2026 05:08 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_median), peak 121.2, delta +0.1384 (+0.11%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#260  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 05:17 UTC -> Sat May 30 2026 05:18 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_median), peak 121, delta -0.06437 (-0.05%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#261  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 05:27 UTC -> Sat May 30 2026 05:28 UTC (duration 1.0m).

**Magnitude:** baseline 121 (source: prewindow_median), peak 121.1, delta +0.08266 (+0.07%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#262  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 05:38 UTC -> Sat May 30 2026 05:39 UTC (duration 1.0m).

**Magnitude:** baseline 121 (source: prewindow_median), peak 121.1, delta +0.1165 (+0.10%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#263  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 05:48 UTC -> Sat May 30 2026 05:49 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_median), peak 121, delta -0.1121 (-0.09%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#264  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 05:58 UTC -> Sat May 30 2026 05:59 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_median), peak 121.2, delta +0.09043 (+0.07%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#265  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 06:08 UTC -> Sat May 30 2026 06:09 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_median), peak 121.8, delta +0.7291 (+0.60%).

**Calendar context:** Saturday, hour 6 (morning), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#266  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 29 2026 09:14 UTC -> Sat May 30 2026 05:42 UTC (duration 20.47h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 103.9, delta +97.38 (+1498.12%).

**Calendar context:** Friday, hour 9 (morning), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#267  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 30 2026 05:02 UTC -> Sat May 30 2026 18:30 UTC (duration 13.47h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 105.6, delta +99.13 (+1525.06%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#268  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 30 2026 17:42 UTC -> Sun May 31 2026 01:54 UTC (duration 8.20h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 102.2, delta +95.7 (+1472.25%).

**Calendar context:** Saturday, hour 17 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#269  —  TP  —  GT: stuck_at, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Wed May 27 2026 16:02 UTC -> Sun May 31 2026 18:02 UTC (duration 4.08d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 121.1 (source: prewindow_median), peak 119.5, delta -1.646 (-1.36%).

**Calendar context:** Wednesday, hour 16 (afternoon), weekday, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 14.5 (threshold 0).

---

## Case outlet_120d#270  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun May 31 2026 01:02 UTC -> Sun May 31 2026 23:57 UTC (duration 22.92h).

**Magnitude:** baseline 6.5 (source: prewindow_median), peak 106.3, delta +99.8 (+1535.41%).

**Calendar context:** Sunday, hour 1 (night), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#271  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun May 31 2026 16:01 UTC -> Sun May 31 2026 23:59 UTC (duration 7.97h).

**Magnitude:** baseline 121.3 (source: prewindow_median), peak 120.1, delta -1.198 (-0.99%).

**Calendar context:** Sunday, hour 16 (afternoon), weekend, May.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 5.82 (threshold 0).

---
