#!/usr/bin/env python
"""Build the flattened reading projection + technical data layer for a re-read book (v1, 2026-07-14).

Per WA-projection-schema-and-companion-spec-v1. READ-ONLY on the DB; writes CSVs.
Emits four artifacts per book into outputs/projections/<book>/:
  1. <book>_reading_view.csv   one row per reading (analyst-facing; §C)
  2. <book>_nodes.csv          technical nodes (all fields; §D)
  3. <book>_edges.csv          the span-id pair edges — the movement graph (§D)
  4. <book>_dimensions_long.csv  raw ve_lexical reread rows (full fidelity; §D)

Key rules:
  - reading = ve_nr 114 (RELABELLED from 'discovery'); the evidence-anchored note.
  - NONE = ve_lexical value 'none' (reader found none); ABSENT = no row for that ve_nr (never read).
  - derived: translit (parsed), object_kind (rule), discovery_flag (finding-marker), same_as, lemma_freq_book.
  - base_gloss (invariant) vs sense/reading (contextual) kept as sibling columns (§G).

Usage:  python scripts/_build_projection_v1_20260714.py --book 20
        python scripts/_build_projection_v1_20260714.py --book all      # both reread books (19,20)
"""
import sqlite3, os, sys, csv, re, argparse
from collections import Counter, defaultdict

DB = os.path.join('database', 'bible_research.db')
OUTBASE = os.path.join('outputs', 'projections')
DIMS = {101:'sense',102:'type',103:'source',104:'seat',105:'bearer',106:'operation',107:'target',
        108:'manner',109:'intensity',110:'specifier',111:'effect',112:'coupling',113:'prohibition',
        114:'reading',115:'role',116:'locus',117:'device',118:'direction'}   # 114 relabelled; 117/118 added 2026-07-14
PROV = {19:'reread-psalms-2026', 20:'reread-proverbs-2026'}

PERSON = re.compile(r'\b(neighbou?r|enemy|enemies|king|queen|poor|needy|wife|husband|son|daughter|father|mother|'
                    r'friend|friends|man|men|woman|women|people|nation|child|children|others?|servant|master|ruler|fool|'
                    r'righteous|wicked|scoffer|sluggard|adulteress|stranger)\b', re.I)
SELF = re.compile(r'\b(himself|herself|myself|yourself|his own|her own|my own|one\'?s own|the self|his soul|my soul|the soul)\b', re.I)
GOD = re.compile(r'\b(god|the lord|lord|yhwh|the almighty|the holy one|redeemer)\b', re.I)
FINDING = re.compile(r'(\bnot a\b|\bNOT\b|\bthe finding\b|\bagainst\b|physical outcome|\bcf\b|emergent|\bsummit\b|'
                     r'not a human|\brather than\b|reveals|the point is|the gem|surpris)', re.I)
TRANSLIT_HEAD = re.compile(r"^([a-z][a-zA-Z''\-]+(?:\s+[a-z][a-zA-Z''\-]+)?)\s*\(")   # 'sheqer (falsehood) ...'
TRANSLIT_EMBED = re.compile(r"\b([A-Z]{2,})\s*\(([a-z][a-z''\-]+)\)")                   # 'PANTS (arag)'

def state(pivot, ve):
    """NONE / ABSENT / value for a dimension of this span."""
    if ve not in pivot: return 'ABSENT'
    v = pivot[ve]
    if v is None or str(v).strip().lower() == 'none' or str(v).strip() == '': return 'NONE'
    return v

def translit_of(reading, sense):
    for txt in (reading, sense):
        if not txt: continue
        m = TRANSLIT_HEAD.match(txt.strip())
        if m and m.group(1).islower(): return m.group(1), 'head'
        m = TRANSLIT_EMBED.search(txt)
        if m: return m.group(2), 'embed'
    return '', 'none'

def object_kind(target, bearer, locus):
    t = (target or '') + ' ' + (bearer or '')
    if not target or str(target).lower() in ('none','absent'): return 'none'
    if GOD.search(target) or locus == 'external:god': return 'god'
    if SELF.search(target): return 'self'
    if PERSON.search(target): return 'person'
    # abstractions: wisdom/justice/wealth/sin/etc. — a rough catch
    if re.search(r'\b(wisdom|folly|justice|righteousness|wealth|riches|sin|law|truth|honou?r|life|death|way|word|counsel|knowledge|fear|plans?|counsel|strife|peace)\b', target, re.I):
        return 'abstraction'
    return 'other'   # honest catch-all (derived/heuristic — never assert 'thing' when uncategorised)

