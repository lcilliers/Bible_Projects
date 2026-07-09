"""
LIVE (DB write): reset FACULTY to be verse-grounded per the researcher's rule
(2026-06-26): faculty appears on a verse ONLY if explicitly mentioned / inferred
ON THE VERSE, never via the lemma.

Mechanism = Variant C (see wa-faculty-reset-dryrun-v1-20260626.md):
  - faculty-WORD (1-3 faculties in lemma_faculty_map): carries its own faculty(ies)
      -> provenance 'faculty-verse-explicit-v1-20260626'  (the word IS in the verse)
  - SEAT (>=4 faculties: the 8 heart/spirit lemmas): NO auto-dump; inherits only the
      faculties named by genuine faculty-words (1-3 facs) co-present in the same verse
      -> provenance 'faculty-verse-inferred-seat-v1-20260626'  (lower-confidence inference)
  - non-faculty term (0 faculties): EMPTY

Safety (all-in-DB, reversible):
  - --live first copies the DB to backups/bible_research_pre-faculty-reset_20260626.db
  - snapshots current active faculty rows -> ve_lexical_faculty_pre_reset_20260626
  - SOFT-deletes current faculty rows (delete_flagged=1), then inserts the new rows
  --dry-run prints the write plan and counts only.

Usage:
  python -X utf8 scripts/_apply_faculty_reset_verse_grounded_v1_20260626.py --dry-run
  python -X utf8 scripts/_apply_faculty_reset_verse_grounded_v1_20260626.py --live
"""
import sqlite3, os, json, glob, re, argparse, shutil
from collections import defaultdict, Counter

DB=os.path.join('database','bible_research.db')
BACKUP=os.path.join('backups','bible_research_pre-faculty-reset_20260626.db')
SNAP='ve_lexical_faculty_pre_reset_20260626'
MAPDIR='research/VE-lexical/faculty-map-build'
PROV_EXP='faculty-verse-explicit-v1-20260626'
PROV_SEAT='faculty-verse-inferred-seat-v1-20260626'
SEAT_MIN=4

def canon(s):
    if not s: return None
    m=re.match(r'^([HG])(\d+)([A-Z]?)$', s.strip().upper())
    if not m: return None
    L,num,suf=m.groups(); return f'{L}{int(num):04d}{suf}'

def load_map():
    fac={}
    for f in sorted(glob.glob(f'{MAPDIR}/map-batch*.json')):
        for r in json.load(open(f,encoding='utf-8')):
            ck=canon(r['s'])
            if ck: fac[ck]=r.get('faculty') or []
    return fac

def faculties_of(strong, FAC):
    ck=canon(strong)
    if ck is None: return []
    if ck in FAC: return FAC[ck]
    return FAC.get(re.sub(r'[A-Z]$','',ck), [])

def compute(c, FAC):
    units=c.execute("""
      SELECT vc.id vcid, vr.verse_id vid, m.strongs_number s
      FROM verse_context vc
      JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
      JOIN mti_terms m ON m.id = vc.mti_term_id
      WHERE m.cluster_code IS NOT NULL
        AND COALESCE(vc.delete_flagged,0)=0 AND COALESCE(m.delete_flagged,0)=0
        AND (m.status IS NULL OR m.status NOT IN ('delete','candidate_delete','excluded'))
        AND vr.verse_id IS NOT NULL
    """).fetchall()
    verse_profile=defaultdict(set)
    for r in c.execute("SELECT verse_id, strongs FROM verse_morphology WHERE strongs IS NOT NULL"):
        for tok in (r['strongs'] or '').split():
            f=faculties_of(tok, FAC)
            if 1<=len(f)<=3: verse_profile[r['verse_id']].update(f)
    rows=[]   # (vcid, value, provenance, note)
    for u in units:
        own=faculties_of(u['s'], FAC)
        if 1<=len(own)<=3:
            for f in own:
                rows.append((u['vcid'], f, PROV_EXP, 'faculty-word explicit in verse'))
        elif len(own)>=SEAT_MIN:
            for f in sorted(verse_profile.get(u['vid'], set())):
                rows.append((u['vcid'], f, PROV_SEAT, 'seat: faculty inferred from verse faculty-words'))
    return units, rows

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--live',action='store_true'); ap.add_argument('--dry-run',action='store_true')
    a=ap.parse_args(); live=a.live and not a.dry_run
    FAC=load_map()
    if live:
        print('backing up DB ->', BACKUP); shutil.copy2(DB, BACKUP)
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    units, rows=compute(c, FAC)
    old=c.execute("SELECT COUNT(*) FROM ve_lexical WHERE ve_label='faculty' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    exp=sum(1 for r in rows if r[2]==PROV_EXP); seat=sum(1 for r in rows if r[2]==PROV_SEAT)
    nunits=len(set(r[0] for r in rows))
    print(f'in-scope clustered units: {len(units)}')
    print(f'current active faculty rows to SOFT-DELETE: {old}')
    print(f'NEW rows to insert: {len(rows)}  (explicit={exp}  seat-inferred={seat})  across {nunits} units')
    print(f'value dist: {dict(Counter(r[1] for r in rows).most_common())}')
    if not live:
        print('dry-run (no write).'); c.close(); return
    cur=c.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {SNAP}")
    cur.execute(f"CREATE TABLE {SNAP} AS SELECT * FROM ve_lexical WHERE ve_label='faculty' AND COALESCE(delete_flagged,0)=0")
    cur.execute("UPDATE ve_lexical SET delete_flagged=1, notes=COALESCE(notes,'')||' | soft-deleted 2026-06-26 faculty-reset (lemma-derived, invalid by rule)' WHERE ve_label='faculty' AND COALESCE(delete_flagged,0)=0")
    cur.executemany("""INSERT INTO ve_lexical(verse_context_id,ve_nr,ve_label,related_tier,value,notes,source_provenance,delete_flagged,created_at)
                       VALUES(?,7,'faculty',NULL,?,?,?,0,datetime('now'))""",
                    [(r[0], r[1], r[3], r[2]) for r in rows])
    c.commit()
    newn=c.execute("SELECT COUNT(*) FROM ve_lexical WHERE ve_label='faculty' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
    print(f'LIVE done. snapshot={SNAP} ({old} rows). active faculty rows now: {newn}')
    c.close()

if __name__=='__main__': main()
