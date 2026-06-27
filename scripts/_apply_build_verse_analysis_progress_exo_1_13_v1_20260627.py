"""Build verse_analysis_progress markers for Exo 1:13 (idempotent, additive per focus verse).
Markers (researcher vocabulary 2026-06-27):
  'Analysis in progress'         -> the focus verse (Exo 1:13)
  'Observation cross referenced' -> every in-index verse referenced by the focus verse's
                                    observations, with xref_verse = the focus verse.
Re-derivable from ib_observation; out-of-index refs (e.g. Lev 25:44/45) are excluded.
Reversible: DELETE WHERE reference=FOCUS OR xref_verse=FOCUS, or DROP TABLE."""
import sqlite3, os, re
FOCUS='Exo 1:13'
c=sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory=sqlite3.Row; cur=c.cursor()
refs=set(r['reference'] for r in c.execute("SELECT reference FROM verse"))
amap={'Deut':'Deu','Ps':'Psa','Mark':'Mar','Matt':'Mat','Eccl':'Ecc','Prov':'Pro'}
nb=lambda b: amap.get(b,b)
def extract(t):
    o=[]
    for m in re.finditer(r'\b([1-3]?[A-Z][a-z]+)\s+(\d+):(\d+(?:[-,]\d+)*)', t or ''):
        bk,ch,vp=m.groups()
        for n in re.split(r',',vp):
            if '-' in n:
                a,b=n.split('-'); o+=[(bk,ch,str(x)) for x in range(int(a),int(b)+1)]
            else: o.append((bk,ch,n))
    return o
xref={}
for r in c.execute("SELECT id,dimension,reconsider_at,narrative,basis FROM ib_observation WHERE origin_verse IN ('Exo 1:13','Exo 1:14')"):
    seen=set()
    for f in (r['reconsider_at'],r['narrative'],r['basis']):
        for bk,ch,v in extract(f):
            cand=f'{nb(bk)} {ch}:{v}'
            if cand in seen or cand==FOCUS: continue
            seen.add(cand)
            if cand not in refs: continue
            xref.setdefault(cand,{'obs':set(),'dims':set()})
            xref[cand]['obs'].add(r['id']); xref[cand]['dims'].add(r['dimension'])
cur.execute("""CREATE TABLE IF NOT EXISTS verse_analysis_progress(
  id INTEGER PRIMARY KEY, verse_id INTEGER, reference TEXT,
  marker TEXT, xref_verse TEXT, ref_by_obs TEXT, ref_dims TEXT,
  note TEXT, created TEXT DEFAULT (datetime('now')), updated TEXT DEFAULT (datetime('now')))""")
cur.execute("DELETE FROM verse_analysis_progress WHERE reference=? OR xref_verse=?",(FOCUS,FOCUS))
vid=lambda ref:(c.execute("SELECT id FROM verse WHERE reference=?",(ref,)).fetchone() or [None])[0]
cur.execute("INSERT INTO verse_analysis_progress(verse_id,reference,marker,xref_verse,note) VALUES(?,?,?,?,?)",
            (vid(FOCUS),FOCUS,'Analysis in progress',None,'focus verse; fan-out worklist open'))
for ref in sorted(xref):
    d=xref[ref]
    cur.execute("INSERT INTO verse_analysis_progress(verse_id,reference,marker,xref_verse,ref_by_obs,ref_dims) VALUES(?,?,?,?,?,?)",
       (vid(ref),ref,'Observation cross referenced',FOCUS,
        ','.join(f'#{i}' for i in sorted(d['obs'])),
        ','.join(sorted(d['dims'],key=lambda x:int(re.sub(r'\D','',x))))))
c.commit()
print('Analysis in progress:', c.execute("SELECT COUNT(*) FROM verse_analysis_progress WHERE marker='Analysis in progress'").fetchone()[0],
      '| Observation cross referenced:', c.execute("SELECT COUNT(*) FROM verse_analysis_progress WHERE marker='Observation cross referenced'").fetchone()[0])
