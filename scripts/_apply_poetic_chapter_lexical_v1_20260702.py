"""
_apply_poetic_chapter_lexical_v1_20260702.py

REUSABLE poetic-book (Psalms/Proverbs) Phase-1 lexical build — CHAPTER-DRIVEN.
Per method wa-poetic-chapter-method-and-psalm1-plan-v1-20260702.md:
  - driver = the CHAPTER (all its verses); passage process NOT applicable.
  - each verse built INDEPENDENTLY (its own spans only); cross-verse items OFF (kind='poetic').
  - within-verse items only: sense,type,operation,seat,bearer,target,manner,coupling,intensity,prohibition.
  - two gates: gate 1 = tagged non-T2 term (link verse_context); gate 2 = content span not yet a term (span-keyed).
  - sanity-check role DRAFT per span (characteristic / process-qualifier / standalone); bearer flagged unreliable in D11.
  - marks verse.process_marker.

DRY-RUN writes an inspection .md (no DB change). --live writes ve_lexical + process_marker (backup first).
Usage:
  python scripts/_apply_poetic_chapter_lexical_v1_20260702.py --book=Psa --chapter=1          # dry-run + inspection md
  python scripts/_apply_poetic_chapter_lexical_v1_20260702.py --book=Psa --chapter=1 --live
"""
import sqlite3, os, sys, re, shutil
from datetime import datetime, timezone

DB=os.path.join('database','bible_research.db')
def arg(name,default=None):
    for a in sys.argv[1:]:
        if a.startswith('--%s='%name): return a.split('=',1)[1]
    return default
LIVE='--live' in sys.argv
BOOK=arg('book','Psa'); CHAP=int(arg('chapter','1'))
PROV='lexical-model-2026'; MARKER='%s-%d-poetic-lexical-%s'%(BOOK,CHAP,datetime.now(timezone.utc).strftime('%Y%m%d'))
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
SEATS={'H3820':'heart','H3824':'heart','H5315':'soul','H7307':'spirit','H1320':'flesh'}
NEG={'H3808','H0408'}; INTENS={'H3966':'very','H7227':'many','H3605':'all'}
FUNCTION={'particle','preposition','conjunction','suffix','pronoun'}
# Sanity-check stop-lists (learned Psa 1-3): a gate-1 tagged term in these is NEVER an inner-being
# characteristic. GENRE_LABEL = superscription metadata (mizmor/shir); EXTERNAL_ENTITY = adversary-PERSONS
# (not inner states — cf. external-pole principle). Lemma-level (M44 Relational is mixed, so no cluster rule).
# Extend by adding verified lemmas; keep it data, not logic.
GENRE_LABEL={'H4210','H7892','H5329'}         # Psalm(mizmor), Song(shir), choirmaster(menatseach)
EXTERNAL_ENTITY={'H0341','H6862'}             # enemy, foe/adversary
STOPLIST_NOT_CHARACTERISTIC=GENRE_LABEL|EXTERNAL_ENTITY
# INVERSE of the stop-list (learned Psa 26-81, 2026-07-02): gate-2 content spans whose lemma IS a genuine
# inner-being characteristic (a real affection/operation), promoted to role=characteristic even when
# untagged. aheb recurred ~8x under-tagged as standalone across Ps 26:8/31:23/34:12/45:7/47:4/52:3-4/70:4,
# sometimes the CENTRAL finding (Psa 52 "you love evil"). Its object sets the valence; the love itself is
# always the inner-being characteristic. Keep data, not logic; extend by adding verified lemmas.
PROMOTE_CHARACTERISTIC={'H0157'}              # aheb (love/affection)
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

def load_verse(cur, ref):
    spans=[]
    for m in cur.execute("""SELECT si.id sid, si.word_index wi, si.surface, si.primary_strong ps, si.pos, si.stem, si.morph_code
         FROM verse_span_index si JOIN verse v ON si.verse_id=v.id WHERE v.reference=? ORDER BY si.word_index""",(ref,)):
        spans.append({'ref':ref,'sid':m['sid'],'surface':m['surface'],'strong':canon(m['ps']),'pos':m['pos'],
                      'stem':m['stem'],'feat':morphfeat(m['morph_code'],m['pos']),'g':len(spans)})
    return spans

