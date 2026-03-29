"""List all 100%-shared words with their terms and cross-registry links."""
import sqlite3
import os

DB = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

words = conn.execute("""
    SELECT no, word, cluster_assignment, unique_term_count, shared_term_count,
           phase1_term_count, phase1_verse_count, session_b_status
    FROM word_registry
    WHERE phase1_status != 'Excluded' AND term_sharing_ratio = 1.0 AND phase1_term_count > 0
    ORDER BY phase1_term_count DESC
""").fetchall()

for w in words:
    reg_no = w["no"]
    print(f'=== {reg_no:>3} {w["word"]} ({w["cluster_assignment"]}) — {w["phase1_term_count"]} terms, {w["phase1_verse_count"]} verses ===')

    terms = conn.execute("""
        SELECT ti.strongs_number, ti.transliteration, ti.step_search_gloss, ti.term_owner_type,
               (SELECT COUNT(*) FROM wa_verse_records vr
                WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0) as vc
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE fi.word_registry_fk = ? AND ti.delete_flagged = 0
        ORDER BY vc DESC
    """, (reg_no,)).fetchall()

    for t in terms:
        # Get also_in registries separately
        also = conn.execute("""
            SELECT GROUP_CONCAT(wr2.word)
            FROM wa_term_inventory ti2
            JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
            JOIN word_registry wr2 ON wr2.id = fi2.word_registry_fk
            WHERE ti2.strongs_number = ? AND ti2.delete_flagged = 0
            AND fi2.registry_id != ?
        """, (t["strongs_number"], reg_no)).fetchone()[0] or ""
        if len(also) > 55:
            also = also[:55] + "..."
        print(f'  {t["strongs_number"]:<10} {(t["transliteration"] or ""):<18} {(t["step_search_gloss"] or ""):<22} {t["term_owner_type"]:<6} {t["vc"]:>4}v  also: {also}')
    print()

conn.close()
