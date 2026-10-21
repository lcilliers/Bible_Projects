"""
_probe_lexical_derivation_all14_v5_20260701.py  (READ-ONLY)

Full 14-dimension derivation for every term in a passage, with the two fixes from the end-to-end
review: (1) PRESENCE-TEST (relational items fire only where a real link exists, not nearest-match);
(2) FOCAL-OPERATION filter (source/effect/process only for terms that are operations/affects, not
incidental object-nouns). Better argument parsing: 'et' (H0853) direct-object marker, governing verb
by adjacency/agreement, construct chains, preposition obliques.

14 dimensions (post researcher decisions):
  D1 Identity(sense+type) D2 Source D3 Seat/Bearer D4 Operation D5 Target(+obj-type) D6 Manner(+intensity)
  D7 Process D8 Effect D9 Coupling D10 Valence(prohibition-only) D11 Discovery D12 Hidden(dropped)
  D13 Cohabitation(implicit=passage co-terms) D14 Passage(membership)

Usage: python scripts/_probe_lexical_derivation_all14_v5_20260701.py [--ref "Exo 1:13"]
"""
import sqlite3, os, re, argparse
DB=os.path.join('database','bible_research.db')
SEATS={'H3820':'heart','H3824':'heart','H5315':'soul','H7307':'spirit','H1320':'flesh','H3629':'kidneys'}
# affect / vice / driver lemmas (an inner state that can ELICIT or BE a movement). seed; grows.
DRIVERS={'H6973':'dread','H3372':'fear','H3373':'fear','H0639':'anger','H2534':'wrath','H8130':'hatred/enmity',
         'H6031':'affliction','H7451':'evil','H2555':'violence','H1272':'terror'}
ET='H0853'; NEG={'H3808':'lo','H0408':'al'}   # object marker ; negation/prohibition
INTENS={'H3966':'very','H7227':'many','H3605':'all','H7235':'increase'}
def canon(s):
    m=re.match(r'^([HG])(\d+)',s or ''); return m.group(1)+m.group(2).zfill(4) if m else s
def parse(mc,pos):
    segs=(mc or '').split(); head=segs[0] if segs else ''
    f={'v':pos=='verb','n':pos=='noun','a':pos=='adjective','state':None,'prep':False,'suf':False}
    if head.startswith('HN') and head[-1] in ('c','a'): f['state']='construct' if head[-1]=='c' else 'absolute'
    for s in segs:
        if s.startswith('HR'): f['prep']=True
        if s.startswith('HS'): f['suf']=True
    return f

def load(cur, refs):
    spans=[]; terms=[]
    for ref in refs:
        v=cur.execute("SELECT id FROM verse WHERE reference=?",(ref,)).fetchone()
        for m in cur.execute("SELECT word_index,surface,primary_strong,pos,stem,morph_code FROM verse_morphology WHERE verse_id=? ORDER BY word_index",(v['id'],)):
            spans.append({'ref':ref,'surface':m['surface'],'strong':canon(m['primary_strong']),'pos':m['pos'],
                          'stem':m['stem'],'feat':parse(m['morph_code'],m['pos']),'g':len(spans)})
        for t in cur.execute("""SELECT w.term_id,w.target_word,mt.owning_word,mt.cluster_code FROM wa_verse_records w
            LEFT JOIN mti_terms mt ON w.mti_term_id=mt.id WHERE w.verse_id=? AND COALESCE(w.delete_flagged,0)=0""",(v['id'],)):
            terms.append({'ref':ref,'strong':canon(t['term_id']),'word':t['target_word'],'gloss':t['owning_word'],'cc':t['cluster_code']})
    return spans, terms

def occ(spans, strong):
    for s in spans:
        if s['strong']==strong: return s
    return None
def gov_verb(spans, g):
    # governing verb = nearest verb within +/-3 (a term is usually adjacent to its verb)
    vs=[s for s in spans if s['feat']['v'] and abs(s['g']-g)<=3]
    return min(vs,key=lambda s:abs(s['g']-g)) if vs else None
def object_of(spans, vg):
    # object = the noun after an 'et' following the verb, else the first non-prep noun within +3 (not subject)
    for j in range(vg+1, min(vg+5,len(spans))):
        if spans[j]['strong']==ET and j+1<len(spans) and spans[j+1]['feat']['n']:
            return spans[j+1]
    return None  # strict: only et-marked objects (presence-test); avoids grabbing wrong nouns

def is_focal(term_span):
    f=term_span['feat']
    return f['v'] or (f['n'] and f['prep'])  # an action, or a prep-marked manner-noun (adverbial operation)

