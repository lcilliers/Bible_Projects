"""
_probe_lexical_derivation_end_to_end_v4_20260701.py  (READ-ONLY)

End-to-end: consecutive-run PASSAGE -> startup validators -> anchor -> load all morphology together
-> derive every term's lexical items across the passage. Shows the full result for a decision.

Flow (exactly the agreed pipeline):
  1. start verse -> passage via verse.passage_id (the consecutive run)   [Validator A = lookup]
  2. all member spans present in verse_morphology                        [Validator B]
  3. anchor = first verse (ve-records attach here)
  4. read ALL passage morphology together (one batch)
  5. derive each non-T2 term across the passage span-set

Usage: python scripts/_probe_lexical_derivation_end_to_end_v4_20260701.py [--ref "Exo 1:13"]
"""
import sqlite3, os, re, sys, argparse
DB=os.path.join('database','bible_research.db')
SEATS={'H3820':'heart','H3824':'heart','H5315':'soul','H7307':'spirit','H1320':'flesh'}
DRIVERS={'H6973':'dread','H3372':'fear','H3373':'fear','H0639':'anger','H2534':'wrath','H8130':'hatred','H6031':'affliction'}
def canon(s):
    m=re.match(r'^([HG])(\d+)',s or ''); return m.group(1)+m.group(2).zfill(4) if m else s
def parse(mc,pos):
    segs=(mc or '').split(); head=segs[0] if segs else ''
    f={'v':pos=='verb','n':pos=='noun','a':pos=='adjective','state':None,'prep':False}
    if head.startswith('HN') and head[-1] in ('c','a'): f['state']='construct' if head[-1]=='c' else 'absolute'
    for s in segs:
        if s.startswith('HR'): f['prep']=True
    return f

def load(cur, refs):
    spans=[]; terms=[]
    for ref in refs:
        v=cur.execute("SELECT id,reference FROM verse WHERE reference=?",(ref,)).fetchone()
        for m in cur.execute("SELECT word_index,surface,primary_strong,pos,stem,morph_code FROM verse_morphology WHERE verse_id=? ORDER BY word_index",(v['id'],)):
            spans.append({'ref':ref,'surface':m['surface'],'strong':canon(m['primary_strong']),'pos':m['pos'],
                          'stem':m['stem'],'feat':parse(m['morph_code'],m['pos']),'g':len(spans)})
        for t in cur.execute("""SELECT w.term_id,w.target_word,mt.owning_word,mt.cluster_code FROM wa_verse_records w
            LEFT JOIN mti_terms mt ON w.mti_term_id=mt.id WHERE w.verse_id=? AND COALESCE(w.delete_flagged,0)=0""",(v['id'],)):
            terms.append({'ref':ref,'strong':canon(t['term_id']),'word':t['target_word'],'gloss':t['owning_word'],'cc':t['cluster_code']})
    return spans, terms

def first_occ(spans, strong):
    for s in spans:
        if s['strong']==strong: return s
    return None
def nearest_verb(spans, g):
    vs=[s for s in spans if s['feat']['v']]; return min(vs,key=lambda s:abs(s['g']-g)) if vs else None

def derive(spans, terms, term):
    s=first_occ(spans, term['strong'])
    if not s: return None
    g=s['g']; f=s['feat']; out={}
    out['sense']=term['word'] or s['surface']
    out['type']='action' if f['v'] else 'status' if f['n'] else 'quality' if f['a'] else '?'
    vb=nearest_verb(spans,g)
    out['operation']='%s(%s)'%(vb['surface'],vb['strong']) if vb else None
    # seat: construct chain to a seat
    seat=None
    if s['strong'] in SEATS: seat=SEATS[s['strong']]
    elif f['state']=='construct':
        for j in range(g+1,min(g+3,len(spans))):
            if spans[j]['strong'] in SEATS: seat=SEATS[spans[j]['strong']]; break
    out['seat']=seat
    # manner: prep-marked noun -> manner of verb
    out['manner']=('manner-of %s(%s)'%(vb['surface'],vb['strong'])) if (f['n'] and f['prep'] and vb) else None
    # target: object of the term's verb (skip prep-marked manner nouns)
    tgt=None
    if f['v']:
        for j in range(g+1,len(spans)):
            if spans[j]['feat']['n'] and not spans[j]['feat']['prep']:
                tgt='%s(%s)'%(spans[j]['surface'],spans[j]['strong']); break
    out['target']=tgt
    # source: nearest PRECEDING driver lemma in the passage
    drv=[x for x in spans if x['strong'] in DRIVERS and x['g']<g]
    out['source']=('%s(%s)@%s'%(DRIVERS[drv[-1]['strong']],drv[-1]['strong'],drv[-1]['ref'])) if drv else None
    # effect: produced-state (Piel/Hiphil) verb AFTER, excluding the term's own operation verb
    eff=[x for x in spans if x['feat']['v'] and x['stem'] in ('Piel','Hiphil') and x['g']>g and (not vb or x['strong']!=vb['strong'])]
    out['effect']=('%s(%s,%s)@%s'%(eff[0]['surface'],eff[0]['strong'],eff[0]['stem'],eff[0]['ref'])) if eff else None
    # coupling: morphological weld only (prep-manner to a co-term verb)
    tstr={t['strong'] for t in terms}
    cpl=None
    if f['n'] and f['prep'] and vb and vb['strong'] in tstr:
        cpl='welds %s(%s) as manner'%(vb['surface'],vb['strong'])
    out['coupling']=cpl if 'cpl' in dir() else None
    out['coupling']=cpl
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ref',default='Exo 1:13'); a=ap.parse_args()
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    v=cur.execute("SELECT id,passage_id,is_passage_anchor FROM verse WHERE reference=?",(a.ref,)).fetchone()
    # 1. passage membership
    if v['passage_id']:
        pv=cur.execute("SELECT reference FROM verse WHERE passage_id=? ORDER BY book_id,chapter,verse_num",(v['passage_id'],)).fetchall()
        refs=[r['reference'] for r in pv]
        pref=cur.execute("SELECT ref FROM passage WHERE id=?",(v['passage_id'],)).fetchone()['ref']
    else:
        refs=[a.ref]; pref=a.ref+' (singleton)'
    print('START %s  ->  PASSAGE %s  (%d verses)'%(a.ref,pref,len(refs)))
    # 2. validator B
    miss=[r for r in refs if cur.execute("SELECT COUNT(*) FROM verse_morphology m JOIN verse v ON m.verse_id=v.id WHERE v.reference=?",(r,)).fetchone()[0]==0]
    print('Validator B (spans in DB): %s'%('BLOCKED '+str(miss) if miss else 'OK'))
    if miss: return
    # 3. anchor
    anchor=refs[0]; print('anchor (ve-records attach here): %s\n'%anchor)
    # 4. load all morphology
    spans, terms = load(cur, refs)
    print('loaded %d spans, %d tagged terms across the passage\n'%(len(spans),len(terms)))
    # 5. derive each non-T2 term
    for t in terms:
        if t['cc']=='T2': continue
        d=derive(spans, terms, t)
        if not d: continue
        print('  %-9s %-8s "%s" [%s]'%(t['ref'],t['strong'],t['word'],t['cc']))
        for k in ['sense','type','operation','seat','target','manner','source','effect','coupling']:
            if d.get(k): print('       %-10s = %s'%(k,d[k]))
        print()

if __name__=='__main__': main()
