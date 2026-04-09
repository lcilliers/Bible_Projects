"""
verse_vertical_pass.py
──────────────────────
Verse-centric discovery tool. Takes a verse reference and produces
a complete cross-registry analytical profile: every term, registry,
classification, group, dimension, root family, and anchor verse
that touches the input verse.

Usage:
    python scripts/verse_vertical_pass.py "Jer 7:24"
    python scripts/verse_vertical_pass.py "Rom 10:17" --output custom_name.json
    python scripts/verse_vertical_pass.py "Psa 139:2" "1Sa 15:22"   # multiple verses
"""
import sqlite3
import argparse
import os
import json
from datetime import date

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "exports", "vertical_pass")


def discover_verse(conn, reference):
    """Build complete vertical pass profile for a single verse reference."""

    # Find all verse records matching this reference
    records = conn.execute("""
        SELECT vr.id AS verse_record_id, vr.reference, vr.verse_text,
               vr.delete_flagged AS vr_deleted, vr.target_word, vr.span_strong_match
        FROM wa_verse_records vr
        WHERE vr.reference LIKE ?
        ORDER BY vr.id
    """, (reference + "%",)).fetchall()

    if not records:
        # Try fuzzy match
        parts = reference.replace(":", " ").split()
        if len(parts) >= 2:
            pattern = f"%{parts[0]}%{parts[-1]}%"
            records = conn.execute("""
                SELECT vr.id AS verse_record_id, vr.reference, vr.verse_text,
                       vr.delete_flagged AS vr_deleted, vr.target_word, vr.span_strong_match
                FROM wa_verse_records vr
                WHERE vr.reference LIKE ?
                ORDER BY vr.id
            """, (pattern,)).fetchall()

    if not records:
        return {"reference": reference, "found": False, "verse_text": None, "term_links": []}

    verse_text = next((r["verse_text"] for r in records if r["verse_text"]), None)
    vr_ids = [r["verse_record_id"] for r in records]

    # All term links across all registries
    ph = ",".join("?" for _ in vr_ids)
    term_links = conn.execute(f"""
        SELECT vr.id AS verse_record_id, vr.delete_flagged AS vr_deleted,
            vr.target_word, vr.span_strong_match,
            ti.id AS ti_id, ti.strongs_number, ti.term_owner_type,
            mt.id AS mti_id, mt.transliteration, mt.gloss, mt.language,
            mt.status AS mti_status, mt.delete_flagged AS mti_deleted,
            wr.no AS registry_no, wr.word AS registry_word,
            wr.cluster_assignment, wr.verse_context_status, wr.session_b_status
        FROM wa_verse_records vr
        JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id AND ti.delete_flagged = 0
        JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number AND mt.delete_flagged = 0
        JOIN word_registry wr ON wr.id = mt.owning_registry_fk
        WHERE vr.id IN ({ph})
        ORDER BY wr.no, mt.strongs_number
    """, vr_ids).fetchall()

    # Build enriched term entries
    terms = []
    seen_mti = set()

    for tl in term_links:
        mti_id = tl["mti_id"]

        # Verse context classification for this specific verse+term
        vc_records = conn.execute(f"""
            SELECT vc.id AS vc_id, vc.group_id, vc.is_anchor, vc.is_relevant,
                   vc.is_related, vc.set_aside_reason, vc.vertical_pass_flag,
                   vc.notes AS vc_notes, vc.delete_flagged AS vc_deleted,
                   vcg.group_code, vcg.context_description
            FROM verse_context vc
            LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
            WHERE vc.verse_record_id = ? AND vc.mti_term_id = ?
            ORDER BY vc.delete_flagged, vc.is_relevant DESC
        """, (tl["verse_record_id"], mti_id)).fetchall()

        vc_list = [dict(v) for v in vc_records]

        # Dimension data for each group
        for vc in vc_list:
            if vc.get("group_id"):
                di = conn.execute("""
                    SELECT dimension, dimension_confidence, dominant_subject, manual_override
                    FROM wa_dimension_index
                    WHERE verse_context_group_id = ? AND delete_flagged = 0
                """, (vc["group_id"],)).fetchone()
                if di:
                    vc["dimension"] = di["dimension"]
                    vc["dimension_confidence"] = di["dimension_confidence"]
                    vc["dominant_subject"] = di["dominant_subject"]
                    vc["manual_override"] = di["manual_override"]

        # Root family
        root = conn.execute("""
            SELECT rf.root_code, rf.root_language, rf.root_gloss
            FROM wa_term_root_family rf
            JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged = 0
            WHERE ti.strongs_number = ? LIMIT 1
        """, (tl["strongs_number"],)).fetchone()

        # Root siblings (other terms in same root family with their groups)
        root_siblings = []
        if root:
            siblings = conn.execute("""
                SELECT DISTINCT mt2.strongs_number, mt2.transliteration, mt2.gloss,
                    wr2.no AS reg_no, wr2.word AS reg_word
                FROM wa_term_root_family rf2
                JOIN wa_term_inventory ti2 ON ti2.id = rf2.term_inv_id AND ti2.delete_flagged = 0
                JOIN mti_terms mt2 ON mt2.strongs_number = ti2.strongs_number
                  AND mt2.status IN ('extracted', 'extracted_thin') AND mt2.delete_flagged = 0
                JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
                JOIN word_registry wr2 ON wr2.id = fi2.word_registry_fk
                WHERE rf2.root_code = ? AND mt2.strongs_number != ?
                ORDER BY wr2.no, mt2.strongs_number
            """, (root["root_code"], tl["strongs_number"])).fetchall()
            root_siblings = [dict(s) for s in siblings]

        # All groups for this term (not just the one this verse is in)
        all_groups = conn.execute("""
            SELECT vcg.group_code, vcg.context_description,
                di.dimension, di.dimension_confidence, di.dominant_subject,
                (SELECT COUNT(*) FROM verse_context vc2
                 WHERE vc2.group_id = vcg.id AND vc2.delete_flagged = 0) AS verse_count
            FROM verse_context_group vcg
            LEFT JOIN wa_dimension_index di ON di.verse_context_group_id = vcg.id AND di.delete_flagged = 0
            WHERE vcg.mti_term_id = ? AND vcg.delete_flagged = 0
            ORDER BY vcg.group_code
        """, (mti_id,)).fetchall()

        term_entry = {
            "verse_record_id": tl["verse_record_id"],
            "vr_deleted": tl["vr_deleted"],
            "target_word": tl["target_word"],
            "span_strong_match": tl["span_strong_match"],
            "strongs_number": tl["strongs_number"],
            "transliteration": tl["transliteration"],
            "gloss": tl["gloss"],
            "language": tl["language"],
            "mti_id": mti_id,
            "mti_status": tl["mti_status"],
            "term_owner_type": tl["term_owner_type"],
            "registry_no": tl["registry_no"],
            "registry_word": tl["registry_word"],
            "cluster": tl["cluster_assignment"],
            "verse_context": vc_list,
            "all_groups_for_term": [dict(g) for g in all_groups],
            "root": {
                "root_code": root["root_code"] if root else None,
                "root_language": root["root_language"] if root else None,
                "root_gloss": root["root_gloss"] if root else None,
                "siblings": root_siblings,
            } if root else None,
        }
        terms.append(term_entry)

    # Summary stats
    active_terms = [t for t in terms if not t["vr_deleted"]]
    classified = [t for t in active_terms if any(vc.get("is_relevant") is not None for vc in t["verse_context"])]

    return {
        "reference": records[0]["reference"] if records else reference,
        "found": True,
        "verse_text": verse_text,
        "total_term_links": len(terms),
        "active_term_links": len(active_terms),
        "registries_touched": len(set(t["registry_no"] for t in terms)),
        "clusters_touched": len(set(t["cluster"] for t in terms if t["cluster"])),
        "roots_involved": len(set(t["root"]["root_code"] for t in terms if t.get("root"))),
        "term_links": terms,
    }


