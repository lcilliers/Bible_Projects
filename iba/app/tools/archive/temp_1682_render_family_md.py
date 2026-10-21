"""
temp_1682_render_family_md.py (round 2 -- structured occurrence traces + strong_checks)

Renders the .md companion for a process-(c) family JSON (escalation #1682 spec) from the JSON
itself, so JSON and MD cannot drift apart -- the JSON is the single source of truth, MD is a
derived view. One-off test script pending spec approval (governance.scripts_and_routines temp_
convention).

Usage:
    python iba/app/tools/temp_1682_render_family_md.py --in <family.json> --out <family.md>
"""
import argparse
import json
import sys

TAG_LABELS = {
    "instance-meaning": "Instance meanings (what each occurrence is)",
    "alternative-meaning": "Alternative / candidate meanings",
    "verse-grouping": "Verse groupings (shared meaning)",
    "difference-inference": "Differences and inferences",
    "surface-gloss-divergence": "Surface vs. gloss divergence",
    "no-human-context": "No human context (earmarked, not analysed)",
    "cross-family": "Cross-family observations, anomalies, pointers",
    "data-error": "Data errors",
}
TAG_ORDER = list(TAG_LABELS.keys())


def render_occurrences(occs: list) -> str:
    parts = []
    for o in occs or []:
        bits = [o.get("verse", "?")]
        if o.get("span_surface"):
            bits.append(f"surface='{o['span_surface']}'")
        if o.get("span_morph"):
            bits.append(f"morph={o['span_morph']}")
        parts.append(" ".join(bits))
    return "; ".join(parts) if parts else "(no occurrences traced)"


def render(data: dict) -> str:
    lines = []
    fam = data["family_id"]
    cluster = data["cluster_code"]
    lines.append(f"# Cluster reading — {cluster} / {fam}")
    lines.append("")
    lines.append(
        f"> Process (c) output, escalation #1682 spec "
        f"(`iba/docs/1682-cluster-reading-process-spec-v1-20260911.md`, round 2). "
        f"Strongs in family: {', '.join(data['strongs_in_family'])}. "
        f"Generated from the companion JSON — this file is a derived view, not hand-edited."
    )
    lines.append("")

    checks = data.get("strong_checks", [])
    if checks:
        lines.append("## Per-strong verification (computed, not eyeballed)")
        lines.append("")
        lines.append("| strong | occurrences | traced | missing |")
        lines.append("|---|--:|--:|---|")
        any_missing = False
        for c in checks:
            missing = c.get("missing_verses") or []
            if missing:
                any_missing = True
            missing_str = ", ".join(missing) if missing else "—"
            lines.append(f"| {c['strong']} | {c['occurrence_count']} | {c['traced_count']} | {missing_str} |")
        lines.append("")
        lines.append(
            "**ALL VERSES TRACED**" if not any_missing else
            "**⚠ INCOMPLETE — see missing column above**"
        )
        lines.append("")

    obs = data["observations"]
    counts = {t: sum(1 for o in obs if o["tag"] == t) for t in TAG_ORDER}
    lines.append("## Observation counts")
    lines.append("")
    lines.append("| tag | count |")
    lines.append("|---|--:|")
    for t in TAG_ORDER:
        if counts.get(t):
            lines.append(f"| {TAG_LABELS[t]} | {counts[t]} |")
    lines.append(f"| **Total** | **{len(obs)}** |")
    lines.append("")

    for tag in TAG_ORDER:
        rows = [o for o in obs if o["tag"] == tag]
        if not rows:
            continue
        lines.append(f"## {TAG_LABELS[tag]}")
        lines.append("")
        for o in rows:
            t = o["traces"]
            trace_bits = []
            if t.get("strong"):
                trace_bits.append(f"strong={t['strong']}")
            occ_str = render_occurrences(t.get("occurrences"))
            if occ_str != "(no occurrences traced)":
                trace_bits.append(f"occurrences=[{occ_str}]")
            for key in ("meaning_source", "related_cluster", "related_family"):
                if t.get(key):
                    trace_bits.append(f"{key}={t[key]}")
            trace_str = " · ".join(trace_bits) if trace_bits else "(no traces recorded)"
            lines.append(f"- {o['statement']}")
            lines.append(f"  *[{trace_str}]*")
            lines.append("")

    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True)
    ap.add_argument("--out", dest="out_path", required=True)
    args = ap.parse_args()

    with open(args.in_path, encoding="utf-8") as f:
        data = json.load(f)
    md = render(data)
    with open(args.out_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"rendered {args.out_path} ({len(data['observations'])} observations)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
