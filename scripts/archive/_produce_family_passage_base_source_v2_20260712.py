"""Base source per family — WORK-CONTRACT + PASSAGE-UNIT + RAW-COMPLETE + ANCHORED.
Researcher spec 2026-07-12:
  a) meta = the WORK CONTRACT (objective, prescriptive narrative_directives 1-10,
     worklist, completeness check, backtracking).
  b) unit of work = the PASSAGE.
  c) data = RAW ve_lexical, NOT pre-filtered / NOT pre-judged. 'none' and ABSENT
     dimensions are evidence. Only the organisation eases consumption.
  d) backtracking = ve_lexical.id on every atom.
  e) ANCHOR/DEDUP: identical structured readings collapse to one anchor; later
     identical instances mark same_as -> anchor (narrate once). meta.reading_map
     surfaces each item's distinct readings (1 entry = deduped repetition; >1 =
     variation to interrogate per directive 10).

No verse_span_index node. Full 101..116 frame per lexical; present rows carry
ve_lexical_id; absent dimensions shown (present:false). Signature for 'same' =
char_key + all dimension (nr,value) + absence-pattern, EXCLUDING 114 discovery
and the reference (verse-specific).

Usage: python scripts/_produce_family_passage_base_source_v2_20260712.py --family <slug> [--book 19] [--all]
"""
import sqlite3, os, json, sys
from collections import defaultdict, OrderedDict

BOOK='19'; FAM=None; ALL='--all' in sys.argv
if '--family' in sys.argv: FAM=sys.argv[sys.argv.index('--family')+1]
if '--book' in sys.argv: BOOK=sys.argv[sys.argv.index('--book')+1]
OUT='verse-analysis/psalms/_base-sources'; os.makedirs(OUT,exist_ok=True)
c=sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory=sqlite3.Row
short={r['cluster_code']:(r['short_name'] or r['cluster_code']) for r in c.execute("SELECT cluster_code,short_name FROM cluster")}
LEGEND=OrderedDict([(101,'sense'),(102,'type'),(103,'source'),(104,'seat'),(105,'bearer'),(106,'operation'),
        (107,'target'),(108,'manner'),(109,'intensity'),(110,'specifier'),(111,'effect'),(112,'coupling'),
        (113,'prohibition'),(114,'discovery'),(115,'role'),(116,'locus')])
DIRECTIVES=[
 "1. Cover everything — leave nothing out. Interpret every dimension present in each lexical, and every absence. A narrative that addresses only some dimensions is incomplete.",
 "2. Silence is evidence. value 'none' = the reader explicitly found none; present:false = no row recorded. Interpret what the silence says (e.g. no seat -> the operation is not organ-located); never skip a dimension for being empty.",
 "3. Read in relation to the inner being. Describe what the char DOES within the human inner life — God and others are the arena it acts toward, not the subject. Keep the lens on the inner-being process.",
 "4. Describe the full process, not a label. Trace the movement: source -> operation -> target -> coupling -> effect. Show the flow, not a static tag.",
 "5. No valence bias. Read the descent with the same weight as the ascent — pride, malice, the wicked's interior, failure, the dark movement as fully as praise or trust. Do not privilege the edifying.",
 "6. Do not filter uncomfortable results. Report what the data supports even when uncomfortable or against expectation. Completeness over comfort.",
 "7. Grounded + backtrackable. Only what the passage and its lexicals support; cite ve_lexical_id / reference for each claim; no imported theology, no invention. If evidence is thin, say so.",
 "8. Preserve distinctions. Where a passage holds several lexicals, do not collapse them — the difference between them is a finding.",
 "9. Narrate each distinct reading once. A lexical marked duplicate shares its anchor's outcome (same_as) — do not re-narrate it; reference the anchor. Write the narrative at the anchor and there note the recurrences.",
 "10. Interrogate difference — variation is a finding. Where the same item has >1 distinct reading (see meta.reading_map), ask WHY they differ and whether the difference carries meaning or impact (a shift in bearer/source/target/coupling/intensity, or ascent->descent). How a characteristic varies across contexts is evidence of how it operates.",
]

PC={}
for r in c.execute("SELECT id,ref,start_chapter,start_verse FROM passage WHERE book_id=?",(BOOK,)):
    PC[r['id']]={'ref':r['ref'],'order':(r['start_chapter'] or 0,r['start_verse'] or 0),'text':''}
for r in c.execute("SELECT passage_id,verse_text FROM verse WHERE book_id=? AND passage_id IS NOT NULL ORDER BY passage_id,chapter,verse_num",(BOOK,)):
    p=PC.get(r['passage_id'])
    if p: p['text']+=(('' if not p['text'] else ' ')+(r['verse_text'] or '').strip())

