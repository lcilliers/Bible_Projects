"""
GENERIC full-composition lexical read (read-only) — step 2 of the corrected
sequence, for ANY cluster. Groups a cluster's owned terms by owning-registry
(the semantic field that sourced them), and reports ONLY the per-verse-VARYING
fields as evidence (sense/object/object_type/experiencer/valence + co-seating);
type/faculty/lemma_meaning are QUARANTINED as lemma-constants. 'distinct' shows
whether a field varies per verse.

Usage: python -X utf8 scripts\_read_full_lexical_composition_20260624.py --cluster M13 --corpus <extract.json>
"""
import json, os, sqlite3, argparse
from collections import Counter, defaultdict

OT={'Gen','Exo','Lev','Num','Deu','Jos','Jdg','Rut','1Sa','2Sa','1Ki','2Ki','1Ch','2Ch','Ezr','Neh','Est','Job','Psa','Pro','Ecc','Sng','Isa','Jer','Lam','Eze','Dan','Hos','Joe','Amo','Oba','Jon','Mic','Nah','Hab','Zep','Hag','Zec','Mal'}
PER_VERSE=['sense','object','object_type','experiencer','valence','how']

def norm(v):
    if v is None: return None
    if isinstance(v,list): return '+'.join(str(x) for x in v) if v else None
    return str(v)
def book(ref): return ref.split()[0] if ' ' in ref else ref[:3]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--cluster',required=True); ap.add_argument('--corpus',required=True)
    a=ap.parse_args()
    c=sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory=sqlite3.Row
    terms={}; reg_of={}
    for r in c.execute("""select m.strongs_number s, m.transliteration t, m.gloss g, coalesce(wr.word,'(none)') reg
        from mti_terms m left join word_registry wr on wr.id=m.owning_registry_fk
        where m.cluster_code=? and coalesce(m.delete_flagged,0)=0
          and (m.status is null or m.status not in ('delete','candidate_delete','excluded'))""",(a.cluster,)):
        terms[r['s']]={'t':r['t'],'g':r['g'],'reg':r['reg']}; reg_of[r['s']]=r['reg']
    d=json.load(open(a.corpus,encoding='utf-8')); verses=d.get('data') or d.get('verses')
    grp=defaultdict(lambda: {'occ':0,'ot':0,'nt':0,'terms':set(),
        'sense':Counter(),'object':Counter(),'object_type':Counter(),'experiencer':Counter(),
        'valence':Counter(),'how':0,'coseat':Counter(),'type':Counter(),'faculty':Counter()})
    for V in verses:
        ref=V['verse']['reference']; bk=book(ref)
        focus=[o for o in V['term_occurrences'] if o.get('term',{}).get('focus_cluster') and o['term'].get('strong') in reg_of]
        co=[o for o in V['term_occurrences'] if o not in focus]
        for o in focus:
            s=o['term']['strong']; reg=reg_of[s]; G=grp[reg]; lx=o.get('lexical',{})
            G['occ']+=1; G['ot' if bk in OT else 'nt']+=1; G['terms'].add(f"{terms[s]['t']} {s}")
            for f in ['sense','object','object_type','experiencer','valence','type','faculty']:
                v=norm(lx.get(f));
                if v is not None: G[f][v]+=1
            if lx.get('how'): G['how']+=1
            for cc in co:
                t=cc['term']
                if t.get('cluster') and t.get('translit'): G['coseat'][f"{t['translit']}({t['cluster']})"]+=1
    tot=sum(g['occ'] for g in grp.values())
    print(f'#### {a.cluster}: {len(terms)} owned terms, {tot} focus occ, grouped by owning-registry\n')
    for reg in sorted(grp, key=lambda r:-grp[r]['occ']):
        G=grp[reg]
        varies=' VARIES' if len(G['valence'])>1 else ''
        howpct=round(100*G['how']/G['occ']) if G['occ'] else 0
        print(f"### [{reg}] — {G['occ']} occ (OT {G['ot']}/NT {G['nt']}) — terms: {sorted(G['terms'])}")
        print(f"   sense[{len(G['sense'])}d]: {dict(G['sense'].most_common(6))}")
        print(f"   object[{len(G['object'])}d]: {dict(G['object'].most_common(5))}")
        print(f"   object_type: {dict(G['object_type'].most_common())}")
        print(f"   experiencer: {dict(G['experiencer'].most_common(4))}")
        print(f"   valence[{len(G['valence'])}d{varies}]: {dict(G['valence'].most_common())}")
        print(f"   how-cov: {G['how']}/{G['occ']} ({howpct}%)")
        print(f"   co-seat: {dict(G['coseat'].most_common(6))}")
        print(f"   [CONSTANTS] type={dict(G['type'].most_common())} faculty={dict(G['faculty'].most_common())}\n")

if __name__=='__main__': main()
