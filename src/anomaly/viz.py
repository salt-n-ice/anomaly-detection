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
           window: str = "1d") -> None:
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
