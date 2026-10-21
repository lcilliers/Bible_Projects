"""
_apply_term_driven_lexical_ruthlessness_v7_20260702.py

Term-driven trial (researcher method, 2026-07-02): take an OWNER term (ruthlessness perek H6531),
process its ANCHOR verse's passage first, then batch every verse of the term one by one. Genre-aware
passage treatment; read-back sensibility check -> D11 notes on uncertainty; a completion marker on
each verse so done verses are skipped.

Adds verse.process_marker (completion tracking). Writes only the marker (the 14-item values are shown
for review; the ve_lexical pair-schema is not yet finalised, so values are not persisted here).
Reuses the v6 derivation rules. Genre is derived per verse (a verse-level ve-lexical) and feeds the
passage treatment (narrative/law/prophetic-prose -> cross-verse ON; poetry/wisdom -> two-phase, off).

Usage: python scripts/_apply_term_driven_lexical_ruthlessness_v7_20260702.py [--live]
"""
import sqlite3, os, re, sys, shutil
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
TERM='H6531'; TERM_NAME='ruthlessness (perek)'; STAMP='lexical-v7-20260702'
SEATS={'H3820':'heart','H3824':'heart','H5315':'soul','H7307':'spirit','H1320':'flesh'}
DRIVERS={'H6973':'dread','H3372':'fear','H3373':'fear','H0639':'anger','H2534':'wrath','H8130':'hatred/enmity',
         'H6031':'affliction','H7451':'evil','H2555':'violence'}
AFFECT_VICE={'M01','M02','M03','M06','M24','M27'}
NEG={'H3808','H0408','G3361'}; INTENS={'H3966':'very','H7227':'many','H3605':'all'}
def canon(s):
    m=re.match(r'^([HG])(\d+)',s or ''); return m.group(1)+m.group(2).zfill(4) if m else s
def genre(b):
    if 1<=b<=5: return ('law/narrative','prose')
    if 6<=b<=17: return ('narrative','prose')
    if b in (18,19,20,21,22): return ('poetry/wisdom','poetic')   # Job Psa Pro Ecc Song -> two-phase
    if 23<=b<=39: return ('prophetic','prose')
    if 40<=b<=43: return ('gospel-narrative','prose')
    return ('epistle','prose')
def parse(mc,pos):
    segs=(mc or '').split(); head=segs[0] if segs else ''
    f={'v':pos=='verb','n':pos=='noun','a':pos=='adjective','state':None,'prep':False,'obj':False}
    if head.startswith('HN') and head[-1] in ('c','a'): f['state']='construct' if head[-1]=='c' else 'absolute'
    for s in segs:
        if s.startswith('HR'): f['prep']=True
        if s=='HTo': f['obj']=True
    return f

def load(cur, refs):
    spans=[]; terms=[]
    for vi,ref in enumerate(refs):
        v=cur.execute("SELECT id FROM verse WHERE reference=?",(ref,)).fetchone()
        for m in cur.execute("SELECT surface,primary_strong,pos,stem,morph_code FROM verse_morphology WHERE verse_id=? ORDER BY word_index",(v['id'],)):
            spans.append({'ref':ref,'vi':vi,'surface':m['surface'],'strong':canon(m['primary_strong']),'pos':m['pos'],'stem':m['stem'],'feat':parse(m['morph_code'],m['pos']),'g':len(spans)})
        for t in cur.execute("""SELECT w.term_id,w.target_word,mt.cluster_code FROM wa_verse_records w
            LEFT JOIN mti_terms mt ON w.mti_term_id=mt.id WHERE w.verse_id=? AND COALESCE(w.delete_flagged,0)=0""",(v['id'],)):
            terms.append({'ref':ref,'strong':canon(t['term_id']),'word':t['target_word'],'cc':t['cluster_code']})
    return spans, terms

