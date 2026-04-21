import pandas as pd
from anomaly.core import Alert, SensorConfig, Archetype
from anomaly.fusion import (DefaultAlertFuser, PassThroughCorroboration,
                            ContinuousCorroboration, group_alerts)


def ts(s): return pd.Timestamp(s, tz="UTC")


def _alert(detector, t, score=1.0, atype=None):
    return Alert("s", "v", ts(t), detector, score, 0.0, atype,
                 raw_value=None, state=None,
                 window_start=ts(t), window_end=ts(t),
                 context=[{"detector": detector}])


def _cfg_cont():
    return SensorConfig("s", "v", Archetype.CONTINUOUS, expected_interval_sec=60)


def _cfg_bursty():
    return SensorConfig("s", "v", Archetype.BURSTY, expected_interval_sec=60)


def test_passthrough_corroboration_accepts_all():
    rule = PassThroughCorroboration()
    assert rule.accepts([_alert("cusum", "2026-02-01T00:00:00Z")])


def test_continuous_corroboration_drops_solo_cusum_under_90h():
    rule = ContinuousCorroboration()
    alerts = [_alert("cusum", "2026-02-01T00:00:00Z"),
              _alert("cusum", "2026-02-01T01:00:00Z")]
    assert rule.accepts(alerts) is False


def test_continuous_corroboration_keeps_cusum_mvpca_under_1h():
    rule = ContinuousCorroboration()
    alerts = [_alert("cusum", "2026-02-01T00:00:00Z"),
              _alert("multivariate_pca", "2026-02-01T00:30:00Z")]
    assert rule.accepts(alerts) is True


def test_continuous_corroboration_drops_long_sub_pca_only():
    rule = ContinuousCorroboration()
    alerts = [_alert("sub_pca", "2026-02-01T00:00:00Z"),
              _alert("sub_pca", "2026-02-01T02:00:00Z")]
    # sub_pca window_end - window_start > 1h -> rejected
    assert rule.accepts(alerts) is False


def test_group_alerts_merges_detectors_and_windows():
    alerts = [_alert("cusum", "2026-02-01T00:00:00Z", score=1.0),
              _alert("sub_pca", "2026-02-01T00:30:00Z", score=5.0)]
    merged = group_alerts(alerts)
    assert merged.detector == "cusum+sub_pca"
    assert merged.score == 5.0  # takes highest-score alert
    assert merged.window_start == ts("2026-02-01T00:00:00Z")
    assert merged.window_end == ts("2026-02-01T00:30:00Z")


def test_default_fuser_emits_immediate_state_transition():
    fuser = DefaultAlertFuser(_cfg_bursty(), gap=60*60, max_span=96*3600,
                              anchor_on_non_cusum=False,
                              corroboration=PassThroughCorroboration())
    a = _alert("state_transition", "2026-02-01T00:00:00Z")
    out = fuser.ingest([a])
    assert len(out) == 1
    assert out[0].detector == "state_transition"


def test_default_fuser_buffers_statistical_until_gap():
    fuser = DefaultAlertFuser(_cfg_bursty(), gap=60*60, max_span=96*3600,
                              anchor_on_non_cusum=False,
                              corroboration=PassThroughCorroboration())
    a1 = _alert("cusum", "2026-02-01T00:00:00Z")
    a2 = _alert("sub_pca", "2026-02-01T00:30:00Z")
    a3 = _alert("cusum", "2026-02-01T03:00:00Z")   # gap > 1h -> flushes a1+a2
    out1 = fuser.ingest([a1])
    out2 = fuser.ingest([a2])
    out3 = fuser.ingest([a3])
    assert out1 == [] and out2 == []
    assert len(out3) == 1
    assert out3[0].detector == "cusum+sub_pca"
    # a3 still pending; finalize flushes it
    out_final = fuser.finalize()
    assert len(out_final) == 1
