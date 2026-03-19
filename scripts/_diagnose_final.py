import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

print('=== VERSE DATA DIAGNOSTIC — Full picture ===')
print()

# Total counts
total_vr = conn.execute('SELECT COUNT(*) FROM wa_verse_records').fetchone()[0]
total_ti = conn.execute('SELECT COUNT(*) FROM wa_term_inventory').fetchone()[0]
total_fi = conn.execute('SELECT COUNT(*) FROM wa_file_index').fetchone()[0]
print(f'wa_verse_records total:      {total_vr:>7}')
print(f'wa_term_inventory total:     {total_ti:>7}')
print(f'wa_file_index total:         {total_fi:>7}')
print()

# wa_term_inventory rows with 0 verses
ti_zero = conn.execute('''
    SELECT COUNT(*) FROM wa_term_inventory ti
    WHERE NOT EXISTS (
        SELECT 1 FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id
    )
''').fetchone()[0]
print(f'wa_term_inventory rows with 0 verse records: {ti_zero} of {total_ti}')
print()

# Breakdown: which of those are XREF-owned terms?
# XREF means: the term's mti_terms row points to a different file
ti_xref_zero = conn.execute('''
    SELECT COUNT(*) FROM wa_term_inventory ti
    WHERE NOT EXISTS (SELECT 1 FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id)
      AND EXISTS (
          SELECT 1 FROM mti_terms mt
          WHERE mt.strongs_number = ti.strongs_number
            AND mt.word_data_reference != CAST(ti.file_id AS TEXT)
      )
''').fetchone()[0]
print(f'  Of those: {ti_xref_zero} are XREF terms (owned by a different file)')

# Verses reachable via strongs for those XREF terms
xref_reachable = conn.execute('''
    SELECT COUNT(DISTINCT vr.id) FROM wa_term_inventory ti_original
    JOIN mti_terms mt ON mt.strongs_number = ti_original.strongs_number
    JOIN wa_term_inventory ti_owner ON CAST(ti_owner.file_id AS TEXT) = mt.word_data_reference
       AND ti_owner.strongs_number = ti_original.strongs_number
    JOIN wa_verse_records vr ON vr.term_inv_id = ti_owner.id
    WHERE NOT EXISTS (SELECT 1 FROM wa_verse_records vr2 WHERE vr2.term_inv_id = ti_original.id)
''').fetchone()[0]
print(f'  Verses reachable via strongs cross-lookup for those terms: {xref_reachable}')
print()

# Word-level: how many words are affected
print('=== Per-word verse access ===')
print('(both old zero-padded + new plain registry_id formats covered)')
print()

words_direct = conn.execute('''
    SELECT COUNT(DISTINCT fi.registry_id) FROM wa_file_index fi
    JOIN wa_verse_records vr ON vr.file_id = fi.id
''').fetchone()[0]

print(f'File_index entries with at least 1 direct verse: {words_direct} of {total_fi}')
print()

# Per word_registry: verses direct vs via strongs
print('=== Words with 0 DIRECT verses but verses accessible via strongs lookup ===')
rows = conn.execute('''
    SELECT wr.no, wr.word, wr.phase1_status,
           -- Direct verses (via file_index owned by this word)
           (SELECT COUNT(DISTINCT vr.id) FROM wa_file_index fi
            LEFT JOIN wa_verse_records vr ON vr.file_id = fi.id
            WHERE fi.registry_id IN (CAST(wr.no AS TEXT), PRINTF('%03d', wr.no))
           ) AS direct_verses,
           -- Verses via strongs (owned by any file for this word's terms)
           (SELECT COUNT(DISTINCT vr.id)
            FROM wa_file_index fi
            JOIN wa_term_inventory ti ON ti.file_id = fi.id
            JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
            JOIN wa_term_inventory ti2 ON CAST(ti2.file_id AS TEXT) = mt.word_data_reference
               AND ti2.strongs_number = ti.strongs_number
            JOIN wa_verse_records vr ON vr.term_inv_id = ti2.id
            WHERE fi.registry_id IN (CAST(wr.no AS TEXT), PRINTF('%03d', wr.no))
           ) AS strongs_verses
    FROM word_registry wr
    WHERE wr.phase1_status NOT IN ('Pending')
    ORDER BY wr.no
''').fetchall()

print(f'{"no":>4} {"word":<28} {"status":<14} {"direct":>7} {"via_strongs":>11}')
print('-' * 70)
for r in rows:
    flag = ' *** NO DATA' if r['direct_verses'] == 0 and r['strongs_verses'] == 0 else (
           ' (XREF)' if r['direct_verses'] == 0 else '')
    print(f'{r["no"]:>4} {r["word"]:<28} {r["phase1_status"]:<14} {r["direct_verses"]:>7} {r["strongs_verses"]:>11}{flag}')

print()
print('=== SUMMARY ===')
no_data = [(r['no'], r['word']) for r in rows if r['direct_verses'] == 0 and r['strongs_verses'] == 0]
xref_only = [(r['no'], r['word']) for r in rows if r['direct_verses'] == 0 and r['strongs_verses'] > 0]
has_direct = [r for r in rows if r['direct_verses'] > 0]
print(f'Words with direct verse records:               {len(has_direct)}')
print(f'Words with 0 direct but accessible via XREF:  {len(xref_only)}')
print(f'Words with genuinely 0 accessible verses:      {len(no_data)}')
print()
if no_data:
    print('GENUINELY EMPTY words:')
    for no, word in no_data:
        print(f'  [{no:3}] {word}')
