from pathlib import Path
import pandas as pd
import pytest
from anomaly.pipeline import run
from anomaly.metrics import compute_metrics, interval_match

DATA = Path("C:/Projects/Sensor-data-anomaly-detection/synthetic-generator/out/leak7")


@pytest.mark.skipif(not DATA.exists(), reason="7-day leak dataset not generated")
def test_leak_pipeline_recall(tmp_path):
    out = tmp_path / "detections.csv"
    run(DATA / "events.csv", Path("configs/waterleak.yaml"), out, bootstrap_days=2.0)
    det = pd.read_csv(out)
    labels = pd.read_csv(DATA / "labels.csv")

    m = compute_metrics(labels, det)
    print("\nleak metrics:", m)

    # Print false negatives so we can see what's missed
    tp, fp, fn = interval_match(labels, det)
    print(f"\nTP ({len(tp)}):")
    for x in tp:
        print(f"  TP  {x.sensor_id}/{x.anomaly_type}  {x.start} -- {x.end}")
    print(f"\nFN ({len(fn)}):")
    for x in fn:
        print(f"  FN  {x.sensor_id}/{x.anomaly_type}  {x.start} -- {x.end}")
    print(f"\nFP ({len(fp)}):")
    for x in fp:
        print(f"  FP  {x.sensor_id}/{x.anomaly_type}  {x.start} -- {x.end}")

    assert m["recall"] >= 0.4, f"overall recall {m['recall']:.2f} below 0.4"

    # water_leak_sustained MUST be caught deterministically
    tp_wl, fp_wl, fn_wl = interval_match(
        labels[labels["anomaly_type"] == "water_leak_sustained"], det)
    assert len(tp_wl) >= 1, "water_leak_sustained not caught deterministically"
