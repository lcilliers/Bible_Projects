"""Produce a JSON BASE SOURCE per family (+ one OUTLIERS file) for Psalms.

Each file is the complete, flat, self-describing evidence for one family: every
meaning-record, every instance (master span), with its full lexical ledger
(ve_nr dimensions + relational edges), morphology, verse text, and passage text
(normalised into a file-level `passages` map to avoid duplication). A `meta`
block documents the book+family scope, provenance, counts, the dimension legend,
and the structure of the JSON itself.

Outputs -> outputs/data/psalms-family-base-sources/psalms__<family>.json
        -> outputs/data/psalms-family-base-sources/psalms__OUTLIERS.json

Read-only. Usage: python scripts/_produce_family_base_source_json_20260711.py
"""
import sqlite3, os, json, re
from collections import defaultdict, OrderedDict

GEN = "2026-07-11"
OUT = "outputs/data/psalms-family-base-sources"
os.makedirs(OUT, exist_ok=True)
c = sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory = sqlite3.Row

short = {r['cluster_code']:(r['short_name'] or r['cluster_code']) for r in c.execute("SELECT cluster_code,short_name FROM cluster")}
LEGEND = {101:'sense',102:'type',103:'source',104:'seat',105:'bearer',106:'operation',107:'target',
          108:'manner',109:'intensity',110:'specifier',111:'effect',112:'coupling',113:'prohibition',
          114:'discovery',115:'role',116:'locus'}

# --- outlier determination (genuine crossovers) — mirrors the comparison script ---
EXPECTED = {'inner-seat-heart-soul-spirit':'M47','praise-extol-sing':'M22','prayer-petition-crying-out':'M21',
 'knowing-understanding':'M15','joy-gladness':'M04','desire-longing-appetite':'M29','fear-of-god-awe':'M01',
 'trust-refuge-security':'M19','righteousness-integrity':'M26','blessing-benediction':'M39','wickedness-ungodliness':'M27',
 'malice-enmity-persecution':'M06','sin-guilt-iniquity':'M10','faint-despair-languishing':'M24','thanksgiving':'M22',
 'keeping-guarding-vigilance':'M30','walk-way-conduct':'M30','memory-remembrance':'M41','hope-waiting':'M18',
 'deceit-falsehood':'M14','speech-mouth-tongue':'M42','pride-arrogance-scoffing':'M08','wisdom-folly-teaching':'M15',
 'love-devotion':'M05','grief-lament-sorrow':'M03','rebellion-stubbornness':'M10','shame-confusion':'M07',
 'humility-lowliness-contrition':'M09','worship-prostration-service':'M36','violence-cruelty':'M06',
 'being-heard-listening':'M21','restoration-revival-satisfaction':'M38','faith-faithfulness-truth':'M13',
 'anger-wrath-vexation':'M02','being-searched-tested-by-god':'M35','turning-repentance':'M11','rest-stillness-peace':'M33',
 'life-death-vitality':'M25','strength-courage-steadfastness':'M23','torah-obedience-word':'M30','confession-forgiveness':'M11'}
ADJ = [{'M10','M27','M16','M08','M14','M06'},{'M09','M24','M07'},{'M04','M29','M22','M46','M28'},
       {'M21','M37','M22','M18','M19','M42','M41'},{'M15','M17','M13','M16'},{'M26','M12','M30','M13'},
       {'M03','M24','M01','M20'},{'M05','M39','M36','M13'},{'M11','M10','M30','M45'},{'M38','M46','M23'},{'M02','M06','M28'}]
def adjacent(a,b): return any(a in s and b in s for s in ADJ)
def is_outlier(family, cluster):
    exp = EXPECTED.get(family)
    return bool(cluster and exp and cluster != exp and not adjacent(cluster, exp))

# --- passage cache (normalised) ---
passages = {}
prows = c.execute("""SELECT p.id, p.ref, p.verse_count FROM passage p WHERE p.book_id=19""").fetchall()
pmeta = {r['id']:{'ref':r['ref'],'verse_count':r['verse_count']} for r in prows}
for r in c.execute("""SELECT passage_id, reference, verse_text FROM verse
                      WHERE book_id=19 AND passage_id IS NOT NULL ORDER BY passage_id, chapter, verse_num"""):
    pid=r['passage_id']
    passages.setdefault(pid, {'passage_ref': (pmeta.get(pid) or {}).get('ref'), 'verse_refs':[], 'text':''})
    passages[pid]['verse_refs'].append(r['reference'])
    passages[pid]['text'] += (('' if not passages[pid]['text'] else ' ') + (r['verse_text'] or '').strip())

