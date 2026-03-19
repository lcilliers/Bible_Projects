import sqlite3, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row
rows = conn.execute('SELECT * FROM mti_terms WHERE owning_registry=117 AND strongs_number="H7999A"').fetchall()
for r in rows:
    print(dict(r))
ti_rows = conn.execute('SELECT * FROM wa_term_inventory WHERE strongs_number="H7999A" AND file_id IN (48,49,50)').fetchall()
for r in ti_rows:
    print(dict(r))
