"""Produce the analytical-lens addendum to the M02 dissolution comparison.

Builds three researcher-requested views on the M02 old → new VCG transition:

  Lens 1 — Old VCGs that are 'very different / not repeated' in the new structure.
           Identified by low semantic match between old.context_description and any
           new VCG's description (across all members of any new VCG).

  Lens 2 — Old VCGs with high semantic similarity to a new VCG (KEEP-EQUIVALENT
           candidates). Pairs where old + new descriptions share substantive vocab
           AND the old VCG's members map predominantly to that new VCG.

  Lens 3 — New VCGs that are 'novel synthesis' — not represented in any old VCG.
           Identified by:
           (a) the new VCG's member set is dominated by previously-unrouted vc rows
               (e.g. UT verses from Phase 1, which have no old group_id), OR
           (b) low semantic match to any old VCG description.

The script consumes:
  - The pre-Phase-7 routing snapshot (vc → old_group_id)
  - The post-Phase-7 routing (vc → new_group_id, via cluster_finding's source)
  - context_description fields for old and new VCGs in the cluster

Usage:
  python scripts/_generate_vcg_analytical_lens_v1_20260516.py --m-cluster M02 \\
    --new-vcg-min-id 3762 \\
    --pre-routing-snapshot Sessions/Session_Clusters/M02/WA-M02-pre-phase7-routing-snapshot-v1-20260516.json

Output:
  Sessions/Session_Clusters/{code}/WA-{code}-vcg-analytical-lens-v1-{date}.md
"""
from __future__ import annotations
import argparse, json, re, sqlite3, sys
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"

# Vocabulary trim — exclude stopwords and generic theological/analytical filler
STOPWORDS = {
    "the","a","an","and","or","but","of","to","in","is","that","this","these","those",
    "it","its","as","for","with","by","on","at","be","are","was","were","been","being",
    "term","names","describes","name","what","which","when","where",
    "from","into","out","up","down","over","under","not","no","than","then","so","also",
    "one","two","three","first","second","third","more","most","less","least",
    "him","her","his","hers","they","them","their","he","she","i","you","we","us","our","my",
    "do","does","did","done","have","has","had","will","would","can","could","should","may","might",
    "shall","must","being","becomes","become","came","come","comes","goes","go","went",
    "says","said","speak","spoke","spoken","tells","tell","told",
    "characteristic","inner","verse","verses","scripture","biblical","passage","content",
    "register","register's","registers","cluster","sub-group","subgroup",
    "vcg","vcgs","group","groups","section","term","terms","person","persons",
    "human","divine","god","yhwh","lord","jesus","christ","spirit","being",
    "evidence","evidenced","evidences","corpus","meaning","meanings","analysis",
    "phase","passage","verse_id","verse-context","references","reference",
    "vc_id","vr_id","mti","strong","strongs","translit",
    "anger","wrath","fear","grief","jealousy","indignation",  # cluster-name terms
}
WORD_RE = re.compile(r"\b[a-z]+\b")


def tokens(text: str) -> set[str]:
    if not text:
        return set()
    return {w for w in WORD_RE.findall(text.lower())
            if w not in STOPWORDS and len(w) > 3}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def containment(a: set, b: set) -> float:
    """How much of A's vocabulary is contained in B (asymmetric).
    Good for comparing short-label A against long-paragraph B.
    Returns |A ∩ B| / |A|."""
    if not a:
        return 0.0
    return len(a & b) / len(a)


def fetch_vcgs_for_cluster(conn, cluster_code: str) -> dict[int, dict]:
    out: dict[int, dict] = {}
    for r in conn.execute("""
        SELECT DISTINCT vcg.id, vcg.group_code, vcg.context_description, vcg.delete_flagged
        FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code=?
    """, (cluster_code,)):
        out[r["id"]] = dict(r)
    return out


