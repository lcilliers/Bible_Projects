import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

print('=== Table row counts ===')
for tbl in ['wa_file_index', 'wa_term_inventory', 'wa_verse_records', 'mti_terms', 'wa_meaning_parsed']:
    c = conn.execute(f'SELECT COUNT(*) FROM {tbl}').fetchone()[0]
    print(f'  {tbl:<30} {c:>8}')

print()
print('=== wa_verse_records column names ===')
cols = [c['name'] for c in conn.execute('PRAGMA table_info(wa_verse_records)')]
print(' ', cols)

print()
print('=== wa_term_inventory column names ===')
cols = [c['name'] for c in conn.execute('PRAGMA table_info(wa_term_inventory)')]
print(' ', cols)

print()
print('=== Sample wa_verse_records rows (5) ===')
rows = conn.execute('SELECT * FROM wa_verse_records LIMIT 5').fetchall()
for r in rows:
    print(' ', dict(r))

print()
print('=== Verses per file_id (top 10 by verse count) ===')
rows = conn.execute('''
    SELECT fi.id, fi.word, fi.registry_id,
           COUNT(vr.id) AS verse_count
    FROM wa_file_index fi
    LEFT JOIN wa_verse_records vr ON vr.file_id = fi.id
    GROUP BY fi.id
    ORDER BY verse_count DESC
    LIMIT 10
''').fetchall()
for r in rows:
    print(f'  file_id={r["id"]:3} word={r["word"]:<25} registry={r["registry_id"]:>4} verses={r["verse_count"]}')

print()
print('=== Files with 0 verses (first 10) ===')
rows = conn.execute('''
    SELECT fi.id, fi.word, fi.registry_id,
           COUNT(vr.id) AS verse_count
    FROM wa_file_index fi
    LEFT JOIN wa_verse_records vr ON vr.file_id = fi.id
    GROUP BY fi.id
    HAVING verse_count = 0
    ORDER BY fi.id
    LIMIT 10
''').fetchall()
for r in rows:
    print(f'  file_id={r["id"]:3} word={r["word"]:<25} registry={r["registry_id"]}')

print()
print('=== verse_text sample — does it hold actual text? ===')
has_text = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE verse_text IS NOT NULL AND verse_text != ''").fetchone()[0]
total_vr = conn.execute("SELECT COUNT(*) FROM wa_verse_records").fetchone()[0]
print(f'  Rows with verse_text: {has_text} / {total_vr}')

print()
print('=== wa_verse_records join check (via term_inv_id vs file_id) ===')
via_ti = conn.execute('''
    SELECT COUNT(*) FROM wa_verse_records vr
    JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
''').fetchone()[0]
via_fi = conn.execute('SELECT COUNT(*) FROM wa_verse_records').fetchone()[0]
print(f'  Total verse_records: {via_fi}')
print(f'  With valid term_inv_id join: {via_ti}')
orphaned = conn.execute('''
    SELECT COUNT(*) FROM wa_verse_records
    WHERE term_inv_id NOT IN (SELECT id FROM wa_term_inventory)
''').fetchone()[0]
print(f'  Orphaned (no matching term_inventory): {orphaned}')

print()
print('=== word_registry phase1 summary ===')
rows = conn.execute('''
    SELECT phase1_status, COUNT(*) AS cnt,
           SUM(phase1_verse_count) AS total_verses
    FROM word_registry
    GROUP BY phase1_status
    ORDER BY cnt DESC
''').fetchall()
for r in rows:
    print(f'  {r["phase1_status"]:<15} {r["cnt"]:>4} words   {r["total_verses"] or 0:>7} verses')
