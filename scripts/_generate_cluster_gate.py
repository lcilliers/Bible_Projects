"""
_generate_cluster_gate.py  — READ-ONLY per-cluster gate report for the L2 verse-read.

The per-cluster gate is the cheap, standard check run when a cluster's verse-read
is complete, BEFORE sign-off: (1) coverage, (2) a mechanical tier profile, (3) a
flag-rate breakdown separating genuine artifacts from benign self-audit notes,
(4) homonym / clustering-misfit surfacing, (5) a pointer to the spot-check.

Tier findings are stored POSITIONALLY (no field-name column), but their VALUES come
from distinct controlled vocabularies, so the profile is built by classifying each
finding_value into the field-vocabulary it belongs to — no slot decode required.

Usage:  python scripts/_generate_cluster_gate.py --cluster M02
Output: outputs/markdown/<CLUSTER>-cluster-gate-<YYYYMMDD>.md
Safe: read-only (no DB writes).
"""
import argparse, os, sqlite3, datetime
from collections import Counter

DB = os.path.join('database', 'bible_research.db')

# controlled vocabularies, keyed by the field they belong to (case-sensitive where it matters)
VOCAB = {
    'type':                {'action', 'status', 'quality'},
    'origin':              {'within-person', 'received-from-outside', 'bestowed-by-God',
                            'carried-generationally', 'from-other-spirits'},
    'attributed_to_God':   {'yes', 'no'},
    'typology_direction':  {'human->divine', 'divine->human', 'none'},
    'faculty':             {'perception', 'cognition', 'memory', 'affect', 'creativity',
                            'volition', 'agency', 'moral-evaluation', 'conscience', 'relational'},
    'constitutional_location': {'spirit', 'soul', 'heart', 'mind', 'body'},
    'literary_setting':    {'narrative', 'poetry', 'law', 'prophecy', 'wisdom', 'epistle',
                            'gospel', 'apocalyptic', 'genealogy', 'song'},
    'compound':            {'simple'},
    'immediate_response':  {'SILENT'},
    'null_token':          {'NONE'},
    'not_stated':          {'not-stated'},
}
# reverse index value -> field (first match wins; vocabs are disjoint by design)
VAL2FIELD = {}
for field, vals in VOCAB.items():
    for v in vals:
        VAL2FIELD[v] = field


