"""Deployment-style replay animation for a scenario's detection chains.

Reads:
  synthetic-generator/out/<scenario>/events.csv  (timeline bounds only)
  synthetic-generator/out/<scenario>/labels.csv  (GT band overlays)
  out/<scenario>_detections.csv                  (chain stream -> pins)

Writes:
  out/replay_<scenario>.html  (self-contained, ~150-250 KB)

Default scenario is `household_120d`. Override the synth-gen output root via
the SENSORGEN_OUT environment variable (matches scripts/run_all_scenarios.py).
"""
from __future__ import annotations
import argparse, json, os, sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
GEN_ROOT = Path(os.environ.get("SENSORGEN_OUT", ROOT.parent / "synthetic-generator" / "out"))
OUT = ROOT / "out"


# ---------------------------- classification ----------------------------

# Synonym map: system inferred_type -> set of GT anomaly_types it can match.
# Encodes that the system's verdict and the GT label may use different
# vocabulary for the same underlying phenomenon (see spec section 5).
SYNONYMS = {
    "month_shift": {"level_shift", "month_shift"},
    "calibration_drift": {"trend", "calibration_drift"},
    # weekend_anomaly only matches time_of_day if GT target=weekday - handled
    # in code below because it depends on params_json content.
}


def _types_match(inferred: str, gt_type: str, gt_params_json: str) -> bool:
    if inferred == gt_type:
        return True
    if inferred in SYNONYMS and gt_type in SYNONYMS[inferred]:
        return True
    if inferred == "weekend_anomaly" and gt_type == "time_of_day":
        try:
            p = json.loads(gt_params_json) if gt_params_json else {}
        except (ValueError, TypeError):
            p = {}
        return p.get("target") == "weekday"
    return False


def classify_chain(chain, labels_df) -> str:
    """Return 'tp', 'ambiguous', or 'fp' for one chain against all labels.

    chain: dict-like with sensor_id, start, end, inferred_type.
    labels_df: DataFrame with sensor_id, start, end, anomaly_type, params_json.
    """
    same_sensor = labels_df[labels_df["sensor_id"] == chain["sensor_id"]]
    if same_sensor.empty:
        return "fp"
    overlapping = same_sensor[(same_sensor["start"] < chain["end"]) &
                              (same_sensor["end"] > chain["start"])]
    if overlapping.empty:
        return "fp"
    for _, lbl in overlapping.iterrows():
        if _types_match(chain["inferred_type"], lbl["anomaly_type"], lbl.get("params_json", "{}")):
            return "tp"
    return "ambiguous"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--scenario", default="household_120d")
    p.add_argument("--out", type=Path, default=None,
                   help="HTML output path (default: out/replay_<scenario>.html)")
    p.add_argument("--duration-sec", type=int, default=60,
                   help="Wall-clock seconds for full timeline at 1x speed")
    args = p.parse_args()

    events_csv = GEN_ROOT / args.scenario / "events.csv"
    labels_csv = GEN_ROOT / args.scenario / "labels.csv"
    det_csv    = OUT / f"{args.scenario}_detections.csv"
    for f in (events_csv, labels_csv, det_csv):
        if not f.exists():
            print(f"ERROR: missing {f}", file=sys.stderr)
            return 1

    out_path = args.out or OUT / f"replay_{args.scenario}.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    payload = build_payload(events_csv, labels_csv, det_csv, args.scenario, args.duration_sec)
    html = render_html(payload)
    out_path.write_text(html, encoding="utf-8")
    print(f"wrote {out_path} ({out_path.stat().st_size // 1024} KB, {len(payload['chains'])} chains)")
    return 0


# ----------------------------- payload shaping -----------------------------


SPARKLINE_BUCKETS = 600  # ~1 sample per 4.8h for 120d span


def _ts_ms(s) -> int:
    """Convert a timestamp-like value to integer epoch milliseconds (UTC)."""
    if isinstance(s, pd.Timestamp):
        return int(s.timestamp() * 1000)
    return int(pd.Timestamp(s, tz="UTC").timestamp() * 1000)


