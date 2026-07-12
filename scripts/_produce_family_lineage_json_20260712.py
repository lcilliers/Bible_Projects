"""Produce a RAW LINEAGE file for one family: the actual DB chain, not an
assembled analytical view.

For the selected family it emits:
  meta:
    - family (from ib_characteristic.family) + book
    - stats: #ib_characteristic records, #linked spans, #ve_lexical rows, #passages
    - linkage: documents the REAL foreign-key structure (does ib_char reference
      ve_lexical? — no; the chain runs ib_char <- verse_span_index -> ve_lexical),
      with the declared FKs read live from PRAGMA.
  build_up: the raw chain per record —
    ib_characteristic record
      -> spans (verse_span_index, via .ib_char_id)
          -> ve_lexical rows (RAW, unmodified, via .verse_span_id)
          -> passage text (via verse_span_index.verse_id -> verse.passage_id)

Raw = ve_lexical columns are emitted as stored (no swap-correction, no
self-loop filtering, no relabelling). Authoritative store = the DB; this file
is a generated lineage view.

Usage: python scripts/_produce_family_lineage_json_20260712.py --family <slug> [--book 19]
"""
import sqlite3, os, json, sys
from collections import OrderedDict

FAM = 'anger-wrath-vexation'; BOOK = '19'
if '--family' in sys.argv: FAM = sys.argv[sys.argv.index('--family')+1]
if '--book'   in sys.argv: BOOK = sys.argv[sys.argv.index('--book')+1]
OUT = 'verse-analysis/psalms/_lineage'; os.makedirs(OUT, exist_ok=True)

c = sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory = sqlite3.Row

def declared_fks(t):
    return [f"{r['from']} -> {r['table']}.{r['to']}" for r in c.execute(f"PRAGMA foreign_key_list({t})")] or ["(none declared)"]

# --- records for the family ---
recs = c.execute("SELECT * FROM ib_characteristic WHERE book_scope=? AND family=? ORDER BY instance_count DESC, name",(BOOK,FAM)).fetchall()
ids = [r['id'] for r in recs]
qm = ",".join("?"*len(ids))

nspan = c.execute(f"SELECT COUNT(*) n FROM verse_span_index WHERE ib_char_id IN ({qm})", ids).fetchone()['n']
nlex  = c.execute(f"SELECT COUNT(*) n FROM ve_lexical WHERE COALESCE(delete_flagged,0)=0 AND verse_span_id IN (SELECT id FROM verse_span_index WHERE ib_char_id IN ({qm}))", ids).fetchone()['n']
npass = c.execute(f"SELECT COUNT(DISTINCT v.passage_id) n FROM verse_span_index si JOIN verse v ON v.id=si.verse_id WHERE si.ib_char_id IN ({qm})", ids).fetchone()['n']

# passage text cache
pass_cache = {}
def passage_of(verse_id):
    v = c.execute("SELECT id,reference,passage_id FROM verse WHERE id=?",(verse_id,)).fetchone()
    pid = v['passage_id']
    if pid not in pass_cache:
        p = c.execute("SELECT ref FROM passage WHERE id=?",(pid,)).fetchone()
        verses = c.execute("SELECT reference,verse_text FROM verse WHERE passage_id=? ORDER BY chapter,verse_num",(pid,)).fetchall()
        pass_cache[pid] = {"passage_id": pid, "passage_ref": (p['ref'] if p else None),
                           "verse_refs": [x['reference'] for x in verses],
                           "text": " ".join((x['verse_text'] or '').strip() for x in verses)}
    return pass_cache[pid], v['reference']

