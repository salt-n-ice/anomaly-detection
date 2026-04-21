# outlet_tv_60d — explain cases (run 20260421T182646Z)

## Case outlet_tv_60d#000  —  TP  —  GT: dip

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Feb 07 2026 21:00 UTC -> Sat Feb 07 2026 21:01 UTC (duration 1.0m).

**Magnitude:** baseline 0.3 (source: prewindow_median), peak -99.7, delta -100 (-33333.33%).

**Calendar context:** Saturday, hour 21 (evening), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -99.7 (threshold 0).

---

## Case outlet_tv_60d#001  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Feb 09 2026 20:00 UTC -> Mon Feb 09 2026 20:01 UTC (duration 1.0m).

**Magnitude:** baseline 0.3 (source: prewindow_median), peak 9999, delta +9999 (+3332900.00%).

**Calendar context:** Monday, hour 20 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 1e+04 (threshold 0).

---

## Case outlet_tv_60d#002  —  TP  —  GT: noise_burst

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Feb 13 2026 21:00 UTC -> Fri Feb 13 2026 21:01 UTC (duration 1.0m).

**Magnitude:** baseline 0.3 (source: prewindow_median), peak -76.51, delta -76.81 (-25604.54%).

**Calendar context:** Friday, hour 21 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -20.1 (threshold 0).

---

## Case outlet_tv_60d#003  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 10:30 UTC -> Sun Feb 15 2026 10:31 UTC (duration 1.0m).

**Magnitude:** baseline 120.2 (source: prewindow_median), peak 141.1, delta +20.96 (+17.44%).

**Calendar context:** Sunday, hour 10 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 141 (threshold 0).

---

## Case outlet_tv_60d#004  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 11:12 UTC -> Sun Feb 15 2026 11:13 UTC (duration 1.0m).

**Magnitude:** baseline 120.1 (source: prewindow_median), peak 140.9, delta +20.88 (+17.39%).

**Calendar context:** Sunday, hour 11 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 141 (threshold 0).

---

## Case outlet_tv_60d#005  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 10:00 UTC -> Sun Feb 15 2026 12:01 UTC (duration 2.02h).

**Magnitude:** baseline 120 (source: prewindow_median), peak 96.77, delta -23.26 (-19.38%).

**Calendar context:** Sunday, hour 10 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** temporal_profile.

**Score:** 80.1 (threshold 0).

---

## Case outlet_tv_60d#006  —  TP  —  GT: calibration_drift, trend

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

## Case outlet_tv_60d#007  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Feb 20 2026 21:55 UTC -> Sat Feb 21 2026 15:59 UTC (duration 18.07h).

**Magnitude:** baseline 0.3 (source: prewindow_median), peak 20.3, delta +20 (+6666.67%).

**Calendar context:** Friday, hour 21 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#008  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Feb 21 2026 15:23 UTC -> Sat Feb 21 2026 23:35 UTC (duration 8.20h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 176.8, delta +156.5 (+770.87%).

**Calendar context:** Saturday, hour 15 (afternoon), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca, temporal_profile.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#009  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Feb 22 2026 00:10 UTC -> Sun Feb 22 2026 20:57 UTC (duration 20.78h).

**Magnitude:** baseline 84.36 (source: prewindow_median), peak 177.6, delta +93.24 (+110.53%).

**Calendar context:** Sunday, hour 0 (night), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#010  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Feb 22 2026 21:42 UTC -> Mon Feb 23 2026 15:59 UTC (duration 18.28h).

**Magnitude:** baseline 148.8 (source: prewindow_median), peak 20.3, delta -128.5 (-86.36%).

**Calendar context:** Sunday, hour 21 (evening), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca, temporal_profile.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#011  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Feb 23 2026 20:10 UTC -> Mon Feb 23 2026 20:11 UTC (duration 1.0m).

**Magnitude:** baseline 152.7 (source: prewindow_median), peak -13.34, delta -166 (-108.74%).

**Calendar context:** Monday, hour 20 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -13.3 (threshold 0).

---

## Case outlet_tv_60d#012  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Feb 23 2026 20:43 UTC -> Mon Feb 23 2026 20:44 UTC (duration 1.0m).

