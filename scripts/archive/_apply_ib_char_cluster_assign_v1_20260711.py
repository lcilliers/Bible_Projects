"""Assign each ib_characteristic record (Psalms) to a CLUSTER based on its term.

Adds `cluster` (primary M-code) + `cluster_all` (every candidate preserved, so
the multi-cluster terms are not lossily collapsed). Source of the term->cluster
link = `mti_terms.cluster_code`, matched by the record's base lemma.

Resolution for the primary `cluster` (46 lemmas map to >1 code):
  1. gather all cluster_codes across the lemma's suffixed-strong terms, weighted
     by how many terms carry each;
  2. prefer substantive **M-codes** over T2 (Supplementary/reference) and FLAG
     (seat/qualifier) — drop T2/FLAG if any M-code is present;
  3. among the remainder, take the modal code (tie -> lowest code string).
`cluster_all` keeps ALL distinct codes (with short names) regardless.
Lemmas with no cluster_code (138) -> cluster NULL.

Note/limitation: assignment is at LEMMA grain (the read never linked meaning ->
suffixed sense-strong), so a meaning-keyed record inherits its lemma's cluster;
where a lemma spans clusters the split is not meaning-resolved (see cluster_all).

Usage:  python scripts/_apply_ib_char_cluster_assign_v1_20260711.py [--live]
"""
import sqlite3, os, sys
from collections import Counter, defaultdict

LIVE = '--live' in sys.argv
DB = os.path.join('database','bible_research.db')
c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; cur = c.cursor()

def hascol(t,col): return any(r['name']==col for r in cur.execute(f"PRAGMA table_info({t})"))
for col in ['cluster','cluster_all']:
    if not hascol('ib_characteristic', col):
        if LIVE: cur.execute(f"ALTER TABLE ib_characteristic ADD COLUMN {col} TEXT"); print("  +column", col)
        else: print("  [dry] would add column", col)

short = {r['cluster_code']: (r['short_name'] or r['cluster_code'])
         for r in cur.execute("SELECT cluster_code,short_name FROM cluster")}

def codes_for(lemma):
    """all cluster_codes for the lemma's terms, weighted by term-count."""
    ctr = Counter()
    for r in cur.execute("SELECT cluster_code FROM mti_terms WHERE strongs_number LIKE ?||'%' AND cluster_code IS NOT NULL AND cluster_code<>''",(lemma,)):
        ctr[r['cluster_code']] += 1
    return ctr

def resolve(ctr):
    if not ctr: return None
    m = {k:v for k,v in ctr.items() if k not in ('T2','FLAG')}   # prefer M-codes
    pool = m if m else dict(ctr)
    return sorted(pool.items(), key=lambda kv:(-kv[1], kv[0]))[0][0]

rows = cur.execute("SELECT id,char_key,instance_count FROM ib_characteristic WHERE book_scope='19'").fetchall()
assign = {}
for r in rows:
    lem = r['char_key'].split(':')[0]
    ctr = codes_for(lem)
    primary = resolve(ctr)
    allc = ' | '.join(f"{k}({short.get(k,k)})" for k,_ in ctr.most_common()) or None
    assign[r['id']] = (primary, allc)

# distribution
rec = Counter(); inst = defaultdict(int)
for r in rows:
    p = assign[r['id']][0] or '(none)'
    rec[p]+=1; inst[p]+=r['instance_count']
print(f"\nRecords: {len(rows)} | distinct clusters used: {len([k for k in rec if k!='(none)'])}")
print(f"{'cluster':10} {'name':22} {'recs':>5} {'inst':>6}")
for code,_ in sorted(rec.items(), key=lambda kv:-inst[kv[0]]):
    print(f"  {code:8} {short.get(code,'—' if code=='(none)' else code):22} {rec[code]:5} {inst[code]:6}")

if LIVE:
    cur.executemany("UPDATE ib_characteristic SET cluster=?, cluster_all=? WHERE id=?",
                    [(assign[r['id']][0], assign[r['id']][1], r['id']) for r in rows])
    c.commit()
    print(f"\nLIVE: wrote cluster + cluster_all on {len(rows)} records.")
else:
    print("\n[dry run] no writes. --live to apply.")
