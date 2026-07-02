"""
_apply_write_ruthlessness_index_driven_v3_20260702.py

INDEX-DRIVEN rebuild of the ruthlessness-passage lexicals — the fix for the missing SECOND GATE.
Drives off verse_span_index (every span), not the pre-tagged term list, so BOTH gates run:
  gate 1 (primary) : the span is a tagged non-T2 term (has a verse_context)  -> lexicalise + link vc.
  gate 2 (relevant): the span is a content word NOT yet a term                -> lexicalise, keyed on
                     verse_span_id (pulled in as a span-level lexical; relevance = candidate).
Function words (particle/preposition/conjunction/suffix/pronoun) are skipped.

Supersedes prior lexical-model-2026 rows in these passages. New rows carry gate + verse_span_id
(and verse_context_id for gate-1). Safe: backup, dry-run, verify.
Usage: python scripts/_apply_write_ruthlessness_index_driven_v3_20260702.py [--live]
"""
import sqlite3, os, sys, re, shutil
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
TERM='H6531'; PROV='lexical-model-2026'; MARKER='ruthlessness-lexical-idx-20260702'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
SEATS={'H3820':'heart','H3824':'heart','H5315':'soul','H7307':'spirit','H1320':'flesh'}
DRIVERS={'H6973':'dread','H3372':'fear','H3373':'fear','H0639':'anger','H2534':'wrath','H8130':'hatred/enmity','H7451':'evil','H2555':'violence'}
DIVINE={'H0430','H3068','H0410','H0433'}; NEG={'H3808','H0408'}; INTENS={'H3966':'very','H7227':'many','H3605':'all'}
AFFECT_VICE={'M01','M02','M03','M06','M24','M27'}
FUNCTION={'particle','preposition','conjunction','suffix','pronoun'}
DIMS={'sense':(101,'value'),'type':(102,'value'),'source':(103,'pair'),'seat':(104,'pair'),'bearer':(105,'pair'),
      'operation':(106,'event'),'target':(107,'pair'),'manner':(108,'pair'),'intensity':(109,'value'),
      'effect':(111,'pair'),'coupling':(112,'pair'),'prohibition':(113,'flag'),'discovery':(114,'note')}
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
    """all spans (from verse_span_index) for the passage; each with its verse_span_index id."""
    spans=[]
    for vi,ref in enumerate(refs):
        for m in cur.execute("""SELECT si.id sid, si.word_index wi, si.surface, si.primary_strong ps, si.pos, si.stem, si.morph_code
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
    ag=[x for x in spans if x['feat']['proper'] and x['g']<g and g-x['g']<=6]
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
    plan=[]  # (span, cc, gate, vcid)
    genre_prose=True
    for pid in pids:
        refs=[r['reference'] for r in cur.execute("SELECT reference FROM verse WHERE passage_id=? ORDER BY book_id,chapter,verse_num",(pid,)).fetchall()]
        spans=load(cur,refs)
        # tagged non-T2 terms in these verses: (ref, canon strong) -> (cc, verse_context_id)
        tagged={}
        for ref in refs:
            v=cur.execute("SELECT id FROM verse WHERE reference=?",(ref,)).fetchone()
            for w in cur.execute("""SELECT w.id wid,w.term_id,mt.cluster_code cc FROM wa_verse_records w
                LEFT JOIN mti_terms mt ON w.mti_term_id=mt.id WHERE w.verse_id=? AND COALESCE(w.delete_flagged,0)=0""",(v['id'],)).fetchall():
                vc=cur.execute("SELECT id FROM verse_context WHERE verse_record_id=? AND COALESCE(delete_flagged,0)=0 LIMIT 1",(w['wid'],)).fetchone()
                tagged[(ref,canon(w['term_id']))]=(w['cc'], vc['id'] if vc else None)
        tstr=set(s['strong'] for s in spans)
        for s in spans:
            if s['pos'] in FUNCTION: continue
            key=(s['ref'],s['strong']); tg=tagged.get(key)
            if tg and tg[0]=='T2': continue   # T2 = qualifier, not analysed standalone
            gate='1-primary' if tg else '2-relevant'
            cc = tg[0] if tg else None
            vcid = tg[1] if tg else None
            rows=derive(spans,tstr,s,cc,'prose' if genre_prose else 'poetic')
            if rows: plan.append((s,cc,gate,vcid,rows))
    g1=sum(1 for p in plan if p[2]=='1-primary'); g2=sum(1 for p in plan if p[2]=='2-relevant')
    nrows=sum(len(p[4]) for p in plan)
    print("index-driven spans to lexicalise: %d (gate1-primary=%d, gate2-relevant/content=%d); rows=%d"%(len(plan),g1,g2,nrows))
    if not LIVE:
        print("sample gate-2 (content words now included):")
        for s,cc,gate,vcid,rows in [p for p in plan if p[2]=='2-relevant'][:12]:
            print("   %-10s %-14s %s -> %s"%(s['ref'],s['surface'],s['strong'],[r[0] for r in rows]))
        print("\nDRY-RUN. Re-run with --live."); return
    shutil.copy2(DB,os.path.join('backups','bible_research.pre-idxwrite.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    # supersede prior new-model rows in these passages (by verse_context or by verse_span in these verses)
    refset=set(s['ref'] for p in plan for s in [p[0]])
    for ref in refset:
        cur.execute("""UPDATE ve_lexical SET delete_flagged=1 WHERE source_provenance=? AND (
            verse_context_id IN (SELECT vc.id FROM verse_context vc JOIN wa_verse_records w ON vc.verse_record_id=w.id JOIN verse v ON w.verse_id=v.id WHERE v.reference=?)
            OR verse_span_id IN (SELECT si.id FROM verse_span_index si JOIN verse v ON si.verse_id=v.id WHERE v.reference=?))""",(PROV,ref,ref))
    n=0
    for s,cc,gate,vcid,rows in plan:
        for lbl,val,fr,to,res in rows:
            ve_nr,pk=DIMS.get(lbl,(199,'value'))
            cur.execute("""INSERT INTO ve_lexical (verse_context_id,verse_span_id,gate,ve_nr,ve_label,value,source_provenance,from_span,to_span,direction,resolution,pair_kind,delete_flagged,created_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,0,?)""",(vcid,s['sid'],gate,ve_nr,lbl,val,PROV,fr,to,'1to2' if pk=='pair' else None,res,pk,NOW)); n+=1
    for ref in refset: cur.execute("UPDATE verse SET process_marker=? WHERE reference=?",(MARKER,ref))
    conn.commit()
    print("wrote %d rows over %d spans (gate1=%d gate2=%d)."%(n,len(plan),g1,g2))

if __name__=='__main__': main()
