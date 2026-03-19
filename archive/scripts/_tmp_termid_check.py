import sqlite3, csv

DB  = 'data/bible_research.db'
OUT = r'outputs/verses_gen24_21.csv'

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
rows = con.execute("SELECT * FROM wa_verse_records WHERE reference = 'Gen 24:21' ORDER BY id").fetchall()
con.close()

if rows:
    with open(OUT, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows([dict(r) for r in rows])
    print(f'Exported {len(rows)} rows to {OUT}')
else:
    print('No rows found.')