**Magnitude:** baseline 50.44 (source: prewindow_median), peak -6.34, delta -56.78 (-112.57%).

**Calendar context:** Monday, hour 20 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -6.34 (threshold 0).

---

## Case outlet_tv_60d#013  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Feb 23 2026 21:21 UTC -> Mon Feb 23 2026 21:22 UTC (duration 1.0m).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak -6.34, delta -26.64 (-131.23%).

**Calendar context:** Monday, hour 21 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -6.34 (threshold 0).

---

## Case outlet_tv_60d#014  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Feb 23 2026 22:11 UTC -> Mon Feb 23 2026 22:12 UTC (duration 1.0m).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak -6.34, delta -26.64 (-131.23%).

**Calendar context:** Monday, hour 22 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -6.34 (threshold 0).

---

## Case outlet_tv_60d#015  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Feb 23 2026 17:13 UTC -> Mon Feb 23 2026 23:09 UTC (duration 5.93h).

**Magnitude:** baseline 158.6 (source: prewindow_median), peak -13.34, delta -172 (-108.41%).

**Calendar context:** Monday, hour 17 (afternoon), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 1.19e+05 (threshold 0).

---

## Case outlet_tv_60d#016  —  TP  —  GT: trend

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

## Case outlet_tv_60d#017  —  TP  —  GT: frequency_change, seasonality_loss

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Tue Feb 24 2026 01:12 UTC -> Thu Feb 26 2026 20:08 UTC (duration 2.79d).
**Long-duration framing:** spans 2.8 days; covers 0 weekend day(s).

**Magnitude:** baseline 162.3 (source: prewindow_median), peak 20.3, delta -142 (-87.49%).

**Calendar context:** Tuesday, hour 1 (night), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.67e+05 (threshold 0).

---

## Case outlet_tv_60d#018  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Feb 26 2026 22:35 UTC -> Fri Feb 27 2026 07:59 UTC (duration 9.40h).

**Magnitude:** baseline 158.4 (source: prewindow_median), peak 20.3, delta -138.1 (-87.18%).

**Calendar context:** Thursday, hour 22 (evening), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#019  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Feb 27 2026 07:55 UTC -> Sat Feb 28 2026 02:17 UTC (duration 18.37h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 140.3, delta +120 (+591.13%).

**Calendar context:** Friday, hour 7 (morning), weekday, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#020  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Feb 28 2026 01:24 UTC -> Sat Feb 28 2026 03:31 UTC (duration 2.12h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 176.6, delta +156.3 (+769.79%).

**Calendar context:** Saturday, hour 1 (night), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#021  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Feb 28 2026 02:51 UTC -> Sat Feb 28 2026 07:59 UTC (duration 5.13h).

**Magnitude:** baseline 149.7 (source: prewindow_median), peak 20.3, delta -129.4 (-86.44%).

**Calendar context:** Saturday, hour 2 (night), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#022  —  TP  —  GT: month_shift

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

## Case outlet_tv_60d#023  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Feb 28 2026 07:55 UTC -> Sun Mar 01 2026 07:59 UTC (duration 1.00d).
**Long-duration framing:** spans 1.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 173, delta +152.7 (+752.17%).

**Calendar context:** Saturday, hour 7 (morning), weekend, February.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#024  —  TP  —  GT: time_of_day, weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 01 2026 07:55 UTC -> Mon Mar 02 2026 00:22 UTC (duration 16.45h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 140.3, delta +120 (+591.13%).

**Calendar context:** Sunday, hour 7 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#025  —  TP  —  GT: month_shift

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

## Case outlet_tv_60d#026  —  TP  —  GT: weekend_anomaly, dropout

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Mar 02 2026 00:30 UTC -> Fri Mar 06 2026 02:35 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 176.3, delta +156 (+768.51%).

**Calendar context:** Monday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#027  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 06 2026 00:31 UTC -> Fri Mar 06 2026 03:24 UTC (duration 2.88h).

**Magnitude:** baseline 146 (source: prewindow_median), peak 20.3, delta -125.7 (-86.10%).

