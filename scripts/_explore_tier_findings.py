"""
_explore_tier_findings.py — READ-ONLY explorer/export for the L2 verse-read tier findings.

The per-(verse, term) tier data lives in the `finding` table (provenance l2_api), each row
labelled by its observation-catalogue question via finding_question_link. The view `v_l2_tier`
(migration M57) exposes that join. This script makes it browsable:

  WIDE EXPORT (default) — one row per verse-term, columns = the 14 tier fields (faculty/location
      collapsed to comma-lists). Markdown or CSV. Optionally append the meaning paragraph.
        python scripts/_explore_tier_findings.py --cluster M02 [--format md|csv] [--with-meaning]

  FIELD DISTRIBUTION — value counts for one field (slug or question_code):
        python scripts/_explore_tier_findings.py --cluster M02 --field type
        python scripts/_explore_tier_findings.py --cluster M02 --field faculty

  CROSS-TAB — two fields pivoted (single-value fields only):
        python scripts/_explore_tier_findings.py --cluster M02 --crosstab type,attributed_to_God

Omit --cluster to span all clusters. Read-only; no DB writes.
Output (wide export) -> outputs/markdown/<CLUSTER|ALL>-tier-wide-<YYYYMMDD>.(md|csv)
"""
import argparse, os, sqlite3, datetime, csv
from collections import Counter, defaultdict

DB = os.path.join('database', 'bible_research.db')

# question_code -> friendly slug. Single-value fields first; faculty/location are multi-select.
SLUG = {
    'T7.1.3': 'sense_applied', 'T1.2.1': 'type', 'T1.2.2': 'compound', 'T1.4.1': 'mode',
    'T2.9.1': 'origin', 'T0.1.2': 'attributed_to_God', 'T0.2.1': 'purpose_equips',
    'T0.4.2': 'typology_direction', 'T1.5.1': 'immediate_response', 'T1.6.1': 'produces_effect',
    'T1.1.3': 'relational_implication', 'T7.2.2': 'literary_setting',
}
FACULTY_CODES = {'T3.1.1', 'T3.2.1', 'T3.3.1', 'T3.4.1', 'T3.5.1', 'T3.6.1',
                 'T3.7.1', 'T3.8.1', 'T3.9.1', 'T3.11.1'}
LOCATION_CODES = {'T2.1.1', 'T2.2.1', 'T2.3.1', 'T2.4.1', 'T2.6.1'}
# single-value column order for the wide export
COLS = ['sense_applied', 'type', 'compound', 'mode', 'origin', 'attributed_to_God',
        'purpose_equips', 'typology_direction', 'immediate_response', 'produces_effect',
        'relational_implication', 'literary_setting', 'faculty', 'constitutional_location']
SLUG2CODE = {v: k for k, v in SLUG.items()}


def connect():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    return conn


