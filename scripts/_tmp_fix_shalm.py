import sqlite3
conn = sqlite3.connect('data/bible_research.db')
reason = 'Consolidated sub-gloss of sha.lem (H7999A). Verse set handled by sha.lem entry (id=416). No separate verse record.'
conn.execute('UPDATE mti_terms SET exclusion_reason = ? WHERE id = 414', (reason,))
conn.commit()
row = conn.execute('SELECT id, strongs_number, transliteration, exclusion_reason FROM mti_terms WHERE id = 414').fetchone()
print(row)
