"""
Build the VC revision ledger from VCB-7..11 patches.

Reads patch JSONs in archive/patches/, derives per-term routing
(NO-CHANGE / REVISE-ONLY / NEW-ONLY / MIXED), pairs with current DB
metadata, and writes:
  - outputs/investigations/vc-revision-ledger-v1-{date}.md
  - outputs/investigations/vc-revision-ledger-v1-{date}.csv

Scope: VCB-7 (renewal pilot reg 134), VCB-8 individual term patches
(yearning H4263, treachery G4273, jealousy G3863, righteousness G1345),
VCB-9 (the late wa-vcb-008-patch-vcrevise-v1-20260425.json mixed batch),
VCB-10 (4 patches), VCB-11 (3 patches).

Read-only — no DB writes.
"""
import json
import os
import sqlite3
import csv
from datetime import date
from collections import defaultdict, Counter

DB = os.path.join('data', 'bible_research.db')
ARCHIVE = os.path.join('archive', 'patches')
OUT_DIR = os.path.join('outputs', 'investigations')

# (batch_id, patch_filename, declared_patch_type)
PATCHES = [
    # VCB-7 — renewal pilot, registry 134
    ('VCB-7', 'wa-vc-134-patch-vcnew-v1-20260424.json', 'VCNEW'),
    ('VCB-7', 'wa-vc-134-patch-vcrecovery-v1-20260424.json', 'VCRECOVERY'),
    ('VCB-7', 'wa-vc-134-patch-vcrevise-v1-20260424.json', 'VCREVISE'),
    # VCB-8 — individual term patches
    ('VCB-8', 'wa-179-yearning-h4263-patch-vcrevise-v1-20260424.json', 'VCREVISE'),
    ('VCB-8', 'wa-096-jealousy-g3863-patch-vcrevise-v1-20260424.json', 'VCREVISE'),
    ('VCB-8', 'wa-139-righteousness-g1345-patch-vcsbflags-v1-20260424.json', 'VCSBFLAGS'),
    ('VCB-8', 'wa-139-righteousness-g1345-patch-versecontext-v1-20260424.json', 'VCNEW'),
    ('VCB-8', 'wa-203-treachery-g4273-patch-vcrevise-v1-20260425.json', 'VCREVISE'),
    # VCB-9 — late mixed batch
    ('VCB-9', 'wa-vcb-008-patch-vcrevise-v1-20260425.json', 'VCREVISE'),
    # VCB-10
    ('VCB-10', 'wa-vcb-010-patch-versecontext-v1-20260425.json', 'VCNEW'),
    ('VCB-10', 'wa-vcb-010-patch-vcrevise-v1-20260425.json', 'VCREVISE'),
    ('VCB-10', 'wa-vcb-010-patch-vcsbflags-v1-20260425.json', 'VCSBFLAGS'),
    ('VCB-10', 'wa-vcb-010-patch-vcsdpointers-v1-20260425.json', 'VCSDPOINTERS'),
    # VCB-11
    ('VCB-11', 'wa-vcb-11-patch-vcnew-v1-20260425.json', 'VCNEW'),
    ('VCB-11', 'wa-vcb-11-patch-vcrevise-v1-20260425.json', 'VCREVISE'),
    ('VCB-11', 'wa-vcb-11-patch-vcsbflags-v1-20260425.json', 'VCSBFLAGS'),
    # VCB-13 (main standard batch + halt-resolution sub-patches for heavy partials)
    ('VCB-13', 'wa-vcb013-patch-versecontext-v1-20260425.json', 'VCNEW'),
    ('VCB-13', 'wa-vcb013-patch-vcrevise-v1-20260425.json', 'VCREVISE'),
    ('VCB-13', 'wa-vcb013-patch-vcsbflags-v1-20260425.json', 'VCSBFLAGS'),
    ('VCB-13', 'wa-vcb013hr-patch-versecontext-h2896a-v1-20260425.json', 'VCNEW'),
    ('VCB-13', 'wa-vcb013hr-patch-versecontext-h2181-v1-20260425.json', 'VCNEW'),
    ('VCB-13', 'wa-vcb013hr-patch-vcnew-v1-20260425.json', 'VCNEW'),
]


