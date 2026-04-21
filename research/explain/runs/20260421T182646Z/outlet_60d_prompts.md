# outlet_60d — explain cases (run 20260421T182646Z)

## Case outlet_60d#000  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 09 2026 11:00 UTC -> Mon Feb 09 2026 11:01 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_median), peak 9999, delta +9998 (+666500.00%).

**Calendar context:** Monday, hour 11 (morning), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 1e+04 (threshold 0).

---

## Case outlet_60d#001  —  TP  —  GT: noise_burst

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Feb 13 2026 12:00 UTC -> Fri Feb 13 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_median), peak -56.11, delta -57.61 (-3840.68%).

**Calendar context:** Friday, hour 12 (afternoon), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -13.8 (threshold 0).

---

## Case outlet_60d#002  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 10:30 UTC -> Sun Feb 15 2026 10:31 UTC (duration 1.0m).

**Magnitude:** baseline 120.2 (source: prewindow_median), peak 141.1, delta +20.96 (+17.44%).

**Calendar context:** Sunday, hour 10 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 141 (threshold 0).

---

## Case outlet_60d#003  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 11:12 UTC -> Sun Feb 15 2026 11:13 UTC (duration 1.0m).

**Magnitude:** baseline 120.1 (source: prewindow_median), peak 140.9, delta +20.88 (+17.39%).

**Calendar context:** Sunday, hour 11 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 141 (threshold 0).

---

## Case outlet_60d#004  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 10:00 UTC -> Sun Feb 15 2026 12:01 UTC (duration 2.02h).

**Magnitude:** baseline 120 (source: prewindow_median), peak 96.77, delta -23.26 (-19.38%).

**Calendar context:** Sunday, hour 10 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 80.1 (threshold 0).

---

## Case outlet_60d#005  —  TP  —  GT: calibration_drift, trend

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

## Case outlet_60d#006  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Feb 20 2026 21:57 UTC -> Sat Feb 21 2026 14:39 UTC (duration 16.70h).

**Magnitude:** baseline 1.5 (source: prewindow_median), peak 116.7, delta +115.2 (+7683.21%).

**Calendar context:** Friday, hour 21 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#007  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Feb 21 2026 13:41 UTC -> Sat Feb 21 2026 18:05 UTC (duration 4.40h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 113.4, delta +96.88 (+587.15%).

**Calendar context:** Saturday, hour 13 (afternoon), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#008  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 00:10 UTC -> Mon Feb 23 2026 00:11 UTC (duration 1.0m).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak -2.912, delta -19.41 (-117.65%).

**Calendar context:** Monday, hour 0 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.91 (threshold 0).

---

## Case outlet_60d#009  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 00:43 UTC -> Mon Feb 23 2026 00:44 UTC (duration 1.0m).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak -2.912, delta -19.41 (-117.65%).

**Calendar context:** Monday, hour 0 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.91 (threshold 0).

---

## Case outlet_60d#010  —  TP  —  GT: level_shift, frequency_change

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

## Case outlet_60d#011  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 03:01 UTC -> Mon Feb 23 2026 03:02 UTC (duration 1.0m).

**Magnitude:** baseline 103.7 (source: prewindow_median), peak -2.912, delta -106.7 (-102.81%).

**Calendar context:** Monday, hour 3 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.91 (threshold 0).

---

## Case outlet_60d#012  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 03:34 UTC -> Mon Feb 23 2026 03:35 UTC (duration 1.0m).

**Magnitude:** baseline 89.97 (source: prewindow_median), peak -2.912, delta -92.88 (-103.24%).

**Calendar context:** Monday, hour 3 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.91 (threshold 0).

---

## Case outlet_60d#013  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 04:06 UTC -> Mon Feb 23 2026 04:07 UTC (duration 1.0m).

**Magnitude:** baseline 44.02 (source: prewindow_median), peak -13.38, delta -57.41 (-130.40%).

**Calendar context:** Monday, hour 4 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -13.4 (threshold 0).

---

## Case outlet_60d#014  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 04:36 UTC -> Mon Feb 23 2026 04:37 UTC (duration 1.0m).

**Magnitude:** baseline 30.79 (source: prewindow_median), peak -1.286, delta -32.07 (-104.18%).

**Calendar context:** Monday, hour 4 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.29 (threshold 0).

---

