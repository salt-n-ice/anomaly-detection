"""Explain-quality research harness — case generator.

Produces per-scenario <scenario>_cases.jsonl + <scenario>_prompts.md under
research/explain/runs/<timestamp>/. Each case bundles the explainer output,
the rendered prompt, and the overlapping ground-truth labels. A Claude-in-
session judge then reads cases.jsonl and writes <scenario>_scores.jsonl
(see docs/superpowers/specs/2026-04-21-explain-eval-design.md).

Usage
-----
    python research/explain/run_explain_eval.py --suite all
    python research/explain/run_explain_eval.py --suite 60d
"""
from __future__ import annotations
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "research"))

import pandas as pd  # noqa: E402

from anomaly.explain import explain_detections_csv, build_prompt  # noqa: E402
from run_research_eval import SCENARIOS, GEN, git_hash, git_dirty  # noqa: E402


RUNS = ROOT / "research" / "explain" / "runs"
OUT = ROOT / "out"


def compute_overlap(bundle: dict, labels: pd.DataFrame) -> list[dict]:
    """Return the subset of `labels` overlapping `bundle` by sensor+cap+time.

    `labels` must have columns sensor_id, capability, start, end,
    anomaly_type, and optionally detector_hint / params_json. start / end
    must already be parsed to UTC-aware pd.Timestamp.
    """
    if len(labels) == 0:
        return []
    ws = pd.Timestamp(bundle["window"]["start"])
    we = pd.Timestamp(bundle["window"]["end"])
    mask = (
        (labels["sensor_id"] == bundle["sensor"])
        & (labels["capability"] == bundle["capability"])
        & (labels["start"] <= we)
        & (labels["end"] >= ws)
    )
    return labels[mask].to_dict(orient="records")


def _serialize_labels(labels: list[dict]) -> list[dict]:
    """Convert timestamp-bearing label rows to a JSON-safe shape."""
    out = []
    for L in labels:
        out.append({
            "sensor_id": L["sensor_id"],
            "capability": L["capability"],
            "start": pd.Timestamp(L["start"]).isoformat(),
            "end":   pd.Timestamp(L["end"]).isoformat(),
            "anomaly_type": L["anomaly_type"],
            "detector_hint": L.get("detector_hint"),
            "params_json":  L.get("params_json"),
        })
    return out


def build_cases(scenario: str, suite: str, bundles: list[dict],
                labels: pd.DataFrame) -> list[dict]:
    """Pair each bundle with overlapping labels + rendered prompt."""
    cases = []
    for i, b in enumerate(bundles):
        overlaps = compute_overlap(b, labels)
        cases.append({
            "case_id": f"{scenario}#{i:03d}",
            "scenario": scenario,
            "suite": suite,
            "is_tp": bool(overlaps),
            "bundle": b,
            "prompt": build_prompt(b),
            "gt_labels": _serialize_labels(overlaps),
        })
    return cases


def _render_prompts_md(scenario: str, ts: str, cases: list[dict]) -> str:
    """Produce a human-skim markdown of all cases with their GT tags."""
    lines: list[str] = [f"# {scenario} — explain cases (run {ts})", ""]
    for c in cases:
        gt_str = (", ".join(L["anomaly_type"] for L in c["gt_labels"])
                  if c["gt_labels"] else "(none)")
        tag = "TP" if c["is_tp"] else "FP"
        lines += [
            f"## Case {c['case_id']}  —  {tag}  —  GT: {gt_str}",
            "",
            c["prompt"],
            "",
            "---",
            "",
        ]
    return "\n".join(lines)


def _produce_bundles(events_csv: Path, dets_csv: Path,
                     tmp_jsonl: Path) -> list[dict]:
    """Run the explainer and load the resulting bundles back from JSONL."""
    explain_detections_csv(events_csv, dets_csv, tmp_jsonl)
    lines = tmp_jsonl.read_text(encoding="utf-8").splitlines()
    return [json.loads(ln) for ln in lines if ln.strip()]


def _load_labels(labels_csv: Path) -> pd.DataFrame:
    df = pd.read_csv(labels_csv)
    df["start"] = pd.to_datetime(df["start"], utc=True, format="ISO8601")
    df["end"]   = pd.to_datetime(df["end"],   utc=True, format="ISO8601")
    return df


def run_scenario(scenario: str, suite: str, events_dir: str,
                 out_dir: Path) -> dict:
    events_csv = GEN / events_dir / "events.csv"
    labels_csv = GEN / events_dir / "labels.csv"
    dets_csv   = OUT / f"{scenario}_detections.csv"
    missing = [str(p) for p in (events_csv, labels_csv, dets_csv) if not p.exists()]
    if missing:
        print(f"  [skip] {scenario}: missing {missing}")
        return {"name": scenario, "suite": suite, "skipped": True,
                "missing": missing}

    tmp_jsonl = out_dir / f"{scenario}_bundles.jsonl"
    bundles = _produce_bundles(events_csv, dets_csv, tmp_jsonl)
    labels  = _load_labels(labels_csv)
    cases   = build_cases(scenario, suite, bundles, labels)

    cases_path = out_dir / f"{scenario}_cases.jsonl"
    with cases_path.open("w", encoding="utf-8") as f:
        for c in cases:
            f.write(json.dumps(c, default=str) + "\n")

    prompts_path = out_dir / f"{scenario}_prompts.md"
    prompts_path.write_text(
        _render_prompts_md(scenario, out_dir.name, cases), encoding="utf-8")

    n_tp = sum(1 for c in cases if c["is_tp"])
    n_fp = len(cases) - n_tp
    print(f"  {scenario:<22} cases={len(cases):>4}  tp={n_tp:>4}  fp={n_fp:>4}")
    return {"name": scenario, "suite": suite, "skipped": False,
            "n_cases": len(cases), "n_tp": n_tp, "n_fp": n_fp,
            "cases_path": str(cases_path), "prompts_path": str(prompts_path)}


def filter_suite(suite: str):
    if suite == "all":
        return SCENARIOS
    return [s for s in SCENARIOS if s[0] == suite]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", choices=["all", "60d", "120d"], default="all")
    args = ap.parse_args(argv)

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = RUNS / ts
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for suite_tag, scen, ev_dir, _cfg, _boot in filter_suite(args.suite):
        rows.append(run_scenario(scen, suite_tag, ev_dir, out_dir))

    manifest = {
        "timestamp": ts,
        "git_hash": git_hash(),
        "git_dirty": git_dirty(),
        "suite_filter": args.suite,
        "scenarios": rows,
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))
    (RUNS / "latest.txt").write_text(ts)
    print(f"\nwrote {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
