"""
_apply_rebuild_passages_consecutive_v2_20260701.py

Rebuild the passage layer on the SIMPLE, MECHANICAL definition (researcher, 2026-07-01):
  a passage = a maximal run of CONSECUTIVE verses (sort by book, chapter, verse_num; run length >= 2).
No isolable / openers / semantic detection. Runs break at chapter boundaries. Over the master
`verse` index (all DB verses — a run may include context verses without terms; that is fine, since
each term is evaluated by itself).

Supersedes the isolable-based passage build. Rebuilds:
  passage(id, ref, anchor_verse_id, book_id, start_chapter, start_verse, end_chapter, end_verse,
          verse_count, source='consecutive', review_flag, notes, created_at)
  verse.passage_id        -> passage.id   (members; NULL for singletons)
  verse.is_passage_anchor  -> 1 first verse (anchor, ve-records attach here), 0 member, NULL singleton

Safe: backs up; dry-run default; verifies. Idempotent (clears + rebuilds).
Usage: python scripts/_apply_rebuild_passages_consecutive_v2_20260701.py [--live]
"""
import sqlite3, os, sys, shutil, collections
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def main():
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    vs=cur.execute("SELECT id,reference,book_id,chapter,verse_num FROM verse ORDER BY book_id,chapter,verse_num").fetchall()
    # book label from reference
    bookname={}
    for r in vs: bookname.setdefault(r['book_id'], r['reference'].rsplit(' ',1)[0])
    # consecutive runs within (book,chapter)
    runs=[]; cur_run=[]
    for r in vs:
        if cur_run and r['book_id']==cur_run[-1]['book_id'] and r['chapter']==cur_run[-1]['chapter'] and r['verse_num']==cur_run[-1]['verse_num']+1:
            cur_run.append(r)
        else:
            if len(cur_run)>=2: runs.append(cur_run)
            cur_run=[r]
    if len(cur_run)>=2: runs.append(cur_run)

    sizes=[len(x) for x in runs]
    print('consecutive-run passages: %d ; verses in passages: %d ; max run %d ; mean %.1f'
          % (len(runs), sum(sizes), max(sizes), sum(sizes)/len(sizes)))
    if not LIVE:
        print('sample:')
        for run in runs[:6]:
            print('   %s %d:%d-%d  (%d verses, anchor %s)'%(bookname[run[0]['book_id']],run[0]['chapter'],run[0]['verse_num'],run[-1]['verse_num'],len(run),run[0]['reference']))
        # show the Exo 1:13 passage
        for run in runs:
            if any(r['reference']=='Exo 1:13' for r in run):
                print('   Exo 1:13 is in passage: %s (%s..%s)'%(' '.join(r['reference'].split(' ')[-1] for r in run), run[0]['reference'], run[-1]['reference'])); break
        print('\nDRY-RUN. Re-run with --live.'); return

    shutil.copy2(DB, os.path.join('backups','bible_research.pre-passages-v2.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    # reset
    cols=[r[1] for r in cur.execute("PRAGMA table_info(verse)").fetchall()]
    if 'is_passage_anchor' not in cols: cur.execute("ALTER TABLE verse ADD COLUMN is_passage_anchor INTEGER")
    cur.execute("UPDATE verse SET passage_id=NULL, is_passage_anchor=NULL")
    cur.execute("DELETE FROM passage")
    cur.execute("""CREATE TABLE IF NOT EXISTS passage (id INTEGER PRIMARY KEY, ref TEXT, anchor_verse_id INTEGER,
      book_id INTEGER, start_chapter INTEGER, start_verse INTEGER, end_chapter INTEGER, end_verse INTEGER,
      verse_count INTEGER, source TEXT, review_flag TEXT, notes TEXT, created_at TEXT)""")
    npass=0
    for run in runs:
        a=run[0]; z=run[-1]
        ref='%s %d:%d-%d'%(bookname[a['book_id']],a['chapter'],a['verse_num'],z['verse_num'])
        cur.execute("""INSERT INTO passage (ref,anchor_verse_id,book_id,start_chapter,start_verse,end_chapter,end_verse,verse_count,source,created_at)
           VALUES (?,?,?,?,?,?,?,?,?,?)""",(ref,a['id'],a['book_id'],a['chapter'],a['verse_num'],z['chapter'],z['verse_num'],len(run),'consecutive',NOW))
        pid=cur.lastrowid; npass+=1
        for i,r in enumerate(run):
            cur.execute("UPDATE verse SET passage_id=?, is_passage_anchor=? WHERE id=?",(pid, 1 if i==0 else 0, r['id']))
    conn.commit()
    print('rebuilt: %d passages ; verses linked %d ; anchors %d'
          % (npass, cur.execute("SELECT COUNT(*) FROM verse WHERE passage_id IS NOT NULL").fetchone()[0],
             cur.execute("SELECT COUNT(*) FROM verse WHERE is_passage_anchor=1").fetchone()[0]))

if __name__=='__main__': main()
