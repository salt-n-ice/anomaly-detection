# outlet_120d — explain cases (run 20260421T192913Z)

## Case outlet_120d#000  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 09 2026 11:00 UTC -> Mon Feb 09 2026 11:01 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 9999, delta +9998 (+666500.00%).

**Calendar context:** Monday, hour 11 (morning), weekday, February.

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=9999.0, score=9999.0

**Detectors fired:** data_quality_gate.

**Score:** 1e+04 (threshold 0).

---

## Case outlet_120d#001  —  TP  —  GT: noise_burst

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Feb 13 2026 12:00 UTC -> Fri Feb 13 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak -56.11, delta -57.61 (-3840.68%).

**Calendar context:** Friday, hour 12 (afternoon), weekday, February.
**Same-hour-of-weekday baseline:** peak is -1.72σ vs. the median of 14 prior Friday 12:00 samples (peer median 21.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-56.11021770354085, score=-13.809212303630025

**Detectors fired:** data_quality_gate.

**Score:** -13.8 (threshold 0).

---

## Case outlet_120d#002  —  TP  —  GT: noise_floor_up

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

## Case outlet_120d#003  —  TP  —  GT: noise_floor_up

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

## Case outlet_120d#004  —  TP  —  GT: noise_floor_up

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

## Case outlet_120d#005  —  TP  —  GT: calibration_drift, trend

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

## Case outlet_120d#006  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Feb 20 2026 21:57 UTC -> Sat Feb 21 2026 14:39 UTC (duration 16.70h).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 116.7, delta +115.2 (+7683.21%).

**Calendar context:** Friday, hour 21 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is +2.71σ vs. the median of 43 prior Friday 21:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=1.5, sigma=42.07332654764625, direction=+, delta=115.24812298407484, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.739220604616591, baseline=1.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.739220604616591, baseline=1.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#007  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Feb 21 2026 13:41 UTC -> Sat Feb 21 2026 18:05 UTC (duration 4.40h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 113.4, delta +96.88 (+587.15%).

**Calendar context:** Saturday, hour 13 (afternoon), weekend, February.
**Same-hour-of-weekday baseline:** peak is +4.55σ vs. the median of 35 prior Saturday 13:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=39.90862025811527, direction=+, delta=96.87929982511554, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.4275281680632768, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.4275281680632768, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#008  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 00:10 UTC -> Mon Feb 23 2026 00:11 UTC (duration 1.0m).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak -2.912, delta -19.41 (-117.65%).

**Calendar context:** Monday, hour 0 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.15σ vs. the median of 42 prior Monday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.91167884708333, score=-2.91167884708333

**Detectors fired:** data_quality_gate.

**Score:** -2.91 (threshold 0).

---

## Case outlet_120d#009  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 00:43 UTC -> Mon Feb 23 2026 00:44 UTC (duration 1.0m).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak -2.912, delta -19.41 (-117.65%).

**Calendar context:** Monday, hour 0 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.17σ vs. the median of 56 prior Monday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.911678847083369, score=-2.911678847083369

**Detectors fired:** data_quality_gate.

**Score:** -2.91 (threshold 0).

---

## Case outlet_120d#010  —  TP  —  GT: level_shift, frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Feb 21 2026 17:51 UTC -> Mon Feb 23 2026 01:14 UTC (duration 1.31d).
**Long-duration framing:** spans 1.3 days; covers 2 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 117.4, delta +100.9 (+611.33%).

**Calendar context:** Saturday, hour 17 (afternoon), weekend, February.
**Same-hour-of-weekday baseline:** peak is +0.67σ vs. the median of 41 prior Saturday 17:00 samples (peer median 85.57).

**Detector evidence:**
- cusum: mu=16.5, sigma=44.6644198486153, direction=+, delta=100.86909487855247, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.2583769188189655, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2583769188189655, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=17, same_hour_median=1.5, approx_hour_z=2.613160776706719, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 6.32e+04 (threshold 0).

---

## Case outlet_120d#011  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 03:01 UTC -> Mon Feb 23 2026 03:02 UTC (duration 1.0m).

**Magnitude:** baseline 103.7 (source: prewindow_2h), peak -2.912, delta -106.7 (-102.81%).

**Calendar context:** Monday, hour 3 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.13σ vs. the median of 39 prior Monday 3:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.911678847083202, score=-2.911678847083202

**Detectors fired:** data_quality_gate.

**Score:** -2.91 (threshold 0).

---

## Case outlet_120d#012  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 03:34 UTC -> Mon Feb 23 2026 03:35 UTC (duration 1.0m).

**Magnitude:** baseline 89.97 (source: prewindow_2h), peak -2.912, delta -92.88 (-103.24%).

**Calendar context:** Monday, hour 3 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.14σ vs. the median of 53 prior Monday 3:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.9116788470832127, score=-2.9116788470832127

**Detectors fired:** data_quality_gate.

**Score:** -2.91 (threshold 0).

---

## Case outlet_120d#013  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 04:06 UTC -> Mon Feb 23 2026 04:07 UTC (duration 1.0m).

**Magnitude:** baseline 44.02 (source: prewindow_2h), peak -13.38, delta -57.41 (-130.40%).

**Calendar context:** Monday, hour 4 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.34σ vs. the median of 52 prior Monday 4:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-13.384008274295184, score=-13.384008274295184

**Detectors fired:** data_quality_gate.

**Score:** -13.4 (threshold 0).

---

## Case outlet_120d#014  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 04:36 UTC -> Mon Feb 23 2026 04:37 UTC (duration 1.0m).

**Magnitude:** baseline 30.79 (source: prewindow_2h), peak -1.286, delta -32.07 (-104.18%).

**Calendar context:** Monday, hour 4 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.66σ vs. the median of 67 prior Monday 4:00 samples (peer median 28.93).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-1.2857046048319276, score=-1.2857046048319276

**Detectors fired:** data_quality_gate.

**Score:** -1.29 (threshold 0).

---

## Case outlet_120d#015  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 05:10 UTC -> Mon Feb 23 2026 05:11 UTC (duration 1.0m).

**Magnitude:** baseline 28.06 (source: prewindow_2h), peak -1.286, delta -29.35 (-104.58%).

**Calendar context:** Monday, hour 5 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.21σ vs. the median of 44 prior Monday 5:00 samples (peer median 7.682).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-1.285704604831917, score=-1.285704604831917

**Detectors fired:** data_quality_gate.

**Score:** -1.29 (threshold 0).

---

## Case outlet_120d#016  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 05:48 UTC -> Mon Feb 23 2026 05:49 UTC (duration 1.0m).

**Magnitude:** baseline 29.1 (source: prewindow_2h), peak -2.331, delta -31.43 (-108.01%).

**Calendar context:** Monday, hour 5 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.38σ vs. the median of 61 prior Monday 5:00 samples (peer median 14.05).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-2.3307408387209776, score=-2.3307408387209776

**Detectors fired:** data_quality_gate.

**Score:** -2.33 (threshold 0).

---

## Case outlet_120d#017  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 00:43 UTC -> Mon Feb 23 2026 13:26 UTC (duration 12.72h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 145.4, delta +128.9 (+780.95%).

**Calendar context:** Monday, hour 0 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is +5.43σ vs. the median of 56 prior Monday 0:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=30.162812555767875, direction=+, delta=128.85731033673994, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=4.272058850562967, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.272058850562967, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=0, same_hour_median=1.5, approx_hour_z=3.716593347010101, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 8.97e+04 (threshold 0).

---

## Case outlet_120d#018  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 12:39 UTC -> Tue Feb 24 2026 00:04 UTC (duration 11.42h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 114.7, delta +98.18 (+595.04%).

**Calendar context:** Monday, hour 12 (afternoon), weekday, February.
**Same-hour-of-weekday baseline:** peak is +2.86σ vs. the median of 47 prior Monday 12:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=17.136676947624903, direction=+, delta=98.18096366268384, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=5.7292883540231205, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=5.7292883540231205, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=18.333190864306594, approx_hour_z=1.905458658358056, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#019  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 23 2026 23:02 UTC -> Tue Feb 24 2026 16:38 UTC (duration 17.60h).

**Magnitude:** baseline 103.7 (source: prewindow_2h), peak 16.5, delta -87.21 (-84.09%).

**Calendar context:** Monday, hour 23 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is +0.37σ vs. the median of 41 prior Monday 23:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=103.71054997207771, sigma=31.991013799069027, direction=-, delta=-87.21054997207771, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.7260952253603055, baseline=103.71054997207771, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.7260952253603055, baseline=103.71054997207771, source=derived_from_prewindow
- temporal_profile: hour_of_day=23, same_hour_median=1.5, approx_hour_z=0.3451112817657166, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#020  —  TP  —  GT: trend

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

## Case outlet_120d#021  —  TP  —  GT: seasonality_loss, time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Feb 24 2026 15:52 UTC -> Fri Feb 27 2026 03:44 UTC (duration 2.49d).
**Long-duration framing:** spans 2.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 186.2, delta +169.7 (+1028.77%).

**Calendar context:** Tuesday, hour 15 (afternoon), weekday, February.
**Same-hour-of-weekday baseline:** peak is +4.08σ vs. the median of 51 prior Tuesday 15:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=18.242351424159555, direction=+, delta=169.74642771315703, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=9.30507387815973, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=9.30507387815973, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=15, same_hour_median=16.5, approx_hour_z=3.850857680778713, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 1.88e+05 (threshold 0).

---

## Case outlet_120d#022  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Feb 27 2026 02:55 UTC -> Fri Feb 27 2026 06:22 UTC (duration 3.45h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 186.2, delta +169.7 (+1028.77%).

**Calendar context:** Friday, hour 2 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is +4.45σ vs. the median of 52 prior Friday 2:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=36.35733424142289, direction=+, delta=169.74642771315703, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=4.668835910410625, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.668835910410625, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#023  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Feb 27 2026 05:32 UTC -> Sat Feb 28 2026 02:59 UTC (duration 21.45h).

**Magnitude:** baseline 96.5 (source: prewindow_2h), peak 16.5, delta -80 (-82.90%).

**Calendar context:** Friday, hour 5 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is +0.41σ vs. the median of 47 prior Friday 5:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=96.5, sigma=46.80236852191502, direction=-, delta=-80.0, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.7093152019120639, baseline=96.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.7093152019120639, baseline=96.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#024  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Feb 28 2026 03:21 UTC -> Sat Feb 28 2026 21:31 UTC (duration 18.17h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 192.1, delta +175.6 (+1064.26%).

**Calendar context:** Saturday, hour 3 (night), weekend, February.
**Same-hour-of-weekday baseline:** peak is +4.43σ vs. the median of 44 prior Saturday 3:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=43.58856464693132, direction=+, delta=175.6033270571233, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=4.028655875216711, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.028655875216711, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#025  —  TP  —  GT: month_shift

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

## Case outlet_120d#026  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Feb 28 2026 20:52 UTC -> Sat Feb 28 2026 23:24 UTC (duration 2.53h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 110.7, delta +94.16 (+570.67%).

**Calendar context:** Saturday, hour 20 (evening), weekend, February.
**Same-hour-of-weekday baseline:** peak is +2.48σ vs. the median of 49 prior Saturday 20:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=42.37259898601417, direction=+, delta=94.15985333359583, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.222187347173936, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.222187347173936, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#027  —  TP  —  GT: time_of_day, weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 01 2026 00:05 UTC -> Mon Mar 02 2026 06:35 UTC (duration 1.27d).
**Long-duration framing:** spans 1.3 days; covers 1 weekend day(s).

**Magnitude:** baseline 104 (source: prewindow_2h), peak 16.5, delta -87.46 (-84.13%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.50σ vs. the median of 51 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=103.95876598068679, sigma=38.24626371104125, direction=-, delta=-87.45876598068679, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.286727054999583, baseline=103.95876598068679, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.286727054999583, baseline=103.95876598068679, source=derived_from_prewindow
- temporal_profile: hour_of_day=0, same_hour_median=1.5, approx_hour_z=0.37093722592533807, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 7.96e+05 (threshold 0).

---

## Case outlet_120d#028  —  TP  —  GT: month_shift

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

## Case outlet_120d#029  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Mar 02 2026 06:58 UTC -> Thu Mar 05 2026 06:34 UTC (duration 2.98d).
**Long-duration framing:** spans 3.0 days; covers 0 weekend day(s).

**Magnitude:** baseline 58.18 (source: prewindow_2h), peak 116.4, delta +58.23 (+100.08%).

**Calendar context:** Monday, hour 6 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.45σ vs. the median of 66 prior Monday 6:00 samples (peer median 9).

**Detector evidence:**
- cusum: mu=58.18386351435895, sigma=45.61839243526748, direction=+, delta=58.23289324932455, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.2765222564989998, baseline=58.18386351435895, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.2765222564989998, baseline=58.18386351435895, source=derived_from_prewindow
- temporal_profile: hour_of_day=6, same_hour_median=16.5, approx_hour_z=2.2843580338006357, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#030  —  TP  —  GT: weekend_anomaly, dropout

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 05 2026 05:36 UTC -> Thu Mar 05 2026 13:41 UTC (duration 8.08h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 111.4, delta +94.86 (+574.92%).

**Calendar context:** Thursday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.58σ vs. the median of 61 prior Thursday 5:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=42.93314073271987, direction=+, delta=94.86106204309972, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=111.36106204309972, score=28080.999943142862
- multivariate_pca: approx_residual_z=2.209506698651677, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.209506698651677, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=5, same_hour_median=16.5, approx_hour_z=2.142974735544841, source=derived_from_same_hour_history

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#031  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 05 2026 13:25 UTC -> Thu Mar 05 2026 19:39 UTC (duration 6.23h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 114.8, delta +98.31 (+595.81%).

**Calendar context:** Thursday, hour 13 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.24σ vs. the median of 57 prior Thursday 13:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=44.87019655316138, direction=+, delta=98.30820412650728, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.1909465899048053, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.1909465899048053, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#032  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 05 2026 19:26 UTC -> Thu Mar 05 2026 21:50 UTC (duration 2.40h).

**Magnitude:** baseline 101.1 (source: prewindow_2h), peak 16.5, delta -84.63 (-83.68%).

**Calendar context:** Thursday, hour 19 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.48σ vs. the median of 56 prior Thursday 19:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=101.129520989105, sigma=43.5364466783742, direction=-, delta=-84.629520989105, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.9438775427472568, baseline=101.129520989105, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.9438775427472568, baseline=101.129520989105, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#033  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 05 2026 20:58 UTC -> Fri Mar 06 2026 21:44 UTC (duration 1.03d).
**Long-duration framing:** spans 1.0 days; covers 0 weekend day(s).

**Magnitude:** baseline 100.1 (source: prewindow_2h), peak 16.5, delta -83.63 (-83.52%).

**Calendar context:** Thursday, hour 20 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 67 prior Thursday 20:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=100.13482342463145, sigma=38.94787345858748, direction=-, delta=-83.63482342463145, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.147352756333635, baseline=100.13482342463145, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.147352756333635, baseline=100.13482342463145, source=derived_from_prewindow
- temporal_profile: hour_of_day=20, same_hour_median=16.5, approx_hour_z=0.0, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#034  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 06 2026 20:57 UTC -> Fri Mar 06 2026 23:59 UTC (duration 3.03h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 116, delta +99.52 (+603.17%).

**Calendar context:** Friday, hour 20 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +3.97σ vs. the median of 63 prior Friday 20:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=17.765871637248942, direction=+, delta=99.5227033824193, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=5.601903774524313, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=5.601903774524313, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#035  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 01:00 UTC -> Sat Mar 07 2026 01:59 UTC (duration 59.0m).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak 147.2, delta +90.74 (+160.60%).

**Calendar context:** Saturday, hour 1 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.14σ vs. the median of 65 prior Saturday 1:00 samples (peer median 93.09).

**Detector evidence:**
- temporal_profile: hour_of_day=1, same_hour_median=16.5, approx_hour_z=2.865530233042063, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 5.5 (threshold 0).

---

## Case outlet_120d#036  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 05:00 UTC -> Sat Mar 07 2026 06:59 UTC (duration 1.98h).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak 148.6, delta +92.11 (+163.03%).

**Calendar context:** Saturday, hour 5 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +2.64σ vs. the median of 54 prior Saturday 5:00 samples (peer median 16.5).

**Detector evidence:**
- temporal_profile: hour_of_day=5, same_hour_median=16.5, approx_hour_z=2.9973661148717428, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 7.07 (threshold 0).

---

## Case outlet_120d#037  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 08:00 UTC -> Sat Mar 07 2026 08:59 UTC (duration 59.0m).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak 151.8, delta +95.29 (+168.66%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.41σ vs. the median of 58 prior Saturday 8:00 samples (peer median 89.16).

**Detector evidence:**
- temporal_profile: hour_of_day=8, same_hour_median=40.27782203041373, approx_hour_z=2.5342883582295137, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 6.45 (threshold 0).

---

## Case outlet_120d#038  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 11:03 UTC -> Sat Mar 07 2026 11:03 UTC (duration 0s).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak nan, delta +nan (+nan%).

**Calendar context:** Saturday, hour 11 (morning), weekend, March.

**Detector evidence:**
- multivariate_pca: approx_residual_z=0.0, baseline=56.5, source=derived_from_prewindow

**Detectors fired:** multivariate_pca.

**Score:** 3.25e+04 (threshold 0).

---

## Case outlet_120d#039  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 12:55 UTC -> Sat Mar 07 2026 15:03 UTC (duration 2.13h).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak 153.2, delta +96.68 (+171.12%).

**Calendar context:** Saturday, hour 12 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is +3.58σ vs. the median of 61 prior Saturday 12:00 samples (peer median 16.5).

**Detector evidence:**
- multivariate_pca: approx_residual_z=2.7022796762575765, baseline=56.5, source=derived_from_prewindow

**Detectors fired:** multivariate_pca.

**Score:** 3.73e+04 (threshold 0).

---

## Case outlet_120d#040  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 17:00 UTC -> Sun Mar 08 2026 02:16 UTC (duration 9.27h).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak 151.3, delta +94.75 (+167.71%).

**Calendar context:** Saturday, hour 17 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.41σ vs. the median of 57 prior Saturday 17:00 samples (peer median 85.44).

**Detector evidence:**
- cusum: mu=56.5, sigma=18.690203339161684, direction=+, delta=94.75374918394064, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=151.25374918394064, score=69778.8924881529
- multivariate_pca: approx_residual_z=5.069701354473902, baseline=56.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=17, same_hour_median=16.5, approx_hour_z=2.9965627178502965, source=derived_from_same_hour_history

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, temporal_profile.

**Score:** 6.98e+04 (threshold 0).

---

## Case outlet_120d#041  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 02:31 UTC -> Sun Mar 08 2026 09:01 UTC (duration 6.51h).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak 153.3, delta +96.84 (+171.40%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +4.16σ vs. the median of 63 prior Sunday 2:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=56.5, sigma=0.0, direction=+, delta=96.842511707879, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=153.342511707879, score=4589.0
- temporal_profile: hour_of_day=2, same_hour_median=16.5, approx_hour_z=3.0623708002616397, source=derived_from_same_hour_history

**Detectors fired:** cusum, data_quality_gate, temporal_profile.

**Score:** 4.59e+03 (threshold 0).

---

## Case outlet_120d#042  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 09:01 UTC -> Sun Mar 08 2026 13:59 UTC (duration 4.95h).

**Magnitude:** baseline 150.2 (source: prewindow_2h), peak 56.5, delta -93.74 (-62.39%).

**Calendar context:** Sunday, hour 9 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.65σ vs. the median of 65 prior Sunday 9:00 samples (peer median 86.29).

**Detector evidence:**
- cusum: mu=150.23933317616527, sigma=5.046223341612838, direction=-, delta=-93.73933317616527, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=56.5, score=5251.0
- temporal_profile: hour_of_day=9, same_hour_median=16.5, approx_hour_z=0.9066951537853376, source=derived_from_same_hour_history

**Detectors fired:** cusum, data_quality_gate, temporal_profile.

**Score:** 5.25e+03 (threshold 0).

---

## Case outlet_120d#043  —  TP  —  GT: month_shift, duplicate_stale

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

## Case outlet_120d#044  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#045  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#046  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#047  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#048  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#049  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#050  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#051  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#052  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#053  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#054  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#055  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#056  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#057  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#058  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#059  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#060  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#061  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#062  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#063  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#064  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#065  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#066  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#067  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#068  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#069  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#070  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#071  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#072  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#073  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#074  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#075  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#076  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#077  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 14:09 UTC -> Tue Mar 10 2026 05:27 UTC (duration 1.64d).
**Long-duration framing:** spans 1.6 days; covers 1 weekend day(s).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak 150.3, delta +93.78 (+165.98%).

**Calendar context:** Sunday, hour 14 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is +3.41σ vs. the median of 74 prior Sunday 14:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=56.5, sigma=0.0, direction=+, delta=93.77937954707119, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=150.2793795470712, score=28080.999943142862
- multivariate_pca: approx_residual_z=nan, baseline=56.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=56.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=14, same_hour_median=16.5, approx_hour_z=2.5993303941252517, source=derived_from_same_hour_history

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#078  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 10 2026 04:29 UTC -> Tue Mar 10 2026 18:24 UTC (duration 13.92h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 114.4, delta +97.88 (+593.23%).

**Calendar context:** Tuesday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.24σ vs. the median of 76 prior Tuesday 4:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=29.36732650614132, direction=+, delta=97.88254776187816, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.333042513808973, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.333042513808973, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#079  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 10 2026 17:47 UTC -> Wed Mar 11 2026 10:38 UTC (duration 16.85h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 117.1, delta +100.6 (+609.54%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.19σ vs. the median of 73 prior Tuesday 17:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=29.589765239909262, direction=+, delta=100.57378937364231, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.3989384017820186, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.3989384017820186, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=17, same_hour_median=16.5, approx_hour_z=2.2677863577144897, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#080  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 11 2026 09:59 UTC -> Wed Mar 11 2026 23:42 UTC (duration 13.72h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 114.6, delta +98.14 (+594.81%).

**Calendar context:** Wednesday, hour 9 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.94σ vs. the median of 80 prior Wednesday 9:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=35.90068053529542, direction=+, delta=98.14384040057492, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.7337598880357077, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.7337598880357077, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=9, same_hour_median=16.5, approx_hour_z=2.209804005840876, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#081  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 103.2 (source: prewindow_2h), peak 16.5, delta -86.69 (-84.01%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 71 prior Thursday 0:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=16.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#082  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 103.2 (source: prewindow_2h), peak 16.5, delta -86.69 (-84.01%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 71 prior Thursday 0:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=16.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#083  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 103.2 (source: prewindow_2h), peak 16.5, delta -86.69 (-84.01%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 71 prior Thursday 0:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=16.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#084  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 103.2 (source: prewindow_2h), peak 16.5, delta -86.69 (-84.01%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 71 prior Thursday 0:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=batch_arrival, value=16.5, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#085  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 11 2026 23:00 UTC -> Thu Mar 12 2026 14:12 UTC (duration 15.20h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 114.7, delta +98.18 (+595.03%).

**Calendar context:** Wednesday, hour 23 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.65σ vs. the median of 64 prior Wednesday 23:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=43.12415863550661, direction=+, delta=98.1806176149688, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=114.6806176149688, score=28080.999943142862
- multivariate_pca: approx_residual_z=2.2766964207883937, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2766964207883937, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=23, same_hour_median=16.5, approx_hour_z=2.412003990213859, source=derived_from_same_hour_history

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#086  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_120d#087  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Mar 12 2026 13:21 UTC -> Fri Mar 13 2026 07:36 UTC (duration 18.25h).

**Magnitude:** baseline 102.1 (source: prewindow_2h), peak 16.5, delta -85.56 (-83.83%).

**Calendar context:** Thursday, hour 13 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 69 prior Thursday 13:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=102.05610754894936, sigma=44.882400270351894, direction=-, delta=-85.55610754894936, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.9062284332744437, baseline=102.05610754894936, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.9062284332744437, baseline=102.05610754894936, source=derived_from_prewindow
- temporal_profile: hour_of_day=13, same_hour_median=16.5, approx_hour_z=0.0, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#088  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 13 2026 07:04 UTC -> Fri Mar 13 2026 20:57 UTC (duration 13.88h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 116.6, delta +100.1 (+606.55%).

**Calendar context:** Friday, hour 7 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.70σ vs. the median of 73 prior Friday 7:00 samples (peer median 85.39).

**Detector evidence:**
- cusum: mu=16.5, sigma=23.903175384411778, direction=+, delta=100.08099033204424, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=4.186932854005292, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.186932854005292, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#089  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 13 2026 20:05 UTC -> Fri Mar 13 2026 23:59 UTC (duration 3.90h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 110.9, delta +94.41 (+572.17%).

**Calendar context:** Friday, hour 20 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +3.32σ vs. the median of 65 prior Friday 20:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=45.71946213293982, direction=+, delta=94.40730016074824, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.064925870873926, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.064925870873926, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#090  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 01:00 UTC -> Sat Mar 14 2026 02:37 UTC (duration 1.62h).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak 149.3, delta +92.77 (+164.20%).

**Calendar context:** Saturday, hour 1 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.16σ vs. the median of 78 prior Saturday 1:00 samples (peer median 92.6).

**Detector evidence:**
- cusum: mu=56.5, sigma=35.22857101034193, direction=+, delta=92.77392285096715, source=derived_from_prewindow
- temporal_profile: hour_of_day=1, same_hour_median=16.5, approx_hour_z=2.9292036547120275, source=derived_from_same_hour_history

**Detectors fired:** cusum, temporal_profile.

**Score:** 1.3e+03 (threshold 0).

---

## Case outlet_120d#091  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 05:00 UTC -> Sat Mar 14 2026 06:59 UTC (duration 1.98h).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak 151.4, delta +94.86 (+167.89%).

**Calendar context:** Saturday, hour 5 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.99σ vs. the median of 67 prior Saturday 5:00 samples (peer median 56.5).

**Detector evidence:**
- temporal_profile: hour_of_day=5, same_hour_median=16.5, approx_hour_z=3.0818979669141773, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 7.12 (threshold 0).

---

## Case outlet_120d#092  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 08:00 UTC -> Sat Mar 14 2026 08:59 UTC (duration 59.0m).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak 143.3, delta +86.76 (+153.56%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.20σ vs. the median of 71 prior Saturday 8:00 samples (peer median 88.25).

**Detector evidence:**
- temporal_profile: hour_of_day=8, same_hour_median=56.5, approx_hour_z=1.9388909414293436, source=derived_from_same_hour_history

**Detectors fired:** temporal_profile.

**Score:** 5.42 (threshold 0).

---

## Case outlet_120d#093  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 11:59 UTC -> Sat Mar 14 2026 11:59 UTC (duration 0s).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak nan, delta +nan (+nan%).

**Calendar context:** Saturday, hour 11 (morning), weekend, March.

**Detector evidence:**
- cusum: mu=56.5, sigma=0.0, direction=0, delta=nan, source=derived_from_prewindow

**Detectors fired:** cusum.

**Score:** 1.29e+03 (threshold 0).

---

## Case outlet_120d#094  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 13:55 UTC -> Sat Mar 14 2026 14:15 UTC (duration 20.0m).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak 150.1, delta +93.56 (+165.58%).

**Calendar context:** Saturday, hour 13 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is +2.82σ vs. the median of 77 prior Saturday 13:00 samples (peer median 16.5).

**Detector evidence:**
- multivariate_pca: approx_residual_z=5.1946655144113505, baseline=56.5, source=derived_from_prewindow

**Detectors fired:** multivariate_pca.

**Score:** 3.96e+04 (threshold 0).

---

## Case outlet_120d#095  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 15:35 UTC -> Mon Mar 16 2026 09:32 UTC (duration 1.75d).
**Long-duration framing:** spans 1.7 days; covers 2 weekend day(s).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak 160.1, delta +103.6 (+183.33%).

**Calendar context:** Saturday, hour 15 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is +2.47σ vs. the median of 72 prior Saturday 15:00 samples (peer median 56.5).

**Detector evidence:**
- cusum: mu=56.5, sigma=39.1097764378433, direction=+, delta=103.5798091783756, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.648437772151261, baseline=56.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.648437772151261, baseline=56.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=15, same_hour_median=16.5, approx_hour_z=3.3089870088731748, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.1e+05 (threshold 0).

---

## Case outlet_120d#096  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Mar 16 2026 08:31 UTC -> Mon Mar 16 2026 15:26 UTC (duration 6.92h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 116.3, delta +99.77 (+604.66%).

**Calendar context:** Monday, hour 8 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.80σ vs. the median of 99 prior Monday 8:00 samples (peer median 81.08).

**Detector evidence:**
- cusum: mu=16.5, sigma=42.96591334054689, direction=+, delta=99.76860334822214, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.3220407898107127, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.3220407898107127, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#097  —  TP  —  GT: month_shift, stuck_at

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

## Case outlet_120d#098  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Mar 16 2026 14:36 UTC -> Wed Mar 18 2026 02:28 UTC (duration 1.49d).
**Long-duration framing:** spans 1.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 115.6, delta +99.12 (+600.72%).

**Calendar context:** Monday, hour 14 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.17σ vs. the median of 90 prior Monday 14:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=45.18653237970668, direction=+, delta=99.11813879409576, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.1935327535469358, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.1935327535469358, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=14, same_hour_median=16.5, approx_hour_z=1.9297682839600299, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#099  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 18 2026 01:41 UTC -> Fri Mar 20 2026 18:04 UTC (duration 2.68d).
**Long-duration framing:** spans 2.7 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 115.3, delta +98.78 (+598.69%).

**Calendar context:** Wednesday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.60σ vs. the median of 86 prior Wednesday 1:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=33.228825730714384, direction=+, delta=98.7841645235074, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.9728454843409735, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.9728454843409735, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=1, same_hour_median=16.5, approx_hour_z=2.057241995820512, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#100  —  TP  —  GT: month_shift, stuck_at, degradation_trajectory

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

## Case outlet_120d#101  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 20 2026 17:02 UTC -> Sat Mar 21 2026 02:09 UTC (duration 9.12h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 115.2, delta +98.67 (+597.98%).

**Calendar context:** Friday, hour 17 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.20σ vs. the median of 86 prior Friday 17:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=43.618903685276045, direction=+, delta=98.6659316264218, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.2619993463918115, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2619993463918115, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#102  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 21 2026 01:11 UTC -> Tue Mar 24 2026 15:11 UTC (duration 3.58d).
**Long-duration framing:** spans 3.6 days; covers 2 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 117.7, delta +101.2 (+613.56%).

**Calendar context:** Saturday, hour 1 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.37σ vs. the median of 92 prior Saturday 1:00 samples (peer median 98.79).

**Detector evidence:**
- cusum: mu=16.5, sigma=44.63759891579231, direction=+, delta=101.23682084870885, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.2679719184647347, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2679719184647347, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=1, same_hour_median=16.5, approx_hour_z=2.1329320995849694, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#103  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 24 2026 14:43 UTC -> Tue Mar 24 2026 21:01 UTC (duration 6.30h).

**Magnitude:** baseline 93.16 (source: prewindow_2h), peak 16.5, delta -76.66 (-82.29%).

**Calendar context:** Tuesday, hour 14 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 113 prior Tuesday 14:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=93.15630629203233, sigma=44.86927290749415, direction=-, delta=-76.65630629203233, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.7084365608079433, baseline=93.15630629203233, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.7084365608079433, baseline=93.15630629203233, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#104  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 24 2026 20:03 UTC -> Tue Mar 24 2026 22:22 UTC (duration 2.32h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 110, delta +93.5 (+566.67%).

**Calendar context:** Tuesday, hour 20 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.39σ vs. the median of 94 prior Tuesday 20:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=0.0, direction=+, delta=93.49982168744714, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#105  —  TP  —  GT: month_shift, degradation_trajectory

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

## Case outlet_120d#106  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 24 2026 21:21 UTC -> Wed Mar 25 2026 10:08 UTC (duration 12.78h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 113, delta +96.46 (+584.61%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.47σ vs. the median of 92 prior Tuesday 21:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=32.992283586554144, direction=+, delta=96.4598510425418, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.923709442224047, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.923709442224047, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#107  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 25 2026 09:32 UTC -> Wed Mar 25 2026 11:54 UTC (duration 2.37h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 109.1, delta +92.6 (+561.18%).

**Calendar context:** Wednesday, hour 9 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.36σ vs. the median of 99 prior Wednesday 9:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=38.73595143486779, direction=+, delta=92.59524201476808, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.390421264608964, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.390421264608964, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#108  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Mar 25 2026 11:02 UTC -> Fri Mar 27 2026 05:12 UTC (duration 1.76d).
**Long-duration framing:** spans 1.8 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 117.9, delta +101.4 (+614.46%).

**Calendar context:** Wednesday, hour 11 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.65σ vs. the median of 94 prior Wednesday 11:00 samples (peer median 40.28).

**Detector evidence:**
- cusum: mu=16.5, sigma=44.954275047629245, direction=+, delta=101.3865853690004, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.2553268907480075, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2553268907480075, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=11, same_hour_median=16.5, approx_hour_z=0.2633461196155891, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#109  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 27 2026 04:25 UTC -> Fri Mar 27 2026 06:37 UTC (duration 2.20h).

**Magnitude:** baseline 103.5 (source: prewindow_2h), peak 16.5, delta -86.99 (-84.06%).

**Calendar context:** Friday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 97 prior Friday 4:00 samples (peer median 16.5).

**Detector evidence:**
- multivariate_pca: approx_residual_z=2.4418997590739298, baseline=103.48653461869002, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.4418997590739298, baseline=103.48653461869002, source=derived_from_prewindow

**Detectors fired:** multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#110  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 27 2026 06:06 UTC -> Fri Mar 27 2026 08:57 UTC (duration 2.85h).

**Magnitude:** baseline 100.2 (source: prewindow_2h), peak 16.5, delta -83.69 (-83.53%).

**Calendar context:** Friday, hour 6 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 104 prior Friday 6:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=100.188338271834, sigma=43.777792297932244, direction=-, delta=-83.688338271834, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.9116619152991607, baseline=100.188338271834, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.9116619152991607, baseline=100.188338271834, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#111  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 27 2026 08:15 UTC -> Fri Mar 27 2026 15:05 UTC (duration 6.83h).

**Magnitude:** baseline 104.6 (source: prewindow_2h), peak 16.5, delta -88.13 (-84.23%).

**Calendar context:** Friday, hour 8 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.54σ vs. the median of 102 prior Friday 8:00 samples (peer median 88.22).

**Detector evidence:**
- cusum: mu=104.63351336021576, sigma=29.53044073466426, direction=-, delta=-88.13351336021576, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.984497053467962, baseline=104.63351336021576, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.984497053467962, baseline=104.63351336021576, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#112  —  TP  —  GT: month_shift, degradation_trajectory

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

## Case outlet_120d#113  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Mar 27 2026 14:07 UTC -> Tue Mar 31 2026 14:10 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 115.9, delta +99.4 (+602.40%).

**Calendar context:** Friday, hour 14 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.23σ vs. the median of 105 prior Friday 14:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=41.287292634762885, direction=+, delta=99.3957598054547, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.4074177177160294, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.4074177177160294, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#114  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 13:32 UTC -> Tue Mar 31 2026 18:59 UTC (duration 5.45h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 113.7, delta +97.22 (+589.21%).

**Calendar context:** Tuesday, hour 13 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.48σ vs. the median of 116 prior Tuesday 13:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=42.499826302812416, direction=+, delta=97.22013256957682, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.287541880215715, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.287541880215715, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#115  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 17:55 UTC -> Tue Mar 31 2026 22:29 UTC (duration 4.57h).

**Magnitude:** baseline 98.56 (source: prewindow_2h), peak 16.5, delta -82.06 (-83.26%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 116 prior Tuesday 17:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=98.55804252935414, sigma=44.949029112429315, direction=-, delta=-82.05804252935414, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.8255798656764186, baseline=98.55804252935414, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.8255798656764186, baseline=98.55804252935414, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#116  —  TP  —  GT: month_shift, degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat Mar 28 2026 22:05 UTC -> Thu Apr 02 2026 00:10 UTC (duration 4.09d).
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

## Case outlet_120d#117  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 21:29 UTC -> Thu Apr 02 2026 00:19 UTC (duration 1.12d).
**Long-duration framing:** spans 1.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 118.3, delta +101.8 (+616.85%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.47σ vs. the median of 106 prior Tuesday 21:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=43.544224652660894, direction=+, delta=101.77961473010592, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.337384935475855, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.337384935475855, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#118  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Apr 02 2026 00:11 UTC -> Fri Apr 03 2026 10:15 UTC (duration 1.42d).
**Long-duration framing:** spans 1.4 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 117.2, delta +100.7 (+610.42%).

**Calendar context:** Thursday, hour 0 (night), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.27σ vs. the median of 114 prior Thursday 0:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=17.34967886768814, direction=+, delta=100.71918570762274, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=5.805247836327455, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=5.805247836327455, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=0, same_hour_median=16.5, approx_hour_z=2.3195615250506982, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#119  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Apr 03 2026 09:31 UTC -> Sat Apr 04 2026 01:21 UTC (duration 15.83h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 115.7, delta +99.17 (+601.06%).

**Calendar context:** Friday, hour 9 (morning), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.23σ vs. the median of 107 prior Friday 9:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=39.155861820885896, direction=+, delta=99.17438884596652, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.532810778105936, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.532810778105936, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#120  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Wed Apr 01 2026 22:06 UTC -> Mon Apr 06 2026 00:11 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 124.3 (source: prewindow_2h), peak 122.8, delta -1.45 (-1.17%).

**Calendar context:** Wednesday, hour 22 (evening), weekday, April.
**Same-hour-of-weekday baseline:** peak is -0.82σ vs. the median of 49 prior Wednesday 22:00 samples (peer median 125).

**Detector evidence:**
- cusum: mu=124.29547658956011, sigma=0.5567862718916698, direction=-, delta=-1.4498115850625481, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.603892477694975, baseline=124.29547658956011, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.603892477694975, baseline=124.29547658956011, source=derived_from_prewindow
- temporal_profile: hour_of_day=22, same_hour_median=125.54556755098564, approx_hour_z=-1.006757453074711, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 45.9 (threshold 0).

---

## Case outlet_120d#121  —  TP  —  GT: spike

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Apr 04 2026 00:17 UTC -> Mon Apr 06 2026 03:08 UTC (duration 2.12d).
**Long-duration framing:** spans 2.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 656.4, delta +639.9 (+3878.35%).

**Calendar context:** Saturday, hour 0 (night), weekend, April.
**Same-hour-of-weekday baseline:** peak is +14.99σ vs. the median of 120 prior Saturday 0:00 samples (peer median 36.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=43.42592898996616, direction=+, delta=639.9272725122842, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=14.736064084205164, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=14.736064084205164, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=0, same_hour_median=16.5, approx_hour_z=14.742823783459546, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 6.72e+05 (threshold 0).

---

## Case outlet_120d#122  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Apr 06 2026 02:25 UTC -> Tue Apr 07 2026 12:24 UTC (duration 1.42d).
**Long-duration framing:** spans 1.4 days; covers 0 weekend day(s).

**Magnitude:** baseline 103.4 (source: prewindow_2h), peak 16.5, delta -86.95 (-84.05%).

**Calendar context:** Monday, hour 2 (night), weekday, April.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 153 prior Monday 2:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=103.44807450909718, sigma=44.37293498296398, direction=-, delta=-86.94807450909718, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.959484414147475, baseline=103.44807450909718, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.959484414147475, baseline=103.44807450909718, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#123  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 07 2026 11:24 UTC -> Tue Apr 07 2026 21:33 UTC (duration 10.15h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 115.1, delta +98.64 (+597.83%).

**Calendar context:** Tuesday, hour 11 (morning), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.34σ vs. the median of 128 prior Tuesday 11:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=32.901903704052316, direction=+, delta=98.64137631410884, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.9980446481569336, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.9980446481569336, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#124  —  TP  —  GT: dip

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 08 2026 09:00 UTC -> Wed Apr 08 2026 09:01 UTC (duration 1.0m).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak -68.5, delta -85 (-515.15%).

**Calendar context:** Wednesday, hour 9 (morning), weekday, April.
**Same-hour-of-weekday baseline:** peak is -2.11σ vs. the median of 120 prior Wednesday 9:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-68.5, score=-68.5

**Detectors fired:** data_quality_gate.

**Score:** -68.5 (threshold 0).

---

## Case outlet_120d#125  —  TP  —  GT: dip

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 07 2026 21:10 UTC -> Wed Apr 08 2026 15:38 UTC (duration 18.47h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 118.1, delta +101.6 (+615.48%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.50σ vs. the median of 115 prior Tuesday 21:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=41.33462997614855, direction=+, delta=101.5544915185688, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.45688643099428, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.45688643099428, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=21, same_hour_median=16.5, approx_hour_z=2.275683481338943, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 5.15e+04 (threshold 0).

---

## Case outlet_120d#126  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 08 2026 14:42 UTC -> Thu Apr 09 2026 06:04 UTC (duration 15.37h).

**Magnitude:** baseline 57.78 (source: prewindow_2h), peak 115.8, delta +57.97 (+100.33%).

**Calendar context:** Wednesday, hour 14 (afternoon), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.51σ vs. the median of 129 prior Wednesday 14:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=57.78167120932825, sigma=45.75540075973209, direction=+, delta=57.97498968975363, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.2670633133384248, baseline=57.78167120932825, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.2670633133384248, baseline=57.78167120932825, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#127  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Apr 05 2026 22:07 UTC -> Fri Apr 10 2026 00:12 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 124.2 (source: prewindow_2h), peak 122.8, delta -1.392 (-1.12%).

**Calendar context:** Sunday, hour 22 (evening), weekend, April.
**Same-hour-of-weekday baseline:** peak is -1.04σ vs. the median of 55 prior Sunday 22:00 samples (peer median 125.8).

**Detector evidence:**
- cusum: mu=124.15404223590039, sigma=0.42751980084698804, direction=-, delta=-1.3923708138320308, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.2568569013026107, baseline=124.15404223590039, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.2568569013026107, baseline=124.15404223590039, source=derived_from_prewindow
- temporal_profile: hour_of_day=22, same_hour_median=125.03930200237824, approx_hour_z=-0.8769311832781083, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 46 (threshold 0).

---

## Case outlet_120d#128  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Apr 09 2026 05:20 UTC -> Fri Apr 10 2026 01:17 UTC (duration 19.95h).

**Magnitude:** baseline 98.63 (source: prewindow_2h), peak 16.5, delta -82.13 (-83.27%).

**Calendar context:** Thursday, hour 5 (night), weekday, April.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 122 prior Thursday 5:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=98.63056137224979, sigma=44.19805891682972, direction=-, delta=-82.13056137224979, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.8582391033687713, baseline=98.63056137224979, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.8582391033687713, baseline=98.63056137224979, source=derived_from_prewindow
- temporal_profile: hour_of_day=5, same_hour_median=16.5, approx_hour_z=0.0, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#129  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Apr 10 2026 00:40 UTC -> Fri Apr 10 2026 22:04 UTC (duration 21.40h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 118.1, delta +101.6 (+615.60%).

**Calendar context:** Friday, hour 0 (night), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.46σ vs. the median of 132 prior Friday 0:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=42.29635968636219, direction=+, delta=101.5737535824144, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.401477440035231, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.401477440035231, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#130  —  TP  —  GT: noise_burst

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Apr 11 2026 12:00 UTC -> Sat Apr 11 2026 12:01 UTC (duration 1.0m).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak -48.58, delta -65.08 (-394.44%).

**Calendar context:** Saturday, hour 12 (afternoon), weekend, April.
**Same-hour-of-weekday baseline:** peak is -1.79σ vs. the median of 112 prior Saturday 12:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-48.5832379776826, score=-22.63331589171321

**Detectors fired:** data_quality_gate.

**Score:** -22.6 (threshold 0).

---

## Case outlet_120d#131  —  TP  —  GT: noise_burst

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Apr 10 2026 21:01 UTC -> Sat Apr 11 2026 18:50 UTC (duration 21.82h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 194, delta +177.5 (+1075.50%).

**Calendar context:** Friday, hour 21 (evening), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.17σ vs. the median of 133 prior Friday 21:00 samples (peer median 92.01).

**Detector evidence:**
- cusum: mu=16.5, sigma=45.0658932157475, direction=+, delta=177.4579146212552, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.937743201309624, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.937743201309624, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 3.02e+04 (threshold 0).

---

## Case outlet_120d#132  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Apr 11 2026 17:53 UTC -> Sun Apr 12 2026 17:56 UTC (duration 1.00d).
**Long-duration framing:** spans 1.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 114.4, delta +97.91 (+593.41%).

**Calendar context:** Saturday, hour 17 (afternoon), weekend, April.
**Same-hour-of-weekday baseline:** peak is +2.36σ vs. the median of 130 prior Saturday 17:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=35.96290215999942, direction=+, delta=97.91310397325724, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.722614085416148, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.722614085416148, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#133  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Apr 12 2026 16:53 UTC -> Mon Apr 13 2026 04:34 UTC (duration 11.68h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 115.1, delta +98.61 (+597.64%).

**Calendar context:** Sunday, hour 16 (afternoon), weekend, April.
**Same-hour-of-weekday baseline:** peak is +0.64σ vs. the median of 158 prior Sunday 16:00 samples (peer median 86.9).

**Detector evidence:**
- cusum: mu=16.5, sigma=43.9978852670796, direction=+, delta=98.6100163377324, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.241244453890039, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.241244453890039, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#134  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Apr 09 2026 22:08 UTC -> Tue Apr 14 2026 00:13 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 124 (source: prewindow_2h), peak 125.4, delta +1.411 (+1.14%).

**Calendar context:** Thursday, hour 22 (evening), weekday, April.
**Same-hour-of-weekday baseline:** peak is +0.04σ vs. the median of 55 prior Thursday 22:00 samples (peer median 125.3).

**Detector evidence:**
- cusum: mu=123.99695996262841, sigma=0.5456325986553483, direction=+, delta=1.410538460229688, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.5851433065139533, baseline=123.99695996262841, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.5851433065139533, baseline=123.99695996262841, source=derived_from_prewindow
- temporal_profile: hour_of_day=22, same_hour_median=124.55842056965687, approx_hour_z=0.3368874892756497, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 44.4 (threshold 0).

---

## Case outlet_120d#135  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Apr 13 2026 03:41 UTC -> Tue Apr 14 2026 02:26 UTC (duration 22.75h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 116.4, delta +99.9 (+605.46%).

**Calendar context:** Monday, hour 3 (night), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.29σ vs. the median of 159 prior Monday 3:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=41.65007020199092, direction=+, delta=99.90093515686242, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.3985778336596186, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.3985778336596186, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#136  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Apr 14 2026 14:00 UTC -> Tue Apr 14 2026 14:01 UTC (duration 1.0m).

**Magnitude:** baseline 124.1 (source: prewindow_2h), peak 180, delta +55.89 (+45.04%).

**Calendar context:** Tuesday, hour 14 (afternoon), weekday, April.
**Same-hour-of-weekday baseline:** peak is +24.97σ vs. the median of 60 prior Tuesday 14:00 samples (peer median 124.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=180.0, score=180.0

**Detectors fired:** data_quality_gate.

**Score:** 180 (threshold 0).

---

## Case outlet_120d#137  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 14 2026 01:57 UTC -> Tue Apr 14 2026 13:21 UTC (duration 11.40h).

**Magnitude:** baseline 100.6 (source: prewindow_2h), peak 16.5, delta -84.11 (-83.60%).

**Calendar context:** Tuesday, hour 1 (night), weekday, April.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 143 prior Tuesday 1:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=100.61014471444969, sigma=44.25779269066012, direction=-, delta=-84.11014471444969, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.9004595484988964, baseline=100.61014471444969, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.9004595484988964, baseline=100.61014471444969, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#138  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 14 2026 12:57 UTC -> Thu Apr 16 2026 09:23 UTC (duration 1.85d).
**Long-duration framing:** spans 1.9 days; covers 0 weekend day(s).

**Magnitude:** baseline 59.23 (source: prewindow_2h), peak 115.7, delta +56.52 (+95.42%).

**Calendar context:** Tuesday, hour 12 (afternoon), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.23σ vs. the median of 150 prior Tuesday 12:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=59.2272631947959, sigma=45.711778000175784, direction=+, delta=56.515532964624676, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.2363451048525689, baseline=59.2272631947959, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.2363451048525689, baseline=59.2272631947959, source=derived_from_prewindow
- temporal_profile: hour_of_day=12, same_hour_median=24.76688993812272, approx_hour_z=1.813046451664535, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#139  —  TP  —  GT: out_of_range, calibration_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Mon Apr 13 2026 22:09 UTC -> Sat Apr 18 2026 00:14 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 123.8 (source: prewindow_2h), peak 180, delta +56.17 (+45.36%).

**Calendar context:** Monday, hour 22 (evening), weekday, April.
**Same-hour-of-weekday baseline:** peak is +20.41σ vs. the median of 61 prior Monday 22:00 samples (peer median 124.9).

**Detector evidence:**
- cusum: mu=123.83241787963291, sigma=0.29432694337029913, direction=+, delta=56.167582120367086, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=190.83398032541461, baseline=123.83241787963291, source=derived_from_prewindow
- sub_pca: approx_residual_z=190.83398032541461, baseline=123.83241787963291, source=derived_from_prewindow
- temporal_profile: hour_of_day=22, same_hour_median=124.46657956821072, approx_hour_z=22.668066542481046, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 5.76e+03 (threshold 0).

---

## Case outlet_120d#140  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Apr 16 2026 08:25 UTC -> Sat Apr 18 2026 00:18 UTC (duration 1.66d).
**Long-duration framing:** spans 1.7 days; covers 1 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 116.7, delta +100.2 (+607.32%).

**Calendar context:** Thursday, hour 8 (morning), weekday, April.
**Same-hour-of-weekday baseline:** peak is +0.69σ vs. the median of 140 prior Thursday 8:00 samples (peer median 86.79).

**Detector evidence:**
- cusum: mu=16.5, sigma=32.3071096307181, direction=+, delta=100.20788498276066, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.101728570836973, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.101728570836973, baseline=16.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=8, same_hour_median=16.5, approx_hour_z=2.2490166172875212, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#141  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Apr 17 2026 23:16 UTC -> Sat Apr 18 2026 03:01 UTC (duration 3.75h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 115.8, delta +99.35 (+602.10%).

**Calendar context:** Friday, hour 23 (evening), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.47σ vs. the median of 140 prior Friday 23:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=42.954417508468026, direction=+, delta=99.34700044677066, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.312847111177457, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.312847111177457, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#142  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Apr 18 2026 01:58 UTC -> Sat Apr 18 2026 11:53 UTC (duration 9.92h).

**Magnitude:** baseline 103.4 (source: prewindow_2h), peak 16.5, delta -86.89 (-84.04%).

**Calendar context:** Saturday, hour 1 (night), weekend, April.
**Same-hour-of-weekday baseline:** peak is -1.57σ vs. the median of 154 prior Saturday 1:00 samples (peer median 95.46).

**Detector evidence:**
- cusum: mu=103.38602678614836, sigma=37.89695279938275, direction=-, delta=-86.88602678614836, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.292691637929357, baseline=103.38602678614836, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.292691637929357, baseline=103.38602678614836, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#143  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Apr 18 2026 10:53 UTC -> Tue Apr 21 2026 03:34 UTC (duration 2.70d).
**Long-duration framing:** spans 2.7 days; covers 2 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 115.8, delta +99.27 (+601.61%).

**Calendar context:** Saturday, hour 10 (morning), weekend, April.
**Same-hour-of-weekday baseline:** peak is +2.74σ vs. the median of 141 prior Saturday 10:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=42.00270506691631, direction=+, delta=99.2658640703612, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.3633207411812287, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.3633207411812287, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#144  —  TP  —  GT: calibration_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Fri Apr 17 2026 22:10 UTC -> Wed Apr 22 2026 00:15 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 123.9 (source: prewindow_2h), peak 119.9, delta -3.958 (-3.19%).

**Calendar context:** Friday, hour 22 (evening), weekday, April.
**Same-hour-of-weekday baseline:** peak is -1.98σ vs. the median of 61 prior Friday 22:00 samples (peer median 124.9).

**Detector evidence:**
- cusum: mu=123.88305887000641, sigma=0.3262454991121795, direction=-, delta=-3.957603903912613, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=12.130754032415911, baseline=123.88305887000641, source=derived_from_prewindow
- sub_pca: approx_residual_z=12.130754032415911, baseline=123.88305887000641, source=derived_from_prewindow
- temporal_profile: hour_of_day=22, same_hour_median=124.39140085067882, approx_hour_z=-1.8726924432516294, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 23.1 (threshold 0).

---

## Case outlet_120d#145  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 21 2026 02:34 UTC -> Wed Apr 22 2026 09:48 UTC (duration 1.30d).
**Long-duration framing:** spans 1.3 days; covers 0 weekend day(s).

**Magnitude:** baseline 94.16 (source: prewindow_2h), peak 16.5, delta -77.66 (-82.48%).

**Calendar context:** Tuesday, hour 2 (night), weekday, April.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 166 prior Tuesday 2:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=94.16312018420184, sigma=45.309340490166896, direction=-, delta=-77.66312018420184, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.7140642380582964, baseline=94.16312018420184, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.7140642380582964, baseline=94.16312018420184, source=derived_from_prewindow
- temporal_profile: hour_of_day=2, same_hour_median=16.5, approx_hour_z=0.0, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#146  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 22 2026 09:02 UTC -> Wed Apr 22 2026 11:53 UTC (duration 2.85h).

**Magnitude:** baseline 102.1 (source: prewindow_2h), peak 16.5, delta -85.63 (-83.84%).

**Calendar context:** Wednesday, hour 9 (morning), weekday, April.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 149 prior Wednesday 9:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=102.12894000765505, sigma=44.784548712927666, direction=-, delta=-85.62894000765505, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.9120197136861423, baseline=102.12894000765505, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.9120197136861423, baseline=102.12894000765505, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#147  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 22 2026 11:15 UTC -> Thu Apr 23 2026 05:08 UTC (duration 17.88h).

**Magnitude:** baseline 104.5 (source: prewindow_2h), peak 16.5, delta -87.99 (-84.21%).

**Calendar context:** Wednesday, hour 11 (morning), weekday, April.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 149 prior Wednesday 11:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=104.48762041428769, sigma=39.50616229912097, direction=-, delta=-87.98762041428769, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.2271872359580076, baseline=104.48762041428769, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2271872359580076, baseline=104.48762041428769, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#148  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu Apr 23 2026 04:15 UTC -> Fri Apr 24 2026 16:30 UTC (duration 1.51d).
**Long-duration framing:** spans 1.5 days; covers 0 weekend day(s).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 119.9, delta +103.4 (+626.72%).

**Calendar context:** Thursday, hour 4 (night), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.46σ vs. the median of 156 prior Thursday 4:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=32.70355216183907, direction=+, delta=103.4086686297466, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.1620011220191397, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.1620011220191397, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#149  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri Apr 24 2026 16:18 UTC -> Sat Apr 25 2026 14:20 UTC (duration 22.03h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 117.6, delta +101.1 (+612.78%).

**Calendar context:** Friday, hour 16 (afternoon), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.37σ vs. the median of 149 prior Friday 16:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=25.037503274751547, direction=+, delta=101.10819025004376, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=4.038269676513785, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.038269676513785, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#150  —  TP  —  GT: trend

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Apr 21 2026 23:13 UTC -> Sun Apr 26 2026 00:16 UTC (duration 4.04d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 120.9 (source: prewindow_2h), peak 119.3, delta -1.555 (-1.29%).

**Calendar context:** Tuesday, hour 23 (evening), weekday, April.
**Same-hour-of-weekday baseline:** peak is -2.26σ vs. the median of 68 prior Tuesday 23:00 samples (peer median 124.2).

**Detector evidence:**
- cusum: mu=120.85892113149194, sigma=0.31727423330572474, direction=-, delta=-1.555035023189916, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=4.9012332548653195, baseline=120.85892113149194, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.9012332548653195, baseline=120.85892113149194, source=derived_from_prewindow
- temporal_profile: hour_of_day=23, same_hour_median=124.3854661567555, approx_hour_z=-2.1332084495244668, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 12.6 (threshold 0).

---

## Case outlet_120d#151  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Apr 25 2026 14:01 UTC -> Mon Apr 27 2026 18:29 UTC (duration 2.19d).
**Long-duration framing:** spans 2.2 days; covers 2 weekend day(s).

**Magnitude:** baseline 104.1 (source: prewindow_2h), peak 16.5, delta -87.57 (-84.14%).

**Calendar context:** Saturday, hour 14 (afternoon), weekend, April.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 141 prior Saturday 14:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=104.06657034321229, sigma=40.14718409270328, direction=-, delta=-87.56657034321229, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.1811385361676576, baseline=104.06657034321229, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.1811385361676576, baseline=104.06657034321229, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#152  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Apr 27 2026 17:59 UTC -> Tue Apr 28 2026 04:30 UTC (duration 10.52h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 116, delta +99.53 (+603.19%).

**Calendar context:** Monday, hour 17 (afternoon), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.26σ vs. the median of 196 prior Monday 17:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=43.97263083669014, direction=+, delta=99.52604965151804, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.2633635458644177, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2633635458644177, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#153  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 28 2026 03:40 UTC -> Tue Apr 28 2026 21:47 UTC (duration 18.12h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 117.6, delta +101.1 (+612.87%).

**Calendar context:** Tuesday, hour 3 (night), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.30σ vs. the median of 171 prior Tuesday 3:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=43.000093644295454, direction=+, delta=101.12374137687408, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.3517097942480762, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.3517097942480762, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#154  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Apr 28 2026 20:46 UTC -> Wed Apr 29 2026 01:28 UTC (duration 4.70h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 112, delta +95.49 (+578.72%).

**Calendar context:** Tuesday, hour 20 (evening), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.58σ vs. the median of 166 prior Tuesday 20:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=44.650210087249775, direction=+, delta=95.4883264241364, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.138586274007339, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.138586274007339, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#155  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 29 2026 00:55 UTC -> Wed Apr 29 2026 14:56 UTC (duration 14.02h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 117.1, delta +100.6 (+609.56%).

**Calendar context:** Wednesday, hour 0 (night), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.52σ vs. the median of 172 prior Wednesday 0:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=41.59349715141766, direction=+, delta=100.57797783773688, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.4181178483644, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.4181178483644, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#156  —  TP  —  GT: trend

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun Apr 26 2026 21:41 UTC -> Wed Apr 29 2026 16:02 UTC (duration 2.76d).
**Long-duration framing:** spans 2.8 days; covers 1 weekend day(s).

**Magnitude:** baseline 119.3 (source: prewindow_2h), peak 121.9, delta +2.588 (+2.17%).

**Calendar context:** Sunday, hour 21 (evening), weekend, April.
**Same-hour-of-weekday baseline:** peak is -0.88σ vs. the median of 77 prior Sunday 21:00 samples (peer median 124.3).

**Detector evidence:**
- cusum: mu=119.26965015329783, sigma=0.311034260506075, direction=+, delta=2.588480472590433, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=8.322171545921629, baseline=119.26965015329783, source=derived_from_prewindow
- sub_pca: approx_residual_z=8.322171545921629, baseline=119.26965015329783, source=derived_from_prewindow
- temporal_profile: hour_of_day=21, same_hour_median=124.12381668079732, approx_hour_z=-0.9220641576399442, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 21.3 (threshold 0).

---

## Case outlet_120d#157  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 29 2026 13:56 UTC -> Wed Apr 29 2026 21:08 UTC (duration 7.20h).

**Magnitude:** baseline 16.5 (source: prewindow_2h), peak 114.7, delta +98.21 (+595.21%).

**Calendar context:** Wednesday, hour 13 (afternoon), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.82σ vs. the median of 165 prior Wednesday 13:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=16.5, sigma=40.43891610001744, direction=+, delta=98.21008512938384, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.428603301000481, baseline=16.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.428603301000481, baseline=16.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#158  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Apr 29 2026 20:15 UTC -> Fri May 01 2026 12:57 UTC (duration 1.70d).
**Long-duration framing:** spans 1.7 days; covers 0 weekend day(s).

**Magnitude:** baseline 55.93 (source: prewindow_2h), peak 114, delta +58.08 (+103.84%).

**Calendar context:** Wednesday, hour 20 (evening), weekday, April.
**Same-hour-of-weekday baseline:** peak is +1.71σ vs. the median of 166 prior Wednesday 20:00 samples (peer median 40.28).

**Detector evidence:**
- cusum: mu=55.93235396473218, sigma=44.974962174154875, direction=+, delta=58.08258840887506, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.2914427406067406, baseline=55.93235396473218, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.2914427406067406, baseline=55.93235396473218, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.81e+04 (threshold 0).

---

## Case outlet_120d#159  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 01 2026 12:00 UTC -> Fri May 01 2026 19:21 UTC (duration 7.35h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 101.1, delta +94.56 (+1454.72%).

**Calendar context:** Friday, hour 12 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.59σ vs. the median of 1470 prior Friday 12:00 samples (peer median 19.48).

**Detector evidence:**
- cusum: mu=6.5, sigma=39.46716914198736, direction=+, delta=94.55702265021914, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.39584000337192, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#160  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 01 2026 18:21 UTC -> Fri May 01 2026 23:55 UTC (duration 5.57h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 100.1, delta +93.58 (+1439.64%).

**Calendar context:** Friday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.77σ vs. the median of 164 prior Friday 18:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=44.5658926503969, direction=+, delta=93.57655864991044, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.0997348663917554, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#161  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 01 2026 23:23 UTC -> Sat May 02 2026 05:13 UTC (duration 5.83h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 103.8, delta +97.3 (+1496.93%).

**Calendar context:** Friday, hour 23 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.13σ vs. the median of 171 prior Friday 23:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=42.33688143499345, direction=+, delta=97.30062912004112, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2982474339646926, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#162  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 02 2026 04:21 UTC -> Sun May 03 2026 07:29 UTC (duration 1.13d).
**Long-duration framing:** spans 1.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 103.8, delta +97.3 (+1496.93%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is +1.77σ vs. the median of 161 prior Saturday 4:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=42.28580468556112, direction=+, delta=97.30062912004112, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.301023472145614, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#163  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Wed Apr 29 2026 17:55 UTC -> Sun May 03 2026 17:55 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 121.1 (source: prewindow_2h), peak 119.8, delta -1.333 (-1.10%).

**Calendar context:** Wednesday, hour 17 (afternoon), weekday, April.
**Same-hour-of-weekday baseline:** peak is -1.83σ vs. the median of 78 prior Wednesday 17:00 samples (peer median 124.1).

**Detector evidence:**
- cusum: mu=121.12697506883745, sigma=0.41509549377295474, direction=-, delta=-1.3332466842142878, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.211903535969329, baseline=121.12697506883745, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.211903535969329, baseline=121.12697506883745, source=derived_from_prewindow
- temporal_profile: hour_of_day=17, same_hour_median=124.10786804593319, approx_hour_z=-1.6824509026108017, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 9.55 (threshold 0).

---

## Case outlet_120d#164  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun May 03 2026 06:33 UTC -> Sun May 03 2026 20:51 UTC (duration 14.30h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 104.8, delta +98.29 (+1512.15%).

**Calendar context:** Sunday, hour 6 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is +2.06σ vs. the median of 175 prior Sunday 6:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=43.26185807550174, direction=+, delta=98.28988954523784, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2719756829144906, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#165  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun May 03 2026 19:58 UTC -> Mon May 04 2026 02:54 UTC (duration 6.93h).

**Magnitude:** baseline 94.58 (source: prewindow_2h), peak 6.5, delta -88.08 (-93.13%).

**Calendar context:** Sunday, hour 19 (evening), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.69σ vs. the median of 182 prior Sunday 19:00 samples (peer median 36.5).

**Detector evidence:**
- cusum: mu=94.58347364621812, sigma=37.32242156691842, direction=-, delta=-88.08347364621812, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.3600685579387197, baseline=94.58347364621812, source=derived_from_prewindow
- temporal_profile: hour_of_day=19, same_hour_median=16.5, approx_hour_z=-0.22893988548692495, source=derived_from_same_hour_history

**Detectors fired:** cusum, sub_pca, temporal_profile.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#166  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 04 2026 01:55 UTC -> Mon May 04 2026 22:49 UTC (duration 20.90h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 167.8, delta +161.3 (+2481.22%).

**Calendar context:** Monday, hour 1 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +3.28σ vs. the median of 204 prior Monday 1:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=33.385032158306494, direction=+, delta=161.27928404026667, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.830885987334265, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#167  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 04 2026 21:54 UTC -> Thu May 07 2026 00:04 UTC (duration 2.09d).
**Long-duration framing:** spans 2.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 169.9, delta +163.4 (+2514.01%).

**Calendar context:** Monday, hour 21 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is +3.44σ vs. the median of 186 prior Monday 21:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=32.73065837866703, direction=+, delta=163.410854043391, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.9925929430707034, baseline=6.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=21, same_hour_median=16.5, approx_hour_z=3.4973662906364558, source=derived_from_same_hour_history

**Detectors fired:** cusum, sub_pca, temporal_profile.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#168  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun May 03 2026 16:19 UTC -> Thu May 07 2026 17:56 UTC (duration 4.07d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 121 (source: prewindow_2h), peak 122.4, delta +1.428 (+1.18%).

**Calendar context:** Sunday, hour 16 (afternoon), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.54σ vs. the median of 80 prior Sunday 16:00 samples (peer median 123.9).

**Detector evidence:**
- cusum: mu=120.9527773861839, sigma=0.32516459892984895, direction=+, delta=1.4284048064352248, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=4.39286690844039, baseline=120.9527773861839, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.39286690844039, baseline=120.9527773861839, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 9.16 (threshold 0).

---

## Case outlet_120d#169  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed May 06 2026 23:10 UTC -> Fri May 08 2026 03:40 UTC (duration 1.19d).
**Long-duration framing:** spans 1.2 days; covers 0 weekend day(s).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 106.8, delta +100.3 (+1543.64%).

**Calendar context:** Wednesday, hour 23 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.24σ vs. the median of 172 prior Wednesday 23:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=18.638769416016817, direction=+, delta=100.33686283333324, source=derived_from_prewindow
- sub_pca: approx_residual_z=5.383234300173861, baseline=6.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=23, same_hour_median=16.5, approx_hour_z=2.1709672226246086, source=derived_from_same_hour_history

**Detectors fired:** cusum, sub_pca, temporal_profile.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#170  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 08 2026 02:38 UTC -> Fri May 08 2026 12:27 UTC (duration 9.82h).

**Magnitude:** baseline 87.85 (source: prewindow_2h), peak 6.5, delta -81.35 (-92.60%).

**Calendar context:** Friday, hour 2 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.23σ vs. the median of 185 prior Friday 2:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=87.85241859858142, sigma=45.45584412676675, direction=-, delta=-81.35241859858142, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.7897020759686413, baseline=87.85241859858142, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#171  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 02:21 UTC -> Sat May 09 2026 02:22 UTC (duration 1.0m).

**Magnitude:** baseline 88.47 (source: prewindow_2h), peak -9.436, delta -97.91 (-110.66%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.51σ vs. the median of 188 prior Saturday 2:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-9.435599743717225, score=-9.435599743717225

**Detectors fired:** data_quality_gate.

**Score:** -9.44 (threshold 0).

---

## Case outlet_120d#172  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 02:55 UTC -> Sat May 09 2026 02:56 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak -9.192, delta -15.69 (-241.42%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.51σ vs. the median of 204 prior Saturday 2:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-9.192284032267558, score=-9.192284032267558

**Detectors fired:** data_quality_gate.

**Score:** -9.19 (threshold 0).

---

## Case outlet_120d#173  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 03:28 UTC -> Sat May 09 2026 03:29 UTC (duration 1.0m).

**Magnitude:** baseline 14.82 (source: prewindow_2h), peak -10.38, delta -25.2 (-170.06%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.52σ vs. the median of 196 prior Saturday 3:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-10.383320203025692, score=-10.383320203025692

**Detectors fired:** data_quality_gate.

**Score:** -10.4 (threshold 0).

---

## Case outlet_120d#174  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 04:01 UTC -> Sat May 09 2026 04:02 UTC (duration 1.0m).

**Magnitude:** baseline 14.82 (source: prewindow_2h), peak -10.38, delta -25.2 (-170.06%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.55σ vs. the median of 171 prior Saturday 4:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-10.383320203025676, score=-10.383320203025676

**Detectors fired:** data_quality_gate.

**Score:** -10.4 (threshold 0).

---

## Case outlet_120d#175  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 04:59 UTC -> Sat May 09 2026 05:00 UTC (duration 1.0m).

**Magnitude:** baseline 19.63 (source: prewindow_2h), peak -5.544, delta -25.17 (-128.24%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.45σ vs. the median of 208 prior Saturday 4:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-5.543841852543249, score=-5.543841852543249

**Detectors fired:** data_quality_gate.

**Score:** -5.54 (threshold 0).

---

## Case outlet_120d#176  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 05:33 UTC -> Sat May 09 2026 05:34 UTC (duration 1.0m).

**Magnitude:** baseline 19.63 (source: prewindow_2h), peak -5.544, delta -25.17 (-128.24%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.50σ vs. the median of 198 prior Saturday 5:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-5.543841852543228, score=-5.543841852543228

**Detectors fired:** data_quality_gate.

**Score:** -5.54 (threshold 0).

---

## Case outlet_120d#177  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 06:06 UTC -> Sat May 09 2026 06:07 UTC (duration 1.0m).

**Magnitude:** baseline 19.63 (source: prewindow_2h), peak -0.6255, delta -20.25 (-103.19%).

**Calendar context:** Saturday, hour 6 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.25σ vs. the median of 179 prior Saturday 6:00 samples (peer median 56.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.6254815617492255, score=-0.6254815617492255

**Detectors fired:** data_quality_gate.

**Score:** -0.625 (threshold 0).

---

## Case outlet_120d#178  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 06:39 UTC -> Sat May 09 2026 06:40 UTC (duration 1.0m).

**Magnitude:** baseline 14.52 (source: prewindow_2h), peak -0.6255, delta -15.15 (-104.31%).

**Calendar context:** Saturday, hour 6 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.65σ vs. the median of 203 prior Saturday 6:00 samples (peer median 29.63).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.6254815617492016, score=-0.6254815617492016

**Detectors fired:** data_quality_gate.

**Score:** -0.625 (threshold 0).

---

## Case outlet_120d#179  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 07:12 UTC -> Sat May 09 2026 07:13 UTC (duration 1.0m).

**Magnitude:** baseline 9.633 (source: prewindow_2h), peak -0.6255, delta -10.26 (-106.49%).

**Calendar context:** Saturday, hour 7 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.41σ vs. the median of 185 prior Saturday 7:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.6254815617498597, score=-0.6254815617498597

**Detectors fired:** data_quality_gate.

**Score:** -0.625 (threshold 0).

---

## Case outlet_120d#180  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 07:46 UTC -> Sat May 09 2026 07:47 UTC (duration 1.0m).

**Magnitude:** baseline 14.52 (source: prewindow_2h), peak -0.6255, delta -15.15 (-104.31%).

**Calendar context:** Saturday, hour 7 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.41σ vs. the median of 209 prior Saturday 7:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-0.6254815617491545, score=-0.6254815617491545

**Detectors fired:** data_quality_gate.

**Score:** -0.625 (threshold 0).

---

## Case outlet_120d#181  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 08 2026 11:31 UTC -> Sat May 09 2026 07:57 UTC (duration 20.43h).

**Magnitude:** baseline 86.51 (source: prewindow_2h), peak -15.7, delta -102.2 (-118.15%).

**Calendar context:** Friday, hour 11 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.75σ vs. the median of 181 prior Friday 11:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=86.51167254974655, sigma=45.390077480916055, direction=-, delta=-102.21508377008553, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.251925738903203, baseline=86.51167254974655, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.251925738903203, baseline=86.51167254974655, source=derived_from_prewindow
- temporal_profile: hour_of_day=11, same_hour_median=16.5, approx_hour_z=-0.11471498148013091, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 4.33e+04 (threshold 0).

---

## Case outlet_120d#182  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 07:11 UTC -> Sat May 09 2026 15:00 UTC (duration 7.82h).

**Magnitude:** baseline 9.633 (source: prewindow_2h), peak 111.3, delta +101.7 (+1055.22%).

**Calendar context:** Saturday, hour 7 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is +2.25σ vs. the median of 184 prior Saturday 7:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=9.633330839107838, sigma=19.914789329240534, direction=+, delta=101.6529007473204, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=5.104392472686881, baseline=9.633330839107838, source=derived_from_prewindow
- sub_pca: approx_residual_z=5.104392472686881, baseline=9.633330839107838, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 4.16e+04 (threshold 0).

---

## Case outlet_120d#183  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 09 2026 14:04 UTC -> Mon May 11 2026 06:11 UTC (duration 1.67d).
**Long-duration framing:** spans 1.7 days; covers 2 weekend day(s).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 105.2, delta +98.65 (+1517.73%).

**Calendar context:** Saturday, hour 14 (afternoon), weekend, May.
**Same-hour-of-weekday baseline:** peak is +1.92σ vs. the median of 167 prior Saturday 14:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=43.12022941254963, direction=+, delta=98.6526424377823, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2878505931387885, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#184  —  TP  —  GT: degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu May 07 2026 17:57 UTC -> Mon May 11 2026 17:57 UTC (duration 4.00d).
**Long-duration framing:** spans 4.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 121 (source: prewindow_2h), peak 122.8, delta +1.798 (+1.49%).

**Calendar context:** Thursday, hour 17 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.52σ vs. the median of 84 prior Thursday 17:00 samples (peer median 124).

**Detector evidence:**
- cusum: mu=120.98811688711008, sigma=0.3666261638499898, direction=+, delta=1.7982288999445188, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=4.90480243161339, baseline=120.98811688711008, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.90480243161339, baseline=120.98811688711008, source=derived_from_prewindow
- temporal_profile: hour_of_day=17, same_hour_median=123.99110647495678, approx_hour_z=-0.4704743291836364, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 21.2 (threshold 0).

---

## Case outlet_120d#185  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 11 2026 06:17 UTC -> Tue May 12 2026 02:09 UTC (duration 19.87h).

**Magnitude:** baseline 87.93 (source: prewindow_2h), peak 6.5, delta -81.43 (-92.61%).

**Calendar context:** Monday, hour 6 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.22σ vs. the median of 194 prior Monday 6:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=87.92939714602238, sigma=44.71776040306526, direction=-, delta=-81.42939714602238, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.8209632238299807, baseline=87.92939714602238, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#186  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue May 12 2026 01:12 UTC -> Tue May 12 2026 18:44 UTC (duration 17.53h).

**Magnitude:** baseline 92.83 (source: prewindow_2h), peak 6.5, delta -86.33 (-93.00%).

**Calendar context:** Tuesday, hour 1 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.24σ vs. the median of 191 prior Tuesday 1:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=92.831868025477, sigma=45.035161153569405, direction=-, delta=-86.331868025477, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.916988100277609, baseline=92.831868025477, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#187  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue May 12 2026 17:55 UTC -> Tue May 12 2026 21:43 UTC (duration 3.80h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 102.1, delta +95.6 (+1470.76%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.94σ vs. the median of 193 prior Tuesday 17:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=44.51540124786521, direction=+, delta=95.59915987380263, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.147552469346487, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#188  —  TP  —  GT: seasonality_loss

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue May 12 2026 20:39 UTC -> Thu May 14 2026 12:50 UTC (duration 1.67d).
**Long-duration framing:** spans 1.7 days; covers 0 weekend day(s).

**Magnitude:** baseline 93.51 (source: prewindow_2h), peak 6.5, delta -87.01 (-93.05%).

**Calendar context:** Tuesday, hour 20 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.26σ vs. the median of 191 prior Tuesday 20:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=93.50586041786033, sigma=37.10276794993405, direction=-, delta=-87.00586041786033, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.344996484770754, baseline=93.50586041786033, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.344996484770754, baseline=93.50586041786033, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 1.36e+05 (threshold 0).

---

## Case outlet_120d#189  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu May 14 2026 11:47 UTC -> Fri May 15 2026 11:23 UTC (duration 23.60h).

**Magnitude:** baseline 91.19 (source: prewindow_2h), peak 6.5, delta -84.69 (-92.87%).

**Calendar context:** Thursday, hour 11 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.24σ vs. the median of 199 prior Thursday 11:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=91.19010576214552, sigma=44.715959337826725, direction=-, delta=-84.69010576214552, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.893957034943972, baseline=91.19010576214552, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.893957034943972, baseline=91.19010576214552, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#190  —  TP  —  GT: degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Mon May 11 2026 16:00 UTC -> Fri May 15 2026 17:58 UTC (duration 4.08d).
**Long-duration framing:** spans 4.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 121 (source: prewindow_2h), peak 122.4, delta +1.423 (+1.18%).

**Calendar context:** Monday, hour 16 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.51σ vs. the median of 84 prior Monday 16:00 samples (peer median 123.8).

**Detector evidence:**
- cusum: mu=121.01130553830126, sigma=0.28198974409044, direction=+, delta=1.423232885880367, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=5.0471086828743195, baseline=121.01130553830126, source=derived_from_prewindow
- sub_pca: approx_residual_z=5.0471086828743195, baseline=121.01130553830126, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 11.1 (threshold 0).

---

## Case outlet_120d#191  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 15 2026 10:24 UTC -> Sat May 16 2026 02:25 UTC (duration 16.02h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 109.2, delta +102.7 (+1579.26%).

**Calendar context:** Friday, hour 10 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.02σ vs. the median of 200 prior Friday 10:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=17.598913247007182, direction=+, delta=102.65176798704978, source=derived_from_prewindow
- sub_pca: approx_residual_z=5.832846980168303, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#192  —  TP  —  GT: dropout

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 16 2026 01:32 UTC -> Sat May 16 2026 11:44 UTC (duration 10.20h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 104.6, delta +98.09 (+1509.03%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is +0.96σ vs. the median of 202 prior Saturday 1:00 samples (peer median 56.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=23.86960712502054, direction=+, delta=98.08725155036292, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=104.58725155036292, score=3166.0
- sub_pca: approx_residual_z=4.109294762859593, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.17e+03 (threshold 0).

---

## Case outlet_120d#193  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 16 2026 10:50 UTC -> Sat May 16 2026 19:10 UTC (duration 8.33h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 104, delta +97.46 (+1499.40%).

**Calendar context:** Saturday, hour 10 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is +2.50σ vs. the median of 192 prior Saturday 10:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=39.74981752129331, direction=+, delta=97.46121577169096, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.4518657405026483, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#194  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 16 2026 18:08 UTC -> Sun May 17 2026 13:19 UTC (duration 19.18h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 108.4, delta +101.9 (+1568.29%).

**Calendar context:** Saturday, hour 18 (evening), weekend, May.
**Same-hour-of-weekday baseline:** peak is +2.06σ vs. the median of 198 prior Saturday 18:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=36.44733854157455, direction=+, delta=101.93903693313284, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.796885616678254, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#195  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun May 17 2026 12:17 UTC -> Mon May 18 2026 20:37 UTC (duration 1.35d).
**Long-duration framing:** spans 1.3 days; covers 1 weekend day(s).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 104.2, delta +97.68 (+1502.77%).

**Calendar context:** Sunday, hour 12 (afternoon), weekend, May.
**Same-hour-of-weekday baseline:** peak is +2.10σ vs. the median of 200 prior Sunday 12:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=41.19144121587526, direction=+, delta=97.6797712534391, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.3713608548319773, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#196  —  TP  —  GT: degradation_trajectory, duplicate_stale

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Fri May 15 2026 16:40 UTC -> Tue May 19 2026 17:59 UTC (duration 4.05d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 121.2 (source: prewindow_2h), peak 122.9, delta +1.716 (+1.42%).

**Calendar context:** Friday, hour 16 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.40σ vs. the median of 88 prior Friday 16:00 samples (peer median 123.9).

**Detector evidence:**
- cusum: mu=121.21159923514924, sigma=0.3408218893510002, direction=+, delta=1.7159550767832883, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=5.034756071714889, baseline=121.21159923514924, source=derived_from_prewindow
- sub_pca: approx_residual_z=5.034756071714889, baseline=121.21159923514924, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#197  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 18 2026 19:40 UTC -> Tue May 19 2026 18:24 UTC (duration 22.73h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 105.6, delta +99.11 (+1524.76%).

**Calendar context:** Monday, hour 19 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.03σ vs. the median of 218 prior Monday 19:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=43.37652746753466, direction=+, delta=99.10957118607033, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2848664236723257, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#198  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue May 19 2026 17:28 UTC -> Wed May 20 2026 01:00 UTC (duration 7.53h).

**Magnitude:** baseline 91.27 (source: prewindow_2h), peak 6.5, delta -84.77 (-92.88%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.23σ vs. the median of 202 prior Tuesday 17:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=91.26874347894052, sigma=44.39856293368846, direction=-, delta=-84.76874347894052, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.90926773025395, baseline=91.26874347894052, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#199  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed May 20 2026 00:39 UTC -> Wed May 20 2026 08:35 UTC (duration 7.93h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 105.2, delta +98.68 (+1518.08%).

**Calendar context:** Wednesday, hour 0 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.31σ vs. the median of 206 prior Wednesday 0:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=43.59643886373869, direction=+, delta=98.67551940356968, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.263384853794629, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#200  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed May 20 2026 07:36 UTC -> Thu May 21 2026 00:47 UTC (duration 17.18h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 104.8, delta +98.27 (+1511.78%).

**Calendar context:** Wednesday, hour 7 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.09σ vs. the median of 220 prior Wednesday 7:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=38.38229599206274, direction=+, delta=98.26576791444135, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.5601847251337495, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#201  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed May 20 2026 23:45 UTC -> Thu May 21 2026 15:18 UTC (duration 15.55h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 107.6, delta +101.1 (+1554.93%).

**Calendar context:** Wednesday, hour 23 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.35σ vs. the median of 205 prior Wednesday 23:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=35.52676688224279, direction=+, delta=101.07048890269428, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.844910971991993, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#202  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu May 21 2026 14:23 UTC -> Thu May 21 2026 18:46 UTC (duration 4.38h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 104.3, delta +97.78 (+1504.37%).

**Calendar context:** Thursday, hour 14 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is +0.35σ vs. the median of 228 prior Thursday 14:00 samples (peer median 84.01).

**Detector evidence:**
- cusum: mu=6.5, sigma=44.68282610487971, direction=+, delta=97.7843073585527, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.1884091916888377, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#203  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu May 21 2026 17:52 UTC -> Fri May 22 2026 00:47 UTC (duration 6.92h).

**Magnitude:** baseline 48.25 (source: prewindow_2h), peak 105.4, delta +57.1 (+118.34%).

**Calendar context:** Thursday, hour 17 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.12σ vs. the median of 220 prior Thursday 17:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=48.24976910294078, sigma=44.96162784067924, direction=+, delta=57.101050297246495, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.269995172318562, baseline=48.24976910294078, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#204  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 00:06 UTC -> Fri May 22 2026 02:55 UTC (duration 2.82h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 100.1, delta +93.62 (+1440.38%).

**Calendar context:** Friday, hour 0 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.97σ vs. the median of 216 prior Friday 0:00 samples (peer median 16.5).

**Detector evidence:**
- sub_pca: approx_residual_z=2.2299185980636556, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#205  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.88σ vs. the median of 200 prior Friday 3:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=101.87453453222152, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#206  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.88σ vs. the median of 200 prior Friday 3:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=101.87453453222152, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#207  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.88σ vs. the median of 200 prior Friday 3:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=101.87453453222152, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#208  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.88σ vs. the median of 200 prior Friday 3:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=batch_arrival, value=101.87453453222152, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_120d#209  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.88σ vs. the median of 200 prior Friday 3:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=101.87453453222152, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#210  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.88σ vs. the median of 200 prior Friday 3:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=101.87453453222152, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#211  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 03:59 UTC -> Fri May 22 2026 04:00 UTC (duration 1.0m).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 101.9, delta +95.37 (+1467.30%).

**Calendar context:** Friday, hour 3 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.88σ vs. the median of 200 prior Friday 3:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=101.87453453222152, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_120d#212  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 00:51 UTC -> Fri May 22 2026 17:05 UTC (duration 16.23h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 104.3, delta +97.84 (+1505.27%).

**Calendar context:** Friday, hour 0 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.08σ vs. the median of 225 prior Friday 0:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=39.221487104224934, direction=+, delta=97.84234845368712, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=104.34234845368712, score=3847.0
- sub_pca: approx_residual_z=2.494610879839575, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.85e+03 (threshold 0).

---

## Case outlet_120d#213  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 22 2026 16:38 UTC -> Sat May 23 2026 09:24 UTC (duration 16.77h).

**Magnitude:** baseline 91.4 (source: prewindow_2h), peak 6.5, delta -84.9 (-92.89%).

**Calendar context:** Friday, hour 16 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.23σ vs. the median of 208 prior Friday 16:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=91.40182911932096, sigma=44.6108878930291, direction=-, delta=-84.90182911932096, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.9031638492133156, baseline=91.40182911932096, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#214  —  TP  —  GT: degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue May 19 2026 15:55 UTC -> Sat May 23 2026 18:00 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 121.9 (source: prewindow_2h), peak 123.2, delta +1.282 (+1.05%).

**Calendar context:** Tuesday, hour 15 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.20σ vs. the median of 95 prior Tuesday 15:00 samples (peer median 123.7).

**Detector evidence:**
- cusum: mu=121.92714817000432, sigma=0.32043536628109537, direction=+, delta=1.282260377658929, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=4.001619398447088, baseline=121.92714817000432, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.001619398447088, baseline=121.92714817000432, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 17.9 (threshold 0).

---

## Case outlet_120d#215  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 23 2026 09:28 UTC -> Sun May 24 2026 18:05 UTC (duration 1.36d).
**Long-duration framing:** spans 1.4 days; covers 2 weekend day(s).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 105.8, delta +99.25 (+1526.98%).

**Calendar context:** Saturday, hour 9 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is +1.06σ vs. the median of 220 prior Saturday 9:00 samples (peer median 56.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=39.04968449674268, direction=+, delta=99.25351512752074, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.541723868109612, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#216  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun May 24 2026 17:03 UTC -> Mon May 25 2026 00:28 UTC (duration 7.43h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 102.7, delta +96.19 (+1479.87%).

**Calendar context:** Sunday, hour 17 (afternoon), weekend, May.
**Same-hour-of-weekday baseline:** peak is +1.95σ vs. the median of 215 prior Sunday 17:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=32.57031357570335, direction=+, delta=96.19144829428495, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=102.69144829428495, score=3117.065078640921
- sub_pca: approx_residual_z=2.9533473195063555, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#217  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun May 24 2026 22:24 UTC -> Mon May 25 2026 03:23 UTC (duration 5.00h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 99.28, delta +92.78 (+1427.41%).

**Calendar context:** Sunday, hour 22 (evening), weekend, May.
**Same-hour-of-weekday baseline:** peak is +1.93σ vs. the median of 210 prior Sunday 22:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=24.370359663910087, direction=+, delta=92.78192343002247, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=99.28192343002247, score=4743.0
- sub_pca: approx_residual_z=3.8071626643829406, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 4.74e+03 (threshold 0).

---

## Case outlet_120d#218  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 02:49 UTC -> Mon May 25 2026 05:25 UTC (duration 2.61h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 99.28, delta +92.78 (+1427.41%).

**Calendar context:** Monday, hour 2 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.76σ vs. the median of 246 prior Monday 2:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=99.28192343002247, score=3953.0
- sub_pca: approx_residual_z=1.784717793071324, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** data_quality_gate, sub_pca.

**Score:** 3.95e+03 (threshold 0).

---

## Case outlet_120d#219  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 05:36 UTC -> Mon May 25 2026 06:30 UTC (duration 54.5m).

**Magnitude:** baseline 84.18 (source: prewindow_2h), peak 94.44, delta +10.25 (+12.18%).

**Calendar context:** Monday, hour 5 (night), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.76σ vs. the median of 229 prior Monday 5:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=94.43828798304884, score=3272.0

**Detectors fired:** data_quality_gate.

**Score:** 3.27e+03 (threshold 0).

---

## Case outlet_120d#220  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 07:06 UTC -> Mon May 25 2026 08:05 UTC (duration 59.6m).

**Magnitude:** baseline 94.44 (source: prewindow_2h), peak 99.11, delta +4.671 (+4.95%).

**Calendar context:** Monday, hour 7 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is +1.96σ vs. the median of 203 prior Monday 7:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=99.10962353320754, score=3577.0

**Detectors fired:** data_quality_gate.

**Score:** 3.58e+03 (threshold 0).

---

## Case outlet_120d#221  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 08:35 UTC -> Mon May 25 2026 10:42 UTC (duration 2.12h).

**Magnitude:** baseline 95.26 (source: prewindow_2h), peak 6.5, delta -88.76 (-93.18%).

**Calendar context:** Monday, hour 8 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.23σ vs. the median of 231 prior Monday 8:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=6.5, score=7615.0

**Detectors fired:** data_quality_gate.

**Score:** 7.62e+03 (threshold 0).

---

## Case outlet_120d#222  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 08:38 UTC -> Mon May 25 2026 11:44 UTC (duration 3.10h).

**Magnitude:** baseline 95.55 (source: prewindow_2h), peak 6.5, delta -89.05 (-93.20%).

**Calendar context:** Monday, hour 8 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.23σ vs. the median of 232 prior Monday 8:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=95.5471786199648, sigma=2.474530797056366, direction=-, delta=-89.0471786199648, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=6.5, score=3684.0
- sub_pca: approx_residual_z=35.985480045709224, baseline=95.5471786199648, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.68e+03 (threshold 0).

---

## Case outlet_120d#223  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 09:56 UTC -> Mon May 25 2026 14:48 UTC (duration 4.88h).

**Magnitude:** baseline 93.67 (source: prewindow_2h), peak 6.5, delta -87.17 (-93.06%).

**Calendar context:** Monday, hour 9 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.23σ vs. the median of 216 prior Monday 9:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=93.67224805992196, sigma=2.9918729885375046, direction=-, delta=-87.17224805992196, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=6.5, score=3154.0
- sub_pca: approx_residual_z=29.136346493951176, baseline=93.67224805992196, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.15e+03 (threshold 0).

---

## Case outlet_120d#224  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 13:29 UTC -> Mon May 25 2026 16:53 UTC (duration 3.40h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 104.2, delta +97.71 (+1503.19%).

**Calendar context:** Monday, hour 13 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.01σ vs. the median of 226 prior Monday 13:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=45.45080793471448, direction=+, delta=97.70740079692098, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=104.20740079692098, score=3117.065078640921
- sub_pca: approx_residual_z=2.149739580807185, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#225  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 16:11 UTC -> Mon May 25 2026 19:35 UTC (duration 3.40h).

**Magnitude:** baseline 92.59 (source: prewindow_2h), peak 6.5, delta -86.09 (-92.98%).

**Calendar context:** Monday, hour 16 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.24σ vs. the median of 225 prior Monday 16:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=92.59055423413578, sigma=39.87580726025352, direction=-, delta=-86.09055423413578, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=6.5, score=3273.0
- sub_pca: approx_residual_z=2.158967056698238, baseline=92.59055423413578, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 3.27e+03 (threshold 0).

---

## Case outlet_120d#226  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 17:57 UTC -> Mon May 25 2026 20:41 UTC (duration 2.74h).

**Magnitude:** baseline 94.38 (source: prewindow_2h), peak 6.5, delta -87.88 (-93.11%).

**Calendar context:** Monday, hour 17 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.23σ vs. the median of 235 prior Monday 17:00 samples (peer median 16.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=None, value=6.5, score=3117.065078640921
- sub_pca: approx_residual_z=12.657485270753787, baseline=94.38336729696783, source=derived_from_prewindow

**Detectors fired:** data_quality_gate, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#227  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon May 25 2026 18:37 UTC -> Tue May 26 2026 11:37 UTC (duration 17.00h).

**Magnitude:** baseline 45.89 (source: prewindow_2h), peak 102.8, delta +56.95 (+124.11%).

**Calendar context:** Monday, hour 18 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.14σ vs. the median of 221 prior Monday 18:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=45.88661090522455, sigma=47.34157506007124, direction=+, delta=56.94818221580589, source=derived_from_prewindow
- data_quality_gate: anomaly_type=dropout, value=102.83479312103044, score=4570.0
- sub_pca: approx_residual_z=1.2029211563735454, baseline=45.88661090522455, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 4.57e+03 (threshold 0).

---

## Case outlet_120d#228  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue May 26 2026 10:52 UTC -> Tue May 26 2026 18:09 UTC (duration 7.28h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 106.8, delta +100.3 (+1543.29%).

**Calendar context:** Tuesday, hour 10 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.11σ vs. the median of 233 prior Tuesday 10:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=0.0, direction=+, delta=100.31372278575664, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#229  —  TP  —  GT: degradation_trajectory

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 23 2026 15:56 UTC -> Wed May 27 2026 18:01 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 121.8 (source: prewindow_2h), peak 119.7, delta -2.118 (-1.74%).

**Calendar context:** Saturday, hour 15 (afternoon), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.44σ vs. the median of 95 prior Saturday 15:00 samples (peer median 123.2).

**Detector evidence:**
- cusum: mu=121.81328690578124, sigma=0.6008593817515909, direction=-, delta=-2.1176192837832843, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.5243175826099638, baseline=121.81328690578124, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.5243175826099638, baseline=121.81328690578124, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 14 (threshold 0).

---

## Case outlet_120d#230  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue May 26 2026 17:10 UTC -> Thu May 28 2026 23:14 UTC (duration 2.25d).
**Long-duration framing:** spans 2.3 days; covers 0 weekend day(s).

**Magnitude:** baseline 88.18 (source: prewindow_2h), peak 6.5, delta -81.68 (-92.63%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -0.23σ vs. the median of 213 prior Tuesday 17:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=88.17639328027585, sigma=44.01075958851963, direction=-, delta=-81.67639328027585, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.8558278485514126, baseline=88.17639328027585, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#231  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Thu May 28 2026 22:30 UTC -> Fri May 29 2026 10:17 UTC (duration 11.78h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 106.7, delta +100.2 (+1542.24%).

**Calendar context:** Thursday, hour 22 (evening), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.20σ vs. the median of 222 prior Thursday 22:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=25.010161573647895, direction=+, delta=100.24568518936005, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.008198223516657, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#232  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 00:30 UTC -> Sat May 30 2026 00:31 UTC (duration 1.0m).

**Magnitude:** baseline 121 (source: prewindow_2h), peak 120.7, delta -0.2459 (-0.20%).

**Calendar context:** Saturday, hour 0 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.65σ vs. the median of 98 prior Saturday 0:00 samples (peer median 122.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.70948853483723, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#233  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 00:40 UTC -> Sat May 30 2026 00:41 UTC (duration 1.0m).

**Magnitude:** baseline 120.9 (source: prewindow_2h), peak 120.8, delta -0.06738 (-0.06%).

**Calendar context:** Saturday, hour 0 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.57σ vs. the median of 99 prior Saturday 0:00 samples (peer median 122.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.82133466019044, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#234  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 00:51 UTC -> Sat May 30 2026 00:52 UTC (duration 1.0m).

**Magnitude:** baseline 120.9 (source: prewindow_2h), peak 120.8, delta -0.03882 (-0.03%).

**Calendar context:** Saturday, hour 0 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.57σ vs. the median of 100 prior Saturday 0:00 samples (peer median 122.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.81489501064264, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#235  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 01:01 UTC -> Sat May 30 2026 01:02 UTC (duration 1.0m).

**Magnitude:** baseline 120.8 (source: prewindow_2h), peak 121.9, delta +1.034 (+0.86%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.40σ vs. the median of 96 prior Saturday 1:00 samples (peer median 122.8).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.8706286350743, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#236  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 01:11 UTC -> Sat May 30 2026 01:12 UTC (duration 1.0m).

**Magnitude:** baseline 120.8 (source: prewindow_2h), peak 121.1, delta +0.2401 (+0.20%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.49σ vs. the median of 97 prior Saturday 1:00 samples (peer median 122.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.07667754340856, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#237  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 01:21 UTC -> Sat May 30 2026 01:22 UTC (duration 1.0m).

**Magnitude:** baseline 120.9 (source: prewindow_2h), peak 120.5, delta -0.3687 (-0.31%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.73σ vs. the median of 98 prior Saturday 1:00 samples (peer median 122.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.48506026552926, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#238  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 01:32 UTC -> Sat May 30 2026 01:33 UTC (duration 1.0m).

**Magnitude:** baseline 120.8 (source: prewindow_2h), peak 120.7, delta -0.1372 (-0.11%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.62σ vs. the median of 99 prior Saturday 1:00 samples (peer median 122.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.69941372901268, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#239  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 01:42 UTC -> Sat May 30 2026 01:43 UTC (duration 1.0m).

**Magnitude:** baseline 120.8 (source: prewindow_2h), peak 120.9, delta +0.08084 (+0.07%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.51σ vs. the median of 100 prior Saturday 1:00 samples (peer median 122.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.9021767337265, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#240  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 01:52 UTC -> Sat May 30 2026 01:53 UTC (duration 1.0m).

**Magnitude:** baseline 120.8 (source: prewindow_2h), peak 121.5, delta +0.6448 (+0.53%).

**Calendar context:** Saturday, hour 1 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.23σ vs. the median of 101 prior Saturday 1:00 samples (peer median 122).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.48139893861853, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#241  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 02:02 UTC -> Sat May 30 2026 02:03 UTC (duration 1.0m).

**Magnitude:** baseline 120.9 (source: prewindow_2h), peak 121.2, delta +0.3612 (+0.30%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.76σ vs. the median of 96 prior Saturday 2:00 samples (peer median 123).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.21489293389271, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#242  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 02:13 UTC -> Sat May 30 2026 02:14 UTC (duration 1.0m).

**Magnitude:** baseline 120.9 (source: prewindow_2h), peak 120.6, delta -0.2661 (-0.22%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -1.00σ vs. the median of 97 prior Saturday 2:00 samples (peer median 123).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.63611687978286, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#243  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 02:23 UTC -> Sat May 30 2026 02:24 UTC (duration 1.0m).

**Magnitude:** baseline 120.8 (source: prewindow_2h), peak 121.2, delta +0.3911 (+0.32%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.59σ vs. the median of 98 prior Saturday 2:00 samples (peer median 122.6).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.212459685699, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#244  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 02:33 UTC -> Sat May 30 2026 02:34 UTC (duration 1.0m).

**Magnitude:** baseline 120.9 (source: prewindow_2h), peak 121.2, delta +0.2926 (+0.24%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.43σ vs. the median of 99 prior Saturday 2:00 samples (peer median 122.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.1947633637787, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#245  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 02:43 UTC -> Sat May 30 2026 02:44 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_2h), peak 121.2, delta +0.1354 (+0.11%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.40σ vs. the median of 100 prior Saturday 2:00 samples (peer median 122.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.21210543837417, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#246  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 02:54 UTC -> Sat May 30 2026 02:55 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_2h), peak 120.9, delta -0.2864 (-0.24%).

**Calendar context:** Saturday, hour 2 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.51σ vs. the median of 101 prior Saturday 2:00 samples (peer median 122.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.90841133553177, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#247  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 03:04 UTC -> Sat May 30 2026 03:05 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_2h), peak 121.6, delta +0.5119 (+0.42%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.62σ vs. the median of 96 prior Saturday 3:00 samples (peer median 123).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.58855668800553, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#248  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 03:14 UTC -> Sat May 30 2026 03:15 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_2h), peak 121.3, delta +0.09767 (+0.08%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.60σ vs. the median of 97 prior Saturday 3:00 samples (peer median 122.7).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.29243502491252, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#249  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 03:24 UTC -> Sat May 30 2026 03:25 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_2h), peak 121.1, delta -0.1181 (-0.10%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.58σ vs. the median of 98 prior Saturday 3:00 samples (peer median 122.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.093968504007, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#250  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 03:35 UTC -> Sat May 30 2026 03:36 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_2h), peak 121.7, delta +0.4544 (+0.37%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.23σ vs. the median of 99 prior Saturday 3:00 samples (peer median 122.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.66654016246984, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#251  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 03:45 UTC -> Sat May 30 2026 03:46 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_2h), peak 120.6, delta -0.6532 (-0.54%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.70σ vs. the median of 100 prior Saturday 3:00 samples (peer median 122.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.55930015708095, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#252  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 03:55 UTC -> Sat May 30 2026 03:56 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_2h), peak 121, delta -0.2479 (-0.20%).

**Calendar context:** Saturday, hour 3 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.53σ vs. the median of 101 prior Saturday 3:00 samples (peer median 122.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.96425183912444, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#253  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 04:05 UTC -> Sat May 30 2026 04:06 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_2h), peak 121.2, delta -0.01197 (-0.01%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.63σ vs. the median of 96 prior Saturday 4:00 samples (peer median 122.7).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.1827948659146, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#254  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 04:16 UTC -> Sat May 30 2026 04:17 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_2h), peak 121.6, delta +0.4291 (+0.35%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.20σ vs. the median of 97 prior Saturday 4:00 samples (peer median 122.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.62390795467208, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#255  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 04:26 UTC -> Sat May 30 2026 04:27 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_2h), peak 120.5, delta -0.7395 (-0.61%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.69σ vs. the median of 98 prior Saturday 4:00 samples (peer median 122.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.45530827306726, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#256  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 04:36 UTC -> Sat May 30 2026 04:37 UTC (duration 1.0m).

**Magnitude:** baseline 121.2 (source: prewindow_2h), peak 121, delta -0.2297 (-0.19%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.48σ vs. the median of 99 prior Saturday 4:00 samples (peer median 122.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.95307043260456, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#257  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 04:46 UTC -> Sat May 30 2026 04:47 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_2h), peak 120.8, delta -0.3065 (-0.25%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.53σ vs. the median of 100 prior Saturday 4:00 samples (peer median 122).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.78743773809626, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#258  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 04:57 UTC -> Sat May 30 2026 04:58 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_2h), peak 121.1, delta -0.02178 (-0.02%).

**Calendar context:** Saturday, hour 4 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.38σ vs. the median of 101 prior Saturday 4:00 samples (peer median 122).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.07218979856953, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#259  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 05:07 UTC -> Sat May 30 2026 05:08 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_2h), peak 121.2, delta +0.1384 (+0.11%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.69σ vs. the median of 96 prior Saturday 5:00 samples (peer median 122.8).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.21063131250092, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#260  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 05:17 UTC -> Sat May 30 2026 05:18 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_2h), peak 121, delta -0.06437 (-0.05%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.53σ vs. the median of 97 prior Saturday 5:00 samples (peer median 122.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.00781522812788, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#261  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 05:27 UTC -> Sat May 30 2026 05:28 UTC (duration 1.0m).

**Magnitude:** baseline 121 (source: prewindow_2h), peak 121.1, delta +0.08266 (+0.07%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.49σ vs. the median of 98 prior Saturday 5:00 samples (peer median 122.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.09047801296632, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#262  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 05:38 UTC -> Sat May 30 2026 05:39 UTC (duration 1.0m).

**Magnitude:** baseline 121 (source: prewindow_2h), peak 121.1, delta +0.1165 (+0.10%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.47σ vs. the median of 99 prior Saturday 5:00 samples (peer median 122.2).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.1242958714015, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#263  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 05:48 UTC -> Sat May 30 2026 05:49 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_2h), peak 121, delta -0.1121 (-0.09%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.49σ vs. the median of 100 prior Saturday 5:00 samples (peer median 122.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.96010838402304, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#264  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 05:58 UTC -> Sat May 30 2026 05:59 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_2h), peak 121.2, delta +0.09043 (+0.07%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.34σ vs. the median of 101 prior Saturday 5:00 samples (peer median 121.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.16261775098472, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#265  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sat May 30 2026 06:08 UTC -> Sat May 30 2026 06:09 UTC (duration 1.0m).

**Magnitude:** baseline 121.1 (source: prewindow_2h), peak 121.8, delta +0.7291 (+0.60%).

**Calendar context:** Saturday, hour 6 (morning), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.38σ vs. the median of 96 prior Saturday 6:00 samples (peer median 122.7).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.80129335505562, score=15.0

**Detectors fired:** data_quality_gate.

**Score:** 15 (threshold 0).

---

## Case outlet_120d#266  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Fri May 29 2026 09:14 UTC -> Sat May 30 2026 05:42 UTC (duration 20.47h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 103.9, delta +97.38 (+1498.12%).

**Calendar context:** Friday, hour 9 (morning), weekday, May.
**Same-hour-of-weekday baseline:** peak is +2.03σ vs. the median of 208 prior Friday 9:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=42.74847174682391, direction=+, delta=97.3777178151764, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2779227849802908, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#267  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 30 2026 05:02 UTC -> Sat May 30 2026 18:30 UTC (duration 13.47h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 105.6, delta +99.13 (+1525.06%).

**Calendar context:** Saturday, hour 5 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is +2.02σ vs. the median of 244 prior Saturday 5:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=37.81873172860984, direction=+, delta=99.1288181678818, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.621156597192045, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#268  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat May 30 2026 17:42 UTC -> Sun May 31 2026 01:54 UTC (duration 8.20h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 102.2, delta +95.7 (+1472.25%).

**Calendar context:** Saturday, hour 17 (afternoon), weekend, May.
**Same-hour-of-weekday baseline:** peak is +2.12σ vs. the median of 217 prior Saturday 17:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=45.00647277447693, direction=+, delta=95.69604845308038, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.1262730126087415, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#269  —  TP  —  GT: stuck_at, clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Wed May 27 2026 16:02 UTC -> Sun May 31 2026 18:02 UTC (duration 4.08d).
**Long-duration framing:** spans 4.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 121.1 (source: prewindow_2h), peak 119.5, delta -1.646 (-1.36%).

**Calendar context:** Wednesday, hour 16 (afternoon), weekday, May.
**Same-hour-of-weekday baseline:** peak is -1.88σ vs. the median of 96 prior Wednesday 16:00 samples (peer median 123.7).

**Detector evidence:**
- cusum: mu=121.11165298828489, sigma=0.26134238394475073, direction=-, delta=-1.6459971461285932, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=6.2982403438876045, baseline=121.11165298828489, source=derived_from_prewindow
- sub_pca: approx_residual_z=6.2982403438876045, baseline=121.11165298828489, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 14.5 (threshold 0).

---

## Case outlet_120d#270  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun May 31 2026 01:02 UTC -> Sun May 31 2026 23:57 UTC (duration 22.92h).

**Magnitude:** baseline 6.5 (source: prewindow_2h), peak 106.3, delta +99.8 (+1535.41%).

**Calendar context:** Sunday, hour 1 (night), weekend, May.
**Same-hour-of-weekday baseline:** peak is +1.84σ vs. the median of 213 prior Sunday 1:00 samples (peer median 16.5).

**Detector evidence:**
- cusum: mu=6.5, sigma=28.466739470575842, direction=+, delta=99.80163837185412, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.5059033885848563, baseline=6.5, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 3.12e+03 (threshold 0).

---

## Case outlet_120d#271  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Sun May 31 2026 16:01 UTC -> Sun May 31 2026 23:59 UTC (duration 7.97h).

**Magnitude:** baseline 121.3 (source: prewindow_2h), peak 120.1, delta -1.198 (-0.99%).

**Calendar context:** Sunday, hour 16 (afternoon), weekend, May.
**Same-hour-of-weekday baseline:** peak is -0.83σ vs. the median of 102 prior Sunday 16:00 samples (peer median 122.3).

**Detector evidence:**
- cusum: mu=121.31814395652, sigma=0.30765802295481126, direction=-, delta=-1.1981172223050862, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.894314898074559, baseline=121.31814395652, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.894314898074559, baseline=121.31814395652, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 5.82 (threshold 0).

---
