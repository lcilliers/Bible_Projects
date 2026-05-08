"""_apply_bucket_sweep_v1_20260504.py — read-only assembly.

Applies a "bucket-sweep" rule: every term whose bucket is FLAG (v1) and is
still unassigned by v4 -> assign to FLAG cluster. Every term whose bucket is
GENERICS and is still unassigned -> assign to T2 cluster.

Inputs:
  outputs/markdown/wa-term-anchor-v4-20260504.json
  outputs/markdown/wa-meaning-clusters-v2-2026-05-04.json   (for cluster labels)

Outputs:
  outputs/markdown/wa-term-anchor-v5-20260504.json
  outputs/markdown/wa-term-anchor-v5-20260504-summary.md
  outputs/markdown/wa-term-anchor-v5-20260504-unassigned.md
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

V4_PATH = "outputs/markdown/wa-term-anchor-v4-20260504.json"
V2M_PATH = "outputs/markdown/wa-meaning-clusters-v2-2026-05-04.json"
V5_PATH = "outputs/markdown/wa-term-anchor-v5-20260504.json"
V5_SUMMARY_PATH = "outputs/markdown/wa-term-anchor-v5-20260504-summary.md"
V5_UNASSIGNED_PATH = (
    "outputs/markdown/wa-term-anchor-v5-20260504-unassigned.md"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    print("Loading v4 anchor...", flush=True)
    with open(V4_PATH, encoding="utf-8") as f:
        v4 = json.load(f)
    print("Loading v2 meaning-clusters (for labels)...", flush=True)
    with open(V2M_PATH, encoding="utf-8") as f:
        v2m = json.load(f)

    cluster_labels = {cid: c["label"] for cid, c in v2m["clusters"].items()}
    flag_label = cluster_labels.get("FLAG", "Flagged for Review")
    t2_label = cluster_labels.get("T2", "T2 - Supplementary")

    v4_terms = v4.get("term_anchors", {})
    print(f"  v4 term_anchors: {len(v4_terms):,}", flush=True)

    # Build v5
    v5_terms = {k: dict(v) for k, v in v4_terms.items()}

    # Identify which terms are currently unassigned (cluster_id not in
    # M.. / T2 / FLAG)
    def is_unassigned(t):
        cid = t.get("cluster_id") or ""
        if cid in ("T2", "FLAG"):
            return False
        if cid.startswith("M") and cid[1:].isdigit():
            return False
        return True

    flag_sweep = []
    generics_sweep = []
    for s, t in v5_terms.items():
        if not is_unassigned(t):
            continue
        bucket = t.get("bucket")
        if bucket == "FLAG":
            t["cluster_id"] = "FLAG"
            t["cluster_label"] = flag_label
            t["cluster_source"] = "bucket_sweep_FLAG"
            flag_sweep.append(s)
        elif bucket == "GENERICS":
            t["cluster_id"] = "T2"
            t["cluster_label"] = t2_label
            t["cluster_source"] = "bucket_sweep_GENERICS_to_T2"
            generics_sweep.append(s)

    print(f"  FLAG-bucket -> FLAG cluster: {len(flag_sweep)}", flush=True)
    print(f"  GENERICS-bucket -> T2 cluster: {len(generics_sweep)}",
          flush=True)

    # Reconcile remaining unassigned
    unassigned = []
    for s, t in v5_terms.items():
        if is_unassigned(t):
            unassigned.append({
                "strong": s,
                "lang": t.get("lang"),
                "gloss": t.get("gloss"),
                "transliteration": t.get("transliteration"),
                "verse_count": t.get("verse_count"),
                "bucket": t.get("bucket"),
                "current_cluster_id": t.get("cluster_id"),
                "current_cluster_label": t.get("cluster_label"),
                "cluster_source": t.get("cluster_source"),
            })

    # Build v5 file
    v5 = dict(v4)
    v5["meta"] = dict(v4["meta"])
    v5["meta"]["version"] = "v5"
    v5["meta"]["generated"] = now_iso()
    v5["meta"]["bucket_sweep_FLAG_count"] = len(flag_sweep)
    v5["meta"]["bucket_sweep_GENERICS_to_T2_count"] = len(generics_sweep)
    v5["meta"]["n_terms_unassigned_after_v5"] = len(unassigned)
    v5["term_anchors"] = v5_terms
    v5_clusters = defaultdict(list)
    for s, t in v5_terms.items():
        v5_clusters[t.get("cluster_id") or "(none)"].append(s)
    v5["cluster_index"] = {
        cid: sorted(strongs)
        for cid, strongs in sorted(v5_clusters.items())
    }
    v5["bucket_sweep_audit"] = {
        "flag_terms_added": flag_sweep,
        "generics_terms_added": generics_sweep,
    }

    with open(V5_PATH, "w", encoding="utf-8") as f:
        json.dump(v5, f, indent=2, ensure_ascii=False)
    print(f"Wrote: {V5_PATH}", flush=True)

    # Summary
    src_counts = Counter(t.get("cluster_source") for t in v5_terms.values())
    cluster_member_counts = Counter(
        t.get("cluster_id") for t in v5_terms.values()
    )

    lines = []
    lines.append("# Term-anchor v5 — bucket sweep applied\n")
    lines.append(f"**Generated:** {v5['meta']['generated']}  ")
    lines.append(f"**Built from:** v4 + bucket-sweep rule  \n")
    lines.append("## Headline\n")
    lines.append(f"- v5 term_anchors: **{len(v5_terms):,}**")
    lines.append(f"- Bucket-FLAG → FLAG cluster: "
                 f"**{len(flag_sweep)}**")
    lines.append(f"- Bucket-GENERICS → T2 cluster: "
                 f"**{len(generics_sweep)}**")
    lines.append(f"- **Unassigned after sweep:** "
                 f"**{len(unassigned)}**")
    lines.append("")
    lines.append("## Cluster-source breakdown (v5)\n")
    lines.append("| Source | Count |")
    lines.append("|---|---:|")
    for s, n in src_counts.most_common():
        lines.append(f"| {s or '(none)'} | {n} |")
    lines.append("")
    lines.append("## Special-cluster sizes (v5)\n")
    lines.append(f"- **T2 — Supplementary:** "
                 f"{cluster_member_counts.get('T2', 0):,} members")
    lines.append(f"- **FLAG — Flagged for Review:** "
                 f"{cluster_member_counts.get('FLAG', 0):,} members")

    with open(V5_SUMMARY_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {V5_SUMMARY_PATH}", flush=True)

    # Unassigned report
    ua = []
    ua.append("# Unassigned terms after v5 bucket sweep\n")
    ua.append(f"**Generated:** {v5['meta']['generated']}  ")
    ua.append(f"**Total unassigned:** {len(unassigned):,} of "
              f"{len(v5_terms):,}\n")
    ua.append("These terms still have legacy or null cluster IDs after the "
              "bucket-sweep (FLAG→FLAG, GENERICS→T2).\n")
    ua.append("## Distribution by bucket\n")
    bk = Counter(u.get("bucket") or "(none)" for u in unassigned)
    ua.append("| Bucket | Count |")
    ua.append("|---|---:|")
    for b, n in bk.most_common():
        ua.append(f"| {b} | {n} |")
    ua.append("")
    ua.append("## Distribution by language\n")
    lc = Counter(u.get("lang") or "(none)" for u in unassigned)
    ua.append("| Lang | Count |")
    ua.append("|---|---:|")
    for l, n in lc.most_common():
        ua.append(f"| {l} | {n} |")
    ua.append("")
    ua.append("## Full unassigned term list\n")
    ua.append("| Strong's | Lang | Translit | Gloss | Verses | Bucket | "
              "Legacy cluster |")
    ua.append("|---|---|---|---|---:|---|---|")
    for u in sorted(
        unassigned,
        key=lambda x: (x.get("bucket") or "ZZ", x.get("strong") or "")
    ):
        verses = (
            u.get("verse_count")
            if u.get("verse_count") is not None else ""
        )
        ua.append(
            f"| {u.get('strong', '')} | "
            f"{u.get('lang') or ''} | "
            f"{u.get('transliteration') or ''} | "
            f"{u.get('gloss') or ''} | "
            f"{verses} | "
            f"{u.get('bucket') or ''} | "
            f"{u.get('current_cluster_id') or ''} |"
        )

    with open(V5_UNASSIGNED_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(ua) + "\n")
    print(f"Wrote: {V5_UNASSIGNED_PATH}", flush=True)

    print(f"\nSummary: flag_sweep={len(flag_sweep)} "
          f"generics_sweep={len(generics_sweep)} "
          f"unassigned={len(unassigned):,}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
