import sqlite3
conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row
print('=== word_registry nos 201-211 ===')
rows = conn.execute('SELECT no, word, phase1_status, phase1_term_count, phase1_verse_count FROM word_registry WHERE no >= 201 ORDER BY no').fetchall()
for r in rows:
    print(f"  [{r['no']:3}] {r['word']:<25} {r['phase1_status']:<12} terms={r['phase1_term_count']} verses={r['phase1_verse_count']}")
print()
print('=== Integrity check ===')
ic = conn.execute('PRAGMA integrity_check').fetchone()[0]
print('Result:', ic)
