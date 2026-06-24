"""
Lexical-Revelation Test (LRT) — runs DURING deep evidence gathering (step 3) to
check whether the lexical is FULLY REVEALING for a unit, BEFORE conclusions.

Researcher's checks (2026-06-24):
  1. what is MISSING / expected-but-not-present
  2. what CONTRADICTS
  3. were ALL the lexical fields properly considered
  4. is there an ODD ONE OUT
  5. how do the PARTS PLAY TOGETHER
  + the EXPECTEDNESS principle: a field empty where the term's NATURE demands it
    is a red flag (giving [act] DEMANDS a manner -> how cannot be null) -> locate
    the missing content (verse_text? bound term?) and propose how to assess it.

Usage: python -X utf8 scripts\_lexical_revelation_test_20260624.py --strongs H5414G --label GIVING --nature act
       --nature one of: act | state | characteristic | relational  (drives expectedness)
"""
import json, os, re, argparse
from collections import Counter, defaultdict

EX = os.path.join('Sessions-v2','M12-Purity','Data','wa-ve-lexical-extract-M12-20260623.json')
PER_VERSE = ['sense','object','object_type','experiencer','valence','how']      # legit per-verse fields
CONSTANTS = ['type','faculty','lemma_meaning']                                   # lemma-constants
# fields a unit's NATURE expects to be populated (empty where expected = red flag)
EXPECTED = {
 'act':            ['sense','object','how','experiencer'],     # an act has a manner (how) + what it acts on
 'state':          ['sense','valence'],                        # a state has a valence register
 'characteristic': ['sense','object','experiencer'],           # a faculty-in-operation is directed
 'relational':     ['sense','object','experiencer'],
}
MANNER = re.compile(r'\b(freely|freewill|willing\w*|whole heart|cheerful\w*|generous\w*|liberal\w*|grudg\w*|bountif\w*|abund\w*|gladly|reluctan\w*|sincer\w*|secret\w*|openly|with all (his|their|your) heart)\b', re.I)

def norm(v):
    if v is None: return None
    if isinstance(v,list): return '+'.join(str(x) for x in v) if v else None
    return str(v)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--strongs',required=True); ap.add_argument('--label',default='unit')
    ap.add_argument('--nature',default='act',choices=EXPECTED)
    ap.add_argument('--corpus',default=EX)
    a=ap.parse_args()
    ss=set(s.strip() for s in a.strongs.split(','))
    d=json.load(open(a.corpus,encoding='utf-8')); verses=d.get('data') or d.get('verses')
    occ=[]
    for V in verses:
        for o in V['term_occurrences']:
            t=o.get('term',{})
            if t.get('focus_cluster') and t.get('strong') in ss:
                occ.append((V['verse']['reference'], V['verse'].get('verse_text',''), o.get('lexical',{}),
                            [c['term'] for c in V['term_occurrences'] if c is not o]))
    n=len(occ)
    print(f'=== LRT: {a.label} ({a.strongs}) — {n} occ — nature={a.nature} ===\n')
    # 1+3. coverage of ALL fields (were all fields considered?)
    cov={f: sum(1 for _,_,lx,_ in occ if norm(lx.get(f)) is not None) for f in PER_VERSE+CONSTANTS}
    print('FIELD COVERAGE (per-verse fields):')
    for f in PER_VERSE:
        pct=round(100*cov[f]/n) if n else 0
        exp='  <-- EXPECTED' if f in EXPECTED[a.nature] else ''
        flag='  *** RED FLAG: expected but sparse' if (f in EXPECTED[a.nature] and pct<50) else ''
        print(f'   {f:<12} {cov[f]:>4}/{n} ({pct:>3}%){exp}{flag}')
    print('  constants:',{f:cov[f] for f in CONSTANTS})
    # 5. parts play together: distinct values per field (does it vary = per-verse signal?)
    distinct={f: len({norm(lx.get(f)) for _,_,lx,_ in occ if norm(lx.get(f)) is not None}) for f in PER_VERSE}
    print('\nDISTINCTNESS (varies per verse?):',distinct)
    # 4. odd-one-out: rare (object_type,valence) combos
    combo=Counter((norm(lx.get('object_type')),norm(lx.get('valence'))) for _,_,lx,_ in occ)
    odd=[(k,v) for k,v in combo.items() if v<=max(2,n//40)]
    print(f'\nODD-ONE-OUT (rare object_type x valence combos, <= {max(2,n//40)}):')
    for k,v in sorted(odd,key=lambda x:x[1])[:10]: print(f'   {k}: {v}')
    # 2. contradiction heuristics
    print('\nCONTRADICTION CHECKS:')
    contr=0
    for ref,txt,lx,_ in occ:
        if norm(lx.get('type'))=='action' and norm(lx.get('object')) is None and norm(lx.get('how')) is None:
            contr+=1
    print(f'   action-type w/ no object AND no how (manner+target both blank): {contr}/{n}')
    # MISSING-CONTENT RECOVERY (the giving case): if an EXPECTED field is sparse, locate it
    for f in EXPECTED[a.nature]:
        pct=round(100*cov[f]/n) if n else 0
        if pct<50:
            print(f'\nRECOVERY for missing [{f}] (expected by nature={a.nature}, only {pct}% populated):')
            if f=='how':
                inverse=sum(1 for _,txt,_,_ in occ if MANNER.search(txt))
                print(f'   manner-words present in verse_text (recoverable how): {inverse}/{n} ({round(100*inverse/n)}%)')
                # which bound terms carry manner/characteristic
                bind=Counter()
                for _,_,_,cot in occ:
                    for t in cot:
                        tl=(t.get('translit') or '')
                        if t.get('cluster'): bind[f"{tl}({t.get('cluster')})"]+=1
                print('   binding co-terms (where the characteristic/manner may live):',dict(bind.most_common(8)))
            else:
                miss=[ref for ref,_,lx,_ in occ if norm(lx.get(f)) is None][:5]
                print(f'   sample occ with [{f}] blank: {miss}')

if __name__=='__main__':
    main()
