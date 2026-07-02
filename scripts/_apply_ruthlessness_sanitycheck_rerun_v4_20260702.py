"""
_apply_ruthlessness_sanitycheck_rerun_v4_20260702.py

Re-run the pipeline for the 5 ruthlessness passages WITH the sanity-check gate (method §13):
  (a) PASSAGE-BOUNDARY verification — confirm each is a maximal consecutive run (the verse before
      start / after end is NOT in the DB); flag any that should extend (i.e., a candidate is
      actually part of a longer passage).
  (b) Re-derive index-driven (both gates) with the BEARER fix (exclude object/HTo proper nouns).
  (c) SANITY-CHECK EVALUATION assigns a ROLE per span (ve_nr 115) and writes it into the ve records:
        characteristic = gate-1 disposition (cluster in {M01,M02,M03,M06,M27}, type status/quality)
        standalone     = binds to nothing (no relational pair, not referenced, not a gate-1 operation)
        process-qualifier = otherwise (gives value/context to a binding pair)
  Supersedes prior lexical-model-2026 rows in these passages. Safe: backup, dry-run, verify.
Usage: python scripts/_apply_ruthlessness_sanitycheck_rerun_v4_20260702.py [--live]
"""
import sqlite3, os, sys, re, shutil, collections
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
TERM='H6531'; PROV='lexical-model-2026'; MARKER='ruthlessness-sanitychecked-20260702'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
SEATS={'H3820':'heart','H3824':'heart','H5315':'soul','H7307':'spirit','H1320':'flesh'}
DRIVERS={'H6973':'dread','H3372':'fear','H3373':'fear','H0639':'anger','H2534':'wrath','H8130':'hatred/enmity','H7451':'evil','H2555':'violence'}
DIVINE={'H0430','H3068','H0410','H0433'}; NEG={'H3808','H0408'}; INTENS={'H3966':'very','H7227':'many','H3605':'all'}
DISP={'M01','M02','M03','M06','M27'}   # affect/vice DISPOSITION clusters (characteristic candidates)
AFFECT_VICE={'M01','M02','M03','M06','M24','M27'}
FUNCTION={'particle','preposition','conjunction','suffix','pronoun'}
REL={'coupling','manner','source','effect','target','seat','bearer'}
DIMS={'sense':(101,'value'),'type':(102,'value'),'source':(103,'pair'),'seat':(104,'pair'),'bearer':(105,'pair'),
      'operation':(106,'event'),'target':(107,'pair'),'manner':(108,'pair'),'intensity':(109,'value'),
      'effect':(111,'pair'),'coupling':(112,'pair'),'prohibition':(113,'flag'),'discovery':(114,'note'),'role':(115,'value')}
def canon(s):
    m=re.match(r'^([HG])(\d+)',s or ''); return m.group(1)+m.group(2).zfill(4) if m else s
def morphfeat(mc,pos):
    segs=(mc or '').split(); head=segs[0] if segs else ''
    f={'v':pos=='verb','n':pos=='noun','a':pos=='adjective','proper':head.startswith('HNp'),'state':None,'prep':False,'obj':False}
    if head.startswith('HN') and head[-1] in ('c','a'): f['state']='construct' if head[-1]=='c' else 'absolute'
    for s in segs:
        if s.startswith('HR'): f['prep']=True
        if s=='HTo': f['obj']=True
    return f
def load(cur, refs):
    spans=[]
    for vi,ref in enumerate(refs):
        for m in cur.execute("""SELECT si.id sid,si.surface,si.primary_strong ps,si.pos,si.stem,si.morph_code
             FROM verse_span_index si JOIN verse v ON si.verse_id=v.id WHERE v.reference=? ORDER BY si.word_index""",(ref,)):
            spans.append({'ref':ref,'vi':vi,'sid':m['sid'],'surface':m['surface'],'strong':canon(m['ps']),'pos':m['pos'],'stem':m['stem'],'feat':morphfeat(m['morph_code'],m['pos']),'g':len(spans)})
    return spans
