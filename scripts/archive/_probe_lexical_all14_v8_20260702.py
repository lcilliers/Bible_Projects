"""
_probe_lexical_all14_v8_20260702.py  (READ-ONLY)

Refinement cycle for all D1-D14, tested per genre. Fixes over v6/v7:
  * D2 source  -> distinguish DRIVER from RESTRAINT (fear-of-God / prohibition-contrast frame ->
                 restraint, recorded in D11, NOT source).
  * D3 bearer  -> derive the bearer/subject (the one who does it): the term's suffix owner, else the
                 nearest preceding agent (proper noun / subject pronoun).
  * D5 target  -> HTo direct-object, preferring the closest person/group patient.
  * genre gate -> poetic/wisdom = per-verse (Phase 1); cross-verse items OFF.
Usage: python scripts/_probe_lexical_all14_v8_20260702.py --ref "Exo 1:13"
"""
import sqlite3, os, re, argparse
DB=os.path.join('database','bible_research.db')
SEATS={'H3820':'heart','H3824':'heart','H5315':'soul','H7307':'spirit','H1320':'flesh','H3629':'kidneys'}
DRIVERS={'H6973':'dread','H3372':'fear','H3373':'fear','H0639':'anger','H2534':'wrath','H8130':'hatred/enmity','H7451':'evil','H2555':'violence'}
DIVINE={'H0430','H3068','H0410','H0433'}      # Elohim/YHWH/El/Eloah
AFFECT_VICE={'M01','M02','M03','M06','M24','M27'}
PERSONISH=('proper',)  # heuristic: proper nouns / pronouns are agent/patient candidates
NEG={'H3808','H0408','G3361'}; INTENS={'H3966':'very','H7227':'many','H3605':'all'}
CONTRAST={'H3588'}  # ki (but/rather in some frames) — weak signal
def canon(s):
    m=re.match(r'^([HG])(\d+)',s or ''); return m.group(1)+m.group(2).zfill(4) if m else s
def genre(b):
    if 1<=b<=5: return ('law/narrative','prose')
    if 6<=b<=17: return ('narrative','prose')
    if b in (18,19,20,21,22): return ('poetic/wisdom','poetic')
    if 23<=b<=39: return ('prophetic','prose')
    if 40<=b<=44: return ('gospel-narrative','prose')
    return ('epistle','prose')
def parse(mc,pos):
    segs=(mc or '').split(); head=segs[0] if segs else ''
    f={'v':pos=='verb','n':pos=='noun','a':pos=='adjective','proper':False,'state':None,'prep':False,'obj':False,'suf':False}
    if head.startswith('HNp'): f['proper']=True
    if head.startswith('HN') and head[-1] in ('c','a'): f['state']='construct' if head[-1]=='c' else 'absolute'
    for s in segs:
        if s.startswith('HR'): f['prep']=True
        if s=='HTo': f['obj']=True
        if s.startswith('HS'): f['suf']=True
    return f
def load(cur, refs):
    spans=[]; terms=[]
    for vi,ref in enumerate(refs):
        v=cur.execute("SELECT id FROM verse WHERE reference=?",(ref,)).fetchone()
        for m in cur.execute("SELECT surface,primary_strong,pos,stem,morph_code FROM verse_morphology WHERE verse_id=? ORDER BY word_index",(v['id'],)):
            spans.append({'ref':ref,'vi':vi,'surface':m['surface'],'strong':canon(m['primary_strong']),'pos':m['pos'],'stem':m['stem'],'feat':parse(m['morph_code'],m['pos']),'g':len(spans)})
        for t in cur.execute("""SELECT w.term_id,w.target_word,mt.cluster_code FROM wa_verse_records w LEFT JOIN mti_terms mt ON w.mti_term_id=mt.id
            WHERE w.verse_id=? AND COALESCE(w.delete_flagged,0)=0""",(v['id'],)):
            terms.append({'ref':ref,'strong':canon(t['term_id']),'word':t['target_word'],'cc':t['cluster_code']})
    return spans,terms
def occ(spans,strong):
    for s in spans:
        if s['strong']==strong: return s
def govverb(spans,g):
    vs=[s for s in spans if s['feat']['v'] and abs(s['g']-g)<=3]
    return min(vs,key=lambda s:abs(s['g']-g)) if vs else None

