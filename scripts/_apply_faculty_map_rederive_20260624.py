"""
Re-found FACULTY on a curated Strong's-lemma->faculty MAP (P2-compliant, replacing
the English-gloss-stem derivation). Builds `lemma_faculty_map` from the classified
batches, then re-derives the `faculty` ve_lexical rows across ALL clustered terms:
faculty = the term's intrinsic faculty (per-lemma, applied to every occurrence;
sub-entries keyed separately). T2/FLAG + 'none' terms get NO faculty row.

Safety: --dry-run shows the diff (add/remove/change/same) + blast radius; --live
backs up current faculty rows to `ve_lexical_faculty_backup` THEN replaces.

Usage:
  python -X utf8 scripts\_apply_faculty_map_rederive_20260624.py --dry-run
  python -X utf8 scripts\_apply_faculty_map_rederive_20260624.py --live
"""
import sqlite3, os, json, argparse, glob
from collections import Counter, defaultdict

DB=os.path.join('database','bible_research.db')
MAPDIR='research/VE-lexical/faculty-map-build'
PROV='faculty-map-v1-20260624'

def load_map():
    m={}
    for f in sorted(glob.glob(f'{MAPDIR}/map-batch*.json')):
        for r in json.load(open(f,encoding='utf-8')):
            m[r['s']]={'faculty':r.get('faculty') or [], 'basis':r.get('basis',''), 'conf':r.get('confidence','')}
    return m

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--live',action='store_true'); ap.add_argument('--dry-run',action='store_true')
    a=ap.parse_args(); live=a.live and not a.dry_run
    M=load_map()
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    # 1. build/refresh the map table
    c.execute("""CREATE TABLE IF NOT EXISTS lemma_faculty_map(
       strongs_number TEXT PRIMARY KEY, faculty TEXT, basis TEXT, confidence TEXT,
       model_version TEXT, created_at TEXT)""")
    if live:
        c.execute("delete from lemma_faculty_map")
        for s,r in M.items():
            c.execute("insert into lemma_faculty_map values(?,?,?,?,?,datetime('now'))",
                      (s, ','.join(r['faculty']), r['basis'], r['conf'], PROV))
        c.commit()
    # 2. compute current vs map faculty per clustered term-in-verse unit
    units=c.execute("""select vc.id vcid, m.strongs_number s
       from verse_context vc join mti_terms m on m.id=vc.mti_term_id
       where m.cluster_code is not null and coalesce(vc.delete_flagged,0)=0
         and coalesce(m.delete_flagged,0)=0
         and (m.status is null or m.status not in ('delete','candidate_delete','excluded'))""").fetchall()
    cur=defaultdict(set)
    for r in c.execute("""select vl.verse_context_id vcid, vl.value v from ve_lexical vl
       where vl.ve_label='faculty' and coalesce(vl.delete_flagged,0)=0"""):
        cur[r['vcid']].add(r['v'])
    add=rem=chg=same=newfac_units=0; valdist=Counter()
    for u in units:
        old=cur.get(u['vcid'],set())
        new=set(M.get(u['s'],{}).get('faculty',[]))
        for f in new: valdist[f]+=1
        if new: newfac_units+=1
        if old==new: same+=1
        elif not old and new: add+=1
        elif old and not new: rem+=1
        else: chg+=1
    print(f"map terms={len(M)} | clustered units={len(units)}")
    print(f"DIFF vs current faculty:  same={same}  ADD(none->fac)={add}  REMOVE(fac->none)={rem}  CHANGE={chg}")
    print(f"units that will carry a faculty after re-derive: {newfac_units} ({round(100*newfac_units/len(units))}%)  [was {sum(1 for u in units if cur.get(u['vcid']))}]")
    print(f"new faculty value distribution (unit-mentions): {dict(valdist.most_common())}")
    if live:
        # 3. backup then replace faculty rows for clustered units
        c.execute("""CREATE TABLE IF NOT EXISTS ve_lexical_faculty_backup AS
                     SELECT * FROM ve_lexical WHERE ve_label='faculty'""")
        # (re-create fresh each run is unsafe; only create once)
        vcids=tuple(u['vcid'] for u in units)
        # delete current faculty rows for these units in chunks
        cur2=c.cursor()
        CH=900
        for i in range(0,len(vcids),CH):
            chunk=vcids[i:i+CH]
            q="delete from ve_lexical where ve_label='faculty' and verse_context_id in (%s)"%','.join('?'*len(chunk))
            cur2.execute(q, chunk)
        # insert map-derived
        ins=0
        for u in units:
            for f in M.get(u['s'],{}).get('faculty',[]):
                cur2.execute("""insert into ve_lexical(verse_context_id,ve_nr,ve_label,value,notes,source_provenance,delete_flagged,created_at)
                   values(?,7,'faculty',?,?,?,0,datetime('now'))""",(u['vcid'],f,'R1 term-intrinsic from lemma_faculty_map',PROV))
                ins+=1
        c.commit()
        print(f"LIVE: backed up to ve_lexical_faculty_backup; replaced faculty rows; inserted {ins} map-derived faculty rows.")
    else:
        print("dry-run (no write).")
    c.close()

if __name__=='__main__': main()
