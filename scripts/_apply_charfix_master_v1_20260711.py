#!/usr/bin/env python
"""Fix (a) the emergent-characteristic seed failure + (b) populate the char on the master.
Reusable per book via --book-id (default 19 = Psalms).

(a) Every span roled 'characteristic' MUST be a candidate. Spans that emerged in reading
    without a seed flag are stamped char_candidate=1 + tag 'READ-EMERGENT-2026', and their
    base lemmas are written to a seed-extension file so a future seed run catches them.
(b) verse_span_index.characteristic (new column) is populated with the read char (ve_lexical
    sense, ve_nr=101) for every read-2026 characteristic span.

Integrity-gated: run after a DB backup. Idempotent.
"""
import sqlite3, os, json, sys, datetime

DB='database/bible_research.db'
BOOK=19
for i,a in enumerate(sys.argv):
    if a=='--book-id': BOOK=int(sys.argv[i+1])
NOW=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()

# --- schema: add master char column if missing ---
cols=[r['name'] for r in cur.execute("PRAGMA table_info(verse_span_index)")]
if 'characteristic' not in cols:
    cur.execute("ALTER TABLE verse_span_index ADD COLUMN characteristic TEXT")
    print("added column verse_span_index.characteristic")
else:
    print("column verse_span_index.characteristic already present")

CH=f"role='characteristic' AND role_provenance='read-2026' AND verse_id IN (SELECT id FROM verse WHERE book_id={BOOK})"

# --- (a) the emergent 403: stamp candidate + tag, collect lemmas ---
emergent=cur.execute(f"""SELECT id, primary_strong, surface,
  (SELECT value FROM ve_lexical x WHERE x.verse_span_id=verse_span_index.id AND x.ve_nr=101 AND COALESCE(x.delete_flagged,0)=0 LIMIT 1) sense
  FROM verse_span_index WHERE {CH} AND char_candidate IS NULL AND char_candidate_tag IS NULL""").fetchall()
lemmas={}
for r in emergent:
    cur.execute("UPDATE verse_span_index SET char_candidate=1, char_candidate_tag='READ-EMERGENT-2026' WHERE id=?", (r['id'],))
    base=(r['primary_strong'] or '')[:5]
    if base: lemmas.setdefault(base, r['sense'] or r['surface'])
print(f"(a) stamped {len(emergent)} emergent characteristics as candidates; {len(lemmas)} distinct base lemmas")

# write the seed-extension file (formal dynamic-extension record)
os.makedirs('outputs/data', exist_ok=True)
extpath=f"verse-analysis/psalms/_model/char-seed-extension-read-emergent-{BOOK}-20260711.json"
json.dump({"generated_utc":NOW,"origin":"read-emergent","book_id":BOOK,
           "note":"lemmas that surfaced as characteristics during reading but were absent from the base seed; the seed process MUST consume this on every run",
           "lemmas":[{"strong":k,"seed_word":v} for k,v in sorted(lemmas.items())]},
          open(extpath,'w',encoding='utf-8'), indent=2, ensure_ascii=False)
print(f"    wrote seed extension: {extpath}")

# --- (b) populate the master char from the lexical sense(101) ---
n=cur.execute(f"""UPDATE verse_span_index SET characteristic=(
     SELECT value FROM ve_lexical x WHERE x.verse_span_id=verse_span_index.id AND x.ve_nr=101 AND COALESCE(x.delete_flagged,0)=0 LIMIT 1)
   WHERE {CH}""").rowcount
print(f"(b) populated verse_span_index.characteristic on {n} characteristic spans")

# --- verify ---
noflag=cur.execute(f"SELECT COUNT(*) FROM verse_span_index WHERE {CH} AND char_candidate IS NULL").fetchone()[0]
nochar=cur.execute(f"SELECT COUNT(*) FROM verse_span_index WHERE {CH} AND (characteristic IS NULL OR characteristic='')").fetchone()[0]
print(f"VERIFY: char-spans with no candidate flag = {noflag} (must be 0); with no char text = {nochar} (must be 0)")

if noflag==0 and nochar==0:
    c.commit(); print("COMMITTED")
else:
    c.rollback(); print("ROLLED BACK — verification failed")