## Case outlet_60d#015  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 05:10 UTC -> Mon Feb 23 2026 05:11 UTC (duration 1.0m).

**Magnitude:** baseline 28.06 (source: prewindow_median), peak -1.286, delta -29.35 (-104.58%).

**Calendar context:** Monday, hour 5 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.29 (threshold 0).

---

## Case outlet_60d#016  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 05:48 UTC -> Mon Feb 23 2026 05:49 UTC (duration 1.0m).

**Magnitude:** baseline 29.1 (source: prewindow_median), peak -2.331, delta -31.43 (-108.01%).

**Calendar context:** Monday, hour 5 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -2.33 (threshold 0).

---

## Case outlet_60d#017  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 00:43 UTC -> Mon Feb 23 2026 13:26 UTC (duration 12.72h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 145.4, delta +128.9 (+780.95%).

**Calendar context:** Monday, hour 0 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 8.97e+04 (threshold 0).

---

## Case outlet_60d#018  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 12:39 UTC -> Tue Feb 24 2026 00:04 UTC (duration 11.42h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 114.7, delta +98.18 (+595.04%).

**Calendar context:** Monday, hour 12 (afternoon), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#019  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 23:02 UTC -> Tue Feb 24 2026 16:38 UTC (duration 17.60h).

**Magnitude:** baseline 103.7 (source: prewindow_median), peak 16.5, delta -87.21 (-84.09%).

**Calendar context:** Monday, hour 23 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#020  —  TP  —  GT: trend

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

## Case outlet_60d#021  —  TP  —  GT: seasonality_loss, time_of_day

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

## Case outlet_60d#022  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Feb 27 2026 02:55 UTC -> Fri Feb 27 2026 06:22 UTC (duration 3.45h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 186.2, delta +169.7 (+1028.77%).

**Calendar context:** Friday, hour 2 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#023  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Feb 27 2026 05:32 UTC -> Sat Feb 28 2026 02:59 UTC (duration 21.45h).

**Magnitude:** baseline 96.5 (source: prewindow_median), peak 16.5, delta -80 (-82.90%).

**Calendar context:** Friday, hour 5 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#024  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Feb 28 2026 03:21 UTC -> Sat Feb 28 2026 21:31 UTC (duration 18.17h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 192.1, delta +175.6 (+1064.26%).

**Calendar context:** Saturday, hour 3 (night), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#025  —  TP  —  GT: month_shift

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

## Case outlet_60d#026  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Feb 28 2026 20:52 UTC -> Sat Feb 28 2026 23:24 UTC (duration 2.53h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 110.7, delta +94.16 (+570.67%).

**Calendar context:** Saturday, hour 20 (evening), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#027  —  TP  —  GT: time_of_day, weekend_anomaly

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

## Case outlet_60d#028  —  TP  —  GT: month_shift

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