def _build_sparklines(events_csv, sensor_ids, timeline_start_ms, timeline_end_ms):
    """Return {sensor_id: {"y": [...], "outliers": [...]}}.

    y: 600-element list, each in [0,1] or None for empty buckets (per-sensor normalized).
    outliers: 600-element list of bools, True where bucket value > 3*MAD from sensor median.
    """
    df = pd.read_csv(events_csv, usecols=["timestamp", "sensor_id", "value"])
    df = df[df["sensor_id"].isin(sensor_ids)].copy()
    # ISO8601 sometimes lands as us-precision in pandas 2.x; force ns so the
    # int64 cast below has a known scale.
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True, format="ISO8601").dt.as_unit("ns")
    df["ts_ms"] = df["timestamp"].astype("int64") // 1_000_000  # ns -> ms

    span_ms = max(1, timeline_end_ms - timeline_start_ms)
    bucket_ms = span_ms / SPARKLINE_BUCKETS
    df["bucket"] = ((df["ts_ms"] - timeline_start_ms) / bucket_ms).astype(int).clip(0, SPARKLINE_BUCKETS - 1)

    out = {}
    for sensor_id, sg in df.groupby("sensor_id"):
        bmean = sg.groupby("bucket")["value"].mean()
        y_raw = [None] * SPARKLINE_BUCKETS
        for b, v in bmean.items():
            y_raw[int(b)] = float(v)

        # Outlier rule: bucket mean is in the top 5% of |bucket - bucket_median|.
        # MAD-based 3-sigma fails on bimodal sensors (TV/fridge: idle vs on),
        # where MAD collapses to ~0 and any non-idle reading flags. The
        # percentile-of-deviations rule is distribution-shape-agnostic and
        # always flags a bounded ~5% of buckets, regardless of sensor type.
        valid = [y for y in y_raw if y is not None]
        if len(valid) >= 20:
            bucket_med = sorted(valid)[len(valid) // 2]
            deltas = sorted(abs(y - bucket_med) for y in valid)
            p95_delta = deltas[int(0.95 * len(deltas))]
            outliers = [
                (y is not None and p95_delta > 0 and abs(y - bucket_med) > p95_delta)
                for y in y_raw
            ]
        else:
            outliers = [False] * SPARKLINE_BUCKETS

        # Normalize y to [0,1] per sensor
        valid = [y for y in y_raw if y is not None]
        if valid:
            lo, hi = min(valid), max(valid)
            rng = max(1e-9, hi - lo)
            ynorm = [None if y is None else round((y - lo) / rng, 4) for y in y_raw]
        else:
            ynorm = [None] * SPARKLINE_BUCKETS
        out[sensor_id] = {"y": ynorm, "outliers": outliers}
    return out


def build_payload(events_csv, labels_csv, det_csv, scenario, duration_sec):
    # Timeline bounds from events.csv (cheapest read possible)
    ts = pd.read_csv(events_csv, usecols=["timestamp"])["timestamp"]
    ts = pd.to_datetime(ts, utc=True, format="ISO8601")
    timeline_start_ms = _ts_ms(ts.min())
    timeline_end_ms   = _ts_ms(ts.max())

    # Labels: parse start/end as UTC, keep params_json for synonym lookup
    labels = pd.read_csv(labels_csv)
    if not labels.empty:
        labels["start"] = pd.to_datetime(labels["start"], utc=True, format="ISO8601")
        labels["end"]   = pd.to_datetime(labels["end"],   utc=True, format="ISO8601")

    # Detections: parse times, classify each chain
    dets = pd.read_csv(det_csv)
    for col in ("start", "end", "first_fire_ts"):
        dets[col] = pd.to_datetime(dets[col], utc=True, format="ISO8601")
    dets["classification"] = [classify_chain(r, labels) for _, r in dets.iterrows()]

    # Sensor inventory: only sensors with chains, ordered by count desc, tie-break alpha
    counts = dets.groupby("sensor_id").size().reset_index(name="n")
    counts = counts.sort_values(["n", "sensor_id"], ascending=[False, True])
    sensors = [{"id": row["sensor_id"], "chain_count": int(row["n"])}
               for _, row in counts.iterrows()]

    # Sparkline (downsampled signal + outlier flags) per lane
    sparklines = _build_sparklines(events_csv, [s["id"] for s in sensors],
                                    timeline_start_ms, timeline_end_ms)
    for s in sensors:
        s["sparkline"] = sparklines.get(
            s["id"], {"y": [None]*SPARKLINE_BUCKETS, "outliers": [False]*SPARKLINE_BUCKETS})

    chains = [{
        "sensor_id": r["sensor_id"],
        "fire_ts_ms": _ts_ms(r["first_fire_ts"]),
        "start_ms": _ts_ms(r["start"]),
        "end_ms":   _ts_ms(r["end"]),
        "inferred_type": r["inferred_type"],
        "score": float(r["score"]) if pd.notna(r["score"]) else 0.0,
        "classification": r["classification"],
    } for _, r in dets.iterrows()]

    label_payload = [{
        "sensor_id": r["sensor_id"],
        "anomaly_type": r["anomaly_type"],
        "start_ms": _ts_ms(r["start"]),
        "end_ms":   _ts_ms(r["end"]),
    } for _, r in labels.iterrows()] if not labels.empty else []

    return {
        "scenario": scenario,
        "duration_sec": duration_sec,
        "timeline_start_ms": timeline_start_ms,
        "timeline_end_ms":   timeline_end_ms,
        "sensors": sensors,
        "labels":  label_payload,
        "chains":  chains,
    }


# --------------------------------- render ---------------------------------

# Type-name -> short label inside pin (spec section 4.5).
TYPE_ABBREV = {
    "level_shift": "lvl",
    "time_of_day": "tod",
    "weekend_anomaly": "wkend",
    "month_shift": "month",
    "trend": "trend",
    "calibration_drift": "drift",
    "frequency_change": "freq",
    "water_leak_sustained": "leak",
    "extreme_value": "spike",
    "dropout": "drop",
    "usage_anomaly": "usage",
}

# Per-type GT band tints (alpha applied in CSS via rgba()).
GT_BAND_RGB = {
    "level_shift": "62,197,184",
    "month_shift": "62,197,184",
    "trend": "120,160,220",
    "time_of_day": "100,140,210",
    "weekend_anomaly": "170,130,210",
    "water_leak_sustained": "210,90,90",
    "frequency_change": "200,170,90",
    "extreme_value": "210,140,90",
    "dropout": "150,150,150",
}
DEFAULT_GT_RGB = "150,150,150"


def render_html(payload):
    # Inject abbreviation + tint maps so JS doesn't have to duplicate them.
    payload = dict(payload)
    payload["type_abbrev"] = TYPE_ABBREV
    payload["gt_band_rgb"] = GT_BAND_RGB
    payload["default_gt_rgb"] = DEFAULT_GT_RGB

    payload_json = json.dumps(payload, separators=(",", ":"))
    return (TEMPLATE
            .replace("__PAYLOAD_JSON__", payload_json)
            .replace("__SCENARIO__", payload["scenario"]))


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>__SCENARIO__ - anomaly replay</title>
<style>
  :root {
    --bg: #0f1419;
    --surface: #1a1f26;
    --surface-2: #232932;
    --text: #d8dde6;
    --muted: #7a8290;
    --tp: #3ec5b8;
    --fp: #e0a050;
    --amb: #5a6068;
    --burst: #e0a050;
  }
  * { box-sizing: border-box; }
  html, body {
    margin: 0; padding: 0;
    background: var(--bg); color: var(--text);
    font: 14px/1.4 system-ui, -apple-system, "Segoe UI", Inter, sans-serif;
    height: 100vh; overflow: hidden;
  }
  .app { display: flex; flex-direction: column; height: 100vh; padding: 18px 24px; gap: 14px; }

  /* Header */
  .header { display: flex; align-items: center; gap: 24px; }
  .scenario { font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--muted); }
  .clock {
    font-family: ui-monospace, "SF Mono", Menlo, monospace;
    font-size: 28px; font-weight: 500; color: var(--text);
    flex: 1;
  }
  .controls { display: flex; gap: 6px; align-items: center; }
  .btn {
    background: var(--surface); border: 1px solid #2a313c; color: var(--text);
    padding: 6px 12px; border-radius: 6px; cursor: pointer;
    font: inherit; font-size: 13px;
    transition: background 120ms ease, border-color 120ms ease;
  }
  .btn:hover { background: var(--surface-2); border-color: #3a414c; }
  .btn.active { background: var(--tp); color: #0a1316; border-color: var(--tp); }

  /* Counter row */
  .counters { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
  .tile {
    background: var(--surface); border-radius: 8px; padding: 14px 16px;
    border: 1px solid #232932;
  }
  .tile-label {
    font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase;
    color: var(--muted); margin-bottom: 8px;
  }
  .tile-value {
    font-size: 22px; font-weight: 500;
    transition: color 200ms ease;
  }
  .tile-sub { font-size: 12px; color: var(--muted); margin-top: 4px; }
  .typemix {
    display: flex; height: 18px; border-radius: 3px; overflow: hidden;
    background: #232932;
  }
  .typemix-seg { transition: width 200ms ease; }
  .typemix-legend { display: flex; flex-wrap: wrap; gap: 8px 14px; margin-top: 8px; font-size: 11px; color: var(--muted); }
  .typemix-legend-dot {
    display: inline-block; width: 8px; height: 8px; border-radius: 2px; margin-right: 5px; vertical-align: middle;
  }

  /* Burst banner */
  .burst {
    background: rgba(224,160,80,0.10); border: 1px solid rgba(224,160,80,0.35);
    color: var(--burst); padding: 10px 14px; border-radius: 6px;
    font-size: 13px; opacity: 0;
    transition: opacity 280ms ease;
    box-shadow: 0 0 0 0 rgba(224,160,80,0.0);
  }
  .burst.active { opacity: 1; box-shadow: 0 0 24px -4px rgba(224,160,80,0.4); }

  /* Lanes */
  .lanes { flex: 1; display: flex; flex-direction: column; gap: 6px; min-height: 0; }
  .lane {
    position: relative; height: 56px; background: var(--surface);
    border-radius: 6px; border: 1px solid #232932; overflow: hidden;
  }
  .lane-name {
    position: absolute; left: 12px; top: 50%; transform: translateY(-50%);
    font-size: 12px; color: var(--muted);
    z-index: 3; pointer-events: none;
    text-shadow: 0 0 6px var(--surface), 0 0 6px var(--surface);
  }
  .lane-track {
    position: absolute; left: 160px; right: 12px; top: 0; bottom: 0;
  }
  .gt-band {
    position: absolute; top: 6px; bottom: 6px;
    border-radius: 3px;
    transition: opacity 180ms ease;
    z-index: 1;
  }
  .lanes.no-gt .gt-band { opacity: 0; }

  .sparkline {
    position: absolute; left: 0; right: 0; top: 0; bottom: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
  }

  .pin {
    position: absolute; top: 50%; transform: translate(-50%, -50%) scale(0.7);
    background: var(--amb); color: #0a1316;
    font-size: 10px; font-weight: 600;
    padding: 3px 7px; border-radius: 9px;
    opacity: 0;
    transition: opacity 200ms ease, transform 200ms ease;
    white-space: nowrap;
    z-index: 2;
    display: flex; align-items: center; gap: 4px;
  }
  .pin.shown { opacity: 1; transform: translate(-50%, -50%) scale(1.0); }
  .pin.tp  { background: var(--tp); }
  .pin.fp  { background: var(--fp); }
  .pin.amb { background: var(--amb); color: #d8dde6; }
  .pin .score-bar {
    width: 2px; background: rgba(0,0,0,0.35);
    align-self: stretch; margin-left: 2px; border-radius: 1px;
  }

  .cursor {
    position: absolute; top: 0; bottom: 0; width: 1.5px;
    background: rgba(216,221,230,0.5); pointer-events: none; z-index: 4;
    box-shadow: 0 0 6px rgba(216,221,230,0.3);
  }
  .axis {
    position: absolute; left: 160px; right: 12px; bottom: 0; height: 18px;
    color: var(--muted); font-size: 10px;
    pointer-events: none;
  }
  .axis-tick { position: absolute; transform: translateX(-50%); }
  .axis-tick::before {
    content: ""; position: absolute; top: -3px; left: 50%; width: 1px; height: 4px;
    background: rgba(122,130,144,0.5);
  }

  .tooltip {
    position: fixed; pointer-events: none; z-index: 100;
    background: #0a1014; border: 1px solid #2a313c; border-radius: 6px;
    padding: 10px 12px; font-size: 12px; color: var(--text);
    opacity: 0; transition: opacity 100ms ease;
    max-width: 280px;
  }
  .tooltip.shown { opacity: 1; }
  .tooltip-row { margin: 2px 0; }
  .tooltip-key { color: var(--muted); margin-right: 8px; }
</style>
</head>
<body>
<div class="app">
  <div class="header">
    <div>
      <div class="scenario" id="scenario"></div>
      <div class="clock" id="clock">--:--</div>
    </div>
    <div style="flex:1"></div>
    <div class="controls">
      <button class="btn" id="play-btn">&#9654; play</button>
      <button class="btn" data-speed="0.5">&frac12;&times;</button>
      <button class="btn active" data-speed="1">1&times;</button>
      <button class="btn" data-speed="2">2&times;</button>
      <button class="btn" data-speed="4">4&times;</button>
      <button class="btn" id="gt-btn">GT bands &check;</button>
    </div>
  </div>

  <div class="counters">
    <div class="tile">
      <div class="tile-label">Alerts / day (7-day rolling)</div>
      <div class="tile-value" id="t-rate">0.0</div>
    </div>
    <div class="tile">
      <div class="tile-label">Type mix</div>
      <div class="typemix" id="t-mix"></div>
      <div class="typemix-legend" id="t-legend"></div>
    </div>
    <div class="tile">
      <div class="tile-label">Hottest sensor (24h)</div>
      <div class="tile-value" id="t-hot" style="font-size:16px">&mdash;</div>
      <div class="tile-sub" id="t-hot-sub"></div>
    </div>
  </div>

  <div class="burst" id="burst"></div>

  <div class="lanes" id="lanes"></div>
  <div id="tooltip" class="tooltip"></div>
</div>

<script>
const PAYLOAD = __PAYLOAD_JSON__;

// ---------- state ----------
const state = {
  now_ms: PAYLOAD.timeline_start_ms,
  speed: 1.0,
  paused: true,
  gt_visible: true,
  last_frame_t: null,
};

const TIMELINE_MS = PAYLOAD.timeline_end_ms - PAYLOAD.timeline_start_ms;
const TYPE_PALETTE = ["#3ec5b8","#7da6e0","#aa82d2","#e0a050","#d25a5a","#c8a850","#5a6068"];

// Pre-sort chains by fire_ts so we can advance a cursor instead of filtering each frame.
const CHAINS = [...PAYLOAD.chains].sort((a,b) => a.fire_ts_ms - b.fire_ts_ms);
let nextChainIdx = 0;

// Counters tracked incrementally as chains are emitted.
const emittedSoFar = [];
const typeCounts = {};

// ---------- DOM build ----------
const lanesEl = document.getElementById("lanes");
const tooltipEl = document.getElementById("tooltip");
document.getElementById("scenario").textContent = PAYLOAD.scenario;

const laneEls = {};   // sensor_id -> {root, track}
PAYLOAD.sensors.forEach(s => {
  const lane = document.createElement("div");
  lane.className = "lane";
  lane.innerHTML =
    `<div class="lane-name">${s.id}</div>
     <div class="lane-track" data-sensor="${s.id}"></div>`;
  lanesEl.appendChild(lane);
  laneEls[s.id] = { root: lane, track: lane.querySelector(".lane-track") };
  buildSparkline(s, laneEls[s.id].track);
});

function buildSparkline(sensor, track) {
  const sl = sensor.sparkline;
  if (!sl || !sl.y) return;
  const N = sl.y.length;
  const W = 1000, H = 100;
  const TOP_PAD = 14, BOT_PAD = 8;
  const drawY = v => v == null ? null : TOP_PAD + (1 - v) * (H - TOP_PAD - BOT_PAD);
  const svgNS = "http://www.w3.org/2000/svg";
  const svg = document.createElementNS(svgNS, "svg");
  svg.setAttribute("class", "sparkline");
  svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
  svg.setAttribute("preserveAspectRatio", "none");

  // Outlier columns first (so they sit behind the line within the SVG)
  let rectsSvg = "";
  for (let i = 0; i < N; i++) {
    if (sl.outliers[i]) {
      const x = (i / N) * W;
      const w = Math.max(W / N, 1.2);
      rectsSvg += `<rect x="${x.toFixed(2)}" y="2" width="${w.toFixed(2)}" height="${H-4}" fill="rgba(224,160,80,0.22)"/>`;
    }
  }
  // Build line path; break on null buckets
  const segs = [];
  let started = false;
  for (let i = 0; i < N; i++) {
    const yv = drawY(sl.y[i]);
    if (yv == null) { started = false; continue; }
    const x = (i / N) * W;
    segs.push(`${started ? "L" : "M"}${x.toFixed(2)} ${yv.toFixed(2)}`);
    started = true;
  }
  svg.innerHTML = rectsSvg +
    `<path d="${segs.join(" ")}" fill="none" stroke="rgba(216,221,230,0.32)" stroke-width="1" vector-effect="non-scaling-stroke"/>`;
  track.appendChild(svg);
}

// Add an axis row at the bottom of the lanes column
const axis = document.createElement("div");
axis.style.position = "relative";
axis.style.height = "20px";
axis.innerHTML = `<div class="axis" id="axis"></div>`;
lanesEl.appendChild(axis);
buildAxisTicks();

// GT band rendering (build once; visibility toggled via container class)
PAYLOAD.labels.forEach(lbl => {
  const lane = laneEls[lbl.sensor_id];
  if (!lane) return;
  const band = document.createElement("div");
  band.className = "gt-band";
  const rgb = PAYLOAD.gt_band_rgb[lbl.anomaly_type] || PAYLOAD.default_gt_rgb;
  band.style.background = `rgba(${rgb},0.18)`;
  band.style.borderLeft  = `1px dashed rgba(${rgb},0.5)`;
  band.style.borderRight = `1px dashed rgba(${rgb},0.5)`;
  band.style.left  = pctOf(lbl.start_ms) + "%";
  band.style.width = (pctOf(lbl.end_ms) - pctOf(lbl.start_ms)) + "%";
  lane.track.appendChild(band);
});

// One cursor per lane track so it spans the full lane height.
const cursorEls = [];
Object.values(laneEls).forEach(({track}) => {
  const c = document.createElement("div");
  c.className = "cursor";
  track.appendChild(c);
  cursorEls.push(c);
});

function pctOf(ms) {
  return ((ms - PAYLOAD.timeline_start_ms) / TIMELINE_MS) * 100;
}

function buildAxisTicks() {
  const axisEl = document.getElementById("axis");
  const spanDays = TIMELINE_MS / 86400000;
  let stepMs, fmt;
  if (spanDays > 60) { stepMs = 30*86400000; fmt = (d) => d.toLocaleString("en-US", {month:"short"}); }
  else if (spanDays > 21) { stepMs = 7*86400000; fmt = (d) => `${d.getUTCMonth()+1}/${d.getUTCDate()}`; }
  else { stepMs = 86400000; fmt = (d) => `${d.getUTCMonth()+1}/${d.getUTCDate()}`; }
  for (let t = PAYLOAD.timeline_start_ms; t <= PAYLOAD.timeline_end_ms; t += stepMs) {
    const tick = document.createElement("div");
    tick.className = "axis-tick";
    tick.style.left = pctOf(t) + "%";
    tick.textContent = fmt(new Date(t));
    axisEl.appendChild(tick);
  }
}

// ---------- emission ----------
function emitChain(chain) {
  const lane = laneEls[chain.sensor_id];
  if (!lane) return;
  const pin = document.createElement("div");
  pin.className = `pin ${chain.classification === "tp" ? "tp" :
                          chain.classification === "fp" ? "fp" : "amb"}`;
  const abbrev = PAYLOAD.type_abbrev[chain.inferred_type] || chain.inferred_type;
  const scoreH = Math.max(2, Math.min(14, Math.log10(Math.max(1, chain.score)) * 5));
  pin.innerHTML = `<span>${abbrev}</span><span class="score-bar" style="height:${scoreH}px"></span>`;
  pin.style.left = pctOf(chain.fire_ts_ms) + "%";
  pin.dataset.chain = JSON.stringify(chain);
  pin.addEventListener("mouseenter", showTooltip);
  pin.addEventListener("mouseleave", hideTooltip);
  lane.track.appendChild(pin);
  requestAnimationFrame(() => pin.classList.add("shown"));
  emittedSoFar.push(chain);
  typeCounts[chain.inferred_type] = (typeCounts[chain.inferred_type] || 0) + 1;
}

// ---------- counters ----------
const T_RATE = document.getElementById("t-rate");
const T_MIX  = document.getElementById("t-mix");
const T_LEG  = document.getElementById("t-legend");
const T_HOT  = document.getElementById("t-hot");
const T_HOT_SUB = document.getElementById("t-hot-sub");
const BURST  = document.getElementById("burst");

function updateCounters() {
  // Alerts/day rolling 7d ending at now_ms
  const windowStart = state.now_ms - 7*86400000;
  let n7 = 0;
  for (let i = emittedSoFar.length - 1; i >= 0; i--) {
    if (emittedSoFar[i].fire_ts_ms < windowStart) break;
    n7++;
  }
  const days = Math.max(1, Math.min(7, (state.now_ms - PAYLOAD.timeline_start_ms) / 86400000));
  T_RATE.textContent = (n7 / days).toFixed(1);

  // Type mix
  const types = Object.keys(typeCounts).sort((a,b) => typeCounts[b] - typeCounts[a]);
  const total = types.reduce((s,t) => s + typeCounts[t], 0) || 1;
  T_MIX.innerHTML = "";
  T_LEG.innerHTML = "";
  types.slice(0, 7).forEach((t, i) => {
    const seg = document.createElement("div");
    seg.className = "typemix-seg";
    seg.style.background = TYPE_PALETTE[i] || TYPE_PALETTE[TYPE_PALETTE.length-1];
    seg.style.width = (typeCounts[t] / total * 100) + "%";
    T_MIX.appendChild(seg);
    const li = document.createElement("span");
    li.innerHTML = `<span class="typemix-legend-dot" style="background:${TYPE_PALETTE[i] || TYPE_PALETTE[TYPE_PALETTE.length-1]}"></span>${PAYLOAD.type_abbrev[t]||t} ${typeCounts[t]}`;
    T_LEG.appendChild(li);
  });

  // Hottest sensor in trailing 24h
  const day24 = state.now_ms - 86400000;
  const counts24 = {};
  for (let i = emittedSoFar.length - 1; i >= 0; i--) {
    if (emittedSoFar[i].fire_ts_ms < day24) break;
    counts24[emittedSoFar[i].sensor_id] = (counts24[emittedSoFar[i].sensor_id]||0) + 1;
  }
  const hot = Object.entries(counts24).sort((a,b) => b[1]-a[1])[0];
  if (hot) { T_HOT.textContent = hot[0]; T_HOT_SUB.textContent = `${hot[1]} alerts in last 24h`; }
  else     { T_HOT.textContent = "—";    T_HOT_SUB.textContent = "no alerts in last 24h"; }

  // Burst: any sensor with >=6 chains in last 6h?
  const sixH = state.now_ms - 6*3600000;
  const counts6 = {};
  for (let i = emittedSoFar.length - 1; i >= 0; i--) {
    if (emittedSoFar[i].fire_ts_ms < sixH) break;
    counts6[emittedSoFar[i].sensor_id] = (counts6[emittedSoFar[i].sensor_id]||0) + 1;
  }
  const top = Object.entries(counts6).filter(([_,n]) => n >= 6).sort((a,b) => b[1]-a[1] || a[0].localeCompare(b[0]))[0];
  if (top) {
    BURST.textContent = `⚡ ${top[0]} · ${top[1]} alerts in 6h`;
    BURST.classList.add("active");
  } else {
    BURST.classList.remove("active");
  }
}

// ---------- tooltip ----------
function showTooltip(e) {
  const c = JSON.parse(e.currentTarget.dataset.chain);
  const dStart = new Date(c.start_ms).toISOString().replace("T"," ").slice(0,19);
  const dEnd   = new Date(c.end_ms).toISOString().replace("T"," ").slice(0,19);
  const dFire  = new Date(c.fire_ts_ms).toISOString().replace("T"," ").slice(0,19);
  tooltipEl.innerHTML =
    `<div class="tooltip-row"><span class="tooltip-key">sensor</span>${c.sensor_id}</div>
     <div class="tooltip-row"><span class="tooltip-key">type</span>${c.inferred_type}</div>
     <div class="tooltip-row"><span class="tooltip-key">class</span>${c.classification}</div>
     <div class="tooltip-row"><span class="tooltip-key">score</span>${c.score.toFixed(2)}</div>
     <div class="tooltip-row"><span class="tooltip-key">fired</span>${dFire}</div>
     <div class="tooltip-row"><span class="tooltip-key">window</span>${dStart} → ${dEnd}</div>`;
  tooltipEl.style.left = (e.clientX + 14) + "px";
  tooltipEl.style.top  = (e.clientY + 14) + "px";
  tooltipEl.classList.add("shown");
}
function hideTooltip() { tooltipEl.classList.remove("shown"); }

// ---------- clock + cursor ----------
function updateClock() {
  const d = new Date(state.now_ms);
  document.getElementById("clock").textContent =
    d.toISOString().replace("T", "  ").slice(0,16) + " UTC";
  const pct = pctOf(state.now_ms);
  cursorEls.forEach(c => c.style.left = pct + "%");
}

// ---------- animation loop ----------
function frame(t) {
  if (state.paused) { state.last_frame_t = null; requestAnimationFrame(frame); return; }
  if (state.last_frame_t == null) { state.last_frame_t = t; requestAnimationFrame(frame); return; }
  const dt = t - state.last_frame_t;
  state.last_frame_t = t;
  const tlPerWall = (TIMELINE_MS / (PAYLOAD.duration_sec * 1000)) * state.speed;
  state.now_ms += dt * tlPerWall;
  if (state.now_ms >= PAYLOAD.timeline_end_ms) {
    state.now_ms = PAYLOAD.timeline_end_ms;
    state.paused = true;
    document.getElementById("play-btn").innerHTML = "↻ replay";
  }
  while (nextChainIdx < CHAINS.length && CHAINS[nextChainIdx].fire_ts_ms <= state.now_ms) {
    emitChain(CHAINS[nextChainIdx++]);
  }
  updateClock();
  updateCounters();
  requestAnimationFrame(frame);
}

// ---------- controls ----------
const playBtn = document.getElementById("play-btn");
playBtn.addEventListener("click", () => {
  if (state.now_ms >= PAYLOAD.timeline_end_ms) {
    state.now_ms = PAYLOAD.timeline_start_ms;
    nextChainIdx = 0;
    emittedSoFar.length = 0;
    Object.keys(typeCounts).forEach(k => delete typeCounts[k]);
    Object.values(laneEls).forEach(({track}) => {
      track.querySelectorAll(".pin").forEach(p => p.remove());
    });
  }
  state.paused = !state.paused;
  playBtn.innerHTML = state.paused ? "▶ play" : "❚❚ pause";
});

document.querySelectorAll("[data-speed]").forEach(b => {
  b.addEventListener("click", () => {
    state.speed = parseFloat(b.dataset.speed);
    document.querySelectorAll("[data-speed]").forEach(x => x.classList.remove("active"));
    b.classList.add("active");
  });
});

document.getElementById("gt-btn").addEventListener("click", () => {
  state.gt_visible = !state.gt_visible;
  lanesEl.classList.toggle("no-gt", !state.gt_visible);
  document.getElementById("gt-btn").innerHTML = state.gt_visible ? "GT bands ✓" : "GT bands ✗";
});

// ---------- boot ----------
updateClock();
updateCounters();
requestAnimationFrame(frame);
</script>
</body>
</html>
"""


if __name__ == "__main__":
    sys.exit(main())
