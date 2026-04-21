# outlet_kettle_60d — explain cases (run 20260421T182646Z)

## Case outlet_kettle_60d#000  —  TP  —  GT: dip

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sat Feb 07 2026 09:00 UTC -> Sat Feb 07 2026 09:01 UTC (duration 1.0m).

**Magnitude:** baseline 0 (source: prewindow_median), peak -800, delta -800 (+nan%).

**Calendar context:** Saturday, hour 9 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -800 (threshold 0).

---

## Case outlet_kettle_60d#001  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 09 2026 11:00 UTC -> Mon Feb 09 2026 11:01 UTC (duration 1.0m).

**Magnitude:** baseline 0 (source: prewindow_median), peak 9999, delta +9999 (+nan%).

**Calendar context:** Monday, hour 11 (morning), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 1e+04 (threshold 0).

---

## Case outlet_kettle_60d#002  —  TP  —  GT: noise_burst

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Fri Feb 13 2026 12:00 UTC -> Fri Feb 13 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline 1423 (source: prewindow_median), peak -384.1, delta -1807 (-126.99%).

**Calendar context:** Friday, hour 12 (afternoon), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -102 (threshold 0).

---

## Case outlet_kettle_60d#003  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 10:30 UTC -> Sun Feb 15 2026 10:31 UTC (duration 1.0m).

**Magnitude:** baseline 120.2 (source: prewindow_median), peak 141.1, delta +20.96 (+17.44%).

**Calendar context:** Sunday, hour 10 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 141 (threshold 0).

---

## Case outlet_kettle_60d#004  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 11:12 UTC -> Sun Feb 15 2026 11:13 UTC (duration 1.0m).

**Magnitude:** baseline 120.1 (source: prewindow_median), peak 140.9, delta +20.88 (+17.39%).

**Calendar context:** Sunday, hour 11 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 141 (threshold 0).

---

## Case outlet_kettle_60d#005  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 10:00 UTC -> Sun Feb 15 2026 12:01 UTC (duration 2.02h).

**Magnitude:** baseline 120 (source: prewindow_median), peak 96.77, delta -23.26 (-19.38%).

**Calendar context:** Sunday, hour 10 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 80.1 (threshold 0).

---

## Case outlet_kettle_60d#006  —  TP  —  GT: calibration_drift, trend

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

## Case outlet_kettle_60d#007  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 00:10 UTC -> Mon Feb 23 2026 00:11 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak -68.19, delta -168.2 (-168.19%).

**Calendar context:** Monday, hour 0 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -68.2 (threshold 0).

---

## Case outlet_kettle_60d#008  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 00:43 UTC -> Mon Feb 23 2026 00:44 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak -33.2, delta -133.2 (-133.20%).

**Calendar context:** Monday, hour 0 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -33.2 (threshold 0).

---

## Case outlet_kettle_60d#009  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 01:16 UTC -> Mon Feb 23 2026 01:17 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak -0.7246, delta -100.7 (-100.72%).

**Calendar context:** Monday, hour 1 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.725 (threshold 0).

---

## Case outlet_kettle_60d#010  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 01:50 UTC -> Mon Feb 23 2026 01:51 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak -68.19, delta -168.2 (-168.19%).

**Calendar context:** Monday, hour 1 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -68.2 (threshold 0).

---

## Case outlet_kettle_60d#011  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 02:23 UTC -> Mon Feb 23 2026 02:24 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak -33.2, delta -133.2 (-133.20%).

**Calendar context:** Monday, hour 2 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -33.2 (threshold 0).

---

## Case outlet_kettle_60d#012  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 02:56 UTC -> Mon Feb 23 2026 02:57 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak -0.7246, delta -100.7 (-100.72%).

**Calendar context:** Monday, hour 2 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -0.725 (threshold 0).

---

## Case outlet_kettle_60d#013  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 03:30 UTC -> Mon Feb 23 2026 03:31 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak -68.19, delta -168.2 (-168.19%).