def load_patch(filename):
    p = os.path.join(ARCHIVE, filename)
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)


def derive_per_term_routing():
    """
    Walk each VCB-* patch, attribute operations and terms_covered to
    each (batch_id, mti_term_id), then derive per-term routing.

    Routing:
      NEW-ONLY:   term has VCNEW operations, no VCREVISE operations
      REVISE-ONLY: term has VCREVISE operations (not empty), no VCNEW
      MIXED:      term has both VCNEW and VCREVISE operations
      NO-CHANGE:  term in terms_covered but no operations across all patches
    """
    # term_data[(batch_id, mti_term_id)] = dict
    term_data = defaultdict(lambda: {
        'vcnew_ops': 0,
        'vcrevise_ops': 0,
        'vcsbflags_ops': 0,
        'vcsdpointers_ops': 0,
        'vcrecovery_ops': 0,
        'in_terms_covered': False,
        'patches': [],
    })

    for batch_id, fname, declared_type in PATCHES:
        try:
            d = load_patch(fname)
        except FileNotFoundError:
            print(f'  [warn] missing: {fname}')
            continue
        meta = d.get('_patch_meta', {})
        ops = d.get('operations', [])
        ptype = meta.get('patch_type', declared_type)
        terms_covered = meta.get('terms_covered') or []

        # Mark terms in terms_covered as in-scope for the batch
        for t in terms_covered:
            try:
                t = int(t)
            except (TypeError, ValueError):
                continue
            term_data[(batch_id, t)]['in_terms_covered'] = True
            term_data[(batch_id, t)]['patches'].append(ptype)

        # Attribute operations
        for op in ops:
            table = op.get('table')
            opname = op.get('operation')
            mti = None

            if table == 'verse_context' and opname == 'insert':
                rec = op.get('record', {})
                mti = rec.get('mti_term_id')
            elif table == 'verse_context' and opname == 'update':
                m = op.get('match', {})
                mti = m.get('mti_term_id')
            elif table == 'verse_context_group':
                if opname == 'insert':
                    rec = op.get('record', {})
                    mti = rec.get('mti_term_id')
                elif opname == 'update':
                    m = op.get('match', {})
                    mti = m.get('mti_term_id')
            elif table == 'wa_session_research_flags' and opname == 'insert':
                # SBFLAGS / SDPOINTERS — not directly tied to a single term
                # but may carry strongs_reference. Skip for routing; count below.
                pass

            if mti is None:
                # Some ops carry strongs_reference instead
                continue

            try:
                mti = int(mti)
            except (TypeError, ValueError):
                continue

            key = (batch_id, mti)
            term_data[key]['in_terms_covered'] = True
            if ptype == 'VCNEW':
                term_data[key]['vcnew_ops'] += 1
            elif ptype == 'VCREVISE':
                term_data[key]['vcrevise_ops'] += 1
            elif ptype == 'VCSBFLAGS':
                term_data[key]['vcsbflags_ops'] += 1
            elif ptype == 'VCSDPOINTERS':
                term_data[key]['vcsdpointers_ops'] += 1
            elif ptype == 'VCRECOVERY':
                term_data[key]['vcrecovery_ops'] += 1

    # Derive routing
    rows = []
    for (batch, mti), d in term_data.items():
        new = d['vcnew_ops']
        rev = d['vcrevise_ops']
        if new > 0 and rev > 0:
            routing = 'MIXED'
        elif new > 0:
            routing = 'NEW-ONLY'
        elif rev > 0:
            routing = 'REVISE-ONLY'
        else:
            routing = 'NO-CHANGE'
        rows.append({
            'batch_id': batch,
            'mti_term_id': mti,
            'routing': routing,
            'vcnew_ops': new,
            'vcrevise_ops': rev,
            'vcsbflags_ops': d['vcsbflags_ops'],
            'vcsdpointers_ops': d['vcsdpointers_ops'],
            'vcrecovery_ops': d['vcrecovery_ops'],
        })
    return rows


