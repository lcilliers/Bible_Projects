"""
_probe_lexical_derivation_all14_v6_20260701.py  (READ-ONLY)

Round-B refinement of the full 14-dimension deriver. Fixes over-application found in v5:
  * D4 operation  -> only for action-terms (the term is the act) or a prep-manner noun (its governed
                    verb); pure status/quality object-nouns get NONE.
  * D8 effect     -> a produced-state (Piel/Hiphil) that IS a term, within +2 verses, distinct from
                    the operation; else NONE (kills multiplied->afflict-4-verses-away).
  * D2 source     -> only for focal terms in an AFFECT/VICE cluster (seed set) or a driver lemma;
                    service/lives/multiply no longer get a spurious source.
  * D7 process    -> passage-level: the ordered chain of focal AFFECT/VICE/oppression operations.
Usage: python scripts/_probe_lexical_derivation_all14_v6_20260701.py [--ref "Exo 1:13"]
"""
import sqlite3, os, re, argparse
DB=os.path.join('database','bible_research.db')
SEATS={'H3820':'heart','H3824':'heart','H5315':'soul','H7307':'spirit','H1320':'flesh','H3629':'kidneys'}
DRIVERS={'H6973':'dread','H3372':'fear','H3373':'fear','H0639':'anger','H2534':'wrath','H8130':'hatred/enmity',
         'H6031':'affliction','H7451':'evil','H2555':'violence'}
AFFECT_VICE={'M01','M02','M03','M06','M24','M27'}   # fear/anger/grief/ruthlessness/affliction/distress (SEED)
ET='H0853'; NEG={'H3808','H0408','G3361'}; INTENS={'H3966':'very','H7227':'many','H3605':'all'}
def canon(s):
    m=re.match(r'^([HG])(\d+)',s or ''); return m.group(1)+m.group(2).zfill(4) if m else s
def parse(mc,pos):
    segs=(mc or '').split(); head=segs[0] if segs else ''
    f={'v':pos=='verb','n':pos=='noun','a':pos=='adjective','state':None,'prep':False,'obj':False}
    if head.startswith('HN') and head[-1] in ('c','a'): f['state']='construct' if head[-1]=='c' else 'absolute'
    for s in segs:
        if s.startswith('HR'): f['prep']=True
        if s=='HTo': f['obj']=True   # direct-object marker (et) attached to the noun
    return f

def load(cur, refs):
    spans=[]; terms=[]
    for vi,ref in enumerate(refs):
        v=cur.execute("SELECT id FROM verse WHERE reference=?",(ref,)).fetchone()
        for m in cur.execute("SELECT word_index,surface,primary_strong,pos,stem,morph_code FROM verse_morphology WHERE verse_id=? ORDER BY word_index",(v['id'],)):
            spans.append({'ref':ref,'vi':vi,'surface':m['surface'],'strong':canon(m['primary_strong']),'pos':m['pos'],
                          'stem':m['stem'],'feat':parse(m['morph_code'],m['pos']),'g':len(spans)})
        for t in cur.execute("""SELECT w.term_id,w.target_word,mt.owning_word,mt.cluster_code FROM wa_verse_records w
            LEFT JOIN mti_terms mt ON w.mti_term_id=mt.id WHERE w.verse_id=? AND COALESCE(w.delete_flagged,0)=0""",(v['id'],)):
            terms.append({'ref':ref,'vi':vi,'strong':canon(t['term_id']),'word':t['target_word'],'gloss':t['owning_word'],'cc':t['cluster_code']})
    return spans, terms

def occ(spans,strong):
    for s in spans:
        if s['strong']==strong: return s
def gov_verb(spans,g):
    vs=[s for s in spans if s['feat']['v'] and abs(s['g']-g)<=3]
    return min(vs,key=lambda s:abs(s['g']-g)) if vs else None
def obj_of(spans,vg):
    # direct object = the nearest HTo-marked noun in either direction within the clause (+/-4)
    cands=[s for s in spans if s['feat']['n'] and s['feat']['obj'] and abs(s['g']-vg)<=4]
    return min(cands,key=lambda s:abs(s['g']-vg)) if cands else None