**Calendar context:** Monday, hour 3 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -68.2 (threshold 0).

---

## Case outlet_kettle_60d#014  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 04:03 UTC -> Mon Feb 23 2026 04:04 UTC (duration 1.0m).

**Magnitude:** baseline 132.5 (source: prewindow_median), peak -28.45, delta -161 (-121.47%).

**Calendar context:** Monday, hour 4 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -28.5 (threshold 0).

---

## Case outlet_kettle_60d#015  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 04:36 UTC -> Mon Feb 23 2026 04:37 UTC (duration 1.0m).

**Magnitude:** baseline 132.5 (source: prewindow_median), peak -29.41, delta -161.9 (-122.19%).

**Calendar context:** Monday, hour 4 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -29.4 (threshold 0).

---

## Case outlet_kettle_60d#016  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 05:10 UTC -> Mon Feb 23 2026 05:11 UTC (duration 1.0m).

**Magnitude:** baseline 132.5 (source: prewindow_median), peak -29.41, delta -161.9 (-122.19%).

**Calendar context:** Monday, hour 5 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -29.4 (threshold 0).

---

## Case outlet_kettle_60d#017  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 05:43 UTC -> Mon Feb 23 2026 05:44 UTC (duration 1.0m).

**Magnitude:** baseline 133.9 (source: prewindow_median), peak -29.41, delta -163.3 (-121.97%).

**Calendar context:** Monday, hour 5 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -29.4 (threshold 0).

---

## Case outlet_kettle_60d#018  —  TP  —  GT: level_shift, frequency_change, seasonality_loss

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Fri Feb 20 2026 21:56 UTC -> Wed Feb 25 2026 00:01 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 0 (source: prewindow_median), peak 1805, delta +1805 (+nan%).

**Calendar context:** Friday, hour 21 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 3.43e+06 (threshold 0).

---

## Case outlet_kettle_60d#019  —  TP  —  GT: trend

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

