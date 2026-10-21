"""
_apply_write_ruthlessness_lexical_v1_20260702.py

FIRST REAL WRITE of the new-model verse-lexical. Derives the full D1-D14 lexical for ruthlessness
(perek H6531) across its 6 OT prose verses (passage-aware, genre-aware) and PERSISTS it to ve_lexical
as new-model rows, then marks each verse complete.

New-model rows are cleanly separable from legacy:
  * source_provenance = 'lexical-model-2026' ; pair_kind NOT NULL (legacy has pair_kind NULL)
  * ve_nr 101+ (new-model block; legacy is 0-29)
Storage per dimension value: ve_lexical(verse_context_id, ve_nr, ve_label, value, notes,
  source_provenance, from_span, to_span, direction, resolution, pair_kind).
verse.process_marker = 'ruthlessness-lexical-20260702' on completed verses.

Safe: backs up; dry-run default; verifies; additive (does not touch legacy). Reversible by
soft-deleting source_provenance='lexical-model-2026'.
Usage: python scripts/_apply_write_ruthlessness_lexical_v1_20260702.py [--live]
"""
import sqlite3, os, sys, re, shutil
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
TERM='H6531'; PROV='lexical-model-2026'; MARKER='ruthlessness-lexical-20260702'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
SEATS={'H3820':'heart','H3824':'heart','H5315':'soul','H7307':'spirit','H1320':'flesh'}
DRIVERS={'H6973':'dread','H3372':'fear','H3373':'fear','H0639':'anger','H2534':'wrath','H8130':'hatred/enmity','H7451':'evil','H2555':'violence'}
DIVINE={'H0430','H3068','H0410','H0433'}; NEG={'H3808','H0408'}; INTENS={'H3966':'very','H7227':'many','H3605':'all'}
# ve_nr / label / pair_kind per dimension
DIMS={'sense':(101,'value'),'type':(102,'value'),'source':(103,'pair'),'seat':(104,'pair'),'bearer':(105,'pair'),
      'operation':(106,'event'),'target':(107,'pair'),'manner':(108,'pair'),'intensity':(109,'value'),
      'effect':(111,'pair'),'coupling':(112,'pair'),'prohibition':(113,'flag'),'discovery':(114,'note')}
def canon(s):
    m=re.match(r'^([HG])(\d+)',s or ''); return m.group(1)+m.group(2).zfill(4) if m else s
def parse(mc,pos):
    segs=(mc or '').split(); head=segs[0] if segs else ''
    f={'v':pos=='verb','n':pos=='noun','a':pos=='adjective','proper':head.startswith('HNp'),'state':None,'prep':False,'obj':False}
    if head.startswith('HN') and head[-1] in ('c','a'): f['state']='construct' if head[-1]=='c' else 'absolute'
    for s in segs:
        if s.startswith('HR'): f['prep']=True
        if s=='HTo': f['obj']=True
    return f
def load(cur,refs):
    spans=[]
    for vi,ref in enumerate(refs):
        v=cur.execute("SELECT id FROM verse WHERE reference=?",(ref,)).fetchone()
        for m in cur.execute("SELECT surface,primary_strong,pos,stem,morph_code FROM verse_morphology WHERE verse_id=? ORDER BY word_index",(v['id'],)):
            spans.append({'ref':ref,'vi':vi,'surface':m['surface'],'strong':canon(m['primary_strong']),'pos':m['pos'],'stem':m['stem'],'feat':parse(m['morph_code'],m['pos']),'g':len(spans)})
    return spans
def terms_of(cur,refs):
    tstr=set()
    for ref in refs:
        v=cur.execute("SELECT id FROM verse WHERE reference=?",(ref,)).fetchone()
        for r in cur.execute("SELECT term_id FROM wa_verse_records WHERE verse_id=? AND COALESCE(delete_flagged,0)=0",(v['id'],)):
            tstr.add(canon(r['term_id']))
    return tstr

