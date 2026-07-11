"""Read-only: compare the FAMILY grouping (meaning/keyword-based) with the CLUSTER
assignment (term-based) over the 877 Psalms ib_characteristic records, and report
outliers -> a filed .md.

Outlier = a record whose term-CLUSTER differs from the modal cluster of its
meaning-FAMILY (both non-null). These are where the two independent groupings
disagree: a mis-family, a mis-cluster, or a genuine meaning/term cross-over.
"""
import sqlite3, os
from collections import Counter, defaultdict

c = sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory = sqlite3.Row
short = {r['cluster_code']:(r['short_name'] or r['cluster_code']) for r in c.execute("SELECT cluster_code,short_name FROM cluster")}
rows = c.execute("SELECT id,name,instance_count,family,cluster,cluster_all FROM ib_characteristic WHERE book_scope='19'").fetchall()

# direct family -> expected concept-cluster twin (None = no single clean twin; skipped from outlier test)
EXPECTED = {
 'inner-seat-heart-soul-spirit':'M47', 'praise-extol-sing':'M22', 'prayer-petition-crying-out':'M21',
 'knowing-understanding':'M15', 'joy-gladness':'M04', 'desire-longing-appetite':'M29',
 'fear-of-god-awe':'M01', 'trust-refuge-security':'M19', 'righteousness-integrity':'M26',
 'blessing-benediction':'M39', 'wickedness-ungodliness':'M27', 'malice-enmity-persecution':'M06',
 'sin-guilt-iniquity':'M10', 'faint-despair-languishing':'M24', 'thanksgiving':'M22',
 'keeping-guarding-vigilance':'M30', 'walk-way-conduct':'M30', 'memory-remembrance':'M41',
 'hope-waiting':'M18', 'deceit-falsehood':'M14', 'speech-mouth-tongue':'M42',
 'pride-arrogance-scoffing':'M08', 'wisdom-folly-teaching':'M15', 'love-devotion':'M05',
 'grief-lament-sorrow':'M03', 'rebellion-stubbornness':'M10', 'shame-confusion':'M07',
 'humility-lowliness-contrition':'M09', 'worship-prostration-service':'M36', 'violence-cruelty':'M06',
 'being-heard-listening':'M21', 'restoration-revival-satisfaction':'M38', 'faith-faithfulness-truth':'M13',
 'anger-wrath-vexation':'M02', 'being-searched-tested-by-god':'M35', 'turning-repentance':'M11',
 'rest-stillness-peace':'M33', 'life-death-vitality':'M25', 'strength-courage-steadfastness':'M23',
 'torah-obedience-word':'M30', 'confession-forgiveness':'M11',
 # ambiguous (no single clean twin) -> not outlier-tested:
 'seeking-inquiring':None, 'will-resolve-vow-intent':None, 'lifting-bearing':None, 'grace-mercy-compassion':None,
}
fam_clusters = defaultdict(Counter)
for r in rows:
    if r['cluster']: fam_clusters[r['family']][r['cluster']] += 1
fam_modal = {f: cc.most_common(1)[0][0] for f,cc in fam_clusters.items()}

# clusters that are semantic NEIGHBOURS — a record landing here vs its family-twin is
# a benign adjacency, not a genuine crossover.
ADJ = [{'M10','M27','M16','M08'},          # sin / evil / folly / pride (the descent)
       {'M09','M24','M07'},                # humility / weakness / shame (the low estate)
       {'M04','M29','M22','M46'},          # joy / desire / praise / abundance (the up-swell)
       {'M21','M37','M22','M18','M19'},    # prayer / calling / praise / hope / trust (Godward reach)
       {'M15','M17','M13'},                # wisdom / counsel / truth (the mind)
       {'M26','M12','M30'},                # righteousness / purity / obedience (the upright)
       {'M42','M22'},                      # speech / praise (outflow)
       {'M03','M24'},                      # grief / weakness
       {'M05','M39','M36'},                # love / blessing / service
       {'M11','M10'}]                      # repentance / sin
def adjacent(a,b):
    return any(a in s and b in s for s in ADJ)

testable = [r for r in rows if r['cluster'] and r['family'] and EXPECTED.get(r['family'])]
agree = [r for r in testable if r['cluster']==EXPECTED[r['family']]]
outliers = [r for r in testable if r['cluster']!=EXPECTED[r['family']]]
adj_out = [r for r in outliers if adjacent(r['cluster'], EXPECTED[r['family']])]
genuine = [r for r in outliers if not adjacent(r['cluster'], EXPECTED[r['family']])]
both = testable

L = []
L.append("# Family (meaning) vs Cluster (term) — comparison & outliers — Psalms\n")
L.append("> Read-only, 2026-07-11. Two independent groupings of the 877 meaning-records: "
         "**family** = keyword/meaning-based (46, `_apply_ib_char_family_grouping_v1`); "
         "**cluster** = term-based `master->mti_term->cluster_code` (`_apply_ib_char_cluster_assign_v2`). "
         "Where they disagree is the signal.\n")
