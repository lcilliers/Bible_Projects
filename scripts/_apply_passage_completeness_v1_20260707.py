"""Passage completeness (reading-unit repair) — per book, reusable.

Implements wa-passage-completeness-rule-v1-20260707.md:
every verse that has an active verse-record but no passage_id is captured into a passage:
consecutive scope verses form a RUN; a run adjacent to exactly one existing passage is
MERGED into it (extend/prepend); a run between two passages, or isolated, becomes its OWN
new passage. Only `passage` + `verse.passage_id`/`is_passage_anchor` are written (ve_lexical /
verse-records track via verse.passage_id — normalized, no change).

Usage: python scripts/_apply_passage_completeness_v1_20260707.py --book N [--dry-run|--live]
"""
import sqlite3, argparse
from datetime import datetime, timezone

DB='database/bible_research.db'
SOURCE='readingunit-fix-2026'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--book',type=int,required=True)
    g=ap.add_mutually_exclusive_group(required=True); g.add_argument('--dry-run',action='store_true'); g.add_argument('--live',action='store_true')
    a=ap.parse_args()
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    abbr=c.execute('SELECT abbreviation FROM books WHERE id=?',(a.book,)).fetchone()['abbreviation']

    # scope verses (passage_id NULL + active verse-record)
    scope=[dict(r) for r in c.execute('''SELECT v.id,v.chapter,v.verse_num FROM verse v
        WHERE v.book_id=? AND v.passage_id IS NULL
          AND EXISTS(SELECT 1 FROM wa_verse_records w WHERE w.verse_id=v.id AND COALESCE(w.delete_flagged,0)=0)
        ORDER BY v.chapter,v.verse_num''',(a.book,))]
    vid={(r['chapter'],r['verse_num']):r['id'] for r in scope}
    sset=set(vid)
    def pid(ch,vn):
        r=c.execute('SELECT passage_id FROM verse WHERE book_id=? AND chapter=? AND verse_num=?',(a.book,ch,vn)).fetchone()
        return (r['passage_id'] if r else None)

    # group consecutive within-chapter runs
    runs=[]; cur=[]
    for ch,vn in sorted(sset):
        if cur and cur[-1][0]==ch and cur[-1][1]==vn-1: cur.append((ch,vn))
        else:
            if cur: runs.append(cur)
            cur=[(ch,vn)]
    if cur: runs.append(cur)

    plan=[]   # (kind, passage_id_or_None, run)
    for run in runs:
        ch=run[0][0]; first=run[0][1]; last=run[-1][1]
        pprev=pid(ch,first-1); pnext=pid(ch,last+1)
        if pprev and not pnext:   plan.append(('extend',pprev,run))
        elif pnext and not pprev: plan.append(('prepend',pnext,run))
        else:                     plan.append(('new',None,run))

    def ref(ch,f,l): return f'{abbr} {ch}:{f}' + (f'-{l}' if l>f else '')
    counts={'extend':0,'prepend':0,'new':0}
    for kind,pid_,run in plan:
        ch=run[0][0]; first=run[0][1]; last=run[-1][1]; n=len(run); counts[kind]+=1
        if a.dry_run:
            print(f'  {kind:8} run {ref(ch,first,last):14} ({n}v)' + (f' -> passage {pid_}' if pid_ else ' -> NEW passage'))
            continue
        run_vids=[vid[(ch,vn)] for _,vn in [(ch,x[1]) for x in run]]
        if kind=='extend':
            p=c.execute('SELECT * FROM passage WHERE id=?',(pid_,)).fetchone()
            c.execute('UPDATE passage SET end_chapter=?, end_verse=?, verse_count=verse_count+?, ref=?, last_changed_note=? WHERE id=?'
                      if 'last_changed_note' in p.keys() else
                      'UPDATE passage SET end_chapter=?, end_verse=?, verse_count=verse_count+?, ref=? WHERE id=?',
                      ((ch,last,n,ref(p['start_chapter'],p['start_verse'],last),f'{SOURCE} extend {now}',pid_)
                       if 'last_changed_note' in p.keys() else (ch,last,n,ref(p['start_chapter'],p['start_verse'],last),pid_)))
            for v in run_vids: c.execute('UPDATE verse SET passage_id=? WHERE id=?',(pid_,v))
        elif kind=='prepend':
            p=c.execute('SELECT * FROM passage WHERE id=?',(pid_,)).fetchone()
            old_anchor=p['anchor_verse_id']; new_anchor=run_vids[0]
            c.execute('UPDATE passage SET start_chapter=?, start_verse=?, anchor_verse_id=?, verse_count=verse_count+?, ref=? WHERE id=?',
                      (ch,first,new_anchor,n,ref(ch,first,p['end_verse']) if p['end_chapter']==ch else f"{abbr} {ch}:{first}-{p['end_chapter']}:{p['end_verse']}",pid_))
            if old_anchor: c.execute('UPDATE verse SET is_passage_anchor=0 WHERE id=?',(old_anchor,))
            c.execute('UPDATE verse SET is_passage_anchor=1 WHERE id=?',(new_anchor,))
            for v in run_vids: c.execute('UPDATE verse SET passage_id=? WHERE id=?',(pid_,v))
        else:  # new
            anchor=run_vids[0]
            c.execute('INSERT INTO passage (ref,anchor_verse_id,book_id,start_chapter,start_verse,end_chapter,end_verse,verse_count,source,created_at) VALUES (?,?,?,?,?,?,?,?,?,?)',
                      (ref(ch,first,last),anchor,a.book,ch,first,ch,last,n,SOURCE,now))
            newid=c.execute('SELECT last_insert_rowid()').fetchone()[0]
            c.execute('UPDATE verse SET is_passage_anchor=1 WHERE id=?',(anchor,))
            for v in run_vids: c.execute('UPDATE verse SET passage_id=? WHERE id=?',(newid,v))

    print(f"book {a.book} ({abbr}): scope verses={len(scope)}  runs={len(runs)}  "
          f"extend={counts['extend']} prepend={counts['prepend']} new={counts['new']}")
    if a.dry_run:
        print('  (dry-run, no writes)')
        return
    c.commit()
    left=c.execute('''SELECT COUNT(*) FROM verse v WHERE v.book_id=? AND v.passage_id IS NULL
        AND EXISTS(SELECT 1 FROM wa_verse_records w WHERE w.verse_id=v.id AND COALESCE(w.delete_flagged,0)=0)''',(a.book,)).fetchone()[0]
    print(f'  APPLIED. verse-record verses still passage-less (must be 0): {left}')

if __name__=='__main__':
    main()
