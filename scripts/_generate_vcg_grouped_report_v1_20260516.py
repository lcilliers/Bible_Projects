"""Generate the VCG-grouped report (Phase 9 input).

Per wa-sessionb-cluster-instruction-v2_0-20260515 §12.1 — for each sub-group of the
cluster, then each VCG within that sub-group (post-Phase-7), list every routed verse
with its term and Phase 2 meaning. The anchor verse is marked. This is AI's Phase 9
input for catalogue-prompt findings authoring.

Structure (per active sub-group):
  ## Sub-group {code} — {label}
  Core description + counts
    ### VCG {group_code} (anchor: {ref})
    {context_description}
    | vc_id | reference | term | meaning |

Dual-membership: verses with `notes` containing "dual-membership" are flagged.
Set-asides (is_relevant=0): listed in a per-sub-group appendix.

Usage:
  python scripts/_generate_vcg_grouped_report_v1_20260516.py --m-cluster M01

Output:
  Sessions/Session_Clusters/{code}/wa-cluster-{code}-vcg-grouped-v{N}-{date}.md
"""
from __future__ import annotations
import argparse, re, sqlite3, sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"


def next_version_for(out_dir: Path, prefix: str, date_str: str) -> str:
    pat = re.compile(rf"^{re.escape(prefix)}-v(\d+)-{date_str}\.md$")
    max_v = 0
    if out_dir.exists():
        for p in out_dir.iterdir():
            m = pat.match(p.name)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return f"v{max_v + 1}"