def dimension_frame(span_id):
    byNr=defaultdict(list)
    for r in c.execute("""SELECT id,ve_nr,ve_label,value,pair_kind,from_span,to_span,direction,resolution,notes,source_provenance
                          FROM ve_lexical WHERE verse_span_id=? AND COALESCE(delete_flagged,0)=0 ORDER BY ve_nr,id""",(span_id,)):
        byNr[r['ve_nr']].append(r)
    out=[]; ids=[]
    for nr,label in LEGEND.items():
        if nr in byNr:
            for r in byNr[nr]:
                ids.append(r['id'])
                out.append(OrderedDict([('nr',nr),('label',label),('value',r['value']),('ve_lexical_id',r['id']),
                    ('item_type',r['pair_kind']),('from_span',r['from_span']),('to_span',r['to_span']),
                    ('direction',r['direction']),('resolution',r['resolution']),('notes',r['notes']),('provenance',r['source_provenance'])]))
        else:
            out.append(OrderedDict([('nr',nr),('label',label),('present',False)]))
    return out, ids

def signature(char_key, frame):
    parts=[]
    for d in frame:
        if d.get('present') is False: parts.append(('absent',str(d['nr'])))
        elif d['nr']==114: continue
        else: parts.append((str(d['nr']), str(d['value'])))
    return (char_key, tuple(sorted(parts)))

