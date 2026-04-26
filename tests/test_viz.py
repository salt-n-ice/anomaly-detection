import pandas as pd


def test_style_palette_constants_present():
    from anomaly.viz import style
    assert style.LINE == "#1a1a1a"
    assert style.TP == "#2a7f2a"
    assert style.GT == "#d62828"
    assert style.FP == "#d6a228"
    assert style.SUPPRESSED == "#888888"


def test_style_apply_runs_without_error():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from anomaly.viz import style
    style.apply()
    assert plt.rcParams["font.family"] == ["DejaVu Sans"]


def test_type_friendly_known():
    from anomaly.viz.style import type_friendly
    assert type_friendly("level_shift") == "level shift"
    assert type_friendly("water_leak_sustained") == "sustained water leak"
    assert type_friendly("trend") == "gradual drift"


def test_type_friendly_fallback():
    from anomaly.viz.style import type_friendly
    assert type_friendly("brand_new_type") == "brand new type"
    assert type_friendly("") == ""


def test_sensor_friendly_outlet():
    from anomaly.viz.style import sensor_friendly
    assert sensor_friendly("outlet_tv_power") == "TV outlet"
    assert sensor_friendly("outlet_kettle_power") == "Kettle outlet"
    assert sensor_friendly("outlet_fridge_power") == "Fridge outlet"


def test_sensor_friendly_other_prefixes():
    from anomaly.viz.style import sensor_friendly
    assert sensor_friendly("mains_voltage") == "Mains voltage"
    assert sensor_friendly("basement_leak") == "Basement leak sensor"
    assert sensor_friendly("kitchen_temperature") == "Kitchen temperature"


def test_sensor_friendly_override():
    from anomaly.viz.style import sensor_friendly
    overrides = {"outlet_tv_power": "Living-room TV"}
    assert sensor_friendly("outlet_tv_power", overrides) == "Living-room TV"
    # Unrelated sensor falls through to auto-derive
    assert sensor_friendly("outlet_kettle_power", overrides) == "Kettle outlet"


def test_sensor_friendly_unknown_pattern():
    from anomaly.viz.style import sensor_friendly
    # Unknown shape — title-case fallback
    assert sensor_friendly("weird_id_thing") == "Weird id thing"
