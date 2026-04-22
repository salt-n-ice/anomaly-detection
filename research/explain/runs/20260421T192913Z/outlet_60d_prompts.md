# outlet_60d — explain cases (run 20260421T192913Z)

## Case outlet_60d#000  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 09 2026 11:00 UTC -> Mon Feb 09 2026 11:01 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 9999, delta +9998 (+666500.00%).

**Calendar context:** Monday, hour 11 (morning), weekday, February.

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=9999.0, score=9999.0

**Detectors fired:** data_quality_gate.

**Score:** 1e+04 (threshold 0).

---

## Case outlet_60d#001  —  TP  —  GT: noise_burst

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

## Case outlet_60d#002  —  TP  —  GT: noise_floor_up

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

## Case outlet_60d#003  —  TP  —  GT: noise_floor_up

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

## Case outlet_60d#004  —  TP  —  GT: noise_floor_up

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

## Case outlet_60d#005  —  TP  —  GT: calibration_drift, trend

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

## Case outlet_60d#006  —  TP  —  GT: level_shift

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

## Case outlet_60d#007  —  TP  —  GT: level_shift

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

## Case outlet_60d#008  —  TP  —  GT: frequency_change

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

## Case outlet_60d#009  —  TP  —  GT: frequency_change

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

## Case outlet_60d#010  —  TP  —  GT: level_shift, frequency_change

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

## Case outlet_60d#011  —  TP  —  GT: frequency_change

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

## Case outlet_60d#012  —  TP  —  GT: frequency_change

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

## Case outlet_60d#013  —  TP  —  GT: frequency_change

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

## Case outlet_60d#014  —  TP  —  GT: frequency_change

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

## Case outlet_60d#015  —  TP  —  GT: frequency_change

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

## Case outlet_60d#016  —  TP  —  GT: frequency_change

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

## Case outlet_60d#017  —  TP  —  GT: frequency_change

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

## Case outlet_60d#018  —  FP  —  GT: (none)

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

## Case outlet_60d#019  —  FP  —  GT: (none)

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

## Case outlet_60d#020  —  TP  —  GT: trend

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

## Case outlet_60d#021  —  TP  —  GT: seasonality_loss, time_of_day

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

## Case outlet_60d#022  —  TP  —  GT: time_of_day

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

## Case outlet_60d#023  —  TP  —  GT: time_of_day

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

## Case outlet_60d#024  —  TP  —  GT: time_of_day

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

## Case outlet_60d#025  —  TP  —  GT: month_shift

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

## Case outlet_60d#026  —  TP  —  GT: time_of_day

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

## Case outlet_60d#027  —  TP  —  GT: time_of_day, weekend_anomaly

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

## Case outlet_60d#028  —  TP  —  GT: month_shift

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

## Case outlet_60d#029  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#030  —  TP  —  GT: weekend_anomaly, dropout

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

## Case outlet_60d#031  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#032  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#033  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#034  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#035  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#036  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#037  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#038  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 11:03 UTC -> Sat Mar 07 2026 11:03 UTC (duration 0s).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak nan, delta +nan (+nan%).

**Calendar context:** Saturday, hour 11 (morning), weekend, March.

**Detector evidence:**
- multivariate_pca: approx_residual_z=0.0, baseline=56.5, source=derived_from_prewindow

**Detectors fired:** multivariate_pca.

**Score:** 3.25e+04 (threshold 0).

---

## Case outlet_60d#039  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#040  —  TP  —  GT: weekend_anomaly, reporting_rate_change

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

## Case outlet_60d#041  —  TP  —  GT: weekend_anomaly, reporting_rate_change

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

## Case outlet_60d#042  —  TP  —  GT: weekend_anomaly, reporting_rate_change

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

## Case outlet_60d#043  —  TP  —  GT: month_shift, duplicate_stale

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

## Case outlet_60d#044  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#045  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#046  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#047  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#048  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#049  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#050  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#051  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#052  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#053  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#054  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#055  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#056  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#057  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#058  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#059  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#060  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#061  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#062  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#063  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#064  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#065  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#066  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#067  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#068  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#069  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#070  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#071  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#072  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#073  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#074  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#075  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#076  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#077  —  TP  —  GT: weekend_anomaly, reporting_rate_change

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

## Case outlet_60d#078  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#079  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#080  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#081  —  TP  —  GT: weekend_anomaly, batch_arrival

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

## Case outlet_60d#082  —  TP  —  GT: weekend_anomaly, batch_arrival

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

## Case outlet_60d#083  —  TP  —  GT: weekend_anomaly, batch_arrival

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

## Case outlet_60d#084  —  TP  —  GT: weekend_anomaly, batch_arrival

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

## Case outlet_60d#085  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_60d#086  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#087  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#088  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#089  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#090  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#091  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#092  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 14 2026 11:59 UTC -> Sat Mar 14 2026 11:59 UTC (duration 0s).

**Magnitude:** baseline 56.5 (source: prewindow_2h), peak nan, delta +nan (+nan%).

**Calendar context:** Saturday, hour 11 (morning), weekend, March.

**Detector evidence:**
- cusum: mu=56.5, sigma=0.0, direction=0, delta=nan, source=derived_from_prewindow

**Detectors fired:** cusum.

**Score:** 1.29e+03 (threshold 0).

---

## Case outlet_60d#093  —  TP  —  GT: weekend_anomaly

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

## Case outlet_60d#094  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

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

## Case outlet_60d#095  —  FP  —  GT: (none)

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

## Case outlet_60d#096  —  TP  —  GT: month_shift, stuck_at

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

## Case outlet_60d#097  —  FP  —  GT: (none)

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

## Case outlet_60d#098  —  FP  —  GT: (none)

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

## Case outlet_60d#099  —  TP  —  GT: month_shift, stuck_at, degradation_trajectory

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

## Case outlet_60d#100  —  FP  —  GT: (none)

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

## Case outlet_60d#101  —  FP  —  GT: (none)

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

## Case outlet_60d#102  —  FP  —  GT: (none)

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

## Case outlet_60d#103  —  FP  —  GT: (none)

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

## Case outlet_60d#104  —  TP  —  GT: month_shift, degradation_trajectory

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

## Case outlet_60d#105  —  FP  —  GT: (none)

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

## Case outlet_60d#106  —  FP  —  GT: (none)

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

## Case outlet_60d#107  —  FP  —  GT: (none)

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

## Case outlet_60d#108  —  FP  —  GT: (none)

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

## Case outlet_60d#109  —  FP  —  GT: (none)

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

## Case outlet_60d#110  —  FP  —  GT: (none)

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

## Case outlet_60d#111  —  TP  —  GT: month_shift, degradation_trajectory

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

## Case outlet_60d#112  —  FP  —  GT: (none)

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

## Case outlet_60d#113  —  FP  —  GT: (none)

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

## Case outlet_60d#114  —  FP  —  GT: (none)

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

## Case outlet_60d#115  —  FP  —  GT: (none)

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 21:29 UTC -> Wed Apr 01 2026 23:58 UTC (duration 1.10d).
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

## Case outlet_60d#116  —  TP  —  GT: month_shift, degradation_trajectory

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
