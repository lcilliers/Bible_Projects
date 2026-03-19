import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

tbls = [r[0] for r in conn.execute(
    "SELECT tbl_name FROM sqlite_master WHERE type='table' AND (tbl_name LIKE '%xref%' OR tbl_name LIKE '%cross%')"
    " AND tbl_name NOT LIKE 'sqlite_%' AND tbl_name NOT LIKE 'idx_%'"
).fetchall()]
print('XREF/cross tables:', tbls)
for t in tbls:
    cols = [c['name'] for c in conn.execute(f'PRAGMA table_info({t})').fetchall()]
    cnt = conn.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
    print(f'\n{t}: {cnt} rows\n  cols={cols}')
    for r in conn.execute(f'SELECT * FROM {t} LIMIT 3').fetchall():
        print(f'  {dict(r)}')

print()
print('=== mti_terms structure ===')
cols = [c['name'] for c in conn.execute('PRAGMA table_info(mti_terms)').fetchall()]
print('cols:', cols)
for r in conn.execute('SELECT * FROM mti_terms LIMIT 3').fetchall():
    print(' ', dict(r))

print()
print('=== term_fetch_log (if exists) ===')
tfl = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND tbl_name='term_fetch_log'").fetchone()[0]
print('term_fetch_log exists:', bool(tfl))
if tfl:
    cols = [c['name'] for c in conn.execute('PRAGMA table_info(term_fetch_log)').fetchall()]
    print('cols:', cols)
