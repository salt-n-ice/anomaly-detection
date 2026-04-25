"""Deterministic explainer layer (package facade).

Re-exports the public API from focused submodules:
- types       : USER_BEHAVIOR_TYPES, SENSOR_FAULT_TYPES, type_to_class
- signals     : Signals, DETECTOR_CLASSES
- classify    : classify_type
- magnitude   : extract_magnitude
- temporal    : temporal_framing
- bundle      : explain
- prompt      : build_prompt
- csv         : explain_detections_csv

The pipeline (`anomaly.pipeline`) calls `classify_type` and `type_to_class`
at detection-write time. The research/explain harness reads bundles via
`explain_detections_csv` and renders prompts via `build_prompt`.
"""
from __future__ import annotations

from .types import USER_BEHAVIOR_TYPES, SENSOR_FAULT_TYPES, type_to_class
from .signals import Signals, DETECTOR_CLASSES
from .classify import classify_type, classify, ClassificationResult
from .magnitude import extract_magnitude
from .temporal import temporal_framing
from .bundle import explain
from .prompt import build_prompt
from .csv import explain_detections_csv, _detections_to_alerts

# `_detections_to_alerts` is not part of the public API but is reached by
# tests (tests/test_explain.py) and viz (src/anomaly/viz.py) — keep it
# exposed via the package facade so existing call sites compile unchanged.

__all__ = [
    "USER_BEHAVIOR_TYPES",
    "SENSOR_FAULT_TYPES",
    "type_to_class",
    "Signals",
    "DETECTOR_CLASSES",
    "classify_type",
    "classify",
    "ClassificationResult",
    "extract_magnitude",
    "temporal_framing",
    "explain",
    "build_prompt",
    "explain_detections_csv",
]
