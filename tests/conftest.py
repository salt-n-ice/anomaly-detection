import os as _os
import sys as _sys

# Make this conftest.py importable as a top-level `conftest` module so test
# modules can do `from conftest import ts`. Without this, the empty
# tests/__init__.py turns the dir into a package and shadows the bare import.
_HERE = _os.path.dirname(_os.path.abspath(__file__))
if _HERE not in _sys.path:
    _sys.path.insert(0, _HERE)

import pandas as pd


def ts(s: str) -> pd.Timestamp:
    return pd.Timestamp(s, tz="UTC")


def _minimal_viz_scenario():
    """Returns (events_df, labels_df, detections_df) covering one TP user_behavior,
    one FN, one user-visible FP, and one sensor-fault chain (suppressed).
    Used across viz tests."""
    import pandas as _pd
    events = _pd.DataFrame({
        "timestamp": _pd.to_datetime([
            "2026-02-15T00:00:00Z", "2026-02-16T00:00:00Z",
            "2026-02-17T00:00:00Z", "2026-02-18T00:00:00Z",
            "2026-02-19T00:00:00Z", "2026-02-20T00:00:00Z",
            # FN sensor
            "2026-02-15T00:00:00Z", "2026-02-16T00:00:00Z",
            "2026-02-17T00:00:00Z", "2026-02-18T00:00:00Z",
        ]),
        "sensor_id": (["outlet_tv_power"]*6 + ["bedroom_motion"]*4),
        "capability": (["power"]*6 + ["motion"]*4),
        "value": [100.0, 110.0, 250.0, 240.0, 105.0, 102.0,
                  0, 0, 1, 0],
        "unit": ["W"]*6 + [""]*4,
    })
    labels = _pd.DataFrame({
        "sensor_id": ["outlet_tv_power", "bedroom_motion"],
        "capability": ["power", "motion"],
        "start": _pd.to_datetime(["2026-02-16T12:00:00Z", "2026-02-17T03:00:00Z"]),
        "end":   _pd.to_datetime(["2026-02-18T12:00:00Z", "2026-02-17T04:00:00Z"]),
        "anomaly_type": ["weekend_anomaly", "unusual_occupancy"],
        "label_class": ["user_behavior", "user_behavior"],
        "detector_hint": ["", ""],
        "params_json": ["{}", "{}"],
    })
    detections = _pd.DataFrame({
        "sensor_id": ["outlet_tv_power", "outlet_tv_power", "outlet_tv_power"],
        "capability": ["power", "power", "power"],
        "start": _pd.to_datetime([
            "2026-02-17T00:00:00Z",  # TP — overlaps the weekend label
            "2026-02-19T00:00:00Z",  # FP — user-visible (no GT overlap)
            "2026-02-20T00:00:00Z",  # Suppressed sensor-fault
        ]),
        "end": _pd.to_datetime([
            "2026-02-17T00:01:00Z",
            "2026-02-19T00:01:00Z",
            "2026-02-20T00:01:00Z",
        ]),
        "first_fire_ts": _pd.to_datetime([
            "2026-02-17T00:01:00Z",
            "2026-02-19T00:01:00Z",
            "2026-02-20T00:01:00Z",
        ]),
        "anomaly_type": ["duty_cycle_shift_6h", "duty_cycle_shift_6h", "out_of_range"],
        "inferred_type": ["weekend_anomaly", "level_shift", "out_of_range"],
        "inferred_class": ["user_behavior", "user_behavior", "sensor_fault"],
        "detector": ["duty_cycle_shift_6h", "duty_cycle_shift_6h", "data_quality_gate"],
        "threshold": [3.0, 3.0, 3.0],
        "score": [4.5, 3.2, 5.1],
    })
    return events, labels, detections
