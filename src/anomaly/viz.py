from __future__ import annotations
from pathlib import Path
from typing import Iterator
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Patch
from .metrics import Interval, _overlaps

_LINE = "#1a1a1a"
_TRUTH = "#d62828"
_DETECT = "#1565c0"
_GRID = "#ececec"
_MUTED = "#888888"
_TEXT = "#222222"
_LANE_BG = "#fafafa"


def _windows(start: pd.Timestamp, end: pd.Timestamp,
             width: pd.Timedelta) -> Iterator[tuple[pd.Timestamp, pd.Timestamp]]:
    t = start
    while t < end:
        yield t, min(t + width, end)
        t = t + width


def _classify(gt: list[Interval], det: list[Interval]):
    tp_gt = [g for g in gt if any(_overlaps(g, d) for d in det)]
    fn = [g for g in gt if g not in tp_gt]
    tp_det = [d for d in det if any(_overlaps(g, d) for g in gt)]
    fp = [d for d in det if d not in tp_det]
    return tp_gt, fn, fp


def _load(df: pd.DataFrame) -> list[Interval]:
    if df is None or len(df) == 0: return []
    out = []
    for r in df.itertuples(index=False):
        out.append(Interval(r.sensor_id,
                            pd.Timestamp(r.start) if not isinstance(r.start, pd.Timestamp) else r.start,
                            pd.Timestamp(r.end) if not isinstance(r.end, pd.Timestamp) else r.end,
                            getattr(r, "anomaly_type", "")))
    return out


def _style() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": "#cccccc",
        "axes.linewidth": 0.6,
        "axes.labelcolor": _TEXT,
        "xtick.color": _MUTED,
        "ytick.color": _MUTED,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
    })


def _strip(ax) -> None:
    ax.set_yticks([])
    ax.set_xticks([])
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)
    ax.set_facecolor(_LANE_BG)


def _gantt(ax, intervals: list[Interval], w0, w1, color: str,
           empty_label: str, max_rows: int = 8) -> None:
    groups: dict[str, list[Interval]] = {}
    for iv in intervals:
        groups.setdefault(iv.anomaly_type or "—", []).append(iv)
    if not groups:
        ax.text(0.5, 0.5, empty_label, transform=ax.transAxes,
                fontsize=7, color="#bbbbbb", ha="center", va="center",
                style="italic")
        return
    ranked = sorted(groups.items(),
                    key=lambda kv: -sum((iv.end - iv.start).total_seconds()
                                        for iv in kv[1]))[:max_rows]
    n = len(ranked)
    for i, (typ, ivs) in enumerate(ranked):
        y_lo = (n - 1 - i) / n
        y_hi = y_lo + 1 / n
        pad = min(0.22 / max(n, 1), 0.12)
        for iv in ivs:
            ax.axvspan(max(iv.start, w0), min(iv.end, w1),
                       ymin=y_lo + pad, ymax=y_hi - pad,
                       color=color, lw=0, alpha=0.92)
        ax.text(-0.008, (y_lo + y_hi) / 2, typ,
                transform=ax.transAxes, fontsize=6.5, color=_MUTED,
                ha="right", va="center", clip_on=False)


