# waterleak_60d — explain cases (run 20260421T192913Z)

## Case waterleak_60d#000  —  TP  —  GT: out_of_range

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Feb 14 2026 09:00 UTC -> Sat Feb 14 2026 09:01 UTC (duration 1.0m).

**Magnitude:** baseline 22.06 (source: prewindow_2h), peak -999, delta -1021 (-4627.67%).

**Calendar context:** Saturday, hour 9 (morning), weekend, February.
**Same-hour-of-weekday baseline:** peak is -4205.95σ vs. the median of 6 prior Saturday 9:00 samples (peer median 22.85).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-999.0, score=-999.0

**Detectors fired:** data_quality_gate.

**Score:** -999 (threshold 0).

---

## Case waterleak_60d#001  —  TP  —  GT: water_leak_sustained

# Anomaly on sensor leak_basement (capability: water)

**When:** Wed Feb 18 2026 03:00 UTC -> Wed Feb 18 2026 03:00 UTC (duration 0s).

**Magnitude:** baseline 0 (source: prewindow_2h), peak 1, delta +1 (+nan%).

**Calendar context:** Wednesday, hour 3 (night), weekday, February.

**Detector evidence:**
- state_transition: anomaly_type=water_leak_sustained, raw_value=1.0

**Detectors fired:** state_transition.

**Score:** 1 (threshold 0).

---

## Case waterleak_60d#002  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Thu Feb 19 2026 23:55 UTC -> Sat Feb 21 2026 08:05 UTC (duration 1.34d).
**Long-duration framing:** spans 1.3 days; covers 1 weekend day(s).

**Magnitude:** baseline 18.35 (source: prewindow_2h), peak 27.01, delta +8.662 (+47.22%).

**Calendar context:** Thursday, hour 23 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is +44.81σ vs. the median of 18 prior Thursday 23:00 samples (peer median 18.24).

**Detector evidence:**
- cusum: mu=18.345891730488304, sigma=0.22144698739020088, direction=+, delta=8.662179572532583, source=derived_from_prewindow
- temporal_profile: hour_of_day=23, same_hour_median=18.09596584705205, approx_hour_z=23.456759607038794, source=derived_from_same_hour_history

**Detectors fired:** cusum, temporal_profile.

**Score:** 59.1 (threshold 0).

---

## Case waterleak_60d#003  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri Feb 20 2026 00:02 UTC -> Sat Feb 21 2026 06:42 UTC (duration 1.28d).
**Long-duration framing:** spans 1.3 days; covers 1 weekend day(s).

**Magnitude:** baseline 80.98 (source: prewindow_2h), peak 79.8, delta -1.179 (-1.46%).

**Calendar context:** Friday, hour 0 (night), weekday, February.

**Detector evidence:**
- cusum: mu=80.983550907701, sigma=nan, direction=-, delta=-1.1792157136923294, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=80.983550907701, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 25.6 (threshold 0).

---

## Case waterleak_60d#004  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Feb 21 2026 09:11 UTC -> Tue Feb 24 2026 12:06 UTC (duration 3.12d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 25.2 (source: prewindow_2h), peak 20.24, delta -4.953 (-19.66%).

**Calendar context:** Saturday, hour 9 (morning), weekend, February.
**Same-hour-of-weekday baseline:** peak is -0.01σ vs. the median of 15 prior Saturday 9:00 samples (peer median 22.89).

**Detector evidence:**
- cusum: mu=25.197908090834353, sigma=0.37090456192586907, direction=-, delta=-4.953241838062784, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=13.354491549911874, baseline=25.197908090834353, source=derived_from_prewindow
- temporal_profile: hour_of_day=9, same_hour_median=23.4616416086597, approx_hour_z=-0.03488996522878708, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.5 (threshold 0).

---

## Case waterleak_60d#005  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat Feb 21 2026 06:44 UTC -> Wed Feb 25 2026 06:44 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 79.8 (source: prewindow_2h), peak 75.72, delta -4.084 (-5.12%).

**Calendar context:** Saturday, hour 6 (morning), weekend, February.

**Detector evidence:**
- cusum: mu=79.80433519400867, sigma=nan, direction=-, delta=-4.083621092854727, source=derived_from_prewindow

