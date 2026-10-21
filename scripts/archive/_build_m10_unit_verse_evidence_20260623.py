"""
Emit the PER-VERSE structured evidence section for an M10 unit, from the on-disk
corpus (wa-m10-corpus-1904verses). Mechanical only — the general/non-verse
section is copied from the digests separately.

Select the unit's verses by focus Strong's, optionally narrowed to a ref-list
(for units distinguished by a per-occurrence reading, e.g. political pa.sha).

Usage:
  python _build_m10_unit_verse_evidence_20260623.py --strongs H6586 --refs "2Ki 1:1,2Ki 3:5,..."
  python _build_m10_unit_verse_evidence_20260623.py --strongs H7563,H7562
Outputs markdown to stdout.
"""
import json, os, argparse

CORPUS = os.path.join('Sessions-v2','M10-Sin','findings','wa-m10-corpus-1904verses-v1_0-20260622.json')
OSIS = ['Gen','Exo','Lev','Num','Deu','Jos','Jdg','Rut','1Sa','2Sa','1Ki','2Ki','1Ch','2Ch','Ezr','Neh','Est','Job','Psa','Pro','Ecc','Sng','Isa','Jer','Lam','Eze','Dan','Hos','Joe','Amo','Oba','Jon','Mic','Nah','Hab','Zep','Hag','Zec','Mal','Mat','Mar','Luk','Joh','Act','Rom','1Co','2Co','Gal','Eph','Php','Col','1Th','2Th','1Ti','2Ti','Tit','Phm','Heb','Jas','1Pe','2Pe','1Jo','2Jo','3Jo','Jud','Rev']

def sortkey(ref):
    p = ref.split()
    bk = p[0]
    try:
        cv = p[1].split(':'); ch, vs = int(cv[0]), int(cv[1])
    except Exception:
        ch, vs = 0, 0
    return (OSIS.index(bk) if bk in OSIS else 99, ch, vs)

def fld(lx, k):
    v = lx.get(k)
    return v if v not in (None, '') else None

LEX_ORDER = ['sense','lemma_meaning','type','faculty','location','origin','how','object',
             'object_type','cause','cause_clause','experiencer','divine_involvement',
             'intensity','valence','immediate_response','relational']

def emit_term(o, is_focus):
    """Full record for one term occurrence (self-standing)."""
    t = o.get('term', {}); vr = o.get('verse_report', {}) or {}; lx = o.get('lexical', {}) or {}
    head = f"**{t.get('translit')} ({t.get('strong')})** — {t.get('gloss')}"
    meta = [t.get('language'), t.get('cluster')]
    if is_focus: meta.append('**FOCUS**')
    mm = []
    if vr.get('morph'): mm.append(f"morph={vr['morph']}")
    if vr.get('stem'): mm.append(f"stem={vr['stem']}")
    if vr.get('target_word'): mm.append(f"target=“{vr['target_word']}”")
    line = f"- {head}  [{' · '.join(str(m) for m in meta if m)}]"
    if mm: line += '  ' + ' · '.join(mm)
    print(line)
    bits = []
    for k in LEX_ORDER:
        v = fld(lx, k)
        if v is not None: bits.append(f"{k}={v}")
    if bits:
        print('  - ' + ' · '.join(bits))
    comp = lx.get('compound')
    comp = [comp] if isinstance(comp, str) else (comp or [])
    if comp:
        print('  - compound: ' + '; '.join(comp))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--strongs', required=True, help='comma-separated Strong\'s')
    ap.add_argument('--refs', default='', help='optional comma-separated ref allow-list')
    ap.add_argument('--corpus', default=CORPUS, help='corpus/extract JSON (default: M10 corpus)')
    a = ap.parse_args()
    strongs = set(s.strip() for s in a.strongs.split(','))
    reflist = set(r.strip() for r in a.refs.split(',') if r.strip()) if a.refs else None

    corpus = json.load(open(a.corpus, encoding='utf-8'))
    verses = corpus['verses'] if isinstance(corpus, dict) and 'verses' in corpus \
        else corpus['data'] if isinstance(corpus, dict) and 'data' in corpus else corpus
    rows = []
    for V in verses:
        ref = V['verse']['reference']
        if reflist is not None and ref not in reflist:
            continue
        foci = [o for o in V['term_occurrences']
                if o['term'].get('strong') in strongs and o['term'].get('focus_cluster')]
        if not foci:
            continue
        rows.append((ref, V['verse'].get('verse_text',''), foci, V['term_occurrences']))

    rows.sort(key=lambda r: sortkey(r[0]))
    print(f'_Per-verse structured evidence — {len(rows)} verses; Strong\'s {sorted(strongs)}'
          + (f'; ref-filtered to {len(reflist)}' if reflist else '') + '. From the corpus; evidence only._\n')
    for ref, text, foci, allocc in rows:
        print(f'#### {ref}')
        print(f'> {text}')
        # focus term(s) first (full record), then every co-term (full record) — self-standing
        for o in foci:
            emit_term(o, True)
        for o in allocc:
            if o in foci:
                continue
            emit_term(o, False)
        print()

if __name__ == '__main__':
    main()
