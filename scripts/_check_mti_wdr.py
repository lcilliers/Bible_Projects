"""Dig into mti_terms rows where word_data_reference has no matching wa_file_index row."""
import sqlite3

conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

print('=== All mti_terms with word_data_reference not in wa_file_index ===')
rows = conn.execute('''
    SELECT mt.id, mt.strongs_number, mt.owning_registry, mt.owning_word,
           mt.word_data_reference, mt.status, mt.owning_part
    FROM mti_terms mt
    LEFT JOIN wa_file_index fi ON CAST(mt.word_data_reference AS INTEGER) = fi.id
    WHERE fi.id IS NULL
      AND mt.word_data_reference IS NOT NULL
      AND mt.word_data_reference != ''
    ORDER BY CAST(mt.word_data_reference AS INTEGER)
''').fetchall()
print(f'Total: {len(rows)}')
for r in rows:
    print(f'  mti.id={r["id"]:4}  strongs={str(r["strongs_number"]):12}  '
          f'wdr={r["word_data_reference"]:5}  part={r["owning_part"]}  status={r["status"]}')

wdr_vals = sorted([int(r['word_data_reference']) for r in rows])
print(f'WDR range: {wdr_vals[0]} to {wdr_vals[-1]}')
print(f'Distinct wdr values: {sorted(set(wdr_vals))}')

print()
print('=== wa_file_index rows for peace ===')
fi_rows = conn.execute(
    'SELECT id, word, word_registry_fk, part_number, filename, last_changed '
    'FROM wa_file_index WHERE word = ?', ('peace',)
).fetchall()
for r in fi_rows:
    print(f'  fi.id={r["id"]}  reg_fk={r["word_registry_fk"]}  part={r["part_number"]}  '
          f'filename={r["filename"]}  changed={r["last_changed"]}')

print()
print('=== word_registry for peace ===')
wr = conn.execute(
    'SELECT id, no, word, phase1_status, phase1_term_count FROM word_registry WHERE word = ?',
    ('peace',)
).fetchone()
print('  ', dict(wr) if wr else 'NOT FOUND')

print()
print('=== wa_term_inventory rows for peace (via fi) ===')
ti_count = conn.execute('''
    SELECT COUNT(*) as n FROM wa_term_inventory ti
    JOIN wa_file_index fi ON fi.id = ti.file_id
    WHERE fi.word = 'peace'
''').fetchone()
print(f'  wa_term_inventory rows: {ti_count["n"]}')

print()
print('=== What do the wdr values represent? Max fi.id currently ===')
max_fi = conn.execute('SELECT MAX(id) as m FROM wa_file_index').fetchone()
print(f'  MAX wa_file_index.id = {max_fi["m"]}')
print(f'  Bad wdr values start at {wdr_vals[0]} (above current max: {wdr_vals[0] > max_fi["m"]})')

conn.close()
