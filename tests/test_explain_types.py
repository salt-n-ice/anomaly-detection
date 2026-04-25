from anomaly.explain.types import (
    USER_BEHAVIOR_TYPES, SENSOR_FAULT_TYPES, type_to_class,
)


def test_user_behavior_types_includes_canonical_set():
    expected = {"spike", "dip", "level_shift", "trend",
                "degradation_trajectory", "frequency_change",
                "seasonality_loss", "time_of_day", "weekend_anomaly",
                "month_shift", "seasonal_mismatch",
                "water_leak_sustained", "unusual_occupancy"}
    assert USER_BEHAVIOR_TYPES == frozenset(expected)


def test_sensor_fault_types_includes_canonical_set():
    expected = {"out_of_range", "saturation", "noise_burst",
                "noise_floor_up", "stuck_at", "calibration_drift",
                "dropout", "duplicate_stale", "reporting_rate_change",
                "clock_drift", "batch_arrival"}
    assert SENSOR_FAULT_TYPES == frozenset(expected)


def test_type_to_class_user_behavior():
    assert type_to_class("level_shift") == "user_behavior"
    assert type_to_class("water_leak_sustained") == "user_behavior"


def test_type_to_class_sensor_fault():
    assert type_to_class("dropout") == "sensor_fault"
    assert type_to_class("calibration_drift") == "sensor_fault"


def test_type_to_class_unknown_for_detector_string():
    assert type_to_class("cusum+multivariate_pca") == "unknown"
    assert type_to_class("statistical_anomaly") == "unknown"


def test_re_export_from_package_root_still_works():
    from anomaly.explain import (
        USER_BEHAVIOR_TYPES as a, SENSOR_FAULT_TYPES as b, type_to_class as c)
    assert a == USER_BEHAVIOR_TYPES
    assert b == SENSOR_FAULT_TYPES
    assert c is type_to_class
