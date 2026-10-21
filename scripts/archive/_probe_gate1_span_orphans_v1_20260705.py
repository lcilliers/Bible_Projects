#!/usr/bin/env python
"""
_probe_gate1_span_orphans_v1_20260705.py  — Gate-1 span-orphan audit (reusable, read-only).

THE METHOD RULE (feedback_term_coverage_cascade_is_index_not_census): the term registry is a
SEED, not a census. Before/after any span-depth reading of a book, scan the FULL word index
(verse_span_index) for inner-being-like content words that the curated term set (wa_verse_records)
did NOT pick up — the "span-orphans". This is Gate 1. It must run for every book.

For a book it prints, per un-registered content-strong, the gloss + frequency + a first verse,
sorted so the inner-being candidates surface. Nothing is written; this is the audit that feeds
the coding/reading revision.

Usage:
  python scripts/_probe_gate1_span_orphans_v1_20260705.py --book Genesis [--all] [--min-freq 1]
    (default: only gloss-keyword inner-being CANDIDATES; --all shows every un-registered content word)
"""
import argparse, os, sqlite3

# inner-being gloss keywords (broad; false positives filtered by human review)
KW = ('love hate fear joy rejoice glad mourn weep grief anger wrath fury pride humble trust redeem ransom '
 'deliver save life live die death dead soul heart mind spirit will sin guilt iniqu transgress wicked evil '
 'right just holy clean pure defile abomin shame honor bless curse vow oath desire covet despise forgive mercy '
 'compassion grace kind faith peace rest afflict oppress humili remember forget know wise folly fool glory serve '
 'rule free liberty avenge vengeance hope confid secur dread terror repent neighbor brother kin stranger poor '
 'needy widow orphan bribe deceit lie truth swear profane comfort jealous envy strive wrestle bitter long yearn '
 'delight loathe abhor willing strength courage weep tremble rejoic zeal lust proud faint humble mercy').split()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--book', required=True)
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--min-freq', type=int, default=1)
    ap.add_argument('--db', default=os.path.join('database','bible_research.db'))
    a=ap.parse_args()
    conn=sqlite3.connect(a.db); conn.row_factory=sqlite3.Row; c=conn.cursor()
    bid=c.execute("SELECT id FROM books WHERE name=?",(a.book,)).fetchone()
    if not bid: print("unknown book",a.book); return
    bid=bid['id']
    reg=set(r['ts'][:5] for r in c.execute("SELECT DISTINCT term_id ts FROM wa_verse_records WHERE book_id=? AND term_id LIKE 'H%' AND COALESCE(delete_flagged,0)=0",(bid,)))
    rows=c.execute("""SELECT vsi.primary_strong ps, COUNT(*) f, lx.gloss g, lx.transliteration tl,
             MIN(v.chapter*1000+v.verse_num) firstref
      FROM verse_span_index vsi JOIN verse v ON v.id=vsi.verse_id
      LEFT JOIN lexicon lx ON lx.strong=vsi.primary_strong
      WHERE v.book_id=? AND vsi.primary_strong LIKE 'H%' AND vsi.primary_strong NOT LIKE 'H9%'
      GROUP BY vsi.primary_strong""",(bid,)).fetchall()
    unreg=[r for r in rows if r['ps'][:5] not in reg and r['f']>=a.min_freq]
    def cand(g): g=(g or '').lower(); return any(k in g for k in KW)
    show=unreg if a.all else [r for r in unreg if cand(r['g'])]
    show.sort(key=lambda r:-r['f'])
    print(f"=== Gate-1 span-orphan audit: {a.book} ===")
    print(f"registered content-strongs: {len(reg)} | un-registered: {len(unreg)} | shown ({'ALL' if a.all else 'IB-candidates'}): {len(show)}")
    for r in show:
        fr=f"{r['firstref']//1000}:{r['firstref']%1000}"
        print(f"  {r['ps']} {(r['tl'] or '')[:14]:<15} x{r['f']:<3} {fr:<7} {r['g']}")
    conn.close()

if __name__=='__main__':
    main()
