"""
Reverse out UNGROUNDED read-API overlay values per the verse-bounded rule
(researcher 2026-06-26): a value with no basis in THE VERSE is an error.

Targets (mechanically-confirmed ungrounded only; valence handled separately):
  A. object-type='God' with NO divine name in the verse          (imported, like divine-involvement)
  B. object-type on a unit that has NO 'object' field             (type with no referent)
  C. cause (cause_read_api) sharing NO content word with the verse (cause inferred, not stated)
  D. location (location_read_api) whose seat word is not in verse  (tiny)

Soft-delete (reversible). --live backs up DB + snapshots removed rows to ve_lexical_overlay_reverse_20260626.
  --dry-run : counts + samples, no write
"""
import sqlite3, os, re, argparse, shutil
from collections import Counter

DB=os.path.join('database','bible_research.db')
BACKUP=os.path.join('backups','bible_research_pre-overlay-reverse_20260626.db')
SNAP='ve_lexical_overlay_reverse_20260626'
DIV={'H3068','H3069','H0430','H0410','H0433','H0136','H3050','H5945','H7706','H0113','G2316','G2962','G3962','G5547','G2424','G0040'}
# seat lemmas by location value (canonical, suffix-stripped base)
SEAT={'heart':{'H3820','H3824','H3826','H3825','H3821','G2588'},'soul':{'H5315','G5590'},
      'flesh':{'H1320','G4561'},'spirit':{'H7307','G4151'},'mind':{'G3563','G1271','G3540'},
      'conscience':{'G4893'},'inward-parts':{'H7130','H3629','H4578','H0990'}}
STOP=set('the a an of to in and or for with by from on at is are was were be been have has had he she it they them his her their your you i we our us that this these those which who whom whose as so but not no nor than then thus into out up down over under off about against because shall will would may might can could do does did then there here when where what why how all any some'.lower().split())

def canon(s):
    m=re.match(r'^([HG])(\d+)([A-Z]?)$',(s or '').strip().upper()); return f'{m.group(1)}{int(m.group(2)):04d}' if m else None
def base(s):
    cs=canon(s); return re.sub(r'[A-Z]$','',cs) if cs else None
def words(t): return set(w for w in re.findall(r'[a-z]+',(t or '').lower()) if w not in STOP and len(w)>2)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--live',action='store_true'); ap.add_argument('--dry-run',action='store_true')
    a=ap.parse_args(); live=a.live and not a.dry_run
    if live: print('backing up DB ->',BACKUP); shutil.copy2(DB,BACKUP)
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    div_verses=set(); verse_bases={}
    vb=verse_bases
    for r in c.execute('SELECT verse_id, strongs FROM verse_morphology WHERE strongs IS NOT NULL'):
        s=vb.setdefault(r['verse_id'],set())
        for tok in (r['strongs'] or '').split():
            cb=base(tok)
            if cb: s.add(cb)
            if canon(tok) in DIV: div_verses.add(r['verse_id'])
    obj_units=set(x[0] for x in c.execute("SELECT DISTINCT verse_context_id FROM ve_lexical WHERE ve_label='object' AND COALESCE(delete_flagged,0)=0"))

    kill=[]  # (id, reason)
    # A + B: object-type
    for r in c.execute('''SELECT vl.id, vl.verse_context_id u, vl.value val, vr.verse_id vid
        FROM ve_lexical vl JOIN verse_context vc ON vc.id=vl.verse_context_id JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
        WHERE vl.ve_label="object-type" AND COALESCE(vl.delete_flagged,0)=0 AND vr.verse_id IS NOT NULL''').fetchall():
        if r['val']=='God' and r['vid'] not in div_verses: kill.append((r['id'],'A:object-type=God no divine name'))
        elif r['u'] not in obj_units: kill.append((r['id'],'B:object-type with no object'))
    # C: cause read_api no overlap
    for r in c.execute('''SELECT vl.id, vl.value val, vr.verse_text txt FROM ve_lexical vl
        JOIN verse_context vc ON vc.id=vl.verse_context_id JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
        WHERE vl.ve_label="cause" AND vl.source_provenance="cause_read_api" AND COALESCE(vl.delete_flagged,0)=0''').fetchall():
        cw=words(r['val'])
        if cw and not (cw & words(r['txt'])): kill.append((r['id'],'C:cause not in verse'))
    # D: location read_api seat not in verse
    for r in c.execute('''SELECT vl.id, vl.value val, vr.verse_id vid FROM ve_lexical vl
        JOIN verse_context vc ON vc.id=vl.verse_context_id JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
        WHERE vl.ve_label="location" AND vl.source_provenance="location_read_api" AND COALESCE(vl.delete_flagged,0)=0 AND vr.verse_id IS NOT NULL''').fetchall():
        seats=SEAT.get(r['val'],set())
        if seats and not (seats & vb.get(r['vid'],set())): kill.append((r['id'],'D:location seat not in verse'))

    print(f'TOTAL rows to reverse: {len(kill)}')
    print('  by reason:', dict(Counter(reason.split(":")[0]+":"+reason.split(":",1)[1][:30] for _,reason in kill).most_common()))
    if kill:
        ids=[k[0] for k in kill]
        for r in c.execute("SELECT ve_label, value FROM ve_lexical WHERE id IN (%s) LIMIT 8"%','.join('?'*min(len(ids),8)), ids[:8]).fetchall():
            print(f'    e.g. {r["ve_label"]}={r["value"]}')
    if not live: print('dry-run (no write).'); c.close(); return
    ids=[k[0] for k in kill]; cur=c.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {SNAP}")
    cur.execute(f"CREATE TABLE {SNAP} AS SELECT * FROM ve_lexical WHERE id IN (%s)"%','.join('?'*len(ids)), ids)
    CH=900
    for i in range(0,len(ids),CH):
        ch=ids[i:i+CH]
        cur.execute("UPDATE ve_lexical SET delete_flagged=1, notes=COALESCE(notes,'')||' | reversed 2026-06-26 ungrounded overlay (verse-bounded rule)' WHERE id IN (%s)"%','.join('?'*len(ch)), ch)
    c.commit()
    print(f'LIVE: snapshot {SNAP} ({len(ids)} rows); soft-deleted {len(ids)}.')
    c.close()

if __name__=='__main__': main()
