# waterleak_120d — explain cases (run 20260421T192913Z)

## Case waterleak_120d#000  —  TP  —  GT: out_of_range

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

## Case waterleak_120d#001  —  TP  —  GT: water_leak_sustained

# Anomaly on sensor leak_basement (capability: water)

**When:** Wed Feb 18 2026 03:00 UTC -> Wed Feb 18 2026 03:00 UTC (duration 0s).

**Magnitude:** baseline 0 (source: prewindow_2h), peak 1, delta +1 (+nan%).

**Calendar context:** Wednesday, hour 3 (night), weekday, February.

**Detector evidence:**
- state_transition: anomaly_type=water_leak_sustained, raw_value=1.0

**Detectors fired:** state_transition.

**Score:** 1 (threshold 0).

---

## Case waterleak_120d#002  —  TP  —  GT: calibration_drift

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

## Case waterleak_120d#003  —  FP  —  GT: (none)

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

## Case waterleak_120d#004  —  TP  —  GT: calibration_drift

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

## Case waterleak_120d#005  —  FP  —  GT: (none)

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

## Case waterleak_120d#006  —  TP  —  GT: calibration_drift

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

## Case waterleak_120d#007  —  TP  —  GT: unusual_occupancy

# Anomaly on sensor leak_basement (capability: water)

**When:** Sun Mar 01 2026 02:00 UTC -> Sun Mar 01 2026 02:00 UTC (duration 0s).

