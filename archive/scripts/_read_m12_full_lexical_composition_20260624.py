"""
M12 full-composition lexical read (read-only) — STEP 2 of the corrected sequence.
Reads the M12 extract and, per term-family, reports ONLY the per-verse-VARYING
fields as evidence (sense/object/object_type/experiencer/valence + co-seating),
and QUARANTINES type/faculty/lemma_meaning as LEMMA-CONSTANTS (not object-type
evidence). 'distinct' counts show whether a field actually varies per verse.

This re-establishes the principle: preliminary units derive from reading the
lexical evidence in-cluster; object-type is decided later, only from varying fields.

Usage: python -X utf8 scripts\_read_m12_full_lexical_composition_20260624.py
"""
import json, os
from collections import Counter, defaultdict

EXTRACT = os.path.join('Sessions-v2','M12-Purity','Data','wa-ve-lexical-extract-M12-20260623.json')

# Full M12 composition (48 active owned terms) grouped by lexical family — IN-CLUSTER, nothing exported.
FAMILIES = {
 'purity-HEB (tahor)':      ['H2889','H2890','H2891','H2892A','H2892B','H2893'],
 'purity-GK (hagn)':        ['G0047','G0048','G0049','G0053','G0054'],
 'purity-GK (kathar)':      ['G2511','G2512','G2513'],
 'holiness/consecr (qadosh)':['H6918H','H6942G','H6942H','H6942I','H6942J','H6942K','H5144A','G3741'],
 'innocence/blameless':     ['H5352','H5355A','H5355B','H8549G','H8549H','H8549I','H8549J','G0172','G0338','G0361','G0178'],
 'sincerity/genuine':       ['G1506','G0505','G0097'],
 'incorruptibility':        ['G0861'],
 'GIVING (na.tan)':         ['H5414G'],
 'FORMING (tsur/morfoo)':   ['H6696C','G3445'],
 'anointing':               ['G1472','G2025'],
 'NEG-POLE (defile/stain)': ['H2932','G3392','G0462'],
 'perfection/soundness':    ['H4974','H4357','H8502'],
}

OT={'Gen','Exo','Lev','Num','Deu','Jos','Jdg','Rut','1Sa','2Sa','1Ki','2Ki','1Ch','2Ch','Ezr','Neh','Est','Job','Psa','Pro','Ecc','Sng','Isa','Jer','Lam','Eze','Dan','Hos','Joe','Amo','Oba','Jon','Mic','Nah','Hab','Zep','Hag','Zec','Mal'}

def norm(v):
    if v is None: return None
    if isinstance(v,list): return '+'.join(str(x) for x in v) if v else None
    return str(v)

def load():
    d=json.load(open(EXTRACT,encoding='utf-8'))
    return d.get('data') or d.get('verses') if isinstance(d,dict) else d

def book(ref): return ref.split()[0] if ' ' in ref else ref[:3]

def main():
    verses=load()
    # bucket occurrences by family
    fam_of={}
    for fam,ss in FAMILIES.items():
        for s in ss: fam_of[s]=fam
    data=defaultdict(lambda: {'occ':0,'ot':0,'nt':0,
        'sense':Counter(),'object':Counter(),'object_type':Counter(),'experiencer':Counter(),
        'valence':Counter(),'coseat':Counter(),'type':Counter(),'faculty':Counter(),'how':0})
    for V in verses:
        ref=V['verse']['reference']; bk=book(ref)
        focus=[o for o in V['term_occurrences'] if o.get('term',{}).get('focus_cluster') and o['term'].get('strong') in fam_of]
        coterms=[o for o in V['term_occurrences'] if o not in focus]
        for o in focus:
            fam=fam_of[o['term']['strong']]; d=data[fam]; lx=o.get('lexical',{})
            d['occ']+=1; d['ot' if bk in OT else 'nt']+=1
            for f in ['sense','object','object_type','experiencer','valence','type','faculty']:
                val=norm(lx.get(f))
                if val is not None: d[f][val]+=1
            if lx.get('how'): d['how']+=1
            for c in coterms:
                t=c['term']
                if t.get('cluster') and t.get('translit'):
                    d['coseat'][f"{t.get('translit')}({t.get('cluster')})"]+=1
    # report
    for fam in FAMILIES:
        d=data.get(fam)
        if not d or not d['occ']:
            print(f'\n### {fam}: 0 occ (absent in extract)'); continue
        print(f'\n### {fam} — {d["occ"]} occ (OT {d["ot"]} / NT {d["nt"]})')
        print('  PER-VERSE-VARYING EVIDENCE (the legitimate object-type signals):')
        print(f'    sense      [{len(d["sense"])} distinct]: {dict(d["sense"].most_common(6))}')
        print(f'    object     [{len(d["object"])} distinct]: {dict(d["object"].most_common(6))}')
        print(f'    object_type[{len(d["object_type"])} distinct]: {dict(d["object_type"].most_common())}')
        print(f'    experiencer[{len(d["experiencer"])} distinct]: {dict(d["experiencer"].most_common(6))}')
        vd=dict(d["valence"].most_common())
        print(f'    valence    [{len(d["valence"])} distinct{" — VARIES (state-signal)" if len(d["valence"])>1 else ""}]: {vd}')
        print(f'    how-coverage: {d["how"]}/{d["occ"]} ({round(100*d["how"]/d["occ"])}%)')
        print(f'    co-seated (top): {dict(d["coseat"].most_common(8))}')
        print('  LEMMA-CONSTANTS (NOT object-type evidence — descriptive only):')
        print(f'    type={dict(d["type"].most_common())}  faculty={dict(d["faculty"].most_common())}')

if __name__=='__main__':
    main()
