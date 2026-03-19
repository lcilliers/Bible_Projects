import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

print('=== Multiple wa_file_index rows per registry (duplicates) ===')
rows = conn.execute('''
    SELECT fi.registry_id, fi.word,
           GROUP_CONCAT(fi.id || ':' || COALESCE(vc.cnt,0) ORDER BY fi.id) AS id_verses
    FROM wa_file_index fi
    LEFT JOIN (
        SELECT file_id, COUNT(*) AS cnt FROM wa_verse_records GROUP BY file_id
    ) vc ON vc.file_id = fi.id
    GROUP BY fi.registry_id
    HAVING COUNT(fi.id) > 1
    ORDER BY fi.registry_id
''').fetchall()
print(f'  Registries with >1 file_index row: {len(rows)}')
for r in rows[:20]:
    print(f'  registry={r["registry_id"]:<5} word={r["word"]:<25} files(id:verses)={r["id_verses"]}')

print()
print('=== word_registry: which file_id is "active"? ===')
# The wa_file_index has specification field - check what's there
spec_rows = conn.execute('''
    SELECT specification, COUNT(*) AS cnt FROM wa_file_index GROUP BY specification
''').fetchall()
for r in spec_rows:
    print(f'  specification={repr(r["specification"]):<20} count={r["cnt"]}')

print()
print('=== wa_file_index sample showing specification + verse count ===')
rows = conn.execute('''
    SELECT fi.id, fi.registry_id, fi.word, fi.specification,
           COALESCE(vc.cnt,0) AS verses
    FROM wa_file_index fi
    LEFT JOIN (
        SELECT file_id, COUNT(*) AS cnt FROM wa_verse_records GROUP BY file_id
    ) vc ON vc.file_id = fi.id
    WHERE fi.registry_id IN ('9','10','12','14','21')
    ORDER BY fi.registry_id, fi.id
''').fetchall()
for r in rows:
    print(f'  id={r["id"]:3} registry={r["registry_id"]:<5} word={r["word"]:<20} spec={repr(r["specification"]):<15} verses={r["verses"]}')

print()
print('=== Overall: how many registries have at least 1 file with verses? ===')
rows = conn.execute('''
    SELECT COUNT(DISTINCT fi.registry_id) AS registries_with_verses
    FROM wa_file_index fi
    JOIN wa_verse_records vr ON vr.file_id = fi.id
''').fetchone()
print(f'  Registries with verses: {rows["registries_with_verses"]}')

total_reg = conn.execute('SELECT COUNT(*) FROM word_registry').fetchone()[0]
print(f'  Total word_registry entries: {total_reg}')

print()
print('=== word_registry entries with NO file_index row having verses ===')
rows = conn.execute('''
    SELECT wr.no, wr.word, wr.phase1_status, wr.phase1_verse_count
    FROM word_registry wr
    WHERE wr.phase1_status NOT IN ('Pending', 'N/A')
      AND NOT EXISTS (
          SELECT 1 FROM wa_file_index fi
          JOIN wa_verse_records vr ON vr.file_id = fi.id
          WHERE fi.registry_id = CAST(wr.no AS TEXT)
      )
    ORDER BY wr.no
    LIMIT 30
''').fetchall()
print(f'  Count: {len(rows)}')
for r in rows[:20]:
    print(f'  [{r["no"]:3}] {r["word"]:<25} {r["phase1_status"]:<12} wr_verses={r["phase1_verse_count"]}')
