"""(v3) Rebuild ib_characteristic keyed on MEANING-IN-CONTEXT, not base lemma.

WHY: v2 keyed on base lemma (substr(primary_strong,1,5)) which MERGED distinct
meanings of one word (halal praise+boast+deride; gur sojourn+stir-strife).
The 2026-07-11 dry runs proved:
  - stem alone is insufficient (Piel still holds praise+deride);
  - the read-sense field (ve_nr 101) is often a CONTEXTUAL PHRASE, not the word's
    meaning ("he restores my soul") -> keying on it OVER-SPLITS (1269 records).
  - the ESV rendering + stem captures the TRUE meaning: halal -> (Piel,praise 37),
    (Piel,deride 1), (Hithpael,glory/exult/boast), (Qal,boastful); nephesh ->
    soul/life/self/craving. This even splits the Piel praise/deride homograph.

RECORD IDENTITY = (base-lemma, stem, normalised-ESV-rendering). The read-sense
phrases are PRESERVED as evidence (read_sense_variants) so nothing is lost.
Record NAME = the modal raw ESV word (readable). Grouping is by the word's
rendered meaning, with form/ESV/morph/gloss shown on the record so any bad merge
is visible (guards the grouping-danger). Researcher direction 2026-07-11.

Reversible: current book records exported to JSON before delete. Derived table.

Usage:  python scripts/_apply_rebuild_ib_char_meaning_keyed_v3_20260711.py [--book 19] [--live]
"""
import sqlite3, os, re, json, sys, datetime
from collections import defaultdict, Counter

BOOK = '19'
LIVE = '--live' in sys.argv
if '--book' in sys.argv: BOOK = sys.argv[sys.argv.index('--book')+1]
STAMP = datetime.datetime.now(datetime.UTC).strftime('%Y%m%dT%H%M%SZ')
PROV = 'ib-char-index-v3-meaning-keyed-2026'

DB = os.path.join('database','bible_research.db')
c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; cur = c.cursor()

