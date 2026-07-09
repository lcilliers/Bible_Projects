"""_apply_meaning_clusters_v1_20260504.py — read-only assembly.

Takes the researcher-curated meaning-cluster file and applies it on top of the
existing term-anchor structure to produce a new term-anchor v2.

Inputs:
  outputs/markdown/wa-meaning-clusters-v1-2026-05-04.json   (researcher-curated)
  outputs/markdown/wa-term-anchor-20260504.json             (v1 / existing)

Outputs:
  outputs/markdown/wa-term-anchor-v2-20260504.json          (new canonical)
  outputs/markdown/wa-term-anchor-v2-20260504-summary.md    (change report)

Logic:
  - For every term in the meaning-clusters file, set cluster_id = M-prefix and
    cluster_label = the curated label. Preserve original cluster_id as
    `legacy_cluster_id`.
  - For every term in the v1 anchor that is NOT in the meaning-clusters file,
    keep its v1 cluster_id BUT mark `cluster_source = 'legacy'` so downstream
    code can tell what's been re-assigned vs what hasn't.
  - Bucket field preserved from v1 (T1 / T2 / FLAG / EXTRACTION-NOISE).
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

MEANING_PATH = "outputs/markdown/wa-meaning-clusters-v1-2026-05-04.json"
V1_PATH = "outputs/markdown/wa-term-anchor-20260504.json"
V2_PATH = "outputs/markdown/wa-term-anchor-v2-20260504.json"
V2_SUMMARY_PATH = "outputs/markdown/wa-term-anchor-v2-20260504-summary.md"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    print("Loading meaning clusters...", flush=True)
    with open(MEANING_PATH, encoding="utf-8") as f:
        meaning = json.load(f)
    print("Loading v1 anchor...", flush=True)
    with open(V1_PATH, encoding="utf-8") as f:
        v1 = json.load(f)

    v1_terms = v1.get("term_anchors", {})
    print(f"  v1 term_anchors: {len(v1_terms):,}", flush=True)
    print(f"  meaning clusters: {len(meaning['clusters'])}", flush=True)
    print(f"  meaning total members: {meaning['meta']['total_terms']:,}",
          flush=True)

    # Build strong -> (cluster_id, cluster_label) map from meaning file
    meaning_assign = {}
    for cid, cluster in meaning["clusters"].items():
        label = cluster["label"]
        for m in cluster["members"]:
            meaning_assign[m["strong"]] = {
                "cluster_id": cid,
                "cluster_label": label,
            }
    print(f"  meaning assignments: {len(meaning_assign):,}", flush=True)

    # Build v2 term anchors
    v2_terms = {}
    n_reassigned = 0
    n_legacy = 0
    n_only_in_meaning = 0
    legacy_cluster_keep = Counter()
    for strong, term in v1_terms.items():
        new_term = dict(term)
        new_term["legacy_cluster_id"] = term.get("cluster_id")
        new_term["legacy_cluster_label"] = term.get("cluster_label")
        if strong in meaning_assign:
            new_term["cluster_id"] = meaning_assign[strong]["cluster_id"]
            new_term["cluster_label"] = meaning_assign[strong]["cluster_label"]
            new_term["cluster_source"] = "meaning_v1"
            n_reassigned += 1
        else:
            new_term["cluster_source"] = "legacy_v1"
            legacy_cluster_keep[term.get("cluster_id", "(none)")] += 1
            n_legacy += 1
        v2_terms[strong] = new_term

    # Any meaning-cluster terms not in v1 anchor? (shouldn't be many)
    for strong in meaning_assign:
        if strong not in v1_terms:
            n_only_in_meaning += 1
            v2_terms[strong] = {
                "strong": strong,
                "cluster_id": meaning_assign[strong]["cluster_id"],
                "cluster_label": meaning_assign[strong]["cluster_label"],
                "cluster_source": "meaning_v1_only",
                "legacy_cluster_id": None,
                "legacy_cluster_label": None,
                "bucket": None,
                "lang": None,
                "transliteration": None,
                "gloss": None,
                "verse_count": None,
                "multi_term_pct": None,
            }

    # Build v2 cluster index (group terms by new cluster_id)
    v2_clusters = defaultdict(list)
    for strong, t in v2_terms.items():
        v2_clusters[t["cluster_id"] or "(none)"].append(strong)

    # Output meta
    out = {
        "meta": {
            "version": "v2",
            "generated": now_iso(),
            "source_meaning_file": MEANING_PATH,
            "source_v1_anchor_file": V1_PATH,
            "n_terms_total": len(v2_terms),
            "n_terms_reassigned_by_meaning": n_reassigned,
            "n_terms_legacy_kept": n_legacy,
            "n_terms_only_in_meaning_file": n_only_in_meaning,
            "meaning_cluster_count": len(meaning["clusters"]),
            "convention": (
                "cluster_id with M-prefix = curated meaning cluster (M01..M46). "
                "cluster_id with H/G-prefix = legacy term-anchor cluster (term "
                "not yet assigned to a meaning characteristic). "
                "legacy_cluster_id always preserves the v1 assignment."
            ),
        },
        "meaning_clusters_meta": meaning["meta"],
        "meaning_cluster_labels": {
            cid: c["label"] for cid, c in meaning["clusters"].items()
        },
        "term_anchors": v2_terms,
        "cluster_index": {
            cid: sorted(strongs)
            for cid, strongs in sorted(v2_clusters.items())
        },
    }

    os.makedirs(os.path.dirname(V2_PATH), exist_ok=True)
    with open(V2_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Wrote: {V2_PATH}", flush=True)

    # Build summary markdown
    lines = []
    lines.append("# Term-anchor v2 — meaning-cluster overlay applied\n")
    lines.append(f"**Generated:** {out['meta']['generated']}  ")
    lines.append(f"**Source meaning clusters:** "
                 f"`{os.path.basename(MEANING_PATH)}` "
                 f"(45 named-characteristic clusters)  ")
    lines.append(f"**Source v1 anchor:** "
                 f"`{os.path.basename(V1_PATH)}`  \n")
    lines.append("## Headline\n")
    lines.append(f"- Total terms in v2: **{len(v2_terms):,}**")
    lines.append(f"- Reassigned to meaning clusters (M01..M46): "
                 f"**{n_reassigned:,}**")
    lines.append(f"- Kept on legacy v1 cluster (no meaning-cluster home): "
                 f"**{n_legacy:,}**")
    if n_only_in_meaning:
        lines.append(f"- In meaning file but not in v1 anchor: "
                     f"**{n_only_in_meaning}**")
    lines.append("")
    lines.append("## Meaning-cluster catalogue (45 named characteristics)\n")
    lines.append("| ID | Name | Members |")
    lines.append("|---|---|---:|")
    for cid in sorted(meaning["clusters"].keys()):
        c = meaning["clusters"][cid]
        lines.append(f"| {cid} | {c['label']} | {len(c['members'])} |")
    lines.append("")
    lines.append("## Legacy clusters still holding terms (top 20)\n")
    lines.append("These are the v1 H/G-prefix clusters that retain terms "
                 "not yet assigned to a meaning characteristic. Useful for "
                 "deciding whether to extend the meaning-cluster set.\n")
    lines.append("| Legacy cluster | Terms still on it |")
    lines.append("|---|---:|")
    for cid, n in legacy_cluster_keep.most_common(20):
        lines.append(f"| {cid} | {n} |")
    lines.append("")
    lines.append("## Bucket distribution after overlay\n")
    bucket_counts = Counter()
    for t in v2_terms.values():
        bucket_counts[t.get("bucket") or "(unset)"] += 1
    lines.append("| Bucket | Count |")
    lines.append("|---|---:|")
    for b, n in bucket_counts.most_common():
        lines.append(f"| {b} | {n} |")
    lines.append("")
    lines.append("## Cluster-source breakdown\n")
    src_counts = Counter(t.get("cluster_source") for t in v2_terms.values())
    lines.append("| Source | Count |")
    lines.append("|---|---:|")
    for s, n in src_counts.most_common():
        lines.append(f"| {s} | {n} |")
    lines.append("")
    lines.append("## Schema (v2 term anchor records)\n")
    lines.append("```")
    lines.append("{")
    lines.append('  "strong":              "H0056",')
    lines.append('  "lang":                "H" | "G",')
    lines.append('  "transliteration":     "a.val",')
    lines.append('  "gloss":               "to mourn",')
    lines.append('  "verse_count":         38,')
    lines.append('  "multi_term_pct":      84.2,')
    lines.append('  "bucket":              "T1" | "T2" | "FLAG" | '
                 '"EXTRACTION-NOISE",')
    lines.append('  "cluster_id":          "M03" | "H011" | ...,')
    lines.append('  "cluster_label":       "Grief, Sorrow and Mourning" | ...,')
    lines.append('  "cluster_source":      "meaning_v1" | "legacy_v1",')
    lines.append('  "legacy_cluster_id":   "H011",')
    lines.append('  "legacy_cluster_label":"mourning/mourn/weep"')
    lines.append("}")
    lines.append("```")

    with open(V2_SUMMARY_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {V2_SUMMARY_PATH}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
