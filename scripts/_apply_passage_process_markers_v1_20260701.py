"""
_apply_passage_process_markers_v1_20260701.py

Batch processor with the two startup validators + a PROCESS MARKER (researcher, 2026-07-01).

Adds two VERSE-LEVEL fields (verse-first model — passage/anchor are verse-level, so they live on
`verse`, the master index; note the researcher said "verse_record" — flag if wa_verse_records is
preferred instead):
   verse.process_marker    TEXT    -- outcome of processing this verse
   verse.is_passage_anchor  INTEGER -- 1 = first verse of its passage (ve-records attach here); 0 = member; NULL = unprocessed

Per verse in the batch (skip if already assigned to a processed passage):
   VALIDATOR A  passage membership forward+backward (confirmed = isolable=no; candidate = continuation opener).
       -> ANY candidate (unconfirmed) link  => marker 'A-REVIEW:<n>cand' on the start verse; MOVE ON.
       -> a member verse missing from the index => marker 'A-FAIL:index'; MOVE ON.
   VALIDATOR B  all member spans in verse_morphology.
       -> any missing => marker 'B-BLOCKED:<refs>'; MOVE ON.
   PASS both => anchor = first verse: is_passage_anchor=1 + marker 'ANCHOR:<full passage ref>';
       other members: is_passage_anchor=0 + marker 'MEMBER:<anchor ref>'.

Safe: backs up; dry-run default; verifies. Idempotent (re-run recomputes).
Usage: python scripts/_apply_passage_process_markers_v1_20260701.py --book 2 --chapter 1 [--live]
"""
import sqlite3, os, sys, re, argparse, shutil
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db')
CONT_OPENERS=('so ','and ','but ','for ','therefore','then ','thus ')
def canon(s):
    m=re.match(r'^([HG])(\d+)',s or ''); return m.group(1)+m.group(2).zfill(4) if m else s
def opener_continues(text):
    m=re.match(r'^\s*\S+\s+\d+:\d+\s+(.*)$',text or ''); op=(m.group(1) if m else (text or '')).lower()
    return any(op.startswith(c) for c in CONT_OPENERS)

def reads_back(cur,vid):
    return cur.execute("""SELECT COUNT(*) FROM ve_lexical vl JOIN verse_context vc ON vl.verse_context_id=vc.id
        JOIN wa_verse_records w ON vc.verse_record_id=w.id
        WHERE w.verse_id=? AND vl.ve_label='isolable' AND vl.value='no' AND vl.delete_flagged=0""",(vid,)).fetchone()[0]>0

def vrow(cur,b,ch,vn):
    return cur.execute("SELECT id,reference,verse_text,verse_num FROM verse WHERE book_id=? AND chapter=? AND verse_num=?",(b,ch,vn)).fetchone()

def validate_A(cur,v,b,ch):
    """returns (members[ordered], has_candidate, index_fail)."""
    members=[dict(v)]; has_cand=False
    cur_v=v
    while True:
        prev=vrow(cur,b,ch,cur_v['verse_num']-1)
        if not prev: break
        if reads_back(cur,cur_v['id']): members.insert(0,dict(prev)); cur_v=prev; continue
        if opener_continues(cur_v['verse_text']): members.insert(0,dict(prev)); has_cand=True; cur_v=prev; continue
        break
    cur_v=v
    while True:
        nxt=vrow(cur,b,ch,cur_v['verse_num']+1)
        if not nxt: break
        if reads_back(cur,nxt['id']): members.append(dict(nxt)); cur_v=nxt; continue
        if opener_continues(nxt['verse_text']): members.append(dict(nxt)); has_cand=True; cur_v=nxt; continue
        break
    seen=set(); out=[]
    for m in members:
        if m['id'] not in seen: seen.add(m['id']); out.append(m)
    return out, has_cand

def validate_B(cur,members):
    missing=[m['reference'] for m in members if cur.execute("SELECT COUNT(*) FROM verse_morphology WHERE verse_id=?",(m['id'],)).fetchone()[0]==0]
    return missing

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--book',type=int,required=True); ap.add_argument('--chapter',type=int,required=True)
    ap.add_argument('--live',action='store_true'); a=ap.parse_args()
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    verses=cur.execute("SELECT id,reference,verse_text,verse_num,book_id,chapter FROM verse WHERE book_id=? AND chapter=? ORDER BY verse_num",(a.book,a.chapter)).fetchall()
    if not verses: print('no verses'); return

    plan={}  # verse_id -> (is_anchor, marker)
    done=set()
    for v in verses:
        if v['id'] in done: continue
        members,has_cand=validate_A(cur,v,a.book,a.chapter)
        if has_cand:
            plan[v['id']]=(None,'A-REVIEW:%dv-candidate-boundary'%len(members)); done.add(v['id']); continue
        missing=validate_B(cur,members)
        if missing:
            plan[v['id']]=(None,'B-BLOCKED:'+','.join(missing)); done.add(v['id']); continue
        anchor=members[0]; pref='%s-%d'%(anchor['reference'],members[-1]['verse_num'])
        plan[anchor['id']]=(1,'ANCHOR:'+pref)
        for m in members[1:]: plan[m['id']]=(0,'MEMBER:'+anchor['reference'])
        for m in members: done.add(m['id'])

    # report
    from collections import Counter
    tally=Counter(mk.split(':')[0] for _,mk in plan.values())
    print('batch book %d ch %d: %d verses'%(a.book,a.chapter,len(verses)))
    for k,n in tally.most_common(): print('  %-10s %d'%(k,n))
    print('sample:')
    for v in verses[:12]:
        anc,mk=plan.get(v['id'],(None,'(unset)')); print('  %-9s anchor=%-4s %s'%(v['reference'],anc,mk))

    if not a.live: print('\nDRY-RUN. Re-run with --live to write markers.'); return
    os.makedirs('backups',exist_ok=True)
    shutil.copy2(DB,os.path.join('backups','bible_research.pre-procmarker.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    cols=[r[1] for r in cur.execute("PRAGMA table_info(verse)").fetchall()]
    if 'process_marker' not in cols: cur.execute("ALTER TABLE verse ADD COLUMN process_marker TEXT")
    if 'is_passage_anchor' not in cols: cur.execute("ALTER TABLE verse ADD COLUMN is_passage_anchor INTEGER")
    for vid,(anc,mk) in plan.items():
        cur.execute("UPDATE verse SET process_marker=?, is_passage_anchor=? WHERE id=?",(mk,anc,vid))
    conn.commit()
    print('\nwrote markers for %d verses; anchors=%d'%(len(plan),sum(1 for a2,_ in plan.values() if a2==1)))

if __name__=='__main__': main()