def raw_lexical(span_id):
    rows = c.execute("""SELECT id,ve_nr,ve_label,value,pair_kind,from_span,to_span,direction,resolution,notes,gate,source_provenance
                        FROM ve_lexical WHERE verse_span_id=? AND COALESCE(delete_flagged,0)=0 ORDER BY ve_nr""",(span_id,))
    out=[]
    for r in rows:
        out.append(OrderedDict([("id",r["id"]),("ve_nr",r["ve_nr"]),("ve_label",r["ve_label"]),
            ("value",r["value"]),("pair_kind",r["pair_kind"]),("from_span",r["from_span"]),
            ("to_span",r["to_span"]),("direction",r["direction"]),("resolution",r["resolution"]),
            ("notes",r["notes"]),("gate",r["gate"]),("source_provenance",r["source_provenance"])]))
    return out

build_up=[]
for rec in recs:
    spans = c.execute("SELECT id,reference,verse_id,word_index,surface,morph_code,stem,primary_strong,characteristic,char_candidate,role FROM verse_span_index WHERE ib_char_id=? ORDER BY id",(rec['id'],)).fetchall()
    span_nodes=[]
    for s in spans:
        pnode, vref = passage_of(s['verse_id'])
        span_nodes.append(OrderedDict([
            ("verse_span_index", OrderedDict([(k, s[k]) for k in ['id','reference','verse_id','word_index','surface','morph_code','stem','primary_strong','characteristic','char_candidate','role']])),
            ("ve_lexical_rows_raw", raw_lexical(s['id'])),
            ("passage", pnode),
        ]))
    build_up.append(OrderedDict([
        ("ib_characteristic", OrderedDict([(k, rec[k]) for k in ['id','char_key','name','family','cluster','cluster_all','instance_count','key_span_id','lexical_gloss','read_sense_variants']])),
        ("spans", span_nodes),
    ]))

doc = OrderedDict([
  ("meta", OrderedDict([
    ("family", FAM), ("book","Psalms"), ("book_id", int(BOOK)),
    ("source_of_truth", "database/bible_research.db (SQLite) — authoritative. This file is a GENERATED lineage view; delete it and nothing is lost."),
    ("generated", "2026-07-12"),
    ("stats", OrderedDict([
        ("ib_characteristic_records", len(recs)),
        ("linked_spans_verse_span_index", nspan),
        ("ve_lexical_rows", nlex),
        ("distinct_passages", npass),
    ])),
    ("linkage", OrderedDict([
        ("question", "What FK does ib_characteristic use? Does it reference ve_lexical?"),
        ("answer", "NO. ib_characteristic declares no foreign keys and does not reference ve_lexical. "
                   "The link is reverse + indirect: verse_span_index.ib_char_id points to ib_characteristic.id "
                   "(a bypass-link, NOT a declared FK), and ve_lexical.verse_span_id points to verse_span_index.id "
                   "(the one DECLARED FK). So ib_characteristic reaches ve_lexical ONLY through verse_span_index. "
                   "ib_characteristic.key_span_id holds a single representative span, not the whole set."),
        ("fk_chain", [
            "ib_characteristic.id  <--(verse_span_index.ib_char_id)--  verse_span_index   [1 record -> many spans; bypass-link]",
            "verse_span_index.id   <--(ve_lexical.verse_span_id)--     ve_lexical         [1 span -> many dimension rows; DECLARED FK]",
            "verse_span_index.verse_id --> verse.id;  verse.passage_id --> passage.id     [span -> its verse -> its passage text]",
            "ib_characteristic.key_span_id --> verse_span_index.id   [ONE representative span only]",
        ]),
        ("declared_foreign_keys", OrderedDict([(t, declared_fks(t)) for t in ['ib_characteristic','verse_span_index','ve_lexical','verse']])),
    ])),
    ("build_up_note", "Each build_up entry walks the raw chain: ib_characteristic record -> its spans (verse_span_index) -> each span's RAW ve_lexical rows (unmodified) -> the passage text that span sits in."),
  ])),
  ("build_up", build_up),
])

slug = FAM.lower()
path = os.path.join(OUT, f"psalms__{slug}__lineage.json")
json.dump(doc, open(path,'w',encoding='utf-8'), indent=1, ensure_ascii=False, default=str)
print(f"family={FAM} records={len(recs)} spans={nspan} ve_lexical={nlex} passages={npass}")
print("written ->", path)
