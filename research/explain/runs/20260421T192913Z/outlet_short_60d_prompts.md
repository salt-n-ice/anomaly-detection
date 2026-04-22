# outlet_short_60d — explain cases (run 20260421T192913Z)

## Case outlet_short_60d#000  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Feb 09 2026 11:00 UTC -> Mon Feb 09 2026 11:01 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 9999, delta +9998 (+666500.00%).

**Calendar context:** Monday, hour 11 (morning), weekday, February.

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=9999.0, score=9999.0

**Detectors fired:** data_quality_gate.

**Score:** 1e+04 (threshold 0).

---

## Case outlet_short_60d#001  —  TP  —  GT: noise_burst

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

## Case outlet_short_60d#002  —  TP  —  GT: noise_floor_up

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

## Case outlet_short_60d#003  —  TP  —  GT: noise_floor_up

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

## Case outlet_short_60d#004  —  TP  —  GT: noise_floor_up

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

## Case outlet_short_60d#005  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Feb 18 2026 03:09 UTC -> Wed Feb 18 2026 03:10 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak -8.662, delta -10.16 (-677.48%).

**Calendar context:** Wednesday, hour 3 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.36σ vs. the median of 29 prior Wednesday 3:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-8.662137607358744, score=-8.662137607358744

**Detectors fired:** data_quality_gate.

**Score:** -8.66 (threshold 0).

---

## Case outlet_short_60d#006  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Feb 18 2026 03:42 UTC -> Wed Feb 18 2026 03:43 UTC (duration 1.0m).

**Magnitude:** baseline 3.473 (source: prewindow_2h), peak -9.719, delta -13.19 (-379.80%).

**Calendar context:** Wednesday, hour 3 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.33σ vs. the median of 44 prior Wednesday 3:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-9.718776172134024, score=-9.718776172134024

**Detectors fired:** data_quality_gate.

**Score:** -9.72 (threshold 0).

---

## Case outlet_short_60d#007  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Feb 18 2026 05:58 UTC -> Wed Feb 18 2026 05:59 UTC (duration 1.0m).

**Magnitude:** baseline 91.4 (source: prewindow_2h), peak -26.46, delta -117.9 (-128.95%).

**Calendar context:** Wednesday, hour 5 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -3.23σ vs. the median of 71 prior Wednesday 5:00 samples (peer median 87.51).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-26.46213337374641, score=-26.46213337374641

**Detectors fired:** data_quality_gate.

**Score:** -26.5 (threshold 0).

---

## Case outlet_short_60d#008  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Feb 18 2026 06:29 UTC -> Wed Feb 18 2026 06:30 UTC (duration 1.0m).

**Magnitude:** baseline 78.69 (source: prewindow_2h), peak -11.44, delta -90.14 (-114.54%).

**Calendar context:** Wednesday, hour 6 (morning), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.36σ vs. the median of 41 prior Wednesday 6:00 samples (peer median 4.511).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-11.443681370428704, score=-11.443681370428704

**Detectors fired:** data_quality_gate.

**Score:** -11.4 (threshold 0).

---

## Case outlet_short_60d#009  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Feb 18 2026 07:03 UTC -> Wed Feb 18 2026 07:04 UTC (duration 1.0m).

**Magnitude:** baseline 64.73 (source: prewindow_2h), peak -14.26, delta -78.98 (-122.02%).

**Calendar context:** Wednesday, hour 7 (morning), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.42σ vs. the median of 30 prior Wednesday 7:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-14.255238898839082, score=-14.255238898839082

**Detectors fired:** data_quality_gate.

**Score:** -14.3 (threshold 0).

---

## Case outlet_short_60d#010  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Feb 18 2026 07:53 UTC -> Wed Feb 18 2026 07:54 UTC (duration 1.0m).

**Magnitude:** baseline 19.59 (source: prewindow_2h), peak -14.73, delta -34.32 (-175.22%).

**Calendar context:** Wednesday, hour 7 (morning), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.68σ vs. the median of 57 prior Wednesday 7:00 samples (peer median 15.45).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-14.733637563806166, score=-14.733637563806166

**Detectors fired:** data_quality_gate.

**Score:** -14.7 (threshold 0).

---

## Case outlet_short_60d#011  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Feb 18 2026 08:26 UTC -> Wed Feb 18 2026 08:27 UTC (duration 1.0m).

**Magnitude:** baseline 18.67 (source: prewindow_2h), peak -14.73, delta -33.41 (-178.90%).

**Calendar context:** Wednesday, hour 8 (morning), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.43σ vs. the median of 36 prior Wednesday 8:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-14.73363756380651, score=-14.73363756380651

**Detectors fired:** data_quality_gate.

**Score:** -14.7 (threshold 0).

---

## Case outlet_short_60d#012  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Feb 18 2026 08:59 UTC -> Wed Feb 18 2026 09:00 UTC (duration 1.0m).

**Magnitude:** baseline 15.45 (source: prewindow_2h), peak -14.73, delta -30.19 (-195.34%).

