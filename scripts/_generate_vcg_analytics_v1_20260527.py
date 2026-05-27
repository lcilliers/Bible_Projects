"""Cross-cluster VCG analytics.

Surfaces what's actually in the DB for verse_context_group rows so the
researcher can see what VCGs hold before deciding whether v3_0 retains them.

Lenses:
  §1 Cluster-level coverage — which clusters have VCGs, totals, ratios
  §2 VCG size distribution — histogram of verses-per-VCG (singleton VCGs
     are a key signal: do we create 1-verse VCGs?)
  §3 VCG description analysis — length, similarity to parent sub-group
     description (the test: does the VCG description say something
     analytically distinct?)
  §4 Analytical-rent test — how often each VCG is cited by code in
     cluster_finding.finding_text (the test: do Phase 9 findings actually
     refer to VCG codes, or just sub-group codes?)
  §5 Cross-cluster pattern survey — VCGs grouped by description keywords;
     do similar within-sub-group axes appear across clusters?
  §6 Per-cluster VCG inventory (appendix) — every VCG in every active
     cluster, with member count and description excerpt

Output: Workflow/Clusters/wa-vcg-analytics-v1-{date}.md
"""
from __future__ import annotations
import io
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
OUT_DIR = REPO / "Workflow" / "Clusters"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
TODAY = datetime.now(timezone.utc).strftime("%Y%m%d")

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "in", "on", "at", "by", "with",
    "from", "to", "is", "as", "be", "are", "was", "were", "for", "this",
    "that", "these", "those", "its", "their", "it", "not", "no", "but",
    "which", "who", "whom", "where", "when", "what", "how", "any", "all",
    "some", "more", "most", "less", "than", "into", "across", "through",
    "between", "within", "under", "over", "above", "below",
    "verses", "verse", "person", "inner", "being", "content",
}


def tokens(text: str) -> set[str]:
    if not text:
        return set()
    parts = re.split(r"[\s,.;:()\-/—]+", text.lower())
    return {p for p in parts if p and p not in STOPWORDS and len(p) > 2 and not p.isdigit()}


