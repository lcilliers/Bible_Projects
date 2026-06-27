"""
Build `verse_coverage` — a DERIVED coverage anchor (one row per verse).
The unique-verse anchor is `verse` (stable). This is a *view of* it carrying
provisional scope + touched, so coverage checks are one query, not a 4-table join.

  scope  : 'in-scope' (>=1 NON-T2 study-term span) | 'T2-only' | 'no-study'
  touched: 1 if the verse has an active ve_lexical unit on a NON-T2 term, else 0

NOTE: scope rests on the cluster/term classification (the debunked anchor) — it is
PROVISIONAL and recomputable; `verse` remains the source of truth. Reversible: DROP TABLE.
"""
import sqlite3, os, re
from collections import defaultdict
DB=os.path.join('database','bible_research.db')

def canon(s):
    m=re.match(r'^([HG])(\d+)',(s or '').upper()); return f'{m.group(1)}{int(m.group(2)):04d}' if m else None

DDL="""
CREATE TABLE verse_coverage (
  verse_id        INTEGER PRIMARY KEY,
  reference       TEXT,
  testament       TEXT,
  n_spans         INTEGER,
  n_study_nonT2   INTEGER,
  n_T2            INTEGER,
  scope           TEXT,      -- in-scope | T2-only | no-study  (PROVISIONAL: cluster-based)
  n_lexical_units INTEGER,   -- active ve_lexical units on non-T2 terms
  touched         INTEGER,   -- 1/0
  scope_basis     TEXT DEFAULT 'provisional: mti cluster_code (non-T2 study term) — debunked anchor; recomputable',
  built_at        TEXT DEFAULT (datetime('now'))
)
"""

def main():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()
    # cluster family
    fam={}
    for r in c.execute("SELECT strongs_number, cluster_code FROM mti_terms WHERE cluster_code IS NOT NULL AND COALESCE(delete_flagged,0)=0 AND (status IS NULL OR status NOT IN ('delete','candidate_delete','excluded'))"):
        fam.setdefault(canon(r['strongs_number']),r['cluster_code'])
    # per verse span tallies
    nspans=defaultdict(int); nstudy=defaultdict(int); nt2=defaultdict(int)
    for r in c.execute('SELECT verse_id, primary_strong FROM verse_span_index'):
        nspans[r['verse_id']]+=1
        cl=fam.get(canon(r['primary_strong']))
        if cl=='T2': nt2[r['verse_id']]+=1
        elif cl: nstudy[r['verse_id']]+=1
    # touched + lexical-unit counts (active ve_lexical on non-T2 term)
    units=defaultdict(int)
    for r in c.execute("""SELECT vr.verse_id vid, COUNT(DISTINCT vl.verse_context_id) u
        FROM ve_lexical vl JOIN verse_context vc ON vc.id=vl.verse_context_id
        JOIN wa_verse_records vr ON vr.id=vc.verse_record_id JOIN mti_terms m ON m.id=vc.mti_term_id
        WHERE COALESCE(vl.delete_flagged,0)=0 AND m.cluster_code IS NOT NULL AND m.cluster_code!='T2' AND vr.verse_id IS NOT NULL
        GROUP BY vr.verse_id"""):
        units[r['vid']]=r['u']

    cur.execute("DROP TABLE IF EXISTS verse_coverage"); cur.execute(DDL)
    rows=[]
    for v in c.execute('SELECT id, reference, testament FROM verse').fetchall():
        vid=v['id']; st=nstudy.get(vid,0); t2=nt2.get(vid,0)
        scope='in-scope' if st>0 else ('T2-only' if t2>0 else 'no-study')
        u=units.get(vid,0)
        rows.append((vid, v['reference'], v['testament'], nspans.get(vid,0), st, t2, scope, u, 1 if u>0 else 0))
    cur.executemany("INSERT INTO verse_coverage(verse_id,reference,testament,n_spans,n_study_nonT2,n_T2,scope,n_lexical_units,touched) VALUES(?,?,?,?,?,?,?,?,?)", rows)
    c.commit()

    print('verse_coverage built:', len(rows), 'rows')
    print('  by scope:', dict(c.execute("SELECT scope, COUNT(*) FROM verse_coverage GROUP BY scope").fetchall()))
    print('  in-scope touched:', c.execute("SELECT COUNT(*) FROM verse_coverage WHERE scope='in-scope' AND touched=1").fetchone()[0])
    print('  in-scope NOT touched:', c.execute("SELECT COUNT(*) FROM verse_coverage WHERE scope='in-scope' AND touched=0").fetchone()[0])
    print('\n  one-query coverage check example:')
    print("    SELECT scope, touched, COUNT(*) FROM verse_coverage GROUP BY scope, touched;")
    for r in c.execute("SELECT scope, touched, COUNT(*) n FROM verse_coverage GROUP BY scope, touched ORDER BY scope, touched"):
        print(f"      {r['scope']:<10} touched={r['touched']}  {r['n']}")
    c.close()

if __name__=='__main__': main()
