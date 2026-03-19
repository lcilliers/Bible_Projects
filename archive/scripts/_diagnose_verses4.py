import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

print('=== ROOT CAUSE ANALYSIS ===')
print()
print('wa_file_index uses TWO registry_id formats:')
print("  Old (v4-v8):  zero-padded  e.g. '001', '026', '103'")
print("  New (v9):     plain int    e.g. '9', '26', '103'")
print()

# For each word in word_registry, find ALL verses accessible via any file
print('=== Words with genuinely 0 verses (any route) ===')
rows = conn.execute('''
    SELECT wr.no, wr.word, wr.phase1_status,
           COUNT(DISTINCT vr.id) AS total_verses
    FROM word_registry wr
    LEFT JOIN wa_file_index fi
        ON fi.registry_id IN (
            CAST(wr.no AS TEXT),
            PRINTF('%03d', wr.no)
        )
    LEFT JOIN wa_verse_records vr ON vr.file_id = fi.id
    GROUP BY wr.no
    HAVING total_verses = 0
    ORDER BY wr.no
''').fetchall()
print(f'Words with 0 verses across ALL files: {len(rows)}')
for r in rows:
    print(f'  [{r["no"]:3}] {r["word"]:<30} {r["phase1_status"]}')

print()
print('=== Words accessible via old registry_id format only ===')
rows = conn.execute('''
    SELECT wr.no, wr.word, wr.phase1_status,
           COUNT(DISTINCT vr.id) AS total_verses
    FROM word_registry wr
    JOIN wa_file_index fi
        ON fi.registry_id = PRINTF('%03d', wr.no)
        AND NOT EXISTS (
            SELECT 1 FROM wa_file_index fi2
            WHERE fi2.registry_id = CAST(wr.no AS TEXT)
        )
    LEFT JOIN wa_verse_records vr ON vr.file_id = fi.id
    GROUP BY wr.no
    HAVING total_verses > 0
    ORDER BY wr.no
''').fetchall()
print(f'Words with data ONLY in old-format files (zero-padded): {len(rows)}')
for r in rows:
    print(f'  [{r["no"]:3}] {r["word"]:<30} {r["phase1_status"]}  verses={r["total_verses"]}')

print()
print('=== Breakdown: verse count per word (both sources) ===')
rows = conn.execute('''
    SELECT wr.no, wr.word, wr.phase1_status,
           COUNT(DISTINCT vr.id) AS total_verses,
           SUM(CASE WHEN fi.specification = 'Session A v9 Automation' THEN 1 ELSE 0 END) AS v9_vers,
           SUM(CASE WHEN fi.specification != 'Session A v9 Automation' THEN 1 ELSE 0 END) AS old_vers
    FROM word_registry wr
    LEFT JOIN wa_file_index fi
        ON fi.registry_id IN (CAST(wr.no AS TEXT), PRINTF('%03d', wr.no))
    LEFT JOIN wa_verse_records vr ON vr.file_id = fi.id
    WHERE wr.no <= 30
    GROUP BY wr.no
    ORDER BY wr.no
''').fetchall()
print('no | word                       | status       | total | v9  | old')
print('-' * 75)
for r in rows:
    print(f'{r["no"]:3} | {r["word"]:<26} | {r["phase1_status"]:<12} | {r["total_verses"]:5} | {r["v9_vers"]:3} | {r["old_vers"]:3}')