def derive(spans, terms, term):
    s=occ(spans, term['strong'])
    if not s: return None
    g=s['g']; f=s['feat']; d={}
    tstr={t['strong'] for t in terms}
    d['D1 identity']='%s / %s'%(term['word'] or s['surface'], 'action' if f['v'] else 'status' if f['n'] else 'quality' if f['a'] else '?')
    vb=gov_verb(spans,g)
    # D4 operation: the governing verb (only if genuinely adjacent)
    d['D4 operation']=('%s(%s%s)'%(vb['surface'],vb['strong'],','+vb['stem'] if vb['stem'] else '')) if vb else None
    # D3 seat / bearer
    seat=SEATS.get(s['strong'])
    if not seat and f['state']=='construct':
        for j in range(g+1,min(g+3,len(spans))):
            if spans[j]['strong'] in SEATS: seat=SEATS[spans[j]['strong']]; break
    d['D3 seat']=seat
    # D5 target (+ obj-type): only et-marked object of THIS term's verb
    tgt=None
    if f['v']:
        o=object_of(spans,g)
        if o: tgt='%s(%s)'%(o['surface'],o['strong'])
    d['D5 target']=tgt
    # D6 manner (+ intensity)
    manner=('manner-of %s(%s)'%(vb['surface'],vb['strong'])) if (f['n'] and f['prep'] and vb) else None
    d['D6 manner']=manner
    inten=[INTENS[x['strong']] for x in spans if x['strong'] in INTENS and abs(x['g']-g)<=3]
    d['D6 intensity']=(', '.join(sorted(set(inten))) or None)
    # FOCAL gate for source/effect/process
    focal=is_focal(s)
    # D2 source: focal AFFECT/vice term -> nearest preceding driver; else NONE
    src=None
    if focal and (s['strong'] in DRIVERS or f['prep']):
        drv=[x for x in spans if x['strong'] in DRIVERS and x['g']<g and x['strong']!=s['strong']]
        if drv: d_=drv[-1]; src='%s(%s)@%s'%(DRIVERS[d_['strong']],d_['strong'],d_['ref'])
    d['D2 source']=src
    # D8 effect: focal ACTION -> a distinct produced-state (Piel/Hiphil) after it acting onward; else NONE
    eff=None
    if focal and f['v']:
        cands=[x for x in spans if x['feat']['v'] and x['stem'] in ('Piel','Hiphil') and x['g']>g and x['strong']!=s['strong'] and x['strong'] in tstr]
        if cands: e=cands[0]; eff='%s(%s,%s)@%s'%(e['surface'],e['strong'],e['stem'],e['ref'])
    d['D8 effect']=eff
    # D9 coupling: morphological weld only
    cpl=None
    if f['n'] and f['prep'] and vb and vb['strong'] in tstr:
        cpl='welds %s(%s) as manner'%(vb['surface'],vb['strong'])
    d['D9 coupling']=cpl
    # D10 valence: mechanical prohibition only
    proh=any(x['strong'] in NEG and abs(x['g']-g)<=3 for x in spans)
    d['D10 prohibition']=('forbidden (neg particle)' if proh else None)
    return d, focal

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ref',default='Exo 1:13'); a=ap.parse_args()
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    v=cur.execute("SELECT passage_id FROM verse WHERE reference=?",(a.ref,)).fetchone()
    if v['passage_id']:
        refs=[r['reference'] for r in cur.execute("SELECT reference FROM verse WHERE passage_id=? ORDER BY book_id,chapter,verse_num",(v['passage_id'],)).fetchall()]
        pref=cur.execute("SELECT ref FROM passage WHERE id=?",(v['passage_id'],)).fetchone()['ref']
    else: refs=[a.ref]; pref=a.ref+' (singleton)'
    spans, terms = load(cur, refs)
    # D14 passage + D13 cohabitation (implicit = the passage's other terms)
    print('PASSAGE %s  | anchor %s | %d spans %d terms'%(pref,refs[0],len(spans),len(terms)))
    print('D14 passage = %s ; D13 cohabitation (implicit co-terms) = %d terms in unit\n'%(pref,len(terms)))
    for t in terms:
        if t['cc']=='T2': continue
        res=derive(spans, terms, t)
        if not res: continue
        d,focal=res
        print('  %-9s %-8s "%s" [%s]%s'%(t['ref'],t['strong'],t['word'],t['cc'],'  <FOCAL>' if focal else ''))
        for k in ['D1 identity','D2 source','D3 seat','D4 operation','D5 target','D6 manner','D6 intensity','D8 effect','D9 coupling','D10 prohibition']:
            if d.get(k): print('       %-16s %s'%(k,d[k]))
        print()

if __name__=='__main__': main()
