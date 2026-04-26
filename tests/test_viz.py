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
