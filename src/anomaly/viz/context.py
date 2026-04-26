"""Per-scenario data bag built once before any page renders.

Centralizes filtering (excluded sensors), classification (TP/FN/user-visible
FP/suppressed), best-chain selection, friendly-name resolution, and counts.
Page renderers consume this read-only object.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import pandas as pd

from . import style
from . import selection


@dataclass(frozen=True)
class Context:
    events: dict[str, pd.DataFrame]              # sensor_id -> events df
    sensor_capability: dict[str, str]            # sensor_id -> capability
    labels: pd.DataFrame                         # with is_tp, best_chain_idx
    detections: pd.DataFrame                     # parsed UTC, classified
    scenario_start: pd.Timestamp
    scenario_end: pd.Timestamp
    title: str
    eyebrow: str
    n_tp: int
    n_fn: int
    n_total_labels: int
    n_user_visible_fps: int
    n_suppressed: int
    suppression_by_sensor: list[tuple[str, int]]  # (sensor_id, count) desc
    sensor_friendly: dict[str, str]              # resolver: id -> friendly
    excluded_sensors: frozenset[str]

    @staticmethod
    def build(events: pd.DataFrame, labels: pd.DataFrame,
              detections: pd.DataFrame, *,
              sensor_names: dict[str, str] | None = None,
              excluded_sensors: frozenset[str] = frozenset(),
              title: str | None = None,
              source_path: Path | None = None) -> "Context":
        sensor_names = sensor_names or {}
        events = events.copy()
        events["timestamp"] = pd.to_datetime(events["timestamp"], utc=True,
                                             format="ISO8601")
        labels = labels.copy()
        labels["start"] = pd.to_datetime(labels["start"], utc=True,
                                         format="ISO8601")
        labels["end"] = pd.to_datetime(labels["end"], utc=True,
                                       format="ISO8601")
        detections = detections.copy()
        detections["start"] = pd.to_datetime(detections["start"], utc=True,
                                             format="ISO8601")
        detections["end"] = pd.to_datetime(detections["end"], utc=True,
                                           format="ISO8601")
        if "first_fire_ts" in detections.columns:
            detections["first_fire_ts"] = pd.to_datetime(
                detections["first_fire_ts"], utc=True, format="ISO8601")

        # Apply excluded-sensors filter
        if excluded_sensors:
            events = events[~events["sensor_id"].isin(excluded_sensors)]
            labels = labels[~labels["sensor_id"].isin(excluded_sensors)]
            detections = detections[~detections["sensor_id"].isin(excluded_sensors)]

        # Group events by sensor for fast page-time lookup
        events_by_sensor: dict[str, pd.DataFrame] = {
            sid: g.reset_index(drop=True)
            for sid, g in events.groupby("sensor_id")
        }
        sensor_capability: dict[str, str] = {}
        for sid, g in events.groupby("sensor_id"):
            caps = g["capability"].dropna().unique()
            sensor_capability[sid] = caps[0] if len(caps) else ""

        # Classify TP/FN per label
        labels = selection.classify_labels(labels, detections)

        # Best chain per TP label
        labels = selection.attach_best_chain(labels, detections)

        # User-visible FP and suppressed counts
        n_user_fps, n_suppressed, suppression_by_sensor = (
            selection.compute_buckets(labels, detections)
        )

        # Friendly-name resolver (precomputed for all sensors in events)
        friendly_map = {sid: style.sensor_friendly(sid, sensor_names)
                        for sid in events_by_sensor.keys()}

        # Title
        scen_start = events["timestamp"].min()
        scen_end = events["timestamp"].max()
        scenario_name = None
        if source_path is not None:
            scenario_name = Path(source_path).parent.name
        eyebrow = style.format_eyebrow(scen_start, scen_end, scenario_name)
        if title is None:
            title = scenario_name or "anomaly detection report"

        n_total = int(len(labels))
        n_tp = int(labels["is_tp"].sum()) if n_total else 0
        n_fn = n_total - n_tp

        return Context(
            events=events_by_sensor,
            sensor_capability=sensor_capability,
            labels=labels.reset_index(drop=True),
            detections=detections.reset_index(drop=True),
            scenario_start=scen_start,
            scenario_end=scen_end,
            title=title,
            eyebrow=eyebrow,
            n_tp=n_tp,
            n_fn=n_fn,
            n_total_labels=n_total,
            n_user_visible_fps=n_user_fps,
            n_suppressed=n_suppressed,
            suppression_by_sensor=suppression_by_sensor,
            sensor_friendly=friendly_map,
            excluded_sensors=excluded_sensors,
        )