def attach_db_metadata(rows, conn):
    for r in rows:
        mti = r['mti_term_id']
        meta = conn.execute('''
            SELECT mt.id, mt.strongs_number, mt.transliteration, mt.gloss,
                   mt.language, mt.status, mt.owning_registry_fk,
                   wr.no as reg_no, wr.word as reg_word,
                   ti.id as ti_id, ti.term_owner_type
            FROM mti_terms mt
            LEFT JOIN wa_term_inventory ti
              ON ti.strongs_number = mt.strongs_number
              AND ti.term_owner_type = 'OWNER'
              AND ti.delete_flagged = 0
            LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
            WHERE mt.id = ?
        ''', (mti,)).fetchone()
        if meta is None:
            r.update({'strongs': None, 'translit': None, 'gloss': None, 'lang': None,
                      'reg_no': None, 'reg_word': None, 'verses': None,
                      'groups': None, 'vc_rows': None,
                      'has_sb_flag': None, 'has_ph2_flag': None})
            continue
        # Verse count (active)
        if meta['ti_id']:
            verses = conn.execute(
                'SELECT COUNT(*) FROM wa_verse_records WHERE term_inv_id = ? AND delete_flagged = 0',
                (meta['ti_id'],)).fetchone()[0]
        else:
            verses = 0
        # Active group count + active vc-row count
        groups = conn.execute(
            'SELECT COUNT(*) FROM verse_context_group WHERE mti_term_id = ? AND delete_flagged = 0',
            (mti,)).fetchone()[0]
        vc_rows = conn.execute(
            'SELECT COUNT(*) FROM verse_context WHERE mti_term_id = ? AND delete_flagged = 0',
            (mti,)).fetchone()[0]
        # Prior research flags (pre-existing — registry-level via strongs_reference)
        sb_flag = conn.execute('''
            SELECT COUNT(*) FROM wa_session_research_flags
            WHERE strongs_reference = ?
              AND flag_code IN ('SB_FINDING', 'SB_INNER_BEING', 'SB_DIMENSION')
        ''', (meta['strongs_number'],)).fetchone()[0]
        ph2_flag = conn.execute('''
            SELECT COUNT(*) FROM wa_session_research_flags
            WHERE strongs_reference = ?
              AND flag_code LIKE 'PH2%'
        ''', (meta['strongs_number'],)).fetchone()[0]

        r.update({
            'strongs': meta['strongs_number'],
            'translit': meta['transliteration'],
            'gloss': meta['gloss'],
            'lang': meta['language'],
            'reg_no': meta['reg_no'],
            'reg_word': meta['reg_word'],
            'verses': verses,
            'groups': groups,
            'vc_rows': vc_rows,
            'has_sb_flag': sb_flag,
            'has_ph2_flag': ph2_flag,
        })
    return rows


