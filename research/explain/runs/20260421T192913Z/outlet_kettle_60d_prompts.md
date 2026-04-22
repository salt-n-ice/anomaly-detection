# outlet_kettle_60d — explain cases (run 20260421T192913Z)

## Case outlet_kettle_60d#000  —  TP  —  GT: dip

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sat Feb 07 2026 09:00 UTC -> Sat Feb 07 2026 09:01 UTC (duration 1.0m).

**Magnitude:** baseline 0 (source: prewindow_2h), peak -800, delta -800 (+nan%).

**Calendar context:** Saturday, hour 9 (morning), weekend, February.

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-800.0, score=-800.0

**Detectors fired:** data_quality_gate.

**Score:** -800 (threshold 0).

---

## Case outlet_kettle_60d#001  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 09 2026 11:00 UTC -> Mon Feb 09 2026 11:01 UTC (duration 1.0m).

**Magnitude:** baseline 0 (source: prewindow_2h), peak 9999, delta +9999 (+nan%).

**Calendar context:** Monday, hour 11 (morning), weekday, February.

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=9999.0, score=9999.0

**Detectors fired:** data_quality_gate.

**Score:** 1e+04 (threshold 0).

---

## Case outlet_kettle_60d#002  —  TP  —  GT: noise_burst

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Fri Feb 13 2026 12:00 UTC -> Fri Feb 13 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline 1423 (source: prewindow_2h), peak -384.1, delta -1807 (-126.99%).

**Calendar context:** Friday, hour 12 (afternoon), weekday, February.
**Same-hour-of-weekday baseline:** peak is -5.09σ vs. the median of 13 prior Friday 12:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-384.0681180236057, score=-102.0614153575335

**Detectors fired:** data_quality_gate.

**Score:** -102 (threshold 0).

---

## Case outlet_kettle_60d#003  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 10:30 UTC -> Sun Feb 15 2026 10:31 UTC (duration 1.0m).

**Magnitude:** baseline 120.2 (source: prewindow_2h), peak 141.1, delta +20.96 (+17.44%).

