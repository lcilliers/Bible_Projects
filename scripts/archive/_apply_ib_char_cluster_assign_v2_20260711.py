"""Assign CLUSTER via the deterministic chain: master -> its 1 mti_term -> its 1
cluster. NO dominant vote. Researcher model 2026-07-11.

- Stamps `verse_span_index.cluster` on each Psalms characteristic master (the true
  1:1 assignment: the master's term's cluster_code).
- Rolls up to `ib_characteristic.cluster` (+ `cluster_all`): the single concept
  cluster its masters agree on; NULL where all masters' terms are unclustered;
  NULL + note where masters genuinely split across >1 concept cluster.
- **T2 is treated as NOT a concept cluster** (researcher: reference/supplementary
  bucket) — excluded from the concept resolution; still shown in cluster_all.
  FLAG (constitutional seats) is kept as a real bucket.

Usage:  python scripts/_apply_ib_char_cluster_assign_v2_20260711.py [--live]
"""
import sqlite3, os, sys
from collections import Counter, defaultdict

LIVE = '--live' in sys.argv
DB = os.path.join('database','bible_research.db')
c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; cur = c.cursor()
CH = "si.role='characteristic' AND si.role_provenance='read-2026' AND v.book_id=19"

def hascol(t,col): return any(r['name']==col for r in cur.execute(f"PRAGMA table_info({t})"))
for t,col in [('verse_span_index','cluster'),('ib_characteristic','cluster'),('ib_characteristic','cluster_all')]:
    if not hascol(t,col):
        if LIVE: cur.execute(f"ALTER TABLE {t} ADD COLUMN {col} TEXT"); print(f"  +column {t}.{col}")
        else: print(f"  [dry] would add {t}.{col}")

short = {r['cluster_code']:(r['short_name'] or r['cluster_code']) for r in cur.execute("SELECT cluster_code,short_name FROM cluster")}

# raw: every span -> the cluster_codes of its linked terms
rows = cur.execute(f"""SELECT si.id span, si.ib_char_id, mt.cluster_code code
  FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
  LEFT JOIN wa_verse_records w ON w.verse_span_id=si.id
  LEFT JOIN mti_terms mt ON mt.id=w.mti_term_id
  WHERE {CH}""").fetchall()

span_codes = defaultdict(list); span_ib = {}
for r in rows:
    span_codes[r['span']].append(r['code']); span_ib[r['span']] = r['ib_char_id']

def concept(codes):
    """distinct real concept clusters (exclude T2 as non-cluster, and null)."""
    return sorted({x for x in codes if x and x != 'T2'})

# master-level cluster (verse_span_index): the single concept cluster of its term
master_cluster = {}
for span, codes in span_codes.items():
    real = concept(codes)
    master_cluster[span] = real[0] if len(real)==1 else (Counter(x for x in codes if x and x!='T2').most_common(1)[0][0] if real else None)

# ib_char rollup
ib_spans = defaultdict(list)
for span, codes in span_codes.items(): ib_spans[span_ib[span]].append(codes)
ib_cluster = {}; ib_all = {}
n_clean=n_null=n_conflict=0
conflicts=[]
for ibid, spanlists in ib_spans.items():
    allcodes = [x for cl in spanlists for x in cl]
    real = concept(allcodes)
    rawdistinct = [x for x in dict.fromkeys([y for y in allcodes if y])]  # incl T2, order-preserved
    ib_all[ibid] = ' | '.join(f"{x}({short.get(x,x)})" for x in rawdistinct) or None
    if len(real)==1: ib_cluster[ibid]=real[0]; n_clean+=1
    elif len(real)==0: ib_cluster[ibid]=None; n_null+=1
    else:
        ib_cluster[ibid]=None; n_conflict+=1
        nm=cur.execute("SELECT name FROM ib_characteristic WHERE id=?",(ibid,)).fetchone()['name']
        conflicts.append((nm, real))

print(f"\nMASTER spans stamped: {len(master_cluster)}  (with concept cluster: {sum(1 for v in master_cluster.values() if v)}, null: {sum(1 for v in master_cluster.values() if not v)})")
print(f"ib_char rollup: clean single={n_clean}  null(all-unclustered)={n_null}  conflict(>1 concept)={n_conflict}")
print("conflicts (left NULL, flagged in cluster_all):")
for nm,real in conflicts: print(f"   '{nm}' -> {real}")

# distribution
dist=Counter();
for ibid,cl in ib_cluster.items():
    d=cur.execute("SELECT instance_count FROM ib_characteristic WHERE id=?",(ibid,)).fetchone()['instance_count']
    dist[cl or '(NULL)']+=1
print("\nib_char cluster distribution (records):")
for cl,n in sorted(dist.items(), key=lambda kv:-kv[1]):
    print(f"   {str(cl):8} {short.get(cl,''):16} {n}")

if LIVE:
    cur.executemany("UPDATE verse_span_index SET cluster=? WHERE id=?", [(v,k) for k,v in master_cluster.items()])
    cur.executemany("UPDATE ib_characteristic SET cluster=?, cluster_all=? WHERE id=?",
                    [(ib_cluster[k], ib_all[k], k) for k in ib_spans])
    c.commit()
    print(f"\nLIVE: stamped {len(master_cluster)} masters + {len(ib_spans)} ib_char records.")
else:
    print("\n[dry run] no writes. --live to apply.")