## Case outlet_kettle_60d#020  —  TP  —  GT: seasonality_loss, time_of_day

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Tue Feb 24 2026 21:57 UTC -> Sun Mar 01 2026 00:02 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 1523 (source: prewindow_median), peak 100, delta -1423 (-93.43%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 4.32e+07 (threshold 0).

---

## Case outlet_kettle_60d#021  —  TP  —  GT: month_shift

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

## Case outlet_kettle_60d#022  —  TP  —  GT: time_of_day, weekend_anomaly

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sat Feb 28 2026 21:58 UTC -> Thu Mar 05 2026 00:03 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1748, delta +1648 (+1648.28%).

**Calendar context:** Saturday, hour 21 (evening), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 4.32e+07 (threshold 0).

---

## Case outlet_kettle_60d#023  —  TP  —  GT: month_shift

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

## Case outlet_kettle_60d#024  —  TP  —  GT: weekend_anomaly, dropout, reporting_rate_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Wed Mar 04 2026 21:59 UTC -> Sun Mar 08 2026 02:36 UTC (duration 3.19d).
**Long-duration framing:** spans 3.2 days; covers 2 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1919, delta +1819 (+1819.35%).

**Calendar context:** Wednesday, hour 21 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 1.1e+07 (threshold 0).

---

## Case outlet_kettle_60d#025  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sun Mar 08 2026 00:32 UTC -> Sun Mar 08 2026 12:49 UTC (duration 12.28h).

**Magnitude:** baseline 300 (source: prewindow_median), peak 1768, delta +1468 (+489.23%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 1.1e+07 (threshold 0).

---

## Case outlet_kettle_60d#026  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sun Mar 08 2026 10:45 UTC -> Sun Mar 08 2026 14:24 UTC (duration 3.65h).

**Magnitude:** baseline 300 (source: prewindow_median), peak 300, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 10 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 1.1e+07 (threshold 0).

---

## Case outlet_kettle_60d#027  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sun Mar 08 2026 12:20 UTC -> Sun Mar 08 2026 18:44 UTC (duration 6.40h).

**Magnitude:** baseline 300 (source: prewindow_median), peak 300, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 12 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 1.1e+07 (threshold 0).

---

## Case outlet_kettle_60d#028  —  TP  —  GT: month_shift, duplicate_stale

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

## Case outlet_kettle_60d#029  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:30 UTC -> Tue Mar 10 2026 00:31 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_median), peak 126.3, delta +0.3413 (+0.27%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#030  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:40 UTC -> Tue Mar 10 2026 00:41 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126, delta -0.05924 (-0.05%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#031  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:51 UTC -> Tue Mar 10 2026 00:52 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.9, delta -0.1839 (-0.15%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#032  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:01 UTC -> Tue Mar 10 2026 01:02 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.6, delta -0.4125 (-0.33%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#033  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:11 UTC -> Tue Mar 10 2026 01:12 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.9, delta -0.07685 (-0.06%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#034  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:21 UTC -> Tue Mar 10 2026 01:22 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_median), peak 126, delta +0.07243 (+0.06%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#035  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:31 UTC -> Tue Mar 10 2026 01:32 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.2, delta +0.1755 (+0.14%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#036  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:42 UTC -> Tue Mar 10 2026 01:43 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.7, delta -0.2747 (-0.22%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#037  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:52 UTC -> Tue Mar 10 2026 01:53 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.5, delta +0.5505 (+0.44%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#038  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:02 UTC -> Tue Mar 10 2026 02:03 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.3, delta +0.2887 (+0.23%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#039  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:12 UTC -> Tue Mar 10 2026 02:13 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.2, delta +0.1948 (+0.15%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#040  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:22 UTC -> Tue Mar 10 2026 02:23 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.5, delta +0.5245 (+0.42%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#041  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:33 UTC -> Tue Mar 10 2026 02:34 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.1, delta +0.09375 (+0.07%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#042  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:43 UTC -> Tue Mar 10 2026 02:44 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 125.9, delta -0.1808 (-0.14%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#043  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:53 UTC -> Tue Mar 10 2026 02:54 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.3, delta +0.2345 (+0.19%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#044  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:03 UTC -> Tue Mar 10 2026 03:04 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.4, delta -0.7105 (-0.56%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#045  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:13 UTC -> Tue Mar 10 2026 03:14 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 126.3, delta +0.1019 (+0.08%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#046  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:24 UTC -> Tue Mar 10 2026 03:25 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.8, delta -0.4178 (-0.33%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#047  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:34 UTC -> Tue Mar 10 2026 03:35 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.4, delta -0.7889 (-0.63%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#048  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:44 UTC -> Tue Mar 10 2026 03:45 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.8, delta -0.3544 (-0.28%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#049  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:54 UTC -> Tue Mar 10 2026 03:55 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.1, delta -0.01955 (-0.02%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#050  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:04 UTC -> Tue Mar 10 2026 04:05 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.3, delta +0.2701 (+0.21%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#051  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:15 UTC -> Tue Mar 10 2026 04:16 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.1, delta +0.07486 (+0.06%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#052  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:25 UTC -> Tue Mar 10 2026 04:26 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 125.5, delta -0.5175 (-0.41%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#053  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:35 UTC -> Tue Mar 10 2026 04:36 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_median), peak 126.3, delta +0.3651 (+0.29%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#054  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:45 UTC -> Tue Mar 10 2026 04:46 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126, delta -0.02427 (-0.02%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#055  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:55 UTC -> Tue Mar 10 2026 04:56 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.3, delta +0.2418 (+0.19%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#056  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:06 UTC -> Tue Mar 10 2026 05:07 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 125.2, delta -0.8694 (-0.69%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#057  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:16 UTC -> Tue Mar 10 2026 05:17 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.2, delta +0.2109 (+0.17%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#058  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:26 UTC -> Tue Mar 10 2026 05:27 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.2, delta +0.1845 (+0.15%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#059  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:36 UTC -> Tue Mar 10 2026 05:37 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.5, delta +0.3431 (+0.27%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#060  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:46 UTC -> Tue Mar 10 2026 05:47 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 126.1, delta -0.1849 (-0.15%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#061  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:57 UTC -> Tue Mar 10 2026 05:58 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.4, delta -0.8825 (-0.70%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#062  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sun Mar 08 2026 16:40 UTC -> Wed Mar 11 2026 23:55 UTC (duration 3.30d).
**Long-duration framing:** spans 3.3 days; covers 1 weekend day(s).

**Magnitude:** baseline 300 (source: prewindow_median), peak 1913, delta +1613 (+537.74%).

**Calendar context:** Sunday, hour 16 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 1.1e+07 (threshold 0).

---

## Case outlet_kettle_60d#063  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#064  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#065  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#066  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#067  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#068  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#069  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#070  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#071  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#072  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#073  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#074  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#075  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_kettle_60d#076  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sun Mar 15 2026 03:28 UTC -> Sun Mar 15 2026 03:29 UTC (duration 1.0m).

**Magnitude:** baseline 312 (source: prewindow_median), peak -1306, delta -1618 (-518.78%).

**Calendar context:** Sunday, hour 3 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -1.17e+03 (threshold 0).

---

## Case outlet_kettle_60d#077  —  TP  —  GT: weekend_anomaly, seasonal_mismatch, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Wed Mar 11 2026 21:51 UTC -> Mon Mar 16 2026 00:59 UTC (duration 4.13d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1892, delta +1792 (+1791.97%).

**Calendar context:** Wednesday, hour 21 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 1.44e+07 (threshold 0).

---

## Case outlet_kettle_60d#078  —  TP  —  GT: month_shift, stuck_at

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

## Case outlet_kettle_60d#079  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sun Mar 15 2026 22:55 UTC -> Fri Mar 20 2026 01:00 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 300 (source: prewindow_median), peak 1731, delta +1431 (+476.89%).

**Calendar context:** Sunday, hour 22 (evening), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 6.17e+06 (threshold 0).

---

## Case outlet_kettle_60d#080  —  TP  —  GT: month_shift, stuck_at, degradation_trajectory

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

## Case outlet_kettle_60d#081  —  FP  —  GT: (none)

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 19 2026 22:56 UTC -> Tue Mar 24 2026 01:01 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1748, delta +1648 (+1647.85%).

**Calendar context:** Thursday, hour 22 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 1.22e+06 (threshold 0).

---

## Case outlet_kettle_60d#082  —  TP  —  GT: month_shift, degradation_trajectory

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

## Case outlet_kettle_60d#083  —  FP  —  GT: (none)

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Mar 23 2026 22:57 UTC -> Sat Mar 28 2026 01:02 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1757, delta +1657 (+1657.27%).

**Calendar context:** Monday, hour 22 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 1.22e+06 (threshold 0).

---

## Case outlet_kettle_60d#084  —  TP  —  GT: month_shift, degradation_trajectory

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

## Case outlet_kettle_60d#085  —  FP  —  GT: (none)

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Fri Mar 27 2026 22:58 UTC -> Wed Apr 01 2026 01:03 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1750, delta +1650 (+1650.37%).

**Calendar context:** Friday, hour 22 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 1.22e+06 (threshold 0).

---

## Case outlet_kettle_60d#086  —  FP  —  GT: (none)

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Tue Mar 31 2026 22:59 UTC -> Wed Apr 01 2026 23:58 UTC (duration 1.04d).
**Long-duration framing:** spans 1.0 days; covers 0 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_median), peak 1800, delta +1700 (+1700.26%).

**Calendar context:** Tuesday, hour 22 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 1.22e+06 (threshold 0).

---

## Case outlet_kettle_60d#087  —  TP  —  GT: month_shift, degradation_trajectory

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