def build_report(conn, cluster_code: str) -> str:
    cluster = conn.execute(
        "SELECT * FROM cluster WHERE cluster_code=?", (cluster_code,)
    ).fetchone()
    if not cluster:
        raise RuntimeError(f"cluster {cluster_code} not found")

    # Sub-groups for cluster
    subgroups = list(conn.execute("""
        SELECT id, subgroup_code, label, core_description, sort_order
        FROM cluster_subgroup
        WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
        ORDER BY sort_order, subgroup_code
    """, (cluster_code,)))
    if not subgroups:
        raise RuntimeError(f"cluster {cluster_code} has no active sub-groups")

    # Active VCGs in cluster (post-Phase-8: only new VCGs remain)
    vcgs = list(conn.execute("""
        SELECT DISTINCT vcg.id, vcg.group_code, vcg.context_description
        FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vcg.delete_flagged,0)=0
          AND COALESCE(vt.delete_flagged,0)=0
        ORDER BY vcg.group_code
    """, (cluster_code,)))
    vcgs_by_id = {v["id"]: dict(v) for v in vcgs}

    # All routed verses with anchor flag
    verses_by_vcg: dict[int, list[dict]] = defaultdict(list)
    anchors_by_vcg: dict[int, list[int]] = defaultdict(list)
    set_asides_by_sg: dict[int, list[dict]] = defaultdict(list)
    sg_of_vcg: dict[int, int] = {}  # vcg_id -> dominant sub-group id (for ordering)

    # Active routed (is_relevant=1, group_id NOT NULL)
    for r in conn.execute("""
        SELECT vc.id AS vc_id, vc.cluster_subgroup_id, vc.group_id, vc.is_anchor,
               vc.is_relevant, vc.analysis_note, vc.notes,
               vr.book_id, vr.chapter, vr.verse_num, vr.reference,
               mt.strongs_number, mt.transliteration, mt.gloss, mt.language
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
          AND mt.status IN ('extracted','extracted_thin') AND COALESCE(mt.delete_flagged,0)=0
          AND vc.is_relevant=1 AND vc.group_id IS NOT NULL
        ORDER BY vc.group_id, vr.book_id, vr.chapter, vr.verse_num, mt.strongs_number, vc.id
    """, (cluster_code,)):
        gid = r["group_id"]
        sg = r["cluster_subgroup_id"]
        if gid not in sg_of_vcg and sg is not None:
            sg_of_vcg[gid] = sg
        verses_by_vcg[gid].append(dict(r))
        if r["is_anchor"]:
            anchors_by_vcg[gid].append(r["vc_id"])

    # Set-asides per sub-group
    for r in conn.execute("""
        SELECT vc.id AS vc_id, vc.cluster_subgroup_id, vc.set_aside_reason, vc.analysis_note,
               vr.reference, mt.strongs_number, mt.transliteration
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
          AND mt.status IN ('extracted','extracted_thin') AND COALESCE(mt.delete_flagged,0)=0
          AND vc.is_relevant=0
        ORDER BY vc.cluster_subgroup_id, vr.book_id, vr.chapter, vr.verse_num
    """, (cluster_code,)):
        if r["cluster_subgroup_id"] is not None:
            set_asides_by_sg[r["cluster_subgroup_id"]].append(dict(r))

    # Term coverage per sub-group (active terms reachable via mti_term_subgroup)
    sg_term_count: dict[int, int] = {}
    sg_term_list: dict[int, list[dict]] = defaultdict(list)
    for r in conn.execute("""
        SELECT mts.cluster_subgroup_id AS subgroup_id,
               (CASE WHEN COALESCE(mts.placement_note,'') LIKE '%[primary]%' THEN 1 ELSE 0 END) AS is_primary,
               mt.id AS mti_id,
               mt.strongs_number, mt.transliteration, mt.gloss, mt.language
        FROM mti_term_subgroup mts
        JOIN mti_terms mt ON mt.id = mts.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
          AND mt.status IN ('extracted','extracted_thin')
          AND COALESCE(mts.delete_flagged,0)=0
        ORDER BY mts.cluster_subgroup_id, mt.strongs_number
    """, (cluster_code,)):
        sg_term_list[r["subgroup_id"]].append(dict(r))
    for sg_id, terms in sg_term_list.items():
        sg_term_count[sg_id] = len({t["mti_id"] for t in terms})

    # ===== Render =====
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# {cluster_code} {cluster['description']} — VCG-grouped report (Phase 9 input)")
    lines.append("")
    lines.append(f"**Generated:** {now_iso}  ")
    lines.append(f"**Cluster:** `{cluster_code}` ({cluster['short_name']}) · status={cluster['status']} · version={cluster['version']}  ")
    lines.append(f"**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §12 (Phase 9)  ")
    lines.append(f"**Source:** `database/bible_research.db` (post-Phase-8 — only new VCGs visible)  ")
    lines.append("")
    lines.append("**Scope:** for each active sub-group, every VCG with its anchor verse and member verses (reference, term, meaning) in canonical Bible order. This is the analytical material for Phase 9 catalogue-prompt findings authoring.")
    lines.append("")
    lines.append("**Suppressed by design (per §2.3 — structurally enforced):** no inherited VCG references, no pre-Phase-7 group_ids, no prior session findings (those go into Phase 10 reconciliation, not Phase 9).")
    lines.append("")
    lines.append("---")
    lines.append("")
    # ===== Cluster header summary =====
    total_verses = sum(len(v) for v in verses_by_vcg.values())
    total_anchors = sum(len(a) for a in anchors_by_vcg.values())
    total_set_asides = sum(len(v) for v in set_asides_by_sg.values())
    lines.append("## Cluster header summary")
    lines.append("")
    lines.append("| Item | Count |")
    lines.append("|---|---:|")
    lines.append(f"| Active sub-groups | {len(subgroups)} |")
    lines.append(f"| Active VCGs | {len(vcgs)} |")
    lines.append(f"| Active is_relevant verses (routed) | {total_verses} |")
    lines.append(f"| Anchors | {total_anchors} |")
    lines.append(f"| Set-asides (is_relevant=0) | {total_set_asides} |")
    lines.append("")
    lines.append("### Sub-groups overview")
    lines.append("")
    lines.append("| Code | Label | Terms | VCGs | Verses |")
    lines.append("|---|---|---:|---:|---:|")
    vcgs_by_sg: dict[int, list[int]] = defaultdict(list)
    for vcg_id, sg_id in sg_of_vcg.items():
        vcgs_by_sg[sg_id].append(vcg_id)
    for sg in subgroups:
        n_vcgs = len(vcgs_by_sg.get(sg["id"], []))
        n_verses = sum(len(verses_by_vcg[v]) for v in vcgs_by_sg.get(sg["id"], []))
        lines.append(f"| `{sg['subgroup_code']}` | {sg['label']} | {sg_term_count.get(sg['id'],0)} | {n_vcgs} | {n_verses} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ===== Per-sub-group sections =====
    for sg in subgroups:
        sg_id = sg["id"]
        sg_vcg_ids = sorted(vcgs_by_sg.get(sg_id, []), key=lambda v: vcgs_by_id[v]["group_code"])
        n_verses = sum(len(verses_by_vcg[v]) for v in sg_vcg_ids)
        lines.append(f"## Sub-group `{sg['subgroup_code']}` — {sg['label']}")
        lines.append("")
        lines.append(f"**Core description:** {sg['core_description']}")
        lines.append("")
        lines.append(f"**Stats:** {sg_term_count.get(sg_id, 0)} terms · {len(sg_vcg_ids)} VCGs · {n_verses} verses")
        lines.append("")

        # Term list per sub-group (compact)
        terms = sg_term_list.get(sg_id, [])
        if terms:
            primary = [t for t in terms if t["is_primary"]]
            secondary = [t for t in terms if not t["is_primary"]]
            if primary:
                lines.append("**Primary terms:** " + ", ".join(
                    f"{t['strongs_number']} *{t['transliteration']}*" for t in primary
                ))
            if secondary:
                lines.append("**Secondary terms:** " + ", ".join(
                    f"{t['strongs_number']} *{t['transliteration']}*" for t in secondary
                ))
            lines.append("")

        # Per-VCG detail
        if not sg_vcg_ids:
            lines.append("_(No VCGs in this sub-group.)_")
            lines.append("")
        for vcg_id in sg_vcg_ids:
            vcg = vcgs_by_id[vcg_id]
            verses = verses_by_vcg[vcg_id]
            anchors = set(anchors_by_vcg.get(vcg_id, []))

            # Find anchor reference(s) for header
            anchor_refs = []
            for vc in verses:
                if vc["vc_id"] in anchors:
                    anchor_refs.append(f"{vc['reference']} ({vc['strongs_number']})")

            lines.append(f"### VCG `{vcg['group_code']}` ({len(verses)} verses)")
            lines.append("")
            lines.append(f"**Context:** {vcg['context_description']}")
            lines.append("")
            if anchor_refs:
                lines.append(f"**Anchor(s):** {' · '.join(anchor_refs)}")
                lines.append("")

            lines.append("| Ref | Term | Meaning |")
            lines.append("|---|---|---|")
            for vc in verses:
                meaning = (vc["analysis_note"] or "").replace("|","\\|").replace("\n"," ").strip()
                anchor_mark = " ⚓" if vc["vc_id"] in anchors else ""
                dual = ""
                if vc["notes"] and "dual-membership" in (vc["notes"] or ""):
                    dual = " ⇄"
                term_str = f"{vc['strongs_number']} *{vc['transliteration']}*"
                lines.append(f"| **{vc['reference']}**{anchor_mark}{dual} | {term_str} | {meaning} |")
            lines.append("")

        # Set-asides for this sub-group
        sa = set_asides_by_sg.get(sg_id, [])
        if sa:
            lines.append(f"### Set-asides in `{sg['subgroup_code']}` ({len(sa)})")
            lines.append("")
            lines.append("Verses set aside (is_relevant=0) from this sub-group — outside programme scope or other documented reason:")
            lines.append("")
            lines.append("| Ref | Term | Reason | Meaning |")
            lines.append("|---|---|---|---|")
            for vc in sa:
                reason = (vc["set_aside_reason"] or "").replace("|","\\|").replace("\n"," ").strip()
                meaning = (vc["analysis_note"] or "").replace("|","\\|").replace("\n"," ").strip()
                term_str = f"{vc['strongs_number']} *{vc['transliteration']}*"
                lines.append(f"| {vc['reference']} | {term_str} | {reason} | {meaning} |")
            lines.append("")

        lines.append("---")
        lines.append("")

    # ===== Legend =====
    lines.append("## Legend")
    lines.append("")
    lines.append("- ⚓ = anchor verse (single definitional verse per VCG; 36 AI-designated + 53 provisional per R4 fallback)")
    lines.append("- ⇄ = dual-membership flagged (verse meaning also belongs to a secondary VCG; primary is the one shown here)")
    lines.append("")
    lines.append("*End of report.*")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    args = ap.parse_args()
    code = args.m_cluster.strip()

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    try:
        report = build_report(conn, code)
        out_dir = REPO / "Sessions" / "Session_Clusters" / code
        out_dir.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
        version = next_version_for(out_dir, f"wa-cluster-{code}-vcg-grouped", date_str)
        out_path = out_dir / f"wa-cluster-{code}-vcg-grouped-{version}-{date_str}.md"
        out_path.write_text(report, encoding="utf-8")
        print(f"Wrote: {out_path.relative_to(REPO)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
