"""
_explore_drop_code_findings.py — READ-ONLY extract of every finding referencing the §3 DROP tier codes.

DROP families (catalogue restructured v2 §3): T1.2.3 best-description · T1.8 Dimension Classification ·
T2.8 Body-Deposit (DNA/generational) · T5.7 Deposit Consequence · T6.6 Shared Verse Anchors · T6.7
Dimensional Sharing. Reports by cluster, both sources:
  - cluster_finding (obs_id) — cluster-level findings
  - wa_session_b_findings via wa_finding_catalogue_links (question_id) — Session B findings
The L2 verse-read (finding_question_link) references these = 0 (they are characteristic/synthesis-level).

Usage:  python scripts/_explore_drop_code_findings.py
Output: outputs/markdown/drop-code-findings-extract-<YYYYMMDD>.md   (+ .csv for filtering). Read-only.
"""
import os, sqlite3, datetime, csv
from collections import defaultdict, Counter

DB = os.path.join('database', 'bible_research.db')

FAMILIES = [
    ('T1.2.3', 'Best working description', [241]),
    ('T1.8',   'Dimension Classification', [257, 258, 259]),
    ('T2.8',   'Body-Deposit (DNA / generational)', [282, 283, 284]),
    ('T5.7',   'Deposit Consequence', [366, 367, 368]),
    ('T6.6',   'Shared Verse Anchors', [387, 388, 389]),
    ('T6.7',   'Dimensional Sharing', [390, 391, 392]),
]
OBS2CODE = {}
OBS2FAM = {}
for fam, _t, olist in FAMILIES:
    for i, o in enumerate(olist, 1):
        OBS2CODE[o] = f'{fam}.{i}' if fam != 'T1.2.3' else 'T1.2.3'
        OBS2FAM[o] = fam
ALL_OBS = [o for _f, _t, ol in FAMILIES for o in ol]


def clean(t):
    return (t or '').replace('\r', ' ').replace('\n', ' ').replace('|', '\\|').strip()


def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    c = conn.cursor()
    ph = ','.join('?' * len(ALL_OBS))

    # registry -> cluster
    reg2cl = {r['no']: r['cluster_assignment'] for r in
              c.execute("SELECT no, cluster_assignment FROM word_registry")}

    rows = []  # dict per finding occurrence
    # --- source 1: cluster_finding ---
    for r in c.execute(f"""SELECT obs_id, cluster_code, finding_type, finding_status, needs_research,
                           finding_text FROM cluster_finding
                           WHERE obs_id IN ({ph}) AND delete_flagged=0
                           ORDER BY cluster_code, obs_id""", ALL_OBS):
        rows.append(dict(source='cluster_finding', cluster=r['cluster_code'] or '?',
                         code=OBS2CODE.get(r['obs_id'], '?'), fam=OBS2FAM.get(r['obs_id']),
                         ftype=r['finding_type'] or '', status=r['finding_status'] or '',
                         needs_research=r['needs_research'], text=r['finding_text'] or ''))
    # --- source 2: Session B findings via catalogue links ---
    for r in c.execute(f"""SELECT DISTINCT sb.id, sb.registry_id, sb.finding_type, sb.status,
                           sb.finding, sb.anchor_verses, l.question_id
                           FROM wa_finding_catalogue_links l
                           JOIN wa_session_b_findings sb ON sb.id = l.finding_id
                           WHERE l.question_id IN ({ph}) AND sb.delete_flag=0""", ALL_OBS):
        rows.append(dict(source='session_b', cluster=reg2cl.get(r['registry_id'], '?'),
                         code=OBS2CODE.get(r['question_id'], '?'), fam=OBS2FAM.get(r['question_id']),
                         ftype=r['finding_type'] or '', status=r['status'] or '',
                         needs_research='', text=(r['finding'] or '') +
                         (f"  [anchors: {r['anchor_verses']}]" if r['anchor_verses'] else '')))

    # ---- build report ----
    today = datetime.date.today()
    by_cluster = defaultdict(list)
    for r in rows:
        by_cluster[r['cluster']].append(r)
    fam_titles = {f: t for f, t, _ in FAMILIES}

    # summary matrix: cluster x family
    clusters = sorted(by_cluster)
    fam_order = [f for f, _, _ in FAMILIES]
    L = []
    L.append('# DROP-code findings — full extract by cluster')
    L.append('')
    L.append(f'> Read-only. Generated {today.isoformat()}. Every active finding referencing a §3 **DROP** tier code '
             f'(catalogue restructured v2). Sources: `cluster_finding` (obs_id) + `wa_session_b_findings` via '
             f'`wa_finding_catalogue_links`. The L2 verse-read (`finding_question_link`) references these codes **0 times** '
             f'— they are characteristic/synthesis-level, never written at the verse. **Total occurrences: {len(rows)}** '
             f'across {len(clusters)} clusters. This is what the DROP would retire/relabel.')
    L.append('')
    L.append('## Summary — occurrences by cluster × DROP family')
    L.append('')
    L.append('| cluster | ' + ' | '.join(f'{f}' for f in fam_order) + ' | **total** |')
    L.append('|---|' + '|'.join(['---'] * (len(fam_order) + 1)) + '|')
    fam_tot = Counter()
    for cl in clusters:
        cnt = Counter(r['fam'] for r in by_cluster[cl])
        for f in fam_order:
            fam_tot[f] += cnt.get(f, 0)
        L.append(f'| **{cl}** | ' + ' | '.join(str(cnt.get(f, 0) or '·') for f in fam_order) +
                 f' | **{len(by_cluster[cl])}** |')
    L.append('| **total** | ' + ' | '.join(f'**{fam_tot[f]}**' for f in fam_order) + f' | **{len(rows)}** |')
    L.append('')
    L.append('Family key: ' + ' · '.join(f'**{f}** {fam_titles[f]}' for f in fam_order))
    L.append('')
    L.append('---')
    L.append('')

    # full extract by cluster -> family -> findings
    L.append('## Full extract')
    L.append('')
    for cl in clusters:
        L.append(f'### {cl}  ({len(by_cluster[cl])} findings)')
        L.append('')
        crows = by_cluster[cl]
        for f in fam_order:
            frows = [r for r in crows if r['fam'] == f]
            if not frows:
                continue
            L.append(f'**{f} · {fam_titles[f]}**  ({len(frows)})')
            L.append('')
            for r in frows:
                tag = f"`{r['code']}` · {r['source']} · {r['ftype']}/{r['status']}"
                nr = ' · needs_research' if r['needs_research'] else ''
                L.append(f'- {tag}{nr} — {clean(r["text"])}')
            L.append('')
        L.append('')

    out = os.path.join('outputs', 'markdown', f'drop-code-findings-extract-{today.strftime("%Y%m%d")}.md')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(L))
    # csv for filtering
    out_csv = os.path.join('outputs', 'markdown', f'drop-code-findings-extract-{today.strftime("%Y%m%d")}.csv')
    with open(out_csv, 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['cluster', 'drop_family', 'code', 'source', 'finding_type', 'status', 'needs_research', 'text'])
        for r in sorted(rows, key=lambda x: (x['cluster'], x['fam'], x['code'])):
            w.writerow([r['cluster'], r['fam'], r['code'], r['source'], r['ftype'], r['status'],
                        r['needs_research'], clean(r['text'])])
    print(f'wrote {out}')
    print(f'wrote {out_csv}')
    print(f'  {len(rows)} occurrences across {len(clusters)} clusters; by family: ' +
          ', '.join(f'{f}={fam_tot[f]}' for f in fam_order))


if __name__ == '__main__':
    main()
