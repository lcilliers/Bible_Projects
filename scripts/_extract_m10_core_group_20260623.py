"""
Mechanical assembly of an M10 CORE reading group from the on-disk corpus
(wa-m10-corpus-1904verses). Produces a per-group working JSON: every focus
verse for the group's lemmas with verse_text + the focus term's lexical + the
co-term web (partner/qualifier/co-seated) + group-level mechanical summaries
(sense/type/faculty/valence/object_type counts, co-seated tally, book spread).

This is the MECHANICAL layer only — the reading/evidence digest is authored
separately (CC, no-conclusions discipline, per the per-verse schema spec).

Usage: python _extract_m10_core_group_20260623.py --group pesha
Groups: hata | avon | pesha | hamart
"""
import json, os, sys, argparse
from collections import Counter, defaultdict

CORPUS = os.path.join('Sessions-v2','M10-Sin','findings','wa-m10-corpus-1904verses-v1_0-20260622.json')
OUTDIR = os.path.join('Sessions-v2','M10-Sin','findings')

GROUPS = {
    'hata':  {'H2398','H2403B','H2403H','H2403I','H2399','H2400','H2401','H2403A'},  # chata family
    'avon':  {'H5771G','H5771H','H5771I'},                                            # a.von
    'pesha': {'H6588','H6586'},                                                       # pe.sha + pa.sha
    'hamart':{'G0266','G0264','G0265','G0268'},                                       # NT hamart-
    'm10c':  {'H2930A','H2931','H5079','G0169','G0167','G3435','G3436','G3394'},       # M10c defilement/impurity
}

# canonical book order for the spread report
OSIS_ORDER = ['Gen','Exo','Lev','Num','Deu','Jos','Jdg','Rut','1Sa','2Sa','1Ki','2Ki','1Ch','2Ch',
 'Ezr','Neh','Est','Job','Psa','Pro','Ecc','Sng','Isa','Jer','Lam','Eze','Dan','Hos','Joe','Amo',
 'Oba','Jon','Mic','Nah','Hab','Zep','Hag','Zec','Mal','Mat','Mar','Luk','Joh','Act','Rom','1Co',
 '2Co','Gal','Eph','Php','Col','1Th','2Th','1Ti','2Ti','Tit','Phm','Heb','Jas','1Pe','2Pe','1Jo',
 '2Jo','3Jo','Jud','Rev']

def book_of(ref):
    return ref.split()[0] if ' ' in ref else ref[:3]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--group', choices=GROUPS, help='predefined M10 group')
    ap.add_argument('--corpus', default=CORPUS, help='extract/corpus JSON (any cluster)')
    ap.add_argument('--strongs', help='comma-separated Strong\'s (override --group)')
    ap.add_argument('--label', help='batch label for the output filename (with --strongs)')
    ap.add_argument('--outdir', default=OUTDIR, help='output dir')
    a = ap.parse_args()
    if a.strongs:
        strongs = set(s.strip() for s in a.strongs.split(','))
        a.group = a.label or 'batch'
    elif a.group:
        strongs = GROUPS[a.group]
    else:
        ap.error('need --group or --strongs')
    corpus = json.load(open(a.corpus, encoding='utf-8'))
    corpus = {'verses': corpus['verses'] if isinstance(corpus, dict) and 'verses' in corpus
              else corpus['data'] if isinstance(corpus, dict) and 'data' in corpus else corpus}
    global OUTDIR; OUTDIR = a.outdir

    out_verses = []
    sense_c, type_c, fac_c, val_c, objt_c = Counter(), Counter(), Counter(), Counter(), Counter()
    coseat_c, role_c, book_c = Counter(), Counter(), Counter()
    nocc = 0

    for V in corpus['verses']:
        ref = V['verse']['reference']; text = V['verse'].get('verse_text','')
        focus = [o for o in V['term_occurrences']
                 if o.get('term',{}).get('strong') in strongs and o.get('term',{}).get('focus_cluster')]
        if not focus:
            continue
        coterms = [o for o in V['term_occurrences'] if o not in focus]
        book_c[book_of(ref)] += 1
        rec = {'ref': ref, 'text': text, 'focus': [], 'coterms': []}
        for o in focus:
            nocc += 1
            t = o['term']; lx = o.get('lexical',{})
            sense_c[lx.get('sense') or '(none)'] += 1
            type_c[lx.get('type') or '(none)'] += 1
            fac_c[lx.get('faculty') or '(none)'] += 1
            val_c[lx.get('valence') or '(none)'] += 1
            objt_c[lx.get('object_type') or '(none)'] += 1
            # compound: a list of strings 'translit "gloss" — role' (sometimes a single string)
            comp_raw = lx.get('compound') or []
            comp_list = [comp_raw] if isinstance(comp_raw, str) else comp_raw
            for comp in comp_list:
                if not isinstance(comp, str):
                    continue
                role = comp.rsplit('—', 1)[-1].strip() if '—' in comp else '(unmarked)'
                role_c[role] += 1
                if role == 'co-seated':
                    partner = comp.split('"')[0].strip()  # translit before the gloss-quote
                    coseat_c[partner or '?'] += 1
            rec['focus'].append({'translit': t.get('translit'), 'strong': t.get('strong'),
                'gloss': t.get('gloss'), 'sense': lx.get('sense'), 'lemma_meaning': lx.get('lemma_meaning'),
                'type': lx.get('type'), 'faculty': lx.get('faculty'), 'how': lx.get('how'),
                'object': lx.get('object'), 'object_type': lx.get('object_type'),
                'valence': lx.get('valence'), 'experiencer': lx.get('experiencer'),
                'compound': lx.get('compound')})
        for o in coterms:
            t = o['term']
            rec['coterms'].append({'translit': t.get('translit'), 'gloss': t.get('gloss'),
                'cluster': t.get('cluster'), 'strong': t.get('strong')})
        out_verses.append(rec)

    summary = {
        'group': a.group, 'strongs': sorted(strongs), 'focus_occ': nocc,
        'unique_verses': len(out_verses),
        'book_spread': {b: book_c[b] for b in OSIS_ORDER if book_c[b]},
        'type': dict(type_c.most_common()), 'sense_top': dict(sense_c.most_common(25)),
        'faculty': dict(fac_c.most_common()), 'valence': dict(val_c.most_common()),
        'object_type': dict(objt_c.most_common()), 'compound_roles': dict(role_c.most_common()),
        'co_seated_tally': dict(coseat_c.most_common()),
    }
    out = {'_meta': {'source': CORPUS, 'built': '2026-06-23',
                     'note': 'mechanical assembly for CC evidence reading; no conclusions'},
           'summary': summary, 'verses': out_verses}
    stem = f'{a.label}-lexbatch' if a.label else f'm10-core-{a.group}-assembly'
    path = os.path.join(OUTDIR, f'wa-{stem}-v1_0-20260623.json')
    json.dump(out, open(path,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'wrote {path}')
    print(json.dumps(summary, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
