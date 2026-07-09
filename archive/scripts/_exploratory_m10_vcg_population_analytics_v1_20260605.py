"""_exploratory_m10_vcg_population_analytics_v1_20260605.py  (READ-ONLY)
Are M10's verse populations too large to read the actual verses together at the VCG stage?
Reports verses-per-sub-group and verses-per-VCG distributions.
"""
import sqlite3, os, statistics
c = sqlite3.connect('database/bible_research.db'); c.row_factory = sqlite3.Row; cur = c.cursor()
OUT = os.path.join('research', 'investigations', 'm10-vcg-population-analytics-20260605.md')
CL = 'M10'

base = """FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id
WHERE mt.cluster_code=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0"""

total = cur.execute("SELECT COUNT(*) " + base, (CL,)).fetchone()[0]

# per sub-group
subs = cur.execute(f"""
 SELECT cs.subgroup_code code, cs.label, COUNT(*) n
 {base} AND vc.cluster_subgroup_id=cs.id""".replace("FROM verse_context vc",
        "FROM verse_context vc JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id"),
        (CL,)).fetchall()
# simpler: redo cleanly
subs = cur.execute("""
 SELECT cs.subgroup_code code, cs.label, COUNT(*) n
 FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id
 JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id
 WHERE mt.cluster_code=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
 GROUP BY cs.id ORDER BY n DESC""", (CL,)).fetchall()

vcgs = cur.execute("""
 SELECT g.group_code code, COUNT(*) n
 FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id
 JOIN verse_context_group g ON g.id=vc.group_id
 WHERE mt.cluster_code=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
 GROUP BY g.id ORDER BY n DESC""", (CL,)).fetchall()

vsz = [r['n'] for r in vcgs]
ssz = [r['n'] for r in subs]

def stats(xs):
    xs = sorted(xs)
    return dict(count=len(xs), total=sum(xs), min=min(xs), median=statistics.median(xs),
                mean=round(statistics.mean(xs),1), max=max(xs),
                p90=xs[int(0.9*len(xs))-1] if xs else 0)

def hist(xs, edges):
    out=[]
    for lo,hi in edges:
        label = ('%d+' % lo) if hi >= 10**6 else ('%d-%d' % (lo, hi))
        out.append((label, sum(1 for x in xs if lo<=x<=hi)))
    return out

EDGES=[(1,5),(6,15),(16,30),(31,50),(51,100),(101,10**6)]

L=[f'# M10 — VCG / sub-group population analytics','',
   '> Read-only, 2026-06-05. Feasibility check for the new VCG approach (read the **actual verses** of a',
   '> group together, not the derived meaning or just the anchor). Question: are the populations too large?','',
   f'**M10 total** is_relevant active verses: **{total}**','',
   '## Sub-groups (the population read together to (re)form VCGs)','',
   f"- {len(subs)} sub-groups. sizes: min {stats(ssz)['min']} · median {stats(ssz)['median']} · "
   f"mean {stats(ssz)['mean']} · p90 {stats(ssz)['p90']} · **max {stats(ssz)['max']}**",'',
   '| Sub-group | Label | Verses |','|---|---|---|']
for r in subs:
    L.append(f"| {r['code']} | {(r['label'] or '')[:40]} | {r['n']} |")
L += ['','## VCGs (current grouping granularity)','',
   f"- {len(vcgs)} VCGs. sizes: min {stats(vsz)['min']} · median {stats(vsz)['median']} · "
   f"mean {stats(vsz)['mean']} · p90 {stats(vsz)['p90']} · **max {stats(vsz)['max']}**",'',
   '**VCG size histogram:**','']
for lab,n in hist(vsz, EDGES):
    L.append(f'- {lab} verses: {n} VCGs')
L += ['','**Largest VCGs:**','','| VCG | Verses |','|---|---|']
for r in vcgs[:12]:
    L.append(f"| {r['code']} | {r['n']} |")

# feasibility read
big_sub=sum(1 for x in ssz if x>100); big_vcg=sum(1 for x in vsz if x>50)
L += ['','## Feasibility read','',
   f'- Sub-groups > 100 verses (heavy to read whole): **{big_sub}** of {len(subs)}.',
   f'- VCGs > 50 verses: **{big_vcg}** of {len(vcgs)}.',
   f'- A verse text averages ~30–60 words; reading N verses together ≈ N×~45 words.',
   f"  Largest sub-group ({stats(ssz)['max']} verses) ≈ ~{stats(ssz)['max']*45:,} words to read at once.",]

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT,'w',encoding='utf-8').write('\n'.join(L)+'\n')
print('total', total, '| subgroups', len(subs), '| VCGs', len(vcgs),
      '| max sub', stats(ssz)['max'], '| max VCG', stats(vsz)['max'])
print('wrote', OUT)