def derive(spans, tstr, s):
    """WITHIN-VERSE items only (poetic: no cross-verse source/effect/process)."""
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
    if ag:
        add('bearer', ag[-1]['surface'], fr=ag[-1]['strong'], to=s['strong'], res='span')
        add('discovery','bearer unreliable (nearest-proper heuristic; subject-agreement not parsed)')
    if f['v']:
        objs=[x for x in spans if x['feat']['obj'] and x['feat']['n'] and not x['feat']['prep'] and x['g']!=g]
        if objs: o=min(objs,key=lambda x:abs(x['g']-g)); add('target',o['surface'],fr=s['strong'],to=o['strong'],res='span')
    if manner_noun and vb:
        add('manner','manner-of %s'%vb['surface'],fr=s['strong'],to='%s@%s'%(vb['strong'],vb['ref']),res='span')
        if vb['strong'] in tstr: add('coupling','welds %s'%vb['surface'],fr=s['strong'],to=vb['strong'],res='span')
    inten=sorted({INTENS[x['strong']] for x in spans if x['strong'] in INTENS and abs(x['g']-g)<=3})
    if inten: add('intensity',', '.join(inten))
    if any(x['strong'] in NEG and abs(x['g']-g)<=3 for x in spans): add('prohibition','forbidden (neg particle)')
    return rows

def role_of(gate, rows, strong):
    """Sanity-check role (per-occurrence). Learned rules (Psalm 1-3, 2026-07-02):
       (a) a gate-1 term in STOPLIST_NOT_CHARACTERISTIC (genre-label metadata / external-entity adversary)
           is never an inner-being characteristic -> standalone (Psa 3 mizmor; Psa 2-3 foes/enemies).
       (b) a gate-1 term that itself functions ADVERBIALLY (derived a manner/coupling on a verb — a
           prep-marked noun qualifying the predicate) is a PROCESS-QUALIFIER (Psa 1:1 counsel, 1:5 judgment).
       Role is per-occurrence, so the same lemma can be a characteristic elsewhere.
       gate-2 content span = process-qualifier if it binds, else standalone."""
    labels={r[0] for r in rows}
    # (c) inner-being lemmas in PROMOTE_CHARACTERISTIC are a characteristic at ANY gate (unless functioning
    #     adverbially) — e.g. aheb (love), whose object sets the valence but which is itself the characteristic.
    if strong in PROMOTE_CHARACTERISTIC:
        return 'process-qualifier' if labels & {'manner','coupling'} else 'characteristic'
    if gate=='1-primary':
        if strong in STOPLIST_NOT_CHARACTERISTIC: return 'standalone'
        if labels & {'manner','coupling'}: return 'process-qualifier'
        return 'characteristic'
    if labels & {'manner','coupling','target','seat'}: return 'process-qualifier'
    return 'standalone'