def build_book(c, bid, bname):
    prov = PROV[bid]
    outdir = os.path.join(OUTBASE, bname.lower())
    os.makedirs(outdir, exist_ok=True)
    # all read-2026 char spans (the readings)
    spans = c.execute("""SELECT si.*, v.reference vref, v.book_id, v.chapter, v.verse_num, v.testament,
              v.genre, v.passage_id, v.is_passage_anchor, v.verse_text,
              ic.name ib_char, ic.char_key ick, ic.family, ic.lexical_gloss base_gloss,
              ic.read_sense_variants, ic.esv_words, ic.stems ic_stems, ic.morph_codes ic_morphs,
              ic.instance_count, ic.cluster_all
           FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
           LEFT JOIN ib_characteristic ic ON ic.id=si.ib_char_id
           WHERE v.book_id=? AND si.role='characteristic' AND si.role_provenance='read-2026'
           ORDER BY v.chapter, v.verse_num, si.id""", (bid,)).fetchall()
    # pivot ve_lexical (reread) per span
    pivot = defaultdict(dict)
    veh_map = {}   # span -> vehicle span-id (from the device(117) typed pair)
    for r in c.execute("""SELECT x.verse_span_id sid, x.ve_nr, x.value, x.to_span, x.resolution FROM ve_lexical x
           JOIN verse_span_index si ON si.id=x.verse_span_id JOIN verse v ON v.id=si.verse_id
           WHERE v.book_id=? AND x.source_provenance=? AND x.delete_flagged=0 AND x.ve_nr BETWEEN 101 AND 118""",
           (bid, prov)):
        pivot[r['sid']][r['ve_nr']] = r['value']
        if r['ve_nr'] == 117 and r['resolution'] == 'span' and r['to_span']:
            veh_map[r['sid']] = r['to_span']
    # salience
    lemma_freq = Counter(s['strongs'] for s in spans)
    ckey_members = defaultdict(list)
    for s in spans: ckey_members[s['ick']].append(s['id'])

    # ---- reading_view ----
    rv_cols = ['reading_id','span_id','book','chapter','verse_ref','corpus','genre','passage_id','anchor',
               'lemma','strongs','morph','pos','stem','surface_en','hebrew_form','translit','translit_conf',
               'char_key','ib_char','base_gloss','read_sense_variants','esv_words','family','cluster','cluster_all',
               'same_as','role_provenance','char_candidate_tag','lemma_freq_book','ib_instance_count',
               'sense','type','source','seat','bearer','operation','target','object_kind','manner',
               'intensity','specifier','effect','device','vehicle','coupling','prohibition','reading','discovery_flag',
               'role','locus','direction','verse_text']
    with open(os.path.join(outdir, f"{bname.lower()}_reading_view.csv"), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(rv_cols)
        for s in spans:
            p = pivot.get(s['id'], {})
            reading = state(p,114); sense = state(p,101)
            tr, trc = translit_of(p.get(114) or '', p.get(101) or '')
            same = [x for x in ckey_members.get(s['ick'], []) if x != s['id']]
            row = [
                (s['ick'] or s['strongs']) + f"#{s['id']}", s['id'], s['book_id'], s['chapter'], s['vref'],
                s['testament'], s['genre'], s['passage_id'], s['is_passage_anchor'],
                s['strongs'], s['primary_strong'], s['morph_code'], s['pos'], s['stem'], s['surface'],
                '', tr, trc,
                s['ick'], s['ib_char'], s['base_gloss'], s['read_sense_variants'], s['esv_words'], s['family'],
                s['cluster'], s['cluster_all'],
                '|'.join(str(x) for x in same), s['role_provenance'], s['char_candidate_tag'],
                lemma_freq[s['strongs']], s['instance_count'],
                sense, state(p,102), state(p,103), state(p,104), state(p,105), state(p,106), state(p,107),
                object_kind(p.get(107), p.get(105), p.get(116)), state(p,108),
                state(p,109), state(p,110), state(p,111), state(p,117), veh_map.get(s['id'], ''),
                state(p,112), state(p,113), reading,
                'present' if FINDING.search(reading or '') else 'absent',
                state(p,115), state(p,116), state(p,118), s['verse_text'],
            ]
            w.writerow(row)

    # ---- nodes (technical: every span field) ----
    node_cols = [k for k in spans[0].keys()]
    with open(os.path.join(outdir, f"{bname.lower()}_nodes.csv"), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(node_cols)
        for s in spans: w.writerow([s[k] for k in node_cols])

    # ---- edges (the movement graph) ----
    edges = c.execute("""SELECT x.from_span, x.to_span, x.ve_nr, x.ve_label edge_type, x.direction, x.pair_kind,
              x.value phrase, v.book_id, v.reference from_verse_ref
           FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id JOIN verse v ON v.id=si.verse_id
           WHERE v.book_id=? AND x.source_provenance=? AND x.delete_flagged=0 AND x.resolution='span'
             AND x.to_span IS NOT NULL AND x.to_span!=''""", (bid, prov)).fetchall()
    with open(os.path.join(outdir, f"{bname.lower()}_edges.csv"), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(['from_span','to_span','edge_type','ve_nr','direction','pair_kind','phrase','book','from_verse_ref'])
        for e in edges:
            w.writerow([e['from_span'], e['to_span'], e['edge_type'], e['ve_nr'], e['direction'], e['pair_kind'],
                        e['phrase'], e['book_id'], e['from_verse_ref']])

    # ---- dimensions_long (raw fidelity) ----
    with open(os.path.join(outdir, f"{bname.lower()}_dimensions_long.csv"), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(['verse_span_id','ve_nr','ve_label','value','from_span','to_span','resolution','pair_kind'])
        for r in c.execute("""SELECT x.verse_span_id, x.ve_nr, x.ve_label, x.value, x.from_span, x.to_span, x.resolution, x.pair_kind
               FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id JOIN verse v ON v.id=si.verse_id
               WHERE v.book_id=? AND x.source_provenance=? AND x.delete_flagged=0 ORDER BY x.verse_span_id, x.ve_nr""",
               (bid, prov)):
            w.writerow([r['verse_span_id'], r['ve_nr'], r['ve_label'], r['value'], r['from_span'], r['to_span'], r['resolution'], r['pair_kind']])

    print(f"  {bname}: {len(spans)} readings | {len(edges)} edges -> {outdir}/")
    return len(spans), len(edges)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--book', required=True)
    a = ap.parse_args()
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    books = [19,20] if a.book == 'all' else [int(a.book) if str(a.book).isdigit()
             else c.execute("SELECT id FROM books WHERE LOWER(name) LIKE ?", (f"%{a.book.lower()}%",)).fetchone()[0]]
    print("# building projection(s)")
    for bid in books:
        bname = c.execute("SELECT name FROM books WHERE id=?", (bid,)).fetchone()[0]
        build_book(c, bid, bname)
    c.close()

if __name__ == '__main__':
    main()
