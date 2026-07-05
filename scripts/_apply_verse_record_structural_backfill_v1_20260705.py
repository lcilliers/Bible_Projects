#!/usr/bin/env python
"""_apply_verse_record_structural_backfill_v1_20260705.py — safe, determinate structural backfill.

Fills ONLY fields on EXISTING wa_verse_records that are NULL and have a single authoritative value on
their own verse_span_index span (matched by verse_id + term_id=primary_strong, UNIQUE match only):
  - morph_code  (where NULL and span has one)
  - stem        (where NULL, pos=verb, and span has one)
No new rows; no interpretation; source is the span index (linguistic source of truth). Reversible.
Read-only unless --live.
"""
import sqlite3, os, sys
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()

# candidates: NULL field on record, single matching span carrying the value
def candidates(field, verb_only=False):
    vf = "AND vsi.pos='verb'" if verb_only else ""
    return cur.execute(f"""
      SELECT w.id wid, vsi.{field} val
      FROM wa_verse_records w
      JOIN verse_span_index vsi ON vsi.verse_id=w.verse_id AND vsi.primary_strong=w.term_id
      WHERE COALESCE(w.delete_flagged,0)=0 AND (w.{field} IS NULL OR w.{field}='')
        AND vsi.{field} IS NOT NULL AND vsi.{field}<>'' {vf}
        AND (SELECT COUNT(*) FROM verse_span_index s2 WHERE s2.verse_id=w.verse_id AND s2.primary_strong=w.term_id)=1
    """).fetchall()

morph=candidates('morph_code')
stem=candidates('stem', verb_only=True)
print(f"morph_code backfill candidates (unique-span): {len(morph)}")
print(f"stem backfill candidates (verb, unique-span): {len(stem)}")
if not LIVE:
    print("\nDRY-RUN. Re-run with --live."); sys.exit(0)
for r in morph: cur.execute("UPDATE wa_verse_records SET morph_code=?, updated_at=updated_at WHERE id=?",(r['val'],r['wid']))
for r in stem:  cur.execute("UPDATE wa_verse_records SET stem=? WHERE id=?",(r['val'],r['wid']))
c.commit()
print(f"\nLIVE: {len(morph)} morph_code + {len(stem)} stem values backfilled.")
# verify
mn=cur.execute("SELECT COUNT(*) FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 AND (morph_code IS NULL OR morph_code='')").fetchone()[0]
print(f"remaining NULL morph_code (source also empty, not fillable): {mn}")
