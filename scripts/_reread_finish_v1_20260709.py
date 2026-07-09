#!/usr/bin/env python
"""
_reread_finish_v1_20260709.py -- finish one re-read chapter: apply -> gate -> commit -> close -> stamp.

Usage:
  python scripts/_reread_finish_v1_20260709.py --chapter 21 --chars 23 \
      --msg "king thanksgiving; joy-cluster samach/gil/chadah, batach+chesed, aph wrath" \
      [--book-id 19] [--prov reread-psalms-2026] [--file <path>]

If gates fail (g10>0 or g6>0) it does NOT commit; it prints the offending verses so the
analyst can add discoveries / fix, then re-run. The reading JSON must already exist.
"""
import argparse, subprocess, sqlite3, os, sys

DB = os.path.join('database', 'bible_research.db')

def gates(c, book_id, ch):
    M=[101,102,104,105,106,107,108,112]
    vs=[r[0] for r in c.execute("SELECT DISTINCT v.id FROM verse v JOIN verse_span_index s ON s.verse_id=v.id WHERE v.book_id=? AND v.chapter=? AND (s.role='characteristic' OR s.char_candidate=1)",(book_id,ch))]
    g10=[]
    for sp in c.execute("SELECT s.id,v.verse_num vn FROM verse_span_index s JOIN verse v ON v.id=s.verse_id WHERE v.book_id=? AND v.chapter=? AND s.role='characteristic'",(book_id,ch)):
        have=set(r[0] for r in c.execute("SELECT DISTINCT ve_nr FROM ve_lexical WHERE verse_span_id=? AND delete_flagged=0",(sp[0],)))
        if not set(M)<=have: g10.append(sp[1])
    g6=[]
    for vid in vs:
        n=c.execute("SELECT COUNT(*) FROM ve_lexical x JOIN verse_span_index s ON s.id=x.verse_span_id WHERE s.verse_id=? AND x.ve_nr=114 AND x.delete_flagged=0",(vid,)).fetchone()[0]
        if n==0:
            g6.append(c.execute("SELECT verse_num FROM verse WHERE id=?",(vid,)).fetchone()[0])
    return g10,g6

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--chapter',type=int,required=True)
    ap.add_argument('--chars',type=int,required=True)
    ap.add_argument('--msg',required=True)
    ap.add_argument('--book-id',type=int,default=19)
    ap.add_argument('--prov',default='reread-psalms-2026')
    ap.add_argument('--file')
    ap.add_argument('--book',default='Psalms')
    a=ap.parse_args()
    ch=a.chapter
    f=a.file or f"verse-analysis/psalms/_read/psalm-{ch:03d}-reread-v1.json"
    if not os.path.exists(f):
        print("MISSING JSON:",f); sys.exit(2)
    # apply
    r=subprocess.run([sys.executable,"scripts/_apply_reread_lexical_v1_20260709.py",f"--in={f}","--live","--no-backup"],capture_output=True,text=True)
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[-300:])
    if r.returncode!=0:
        print("APPLY FAILED"); sys.exit(2)
    # gate
    c=sqlite3.connect(DB)
    g10,g6=gates(c,a.book_id,ch)
    if g10 or g6:
        print(f"GATE FAIL ch{ch}: g10_verses={g10} g6_verses={g6}  (fix discoveries, re-run finish)")
        sys.exit(1)
    # commit
    subprocess.run(["git","add","-A"],capture_output=True,text=True)
    cm=subprocess.run(["git","commit","-q","-m",f"session 20260709: Psalm {ch} COMPLETE ({a.chars} chars) - {a.msg}\n\nCo-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"],capture_output=True,text=True)
    sha=subprocess.run(["git","rev-parse","--short","HEAD"],capture_output=True,text=True).stdout.strip()
    # close worklist
    subprocess.run([sys.executable,"scripts/_reread_worklist_v1_20260709.py","--close","--book",a.book,"--chapter",str(ch),"--g10","0","--g6","0","--sha",sha],capture_output=True,text=True)
    print(f"STAMP: Ps{ch} done | {a.chars} chars | G10=0 G6=0 | {sha}")

if __name__=='__main__':
    main()
