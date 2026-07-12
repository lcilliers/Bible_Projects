"""Base source per family, PASSAGE-NODE form (researcher spec 2026-07-12).

Principle: as close to the DB as possible, without carrying everything. Only two
things: (1) the passage text, (2) the lexicals that match the family's ib_char
rows. NO verse_span_index (noise). Organised as passage nodes: each node = the
passage text, then the lexicals that fall in that passage.

Purpose: write, per passage, a narrative answering — what does this passage say
about the ib_char item for the inner-being operations.

Node shape:
  { passage_ref, passage_text,
    lexicals: [ { ib_char, char_key, reference, dimensions:[ {nr,label,value,resolution?,notes?} ] } ] }

Only ve_lexical rows for char-spans linked to this family's ib_characteristic
rows are included. Span-link plumbing (span ids, from/to_span, morphology) is
dropped — the verse reference is kept as the only locator.

Usage: python scripts/_produce_family_passage_base_source_v2_20260712.py --family <slug> [--book 19] [--all]
Output: verse-analysis/psalms/_base-sources/psalms__<slug>.json
"""
import sqlite3, os, json, sys
from collections import defaultdict, OrderedDict

BOOK='19'; FAM=None; ALL='--all' in sys.argv
if '--family' in sys.argv: FAM=sys.argv[sys.argv.index('--family')+1]
if '--book' in sys.argv: BOOK=sys.argv[sys.argv.index('--book')+1]
OUT='verse-analysis/psalms/_base-sources'; os.makedirs(OUT,exist_ok=True)
c=sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory=sqlite3.Row
short={r['cluster_code']:(r['short_name'] or r['cluster_code']) for r in c.execute("SELECT cluster_code,short_name FROM cluster")}
def declared_fks(t): return [f"{r['from']} -> {r['table']}.{r['to']}" for r in c.execute(f"PRAGMA foreign_key_list({t})")] or ["(none declared)"]
LEGEND={101:'sense',102:'type',103:'source',104:'seat',105:'bearer',106:'operation',107:'target',108:'manner',
        109:'intensity',110:'specifier',111:'effect',112:'coupling',113:'prohibition',114:'discovery',115:'role',116:'locus'}

# passage cache (id -> ref, text, order key)
PC={}
for r in c.execute("SELECT id,ref,start_chapter,start_verse FROM passage WHERE book_id=?",(BOOK,)):
    PC[r['id']]={'ref':r['ref'],'order':(r['start_chapter'] or 0, r['start_verse'] or 0),'verses':[],'text':''}
for r in c.execute("SELECT passage_id,reference,verse_text FROM verse WHERE book_id=? AND passage_id IS NOT NULL ORDER BY passage_id,chapter,verse_num",(BOOK,)):
    p=PC.get(r['passage_id']);
    if p: p['verses'].append(r['reference']); p['text']+=(('' if not p['text'] else ' ')+(r['verse_text'] or '').strip())

# ve_lexical per span (dimensions only, span-link plumbing dropped)
def dims(span_id):
    out=[]
    for r in c.execute("""SELECT ve_nr,ve_label,value,resolution,notes FROM ve_lexical
                          WHERE verse_span_id=? AND COALESCE(delete_flagged,0)=0 ORDER BY ve_nr""",(span_id,)):
        d=OrderedDict([('nr',r['ve_nr']),('label',r['ve_label'] or LEGEND.get(r['ve_nr'])),('value',r['value'])])
        if r['resolution'] and r['resolution']!='none': d['resolution']=r['resolution']
        if r['notes']: d['notes']=r['notes']
        out.append(d)
    return out

def build(fam):
    recs=c.execute("SELECT id,char_key,name,cluster,cluster_all FROM ib_characteristic WHERE book_scope=? AND family=? ORDER BY instance_count DESC,name",(BOOK,fam)).fetchall()
    ids=[r['id'] for r in recs]; qm=','.join('?'*len(ids))
    # spans of the family (via ib_char_id) -> passage grouping; verse_span_index used only as the join, never emitted
    rows=c.execute(f"""SELECT si.id span_id, si.ib_char_id, v.reference, v.passage_id, v.id verse_id
                       FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                       WHERE si.ib_char_id IN ({qm}) ORDER BY v.id""",ids).fetchall()
    name={r['id']:r['name'] for r in recs}; ckey={r['id']:r['char_key'] for r in recs}
    by_pass=defaultdict(list); nlex=0
    for s in rows:
        by_pass[s['passage_id']].append(s); nlex+=1
    nodes=[]
    for pid in sorted(by_pass, key=lambda p:(PC.get(p) or {}).get('order',(9999,9999))):
        p=PC.get(pid) or {'ref':None,'text':None}
        lex=[]
        for s in sorted(by_pass[pid], key=lambda x:(x['verse_id'], ckey.get(x['ib_char_id'],''))):
            lex.append(OrderedDict([
                ('ib_char', name.get(s['ib_char_id'])),
                ('char_key', ckey.get(s['ib_char_id'])),
                ('reference', s['reference']),
                ('dimensions', dims(s['span_id'])),
            ]))
        nodes.append(OrderedDict([('passage_ref',p['ref']),('passage_text',p['text']),('lexicals',lex)]))
    doc=OrderedDict([
      ('meta', OrderedDict([
        ('family',fam),('book','Psalms'),('book_id',int(BOOK)),('generated','2026-07-12'),
        ('purpose','Per-passage base source: each node = passage text + the lexicals of this family\'s ib_char rows that fall in it. Write, per passage, a narrative of what the passage says about the ib_char item for the inner-being operations.'),
        ('source_of_truth','database/bible_research.db — authoritative; this is a regenerable view (delete it and nothing is lost).'),
        ('linkage', OrderedDict([
          ('derivation','ib_characteristic (this family) --[ib_char_id]--> verse_span_index --[verse_span_id]--> ve_lexical; and verse_span_index.verse_id --> verse --> passage. verse_span_index is the JOIN ONLY and is intentionally NOT emitted (dropped as noise).'),
          ('does_ib_char_reference_ve_lexical','No. ib_characteristic declares no FK; the one declared FK is ve_lexical.verse_span_id -> verse_span_index.id; the join to ve_lexical runs through verse_span_index.'),
          ('declared_foreign_keys', OrderedDict([(t, declared_fks(t)) for t in ['ib_characteristic','verse_span_index','ve_lexical','verse']])),
        ])),
        ('ib_char_items',[OrderedDict([('char_key',r['char_key']),('meaning',r['name']),('cluster',short.get(r['cluster']) or r['cluster_all'])]) for r in recs]),
        ('stats',{'ib_char_items':len(recs),'spans_joined':len(rows),'lexicals':nlex,'passages':len(nodes)}),
        ('dimension_legend',{str(k):v for k,v in LEGEND.items()}),
      ])),
      ('passages', nodes),
    ])
    path=os.path.join(OUT,f"psalms__{fam}.json")
    json.dump(doc,open(path,'w',encoding='utf-8'),indent=1,ensure_ascii=False,default=str)
    return path,len(recs),len(nodes),nlex

if ALL:
    fams=[r['family'] for r in c.execute("SELECT DISTINCT family FROM ib_characteristic WHERE book_scope=? AND family IS NOT NULL",(BOOK,))]
    for f in sorted(fams):
        p,ni,np,nl=build(f); print(f"{f}: {ni} items, {np} passages, {nl} lexicals")
else:
    p,ni,np,nl=build(FAM); print(f"family={FAM}: {ni} ib_char items, {np} passages, {nl} lexicals -> {p}")