def wide(conn, cluster, fmt, with_meaning):
    c = conn.cursor()
    where = "WHERE cluster_code=?" if cluster else ""
    args = (cluster,) if cluster else ()
    rows = c.execute(f"""SELECT verse_context_id, mti_term_id, cluster_code, verse_ref, term, strongs,
                         question_code, value, status FROM v_l2_tier {where}""", args).fetchall()
    # assemble per (vc, term)
    recs = defaultdict(lambda: {'faculty': [], 'constitutional_location': []})
    meta = {}
    for r in rows:
        key = (r['verse_context_id'], r['mti_term_id'])
        meta[key] = (r['cluster_code'], r['verse_ref'], r['term'], r['strongs'])
        qc, val, st = r['question_code'], r['value'], r['status']
        if qc in FACULTY_CODES:
            if st == 'ANSWERED' and val and val != 'NONE':
                recs[key]['faculty'].append(val)
        elif qc in LOCATION_CODES:
            if st == 'ANSWERED' and val and val != 'NONE':
                recs[key]['constitutional_location'].append(val)
        elif qc in SLUG:
            recs[key][SLUG[qc]] = val
    meanings = {}
    if with_meaning:
        for r in c.execute(f"""SELECT verse_context_id, mti_term_id, meaning FROM v_l2_meaning {where}""", args):
            meanings[(r['verse_context_id'], r['mti_term_id'])] = r['meaning']

    header = ['cluster', 'verse_ref', 'term', 'strongs'] + COLS + (['meaning'] if with_meaning else [])
    out_rows = []
    for key in sorted(meta):
        cc, ref, term, strongs = meta[key]
        rec = recs[key]
        line = [cc, ref, term, strongs]
        for col in COLS:
            v = rec.get(col, '')
            if isinstance(v, list):
                v = ', '.join(v) if v else ''
            line.append(v)
        if with_meaning:
            line.append(meanings.get(key, ''))
        out_rows.append(line)

    today = datetime.date.today().strftime('%Y%m%d')
    tag = cluster or 'ALL'
    ext = 'csv' if fmt == 'csv' else 'md'
    out = os.path.join('outputs', 'markdown', f'{tag}-tier-wide-{today}.{ext}')
    if fmt == 'csv':
        with open(out, 'w', encoding='utf-8', newline='') as fh:
            w = csv.writer(fh); w.writerow(header); w.writerows(out_rows)
    else:
        L = [f'# {tag} — L2 tier findings (wide: one row per verse-term)', '',
             f'> Read-only export. Generated {datetime.date.today().isoformat()}. '
             f'{len(out_rows)} term-in-verses. Source view: v_l2_tier. faculty/location are comma-lists of present values.', '']
        # markdown table (truncate long free-text cells for readability)
        def cell(x):
            x = str(x).replace('|', '\\|').replace('\n', ' ')
            return (x[:60] + '…') if len(x) > 60 else x
        L.append('| ' + ' | '.join(header) + ' |')
        L.append('|' + '|'.join(['---'] * len(header)) + '|')
        for line in out_rows:
            L.append('| ' + ' | '.join(cell(x) for x in line) + ' |')
        with open(out, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(L))
    print(f'wrote {out}  ({len(out_rows)} term-in-verses x {len(header)} columns)')


def field_dist(conn, cluster, field):
    c = conn.cursor()
    code = SLUG2CODE.get(field, field)
    codes = (FACULTY_CODES if field == 'faculty' else
             LOCATION_CODES if field in ('constitutional_location', 'location') else {code})
    where = "WHERE question_code IN (%s)" % ','.join('?' * len(codes))
    args = list(codes)
    if cluster:
        where += " AND cluster_code=?"; args.append(cluster)
    rows = c.execute(f"""SELECT value, COUNT(*) n FROM v_l2_tier {where} AND status='ANSWERED'
                         GROUP BY value ORDER BY n DESC""", args).fetchall()
    tot = sum(r['n'] for r in rows)
    print(f"\nField '{field}'  ({'cluster '+cluster if cluster else 'ALL clusters'})  — {tot} answered values")
    for r in rows:
        print(f"  {r['n']:6}  {100*r['n']/tot:5.1f}%  {r['value']}")


def crosstab(conn, cluster, spec):
    a, b = [s.strip() for s in spec.split(',')]
    ca, cb = SLUG2CODE.get(a, a), SLUG2CODE.get(b, b)
    c = conn.cursor()
    where = "WHERE question_id IS NOT NULL"
    args = []
    extra = " AND cluster_code=?" if cluster else ""
    if cluster: args = [cluster]
    rows = c.execute(f"""
        SELECT verse_context_id vc, mti_term_id mid,
               MAX(CASE WHEN question_code=? THEN value END) AS a,
               MAX(CASE WHEN question_code=? THEN value END) AS b
        FROM v_l2_tier WHERE question_code IN (?,?){extra}
        GROUP BY verse_context_id, mti_term_id""",
        [ca, cb, ca, cb] + args).fetchall()
    ct = Counter((r['a'], r['b']) for r in rows if r['a'] is not None and r['b'] is not None)
    print(f"\nCross-tab {a} x {b}  ({'cluster '+cluster if cluster else 'ALL'})  — {len(rows)} term-in-verses")
    print(f"  {a:18} {b:18} count")
    for (va, vb), n in ct.most_common():
        print(f"  {str(va):18} {str(vb):18} {n}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cluster')
    ap.add_argument('--format', choices=['md', 'csv'], default='md')
    ap.add_argument('--with-meaning', action='store_true')
    ap.add_argument('--field')
    ap.add_argument('--crosstab')
    args = ap.parse_args()
    conn = connect()
    if args.field:
        field_dist(conn, args.cluster, args.field)
    elif args.crosstab:
        crosstab(conn, args.cluster, args.crosstab)
    else:
        wide(conn, args.cluster, args.format, args.with_meaning)


if __name__ == '__main__':
    main()
