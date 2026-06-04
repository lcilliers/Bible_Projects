"""_exploratory_rescue_physical_setaside_v1_20260604.py  (READ-ONLY)
Pull the anchor verse-contexts whose keywords include 'rescue physical', with cluster,
verse, meaning, keywords and set-aside status — for a set-aside-violation review.
"""
import sqlite3, os

DB = os.path.join('database', 'bible_research.db')
OUT = os.path.join('research', 'investigations', 'rescue-physical-setaside-20260604.md')
conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
cur = conn.cursor()

mt_cols = [c['name'] for c in cur.execute('PRAGMA table_info(mti_terms)')]
strong_col = 'strongs' if 'strongs' in mt_cols else ('strongs_number' if 'strongs_number' in mt_cols else 'cluster_code')

cn = {r['cluster_code']: (r['short_name'] or r['cluster_code'])
      for r in cur.execute('SELECT cluster_code, short_name FROM cluster')}

rows = cur.execute(f"""
 SELECT wr.reference ref, wr.testament t, b.name book, TRIM(mt.cluster_code) code,
        mt.{strong_col} strongs, vc.is_anchor anc, vc.is_relevant rel,
        vc.set_aside_reason sar, vc.group_id gid,
        wr.verse_text vtext, vc.analysis_note meaning, vc.keywords kw
 FROM verse_context vc
 JOIN wa_verse_records wr ON wr.id = vc.verse_record_id
 LEFT JOIN books b      ON b.id = wr.book_id
 LEFT JOIN mti_terms mt ON mt.id = vc.mti_term_id
 WHERE LOWER(vc.keywords) LIKE '%rescue physical%'
   AND COALESCE(vc.delete_flagged,0)=0 AND vc.is_anchor=1
 ORDER BY mt.cluster_code, b.book_order, wr.chapter, wr.verse_num""").fetchall()

L = ['# "rescue physical" anchors — set-aside review', '',
     '> Read-only, 2026-06-04. The **6 anchor** verse-contexts whose keywords include the phrase',
     '> "rescue physical" (the phrase appears on 27 verse-contexts in all; only these 6 are anchors).',
     '> Question to weigh: these read as *physical / temporal* rescue — should any be **set aside** as',
     '> not inner-being salvation, or does the inner-being cry (fear, faith, soul) keep them in?',
     '> **None is currently set aside.**', '',
     '| # | Ref | Cluster | Strong | anchor | set_aside |',
     '|---|---|---|---|---|---|']
for i, r in enumerate(rows, 1):
    L.append('| %d | %s | %s %s | %s | %s | %s |'
             % (i, r['ref'], r['code'], cn.get(r['code'], '?'), r['strongs'], r['anc'], r['sar']))
L.append('')
for i, r in enumerate(rows, 1):
    L.append('### %d. %s — %s (%s) · cluster %s %s'
             % (i, r['ref'], r['book'], r['t'], r['code'], cn.get(r['code'], '?')))
    L.append('')
    L.append('- *Verse:* %s' % (r['vtext'] or '').strip())
    L.append('- *Meaning:* %s' % (r['meaning'] or '').strip())
    L.append('- *Keywords:* %s' % r['kw'])
    L.append('- *Status:* anchor=%s · is_relevant=%s · set_aside_reason=%r · group_id=%s'
             % (r['anc'], r['rel'], r['sar'], r['gid']))
    L.append('')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(L) + '\n')
print('strong_col=%s rows=%d -> %s' % (strong_col, len(rows), OUT))