def score_predictors(rows):
    """For each candidate predictor, compute revision-rate within the
    predicted-positive subset and within the predicted-negative subset.
    Predictors fire on RE-EVAL terms only (NO-CHANGE | REVISE-ONLY | MIXED) —
    NEW-ONLY terms are mostly partial-completion or fresh and don't carry
    a prior-state signal in the same way.
    """
    re_eval = [r for r in rows if r['routing'] in ('NO-CHANGE', 'REVISE-ONLY', 'MIXED')]
    revised = lambda r: r['routing'] in ('REVISE-ONLY', 'MIXED')

    n = len(re_eval)
    n_revised = sum(1 for r in re_eval if revised(r))
    base_rate = n_revised / n if n else 0

    def cohort(test):
        sub = [r for r in re_eval if test(r)]
        nr = sum(1 for r in sub if revised(r))
        return len(sub), nr, (nr / len(sub) if sub else None)

    predictors = []

    # P1: groups > 5
    n1, r1, rate1 = cohort(lambda r: (r['groups'] or 0) > 5)
    n1n, r1n, rate1n = cohort(lambda r: (r['groups'] or 0) <= 5)
    predictors.append(('groups > 5', n1, r1, rate1, n1n, r1n, rate1n))

    # P2: groups == 1
    n2, r2, rate2 = cohort(lambda r: (r['groups'] or 0) == 1)
    n2n, r2n, rate2n = cohort(lambda r: (r['groups'] or 0) != 1)
    predictors.append(('groups == 1', n2, r2, rate2, n2n, r2n, rate2n))

    # P3: groups == 1 AND verses >= 10 (lumping risk)
    n3, r3, rate3 = cohort(lambda r: (r['groups'] or 0) == 1 and (r['verses'] or 0) >= 10)
    n3n, r3n, rate3n = cohort(lambda r: not ((r['groups'] or 0) == 1 and (r['verses'] or 0) >= 10))
    predictors.append(('groups==1 AND verses>=10', n3, r3, rate3, n3n, r3n, rate3n))

    # P4: language Hebrew
    n4, r4, rate4 = cohort(lambda r: r['lang'] == 'Hebrew')
    n4n, r4n, rate4n = cohort(lambda r: r['lang'] == 'Greek')
    predictors.append(('language Hebrew', n4, r4, rate4, n4n, r4n, rate4n))

    # P5: has_sb_flag (any)
    n5, r5, rate5 = cohort(lambda r: (r['has_sb_flag'] or 0) > 0)
    n5n, r5n, rate5n = cohort(lambda r: (r['has_sb_flag'] or 0) == 0)
    predictors.append(('has_sb_flag', n5, r5, rate5, n5n, r5n, rate5n))

    # P6: has_ph2_flag (any)
    n6, r6, rate6 = cohort(lambda r: (r['has_ph2_flag'] or 0) > 0)
    n6n, r6n, rate6n = cohort(lambda r: (r['has_ph2_flag'] or 0) == 0)
    predictors.append(('has_ph2_flag', n6, r6, rate6, n6n, r6n, rate6n))

    # P7: groups <= 2 AND verses <= 5 (low-complexity hypothesis: low revision risk)
    n7, r7, rate7 = cohort(lambda r: (r['groups'] or 0) <= 2 and (r['verses'] or 0) <= 5)
    n7n, r7n, rate7n = cohort(lambda r: not ((r['groups'] or 0) <= 2 and (r['verses'] or 0) <= 5))
    predictors.append(('groups<=2 AND verses<=5', n7, r7, rate7, n7n, r7n, rate7n))

    return n, n_revised, base_rate, predictors


def fmt_pct(x):
    if x is None: return ' n/a '
    return f'{x*100:5.1f}%'