**Calendar context:** Friday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#028  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 06 2026 03:56 UTC -> Fri Mar 06 2026 15:59 UTC (duration 12.05h).

**Magnitude:** baseline 149.6 (source: prewindow_median), peak 20.3, delta -129.3 (-86.43%).

**Calendar context:** Friday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#029  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 06 2026 15:25 UTC -> Fri Mar 06 2026 22:36 UTC (duration 7.18h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 176.2, delta +155.9 (+767.96%).

**Calendar context:** Friday, hour 15 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#030  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 06 2026 23:09 UTC -> Sun Mar 08 2026 01:38 UTC (duration 1.10d).
**Long-duration framing:** spans 1.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 148.8 (source: prewindow_median), peak 228.3, delta +79.45 (+53.38%).

**Calendar context:** Friday, hour 23 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca, temporal_profile.

**Score:** 6.17e+05 (threshold 0).

---

## Case outlet_tv_60d#031  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Mar 07 2026 23:34 UTC -> Sun Mar 08 2026 05:21 UTC (duration 5.79h).

**Magnitude:** baseline 70.3 (source: prewindow_median), peak 223.2, delta +152.9 (+217.47%).

**Calendar context:** Saturday, hour 23 (evening), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, sub_pca, temporal_profile.

**Score:** 5.97e+05 (threshold 0).

---

## Case outlet_tv_60d#032  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 08 2026 03:17 UTC -> Sun Mar 08 2026 09:41 UTC (duration 6.40h).

**Magnitude:** baseline 200 (source: prewindow_median), peak 70.3, delta -129.7 (-64.86%).

**Calendar context:** Sunday, hour 3 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#033  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 08 2026 07:37 UTC -> Sun Mar 08 2026 11:16 UTC (duration 3.65h).

**Magnitude:** baseline 70.3 (source: prewindow_median), peak 70.3, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 7 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#034  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 08 2026 09:12 UTC -> Sun Mar 08 2026 15:36 UTC (duration 6.40h).

**Magnitude:** baseline 70.3 (source: prewindow_median), peak 70.3, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 9 (morning), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#035  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 08 2026 13:32 UTC -> Sun Mar 08 2026 17:41 UTC (duration 4.15h).

**Magnitude:** baseline 70.3 (source: prewindow_median), peak 70.3, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 13 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#036  —  TP  —  GT: month_shift, duplicate_stale

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

## Case outlet_tv_60d#037  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 08 2026 15:37 UTC -> Mon Mar 09 2026 02:36 UTC (duration 10.98h).

**Magnitude:** baseline 70.3 (source: prewindow_median), peak 174.8, delta +104.5 (+148.72%).

**Calendar context:** Sunday, hour 15 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#038  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Mar 09 2026 01:52 UTC -> Mon Mar 09 2026 15:59 UTC (duration 14.12h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 174.8, delta +154.5 (+761.32%).

**Calendar context:** Monday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 1.47e+05 (threshold 0).

---

## Case outlet_tv_60d#039  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Mar 09 2026 15:05 UTC -> Mon Mar 09 2026 18:08 UTC (duration 3.05h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 172.4, delta +152.1 (+749.40%).

