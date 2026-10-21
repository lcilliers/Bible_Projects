"""Verse-record -> verse / master-index link repair (per book, reusable).

Fixes verse-records left with NULL verse_id / verse_span_id by the gate-1 onboarding
(the record has a reference + strong but was never linked to the verse row / master-index span).

Deterministic only:
  - verse_id: set from the record's reference (unambiguous) wherever it resolves to a verse row.
  - verse_span_id: set ONLY when exactly ONE master-index span matches (verse_id + exact strong,
    else verse_id + base strong). Records where the term repeats in the verse (multiple spans) or
    have no span are LEFT and reported — no guessing which span.

Usage: python scripts/_apply_verse_record_link_repair_v1_20260707.py --book N [--dry-run|--live]
"""
import sqlite3, argparse
def base(s): return s[:-1] if (s and len(s)>1 and s[-1].isalpha() and s[0] in 'HG') else s
DB='database/bible_research.db'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--book',type=int,required=True)
    g=ap.add_mutually_exclusive_group(required=True); g.add_argument('--dry-run',action='store_true'); g.add_argument('--live',action='store_true')
    a=ap.parse_args()
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    rows=[dict(r) for r in c.execute('SELECT id,reference,term_id,verse_id,verse_span_id FROM wa_verse_records WHERE book_id=? AND COALESCE(delete_flagged,0)=0 AND (verse_id IS NULL OR verse_span_id IS NULL)',(a.book,))]
    set_vid=set_span=amb=nospan=novref=0
    for r in rows:
        v=c.execute('SELECT id FROM verse WHERE reference=?',(r['reference'],)).fetchone()
        if not v: novref+=1; continue
        vid=v['id']
        # verse_id (unambiguous)
        if r['verse_id'] is None:
            if a.live: c.execute('UPDATE wa_verse_records SET verse_id=? WHERE id=?',(vid,r['id']))
            set_vid+=1
        # verse_span_id (only if exactly one span)
        if r['verse_span_id'] is None:
            ex=[x['id'] for x in c.execute('SELECT id FROM verse_span_index WHERE verse_id=? AND primary_strong=? ORDER BY word_index',(vid,r['term_id']))]
            cand=ex
            if len(cand)!=1:
                bm=[x['id'] for x in c.execute('SELECT id FROM verse_span_index WHERE verse_id=? AND substr(primary_strong,1,5)=? ORDER BY word_index',(vid,base(r['term_id'])))]
                cand=bm
            if len(cand)==1:
                if a.live: c.execute('UPDATE wa_verse_records SET verse_span_id=? WHERE id=?',(cand[0],r['id']))
                set_span+=1
            elif len(cand)>1: amb+=1
            else: nospan+=1
    if a.live: c.commit()
    print(f"book {a.book}: records needing link={len(rows)}")
    print(f"  verse_id set (passage tracking): {set_vid}")
    print(f"  verse_span_id set (master-index link, 1-span clean): {set_span}")
    print(f"  LEFT: ambiguous (multi-span)={amb} | no span={nospan} | reference unresolved={novref}")
    if a.dry_run: print('  (dry-run, no writes)')

if __name__=='__main__':
    main()
