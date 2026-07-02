"""
_apply_write_ruthlessness_passages_full_v2_20260702.py

Layer-1 FULL lexical: write ve_lexical for ALL non-T2 terms in ruthlessness's passages (not just
perek) so the full story of the underlying lexicals can be told. Supersedes the perek-only write
(soft-deletes prior source_provenance='lexical-model-2026' rows for these passages, rewrites all).

Reuses the v8 derivation (genre-aware, passage-loaded). New-model rows: pair columns set,
source_provenance='lexical-model-2026', ve_nr 101+. verse.process_marker='ruthlessness-lexical-20260702'.
Safe: backs up; dry-run default; additive to legacy; reversible.
Usage: python scripts/_apply_write_ruthlessness_passages_full_v2_20260702.py [--live]
"""
import sqlite3, os, sys, re, shutil
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
TERM='H6531'; PROV='lexical-model-2026'; MARKER='ruthlessness-lexical-20260702'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
SEATS={'H3820':'heart','H3824':'heart','H5315':'soul','H7307':'spirit','H1320':'flesh'}
DRIVERS={'H6973':'dread','H3372':'fear','H3373':'fear','H0639':'anger','H2534':'wrath','H8130':'hatred/enmity','H7451':'evil','H2555':'violence'}
DIVINE={'H0430','H3068','H0410','H0433'}; NEG={'H3808','H0408'}; INTENS={'H3966':'very','H7227':'many','H3605':'all'}
AFFECT_VICE={'M01','M02','M03','M06','M24','M27'}
DIMS={'sense':(101,'value'),'type':(102,'value'),'source':(103,'pair'),'seat':(104,'pair'),'bearer':(105,'pair'),
      'operation':(106,'event'),'target':(107,'pair'),'manner':(108,'pair'),'intensity':(109,'value'),
      'effect':(111,'pair'),'coupling':(112,'pair'),'prohibition':(113,'flag'),'discovery':(114,'note')}
def canon(s):
    m=re.match(r'^([HG])(\d+)',s or ''); return m.group(1)+m.group(2).zfill(4) if m else s
def genre(b):
    if 1<=b<=5: return 'prose'
    if b in (18,19,20,21,22): return 'poetic'
    return 'prose'
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

def derive(spans, tstr, term_strong, ref, cc, kind):
    occ=[s for s in spans if s['strong']==term_strong and s['ref']==ref]
    if not occ: return []
    s=occ[0]; g=s['g']; f=s['feat']; rows=[]
    vs=[x for x in spans if x['feat']['v'] and abs(x['g']-g)<=3]; vb=min(vs,key=lambda x:abs(x['g']-g)) if vs else None
    manner_noun=f['n'] and f['prep']
    def add(lbl,val,fr=None,to=None,res=None): rows.append((lbl,val,fr,to,res))
    add('sense', s['surface']); add('type','status' if f['n'] else 'action' if f['v'] else 'quality')
    if f['v']: add('operation', s['surface'])
    elif manner_noun and vb: add('operation','(qualifies) %s'%vb['surface'], to='%s@%s'%(vb['strong'],vb['ref']))
    seat=SEATS.get(s['strong'])
    if not seat and f['state']=='construct':
        for j in range(g+1,min(g+3,len(spans))):
            if spans[j]['strong'] in SEATS: seat=SEATS[spans[j]['strong']]; break
    if seat: add('seat',seat,fr=seat,to=s['strong'],res='span')
    ag=[x for x in spans if x['feat']['proper'] and x['g']<g and g-x['g']<=6]
    if ag: add('bearer', ag[-1]['surface'], fr=ag[-1]['strong'], to=s['strong'], res='span')
    if f['v']:
        objs=[x for x in spans if x['feat']['obj'] and x['feat']['n'] and not x['feat']['prep'] and x['vi']==s['vi'] and x['strong']!=s['strong']]
        if objs: o=min(objs,key=lambda x:abs(x['g']-g)); add('target','%s'%o['surface'],fr=s['strong'],to=o['strong'],res='span')
    if manner_noun and vb:
        add('manner','manner-of %s'%vb['surface'],fr=s['strong'],to='%s@%s'%(vb['strong'],vb['ref']),res='span')
        if vb['strong'] in tstr: add('coupling','welds %s'%vb['surface'],fr=s['strong'],to=vb['strong'],res='span')
    inten=sorted({INTENS[x['strong']] for x in spans if x['strong'] in INTENS and abs(x['g']-g)<=3})
    if inten: add('intensity',', '.join(inten))
    focal=f['v'] or manner_noun
    restraint=None
    if focal and (cc in AFFECT_VICE or s['strong'] in DRIVERS) and kind=='prose':
        drv=[x for x in spans if x['strong'] in DRIVERS and x['strong']!=s['strong']]; near=[x for x in drv if x['g']<g] or drv
        if near:
            e=near[-1]; fearish=e['strong'] in ('H3372','H3373'); divnear=any(x['strong'] in DIVINE and abs(x['g']-e['g'])<=2 for x in spans)
            if fearish and divnear: restraint='fear-of-God@%s'%e['ref']
            else: add('source','%s@%s'%(DRIVERS[e['strong']],e['ref']),fr='%s@%s'%(e['strong'],e['ref']),to=s['strong'],res='span')
    if f['v'] and kind=='prose':
        c=[x for x in spans if x['feat']['v'] and x['stem'] in ('Piel','Hiphil') and x['g']>g and x['strong']!=s['strong'] and x['strong'] in tstr and 0<=x['vi']-s['vi']<=1]
        if c: e=c[0]; add('effect','%s'%e['surface'],fr=s['strong'],to='%s@%s'%(e['strong'],e['ref']),res='span')
    if any(x['strong'] in NEG and abs(x['g']-g)<=3 for x in spans): add('prohibition','forbidden (neg particle)')
    notes=[]
    if restraint: notes.append('restrained-by: '+restraint)
    if notes: add('discovery','; '.join(notes))
    return rows

