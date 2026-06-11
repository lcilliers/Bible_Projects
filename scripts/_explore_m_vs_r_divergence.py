"""
_explore_m_vs_r_divergence.py — READ-ONLY. For VE-01 (obs 395), compare the MECHANICAL term-gloss (M)
against the verse-specific READ sense (R) for every term-in-verse that has BOTH, and isolate those where
R lands MATERIALLY OUTSIDE the M lexical range.

M = l2_mechanical finding_value (the term's lexical gloss range, constant per term; may have >1 sense-branch).
R = l2_api finding_value (the verse-specific applied sense, one per verse-occurrence).

Method (crude, navigation-only — NOT validation; read the actual content for anything that matters):
  - content-stem each side: lowercase, drop stopwords/short words, truncate each word to a 5-char stem.
  - overlap = |R_stems INTERSECT M_stems| / |R_stems|.
  - MATERIAL when overlap below threshold: bucket ZERO (no shared stem) and LOW (<0.25).

Usage:  python scripts/_explore_m_vs_r_divergence.py [--threshold 0.25]
Output: outputs/markdown/m-vs-r-divergence-<YYYYMMDD>.md  (+ .csv). Read-only.
"""
import os, sqlite3, datetime, csv, argparse, re
from collections import defaultdict

DB = os.path.join('database', 'bible_research.db')
OBS = 395

STOP = set('''a an the and or but to be is are was were of in on at by for with as from into onto
  that this these those it its his her their our your my one some any all no not nor so such than then
  who whom which what when where why how do does did done being been have has had will would can could
  may might must shall should about over under up down out off through e g eg ie etc'''.split())


def stems(text):
    """content stems: drop stopwords/short, truncate to 5-char crude stem."""
    out = set()
    for w in re.split(r'[^a-z]+', (text or '').lower()):
        if len(w) < 3 or w in STOP:
            continue
        out.add(w[:5])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--threshold', type=float, default=0.25)
    args = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # M: union of mechanical gloss(es) per term -> stem set
    mech = defaultdict(set)          # mid -> stem set
    mech_text = defaultdict(set)     # mid -> raw gloss variants
    for r in c.execute(f"""SELECT f.mti_term_id mid, f.finding_value v FROM finding f
        JOIN finding_question_link l ON l.finding_id=f.id
        WHERE l.question_id={OBS} AND f.provenance='l2_mechanical' AND f.delete_flagged=0"""):
        mech[r['mid']] |= stems(r['v'])
        mech_text[r['mid']].add((r['v'] or '').strip())

    # R: each api finding (one per verse-occurrence)
    apis = list(c.execute(f"""SELECT f.id fid, f.verse_context_id vcid, f.mti_term_id mid,
        f.finding_value v, f.cluster_code cl, f.flagged_for_review fr,
        mt.transliteration tr, mt.strongs_number sn, vr.reference ref
        FROM finding f
        JOIN finding_question_link l ON l.finding_id=f.id
        JOIN mti_terms mt ON mt.id=f.mti_term_id
        LEFT JOIN verse_context vc ON vc.id=f.verse_context_id
        LEFT JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
        WHERE l.question_id={OBS} AND f.provenance='l2_api' AND f.delete_flagged=0"""))

    both = 0
    flagged = []   # (overlap, bucket, row)
    for r in apis:
        mid = r['mid']
        if mid not in mech:
            continue   # no M for this term -> not a 'both', skip
        both += 1
        rs = stems(r['v'])
        if not rs:
            continue
        inter = rs & mech[mid]
        ov = len(inter) / len(rs)
        if ov == 0:
            bucket = 'ZERO'
        elif ov < args.threshold:
            bucket = 'LOW'
        else:
            continue
        flagged.append((ov, bucket, r, sorted(inter)))

    flagged.sort(key=lambda x: (x[0], x[2]['cl'] or '', x[2]['tr'] or ''))

    today = datetime.date.today()
    zero = [f for f in flagged if f[1] == 'ZERO']
    low = [f for f in flagged if f[1] == 'LOW']

    # by cluster / by term tallies
    by_cluster = defaultdict(int); by_term = defaultdict(int)
    for ov, bk, r, inter in flagged:
        by_cluster[r['cl'] or '?'] += 1
        by_term[(r['cl'] or '?', r['tr'], r['sn'])] += 1

    L = []
    L.append('# VE-01 (obs 395) — M vs R divergence: where the read lands outside the lexical range')
    L.append('')
    L.append(f'> Read-only. Generated {today.isoformat()}. **M** = mechanical term-gloss (lexical range). '
             f'**R** = verse-specific read sense. Compared for **{both}** term-in-verses that have BOTH. '
             f'Crude 5-char-stem overlap; threshold {args.threshold}. '
             f'**Material divergence: {len(flagged)}** ({len(zero)} ZERO-overlap, {len(low)} LOW). '
             f'This NAVIGATES to candidates — it does NOT validate. Read the verse + both values before judging '
             f'(metaphor / extended sense / homonym / too-narrow gloss / read error all live here).')
    L.append('')
    L.append('## By cluster')
    L.append('')
    L.append('| cluster | material | ')
    L.append('|---|---|')
    for cl, n in sorted(by_cluster.items(), key=lambda x: -x[1]):
        L.append(f'| {cl} | {n} |')
    L.append('')
    L.append('## Top terms (by material count)')
    L.append('')
    L.append('| cluster | term | strongs | material |')
    L.append('|---|---|---|---|')
    for (cl, tr, sn), n in sorted(by_term.items(), key=lambda x: -x[1])[:30]:
        L.append(f'| {cl} | {tr} | {sn} | {n} |')
    L.append('')
    L.append('---')
    L.append('')

    def block(title, items):
        L.append(f'## {title}  ({len(items)})')
        L.append('')
        for ov, bk, r, inter in items:
            mtexts = ' /// '.join(sorted(mech_text[r['mid']]))
            L.append(f"### {r['ref'] or '?'} — {r['tr']} ({r['sn']}) · {r['cl']}"
                     + ('  ⚑flagged' if r['fr'] else ''))
            L.append(f"- **R (read):** {r['v']}")
            L.append(f"- **M (lexical):** {mtexts}")
            L.append(f"- overlap {ov:.2f}" + (f"  shared-stems: {inter}" if inter else "  (no shared stem)"))
            L.append('')

    block('ZERO-overlap — R shares no lexical stem with M', zero)
    L.append('---')
    L.append('')
    block('LOW-overlap', low)

    out = os.path.join('outputs', 'markdown', f'm-vs-r-divergence-{today.strftime("%Y%m%d")}.md')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(L))
    out_csv = os.path.join('outputs', 'markdown', f'm-vs-r-divergence-{today.strftime("%Y%m%d")}.csv')
    with open(out_csv, 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['cluster', 'verse', 'term', 'strongs', 'bucket', 'overlap', 'R_read', 'M_lexical', 'flagged'])
        for ov, bk, r, inter in flagged:
            w.writerow([r['cl'], r['ref'], r['tr'], r['sn'], bk, f'{ov:.2f}', r['v'],
                        ' /// '.join(sorted(mech_text[r['mid']])), r['fr']])
    print(f'both (M+R) compared : {both}')
    print(f'material divergence : {len(flagged)}  (ZERO {len(zero)}, LOW {len(low)})')
    print('by cluster:', dict(sorted(by_cluster.items(), key=lambda x: -x[1])))
    print(f'wrote {out}')
    print(f'wrote {out_csv}')


if __name__ == '__main__':
    main()
