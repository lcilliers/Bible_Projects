"""Dig deeper into the two distinct bad-wdr groups."""
import sqlite3

conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

# ── Group A: numeric WDR values not in wa_file_index (peace) ──────────────
print('=== GROUP A: numeric WDR — peace (parts 1/2/3) ===')
peace_rows = conn.execute('''
    SELECT mt.id, mt.strongs_number, mt.owning_registry, mt.owning_word,
           mt.word_data_reference, mt.owning_part, mt.status
    FROM mti_terms mt
    LEFT JOIN wa_file_index fi ON CAST(mt.word_data_reference AS INTEGER) = fi.id
    WHERE fi.id IS NULL
      AND mt.word_data_reference IS NOT NULL
      AND mt.word_data_reference != ''
      AND mt.word_data_reference GLOB '[0-9]*'
    ORDER BY mt.owning_part, CAST(mt.word_data_reference AS INTEGER)
''').fetchall()
print(f'Rows: {len(peace_rows)}')
parts = {}
for r in peace_rows:
    parts.setdefault(r['owning_part'], []).append(r)
for part, prows in sorted(parts.items()):
    wdrs = sorted(set(int(r['word_data_reference']) for r in prows))
    print(f'  Part {part}: {len(prows)} terms, wdr range {wdrs[0]}–{wdrs[-1]}')

print()
print('What wa_file_index rows actually exist for peace?')
fi_peace = conn.execute(
    'SELECT id, word, word_registry_fk, part_number, total_parts, is_split, filename '
    'FROM wa_file_index WHERE word = ?', ('peace',)
).fetchall()
for r in fi_peace:
    print(f'  fi.id={r["id"]}  reg_fk={r["word_registry_fk"]}  '
          f'part={r["part_number"]}/{r["total_parts"]}  split={r["is_split"]}  '
          f'filename={r["filename"]}')

print()
max_fi = conn.execute('SELECT MAX(id) as m FROM wa_file_index').fetchone()
print(f'MAX wa_file_index.id currently = {max_fi["m"]}')
print(f'Peace wdr values: 617–650 (well above current max)')

# ── Group B: filename-style WDR (gladness) ────────────────────────────────
print()
print('=== GROUP B: filename-style WDR — gladness ===')
glad_rows = conn.execute('''
    SELECT mt.id, mt.strongs_number, mt.owning_registry, mt.owning_word,
           mt.word_data_reference, mt.owning_part, mt.status
    FROM mti_terms mt
    WHERE mt.word_data_reference IS NOT NULL
      AND mt.word_data_reference NOT GLOB '[0-9]*'
      AND mt.word_data_reference != ''
    ORDER BY mt.id
''').fetchall()
print(f'Rows: {len(glad_rows)}')
for r in glad_rows:
    print(f'  mti.id={r["id"]}  strongs={str(r["strongs_number"]):12}  '
          f'wdr={r["word_data_reference"]}  status={r["status"]}')

print()
print('What wa_file_index rows exist for gladness?')
fi_glad = conn.execute(
    'SELECT id, word, word_registry_fk, part_number, filename '
    'FROM wa_file_index WHERE word = ?', ('gladness',)
).fetchall()
for r in fi_glad:
    print(f'  fi.id={r["id"]}  reg_fk={r["word_registry_fk"]}  '
          f'part={r["part_number"]}  filename={r["filename"]}')

print()
print('word_registry for gladness:')
wr_g = conn.execute(
    'SELECT id, no, word, phase1_status FROM word_registry WHERE word = ?', ('gladness',)
).fetchone()
print(' ', dict(wr_g) if wr_g else 'NOT FOUND')

# Does any wa_term_inventory exist for gladness?
ti_g = conn.execute('''
    SELECT COUNT(*) as n FROM wa_term_inventory ti
    JOIN wa_file_index fi ON fi.id = ti.file_id
    WHERE fi.word = 'gladness'
''').fetchone()
print(f'  wa_term_inventory rows for gladness: {ti_g["n"]}')

conn.close()