**Detectors fired:** cusum.

**Score:** 33.8 (threshold 0).

---

## Case waterleak_60d#006  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Feb 24 2026 12:17 UTC -> Sat Feb 28 2026 08:02 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.37 (source: prewindow_2h), peak 20.14, delta -7.227 (-26.41%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, February.
**Same-hour-of-weekday baseline:** peak is -4.97σ vs. the median of 20 prior Tuesday 12:00 samples (peer median 24.41).

**Detector evidence:**
- cusum: mu=27.367101442544595, sigma=0.24847702222579887, direction=-, delta=-7.226535126791475, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=29.083313467208633, baseline=27.367101442544595, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=24.200694131580818, approx_hour_z=-3.638582501906296, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.8 (threshold 0).

---

## Case waterleak_60d#007  —  TP  —  GT: unusual_occupancy

# Anomaly on sensor leak_basement (capability: water)

**When:** Sun Mar 01 2026 02:00 UTC -> Sun Mar 01 2026 02:00 UTC (duration 0s).

**Magnitude:** baseline 0 (source: prewindow_2h), peak 1, delta +1 (+nan%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.

**Detector evidence:**
- state_transition: anomaly_type=water_leak_sustained, raw_value=1.0

**Detectors fired:** state_transition.

**Score:** 1 (threshold 0).

---

## Case waterleak_60d#008  —  TP  —  GT: water_leak_sustained

# Anomaly on sensor leak_basement (capability: water)

**When:** Wed Feb 18 2026 03:00 UTC -> Thu Feb 19 2026 04:00 UTC (duration 1.04d).
**Long-duration framing:** spans 1.0 days; covers 0 weekend day(s).

**Magnitude:** baseline 0 (source: prewindow_2h), peak 1, delta +1 (+nan%).

**Calendar context:** Wednesday, hour 3 (night), weekday, February.

**Detector evidence:**
- cusum: mu=0.0, sigma=nan, direction=+, delta=1.0, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=0.0, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca.

**Score:** 5 (threshold 0).

---

## Case waterleak_60d#009  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed Feb 25 2026 06:46 UTC -> Sun Mar 01 2026 06:46 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 75.72 (source: prewindow_2h), peak 71.69, delta -4.031 (-5.32%).

**Calendar context:** Wednesday, hour 6 (morning), weekday, February.
**Same-hour-of-weekday baseline:** peak is -1.61σ vs. the median of 4 prior Wednesday 6:00 samples (peer median 86.34).

**Detector evidence:**
- cusum: mu=75.72071410115394, sigma=nan, direction=-, delta=-4.030918728595211, source=derived_from_prewindow

**Detectors fired:** cusum.

**Score:** 40.4 (threshold 0).

---

## Case waterleak_60d#010  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Feb 28 2026 08:52 UTC -> Tue Mar 03 2026 12:05 UTC (duration 3.13d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 25.09 (source: prewindow_2h), peak 20.28, delta -4.808 (-19.16%).

**Calendar context:** Saturday, hour 8 (morning), weekend, February.
**Same-hour-of-weekday baseline:** peak is -2.34σ vs. the median of 24 prior Saturday 8:00 samples (peer median 23.92).

**Detector evidence:**
- cusum: mu=25.086527976038685, sigma=0.4669342253842396, direction=-, delta=-4.807555637000885, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=10.296001825620628, baseline=25.086527976038685, source=derived_from_prewindow
- temporal_profile: hour_of_day=8, same_hour_median=23.151707551153812, approx_hour_z=-2.031364863096679, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.5 (threshold 0).

---

## Case waterleak_60d#011  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun Mar 01 2026 06:47 UTC -> Thu Mar 05 2026 06:47 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 71.69 (source: prewindow_2h), peak 67.71, delta -3.978 (-5.55%).

**Calendar context:** Sunday, hour 6 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is -1.63σ vs. the median of 5 prior Sunday 6:00 samples (peer median 85.8).

**Detector evidence:**
- cusum: mu=71.68979537255873, sigma=nan, direction=-, delta=-3.977967556476216, source=derived_from_prewindow

**Detectors fired:** cusum.

**Score:** 24.9 (threshold 0).

---

## Case waterleak_60d#012  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu Mar 05 2026 05:21 UTC -> Thu Mar 05 2026 13:15 UTC (duration 7.90h).

**Magnitude:** baseline 68.34 (source: prewindow_24h), peak 67.24, delta -1.095 (-1.60%).

**Calendar context:** Thursday, hour 5 (night), weekday, March.

**Detector evidence:**
- cusum: mu=nan, sigma=nan, direction=-, delta=-1.0945176008985698, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 25.4 (threshold 0).

---

## Case waterleak_60d#013  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu Mar 05 2026 13:16 UTC -> Sat Mar 07 2026 00:36 UTC (duration 1.47d).
**Long-duration framing:** spans 1.5 days; covers 1 weekend day(s).

**Magnitude:** baseline 67.24 (source: prewindow_2h), peak 65.06, delta -2.18 (-3.24%).

**Calendar context:** Thursday, hour 13 (afternoon), weekday, March.

**Detector evidence:**
- cusum: mu=67.24369587038592, sigma=nan, direction=-, delta=-2.180041347011638, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=67.24369587038592, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 27.6 (threshold 0).

---

## Case waterleak_60d#014  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Mar 03 2026 12:16 UTC -> Sat Mar 07 2026 08:01 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.31 (source: prewindow_2h), peak 20.21, delta -7.101 (-26.00%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is -3.13σ vs. the median of 26 prior Tuesday 12:00 samples (peer median 24.5).

**Detector evidence:**
- cusum: mu=27.311849993526813, sigma=0.18816470176504885, direction=-, delta=-7.1010229952249055, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=37.73833736410122, baseline=27.311849993526813, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=24.422476948275076, approx_hour_z=-2.939518085858099, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.5 (threshold 0).

---

## Case waterleak_60d#015  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat Mar 07 2026 00:37 UTC -> Sat Mar 07 2026 18:30 UTC (duration 17.88h).

**Magnitude:** baseline 65.06 (source: prewindow_2h), peak 63.93, delta -1.13 (-1.74%).

**Calendar context:** Saturday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is -1.40σ vs. the median of 5 prior Saturday 0:00 samples (peer median 79.86).

**Detector evidence:**
- cusum: mu=65.06365452337428, sigma=nan, direction=-, delta=-1.1301380085015609, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=65.06365452337428, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 28.7 (threshold 0).

---

## Case waterleak_60d#016  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat Mar 07 2026 18:31 UTC -> Mon Mar 09 2026 12:54 UTC (duration 1.77d).
**Long-duration framing:** spans 1.8 days; covers 2 weekend day(s).

**Magnitude:** baseline 63.93 (source: prewindow_2h), peak 61.39, delta -2.545 (-3.98%).

**Calendar context:** Saturday, hour 18 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is -1.56σ vs. the median of 5 prior Saturday 18:00 samples (peer median 79.25).

**Detector evidence:**
- cusum: mu=63.93351651487272, sigma=nan, direction=-, delta=-2.5450405514396977, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=63.93351651487272, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 31.2 (threshold 0).

---

## Case waterleak_60d#017  —  TP  —  GT: stuck_at

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Mar 07 2026 09:07 UTC -> Tue Mar 10 2026 12:13 UTC (duration 3.13d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 25.02 (source: prewindow_2h), peak 20.35, delta -4.671 (-18.67%).

**Calendar context:** Saturday, hour 9 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.02σ vs. the median of 26 prior Saturday 9:00 samples (peer median 24.38).

**Detector evidence:**
- cusum: mu=25.019358511576087, sigma=0.34995019144488265, direction=-, delta=-4.670662311188245, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=13.346648824233824, baseline=25.019358511576087, source=derived_from_prewindow
- temporal_profile: hour_of_day=9, same_hour_median=23.8902775377192, approx_hour_z=-0.049644300414677024, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.4 (threshold 0).

---

## Case waterleak_60d#018  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon Mar 09 2026 12:55 UTC -> Wed Mar 11 2026 01:12 UTC (duration 1.51d).
**Long-duration framing:** spans 1.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 61.39 (source: prewindow_2h), peak 59.31, delta -2.082 (-3.39%).

**Calendar context:** Monday, hour 12 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.59σ vs. the median of 6 prior Monday 12:00 samples (peer median 80.98).

**Detector evidence:**
- cusum: mu=61.388475963433024, sigma=nan, direction=-, delta=-2.0817787009386777, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=61.388475963433024, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 33.4 (threshold 0).

---

## Case waterleak_60d#019  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed Mar 11 2026 01:13 UTC -> Thu Mar 12 2026 01:12 UTC (duration 23.98h).

**Magnitude:** baseline 59.31 (source: prewindow_2h), peak 57.89, delta -1.414 (-2.38%).

**Calendar context:** Wednesday, hour 1 (night), weekday, March.

**Detector evidence:**
- cusum: mu=59.306697262494346, sigma=nan, direction=-, delta=-1.4138515582867441, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=59.306697262494346, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 34.8 (threshold 0).

---

## Case waterleak_60d#020  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu Mar 12 2026 01:13 UTC -> Fri Mar 13 2026 12:49 UTC (duration 1.48d).
**Long-duration framing:** spans 1.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 57.89 (source: prewindow_2h), peak 55.8, delta -2.096 (-3.62%).

**Calendar context:** Thursday, hour 1 (night), weekday, March.

**Detector evidence:**
- cusum: mu=57.8928457042076, sigma=nan, direction=-, delta=-2.095937545921309, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=57.8928457042076, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 36.9 (threshold 0).

---

## Case waterleak_60d#021  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Mar 10 2026 12:23 UTC -> Sat Mar 14 2026 08:00 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.29 (source: prewindow_2h), peak 20.41, delta -6.879 (-25.21%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is -2.86σ vs. the median of 33 prior Tuesday 12:00 samples (peer median 24.68).

**Detector evidence:**
- cusum: mu=27.28511920292772, sigma=0.21746922180807418, direction=-, delta=-6.878670478206825, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=31.63054716900373, baseline=27.28511920292772, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=24.817240327490087, approx_hour_z=-2.9451622950847742, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.5 (threshold 0).

---

## Case waterleak_60d#022  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri Mar 13 2026 12:50 UTC -> Sun Mar 15 2026 20:43 UTC (duration 2.33d).
**Long-duration framing:** spans 2.3 days; covers 2 weekend day(s).

**Magnitude:** baseline 55.8 (source: prewindow_2h), peak 58.05, delta +2.258 (+4.05%).

**Calendar context:** Friday, hour 12 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.33σ vs. the median of 6 prior Friday 12:00 samples (peer median 76.95).

**Detector evidence:**
- cusum: mu=55.79690815828629, sigma=nan, direction=+, delta=2.257509436823554, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=55.79690815828629, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=55.79690815828629, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 38.6 (threshold 0).

---

## Case waterleak_60d#023  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Mar 14 2026 08:51 UTC -> Tue Mar 17 2026 12:10 UTC (duration 3.14d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 24.96 (source: prewindow_2h), peak 20.38, delta -4.576 (-18.34%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is -3.25σ vs. the median of 36 prior Saturday 8:00 samples (peer median 25.09).

**Detector evidence:**
- cusum: mu=24.95621095971245, sigma=0.3969429416271148, direction=-, delta=-4.57615075123849, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=11.528485007140628, baseline=24.95621095971245, source=derived_from_prewindow
- temporal_profile: hour_of_day=8, same_hour_median=25.119137655510514, approx_hour_z=-3.108014780419038, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.5 (threshold 0).

---

## Case waterleak_60d#024  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun Mar 15 2026 20:44 UTC -> Thu Mar 19 2026 20:44 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 57.64 (source: prewindow_24h), peak 53.23, delta -4.412 (-7.65%).

**Calendar context:** Sunday, hour 20 (evening), weekend, March.

**Detector evidence:**
- cusum: mu=nan, sigma=nan, direction=-, delta=-4.411521522382344, source=derived_from_prewindow

**Detectors fired:** cusum.

**Score:** 39.5 (threshold 0).

---

## Case waterleak_60d#025  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Mar 17 2026 12:20 UTC -> Fri Mar 20 2026 01:20 UTC (duration 2.54d).
**Long-duration framing:** spans 2.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 27.27 (source: prewindow_2h), peak 20.7, delta -6.567 (-24.08%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is -4.19σ vs. the median of 38 prior Tuesday 12:00 samples (peer median 27.08).

**Detector evidence:**
- cusum: mu=27.271539394927622, sigma=0.1887532139656017, direction=-, delta=-6.566750463665926, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=34.79013853964175, baseline=27.271539394927622, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=26.482952871940498, approx_hour_z=-3.8516780691097416, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.6 (threshold 0).

---

## Case waterleak_60d#026  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 01:20 UTC -> Fri Mar 20 2026 03:50 UTC (duration 2.50h).

**Magnitude:** baseline 21.07 (source: prewindow_2h), peak 22, delta +0.9231 (+4.38%).

**Calendar context:** Friday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.76σ vs. the median of 37 prior Friday 1:00 samples (peer median 20.89).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=21.9959761154928, score=6600.0
- multivariate_pca: approx_residual_z=3.7167524775718976, baseline=21.07284028298551, source=derived_from_prewindow
- temporal_profile: hour_of_day=1, same_hour_median=20.75736546441528, approx_hour_z=0.8332162492602315, source=derived_from_same_hour_history

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 6.6e+03 (threshold 0).

---

## Case waterleak_60d#027  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 03:50 UTC -> Fri Mar 20 2026 05:10 UTC (duration 1.33h).

**Magnitude:** baseline 21.75 (source: prewindow_2h), peak 23.1, delta +1.358 (+6.24%).

**Calendar context:** Friday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.02σ vs. the median of 37 prior Friday 3:00 samples (peer median 21.62).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=23.104112094528297, score=3600.0
- multivariate_pca: approx_residual_z=nan, baseline=21.746300304633884, source=derived_from_prewindow
- temporal_profile: hour_of_day=3, same_hour_median=21.652278782803776, approx_hour_z=0.9644703708132986, source=derived_from_same_hour_history

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 3.6e+03 (threshold 0).

---

## Case waterleak_60d#028  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 05:10 UTC -> Fri Mar 20 2026 08:20 UTC (duration 3.17h).

**Magnitude:** baseline 22 (source: prewindow_2h), peak 25.36, delta +3.366 (+15.30%).

**Calendar context:** Friday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.67σ vs. the median of 36 prior Friday 5:00 samples (peer median 23.01).

**Detector evidence:**
- cusum: mu=21.9959761154928, sigma=0.662171796775386, direction=+, delta=3.36578602422874, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=25.36176213972154, score=10200.0
- multivariate_pca: approx_residual_z=5.082949833591964, baseline=21.9959761154928, source=derived_from_prewindow
- temporal_profile: hour_of_day=5, same_hour_median=23.023083729834934, approx_hour_z=1.544412419258896, source=derived_from_same_hour_history

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 1.02e+04 (threshold 0).

---

## Case waterleak_60d#029  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 08:20 UTC -> Fri Mar 20 2026 14:40 UTC (duration 6.33h).

**Magnitude:** baseline 25.26 (source: prewindow_2h), peak 26.22, delta +0.9671 (+3.83%).

**Calendar context:** Friday, hour 8 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.57σ vs. the median of 37 prior Friday 8:00 samples (peer median 25.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=26.223280655811973, score=22800.0
- multivariate_pca: approx_residual_z=nan, baseline=25.25620456640168, source=derived_from_prewindow
- temporal_profile: hour_of_day=8, same_hour_median=25.3145090076006, approx_hour_z=0.6006490185541087, source=derived_from_same_hour_history

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 2.28e+04 (threshold 0).

---

## Case waterleak_60d#030  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 14:40 UTC -> Fri Mar 20 2026 16:30 UTC (duration 1.83h).

**Magnitude:** baseline 23 (source: prewindow_24h), peak 26.22, delta +3.226 (+14.03%).

**Calendar context:** Friday, hour 14 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.04σ vs. the median of 36 prior Friday 14:00 samples (peer median 26.17).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=26.223280655811973, score=6600.0
- multivariate_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow
- temporal_profile: hour_of_day=14, same_hour_median=26.00649704270241, approx_hour_z=0.1420456510166682, source=derived_from_same_hour_history

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 6.6e+03 (threshold 0).

---

## Case waterleak_60d#031  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 16:30 UTC -> Fri Mar 20 2026 18:40 UTC (duration 2.17h).

**Magnitude:** baseline 26.22 (source: prewindow_2h), peak 23.27, delta -2.948 (-11.24%).

**Calendar context:** Friday, hour 16 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.06σ vs. the median of 36 prior Friday 16:00 samples (peer median 24.83).

**Detector evidence:**
- cusum: mu=26.223280655811973, sigma=nan, direction=-, delta=-2.948431179057195, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=23.274849476754778, score=7200.0
- multivariate_pca: approx_residual_z=nan, baseline=26.223280655811973, source=derived_from_prewindow
- temporal_profile: hour_of_day=16, same_hour_median=24.702827254930508, approx_hour_z=-0.9337376294585683, source=derived_from_same_hour_history

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 7.2e+03 (threshold 0).

---

## Case waterleak_60d#032  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 18:40 UTC -> Fri Mar 20 2026 22:20 UTC (duration 3.67h).

**Magnitude:** baseline 23.59 (source: prewindow_2h), peak 21.09, delta -2.498 (-10.59%).

**Calendar context:** Friday, hour 18 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.51σ vs. the median of 37 prior Friday 18:00 samples (peer median 23.3).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=21.09304161724912, score=10200.0
- multivariate_pca: approx_residual_z=nan, baseline=23.590645534818343, source=derived_from_prewindow
- temporal_profile: hour_of_day=18, same_hour_median=23.207197770279283, approx_hour_z=-1.3733006261371148, source=derived_from_same_hour_history

**Detectors fired:** data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 1.02e+04 (threshold 0).

---

## Case waterleak_60d#033  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri Mar 20 2026 22:20 UTC -> Sat Mar 21 2026 08:01 UTC (duration 9.68h).

**Magnitude:** baseline 21.38 (source: prewindow_2h), peak 25.11, delta +3.732 (+17.46%).

**Calendar context:** Friday, hour 22 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +3.00σ vs. the median of 36 prior Friday 22:00 samples (peer median 20.92).

**Detector evidence:**
- cusum: mu=21.378108389014713, sigma=0.13608236817344818, direction=+, delta=3.7321635547046874, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=25.1102719437194, score=6000.0
- multivariate_pca: approx_residual_z=27.425768707579646, baseline=21.378108389014713, source=derived_from_prewindow
- temporal_profile: hour_of_day=22, same_hour_median=20.845505908547526, approx_hour_z=2.8096108446173447, source=derived_from_same_hour_history

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 6e+03 (threshold 0).

---

## Case waterleak_60d#034  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu Mar 19 2026 20:45 UTC -> Mon Mar 23 2026 20:45 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 53.58 (source: prewindow_24h), peak 49.11, delta -4.473 (-8.35%).

**Calendar context:** Thursday, hour 20 (evening), weekday, March.

**Detector evidence:**
- cusum: mu=nan, sigma=nan, direction=-, delta=-4.472814725858775, source=derived_from_prewindow

**Detectors fired:** cusum.

**Score:** 43.6 (threshold 0).

---

## Case waterleak_60d#035  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Mar 21 2026 08:35 UTC -> Tue Mar 24 2026 12:08 UTC (duration 3.15d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 24.69 (source: prewindow_2h), peak 20.36, delta -4.333 (-17.54%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is -3.39σ vs. the median of 40 prior Saturday 8:00 samples (peer median 25.1).

**Detector evidence:**
- cusum: mu=24.694543297686494, sigma=0.44424007740877375, direction=-, delta=-4.332605186284923, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=9.752846279779064, baseline=24.694543297686494, source=derived_from_prewindow
- temporal_profile: hour_of_day=8, same_hour_median=25.30647483814836, approx_hour_z=-3.291779943351977, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.3 (threshold 0).

---

## Case waterleak_60d#036  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon Mar 23 2026 20:46 UTC -> Fri Mar 27 2026 20:46 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 0 weekend day(s).

**Magnitude:** baseline 49.58 (source: prewindow_24h), peak 45.22, delta -4.361 (-8.80%).

**Calendar context:** Monday, hour 20 (evening), weekday, March.

**Detector evidence:**
- cusum: mu=nan, sigma=nan, direction=-, delta=-4.361256227190076, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 47.4 (threshold 0).

---

## Case waterleak_60d#037  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri Mar 27 2026 18:42 UTC -> Sat Mar 28 2026 01:56 UTC (duration 7.23h).

**Magnitude:** baseline 45.22 (source: prewindow_2h), peak 45.14, delta -0.08024 (-0.18%).

**Calendar context:** Friday, hour 18 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.38σ vs. the median of 8 prior Friday 18:00 samples (peer median 69.36).

**Detector evidence:**
- cusum: mu=45.21912291172003, sigma=nan, direction=-, delta=-0.08023577517629832, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=45.21912291172003, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=45.21912291172003, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 47.6 (threshold 0).

---

## Case waterleak_60d#038  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Mar 24 2026 12:19 UTC -> Sat Mar 28 2026 08:06 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.11 (source: prewindow_2h), peak 20.29, delta -6.818 (-25.15%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is -4.64σ vs. the median of 44 prior Tuesday 12:00 samples (peer median 27.13).

**Detector evidence:**
- cusum: mu=27.11050414406433, sigma=0.18054946212449102, direction=-, delta=-6.8183670018103975, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=37.76453788108796, baseline=27.11050414406433, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=26.548971130988267, approx_hour_z=-4.255653907663324, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.7 (threshold 0).

---

## Case waterleak_60d#039  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Mar 28 2026 08:57 UTC -> Tue Mar 31 2026 12:10 UTC (duration 3.13d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 24.81 (source: prewindow_2h), peak 20.21, delta -4.6 (-18.54%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is -3.70σ vs. the median of 48 prior Saturday 8:00 samples (peer median 25.13).

**Detector evidence:**
- cusum: mu=24.81232973493271, sigma=0.43360134035440767, direction=-, delta=-4.599751300574983, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=10.608249727307895, baseline=24.81232973493271, source=derived_from_prewindow
- temporal_profile: hour_of_day=8, same_hour_median=25.406424082885906, approx_hour_z=-3.555006316201047, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.8 (threshold 0).

---

## Case waterleak_60d#040  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat Mar 28 2026 01:57 UTC -> Wed Apr 01 2026 01:57 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 45.14 (source: prewindow_2h), peak 40.97, delta -4.165 (-9.23%).

**Calendar context:** Saturday, hour 1 (night), weekend, March.

**Detector evidence:**
- cusum: mu=45.13888713654373, sigma=nan, direction=-, delta=-4.164833966992482, source=derived_from_prewindow

**Detectors fired:** cusum.

**Score:** 51.7 (threshold 0).

---

## Case waterleak_60d#041  —  TP  —  GT: unusual_occupancy

# Anomaly on sensor leak_basement (capability: water)

**When:** Sun Mar 01 2026 02:00 UTC -> Mon Mar 02 2026 02:10 UTC (duration 1.01d).
**Long-duration framing:** spans 1.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 0 (source: prewindow_2h), peak 1, delta +1 (+nan%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.

**Detector evidence:**
- cusum: mu=0.0, sigma=nan, direction=+, delta=1.0, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=0.0, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca.

**Score:** 5 (threshold 0).

---

## Case waterleak_60d#042  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Mar 31 2026 12:20 UTC -> Wed Apr 01 2026 23:50 UTC (duration 1.48d).
**Long-duration framing:** spans 1.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 27.31 (source: prewindow_2h), peak 21.28, delta -6.035 (-22.10%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is -4.08σ vs. the median of 50 prior Tuesday 12:00 samples (peer median 27.16).

**Detector evidence:**
- cusum: mu=27.31062186210398, sigma=0.18364154762242743, direction=-, delta=-6.034937386262676, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=32.86259272150488, baseline=27.31062186210398, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=26.596612382866113, approx_hour_z=-3.7125034297472124, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.8 (threshold 0).

---
