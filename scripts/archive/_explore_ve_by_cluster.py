"""
_explore_ve_by_cluster.py — READ-ONLY: VE field x cluster x value comparison across clusters.

For each verse-extraction (VE) field, shows the value distribution per cluster, side by side,
normalised to each cluster's term-in-verse count (clusters differ in size). Uses v_l2_tier.

  CATEGORICAL fields (closed option-list) -> full value distribution.
  MULTI-SELECT (faculty, constitutional_location) -> per-present-value distribution.
  TEXTUAL fields (free text) -> answered vs null-token (SILENT/NONE/not-stated) rate only.

Usage:  python scripts/_explore_ve_by_cluster.py [--clusters M01,M02,M15]
Output: outputs/markdown/ve-by-cluster-<YYYYMMDD>.md   (read-only; no DB writes)
"""
import argparse, os, sqlite3, datetime
from collections import defaultdict

DB = os.path.join('database', 'bible_research.db')

# VE field -> (question_code(s), kind). kind: cat | multi | text
VE = [
    ('type',                   ['T1.2.1'],  'cat'),
    ('compound',               ['T1.2.2'],  'cat'),
    ('origin',                 ['T2.9.1'],  'cat'),
    ('attributed_to_God',      ['T0.1.2'],  'cat'),
    ('typology_direction',     ['T0.4.2'],  'cat'),
    ('literary_setting',       ['T7.2.2'],  'cat'),
    ('faculty',                ['T3.1.1','T3.2.1','T3.3.1','T3.4.1','T3.5.1','T3.6.1',
                                'T3.7.1','T3.8.1','T3.9.1','T3.11.1'], 'multi'),
    ('constitutional_location',['T2.1.1','T2.2.1','T2.3.1','T2.4.1','T2.6.1'], 'multi'),
    ('sense_applied',          ['T7.1.3'],  'text'),
    ('mode',                   ['T1.4.1'],  'text'),
    ('purpose_equips',         ['T0.2.1'],  'text'),
    ('immediate_response',     ['T1.5.1'],  'text'),
    ('produces_effect',        ['T1.6.1'],  'text'),
    ('relational_implication', ['T1.1.3'],  'text'),
]
NULLTOKENS = {'NONE', 'SILENT', 'not-stated', ''}

# normalisers for fields whose values carry free-text tails (bucket to the base form)
def _norm(field, v):
    if field == 'compound':
        return 'simple' if v == 'simple' else 'compound'
    if field == 'literary_setting':
        return v.split(' (')[0].strip() or v
    return v
NORMALISE = {'compound', 'literary_setting'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--clusters', default='M01,M02,M15')
    args = ap.parse_args()
    clusters = [x.strip() for x in args.clusters.split(',')]

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    c = conn.cursor()
    # denominator: term-in-verses per cluster
    denom = {}
    names = {'M01': 'Fear', 'M02': 'Anger', 'M15': 'Wisdom'}
    for cl in clusters:
        denom[cl] = c.execute("SELECT COUNT(*) FROM v_l2_meaning WHERE cluster_code=?", (cl,)).fetchone()[0]

    def pct(n, cl):
        return f'{100*n/denom[cl]:.0f}%' if denom[cl] else '-'

    L = []
    L.append('# Verse-Extraction (VE) fields — value distribution across the three completed clusters')
    L.append('')
    L.append(f'> Read-only. Generated {datetime.date.today().isoformat()}. Source view: v_l2_tier. '
             f'Each cell = count (share of that cluster\'s term-in-verses). '
             f'Denominators: ' + ' · '.join(f'**{cl} ({names.get(cl,cl)}) {denom[cl]}**' for cl in clusters) + '.')
    L.append('')
    L.append('Old-code refs per field are in the restructured catalogue (wa-tier-catalogue-restructured-v1). '
             'CATEGORICAL = full value list; MULTI = per present value; TEXTUAL = answered vs null-token only.')
    L.append('')

    for field, codes, kind in VE:
        L.append(f'## {field}  ({kind})')
        L.append('')
        ph = ','.join('?' * len(codes))
        if kind in ('cat', 'multi'):
            # value -> {cluster: count}
            data = defaultdict(lambda: defaultdict(int))
            if kind == 'cat':
                rows = c.execute(f"""SELECT cluster_code, value, COUNT(*) n FROM v_l2_tier
                    WHERE question_code IN ({ph}) AND cluster_code IN ({','.join('?'*len(clusters))})
                    GROUP BY cluster_code, value""", codes + clusters).fetchall()
            else:  # multi: only ANSWERED present values
                rows = c.execute(f"""SELECT cluster_code, value, COUNT(*) n FROM v_l2_tier
                    WHERE question_code IN ({ph}) AND status='ANSWERED' AND value NOT IN ('NONE','')
                    AND cluster_code IN ({','.join('?'*len(clusters))})
                    GROUP BY cluster_code, value""", codes + clusters).fetchall()
            for r in rows:
                val = _norm(field, r['value']) if field in NORMALISE else r['value']
                data[val][r['cluster_code']] += r['n']
            # order values by total desc
            order = sorted(data, key=lambda v: -sum(data[v].values()))
            L.append('| value | ' + ' | '.join(f'{cl} ({names.get(cl,cl)})' for cl in clusters) + ' |')
            L.append('|---|' + '|'.join(['---'] * len(clusters)) + '|')
            for v in order:
                cells = []
                for cl in clusters:
                    n = data[v].get(cl, 0)
                    cells.append(f'{n} ({pct(n, cl)})' if n else '·')
                L.append(f'| {v} | ' + ' | '.join(cells) + ' |')
            L.append('')
        else:  # text: answered vs null-token
            L.append('| | ' + ' | '.join(f'{cl} ({names.get(cl,cl)})' for cl in clusters) + ' |')
            L.append('|---|' + '|'.join(['---'] * len(clusters)) + '|')
            for label, want_answered in (('answered', True), ('null (SILENT/NONE/not-stated)', False)):
                cells = []
                for cl in clusters:
                    if want_answered:
                        n = c.execute(f"""SELECT COUNT(*) FROM v_l2_tier WHERE question_code IN ({ph})
                            AND cluster_code=? AND status='ANSWERED'
                            AND value NOT IN ('NONE','SILENT','not-stated','')""", codes + [cl]).fetchone()[0]
                    else:
                        n = c.execute(f"""SELECT COUNT(*) FROM v_l2_tier WHERE question_code IN ({ph})
                            AND cluster_code=? AND (status!='ANSWERED'
                            OR value IN ('NONE','SILENT','not-stated',''))""", codes + [cl]).fetchone()[0]
                    cells.append(f'{n} ({pct(n, cl)})')
                L.append(f'| {label} | ' + ' | '.join(cells) + ' |')
            L.append('')

    out = os.path.join('outputs', 'markdown', f've-by-cluster-{datetime.date.today().strftime("%Y%m%d")}.md')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(L))
    print(f'wrote {out}')
    print('  denominators:', {cl: denom[cl] for cl in clusters})


if __name__ == '__main__':
    main()