def main() -> int:
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"wa-vcg-analytics-v1-{TODAY}.md"

    # ============================================================
    # GATHER
    # ============================================================

    # Get all active VCGs (no per-row subqueries — gather aggregates separately)
    vcg_base = conn.execute("""
        SELECT id AS vcg_id, group_code, context_description, notes
        FROM verse_context_group
        WHERE COALESCE(delete_flagged,0)=0
    """).fetchall()

    # Gather per-VCG aggregates in one pass
    vcg_agg = {}  # vcg_id -> {cluster_code, subgroup_code, n_verses, n_anchors}
    for r in conn.execute("""
        SELECT vc.group_id AS vcg_id,
               mt.cluster_code,
               cs.subgroup_code,
               COUNT(DISTINCT vc.id) AS n_verses,
               SUM(CASE WHEN vc.is_anchor=1 THEN 1 ELSE 0 END) AS n_anchors
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        WHERE vc.group_id IS NOT NULL
          AND vc.is_relevant=1
          AND COALESCE(vc.delete_flagged,0)=0
          AND COALESCE(mt.delete_flagged,0)=0
        GROUP BY vc.group_id, mt.cluster_code, cs.subgroup_code
    """).fetchall():
        vid = r["vcg_id"]
        # If a VCG spans multiple sub-groups (rare), keep the first
        if vid not in vcg_agg:
            vcg_agg[vid] = {
                "cluster_code": r["cluster_code"],
                "subgroup_code": r["subgroup_code"],
                "n_verses": r["n_verses"],
                "n_anchors": r["n_anchors"] or 0,
            }
        else:
            # Add verse counts (in case of split-cluster sub-groups)
            vcg_agg[vid]["n_verses"] += r["n_verses"]
            vcg_agg[vid]["n_anchors"] += r["n_anchors"] or 0

    # Compose vcg_rows like the previous query produced
    vcg_rows = []
    for r in vcg_base:
        agg = vcg_agg.get(r["vcg_id"], {})
        vcg_rows.append({
            "vcg_id": r["vcg_id"],
            "group_code": r["group_code"],
            "context_description": r["context_description"],
            "notes": r["notes"],
            "cluster_code": agg.get("cluster_code"),
            "subgroup_code": agg.get("subgroup_code"),
            "n_verses": agg.get("n_verses", 0),
            "n_anchors": agg.get("n_anchors", 0),
        })

    # Sub-group descriptions by id and code
    subgroup_desc = {
        (r["cluster_code"], r["subgroup_code"]): r["core_description"]
        for r in conn.execute("""
            SELECT cluster_code, subgroup_code, core_description
            FROM cluster_subgroup
            WHERE COALESCE(delete_flagged,0)=0
        """).fetchall()
    }

    # Cluster status map
    cluster_status = {r["cluster_code"]: r["status"] for r in conn.execute(
        "SELECT cluster_code, status FROM cluster"
    ).fetchall()}

    # Total cluster_finding bodies (lowercase concatenated) for citation test
    all_findings_text = "\n".join(
        (r["finding_text"] or "").lower()
        for r in conn.execute(
            "SELECT finding_text FROM cluster_finding WHERE COALESCE(delete_flagged,0)=0"
        ).fetchall()
    )

    # Per-cluster aggregates
    by_cluster: dict[str, list[dict]] = defaultdict(list)
    orphan_vcgs: list[dict] = []  # VCGs with no active verses (shouldn't exist but might)
    for r in vcg_rows:
        if r["cluster_code"]:
            by_cluster[r["cluster_code"]].append(dict(r))
        else:
            orphan_vcgs.append(dict(r))

    # ============================================================
    # BUILD REPORT
    # ============================================================

    L: list[str] = []
    L.append("# VCG analytics — what's actually in the database")
    L.append("")
    L.append(f"_Generated: {NOW}_  ")
    L.append(f"_Source: `database/bible_research.db` — `verse_context_group` + `vcg_term` + `verse_context.group_id`_")
    L.append("")
    L.append("**Purpose:** surface what the VCG layer holds across all clusters so the v3_0 decision (drop VCGs as Phase 7 design layer) can be made with full visibility of what would become legacy.")
    L.append("")
    L.append("---")
    L.append("")

    # §1 Coverage
    L.append("## §1. Cluster-level coverage")
    L.append("")
    L.append("Clusters with active VCGs in the DB and their analytical state.")
    L.append("")
    L.append("| Cluster | Status | # VCGs | # is_rel verses (in VCGs) | Avg V/VCG | Med V/VCG | Anchors |")
    L.append("|---|---|---:|---:|---:|---:|---:|")
    n_vcg_total = 0
    n_v_total = 0
    n_anchor_total = 0
    for code in sorted(by_cluster.keys()):
        vcgs = by_cluster[code]
        n_vcg = len(vcgs)
        n_v = sum(v["n_verses"] for v in vcgs)
        n_anchor = sum(v["n_anchors"] or 0 for v in vcgs)
        sizes = sorted([v["n_verses"] for v in vcgs])
        median_v = sizes[len(sizes)//2] if sizes else 0
        avg_v = n_v / n_vcg if n_vcg else 0
        L.append(f"| **{code}** | {cluster_status.get(code, '?')} | {n_vcg} | {n_v} | {avg_v:.1f} | {median_v} | {n_anchor} |")
        n_vcg_total += n_vcg
        n_v_total += n_v
        n_anchor_total += n_anchor
    L.append(f"| **TOTAL** | — | **{n_vcg_total}** | **{n_v_total:,}** | — | — | **{n_anchor_total}** |")
    L.append("")
    if orphan_vcgs:
        L.append(f"**Orphan VCGs** (active VCG row with zero active is_relevant verses): {len(orphan_vcgs)}")
        for v in orphan_vcgs[:10]:
            L.append(f"- `{v['group_code']}` (vcg_id={v['vcg_id']}) — `{(v['context_description'] or '')[:80]}`")
    L.append("")
    L.append("---")
    L.append("")

    # §2 Size distribution
    L.append("## §2. VCG size distribution")
    L.append("")
    L.append("Histogram of verses per VCG. **Singleton VCGs (1 verse) are a key signal — do we create VCGs that hold just one verse?**")
    L.append("")
    all_sizes = [v["n_verses"] for vcgs in by_cluster.values() for v in vcgs]
    bins = [(1, 1), (2, 3), (4, 5), (6, 10), (11, 20), (21, 50), (51, 100), (101, 10000)]
    L.append("| Size range | # VCGs | % of total | Cumulative % |")
    L.append("|---|---:|---:|---:|")
    total = len(all_sizes)
    cum = 0
    for lo, hi in bins:
        n_in = sum(1 for s in all_sizes if lo <= s <= hi)
        cum += n_in
        label = f"{lo} verse" if lo == hi == 1 else (f"{lo}-{hi} verses" if hi < 10000 else f"{lo}+ verses")
        pct = 100 * n_in / total if total else 0
        cum_pct = 100 * cum / total if total else 0
        L.append(f"| {label} | {n_in} | {pct:.1f}% | {cum_pct:.1f}% |")
    L.append(f"| **Total** | **{total}** | 100% | — |")
    L.append("")

    # Specific singleton list (the most direct waste signal)
    singletons = [v for vcgs in by_cluster.values() for v in vcgs if v["n_verses"] == 1]
    L.append(f"### §2.1 Singleton VCGs ({len(singletons)} total — each holds exactly 1 verse)")
    L.append("")
    if singletons:
        L.append("These are the most direct signal for 'VCG layer overhead without analytical density.' One verse cannot internally cluster; the VCG description is effectively a per-verse note.")
        L.append("")
        L.append("| Cluster | VCG code | Description excerpt |")
        L.append("|---|---|---|")
        for v in sorted(singletons, key=lambda x: (x["cluster_code"], x["group_code"]))[:50]:
            desc = (v["context_description"] or "")[:100]
            L.append(f"| {v['cluster_code']} | `{v['group_code']}` | {desc} |")
        if len(singletons) > 50:
            L.append(f"| … | … and {len(singletons)-50} more singletons |  |")
    L.append("")
    L.append("---")
    L.append("")

    # §3 Description distinctness from parent sub-group
    L.append("## §3. VCG description distinctness from parent sub-group")
    L.append("")
    L.append("For each VCG: how much new analytical content does the VCG description carry over its parent sub-group's `core_description`? Measured by Jaccard token similarity (1.0 = identical token set; 0.0 = no shared tokens). **High similarity = VCG description duplicates sub-group description.**")
    L.append("")
    pairs: list[tuple[str, str, str, float, int]] = []  # (cluster, vcg_code, subgroup_code, jaccard, n_verses)
    for code, vcgs in by_cluster.items():
        for v in vcgs:
            sg_code = v["subgroup_code"]
            sg_desc = subgroup_desc.get((code, sg_code), "") if sg_code else ""
            vcg_desc = v["context_description"] or ""
            t_vcg = tokens(vcg_desc)
            t_sg = tokens(sg_desc)
            if t_vcg and t_sg:
                jacc = len(t_vcg & t_sg) / len(t_vcg | t_sg)
            elif not t_vcg and not t_sg:
                jacc = 1.0
            else:
                jacc = 0.0
            pairs.append((code, v["group_code"], sg_code or "?", jacc, v["n_verses"]))
    bins_j = [(0.0, 0.1), (0.1, 0.2), (0.2, 0.3), (0.3, 0.4), (0.4, 0.5), (0.5, 0.7), (0.7, 1.01)]
    L.append("| Jaccard similarity (VCG desc vs parent sub-group desc) | # VCGs | % |")
    L.append("|---|---:|---:|")
    for lo, hi in bins_j:
        n_in = sum(1 for p in pairs if lo <= p[3] < hi)
        pct = 100 * n_in / len(pairs) if pairs else 0
        rng = f"{lo:.1f} <= j < {hi:.2f}" if hi < 1.0 else f"{lo:.1f} <= j <= 1.0"
        L.append(f"| {rng} | {n_in} | {pct:.1f}% |")
    L.append("")
    avg_jacc = sum(p[3] for p in pairs) / len(pairs) if pairs else 0
    L.append(f"**Average Jaccard:** {avg_jacc:.2f}. (Lower = VCG descriptions analytically distinct from sub-group; higher = VCG descriptions overlap sub-group content.)")
    L.append("")
    L.append("---")
    L.append("")

    # §4 Analytical-rent test
    L.append("## §4. Analytical-rent test — VCG code citation in `cluster_finding`")
    L.append("")
    L.append("For each cluster, count how many of its VCGs are mentioned by code at least once in any `cluster_finding.finding_text` body. **A VCG that is never cited is analytical overhead that paid no Phase 9 rent.**")
    L.append("")
    L.append("| Cluster | # VCGs | # cited at least once | Citation rate |")
    L.append("|---|---:|---:|---:|")
    total_vcg = 0
    total_cited = 0
    for code in sorted(by_cluster.keys()):
        vcgs = by_cluster[code]
        n_cited = sum(1 for v in vcgs if v["group_code"].lower() in all_findings_text)
        n_vcg = len(vcgs)
        rate = 100 * n_cited / n_vcg if n_vcg else 0
        total_vcg += n_vcg
        total_cited += n_cited
        L.append(f"| {code} | {n_vcg} | {n_cited} | {rate:.0f}% |")
    rate_total = 100 * total_cited / total_vcg if total_vcg else 0
    L.append(f"| **Total** | **{total_vcg}** | **{total_cited}** | **{rate_total:.0f}%** |")
    L.append("")
    L.append("**Interpretation:** the citation rate is the most direct measure of whether VCGs paid analytical rent during Phase 9. Codes that never appear in any finding text were structural overhead. (Note: synthesis findings may cite sub-group codes more than VCG codes, which is consistent with Phase 9 firing at characteristic scope.)")
    L.append("")
    L.append("---")
    L.append("")

    # §5 Cross-cluster pattern survey
    L.append("## §5. Cross-cluster VCG description token patterns")
    L.append("")
    L.append("Tokens appearing in VCG descriptions across multiple clusters surface common within-sub-group axes (e.g. 'external' / 'internal' / 'volitional' / 'corporate'). Filtered to tokens with cluster-spread >= 3.")
    L.append("")
    tok_cluster: dict[str, set[str]] = defaultdict(set)
    tok_count: Counter = Counter()
    for code, vcgs in by_cluster.items():
        for v in vcgs:
            for t in tokens(v["context_description"] or ""):
                tok_cluster[t].add(code)
                tok_count[t] += 1
    cross_tokens = [
        (t, len(clus), tok_count[t]) for t, clus in tok_cluster.items() if len(clus) >= 3
    ]
    cross_tokens.sort(key=lambda x: (-x[1], -x[2]))
    L.append("| Token | # clusters | # VCG descs |")
    L.append("|---|---:|---:|")
    for t, n_c, n_t in cross_tokens[:30]:
        L.append(f"| `{t}` | {n_c} | {n_t} |")
    L.append("")
    L.append("---")
    L.append("")

    # §6 Appendix: per-cluster inventory (just title + size; full descriptions would balloon)
    L.append("## §6. Per-cluster VCG inventory (compact)")
    L.append("")
    L.append("Every active VCG, by cluster, with verse count and description excerpt (first 120 chars).")
    L.append("")
    for code in sorted(by_cluster.keys()):
        vcgs = by_cluster[code]
        L.append(f"### {code} ({len(vcgs)} VCGs · status: {cluster_status.get(code, '?')})")
        L.append("")
        L.append("| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |")
        L.append("|---|---|---:|---:|:-:|---|")
        for v in sorted(vcgs, key=lambda x: x["group_code"]):
            desc = ((v["context_description"] or "").replace("\n", " "))[:120]
            cited = "✓" if v["group_code"].lower() in all_findings_text else "—"
            L.append(f"| `{v['group_code']}` | {v['subgroup_code'] or '?'} | {v['n_verses']} | {v['n_anchors'] or 0} | {cited} | {desc} |")
        L.append("")

    L.append("---")
    L.append("")
    L.append("## §7. Summary")
    L.append("")
    L.append(f"- **Clusters with active VCGs:** {len(by_cluster)}")
    L.append(f"- **Total active VCGs:** {n_vcg_total}")
    L.append(f"- **Singleton VCGs (1 verse):** {len(singletons)} ({100*len(singletons)/n_vcg_total:.1f}% of all VCGs)")
    L.append(f"- **VCGs cited in cluster_finding:** {total_cited} of {total_vcg} ({rate_total:.0f}%)")
    L.append(f"- **Avg Jaccard similarity** VCG-desc vs sub-group-desc: {avg_jacc:.2f}")
    L.append(f"- **Cross-cluster description tokens (≥3 clusters):** {len(cross_tokens)}")
    L.append("")
    L.append("**For the v3_0 decision:** §2.1 (singleton count), §4 (citation rate), and §3 (Jaccard) are the three direct rent-tests. A low citation rate combined with a high singleton fraction and high Jaccard would argue strongly for dropping the layer. A high citation rate with low singleton fraction would argue for keeping it.")

    out_path.write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote: {out_path.relative_to(REPO)}")
    print(f"  Clusters with VCGs:           {len(by_cluster)}")
    print(f"  Total active VCGs:            {n_vcg_total}")
    print(f"  Singleton VCGs:               {len(singletons)} ({100*len(singletons)/n_vcg_total:.1f}%)")
    print(f"  VCGs cited in cluster_finding: {total_cited}/{total_vcg} ({rate_total:.0f}%)")
    print(f"  Avg Jaccard sim vs sub-group: {avg_jacc:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
