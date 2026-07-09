"""_exploratory_verse_cross_cluster_usage_v1_20260605.py  (READ-ONLY)
Answer: how do we know if a verse is used in other parts of the study?
A verse = (book_id, chapter, verse_num). Its spans = wa_verse_records rows for that key,
each with a term -> cluster_code. The verse is 'used' in every cluster its spans touch.
Demonstrated for M01.
"""
import sqlite3, os
c = sqlite3.connect('database/bible_research.db'); c.row_factory = sqlite3.Row; cur = c.cursor()

TARGET = 'M01'

# M01's analytic verses (is_relevant=1), keyed canonically
m01_keys = cur.execute("""
  SELECT DISTINCT wr.book_id, wr.chapter, wr.verse_num
  FROM verse_context vc
  JOIN wa_verse_records wr ON wr.id = vc.verse_record_id
  JOIN mti_terms mt ON mt.id = vc.mti_term_id
  WHERE mt.cluster_code = ? AND vc.is_relevant = 1 AND COALESCE(vc.delete_flagged,0)=0
""", (TARGET,)).fetchall()
m01_set = {(r['book_id'], r['chapter'], r['verse_num']) for r in m01_keys}

# For every span anywhere, map verse-key -> set of clusters touching it
rows = cur.execute("""
  SELECT wr.book_id, wr.chapter, wr.verse_num, TRIM(mt.cluster_code) cc
  FROM wa_verse_records wr
  JOIN mti_terms mt ON mt.id = wr.mti_term_id
  WHERE COALESCE(wr.delete_flagged,0)=0 AND COALESCE(TRIM(mt.cluster_code),'')<>''
""").fetchall()
verse_clusters = {}
for r in rows:
    k = (r['book_id'], r['chapter'], r['verse_num'])
    verse_clusters.setdefault(k, set()).add(r['cc'])

# How many M01 verses also appear in other clusters?
shared = 0
other_counter = {}
for k in m01_set:
    cls = verse_clusters.get(k, set())
    others = cls - {TARGET}
    if others:
        shared += 1
        for o in others:
            other_counter[o] = other_counter.get(o, 0) + 1

print(f"M01 analytic verses (distinct): {len(m01_set)}")
print(f"  ...also carrying a span in >=1 OTHER cluster: {shared} ({100*shared/max(len(m01_set),1):.0f}%)")
print()
print("Top other clusters co-occurring on M01 verses:")
names = {r['cluster_code']: (r['short_name'] or r['cluster_code']) for r in cur.execute('SELECT cluster_code,short_name FROM cluster')}
for o, n in sorted(other_counter.items(), key=lambda x:-x[1])[:12]:
    print(f"  {o:5s} {names.get(o,'?'):16s} {n}")

# Worked example: an M01 verse with the most cross-cluster spans
best = None
for k in m01_set:
    cls = verse_clusters.get(k, set())
    if best is None or len(cls) > len(verse_clusters.get(best, set())):
        best = k
bk, ch, vn = best
print()
print(f"Worked example — book_id={bk} {ch}:{vn} touches clusters: {sorted(verse_clusters.get(best,set()))}")
ex = cur.execute("""
  SELECT wr.reference, wr.target_word span, wr.term_id, TRIM(mt.cluster_code) cc
  FROM wa_verse_records wr JOIN mti_terms mt ON mt.id=wr.mti_term_id
  WHERE wr.book_id=? AND wr.chapter=? AND wr.verse_num=? AND COALESCE(wr.delete_flagged,0)=0
  ORDER BY mt.cluster_code
""", (bk, ch, vn)).fetchall()
for e in ex:
    print(f"   span '{e['span']}' ({e['term_id']}) -> {e['cc']} {names.get(e['cc'],'')}")
