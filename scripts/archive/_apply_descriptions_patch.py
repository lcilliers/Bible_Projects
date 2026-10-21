import sqlite3, json, os

conn = sqlite3.connect(os.path.join('data','bible_research.db'))
cur = conn.cursor()

with open(r'data\imports\WA\Patches\word-descriptions-patch-20260319-v1.json', encoding='utf-8') as f:
    p = json.load(f)

updated = 0
skipped = 0
mismatch = 0

for r in p['records']:
    cur.execute('SELECT word FROM word_registry WHERE id = ?', (r['id'],))
    row = cur.fetchone()
    if row is None:
        skipped += 1
        continue
    if row[0].lower() != r['word'].lower():
        print('  MISMATCH id=' + str(r['id']) + ' DB=' + row[0] + ' patch=' + r['word'])
        mismatch += 1
        continue
    cur.execute('UPDATE word_registry SET description = ? WHERE id = ?', (r['description'], r['id']))
    updated += cur.rowcount

conn.commit()
print('Updated   : ' + str(updated))
print('Skipped   : ' + str(skipped))
print('Mismatches: ' + str(mismatch))
print()

cur.execute("SELECT COUNT(*) FROM word_registry WHERE description IS NOT NULL AND description != ''")
print('Rows with description populated: ' + str(cur.fetchone()[0]))
cur.execute("SELECT COUNT(*) FROM word_registry WHERE description IS NULL OR description = ''")
print('Rows without description       : ' + str(cur.fetchone()[0]))
print()

# Sample a few
cur.execute("SELECT id, word, LENGTH(description) as len FROM word_registry WHERE description IS NOT NULL ORDER BY id LIMIT 5")
for r in cur.fetchall():
    print('  id=' + str(r[0]) + '  ' + str(r[1]).ljust(20) + '  chars=' + str(r[2]))

conn.close()
print('\nDone.')
