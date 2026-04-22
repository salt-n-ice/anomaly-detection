# outlet_tv_60d — explain cases (run 20260421T192913Z)

## Case outlet_tv_60d#000  —  TP  —  GT: dip

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Feb 07 2026 21:00 UTC -> Sat Feb 07 2026 21:01 UTC (duration 1.0m).

**Magnitude:** baseline 0.3 (source: prewindow_2h), peak -99.7, delta -100 (-33333.33%).

**Calendar context:** Saturday, hour 21 (evening), weekend, February.

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-99.7, score=-99.7

**Detectors fired:** data_quality_gate.

**Score:** -99.7 (threshold 0).

---

## Case outlet_tv_60d#001  —  TP  —  GT: out_of_range

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Feb 09 2026 20:00 UTC -> Mon Feb 09 2026 20:01 UTC (duration 1.0m).

**Magnitude:** baseline 0.3 (source: prewindow_2h), peak 9999, delta +9999 (+3332900.00%).

**Calendar context:** Monday, hour 20 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is +172452312913532485632.00σ vs. the median of 12 prior Monday 20:00 samples (peer median 0.3).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=9999.0, score=9999.0

**Detectors fired:** data_quality_gate.

**Score:** 1e+04 (threshold 0).

---

## Case outlet_tv_60d#002  —  TP  —  GT: noise_burst

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Feb 13 2026 21:00 UTC -> Fri Feb 13 2026 21:01 UTC (duration 1.0m).

**Magnitude:** baseline 0.3 (source: prewindow_2h), peak -76.51, delta -76.81 (-25604.54%).

**Calendar context:** Friday, hour 21 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is -5.09σ vs. the median of 13 prior Friday 21:00 samples (peer median 0.3).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-76.51362360472115, score=-20.1122830715067

**Detectors fired:** data_quality_gate.

**Score:** -20.1 (threshold 0).

---

## Case outlet_tv_60d#003  —  TP  —  GT: noise_floor_up

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

## Case outlet_tv_60d#004  —  TP  —  GT: noise_floor_up

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

## Case outlet_tv_60d#005  —  TP  —  GT: noise_floor_up

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

## Case outlet_tv_60d#006  —  TP  —  GT: calibration_drift, trend

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

## Case outlet_tv_60d#007  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Feb 20 2026 21:55 UTC -> Sat Feb 21 2026 15:59 UTC (duration 18.07h).

**Magnitude:** baseline 0.3 (source: prewindow_2h), peak 20.3, delta +20 (+6666.67%).

