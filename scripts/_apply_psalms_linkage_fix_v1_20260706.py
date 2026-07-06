#!/usr/bin/env python
"""_apply_psalms_linkage_fix_v1_20260706.py — Step 1 (linkages) for PSALMS only.

Makes lexical<->verse-record a DIRECT keyed link through the master index (verse_span_index),
so tracking is by index not by (reference,term_id) scanning:
  - ADD COLUMN wa_verse_records.verse_span_id  (global infra, nullable)
  - POPULATE it for PSALMS rows: match (verse_id, base-strong) to the unique span
  - INDEX wa_verse_records.verse_span_id  and  verse(book_id, chapter)  [chapter = reading unit]
Reading unit = chapter (already on every verse); lexical unit = verse (span->verse). No passage-table change.
Read-only unless --live. Idempotent (skips if column/index exist; re-matches unset Psalms rows).
"""
import sqlite3, os, sys, re
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()
def base(s): m=re.match(r'(H\d+)', s or ''); return m.group(1) if m else (s or '')

cols=[r['name'] for r in cur.execute('PRAGMA table_info(wa_verse_records)')]
has_col='verse_span_id' in cols
pb=cur.execute("SELECT id FROM books WHERE name='Psalms'").fetchone()['id']

# build match plan for Psalms rows (dry countable)
rows=cur.execute("SELECT id, verse_id, term_id FROM wa_verse_records WHERE book_id=? AND COALESCE(delete_flagged,0)=0 AND term_id LIKE 'H%'",(pb,)).fetchall()
# spans per (verse_id, base-strong)
from collections import defaultdict
span_by=defaultdict(list)
for s in cur.execute("""SELECT vsi.id, vsi.verse_id, vsi.primary_strong FROM verse_span_index vsi JOIN verse v ON v.id=vsi.verse_id WHERE v.book_id=?""",(pb,)):
    span_by[(s['verse_id'], base(s['primary_strong']))].append(s['id'])
matched=ambig=none=0; plan=[]; nospan_refs=[]
for r in rows:
    cand=span_by.get((r['verse_id'], base(r['term_id'])), [])
    if len(cand)==1: matched+=1; plan.append((r['id'], cand[0]))
    elif len(cand)>1: ambig+=1  # repeated word -> resolved via composite index, verse_span_id left NULL
    else:
        none+=1
        if len(nospan_refs)<12:
            vr=cur.execute("SELECT reference FROM wa_verse_records WHERE id=?",(r['id'],)).fetchone()
            nospan_refs.append(f"{vr['reference']}/{r['term_id']}")
print(f"Psalms verse-records: {len(rows)} | unique-span match: {matched} | ambiguous(>1 span): {ambig} | no-span: {none}")
if nospan_refs: print("  no-span sample (verse-record strong not in that verse's spans - integrity flag):", nospan_refs)

if not LIVE:
    print(f"has verse_span_id column: {has_col}"); print("\nDRY-RUN. Re-run with --live."); sys.exit(0)

if not has_col:
    cur.execute("ALTER TABLE wa_verse_records ADD COLUMN verse_span_id INTEGER")
    print("  added column wa_verse_records.verse_span_id")
for wid, sid in plan:
    cur.execute("UPDATE wa_verse_records SET verse_span_id=? WHERE id=?", (sid, wid))
# indexes: direct single-hop FK (unambiguous) + composite natural-key (all cases, incl. repeated words) + chapter access
cur.execute("CREATE INDEX IF NOT EXISTS ix_wavr_span ON wa_verse_records(verse_span_id)")
cur.execute("CREATE INDEX IF NOT EXISTS ix_vsi_verse_strong ON verse_span_index(verse_id, primary_strong)")
cur.execute("CREATE INDEX IF NOT EXISTS ix_wavr_verse_term ON wa_verse_records(verse_id, term_id)")
cur.execute("CREATE INDEX IF NOT EXISTS ix_verse_book_chapter ON verse(book_id, chapter)")
c.commit()
print(f"  LIVE: populated {len(plan)} Psalms verse-records with verse_span_id; indexes ensured.")
# quick verify
pop=cur.execute("SELECT COUNT(*) FROM wa_verse_records WHERE book_id=? AND verse_span_id IS NOT NULL",(pb,)).fetchone()[0]
print(f"  Psalms verse-records now linked to a span: {pop}")
