"""Cold-read validation aggregator for M10 CHARACTERISTIC vs CONDITION units.
Computes, per unit (Strong's set), from the on-disk corpus:
 - per-TERM variance of type/faculty (to confirm they are lemma-constants)
 - distribution of legit per-verse fields: sense, object, object_type, experiencer, valence
 - location/co-seated counts (legit per-verse interior signal)
 - LEXICAL-GAP: occ with empty object / object_type / sense
No conclusions; evidence only."""
import json, os
from collections import Counter, defaultdict

CORPUS = os.path.join('Sessions-v2','M10-Sin','findings','wa-m10-corpus-1904verses-v1_0-20260622.json')

UNITS = {
 '#20 Faithlessness (CHAR claim)':        ['H0898','H4603','H4604'],
 '#21 Perversion (CHAR claim)':           ['G1311','G5351','G5356','H2017','H2254B','H3891','H4297','H5040','H5494','H5557','H5753A','H5753B','H8397','H8419'],
 '#27 Iniquity-scheming (CHAR anchor)':   ['H0205G','H7455'],
 '#11/#12 Sin-noun (CONDITION claim)':    ['H2403B','H2403H','H5771G'],
 '#24 Evil-constitutional (CONDITION)':   ['G0093','G2549','G4189','G4190','G5337'],
 '#29-32 Defilement (CONDITION/STATE)':   ['H2930A','H2931','H5079','G0169','G0167','G3435','G3436','G3394'],
}

def cnt(c, n=12):
    return ', '.join(f'{k}:{v}' for k,v in c.most_common(n))

def main():
    corpus = json.load(open(CORPUS, encoding='utf-8'))['verses']
    for label, strongs in UNITS.items():
        S=set(strongs)
        # per-term value sets for constancy
        term_type=defaultdict(set); term_fac=defaultdict(set)
        sense_c=Counter(); type_c=Counter(); fac_c=Counter()
        objt_c=Counter(); obj_c=Counter(); exp_c=Counter(); val_c=Counter()
        loc_c=Counter(); coseat_c=Counter()
        nocc=0; nverse=0
        gap_obj=0; gap_objt=0; gap_sense=0; gap_how=0
        objt_by_term=defaultdict(Counter)
        for V in corpus:
            focus=[o for o in V['term_occurrences']
                   if o.get('term',{}).get('strong') in S and o.get('term',{}).get('focus_cluster')]
            if not focus: continue
            nverse+=1
            for o in focus:
                nocc+=1
                t=o['term']; lx=o.get('lexical',{})
                st=t['strong']
                ty=lx.get('type'); fc=lx.get('faculty')
                term_type[st].add(str(ty)); term_fac[st].add(str(fc))
                sense_c[lx.get('sense') or '(empty)']+=1
                type_c[str(ty) or '(empty)']+=1
                fac_c[str(fc) or '(empty)']+=1
                ot=lx.get('object_type'); ob=lx.get('object')
                objt_c[ot or '(empty)']+=1; obj_c[ob or '(empty)']+=1
                objt_by_term[st][ot or '(empty)']+=1
                exp_c[lx.get('experiencer') or '(empty)']+=1
                val_c[lx.get('valence') or '(empty)']+=1
                lo=lx.get('location')
                if lo: loc_c[str(lo)]+=1
                if not ob: gap_obj+=1
                if not ot: gap_objt+=1
                if not lx.get('sense'): gap_sense+=1
                if not lx.get('how'): gap_how+=1
                comp=lx.get('compound') or []
                comp=[comp] if isinstance(comp,str) else comp
                for c in comp:
                    if isinstance(c,str) and 'co-seated' in c:
                        coseat_c[c.split('\"')[0].strip()]+=1
        print('\n================', label)
        print(f'occ={nocc}  verses={nverse}')
        # constancy
        tvar=sum(1 for st in term_type if len(term_type[st])>1)
        fvar=sum(1 for st in term_fac if len(term_fac[st])>1)
        print(f'TERMS={len(term_type)}  type-varies-per-term={tvar}  faculty-varies-per-term={fvar}')
        for st in sorted(term_type):
            tv='VARIES' if len(term_type[st])>1 else 'const'
            print(f'   {st}: type[{tv}]={sorted(term_type[st])}  faculty={sorted(term_fac[st])}')
        print('TYPE     :', cnt(type_c))
        print('FACULTY  :', cnt(fac_c))
        print('SENSE    :', cnt(sense_c,15))
        print('OBJ_TYPE :', cnt(objt_c))
        print('OBJECT   :', cnt(obj_c,15))
        print('EXPERNCR :', cnt(exp_c))
        print('VALENCE  :', cnt(val_c))
        print('LOCATION :', cnt(loc_c), f'(total located occ={sum(loc_c.values())}/{nocc})')
        print('CO-SEATED:', cnt(coseat_c), f'(total co-seat={sum(coseat_c.values())})')
        print(f'GAPS: empty object={gap_obj}/{nocc}  empty object_type={gap_objt}/{nocc}  empty sense={gap_sense}/{nocc}  empty how={gap_how}/{nocc}')

if __name__=='__main__':
    main()