# --- ve_lexical per span ---
CH = "si.role='characteristic' AND si.role_provenance='read-2026' AND v.book_id=19"
velex = defaultdict(list)
for r in c.execute(f"""SELECT x.verse_span_id sp, x.ve_nr, x.ve_label, x.value, x.notes,
      x.from_span, x.to_span, x.direction, x.resolution, x.pair_kind
   FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id JOIN verse v ON v.id=si.verse_id
   WHERE {CH} AND COALESCE(x.delete_flagged,0)=0 ORDER BY x.verse_span_id, x.ve_nr"""):
    velex[r['sp']].append(r)

# --- spans with their meaning-record + verse ---
spans = c.execute(f"""SELECT si.id span_id, si.reference, si.word_index, si.surface, si.morph_code, si.stem,
      si.characteristic read_char, si.primary_strong,
      ic.char_key, ic.name meaning, ic.family, ic.cluster, ic.cluster_all, ic.instance_count,
      ic.stems, ic.morph_codes, ic.esv_words, ic.lexical_gloss, ic.read_sense_variants,
      v.verse_text, v.passage_id, v.is_passage_anchor, v.genre,
      (SELECT target_word FROM wa_verse_records w WHERE w.verse_span_id=si.id LIMIT 1) esv
   FROM verse_span_index si JOIN verse v ON v.id=si.verse_id JOIN ib_characteristic ic ON ic.id=si.ib_char_id
   WHERE {CH} ORDER BY ic.family, ic.name, v.id""").fetchall()

def instance_obj(s):
    lex=[]; edges=[]
    for r in velex.get(s['span_id'], []):
        # every ve_nr row is a dimension reading; pair_kind is its item-type
        item={'nr':r['ve_nr'],'label':r['ve_label'] or LEGEND.get(r['ve_nr']),
              'value':r['value'],'item_type':r['pair_kind']}
        if r['resolution'] and r['resolution']!='none': item['resolution']=r['resolution']
        if r['notes']: item['notes']=r['notes']
        lex.append(item)
        # a genuine relational edge = a dimension whose item links to ANOTHER span
        if r['from_span'] or r['to_span']:
            edges.append({'on_dimension':r['ve_nr'],'label':r['ve_label'] or LEGEND.get(r['ve_nr']),
                          'item_type':r['pair_kind'],'from_span':r['from_span'],'to_span':r['to_span'],
                          'direction':r['direction'],'resolution':r['resolution']})
    return OrderedDict([
        ('span_id', s['span_id']),
        ('reference', s['reference']),
        ('hebrew_surface', s['surface']),
        ('esv_word', s['esv']),
        ('morphology', {'morph_code':s['morph_code'],'stem':s['stem']}),
        ('read_characteristic', s['read_char']),
        ('position', {'word_index':s['word_index'],'passage_id':s['passage_id'],
                      'is_passage_anchor':bool(s['is_passage_anchor']),'genre':s['genre']}),
        ('verse_text', s['verse_text']),
        ('passage_id', s['passage_id']),
        ('lexical', lex),
        ('edges', edges),
    ])

# group family -> meaning(char_key) -> [spans]
fam_mean = defaultdict(lambda: defaultdict(list))
mean_row = {}
for s in spans:
    fam_mean[s['family']][s['char_key']].append(s)
    mean_row[s['char_key']] = s

def meaning_obj(ck, span_list):
    m = mean_row[ck]
    out = is_outlier(m['family'], m['cluster'])
    o = OrderedDict([
        ('char_key', ck),
        ('meaning', m['meaning']),
        ('lemma', ck.split(':')[0]),
        ('cluster', {'code':m['cluster'],'name':short.get(m['cluster']),'all_candidates':m['cluster_all']}),
        ('instance_count', m['instance_count']),
        ('is_outlier', out),
    ])
    if out:
        o['outlier_note'] = f"meaning-family '{m['family']}' expects cluster {EXPECTED.get(m['family'])}({short.get(EXPECTED.get(m['family']))}), but the term-cluster is {m['cluster']}({short.get(m['cluster'])})"
    o['evidence'] = {'stems':m['stems'],'morph_codes':m['morph_codes'],'esv_words':m['esv_words'],
                     'lexical_gloss':m['lexical_gloss'],'read_sense_variants':m['read_sense_variants']}
    o['instances'] = [instance_obj(s) for s in span_list]
    return o

