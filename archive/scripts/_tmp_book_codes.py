import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row
try:
    rows = conn.execute('SELECT code, book_id FROM book_code_variants ORDER BY book_id LIMIT 50').fetchall()
    for r in rows:
        print(r['code'], '->', r['book_id'])
    print('Total:', conn.execute('SELECT COUNT(*) AS c FROM book_code_variants').fetchone()['c'])
except Exception as e:
    print('ERROR:', e)
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    print('Tables:', [r['name'] for r in tables])
