#!/usr/bin/env python3
"""
Delete H4578 (id=490), H5397 (id=491), G5590 (id=493) — researcher confirmed 2026-03-23.
Backup: data/bible_research.db.bak_Before_Delete_DBOnly_20260323_205118
"""
import sqlite3, os

DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "bible_research.db")
FILE_ID = 36
REG_NO  = 182

conn = sqlite3.connect(DB)
conn.execute("PRAGMA foreign_keys = OFF")

try:
    # ── Child tables ──────────────────────────────────────────────
    r1 = conn.execute("DELETE FROM wa_data_quality_flags WHERE file_id=36 AND term_id IN ('H4578','H5397','G5590')").rowcount
    r2 = conn.execute("DELETE FROM wa_term_root_family   WHERE term_inv_id IN (490,491,493)").rowcount
    r3 = conn.execute("DELETE FROM wa_term_related_words WHERE term_inv_id IN (490,491,493)").rowcount
    r4 = conn.execute("DELETE FROM wa_verse_term_links   WHERE term_inv_id IN (490,491,493)").rowcount
    r5 = conn.execute("DELETE FROM wa_term_phase2_flags  WHERE term_inv_id IN (490,491,493)").rowcount
    r6 = conn.execute("DELETE FROM wa_meaning_parsed     WHERE term_inv_id IN (490,491,493)").rowcount

    # ── MTI ───────────────────────────────────────────────────────
    r7 = conn.execute("DELETE FROM mti_terms WHERE id IN (515,516,517)").rowcount

    # ── Inventory ─────────────────────────────────────────────────
    r8 = conn.execute("DELETE FROM wa_term_inventory WHERE id IN (490,491,493)").rowcount

    # ── Registry count ────────────────────────────────────────────
    new_count = conn.execute(
        "SELECT COUNT(*) FROM wa_term_inventory WHERE file_id=? AND delete_flagged=0",
        (FILE_ID,)
    ).fetchone()[0]
    conn.execute("UPDATE word_registry SET phase1_term_count=? WHERE no=?", (new_count, REG_NO))

    conn.commit()
    print("COMMITTED.")
    print(f"  wa_data_quality_flags : -{r1}")
    print(f"  wa_term_root_family   : -{r2}")
    print(f"  wa_term_related_words : -{r3}")
    print(f"  wa_verse_term_links   : -{r4}")
    print(f"  wa_term_phase2_flags  : -{r5}")
    print(f"  wa_meaning_parsed     : -{r6}")
    print(f"  mti_terms             : -{r7}")
    print(f"  wa_term_inventory     : -{r8}")
    print(f"  word_registry.phase1_term_count → {new_count}")

except Exception as exc:
    conn.rollback()
    print(f"ERROR — rolled back: {exc}")
    raise

finally:
    conn.execute("PRAGMA foreign_keys = ON")
    conn.close()