def derive(spans, tstr, s, cc, kind):
    g=s['g']; f=s['feat']; rows=[]
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
    # BEARER FIX: nearest preceding proper noun that is NOT an object (not HTo-marked)
    ag=[x for x in spans if x['feat']['proper'] and not x['feat']['obj'] and x['g']<g and g-x['g']<=6]
    if ag: add('bearer', ag[-1]['surface'], fr=ag[-1]['strong'], to=s['strong'], res='span')
    if f['v']:
        objs=[x for x in spans if x['feat']['obj'] and x['feat']['n'] and not x['feat']['prep'] and x['vi']==s['vi'] and x['g']!=g]
        if objs: o=min(objs,key=lambda x:abs(x['g']-g)); add('target',o['surface'],fr=s['strong'],to=o['strong'],res='span')
    if manner_noun and vb:
        add('manner','manner-of %s'%vb['surface'],fr=s['strong'],to='%s@%s'%(vb['strong'],vb['ref']),res='span')
        if vb['strong'] in tstr: add('coupling','welds %s'%vb['surface'],fr=s['strong'],to=vb['strong'],res='span')
    inten=sorted({INTENS[x['strong']] for x in spans if x['strong'] in INTENS and abs(x['g']-g)<=3})
    if inten: add('intensity',', '.join(inten))
    restraint=None
    if (f['v'] or manner_noun) and (cc in AFFECT_VICE or s['strong'] in DRIVERS) and kind=='prose':
        drv=[x for x in spans if x['strong'] in DRIVERS and x['g']!=g]; near=[x for x in drv if x['g']<g] or drv
        if near:
            e=near[-1]; fearish=e['strong'] in ('H3372','H3373'); divnear=any(x['strong'] in DIVINE and abs(x['g']-e['g'])<=2 for x in spans)
            if fearish and divnear: restraint='fear-of-God@%s'%e['ref']
            else: add('source','%s@%s'%(DRIVERS[e['strong']],e['ref']),fr='%s@%s'%(e['strong'],e['ref']),to=s['strong'],res='span')
    if f['v'] and kind=='prose':
        cnd=[x for x in spans if x['feat']['v'] and x['stem'] in ('Piel','Hiphil') and x['g']>g and x['strong']!=s['strong'] and 0<=x['vi']-s['vi']<=1]
        if cnd: e=cnd[0]; add('effect',e['surface'],fr=s['strong'],to='%s@%s'%(e['strong'],e['ref']),res='span')
    if any(x['strong'] in NEG and abs(x['g']-g)<=3 for x in spans): add('prohibition','forbidden (neg particle)')
    if restraint: add('discovery','restrained-by: '+restraint)
    return rows

