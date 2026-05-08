"""_apply_supplement_v2_v1_20260504.py — read-only assembly.

Applies the second supplement (final 11 T1 stragglers) on top of v5,
producing v6.

Inputs:
  outputs/markdown/wa-term-anchor-v5-20260504.json
  outputs/markdown/wa-meaning-clusters-supplement-v2-20260504.json

Outputs:
  outputs/markdown/wa-term-anchor-v6-20260504.json
  outputs/markdown/wa-term-anchor-v6-20260504-summary.md
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

V5_PATH = "outputs/markdown/wa-term-anchor-v5-20260504.json"
SUP_PATH = "outputs/markdown/wa-meaning-clusters-supplement-v2-20260504.json"
V6_PATH = "outputs/markdown/wa-term-anchor-v6-20260504.json"
V6_SUMMARY_PATH = "outputs/markdown/wa-term-anchor-v6-20260504-summary.md"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    print("Loading v5 anchor...", flush=True)
    with open(V5_PATH, encoding="utf-8") as f:
        v5 = json.load(f)
    print("Loading supplement v2...", flush=True)
    with open(SUP_PATH, encoding="utf-8") as f:
        sup = json.load(f)

    cluster_labels = v5.get("meaning_cluster_labels", {})
    v5_terms = v5.get("term_anchors", {})
    v6_terms = {k: dict(v) for k, v in v5_terms.items()}

    audit = []
    n_applied = 0
    n_missing = 0
    cluster_destination = Counter()

    for a in sup["assignments"]:
        strong = a["strong"]
        target = a["to_cluster"]
        target_label = cluster_labels.get(target, "(UNKNOWN)")
        if strong not in v6_terms:
            audit.append({
                "strong": strong,
                "outcome": "MISSING",
                "to": target,
            })
            n_missing += 1
            continue
        prev_cid = v6_terms[strong].get("cluster_id")
        prev_label = v6_terms[strong].get("cluster_label")
        v6_terms[strong]["cluster_id"] = target
        v6_terms[strong]["cluster_label"] = target_label
        v6_terms[strong]["cluster_source"] = "meaning_v2_supplement_2"
        if a.get("note"):
            v6_terms[strong]["supplement_note"] = a["note"]
        audit.append({
            "strong": strong,
            "gloss_actual": v6_terms[strong].get("gloss"),
            "from_cluster": prev_cid,
            "from_label": prev_label,
            "to_cluster": target,
            "to_label": target_label,
            "outcome": "APPLIED",
        })
        n_applied += 1
        cluster_destination[target] += 1

    # Reconcile
    def is_unassigned(t):
        cid = t.get("cluster_id") or ""
        if cid in ("T2", "FLAG"):
            return False
        if cid.startswith("M") and cid[1:].isdigit():
            return False
        return True

    unassigned = [
        {"strong": s, **{k: v for k, v in t.items()
                         if k in ("lang", "gloss", "transliteration",
                                  "verse_count", "bucket",
                                  "cluster_id", "cluster_source")}}
        for s, t in v6_terms.items() if is_unassigned(t)
    ]

    v6 = dict(v5)
    v6["meta"] = dict(v5["meta"])
    v6["meta"]["version"] = "v6"
    v6["meta"]["generated"] = now_iso()
    v6["meta"]["supplement_v2_source"] = SUP_PATH
    v6["meta"]["n_supplement_v2_applied"] = n_applied
    v6["meta"]["n_supplement_v2_missing"] = n_missing
    v6["meta"]["n_terms_unassigned_after_v6"] = len(unassigned)
    v6["term_anchors"] = v6_terms
    v6_clusters = defaultdict(list)
    for s, t in v6_terms.items():
        v6_clusters[t.get("cluster_id") or "(none)"].append(s)
    v6["cluster_index"] = {
        cid: sorted(strongs)
        for cid, strongs in sorted(v6_clusters.items())
    }
    v6["supplement_v2_audit"] = audit

    with open(V6_PATH, "w", encoding="utf-8") as f:
        json.dump(v6, f, indent=2, ensure_ascii=False)
    print(f"Wrote: {V6_PATH}", flush=True)

    # Summary md
    src_counts = Counter(t.get("cluster_source") for t in v6_terms.values())
    cluster_member_counts = Counter(
        t.get("cluster_id") for t in v6_terms.values()
    )
    bucket_unassigned = Counter(
        u.get("bucket") or "(none)" for u in unassigned
    )

    lines = []
    lines.append("# Term-anchor v6 — final supplement applied\n")
    lines.append(f"**Generated:** {v6['meta']['generated']}  ")
    lines.append(f"**Built from:** v5 + "
                 f"`{os.path.basename(SUP_PATH)}` (final 11 T1 stragglers)  \n")
    lines.append("## Headline\n")
    lines.append(f"- Supplement assignments: **{len(sup['assignments'])}**")
    lines.append(f"- Applied: **{n_applied}**")
    lines.append(f"- Missing from v5 anchor: **{n_missing}**")
    lines.append(f"- **Unassigned after v6:** **{len(unassigned)}**")
    lines.append("")
    lines.append("## Per-cluster destination of supplement-v2 terms\n")
    lines.append("| Cluster | Label | Terms added |")
    lines.append("|---|---|---:|")
    for cid, n in cluster_destination.most_common():
        lines.append(f"| {cid} | {cluster_labels.get(cid, '?')} | {n} |")
    lines.append("")
    lines.append("## Per-term audit (applied)\n")
    lines.append("| Strong's | Gloss | From | To |")
    lines.append("|---|---|---|---|")
    for r in audit:
        if r["outcome"] != "APPLIED":
            continue
        from_disp = (r.get("from_cluster") or "(none)")
        if r.get("from_label"):
            from_disp = f"{from_disp} / {r['from_label']}"
        to_disp = f"{r['to_cluster']} / {r.get('to_label', '?')}"
        lines.append(
            f"| {r['strong']} | {r.get('gloss_actual', '')} | "
            f"{from_disp} | {to_disp} |"
        )
    lines.append("")
    lines.append("## Cluster-source breakdown (v6)\n")
    lines.append("| Source | Count |")
    lines.append("|---|---:|")
    for s, n in src_counts.most_common():
        lines.append(f"| {s or '(none)'} | {n} |")
    lines.append("")
    lines.append("## Special-cluster sizes (v6)\n")
    lines.append(f"- **T2 — Supplementary:** "
                 f"{cluster_member_counts.get('T2', 0):,} members")
    lines.append(f"- **FLAG — Flagged for Review:** "
                 f"{cluster_member_counts.get('FLAG', 0):,} members")
    lines.append("")
    lines.append("## Bucket distribution of remaining unassigned\n")
    if not bucket_unassigned:
        lines.append("**None — every term now has a cluster assignment.**\n")
    else:
        lines.append("| Bucket | Count |")
        lines.append("|---|---:|")
        for b, n in bucket_unassigned.most_common():
            lines.append(f"| {b} | {n} |")

    with open(V6_SUMMARY_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {V6_SUMMARY_PATH}", flush=True)

    print(f"\nSummary: applied={n_applied} unassigned={len(unassigned):,}",
          flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
