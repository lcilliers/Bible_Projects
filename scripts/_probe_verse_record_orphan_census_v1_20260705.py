#!/usr/bin/env python
"""_probe_verse_record_orphan_census_v1_20260705.py — per-book IB span-orphan census (read-only).

For every book: how many inner-being-candidate content-strongs appear in the FULL word index
(verse_span_index) but are NOT registered in the verse-record (wa_verse_records) — i.e. the IB
spans the foundational rule required be ADDED to the verse-record but (as created_at shows) never
were. Reports distinct orphan TERMS, orphan span TOKENS, and distinct VERSES touched, per book.
Candidate filter = inner-being gloss keywords (heuristic; needs per-book human review, exactly as
Gate-1 works). Prints a table + writes nothing.
"""
import sqlite3, os
KW=('love hate fear joy rejoice glad mourn weep grief anger wrath fury pride humble trust redeem ransom '
 'deliver save life live die death dead soul heart mind spirit will sin guilt iniqu transgress wicked evil '
 'right just holy clean pure defile abomin shame honor bless curse vow oath desire covet despise forgive mercy '
 'compassion grace kind faith peace rest afflict oppress humili remember forget know wise folly fool glory serve '
 'rule free liberty avenge vengeance hope confid secur dread terror repent neighbor brother kin stranger poor '
 'needy widow orphan bribe deceit lie truth swear profane comfort jealous envy strive wrestle bitter long yearn '
 'delight loathe abhor willing strength courage tremble zeal lust proud faint').split()
def cand(g): g=(g or '').lower(); return any(k in g for k in KW)
c=sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory=sqlite3.Row; cur=c.cursor()
print(f"{'Book':<16}{'reg':>5}{'unreg':>7}{'IBorph':>7}{'orphTok':>9}{'orphVs':>8}")
tt=ttok=tvs=0
for b in cur.execute('SELECT id,name FROM books ORDER BY id').fetchall():
    reg=set(r['ts'][:5] for r in cur.execute("SELECT DISTINCT term_id ts FROM wa_verse_records WHERE book_id=? AND term_id LIKE 'H%' AND COALESCE(delete_flagged,0)=0",(b['id'],)))
    rows=cur.execute("""SELECT vsi.primary_strong ps, COUNT(*) f, lx.gloss g, COUNT(DISTINCT vsi.verse_id) vs
      FROM verse_span_index vsi JOIN verse v ON v.id=vsi.verse_id
      LEFT JOIN lexicon lx ON lx.strong=vsi.primary_strong
      WHERE v.book_id=? AND vsi.primary_strong LIKE 'H%' AND vsi.primary_strong NOT LIKE 'H9%'
      GROUP BY vsi.primary_strong""",(b['id'],)).fetchall()
    if not rows: continue
    unreg=[r for r in rows if r['ps'][:5] not in reg]
    ib=[r for r in unreg if cand(r['g'])]
    orphTok=sum(r['f'] for r in ib); orphVs=sum(r['vs'] for r in ib)
    tt+=len(ib); ttok+=orphTok; tvs+=orphVs
    print(f"{b['name']:<16}{len(reg):>5}{len(unreg):>7}{len(ib):>7}{orphTok:>9}{orphVs:>8}",flush=True)
print(f"{'TOTAL':<16}{'':>5}{'':>7}{tt:>7}{ttok:>9}{tvs:>8}")