def bar(n, total, width=32):
    if not total:
        return ''
    fill = int(round(width * n / total))
    return '█' * fill + '·' * (width - fill)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cluster', required=True)
    args = ap.parse_args()
    cl = args.cluster

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    def q(sql, *a):
        return list(c.execute(sql, a))

    # ---- 1. coverage ----
    total_tiv = q("""SELECT COUNT(*) n FROM verse_context vc
                     JOIN mti_terms mt ON mt.id = vc.mti_term_id
                     WHERE mt.cluster_code = ?""", cl)[0]['n']
    covered = q("""SELECT COUNT(DISTINCT verse_context_id) n FROM finding
                   WHERE cluster_code=? AND provenance='l2_meaning'""", cl)[0]['n']

    prov = q("""SELECT provenance, COUNT(*) n FROM finding WHERE cluster_code=?
                GROUP BY provenance ORDER BY n DESC""", cl)
    n_api = q("SELECT COUNT(*) n FROM finding WHERE cluster_code=? AND provenance='l2_api'", cl)[0]['n']
    n_meaning = q("SELECT COUNT(*) n FROM finding WHERE cluster_code=? AND provenance='l2_meaning'", cl)[0]['n']

    # ---- 2. tier profile (classify l2_api values) ----
    profile = {f: Counter() for f in VOCAB}
    rows = q("""SELECT finding_value FROM finding
                WHERE cluster_code=? AND provenance='l2_api'""", cl)
    unclassified = 0
    for r in rows:
        v = r['finding_value']
        f = VAL2FIELD.get(v)
        if f:
            profile[f][v] += 1
        else:
            unclassified += 1  # free-text fields: sense_applied, mode, purpose, produces_effect, relational, compound:<parts>

    # ---- 3. flag analysis ----
    flagged = q("""SELECT finding_value FROM finding
                   WHERE cluster_code=? AND provenance='l2_meaning' AND flagged_for_review=1""", cl)
    genuine = [r for r in flagged if any(k in r['finding_value']
               for k in ('HOMONYM', 'FLAGGED as', 'wrong-sense', 'set aside from'))]
    benign = len(flagged) - len(genuine)

    # ---- 4. homonym / misfit surfacing (genuine flagged meanings, first sentence) ----
    def first_sentence(t):
        t = t.replace('\n', ' ')
        return (t[:200] + '...') if len(t) > 200 else t

    # ---- write report ----
    today = datetime.date.today().strftime('%Y%m%d')
    out = os.path.join('outputs', 'markdown', f'{cl}-cluster-gate-{today}.md')
    L = []
    L.append(f'# {cl} — Per-Cluster Gate Report')
    L.append('')
    L.append(f'> Read-only mechanical gate for the L2 verse-read. Generated {datetime.date.today().isoformat()}. '
             f'Tier profile built by value-classification (positional storage; no slot decode). '
             f'This report does not sign off the cluster — it surfaces the evidence for the researcher to.')
    L.append('')

    # 1 coverage
    pct = (100.0 * covered / total_tiv) if total_tiv else 0
    L.append('## 1. Coverage')
    L.append('')
    L.append(f'- **{covered} / {total_tiv} own term-in-verses have a meaning ({pct:.0f}%)**')
    L.append('')
    L.append('| provenance | findings |')
    L.append('|---|---:|')
    for r in prov:
        L.append(f'| {r["provenance"]} | {r["n"]:,} |')
    L.append('')
    if n_meaning:
        L.append(f'- Fan-out ratio: {n_api/n_meaning:.1f} tier findings (l2_api) per meaning paragraph (l2_meaning).')
    L.append('')

    # 2 tier profile
    L.append('## 2. Mechanical tier profile')
    L.append('')
    L.append('Distribution of the controlled-vocabulary tier values across all l2_api findings. '
             'Free-text fields (sense_applied, mode, purpose_equips, produces_effect, relational_implication) '
             f'are not profiled here ({unclassified:,} free-text values).')
    L.append('')
    order = ['type', 'origin', 'attributed_to_God', 'typology_direction', 'faculty',
             'constitutional_location', 'literary_setting', 'immediate_response']
    for f in order:
        ctr = profile[f]
        tot = sum(ctr.values())
        if not tot:
            continue
        L.append(f'### {f}  ({tot:,} values)')
        L.append('')
        L.append('| value | n | share |')
        L.append('|---|---:|---|')
        for v, n in ctr.most_common():
            L.append(f'| {v} | {n:,} | {bar(n, tot)} {100*n/tot:.0f}% |')
        L.append('')

    # 3 flags
    L.append('## 3. Flag-rate analysis')
    L.append('')
    fr = (100.0 * len(flagged) / n_meaning) if n_meaning else 0
    gr = (100.0 * len(genuine) / n_meaning) if n_meaning else 0
    L.append(f'- **{len(flagged)} / {n_meaning} meanings flagged ({fr:.1f}%)**, of which:')
    L.append(f'  - **{len(genuine)} genuine** homonym / wrong-sense artifacts to set aside ({gr:.1f}% of cluster) — see §4.')
    L.append(f'  - **{benign} benign** self-audit notes (a non-null field, typically `immediate_response=SILENT`, '
             f'not reflected in the prose of forensic/siege records) — no quality problem.')
    L.append('')

    # 4 homonym / misfit
    L.append('## 4. Homonym & clustering-misfit surfacing')
    L.append('')
    L.append('Genuine flagged meanings (artifacts whose true sense is **not** this cluster):')
    L.append('')
    for r in genuine:
        L.append(f'- {first_sentence(r["finding_value"])}')
    L.append('')
    # tsur-style misfit signature, if present
    sig = q("""SELECT COUNT(*) n FROM finding WHERE cluster_code=? AND provenance='l2_meaning'
               AND finding_value LIKE '%besieg%'""", cl)[0]['n']
    if sig:
        L.append(f'**Clustering-misfit signal:** {sig} meanings carry a military-siege sense '
                 f'(`besiege`). Pure siege is an external act of war with thin inner-being content '
                 f'(affect SILENT). Recommend the researcher adjudicate whether this term belongs in {cl}.')
        L.append('')

    # 5 spot-check pointer
    L.append('## 5. Spot-check')
    L.append('')
    L.append(f'- Random-sample spot-check: `python scripts/_generate_meaning_quality_check.py --cluster {cl}` '
             f'→ `outputs/markdown/{cl}-meaning-quality-check-{today}.md`.')
    L.append(f'- Full meaning export: `python scripts/_generate_verse_meanings_export.py --cluster {cl}` '
             f'→ `outputs/markdown/{cl}-verse-meanings-{today}.md`.')
    L.append('')

    # gate verdict (mechanical only)
    L.append('## 6. Mechanical verdict (not a sign-off)')
    L.append('')
    verdict = []
    verdict.append(('Coverage 100%', pct >= 99.5))
    verdict.append(('Genuine-artifact rate < 2%', gr < 2.0))
    verdict.append(('Type/origin/faculty profiles populated', all(sum(profile[f].values()) for f in ('type', 'origin', 'faculty'))))
    for label, ok in verdict:
        L.append(f'- [{"x" if ok else " "}] {label}')
    L.append('')
    L.append('> Mechanical checks are necessary, not sufficient. Cluster sign-off remains a non-mechanical '
             'researcher judgement (per the analysis rules).')
    L.append('')

    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(L))
    print(f'wrote {out}')
    print(f'  coverage {covered}/{total_tiv} ({pct:.0f}%) · flags {len(flagged)} '
          f'({len(genuine)} genuine / {benign} benign) · l2_api {n_api:,}')


if __name__ == '__main__':
    main()