def main():
    parser = argparse.ArgumentParser(description="Verse-centric vertical pass discovery tool")
    parser.add_argument("verses", nargs="+", help="Verse reference(s) e.g. 'Jer 7:24' 'Rom 10:17'")
    parser.add_argument("--output", help="Custom output filename")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    today = date.today().isoformat()

    verses_out = []
    for ref in args.verses:
        print(f"Processing: {ref}")
        result = discover_verse(conn, ref)
        if result["found"]:
            print(f"  {result['total_term_links']} term links, "
                  f"{result['active_term_links']} active, "
                  f"{result['registries_touched']} registries, "
                  f"{result['roots_involved']} roots")
        else:
            print(f"  NOT FOUND")
        verses_out.append(result)

    output = {
        "produced_date": today,
        "produced_by": "Claude Code — verse_vertical_pass.py",
        "verse_count": len(verses_out),
        "verses": verses_out,
    }

    if args.output:
        out_path = os.path.join(OUT_DIR, args.output)
    else:
        # Generate name from first verse
        safe_ref = args.verses[0].replace(" ", "").replace(":", "-").lower()
        out_path = os.path.join(OUT_DIR, f"wa-verticalpass-{safe_ref}-{today}.json")

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    fsize = os.path.getsize(out_path)
    print(f"\nWritten: {out_path} ({fsize / 1024:.0f} KB)")

    conn.close()


if __name__ == "__main__":
    main()