STRUCTURE = {
 "meta": "book+family scope, provenance, counts, dimension_legend (ve_nr->name), and this structure doc",
 "passages": "map of passage_id -> {passage_ref, verse_refs[], text}; instances reference it by passage_id (normalised to avoid repeating passage text)",
 "meanings[]": {
   "char_key":"lemma:normalised-ESV key (record identity)",
   "meaning":"readable meaning label (modal ESV rendering)",
   "lemma":"base Strong's number",
   "cluster":"{code,name,all_candidates} — term-based M-code cluster (master->1 mti_term->1 cluster)",
   "instance_count":"number of master spans",
   "is_outlier":"true if the term-cluster is a genuine (non-adjacent) crossover from the family's expected cluster",
   "evidence":"aggregate proof on the record: stems, morph_codes, esv_words, lexical_gloss (attested inventory), read_sense_variants (the read phrases)",
   "instances[]": {
     "span_id":"verse_span_index.id (the unique master)",
     "reference":"verse reference",
     "hebrew_surface":"the Hebrew surface word of the span",
     "esv_word":"the ESV rendering in this verse",
     "morphology":"{morph_code, stem}",
     "read_characteristic":"the read characteristic-in-words on the master",
     "position":"{word_index, passage_id, is_passage_anchor, genre}",
     "verse_text":"full text of this verse (ESV)",
     "passage_id":"-> lookup in top-level passages map for the passage text",
     "lexical":"[] the full ve_lexical ledger for this span: one {nr,label,value,item_type,resolution?,notes?} per dimension. item_type = value|flag|event|note|pair (the method's item kinds). Dimensions: 101 sense,102 type,103 source,104 seat,105 bearer,106 operation,107 target,108 manner,109 intensity,110 specifier,111 effect,112 coupling,113 prohibition,114 discovery,115 role,116 locus",
     "edges":"[] the relational sub-set of the ledger — dimensions whose item links to ANOTHER span (the inner-being network): {on_dimension,label,item_type,from_span,to_span,direction,resolution}",
   }
 }
}

def write_file(fname, scope, meanings_dict, description):
    used_pids = {s['passage_id'] for ms in meanings_dict.values() for s in ms if s['passage_id']}
    meanings = [meaning_obj(ck, sl) for ck, sl in sorted(meanings_dict.items(),
                key=lambda kv: -mean_row[kv[0]]['instance_count'])]
    ninst = sum(len(sl) for sl in meanings_dict.values())
    doc = OrderedDict([
      ('meta', OrderedDict([
        ('book','Psalms'), ('book_id',19), ('scope',scope), ('generated',GEN),
        ('source_provenance','ib_characteristic v3 (meaning-keyed) + family grouping v1 + term-based cluster v2'),
        ('description',description),
        ('counts',{'meanings':len(meanings),'instances':ninst,'passages':len(used_pids)}),
        ('dimension_legend',{str(k):v for k,v in LEGEND.items()}),
        ('structure',STRUCTURE),
      ])),
      ('passages',{str(pid):passages[pid] for pid in sorted(used_pids) if pid in passages}),
      ('meanings',meanings),
    ])
    path=os.path.join(OUT,fname)
    json.dump(doc, open(path,'w',encoding='utf-8'), indent=1, ensure_ascii=False, default=str)
    return path, len(meanings), ninst

# --- write one file per family ---
written=0
for fam, md in sorted(fam_mean.items()):
    slug=re.sub(r'[^a-z0-9-]+','-',fam.lower()).strip('-')
    desc=f"Base source for the Psalms inner-being family '{fam}': all meanings, instances, lexical ledgers, and verse/passage text."
    p,nm,ni=write_file(f"psalms__{slug}.json", {'family':fam}, md, desc)
    written+=1
print(f"family files written: {written}")

# --- outliers file (genuine crossovers) ---
out_md=defaultdict(list)
for s in spans:
    if is_outlier(s['family'], s['cluster']):
        out_md[s['char_key']].append(s)
desc=("All genuine cross-over meanings across Psalms: records whose term-based CLUSTER names a concept "
      "UNRELATED (non-adjacent) to their meaning-based FAMILY's expected cluster. Collected for review; "
      "each still lives in its family file too.")
p,nm,ni=write_file("psalms__OUTLIERS.json", {'set':'outliers-genuine-crossovers'}, out_md, desc)
print(f"outliers file: {nm} meanings, {ni} instances -> {p}")
print(f"\nAll files in: {OUT}")