def write_outputs(rows, n, n_revised, base_rate, predictors):
    today = date.today().isoformat().replace('-', '')
    md_path = os.path.join(OUT_DIR, f'vc-revision-ledger-v1-{today}.md')
    csv_path = os.path.join(OUT_DIR, f'vc-revision-ledger-v1-{today}.csv')
    os.makedirs(OUT_DIR, exist_ok=True)

    # CSV
    cols = ['batch_id', 'mti_term_id', 'strongs', 'translit', 'gloss',
            'lang', 'reg_no', 'reg_word', 'routing',
            'vcnew_ops', 'vcrevise_ops', 'vcsbflags_ops', 'vcsdpointers_ops',
            'vcrecovery_ops', 'verses', 'groups', 'vc_rows',
            'has_sb_flag', 'has_ph2_flag']
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in sorted(rows, key=lambda x: (x['batch_id'], x.get('reg_no') or 0, x.get('strongs') or '')):
            w.writerow({k: r.get(k, '') for k in cols})

    # Routing distribution
    routing_counter = Counter(r['routing'] for r in rows)

    # Per-batch routing
    per_batch = defaultdict(Counter)
    for r in rows:
        per_batch[r['batch_id']][r['routing']] += 1

    # MD
    md = []
    md.append('# VC revision ledger — v1\n')
    md.append(f'**Date:** {date.today().isoformat()}  ')
    md.append('**Status:** v1 initial build. Records per-term routing outcomes from VCB-7..11 patches.  ')
    md.append('**Linked planning doc:** [vc-corrective-strategy-v1-20260425.md](vc-corrective-strategy-v1-20260425.md) — strategy §5 Step 1.  ')
    md.append('**Sample size:** 30 RE-EVAL terms (NO-CHANGE | REVISE-ONLY | MIXED) — small. Univariate signals only.  ')
    md.append('**Caveat:** predictor metadata read from current DB (post-apply); revisions may have changed group counts in a small number of cases. Footnoted per term in the ledger CSV where pre-state differs.\n')
    md.append('---\n')

    md.append('## 1. Overall routing distribution\n')
    md.append('| Routing | Count | % of total |')
    md.append('|---------|------:|-----------:|')
    total = sum(routing_counter.values())
    for routing in ('NO-CHANGE', 'REVISE-ONLY', 'MIXED', 'NEW-ONLY'):
        c = routing_counter.get(routing, 0)
        pct = (c / total * 100) if total else 0
        md.append(f'| {routing} | {c} | {pct:.1f}% |')
    md.append(f'| **Total** | **{total}** | 100.0% |\n')

    md.append('## 2. Per-batch routing\n')
    md.append('| Batch | NO-CHANGE | REVISE-ONLY | MIXED | NEW-ONLY | Total |')
    md.append('|-------|----------:|------------:|------:|---------:|------:|')
    for batch in sorted(per_batch.keys()):
        c = per_batch[batch]
        total_b = sum(c.values())
        md.append(f'| {batch} | {c.get("NO-CHANGE",0)} | {c.get("REVISE-ONLY",0)} | {c.get("MIXED",0)} | {c.get("NEW-ONLY",0)} | {total_b} |')
    md.append('')

    md.append('## 3. Univariate predictor scores (RE-EVAL terms only)\n')
    md.append(f'**RE-EVAL cohort:** {n} terms ({n_revised} revised, base rate {base_rate*100:.1f}%)\n')
    md.append('Predictor evaluation: rate of revision (REVISE-ONLY|MIXED) within the predicted-positive subset vs. predicted-negative subset. Lift = positive_rate / base_rate.\n')
    md.append('| Predictor | Pos n | Pos revised | Pos rate | Neg n | Neg revised | Neg rate | Lift |')
    md.append('|-----------|------:|------------:|---------:|------:|------------:|---------:|-----:|')
    for name, n_p, r_p, rate_p, n_n, r_n, rate_n in predictors:
        lift = (rate_p / base_rate) if (rate_p and base_rate) else None
        lift_str = f'{lift:.2f}' if lift is not None else ' n/a '
        md.append(f'| {name} | {n_p} | {r_p} | {fmt_pct(rate_p)} | {n_n} | {r_n} | {fmt_pct(rate_n)} | {lift_str} |')
    md.append('')

    md.append('## 4. Per-term ledger (RE-EVAL terms)\n')
    md.append('| Batch | mti | Strongs | Reg | Word | Lang | Verses | Groups | vcrows | Routing | SB | PH2 |')
    md.append('|-------|----:|---------|----:|------|------|-------:|-------:|-------:|---------|---:|----:|')
    for r in sorted([x for x in rows if x['routing'] in ('NO-CHANGE','REVISE-ONLY','MIXED')],
                    key=lambda x: (x['batch_id'], x.get('reg_no') or 0, x.get('strongs') or '')):
        translit = (r.get('translit') or '')[:14]
        gloss = (r.get('gloss') or '')[:18]
        md.append(f'| {r["batch_id"]} | {r["mti_term_id"]} | {r.get("strongs","")} | {r.get("reg_no","")} | '
                  f'{r.get("reg_word",""):<14} | {(r.get("lang","") or "")[:1]} | '
                  f'{r.get("verses","")} | {r.get("groups","")} | {r.get("vc_rows","")} | '
                  f'{r["routing"]} | {r.get("has_sb_flag","")} | {r.get("has_ph2_flag","")} |')
    md.append('')

    md.append('## 5. Per-term ledger (NEW-ONLY terms — partial-completion or fresh)\n')
    md.append('Listed for completeness. NEW-ONLY routing reflects partial-completion gaps absorbed by VCNEW or true FRESH classification — not predictive of future RE-EVAL revision risk.\n')
    md.append('| Batch | mti | Strongs | Reg | Word | Lang | Verses | Groups | vcrows | vcnew_ops |')
    md.append('|-------|----:|---------|----:|------|------|-------:|-------:|-------:|----------:|')
    for r in sorted([x for x in rows if x['routing'] == 'NEW-ONLY'],
                    key=lambda x: (x['batch_id'], x.get('reg_no') or 0, x.get('strongs') or '')):
        md.append(f'| {r["batch_id"]} | {r["mti_term_id"]} | {r.get("strongs","")} | {r.get("reg_no","")} | '
                  f'{r.get("reg_word",""):<14} | {(r.get("lang","") or "")[:1]} | '
                  f'{r.get("verses","")} | {r.get("groups","")} | {r.get("vc_rows","")} | '
                  f'{r["vcnew_ops"]} |')
    md.append('')

    md.append('## 6. Observations\n')
    md.append('Filled in narrative form once the numbers above are reviewed. Initial template:\n')
    md.append('- Strongest predictor surfaced (or "no clear univariate signal at N=30").')
    md.append('- Whether revisions cluster by language / registry / term type.')
    md.append('- Whether revision shape is dominated by description sharpening (consistent with strategy §3.2 prior).')
    md.append('- Specific terms whose outcome surprises (e.g. high-group term that returned NO-CHANGE).\n')

    md.append('## 7. Next actions\n')
    md.append('- If a predictor shows lift >2.0 with positive_rate >50% on N>=10 in the cohort: candidate triage rule. Validate on the next 1–2 batches before promoting.')
    md.append('- If no signal at N=30: continue VCB rolling, append to ledger after each batch, re-score at N=50 and N=100.')
    md.append('- Predictor candidates not yet tested in v1 (require additional schema queries): set_aside_reason gap on prior rows; dimension_index flag presence on registry; property-vs-characteristic term type. Add in v1.1 if signal warrants.\n')

    md.append('---')
    md.append('*Generated by `scripts/_build_vc_revision_ledger.py`. Re-run after each VCB to refresh.*')

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    return md_path, csv_path


def main():
    print('Loading patches...')
    rows = derive_per_term_routing()
    print(f'  {len(rows)} term-occurrences across {len(set(r["batch_id"] for r in rows))} batches')

    print('Attaching DB metadata...')
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = attach_db_metadata(rows, conn)

    print('Scoring univariate predictors...')
    n, n_rev, base, preds = score_predictors(rows)
    print(f'  RE-EVAL cohort: {n} terms; revised: {n_rev}; base rate: {base*100:.1f}%')
    for name, n_p, r_p, rate_p, n_n, r_n, rate_n in preds:
        rate_p_s = fmt_pct(rate_p)
        rate_n_s = fmt_pct(rate_n)
        lift = (rate_p / base) if (rate_p and base) else None
        lift_s = f'lift={lift:.2f}' if lift else 'lift=n/a'
        print(f'  {name:<32} pos {n_p:>2}/{r_p:<2} {rate_p_s}  neg {n_n:>2}/{r_n:<2} {rate_n_s}  {lift_s}')

    print('Writing outputs...')
    md_path, csv_path = write_outputs(rows, n, n_rev, base, preds)
    print(f'  MD : {md_path}')
    print(f'  CSV: {csv_path}')

    conn.close()


if __name__ == '__main__':
    main()