def derive(spans, terms, term):
    s=occ(spans,term['strong'])
    if not s: return None
    g=s['g']; f=s['feat']; cc=term['cc']; tstr={t['strong'] for t in terms}; d={}
    d['D1 identity']='%s / %s'%(term['word'] or s['surface'],'action' if f['v'] else 'status' if f['n'] else 'quality' if f['a'] else '?')
    vb=gov_verb(spans,g)
    manner_noun = f['n'] and f['prep']
    # D4 operation
    if f['v']: d['D4 operation']='%s(%s%s)'%(s['surface'],s['strong'],','+s['stem'] if s['stem'] else '')
    elif manner_noun and vb: d['D4 operation']='(qualifies) %s(%s)'%(vb['surface'],vb['strong'])
    else: d['D4 operation']=None
    # D3 seat
    seat=SEATS.get(s['strong'])
    if not seat and f['state']=='construct':
        for j in range(g+1,min(g+3,len(spans))):
            if spans[j]['strong'] in SEATS: seat=SEATS[spans[j]['strong']]; break
    d['D3 seat']=seat
    # D5 target: et-marked object of the term's verb
    tgt=None
    if f['v']:
        o=obj_of(spans,g)
        if o: tgt='%s(%s)'%(o['surface'],o['strong'])
    d['D5 target']=tgt
    # D6 manner + intensity
    d['D6 manner']=('manner-of %s(%s)'%(vb['surface'],vb['strong'])) if (manner_noun and vb) else None
    inten=sorted({INTENS[x['strong']] for x in spans if x['strong'] in INTENS and abs(x['g']-g)<=3})
    d['D6 intensity']=', '.join(inten) or None
    focal = f['v'] or manner_noun
    # D2 source: affect/vice focal term -> nearest preceding driver
    src=None
    if focal and (cc in AFFECT_VICE or s['strong'] in DRIVERS):
        drv=[x for x in spans if x['strong'] in DRIVERS and x['g']<g and x['strong']!=s['strong']]
        if drv: e=drv[-1]; src='%s(%s)@%s'%(DRIVERS[e['strong']],e['strong'],e['ref'])
    d['D2 source']=src
    # D8 effect: focal action -> produced-state (Piel/Hiphil) term within +2 verses, distinct
    eff=None
    if f['v']:
        c=[x for x in spans if x['feat']['v'] and x['stem'] in ('Piel','Hiphil') and x['g']>g and x['strong']!=s['strong'] and x['strong'] in tstr and 0<=x['vi']-s['vi']<=1]
        if c: e=c[0]; eff='%s(%s,%s)@%s'%(e['surface'],e['strong'],e['stem'],e['ref'])
    d['D8 effect']=eff
    # D9 coupling: weld
    d['D9 coupling']=('welds %s(%s) as manner'%(vb['surface'],vb['strong'])) if (manner_noun and vb and vb['strong'] in tstr) else None
    # D10 prohibition
    d['D10 prohibition']='forbidden (neg particle)' if any(x['strong'] in NEG and abs(x['g']-g)<=3 for x in spans) else None
    return d, focal, cc

def process_chain(spans, terms):
    tstr={t['strong']:t for t in terms}
    seq=[s for s in spans if s['feat']['v'] and (tstr.get(s['strong']) and tstr[s['strong']]['cc'] in AFFECT_VICE)]
    return ' -> '.join('%s@%s'%(s['surface'],s['ref']) for s in seq)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ref',default='Exo 1:13'); a=ap.parse_args()
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    v=cur.execute("SELECT passage_id FROM verse WHERE reference=?",(a.ref,)).fetchone()
    if v and v['passage_id']:
        refs=[r['reference'] for r in cur.execute("SELECT reference FROM verse WHERE passage_id=? ORDER BY book_id,chapter,verse_num",(v['passage_id'],)).fetchall()]
        pref=cur.execute("SELECT ref FROM passage WHERE id=?",(v['passage_id'],)).fetchone()['ref']
    else: refs=[a.ref]; pref=a.ref+' (singleton)'
    spans,terms=load(cur,refs)
    print('PASSAGE %s | anchor %s | %d spans %d terms'%(pref,refs[0],len(spans),len(terms)))
    print('D7 process (passage) = %s'%(process_chain(spans,terms) or 'none'))
    print('D14 passage=%s ; D13 cohabitation (implicit co-terms)=%d\n'%(pref,len([t for t in terms if t['cc']!='T2'])))
    for t in terms:
        if t['cc']=='T2': continue
        r=derive(spans,terms,t)
        if not r: continue
        d,focal,cc=r
        print('  %-9s %-8s "%s" [%s]%s'%(t['ref'],t['strong'],t['word'],t['cc'],'  <FOCAL>' if focal else ''))
        for k in ['D1 identity','D2 source','D3 seat','D4 operation','D5 target','D6 manner','D6 intensity','D8 effect','D9 coupling','D10 prohibition']:
            if d.get(k): print('       %-16s %s'%(k,d[k]))
        print()

if __name__=='__main__': main()
