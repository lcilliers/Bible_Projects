import sqlite3
conn = sqlite3.connect('../data/bible_research.db')
conn.row_factory = sqlite3.Row

# term_fetch_log: span_conflict rows and overall shape
r = conn.execute('SELECT COUNT(*) FROM term_fetch_log').fetchone()[0]
r2 = conn.execute('SELECT COUNT(*) FROM term_fetch_log WHERE span_conflict = 1').fetchone()[0]
r3 = conn.execute('SELECT COUNT(DISTINCT strongs_input) FROM term_fetch_log WHERE span_conflict = 1').fetchone()[0]
print('term_fetch_log: total=%d  span_conflict=1: %d rows / %d distinct strongs' % (r, r2, r3))

# distinct runs
runs = conn.execute('SELECT COUNT(DISTINCT run_id) FROM term_fetch_log').fetchone()[0]
print('distinct run_ids: %d' % runs)

# wa_verse_records: span_strong_match distribution
print('\nwa_verse_records span_strong_match:')
for row in conn.execute(
    'SELECT span_strong_match, COUNT(*) AS cnt FROM wa_verse_records GROUP BY span_strong_match ORDER BY span_strong_match'
).fetchall():
    print('  span_strong_match=%-5s  %d' % (str(row['span_strong_match']), row['cnt']))

# count terms with at least 1 filtered verse (span_strong_match=0)
filtered_terms = conn.execute('''
    SELECT COUNT(DISTINCT term_inv_id) FROM wa_verse_records WHERE span_strong_match = 0
''').fetchone()[0]
print('\nDistinct term_inv_ids with span_strong_match=0: %d' % filtered_terms)

# Excluded words with fi rows (need NO_FURTHER_ACTION)
ex_with_fi = conn.execute('''
    SELECT COUNT(DISTINCT fi.id) FROM wa_file_index fi
    JOIN word_registry wr ON wr.id = fi.word_registry_fk
    WHERE wr.phase1_status = 'Excluded'
''').fetchone()[0]
print('\nExcluded words with wa_file_index rows (get NO_FURTHER_ACTION): %d' % ex_with_fi)

# Complete words file count
complete_files = conn.execute('''
    SELECT COUNT(DISTINCT fi.id) FROM wa_file_index fi
    JOIN word_registry wr ON wr.id = fi.word_registry_fk
    WHERE wr.phase1_status = 'Complete'
''').fetchone()[0]
print('Complete word files (get flag recompute): %d' % complete_files)



