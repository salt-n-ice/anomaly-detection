"""LLM-based type classifier for the research-loop NAB metric.

Path-C from the session autopsy: instead of a feature-based ML classifier
that caps at ~0.61 weighted F1 on this data (because `mains_voltage`
long CUSUM/RecentShift fires during `calibration_drift` and `month_shift`
are feature-indistinguishable), pass the detection bundle to Claude and
let it apply world-knowledge priors — "voltage shifts are calibration
faults", "appliance shifts are user behavior", etc.

Output is the `llm_inferred_type` column, consumed by `nab_metric.py`
through `apply_type_classifier.py`'s `ml_inferred_type` channel. This is
research-loop only — production `src/anomaly/explain.py::classify_type`
stays rule-based until the LLM explainer is designed (see
`ITERATIONS.md` discussion on Plan A vs Plan B).

Cost / latency:
- Model: `claude-haiku-4-5` (fast, $1/$5 per 1M tokens).
- Explicit-type rows (DQG, state_transition) pass through without an
  LLM call — only fused-detector chains hit the API.
- Per-detection deterministic-hash cache → each distinct detection
  signature costs one call across all iterations.
- Prompt caching on the system prompt → 90% discount on stable prefix
  within a 5-minute window.

Usage (as a module):

    from llm_classifier import apply_llm_classifier
    out = apply_llm_classifier(det_df, scenario_name="household_60d")

Usage (CLI, classifies a detection CSV and writes a new one):

    python research/llm_classifier.py \\
        --detections out/household_60d_detections.csv \\
        --out out/household_60d_detections_llm.csv \\
        --scenario household_60d
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

import anthropic
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "research"))

from anomaly.explain import USER_BEHAVIOR_TYPES, SENSOR_FAULT_TYPES  # noqa: E402

CACHE_DIR = ROOT / "research" / "llm_cache"
CACHE_DIR.mkdir(exist_ok=True)

CLASSIFIER_MODEL = "claude-haiku-4-5"

# Types DQG / state_transition set explicitly — pass through, don't ask LLM.
EXPLICIT_TYPES: frozenset[str] = frozenset({
    "out_of_range", "saturation", "stuck_at", "dropout", "clock_drift",
    "batch_arrival", "duplicate_stale", "reporting_rate_change",
    "extreme_value",
    "water_leak_sustained", "unusual_occupancy",
})

# Full label vocabulary — union of user_behavior + sensor_fault + the
# `statistical_anomaly` unknown-fallback. Must align with the NAB metric's
# per-type semantics in `anomaly_semantics.py`.
ALLOWED_TYPES: list[str] = sorted(
    USER_BEHAVIOR_TYPES | SENSOR_FAULT_TYPES | {"statistical_anomaly"}
)

SYSTEM_PROMPT = """You classify anomaly detections in a household sensor pipeline.

You will receive a JSON bundle describing one fused detection: sensor, timing, detector combination that fired, and signal context. Pick the single most likely anomaly type from the provided list.

Domain priors (apply these; they are reliable on this dataset):

- `mains_voltage` shifts are almost always `calibration_drift` (sensor_fault). A `month_shift` is possible but rare and signals a seasonal voltage change; do NOT default to it unless the detection window aligns with a month boundary AND the shift is modest (~1-2V).
- `basement_temp`:
  - Brief (< 24h) temperature dips or spikes → `dip` / `spike` (user_behavior, e.g. brief cold exposure).
  - Sustained (multi-day) bias → `calibration_drift` (sensor_fault).
- `outlet_*_power` (fridge, kettle, tv):
  - Sudden sustained offset → `level_shift` (user_behavior — appliance reconfigured).
  - Slow multi-day ramp → `trend` (user_behavior — appliance decline).
  - Very slow (week+) ramp → `degradation_trajectory` (user_behavior — appliance EOL).
  - Pattern deviation at specific hours → `time_of_day` or `weekend_anomaly`.
  - Sinusoidal / oscillation → `frequency_change`.
- Motion sensors (`bedroom_motion`, `utility_motion`): triggers fire on occupancy. Unusual timing → `unusual_occupancy`. Stuck-ON → `stuck_at` (sensor_fault).
- Water sensors: sustained ON → `water_leak_sustained`.

When truly ambiguous (e.g. a cusum-only chain with no distinguishing signal, a very short multi-detector burst without clear shape), return `statistical_anomaly`.

