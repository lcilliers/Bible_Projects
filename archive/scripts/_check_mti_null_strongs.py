"""Investigate Issue 3: 1 mti_terms row with NULL strongs_number."""
import sqlite3

DB = r"G:\My Drive\Bible_study_projects\data\bible_research.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

print("=" * 70)
print("ISSUE 3 — NULL strongs_number in mti_terms")
print("=" * 70)

cur.execute("""
    SELECT id, strongs_number, transliteration, gloss, language,
           owning_registry, owning_word, owning_part,
           word_data_reference, status, status_note,
           extraction_date, strongs_reconciled, anchor_note
    FROM mti_terms
    WHERE strongs_number IS NULL
""")
rows = cur.fetchall()
print(f"\nRows with NULL strongs: {len(rows)}")
for r in rows:
    print()
    for k in r.keys():
        print(f"  {k:<25}: {r[k]}")

# Also check mti_term_flags and mti_term_cross_refs for these rows
print("\n\nRelated mti_term_flags:")
for r in rows:
    cur.execute("""
        SELECT f.flag_code
        FROM mti_term_flags mf
        JOIN phase2_flag_types f ON f.id = mf.flag_id
        WHERE mf.mti_term_id = ?
    """, (r['id'],))
    flags = [x['flag_code'] for x in cur.fetchall()]
    print(f"  mti_term id={r['id']}: flags={flags}")

print("\n\nRelated mti_term_cross_refs:")
for r in rows:
    cur.execute("""
        SELECT registry, word, part, word_data_reference
        FROM mti_term_cross_refs WHERE mti_term_id = ?
    """, (r['id'],))
    xrefs = cur.fetchall()
    for x in xrefs:
        print(f"  mti_term id={r['id']}: xref → reg={x['registry']} word={x['word']} part={x['part']} wdr={x['word_data_reference']}")
    if not xrefs:
        print(f"  mti_term id={r['id']}: no cross-refs")

# Try to find the strongs from wa_term_inventory by transliteration/gloss match
print("\n\nAttempt recovery — search wa_term_inventory for matching transliteration:")
for r in rows:
    cur.execute("""
        SELECT ti.strongs_number, ti.transliteration, ti.word_analysis_gloss,
               ti.step_search_gloss, fi.word, fi.word_registry_fk
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE LOWER(ti.transliteration) = LOWER(?)
        LIMIT 5
    """, (r['transliteration'],))
    matches = cur.fetchall()
    print(f"\n  Searching transliteration='{r['transliteration']}':")
    if matches:
        for m in matches:
            print(f"    → strongs={m['strongs_number']} trans={m['transliteration']} "
                  f"gloss='{m['word_analysis_gloss']}' word={m['word']} reg={m['word_registry_fk']}")
    else:
        print(f"    (no match by transliteration)")
    # Try gloss match
    cur.execute("""
        SELECT ti.strongs_number, ti.transliteration, ti.word_analysis_gloss,
               fi.word
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE LOWER(ti.word_analysis_gloss) LIKE LOWER(?)
        LIMIT 5
    """, (f"%{r['gloss']}%",))
    gmatches = cur.fetchall()
    print(f"  Searching gloss LIKE '%{r['gloss']}%':")
    if gmatches:
        for m in gmatches:
            print(f"    → strongs={m['strongs_number']} trans={m['transliteration']} "
                  f"gloss='{m['word_analysis_gloss']}' word={m['word']}")
    else:
        print(f"    (no match by gloss)")

conn.close()
