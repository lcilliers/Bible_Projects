"""
Cross-cluster BONDS for the M10-family logical units (read-only).

Two factual signals of where a unit is "also dealt with" in other clusters:
 (1) CO-OCCURRENCE (primary): the unit's focus terms share verses with terms
     owned by other clusters (from the on-disk corpus fan-out). Count = number
     of the unit's verses in which a term of that other cluster also appears.
 (2) XREF (term-architecture): the unit's Strong's has an XREF copy in a
     registry whose dominant cluster is non-family (thin — every sin-term is
     M10-owned, so this mostly adds a few; reported as "XREF-adds").

Outputs a markdown table + a cluster-name legend. No DB writes.
"""
import sqlite3, json, os
from collections import Counter, defaultdict

DB = os.path.join('database','bible_research.db')
CORPUS = os.path.join('Sessions-v2','M10-Sin','findings','wa-m10-corpus-1904verses-v1_0-20260622.json')
FAM = {'M10','M10b','M10c','T2','FLAG'}

c = sqlite3.connect(DB); c.row_factory = sqlite3.Row

# unit -> {name, strongs}
units = defaultdict(lambda: {'name':'', 'strongs':set()})
q = '''SELECT ch.cluster_code uc, ch.char_seq seq, ch.short_name nm, mt.strongs_number sn
 FROM characteristic ch
 JOIN characteristic_subgroup cs ON cs.characteristic_id=ch.id AND cs.delete_flagged=0
 JOIN mti_term_subgroup mts ON mts.cluster_subgroup_id=cs.cluster_subgroup_id AND mts.delete_flagged=0
 JOIN mti_terms mt ON mt.id=mts.mti_term_id AND (mt.delete_flagged IS NULL OR mt.delete_flagged=0)
 WHERE ch.cluster_code IN ("M10","M10b","M10c") GROUP BY ch.id, mt.id'''
for r in c.execute(q):
    k = (r['uc'], r['seq']); units[k]['name'] = r['nm']; units[k]['strongs'].add(r['sn'])

# cluster code -> short name
cname = {r['cluster_code']: (r['description'] or '') for r in c.execute('SELECT cluster_code, description FROM cluster')}

def reg_dom_cluster(fk):
    for x in c.execute('SELECT cluster_code cc,count(*) n FROM mti_terms WHERE owning_registry_fk=? AND (delete_flagged IS NULL OR delete_flagged=0) GROUP BY cc ORDER BY n DESC',(fk,)):
        if x['cc'] not in FAM: return x['cc']
    return None

xref_map = defaultdict(set)
for r in c.execute('SELECT strongs_number sn, word_registry_fk fk FROM wa_term_inventory WHERE term_owner_type="XREF" AND (delete_flagged IS NULL OR delete_flagged=0)'):
    xref_map[r['sn']].add(r['fk'])

# corpus co-occurrence: strong -> Counter(other cluster), counting verses
corpus = json.load(open(CORPUS, encoding='utf-8'))
strong_coocc = defaultdict(Counter)
for V in corpus['verses']:
    occ = V['term_occurrences']
    foci = [o for o in occ if o['term'].get('focus_cluster') and o['term'].get('cluster') in ('M10','M10b','M10c')]
    others = set(o['term'].get('cluster') for o in occ
                 if o['term'].get('cluster') and o['term'].get('cluster') not in FAM)
    for f in foci:
        for oc in others:
            strong_coocc[f['term']['strong']][oc] += 1

used = set()
rows = []
for (uc, seq), d in sorted(units.items()):
    co = Counter(); xref = set()
    for sn in d['strongs']:
        co.update(strong_coocc[sn])
        for fk in xref_map.get(sn, ()):
            dc = reg_dom_cluster(fk)
            if dc and dc not in FAM: xref.add(dc)
    top = co.most_common(4)
    used.update(k for k, _ in top); used.update(xref)
    xadd = sorted(xref - set(k for k, _ in top))
    bonds = ' · '.join(f'{k}({v})' for k, v in top) if top else '—'
    rows.append((f'{uc} #{seq}', d['name'], bonds, ', '.join(xadd) if xadd else '—'))

print('| Unit | Bonds — co-occurrence (verses shared) | XREF-adds |')
print('|---|---|---|')
for code, name, bonds, xadd in rows:
    print(f'| **{code}** {name} | {bonds} | {xadd} |')
print()
print('**Cluster legend:** ' + ' · '.join(f'{k}={cname.get(k,k)}' for k in sorted(used)))
