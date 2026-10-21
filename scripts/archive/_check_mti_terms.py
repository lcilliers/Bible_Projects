"""Consistency check for mti_terms table."""
import sqlite3

conn = sqlite3.connect('database/bible_research.db')
conn.row_factory = sqlite3.Row

print('=== mti_terms overview ===')
print('Total rows:', conn.execute('SELECT COUNT(*) FROM mti_terms').fetchone()[0])

print()
print('--- status values ---')
for r in conn.execute('SELECT status, COUNT(*) AS n FROM mti_terms GROUP BY status ORDER BY n DESC'):
    print(f'  {str(r["status"]):30} {r["n"]}')

print()
print('--- language values ---')
for r in conn.execute('SELECT language, COUNT(*) AS n FROM mti_terms GROUP BY language ORDER BY n DESC'):
    print(f'  {str(r["language"]):20} {r["n"]}')

print()
print('--- NULL strongs_number ---')
print(' ', conn.execute('SELECT COUNT(*) FROM mti_terms WHERE strongs_number IS NULL').fetchone()[0])

print()
print('--- NULL owning_registry ---')
print(' ', conn.execute('SELECT COUNT(*) FROM mti_terms WHERE owning_registry IS NULL OR owning_registry = ""').fetchone()[0])

print()
print('--- NULL word_data_reference ---')
print(' ', conn.execute('SELECT COUNT(*) FROM mti_terms WHERE word_data_reference IS NULL OR word_data_reference = ""').fetchone()[0])

print()
print('--- strongs_reconciled breakdown ---')
for r in conn.execute('SELECT strongs_reconciled, COUNT(*) AS n FROM mti_terms GROUP BY strongs_reconciled'):
    print(f'  {str(r["strongs_reconciled"]):10} {r["n"]}')

print()
print('--- owning_registry not in word_registry ---')
orphans = conn.execute('''
    SELECT mt.owning_registry, mt.owning_word, COUNT(*) AS n
    FROM mti_terms mt
    LEFT JOIN word_registry wr ON CAST(mt.owning_registry AS INTEGER) = wr.id
    WHERE wr.id IS NULL AND mt.owning_registry IS NOT NULL
    GROUP BY mt.owning_registry, mt.owning_word
    ORDER BY CAST(mt.owning_registry AS INTEGER)
''').fetchall()
print(f'  {len(orphans)} distinct owning_registry values not in word_registry')
for r in orphans:
    print(f'    registry={r["owning_registry"]}  word={r["owning_word"]}  n={r["n"]}')

print()
print('--- word_data_reference not in wa_file_index ---')
bad_wdr = conn.execute('''
    SELECT mt.id, mt.strongs_number, mt.owning_word, mt.word_data_reference
    FROM mti_terms mt
    LEFT JOIN wa_file_index fi ON CAST(mt.word_data_reference AS INTEGER) = fi.id
    WHERE fi.id IS NULL
      AND mt.word_data_reference IS NOT NULL
      AND mt.word_data_reference != ""
''').fetchall()
print(f'  {len(bad_wdr)} rows with word_data_reference not matching wa_file_index')
for r in bad_wdr[:20]:
    print(f'    mti.id={r["id"]}  strongs={r["strongs_number"]}  word={r["owning_word"]}  wdr={r["word_data_reference"]}')

print()
print('--- duplicate strongs_number within same owning_registry ---')
dupes = conn.execute('''
    SELECT owning_registry, owning_word, strongs_number, COUNT(*) AS n
    FROM mti_terms
    WHERE strongs_number IS NOT NULL
    GROUP BY owning_registry, strongs_number
    HAVING COUNT(*) > 1
    ORDER BY CAST(owning_registry AS INTEGER)
''').fetchall()
print(f'  {len(dupes)} duplicate strongs within same registry')
for r in dupes[:20]:
    print(f'    registry={r["owning_registry"]}  word={r["owning_word"]}  strongs={r["strongs_number"]}  n={r["n"]}')

print()
print('--- mti_term_cross_refs overview ---')
print('Total cross-refs:', conn.execute('SELECT COUNT(*) FROM mti_term_cross_refs').fetchone()[0])
bad_xref = conn.execute('''
    SELECT x.id, x.mti_term_id, x.registry, x.word
    FROM mti_term_cross_refs x
    LEFT JOIN mti_terms mt ON mt.id = x.mti_term_id
    WHERE mt.id IS NULL
''').fetchall()
print(f'  cross-refs with missing mti_term_id: {len(bad_xref)}')

bad_xref_reg = conn.execute('''
    SELECT x.registry, x.word, COUNT(*) AS n
    FROM mti_term_cross_refs x
    LEFT JOIN word_registry wr ON CAST(x.registry AS INTEGER) = wr.id
    WHERE wr.id IS NULL
    GROUP BY x.registry, x.word
''').fetchall()
print(f'  cross-refs pointing to missing registry: {len(bad_xref_reg)}')
for r in bad_xref_reg:
    print(f'    registry={r["registry"]}  word={r["word"]}  n={r["n"]}')

conn.close()
