"""Build a comprehensive M11 sub-group / VCG / verse review markdown.

Reads the post-Phase-C DB state and writes a single review document
showing every verse under its assigned sub-group and VCG, with reference,
Pass A meaning, keywords, and anchor designation.

For researcher review of the B.2 + B.3 designs.
"""
from __future__ import annotations
import io, json, sqlite3, sys
from collections import defaultdict
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
OUT = REPO / "Sessions" / "Session_Clusters" / "M11" / "WA-M11-subgroup-vcg-verses-review-v1-20260527.md"
CLUSTER = "M11"


def main() -> int:
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Sub-groups + characteristics
    subgroups = conn.execute("""
        SELECT sg.id AS sg_id, sg.subgroup_code, sg.label, sg.core_description, sg.sort_order,
               ch.id AS char_id, ch.char_seq, ch.short_name AS char_name
        FROM cluster_subgroup sg
        LEFT JOIN characteristic_subgroup csg ON csg.cluster_subgroup_id = sg.id AND COALESCE(csg.delete_flagged,0)=0
        LEFT JOIN characteristic ch ON ch.id = csg.characteristic_id AND COALESCE(ch.delete_flagged,0)=0
        WHERE sg.cluster_code=? AND COALESCE(sg.delete_flagged,0)=0
        ORDER BY sg.sort_order
    """, (CLUSTER,)).fetchall()

    # VCGs grouped by sub-group via membership
    # Build: vcg_id -> {sg_id, group_code, context_description}
    vcgs = conn.execute("""
        SELECT DISTINCT vcg.id AS vcg_id, vcg.group_code, vcg.context_description
        FROM verse_context_group vcg
        WHERE vcg.id IN (
            SELECT DISTINCT vc.group_id FROM verse_context vc
            JOIN mti_terms m ON m.id = vc.mti_term_id
            WHERE m.cluster_code=? AND vc.group_id IS NOT NULL AND COALESCE(vc.delete_flagged,0)=0
        )
          AND COALESCE(vcg.delete_flagged,0)=0
    """, (CLUSTER,)).fetchall()

    # Map vcg_id -> sg_id (via verses)
    vcg_to_sg: dict[int, int] = {}
    for vcg in vcgs:
        r = conn.execute("""
            SELECT DISTINCT cluster_subgroup_id FROM verse_context
            WHERE group_id=? AND COALESCE(delete_flagged,0)=0
            LIMIT 1
        """, (vcg["vcg_id"],)).fetchone()
        if r:
            vcg_to_sg[vcg["vcg_id"]] = r["cluster_subgroup_id"]

    # Verses grouped by (sg_id, vcg_id)
    verses = conn.execute("""
        SELECT vc.id AS vc_id, vc.cluster_subgroup_id, vc.group_id, vc.is_anchor,
               vc.analysis_note, vc.keywords, vr.reference,
               m.strongs_number, m.transliteration, m.gloss, m.language
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms m ON m.id = vc.mti_term_id
        WHERE m.cluster_code=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
        ORDER BY vc.cluster_subgroup_id, vc.group_id, m.language, m.strongs_number, vr.reference
    """, (CLUSTER,)).fetchall()

    # Bucket
    by_sg_vcg: defaultdict[tuple, list] = defaultdict(list)
    for v in verses:
        by_sg_vcg[(v["cluster_subgroup_id"], v["group_id"])].append(v)

    vcg_lookup = {v["vcg_id"]: v for v in vcgs}

    print(f"Building review for {CLUSTER} ({len(subgroups)} sub-groups, {len(vcgs)} VCGs, {len(verses)} verses)")

    with OUT.open("w", encoding="utf-8") as f:
        f.write(f"# {CLUSTER} — Sub-group / VCG / Verse review\n\n")
        f.write(f"**Cluster:** {CLUSTER} — Repentance, Forgiveness and Restoration  \n")
        f.write(f"**Date:** 2026-05-27  \n")
        f.write(f"**Purpose:** Researcher visibility into the Phase B.2 (sub-group) + Phase B.3 (VCG) designs and per-verse assignments.  \n")
        f.write(f"**Source:** Live DB after Phase C apply (commit 50b2f5f).\n\n")
        f.write(f"**Caveat:** The B.2 + B.3 designs were authored by me (Claude Code, this session) "
                f"rather than via a separate AI chat session as v3_0 protocol prescribes. "
                f"This review is for the researcher to inspect what was produced and decide whether to "
                f"keep, revise, or redo via proper protocol.\n\n")

        f.write(f"## Summary\n\n")
        f.write(f"| Sub-group | Characteristic | VCGs | Verses |\n")
        f.write(f"|---|---|---:|---:|\n")
        total_vcgs = 0
        total_verses = 0
        for sg in subgroups:
            sg_vcg_ids = [vid for vid, sid in vcg_to_sg.items() if sid == sg["sg_id"]]
            sg_verse_count = sum(len(by_sg_vcg[(sg["sg_id"], vid)]) for vid in sg_vcg_ids)
            f.write(f"| **{sg['subgroup_code']}** {sg['label']} | char_seq={sg['char_seq']} {sg['char_name']} | {len(sg_vcg_ids)} | {sg_verse_count} |\n")
            total_vcgs += len(sg_vcg_ids)
            total_verses += sg_verse_count
        f.write(f"| **Total** | | **{total_vcgs}** | **{total_verses}** |\n\n")
        f.write("---\n\n")

        for sg in subgroups:
            f.write(f"## {sg['subgroup_code']} — {sg['label']}\n\n")
            f.write(f"**Characteristic:** {sg['char_name']} (char_seq={sg['char_seq']})  \n")
            f.write(f"**Core description:** {sg['core_description']}\n\n")

            sg_vcg_ids = [vid for vid, sid in vcg_to_sg.items() if sid == sg["sg_id"]]
            # Sort VCGs by group_code (M11-A-VCG-01, ..., -02, etc.)
            sg_vcgs_sorted = sorted(
                (vcg_lookup[v] for v in sg_vcg_ids),
                key=lambda v: v["group_code"],
            )

            for vcg in sg_vcgs_sorted:
                vcg_verses = by_sg_vcg[(sg["sg_id"], vcg["vcg_id"])]
                anchor_vc = next((v for v in vcg_verses if v["is_anchor"]), None)
                f.write(f"### {vcg['group_code']}  ({len(vcg_verses)} verses)\n\n")
                f.write(f"**Context:** {vcg['context_description']}\n\n")
                if anchor_vc:
                    f.write(f"**Anchor:** `{anchor_vc['reference']}` (vc={anchor_vc['vc_id']}) — *{anchor_vc['strongs_number']} {anchor_vc['transliteration']}*\n\n")

                f.write(f"**Verses:**\n\n")
                for v in vcg_verses:
                    star = " ★" if v["is_anchor"] else ""
                    note = (v["analysis_note"] or "").replace("\n", " ").strip()
                    kw = v["keywords"] or ""
                    try:
                        kw_list = json.loads(kw) if kw else []
                        kw_disp = " · ".join(kw_list) if isinstance(kw_list, list) else kw
                    except Exception:
                        kw_disp = kw
                    f.write(f"- **vc={v['vc_id']}**{star} `{v['reference']}` *{v['strongs_number']} {v['transliteration']}* — {note}  \n")
                    if kw_disp:
                        f.write(f"  *keywords:* {kw_disp}\n")
                f.write("\n")

            f.write("---\n\n")

        f.write(f"*Built by `_build_m11_b3_review_v1_20260527.py` from live DB. Verify against:*  \n")
        f.write(f"*  - `WA-M11-subgroup-design-v1-20260527.md` (B.2 design)*  \n")
        f.write(f"*  - `WA-M11-M11-{{A..E}}-vcg-design-v1-20260527.md` (B.3 per-sub-group designs)*  \n")
        f.write(f"*  - `WA-M11-vcg-creation-v1-20260527.json` (unified VCG creation JSON)*\n")

    print(f"Wrote {OUT}")
    print(f"  {total_vcgs} VCGs, {total_verses} verses")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
