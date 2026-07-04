"""Read-only: pull the raw material for one narrative passage (segment_unit) so the
reading can be written OFF the verses. Prints, per verse in the unit: the verse text,
and each non-T2 span (target word, translit, gloss). Nothing written.

Usage: python scripts/_probe_passage_material_v1_20260704.py --unit-code=JAC-01-birth-oracle
"""
import sqlite3, os, sys
DB=os.path.join('database','bible_research.db')
def arg(n,d=None):
    for a in sys.argv[1:]:
        if a.startswith('--%s='%n): return a.split('=',1)[1]
    return d
UNIT=arg('unit-code')
conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
su=cur.execute("SELECT id, book, chapter, verse_ref_summary, gist FROM segment_unit WHERE unit_code=? AND COALESCE(delete_flagged,0)=0 ORDER BY id DESC LIMIT 1",(UNIT,)).fetchone()
if not su: print("no unit",UNIT); sys.exit()
print("=== %s | %s ch%s | refs %s ===" % (UNIT, su['book'], su['chapter'], su['verse_ref_summary']))
verses=cur.execute("""SELECT v.id, v.chapter ch, v.verse_num vn, v.verse_text txt
  FROM segment_unit_verse suv JOIN verse v ON v.id=suv.verse_id
  WHERE suv.unit_id=? ORDER BY v.chapter, v.verse_num""",(su['id'],)).fetchall()
# spans per verse_id
def spans(vid):
    return cur.execute("""SELECT w.target_word tw, w.transliteration tr, mt.gloss gloss, mt.cluster_code cc
      FROM wa_verse_records w JOIN mti_terms mt ON w.mti_term_id=mt.id
      WHERE w.verse_id=? AND COALESCE(w.delete_flagged,0)=0
        AND (mt.cluster_code IS NULL OR mt.cluster_code!='T2')
      ORDER BY w.id""",(vid,)).fetchall()
for v in verses:
    sp=spans(v['id'])
    print("\n%d:%d  %s" % (v['ch'], v['vn'], (v['txt'] or '').strip()))
    for s in sp:
        print("     [%s] %-16s %-14s | %s" % ((s['cc'] or '-'), (s['tw'] or '')[:16], (s['tr'] or '')[:14], s['gloss']))