def render(events: pd.DataFrame, labels: pd.DataFrame,
           detections: pd.DataFrame | None, out_path: Path,
           window: str = "1d", explain: bool = False) -> None:
    _style()
    events = events.copy()
    events["timestamp"] = pd.to_datetime(events["timestamp"], utc=True, format="ISO8601")
    for col in ("start", "end"):
        if col in labels.columns:
            labels[col] = pd.to_datetime(labels[col], utc=True, format="ISO8601")
        if detections is not None and col in detections.columns:
            detections[col] = pd.to_datetime(detections[col], utc=True, format="ISO8601")
    width = pd.Timedelta(window)
    start = events["timestamp"].min()
    end = events["timestamp"].max()
    sensors = list(events.groupby(["sensor_id", "capability"]).size().index)
    gt_all = _load(labels)
    det_all = _load(detections) if detections is not None else []
    if explain and detections is not None and len(det_all):
        # Re-label each detection interval with the explainer's inferred_type.
        # Grouping in `_gantt` is by anomaly_type, so swapping that field here
        # makes the detected lane's rows read as canonical types ("level_shift",
        # "spike", "dropout") instead of the detector combination string. The
        # detector combination is lossy for a human reader — e.g., the same
        # "cusum+sub_pca+temporal_profile" combo fires on both short spikes
        # and multi-day drifts, which the classifier separates cleanly.
        from .explain import _detections_to_alerts, classify_type
        alerts = _detections_to_alerts(detections)
        type_by_key: dict[tuple[str, pd.Timestamp, pd.Timestamp], str] = {
            (a.sensor_id, a.window_start, a.window_end): classify_type(a)
            for a in alerts
        }
        det_all = [Interval(iv.sensor_id, iv.start, iv.end,
                            type_by_key.get((iv.sensor_id, iv.start, iv.end),
                                            iv.anomaly_type))
                   for iv in det_all]
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    n = max(1, len(sensors))
    ratios = ([10, 3.5, 3.5] * n)

    with PdfPages(out_path) as pdf:
        for w0, w1 in _windows(start, end, width):
            fig, axes = plt.subplots(
                3 * n, 1, sharex=True, figsize=(13, 3.0 * n + 1.2),
                gridspec_kw={"height_ratios": ratios, "hspace": 0.08})
            axes = axes if hasattr(axes, "__len__") else [axes]
            for i, (sid, cap) in enumerate(sensors):
                ax_sig, ax_gt, ax_dt = axes[3*i], axes[3*i+1], axes[3*i+2]
                sub = events[(events["sensor_id"] == sid)
                             & (events["capability"] == cap)
                             & (events["timestamp"] >= w0)
                             & (events["timestamp"] < w1)]
                if len(sub):
                    vals = sub["value"].to_numpy()
                    is_bin = set(pd.unique(vals)).issubset({0, 1, 0.0, 1.0})
                    if is_bin:
                        ax_sig.step(sub["timestamp"], vals, where="post",
                                    color=_LINE, lw=1.0)
                    else:
                        ax_sig.plot(sub["timestamp"], vals, color=_LINE, lw=0.7)
                ax_sig.set_xlim(w0, w1)
                ax_sig.text(0.005, 0.93, f"{sid}  ·  {cap}",
                            transform=ax_sig.transAxes, fontsize=9,
                            fontweight="semibold", color=_TEXT,
                            va="top", ha="left")
                ax_sig.grid(True, axis="x", color=_GRID, lw=0.5)
                ax_sig.grid(False, axis="y")
                ax_sig.tick_params(length=0, labelbottom=False)
                for s in ("top", "right"):
                    ax_sig.spines[s].set_visible(False)

                gt_s = [g for g in gt_all if g.sensor_id == sid
                        and g.end > w0 and g.start < w1]
                det_s = [d for d in det_all if d.sensor_id == sid
                         and d.end > w0 and d.start < w1]
                _strip(ax_gt); _strip(ax_dt)
                ax_gt.set_xlim(w0, w1); ax_dt.set_xlim(w0, w1)
                ax_gt.text(-0.075, 0.5, "truth", transform=ax_gt.transAxes,
                           fontsize=7.5, color=_TRUTH, ha="right", va="center",
                           fontweight="semibold", clip_on=False)
                ax_dt.text(-0.075, 0.5, "detected", transform=ax_dt.transAxes,
                           fontsize=7.5, color=_DETECT, ha="right", va="center",
                           fontweight="semibold", clip_on=False)
                _gantt(ax_gt, gt_s, w0, w1, _TRUTH, "no labeled anomalies")
                _gantt(ax_dt, det_s, w0, w1, _DETECT, "no detections")

            bottom = axes[-1]
            bottom.tick_params(labelbottom=True, length=3, color="#cccccc")
            bottom.spines["bottom"].set_visible(True)
            bottom.spines["bottom"].set_color("#cccccc")
            loc = mdates.AutoDateLocator(maxticks=8)
            bottom.xaxis.set_major_locator(loc)
            bottom.xaxis.set_major_formatter(mdates.ConciseDateFormatter(loc))

            title = (w0.strftime("%A, %d %b %Y") if width >= pd.Timedelta("1D")
                     else f"{w0.strftime('%d %b %H:%M')} – {w1.strftime('%H:%M')}")
            fig.suptitle(title, fontsize=11, fontweight="semibold",
                         color=_TEXT, y=0.985)
            handles = [Patch(facecolor=_TRUTH, edgecolor="none", label="true anomaly"),
                       Patch(facecolor=_DETECT, edgecolor="none", label="detected")]
            fig.legend(handles=handles, loc="lower center", ncol=2,
                       frameon=False, fontsize=8, bbox_to_anchor=(0.5, 0.008))
            fig.tight_layout(rect=[0.09, 0.04, 0.995, 0.96])
            pdf.savefig(fig, facecolor="white")
            plt.close(fig)


