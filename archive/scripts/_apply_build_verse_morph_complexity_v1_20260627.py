"""
Build `verse_morph_complexity` — a DERIVED morphological-simplicity score per verse.
Layer-1 support: find grammatically SIMPLE verses (no isolation by term).
Components are stored so the score can be re-weighted; `verse` remains source of truth.
Reversible: DROP TABLE. Idempotent rebuild.

  score = max(0,finite-1)*2  + subord*2 + nonfinite + max(0,conj-1) + max(0,prep-1) + max(0,content-5)
  (extra clauses & subordination weigh most; then embedded verbs, coordination, phrases, length)
"""
import sqlite3, os, re
from collections import defaultdict
DB=os.path.join('database','bible_research.db')
def canon(s):
    m=re.match(r'^([HG])(\d+)',(s or '').upper()); return f'{m.group(1)}{int(m.group(2)):04d}' if m else None
SUBORD={'H0834','H3588','G3739','G3754','G2443','G1437','G3752','G5613','G1487','G3753','G1893'}
def is_finite(m):
    if m.startswith('HV'): return (m[3] if len(m)>3 else '') in 'piwjvqu'
    p=m.split('-'); return p[0]=='V' and len(p)>1 and any(x in p[1] for x in 'ISMO')
def is_nonfinite(m):
    if m.startswith('HV'): return (m[3] if len(m)>3 else '') in 'cars'
    p=m.split('-'); return p[0]=='V' and len(p)>1 and any(x in p[1] for x in 'NP')

DDL="""
CREATE TABLE verse_morph_complexity (
  verse_id INTEGER PRIMARY KEY, reference TEXT,
  n_content INTEGER, n_finite_verb INTEGER, n_nonfinite_verb INTEGER,
  n_conj INTEGER, n_prep INTEGER, n_subord INTEGER,
  complexity_score INTEGER,
  built_at TEXT DEFAULT (datetime('now'))
)
"""
def main():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()
    spans=defaultdict(list)
    for r in c.execute('SELECT verse_id, primary_strong, pos, morph_code FROM verse_span_index'):
        spans[r['verse_id']].append((r['pos'], r['morph_code'] or '', canon(r['primary_strong'])))
    ref={r['id']:r['reference'] for r in c.execute('SELECT id, reference FROM verse')}
    cur.execute("DROP TABLE IF EXISTS verse_morph_complexity"); cur.execute(DDL)
    out=[]
    for vid,sp in spans.items():
        co=cj=pr=fi=nf=su=0
        for pos,m,cs in sp:
            if pos in ('noun','verb','adjective','pronoun'): co+=1
            if m.startswith('HC') or m=='CONJ' or pos=='conjunction' or cs in ('G2532','H9002'): cj+=1
            if pos=='preposition' or m=='PREP' or m.startswith('HR'): pr+=1
            if is_finite(m): fi+=1
            if is_nonfinite(m): nf+=1
            if cs in SUBORD: su+=1
        score=max(0,fi-1)*2 + su*2 + nf + max(0,cj-1) + max(0,pr-1) + max(0,co-5)
        out.append((vid, ref.get(vid), co, fi, nf, cj, pr, su, score))
    cur.executemany("INSERT INTO verse_morph_complexity(verse_id,reference,n_content,n_finite_verb,n_nonfinite_verb,n_conj,n_prep,n_subord,complexity_score) VALUES(?,?,?,?,?,?,?,?,?)", out)
    c.commit()
    print('verse_morph_complexity built:', len(out), 'rows')
    print('\nin-scope verses by complexity threshold (one-query filter):')
    for thr in [0,1,2,3,5]:
        n=c.execute("SELECT COUNT(*) FROM verse_morph_complexity mc JOIN verse_coverage vc ON vc.verse_id=mc.verse_id WHERE vc.scope='in-scope' AND mc.complexity_score<=?",(thr,)).fetchone()[0]
        print(f'   score <= {thr}: {n} in-scope verses')
    print('\nexample query:  SELECT reference FROM verse_morph_complexity mc JOIN verse_coverage vc ON vc.verse_id=mc.verse_id WHERE vc.scope=\'in-scope\' AND mc.complexity_score<=2;')
    c.close()
if __name__=='__main__': main()
