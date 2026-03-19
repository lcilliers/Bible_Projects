import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.execute('INSERT OR IGNORE INTO book_code_variants (code, book_id) VALUES (?, ?)', ('Acts', 44))
conn.execute('INSERT OR IGNORE INTO book_code_variants (code, book_id) VALUES (?, ?)', ('Prov', 20))
conn.commit()
rows = conn.execute("SELECT code, book_id FROM book_code_variants WHERE code IN ('Acts', 'Prov')").fetchall()
print('Added. Verify:', [(r[0], r[1]) for r in rows])
conn.close()