**Calendar context:** Wednesday, hour 8 (morning), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.48σ vs. the median of 50 prior Wednesday 8:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-14.73363756380614, score=-14.73363756380614

**Detectors fired:** data_quality_gate.

**Score:** -14.7 (threshold 0).

---

## Case outlet_short_60d#013  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Feb 19 2026 03:01 UTC -> Thu Feb 19 2026 03:11 UTC (duration 10.0m).

**Magnitude:** baseline 120.1 (source: prewindow_2h), peak 118.5, delta -1.575 (-1.31%).

**Calendar context:** Thursday, hour 3 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -3.22σ vs. the median of 12 prior Thursday 3:00 samples (peer median 120.1).

**Detector evidence:**
- multivariate_pca: approx_residual_z=3.675517580207656, baseline=120.05087909609166, source=derived_from_prewindow

**Detectors fired:** multivariate_pca.

**Score:** 0.0564 (threshold 0).

---

## Case outlet_short_60d#014  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Feb 18 2026 00:58 UTC -> Wed Feb 18 2026 11:38 UTC (duration 10.67h).

**Magnitude:** baseline 83.67 (source: prewindow_2h), peak -26.46, delta -110.1 (-131.62%).

**Calendar context:** Wednesday, hour 0 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.64σ vs. the median of 41 prior Wednesday 0:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=83.67495728036573, sigma=45.30042726959148, direction=-, delta=-110.13709065411214, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.4312594227569932, baseline=83.67495728036573, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.4312594227569932, baseline=83.67495728036573, source=derived_from_prewindow
- temporal_profile: hour_of_day=0, same_hour_median=1.5, approx_hour_z=-0.7080899086457635, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 4.43e+04 (threshold 0).

---

## Case outlet_short_60d#015  —  TP  —  GT: seasonality_loss

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Feb 21 2026 21:55 UTC -> Sun Feb 22 2026 08:46 UTC (duration 10.85h).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 99.89, delta +98.39 (+6559.27%).

**Calendar context:** Saturday, hour 21 (evening), weekend, February.
**Same-hour-of-weekday baseline:** peak is +2.30σ vs. the median of 44 prior Saturday 21:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=1.5, sigma=32.50801321969431, direction=+, delta=98.38897980723416, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.0266069827862387, baseline=1.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.0266069827862387, baseline=1.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 8.87e+04 (threshold 0).

---

## Case outlet_short_60d#016  —  TP  —  GT: duplicate_stale

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Fri Feb 27 2026 08:16 UTC -> Fri Feb 27 2026 08:35 UTC (duration 19.0m).

**Magnitude:** baseline 120 (source: prewindow_2h), peak 119.5, delta -0.4968 (-0.41%).

**Calendar context:** Friday, hour 8 (morning), weekday, February.
**Same-hour-of-weekday baseline:** peak is -1.41σ vs. the median of 20 prior Friday 8:00 samples (peer median 120).

**Detector evidence:**
- cusum: mu=119.9795500266697, sigma=0.3272289577970412, direction=-, delta=-0.4968225680607219, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=1.5182720117602446, baseline=119.9795500266697, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca.

**Score:** 1.8 (threshold 0).

---

## Case outlet_short_60d#017  —  TP  —  GT: duplicate_stale

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Fri Feb 27 2026 08:56 UTC -> Fri Feb 27 2026 09:07 UTC (duration 11.0m).

**Magnitude:** baseline 120 (source: prewindow_2h), peak 119.4, delta -0.5856 (-0.49%).

**Calendar context:** Friday, hour 8 (morning), weekday, February.
**Same-hour-of-weekday baseline:** peak is -1.87σ vs. the median of 28 prior Friday 8:00 samples (peer median 120).

**Detector evidence:**
- cusum: mu=119.99431593192206, sigma=0.2510711045650232, direction=-, delta=-0.5855709295613849, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.332291207209517, baseline=119.99431593192206, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca.

**Score:** 1.75 (threshold 0).

---