**Calendar context:** Friday, hour 21 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is +0.47σ vs. the median of 1344 prior Friday 21:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=0.3, sigma=0.0, direction=+, delta=20.0, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=0.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#008  —  TP  —  GT: level_shift

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Feb 21 2026 15:23 UTC -> Sat Feb 21 2026 23:35 UTC (duration 8.20h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 176.8, delta +156.5 (+770.87%).

**Calendar context:** Saturday, hour 15 (afternoon), weekend, February.
**Same-hour-of-weekday baseline:** peak is +22.95σ vs. the median of 29 prior Saturday 15:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=156.48703268402468, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow
- temporal_profile: hour_of_day=15, same_hour_median=0.3, approx_hour_z=62.28308816640968, source=derived_from_same_hour_history

**Detectors fired:** cusum, sub_pca, temporal_profile.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#009  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Feb 22 2026 00:10 UTC -> Sun Feb 22 2026 20:57 UTC (duration 20.78h).

**Magnitude:** baseline 84.36 (source: prewindow_2h), peak 177.6, delta +93.24 (+110.53%).

**Calendar context:** Sunday, hour 0 (night), weekend, February.
**Same-hour-of-weekday baseline:** peak is +2.45σ vs. the median of 52 prior Sunday 0:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=84.35613694161499, sigma=72.06188749935207, direction=+, delta=93.23522789693955, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.2938216182274973, baseline=84.35613694161499, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#010  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Feb 22 2026 21:42 UTC -> Mon Feb 23 2026 15:59 UTC (duration 18.28h).

**Magnitude:** baseline 148.8 (source: prewindow_2h), peak 20.3, delta -128.5 (-86.36%).

**Calendar context:** Sunday, hour 21 (evening), weekend, February.
**Same-hour-of-weekday baseline:** peak is -1.52σ vs. the median of 73 prior Sunday 21:00 samples (peer median 142.2).

**Detector evidence:**
- cusum: mu=148.82678290288308, sigma=63.67156423530046, direction=-, delta=-128.52678290288307, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.01859000083472, baseline=148.82678290288308, source=derived_from_prewindow
- temporal_profile: hour_of_day=21, same_hour_median=0.3, approx_hour_z=0.36972859345370596, source=derived_from_same_hour_history

**Detectors fired:** cusum, sub_pca, temporal_profile.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#011  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Feb 23 2026 20:10 UTC -> Mon Feb 23 2026 20:11 UTC (duration 1.0m).

**Magnitude:** baseline 152.7 (source: prewindow_2h), peak -13.34, delta -166 (-108.74%).

**Calendar context:** Monday, hour 20 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.01σ vs. the median of 41 prior Monday 20:00 samples (peer median 0.3).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-13.337783291926758, score=-13.337783291926758

**Detectors fired:** data_quality_gate.

**Score:** -13.3 (threshold 0).

---

## Case outlet_tv_60d#012  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Feb 23 2026 20:43 UTC -> Mon Feb 23 2026 20:44 UTC (duration 1.0m).

**Magnitude:** baseline 50.44 (source: prewindow_2h), peak -6.34, delta -56.78 (-112.57%).

**Calendar context:** Monday, hour 20 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.00σ vs. the median of 54 prior Monday 20:00 samples (peer median 0.3).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.34047469737007, score=-6.34047469737007

**Detectors fired:** data_quality_gate.

**Score:** -6.34 (threshold 0).

---

## Case outlet_tv_60d#013  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Feb 23 2026 21:21 UTC -> Mon Feb 23 2026 21:22 UTC (duration 1.0m).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak -6.34, delta -26.64 (-131.23%).

**Calendar context:** Monday, hour 21 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.10σ vs. the median of 65 prior Monday 21:00 samples (peer median 0.3).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.340474697370024, score=-6.340474697370024

**Detectors fired:** data_quality_gate.

**Score:** -6.34 (threshold 0).

---

## Case outlet_tv_60d#014  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Feb 23 2026 22:11 UTC -> Mon Feb 23 2026 22:12 UTC (duration 1.0m).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak -6.34, delta -26.64 (-131.23%).

**Calendar context:** Monday, hour 22 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is -0.24σ vs. the median of 50 prior Monday 22:00 samples (peer median 10.3).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-6.340474697370038, score=-6.340474697370038

**Detectors fired:** data_quality_gate.

**Score:** -6.34 (threshold 0).

---

## Case outlet_tv_60d#015  —  TP  —  GT: frequency_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Feb 23 2026 17:13 UTC -> Mon Feb 23 2026 23:09 UTC (duration 5.93h).

**Magnitude:** baseline 158.6 (source: prewindow_2h), peak -13.34, delta -172 (-108.41%).

**Calendar context:** Monday, hour 17 (afternoon), weekday, February.
**Same-hour-of-weekday baseline:** peak is -2.53σ vs. the median of 80 prior Monday 17:00 samples (peer median 135.1).

**Detector evidence:**
- cusum: mu=158.63369633214273, sigma=67.04150334088934, direction=-, delta=-171.9714796240695, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=2.565149512677802, baseline=158.63369633214273, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.565149512677802, baseline=158.63369633214273, source=derived_from_prewindow
- temporal_profile: hour_of_day=17, same_hour_median=20.3, approx_hour_z=-0.4777777053945928, source=derived_from_same_hour_history

**Detectors fired:** cusum, multivariate_pca, sub_pca, temporal_profile.

**Score:** 1.19e+05 (threshold 0).

---

## Case outlet_tv_60d#016  —  TP  —  GT: trend

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

## Case outlet_tv_60d#017  —  TP  —  GT: frequency_change, seasonality_loss

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Tue Feb 24 2026 01:12 UTC -> Thu Feb 26 2026 20:08 UTC (duration 2.79d).
**Long-duration framing:** spans 2.8 days; covers 0 weekend day(s).

**Magnitude:** baseline 162.3 (source: prewindow_2h), peak 20.3, delta -142 (-87.49%).

**Calendar context:** Tuesday, hour 1 (night), weekday, February.
**Same-hour-of-weekday baseline:** peak is +0.26σ vs. the median of 46 prior Tuesday 1:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=162.30223686262568, sigma=29.229847115076687, direction=-, delta=-142.00223686262567, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=4.858124515792669, baseline=162.30223686262568, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.858124515792669, baseline=162.30223686262568, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 2.67e+05 (threshold 0).

---

## Case outlet_tv_60d#018  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Feb 26 2026 22:35 UTC -> Fri Feb 27 2026 07:59 UTC (duration 9.40h).

**Magnitude:** baseline 158.4 (source: prewindow_2h), peak 20.3, delta -138.1 (-87.18%).

**Calendar context:** Thursday, hour 22 (evening), weekday, February.
**Same-hour-of-weekday baseline:** peak is +0.25σ vs. the median of 69 prior Thursday 22:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=158.4031758736736, sigma=10.493991019590732, direction=-, delta=-138.1031758736736, source=derived_from_prewindow
- sub_pca: approx_residual_z=13.160214794910283, baseline=158.4031758736736, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#019  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Feb 27 2026 07:55 UTC -> Sat Feb 28 2026 02:17 UTC (duration 18.37h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 140.3, delta +120 (+591.13%).

**Calendar context:** Friday, hour 7 (morning), weekday, February.
**Same-hour-of-weekday baseline:** peak is +16.36σ vs. the median of 47 prior Friday 7:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=120.00000000000001, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#020  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Feb 28 2026 01:24 UTC -> Sat Feb 28 2026 03:31 UTC (duration 2.12h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 176.6, delta +156.3 (+769.79%).

**Calendar context:** Saturday, hour 1 (night), weekend, February.
**Same-hour-of-weekday baseline:** peak is +17.67σ vs. the median of 41 prior Saturday 1:00 samples (peer median 0.3).

**Detector evidence:**
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#021  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Feb 28 2026 02:51 UTC -> Sat Feb 28 2026 07:59 UTC (duration 5.13h).

**Magnitude:** baseline 149.7 (source: prewindow_2h), peak 20.3, delta -129.4 (-86.44%).

**Calendar context:** Saturday, hour 2 (night), weekend, February.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 67 prior Saturday 2:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=149.66590082451702, sigma=69.70955408300868, direction=-, delta=-129.365900824517, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.8557843688179498, baseline=149.66590082451702, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#022  —  TP  —  GT: month_shift

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

## Case outlet_tv_60d#023  —  TP  —  GT: time_of_day

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Feb 28 2026 07:55 UTC -> Sun Mar 01 2026 07:59 UTC (duration 1.00d).
**Long-duration framing:** spans 1.0 days; covers 2 weekend day(s).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 173, delta +152.7 (+752.17%).

**Calendar context:** Saturday, hour 7 (morning), weekend, February.
**Same-hour-of-weekday baseline:** peak is +17.09σ vs. the median of 47 prior Saturday 7:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=152.6912672992689, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#024  —  TP  —  GT: time_of_day, weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 01 2026 07:55 UTC -> Mon Mar 02 2026 00:22 UTC (duration 16.45h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 140.3, delta +120 (+591.13%).

**Calendar context:** Sunday, hour 7 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is +14.23σ vs. the median of 59 prior Sunday 7:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=28.06290618985804, direction=+, delta=120.00000000000001, source=derived_from_prewindow
- sub_pca: approx_residual_z=4.2761073706389015, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#025  —  TP  —  GT: month_shift

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

## Case outlet_tv_60d#026  —  TP  —  GT: weekend_anomaly, dropout

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Mar 02 2026 00:30 UTC -> Fri Mar 06 2026 02:35 UTC (duration 4.09d).
**Long-duration framing:** spans 4.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 176.3, delta +156 (+768.51%).

**Calendar context:** Monday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +5.72σ vs. the median of 55 prior Monday 0:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=39.23200598493046, direction=+, delta=156.00811930742776, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=176.30811930742777, score=47859.486524877706
- sub_pca: approx_residual_z=3.976552189744072, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#027  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 06 2026 00:31 UTC -> Fri Mar 06 2026 03:24 UTC (duration 2.88h).

**Magnitude:** baseline 146 (source: prewindow_2h), peak 20.3, delta -125.7 (-86.10%).

**Calendar context:** Friday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.87σ vs. the median of 120 prior Friday 0:00 samples (peer median 145).

**Detector evidence:**
- cusum: mu=146.04234676810776, sigma=70.91132231781667, direction=-, delta=-125.74234676810777, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.7732337045492472, baseline=146.04234676810776, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#028  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 06 2026 03:56 UTC -> Fri Mar 06 2026 15:59 UTC (duration 12.05h).

**Magnitude:** baseline 149.6 (source: prewindow_2h), peak 20.3, delta -129.3 (-86.43%).

**Calendar context:** Friday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.54σ vs. the median of 100 prior Friday 3:00 samples (peer median 128.6).

**Detector evidence:**
- cusum: mu=149.58809374697373, sigma=70.66597627172786, direction=-, delta=-129.28809374697371, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.8295663708066463, baseline=149.58809374697373, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#029  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 06 2026 15:25 UTC -> Fri Mar 06 2026 22:36 UTC (duration 7.18h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 176.2, delta +155.9 (+767.96%).

**Calendar context:** Friday, hour 15 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +18.66σ vs. the median of 53 prior Friday 15:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=155.89613743124113, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#030  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 06 2026 23:09 UTC -> Sun Mar 08 2026 01:38 UTC (duration 1.10d).
**Long-duration framing:** spans 1.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 148.8 (source: prewindow_2h), peak 228.3, delta +79.45 (+53.38%).

**Calendar context:** Friday, hour 23 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +1.43σ vs. the median of 89 prior Friday 23:00 samples (peer median 127.3).

**Detector evidence:**
- cusum: mu=148.82589102424407, sigma=66.78657859271098, direction=+, delta=79.4493042647598, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=228.27519528900388, score=617225.5168394364
- multivariate_pca: approx_residual_z=1.1895998558223915, baseline=148.82589102424407, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.1895998558223915, baseline=148.82589102424407, source=derived_from_prewindow
- temporal_profile: hour_of_day=23, same_hour_median=126.6534418372724, approx_hour_z=1.4195471873584322, source=derived_from_same_hour_history

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca, temporal_profile.

**Score:** 6.17e+05 (threshold 0).

---

## Case outlet_tv_60d#031  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Mar 07 2026 23:34 UTC -> Sun Mar 08 2026 05:21 UTC (duration 5.79h).

**Magnitude:** baseline 70.3 (source: prewindow_2h), peak 223.2, delta +152.9 (+217.47%).

**Calendar context:** Saturday, hour 23 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is +3.14σ vs. the median of 65 prior Saturday 23:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=70.3, sigma=0.0, direction=+, delta=152.8842178936045, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=223.1842178936045, score=596676.6578918737
- sub_pca: approx_residual_z=nan, baseline=70.3, source=derived_from_prewindow
- temporal_profile: hour_of_day=23, same_hour_median=127.23090752844944, approx_hour_z=1.3447218311978746, source=derived_from_same_hour_history

**Detectors fired:** cusum, data_quality_gate, sub_pca, temporal_profile.

**Score:** 5.97e+05 (threshold 0).

---

## Case outlet_tv_60d#032  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 08 2026 03:17 UTC -> Sun Mar 08 2026 09:41 UTC (duration 6.40h).

**Magnitude:** baseline 200 (source: prewindow_2h), peak 70.3, delta -129.7 (-64.86%).

**Calendar context:** Sunday, hour 3 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.83σ vs. the median of 104 prior Sunday 3:00 samples (peer median 127.6).

**Detector evidence:**
- cusum: mu=200.03791789894564, sigma=9.546791169750922, direction=-, delta=-129.73791789894562, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=70.3, score=586278.7099297518
- multivariate_pca: approx_residual_z=13.58968847145428, baseline=200.03791789894564, source=derived_from_prewindow
- sub_pca: approx_residual_z=13.58968847145428, baseline=200.03791789894564, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#033  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 08 2026 07:37 UTC -> Sun Mar 08 2026 11:16 UTC (duration 3.65h).

**Magnitude:** baseline 70.3 (source: prewindow_2h), peak 70.3, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 7 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is +4.76σ vs. the median of 62 prior Sunday 7:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=70.3, sigma=0.0, direction=0, delta=0.0, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=70.3, score=586278.7099297518
- multivariate_pca: approx_residual_z=nan, baseline=70.3, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=70.3, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#034  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 08 2026 09:12 UTC -> Sun Mar 08 2026 15:36 UTC (duration 6.40h).

**Magnitude:** baseline 70.3 (source: prewindow_2h), peak 70.3, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 9 (morning), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.28σ vs. the median of 61 prior Sunday 9:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=70.3, sigma=0.0, direction=0, delta=0.0, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=70.3, score=586278.7099297518
- multivariate_pca: approx_residual_z=nan, baseline=70.3, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=70.3, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#035  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 08 2026 13:32 UTC -> Sun Mar 08 2026 17:41 UTC (duration 4.15h).

**Magnitude:** baseline 70.3 (source: prewindow_2h), peak 70.3, delta +0 (+0.00%).

**Calendar context:** Sunday, hour 13 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is +5.55σ vs. the median of 61 prior Sunday 13:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=70.3, sigma=0.0, direction=0, delta=0.0, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=70.3, score=586278.7099297518
- multivariate_pca: approx_residual_z=nan, baseline=70.3, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=70.3, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#036  —  TP  —  GT: month_shift, duplicate_stale

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

## Case outlet_tv_60d#037  —  TP  —  GT: weekend_anomaly, reporting_rate_change

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 08 2026 15:37 UTC -> Mon Mar 09 2026 02:36 UTC (duration 10.98h).

**Magnitude:** baseline 70.3 (source: prewindow_2h), peak 174.8, delta +104.5 (+148.72%).

**Calendar context:** Sunday, hour 15 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is +11.87σ vs. the median of 62 prior Sunday 15:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=70.3, sigma=0.0, direction=+, delta=104.548935342111, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=174.848935342111, score=586278.7099297518
- multivariate_pca: approx_residual_z=nan, baseline=70.3, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=70.3, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#038  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Mar 09 2026 01:52 UTC -> Mon Mar 09 2026 15:59 UTC (duration 14.12h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 174.8, delta +154.5 (+761.32%).

**Calendar context:** Monday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.48σ vs. the median of 106 prior Monday 1:00 samples (peer median 139.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=47.991327279615035, direction=+, delta=154.54893534211098, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.2203513447680314, baseline=20.3, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.2203513447680314, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 1.47e+05 (threshold 0).

---

## Case outlet_tv_60d#039  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Mar 09 2026 15:05 UTC -> Mon Mar 09 2026 18:08 UTC (duration 3.05h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 172.4, delta +152.1 (+749.40%).

**Calendar context:** Monday, hour 15 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +17.36σ vs. the median of 61 prior Monday 15:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=152.1279449402686, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#040  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#041  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#042  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#043  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#044  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#045  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#046  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#047  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#048  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#049  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#050  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#051  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#052  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#053  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#054  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#055  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#056  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#057  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#058  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#059  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#060  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#061  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#062  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#063  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#064  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#065  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#066  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Mon Mar 09 2026 17:07 UTC -> Tue Mar 10 2026 01:55 UTC (duration 8.80h).

**Magnitude:** baseline 151 (source: prewindow_2h), peak 20.3, delta -130.7 (-86.56%).

**Calendar context:** Monday, hour 17 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.96σ vs. the median of 119 prior Monday 17:00 samples (peer median 139.3).

**Detector evidence:**
- cusum: mu=150.99010428184687, sigma=55.126774060723896, direction=-, delta=-130.69010428184686, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.37071924683798, baseline=150.99010428184687, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#067  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#068  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#069  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#070  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#071  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#072  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#073  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#074  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Tue Mar 10 2026 02:42 UTC -> Wed Mar 11 2026 20:55 UTC (duration 1.76d).
**Long-duration framing:** spans 1.8 days; covers 0 weekend day(s).

**Magnitude:** baseline 149.2 (source: prewindow_2h), peak 20.3, delta -128.9 (-86.39%).

**Calendar context:** Tuesday, hour 2 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.62σ vs. the median of 105 prior Tuesday 2:00 samples (peer median 146.1).

**Detector evidence:**
- cusum: mu=149.16077651673635, sigma=63.4794173449293, direction=-, delta=-128.86077651673634, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.0299615514197793, baseline=149.16077651673635, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#075  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Wed Mar 11 2026 21:39 UTC -> Wed Mar 11 2026 23:58 UTC (duration 2.32h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 178.4, delta +158.1 (+778.92%).

**Calendar context:** Wednesday, hour 21 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +3.28σ vs. the median of 70 prior Wednesday 21:00 samples (peer median 0.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=70.3538117833165, direction=+, delta=158.11998841426447, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2474971065002136, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#076  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_2h), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.76σ vs. the median of 100 prior Thursday 0:00 samples (peer median 130.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=20.3, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#077  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_2h), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.76σ vs. the median of 100 prior Thursday 0:00 samples (peer median 130.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=20.3, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#078  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_2h), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.76σ vs. the median of 100 prior Thursday 0:00 samples (peer median 130.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=20.3, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#079  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_2h), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.76σ vs. the median of 100 prior Thursday 0:00 samples (peer median 130.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=20.3, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#080  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_2h), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.76σ vs. the median of 100 prior Thursday 0:00 samples (peer median 130.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=20.3, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#081  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_2h), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.76σ vs. the median of 100 prior Thursday 0:00 samples (peer median 130.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=20.3, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#082  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_2h), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.76σ vs. the median of 100 prior Thursday 0:00 samples (peer median 130.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=20.3, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#083  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_2h), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.76σ vs. the median of 100 prior Thursday 0:00 samples (peer median 130.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=20.3, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#084  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_2h), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.76σ vs. the median of 100 prior Thursday 0:00 samples (peer median 130.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=duplicate_stale, value=20.3, score=0.0

**Detectors fired:** data_quality_gate.

**Score:** 0 (threshold 0).

---

## Case outlet_tv_60d#085  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 00:59 UTC -> Thu Mar 12 2026 01:00 UTC (duration 1.0m).

**Magnitude:** baseline 150.8 (source: prewindow_2h), peak 20.3, delta -130.5 (-86.54%).

**Calendar context:** Thursday, hour 0 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.76σ vs. the median of 100 prior Thursday 0:00 samples (peer median 130.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=batch_arrival, value=20.3, score=12.0

**Detectors fired:** data_quality_gate.

**Score:** 12 (threshold 0).

---

## Case outlet_tv_60d#086  —  TP  —  GT: weekend_anomaly, batch_arrival

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Wed Mar 11 2026 21:54 UTC -> Thu Mar 12 2026 04:02 UTC (duration 6.13h).

**Magnitude:** baseline 151 (source: prewindow_2h), peak 20.3, delta -130.7 (-86.55%).

**Calendar context:** Wednesday, hour 21 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 81 prior Wednesday 21:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=150.97828584156565, sigma=67.9475791983249, direction=-, delta=-130.67828584156564, source=derived_from_prewindow
- data_quality_gate: anomaly_type=None, value=20.3, score=47859.486524877706
- sub_pca: approx_residual_z=1.9232220983199828, baseline=150.97828584156565, source=derived_from_prewindow

**Detectors fired:** cusum, data_quality_gate, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#087  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 03:27 UTC -> Thu Mar 12 2026 21:34 UTC (duration 18.12h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 179.7, delta +159.4 (+785.42%).

**Calendar context:** Thursday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.84σ vs. the median of 113 prior Thursday 3:00 samples (peer median 128.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=159.44003636863624, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#088  —  TP  —  GT: month_shift, clock_drift

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

## Case outlet_tv_60d#089  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 15 2026 02:23 UTC -> Sun Mar 15 2026 02:24 UTC (duration 1.0m).

**Magnitude:** baseline 111.9 (source: prewindow_2h), peak -26.32, delta -138.3 (-123.52%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is -2.50σ vs. the median of 114 prior Sunday 2:00 samples (peer median 131.9).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-26.323297106264874, score=-26.323297106264874

**Detectors fired:** data_quality_gate.

**Score:** -26.3 (threshold 0).

---

## Case outlet_tv_60d#090  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 12 2026 21:08 UTC -> Sat Mar 14 2026 23:59 UTC (duration 2.12d).
**Long-duration framing:** spans 2.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 215, delta +194.7 (+959.23%).

**Calendar context:** Thursday, hour 21 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.50σ vs. the median of 91 prior Thursday 21:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=194.72423299779518, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#091  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 15 2026 02:53 UTC -> Sun Mar 15 2026 02:54 UTC (duration 1.0m).

**Magnitude:** baseline -15.26 (source: prewindow_2h), peak -17.51, delta -2.25 (+14.74%).

**Calendar context:** Sunday, hour 2 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is -1.92σ vs. the median of 140 prior Sunday 2:00 samples (peer median 128.4).

**Detector evidence:**
- data_quality_gate: anomaly_type=out_of_range, value=-17.510744139825874, score=-17.510744139825874

**Detectors fired:** data_quality_gate.

**Score:** -17.5 (threshold 0).

---

## Case outlet_tv_60d#092  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 15 2026 00:19 UTC -> Sun Mar 15 2026 03:17 UTC (duration 2.97h).

**Magnitude:** baseline 70.3 (source: prewindow_2h), peak -43.93, delta -114.2 (-162.50%).

**Calendar context:** Sunday, hour 0 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is -1.95σ vs. the median of 86 prior Sunday 0:00 samples (peer median 91.12).

**Detector evidence:**
- cusum: mu=70.3, sigma=15.850363776687955, direction=-, delta=-114.23485913067086, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=7.207081221610993, baseline=70.3, source=derived_from_prewindow
- sub_pca: approx_residual_z=7.207081221610993, baseline=70.3, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 5.82e+05 (threshold 0).

---

## Case outlet_tv_60d#093  —  TP  —  GT: weekend_anomaly, seasonal_mismatch

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 15 2026 03:55 UTC -> Sun Mar 15 2026 23:46 UTC (duration 19.85h).

**Magnitude:** baseline -17.51 (source: prewindow_2h), peak 225.2, delta +242.7 (-1386.28%).

**Calendar context:** Sunday, hour 3 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.41σ vs. the median of 118 prior Sunday 3:00 samples (peer median 125.8).

**Detector evidence:**
- cusum: mu=-17.510744139825874, sigma=64.24503246996443, direction=+, delta=242.74854059126727, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=3.778479537772139, baseline=-17.510744139825874, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.778479537772139, baseline=-17.510744139825874, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 5.86e+05 (threshold 0).

---

## Case outlet_tv_60d#094  —  TP  —  GT: month_shift, stuck_at

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

## Case outlet_tv_60d#095  —  TP  —  GT: weekend_anomaly

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 15 2026 22:54 UTC -> Tue Mar 17 2026 01:27 UTC (duration 1.11d).
**Long-duration framing:** spans 1.1 days; covers 1 weekend day(s).

**Magnitude:** baseline 70.3 (source: prewindow_2h), peak 225.2, delta +154.9 (+220.40%).

**Calendar context:** Sunday, hour 22 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is +2.11σ vs. the median of 112 prior Sunday 22:00 samples (peer median 70.3).

**Detector evidence:**
- cusum: mu=70.3, sigma=0.0, direction=+, delta=154.9377964514414, source=derived_from_prewindow
- multivariate_pca: approx_residual_z=nan, baseline=70.3, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=70.3, source=derived_from_prewindow

**Detectors fired:** cusum, multivariate_pca, sub_pca.

**Score:** 5.82e+05 (threshold 0).

---

## Case outlet_tv_60d#096  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Tue Mar 17 2026 03:56 UTC -> Tue Mar 17 2026 15:59 UTC (duration 12.05h).

**Magnitude:** baseline 161.7 (source: prewindow_2h), peak 20.3, delta -141.4 (-87.44%).

**Calendar context:** Tuesday, hour 3 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is -1.60σ vs. the median of 120 prior Tuesday 3:00 samples (peer median 143.3).

**Detector evidence:**
- cusum: mu=161.65420320988207, sigma=10.824959002754829, direction=-, delta=-141.35420320988206, source=derived_from_prewindow
- sub_pca: approx_residual_z=13.0581744627309, baseline=161.65420320988207, source=derived_from_prewindow
- temporal_profile: hour_of_day=3, same_hour_median=70.3, approx_hour_z=-0.7140344003471096, source=derived_from_same_hour_history

**Detectors fired:** cusum, sub_pca, temporal_profile.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#097  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Tue Mar 17 2026 17:17 UTC -> Wed Mar 18 2026 01:39 UTC (duration 8.37h).

**Magnitude:** baseline 154.6 (source: prewindow_2h), peak 20.3, delta -134.3 (-86.87%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 95 prior Tuesday 17:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=154.61969090681592, sigma=46.22815398306735, direction=-, delta=-134.3196909068159, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.9055819740501665, baseline=154.61969090681592, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#098  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Wed Mar 18 2026 01:03 UTC -> Wed Mar 18 2026 20:20 UTC (duration 19.28h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 174.6, delta +154.3 (+760.11%).

**Calendar context:** Wednesday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.87σ vs. the median of 82 prior Wednesday 1:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=154.30303491817494, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#099  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Wed Mar 18 2026 20:36 UTC -> Thu Mar 19 2026 21:24 UTC (duration 1.03d).
**Long-duration framing:** spans 1.0 days; covers 0 weekend day(s).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 180.1, delta +159.8 (+786.99%).

**Calendar context:** Wednesday, hour 20 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +3.41σ vs. the median of 83 prior Wednesday 20:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=69.09888641849281, direction=+, delta=159.75873350151699, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.3120305084795265, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#100  —  TP  —  GT: month_shift, stuck_at, degradation_trajectory

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

## Case outlet_tv_60d#101  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 20 2026 01:52 UTC -> Sat Mar 21 2026 03:02 UTC (duration 1.05d).
**Long-duration framing:** spans 1.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 161.7 (source: prewindow_2h), peak 20.3, delta -141.4 (-87.44%).

**Calendar context:** Friday, hour 1 (night), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 104 prior Friday 1:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=161.65002202455378, sigma=9.837513475484432, direction=-, delta=-141.35002202455377, source=derived_from_prewindow
- sub_pca: approx_residual_z=14.368470485636943, baseline=161.65002202455378, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#102  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Mar 21 2026 02:48 UTC -> Sun Mar 22 2026 04:10 UTC (duration 1.06d).
**Long-duration framing:** spans 1.1 days; covers 2 weekend day(s).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 174.1, delta +153.8 (+757.84%).

**Calendar context:** Saturday, hour 2 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.57σ vs. the median of 110 prior Saturday 2:00 samples (peer median 70.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=153.8416155979323, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#103  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 22 2026 03:56 UTC -> Sun Mar 22 2026 17:17 UTC (duration 13.35h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 176, delta +155.7 (+766.88%).

**Calendar context:** Sunday, hour 3 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.92σ vs. the median of 131 prior Sunday 3:00 samples (peer median 111.9).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=155.67599127086936, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#104  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 22 2026 19:16 UTC -> Tue Mar 24 2026 18:18 UTC (duration 1.96d).
**Long-duration framing:** spans 2.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 159.2 (source: prewindow_2h), peak 20.3, delta -138.9 (-87.25%).

**Calendar context:** Sunday, hour 19 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 96 prior Sunday 19:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=159.24662076867773, sigma=9.694687162541138, direction=-, delta=-138.94662076867772, source=derived_from_prewindow
- sub_pca: approx_residual_z=14.332243881530006, baseline=159.24662076867773, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#105  —  TP  —  GT: month_shift, degradation_trajectory

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

## Case outlet_tv_60d#106  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Tue Mar 24 2026 17:27 UTC -> Thu Mar 26 2026 20:04 UTC (duration 2.11d).
**Long-duration framing:** spans 2.1 days; covers 0 weekend day(s).

**Magnitude:** baseline 144.4 (source: prewindow_2h), peak 20.3, delta -124.1 (-85.94%).

**Calendar context:** Tuesday, hour 17 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.00σ vs. the median of 119 prior Tuesday 17:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=144.39075971677985, sigma=71.74565135313979, direction=-, delta=-124.09075971677986, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.7295927680130998, baseline=144.39075971677985, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#107  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 26 2026 20:09 UTC -> Fri Mar 27 2026 00:30 UTC (duration 4.35h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 178, delta +157.7 (+776.67%).

**Calendar context:** Thursday, hour 20 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.81σ vs. the median of 89 prior Thursday 20:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=46.307017270960586, direction=+, delta=157.66500966321024, source=derived_from_prewindow
- sub_pca: approx_residual_z=3.4047757544099677, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#108  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Thu Mar 26 2026 23:46 UTC -> Fri Mar 27 2026 17:04 UTC (duration 17.30h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 179, delta +158.7 (+781.87%).

**Calendar context:** Thursday, hour 23 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.41σ vs. the median of 152 prior Thursday 23:00 samples (peer median 147.7).

**Detector evidence:**
- cusum: mu=20.3, sigma=71.44410423972461, direction=+, delta=158.7189303145497, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.2215819206296135, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#109  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 27 2026 16:24 UTC -> Fri Mar 27 2026 20:48 UTC (duration 4.40h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 177.4, delta +157.1 (+773.71%).

**Calendar context:** Friday, hour 16 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +0.67σ vs. the median of 154 prior Friday 16:00 samples (peer median 135.7).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=157.06214411279547, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#110  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Fri Mar 27 2026 20:37 UTC -> Sat Mar 28 2026 03:01 UTC (duration 6.40h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 179.9, delta +159.6 (+786.01%).

**Calendar context:** Friday, hour 20 (evening), weekday, March.
**Same-hour-of-weekday baseline:** peak is +3.18σ vs. the median of 98 prior Friday 20:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=159.56075248540535, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#111  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Mar 28 2026 02:00 UTC -> Sat Mar 28 2026 19:50 UTC (duration 17.83h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 179.9, delta +159.6 (+786.45%).

**Calendar context:** Saturday, hour 2 (night), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.66σ vs. the median of 112 prior Saturday 2:00 samples (peer median 70.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=159.64866774608956, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#112  —  TP  —  GT: month_shift, degradation_trajectory

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

## Case outlet_tv_60d#113  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Mar 28 2026 18:47 UTC -> Sat Mar 28 2026 23:12 UTC (duration 4.42h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 176.3, delta +156 (+768.52%).

**Calendar context:** Saturday, hour 18 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is +2.95σ vs. the median of 115 prior Saturday 18:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=54.26025427367151, direction=+, delta=156.00957879002019, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.8752091356438796, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#114  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sat Mar 28 2026 23:47 UTC -> Sun Mar 29 2026 16:47 UTC (duration 17.00h).

**Magnitude:** baseline 150.9 (source: prewindow_2h), peak 20.3, delta -130.6 (-86.55%).

**Calendar context:** Saturday, hour 23 (evening), weekend, March.
**Same-hour-of-weekday baseline:** peak is -0.73σ vs. the median of 129 prior Saturday 23:00 samples (peer median 70.3).

**Detector evidence:**
- cusum: mu=150.94410392521118, sigma=68.57906855935224, direction=-, delta=-130.64410392521117, source=derived_from_prewindow
- sub_pca: approx_residual_z=1.9050142655720719, baseline=150.94410392521118, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#115  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Sun Mar 29 2026 16:10 UTC -> Tue Mar 31 2026 16:09 UTC (duration 2.00d).
**Long-duration framing:** spans 2.0 days; covers 1 weekend day(s).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 178, delta +157.7 (+777.00%).

**Calendar context:** Sunday, hour 16 (afternoon), weekend, March.
**Same-hour-of-weekday baseline:** peak is +1.71σ vs. the median of 117 prior Sunday 16:00 samples (peer median 70.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=157.73142588716937, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#116  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Tue Mar 31 2026 16:09 UTC -> Tue Mar 31 2026 22:55 UTC (duration 6.77h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 173.7, delta +153.4 (+755.68%).

**Calendar context:** Tuesday, hour 16 (afternoon), weekday, March.
**Same-hour-of-weekday baseline:** peak is +2.06σ vs. the median of 135 prior Tuesday 16:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=0.0, direction=+, delta=153.40356351489, source=derived_from_prewindow
- sub_pca: approx_residual_z=nan, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#117  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Wed Apr 01 2026 02:54 UTC -> Wed Apr 01 2026 17:00 UTC (duration 14.10h).

**Magnitude:** baseline 160.2 (source: prewindow_2h), peak 20.3, delta -139.9 (-87.33%).

**Calendar context:** Wednesday, hour 2 (night), weekday, April.
**Same-hour-of-weekday baseline:** peak is -0.37σ vs. the median of 163 prior Wednesday 2:00 samples (peer median 47.51).

**Detector evidence:**
- cusum: mu=160.17827518804296, sigma=9.839344660380341, direction=-, delta=-139.87827518804295, source=derived_from_prewindow
- sub_pca: approx_residual_z=14.216218662538033, baseline=160.17827518804296, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#118  —  FP  —  GT: (none)

# Anomaly on sensor outlet_tv_power (capability: power)

**When:** Wed Apr 01 2026 16:29 UTC -> Wed Apr 01 2026 23:55 UTC (duration 7.43h).

**Magnitude:** baseline 20.3 (source: prewindow_2h), peak 177.3, delta +157 (+773.50%).

**Calendar context:** Wednesday, hour 16 (afternoon), weekday, April.
**Same-hour-of-weekday baseline:** peak is +2.54σ vs. the median of 120 prior Wednesday 16:00 samples (peer median 20.3).

**Detector evidence:**
- cusum: mu=20.3, sigma=59.81089981856478, direction=+, delta=157.01988956106212, source=derived_from_prewindow
- sub_pca: approx_residual_z=2.6252721500157823, baseline=20.3, source=derived_from_prewindow

**Detectors fired:** cusum, sub_pca.

**Score:** 4.79e+04 (threshold 0).

---

## Case outlet_tv_60d#119  —  TP  —  GT: month_shift, degradation_trajectory

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