def fetch_vc_routing(conn, cluster_code: str) -> dict[int, int]:
    """Return {vc_id: current group_id} for cluster's active is_relevant verses."""
    return {
        r["id"]: r["group_id"] for r in conn.execute("""
            SELECT vc.id, vc.group_id FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
              AND mt.status IN ('extracted','extracted_thin') AND COALESCE(mt.delete_flagged,0)=0
              AND vc.is_relevant=1 AND vc.group_id IS NOT NULL
        """, (cluster_code,))
    }


def build_report(conn, cluster_code: str, new_vcg_min_id: int, snapshot: dict,
                  jaccard_high: float = 0.50, jaccard_low: float = 0.20) -> str:
    cluster = conn.execute(
        "SELECT * FROM cluster WHERE cluster_code=?", (cluster_code,)
    ).fetchone()

    all_vcgs = fetch_vcgs_for_cluster(conn, cluster_code)
    inherited_ids = sorted([vid for vid in all_vcgs
                             if vid < new_vcg_min_id and not all_vcgs[vid]["delete_flagged"]])
    new_ids = sorted([vid for vid in all_vcgs
                       if vid >= new_vcg_min_id and not all_vcgs[vid]["delete_flagged"]])

    # Tokenise descriptions
    old_tokens = {vid: tokens(all_vcgs[vid]["context_description"] or "") for vid in inherited_ids}
    new_tokens = {vid: tokens(all_vcgs[vid]["context_description"] or "") for vid in new_ids}

    # Snapshot routing: {old_vcg_id: [vc_id...]}
    snap = {int(k): v for k, v in snapshot.get("vc_to_old_group", {}).items()}
    old_members: dict[int, list[int]] = defaultdict(list)
    for vc_id, old_gid in snap.items():
        if old_gid is None:
            continue
        old_members[old_gid].append(vc_id)
    pre_unrouted_vcs = {vc_id for vc_id, og in snap.items() if og is None}

    # Current routing
    current = fetch_vc_routing(conn, cluster_code)

    # For each old VCG: which new VCGs received its members + counts
    old_to_new_routing: dict[int, Counter] = {}
    for old_vid in inherited_ids:
        c = Counter()
        for vc in old_members.get(old_vid, []):
            new_gid = current.get(vc)
            if new_gid is not None:
                c[new_gid] += 1
        old_to_new_routing[old_vid] = c

    # For each new VCG: which old VCGs contributed members + counts
    new_from_old: dict[int, Counter] = defaultdict(Counter)
    for old_vid, ctr in old_to_new_routing.items():
        for new_vid, n in ctr.items():
            new_from_old[new_vid][old_vid] = n

    # For each new VCG: how many of its current members were PRE-UNROUTED
    new_from_unrouted: Counter = Counter()
    for vc_id, new_gid in current.items():
        if vc_id in pre_unrouted_vcs:
            new_from_unrouted[new_gid] += 1

    # ===== Compute semantic match scores =====
    # Old descriptions are short labels; new are paragraphs. Use containment "old in new":
    # what fraction of the old description's substantive vocab is captured in the new?
    old_best_semantic: dict[int, tuple[int | None, float]] = {}
    for old_vid in inherited_ids:
        o = old_tokens[old_vid]
        best = (None, 0.0)
        for new_vid in new_ids:
            score = containment(o, new_tokens[new_vid])
            if score > best[1]:
                best = (new_vid, score)
        old_best_semantic[old_vid] = best

    # For each new VCG: best inverse containment — what fraction of its substantive vocab
    # is captured in any old description. Low value → new is novel.
    new_best_semantic: dict[int, tuple[int | None, float]] = {}
    for new_vid in new_ids:
        n = new_tokens[new_vid]
        best = (None, 0.0)
        for old_vid in inherited_ids:
            score = containment(n, old_tokens[old_vid])
            if score > best[1]:
                best = (old_vid, score)
        new_best_semantic[new_vid] = best

    # ===== Classify into lenses =====
    # Lens 1 — old VCGs "very different / not repeated"
    #   Criteria: low semantic match AND members scattered (no clear new VCG home)
    lens1_unique_old: list[dict] = []
    for old_vid in inherited_ids:
        sem_best, sem_score = old_best_semantic[old_vid]
        routing = old_to_new_routing[old_vid]
        total_members = sum(routing.values())
        top_target_n = max(routing.values()) if routing else 0
        top_target_share = (top_target_n / total_members) if total_members > 0 else 0.0
        if sem_score < jaccard_low and (total_members == 0 or top_target_share < 0.5):
            lens1_unique_old.append({
                "old_vid": old_vid,
                "old": all_vcgs[old_vid],
                "sem_best": sem_best,
                "sem_score": sem_score,
                "member_total": total_members,
                "top_target_share": top_target_share,
                "routing": routing,
            })

    # Lens 2 — Old VCGs with HIGH semantic match to a new VCG
    #   Criteria: sem_score >= jaccard_high AND member routing aligns (top new = sem-best new)
    lens2_keep_equivalent: list[dict] = []
    for old_vid in inherited_ids:
        sem_best, sem_score = old_best_semantic[old_vid]
        if sem_score < jaccard_high or sem_best is None:
            continue
        routing = old_to_new_routing[old_vid]
        total_members = sum(routing.values())
        if total_members == 0:
            continue
        top_new = max(routing, key=routing.get)
        top_share = routing[top_new] / total_members
        member_aligned = (top_new == sem_best)
        lens2_keep_equivalent.append({
            "old_vid": old_vid,
            "old": all_vcgs[old_vid],
            "sem_best": sem_best,
            "sem_score": sem_score,
            "top_target": top_new,
            "top_share": top_share,
            "member_aligned": member_aligned,
        })

    # Lens 3 — New VCGs "novel synthesis"
    #   Criteria: high share of pre-unrouted members AND/OR low semantic match to any old VCG
    lens3_novel_new: list[dict] = []
    for new_vid in new_ids:
        cur_members = sum(1 for vc_id, g in current.items() if g == new_vid)
        from_unrouted = new_from_unrouted.get(new_vid, 0)
        unrouted_share = (from_unrouted / cur_members) if cur_members > 0 else 0.0
        sem_best, sem_score = new_best_semantic[new_vid]
        sources = new_from_old.get(new_vid, Counter())
        n_sources = len(sources)
        if (sem_score < jaccard_low) or (unrouted_share >= 0.5 and n_sources <= 2):
            lens3_novel_new.append({
                "new_vid": new_vid,
                "new": all_vcgs[new_vid],
                "sem_best": sem_best,
                "sem_score": sem_score,
                "cur_members": cur_members,
                "from_unrouted": from_unrouted,
                "unrouted_share": unrouted_share,
                "n_sources_old": n_sources,
            })

    # ===== Render =====
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# {cluster_code} {cluster['description']} — VCG analytical lens")
    lines.append("")
    lines.append(f"**Generated:** {now_iso}  ")
    lines.append(f"**Cluster:** `{cluster_code}` ({cluster['short_name']}) · status={cluster['status']}  ")
    lines.append(f"**Boundary:** new VCGs = id ≥ {new_vcg_min_id}; inherited = id < {new_vcg_min_id}  ")
    lines.append(f"**Inherited VCGs analysed:** {len(inherited_ids)}  ")
    lines.append(f"**New VCGs analysed:** {len(new_ids)}  ")
    lines.append(f"**Pre-Phase-7 unrouted vc rows (new arrivals):** {len(pre_unrouted_vcs)} (Phase 1 UT verses had no inherited group_id)  ")
    lines.append(f"**Semantic metric:** **containment** of the old description's substantive vocabulary in the new description's vocabulary (asymmetric — old descriptions are short labels, new are analytical paragraphs). For Lens 3, inverse containment (new in old). Thresholds: high≥{jaccard_high}, low<{jaccard_low}.")
    lines.append("")
    lines.append("**Companion report:** [WA-M02-vcg-dissolution-comparison-v1-20260516.md](WA-M02-vcg-dissolution-comparison-v1-20260516.md) — the per-VCG routing detail. This document adds the three analytical lenses you asked for.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Lens 1
    lines.append("## Lens 1 — Old VCGs that are 'very different / not repeated' in the new structure")
    lines.append("")
    lines.append("Old VCGs whose context_description has **low containment** in any new VCG description "
                 f"(containment < {jaccard_low}) AND whose pre-Phase-7 members did **not** concentrate in any "
                 "single new VCG (<50% share). These represent inherited analytical framings that the new VCG "
                 "structure did not preserve — either the framing was wrong, or the new structure missed something.")
    lines.append("")
    if not lens1_unique_old:
        lines.append("_(None — every inherited VCG has either a semantic match in a new VCG or its members "
                     "concentrated cleanly in one new VCG. The new structure absorbed the old analytical "
                     "content without loss.)_")
        lines.append("")
    else:
        lines.append(f"**Count: {len(lens1_unique_old)} unique-old VCGs**")
        lines.append("")
        for e in sorted(lens1_unique_old, key=lambda x: x["old"]["group_code"]):
            old = e["old"]
            lines.append(f"### `{old['group_code']}` (id={old['id']})")
            lines.append("")
            desc = (old["context_description"] or "").replace("\n"," ")
            lines.append(f"**Old description:** {desc}")
            lines.append("")
            if e["sem_best"]:
                best_code = all_vcgs[e["sem_best"]]["group_code"]
                lines.append(f"- Best semantic match: `{best_code}` (containment {e['sem_score']:.2f}) — still below threshold")
            else:
                lines.append(f"- No semantic match in any new VCG")
            lines.append(f"- Members in snapshot: {e['member_total']}, top target share: {e['top_target_share']:.0%}")
            if e["routing"]:
                lines.append("- Member routing (current):")
                for nv, n in sorted(e["routing"].items(), key=lambda x: -x[1]):
                    lines.append(f"  - `{all_vcgs[nv]['group_code']}` (id={nv}): {n}")
            lines.append("")
        lines.append("")
    lines.append("---")
    lines.append("")

    # Lens 2
    lines.append("## Lens 2 — Old VCGs with high semantic similarity to a new VCG (KEEP-EQUIVALENT candidates)")
    lines.append("")
    lines.append(f"Old VCGs whose vocabulary is well-covered by a new VCG description "
                 f"(containment ≥ {jaccard_high}, i.e. ≥{int(jaccard_high*100)}% of the old description's "
                 "substantive words appear in the new). **Bonus check (`Aligned?`):** does the member routing "
                 "also align — do the old VCG's verses route to the same new VCG that its description matches? "
                 "When alignment is ✗, the description-match new VCG and the actual member-routing new VCG are "
                 "different — the old VCG's *concept* lives in one new place, its *verses* moved to another.")
    lines.append("")
    if not lens2_keep_equivalent:
        lines.append("_(None at high threshold — the new structure was a substantial re-conception, not "
                     "a direct retitling of old VCGs.)_")
        lines.append("")
    else:
        lines.append(f"**Count: {len(lens2_keep_equivalent)} high-similarity old VCGs**")
        lines.append("")
        lines.append("| Old VCG | Best new VCG (containment) | Members → top new | Aligned? |")
        lines.append("|---|---|---|---|")
        for e in sorted(lens2_keep_equivalent, key=lambda x: -x["sem_score"]):
            old = e["old"]
            new_code = all_vcgs[e["sem_best"]]["group_code"]
            top_code = all_vcgs[e["top_target"]]["group_code"]
            aligned = "✓" if e["member_aligned"] else f"✗ (members → {top_code})"
            lines.append(f"| `{old['group_code']}` | `{new_code}` ({e['sem_score']:.2f}) | "
                         f"`{top_code}` ({e['top_share']:.0%}) | {aligned} |")
        lines.append("")
        lines.append("### Detail per high-similarity pair")
        lines.append("")
        for e in sorted(lens2_keep_equivalent, key=lambda x: -x["sem_score"])[:15]:  # top 15
            old = e["old"]
            new = all_vcgs[e["sem_best"]]
            lines.append(f"#### `{old['group_code']}` ↔ `{new['group_code']}` (containment {e['sem_score']:.2f})")
            lines.append("")
            lines.append(f"- **Old:** {(old['context_description'] or '').replace(chr(10),' ')}")
            lines.append(f"- **New:** {(new['context_description'] or '').replace(chr(10),' ')}")
            lines.append("")
        if len(lens2_keep_equivalent) > 15:
            lines.append(f"_(+{len(lens2_keep_equivalent)-15} additional pairs shown only in summary table.)_")
            lines.append("")
    lines.append("---")
    lines.append("")

    # Lens 3
    lines.append("## Lens 3 — New VCGs that are 'novel synthesis' (not found in old VCGs)")
    lines.append("")
    lines.append(f"New VCGs whose description vocabulary is **poorly captured** by any old VCG (inverse "
                 f"containment < {jaccard_low}) OR whose members are dominated (≥50%) by **pre-Phase-7 "
                 "unrouted vc rows** (Phase 1 UT additions — verses that didn't exist in the old structure) "
                 "AND draw from ≤2 old VCGs. These are new analytical contents the inherited structure didn't capture.")
    lines.append("")
    if not lens3_novel_new:
        lines.append("_(None — every new VCG has either a semantic anchor in some old VCG description or "
                     "draws meaningfully from the pre-Phase-7 routing structure.)_")
        lines.append("")
    else:
        lines.append(f"**Count: {len(lens3_novel_new)} novel-synthesis new VCGs**")
        lines.append("")
        for e in sorted(lens3_novel_new, key=lambda x: x["new"]["group_code"]):
            new = e["new"]
            lines.append(f"### `{new['group_code']}` (id={e['new_vid']})")
            lines.append("")
            desc = (new["context_description"] or "").replace("\n", " ")
            lines.append(f"**New description:** {desc}")
            lines.append("")
            if e["sem_best"]:
                best_code = all_vcgs[e["sem_best"]]["group_code"]
                lines.append(f"- Best semantic match in old: `{best_code}` (containment {e['sem_score']:.2f})")
            else:
                lines.append("- No semantic match in any old VCG")
            lines.append(f"- Current member count: {e['cur_members']}; from pre-Phase-7 unrouted (UT additions): "
                         f"{e['from_unrouted']} ({e['unrouted_share']:.0%})")
            lines.append(f"- Old VCG sources: {e['n_sources_old']}")
            lines.append("")
    lines.append("---")
    lines.append("")

    # Summary
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Lens 1 (unique old, not preserved):** {len(lens1_unique_old)}")
    lines.append(f"- **Lens 2 (keep-equivalent candidates):** {len(lens2_keep_equivalent)}")
    lines.append(f"- **Lens 3 (novel new, not in old):** {len(lens3_novel_new)}")
    lines.append("")
    lines.append("Interpretation:")
    lines.append("")
    lines.append("- High Lens 1 count → the new structure dropped analytical content; review whether anything important was lost.")
    lines.append("- High Lens 2 count → many old VCGs map cleanly to new; the restructure largely preserved the old framing.")
    lines.append("- High Lens 3 count → the new structure surfaced analytical content the old structure missed (often because of the Phase 1 UT additions or the v2_0 anti-anchoring guard letting AI see fresh).")
    lines.append("")
    lines.append("*End of analytical lens report.*")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    ap.add_argument("--new-vcg-min-id", type=int, required=True)
    ap.add_argument("--pre-routing-snapshot", required=True)
    ap.add_argument("--jaccard-high", type=float, default=0.30)
    ap.add_argument("--jaccard-low", type=float, default=0.10)
    args = ap.parse_args()

    snap = json.loads(Path(args.pre_routing_snapshot).read_text(encoding="utf-8"))
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    try:
        rpt = build_report(conn, args.m_cluster, args.new_vcg_min_id, snap,
                            args.jaccard_high, args.jaccard_low)
        out_dir = REPO / "Sessions" / "Session_Clusters" / args.m_cluster
        out_dir.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
        out_path = out_dir / f"WA-{args.m_cluster}-vcg-analytical-lens-v1-{date_str}.md"
        out_path.write_text(rpt, encoding="utf-8")
        print(f"Wrote: {out_path.relative_to(REPO)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