def _downsample(ts: pd.Series, vals, max_points: int = 4000):
    # Evenly-spaced subsampling for speed/readability on multi-week plots.
    if len(ts) <= max_points:
        return ts, vals
    step = max(1, len(ts) // max_points)
    return ts.iloc[::step], vals[::step]


def _fmt_dur(hours: float) -> str:
    if hours >= 24:
        return f"{hours/24:.1f}d"
    if hours >= 1:
        return f"{hours:.1f}h"
    return f"{hours*60:.0f}min"


def _label_page(ax_full, ax_zoom, ax_gt, ax_det, events_sub, label, dets_sub,
                scen_start, scen_end, pad: pd.Timedelta):
    dur = label.end - label.start
    zoom_s = max(scen_start, label.start - pad)
    zoom_e = min(scen_end, label.end + pad)

    # --- full scenario signal ---
    ts_full, v_full = _downsample(events_sub["timestamp"], events_sub["value"].to_numpy())
    ax_full.plot(ts_full, v_full, color=_LINE, lw=0.5)
    ax_full.axvspan(label.start, label.end, color=_TRUTH, alpha=0.18, lw=0)
    # detections as thin blue ticks on top
    for d in dets_sub:
        ax_full.axvspan(d.start, d.end, color=_DETECT, alpha=0.35, lw=0,
                        ymin=0.92, ymax=1.0)
    ax_full.set_xlim(scen_start, scen_end)
    ax_full.set_ylabel("value", fontsize=7, color=_MUTED)
    ax_full.text(0.005, 0.93, f"full scenario  ·  {_fmt_dur(((scen_end-scen_start).total_seconds()/3600))}",
                 transform=ax_full.transAxes, fontsize=7, color=_MUTED, va="top")
    ax_full.grid(True, axis="x", color=_GRID, lw=0.4)
    ax_full.tick_params(labelsize=6)
    for s in ("top", "right"): ax_full.spines[s].set_visible(False)

    # --- zoomed signal around the label ---
    m = (events_sub["timestamp"] >= zoom_s) & (events_sub["timestamp"] <= zoom_e)
    sub = events_sub.loc[m]
    ts_z, v_z = _downsample(sub["timestamp"], sub["value"].to_numpy())
    ax_zoom.plot(ts_z, v_z, color=_LINE, lw=0.8)
    ax_zoom.axvspan(label.start, label.end, color=_TRUTH, alpha=0.18, lw=0)
    ax_zoom.axvline(label.start, color=_TRUTH, lw=0.8, alpha=0.7)
    ax_zoom.axvline(label.end,   color=_TRUTH, lw=0.8, alpha=0.7)
    ax_zoom.set_xlim(zoom_s, zoom_e)
    ax_zoom.set_ylabel("value", fontsize=7, color=_MUTED)
    ax_zoom.text(0.005, 0.93,
                 f"zoom  ·  label {_fmt_dur(dur.total_seconds()/3600)}  ·  "
                 f"±{_fmt_dur((zoom_s!=scen_start)*((label.start-zoom_s).total_seconds()/3600))} context",
                 transform=ax_zoom.transAxes, fontsize=7, color=_MUTED, va="top")
    ax_zoom.grid(True, axis="x", color=_GRID, lw=0.4)
    ax_zoom.tick_params(labelsize=6, labelbottom=False)
    for s in ("top", "right"): ax_zoom.spines[s].set_visible(False)

    # --- truth/detected strips within zoom ---
    _strip(ax_gt); _strip(ax_det)
    ax_gt.set_xlim(zoom_s, zoom_e); ax_det.set_xlim(zoom_s, zoom_e)
    ax_gt.axvspan(label.start, label.end, ymin=0.15, ymax=0.85,
                  color=_TRUTH, alpha=0.9, lw=0)
    ax_gt.text(-0.01, 0.5, "truth", transform=ax_gt.transAxes,
               fontsize=7, color=_TRUTH, ha="right", va="center",
               fontweight="semibold", clip_on=False)
    ax_det.text(-0.01, 0.5, "detected", transform=ax_det.transAxes,
                fontsize=7, color=_DETECT, ha="right", va="center",
                fontweight="semibold", clip_on=False)
    for d in dets_sub:
        ax_det.axvspan(max(d.start, zoom_s), min(d.end, zoom_e),
                       ymin=0.15, ymax=0.85, color=_DETECT, alpha=0.85, lw=0)

    # x-axis formatter on the bottom strip
    loc = mdates.AutoDateLocator(maxticks=8)
    ax_det.tick_params(labelbottom=True, labelsize=6, length=3, color="#cccccc")
    ax_det.spines["bottom"].set_visible(True)
    ax_det.spines["bottom"].set_color("#cccccc")
    ax_det.xaxis.set_major_locator(loc)
    ax_det.xaxis.set_major_formatter(mdates.ConciseDateFormatter(loc))


def _summary_page(pdf, labels_df, dets_df, scen_start, scen_end, min_hours):
    rows = []
    for _, g in labels_df.iterrows():
        dur_h = (g["end"] - g["start"]).total_seconds() / 3600
        hits = dets_df[(dets_df["sensor_id"] == g["sensor_id"])
                       & (dets_df["start"] < g["end"])
                       & (dets_df["end"]   > g["start"])]
        tag = "TP" if len(hits) else "FN"
        dets_fired = "-"
        if len(hits):
            names = set()
            for s in hits["detector"].fillna("").astype(str):
                for t in s.split("+"):
                    if t: names.add(t)
            dets_fired = ", ".join(sorted(names))
        rows.append((dur_h, g["sensor_id"], g["anomaly_type"], g["start"], tag, len(hits), dets_fired))
    rows.sort(key=lambda r: -r[0])

    fig, ax = plt.subplots(figsize=(13, max(4, 0.35 * len(rows) + 2)))
    ax.axis("off")
    ax.set_title(f"All anomalies  ·  min shown in detail = {_fmt_dur(min_hours)}",
                 fontsize=12, fontweight="semibold", color=_TEXT,
                 loc="left", pad=12)
    # Header
    cols = ["dur", "sensor", "anomaly", "start", "result", "n_dets", "detectors"]
    widths = [0.06, 0.20, 0.17, 0.16, 0.06, 0.06, 0.29]
    x0 = 0.01
    y = 0.93
    for c, w in zip(cols, widths):
        ax.text(x0, y, c, fontsize=8, fontweight="semibold", color=_TEXT,
                transform=ax.transAxes, va="top")
        x0 += w
    y -= 0.025
    ax.plot([0.01, 0.99], [y, y], color="#e0e0e0", lw=0.7,
            transform=ax.transAxes, clip_on=False)
    y -= 0.02
    for dur_h, sid, atype, start, tag, n, fired in rows:
        x0 = 0.01
        emphasized = dur_h >= min_hours
        color = _TEXT if emphasized else _MUTED
        style = "normal"
        tag_color = "#2a7f2a" if tag == "TP" else _TRUTH
        vals = [_fmt_dur(dur_h), str(sid), str(atype),
                str(start)[:16], tag, str(n), fired[:60]]
        for v, w in zip(vals, widths):
            this_color = tag_color if v == tag else color
            fw = "semibold" if emphasized else "normal"
            ax.text(x0, y, v, fontsize=7.5, color=this_color, fontweight=fw,
                    transform=ax.transAxes, va="top")
            x0 += w
        y -= 0.025
    pdf.savefig(fig, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def render_long(events: pd.DataFrame, labels: pd.DataFrame,
                detections: pd.DataFrame | None, out_path: Path,
                min_hours: float = 24.0) -> None:
    """Per-long-anomaly interpretive PDF. One page per GT label with duration
    >= min_hours, showing the signal (full + zoomed), GT region, and detections.
    """
    _style()
    events = events.copy()
    events["timestamp"] = pd.to_datetime(events["timestamp"], utc=True, format="ISO8601")
    labels = labels.copy()
    for col in ("start", "end"):
        labels[col] = pd.to_datetime(labels[col], utc=True, format="ISO8601")
    if detections is not None:
        detections = detections.copy()
        for col in ("start", "end"):
            detections[col] = pd.to_datetime(detections[col], utc=True, format="ISO8601")

    scen_start = events["timestamp"].min()
    scen_end = events["timestamp"].max()

    min_dur = pd.Timedelta(hours=min_hours)
    long_labels = [g for _, g in labels.iterrows()
                   if (g["end"] - g["start"]) >= min_dur]
    long_labels.sort(key=lambda g: -(g["end"] - g["start"]).total_seconds())

    det_all = _load(detections) if detections is not None else []
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with PdfPages(out_path) as pdf:
        _summary_page(pdf, labels,
                      detections if detections is not None else pd.DataFrame(columns=["sensor_id","start","end","detector"]),
                      scen_start, scen_end, min_hours)

        for g in long_labels:
            sid = g["sensor_id"]
            atype = g["anomaly_type"]
            dur = g["end"] - g["start"]
            # Context padding: 1/3 of label duration, capped [1d, 14d]
            pad = pd.Timedelta(seconds=max(86400, min(14*86400, dur.total_seconds() / 3)))

            events_sub = events[events["sensor_id"] == sid]
            cap = events_sub["capability"].iloc[0] if len(events_sub) else ""
            dets_sub = [d for d in det_all if d.sensor_id == sid
                        and d.end > g["start"] - pad and d.start < g["end"] + pad]

            fig, axes = plt.subplots(
                4, 1, figsize=(13, 8),
                gridspec_kw={"height_ratios": [3, 5, 0.7, 0.7], "hspace": 0.18})
            ax_full, ax_zoom, ax_gt, ax_det = axes

            # Header
            tp = any(d.sensor_id == sid and d.start < g["end"] and d.end > g["start"]
                     for d in det_all)
            tag = "TP" if tp else "FN"
            tag_color = "#2a7f2a" if tp else _TRUTH
            header = (f"{atype}  ·  {sid} ({cap})  ·  "
                      f"duration {_fmt_dur(dur.total_seconds()/3600)}  ·  "
                      f"{g['start'].strftime('%Y-%m-%d %H:%M')} → {g['end'].strftime('%Y-%m-%d %H:%M')}")
            fig.suptitle(header, fontsize=11, fontweight="semibold",
                         color=_TEXT, y=0.98, ha="center")
            fig.text(0.99, 0.98, tag, color=tag_color, fontsize=14,
                     fontweight="bold", ha="right", va="top")

            class _L:
                start = g["start"]
                end   = g["end"]
            _label_page(ax_full, ax_zoom, ax_gt, ax_det, events_sub, _L(),
                        dets_sub, scen_start, scen_end, pad)

            handles = [Patch(facecolor=_TRUTH, alpha=0.5, edgecolor="none", label="truth"),
                       Patch(facecolor=_DETECT, alpha=0.7, edgecolor="none", label="detected")]
            fig.legend(handles=handles, loc="lower center", ncol=2,
                       frameon=False, fontsize=8, bbox_to_anchor=(0.5, 0.01))
            fig.tight_layout(rect=[0.04, 0.04, 0.995, 0.95])
            pdf.savefig(fig, facecolor="white")
            plt.close(fig)
