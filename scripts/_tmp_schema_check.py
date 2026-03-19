import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row
print('word_run_state cols:', [c['name'] for c in conn.execute('PRAGMA table_info(word_run_state)')])
tables = [r['name'] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%flag%'")]
print('flag tables:', tables)
for t in tables:
    print(t, [c['name'] for c in conn.execute(f'PRAGMA table_info({t})')])
# Sample a word_run_state row
row = conn.execute('SELECT * FROM word_run_state LIMIT 1').fetchone()
if row:
    print('\nSample word_run_state row:')
    for k in row.keys():
        v = row[k]
        if v and len(str(v)) > 100:
            v = str(v)[:100] + '...'
        print(f'  {k}: {v}')