def main():
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    pids=[r[0] for r in cur.execute("SELECT DISTINCT v.passage_id FROM wa_verse_records w JOIN verse v ON w.verse_id=v.id WHERE w.term_id LIKE ?||'%' AND COALESCE(w.delete_flagged,0)=0 AND v.passage_id IS NOT NULL",(TERM,)).fetchall()]
    # (a) PASSAGE BOUNDARY verification
    print("=== (a) passage-boundary check (is any run actually longer?) ===")
    for pid in pids:
        vv=cur.execute("SELECT reference,book_id,chapter,verse_num FROM verse WHERE passage_id=? ORDER BY book_id,chapter,verse_num",(pid,)).fetchall()
        a,z=vv[0],vv[-1]
        before=cur.execute("SELECT reference FROM verse WHERE book_id=? AND chapter=? AND verse_num=?",(a['book_id'],a['chapter'],a['verse_num']-1)).fetchone()
        after=cur.execute("SELECT reference FROM verse WHERE book_id=? AND chapter=? AND verse_num=?",(z['book_id'],z['chapter'],z['verse_num']+1)).fetchone()
        flag=''
        if before: flag+=' <-- %s IS in DB (should extend back!)'%before['reference']
        if after: flag+=' --> %s IS in DB (should extend fwd!)'%after['reference']
        print("   %s..%s  boundary %s"%(a['reference'],z['reference'],'CLEAN' if not flag else flag))
    # (b)+(c) re-derive + role
    plan=[]
    for pid in pids:
        refs=[r['reference'] for r in cur.execute("SELECT reference FROM verse WHERE passage_id=? ORDER BY book_id,chapter,verse_num",(pid,)).fetchall()]
        spans=load(cur,refs)
        tagged={}
        for ref in refs:
            v=cur.execute("SELECT id FROM verse WHERE reference=?",(ref,)).fetchone()
            for w in cur.execute("SELECT w.id wid,w.term_id,mt.cluster_code cc FROM wa_verse_records w LEFT JOIN mti_terms mt ON w.mti_term_id=mt.id WHERE w.verse_id=? AND COALESCE(w.delete_flagged,0)=0",(v['id'],)).fetchall():
                vc=cur.execute("SELECT id FROM verse_context WHERE verse_record_id=? AND COALESCE(delete_flagged,0)=0 LIMIT 1",(w['wid'],)).fetchone()
                tagged[(ref,canon(w['term_id']))]=(w['cc'], vc['id'] if vc else None)
        tstr=set(s['strong'] for s in spans)
        # all pair from/to strongs in this passage (for reference-based involvement)
        rowsbyspan=[]
        for s in spans:
            if s['pos'] in FUNCTION: continue
            key=(s['ref'],s['strong']); tg=tagged.get(key)
            if tg and tg[0]=='T2': continue
            gate='1-primary' if tg else '2-relevant'; cc=tg[0] if tg else None; vcid=tg[1] if tg else None
            r=derive(spans,tstr,s,cc,'prose')
            rowsbyspan.append((s,cc,gate,vcid,r))
        # involvement references
        allrefs=set()
        for s,cc,gate,vcid,r in rowsbyspan:
            for lbl,val,fr,to,res in r:
                if fr: allrefs.add(fr)
                if to: allrefs.add(to)
        # assign role
        for s,cc,gate,vcid,r in rowsbyspan:
            labels={x[0] for x in r}; f=s['feat']
            typ='status' if f['n'] else 'action' if f['v'] else 'quality'
            involved = bool(labels & REL) or any(x.startswith(s['strong']) for x in allrefs) or (gate=='1-primary' and f['v'])
            if gate=='1-primary' and cc in DISP and typ in ('status','quality'): role='characteristic'
            elif not involved: role='standalone'
            else: role='process-qualifier'
            r.append(('role',role,None,None,None))
            plan.append((s,gate,vcid,role,r))
    from collections import Counter
    rc=Counter(role for _,_,_,role,_ in plan)
    print("\n=== (c) role distribution (sanity-check evaluation) ===")
    for k in ('characteristic','process-qualifier','standalone'): print("   %-18s %d"%(k,rc[k]))
    print("   (characteristic spans:", [ (s['ref'],s['surface']) for s,_,_,role,_ in plan if role=='characteristic'],")")
    nrows=sum(len(r) for *_,r in plan)
    print("\nspans=%d rows=%d"%(len(plan),nrows))
    if not LIVE:
        print("DRY-RUN. Re-run with --live."); return
    shutil.copy2(DB,os.path.join('backups','bible_research.pre-sanity.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    refset=set(s['ref'] for s,_,_,_,_ in plan)
    for ref in refset:
        cur.execute("""UPDATE ve_lexical SET delete_flagged=1 WHERE source_provenance=? AND (
            verse_context_id IN (SELECT vc.id FROM verse_context vc JOIN wa_verse_records w ON vc.verse_record_id=w.id JOIN verse v ON w.verse_id=v.id WHERE v.reference=?)
            OR verse_span_id IN (SELECT si.id FROM verse_span_index si JOIN verse v ON si.verse_id=v.id WHERE v.reference=?))""",(PROV,ref,ref))
    n=0
    for s,gate,vcid,role,r in plan:
        for lbl,val,fr,to,res in r:
            ve_nr,pk=DIMS.get(lbl,(199,'value'))
            cur.execute("""INSERT INTO ve_lexical (verse_context_id,verse_span_id,gate,ve_nr,ve_label,value,source_provenance,from_span,to_span,direction,resolution,pair_kind,delete_flagged,created_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,0,?)""",(vcid,s['sid'],gate,ve_nr,lbl,val,PROV,fr,to,'1to2' if pk=='pair' else None,res,pk,NOW)); n+=1
    for ref in refset: cur.execute("UPDATE verse SET process_marker=? WHERE reference=?",(MARKER,ref))
    conn.commit()
    print("wrote %d rows over %d spans; roles: %s. marker=%s"%(n,len(plan),dict(rc),MARKER))

if __name__=='__main__': main()
