import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

print('=== word_registry rows for peace and sorrow ===')
words = ('peace', 'sorrow')
for r in conn.execute('SELECT no, word, phase1_status, phase1_term_count, phase1_verse_count, strongs_list FROM word_registry WHERE word IN (?,?) ORDER BY word', words):
    print(f'  no={r["no"]}  word={r["word"]}  status={r["phase1_status"]}  terms={r["phase1_term_count"]}  verses={r["phase1_verse_count"]}  strongs={r["strongs_list"]}')

print()
print('=== wa_file_index rows for peace and sorrow ===')
for r in conn.execute('SELECT id, registry_id, word, specification, testament_coverage FROM wa_file_index WHERE word IN (?,?) ORDER BY word, id', words):
    vc = conn.execute('SELECT COUNT(*) FROM wa_verse_records WHERE file_id=?', (r['id'],)).fetchone()[0]
    print(f'  file_id={r["id"]}  registry_id={r["registry_id"]}  word={r["word"]}  spec={r["specification"]}  verses={vc}')