def build(fam):
    recs=c.execute("SELECT id,char_key,name,cluster,cluster_all FROM ib_characteristic WHERE book_scope=? AND family=? ORDER BY instance_count DESC,name",(BOOK,fam)).fetchall()
    ids=[r['id'] for r in recs]; qm=','.join('?'*len(ids))
    rows=c.execute(f"""SELECT si.id span_id, si.ib_char_id, v.reference, v.passage_id, v.id verse_id
                       FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                       WHERE si.ib_char_id IN ({qm}) ORDER BY v.id""",ids).fetchall()
    name={r['id']:r['name'] for r in recs}; ckey={r['id']:r['char_key'] for r in recs}
    ve_total=c.execute(f"""SELECT COUNT(*) n FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id
                           WHERE si.ib_char_id IN ({qm}) AND COALESCE(x.delete_flagged,0)=0""",ids).fetchone()['n']
    by_pass=defaultdict(list)
    for s in rows: by_pass[s['passage_id']].append(s)
    ordered=sorted(by_pass, key=lambda p:(PC.get(p) or {}).get('order',(9999,9999)))
    sig_reading={}; char_rc=defaultdict(int); reading_map=OrderedDict(); nodes=[]; n_dupe=0
    for pid in ordered:
        p=PC.get(pid) or {'ref':None,'text':None}; lex=[]
        for s in sorted(by_pass[pid], key=lambda x:(x['verse_id'],ckey.get(x['ib_char_id'],''))):
            frame,vids=dimension_frame(s['span_id']); ck=ckey.get(s['ib_char_id']); ref=s['reference']
            sig=signature(ck,frame)
            base=[('ib_char',name.get(s['ib_char_id'])),('char_key',ck),('reference',ref)]
            if sig not in sig_reading:
                char_rc[ck]+=1; rid=f"{ck}#{char_rc[ck]}"
                sig_reading[sig]={'reading_id':rid,'anchor_ref':ref,'anchor_passage':p['ref']}
                reading_map.setdefault(ck,[]).append(OrderedDict([('reading_id',rid),('anchor_ref',ref),('anchor_passage',p['ref']),('recurs_at',[])]))
                lex.append(OrderedDict(base+[('reading_id',rid),('anchor',True),('ve_lexical_ids',vids),('dimensions',frame)]))
            else:
                r=sig_reading[sig]; n_dupe+=1
                for rm in reading_map[ck]:
                    if rm['reading_id']==r['reading_id']: rm['recurs_at'].append(ref)
                lex.append(OrderedDict(base+[('reading_id',r['reading_id']),('duplicate',True),
                    ('same_as',OrderedDict([('reading_id',r['reading_id']),('anchor_ref',r['anchor_ref']),('anchor_passage',r['anchor_passage'])])),
                    ('ve_lexical_ids',vids),('dimensions',frame)]))
        nodes.append(OrderedDict([('passage_ref',p['ref']),('passage_text',p['text']),('lexicals',lex)]))
    distinct=sum(len(v) for v in reading_map.values())
    variation=[k for k,v in reading_map.items() if len(v)>1]
    sql=(f"SELECT COUNT(*) FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id "
         f"WHERE COALESCE(x.delete_flagged,0)=0 AND si.ib_char_id IN "
         f"(SELECT id FROM ib_characteristic WHERE book_scope={BOOK} AND family='{fam}');  -- must equal scope_counts.ve_lexical_rows")
    doc=OrderedDict([
      ('meta', OrderedDict([
        ('WORK_CONTRACT', OrderedDict([
          ('objective','For each distinct reading (anchor) below, write a narrative answering: what does this passage say about the ib_char item for the inner-being operations. Unit of work = the passage.'),
          ('unit_of_work','passage'),
          ('narrative_directives', DIRECTIVES),
          ('worklist', [n['passage_ref'] for n in nodes]),
          ('narratives_needed','one per distinct reading (anchor) = scope_counts.distinct_readings; duplicates (same_as) are cross-referenced, not re-narrated.'),
          ('completeness', OrderedDict([
             ('rule','Complete iff every anchor reading has a narrative, every duplicate is cross-referenced to its anchor, and within each anchor every dimension (incl. none/absent) is interpreted. Nothing here is pre-filtered.'),
             ('this_file_contains','EVERY ve_lexical row (all 101..116 dimensions, incl. value "none"; absences shown present:false) for this family\'s char-spans.'),
             ('verify_against_db', sql),
          ])),
          ('backtracking', OrderedDict([
             ('key','ve_lexical.id — on every present dimension (and collected per lexical in ve_lexical_ids).'),
             ('how','Raw row: SELECT * FROM ve_lexical WHERE id = <ve_lexical_id>.'),
             ('derivation','ib_characteristic(family) -[ib_char_id]-> verse_span_index -[verse_span_id]-> ve_lexical; verse_span_index.verse_id -> verse -> passage. verse_span_index is the join only, not emitted.'),
          ])),
          ('output', OrderedDict([
             ('format','TWO artefacts per family, both required: (1) a companion JSON keyed to this base source by reading_id; (2) a rendered markdown.'),
             ('json_file',f'verse-analysis/psalms/_narratives/psalms__{fam}__narratives.json'),
             ('md_file',f'verse-analysis/psalms/_narratives/psalms__{fam}__narratives.md'),
             ('granularity','One record per ANCHOR reading (reading_id). Duplicates (same_as) are NOT re-narrated — reference the anchor.'),
             ('record_shape',{'reading_id':'str','char_key':'str','ib_char':'str','anchor_ref':'str','passage_ref':'str',
                 'narrative':'the RAW/analytical read — grounded prose meeting directives 1-10, citing the dimensions it rests on (may use study terms).',
                 'story':'the SAME content retold as FLOWING PROSE for a GENERAL ENGLISH READER — a story, with NO study language or technical jargon: no dimension numbers/labels, no sense/operation/bearer/coupling/locus, no ve_lexical/ib_char/anchor. Tell it plainly and vividly as you would to a non-specialist; it must say what `narrative` says, only in plain English.',
                 'citations':'[ve_lexical_id,...] the narrative rests on (backtrack; directive 7)',
                 'recurrences':'[ref,...] where this reading recurs (directive 9)',
                 'variation_note':'why this reading differs from the item\'s other readings, where it applies (directive 10)'}),
             ('markdown_render','REQUIRED in every case. The .md shows, per passage: (a) the passage text, (b) the raw narrative, (c) the story. Renderer: scripts/_render_narratives_to_md_20260712.py --family <slug>.'),
             ('completeness','Every reading_id in this base source appears exactly once in the JSON; each record has BOTH narrative and story; each cites >=1 ve_lexical_id.'),
             ('destination','DB via output -> patch -> DB (all study work in the DB). The JSON is the transport; the .md is the readable rendering.'),
          ])),
        ])),
        ('family',fam),('book','Psalms'),('book_id',int(BOOK)),('generated','2026-07-12'),
        ('source_of_truth','database/bible_research.db — authoritative; regenerable view.'),
        ('ib_char_items',[OrderedDict([('char_key',r['char_key']),('meaning',r['name']),('cluster',short.get(r['cluster']) or r['cluster_all'])]) for r in recs]),
        ('reading_map', reading_map),
        ('scope_counts',OrderedDict([('ib_char_items',len(recs)),('passages',len(nodes)),('lexicals',len(rows)),
             ('distinct_readings',distinct),('duplicate_lexicals',n_dupe),('items_with_variation',len(variation)),('ve_lexical_rows',ve_total)])),
        ('dimension_frame',OrderedDict((str(k),v) for k,v in LEGEND.items())),
        ('reading_note','RAW + COMPLETE, nothing pre-judged. value "none" = reader found none; present:false = no row recorded. Both are evidence — what is NOT said can matter as much as what is.'),
      ])),
      ('passages', nodes),
    ])
    path=os.path.join(OUT,f"psalms__{fam}.json")
    json.dump(doc,open(path,'w',encoding='utf-8'),indent=1,ensure_ascii=False,default=str)
    return path,len(recs),len(nodes),len(rows),distinct,n_dupe,ve_total

if ALL:
    fams=[r['family'] for r in c.execute("SELECT DISTINCT family FROM ib_characteristic WHERE book_scope=? AND family IS NOT NULL",(BOOK,))]
    for f in sorted(fams):
        p,ni,np,nl,dr,du,vt=build(f); print(f"{f}: {ni} items, {np} pass, {nl} lex, {dr} distinct readings, {du} dupes, {vt} ve_lex")
else:
    p,ni,np,nl,dr,du,vt=build(FAM); print(f"family={FAM}: {ni} items, {np} passages, {nl} lexicals, {dr} distinct readings, {du} duplicates, {vt} ve_lexical rows -> {p}")
