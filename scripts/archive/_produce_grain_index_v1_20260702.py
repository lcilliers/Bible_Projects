"""
_produce_grain_index_v1_20260702.py  (READ-ONLY)

The GRAIN INDEX reader — the sense-level access the term-driven method rolls up on. A "term" for the
study is a GRAIN (a per-occurrence STEP sub-gloss), NOT the bare lemma. The grain index is
`wa_verse_term_links` (keyed to wa_verse_records; each row = a term-in-verse + its step_subgloss = grain).

Two modes:
  --strong H5647   list the lemma's GRAINS (step_subgloss_code + label) with verse counts.
  --grain  H5647G  read ALL verses for one grain (the rollup / related-verse set for that sense).
  --at "Exo 1:13" --strong H5647   resolve a specific occurrence to its grain, then read that grain's verses.

Use: replaces lemma-level rollup. perek H6531 = 1 grain (6v); abad H5647 splits into
serve/minister/labour/burden — the enslave thread is the 'to serve' grain (H5647G, ~88v), not 261.
"""
import sqlite3, os, argparse
DB=os.path.join('database','bible_research.db')

def grains(cur, strong):
    return cur.execute("""SELECT l.step_subgloss_code code, l.step_subgloss_label label, COUNT(DISTINCT w.reference) verses
      FROM wa_verse_term_links l JOIN wa_verse_records w ON l.verse_id=w.id
      WHERE w.term_id LIKE ?||'%' AND COALESCE(w.delete_flagged,0)=0
      GROUP BY l.step_subgloss_code ORDER BY verses DESC""",(strong,)).fetchall()

def grain_verses(cur, code):
    return cur.execute("""SELECT DISTINCT w.reference, w.book_id, w.chapter, w.verse_num, l.target_word
      FROM wa_verse_term_links l JOIN wa_verse_records w ON l.verse_id=w.id
      WHERE l.step_subgloss_code=? AND COALESCE(w.delete_flagged,0)=0
      ORDER BY w.book_id, w.chapter, w.verse_num""",(code,)).fetchall()

def grain_at(cur, ref, strong):
    r=cur.execute("""SELECT l.step_subgloss_code code, l.step_subgloss_label label
      FROM wa_verse_term_links l JOIN wa_verse_records w ON l.verse_id=w.id
      WHERE w.reference=? AND w.term_id LIKE ?||'%' LIMIT 1""",(ref,strong)).fetchone()
    return r

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--strong'); ap.add_argument('--grain'); ap.add_argument('--at')
    a=ap.parse_args()
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    if a.at and a.strong:
        g=grain_at(cur, a.at, a.strong)
        if not g: print('no grain at %s for %s'%(a.at,a.strong)); return
        print("%s %s -> grain %s '%s'"%(a.at, a.strong, g['code'], g['label'])); a.grain=g['code']
    if a.grain:
        vs=grain_verses(cur, a.grain)
        print("grain %s : %d verses"%(a.grain, len(vs)))
        for r in vs: print("   %-12s %s"%(r['reference'], r['target_word'] or ''))
    elif a.strong:
        gs=grains(cur, a.strong)
        print("lemma %s : %d grain(s)"%(a.strong, len(gs)))
        for r in gs: print("   %-10s '%s' : %d verses"%(r['code'], r['label'], r['verses']))
    else:
        print("give --strong (list grains) or --grain (read verses) or --at+--strong")

if __name__=='__main__': main()
