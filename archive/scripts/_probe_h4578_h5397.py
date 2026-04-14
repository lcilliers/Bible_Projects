"""Deep probe of H4578 and H5397 across all tables."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine.db import get_connection
conn = get_connection()

for code in ['H4578', 'H5397']:
    print('=' * 60)
    print(f'CODE: {code}')
    print('=' * 60)

    # All mti_terms rows for this strongs_number (any registry)
    rows = conn.execute(
        "SELECT id, strongs_number, gloss, language, owning_registry, owning_registry_fk, owning_word FROM mti_terms WHERE strongs_number=?",
        (code,)
    ).fetchall()
    print(f'mti_terms rows (all registries):')
    for r in rows:
        print(f'  id={r["id"]} owning_registry={r["owning_registry"]} owning_word={r["owning_word"]} gloss={r["gloss"]}')

    # Cross-refs pointing FROM this term
    mti_ids = [r['id'] for r in rows]
    for mid in mti_ids:
        xrefs = conn.execute(
            "SELECT registry, word, part FROM mti_term_cross_refs WHERE mti_term_id=?",
            (mid,)
        ).fetchall()
        if xrefs:
            print(f'  mti_term_cross_refs for mti_id={mid}:')
            for x in xrefs:
                print(f'    → registry={x["registry"]} word={x["word"]} part={x["part"]}')

    # word_registry — does this strongs code appear in any word's strongs_list?
    # Also check if any word has this as its primary term
    # First look for any wa_term_inventory entries for this code
    inv_rows = conn.execute(
        "SELECT ti.id, ti.file_id, ti.strongs_number, ti.step_search_gloss, fi.word, fi.registry_id "
        "FROM wa_term_inventory ti "
        "JOIN wa_file_index fi ON fi.id = ti.file_id "
        "WHERE ti.strongs_number=?",
        (code,)
    ).fetchall()
    print(f'wa_term_inventory rows (all files):')
    for r in inv_rows:
        vc = conn.execute(
            "SELECT COUNT(*) FROM wa_verse_records WHERE term_inv_id=?",
            (r['id'],)
        ).fetchone()[0]
        print(f'  ti_id={r["id"]} file_id={r["file_id"]} word={r["word"]} registry={r["registry_id"]} gloss={r["step_search_gloss"]} verse_count={vc}')

    # Is there a word_registry entry whose primary word IS this concept?
    # Search for approximate match
    candidates = conn.execute(
        "SELECT no, word, phase1_status FROM word_registry WHERE LOWER(word) IN (?, ?, ?, ?)",
        ('belly', 'bowels', 'breath', 'neshamah') if code == 'H4578' else ('breath', 'neshamah', 'spirit', 'wind')
    ).fetchall()
    print(f'word_registry candidates (by English gloss):')
    for r in candidates:
        print(f'  no={r["no"]} word={r["word"]} phase1_status={r["phase1_status"]}')

    print()
