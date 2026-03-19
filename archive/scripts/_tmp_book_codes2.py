import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row
rows = conn.execute('SELECT code, book_id FROM book_code_variants ORDER BY book_id').fetchall()
for r in rows:
    print(r['code'], '->', r['book_id'])
print('Total:', len(rows))
