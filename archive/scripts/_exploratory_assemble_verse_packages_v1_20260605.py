"""_exploratory_assemble_verse_packages_v1_20260605.py  (READ-ONLY)
Assemble the Pass-A input package for chosen verses and measure assembly cost
(wall-clock ms + DB query count), incl. the clarification corpus lookup.
"""
import sqlite3, time
c = sqlite3.connect('database/bible_research.db'); c.row_factory = sqlite3.Row; cur = c.cursor()
named = {r['cluster_code'] for r in cur.execute("SELECT cluster_code FROM cluster WHERE bucket='NAMED'")}
cname = {r['cluster_code']: (r['short_name'] or r['cluster_code']) for r in cur.execute('SELECT cluster_code,short_name FROM cluster')}

REFS = ['Deu 1:19', 'Exo 1:17', 'Exo 3:6', 'Lev 19:3']

def bucket(cc):
    if cc == 'M01': return 'TARGET(M01)'
    if cc == 'T2': return 'T2'
    if cc == 'FLAG': return 'FLAG'
    return 'T1:' + cc + ' ' + cname.get(cc, '')

for ref in REFS:
    q = {'n': 0}
    def run(sql, args=()):
        q['n'] += 1
        return cur.execute(sql, args).fetchall()
    t0 = time.perf_counter()
    # 1) all spans on the verse (the verse text comes with them)
    rows = run('''SELECT wr.id, wr.verse_text, wr.target_word, wr.term_id, wr.mti_term_id,
                         TRIM(mt.cluster_code) cc, mt.gloss, mt.language, mt.strongs_number
                  FROM wa_verse_records wr LEFT JOIN mti_terms mt ON mt.id=wr.mti_term_id
                  WHERE wr.reference=? AND COALESCE(wr.delete_flagged,0)=0
                  ORDER BY mt.cluster_code''', (ref,))
    # 2) for the M01 target term: corpus size (other occurrences) for possible clarification
    m01span = next((r for r in rows if r['cc'] == 'M01'), None)
    corpus_n = 0
    if m01span and m01span['term_id']:
        corpus_n = run('SELECT COUNT(*) n FROM wa_verse_records WHERE term_id=? AND COALESCE(delete_flagged,0)=0',
                       (m01span['term_id'],))[0]['n']
    ms = (time.perf_counter() - t0) * 1000

    vtext = rows[0]['verse_text'] if rows else '(none)'
    print('=' * 78)
    print(f'VERSE: {ref}')
    print(f'  text: {vtext}')
    print(f'  spans ({len(rows)}):')
    for r in rows:
        print(f"    [{bucket(r['cc']):16s}] span='{r['target_word']}' {r['term_id']} gloss='{(r['gloss'] or '')[:40]}' ({r['language'] or ''})")
    if m01span:
        print(f"  M01 target term {m01span['term_id']} gloss='{m01span['gloss']}' — corpus: {corpus_n} occurrences (for clarification)")
    print('  >> assembly: %.1f ms, %d DB queries' % (ms, q['n']))
    print()
