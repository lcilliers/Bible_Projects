#!/usr/bin/env python
"""(c) Build ib_characteristic into the normalised characteristic index, from the sources
(master verse_span_index + lexical ve_lexical). Reusable per book (--book-id, default 19).

Grain = base lemma (primary_strong[:5]) — the mechanical, uniform normalisation ("a specific
char word"). One ib_characteristic record per distinct characteristic-word; every char-span
links to it via verse_span_index.ib_char_id. family stays NULL (the later analytical grouping).

- The 29 legacy rows (old-read families) are EXPORTED to JSON + copied to ib_characteristic_legacy
  before being cleared (recoverable, not destroyed).
- Idempotent for a book: clears that book's contribution and rebuilds.
Run after a DB backup.
"""
import sqlite3, os, json, sys, datetime
DB='database/bible_research.db'; BOOK=19
for i,a in enumerate(sys.argv):
    if a=='--book-id': BOOK=int(sys.argv[i+1])
NOW=datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')
c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()

def hascol(t,col): return col in [r['name'] for r in cur.execute(f"PRAGMA table_info({t})")]

# --- add missing columns ---
for col,typ in [('char_key','TEXT'),('key_word','TEXT'),('key_span_id','INTEGER'),
                ('operation','TEXT'),('ledger','TEXT'),('instance_count','INTEGER'),('book_scope','TEXT')]:
    if not hascol('ib_characteristic',col):
        cur.execute(f"ALTER TABLE ib_characteristic ADD COLUMN {col} {typ}"); print("ib_characteristic +",col)
if not hascol('verse_span_index','ib_char_id'):
    cur.execute("ALTER TABLE verse_span_index ADD COLUMN ib_char_id INTEGER"); print("verse_span_index +ib_char_id")

# --- preserve then clear the legacy 29 (once) ---
legacy=cur.execute("SELECT * FROM ib_characteristic WHERE char_key IS NULL").fetchall()
if legacy:
    os.makedirs('outputs/data',exist_ok=True)
    json.dump([dict(r) for r in legacy], open('outputs/data/ib_characteristic_legacy_29_export_20260711.json','w',encoding='utf-8'), indent=2, ensure_ascii=False)
    cur.execute("""CREATE TABLE IF NOT EXISTS ib_characteristic_legacy AS SELECT * FROM ib_characteristic WHERE 0""")
    cur.execute("""INSERT INTO ib_characteristic_legacy SELECT * FROM ib_characteristic WHERE char_key IS NULL""")
    cur.execute("DELETE FROM ib_characteristic WHERE char_key IS NULL")
    print(f"legacy {len(legacy)} rows exported (JSON + ib_characteristic_legacy) and cleared")

# --- rebuild this book's records + links ---
CH=f"si.role='characteristic' AND si.role_provenance='read-2026' AND v.book_id={BOOK}"
cur.execute(f"DELETE FROM ib_characteristic WHERE book_scope='{BOOK}'")
cur.execute(f"UPDATE verse_span_index SET ib_char_id=NULL WHERE id IN (SELECT si.id FROM verse_span_index si JOIN verse v ON v.id=si.verse_id WHERE {CH})")

rows=cur.execute(f"""SELECT si.id, substr(si.primary_strong,1,5) lemma, si.characteristic sense,
   (SELECT value FROM ve_lexical x WHERE x.verse_span_id=si.id AND x.ve_nr=106 AND COALESCE(x.delete_flagged,0)=0 LIMIT 1) op,
   (SELECT value FROM ve_lexical x WHERE x.verse_span_id=si.id AND x.ve_nr=102 AND COALESCE(x.delete_flagged,0)=0 LIMIT 1) typ
   FROM verse_span_index si JOIN verse v ON v.id=si.verse_id WHERE {CH}""").fetchall()
from collections import defaultdict
groups=defaultdict(list)
for r in rows: groups[r['lemma']].append(r)

built=0; linked=0
for lemma, spans in sorted(groups.items()):
    senses=sorted({s['sense'] for s in spans if s['sense']})
    ops=[s['op'] for s in spans if s['op']]
    typs=sorted({s['typ'] for s in spans if s['typ']})
    key_word = max(senses, key=lambda s:sum(1 for x in spans if x['sense']==s)) if senses else lemma
    rep=spans[0]
    ledger=(f"{key_word} [{lemma}] — {len(spans)} occurrence(s) in book {BOOK}. "
            f"Type(s): {', '.join(typs)}. Senses read: {'; '.join(senses[:12])}"
            + (f" (+{len(senses)-12} more)" if len(senses)>12 else "") + ". "
            f"Representative operation: {ops[0] if ops else '(none)'}")
    cur.execute("""INSERT INTO ib_characteristic
        (code,name,char_key,key_word,key_span_id,operation,ledger,instance_count,family,status,provenance,book_scope,created_at,updated_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (f"psa-{lemma}", key_word, lemma, key_word, rep['id'], ops[0] if ops else None, ledger, len(spans),
         None, 'surfaced', 'ib-char-index-v2-reread-2026', str(BOOK), NOW, NOW))
    cid=cur.lastrowid
    for s in spans:
        cur.execute("UPDATE verse_span_index SET ib_char_id=? WHERE id=?", (cid, s['id'])); linked+=1
    built+=1

# --- verify ---
unl=cur.execute(f"SELECT COUNT(*) FROM verse_span_index si JOIN verse v ON v.id=si.verse_id WHERE {CH} AND si.ib_char_id IS NULL").fetchone()[0]
recs=cur.execute(f"SELECT COUNT(*) FROM ib_characteristic WHERE book_scope='{BOOK}'").fetchone()[0]
unref=cur.execute(f"SELECT COUNT(*) FROM ib_characteristic ic WHERE ic.book_scope='{BOOK}' AND NOT EXISTS(SELECT 1 FROM verse_span_index si WHERE si.ib_char_id=ic.id)").fetchone()[0]
print(f"built {built} records, linked {linked} spans")
print(f"VERIFY: char-spans not linked = {unl} (must be 0); records = {recs}; records referenced by no span = {unref} (must be 0)")
if unl==0 and unref==0 and recs==built:
    c.commit(); print("COMMITTED")
else:
    c.rollback(); print("ROLLED BACK — verification failed")
