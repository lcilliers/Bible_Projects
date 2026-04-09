"""
build_dimension_extract.py
──────────────────────────
Constructs data extracts for the Dimension Review stage.

Three extract types:
  1. Cluster extract (--cluster C01) — primary session input for Claude AI
  2. Group verification extract (--group-verify 112-003) — verse text for description correction
  3. Existing pointers extract (--pointers C01) — pre-existing Session B/D pointers

Output: data/exports/dimension_review/

Usage:
  python scripts/build_dimension_extract.py --cluster C01
  python scripts/build_dimension_extract.py --group-verify 112-003
  python scripts/build_dimension_extract.py --pointers C01
"""
import argparse
import json
import os
import sqlite3
from datetime import date

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "exports", "dimension_review")


def build_cluster_extract(conn, cluster: str, today: str) -> str:
    """Build the cluster extract per Section 9.1."""

    # Cluster registries
    regs = conn.execute("""
        SELECT wr.no as registry_no, wr.word, wr.cluster_assignment,
               wr.verse_context_status, wr.session_b_status, wr.source_list
        FROM word_registry wr
        WHERE wr.cluster_assignment = ? AND wr.phase1_status != 'Excluded'
        ORDER BY wr.no
    """, (cluster,)).fetchall()

    # Per-registry group counts
    cluster_registries = []
    for r in regs:
        counts = conn.execute("""
            SELECT COUNT(*) as total,
                SUM(CASE WHEN dimension IS NOT NULL THEN 1 ELSE 0 END) as classified,
                SUM(CASE WHEN dimension IS NULL THEN 1 ELSE 0 END) as unclassified
            FROM wa_dimension_index
            WHERE owning_registry_no = ? AND delete_flagged = 0
        """, (r["registry_no"],)).fetchone()

        cluster_registries.append({
            "registry_no": r["registry_no"],
            "word": r["word"],
            "cluster_assignment": r["cluster_assignment"],
            "verse_context_status": r["verse_context_status"],
            "session_b_status": r["session_b_status"],
            "source_list": r["source_list"],
            "total_groups": counts["total"] or 0,
            "classified_groups": counts["classified"] or 0,
            "unclassified_groups": counts["unclassified"] or 0,
        })

    # All groups for this cluster
    groups_rows = conn.execute("""
        SELECT id, verse_context_group_id, group_code,
               owning_registry_no, owning_registry_word, cluster_assignment,
               mti_term_id, strongs_number, transliteration, gloss, language,
               context_description, dimension, dimension_confidence,
               manual_override, anchor_count, related_count,
               set_aside_count, total_verse_count, delete_flagged,
               notes, last_modified, dominant_subject
        FROM wa_dimension_index
        WHERE cluster_assignment = ? AND delete_flagged = 0
        ORDER BY owning_registry_no, group_code
    """, (cluster,)).fetchall()

    groups = []
    empty_anchor_groups = []
    for g in groups_rows:
        gd = dict(g)
        vcg_id = g["verse_context_group_id"]

        # Anchor verses
        anchors = conn.execute("""
            SELECT vc.verse_record_id, b.name as book, vr.chapter, vr.verse_num as verse,
                   vr.verse_text
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            LEFT JOIN books b ON b.id = vr.book_id
            WHERE vc.group_id = ? AND vc.is_anchor = 1 AND vc.delete_flagged = 0
            ORDER BY b.book_order, vr.chapter, vr.verse_num
        """, (vcg_id,)).fetchall()

        # Related verses
        related = conn.execute("""
            SELECT vc.verse_record_id, b.name as book, vr.chapter, vr.verse_num as verse,
                   vr.verse_text
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            LEFT JOIN books b ON b.id = vr.book_id
            WHERE vc.group_id = ? AND vc.is_related = 1 AND vc.is_anchor = 0
                  AND vc.delete_flagged = 0
            ORDER BY b.book_order, vr.chapter, vr.verse_num
        """, (vcg_id,)).fetchall()

        gd["anchor_verses"] = [dict(r) for r in anchors]
        gd["related_verses"] = [dict(r) for r in related]

        # Root family data
        root = conn.execute("""
            SELECT rf.root_code, rf.root_language, rf.root_gloss
            FROM wa_term_root_family rf
            JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged = 0
            WHERE ti.strongs_number = ? LIMIT 1
        """, (g["strongs_number"],)).fetchone()
        gd["root_code"] = root["root_code"] if root else None
        gd["root_language"] = root["root_language"] if root else None
        gd["root_gloss"] = root["root_gloss"] if root else None

        if not anchors:
            empty_anchor_groups.append(g["group_code"])

        groups.append(gd)

    result = {
        "extract_meta": {
            "extract_type": "dimension_review_cluster",
            "cluster": cluster,
            "produced_date": today,
            "produced_by": "Claude Code \u2014 WA-DimensionReview-Instruction-v1.9-2026-04-09",
            "governing_instruction": "WA-DimensionReview-Instruction-v1.9-2026-04-09",
            "row_count": len(groups),
        },
        "cluster_registries": cluster_registries,
        "groups": groups,
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    filename = f"wa-dim-{cluster}-extract-{today}.json"
    out_path = os.path.join(OUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Written: {out_path}")
    print(f"Cluster: {cluster}")
    print(f"Registries: {len(cluster_registries)}")
    print(f"Groups: {len(groups)}")
    if empty_anchor_groups:
        print(f"  WARNING: {len(empty_anchor_groups)} groups with empty anchor_verses: {empty_anchor_groups[:5]}")
    return out_path


def build_group_verify_extract(conn, group_code: str, today: str) -> str:
    """Build the group verification extract per Section 9.2."""

    # Get group info
    vcg = conn.execute("""
        SELECT vcg.id, vcg.group_code, vcg.mti_term_id, vcg.context_description, vcg.notes,
               mt.strongs_number, mt.transliteration
        FROM verse_context_group vcg
        JOIN mti_terms mt ON mt.id = vcg.mti_term_id
        WHERE vcg.group_code = ?
    """, (group_code,)).fetchone()

    if not vcg:
        print(f"ERROR: group_code '{group_code}' not found")
        return ""

    # Get owning registry
    di = conn.execute("""
        SELECT owning_registry_no, owning_registry_word
        FROM wa_dimension_index WHERE group_code = ? AND delete_flagged = 0
    """, (group_code,)).fetchone()

    group = {
        "id": vcg["id"],
        "group_code": vcg["group_code"],
        "mti_term_id": vcg["mti_term_id"],
        "strongs_number": vcg["strongs_number"],
        "transliteration": vcg["transliteration"],
        "owning_registry_no": di["owning_registry_no"] if di else None,
        "owning_registry_word": di["owning_registry_word"] if di else None,
        "current_description": vcg["context_description"],
        "notes": vcg["notes"],
    }

    # Get anchor verses
    anchors = conn.execute("""
        SELECT vc.verse_record_id, b.name as book, vr.chapter, vr.verse_num as verse,
               vr.verse_text, vc.is_anchor, vc.is_related
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN books b ON b.id = vr.book_id
        WHERE vc.group_id = ? AND vc.is_anchor = 1 AND vc.delete_flagged = 0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (vcg["id"],)).fetchall()

    # Get related verses
    related = conn.execute("""
        SELECT vc.verse_record_id, b.name as book, vr.chapter, vr.verse_num as verse,
               vr.verse_text, vc.is_anchor, vc.is_related
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN books b ON b.id = vr.book_id
        WHERE vc.group_id = ? AND vc.is_related = 1 AND vc.is_anchor = 0 AND vc.delete_flagged = 0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (vcg["id"],)).fetchall()

    result = {
        "extract_meta": {
            "extract_type": "group_description_verification",
            "group_code": group_code,
            "produced_date": today,
        },
        "group": group,
        "anchor_verses": [dict(r) for r in anchors],
        "related_verses": [dict(r) for r in related],
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    filename = f"wa-dim-{group_code}-grpverify-{today}.json"
    out_path = os.path.join(OUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Written: {out_path}")
    print(f"Group: {group_code}")
    print(f"Anchors: {len(anchors)}, Related: {len(related)}")
    return out_path


def build_existing_pointers_extract(conn, cluster: str, today: str) -> str:
    """Build the existing pointers extract per Section 9.3."""

    # Get registry ids for this cluster
    reg_ids = [r[0] for r in conn.execute("""
        SELECT id FROM word_registry
        WHERE cluster_assignment = ? AND phase1_status != 'Excluded'
    """, (cluster,)).fetchall()]

    if not reg_ids:
        print(f"No registries for cluster {cluster}")
        return ""

    placeholders = ",".join("?" for _ in reg_ids)

    # Session B findings
    findings = conn.execute(f"""
        SELECT finding_id, registry_id, finding_type, finding, raised_date, session_b_instruction
        FROM wa_session_b_findings
        WHERE registry_id IN ({placeholders})
        ORDER BY finding_id
    """, reg_ids).fetchall()

    # Session D pointers
    pointers = conn.execute(f"""
        SELECT flag_label, registry_id, flag_code, description, session_target, raised_date
        FROM wa_session_research_flags
        WHERE registry_id IN ({placeholders}) AND session_target = 'D'
        ORDER BY flag_label
    """, reg_ids).fetchall()

    result = {
        "extract_meta": {
            "extract_type": "existing_pointers",
            "cluster": cluster,
            "produced_date": today,
        },
        "session_b_findings": [dict(r) for r in findings],
        "session_d_pointers": [dict(r) for r in pointers],
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    filename = f"wa-dim-{cluster}-existing-pointers-{today}.json"
    out_path = os.path.join(OUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Written: {out_path}")
    print(f"Cluster: {cluster}")
    print(f"Session B findings: {len(findings)}")
    print(f"Session D pointers: {len(pointers)}")
    return out_path


def build_rootfamily_extract(conn, cluster: str, today: str) -> str:
    """Build the root family cluster extract per Section 9.4."""

    # Step 1: Find root codes with at least one term in this cluster
    root_codes = [r[0] for r in conn.execute("""
        SELECT DISTINCT rf.root_code
        FROM wa_term_root_family rf
        JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged = 0
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        WHERE wr.cluster_assignment = ?
    """, (cluster,)).fetchall()]

    if not root_codes:
        print(f"No root families for cluster {cluster}")
        return ""

    roots_out = []
    total_groups = 0
    cross_count = 0

    for rc in root_codes:
        # All terms in this root (including other clusters)
        terms = conn.execute("""
            SELECT DISTINCT ti.strongs_number, mt.transliteration, mt.gloss, mt.language,
                wr.no as reg_no, wr.word as reg_word, wr.cluster_assignment
            FROM wa_term_root_family rf
            JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged = 0
            JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
              AND mt.status IN ('extracted', 'extracted_thin') AND mt.delete_flagged = 0
            JOIN wa_file_index fi ON fi.id = ti.file_id
            JOIN word_registry wr ON wr.id = fi.word_registry_fk
            WHERE rf.root_code = ?
            ORDER BY wr.no, ti.strongs_number
        """, (rc,)).fetchall()

        if not terms:
            continue

        root_meta = conn.execute(
            "SELECT root_language, root_gloss FROM wa_term_root_family WHERE root_code = ? LIMIT 1",
            (rc,),
        ).fetchone()

        in_cluster_regs = sorted(set(t["reg_no"] for t in terms if t["cluster_assignment"] == cluster))
        all_clusters = set(t["cluster_assignment"] for t in terms if t["cluster_assignment"])
        is_cross = len(all_clusters) > 1

        # Groups + anchor verses for all terms in root
        groups = []
        for t in terms:
            grp_rows = conn.execute("""
                SELECT di.group_code, di.context_description, di.dimension,
                    di.dimension_confidence, di.dominant_subject, di.manual_override,
                    di.owning_registry_no, di.owning_registry_word, di.cluster_assignment,
                    di.verse_context_group_id,
                    mt2.strongs_number, mt2.transliteration, mt2.gloss
                FROM wa_dimension_index di
                JOIN mti_terms mt2 ON mt2.id = di.mti_term_id
                WHERE di.strongs_number = ? AND di.delete_flagged = 0
                ORDER BY di.group_code
            """, (t["strongs_number"],)).fetchall()

            for g in grp_rows:
                anchors = conn.execute("""
                    SELECT vc.verse_record_id, b.name as book, vr.chapter,
                           vr.verse_num as verse, vr.reference, vr.verse_text
                    FROM verse_context vc
                    JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                    LEFT JOIN books b ON b.id = vr.book_id
                    WHERE vc.group_id = ? AND vc.is_anchor = 1 AND vc.delete_flagged = 0
                    ORDER BY b.book_order, vr.chapter, vr.verse_num
                """, (g["verse_context_group_id"],)).fetchall()

                groups.append({
                    "group_code": g["group_code"],
                    "context_description": g["context_description"],
                    "strongs_number": g["strongs_number"],
                    "transliteration": g["transliteration"],
                    "gloss": g["gloss"],
                    "registry_no": g["owning_registry_no"],
                    "registry_word": g["owning_registry_word"],
                    "cluster_assignment": g["cluster_assignment"],
                    "dimension": g["dimension"],
                    "dimension_confidence": g["dimension_confidence"],
                    "dominant_subject": g["dominant_subject"],
                    "manual_override": g["manual_override"],
                    "anchor_verses": [dict(a) for a in anchors],
                })

        if is_cross:
            cross_count += 1
        total_groups += len(groups)

        roots_out.append({
            "root_code": rc,
            "root_language": root_meta["root_language"] if root_meta else None,
            "root_gloss": root_meta["root_gloss"] if root_meta else None,
            "in_cluster_registries": in_cluster_regs,
            "cross_registry": is_cross,
            "term_count": len(terms),
            "group_count": len(groups),
            "terms": [{
                "strongs_number": t["strongs_number"],
                "transliteration": t["transliteration"],
                "gloss": t["gloss"],
                "language": t["language"],
                "reg_no": t["reg_no"],
                "reg_word": t["reg_word"],
                "cluster_assignment": t["cluster_assignment"],
                "in_current_cluster": t["cluster_assignment"] == cluster,
            } for t in terms],
            "groups": groups,
        })

    result = {
        "extract_meta": {
            "extract_type": "dimension_review_rootfamily",
            "cluster": cluster,
            "produced_date": today,
            "produced_by": "Claude Code \u2014 WA-DimensionReview-Instruction-v1.9-2026-04-09",
            "governing_instruction": "WA-DimensionReview-Instruction-v1.9-2026-04-09",
            "root_count": len(roots_out),
            "group_count": total_groups,
            "cross_registry_root_count": cross_count,
        },
        "roots": roots_out,
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    filename = f"wa-dim-{cluster}-rootfamily-{today}.json"
    out_path = os.path.join(OUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    fsize = os.path.getsize(out_path)
    print(f"Written: {out_path}")
    print(f"Cluster: {cluster}")
    print(f"Roots: {len(roots_out)} ({cross_count} cross-registry)")
    print(f"Groups: {total_groups}")
    print(f"Size: {fsize / 1024:.0f} KB")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Build Dimension Review extracts")
    parser.add_argument("--cluster", help="Build cluster extract for given cluster (e.g. C01)")
    parser.add_argument("--rootfamily", help="Build root family extract for given cluster")
    parser.add_argument("--group-verify", help="Build group verification extract for given group_code")
    parser.add_argument("--pointers", help="Build existing pointers extract for given cluster")
    args = parser.parse_args()

    if not any([args.cluster, args.group_verify, args.pointers, args.rootfamily]):
        parser.print_help()
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    today = date.today().isoformat()

    if args.cluster:
        build_cluster_extract(conn, args.cluster, today)
    if args.rootfamily:
        build_rootfamily_extract(conn, args.rootfamily, today)
    if args.group_verify:
        build_group_verify_extract(conn, args.group_verify, today)
    if args.pointers:
        build_existing_pointers_extract(conn, args.pointers, today)

    conn.close()


if __name__ == "__main__":
    main()
