"""#1978, 2026-10-06: pull the M64 x M47 shared verses NOT cited in the narrative, for the researcher
to examine. Read-only.

For each uncited verse it adds `same_pair_cited`: other verses anywhere in iba.db that hold the SAME
M64 Strong's together with the SAME M47 Strong's and ARE cited in the narrative, with their places.
This is a word-pair match only, offered as a lead for "is a similar verse already cited?". It says
nothing about whether the verses say the same thing. That judgement is the researcher's.

Usage: python m64-m47-uncited-pull-v1-20261006.py
"""
import csv, importlib.util, os, re, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
IN = os.path.join(HERE, 'm64-m47-shared-verses-v2-20261006.csv')
OUT_CSV = os.path.join(HERE, 'm64-m47-uncited-verses-v1-20261006.csv')
OUT_MD = os.path.join(HERE, 'm64-m47-uncited-verses-v1-20261006.md')

spec = importlib.util.spec_from_file_location('xref', os.path.join(HERE, 'verse-narrative-ot-crossref-v2-20261006.py'))
xref = importlib.util.module_from_spec(spec)
spec.loader.exec_module(xref)


def strongs(words):
    return sorted({w.split(' ')[0] for w in words.split(' | ')})


def main():
    narr = xref.narrative_index()
    con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
    rows = [r for r in csv.DictReader(open(IN, encoding='utf-8-sig')) if r['narrative_n'] == '0']
    pair_sql = """
        SELECT DISTINCT v.reference FROM verse v
        JOIN verse_lexical a ON a.verse_id = v.id AND a.deleted = 0 AND a.strong = ?
        JOIN verse_lexical b ON b.verse_id = v.id AND b.deleted = 0 AND b.strong = ?
        WHERE v.deleted = 0"""
    out = []
    for r in rows:
        leads = []
        for s64 in strongs(r['m64_words']):
            for s47 in strongs(r['m47_words']):
                refs = [x[0] for x in con.execute(pair_sql, (s64, s47))]
                cited = [x for x in refs if x != r['reference'] and narr.get(xref.ref_key(x))]
                for x in cited:
                    places = narr[xref.ref_key(x)]
                    leads.append(f'{s64}+{s47}: {x} [{"; ".join(places)}]')
                r.setdefault('pair_counts', []).append(f'{s64}+{s47}: {len(refs)} verses, {len(cited)} cited')
        r['same_pair_verses'] = ' | '.join(r.pop('pair_counts'))
        r['same_pair_cited'] = ' | '.join(leads)
        out.append(r)
    cols = ['reference', 'm64_hits', 'm64_words', 'm47_hits', 'm47_words', 'same_pair_verses', 'same_pair_cited', 'esv_text']
    with open(OUT_CSV, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(out)

    def words(s):
        return '; '.join(re.sub(r' @\d+$', '', x) for x in s.split(' | '))
    with_lead = sum(1 for r in out if r['same_pair_cited'])
    L = ['# M64 × M47 shared verses not cited in the narrative', '',
         '**Date:** 2026-10-06 · **Escalation:** #1978 · **Status:** for the researcher to examine. No reading or judgement has been made.', '',
         f'There are **{len(out)} verses**. They are the uncited rows of [`m64-m47-shared-verses-v2-20261006.csv`](m64-m47-shared-verses-v2-20261006.csv), shown in canonical order.',
         f'The same rows are in [`m64-m47-uncited-verses-v1-20261006.csv`](m64-m47-uncited-verses-v1-20261006.csv). They were built by [`m64-m47-uncited-pull-v1-20261006.py`](m64-m47-uncited-pull-v1-20261006.py), which is read-only.', '',
         '**About "Same word pair, cited elsewhere".** This lists other verses that hold the **same M64 Strong\'s and the same M47 Strong\'s** and **are** cited in the narrative, with where they are cited.',
         '- It is a word-pair match only, offered as a lead for your question "is a similar verse already cited?".',
         '- It does not say the verses mean the same thing.',
         f'- {with_lead} of the {len(out)} verses have at least one such lead. The other {len(out) - with_lead} have none: no verse with that exact word pair is cited anywhere in the narrative.',
         '- "x verses, y cited" counts every verse in iba.db with that word pair, the verse itself included.', '']
    for r in out:
        L.append(f"## {r['reference']}")
        L.append('')
        L.append(f"> {r['esv_text']}")
        L.append('')
        L.append(f"- **M64:** {words(r['m64_words'])}")
        L.append(f"- **M47:** {words(r['m47_words'])}")
        L.append(f"- **Word pair:** {'; '.join(r['same_pair_verses'].split(' | '))}")
        if r['same_pair_cited']:
            L.append('- **Same word pair, cited elsewhere:**')
            for lead in r['same_pair_cited'].split(' | '):
                L.append(f'  - {lead}')
        else:
            L.append('- **Same word pair, cited elsewhere:** none')
        L.append('')
    open(OUT_MD, 'w', encoding='utf-8').write('\n'.join(L))
    print(f'{len(out)} verses; {with_lead} with a same-pair cited lead')


if __name__ == '__main__':
    main()
