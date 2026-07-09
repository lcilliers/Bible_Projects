"""
Build the verse_span_lexical INDEX as JSON (researcher spec 2026-06-26).
EVERY span STEP returned is in scope; EVERY span should have a lexical (incl T2);
NO filtering. Fan-out: verse (status) -> span (every verse_morphology word) ->
verse-record (status/missing) -> lexical (status/missing) -> compound (status/missing).

Read-only. Output: outputs/wa-verse-span-lexical-index-v1-20260626.json (+ summary print).
"""
import sqlite3, os, re, json
from collections import defaultdict

DB=os.path.join('database','bible_research.db')
OUT=os.path.join('outputs','wa-verse-span-lexical-index-v1-20260626.json')

def canon(s):
    m=re.match(r'^([HG])(\d+)([A-Z]?)$',(s or '').strip().upper()); return f'{m.group(1)}{int(m.group(2)):04d}{m.group(3)}' if m else None

def main():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    print('loading tables...')
    # mti: id -> info ; strongs -> [ids]
    mti={};
    for r in c.execute("SELECT id, strongs_number, status, delete_flagged, cluster_code, transliteration FROM mti_terms"):
        mti[r['id']]={'strongs':r['strongs_number'],'cs':canon(r['strongs_number']),'status':r['status'],
                      'del':r['delete_flagged'],'cluster':r['cluster_code'],'tr':r['transliteration']}
    # verse-records by verse_id
    vr_by_v=defaultdict(list)
    for r in c.execute("SELECT id, verse_id, mti_term_id, transliteration, delete_flagged FROM wa_verse_records WHERE verse_id IS NOT NULL"):
        vr_by_v[r['verse_id']].append(dict(r))
    # verse_context units by verse_record_id
    unit_by_vr=defaultdict(list)
    for r in c.execute("SELECT id, verse_record_id, mti_term_id, delete_flagged FROM verse_context"):
        unit_by_vr[r['verse_record_id']].append(dict(r))
    # ve_lexical by verse_context_id (active)
    lex_by_u=defaultdict(list)
    for r in c.execute("SELECT verse_context_id u, ve_nr, ve_label, value, related_tier, source_provenance FROM ve_lexical WHERE COALESCE(delete_flagged,0)=0"):
        lex_by_u[r['u']].append({'ve_nr':r['ve_nr'],'label':r['ve_label'],'value':r['value'],'tier':r['related_tier'],'prov':r['source_provenance']})
    # morphology by verse_id
    morph_by_v=defaultdict(list)
    for r in c.execute("SELECT verse_id, word_index, surface, strongs, primary_strong, pos FROM verse_morphology WHERE verse_id IS NOT NULL"):
        morph_by_v[r['verse_id']].append(dict(r))
    verses=c.execute("SELECT id, reference, testament, verse_text FROM verse ORDER BY id").fetchall()
    print(f'verses={len(verses)} morph_words={sum(len(v) for v in morph_by_v.values())}')

    # per (mti strongs) how many verses reference it (for T2 reuse note)
    term_verse_ct=defaultdict(set)
    for vid,recs in vr_by_v.items():
        for r in recs:
            if r['mti_term_id']: term_verse_ct[r['mti_term_id']].add(vid)

    os.makedirs('outputs',exist_ok=True)
    summ=defaultdict(int); lex_present=lex_missing=0
    f=open(OUT,'w',encoding='utf-8'); f.write('{\n"index":"verse_span_lexical","spec":"every span; every span should have a lexical incl T2; no filter",\n"verses":[\n')
    first=True
    for v in verses:
        vid=v['id']
        recs=vr_by_v.get(vid,[])
        v_active = any(not r['delete_flagged'] for r in recs)
        # group records by strongs (via mti)
        recs_by_cs=defaultdict(list)
        for r in recs:
            m=mti.get(r['mti_term_id'])
            if m and m['cs']: recs_by_cs[m['cs']].append(r)
        spans=[]
        for w in sorted(morph_by_v.get(vid,[]), key=lambda x:x['word_index']):
            toks=[canon(t) for t in (w['strongs'] or '').split() if canon(t)]
            # one span entry per distinct strongs token in the word (STEP span)
            seen=set()
            for cs in toks:
                if cs in seen: continue
                seen.add(cs)
                srecs=recs_by_cs.get(cs,[])
                act=[r for r in srecs if not r['delete_flagged']]
                # term status (from any mti of this strongs present in records, else lookup)
                term_stat=None; cluster=None; reuse=None
                if srecs:
                    m=mti.get(srecs[0]['mti_term_id']);
                    if m: term_stat=m['status']; cluster=m['cluster']
                    reuse=max((len(term_verse_ct.get(r['mti_term_id'],())) for r in srecs), default=0)
                # units + lexicals
                units=[]; lexicals=[]; compounds=[]
                for r in act:
                    for u in unit_by_vr.get(r['id'],[]):
                        if u['delete_flagged']: continue
                        units.append(u['id'])
                        for L in lex_by_u.get(u['id'],[]):
                            (compounds if L['label']=='compound' else lexicals).append(L)
                # record status
                if not srecs: rec_status='MISSING'
                elif not act and term_stat=='delete': rec_status='STRANDED_DELETED_TERM'
                elif not act: rec_status='ALL_FLAGGED'
                else: rec_status='ACTIVE'
                lex_status = 'PRESENT' if lexicals else ('NO_UNIT' if (act and not units) else 'MISSING')
                comp_status = 'PRESENT' if compounds else 'MISSING'
                if lexicals: lex_present+=1
                else: lex_missing+=1
                summ[f'rec:{rec_status}']+=1; summ[f'lex:{lex_status}']+=1
                spans.append({
                    'word_index':w['word_index'],'surface':w['surface'],'strongs':cs,'pos':w['pos'],
                    'verse_record':{'status':rec_status,'n_records':len(srecs),'n_active':len(act),
                                    'term_status':term_stat,'cluster':cluster,'term_reuse_verses':reuse,
                                    'records':[{'vr_id':r['id'],'mti':r['mti_term_id'],'tr':r['transliteration'],'flagged':r['delete_flagged']} for r in srecs]},
                    'lexical':{'status':lex_status,'n_units':len(units),'unit_ids':units,'n_lexical':len(lexicals),'lexicals':lexicals},
                    'compound':{'status':comp_status,'n_compound':len(compounds),'compounds':compounds},
                })
        rec={'reference':v['reference'],'verse_id':vid,'testament':v['testament'],
             'verse_status':'active' if v_active else 'no_active_records',
             'verse_text':v['verse_text'],'span_count':len(spans),'spans':spans}
        f.write(('' if first else ',\n')+json.dumps(rec,ensure_ascii=False)); first=False
    f.write('\n]}\n'); f.close()
    sz=os.path.getsize(OUT)
    print(f'\nWROTE {OUT}  ({sz/1024/1024:.1f} MB)')
    print(f'spans with lexical: {lex_present} | spans missing lexical: {lex_missing}')
    print('record status:', {k.split(":")[1]:v for k,v in sorted(summ.items()) if k.startswith("rec:")})
    print('lexical status:', {k.split(":")[1]:v for k,v in sorted(summ.items()) if k.startswith("lex:")})
    c.close()

if __name__=='__main__': main()
