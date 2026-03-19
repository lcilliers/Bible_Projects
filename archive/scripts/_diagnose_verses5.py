import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

print('=== XREF cross-links table ===')
tbls = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND (name LIKE '%xref%' OR name LIKE '%cross%')").fetchall()]
print('Tables:', tbls)
for t in tbls:
    if t.startswith('sqlite_'):
        continue
    cols = [c['name'] for c in conn.execute(f'PRAGMA table_info({t})').fetchall()]
    cnt = conn.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
    print(f'  {t}: {cnt} rows, cols={cols}')
    if cnt > 0:
        for r in conn.execute(f'SELECT * FROM {t} LIMIT 3').fetchall():
            print(f'    {dict(r)}')

print()
print('=== For XREF words: can verses be reached via strongs lookup? ===')
# For assent (no=9), what strongs does it have in mti_terms?
for no, word in [(9,'assent'),(14,'blamelessness'),(25,'conformity'),(30,'contrition')]:
    fi = conn.execute("SELECT id FROM wa_file_index WHERE registry_id = ?", (str(no),)).fetchone()
    if fi:
        xrefs = conn.execute("""
            SELECT mc.xref_strongs, mc.xref_file_id, fi2.word AS xref_word,
                   COUNT(vr.id) AS verses
            FROM wa_xref_crosslinks mc
            JOIN wa_file_index fi2 ON fi2.id = mc.xref_file_id
            LEFT JOIN wa_verse_records vr ON vr.file_id = mc.xref_file_id
            WHERE mc.this_file_id = ?
            GROUP BY mc.xref_strongs
        """, (fi['id'],)).fetchall()
    else:
        print(f'  [{no}] {word}: NO file_index row found')

print()
print('=== SUMMARY: what the user sees vs what exists ===')
print()
print('Route 1: word → registry → wa_file_index (v9 file) → wa_verse_records')
print('  → XREF-only words: 0 verses (terms owned by other words)')
print()
print('Route 2: word → registry → wa_file_index → wa_xref_crosslinks → other file → wa_verse_records')
print('  → XREF verses accessible but requires two-hop join')
print()
print('Route 3: strongs → wa_term_inventory (any file) → wa_verse_records')
print('  → Always works regardless of which file owns the term')
print()

# Count total accessible verses per word via Route 3 (strongs lookup)
print('=== Accessible verses via strongs for first 10 zero-verse words ===')
zero_words = [(9,'assent'),(10,'awareness'),(12,'betrayal'),(14,'blamelessness'),
              (21,'commitment'),(22,'communion'),(25,'conformity'),(30,'contrition'),
              (36,'cowardice'),(37,'darkening')]
for no, word in zero_words:
    # Get strongs from mti_terms for this word's file
    fi = conn.execute("SELECT id FROM wa_file_index WHERE registry_id = ?", (str(no),)).fetchone()
    if fi:
        # Try via XREF crosslinks
        xrefs = conn.execute("""
            SELECT COUNT(DISTINCT vr.id) AS verses
            FROM wa_xref_crosslinks xr
            JOIN wa_verse_records vr ON vr.file_id = xr.xref_file_id
            WHERE xr.this_file_id = ?
        """, (fi['id'],)).fetchone()
        print(f'  [{no}] {word}: file_id={fi["id"]}, xref-accessible verses={xrefs["verses"] if xrefs else "N/A"}')
    else:
        print(f'  [{no}] {word}: no file_index')
