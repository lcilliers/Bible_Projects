"""
_probe_lexical_derivation_harness_v2_passage_20260701.py  (READ-ONLY, PASSAGE-AWARE)

Round-3 fix: evaluate the whole PASSAGE as one unit (researcher: Exo 1:13 must be read with
its passage). Follows the stated processing algorithm:
  select verse -> is it in a passage? -> take the FIRST verse -> load ALL passage spans ->
  derive the operation(s) across the combined passage span-set (cross-verse), anchored on verse 1.

Same architecture: READ ONCE (one batch query for all passage spans/terms), parse morph once,
one function per item, rules build on each other. Adds cross-verse SOURCE / EFFECT / PROCESS,
which only appear at passage scope.

This does NOT write to the DB. Demo passage = Exo 1:11-14 (the oppression pericope; note the DB
currently splits it 1:11-12 and misses 1:13-14 — a marker under-detection to feed back).

Usage: python scripts/_probe_lexical_derivation_harness_v2_passage_20260701.py
"""
import sqlite3, os, re, collections
DB = os.path.join('database', 'bible_research.db')
PASSAGE = ['Exo 1:11', 'Exo 1:12', 'Exo 1:13', 'Exo 1:14']   # the passage, in order
ANCHOR_TERM = 'H6531'   # the operation we trace: ruthlessness (perek)

SEATS = {'H3820':'heart','H3824':'heart','H5315':'soul','H7307':'spirit','H1320':'flesh'}
# affect/driver lemmas that can be a SOURCE (a preceding inner driver). Small seed; grows.
DRIVERS = {'H6973':'dread','H3372':'fear','H3373':'fear','H0639':'anger','H2534':'wrath','H8130':'hatred'}
def canon(s):
    m = re.match(r'^([HG])(\d+)', s or ''); return m.group(1)+m.group(2).zfill(4) if m else s

def parse_morph(mc, pos):
    segs=(mc or '').split(); head=segs[0] if segs else ''
    f={'is_verb':pos=='verb','is_noun':pos=='noun','is_adj':pos=='adjective','state':None,'has_prep':False}
    if head.startswith('HN') and head and head[-1] in ('c','a'): f['state']='construct' if head[-1]=='c' else 'absolute'
    for s in segs:
        if s.startswith('HR'): f['has_prep']=True
    return f

def load_passage(conn, refs):
    conn.row_factory=sqlite3.Row; cur=conn.cursor()
    vs=cur.execute("SELECT id,reference,verse_text FROM verse WHERE reference IN (%s)"%','.join('?'*len(refs)),refs).fetchall()
    order={r:i for i,r in enumerate(refs)}
    vs=sorted(vs,key=lambda r:order[r['reference']])
    spans=[]  # combined, global order; each carries its verse ref + local index + stem
    terms=[]
    for v in vs:
        for m in cur.execute("SELECT word_index,surface,primary_strong,pos,morph_code,stem FROM verse_morphology WHERE verse_id=? ORDER BY word_index",(v['id'],)):
            spans.append({'ref':v['reference'],'w':m['word_index'],'surface':m['surface'],
                          'strong':canon(m['primary_strong']),'pos':m['pos'],'stem':m['stem'],
                          'feat':parse_morph(m['morph_code'],m['pos']),'g':len(spans)})
        for t in cur.execute("""SELECT w.term_id,w.mti_term_id,w.target_word,mt.owning_word,mt.cluster_code
            FROM wa_verse_records w LEFT JOIN mti_terms mt ON w.mti_term_id=mt.id
            WHERE w.verse_id=? AND COALESCE(w.delete_flagged,0)=0""",(v['id'],)):
            d=dict(t); d['ref']=v['reference']; d['strong']=canon(t['term_id']); terms.append(d)
    return vs[0], spans, terms

# ---- rules over the combined passage span-set ----
def occurrences(spans, strong):
    return [s for s in spans if s['strong']==strong]