def deriv_term(spans, terms, strong, genre_kind):
    tstr={t['strong'] for t in terms}
    occ=[s for s in spans if s['strong']==strong]
    out=[]
    for s in occ:
        g=s['g']; f=s['feat']; d={}
        vb=None; vs=[x for x in spans if x['feat']['v'] and abs(x['g']-g)<=3]
        if vs: vb=min(vs,key=lambda x:abs(x['g']-g))
        manner_noun=f['n'] and f['prep']
        d['identity']='%s / %s'%(s['surface'],'action' if f['v'] else 'status' if f['n'] else 'quality')
        d['operation']=('(qualifies) %s(%s)'%(vb['surface'],vb['strong'])) if manner_noun and vb else (('%s(%s)'%(s['surface'],s['strong'])) if f['v'] else None)
        d['manner']=('manner-of %s(%s)'%(vb['surface'],vb['strong'])) if manner_noun and vb else None
        d['coupling']=('welds %s(%s)'%(vb['surface'],vb['strong'])) if manner_noun and vb and vb['strong'] in tstr else None
        # cross-verse items only in prose
        src=None
        if genre_kind=='prose':
            drv=[x for x in spans if x['strong'] in DRIVERS and x['g']<g and x['strong']!=strong]
            if drv: e=drv[-1]; src='%s(%s)@%s'%(DRIVERS[e['strong']],e['strong'],e['ref'])
        d['source']=src
        eff=None
        if genre_kind=='prose' and (f['v'] or manner_noun) and vb:
            c=[x for x in spans if x['feat']['v'] and x['stem'] in ('Piel','Hiphil') and x['g']>g and x['strong'] in tstr and 0<=x['vi']-s['vi']<=1]
            if c: e=c[0]; eff='%s(%s,%s)@%s'%(e['surface'],e['strong'],e['stem'],e['ref'])
        d['effect']=eff
        d['prohibition']='forbidden (neg)' if any(x['strong'] in NEG and abs(x['g']-g)<=3 for x in spans) else None
        # read-back sensibility -> D11 notes
        notes=[]
        if manner_noun and not d['coupling']: notes.append('manner-noun but no co-term weld found')
        if not vb: notes.append('no governing verb near term')
        if genre_kind!='prose': notes.append('poetic: cross-verse items deferred to phase-2 poem read')
        d['D11 notes']='; '.join(notes) or None
        out.append((s['ref'],d))
    return out

def main():
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    if 'process_marker' not in [r[1] for r in cur.execute("PRAGMA table_info(verse)").fetchall()]:
        if LIVE: cur.execute("ALTER TABLE verse ADD COLUMN process_marker TEXT")
    # term verses -> unique passages, anchor passage (Exo 1:7-14) first
    vrows=cur.execute("""SELECT DISTINCT v.id vid, v.reference, v.book_id, v.passage_id
        FROM wa_verse_records w JOIN verse v ON w.verse_id=v.id
        WHERE w.term_id LIKE ?||'%' AND COALESCE(w.delete_flagged,0)=0 ORDER BY v.book_id,v.chapter,v.verse_num""",(TERM,)).fetchall()
    # group by passage
    seen_pass=[]; pass_refs={}
    for r in vrows:
        pid=r['passage_id']
        key=pid or ('single-%d'%r['vid'])
        if key not in pass_refs:
            if pid:
                refs=[x['reference'] for x in cur.execute("SELECT reference FROM verse WHERE passage_id=? ORDER BY book_id,chapter,verse_num",(pid,)).fetchall()]
                pref=cur.execute("SELECT ref FROM passage WHERE id=?",(pid,)).fetchone()['ref']
            else: refs=[r['reference']]; pref=r['reference']
            pass_refs[key]={'refs':refs,'pref':pref,'book':r['book_id'],'termverses':[]}
            seen_pass.append(key)
        pass_refs[key]['termverses'].append(r['reference'])
    # anchor first: the passage containing Exo 1:13
    seen_pass.sort(key=lambda k: 0 if 'Exo 1:13' in pass_refs[k]['termverses'] else 1)

    print('TERM-DRIVEN LEXICAL: %s — %d passages (anchor first)\n'%(TERM_NAME,len(seen_pass)))
    marks=[]
    for i,key in enumerate(seen_pass):
        P=pass_refs[key]; gk,kind=genre(P['book'])
        role='ANCHOR' if i==0 else 'batch #%d'%i
        print('='*70); print('[%s] passage %s | genre=%s (%s) | term-verses: %s'%(role,P['pref'],gk,kind,', '.join(P['termverses'])))
        spans,terms=load(cur,P['refs'])
        res=deriv_term(spans,terms,canon(TERM),kind)
        for ref,d in res:
            print('  %s  ruthlessness:'%ref)
            for k in ['identity','operation','manner','coupling','source','effect','prohibition','D11 notes']:
                if d.get(k): print('       %-11s %s'%(k,d[k]))
        for tv in P['termverses']: marks.append(tv)
        print()
    if LIVE:
        shutil.copy2(DB,os.path.join('backups','bible_research.pre-v7marker.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
        for ref in marks:
            cur.execute("UPDATE verse SET process_marker=? WHERE reference=? AND process_marker IS NULL",(STAMP,ref))
        conn.commit()
        print('marked %d verses completed (%s); skip on re-run.'%(len(marks),STAMP))
    else:
        print('DRY-RUN (no marker written). Verses that WOULD be marked: %s'%marks)

if __name__=='__main__': main()