Respond with ONLY JSON matching the schema: {"type": "<one of the allowed types>", "confidence": <0.0-1.0>, "reasoning": "<one sentence>"}."""


def _stable_bundle(row: pd.Series) -> dict:
    """Extract the fields the LLM will see. Deterministic — same input row
    produces byte-identical JSON, so cache keys are stable across runs.

    Detection CSV columns (see `pipeline.py::_write_detections`) are
    `start`, `end`, `first_fire_ts` — NOT `window_start` / `window_end`.
    """
    w0 = pd.Timestamp(row["start"])
    w1 = pd.Timestamp(row["end"])
    ff = pd.Timestamp(row["first_fire_ts"]) if pd.notna(row.get("first_fire_ts")) else w0
    dur_s = max(0.0, (w1 - w0).total_seconds())

    return {
        "sensor_id":       str(row["sensor_id"]),
        "capability":      str(row["capability"]),
        "detector_set":    sorted(str(row["detector"]).split("+")),
        "window_start":    w0.isoformat(),
        "window_end":      w1.isoformat(),
        "first_fire_ts":   ff.isoformat(),
        "duration_hours":  round(dur_s / 3600, 3),
        "first_fire_hour": ff.hour,
        "first_fire_dow":  ff.dayofweek,
        "first_fire_month": ff.month,
        "score":           round(float(row.get("score", 0.0)), 4),
        # `threshold` is emitted into the Alert but not into the CSV; default 0.
        "threshold":       round(float(row.get("threshold", 0.0)), 4) if "threshold" in row else 0.0,
    }


def _cache_key(bundle: dict) -> str:
    payload = json.dumps(bundle, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:20]


def _classify_once(client: anthropic.Anthropic, bundle: dict) -> dict:
    """Single LLM call, no caching."""
    user_msg = json.dumps(bundle, indent=2)
    resp = client.messages.create(
        model=CLASSIFIER_MODEL,
        max_tokens=512,
        system=[
            {"type": "text", "text": SYSTEM_PROMPT,
             "cache_control": {"type": "ephemeral"}},
        ],
        messages=[{"role": "user", "content": user_msg}],
        output_config={
            "format": {
                "type": "json_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "type":       {"type": "string", "enum": ALLOWED_TYPES},
                        "confidence": {"type": "number"},
                        "reasoning":  {"type": "string"},
                    },
                    "required": ["type", "confidence", "reasoning"],
                    "additionalProperties": False,
                }
            }
        },
    )
    text = next(b.text for b in resp.content if b.type == "text")
    out = json.loads(text)
    # Sanity clamp
    if out["type"] not in ALLOWED_TYPES:
        out["type"] = "statistical_anomaly"
    return out


def classify_detection(
    client: anthropic.Anthropic,
    bundle: dict,
    retries: int = 3,
) -> dict:
    """Classify one detection. Uses local disk cache — same bundle returns
    byte-identical result across runs without re-calling the LLM."""
    key = _cache_key(bundle)
    cached = CACHE_DIR / f"{key}.json"
    if cached.exists():
        try:
            return json.loads(cached.read_text())
        except json.JSONDecodeError:
            cached.unlink()  # corrupted cache; refetch

    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            result = _classify_once(client, bundle)
            cached.write_text(json.dumps(result))
            return result
        except (anthropic.RateLimitError, anthropic.APIStatusError) as e:
            last_err = e
            if isinstance(e, anthropic.RateLimitError) or (
                isinstance(e, anthropic.APIStatusError) and e.status_code >= 500
            ):
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError(f"classifier failed after {retries} retries: {last_err}")


def apply_llm_classifier(
    det_df: pd.DataFrame,
    scenario_name: str = "",
    verbose: bool = True,
) -> pd.DataFrame:
    """Add `llm_inferred_type` column to a detections DataFrame."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError(
            "ANTHROPIC_API_KEY not set — export it before running "
            "`python research/llm_classifier.py ...`."
        )
    client = anthropic.Anthropic()

    out = det_df.copy()
    llm_types: list[str] = []
    llm_confidence: list[float] = []
    ncached = ncalled = nskipped = 0
    total = len(out)

    for i, row in out.iterrows():
        itype = str(row.get("inferred_type", ""))
        if itype in EXPLICIT_TYPES:
            llm_types.append(itype)
            llm_confidence.append(1.0)
            nskipped += 1
            continue

        bundle = _stable_bundle(row)
        key = _cache_key(bundle)
        if (CACHE_DIR / f"{key}.json").exists():
            ncached += 1
        else:
            ncalled += 1

        if verbose and (ncached + ncalled + nskipped) % 50 == 0:
            print(f"  [{scenario_name}] {ncached + ncalled + nskipped}/{total}"
                  f"  cached={ncached} called={ncalled} skipped={nskipped}",
                  flush=True)

        try:
            result = classify_detection(client, bundle)
        except Exception as e:
            print(f"  [{scenario_name}] error on row {i}: {e}", flush=True)
            result = {"type": "statistical_anomaly",
                       "confidence": 0.0, "reasoning": f"error: {e}"}
        llm_types.append(result["type"])
        llm_confidence.append(float(result.get("confidence", 0.0)))

    out["llm_inferred_type"] = llm_types
    out["llm_confidence"] = llm_confidence
    if verbose:
        print(f"  [{scenario_name}] done: {ncached} cached, {ncalled} called, "
              f"{nskipped} skipped (explicit)")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--detections", type=Path, required=True)
    ap.add_argument("--out",        type=Path, required=True)
    ap.add_argument("--scenario",   default="")
    args = ap.parse_args()
    df = pd.read_csv(args.detections)
    out = apply_llm_classifier(df, scenario_name=args.scenario)
    out.to_csv(args.out, index=False)
    print(f"wrote {len(out)} rows to {args.out}")


if __name__ == "__main__":
    main()