def norm_esv(w):
    """Normalise an ESV surface word to a meaning-stem so inflections merge
    (praise/praised/praises/praising -> prais) and doubled artifacts collapse
    (soul soul -> soul). Used only as the grouping key; the readable NAME is the
    modal raw word."""
    if not w: return '(none)'
    w = re.sub(r'[^a-z]', '', w.lower())
    if w and len(w) % 2 == 0 and w[:len(w)//2] == w[len(w)//2:]:  # 'soulsoul'->'soul'
        w = w[:len(w)//2]
    for suf in ('ings','ing','ied','ies','ed','es','s'):
        if len(w) > len(suf)+2 and w.endswith(suf):
            w = w[:-len(suf)]; break
    if len(w) > 4 and w.endswith('e'):   # silent-e: praise->prais == praised->prais
        w = w[:-1]
    return w or '(none)'

def hascol(t,col): return any(r['name']==col for r in cur.execute(f"PRAGMA table_info({t})"))

for col in ['stems','morph_codes','esv_words','lexical_gloss','read_sense_variants']:
    if not hascol('ib_characteristic', col):
        if LIVE:
            cur.execute(f"ALTER TABLE ib_characteristic ADD COLUMN {col} TEXT"); print("  +column", col)
        else:
            print("  [dry] would add column", col)

CH = f"si.role='characteristic' AND si.role_provenance='read-2026' AND v.book_id={BOOK}"
rows = cur.execute(f"""
  SELECT si.id span_id, v.reference, substr(si.primary_strong,1,5) lemma,
    (SELECT value FROM ve_lexical x WHERE x.verse_span_id=si.id AND x.ve_nr=101 AND COALESCE(x.delete_flagged,0)=0 LIMIT 1) sense,
    (SELECT value FROM ve_lexical x WHERE x.verse_span_id=si.id AND x.ve_nr=106 AND COALESCE(x.delete_flagged,0)=0 LIMIT 1) op,
    (SELECT stem        FROM wa_verse_records w WHERE w.reference=v.reference AND w.term_id LIKE substr(si.primary_strong,1,5)||'%' AND COALESCE(w.delete_flagged,0)=0 LIMIT 1) stem,
    (SELECT morph_code  FROM wa_verse_records w WHERE w.reference=v.reference AND w.term_id LIKE substr(si.primary_strong,1,5)||'%' AND COALESCE(w.delete_flagged,0)=0 LIMIT 1) morph,
    (SELECT target_word FROM wa_verse_records w WHERE w.reference=v.reference AND w.term_id LIKE substr(si.primary_strong,1,5)||'%' AND COALESCE(w.delete_flagged,0)=0 LIMIT 1) esv
  FROM verse_span_index si JOIN verse v ON v.id=si.verse_id WHERE {CH}""").fetchall()
print(f"Characteristic spans in book {BOOK}: {len(rows)}")

gloss_cache = {}
def gloss_for(lemma):
    if lemma not in gloss_cache:
        gs = [r['gloss'] for r in cur.execute(
            "SELECT DISTINCT gloss FROM mti_terms WHERE strongs_number LIKE ?||'%' AND gloss IS NOT NULL", (lemma,))]
        gloss_cache[lemma] = '; '.join(dict.fromkeys(gs))
    return gloss_cache[lemma]

groups = defaultdict(list)
for r in rows:
    groups[(r['lemma'], norm_esv(r['esv']))].append(r)   # meaning key = lemma + ESV rendering (voice/stem merged; stem kept as evidence)

old_records = cur.execute(f"SELECT COUNT(*) n FROM ib_characteristic WHERE book_scope='{BOOK}'").fetchone()['n']
singles = sum(1 for g in groups.values() if len(g)==1)
print(f"Old records: {old_records}  ->  New meaning-keyed records: {len(groups)}  (singletons: {singles})")

by_lemma = Counter(k[0] for k in groups)
print("\nWords with the most distinct meanings (was 1 record each):")
for lemma,n in by_lemma.most_common(6):
    names = sorted({Counter(x['esv'] for x in g if x['esv']).most_common(1)[0][0]
                    for k,g in groups.items() if k[0]==lemma and any(x['esv'] for x in g)})
    print(f"  {lemma}: {n} meanings -> {', '.join(names)[:88]}")

if not LIVE:
    print("\n[dry run] no writes. Re-run with --live.")
    sys.exit(0)

os.makedirs('outputs/data', exist_ok=True)
exp = [dict(r) for r in cur.execute(f"SELECT * FROM ib_characteristic WHERE book_scope='{BOOK}'")]
expfile = f"verse-analysis/psalms/_model/ib_characteristic_v2_book{BOOK}_pre_v3rebuild_{STAMP}.json"
json.dump(exp, open(expfile,'w',encoding='utf-8'), indent=2, ensure_ascii=False, default=str)
print(f"\nExported {len(exp)} v2 records -> {expfile} (reversibility)")

cur.execute(f"DELETE FROM ib_characteristic WHERE book_scope='{BOOK}'")
built = linked = 0
for (lemma, nesv), spans in sorted(groups.items()):
    esv_ctr = Counter(s['esv'] for s in spans if s['esv'])
    name    = esv_ctr.most_common(1)[0][0] if esv_ctr else (lemma)   # readable label
    stems   = ', '.join(sorted({s['stem']  for s in spans if s['stem']})) or None
    morphs  = ', '.join(sorted({s['morph'] for s in spans if s['morph']})[:12]) or None
    esvs    = ', '.join(w for w,_ in esv_ctr.most_common(8)) or None
    ops     = Counter(s['op'] for s in spans if s['op'])
    variants= ' | '.join(v for v,_ in Counter(s['sense'] for s in spans if s['sense']).most_common(10)) or None
    rep = spans[0]
    slug = re.sub(r'[^a-z0-9]+','-', name.lower()).strip('-')[:24]
    code = f"psa-{lemma}-{slug}"
    ledger = (f"{name} [{lemma}] — {len(spans)} occurrence(s) in book {BOOK}. "
              f"stem(s): {stems or 'n/a'}. ESV: {esvs or 'n/a'}. attested gloss: {gloss_for(lemma) or 'n/a'}.")
    cur.execute("""INSERT INTO ib_characteristic
        (code,name,char_key,key_word,key_span_id,operation,ledger,instance_count,
         family,status,provenance,book_scope,stems,morph_codes,esv_words,
         lexical_gloss,read_sense_variants,created_at,updated_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (code, name, f"{lemma}:{nesv}", name, rep['span_id'],
         ops.most_common(1)[0][0] if ops else None, ledger, len(spans),
         None, 'surfaced', PROV, BOOK, stems, morphs, esvs,
         gloss_for(lemma), variants, STAMP, STAMP))
    nid = cur.lastrowid; built += 1
    cur.executemany("UPDATE verse_span_index SET ib_char_id=? WHERE id=?",
                    [(nid, s['span_id']) for s in spans])
    linked += len(spans)

c.commit()
print(f"\nBuilt {built} records; re-linked {linked} spans.")

null_link = cur.execute(f"SELECT COUNT(*) n FROM verse_span_index si JOIN verse v ON v.id=si.verse_id WHERE {CH} AND si.ib_char_id IS NULL").fetchone()['n']
dangling  = cur.execute(f"SELECT COUNT(*) n FROM verse_span_index si JOIN verse v ON v.id=si.verse_id WHERE {CH} AND si.ib_char_id NOT IN (SELECT id FROM ib_characteristic WHERE book_scope='{BOOK}')").fetchone()['n']
unref     = cur.execute(f"SELECT COUNT(*) n FROM ib_characteristic ic WHERE ic.book_scope='{BOOK}' AND NOT EXISTS(SELECT 1 FROM verse_span_index si WHERE si.ib_char_id=ic.id)").fetchone()['n']
print(f"VALIDATE  I7 chars with NULL ib_char_id: {null_link} (expect 0)")
print(f"VALIDATE  chars -> dangling record: {dangling} (expect 0)")
print(f"VALIDATE  records with no linked span: {unref} (expect 0)")
print("OK" if null_link==0 and dangling==0 and unref==0 else "*** VALIDATION FAILURE ***")
