"""_apply_meaning_clusters_v2_v1_20260504.py — read-only assembly.

Applies the comprehensive v2 meaning-clusters file (45 M-clusters + T2 + FLAG
special clusters) on top of the v3 term-anchor, producing v4 + a reconciliation
report listing terms that are still on legacy clusters.

Inputs:
  outputs/markdown/wa-term-anchor-v3-20260504.json
  outputs/markdown/wa-meaning-clusters-v2-2026-05-04.json   (researcher-curated)

Outputs:
  outputs/markdown/wa-term-anchor-v4-20260504.json
  outputs/markdown/wa-term-anchor-v4-20260504-summary.md
  outputs/markdown/wa-term-anchor-v4-20260504-unassigned.md
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

V3_PATH = "outputs/markdown/wa-term-anchor-v3-20260504.json"
V2M_PATH = "outputs/markdown/wa-meaning-clusters-v2-2026-05-04.json"
V4_PATH = "outputs/markdown/wa-term-anchor-v4-20260504.json"
V4_SUMMARY_PATH = "outputs/markdown/wa-term-anchor-v4-20260504-summary.md"
V4_UNASSIGNED_PATH = (
    "outputs/markdown/wa-term-anchor-v4-20260504-unassigned.md"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    print("Loading v3 anchor...", flush=True)
    with open(V3_PATH, encoding="utf-8") as f:
        v3 = json.load(f)
    print("Loading v2 meaning-clusters...", flush=True)
    with open(V2M_PATH, encoding="utf-8") as f:
        v2m = json.load(f)

    v3_terms = v3.get("term_anchors", {})
    print(f"  v3 term_anchors: {len(v3_terms):,}", flush=True)

    # Build assignment map from v2 meaning-clusters file
    assign = {}
    cluster_labels = {}
    cluster_kinds = {}  # "named" | "T2" | "FLAG"
    for cid, c in v2m["clusters"].items():
        cluster_labels[cid] = c["label"]
        if cid == "T2":
            kind = "T2"
        elif cid == "FLAG":
            kind = "FLAG"
        else:
            kind = "named"
        cluster_kinds[cid] = kind
        for m in c["members"]:
            assign[m["strong"]] = (cid, c["label"], kind)
    print(f"  v2 cluster assignments: {len(assign):,}", flush=True)
    n_named = sum(1 for k in cluster_kinds.values() if k == "named")
    print(f"  named clusters: {n_named}, T2: 1, FLAG: 1", flush=True)

    # Apply v2 on top of v3
    v4_terms = {k: dict(v) for k, v in v3_terms.items()}
    n_applied = 0
    n_named_applied = 0
    n_t2_applied = 0
    n_flag_applied = 0
    n_already_same = 0
    n_changed = 0
    n_only_in_v2 = 0
    audit_changes = []

    # First pass: apply assignments to existing v3 terms
    for strong, term in v4_terms.items():
        if strong in assign:
            new_cid, new_label, kind = assign[strong]
            prev_cid = term.get("cluster_id")
            prev_label = term.get("cluster_label")
            if prev_cid == new_cid:
                n_already_same += 1
            else:
                term["cluster_id"] = new_cid
                term["cluster_label"] = new_label
                if kind == "named":
                    term["cluster_source"] = "meaning_v2"
                    n_named_applied += 1
                elif kind == "T2":
                    term["cluster_source"] = "meaning_v2_T2"
                    n_t2_applied += 1
                else:
                    term["cluster_source"] = "meaning_v2_FLAG"
                    n_flag_applied += 1
                n_changed += 1
                audit_changes.append({
                    "strong": strong,
                    "from_cluster": prev_cid,
                    "from_label": prev_label,
                    "to_cluster": new_cid,
                    "to_label": new_label,
                    "kind": kind,
                })
            n_applied += 1

    # Second pass: any terms in v2 file but not in v3 anchor
    only_in_v2 = []
    for strong, (cid, label, kind) in assign.items():
        if strong not in v4_terms:
            n_only_in_v2 += 1
            only_in_v2.append((strong, cid, label, kind))
            v4_terms[strong] = {
                "strong": strong,
                "cluster_id": cid,
                "cluster_label": label,
                "cluster_source": (
                    "meaning_v2" if kind == "named"
                    else f"meaning_v2_{kind}"
                ),
                "legacy_cluster_id": None,
                "legacy_cluster_label": None,
                "bucket": None,
                "lang": None,
                "transliteration": None,
                "gloss": None,
                "verse_count": None,
                "multi_term_pct": None,
            }

    # Reconciliation: identify terms still on legacy (not yet assigned to any
    # M / T2 / FLAG cluster in v2)
    unassigned = []
    for strong, term in v4_terms.items():
        cid = term.get("cluster_id") or ""
        if cid not in assign and not cid.startswith(("M", "T", "F")):
            # term is still on legacy H/G or other prefix
            unassigned.append({
                "strong": strong,
                "lang": term.get("lang"),
                "gloss": term.get("gloss"),
                "transliteration": term.get("transliteration"),
                "verse_count": term.get("verse_count"),
                "bucket": term.get("bucket"),
                "current_cluster_id": cid,
                "current_cluster_label": term.get("cluster_label"),
                "cluster_source": term.get("cluster_source"),
            })

    # Build v4
    v4 = dict(v3)
    v4["meta"] = dict(v3["meta"])
    v4["meta"]["version"] = "v4"
    v4["meta"]["generated"] = now_iso()
    v4["meta"]["v2_meaning_source"] = V2M_PATH
    v4["meta"]["n_v2_named_applied"] = n_named_applied
    v4["meta"]["n_v2_T2_applied"] = n_t2_applied
    v4["meta"]["n_v2_FLAG_applied"] = n_flag_applied
    v4["meta"]["n_v2_already_same"] = n_already_same
    v4["meta"]["n_only_in_v2"] = n_only_in_v2
    v4["meta"]["n_terms_total"] = len(v4_terms)
    v4["meta"]["n_terms_unassigned_after_v2"] = len(unassigned)
    # Refresh cluster_labels with the v2 catalogue
    v4["meaning_cluster_labels"] = cluster_labels
    v4["term_anchors"] = v4_terms
    # Rebuild cluster_index
    v4_clusters = defaultdict(list)
    for s, t in v4_terms.items():
        v4_clusters[t.get("cluster_id") or "(none)"].append(s)
    v4["cluster_index"] = {
        cid: sorted(strongs)
        for cid, strongs in sorted(v4_clusters.items())
    }
    v4["v2_audit_changes"] = audit_changes
    v4["v2_only_terms"] = [
        {"strong": s, "cluster_id": c, "cluster_label": l, "kind": k}
        for s, c, l, k in only_in_v2
    ]

    with open(V4_PATH, "w", encoding="utf-8") as f:
        json.dump(v4, f, indent=2, ensure_ascii=False)
    print(f"Wrote: {V4_PATH}", flush=True)

    # ---- Summary markdown ----
    src_counts = Counter(t.get("cluster_source") for t in v4_terms.values())
    cluster_member_counts = Counter(
        t.get("cluster_id") for t in v4_terms.values()
    )

    lines = []
    lines.append("# Term-anchor v4 — v2 meaning-clusters applied\n")
    lines.append(f"**Generated:** {v4['meta']['generated']}  ")
    lines.append(f"**Built from:** v3 + "
                 f"`{os.path.basename(V2M_PATH)}` "
                 f"(45 M-clusters + T2 + FLAG)  \n")
    lines.append("## Headline\n")
    lines.append(f"- v4 term_anchors: **{len(v4_terms):,}**")
    lines.append(f"- Assignments processed from v2 file: "
                 f"**{len(assign):,}**")
    lines.append(f"- Changed cluster as a result: **{n_changed:,}**")
    lines.append(f"  - to a named M-cluster: {n_named_applied:,}")
    lines.append(f"  - to T2 (supplementary): {n_t2_applied:,}")
    lines.append(f"  - to FLAG (review): {n_flag_applied:,}")
    lines.append(f"- Already on target cluster (no-op): "
                 f"**{n_already_same:,}**")
    lines.append(f"- Terms in v2 file but absent from v3 anchor: "
                 f"**{n_only_in_v2}**")
    lines.append(f"- **Unassigned after v2 applied:** "
                 f"**{len(unassigned):,}** "
                 "(see [v4 unassigned report]"
                 "(wa-term-anchor-v4-20260504-unassigned.md))")
    lines.append("")
    lines.append("## Cluster-source breakdown (v4)\n")
    lines.append("| Source | Count |")
    lines.append("|---|---:|")
    for s, n in src_counts.most_common():
        lines.append(f"| {s or '(none)'} | {n} |")
    lines.append("")
    lines.append("## v4 cluster sizes — top 25 named characteristics\n")
    lines.append("| Cluster | Label | Members |")
    lines.append("|---|---|---:|")
    named_only = [(c, n) for c, n in cluster_member_counts.most_common()
                  if c and c.startswith("M")]
    for cid, n in named_only[:25]:
        lines.append(f"| {cid} | "
                     f"{cluster_labels.get(cid, '?')} | {n} |")
    lines.append("")
    lines.append("## Special clusters\n")
    lines.append(f"- **T2 — Supplementary:** "
                 f"{cluster_member_counts.get('T2', 0):,} members")
    lines.append(f"- **FLAG — Flagged for Review:** "
                 f"{cluster_member_counts.get('FLAG', 0):,} members")

    with open(V4_SUMMARY_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {V4_SUMMARY_PATH}", flush=True)

    # ---- Unassigned report ----
    ua_lines = []
    ua_lines.append("# Unassigned terms after v2 reconciliation\n")
    ua_lines.append(f"**Generated:** {v4['meta']['generated']}  ")
    ua_lines.append(f"**Total unassigned:** {len(unassigned):,} of "
                    f"{len(v4_terms):,}")
    ua_lines.append("")
    ua_lines.append("These terms are in the v3 term-anchor but were not "
                    "assigned to any cluster in the v2 meaning-clusters file "
                    "(no M-cluster, not T2, not FLAG). Their `cluster_id` "
                    "still references a legacy v1 cluster (H/G prefix) or is "
                    "unset.\n")
    ua_lines.append("## Distribution by current bucket\n")
    bucket_counts = Counter(u.get("bucket") or "(none)" for u in unassigned)
    ua_lines.append("| Bucket | Count |")
    ua_lines.append("|---|---:|")
    for b, n in bucket_counts.most_common():
        ua_lines.append(f"| {b} | {n} |")
    ua_lines.append("")
    ua_lines.append("## Distribution by current legacy cluster\n")
    legacy_counts = Counter(
        u.get("current_cluster_id") or "(none)" for u in unassigned
    )
    ua_lines.append("| Legacy cluster | Count |")
    ua_lines.append("|---|---:|")
    for c, n in legacy_counts.most_common():
        ua_lines.append(f"| {c} | {n} |")
    ua_lines.append("")
    ua_lines.append("## Distribution by language\n")
    lang_counts = Counter(u.get("lang") or "(none)" for u in unassigned)
    ua_lines.append("| Lang | Count |")
    ua_lines.append("|---|---:|")
    for l, n in lang_counts.most_common():
        ua_lines.append(f"| {l} | {n} |")
    ua_lines.append("")
    ua_lines.append("## Full unassigned term list\n")
    ua_lines.append("Sorted by bucket then by Strong's number.\n")
    ua_lines.append("| Strong's | Lang | Translit | Gloss | Verses | "
                    "Bucket | Legacy cluster |")
    ua_lines.append("|---|---|---|---|---:|---|---|")
    for u in sorted(
        unassigned,
        key=lambda x: (x.get("bucket") or "ZZ", x.get("strong") or "")
    ):
        ua_lines.append(
            f"| {u.get('strong', '')} | "
            f"{u.get('lang', '') or ''} | "
            f"{u.get('transliteration', '') or ''} | "
            f"{u.get('gloss', '') or ''} | "
            f"{u.get('verse_count', '') if u.get('verse_count') is not None else ''} | "
            f"{u.get('bucket', '') or ''} | "
            f"{u.get('current_cluster_id', '') or ''} |"
        )

    with open(V4_UNASSIGNED_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(ua_lines) + "\n")
    print(f"Wrote: {V4_UNASSIGNED_PATH}", flush=True)

    print(f"\nSummary: changed={n_changed:,} same={n_already_same:,} "
          f"only_in_v2={n_only_in_v2:,} unassigned={len(unassigned):,}",
          flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
