"""_apply_supplement_clusters_v1_20260504.py — read-only assembly.

Applies a researcher-supplied supplement of meaning-cluster assignments on top
of term-anchor v2, producing v3.

Inputs:
  outputs/markdown/wa-term-anchor-v2-20260504.json
  outputs/markdown/wa-meaning-clusters-supplement-v1-20260504.json

Outputs:
  outputs/markdown/wa-term-anchor-v3-20260504.json
  outputs/markdown/wa-term-anchor-v3-20260504-summary.md

Logic:
  - For every assignment in the supplement, find the term in v2.
  - If found: update cluster_id, cluster_label, set cluster_source =
    'meaning_v1_supplement'. Preserve legacy_cluster_id from v2.
    Record what the previous cluster_id was (in case it was already meaning_v1).
  - If not found: report as missing.
  - Output v3 with same shape as v2 + a per-supplement-row audit trail.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone

V2_PATH = "outputs/markdown/wa-term-anchor-v2-20260504.json"
SUPPLEMENT_PATH = (
    "outputs/markdown/wa-meaning-clusters-supplement-v1-20260504.json"
)
V3_PATH = "outputs/markdown/wa-term-anchor-v3-20260504.json"
V3_SUMMARY_PATH = "outputs/markdown/wa-term-anchor-v3-20260504-summary.md"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    print("Loading v2 anchor...", flush=True)
    with open(V2_PATH, encoding="utf-8") as f:
        v2 = json.load(f)
    print("Loading supplement...", flush=True)
    with open(SUPPLEMENT_PATH, encoding="utf-8") as f:
        sup = json.load(f)

    v2_terms = v2.get("term_anchors", {})
    cluster_labels = v2.get("meaning_cluster_labels", {})
    print(f"  v2 term_anchors: {len(v2_terms):,}", flush=True)
    print(f"  supplement assignments: "
          f"{len(sup['assignments']):,}", flush=True)

    # Validate cluster IDs in supplement exist in v2 catalogue
    unknown_clusters = set()
    for a in sup["assignments"]:
        if a["to_cluster"] not in cluster_labels:
            unknown_clusters.add(a["to_cluster"])
    if unknown_clusters:
        print(f"WARN: unknown M-cluster IDs referenced in supplement: "
              f"{unknown_clusters}", flush=True)

    # Apply
    v3_terms = {k: dict(v) for k, v in v2_terms.items()}
    audit = []
    n_applied = 0
    n_missing = 0
    n_already_same = 0
    cluster_destination = Counter()

    for a in sup["assignments"]:
        strong = a["strong"]
        target = a["to_cluster"]
        target_label = cluster_labels.get(target, "(UNKNOWN)")
        if strong not in v3_terms:
            audit.append({
                "strong": strong,
                "gloss_supplied": a.get("gloss"),
                "from_cluster": None,
                "to_cluster": target,
                "outcome": "MISSING",
            })
            n_missing += 1
            continue
        prev = v3_terms[strong].get("cluster_id")
        if prev == target:
            audit.append({
                "strong": strong,
                "gloss_supplied": a.get("gloss"),
                "from_cluster": prev,
                "to_cluster": target,
                "outcome": "ALREADY_SAME",
            })
            n_already_same += 1
            continue
        v3_terms[strong]["cluster_id"] = target
        v3_terms[strong]["cluster_label"] = target_label
        v3_terms[strong]["cluster_source"] = "meaning_v1_supplement"
        if "supplement_note" in a or a.get("note"):
            v3_terms[strong]["supplement_note"] = a.get("note")
        audit.append({
            "strong": strong,
            "gloss_actual": v3_terms[strong].get("gloss"),
            "gloss_supplied": a.get("gloss"),
            "from_cluster": prev,
            "from_label": v2_terms.get(strong, {}).get("cluster_label"),
            "to_cluster": target,
            "to_label": target_label,
            "outcome": "APPLIED",
        })
        n_applied += 1
        cluster_destination[target] += 1

    # Build v3
    v3 = dict(v2)
    v3["meta"] = dict(v2["meta"])
    v3["meta"]["version"] = "v3"
    v3["meta"]["generated"] = now_iso()
    v3["meta"]["supplement_source"] = SUPPLEMENT_PATH
    v3["meta"]["n_supplement_applied"] = n_applied
    v3["meta"]["n_supplement_already_same"] = n_already_same
    v3["meta"]["n_supplement_missing"] = n_missing
    v3["term_anchors"] = v3_terms
    # Rebuild cluster_index
    from collections import defaultdict
    v3_clusters = defaultdict(list)
    for s, t in v3_terms.items():
        v3_clusters[t.get("cluster_id") or "(none)"].append(s)
    v3["cluster_index"] = {
        cid: sorted(strongs)
        for cid, strongs in sorted(v3_clusters.items())
    }
    v3["supplement_audit"] = audit

    with open(V3_PATH, "w", encoding="utf-8") as f:
        json.dump(v3, f, indent=2, ensure_ascii=False)
    print(f"Wrote: {V3_PATH}", flush=True)

    # Summary md
    src_counts = Counter(t.get("cluster_source") for t in v3_terms.values())
    cluster_counts = Counter(
        t.get("cluster_id") for t in v3_terms.values()
        if (t.get("cluster_id") or "").startswith("M")
    )
    legacy_kept = Counter(
        t.get("cluster_id") for t in v3_terms.values()
        if t.get("cluster_id") and not str(t["cluster_id"]).startswith("M")
    )

    lines = []
    lines.append("# Term-anchor v3 — supplement applied\n")
    lines.append(f"**Generated:** {v3['meta']['generated']}  ")
    lines.append(f"**Built from:** v2 + "
                 f"`{os.path.basename(SUPPLEMENT_PATH)}`  \n")
    lines.append("## Headline\n")
    lines.append(f"- Supplement assignments: "
                 f"**{len(sup['assignments'])}**")
    lines.append(f"- Applied: **{n_applied}**")
    lines.append(f"- Already on target cluster (no-op): "
                 f"**{n_already_same}**")
    lines.append(f"- Missing from v2 anchor (could not apply): "
                 f"**{n_missing}**")
    if n_missing:
        missing_list = [a for a in audit if a["outcome"] == "MISSING"]
        lines.append("\n### Missing terms (need researcher attention)\n")
        lines.append("| Strong's | Gloss supplied | Target |")
        lines.append("|---|---|---|")
        for r in missing_list:
            lines.append(f"| {r['strong']} | "
                         f"{r.get('gloss_supplied', '')} | "
                         f"{r['to_cluster']} |")
    lines.append("\n## Per-cluster destination of applied terms\n")
    lines.append("| Cluster | Label | Terms added |")
    lines.append("|---|---|---:|")
    for cid, n in cluster_destination.most_common():
        lines.append(f"| {cid} | {cluster_labels.get(cid, '?')} | {n} |")
    lines.append("\n## Per-term audit (applied)\n")
    lines.append("| Strong's | Gloss | From | To |")
    lines.append("|---|---|---|---|")
    for r in audit:
        if r["outcome"] != "APPLIED":
            continue
        from_disp = r.get("from_cluster") or "(none)"
        if r.get("from_label"):
            from_disp = f"{from_disp} / {r['from_label']}"
        to_disp = f"{r['to_cluster']} / {r.get('to_label', '?')}"
        gloss = r.get("gloss_actual") or r.get("gloss_supplied") or ""
        lines.append(f"| {r['strong']} | {gloss} | "
                     f"{from_disp} | {to_disp} |")

    lines.append("\n## Cluster-source breakdown (v3)\n")
    lines.append("| Source | Count |")
    lines.append("|---|---:|")
    for s, n in src_counts.most_common():
        lines.append(f"| {s} | {n} |")
    lines.append("\n## Meaning-cluster sizes (top 20, v3)\n")
    lines.append("| Cluster | Label | Members |")
    lines.append("|---|---|---:|")
    for cid, n in cluster_counts.most_common(20):
        lines.append(f"| {cid} | {cluster_labels.get(cid, '?')} | {n} |")
    lines.append("\n## Legacy clusters still holding terms (top 15)\n")
    lines.append("| Legacy cluster | Terms |")
    lines.append("|---|---:|")
    for cid, n in legacy_kept.most_common(15):
        lines.append(f"| {cid} | {n} |")

    with open(V3_SUMMARY_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {V3_SUMMARY_PATH}", flush=True)

    print(f"\nSummary: applied={n_applied} "
          f"same={n_already_same} missing={n_missing}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