**Calendar context:** Monday, hour 15 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#040  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:30 UTC -> Tue Mar 10 2026 00:31 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_median), peak 126.3, delta +0.3413 (+0.27%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#041  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:40 UTC -> Tue Mar 10 2026 00:41 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126, delta -0.05924 (-0.05%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#042  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:51 UTC -> Tue Mar 10 2026 00:52 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.9, delta -0.1839 (-0.15%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#043  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:01 UTC -> Tue Mar 10 2026 01:02 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.6, delta -0.4125 (-0.33%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#044  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:11 UTC -> Tue Mar 10 2026 01:12 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.9, delta -0.07685 (-0.06%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#045  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:21 UTC -> Tue Mar 10 2026 01:22 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_median), peak 126, delta +0.07243 (+0.06%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#046  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:31 UTC -> Tue Mar 10 2026 01:32 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.2, delta +0.1755 (+0.14%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#047  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:42 UTC -> Tue Mar 10 2026 01:43 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 125.7, delta -0.2747 (-0.22%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#048  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:52 UTC -> Tue Mar 10 2026 01:53 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.5, delta +0.5505 (+0.44%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#049  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:02 UTC -> Tue Mar 10 2026 02:03 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.3, delta +0.2887 (+0.23%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#050  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:12 UTC -> Tue Mar 10 2026 02:13 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.2, delta +0.1948 (+0.15%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#051  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:22 UTC -> Tue Mar 10 2026 02:23 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.5, delta +0.5245 (+0.42%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#052  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:33 UTC -> Tue Mar 10 2026 02:34 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.1, delta +0.09375 (+0.07%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#053  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:43 UTC -> Tue Mar 10 2026 02:44 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 125.9, delta -0.1808 (-0.14%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#054  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:53 UTC -> Tue Mar 10 2026 02:54 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.3, delta +0.2345 (+0.19%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#055  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:03 UTC -> Tue Mar 10 2026 03:04 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.4, delta -0.7105 (-0.56%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#056  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:13 UTC -> Tue Mar 10 2026 03:14 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 126.3, delta +0.1019 (+0.08%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#057  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:24 UTC -> Tue Mar 10 2026 03:25 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.8, delta -0.4178 (-0.33%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#058  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:34 UTC -> Tue Mar 10 2026 03:35 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.4, delta -0.7889 (-0.63%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#059  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:44 UTC -> Tue Mar 10 2026 03:45 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.8, delta -0.3544 (-0.28%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#060  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:54 UTC -> Tue Mar 10 2026 03:55 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.1, delta -0.01955 (-0.02%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#061  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:04 UTC -> Tue Mar 10 2026 04:05 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.3, delta +0.2701 (+0.21%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#062  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:15 UTC -> Tue Mar 10 2026 04:16 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.1, delta +0.07486 (+0.06%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#063  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:25 UTC -> Tue Mar 10 2026 04:26 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 125.5, delta -0.5175 (-0.41%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#064  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:35 UTC -> Tue Mar 10 2026 04:36 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_median), peak 126.3, delta +0.3651 (+0.29%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#065  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:45 UTC -> Tue Mar 10 2026 04:46 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126, delta -0.02427 (-0.02%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#066  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Mar 09 2026 17:07 UTC -> Tue Mar 10 2026 01:55 UTC (duration 8.80h).

**Magnitude:** baseline 151 (source: prewindow_median), peak 20.3, delta -130.7 (-86.56%).

**Calendar context:** Monday, hour 17 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#067  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:55 UTC -> Tue Mar 10 2026 04:56 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.3, delta +0.2418 (+0.19%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#068  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:06 UTC -> Tue Mar 10 2026 05:07 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 125.2, delta -0.8694 (-0.69%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#069  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:16 UTC -> Tue Mar 10 2026 05:17 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_median), peak 126.2, delta +0.2109 (+0.17%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#070  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:26 UTC -> Tue Mar 10 2026 05:27 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.2, delta +0.1845 (+0.15%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#071  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:36 UTC -> Tue Mar 10 2026 05:37 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_median), peak 126.5, delta +0.3431 (+0.27%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#072  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:46 UTC -> Tue Mar 10 2026 05:47 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 126.1, delta -0.1849 (-0.15%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#073  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:57 UTC -> Tue Mar 10 2026 05:58 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_median), peak 125.4, delta -0.8825 (-0.70%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#074  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Tue Mar 10 2026 02:42 UTC -> Wed Mar 11 2026 20:55 UTC (duration 1.76d).
**Long-duration framing:** spans 1.8 days; covers 0 weekend day(s).