def main():
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    bid=cur.execute("SELECT DISTINCT book_id FROM verse WHERE reference LIKE ?||' %' LIMIT 1",(BOOK,)).fetchone()
    if not bid: print("no verses for book '%s'"%BOOK); return
    verses=cur.execute("SELECT id,reference,verse_num FROM verse WHERE book_id=? AND chapter=? ORDER BY verse_num",(bid['book_id'],CHAP)).fetchall()
    if not verses: print("no verses for %s %d"%(BOOK,CHAP)); return
    plan=[]  # (span, gate, cc, vcid, rows, role)
    for v in verses:
        ref=v['reference']
        spans=load_verse(cur,ref)
        tagged={}
        wrecs=cur.execute("""SELECT w.id wid,w.term_id,mt.cluster_code cc FROM wa_verse_records w
            LEFT JOIN mti_terms mt ON w.mti_term_id=mt.id WHERE w.verse_id=? AND COALESCE(w.delete_flagged,0)=0""",(v['id'],)).fetchall()
        for w in wrecs:  # fetchall FIRST: an inner cur.execute would otherwise reposition this cursor and truncate the loop
            vc=cur.execute("SELECT id FROM verse_context WHERE verse_record_id=? AND COALESCE(delete_flagged,0)=0 LIMIT 1",(w['wid'],)).fetchone()
            tagged[canon(w['term_id'])]=(w['cc'], vc['id'] if vc else None)
        tstr=set(s['strong'] for s in spans)
        for s in spans:
            if s['pos'] in FUNCTION: continue
            tg=tagged.get(s['strong'])
            if tg and tg[0]=='T2': continue
            gate='1-primary' if tg else '2-relevant'
            cc=tg[0] if tg else None; vcid=tg[1] if tg else None
            rows=derive(spans,tstr,s)
            if rows: plan.append((s,gate,cc,vcid,rows,role_of(gate,rows,s['strong'])))
    g1=sum(1 for p in plan if p[1]=='1-primary'); g2=len(plan)-g1
    nrows=sum(len(p[4])+1 for p in plan)  # +1 for role
    print("%s %d: verses=%d spans=%d (gate1=%d gate2=%d) rows(incl role)=%d"%(BOOK,CHAP,len(verses),len(plan),g1,g2,nrows))
    # inspection view (always)
    outdir=os.path.join('verse-analysis','_reports'); rep=os.path.join(outdir,'wa-%s%d-phase1-lexical-view-%s.md'%(BOOK.lower(),CHAP,datetime.now(timezone.utc).strftime('%Y%m%d')))
    lines=["# %s %d — Phase-1 per-verse lexical (DB-derived draft) — %s"%(BOOK,CHAP,NOW[:10]),"",
           "> Chapter-driven poetic build; within-verse items only; role = sanity-check DRAFT. %d spans, %d rows."%(len(plan),nrows),""]
    curref=None
    for s,gate,cc,vcid,rows,role in plan:
        if s['ref']!=curref: curref=s['ref']; lines+=["","## %s"%curref,""]
        items="; ".join("%s=%s"%(r[0],r[1]) for r in rows)
        lines.append("- **%s** `%s` [%s%s] **role=%s** — %s"%(s['surface'],s['strong'],gate[0],'/'+cc if cc else '',role,items))
    open(rep,'w',encoding='utf-8').write("\n".join(lines))
    print("inspection view ->",rep)
    if not LIVE:
        print("DRY-RUN. Inspect the view, then re-run with --live."); return
    shutil.copy2(DB,os.path.join('backups','bible_research.pre-%s%d-poetic.%s.db'%(BOOK.lower(),CHAP,datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))))
    refset=[v['reference'] for v in verses]
    for ref in refset:
        cur.execute("""UPDATE ve_lexical SET delete_flagged=1 WHERE source_provenance=? AND (
            verse_context_id IN (SELECT vc.id FROM verse_context vc JOIN wa_verse_records w ON vc.verse_record_id=w.id JOIN verse v ON w.verse_id=v.id WHERE v.reference=?)
            OR verse_span_id IN (SELECT si.id FROM verse_span_index si JOIN verse v ON si.verse_id=v.id WHERE v.reference=?))""",(PROV,ref,ref))
    n=0
    for s,gate,cc,vcid,rows,role in plan:
        allrows=list(rows)+[('role',role,None,None,None)]
        for lbl,val,fr,to,res in allrows:
            ve_nr,pk=DIMS.get(lbl,(199,'value'))
            cur.execute("""INSERT INTO ve_lexical (verse_context_id,verse_span_id,gate,ve_nr,ve_label,value,source_provenance,from_span,to_span,direction,resolution,pair_kind,delete_flagged,created_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,0,?)""",(vcid,s['sid'],gate,ve_nr,lbl,val,PROV,fr,to,'1to2' if pk=='pair' else None,res,pk,NOW)); n+=1
    for ref in refset: cur.execute("UPDATE verse SET process_marker=? WHERE reference=?",(MARKER,ref))
    conn.commit()
    print("wrote %d rows over %d spans; process_marker=%s on %d verses."%(n,len(plan),MARKER,len(refset)))

if __name__=='__main__': main()