L.append(f"- Records: **{len(rows)}** · with a cluster: **{sum(1 for r in rows if r['cluster'])}** · "
         f"NULL cluster (unclustered term): **{sum(1 for r in rows if not r['cluster'])}**.")
L.append(f"- Testable (family has a clean cluster-twin & record has a cluster): **{len(testable)}**.")
L.append(f"- **Agree** (term-cluster == family's expected cluster): **{len(agree)}** ({100*len(agree)//max(len(testable),1)}%).")
L.append(f"- **Adjacent** (differs but a semantic neighbour — benign): **{len(adj_out)}**.")
L.append(f"- **Genuine crossovers** (family & cluster name *unrelated* concepts — the real signal): **{len(genuine)}**.\n")

L.append("## Family → expected cluster twin (agreement of the two lenses)\n")
L.append("| family | expected cluster | records tested | agree | outliers | (modal actual) |")
L.append("|---|---|--:|--:|--:|---|")
for fam in sorted(EXPECTED, key=lambda f:-sum(fam_clusters[f].values())):
    exp=EXPECTED[fam]
    if not exp:
        L.append(f"| {fam} | *(no clean twin — skipped)* | — | — | — | {short.get(fam_modal.get(fam),'')} |"); continue
    recs=[r for r in testable if r['family']==fam]
    a=sum(1 for r in recs if r['cluster']==exp)
    L.append(f"| {fam} | {exp} ({short.get(exp,exp)}) | {len(recs)} | {a} | {len(recs)-a} | {short.get(fam_modal.get(fam),'')} |")

L.append("\n## GENUINE crossovers — family & cluster name unrelated concepts (the real signal)\n")
L.append("Each row: the record, its meaning-FAMILY (expected cluster), vs its own term-CLUSTER — where the two are *not* neighbours.\n")
L.append("| meaning | inst | family (expected) | THIS record's cluster |")
L.append("|---|--:|---|---|")
for r in sorted(genuine, key=lambda r:(-r['instance_count'], r['family'])):
    exp=EXPECTED[r['family']]
    L.append(f"| {r['name']} | {r['instance_count']} | {r['family']} ({short.get(exp,exp)}) | **{short.get(r['cluster'],r['cluster'])}** |")

L.append("\n## Adjacent-only differences (benign — neighbouring concepts)\n")
L.append(f"{len(adj_out)} records differ from their family-twin but land in a *neighbouring* cluster "
         "(e.g. wicked→Sin vs family-Evil; poor→Weakness vs family-Humility). Not errors — the two schemes "
         "just cut the same region slightly differently. Sample:\n")
L.append("| meaning | inst | family (expected) | cluster |")
L.append("|---|--:|---|---|")
for r in sorted(adj_out, key=lambda r:-r['instance_count'])[:20]:
    exp=EXPECTED[r['family']]
    L.append(f"| {r['name']} | {r['instance_count']} | {r['family']} ({short.get(exp,exp)}) | {short.get(r['cluster'],r['cluster'])} |")

L.append("\n## Genuine multi-cluster meanings (cluster NULL, flagged in cluster_all)\n")
for r in rows:
    if not r['cluster'] and r['cluster_all'] and '|' in (r['cluster_all'] or '') and r['family']!='other-uncategorised':
        # only those with >1 concept code
        codes=[x for x in (r['cluster_all'] or '').split(' | ') if not x.startswith('T2')]
        if len(codes)>1:
            L.append(f"- **{r['name']}** ({r['family']}): {r['cluster_all']}")

L.append("\n## How to read the outliers")
L.append("- **Family says X, cluster says Y** — three causes: (a) my keyword family-rule mis-placed the meaning; "
         "(b) the term's `cluster_code` is off; (c) a real cross-over (a word that *means* like X but whose *term* lives in Y, "
         "e.g. a boast-word keyworded into praise but clustered Pride). Each is worth an eyeball; none is auto-wrong.")
L.append("- The comparison is diagnostic, not corrective — nothing is changed here.")

out = 'verse-analysis/psalms/wa-ib-char-family-vs-cluster-comparison-20260711.md'
open(out,'w',encoding='utf-8').write('\n'.join(L))
print(f"records={len(rows)} testable={len(testable)} agree={len(agree)} adjacent={len(adj_out)} genuine={len(genuine)}")
print(f"filed -> {out}")
print("\nGenuine crossovers (family concept != cluster concept, not neighbours):")
for r in sorted(genuine, key=lambda r:-r['instance_count'])[:18]:
    exp=EXPECTED[r['family']]
    print(f"   {r['name']:14} x{r['instance_count']:<2} family={r['family'][:26]:26} (exp {short.get(exp,exp):12}) -> cluster={short.get(r['cluster'],r['cluster'])}")