**Magnitude:** baseline 149.2 (source: prewindow_median), peak 20.3, delta -128.9 (-86.39%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#075  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Wed Mar 11 2026 21:39 UTC -> Wed Mar 11 2026 23:58 UTC (duration 2.32h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 178.4, delta +158.1 (+778.92%).

**Calendar context:** Wednesday, hour 21 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#076  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_median), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#077  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_median), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#078  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_median), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#079  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_median), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#080  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_median), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#081  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_median), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#082  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_median), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#083  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_median), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#084  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_median), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#085  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_median), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#086  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Wed Mar 11 2026 21:54 UTC -> Thu Mar 12 2026 04:02 UTC (duration 6.13h).

**Magnitude:** baseline 151 (source: prewindow_median), peak 20.3, delta -130.7 (-86.55%).

**Calendar context:** Wednesday, hour 21 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#087  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 03:27 UTC -> Thu Mar 12 2026 21:34 UTC (duration 18.12h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 179.7, delta +159.4 (+785.42%).

**Calendar context:** Thursday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#088  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#089  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 15 2026 02:23 UTC -> Sun Mar 15 2026 02:24 UTC (duration 1.0m).

**Magnitude:** baseline 111.9 (source: prewindow_median), peak -26.32, delta -138.3 (-123.52%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -26.3 (threshold 0).

---

## Case outlet_tv_60d#090  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 21:08 UTC -> Sat Mar 14 2026 23:59 UTC (duration 2.12d).
**Long-duration framing:** spans 2.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 215, delta +194.7 (+959.23%).

**Calendar context:** Thursday, hour 21 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#091  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 15 2026 02:53 UTC -> Sun Mar 15 2026 02:54 UTC (duration 1.0m).

**Magnitude:** baseline -15.26 (source: prewindow_median), peak -17.51, delta -2.25 (+14.74%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** data_quality_gate.

**Score:** -17.5 (threshold 0).

---

## Case outlet_tv_60d#092  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 15 2026 00:19 UTC -> Sun Mar 15 2026 03:17 UTC (duration 2.97h).

**Magnitude:** baseline 70.3 (source: prewindow_median), peak -43.93, delta -114.2 (-162.50%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 5.82e+05 (threshold 0).

---

## Case outlet_tv_60d#093  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 15 2026 03:55 UTC -> Sun Mar 15 2026 23:46 UTC (duration 19.85h).

**Magnitude:** baseline -17.51 (source: prewindow_median), peak 225.2, delta +242.7 (-1386.28%).

**Calendar context:** Sunday, hour 3 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#094  —  TP  —  GT: month_shift, stuck_at

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

## Case outlet_tv_60d#095  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 15 2026 22:54 UTC -> Tue Mar 17 2026 01:27 UTC (duration 1.11d).
**Long-duration framing:** spans 1.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 70.3 (source: prewindow_median), peak 225.2, delta +154.9 (+220.40%).

**Calendar context:** Sunday, hour 22 (evening), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 5.82e+05 (threshold 0).

---

## Case outlet_tv_60d#096  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Tue Mar 17 2026 03:56 UTC -> Tue Mar 17 2026 15:59 UTC (duration 12.05h).

**Magnitude:** baseline 161.7 (source: prewindow_median), peak 20.3, delta -141.4 (-87.44%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca, temporal_profile.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#097  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Tue Mar 17 2026 17:17 UTC -> Wed Mar 18 2026 01:39 UTC (duration 8.37h).

**Magnitude:** baseline 154.6 (source: prewindow_median), peak 20.3, delta -134.3 (-86.87%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#098  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Wed Mar 18 2026 01:03 UTC -> Wed Mar 18 2026 20:20 UTC (duration 19.28h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 174.6, delta +154.3 (+760.11%).

**Calendar context:** Wednesday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#099  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Wed Mar 18 2026 20:36 UTC -> Thu Mar 19 2026 21:24 UTC (duration 1.03d).
**Long-duration framing:** spans 1.0 days; covers 0 weekend day(s).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 180.1, delta +159.8 (+786.99%).

**Calendar context:** Wednesday, hour 20 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#100  —  TP  —  GT: month_shift, stuck_at, degradation_trajectory

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

## Case outlet_tv_60d#101  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 20 2026 01:52 UTC -> Sat Mar 21 2026 03:02 UTC (duration 1.05d).
**Long-duration framing:** spans 1.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 161.7 (source: prewindow_median), peak 20.3, delta -141.4 (-87.44%).

**Calendar context:** Friday, hour 1 (night), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#102  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Mar 21 2026 02:48 UTC -> Sun Mar 22 2026 04:10 UTC (duration 1.06d).
**Long-duration framing:** spans 1.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 174.1, delta +153.8 (+757.84%).

**Calendar context:** Saturday, hour 2 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#103  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 22 2026 03:56 UTC -> Sun Mar 22 2026 17:17 UTC (duration 13.35h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 176, delta +155.7 (+766.88%).

**Calendar context:** Sunday, hour 3 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#104  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 22 2026 19:16 UTC -> Tue Mar 24 2026 18:18 UTC (duration 1.96d).
**Long-duration framing:** spans 2.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 159.2 (source: prewindow_median), peak 20.3, delta -138.9 (-87.25%).

**Calendar context:** Sunday, hour 19 (evening), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#105  —  TP  —  GT: month_shift, degradation_trajectory

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

## Case outlet_tv_60d#106  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Tue Mar 24 2026 17:27 UTC -> Thu Mar 26 2026 20:04 UTC (duration 2.11d).
**Long-duration framing:** spans 2.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 144.4 (source: prewindow_median), peak 20.3, delta -124.1 (-85.94%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#107  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 26 2026 20:09 UTC -> Fri Mar 27 2026 00:30 UTC (duration 4.35h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 178, delta +157.7 (+776.67%).

**Calendar context:** Thursday, hour 20 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#108  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 26 2026 23:46 UTC -> Fri Mar 27 2026 17:04 UTC (duration 17.30h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 179, delta +158.7 (+781.87%).

**Calendar context:** Thursday, hour 23 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#109  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 27 2026 16:24 UTC -> Fri Mar 27 2026 20:48 UTC (duration 4.40h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 177.4, delta +157.1 (+773.71%).

**Calendar context:** Friday, hour 16 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#110  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 27 2026 20:37 UTC -> Sat Mar 28 2026 03:01 UTC (duration 6.40h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 179.9, delta +159.6 (+786.01%).

**Calendar context:** Friday, hour 20 (evening), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#111  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Mar 28 2026 02:00 UTC -> Sat Mar 28 2026 19:50 UTC (duration 17.83h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 179.9, delta +159.6 (+786.45%).

**Calendar context:** Saturday, hour 2 (night), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#112  —  TP  —  GT: month_shift, degradation_trajectory

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

## Case outlet_tv_60d#113  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Mar 28 2026 18:47 UTC -> Sat Mar 28 2026 23:12 UTC (duration 4.42h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 176.3, delta +156 (+768.52%).

**Calendar context:** Saturday, hour 18 (evening), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#114  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Mar 28 2026 23:47 UTC -> Sun Mar 29 2026 16:47 UTC (duration 17.00h).

**Magnitude:** baseline 150.9 (source: prewindow_median), peak 20.3, delta -130.6 (-86.55%).

**Calendar context:** Saturday, hour 23 (evening), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#115  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 29 2026 16:10 UTC -> Tue Mar 31 2026 16:09 UTC (duration 2.00d).
**Long-duration framing:** spans 2.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 178, delta +157.7 (+777.00%).

**Calendar context:** Sunday, hour 16 (afternoon), weekend, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#116  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Tue Mar 31 2026 16:09 UTC -> Tue Mar 31 2026 22:55 UTC (duration 6.77h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 173.7, delta +153.4 (+755.68%).

**Calendar context:** Tuesday, hour 16 (afternoon), weekday, March.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#117  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Wed Apr 01 2026 02:54 UTC -> Wed Apr 01 2026 17:00 UTC (duration 14.10h).

**Magnitude:** baseline 160.2 (source: prewindow_median), peak 20.3, delta -139.9 (-87.33%).

**Calendar context:** Wednesday, hour 2 (night), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#118  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Wed Apr 01 2026 16:29 UTC -> Wed Apr 01 2026 23:55 UTC (duration 7.43h).

**Magnitude:** baseline 20.3 (source: prewindow_median), peak 177.3, delta +157 (+773.50%).

**Calendar context:** Wednesday, hour 16 (afternoon), weekday, April.

**Detector evidence:**
- (per-detector context dicts unavailable on this alert; see detectors list below)

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#119  —  TP  —  GT: month_shift, degradation_trajectory

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
