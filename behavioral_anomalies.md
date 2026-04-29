# Behavioral Anomalies — Captured Types & Use Cases

Vocabulary from `USER_BEHAVIOR_TYPES` in `src/anomaly/explain/types.py`.
Each row is what the classifier emits + a one-line household scenario.

| Type | What it means | Use case |
|---|---|---|
| **time_of_day** | Same activity, different hour-of-day than usual | "Your morning kettle moved from 7 AM to 10 AM this week — schedule shift?" Catches WFH transitions, sleep changes, new caregiver routines. |
| **weekend_anomaly** | Pattern fires only on weekdays (or only on weekends) when it shouldn't | "TV is on every Saturday but never on weekdays — is the routine inverted?" Useful for elderly-care: detects whether someone's normally-busy weekdays have gone quiet. |
| **frequency_change** | Same time-of-day, but more or fewer events per hour | "Fridge is opening 3× more often than usual." Flags binge cycles, hosting guests, or appliance overuse. |
| **level_shift** | Step change to a new sustained baseline | "Voltage dropped 5 V on Tuesday and stayed there." Detects breaker switches, new appliance plugged in, or AC compressor wearing in. |
| **spike** | Brief, sharp upward excursion | "Sudden 3 kW draw on the kitchen circuit at 2 AM." Surfaces unattended-appliance moments worth a glance. |
| **dip** | Brief, sharp downward excursion | "Fridge power crashed for 3 minutes." Door left open, brownout, or compressor stall. |
| **trend** | Slow, monotonic drift in either direction | "Basement temperature has been climbing 0.5 °C per week." Early warning for HVAC sizing, insulation degradation, season-change mis-tracking. |
| **degradation_trajectory** | Multi-week decay pattern (≥7 days, gradual) | "Kettle peak draw has slowly dropped from 2200 W to 1900 W over a month." Predictive replacement signal — appliance heading toward failure. |
| **month_shift** | Level offset on a month timescale (longer than level_shift) | "Average voltage this month is 3 V below last month." Utility-side regulator drift, seasonal grid load, or moving-average billing anomalies. |
| **calibration_drift** | Sustained voltage/temperature offset that looks systematic, not behavioral | "Voltage reads 2.5 V high consistently for 12+ hours." Alerts to recalibration need before billing/safety thresholds get triggered. |
| **seasonality_loss** | Expected daily/weekly cycle has flattened | "Basement temperature usually swings 5 °C day-to-night — now it's flat." HVAC stuck on, broken thermostat, or the household has gone away. |
| **seasonal_mismatch** | Activity pattern doesn't match the season | "Heating is running like it's January, but it's April." Forgotten scheduled program or thermostat error. |
| **water_leak_sustained** | Leak sensor turned on and stayed on | "Water detected under the sink — 2 minutes ago, still active." Minutes-budget alert; goes immediate, no statistical wait. |
| **temporal_pattern** | Calendar pattern that isn't cleanly weekend/time-of-day (fallback) | "Activity shifted on a calendar boundary we don't have a name for." Catch-all so unusual but real shifts aren't dropped. |
| **statistical_anomaly** | Statistically unusual but no clean semantic match (fallback) | "Something measurably abnormal here — flagging for human review." Keeps recall up when the dispatch tree can't classify confidently. |

`usage_anomaly` is in the GT vocabulary but the detector classifier doesn't currently emit it — those chains land as `level_shift` / `time_of_day` and contribute `tyAcc=0` for the day, even though they still count as TPs for `evt_F1` / `fpur` / `uvfp/d`.