## Case outlet_60d#029  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#030  —  TP  —  GT: weekend_anomaly, dropout

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 05 2026 05:36 UTC -> Thu Mar 05 2026 13:41 UTC (duration 8.08h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 111.4, delta +94.86 (+574.92%).

**Calendar context:** Thursday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#031  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 05 2026 13:25 UTC -> Thu Mar 05 2026 19:39 UTC (duration 6.23h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 114.8, delta +98.31 (+595.81%).

**Calendar context:** Thursday, hour 13 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#032  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 05 2026 19:26 UTC -> Thu Mar 05 2026 21:50 UTC (duration 2.40h).

**Magnitude:** baseline 101.1 (source: prewindow_median), peak 16.5, delta -84.63 (-83.68%).

**Calendar context:** Thursday, hour 19 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#033  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#034  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 06 2026 20:57 UTC -> Fri Mar 06 2026 23:59 UTC (duration 3.03h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 116, delta +99.52 (+603.17%).

**Calendar context:** Friday, hour 20 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#035  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 01:00 UTC -> Sat Mar 07 2026 01:59 UTC (duration 59.0m).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 147.2, delta +90.74 (+160.60%).

**Calendar context:** Saturday, hour 1 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 5.5 (threshold 0).

---

## Case outlet_60d#036  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 05:00 UTC -> Sat Mar 07 2026 06:59 UTC (duration 1.98h).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 148.6, delta +92.11 (+163.03%).

**Calendar context:** Saturday, hour 5 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 7.07 (threshold 0).

---

## Case outlet_60d#037  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 08:00 UTC -> Sat Mar 07 2026 08:59 UTC (duration 59.0m).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 151.8, delta +95.29 (+168.66%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 6.45 (threshold 0).

---

## Case outlet_60d#038  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 11:03 UTC -> Sat Mar 07 2026 11:03 UTC (duration 0s).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak nan, delta +nan (+nan%).

**Calendar context:** Saturday, hour 11 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** multivariate_pca.

**Score:** 3.25e+04 (threshold 0).

---

## Case outlet_60d#039  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 12:55 UTC -> Sat Mar 07 2026 15:03 UTC (duration 2.13h).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 153.2, delta +96.68 (+171.12%).

**Calendar context:** Saturday, hour 12 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** multivariate_pca.

**Score:** 3.73e+04 (threshold 0).

---

## Case outlet_60d#040  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 17:00 UTC -> Sun Mar 08 2026 02:16 UTC (duration 9.27h).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 151.3, delta +94.75 (+167.71%).

**Calendar context:** Saturday, hour 17 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 6.98e+04 (threshold 0).

---

## Case outlet_60d#041  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 02:31 UTC -> Sun Mar 08 2026 09:01 UTC (duration 6.51h).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 153.3, delta +96.84 (+171.40%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, temporal_profile.

**Score:** 4.59e+03 (threshold 0).

---

## Case outlet_60d#042  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 09:01 UTC -> Sun Mar 08 2026 13:59 UTC (duration 4.95h).

**Magnitude:** baseline 150.2 (source: prewindow_median), peak 56.5, delta -93.74 (-62.39%).

**Calendar context:** Sunday, hour 9 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, temporal_profile.

**Score:** 5.25e+03 (threshold 0).

---

## Case outlet_60d#043  —  TP  —  GT: month_shift, duplicate_stale

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

## Case outlet_60d#044  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:30 UTC -> Tue Mar 10 2026 00:31 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_median), peak 126.3, delta +0.3413 (+0.27%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#045  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:40 UTC -> Tue Mar 10 2026 00:41 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126, delta -0.05924 (-0.05%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#046  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:51 UTC -> Tue Mar 10 2026 00:52 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.9, delta -0.1839 (-0.15%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#047  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:01 UTC -> Tue Mar 10 2026 01:02 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.6, delta -0.4125 (-0.33%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#048  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:11 UTC -> Tue Mar 10 2026 01:12 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.9, delta -0.07685 (-0.06%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#049  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:21 UTC -> Tue Mar 10 2026 01:22 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_median), peak 126, delta +0.07243 (+0.06%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#050  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:31 UTC -> Tue Mar 10 2026 01:32 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.2, delta +0.1755 (+0.14%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#051  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:42 UTC -> Tue Mar 10 2026 01:43 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.7, delta -0.2747 (-0.22%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#052  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:52 UTC -> Tue Mar 10 2026 01:53 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.5, delta +0.5505 (+0.44%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#053  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:02 UTC -> Tue Mar 10 2026 02:03 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.3, delta +0.2887 (+0.23%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#054  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:12 UTC -> Tue Mar 10 2026 02:13 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.2, delta +0.1948 (+0.15%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#055  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:22 UTC -> Tue Mar 10 2026 02:23 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.5, delta +0.5245 (+0.42%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#056  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:33 UTC -> Tue Mar 10 2026 02:34 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.1, delta +0.09375 (+0.07%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#057  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:43 UTC -> Tue Mar 10 2026 02:44 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 125.9, delta -0.1808 (-0.14%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#058  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:53 UTC -> Tue Mar 10 2026 02:54 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.3, delta +0.2345 (+0.19%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#059  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:03 UTC -> Tue Mar 10 2026 03:04 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.4, delta -0.7105 (-0.56%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#060  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:13 UTC -> Tue Mar 10 2026 03:14 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 126.3, delta +0.1019 (+0.08%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#061  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:24 UTC -> Tue Mar 10 2026 03:25 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.8, delta -0.4178 (-0.33%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#062  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:34 UTC -> Tue Mar 10 2026 03:35 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.4, delta -0.7889 (-0.63%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#063  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:44 UTC -> Tue Mar 10 2026 03:45 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.8, delta -0.3544 (-0.28%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#064  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:54 UTC -> Tue Mar 10 2026 03:55 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.1, delta -0.01955 (-0.02%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#065  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:04 UTC -> Tue Mar 10 2026 04:05 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.3, delta +0.2701 (+0.21%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#066  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:15 UTC -> Tue Mar 10 2026 04:16 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.1, delta +0.07486 (+0.06%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#067  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:25 UTC -> Tue Mar 10 2026 04:26 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 125.5, delta -0.5175 (-0.41%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#068  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:35 UTC -> Tue Mar 10 2026 04:36 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_median), peak 126.3, delta +0.3651 (+0.29%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#069  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:45 UTC -> Tue Mar 10 2026 04:46 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126, delta -0.02427 (-0.02%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#070  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:55 UTC -> Tue Mar 10 2026 04:56 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.3, delta +0.2418 (+0.19%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#071  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:06 UTC -> Tue Mar 10 2026 05:07 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 125.2, delta -0.8694 (-0.69%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#072  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:16 UTC -> Tue Mar 10 2026 05:17 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.2, delta +0.2109 (+0.17%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#073  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:26 UTC -> Tue Mar 10 2026 05:27 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.2, delta +0.1845 (+0.15%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#074  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:36 UTC -> Tue Mar 10 2026 05:37 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.5, delta +0.3431 (+0.27%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#075  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:46 UTC -> Tue Mar 10 2026 05:47 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 126.1, delta -0.1849 (-0.15%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#076  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:57 UTC -> Tue Mar 10 2026 05:58 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.4, delta -0.8825 (-0.70%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#077  —  TP  —  GT: weekend_anomaly, reporting_rate_change

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

## Case outlet_60d#078  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 10 2026 04:29 UTC -> Tue Mar 10 2026 18:24 UTC (duration 13.92h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 114.4, delta +97.88 (+593.23%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#079  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 10 2026 17:47 UTC -> Wed Mar 11 2026 10:38 UTC (duration 16.85h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 117.1, delta +100.6 (+609.54%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#080  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 11 2026 09:59 UTC -> Wed Mar 11 2026 23:42 UTC (duration 13.72h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 114.6, delta +98.14 (+594.81%).

**Calendar context:** Wednesday, hour 9 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#081  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 103.2 (source: prewindow_median), peak 16.5, delta -86.69 (-84.01%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_60d#082  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 103.2 (source: prewindow_median), peak 16.5, delta -86.69 (-84.01%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_60d#083  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 103.2 (source: prewindow_median), peak 16.5, delta -86.69 (-84.01%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_60d#084  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 11 2026 23:00 UTC -> Thu Mar 12 2026 14:12 UTC (duration 15.20h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 114.7, delta +98.18 (+595.03%).

**Calendar context:** Wednesday, hour 23 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#085  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#086  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 13:21 UTC -> Fri Mar 13 2026 07:36 UTC (duration 18.25h).

**Magnitude:** baseline 102.1 (source: prewindow_median), peak 16.5, delta -85.56 (-83.83%).

**Calendar context:** Thursday, hour 13 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#087  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 13 2026 07:04 UTC -> Fri Mar 13 2026 20:57 UTC (duration 13.88h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 116.6, delta +100.1 (+606.55%).

**Calendar context:** Friday, hour 7 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#088  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 13 2026 20:05 UTC -> Fri Mar 13 2026 23:59 UTC (duration 3.90h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 110.9, delta +94.41 (+572.17%).

**Calendar context:** Friday, hour 20 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#089  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 01:00 UTC -> Sat Mar 14 2026 02:37 UTC (duration 1.62h).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 149.3, delta +92.77 (+164.20%).

**Calendar context:** Saturday, hour 1 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, temporal_profile.

**Score:** 1.3e+03 (threshold 0).

---

## Case outlet_60d#090  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 05:00 UTC -> Sat Mar 14 2026 06:59 UTC (duration 1.98h).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 151.4, delta +94.86 (+167.89%).

**Calendar context:** Saturday, hour 5 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 7.12 (threshold 0).

---

## Case outlet_60d#091  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 08:00 UTC -> Sat Mar 14 2026 08:59 UTC (duration 59.0m).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 143.3, delta +86.76 (+153.56%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 5.42 (threshold 0).

---

## Case outlet_60d#092  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 11:59 UTC -> Sat Mar 14 2026 11:59 UTC (duration 0s).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak nan, delta +nan (+nan%).

**Calendar context:** Saturday, hour 11 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum.

**Score:** 1.29e+03 (threshold 0).

---

## Case outlet_60d#093  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 13:55 UTC -> Sat Mar 14 2026 14:15 UTC (duration 20.0m).

**Magnitude:** baseline 56.5 (source: prewindow_median), peak 150.1, delta +93.56 (+165.58%).

**Calendar context:** Saturday, hour 13 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** multivariate_pca.

**Score:** 3.96e+04 (threshold 0).

---

## Case outlet_60d#094  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

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

## Case outlet_60d#095  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Mar 16 2026 08:31 UTC -> Mon Mar 16 2026 15:26 UTC (duration 6.92h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 116.3, delta +99.77 (+604.66%).

**Calendar context:** Monday, hour 8 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#096  —  TP  —  GT: month_shift, stuck_at

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

## Case outlet_60d#097  —  FP  —  GT: (none)

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

## Case outlet_60d#098  —  FP  —  GT: (none)

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

## Case outlet_60d#099  —  TP  —  GT: month_shift, stuck_at, degradation_trajectory

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

## Case outlet_60d#100  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 20 2026 17:02 UTC -> Sat Mar 21 2026 02:09 UTC (duration 9.12h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 115.2, delta +98.67 (+597.98%).

**Calendar context:** Friday, hour 17 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#101  —  FP  —  GT: (none)

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

## Case outlet_60d#102  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 24 2026 14:43 UTC -> Tue Mar 24 2026 21:01 UTC (duration 6.30h).

**Magnitude:** baseline 93.16 (source: prewindow_median), peak 16.5, delta -76.66 (-82.29%).

**Calendar context:** Tuesday, hour 14 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#103  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 24 2026 20:03 UTC -> Tue Mar 24 2026 22:22 UTC (duration 2.32h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 110, delta +93.5 (+566.67%).

**Calendar context:** Tuesday, hour 20 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#104  —  TP  —  GT: month_shift, degradation_trajectory

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

## Case outlet_60d#105  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 24 2026 21:21 UTC -> Wed Mar 25 2026 10:08 UTC (duration 12.78h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 113, delta +96.46 (+584.61%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#106  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 25 2026 09:32 UTC -> Wed Mar 25 2026 11:54 UTC (duration 2.37h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 109.1, delta +92.6 (+561.18%).

**Calendar context:** Wednesday, hour 9 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#107  —  FP  —  GT: (none)

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

## Case outlet_60d#108  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 27 2026 04:25 UTC -> Fri Mar 27 2026 06:37 UTC (duration 2.20h).

**Magnitude:** baseline 103.5 (source: prewindow_median), peak 16.5, delta -86.99 (-84.06%).

**Calendar context:** Friday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#109  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 27 2026 06:06 UTC -> Fri Mar 27 2026 08:57 UTC (duration 2.85h).

**Magnitude:** baseline 100.2 (source: prewindow_median), peak 16.5, delta -83.69 (-83.53%).

**Calendar context:** Friday, hour 6 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#110  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 27 2026 08:15 UTC -> Fri Mar 27 2026 15:05 UTC (duration 6.83h).

**Magnitude:** baseline 104.6 (source: prewindow_median), peak 16.5, delta -88.13 (-84.23%).

**Calendar context:** Friday, hour 8 (morning), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#111  —  TP  —  GT: month_shift, degradation_trajectory

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

## Case outlet_60d#112  —  FP  —  GT: (none)

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

## Case outlet_60d#113  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 13:32 UTC -> Tue Mar 31 2026 18:59 UTC (duration 5.45h).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 113.7, delta +97.22 (+589.21%).

**Calendar context:** Tuesday, hour 13 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#114  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 17:55 UTC -> Tue Mar 31 2026 22:29 UTC (duration 4.57h).

**Magnitude:** baseline 98.56 (source: prewindow_median), peak 16.5, delta -82.06 (-83.26%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#115  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 21:29 UTC -> Wed Apr 01 2026 23:58 UTC (duration 1.10d).
**Long-duration framing:** spans 1.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_median), peak 118.3, delta +101.8 (+616.85%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_60d#116  —  TP  —  GT: month_shift, degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat Mar 28 2026 22:05 UTC -> Wed Apr 01 2026 23:50 UTC (duration 4.07d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 126.8 (source: prewindow_median), peak 122.9, delta -3.896 (-3.07%).

**Calendar context:** Saturday, hour 22 (evening), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 97.8 (threshold 0).

---