def r_operations_governed(spans, strong):
    # verbs the manner-noun (perek) qualifies: for each occurrence, the nearest verb
    verbs=[s for s in spans if s['feat']['is_verb']]
    out=[]
    for occ in occurrences(spans,strong):
        if not verbs: continue
        vb=min(verbs,key=lambda s:abs(s['g']-occ['g']))
        out.append((occ['ref'], vb['surface'], vb['strong'], vb['stem']))
    return out

def r_manner_frame(spans, strong):
    occ=[o for o in occurrences(spans,strong) if o['feat']['has_prep'] or o['feat']['is_noun']]
    return ['%s @%s'%(o['surface'],o['ref']) for o in occ]

def r_source(spans, anchor_g):
    # nearest PRECEDING driver lemma (dread/fear/anger...) in the passage
    cands=[s for s in spans if s['strong'] in DRIVERS and s['g']<anchor_g]
    if not cands: return None
    d=max(cands,key=lambda s:s['g'])
    return '%s (%s) @%s'%(DRIVERS[d['strong']],d['strong'],d['ref'])

def r_effect(spans, anchor_g):
    # produced-state: a causative (Piel/Hiphil) verb AFTER the operation -> the effect it yields
    cands=[s for s in spans if s['feat']['is_verb'] and (s['stem'] in ('Piel','Hiphil')) and s['g']>=anchor_g]
    if not cands: return None
    e=min(cands,key=lambda s:s['g'])
    return '%s (%s, %s) @%s'%(e['surface'],e['strong'],e['stem'],e['ref'])

def r_process(spans, terms):
    # the ordered sequence of operation-verbs across the passage (the escalation chain)
    seq=[s for s in spans if s['feat']['is_verb']]
    return ' -> '.join('%s(%s)@%s'%(s['surface'],s['stem'] or 'Qal',s['ref']) for s in seq)

def r_target(spans, anchor_g):
    # the patient: nearest proper/people noun after the anchor
    for s in spans:
        if s['g']>anchor_g and s['feat']['is_noun'] and s['strong'] in ('H3478','H1121'):
            return '%s (%s) @%s'%(s['surface'],s['strong'],s['ref'])
    return None

def main():
    conn=sqlite3.connect(DB)
    anchor_v, spans, terms = load_passage(conn, PASSAGE)
    print('PASSAGE %s  (anchor: %s)'%(PASSAGE[0]+'-'+PASSAGE[-1].split(' ')[-1], anchor_v['reference']))
    for v in PASSAGE:
        vt=[s for s in spans if s['ref']==v]
        print('  %s: %s'%(v, ' '.join('%s'%s['surface'] for s in vt)))
    occ=occurrences(spans, ANCHOR_TERM)
    print('\nANCHOR OPERATION: ruthlessness (perek %s) — occurs %d× in passage: %s'%(
        ANCHOR_TERM, len(occ), ', '.join(o['ref'] for o in occ)))
    anchor_g = occ[0]['g'] if occ else 0
    print('\n=== derivation ACROSS THE PASSAGE ===')
    print('  manner-frame  : %s'%r_manner_frame(spans, ANCHOR_TERM))
    print('  operations    : %s'%['%s: %s(%s,%s)'%(r,su,st,stm) for (r,su,st,stm) in r_operations_governed(spans, ANCHOR_TERM)])
    print('  source (D2)   : %s'%(r_source(spans, anchor_g) or 'NONE'))
    print('  effect (D8)   : %s'%(r_effect(spans, anchor_g) or 'NONE'))
    print('  target (D5)   : %s'%(r_target(spans, anchor_g) or 'NONE'))
    print('  process (D7)  : %s'%r_process(spans, terms))
    print('\n=== vs ISOLATED Exo 1:13 (previous harness) ===')
    print('  source=NONE  effect=NONE  process=not-captured  manner=work only  (all impoverished)')

if __name__=='__main__':
    main()
