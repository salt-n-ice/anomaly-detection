from pathlib import Path
import pandas as pd
import pytest
from anomaly.pipeline import run
from anomaly.metrics import compute_metrics, interval_match

DATA = Path("C:/Projects/Sensor-data-anomaly-detection/synthetic-generator/out/outlet7")


@pytest.mark.skipif(not DATA.exists(), reason="7-day outlet dataset not generated")
def test_outlet_pipeline_recall(tmp_path):
    out = tmp_path / "detections.csv"
    run(DATA / "events.csv", Path("configs/outlet.yaml"), out, bootstrap_days=2.0)
    det = pd.read_csv(out)
    labels = pd.read_csv(DATA / "labels.csv")

    # Report all classes
    m = compute_metrics(labels, det)
    print("\noutlet metrics:", m)

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

    # Minimum targets per spec (interval-overlap recall)
    assert m["recall"] >= 0.5, f"overall recall {m['recall']:.2f} below 0.5"

    # Spot-check: out-of-range spike must be caught
    tp_oor, fp_oor, fn_oor = interval_match(
        labels[labels["anomaly_type"] == "out_of_range"], det)
    assert len(tp_oor) >= 1, "out_of_range anomaly not caught by DQG"

    tp_do, fp_do, fn_do = interval_match(
        labels[labels["anomaly_type"] == "dropout"], det)
    assert len(tp_do) >= 1, "dropout not caught by DQG"