**Magnitude:** baseline 0 (source: prewindow_2h), peak 1, delta +1 (+nan%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.

**Detector evidence:**
- state_transition: anomaly_type=water_leak_sustained, raw_value=1.0

**Detectors fired:** state_transition.

**Score:** 1 (threshold 0).

---

## Case waterleak_120d#008  —  TP  —  GT: water_leak_sustained

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

## Case waterleak_120d#009  —  FP  —  GT: (none)

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

## Case waterleak_120d#010  —  FP  —  GT: (none)

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

## Case waterleak_120d#011  —  TP  —  GT: trend

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

## Case waterleak_120d#012  —  TP  —  GT: trend

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

## Case waterleak_120d#013  —  TP  —  GT: trend

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

## Case waterleak_120d#014  —  FP  —  GT: (none)

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

## Case waterleak_120d#015  —  TP  —  GT: trend

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

## Case waterleak_120d#016  —  TP  —  GT: trend

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

## Case waterleak_120d#017  —  TP  —  GT: stuck_at

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

## Case waterleak_120d#018  —  TP  —  GT: trend

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

## Case waterleak_120d#019  —  TP  —  GT: trend

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

## Case waterleak_120d#020  —  TP  —  GT: trend

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

## Case waterleak_120d#021  —  FP  —  GT: (none)

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

## Case waterleak_120d#022  —  TP  —  GT: trend

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

## Case waterleak_120d#023  —  FP  —  GT: (none)

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

## Case waterleak_120d#024  —  FP  —  GT: (none)

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

## Case waterleak_120d#025  —  TP  —  GT: reporting_rate_change

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

## Case waterleak_120d#026  —  TP  —  GT: reporting_rate_change

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

## Case waterleak_120d#027  —  TP  —  GT: reporting_rate_change

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

## Case waterleak_120d#028  —  TP  —  GT: reporting_rate_change

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

## Case waterleak_120d#029  —  TP  —  GT: reporting_rate_change

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

## Case waterleak_120d#030  —  TP  —  GT: reporting_rate_change

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

## Case waterleak_120d#031  —  TP  —  GT: reporting_rate_change

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

## Case waterleak_120d#032  —  TP  —  GT: reporting_rate_change

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

## Case waterleak_120d#033  —  TP  —  GT: reporting_rate_change

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

## Case waterleak_120d#034  —  FP  —  GT: (none)

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

## Case waterleak_120d#035  —  FP  —  GT: (none)

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

## Case waterleak_120d#036  —  FP  —  GT: (none)

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

## Case waterleak_120d#037  —  FP  —  GT: (none)

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

## Case waterleak_120d#038  —  FP  —  GT: (none)

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

## Case waterleak_120d#039  —  FP  —  GT: (none)

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

## Case waterleak_120d#040  —  FP  —  GT: (none)

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

## Case waterleak_120d#041  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Mar 31 2026 12:20 UTC -> Sat Apr 04 2026 08:03 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.31 (source: prewindow_2h), peak 20.43, delta -6.881 (-25.19%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is -4.66σ vs. the median of 50 prior Tuesday 12:00 samples (peer median 27.16).

**Detector evidence:**
- cusum: mu=27.31062186210398, sigma=0.18364154762242743, direction=-, delta=-6.8807115639160195, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=37.46816367537356, baseline=27.31062186210398, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=26.596612382866113, approx_hour_z=-4.302614701727471, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.8 (threshold 0).

---

## Case waterleak_120d#042  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon Apr 06 2026 01:16 UTC -> Tue Apr 07 2026 09:53 UTC (duration 1.36d).
**Long-duration framing:** spans 1.4 days; covers 0 weekend day(s).

**Magnitude:** baseline 36.07 (source: prewindow_2h), peak 34.85, delta -1.218 (-3.38%).

**Calendar context:** Monday, hour 1 (night), weekday, April.

**Detector evidence:**
- cusum: mu=36.069626034156414, sigma=nan, direction=-, delta=-1.2180704247491434, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=36.069626034156414, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=36.069626034156414, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 58 (threshold 0).

---

## Case waterleak_120d#043  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Apr 04 2026 08:53 UTC -> Tue Apr 07 2026 12:14 UTC (duration 3.14d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 24.92 (source: prewindow_2h), peak 20.34, delta -4.583 (-18.39%).

**Calendar context:** Saturday, hour 8 (morning), weekend, April.
**Same-hour-of-weekday baseline:** peak is -3.76σ vs. the median of 54 prior Saturday 8:00 samples (peer median 25.13).

**Detector evidence:**
- cusum: mu=24.91800486259747, sigma=0.43718101266509385, direction=-, delta=-4.582738896388861, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=10.482474681258644, baseline=24.91800486259747, source=derived_from_prewindow
- temporal_profile: hour_of_day=8, same_hour_median=25.45865064263641, approx_hour_z=-3.6016796117372785, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.4 (threshold 0).

---

## Case waterleak_120d#044  —  TP  —  GT: spike

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Apr 07 2026 12:24 UTC -> Sat Apr 11 2026 08:00 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.42 (source: prewindow_2h), peak 45.71, delta +18.29 (+66.68%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, April.
**Same-hour-of-weekday baseline:** peak is +13.09σ vs. the median of 57 prior Tuesday 12:00 samples (peer median 27.25).

**Detector evidence:**
- cusum: mu=27.42137925122843, sigma=0.22775831700169066, direction=+, delta=18.285011084058176, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=80.28251755970977, baseline=27.42137925122843, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=26.67445919054149, approx_hour_z=13.614780749129304, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 180 (threshold 0).

---

## Case waterleak_120d#045  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Apr 11 2026 08:50 UTC -> Tue Apr 14 2026 12:07 UTC (duration 3.14d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 24.89 (source: prewindow_2h), peak 20.37, delta -4.519 (-18.16%).

**Calendar context:** Saturday, hour 8 (morning), weekend, April.
**Same-hour-of-weekday baseline:** peak is -3.87σ vs. the median of 59 prior Saturday 8:00 samples (peer median 25.15).

**Detector evidence:**
- cusum: mu=24.888214498968402, sigma=0.44664697293553773, direction=-, delta=-4.5193328958785415, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=10.11835559116348, baseline=24.888214498968402, source=derived_from_prewindow
- temporal_profile: hour_of_day=8, same_hour_median=25.53744587661187, approx_hour_z=-3.7353034108829317, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.5 (threshold 0).

---

## Case waterleak_120d#046  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon Apr 13 2026 14:51 UTC -> Wed Apr 15 2026 16:44 UTC (duration 2.08d).
**Long-duration framing:** spans 2.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 28.94 (source: prewindow_24h), peak 26.51, delta -2.427 (-8.39%).

**Calendar context:** Monday, hour 14 (afternoon), weekday, April.

**Detector evidence:**
- cusum: mu=nan, sigma=nan, direction=-, delta=-2.4265036489096836, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 66.3 (threshold 0).

---

## Case waterleak_120d#047  —  TP  —  GT: dip

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Apr 14 2026 12:18 UTC -> Sat Apr 18 2026 08:03 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.31 (source: prewindow_2h), peak 12.56, delta -14.74 (-54.00%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, April.
**Same-hour-of-weekday baseline:** peak is -10.69σ vs. the median of 62 prior Tuesday 12:00 samples (peer median 27.26).

**Detector evidence:**
- cusum: mu=27.30518292673876, sigma=0.14283019882675985, direction=-, delta=-14.744660655410122, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=103.23209500880179, baseline=27.30518292673876, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=26.704558751285262, approx_hour_z=-10.407952296770848, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.7 (threshold 0).

---

## Case waterleak_120d#048  —  TP  —  GT: water_leak_sustained

# Anomaly on sensor leak_basement (capability: water)

**When:** Mon Apr 20 2026 02:00 UTC -> Mon Apr 20 2026 02:00 UTC (duration 0s).

**Magnitude:** baseline 0 (source: prewindow_2h), peak 1, delta +1 (+nan%).

**Calendar context:** Monday, hour 2 (night), weekday, April.

**Detector evidence:**
- state_transition: anomaly_type=water_leak_sustained, raw_value=1.0

**Detectors fired:** state_transition.

**Score:** 1 (threshold 0).

---

## Case waterleak_120d#049  —  TP  —  GT: unusual_occupancy

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

## Case waterleak_120d#050  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Apr 18 2026 08:54 UTC -> Tue Apr 21 2026 12:10 UTC (duration 3.14d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 24.91 (source: prewindow_2h), peak 20.35, delta -4.561 (-18.31%).

**Calendar context:** Saturday, hour 8 (morning), weekend, April.
**Same-hour-of-weekday baseline:** peak is -4.02σ vs. the median of 65 prior Saturday 8:00 samples (peer median 25.15).

**Detector evidence:**
- cusum: mu=24.911629097018967, sigma=0.494669372784965, direction=-, delta=-4.560960541675719, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=9.220220196770478, baseline=24.911629097018967, source=derived_from_prewindow
- temporal_profile: hour_of_day=8, same_hour_median=25.58705388675532, approx_hour_z=-3.8781054196068085, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.8 (threshold 0).

---

## Case waterleak_120d#051  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Apr 21 2026 12:21 UTC -> Sat Apr 25 2026 08:05 UTC (duration 3.82d).
**Long-duration framing:** spans 3.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 27.27 (source: prewindow_2h), peak 20.31, delta -6.957 (-25.51%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, April.
**Same-hour-of-weekday baseline:** peak is -5.21σ vs. the median of 68 prior Tuesday 12:00 samples (peer median 27.27).

**Detector evidence:**
- cusum: mu=27.27113338864057, sigma=0.1682903763373083, direction=-, delta=-6.95742133332114, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=41.34176584985595, baseline=27.27113338864057, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=26.736025803591268, approx_hour_z=-4.8625414781924015, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.6 (threshold 0).

---

## Case waterleak_120d#052  —  TP  —  GT: water_leak_sustained

# Anomaly on sensor leak_basement (capability: water)

**When:** Mon Apr 20 2026 02:00 UTC -> Tue Apr 21 2026 04:00 UTC (duration 1.08d).
**Long-duration framing:** spans 1.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 0 (source: prewindow_2h), peak 1, delta +1 (+nan%).

**Calendar context:** Monday, hour 2 (night), weekday, April.

**Detector evidence:**
- cusum: mu=0.0, sigma=nan, direction=+, delta=1.0, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=0.0, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca.

**Score:** 2.01 (threshold 0).

---

## Case waterleak_120d#053  —  TP  —  GT: noise_burst

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Sat Apr 25 2026 09:14 UTC -> Tue Apr 28 2026 12:10 UTC (duration 3.12d).
**Long-duration framing:** spans 3.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 25.59 (source: prewindow_2h), peak 31.53, delta +5.936 (+23.19%).

**Calendar context:** Saturday, hour 9 (morning), weekend, April.
**Same-hour-of-weekday baseline:** peak is +0.13σ vs. the median of 577 prior Saturday 9:00 samples (peer median 25.79).

**Detector evidence:**
- cusum: mu=25.593029434096493, sigma=2.3211062355004404, direction=+, delta=5.935818856515812, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.5573232132720647, baseline=25.593029434096493, source=derived_from_prewindow
- temporal_profile: hour_of_day=9, same_hour_median=26.07358542850944, approx_hour_z=0.16831707629225343, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.4 (threshold 0).

---

## Case waterleak_120d#054  —  FP  —  GT: (none)

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue Apr 28 2026 12:20 UTC -> Fri May 01 2026 23:57 UTC (duration 3.48d).
**Long-duration framing:** spans 3.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 27.27 (source: prewindow_2h), peak 20.57, delta -6.697 (-24.56%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, April.
**Same-hour-of-weekday baseline:** peak is -5.17σ vs. the median of 74 prior Tuesday 12:00 samples (peer median 27.27).

**Detector evidence:**
- cusum: mu=27.27167780980562, sigma=0.1875450966021541, direction=-, delta=-6.696998096698881, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=35.70873468851843, baseline=27.27167780980562, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=26.763655866024955, approx_hour_z=-4.818873937930084, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 59.8 (threshold 0).

---

## Case waterleak_120d#055  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Mon May 04 2026 21:00 UTC -> Mon May 04 2026 21:08 UTC (duration 8.0m).

**Magnitude:** baseline 20.17 (source: prewindow_2h), peak 19.67, delta -0.4924 (-2.44%).

**Calendar context:** Monday, hour 21 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.46σ vs. the median of 78 prior Monday 21:00 samples (peer median 21.56).

**Detector evidence:**
- temporal_profile: hour_of_day=21, same_hour_median=21.448243876526256, approx_hour_z=-1.355324395182777, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 6.91 (threshold 0).

---

## Case waterleak_120d#056  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 05 2026 20:06 UTC -> Tue May 05 2026 20:14 UTC (duration 8.0m).

**Magnitude:** baseline 21.24 (source: prewindow_2h), peak 20.81, delta -0.4305 (-2.03%).

**Calendar context:** Tuesday, hour 20 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.28σ vs. the median of 79 prior Tuesday 20:00 samples (peer median 22.47).

**Detector evidence:**
- temporal_profile: hour_of_day=20, same_hour_median=22.004067568842324, approx_hour_z=-0.9131664807069932, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 5.14 (threshold 0).

---

## Case waterleak_120d#057  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Wed May 06 2026 21:00 UTC -> Wed May 06 2026 21:35 UTC (duration 35.0m).

**Magnitude:** baseline 20.49 (source: prewindow_2h), peak 19.71, delta -0.7777 (-3.80%).

**Calendar context:** Wednesday, hour 21 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.79σ vs. the median of 78 prior Wednesday 21:00 samples (peer median 22.07).

**Detector evidence:**
- temporal_profile: hour_of_day=21, same_hour_median=21.432075278159807, approx_hour_z=-1.309799156431461, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 6.23 (threshold 0).

---

## Case waterleak_120d#058  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Wed May 06 2026 22:00 UTC -> Wed May 06 2026 22:06 UTC (duration 6.0m).

**Magnitude:** baseline 19.87 (source: prewindow_2h), peak 19.51, delta -0.3562 (-1.79%).

**Calendar context:** Wednesday, hour 22 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.68σ vs. the median of 78 prior Wednesday 22:00 samples (peer median 21.66).

**Detector evidence:**
- temporal_profile: hour_of_day=22, same_hour_median=21.03356980324536, approx_hour_z=-1.1547734733720139, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 5.38 (threshold 0).

---

## Case waterleak_120d#059  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 03 2026 17:32 UTC -> Thu May 07 2026 17:32 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 8.901 (source: prewindow_24h), peak 4.41, delta -4.492 (-50.46%).

**Calendar context:** Sunday, hour 17 (afternoon), weekend, May.

**Detector evidence:**
- cusum: mu=nan, sigma=nan, direction=-, delta=-4.491632856028651, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 88.3 (threshold 0).

---

## Case waterleak_120d#060  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Thu May 07 2026 18:00 UTC -> Thu May 07 2026 18:06 UTC (duration 6.0m).

**Magnitude:** baseline 22.64 (source: prewindow_2h), peak 21.91, delta -0.7248 (-3.20%).

**Calendar context:** Thursday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.37σ vs. the median of 78 prior Thursday 18:00 samples (peer median 23.73).

**Detector evidence:**
- temporal_profile: hour_of_day=18, same_hour_median=23.429045098181504, approx_hour_z=-1.1361873073742668, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 5.13 (threshold 0).

---

## Case waterleak_120d#061  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Thu May 07 2026 21:00 UTC -> Thu May 07 2026 21:05 UTC (duration 5.0m).

**Magnitude:** baseline 20.26 (source: prewindow_2h), peak 19.74, delta -0.5206 (-2.57%).

**Calendar context:** Thursday, hour 21 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.61σ vs. the median of 78 prior Thursday 21:00 samples (peer median 21.77).

**Detector evidence:**
- temporal_profile: hour_of_day=21, same_hour_median=21.419840191008255, approx_hour_z=-1.2819787580649709, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 5.53 (threshold 0).

---

## Case waterleak_120d#062  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Thu May 07 2026 22:00 UTC -> Thu May 07 2026 22:09 UTC (duration 9.0m).

**Magnitude:** baseline 19.57 (source: prewindow_2h), peak 19.18, delta -0.3918 (-2.00%).

**Calendar context:** Thursday, hour 22 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.70σ vs. the median of 78 prior Thursday 22:00 samples (peer median 21.43).

**Detector evidence:**
- temporal_profile: hour_of_day=22, same_hour_median=21.023718370882225, approx_hour_z=-1.4022713216760818, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 5.81 (threshold 0).

---

## Case waterleak_120d#063  —  TP  —  GT: calibration_drift

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Fri May 08 2026 21:00 UTC -> Fri May 08 2026 21:13 UTC (duration 13.0m).

**Magnitude:** baseline 19.83 (source: prewindow_2h), peak 19.13, delta -0.6938 (-3.50%).

**Calendar context:** Friday, hour 21 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -2.02σ vs. the median of 74 prior Friday 21:00 samples (peer median 21.38).

**Detector evidence:**
- temporal_profile: hour_of_day=21, same_hour_median=21.415001624355533, approx_hour_z=-1.7321926550205868, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 5.63 (threshold 0).

---

## Case waterleak_120d#064  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 15 2026 06:00 UTC -> Fri May 15 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline 0 (source: prewindow_24h), peak -0.1296, delta -0.1296 (+nan%).

**Calendar context:** Friday, hour 6 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.69σ vs. the median of 14 prior Friday 6:00 samples (peer median 49.25).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.1296, score=-0.1296

**Detectors fired:** data_quality_gate.

**Score:** -0.13 (threshold 0).

---

## Case waterleak_120d#065  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 15 2026 12:00 UTC -> Fri May 15 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline 0 (source: prewindow_24h), peak -0.2592, delta -0.2592 (+nan%).

**Calendar context:** Friday, hour 12 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.69σ vs. the median of 14 prior Friday 12:00 samples (peer median 49.05).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.2592, score=-0.2592

**Detectors fired:** data_quality_gate.

**Score:** -0.259 (threshold 0).

---

## Case waterleak_120d#066  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 15 2026 18:00 UTC -> Fri May 15 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -0.0648 (source: prewindow_24h), peak -0.3888, delta -0.324 (+500.00%).

**Calendar context:** Friday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.68σ vs. the median of 14 prior Friday 18:00 samples (peer median 48.7).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.3888, score=-0.3888

**Detectors fired:** data_quality_gate.

**Score:** -0.389 (threshold 0).

---

## Case waterleak_120d#067  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 11 2026 17:34 UTC -> Fri May 15 2026 17:34 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 0 weekend day(s).

**Magnitude:** baseline 0.8674 (source: prewindow_24h), peak -0.2592, delta -1.127 (-129.88%).

**Calendar context:** Monday, hour 17 (afternoon), weekday, May.

**Detector evidence:**
- cusum: mu=nan, sigma=nan, direction=-, delta=-1.1266026715449575, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 93 (threshold 0).

---

## Case waterleak_120d#068  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 16 2026 00:00 UTC -> Sat May 16 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -0.1944 (source: prewindow_24h), peak -0.5184, delta -0.324 (+166.67%).

**Calendar context:** Saturday, hour 0 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.68σ vs. the median of 14 prior Saturday 0:00 samples (peer median 48.59).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.5184, score=-0.5184

**Detectors fired:** data_quality_gate.

**Score:** -0.518 (threshold 0).

---

## Case waterleak_120d#069  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 16 2026 06:00 UTC -> Sat May 16 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -0.324 (source: prewindow_24h), peak -0.648, delta -0.324 (+100.00%).

**Calendar context:** Saturday, hour 6 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.68σ vs. the median of 14 prior Saturday 6:00 samples (peer median 48.28).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.648, score=-0.648

**Detectors fired:** data_quality_gate.

**Score:** -0.648 (threshold 0).

---

## Case waterleak_120d#070  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 16 2026 12:00 UTC -> Sat May 16 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -0.4536 (source: prewindow_24h), peak -0.7776, delta -0.324 (+71.43%).

**Calendar context:** Saturday, hour 12 (afternoon), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.67σ vs. the median of 14 prior Saturday 12:00 samples (peer median 47.99).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.7776000000000001, score=-0.7776000000000001

**Detectors fired:** data_quality_gate.

**Score:** -0.778 (threshold 0).

---

## Case waterleak_120d#071  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 16 2026 18:00 UTC -> Sat May 16 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -0.5832 (source: prewindow_24h), peak -0.9072, delta -0.324 (+55.56%).

**Calendar context:** Saturday, hour 18 (evening), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.67σ vs. the median of 14 prior Saturday 18:00 samples (peer median 47.77).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.9072, score=-0.9072

**Detectors fired:** data_quality_gate.

**Score:** -0.907 (threshold 0).

---

## Case waterleak_120d#072  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 17 2026 00:00 UTC -> Sun May 17 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -0.7128 (source: prewindow_24h), peak -1.037, delta -0.324 (+45.45%).

**Calendar context:** Sunday, hour 0 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.66σ vs. the median of 15 prior Sunday 0:00 samples (peer median 50.99).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-1.0368, score=-1.0368

**Detectors fired:** data_quality_gate.

**Score:** -1.04 (threshold 0).

---

## Case waterleak_120d#073  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 17 2026 06:00 UTC -> Sun May 17 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -0.8424 (source: prewindow_24h), peak -1.166, delta -0.324 (+38.46%).

**Calendar context:** Sunday, hour 6 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.66σ vs. the median of 15 prior Sunday 6:00 samples (peer median 50.79).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-1.1664, score=-1.1664

**Detectors fired:** data_quality_gate.

**Score:** -1.17 (threshold 0).

---

## Case waterleak_120d#074  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 17 2026 12:00 UTC -> Sun May 17 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -0.972 (source: prewindow_24h), peak -1.296, delta -0.324 (+33.33%).

**Calendar context:** Sunday, hour 12 (afternoon), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.66σ vs. the median of 15 prior Sunday 12:00 samples (peer median 50.55).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-1.296, score=-1.296

**Detectors fired:** data_quality_gate.

**Score:** -1.3 (threshold 0).

---

## Case waterleak_120d#075  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 17 2026 18:00 UTC -> Sun May 17 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -1.102 (source: prewindow_24h), peak -1.426, delta -0.324 (+29.41%).

**Calendar context:** Sunday, hour 18 (evening), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.65σ vs. the median of 15 prior Sunday 18:00 samples (peer median 50.17).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-1.4256, score=-1.4256

**Detectors fired:** data_quality_gate.

**Score:** -1.43 (threshold 0).

---

## Case waterleak_120d#076  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 18 2026 00:00 UTC -> Mon May 18 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -1.231 (source: prewindow_24h), peak -1.555, delta -0.324 (+26.32%).

**Calendar context:** Monday, hour 0 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.65σ vs. the median of 15 prior Monday 0:00 samples (peer median 49.93).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-1.5552, score=-1.5552

**Detectors fired:** data_quality_gate.

**Score:** -1.56 (threshold 0).

---

## Case waterleak_120d#077  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 18 2026 06:00 UTC -> Mon May 18 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -1.361 (source: prewindow_24h), peak -1.685, delta -0.324 (+23.81%).

**Calendar context:** Monday, hour 6 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.65σ vs. the median of 15 prior Monday 6:00 samples (peer median 49.74).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-1.6848, score=-1.6848

**Detectors fired:** data_quality_gate.

**Score:** -1.68 (threshold 0).

---

## Case waterleak_120d#078  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 18 2026 12:00 UTC -> Mon May 18 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -1.49 (source: prewindow_24h), peak -1.814, delta -0.324 (+21.74%).

**Calendar context:** Monday, hour 12 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.64σ vs. the median of 15 prior Monday 12:00 samples (peer median 49.42).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-1.8144, score=-1.8144

**Detectors fired:** data_quality_gate.

**Score:** -1.81 (threshold 0).

---

## Case waterleak_120d#079  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 18 2026 18:00 UTC -> Mon May 18 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -1.62 (source: prewindow_24h), peak -1.944, delta -0.324 (+20.00%).

**Calendar context:** Monday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.63σ vs. the median of 15 prior Monday 18:00 samples (peer median 49.11).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-1.944, score=-1.944

**Detectors fired:** data_quality_gate.

**Score:** -1.94 (threshold 0).

---

## Case waterleak_120d#080  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 19 2026 00:00 UTC -> Tue May 19 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -1.75 (source: prewindow_24h), peak -2.074, delta -0.324 (+18.52%).

**Calendar context:** Tuesday, hour 0 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.63σ vs. the median of 15 prior Tuesday 0:00 samples (peer median 48.95).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.0736, score=-2.0736

**Detectors fired:** data_quality_gate.

**Score:** -2.07 (threshold 0).

---

## Case waterleak_120d#081  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 19 2026 06:00 UTC -> Tue May 19 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -1.879 (source: prewindow_24h), peak -2.203, delta -0.324 (+17.24%).

**Calendar context:** Tuesday, hour 6 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.63σ vs. the median of 15 prior Tuesday 6:00 samples (peer median 48.78).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.2032000000000003, score=-2.2032000000000003

**Detectors fired:** data_quality_gate.

**Score:** -2.2 (threshold 0).

---

## Case waterleak_120d#082  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 19 2026 12:00 UTC -> Tue May 19 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -2.009 (source: prewindow_24h), peak -2.333, delta -0.324 (+16.13%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.63σ vs. the median of 15 prior Tuesday 12:00 samples (peer median 48.52).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.3328, score=-2.3328

**Detectors fired:** data_quality_gate.

**Score:** -2.33 (threshold 0).

---

## Case waterleak_120d#083  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 19 2026 18:00 UTC -> Tue May 19 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -2.138 (source: prewindow_24h), peak -2.462, delta -0.324 (+15.15%).

**Calendar context:** Tuesday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.63σ vs. the median of 15 prior Tuesday 18:00 samples (peer median 48.27).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.4624, score=-2.4624

**Detectors fired:** data_quality_gate.

**Score:** -2.46 (threshold 0).

---

## Case waterleak_120d#084  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 20 2026 00:00 UTC -> Wed May 20 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -2.268 (source: prewindow_24h), peak -2.592, delta -0.324 (+14.29%).

**Calendar context:** Wednesday, hour 0 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.63σ vs. the median of 15 prior Wednesday 0:00 samples (peer median 48.04).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.592, score=-2.592

**Detectors fired:** data_quality_gate.

**Score:** -2.59 (threshold 0).

---

## Case waterleak_120d#085  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 20 2026 06:00 UTC -> Wed May 20 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -2.398 (source: prewindow_24h), peak -2.722, delta -0.324 (+13.51%).

**Calendar context:** Wednesday, hour 6 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.62σ vs. the median of 15 prior Wednesday 6:00 samples (peer median 47.7).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.7216, score=-2.7216

**Detectors fired:** data_quality_gate.

**Score:** -2.72 (threshold 0).

---

## Case waterleak_120d#086  —  TP  —  GT: dropout

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Wed May 20 2026 02:50 UTC -> Wed May 20 2026 05:00 UTC (duration 2.17h).

**Magnitude:** baseline 19.3 (source: prewindow_2h), peak 21.51, delta +2.204 (+11.42%).

**Calendar context:** Wednesday, hour 2 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.30σ vs. the median of 95 prior Wednesday 2:00 samples (peer median 21.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=21.505490760061743, score=7800.0

**Detectors fired:** data_quality_gate.

**Score:** 7.8e+03 (threshold 0).

---

## Case waterleak_120d#087  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 20 2026 12:00 UTC -> Wed May 20 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -2.527 (source: prewindow_24h), peak -2.851, delta -0.324 (+12.82%).

**Calendar context:** Wednesday, hour 12 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.62σ vs. the median of 15 prior Wednesday 12:00 samples (peer median 47.59).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.8512, score=-2.8512

**Detectors fired:** data_quality_gate.

**Score:** -2.85 (threshold 0).

---

## Case waterleak_120d#088  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 20 2026 18:00 UTC -> Wed May 20 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -2.657 (source: prewindow_24h), peak -2.981, delta -0.324 (+12.20%).

**Calendar context:** Wednesday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.62σ vs. the median of 15 prior Wednesday 18:00 samples (peer median 47.19).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.9808, score=-2.9808

**Detectors fired:** data_quality_gate.

**Score:** -2.98 (threshold 0).

---

## Case waterleak_120d#089  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 21 2026 00:00 UTC -> Thu May 21 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -2.786 (source: prewindow_24h), peak -3.11, delta -0.324 (+11.63%).

**Calendar context:** Thursday, hour 0 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.62σ vs. the median of 15 prior Thursday 0:00 samples (peer median 46.96).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-3.1104000000000003, score=-3.1104000000000003

**Detectors fired:** data_quality_gate.

**Score:** -3.11 (threshold 0).

---

## Case waterleak_120d#090  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 21 2026 06:00 UTC -> Thu May 21 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -2.916 (source: prewindow_24h), peak -3.24, delta -0.324 (+11.11%).

**Calendar context:** Thursday, hour 6 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.62σ vs. the median of 15 prior Thursday 6:00 samples (peer median 46.77).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-3.24, score=-3.24

**Detectors fired:** data_quality_gate.

**Score:** -3.24 (threshold 0).

---

## Case waterleak_120d#091  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 21 2026 12:00 UTC -> Thu May 21 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -3.046 (source: prewindow_24h), peak -3.37, delta -0.324 (+10.64%).

**Calendar context:** Thursday, hour 12 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.61σ vs. the median of 15 prior Thursday 12:00 samples (peer median 46.51).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-3.3696, score=-3.3696

**Detectors fired:** data_quality_gate.

**Score:** -3.37 (threshold 0).

---

## Case waterleak_120d#092  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 21 2026 18:00 UTC -> Thu May 21 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -3.175 (source: prewindow_24h), peak -3.499, delta -0.324 (+10.20%).

**Calendar context:** Thursday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.61σ vs. the median of 15 prior Thursday 18:00 samples (peer median 46.27).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-3.4992, score=-3.4992

**Detectors fired:** data_quality_gate.

**Score:** -3.5 (threshold 0).

---

## Case waterleak_120d#093  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 22 2026 00:00 UTC -> Fri May 22 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -3.305 (source: prewindow_24h), peak -3.629, delta -0.324 (+9.80%).

**Calendar context:** Friday, hour 0 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.61σ vs. the median of 15 prior Friday 0:00 samples (peer median 45.98).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-3.6288, score=-3.6288

**Detectors fired:** data_quality_gate.

**Score:** -3.63 (threshold 0).

---

## Case waterleak_120d#094  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 22 2026 06:00 UTC -> Fri May 22 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -3.434 (source: prewindow_24h), peak -3.758, delta -0.324 (+9.43%).

**Calendar context:** Friday, hour 6 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.61σ vs. the median of 15 prior Friday 6:00 samples (peer median 45.75).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-3.7584, score=-3.7584

**Detectors fired:** data_quality_gate.

**Score:** -3.76 (threshold 0).

---

## Case waterleak_120d#095  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 22 2026 12:00 UTC -> Fri May 22 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -3.564 (source: prewindow_24h), peak -3.888, delta -0.324 (+9.09%).

**Calendar context:** Friday, hour 12 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.60σ vs. the median of 15 prior Friday 12:00 samples (peer median 45.49).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-3.888, score=-3.888

**Detectors fired:** data_quality_gate.

**Score:** -3.89 (threshold 0).

---

## Case waterleak_120d#096  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Fri May 22 2026 18:00 UTC -> Fri May 22 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -3.694 (source: prewindow_24h), peak -4.018, delta -0.324 (+8.77%).

**Calendar context:** Friday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.60σ vs. the median of 15 prior Friday 18:00 samples (peer median 45.22).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-4.0176, score=-4.0176

**Detectors fired:** data_quality_gate.

**Score:** -4.02 (threshold 0).

---

## Case waterleak_120d#097  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 23 2026 00:00 UTC -> Sat May 23 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -3.823 (source: prewindow_24h), peak -4.147, delta -0.324 (+8.47%).

**Calendar context:** Saturday, hour 0 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.60σ vs. the median of 15 prior Saturday 0:00 samples (peer median 45.14).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-4.1472, score=-4.1472

**Detectors fired:** data_quality_gate.

**Score:** -4.15 (threshold 0).

---

## Case waterleak_120d#098  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 23 2026 06:00 UTC -> Sat May 23 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -3.953 (source: prewindow_24h), peak -4.277, delta -0.324 (+8.20%).

**Calendar context:** Saturday, hour 6 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.59σ vs. the median of 15 prior Saturday 6:00 samples (peer median 44.75).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-4.2768, score=-4.2768

**Detectors fired:** data_quality_gate.

**Score:** -4.28 (threshold 0).

---

## Case waterleak_120d#099  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 23 2026 12:00 UTC -> Sat May 23 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -4.082 (source: prewindow_24h), peak -4.406, delta -0.324 (+7.94%).

**Calendar context:** Saturday, hour 12 (afternoon), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.59σ vs. the median of 15 prior Saturday 12:00 samples (peer median 44.52).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-4.4064000000000005, score=-4.4064000000000005

**Detectors fired:** data_quality_gate.

**Score:** -4.41 (threshold 0).

---

## Case waterleak_120d#100  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sat May 23 2026 18:00 UTC -> Sat May 23 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -4.212 (source: prewindow_24h), peak -4.536, delta -0.324 (+7.69%).

**Calendar context:** Saturday, hour 18 (evening), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.59σ vs. the median of 15 prior Saturday 18:00 samples (peer median 44.3).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-4.5360000000000005, score=-4.5360000000000005

**Detectors fired:** data_quality_gate.

**Score:** -4.54 (threshold 0).

---

## Case waterleak_120d#101  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 24 2026 00:00 UTC -> Sun May 24 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -4.342 (source: prewindow_24h), peak -4.666, delta -0.324 (+7.46%).

**Calendar context:** Sunday, hour 0 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.59σ vs. the median of 16 prior Sunday 0:00 samples (peer median 47.49).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-4.6656, score=-4.6656

**Detectors fired:** data_quality_gate.

**Score:** -4.67 (threshold 0).

---

## Case waterleak_120d#102  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 24 2026 06:00 UTC -> Sun May 24 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -4.471 (source: prewindow_24h), peak -4.795, delta -0.324 (+7.25%).

**Calendar context:** Sunday, hour 6 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.58σ vs. the median of 16 prior Sunday 6:00 samples (peer median 47.27).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-4.7952, score=-4.7952

**Detectors fired:** data_quality_gate.

**Score:** -4.8 (threshold 0).

---

## Case waterleak_120d#103  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 24 2026 12:00 UTC -> Sun May 24 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -4.601 (source: prewindow_24h), peak -4.925, delta -0.324 (+7.04%).

**Calendar context:** Sunday, hour 12 (afternoon), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.58σ vs. the median of 16 prior Sunday 12:00 samples (peer median 47.05).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-4.9248, score=-4.9248

**Detectors fired:** data_quality_gate.

**Score:** -4.92 (threshold 0).

---

## Case waterleak_120d#104  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 24 2026 18:00 UTC -> Sun May 24 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -4.73 (source: prewindow_24h), peak -5.054, delta -0.324 (+6.85%).

**Calendar context:** Sunday, hour 18 (evening), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.58σ vs. the median of 16 prior Sunday 18:00 samples (peer median 46.72).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-5.0544, score=-5.0544

**Detectors fired:** data_quality_gate.

**Score:** -5.05 (threshold 0).

---

## Case waterleak_120d#105  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 25 2026 00:00 UTC -> Mon May 25 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -4.86 (source: prewindow_24h), peak -5.184, delta -0.324 (+6.67%).

**Calendar context:** Monday, hour 0 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.58σ vs. the median of 16 prior Monday 0:00 samples (peer median 46.49).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-5.184, score=-5.184

**Detectors fired:** data_quality_gate.

**Score:** -5.18 (threshold 0).

---

## Case waterleak_120d#106  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 25 2026 06:00 UTC -> Mon May 25 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -4.99 (source: prewindow_24h), peak -5.314, delta -0.324 (+6.49%).

**Calendar context:** Monday, hour 6 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.57σ vs. the median of 16 prior Monday 6:00 samples (peer median 46.26).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-5.3136, score=-5.3136

**Detectors fired:** data_quality_gate.

**Score:** -5.31 (threshold 0).

---

## Case waterleak_120d#107  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 25 2026 12:00 UTC -> Mon May 25 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -5.119 (source: prewindow_24h), peak -5.443, delta -0.324 (+6.33%).

**Calendar context:** Monday, hour 12 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.57σ vs. the median of 16 prior Monday 12:00 samples (peer median 45.96).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-5.4432, score=-5.4432

**Detectors fired:** data_quality_gate.

**Score:** -5.44 (threshold 0).

---

## Case waterleak_120d#108  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Mon May 25 2026 18:00 UTC -> Mon May 25 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -5.249 (source: prewindow_24h), peak -5.573, delta -0.324 (+6.17%).

**Calendar context:** Monday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.56σ vs. the median of 16 prior Monday 18:00 samples (peer median 45.69).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-5.5728, score=-5.5728

**Detectors fired:** data_quality_gate.

**Score:** -5.57 (threshold 0).

---

## Case waterleak_120d#109  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 26 2026 00:00 UTC -> Tue May 26 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -5.378 (source: prewindow_24h), peak -5.702, delta -0.324 (+6.02%).

**Calendar context:** Tuesday, hour 0 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.56σ vs. the median of 16 prior Tuesday 0:00 samples (peer median 45.44).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-5.7024, score=-5.7024

**Detectors fired:** data_quality_gate.

**Score:** -5.7 (threshold 0).

---

## Case waterleak_120d#110  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Mon May 25 2026 23:50 UTC -> Tue May 26 2026 01:20 UTC (duration 1.50h).

**Magnitude:** baseline 18.67 (source: prewindow_2h), peak 18.42, delta -0.2535 (-1.36%).

**Calendar context:** Monday, hour 23 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.84σ vs. the median of 101 prior Monday 23:00 samples (peer median 20.94).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=18.41753914408772, score=5400.0

**Detectors fired:** data_quality_gate.

**Score:** 5.4e+03 (threshold 0).

---

## Case waterleak_120d#111  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 02:00 UTC -> Tue May 26 2026 04:50 UTC (duration 2.83h).

**Magnitude:** baseline 19.13 (source: prewindow_2h), peak 21.14, delta +2.01 (+10.50%).

**Calendar context:** Tuesday, hour 2 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.52σ vs. the median of 96 prior Tuesday 2:00 samples (peer median 21.85).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=21.142784749098297, score=10200.0

**Detectors fired:** data_quality_gate.

**Score:** 1.02e+04 (threshold 0).

---

## Case waterleak_120d#112  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 26 2026 06:00 UTC -> Tue May 26 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -5.508 (source: prewindow_24h), peak -5.832, delta -0.324 (+5.88%).

**Calendar context:** Tuesday, hour 6 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.56σ vs. the median of 16 prior Tuesday 6:00 samples (peer median 45.25).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-5.832, score=-5.832

**Detectors fired:** data_quality_gate.

**Score:** -5.83 (threshold 0).

---

## Case waterleak_120d#113  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 04:50 UTC -> Tue May 26 2026 05:50 UTC (duration 1.00h).

**Magnitude:** baseline 22.42 (source: prewindow_24h), peak 21.14, delta -1.279 (-5.70%).

**Calendar context:** Tuesday, hour 4 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.31σ vs. the median of 96 prior Tuesday 4:00 samples (peer median 22.97).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=21.142784749098297, score=3600.0

**Detectors fired:** data_quality_gate.

**Score:** 3.6e+03 (threshold 0).

---

## Case waterleak_120d#114  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 07:10 UTC -> Tue May 26 2026 09:40 UTC (duration 2.50h).

**Magnitude:** baseline 21.58 (source: prewindow_2h), peak 24.44, delta +2.862 (+13.26%).

**Calendar context:** Tuesday, hour 7 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.55σ vs. the median of 96 prior Tuesday 7:00 samples (peer median 25.22).

**Detector evidence:**
- cusum: mu=21.578992255456644, sigma=0.3467230347242995, direction=+, delta=2.861875944919955, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=24.4408682003766, score=8400.0

**Detectors fired:** cusum, data_quality_gate.

**Score:** 8.4e+03 (threshold 0).

---

## Case waterleak_120d#115  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 09:40 UTC -> Tue May 26 2026 11:10 UTC (duration 1.50h).

**Magnitude:** baseline 24.03 (source: prewindow_2h), peak 24.82, delta +0.7961 (+3.31%).

**Calendar context:** Tuesday, hour 9 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.25σ vs. the median of 97 prior Tuesday 9:00 samples (peer median 26.54).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=24.822340629799346, score=5400.0

**Detectors fired:** data_quality_gate.

**Score:** 5.4e+03 (threshold 0).

---

## Case waterleak_120d#116  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 26 2026 12:00 UTC -> Tue May 26 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -5.638 (source: prewindow_24h), peak -5.962, delta -0.324 (+5.75%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.56σ vs. the median of 16 prior Tuesday 12:00 samples (peer median 45.01).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-5.9616, score=-5.9616

**Detectors fired:** data_quality_gate.

**Score:** -5.96 (threshold 0).

---

## Case waterleak_120d#117  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 11:40 UTC -> Tue May 26 2026 14:40 UTC (duration 3.00h).

**Magnitude:** baseline 24.82 (source: prewindow_2h), peak 23.84, delta -0.9821 (-3.96%).

**Calendar context:** Tuesday, hour 11 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -2.50σ vs. the median of 98 prior Tuesday 11:00 samples (peer median 27.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=23.84020577008488, score=10800.0

**Detectors fired:** data_quality_gate.

**Score:** 1.08e+04 (threshold 0).

---

## Case waterleak_120d#118  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 14:40 UTC -> Tue May 26 2026 15:50 UTC (duration 1.17h).

**Magnitude:** baseline 21.04 (source: prewindow_24h), peak 23.84, delta +2.805 (+13.33%).

**Calendar context:** Tuesday, hour 14 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -2.01σ vs. the median of 96 prior Tuesday 14:00 samples (peer median 26.61).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=23.84020577008488, score=4200.0

**Detectors fired:** data_quality_gate.

**Score:** 4.2e+03 (threshold 0).

---

## Case waterleak_120d#119  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Tue May 26 2026 18:00 UTC -> Tue May 26 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -5.767 (source: prewindow_24h), peak -6.091, delta -0.324 (+5.62%).

**Calendar context:** Tuesday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.56σ vs. the median of 16 prior Tuesday 18:00 samples (peer median 44.78).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.0912, score=-6.0912

**Detectors fired:** data_quality_gate.

**Score:** -6.09 (threshold 0).

---

## Case waterleak_120d#120  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 15:50 UTC -> Tue May 26 2026 17:00 UTC (duration 1.17h).

**Magnitude:** baseline 23.84 (source: prewindow_2h), peak 22.63, delta -1.214 (-5.09%).

**Calendar context:** Tuesday, hour 15 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -2.45σ vs. the median of 96 prior Tuesday 15:00 samples (peer median 26.02).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=22.626201610468154, score=4200.0

**Detectors fired:** data_quality_gate.

**Score:** 4.2e+03 (threshold 0).

---

## Case waterleak_120d#121  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 17:00 UTC -> Tue May 26 2026 19:40 UTC (duration 2.67h).

**Magnitude:** baseline 23.33 (source: prewindow_2h), peak 20.59, delta -2.742 (-11.75%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -2.85σ vs. the median of 96 prior Tuesday 17:00 samples (peer median 24.58).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=20.586063184817636, score=9600.0

**Detectors fired:** data_quality_gate.

**Score:** 9.6e+03 (threshold 0).

---

## Case waterleak_120d#122  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor leak_temperature (capability: temperature)

**When:** Tue May 26 2026 19:40 UTC -> Tue May 26 2026 21:50 UTC (duration 2.17h).

**Magnitude:** baseline 19.43 (source: prewindow_24h), peak 20.59, delta +1.154 (+5.94%).

**Calendar context:** Tuesday, hour 19 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.77σ vs. the median of 96 prior Tuesday 19:00 samples (peer median 23.04).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=20.586063184817636, score=7800.0

**Detectors fired:** data_quality_gate.

**Score:** 7.8e+03 (threshold 0).

---

## Case waterleak_120d#123  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 27 2026 00:00 UTC -> Wed May 27 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -5.897 (source: prewindow_24h), peak -6.221, delta -0.324 (+5.49%).

**Calendar context:** Wednesday, hour 0 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.56σ vs. the median of 16 prior Wednesday 0:00 samples (peer median 44.51).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.2208000000000006, score=-6.2208000000000006

**Detectors fired:** data_quality_gate.

**Score:** -6.22 (threshold 0).

---

## Case waterleak_120d#124  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 27 2026 06:00 UTC -> Wed May 27 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -6.026 (source: prewindow_24h), peak -6.35, delta -0.324 (+5.38%).

**Calendar context:** Wednesday, hour 6 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.55σ vs. the median of 16 prior Wednesday 6:00 samples (peer median 44.23).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.3504000000000005, score=-6.3504000000000005

**Detectors fired:** data_quality_gate.

**Score:** -6.35 (threshold 0).

---

## Case waterleak_120d#125  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 27 2026 12:00 UTC -> Wed May 27 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -6.156 (source: prewindow_24h), peak -6.48, delta -0.324 (+5.26%).

**Calendar context:** Wednesday, hour 12 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.55σ vs. the median of 16 prior Wednesday 12:00 samples (peer median 44.06).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.48, score=-6.48

**Detectors fired:** data_quality_gate.

**Score:** -6.48 (threshold 0).

---

## Case waterleak_120d#126  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 27 2026 18:00 UTC -> Wed May 27 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -6.286 (source: prewindow_24h), peak -6.61, delta -0.324 (+5.15%).

**Calendar context:** Wednesday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.55σ vs. the median of 16 prior Wednesday 18:00 samples (peer median 43.74).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.6096, score=-6.6096

**Detectors fired:** data_quality_gate.

**Score:** -6.61 (threshold 0).

---

## Case waterleak_120d#127  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 28 2026 00:00 UTC -> Thu May 28 2026 00:01 UTC (duration 1.0m).

**Magnitude:** baseline -6.415 (source: prewindow_24h), peak -6.739, delta -0.324 (+5.05%).

**Calendar context:** Thursday, hour 0 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.55σ vs. the median of 16 prior Thursday 0:00 samples (peer median 43.48).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.7392, score=-6.7392

**Detectors fired:** data_quality_gate.

**Score:** -6.74 (threshold 0).

---

## Case waterleak_120d#128  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 28 2026 06:00 UTC -> Thu May 28 2026 06:01 UTC (duration 1.0m).

**Magnitude:** baseline -6.545 (source: prewindow_24h), peak -6.869, delta -0.324 (+4.95%).

**Calendar context:** Thursday, hour 6 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.54σ vs. the median of 16 prior Thursday 6:00 samples (peer median 43.19).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.8688, score=-6.8688

**Detectors fired:** data_quality_gate.

**Score:** -6.87 (threshold 0).

---

## Case waterleak_120d#129  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 28 2026 12:00 UTC -> Thu May 28 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline -6.674 (source: prewindow_24h), peak -6.998, delta -0.324 (+4.85%).

**Calendar context:** Thursday, hour 12 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.54σ vs. the median of 16 prior Thursday 12:00 samples (peer median 42.96).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.9984, score=-6.9984

**Detectors fired:** data_quality_gate.

**Score:** -7 (threshold 0).

---

## Case waterleak_120d#130  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Thu May 28 2026 18:00 UTC -> Thu May 28 2026 18:01 UTC (duration 1.0m).

**Magnitude:** baseline -6.804 (source: prewindow_24h), peak -7.128, delta -0.324 (+4.76%).

**Calendar context:** Thursday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.54σ vs. the median of 16 prior Thursday 18:00 samples (peer median 42.74).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-7.128, score=-7.128

**Detectors fired:** data_quality_gate.

**Score:** -7.13 (threshold 0).

---

## Case waterleak_120d#131  —  TP  —  GT: unusual_occupancy

# Anomaly on sensor leak_basement (capability: water)

**When:** Fri May 29 2026 03:00 UTC -> Fri May 29 2026 03:00 UTC (duration 0s).

**Magnitude:** baseline 0 (source: prewindow_2h), peak 1, delta +1 (+nan%).

**Calendar context:** Friday, hour 3 (night), weekday, May.

**Detector evidence:**
- state_transition: anomaly_type=water_leak_sustained, raw_value=1.0

**Detectors fired:** state_transition.

**Score:** 1 (threshold 0).

---

## Case waterleak_120d#132  —  TP  —  GT: trend

# Anomaly on sensor leak_battery (capability: battery)

**When:** Wed May 27 2026 17:38 UTC -> Sun May 31 2026 17:38 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline -6.286 (source: prewindow_24h), peak 0, delta +6.286 (-100.00%).

**Calendar context:** Wednesday, hour 17 (afternoon), weekday, May.

**Detector evidence:**
- cusum: mu=nan, sigma=nan, direction=+, delta=6.2856000000000005, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 99.7 (threshold 0).

---

## Case waterleak_120d#133  —  TP  —  GT: unusual_occupancy

# Anomaly on sensor leak_basement (capability: water)

**When:** Fri May 29 2026 03:00 UTC -> Sat May 30 2026 03:05 UTC (duration 1.00d).
**Long-duration framing:** spans 1.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 0 (source: prewindow_2h), peak 1, delta +1 (+nan%).

**Calendar context:** Friday, hour 3 (night), weekday, May.

**Detector evidence:**
- cusum: mu=0.0, sigma=nan, direction=+, delta=1.0, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=0.0, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca.

**Score:** 5 (threshold 0).

---

## Case waterleak_120d#134  —  FP  —  GT: (none)

# Anomaly on sensor leak_battery (capability: battery)

**When:** Sun May 31 2026 15:34 UTC -> Sun May 31 2026 18:00 UTC (duration 2.43h).

**Magnitude:** baseline 0 (source: prewindow_24h), peak 0, delta +0 (+nan%).

**Calendar context:** Sunday, hour 15 (afternoon), weekend, May.

**Detector evidence:**
- cusum: mu=nan, sigma=nan, direction=0, delta=0.0, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=nan, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 92.6 (threshold 0).

---