**Calendar context:** Sunday, hour 10 (morning), weekend, February.
**Same-hour-of-weekday baseline:** peak is +3.24σ vs. the median of 1349 prior Sunday 10:00 samples (peer median 120.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=141.1385288945216, score=141.1385288945216

**Detectors fired:** data_quality_gate.

**Score:** 141 (threshold 0).

---

## Case outlet_kettle_60d#004  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 11:12 UTC -> Sun Feb 15 2026 11:13 UTC (duration 1.0m).

**Magnitude:** baseline 120.1 (source: prewindow_2h), peak 140.9, delta +20.88 (+17.39%).

**Calendar context:** Sunday, hour 11 (morning), weekend, February.
**Same-hour-of-weekday baseline:** peak is +3.32σ vs. the median of 575 prior Sunday 11:00 samples (peer median 119.7).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=140.93054016735508, score=140.93054016735508

**Detectors fired:** data_quality_gate.

**Score:** 141 (threshold 0).

---

## Case outlet_kettle_60d#005  —  TP  —  GT: noise_floor_up

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Feb 15 2026 10:00 UTC -> Sun Feb 15 2026 12:01 UTC (duration 2.02h).

**Magnitude:** baseline 120 (source: prewindow_2h), peak 96.77, delta -23.26 (-19.38%).

**Calendar context:** Sunday, hour 10 (morning), weekend, February.
**Same-hour-of-weekday baseline:** peak is -79.36σ vs. the median of 12 prior Sunday 10:00 samples (peer median 120.2).

**Detector evidence:**
- temporal_profile: hour_of_day=10, same_hour_median=120.1039914847776, approx_hour_z=-58.7805381882606, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 80.1 (threshold 0).

---

## Case outlet_kettle_60d#006  —  TP  —  GT: calibration_drift, trend

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Feb 17 2026 00:00 UTC -> Sat Feb 21 2026 00:00 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 120 (source: prewindow_2h), peak 127.9, delta +7.908 (+6.59%).

**Calendar context:** Tuesday, hour 0 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is +19.83σ vs. the median of 12 prior Tuesday 0:00 samples (peer median 120.2).

**Detector evidence:**
- cusum: mu=119.98392461506187, sigma=0.44859132340085084, direction=+, delta=7.908088448643852, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=17.62871468108483, baseline=119.98392461506187, source=derived_from_prewindow
- sub_pca: approx_residual_z=17.62871468108483, baseline=119.98392461506187, source=derived_from_prewindow
- temporal_profile: hour_of_day=0, same_hour_median=119.99654625193807, approx_hour_z=20.22002954342041, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 91.1 (threshold 0).

---

## Case outlet_kettle_60d#007  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 00:10 UTC -> Mon Feb 23 2026 00:11 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak -68.19, delta -168.2 (-168.19%).

**Calendar context:** Monday, hour 0 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -1.32σ vs. the median of 40 prior Monday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-68.18891645963382, score=-68.18891645963382

**Detectors fired:** data_quality_gate.

**Score:** -68.2 (threshold 0).

---

## Case outlet_kettle_60d#008  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 00:43 UTC -> Mon Feb 23 2026 00:44 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak -33.2, delta -133.2 (-133.20%).

**Calendar context:** Monday, hour 0 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.43σ vs. the median of 53 prior Monday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-33.20237348685035, score=-33.20237348685035

**Detectors fired:** data_quality_gate.

**Score:** -33.2 (threshold 0).

---

## Case outlet_kettle_60d#009  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 01:16 UTC -> Mon Feb 23 2026 01:17 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak -0.7246, delta -100.7 (-100.72%).

**Calendar context:** Monday, hour 1 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.01σ vs. the median of 42 prior Monday 1:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.7246403271524429, score=-0.7246403271524429

**Detectors fired:** data_quality_gate.

**Score:** -0.725 (threshold 0).

---

## Case outlet_kettle_60d#010  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 01:50 UTC -> Mon Feb 23 2026 01:51 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak -68.19, delta -168.2 (-168.19%).

**Calendar context:** Monday, hour 1 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.89σ vs. the median of 56 prior Monday 1:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-68.18891645963384, score=-68.18891645963384

**Detectors fired:** data_quality_gate.

**Score:** -68.2 (threshold 0).

---

## Case outlet_kettle_60d#011  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 02:23 UTC -> Mon Feb 23 2026 02:24 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak -33.2, delta -133.2 (-133.20%).

**Calendar context:** Monday, hour 2 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.54σ vs. the median of 45 prior Monday 2:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-33.20237348685012, score=-33.20237348685012

**Detectors fired:** data_quality_gate.

**Score:** -33.2 (threshold 0).

---

## Case outlet_kettle_60d#012  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 02:56 UTC -> Mon Feb 23 2026 02:57 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak -0.7246, delta -100.7 (-100.72%).

**Calendar context:** Monday, hour 2 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.01σ vs. the median of 58 prior Monday 2:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.724640327151576, score=-0.724640327151576

**Detectors fired:** data_quality_gate.

**Score:** -0.725 (threshold 0).

---

## Case outlet_kettle_60d#013  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 03:30 UTC -> Mon Feb 23 2026 03:31 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak -68.19, delta -168.2 (-168.19%).

**Calendar context:** Monday, hour 3 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -1.00σ vs. the median of 49 prior Monday 3:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-68.18891645963444, score=-68.18891645963444

**Detectors fired:** data_quality_gate.

**Score:** -68.2 (threshold 0).

---

## Case outlet_kettle_60d#014  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 04:03 UTC -> Mon Feb 23 2026 04:04 UTC (duration 1.0m).

**Magnitude:** baseline 132.5 (source: prewindow_2h), peak -28.45, delta -161 (-121.47%).

**Calendar context:** Monday, hour 4 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.20σ vs. the median of 72 prior Monday 4:00 samples (peer median 122.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-28.450530635316227, score=-28.450530635316227

**Detectors fired:** data_quality_gate.

**Score:** -28.5 (threshold 0).

---

## Case outlet_kettle_60d#015  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 04:36 UTC -> Mon Feb 23 2026 04:37 UTC (duration 1.0m).

**Magnitude:** baseline 132.5 (source: prewindow_2h), peak -29.41, delta -161.9 (-122.19%).

**Calendar context:** Monday, hour 4 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.17σ vs. the median of 86 prior Monday 4:00 samples (peer median 94.97).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-29.41119231388862, score=-29.41119231388862

**Detectors fired:** data_quality_gate.

**Score:** -29.4 (threshold 0).

---

## Case outlet_kettle_60d#016  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 05:10 UTC -> Mon Feb 23 2026 05:11 UTC (duration 1.0m).

**Magnitude:** baseline 132.5 (source: prewindow_2h), peak -29.41, delta -161.9 (-122.19%).

**Calendar context:** Monday, hour 5 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.52σ vs. the median of 40 prior Monday 5:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-29.41119231388853, score=-29.41119231388853

**Detectors fired:** data_quality_gate.

**Score:** -29.4 (threshold 0).

---

## Case outlet_kettle_60d#017  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Feb 23 2026 05:43 UTC -> Mon Feb 23 2026 05:44 UTC (duration 1.0m).

**Magnitude:** baseline 133.9 (source: prewindow_2h), peak -29.41, delta -163.3 (-121.97%).

**Calendar context:** Monday, hour 5 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.35σ vs. the median of 54 prior Monday 5:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-29.41119231388848, score=-29.41119231388848

**Detectors fired:** data_quality_gate.

**Score:** -29.4 (threshold 0).

---

## Case outlet_kettle_60d#018  —  TP  —  GT: level_shift, frequency_change, seasonality_loss

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Fri Feb 20 2026 21:56 UTC -> Wed Feb 25 2026 00:01 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 0 (source: prewindow_2h), peak 1805, delta +1805 (+nan%).

**Calendar context:** Friday, hour 21 (evening), weekday, February.

**Detector evidence:**
- cusum: mu=0.0, sigma=0.0, direction=+, delta=1805.1451134636368, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=0.0, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=0.0, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 3.43e+06 (threshold 0).

---

## Case outlet_kettle_60d#019  —  TP  —  GT: trend

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Fri Feb 20 2026 21:56 UTC -> Wed Feb 25 2026 00:01 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 127.1 (source: prewindow_2h), peak 122.8, delta -4.35 (-3.42%).

**Calendar context:** Friday, hour 21 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is +0.73σ vs. the median of 18 prior Friday 21:00 samples (peer median 120.2).

**Detector evidence:**
- cusum: mu=127.12845511238437, sigma=0.31990175859209435, direction=-, delta=-4.350371644538214, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=13.599086368529028, baseline=127.12845511238437, source=derived_from_prewindow
- sub_pca: approx_residual_z=13.599086368529028, baseline=127.12845511238437, source=derived_from_prewindow
- temporal_profile: hour_of_day=21, same_hour_median=120.13165814324731, approx_hour_z=1.1896201554987826, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 66.5 (threshold 0).

---

## Case outlet_kettle_60d#020  —  TP  —  GT: seasonality_loss, time_of_day

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Tue Feb 24 2026 21:57 UTC -> Sun Mar 01 2026 00:02 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 1523 (source: prewindow_2h), peak 100, delta -1423 (-93.43%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is +0.07σ vs. the median of 72 prior Tuesday 21:00 samples (peer median 50).

**Detector evidence:**
- cusum: mu=1523.1342578964354, sigma=765.1421986803432, direction=-, delta=-1423.1342578964354, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.859960488848929, baseline=1523.1342578964354, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.859960488848929, baseline=1523.1342578964354, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 4.32e+07 (threshold 0).

---

## Case outlet_kettle_60d#021  —  TP  —  GT: month_shift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Feb 24 2026 21:57 UTC -> Sun Mar 01 2026 00:02 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 124 (source: prewindow_2h), peak 126.1, delta +2.092 (+1.69%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is +1.94σ vs. the median of 24 prior Tuesday 21:00 samples (peer median 122).

**Detector evidence:**
- cusum: mu=123.97022750021253, sigma=0.4222369609675262, direction=+, delta=2.091606815956851, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=4.953632697535719, baseline=123.97022750021253, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.953632697535719, baseline=123.97022750021253, source=derived_from_prewindow
- temporal_profile: hour_of_day=21, same_hour_median=120.2299928635509, approx_hour_z=2.512144990758028, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 47 (threshold 0).

---

## Case outlet_kettle_60d#022  —  TP  —  GT: time_of_day, weekend_anomaly

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sat Feb 28 2026 21:58 UTC -> Thu Mar 05 2026 00:03 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1748, delta +1648 (+1648.28%).

**Calendar context:** Saturday, hour 21 (evening), weekend, February.
**Same-hour-of-weekday baseline:** peak is +34.60σ vs. the median of 47 prior Saturday 21:00 samples (peer median 0).

**Detector evidence:**
- cusum: mu=100.0, sigma=0.0, direction=+, delta=1648.2788271350291, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=100.0, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=100.0, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 4.32e+07 (threshold 0).

---

## Case outlet_kettle_60d#023  —  TP  —  GT: month_shift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat Feb 28 2026 21:58 UTC -> Thu Mar 05 2026 00:03 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 124.1 (source: prewindow_2h), peak 127.2, delta +3.186 (+2.57%).

**Calendar context:** Saturday, hour 21 (evening), weekend, February.
**Same-hour-of-weekday baseline:** peak is +2.52σ vs. the median of 24 prior Saturday 21:00 samples (peer median 121.9).

**Detector evidence:**
- cusum: mu=124.05657743815358, sigma=0.38133576535991104, direction=+, delta=3.1856913977344163, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=8.354032553772416, baseline=124.05657743815358, source=derived_from_prewindow
- sub_pca: approx_residual_z=8.354032553772416, baseline=124.05657743815358, source=derived_from_prewindow
- temporal_profile: hour_of_day=21, same_hour_median=120.5042743743259, approx_hour_z=2.908143876309915, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 79.8 (threshold 0).

---

## Case outlet_kettle_60d#024  —  TP  —  GT: weekend_anomaly, dropout, reporting_rate_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Wed Mar 04 2026 21:59 UTC -> Sun Mar 08 2026 02:36 UTC (duration 3.19d).
**Long-duration framing:** spans 3.2 days; covers 2 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1919, delta +1819 (+1819.35%).

**Calendar context:** Wednesday, hour 21 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +37.22σ vs. the median of 60 prior Wednesday 21:00 samples (peer median 0).

**Detector evidence:**
- cusum: mu=100.0, sigma=0.0, direction=+, delta=1819.3510493355511, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=1919.3510493355511, score=10993376.049140511
- multivariate_pca: approx_residual_z=nan, baseline=100.0, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=100.0, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 1.1e+07 (threshold 0).

---

## Case outlet_kettle_60d#025  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sun Mar 08 2026 00:32 UTC -> Sun Mar 08 2026 12:49 UTC (duration 12.28h).

**Magnitude:** baseline 300 (source: prewindow_2h), peak 1768, delta +1468 (+489.23%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +26.33σ vs. the median of 62 prior Sunday 0:00 samples (peer median 0).

**Detector evidence:**
- cusum: mu=300.0, sigma=0.0, direction=+, delta=1467.692218257737, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=1767.692218257737, score=10973376.049140511
- multivariate_pca: approx_residual_z=nan, baseline=300.0, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=300.0, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 1.1e+07 (threshold 0).

---

## Case outlet_kettle_60d#026  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sun Mar 08 2026 10:45 UTC -> Sun Mar 08 2026 14:24 UTC (duration 3.65h).

**Magnitude:** baseline 300 (source: prewindow_2h), peak 300, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 10 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.35σ vs. the median of 74 prior Sunday 10:00 samples (peer median 100).

**Detector evidence:**
- cusum: mu=300.0, sigma=733.8461091288685, direction=0, delta=0.0, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=300.0, score=10973376.049140511
- multivariate_pca: approx_residual_z=0.0, baseline=300.0, source=derived_from_prewindow
- sub_pca: approx_residual_z=0.0, baseline=300.0, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 1.1e+07 (threshold 0).

---

## Case outlet_kettle_60d#027  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sun Mar 08 2026 12:20 UTC -> Sun Mar 08 2026 18:44 UTC (duration 6.40h).

**Magnitude:** baseline 300 (source: prewindow_2h), peak 300, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 12 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.58σ vs. the median of 72 prior Sunday 12:00 samples (peer median 0).

**Detector evidence:**
- cusum: mu=300.0, sigma=0.0, direction=0, delta=0.0, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=300.0, score=10973376.049140511
- multivariate_pca: approx_residual_z=nan, baseline=300.0, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=300.0, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 1.1e+07 (threshold 0).

---

## Case outlet_kettle_60d#028  —  TP  —  GT: month_shift, duplicate_stale

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Wed Mar 04 2026 21:59 UTC -> Mon Mar 09 2026 00:04 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 127, delta +1.08 (+0.86%).

**Calendar context:** Wednesday, hour 21 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.51σ vs. the median of 30 prior Wednesday 21:00 samples (peer median 123.4).

**Detector evidence:**
- cusum: mu=125.96490898151986, sigma=0.28140990144108224, direction=+, delta=1.0803943956981783, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.8392195518549532, baseline=125.96490898151986, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.8392195518549532, baseline=125.96490898151986, source=derived_from_prewindow
- temporal_profile: hour_of_day=21, same_hour_median=122.08688460955071, approx_hour_z=1.9404562168106083, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 92 (threshold 0).

---

## Case outlet_kettle_60d#029  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:30 UTC -> Tue Mar 10 2026 00:31 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_2h), peak 126.3, delta +0.3413 (+0.27%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.93σ vs. the median of 33 prior Tuesday 0:00 samples (peer median 124).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.25557912095036, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#030  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:40 UTC -> Tue Mar 10 2026 00:41 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 126, delta -0.05924 (-0.05%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.80σ vs. the median of 34 prior Tuesday 0:00 samples (peer median 124).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.98509180386736, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#031  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 00:51 UTC -> Tue Mar 10 2026 00:52 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 125.9, delta -0.1839 (-0.15%).

**Calendar context:** Tuesday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.74σ vs. the median of 35 prior Tuesday 0:00 samples (peer median 124.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.86039881162075, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#032  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:01 UTC -> Tue Mar 10 2026 01:02 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 125.6, delta -0.4125 (-0.33%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.80σ vs. the median of 30 prior Tuesday 1:00 samples (peer median 123.6).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.57255891616605, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#033  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:11 UTC -> Tue Mar 10 2026 01:12 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 125.9, delta -0.07685 (-0.06%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.90σ vs. the median of 31 prior Tuesday 1:00 samples (peer median 123.6).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.90824122675018, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#034  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:21 UTC -> Tue Mar 10 2026 01:22 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_2h), peak 126, delta +0.07243 (+0.06%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.92σ vs. the median of 32 prior Tuesday 1:00 samples (peer median 123.6).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.98067244630305, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#035  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:31 UTC -> Tue Mar 10 2026 01:32 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 126.2, delta +0.1755 (+0.14%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.98σ vs. the median of 33 prior Tuesday 1:00 samples (peer median 123.7).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.15619038501896, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#036  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:42 UTC -> Tue Mar 10 2026 01:43 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 125.7, delta -0.2747 (-0.22%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.73σ vs. the median of 34 prior Tuesday 1:00 samples (peer median 123.8).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.71040050590642, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#037  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 01:52 UTC -> Tue Mar 10 2026 01:53 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 126.5, delta +0.5505 (+0.44%).

**Calendar context:** Tuesday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.97σ vs. the median of 35 prior Tuesday 1:00 samples (peer median 124).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.53112529829752, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#038  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:02 UTC -> Tue Mar 10 2026 02:03 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 126.3, delta +0.2887 (+0.23%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.09σ vs. the median of 30 prior Tuesday 2:00 samples (peer median 123.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.26937991842226, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#039  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:12 UTC -> Tue Mar 10 2026 02:13 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 126.2, delta +0.1948 (+0.15%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.03σ vs. the median of 31 prior Tuesday 2:00 samples (peer median 123.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.17546222980076, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#040  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:22 UTC -> Tue Mar 10 2026 02:23 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 126.5, delta +0.5245 (+0.42%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.12σ vs. the median of 32 prior Tuesday 2:00 samples (peer median 123.6).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.5095730133301, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#041  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:33 UTC -> Tue Mar 10 2026 02:34 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 126.1, delta +0.09375 (+0.07%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.91σ vs. the median of 33 prior Tuesday 2:00 samples (peer median 123.7).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.07884501302291, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#042  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:43 UTC -> Tue Mar 10 2026 02:44 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_2h), peak 125.9, delta -0.1808 (-0.14%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.75σ vs. the median of 34 prior Tuesday 2:00 samples (peer median 123.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.8980660969982, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#043  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 02:53 UTC -> Tue Mar 10 2026 02:54 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_2h), peak 126.3, delta +0.2345 (+0.19%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.82σ vs. the median of 35 prior Tuesday 2:00 samples (peer median 124.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.31339394713032, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#044  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:03 UTC -> Tue Mar 10 2026 03:04 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_2h), peak 125.4, delta -0.7105 (-0.56%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.76σ vs. the median of 30 prior Tuesday 3:00 samples (peer median 123.6).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.44564940372346, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#045  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:13 UTC -> Tue Mar 10 2026 03:14 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_2h), peak 126.3, delta +0.1019 (+0.08%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.09σ vs. the median of 31 prior Tuesday 3:00 samples (peer median 123.6).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.25809526890993, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#046  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:24 UTC -> Tue Mar 10 2026 03:25 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_2h), peak 125.8, delta -0.4178 (-0.33%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.87σ vs. the median of 32 prior Tuesday 3:00 samples (peer median 123.6).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.75766235276136, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#047  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:34 UTC -> Tue Mar 10 2026 03:35 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_2h), peak 125.4, delta -0.7889 (-0.63%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.72σ vs. the median of 33 prior Tuesday 3:00 samples (peer median 123.6).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.38660840739604, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#048  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:44 UTC -> Tue Mar 10 2026 03:45 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_2h), peak 125.8, delta -0.3544 (-0.28%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.86σ vs. the median of 34 prior Tuesday 3:00 samples (peer median 123.7).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.8210262789895, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#049  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 03:54 UTC -> Tue Mar 10 2026 03:55 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_2h), peak 126.1, delta -0.01955 (-0.02%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.93σ vs. the median of 35 prior Tuesday 3:00 samples (peer median 123.8).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.05929182052616, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#050  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:04 UTC -> Tue Mar 10 2026 04:05 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_2h), peak 126.3, delta +0.2701 (+0.21%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.11σ vs. the median of 30 prior Tuesday 4:00 samples (peer median 123.7).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.32936441330484, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#051  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:15 UTC -> Tue Mar 10 2026 04:16 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_2h), peak 126.1, delta +0.07486 (+0.06%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.99σ vs. the median of 31 prior Tuesday 4:00 samples (peer median 123.8).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.13415611824048, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#052  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:25 UTC -> Tue Mar 10 2026 04:26 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_2h), peak 125.5, delta -0.5175 (-0.41%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.71σ vs. the median of 32 prior Tuesday 4:00 samples (peer median 123.8).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.54182698033358, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#053  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:35 UTC -> Tue Mar 10 2026 04:36 UTC (duration 1.0m).

**Magnitude:** baseline 125.9 (source: prewindow_2h), peak 126.3, delta +0.3651 (+0.29%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.98σ vs. the median of 33 prior Tuesday 4:00 samples (peer median 123.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.26311913884231, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#054  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:45 UTC -> Tue Mar 10 2026 04:46 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_2h), peak 126, delta -0.02427 (-0.02%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.87σ vs. the median of 34 prior Tuesday 4:00 samples (peer median 123.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.03501850006388, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#055  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 04:55 UTC -> Tue Mar 10 2026 04:56 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 126.3, delta +0.2418 (+0.19%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.95σ vs. the median of 35 prior Tuesday 4:00 samples (peer median 124).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.27681035935414, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#056  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:06 UTC -> Tue Mar 10 2026 05:07 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_2h), peak 125.2, delta -0.8694 (-0.69%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.56σ vs. the median of 30 prior Tuesday 5:00 samples (peer median 123.8).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.1899197068028, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#057  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:16 UTC -> Tue Mar 10 2026 05:17 UTC (duration 1.0m).

**Magnitude:** baseline 126 (source: prewindow_2h), peak 126.2, delta +0.2109 (+0.17%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.97σ vs. the median of 31 prior Tuesday 5:00 samples (peer median 123.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.24587176218373, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#058  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:26 UTC -> Tue Mar 10 2026 05:27 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_2h), peak 126.2, delta +0.1845 (+0.15%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.94σ vs. the median of 32 prior Tuesday 5:00 samples (peer median 123.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.24377946493804, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#059  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:36 UTC -> Tue Mar 10 2026 05:37 UTC (duration 1.0m).

**Magnitude:** baseline 126.1 (source: prewindow_2h), peak 126.5, delta +0.3431 (+0.27%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.01σ vs. the median of 33 prior Tuesday 5:00 samples (peer median 123.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.477251501829, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#060  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:46 UTC -> Tue Mar 10 2026 05:47 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_2h), peak 126.1, delta -0.1849 (-0.15%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.81σ vs. the median of 34 prior Tuesday 5:00 samples (peer median 124).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=126.05887459296522, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#061  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 05:57 UTC -> Tue Mar 10 2026 05:58 UTC (duration 1.0m).

**Magnitude:** baseline 126.2 (source: prewindow_2h), peak 125.4, delta -0.8825 (-0.70%).

**Calendar context:** Tuesday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.51σ vs. the median of 35 prior Tuesday 5:00 samples (peer median 124).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=125.36130291589446, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#062  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sun Mar 08 2026 16:40 UTC -> Wed Mar 11 2026 23:55 UTC (duration 3.30d).
**Long-duration framing:** spans 3.3 days; covers 1 weekend day(s).

**Magnitude:** baseline 300 (source: prewindow_2h), peak 1913, delta +1613 (+537.74%).

**Calendar context:** Sunday, hour 16 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is +32.30σ vs. the median of 61 prior Sunday 16:00 samples (peer median 0).

**Detector evidence:**
- cusum: mu=300.0, sigma=0.0, direction=+, delta=1613.2182018257936, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=1913.2182018257936, score=10973376.049140511
- multivariate_pca: approx_residual_z=nan, baseline=300.0, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=300.0, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 1.1e+07 (threshold 0).

---

## Case outlet_kettle_60d#063  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.11σ vs. the median of 63 prior Thursday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1605.479843362571, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#064  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.11σ vs. the median of 63 prior Thursday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1605.479843362571, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#065  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.11σ vs. the median of 63 prior Thursday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1605.479843362571, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#066  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.11σ vs. the median of 63 prior Thursday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1605.479843362571, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#067  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.11σ vs. the median of 63 prior Thursday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1605.479843362571, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#068  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.11σ vs. the median of 63 prior Thursday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1605.479843362571, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#069  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.11σ vs. the median of 63 prior Thursday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1605.479843362571, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#070  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.11σ vs. the median of 63 prior Thursday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1605.479843362571, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#071  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.11σ vs. the median of 63 prior Thursday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1605.479843362571, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#072  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.11σ vs. the median of 63 prior Thursday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=batch_arrival, value=1605.479843362571, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_kettle_60d#073  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.11σ vs. the median of 63 prior Thursday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1605.479843362571, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#074  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1605, delta +1505 (+1505.48%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.11σ vs. the median of 63 prior Thursday 0:00 samples (peer median 0).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1605.479843362571, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_kettle_60d#075  —  TP  —  GT: month_shift, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Mar 08 2026 22:00 UTC -> Fri Mar 13 2026 00:05 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 126.2 (source: prewindow_2h), peak 124.9, delta -1.287 (-1.02%).

**Calendar context:** Sunday, hour 22 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.71σ vs. the median of 30 prior Sunday 22:00 samples (peer median 120.4).

**Detector evidence:**
- cusum: mu=126.1977513345221, sigma=0.3378774467867094, direction=-, delta=-1.286649140670221, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.8080349928843846, baseline=126.1977513345221, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.8080349928843846, baseline=126.1977513345221, source=derived_from_prewindow
- temporal_profile: hour_of_day=22, same_hour_median=123.57954720449288, approx_hour_z=0.4979153404688716, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 85.1 (threshold 0).

---

## Case outlet_kettle_60d#076  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sun Mar 15 2026 03:28 UTC -> Sun Mar 15 2026 03:29 UTC (duration 1.0m).

**Magnitude:** baseline 312 (source: prewindow_2h), peak -1306, delta -1618 (-518.78%).

**Calendar context:** Sunday, hour 3 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is -3.06σ vs. the median of 74 prior Sunday 3:00 samples (peer median 100).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-1306.4991296408753, score=-1172.933697600788

**Detectors fired:** data_quality_gate.

**Score:** -1.17e+03 (threshold 0).

---

## Case outlet_kettle_60d#077  —  TP  —  GT: weekend_anomaly, seasonal_mismatch, batch_arrival

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Wed Mar 11 2026 21:51 UTC -> Mon Mar 16 2026 00:59 UTC (duration 4.13d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1892, delta +1792 (+1791.97%).

**Calendar context:** Wednesday, hour 21 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +9.84σ vs. the median of 72 prior Wednesday 21:00 samples (peer median 50).

**Detector evidence:**
- cusum: mu=100.0, sigma=289.7060913184519, direction=+, delta=1791.9680225780328, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=1891.9680225780328, score=14419177.614906829
- multivariate_pca: approx_residual_z=6.185468915833939, baseline=100.0, source=derived_from_prewindow
- sub_pca: approx_residual_z=6.185468915833939, baseline=100.0, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 1.44e+07 (threshold 0).

---

## Case outlet_kettle_60d#078  —  TP  —  GT: month_shift, stuck_at

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 12 2026 22:01 UTC -> Tue Mar 17 2026 00:06 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 126.2 (source: prewindow_2h), peak 124.8, delta -1.366 (-1.08%).

**Calendar context:** Thursday, hour 22 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.31σ vs. the median of 31 prior Thursday 22:00 samples (peer median 124).

**Detector evidence:**
- cusum: mu=126.16604924708793, sigma=0.34800301822391955, direction=-, delta=-1.366094022745287, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.925523490334459, baseline=126.16604924708793, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.925523490334459, baseline=126.16604924708793, source=derived_from_prewindow
- temporal_profile: hour_of_day=22, same_hour_median=123.89329892809222, approx_hour_z=0.333658206470373, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 85.8 (threshold 0).

---

## Case outlet_kettle_60d#079  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Sun Mar 15 2026 22:55 UTC -> Fri Mar 20 2026 01:00 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 300 (source: prewindow_2h), peak 1731, delta +1431 (+476.89%).

**Calendar context:** Sunday, hour 22 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is +2.21σ vs. the median of 112 prior Sunday 22:00 samples (peer median 100).

**Detector evidence:**
- cusum: mu=300.0, sigma=0.0, direction=+, delta=1430.659334428626, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=300.0, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=300.0, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 6.17e+06 (threshold 0).

---

## Case outlet_kettle_60d#080  —  TP  —  GT: month_shift, stuck_at, degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Mon Mar 16 2026 22:02 UTC -> Sat Mar 21 2026 00:07 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 126.1 (source: prewindow_2h), peak 124.9, delta -1.207 (-0.96%).

**Calendar context:** Monday, hour 22 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.45σ vs. the median of 37 prior Monday 22:00 samples (peer median 123.6).

**Detector evidence:**
- cusum: mu=126.10434971612261, sigma=0.462505620815597, direction=-, delta=-1.2070201366855144, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.6097415520205294, baseline=126.10434971612261, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.6097415520205294, baseline=126.10434971612261, source=derived_from_prewindow
- temporal_profile: hour_of_day=22, same_hour_median=124.06186062291688, approx_hour_z=0.3072363514299638, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 82.4 (threshold 0).

---

## Case outlet_kettle_60d#081  —  FP  —  GT: (none)

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Thu Mar 19 2026 22:56 UTC -> Tue Mar 24 2026 01:01 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1748, delta +1648 (+1647.85%).

**Calendar context:** Thursday, hour 22 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +33.05σ vs. the median of 83 prior Thursday 22:00 samples (peer median 100).

**Detector evidence:**
- cusum: mu=100.0, sigma=0.0, direction=+, delta=1647.8465508090271, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=100.0, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 1.22e+06 (threshold 0).

---

## Case outlet_kettle_60d#082  —  TP  —  GT: month_shift, degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Fri Mar 20 2026 22:03 UTC -> Wed Mar 25 2026 00:08 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 125.8 (source: prewindow_2h), peak 127.4, delta +1.588 (+1.26%).

**Calendar context:** Friday, hour 22 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.59σ vs. the median of 37 prior Friday 22:00 samples (peer median 125.6).

**Detector evidence:**
- cusum: mu=125.78128151310972, sigma=0.3423414449291572, direction=+, delta=1.5877977577547853, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=4.638052976855776, baseline=125.78128151310972, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.638052976855776, baseline=125.78128151310972, source=derived_from_prewindow
- temporal_profile: hour_of_day=22, same_hour_median=124.3802022058904, approx_hour_z=1.1014309993436324, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 86.1 (threshold 0).

---

## Case outlet_kettle_60d#083  —  FP  —  GT: (none)

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Mon Mar 23 2026 22:57 UTC -> Sat Mar 28 2026 01:02 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1757, delta +1657 (+1657.27%).

**Calendar context:** Monday, hour 22 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +34.05σ vs. the median of 96 prior Monday 22:00 samples (peer median 100).

**Detector evidence:**
- cusum: mu=100.0, sigma=0.0, direction=+, delta=1657.274642886965, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=100.0, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 1.22e+06 (threshold 0).

---

## Case outlet_kettle_60d#084  —  TP  —  GT: month_shift, degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 24 2026 22:04 UTC -> Sun Mar 29 2026 00:09 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 126.6 (source: prewindow_2h), peak 128.2, delta +1.605 (+1.27%).

**Calendar context:** Tuesday, hour 22 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.49σ vs. the median of 43 prior Tuesday 22:00 samples (peer median 124.5).

**Detector evidence:**
- cusum: mu=126.5505776063292, sigma=0.4218701833577107, direction=+, delta=1.6054449905090848, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.805542685503805, baseline=126.5505776063292, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.805542685503805, baseline=126.5505776063292, source=derived_from_prewindow
- temporal_profile: hour_of_day=22, same_hour_median=124.70984369178672, approx_hour_z=1.272046869215845, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 97.3 (threshold 0).

---

## Case outlet_kettle_60d#085  —  FP  —  GT: (none)

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Fri Mar 27 2026 22:58 UTC -> Wed Apr 01 2026 01:03 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1750, delta +1650 (+1650.37%).

**Calendar context:** Friday, hour 22 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.56σ vs. the median of 130 prior Friday 22:00 samples (peer median 100).

**Detector evidence:**
- cusum: mu=100.0, sigma=0.0, direction=+, delta=1650.3729622409185, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=100.0, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=100.0, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 1.22e+06 (threshold 0).

---

## Case outlet_kettle_60d#086  —  FP  —  GT: (none)

# Anomaly on sensor outlet_kettle_power (capability: power)

**When:** Tue Mar 31 2026 22:59 UTC -> Wed Apr 01 2026 23:58 UTC (duration 1.04d).
**Long-duration framing:** spans 1.0 days; covers 0 weekend day(s).

**Magnitude:** baseline 100 (source: prewindow_2h), peak 1800, delta +1700 (+1700.26%).

**Calendar context:** Tuesday, hour 22 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +35.90σ vs. the median of 108 prior Tuesday 22:00 samples (peer median 100).

**Detector evidence:**
- cusum: mu=100.0, sigma=0.0, direction=+, delta=1700.2605770445482, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=100.0, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 1.22e+06 (threshold 0).

---

## Case outlet_kettle_60d#087  —  TP  —  GT: month_shift, degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat Mar 28 2026 22:05 UTC -> Wed Apr 01 2026 23:50 UTC (duration 4.07d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 126.8 (source: prewindow_2h), peak 122.9, delta -3.896 (-3.07%).

**Calendar context:** Saturday, hour 22 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.52σ vs. the median of 43 prior Saturday 22:00 samples (peer median 124.2).

**Detector evidence:**
- cusum: mu=126.78049711132937, sigma=0.36704568378750224, direction=-, delta=-3.8955299316062053, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=10.613201853809258, baseline=126.78049711132937, source=derived_from_prewindow
- sub_pca: approx_residual_z=10.613201853809258, baseline=126.78049711132937, source=derived_from_prewindow
- temporal_profile: hour_of_day=22, same_hour_median=125.43818868644642, approx_hour_z=-0.942311821021507, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 97.8 (threshold 0).

---
