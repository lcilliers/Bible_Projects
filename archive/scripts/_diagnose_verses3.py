import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

print('=== Old file_index rows (non-v9) — what registry_id do they use? ===')
rows = conn.execute('''
    SELECT fi.id, fi.registry_id, fi.word, fi.specification,
           COALESCE(vc.cnt,0) AS verses
    FROM wa_file_index fi
    LEFT JOIN (
        SELECT file_id, COUNT(*) AS cnt FROM wa_verse_records GROUP BY file_id
    ) vc ON vc.file_id = fi.id
    WHERE fi.specification != 'Session A v9 Automation'
    ORDER BY fi.id
''').fetchall()
print(f'  Total non-v9 files: {len(rows)}')
for r in rows:
    print(f'  id={r["id"]:3} registry_id={repr(r["registry_id"]):<10} word={r["word"]:<20} spec={r["specification"]!r:<30} verses={r["verses"]}')

print()
print('=== Terms with 0 verse records ===')
zero = conn.execute('''
    SELECT ti.id, ti.file_id, ti.strongs_number, ti.language,
           fi.word, fi.registry_id, fi.specification,
           COUNT(vr.id) AS verse_count
    FROM wa_term_inventory ti
    JOIN wa_file_index fi ON fi.id = ti.file_id
    LEFT JOIN wa_verse_records vr ON vr.term_inv_id = ti.id
    GROUP BY ti.id
    HAVING verse_count = 0
    ORDER BY ti.file_id
    LIMIT 30
''').fetchall()
print(f'  Terms with 0 verses: {len(zero)} (showing 30)')
for r in zero[:20]:
    print(f'  ti.id={r["id"]:3} file_id={r["file_id"]:3} strongs={r["strongs_number"]:<8} word={r["word"]:<20} spec={r["specification"]!r}')

print()
print('=== v9 Automation words with 0 verses — are they all XREF? ===')
rows = conn.execute('''
    SELECT wr.no, wr.word, wr.phase1_status, wr.phase1_verse_count,
           COUNT(ti.id) AS term_count,
           SUM(COALESCE(vc.cnt,0)) AS actual_verse_count
    FROM word_registry wr
    JOIN wa_file_index fi ON fi.registry_id = CAST(wr.no AS TEXT)
        AND fi.specification = 'Session A v9 Automation'
    LEFT JOIN wa_term_inventory ti ON ti.file_id = fi.id
    LEFT JOIN (
        SELECT term_inv_id, COUNT(*) AS cnt FROM wa_verse_records GROUP BY term_inv_id
    ) vc ON vc.term_inv_id = ti.id
    GROUP BY wr.no
    HAVING actual_verse_count = 0
    ORDER BY wr.no
    LIMIT 30
''').fetchall()
print(f'  v9 words reporting 0 actual verses: {len(rows)}')
for r in rows:
    print(f'  [{r["no"]:3}] {r["word"]:<25} {r["phase1_status"]:<14} terms={r["term_count"]} wr_verses={r["phase1_verse_count"]}')

print()
print('=== SUMMARY: verse count by source ===')
old = conn.execute('''
    SELECT SUM(COALESCE(vc.cnt,0)) AS verses
    FROM wa_file_index fi
    LEFT JOIN (SELECT file_id, COUNT(*) as cnt FROM wa_verse_records GROUP BY file_id) vc
    ON vc.file_id = fi.id
    WHERE fi.specification != 'Session A v9 Automation'
''').fetchone()['verses']
new = conn.execute('''
    SELECT SUM(COALESCE(vc.cnt,0)) AS verses
    FROM wa_file_index fi
    LEFT JOIN (SELECT file_id, COUNT(*) as cnt FROM wa_verse_records GROUP BY file_id) vc
    ON vc.file_id = fi.id
    WHERE fi.specification = 'Session A v9 Automation'
''').fetchone()['verses']
print(f'  Old (v4-v8) files: {old} verses')
print(f'  New (v9) files:    {new} verses')
print(f'  Total:             {(old or 0)+(new or 0)} verses')