## Case outlet_short_60d#018  —  TP  —  GT: dropout

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Wed Feb 25 2026 07:57 UTC -> Wed Feb 25 2026 08:31 UTC (duration 33.9m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Wednesday, hour 7 (morning), weekday, February.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 71 prior Wednesday 7:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=1.5, score=2034.0

**Detectors fired:** data_quality_gate.

**Score:** 2.03e+03 (threshold 0).

---

## Case outlet_short_60d#019  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 00:30 UTC -> Thu Mar 05 2026 00:31 UTC (duration 1.0m).

**Magnitude:** baseline 120.1 (source: prewindow_2h), peak 119.8, delta -0.3062 (-0.26%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.73σ vs. the median of 26 prior Thursday 0:00 samples (peer median 120).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.7784679010536, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#020  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 00:40 UTC -> Thu Mar 05 2026 00:41 UTC (duration 1.0m).

**Magnitude:** baseline 120.1 (source: prewindow_2h), peak 120.6, delta +0.5244 (+0.44%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.67σ vs. the median of 27 prior Thursday 0:00 samples (peer median 120).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.6090604833956, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#021  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 00:50 UTC -> Thu Mar 05 2026 00:51 UTC (duration 1.0m).

**Magnitude:** baseline 120.1 (source: prewindow_2h), peak 120.4, delta +0.2859 (+0.24%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.96σ vs. the median of 28 prior Thursday 0:00 samples (peer median 120).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.39987105905212, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#022  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 01:01 UTC -> Thu Mar 05 2026 01:02 UTC (duration 1.0m).

**Magnitude:** baseline 120.1 (source: prewindow_2h), peak 120, delta -0.1773 (-0.15%).

**Calendar context:** Thursday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.05σ vs. the median of 24 prior Thursday 1:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.9572365040669, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#023  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 01:11 UTC -> Thu Mar 05 2026 01:12 UTC (duration 1.0m).

**Magnitude:** baseline 120.1 (source: prewindow_2h), peak 119.6, delta -0.5529 (-0.46%).

**Calendar context:** Thursday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.91σ vs. the median of 25 prior Thursday 1:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.56111652475946, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#024  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 01:21 UTC -> Thu Mar 05 2026 01:22 UTC (duration 1.0m).

**Magnitude:** baseline 120.1 (source: prewindow_2h), peak 119.9, delta -0.2011 (-0.17%).

**Calendar context:** Thursday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.06σ vs. the median of 26 prior Thursday 1:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.91285950594752, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#025  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 01:31 UTC -> Thu Mar 05 2026 01:32 UTC (duration 1.0m).

**Magnitude:** baseline 120.1 (source: prewindow_2h), peak 119.2, delta -0.8836 (-0.74%).

**Calendar context:** Thursday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.67σ vs. the median of 27 prior Thursday 1:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.23033968138355, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#026  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 01:41 UTC -> Thu Mar 05 2026 01:42 UTC (duration 1.0m).

**Magnitude:** baseline 120 (source: prewindow_2h), peak 120.1, delta +0.1507 (+0.13%).

**Calendar context:** Thursday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.44σ vs. the median of 28 prior Thursday 1:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.10789375036772, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#027  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 01:52 UTC -> Thu Mar 05 2026 01:53 UTC (duration 1.0m).

**Magnitude:** baseline 120 (source: prewindow_2h), peak 119.5, delta -0.4101 (-0.34%).

**Calendar context:** Thursday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.89σ vs. the median of 29 prior Thursday 1:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.54718181458917, score=11.999999000000004

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#028  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 02:02 UTC -> Thu Mar 05 2026 02:03 UTC (duration 1.0m).

**Magnitude:** baseline 120 (source: prewindow_2h), peak 119.6, delta -0.3141 (-0.26%).

**Calendar context:** Thursday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.04σ vs. the median of 24 prior Thursday 2:00 samples (peer median 120.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.64313381509707, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#029  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 02:12 UTC -> Thu Mar 05 2026 02:13 UTC (duration 1.0m).

**Magnitude:** baseline 119.9 (source: prewindow_2h), peak 119.5, delta -0.4334 (-0.36%).

**Calendar context:** Thursday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.41σ vs. the median of 25 prior Thursday 2:00 samples (peer median 120.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.47948361055673, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#030  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 02:22 UTC -> Thu Mar 05 2026 02:23 UTC (duration 1.0m).

**Magnitude:** baseline 119.8 (source: prewindow_2h), peak 120.6, delta +0.7975 (+0.67%).

**Calendar context:** Thursday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.22σ vs. the median of 26 prior Thursday 2:00 samples (peer median 120.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.5759403981236, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#031  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 02:32 UTC -> Thu Mar 05 2026 02:33 UTC (duration 1.0m).

**Magnitude:** baseline 119.9 (source: prewindow_2h), peak 119.9, delta -0.009184 (-0.01%).

**Calendar context:** Thursday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.39σ vs. the median of 27 prior Thursday 2:00 samples (peer median 120.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.90367544934794, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#032  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 02:43 UTC -> Thu Mar 05 2026 02:44 UTC (duration 1.0m).

**Magnitude:** baseline 119.9 (source: prewindow_2h), peak 119.9, delta -0.04662 (-0.04%).

**Calendar context:** Thursday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.45σ vs. the median of 28 prior Thursday 2:00 samples (peer median 120.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.85705908904455, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#033  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 02:53 UTC -> Thu Mar 05 2026 02:54 UTC (duration 1.0m).

**Magnitude:** baseline 119.9 (source: prewindow_2h), peak 119.2, delta -0.6215 (-0.52%).

**Calendar context:** Thursday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.88σ vs. the median of 29 prior Thursday 2:00 samples (peer median 120).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.23559166231448, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#034  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 03:03 UTC -> Thu Mar 05 2026 03:04 UTC (duration 1.0m).

**Magnitude:** baseline 119.6 (source: prewindow_2h), peak 119.7, delta +0.06415 (+0.05%).

**Calendar context:** Thursday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.39σ vs. the median of 24 prior Thursday 3:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.70727979332648, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#035  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 03:13 UTC -> Thu Mar 05 2026 03:14 UTC (duration 1.0m).

**Magnitude:** baseline 119.7 (source: prewindow_2h), peak 119.7, delta +0.02085 (+0.02%).

**Calendar context:** Thursday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.27σ vs. the median of 25 prior Thursday 3:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.728128038748, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#036  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 03:23 UTC -> Thu Mar 05 2026 03:24 UTC (duration 1.0m).

**Magnitude:** baseline 119.7 (source: prewindow_2h), peak 120.9, delta +1.241 (+1.04%).

**Calendar context:** Thursday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.98σ vs. the median of 26 prior Thursday 3:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.94861852574384, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#037  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 03:34 UTC -> Thu Mar 05 2026 03:35 UTC (duration 1.0m).

**Magnitude:** baseline 119.7 (source: prewindow_2h), peak 119.9, delta +0.1592 (+0.13%).

**Calendar context:** Thursday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.02σ vs. the median of 27 prior Thursday 3:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.88730695942316, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#038  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 03:44 UTC -> Thu Mar 05 2026 03:45 UTC (duration 1.0m).

**Magnitude:** baseline 119.7 (source: prewindow_2h), peak 119.2, delta -0.5539 (-0.46%).

**Calendar context:** Thursday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.27σ vs. the median of 28 prior Thursday 3:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.174252541628, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#039  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 03:54 UTC -> Thu Mar 05 2026 03:55 UTC (duration 1.0m).

**Magnitude:** baseline 119.7 (source: prewindow_2h), peak 119, delta -0.6891 (-0.58%).

**Calendar context:** Thursday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.48σ vs. the median of 29 prior Thursday 3:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.03907057383444, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#040  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 04:04 UTC -> Thu Mar 05 2026 04:05 UTC (duration 1.0m).

**Magnitude:** baseline 119.7 (source: prewindow_2h), peak 120.5, delta +0.8179 (+0.68%).

**Calendar context:** Thursday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.00σ vs. the median of 24 prior Thursday 4:00 samples (peer median 120.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.54597895358566, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#041  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 04:14 UTC -> Thu Mar 05 2026 04:15 UTC (duration 1.0m).

**Magnitude:** baseline 119.9 (source: prewindow_2h), peak 119.8, delta -0.02014 (-0.02%).

**Calendar context:** Thursday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.57σ vs. the median of 25 prior Thursday 4:00 samples (peer median 120.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.83691795803364, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#042  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 04:25 UTC -> Thu Mar 05 2026 04:26 UTC (duration 1.0m).

**Magnitude:** baseline 119.8 (source: prewindow_2h), peak 120.1, delta +0.2881 (+0.24%).

**Calendar context:** Thursday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.07σ vs. the median of 26 prior Thursday 4:00 samples (peer median 120.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.12501397628768, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#043  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 04:35 UTC -> Thu Mar 05 2026 04:36 UTC (duration 1.0m).

**Magnitude:** baseline 119.8 (source: prewindow_2h), peak 120.1, delta +0.3005 (+0.25%).

**Calendar context:** Thursday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.09σ vs. the median of 27 prior Thursday 4:00 samples (peer median 120.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.13746205106278, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#044  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 04:45 UTC -> Thu Mar 05 2026 04:46 UTC (duration 1.0m).

**Magnitude:** baseline 119.8 (source: prewindow_2h), peak 119.8, delta -0.07728 (-0.06%).

**Calendar context:** Thursday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.82σ vs. the median of 28 prior Thursday 4:00 samples (peer median 120.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.75963625072066, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#045  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 04:55 UTC -> Thu Mar 05 2026 04:56 UTC (duration 1.0m).

**Magnitude:** baseline 119.8 (source: prewindow_2h), peak 119.7, delta -0.1452 (-0.12%).

**Calendar context:** Thursday, hour 4 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.95σ vs. the median of 29 prior Thursday 4:00 samples (peer median 120.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.69176513678782, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#046  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 05:05 UTC -> Thu Mar 05 2026 05:06 UTC (duration 1.0m).

**Magnitude:** baseline 119.8 (source: prewindow_2h), peak 119.7, delta -0.1529 (-0.13%).

**Calendar context:** Thursday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.85σ vs. the median of 24 prior Thursday 5:00 samples (peer median 120).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.68400287575793, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#047  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 05:16 UTC -> Thu Mar 05 2026 05:17 UTC (duration 1.0m).

**Magnitude:** baseline 119.8 (source: prewindow_2h), peak 119.5, delta -0.3233 (-0.27%).

**Calendar context:** Thursday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.20σ vs. the median of 25 prior Thursday 5:00 samples (peer median 120).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.51362205756416, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#048  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 05:26 UTC -> Thu Mar 05 2026 05:27 UTC (duration 1.0m).

**Magnitude:** baseline 119.8 (source: prewindow_2h), peak 121, delta +1.279 (+1.07%).

**Calendar context:** Thursday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.54σ vs. the median of 26 prior Thursday 5:00 samples (peer median 120).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=121.0382275140286, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#049  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 05:36 UTC -> Thu Mar 05 2026 05:37 UTC (duration 1.0m).

**Magnitude:** baseline 119.8 (source: prewindow_2h), peak 119.6, delta -0.1244 (-0.10%).

**Calendar context:** Thursday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -0.82σ vs. the median of 27 prior Thursday 5:00 samples (peer median 120).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.6352036790333, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#050  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 05:46 UTC -> Thu Mar 05 2026 05:47 UTC (duration 1.0m).

**Magnitude:** baseline 119.8 (source: prewindow_2h), peak 120.3, delta +0.5157 (+0.43%).

**Calendar context:** Thursday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.65σ vs. the median of 28 prior Thursday 5:00 samples (peer median 120).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.27535989009728, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#051  —  TP  —  GT: clock_drift

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 05:56 UTC -> Thu Mar 05 2026 05:57 UTC (duration 1.0m).

**Magnitude:** baseline 119.8 (source: prewindow_2h), peak 120, delta +0.1823 (+0.15%).

**Calendar context:** Thursday, hour 5 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.02σ vs. the median of 29 prior Thursday 5:00 samples (peer median 120).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=120.019249288118, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#052  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 05 2026 06:07 UTC -> Thu Mar 05 2026 06:08 UTC (duration 1.0m).

**Magnitude:** baseline 119.8 (source: prewindow_2h), peak 119.5, delta -0.3429 (-0.29%).

**Calendar context:** Thursday, hour 6 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.32σ vs. the median of 24 prior Thursday 6:00 samples (peer median 119.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=clock_drift, value=119.49401294608964, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#053  —  TP  —  GT: seasonal_mismatch

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Mon Mar 02 2026 02:25 UTC -> Mon Mar 02 2026 13:11 UTC (duration 10.77h).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 114.6, delta +113.1 (+7540.84%).

**Calendar context:** Monday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.63σ vs. the median of 63 prior Monday 2:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=1.5, sigma=34.84045570717137, direction=+, delta=113.1125505625155, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.246586425654387, baseline=1.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.246586425654387, baseline=1.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=2, same_hour_median=1.5, approx_hour_z=3.154195974784113, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 8.3e+04 (threshold 0).

---

## Case outlet_short_60d#054  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 00:59 UTC -> Sun Mar 08 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 61 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_short_60d#055  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 00:59 UTC -> Sun Mar 08 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 61 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_short_60d#056  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 00:59 UTC -> Sun Mar 08 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 61 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_short_60d#057  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 00:59 UTC -> Sun Mar 08 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 61 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_short_60d#058  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 00:59 UTC -> Sun Mar 08 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 61 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_short_60d#059  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 00:59 UTC -> Sun Mar 08 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 61 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_short_60d#060  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 00:59 UTC -> Sun Mar 08 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 61 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_short_60d#061  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 00:59 UTC -> Sun Mar 08 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 61 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_short_60d#062  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 00:59 UTC -> Sun Mar 08 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 61 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_short_60d#063  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 00:59 UTC -> Sun Mar 08 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 61 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_short_60d#064  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 00:59 UTC -> Sun Mar 08 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 61 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=1.5, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_short_60d#065  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 08 2026 00:59 UTC -> Sun Mar 08 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 61 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=batch_arrival, value=1.5, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_short_60d#066  —  FP  —  GT: (none)

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Tue Mar 10 2026 11:51 UTC -> Tue Mar 10 2026 12:13 UTC (duration 22.0m).

**Magnitude:** baseline 120 (source: prewindow_2h), peak 118.8, delta -1.178 (-0.98%).

**Calendar context:** Tuesday, hour 11 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is -3.31σ vs. the median of 35 prior Tuesday 11:00 samples (peer median 120).

**Detector evidence:**
- cusum: mu=120.01946822008418, sigma=0.32408138403722175, direction=-, delta=-1.1780540881153314, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.635056335047089, baseline=120.01946822008418, source=derived_from_prewindow
- temporal_profile: hour_of_day=11, same_hour_median=120.02409758201934, approx_hour_z=-0.1891529760383514, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, temporal_profile.

**Score:** 4.84 (threshold 0).

---

## Case outlet_short_60d#067  —  TP  —  GT: batch_arrival

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 07 2026 23:55 UTC -> Sun Mar 08 2026 00:59 UTC (duration 1.07h).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 1.5, delta +0 (+0.00%).

**Calendar context:** Saturday, hour 23 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 64 prior Saturday 23:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=1.5, score=3848.0

**Detectors fired:** data_quality_gate.

**Score:** 3.85e+03 (threshold 0).

---

## Case outlet_short_60d#068  —  TP  —  GT: stuck_at

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 12 2026 00:57 UTC -> Thu Mar 12 2026 05:16 UTC (duration 4.32h).

**Magnitude:** baseline 119.6 (source: prewindow_2h), peak 121.8, delta +2.24 (+1.87%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +4.49σ vs. the median of 34 prior Thursday 0:00 samples (peer median 120).

**Detector evidence:**
- cusum: mu=119.57490140273288, sigma=0.4194078132144525, direction=+, delta=2.2402646256325625, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=5.34149473387866, baseline=119.57490140273288, source=derived_from_prewindow
- sub_pca: approx_residual_z=5.34149473387866, baseline=119.57490140273288, source=derived_from_prewindow
- temporal_profile: hour_of_day=0, same_hour_median=119.96994601661625, approx_hour_z=4.243226781145033, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 18.3 (threshold 0).

---

## Case outlet_short_60d#069  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 15 2026 00:42 UTC -> Sun Mar 15 2026 02:16 UTC (duration 1.56h).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 90.57, delta +89.07 (+5938.33%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +2.52σ vs. the median of 76 prior Sunday 0:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=90.57496291091282, score=3223.0

**Detectors fired:** data_quality_gate.

**Score:** 3.22e+03 (threshold 0).

---

## Case outlet_short_60d#070  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 15 2026 02:28 UTC -> Sun Mar 15 2026 05:48 UTC (duration 3.34h).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 91.49, delta +89.99 (+5999.20%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +3.44σ vs. the median of 74 prior Sunday 2:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=91.48800422686138, score=4538.0

**Detectors fired:** data_quality_gate.

**Score:** 4.54e+03 (threshold 0).

---

## Case outlet_short_60d#071  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 15 2026 06:14 UTC -> Sun Mar 15 2026 06:56 UTC (duration 42.4m).

**Magnitude:** baseline 90.82 (source: prewindow_2h), peak 1.5, delta -89.32 (-98.35%).

**Calendar context:** Sunday, hour 6 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 82 prior Sunday 6:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=1.5, score=2542.0

**Detectors fired:** data_quality_gate.

**Score:** 2.54e+03 (threshold 0).

---

## Case outlet_short_60d#072  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 15 2026 07:55 UTC -> Sun Mar 15 2026 08:46 UTC (duration 51.2m).

**Magnitude:** baseline 89.82 (source: prewindow_2h), peak 1.5, delta -88.32 (-98.33%).

**Calendar context:** Sunday, hour 7 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 79 prior Sunday 7:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=1.5, score=3071.0

**Detectors fired:** data_quality_gate.

**Score:** 3.07e+03 (threshold 0).

---

## Case outlet_short_60d#073  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 15 2026 08:46 UTC -> Sun Mar 15 2026 10:12 UTC (duration 1.43h).

**Magnitude:** baseline 45.5 (source: prewindow_2h), peak 93.61, delta +48.11 (+105.75%).

**Calendar context:** Sunday, hour 8 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.18σ vs. the median of 87 prior Sunday 8:00 samples (peer median 85.66).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=93.61295391693076, score=5161.0

**Detectors fired:** data_quality_gate.

**Score:** 5.16e+03 (threshold 0).

---

## Case outlet_short_60d#074  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 15 2026 12:37 UTC -> Sun Mar 15 2026 13:46 UTC (duration 1.15h).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 88.66, delta +87.16 (+5810.74%).

**Calendar context:** Sunday, hour 12 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.98σ vs. the median of 92 prior Sunday 12:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=88.66114103611429, score=4145.0

**Detectors fired:** data_quality_gate.

**Score:** 4.14e+03 (threshold 0).

---

## Case outlet_short_60d#075  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 15 2026 14:09 UTC -> Sun Mar 15 2026 17:43 UTC (duration 3.55h).

**Magnitude:** baseline 45.08 (source: prewindow_2h), peak 91.98, delta +46.9 (+104.04%).

**Calendar context:** Sunday, hour 14 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is +2.24σ vs. the median of 87 prior Sunday 14:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=91.98448914423648, score=4424.0

**Detectors fired:** data_quality_gate.

**Score:** 4.42e+03 (threshold 0).

---

## Case outlet_short_60d#076  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 15 2026 18:01 UTC -> Sun Mar 15 2026 19:24 UTC (duration 1.38h).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 89.8, delta +88.3 (+5886.98%).

**Calendar context:** Sunday, hour 18 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.07σ vs. the median of 87 prior Sunday 18:00 samples (peer median 86.57).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=89.8047614720409, score=4962.0

**Detectors fired:** data_quality_gate.

**Score:** 4.96e+03 (threshold 0).

---

## Case outlet_short_60d#077  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 15 2026 19:55 UTC -> Sun Mar 15 2026 20:55 UTC (duration 1.01h).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 87.88, delta +86.38 (+5758.61%).

**Calendar context:** Sunday, hour 19 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.95σ vs. the median of 81 prior Sunday 19:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=87.87908361631635, score=3651.0

**Detectors fired:** data_quality_gate.

**Score:** 3.65e+03 (threshold 0).

---

## Case outlet_short_60d#078  —  TP  —  GT: noise_burst

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Thu Mar 19 2026 09:55 UTC -> Thu Mar 19 2026 14:34 UTC (duration 4.65h).

**Magnitude:** baseline 120.1 (source: prewindow_2h), peak 115.1, delta -5.058 (-4.21%).

**Calendar context:** Thursday, hour 9 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is -11.36σ vs. the median of 41 prior Thursday 9:00 samples (peer median 119.9).

**Detector evidence:**
- cusum: mu=120.1391279879135, sigma=0.3453107654156881, direction=-, delta=-5.0579033955738595, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=14.647395627776364, baseline=120.1391279879135, source=derived_from_prewindow
- sub_pca: approx_residual_z=14.647395627776364, baseline=120.1391279879135, source=derived_from_prewindow
- temporal_profile: hour_of_day=9, same_hour_median=119.9568436207563, approx_hour_z=-11.797998612998127, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 79.6 (threshold 0).

---

## Case outlet_short_60d#079  —  TP  —  GT: reporting_rate_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 15 2026 21:31 UTC -> Sun Mar 15 2026 23:54 UTC (duration 2.38h).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 93.99, delta +92.49 (+6165.99%).

**Calendar context:** Sunday, hour 21 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is +2.57σ vs. the median of 81 prior Sunday 21:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=dropout, value=93.98986257634984, score=3000.0

**Detectors fired:** data_quality_gate.

**Score:** 3e+03 (threshold 0).

---

## Case outlet_short_60d#080  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Wed Mar 25 2026 14:00 UTC -> Wed Mar 25 2026 14:01 UTC (duration 1.0m).

**Magnitude:** baseline 119.7 (source: prewindow_2h), peak 200, delta +80.29 (+67.07%).

**Calendar context:** Wednesday, hour 14 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +200.52σ vs. the median of 42 prior Wednesday 14:00 samples (peer median 120.1).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=200.0, score=200.0

**Detectors fired:** data_quality_gate.

**Score:** 200 (threshold 0).

---

## Case outlet_short_60d#081  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_voltage (capability: voltage)

**When:** Wed Mar 25 2026 11:55 UTC -> Wed Mar 25 2026 16:10 UTC (duration 4.25h).

**Magnitude:** baseline 120.2 (source: prewindow_2h), peak 200, delta +79.83 (+66.44%).

**Calendar context:** Wednesday, hour 11 (morning), weekday, March.
**Same-hour-of-weekday baseline:** peak is +170.84σ vs. the median of 47 prior Wednesday 11:00 samples (peer median 120.1).

**Detector evidence:**
- cusum: mu=120.16675315809724, sigma=0.40841354272756414, direction=+, delta=79.83324684190276, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=195.4715955517573, baseline=120.16675315809724, source=derived_from_prewindow
- sub_pca: approx_residual_z=195.4715955517573, baseline=120.16675315809724, source=derived_from_prewindow
- temporal_profile: hour_of_day=11, same_hour_median=120.02409758201934, approx_hour_z=12.992145010963373, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 6.34e+03 (threshold 0).

---

## Case outlet_short_60d#082  —  TP  —  GT: spike

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sun Mar 22 2026 09:00 UTC -> Sun Mar 22 2026 09:02 UTC (duration 2.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 589.7, delta +588.2 (+39213.66%).

**Calendar context:** Sunday, hour 9 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is +11.43σ vs. the median of 78 prior Sunday 9:00 samples (peer median 86.16).

**Detector evidence:**
- multivariate_pca: approx_residual_z=13.422204482997456, baseline=1.5, source=derived_from_prewindow
- temporal_profile: hour_of_day=9, same_hour_median=1.5, approx_hour_z=13.444956123144431, source=derived_from_same_hour_history

**Detectors fired:** multivariate_pca, temporal_profile.

**Score:** 3.33e+05 (threshold 0).

---

## Case outlet_short_60d#083  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 28 2026 10:21 UTC -> Sat Mar 28 2026 10:22 UTC (duration 1.0m).

**Magnitude:** baseline 88.39 (source: prewindow_2h), peak -11.63, delta -100 (-113.16%).

**Calendar context:** Saturday, hour 10 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.33σ vs. the median of 104 prior Saturday 10:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-11.629365749032404, score=-11.629365749032404

**Detectors fired:** data_quality_gate.

**Score:** -11.6 (threshold 0).

---

## Case outlet_short_60d#084  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 28 2026 10:54 UTC -> Sat Mar 28 2026 10:55 UTC (duration 1.0m).

**Magnitude:** baseline 60.99 (source: prewindow_2h), peak -11.63, delta -72.62 (-119.07%).

**Calendar context:** Saturday, hour 10 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.34σ vs. the median of 120 prior Saturday 10:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-11.629365749032456, score=-11.629365749032456

**Detectors fired:** data_quality_gate.

**Score:** -11.6 (threshold 0).

---

## Case outlet_short_60d#085  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 28 2026 11:28 UTC -> Sat Mar 28 2026 11:29 UTC (duration 1.0m).

**Magnitude:** baseline 18.38 (source: prewindow_2h), peak -11.63, delta -30.01 (-163.26%).

**Calendar context:** Saturday, hour 11 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.40σ vs. the median of 106 prior Saturday 11:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-11.629365749032283, score=-11.629365749032283

**Detectors fired:** data_quality_gate.

**Score:** -11.6 (threshold 0).

---

## Case outlet_short_60d#086  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 28 2026 12:09 UTC -> Sat Mar 28 2026 12:10 UTC (duration 1.0m).

**Magnitude:** baseline 11.28 (source: prewindow_2h), peak -9.71, delta -20.99 (-186.04%).

**Calendar context:** Saturday, hour 12 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.31σ vs. the median of 95 prior Saturday 12:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-9.70958040225079, score=-9.70958040225079

**Detectors fired:** data_quality_gate.

**Score:** -9.71 (threshold 0).

---

## Case outlet_short_60d#087  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 28 2026 12:42 UTC -> Sat Mar 28 2026 12:43 UTC (duration 1.0m).

**Magnitude:** baseline 8.324 (source: prewindow_2h), peak -6.82, delta -15.14 (-181.94%).

**Calendar context:** Saturday, hour 12 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.23σ vs. the median of 119 prior Saturday 12:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.82048861307481, score=-6.82048861307481

**Detectors fired:** data_quality_gate.

**Score:** -6.82 (threshold 0).

---

## Case outlet_short_60d#088  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 28 2026 13:16 UTC -> Sat Mar 28 2026 13:17 UTC (duration 1.0m).

**Magnitude:** baseline 8.324 (source: prewindow_2h), peak -6.82, delta -15.14 (-181.94%).

**Calendar context:** Saturday, hour 13 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.23σ vs. the median of 104 prior Saturday 13:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.820488613074787, score=-6.820488613074787

**Detectors fired:** data_quality_gate.

**Score:** -6.82 (threshold 0).

---

## Case outlet_short_60d#089  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 28 2026 13:49 UTC -> Sat Mar 28 2026 13:50 UTC (duration 1.0m).

**Magnitude:** baseline 8.324 (source: prewindow_2h), peak -6.82, delta -15.14 (-181.94%).

**Calendar context:** Saturday, hour 13 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.25σ vs. the median of 128 prior Saturday 13:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.820488613074764, score=-6.820488613074764

**Detectors fired:** data_quality_gate.

**Score:** -6.82 (threshold 0).

---

## Case outlet_short_60d#090  —  TP  —  GT: dip

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 22:00 UTC -> Tue Mar 31 2026 22:01 UTC (duration 1.0m).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak -78.5, delta -80 (-5333.33%).

**Calendar context:** Tuesday, hour 22 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.92σ vs. the median of 104 prior Tuesday 22:00 samples (peer median 1.5).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-78.5, score=-78.5

**Detectors fired:** data_quality_gate.

**Score:** -78.5 (threshold 0).

---

## Case outlet_short_60d#091  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Sat Mar 28 2026 08:14 UTC -> Sat Mar 28 2026 17:17 UTC (duration 9.05h).

**Magnitude:** baseline 77.78 (source: prewindow_2h), peak -21.86, delta -99.64 (-128.10%).

**Calendar context:** Saturday, hour 8 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.53σ vs. the median of 101 prior Saturday 8:00 samples (peer median 1.5).

**Detector evidence:**
- multivariate_pca: approx_residual_z=2.23317619414256, baseline=77.77811825568418, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.23317619414256, baseline=77.77811825568418, source=derived_from_prewindow
- temporal_profile: hour_of_day=8, same_hour_median=1.5, approx_hour_z=-0.5373934637238377, source=derived_from_same_hour_history

**Detectors fired:** multivariate_pca, sub_pca, temporal_profile.

**Score:** 3.39e+04 (threshold 0).

---

## Case outlet_short_60d#092  —  TP  —  GT: dip

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 19:55 UTC -> Tue Mar 31 2026 22:29 UTC (duration 2.57h).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 91.74, delta +90.24 (+6016.17%).

**Calendar context:** Tuesday, hour 19 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.15σ vs. the median of 120 prior Tuesday 19:00 samples (peer median 1.5).

**Detector evidence:**
- cusum: mu=1.5, sigma=44.75807999499068, direction=+, delta=90.2425474261841, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.0162291911602117, baseline=1.5, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.0162291911602117, baseline=1.5, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 3.21e+04 (threshold 0).

---

## Case outlet_short_60d#093  —  TP  —  GT: dip

# Anomaly on sensor outlet_fridge_power (capability: power)

**When:** Tue Mar 31 2026 21:29 UTC -> Wed Apr 01 2026 01:12 UTC (duration 3.72h).

**Magnitude:** baseline 1.5 (source: prewindow_2h), peak 95.39, delta +93.89 (+6259.35%).

**Calendar context:** Tuesday, hour 21 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.26σ vs. the median of 106 prior Tuesday 21:00 samples (peer median 1.5).

**Detector evidence:**
- sub_pca: approx_residual_z=2.156203452485817, baseline=1.5, source=derived_from_prewindow

**Detectors fired:** sub_pca.

**Score:** 3.2e+04 (threshold 0).

---