def main():
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    pids=[r['passage_id'] for r in cur.execute("SELECT DISTINCT v.passage_id FROM wa_verse_records w JOIN verse v ON w.verse_id=v.id WHERE w.term_id LIKE ?||'%' AND COALESCE(w.delete_flagged,0)=0 AND v.passage_id IS NOT NULL",(TERM,)).fetchall()]
    plan=[]  # (ref, vcid, term_strong, rows)
    for pid in pids:
        refs=[r['reference'] for r in cur.execute("SELECT reference FROM verse WHERE passage_id=? ORDER BY book_id,chapter,verse_num",(pid,)).fetchall()]
        book=cur.execute("SELECT book_id FROM verse WHERE passage_id=? LIMIT 1",(pid,)).fetchone()['book_id']
        kind=genre(book); spans=load(cur,refs)
        tstr=set(s['strong'] for s in spans)  # any strong present
        # all non-T2 terms per verse
        for ref in refs:
            v=cur.execute("SELECT id FROM verse WHERE reference=?",(ref,)).fetchone()
            for w in cur.execute("""SELECT w.id wid, w.term_id, mt.cluster_code cc FROM wa_verse_records w
                LEFT JOIN mti_terms mt ON w.mti_term_id=mt.id WHERE w.verse_id=? AND COALESCE(w.delete_flagged,0)=0""",(v['id'],)).fetchall():
                if w['cc']=='T2': continue
                vc=cur.execute("SELECT id FROM verse_context WHERE verse_record_id=? AND COALESCE(delete_flagged,0)=0 LIMIT 1",(w['wid'],)).fetchone()
                if not vc: continue
                rows=derive(spans, tstr, canon(w['term_id']), ref, w['cc'], kind)
                if rows: plan.append((ref, vc['id'], canon(w['term_id']), rows))
    total=sum(len(r) for _,_,_,r in plan)
    print('passages: %d ; term-in-verse records: %d ; ve_lexical rows: %d'%(len(pids),len(plan),total))
    if not LIVE:
        print('DRY-RUN. Re-run with --live.'); return
    shutil.copy2(DB,os.path.join('backups','bible_research.pre-fullwrite.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    # supersede prior perek-only rows in these passages
    vcids=tuple(set(p[1] for p in plan)) or (0,)
    cur.execute("UPDATE ve_lexical SET delete_flagged=1 WHERE source_provenance=? AND verse_context_id IN (%s)"%','.join('?'*len(vcids)),(PROV,)+vcids)
    n=0
    for ref,vcid,ts,rows in plan:
        for lbl,val,fr,to,res in rows:
            ve_nr,pk=DIMS.get(lbl,(199,'value'))
            cur.execute("""INSERT INTO ve_lexical (verse_context_id,ve_nr,ve_label,value,notes,source_provenance,from_span,to_span,direction,resolution,pair_kind,delete_flagged,created_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,0,?)""",(vcid,ve_nr,lbl,val,None,PROV,fr,to,'1to2' if pk=='pair' else None,res,pk,NOW)); n+=1
        cur.execute("UPDATE verse SET process_marker=? WHERE reference=?",(MARKER,ref))
    conn.commit()
    print('wrote %d rows across %d term-in-verse records (prov=%s).'%(n,len(plan),PROV))

if __name__=='__main__': main()
