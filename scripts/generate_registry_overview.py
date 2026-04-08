"""
generate_registry_overview.py
─────────────────────────────
Generates the registry overview JSON export per RMG v5.7 Section 6c.3.

Includes:
  - All word_registry fields
  - live_owner_count, live_xref_count, live_verse_count (broad count)
  - vcb_scope_verse_count (Section 6c.1 — extracted/extracted_thin OWNER only)
  - special_status_verse_count (Section 6c.2 — theological_anchor + phase2_enrichment)
  - vc_groups, vc_relevant, vc_set_aside, vc_anchors
  - dimension_profile

Output: outputs/reports/programme/wa-registry-overview-{date}.json

Usage:
  python scripts/generate_registry_overview.py
"""
import sqlite3
import os
import json
from datetime import date

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs", "reports", "programme")


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    today = date.today().isoformat()

    regs = conn.execute("SELECT * FROM word_registry ORDER BY no").fetchall()

    registries = []
    for r in regs:
        reg_id = r["id"]

        # Live counts (broad — all active verses regardless of mti_status)
        owner = conn.execute("""SELECT COUNT(*) FROM wa_term_inventory
            WHERE file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk=?)
            AND term_owner_type='OWNER' AND delete_flagged=0""", (reg_id,)).fetchone()[0]
        xref = conn.execute("""SELECT COUNT(*) FROM wa_term_inventory
            WHERE file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk=?)
            AND term_owner_type='XREF' AND delete_flagged=0""", (reg_id,)).fetchone()[0]
        live_verses = conn.execute("""SELECT COUNT(*) FROM wa_verse_records
            WHERE file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk=?)
            AND delete_flagged=0""", (reg_id,)).fetchone()[0]

        # VCB-scope verse count (Section 6c.1)
        vcb_scope = conn.execute("""
            SELECT COUNT(DISTINCT vr.id) FROM wa_verse_records vr
            JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
              AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
            JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
              AND mt.status IN ('extracted', 'extracted_thin') AND mt.delete_flagged = 0
            WHERE vr.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
            AND vr.delete_flagged = 0
        """, (reg_id,)).fetchone()[0]

        # Special-status verse count (Section 6c.2)
        special_status = conn.execute("""
            SELECT COUNT(DISTINCT vr.id) FROM wa_verse_records vr
            JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
              AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
            JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
              AND mt.status IN ('extracted_theological_anchor', 'phase2_enrichment')
              AND mt.delete_flagged = 0
            WHERE vr.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
            AND vr.delete_flagged = 0
        """, (reg_id,)).fetchone()[0]

        # Verse context stats
        vc_groups = conn.execute("""SELECT COUNT(*) FROM verse_context_group vcg
            JOIN mti_terms mt ON mt.id = vcg.mti_term_id
            JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
              AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
            WHERE ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
            AND vcg.delete_flagged = 0""", (reg_id,)).fetchone()[0]
        vc_relevant = conn.execute("""SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
              AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
            WHERE ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
            AND vc.is_relevant = 1 AND vc.delete_flagged = 0""", (reg_id,)).fetchone()[0]
        vc_set_aside = conn.execute("""SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
              AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
            WHERE ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
            AND vc.is_relevant = 0 AND vc.delete_flagged = 0""", (reg_id,)).fetchone()[0]
        vc_anchors = conn.execute("""SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
              AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
            WHERE ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
            AND vc.is_anchor = 1 AND vc.delete_flagged = 0""", (reg_id,)).fetchone()[0]

        # Dimension profile
        dims = conn.execute("""SELECT di.dimension, COUNT(*) as c
            FROM wa_dimension_index di
            JOIN wa_term_inventory ti ON ti.strongs_number = di.strongs_number
              AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
            WHERE ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
            AND di.dimension IS NOT NULL AND di.delete_flagged = 0
            GROUP BY di.dimension ORDER BY c DESC""", (reg_id,)).fetchall()
        dim_profile = {d["dimension"]: d["c"] for d in dims} if dims else None

        entry = {k: r[k] for k in r.keys()}
        entry["live_owner_count"] = owner
        entry["live_xref_count"] = xref
        entry["live_verse_count"] = live_verses
        entry["vcb_scope_verse_count"] = vcb_scope
        entry["special_status_verse_count"] = special_status
        entry["vc_groups"] = vc_groups
        entry["vc_relevant"] = vc_relevant
        entry["vc_set_aside"] = vc_set_aside
        entry["vc_anchors"] = vc_anchors
        entry["dimension_profile"] = dim_profile
        registries.append(entry)

    result = {
        "exported_date": today,
        "total_registries": len(registries),
        "schema_note": "v5.7 — includes vcb_scope_verse_count and special_status_verse_count per RMG Section 6c.3",
        "registries": registries,
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, f"wa-registry-overview-{today.replace('-', '')}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    fsize = os.path.getsize(out_path)
    print(f"Written: {out_path}")
    print(f"Registries: {len(registries)}")
    print(f"Size: {fsize / 1024:.0f} KB")

    conn.close()


if __name__ == "__main__":
    main()