def derive(spans,terms,term,kind):
    s=occ(spans,term['strong']);
    if not s: return None
    g=s['g']; f=s['feat']; cc=term['cc']; tstr={t['strong'] for t in terms}; d={}
    vb=govverb(spans,g); manner_noun=f['n'] and f['prep']
    d['D1 identity']='%s / %s'%(term['word'] or s['surface'],'action' if f['v'] else 'status' if f['n'] else 'quality' if f['a'] else '?')
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
    # D3 bearer: suffix owner else nearest preceding agent (proper noun) within 4
    bearer=None
    ag=[x for x in spans if x['feat']['proper'] and x['g']<g and g-x['g']<=6]
    if ag: bearer=ag[-1]['surface']
    d['D3 bearer']=bearer
    # D5 target: VERB-terms only; a same-verse, non-preposition HTo object (excludes manner-nouns).
    tgt=None
    if f['v']:
        objs=[x for x in spans if x['feat']['obj'] and x['feat']['n'] and not x['feat']['prep'] and x['vi']==s['vi'] and x['strong']!=s['strong']]
        if objs: o=min(objs,key=lambda x:abs(x['g']-g)); tgt='%s(%s)'%(o['surface'],o['strong'])
    d['D5 target']=tgt
    # D6 manner + intensity
    d['D6 manner']=('manner-of %s(%s)'%(vb['surface'],vb['strong'])) if (manner_noun and vb) else None
    d['D6 intensity']=', '.join(sorted({INTENS[x['strong']] for x in spans if x['strong'] in INTENS and abs(x['g']-g)<=3})) or None
    focal=f['v'] or manner_noun
    # D2 source with DRIVER vs RESTRAINT
    src=None; restraint=None
    if focal and (cc in AFFECT_VICE or s['strong'] in DRIVERS) and kind=='prose':
        drv=[x for x in spans if x['strong'] in DRIVERS and x['strong']!=s['strong']]
        near=[x for x in drv if x['g']<g] or drv
        if near:
            e=near[-1]
            # restraint test: fear-type with a divine lemma within +/-2, or a neg particle near it
            fearish=e['strong'] in ('H3372','H3373')
            divnear=any(x['strong'] in DIVINE and abs(x['g']-e['g'])<=2 for x in spans)
            negnear=any(x['strong'] in NEG and abs(x['g']-e['g'])<=3 for x in spans)
            if fearish and (divnear or negnear):
                restraint='%s(%s)@%s'%('fear-of-God' if divnear else 'fear',e['strong'],e['ref'])
            else:
                src='%s(%s)@%s'%(DRIVERS[e['strong']],e['strong'],e['ref'])
    d['D2 source']=src
    # D8 effect (prose, +/-1 verse)
    eff=None
    if f['v'] and kind=='prose':
        c=[x for x in spans if x['feat']['v'] and x['stem'] in ('Piel','Hiphil') and x['g']>g and x['strong']!=s['strong'] and x['strong'] in tstr and 0<=x['vi']-s['vi']<=1]
        if c: e=c[0]; eff='%s(%s,%s)@%s'%(e['surface'],e['strong'],e['stem'],e['ref'])
    d['D8 effect']=eff
    # D9 coupling
    d['D9 coupling']=('welds %s(%s)'%(vb['surface'],vb['strong'])) if (manner_noun and vb and vb['strong'] in tstr) else None
    # D10 prohibition
    d['D10 prohibition']='forbidden (neg)' if any(x['strong'] in NEG and abs(x['g']-g)<=3 for x in spans) else None
    # D11 discovery / uncertainty notes
    notes=[]
    if restraint: notes.append('restrained-by: '+restraint)
    if manner_noun and not d['D9 coupling']: notes.append('manner-noun, no co-term weld')
    if focal and cc in AFFECT_VICE and kind=='prose' and not src and not restraint: notes.append('source: none found')
    if kind=='poetic': notes.append('poetic: cross-verse deferred to phase-2 poem read')
    d['D11 notes']='; '.join(notes) or None
    return d

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ref',default='Exo 1:13'); a=ap.parse_args()
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    v=cur.execute("SELECT passage_id,book_id FROM verse WHERE reference=?",(a.ref,)).fetchone()
    gk,kind=genre(v['book_id'])
    if kind=='poetic': refs=[a.ref]; pref=a.ref+' (poetic: phase-1 per-verse)'
    elif v['passage_id']:
        refs=[r['reference'] for r in cur.execute("SELECT reference FROM verse WHERE passage_id=? ORDER BY book_id,chapter,verse_num",(v['passage_id'],)).fetchall()]
        pref=cur.execute("SELECT ref FROM passage WHERE id=?",(v['passage_id'],)).fetchone()['ref']
    else: refs=[a.ref]; pref=a.ref+' (singleton)'
    spans,terms=load(cur,refs)
    print('PASSAGE %s | genre=%s (%s) | anchor %s\n'%(pref,gk,kind,refs[0]))
    for t in terms:
        if t['cc']=='T2': continue
        d=derive(spans,terms,t,kind)
        if not d: continue
        print('  %-9s %-8s "%s" [%s]'%(t['ref'],t['strong'],t['word'],t['cc']))
        for k in ['D1 identity','D2 source','D3 seat','D3 bearer','D4 operation','D5 target','D6 manner','D6 intensity','D8 effect','D9 coupling','D10 prohibition','D11 notes']:
            if d.get(k): print('       %-16s %s'%(k,d[k]))
        print()

if __name__=='__main__': main()
