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

        if not anchors:
            empty_anchor_groups.append(g["group_code"])

        groups.append(gd)

    result = {
        "extract_meta": {
            "extract_type": "dimension_review_cluster",
            "cluster": cluster,
            "produced_date": today,
            "produced_by": "Claude Code \u2014 WA-DimensionReview-Instruction-v1.6",
            "governing_instruction": "WA-DimensionReview-Instruction-v1.6-2026-04-08",
            "row_count": len(groups),
        },
        "cluster_registries": cluster_registries,
        "groups": groups,
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    filename = f"wa-dim-extract-{cluster}-{today}.json"
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
    filename = f"wa-dim-grpverify-{group_code}-{today}.json"
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
    filename = f"wa-dim-existing-pointers-{cluster}-{today}.json"
    out_path = os.path.join(OUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Written: {out_path}")
    print(f"Cluster: {cluster}")
    print(f"Session B findings: {len(findings)}")
    print(f"Session D pointers: {len(pointers)}")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Build Dimension Review extracts")
    parser.add_argument("--cluster", help="Build cluster extract for given cluster (e.g. C01)")
    parser.add_argument("--group-verify", help="Build group verification extract for given group_code")
    parser.add_argument("--pointers", help="Build existing pointers extract for given cluster")
    args = parser.parse_args()

    if not any([args.cluster, args.group_verify, args.pointers]):
        parser.print_help()
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    today = date.today().isoformat()

    if args.cluster:
        build_cluster_extract(conn, args.cluster, today)
    if args.group_verify:
        build_group_verify_extract(conn, args.group_verify, today)
    if args.pointers:
        build_existing_pointers_extract(conn, args.pointers, today)

    conn.close()


if __name__ == "__main__":
    main()