def derive(spans, tstr, ref):
    """Return list of (ve_label, value, from_span, to_span, resolution) for perek in THIS verse."""
    occ=[s for s in spans if s['strong']==canon(TERM) and s['ref']==ref]
    if not occ: return []
    s=occ[0]; g=s['g']; f=s['feat']; rows=[]
    vs=[x for x in spans if x['feat']['v'] and abs(x['g']-g)<=3]; vb=min(vs,key=lambda x:abs(x['g']-g)) if vs else None
    manner_noun=f['n'] and f['prep']
    def add(lbl,val,fr=None,to=None,res=None): rows.append((lbl,val,fr,to,res))
    add('sense', s['surface'])
    add('type', 'status' if f['n'] else 'action' if f['v'] else 'quality')
    if manner_noun and vb: add('operation', '(qualifies) %s'%vb['surface'], to='%s@%s'%(vb['strong'],vb['ref']))
    # seat
    seat=SEATS.get(s['strong'])
    if not seat and f['state']=='construct':
        for j in range(g+1,min(g+3,len(spans))):
            if spans[j]['strong'] in SEATS: seat=SEATS[spans[j]['strong']]; break
    if seat: add('seat', seat, fr=seat, to=s['strong'], res='span')
    # bearer
    ag=[x for x in spans if x['feat']['proper'] and x['g']<g and g-x['g']<=6]
    if ag: add('bearer', ag[-1]['surface'], fr=ag[-1]['strong'], to=s['strong'], res='span')
    # manner + coupling (perek is a manner-noun)
    if manner_noun and vb:
        add('manner', 'manner-of %s'%vb['surface'], fr=s['strong'], to='%s@%s'%(vb['strong'],vb['ref']), res='span')
        if vb['strong'] in tstr: add('coupling', 'welds %s'%vb['surface'], fr=s['strong'], to=vb['strong'], res='span')
    inten=sorted({INTENS[x['strong']] for x in spans if x['strong'] in INTENS and abs(x['g']-g)<=3})
    if inten: add('intensity', ', '.join(inten))
    # source (driver) with restraint -> discovery note
    restraint=None
    drv=[x for x in spans if x['strong'] in DRIVERS and x['strong']!=s['strong']]
    near=[x for x in drv if x['g']<g] or drv
    if near:
        e=near[-1]; fearish=e['strong'] in ('H3372','H3373'); divnear=any(x['strong'] in DIVINE and abs(x['g']-e['g'])<=2 for x in spans)
        if fearish and divnear: restraint='fear-of-God(%s)@%s'%(e['strong'],e['ref'])
        else: add('source', '%s@%s'%(DRIVERS[e['strong']],e['ref']), fr='%s@%s'%(e['strong'],e['ref']), to=s['strong'], res='span')
    # prohibition
    if any(x['strong'] in NEG and abs(x['g']-g)<=3 for x in spans): add('prohibition','forbidden (neg particle)')
    # discovery / notes
    notes=[]
    if restraint: notes.append('restrained-by: '+restraint)
    if not near: notes.append('source: none stated')
    if notes: add('discovery','; '.join(notes))
    return rows

def main():
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    # perek OT prose verses + their passage + verse_context_id for the perek term
    verses=cur.execute("""SELECT DISTINCT v.id vid, v.reference, v.passage_id, v.book_id, w.mti_term_id,
        (SELECT vc.id FROM verse_context vc WHERE vc.verse_record_id=w.id AND COALESCE(vc.delete_flagged,0)=0 LIMIT 1) vcid
        FROM wa_verse_records w JOIN verse v ON w.verse_id=v.id
        WHERE w.term_id LIKE ?||'%' AND COALESCE(w.delete_flagged,0)=0 ORDER BY v.book_id,v.chapter,v.verse_num""",(TERM,)).fetchall()
    plan=[]
    for v in verses:
        if v['book_id'] in (18,19,20,21,22): continue  # skip poetic (none for perek, but guard)
        refs=[r['reference'] for r in cur.execute("SELECT reference FROM verse WHERE passage_id=? ORDER BY book_id,chapter,verse_num",(v['passage_id'],)).fetchall()] if v['passage_id'] else [v['reference']]
        spans=load(cur,refs); tstr=terms_of(cur,refs)
        rows=derive(spans,tstr,v['reference'])
        plan.append((v['reference'],v['vcid'],rows))
    total=sum(len(r) for _,_,r in plan)
    print('perek OT verses: %d ; ve_lexical rows to write: %d'%(len(plan),total))
    for ref,vcid,rows in plan:
        print('  %-10s vc=%s : %s'%(ref,vcid,', '.join('%s=%s'%(l,(val or '')[:18]) for l,val,_,_,_ in rows)))
    if not LIVE:
        print('\nDRY-RUN. Re-run with --live.'); return
    shutil.copy2(DB,os.path.join('backups','bible_research.pre-ruthwrite.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    n=0
    for ref,vcid,rows in plan:
        if not vcid: print('  skip %s (no verse_context)'%ref); continue
        for lbl,val,fr,to,res in rows:
            ve_nr,pk=DIMS.get(lbl,(199,'value'))
            cur.execute("""INSERT INTO ve_lexical (verse_context_id,ve_nr,ve_label,value,notes,source_provenance,from_span,to_span,direction,resolution,pair_kind,delete_flagged,created_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,0,?)""",(vcid,ve_nr,lbl,val,None,PROV,fr,to,'1to2' if pk=='pair' else None,res,pk,NOW)); n+=1
        cur.execute("UPDATE verse SET process_marker=? WHERE reference=? AND (process_marker IS NULL OR process_marker LIKE 'lexical-v7%')",(MARKER,ref))
    conn.commit()
    print('\nwrote %d ve_lexical rows (prov=%s); marked %d verses (%s).'%(n,PROV,len(plan),MARKER))
    print('verify:', cur.execute("SELECT COUNT(*) FROM ve_lexical WHERE source_provenance=?",(PROV,)).fetchone()[0],'rows present')

if __name__=='__main__': main()
