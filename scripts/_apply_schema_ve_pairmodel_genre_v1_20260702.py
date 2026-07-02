"""
_apply_schema_ve_pairmodel_genre_v1_20260702.py

Bring the DB schema up to date for the new lexical model (2026-07-01/02 decisions). ADDITIVE only.

Adds (all nullable — safe, no data loss):
  ve_lexical:  from_span, to_span, direction, resolution, pair_kind   (the pair/event model, Option B)
  verse:       genre                                                  (per-verse genre; feeds passage treatment)

Formalises what was already applied ad-hoc (passage table; verse.passage_id/is_passage_anchor/
process_marker) by recording ONE schema_version bump 3.34.0 -> 3.35.0 covering the whole
verse-first / passage / pair-model change.

NOT done here (deferred / documented, not destructive):
  - related_tier is DEPRECATED (superseded tier scheme; 372,884 values retained for provenance).
  - item convergence (cause+cause_clause+from-source -> source; how+operation) and ib_observation
    retirement are DATA migrations pending the finalised derivation — not schema, not yet.

Safe: backs up; dry-run default; verifies. Engine constant must be set to 3.35.0 alongside (done separately).
Usage: python scripts/_apply_schema_ve_pairmodel_genre_v1_20260702.py [--live]
"""
import sqlite3, os, sys, shutil, json
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
NEWVER='3.35.0'
def genre(b):
    if 1<=b<=5: return 'law/narrative'
    if 6<=b<=17: return 'narrative'
    if b in (18,19,20,21,22): return 'poetic/wisdom'
    if 23<=b<=39: return 'prophetic'
    if 40<=b<=43: return 'gospel-narrative'
    if b==44: return 'narrative'   # Acts
    return 'epistle'

def main():
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    ve=[r[1] for r in cur.execute("PRAGMA table_info(ve_lexical)").fetchall()]
    vv=[r[1] for r in cur.execute("PRAGMA table_info(verse)").fetchall()]
    add_ve=[c for c in ['from_span','to_span','direction','resolution','pair_kind'] if c not in ve]
    add_v=[c for c in ['genre'] if c not in vv]
    print('ve_lexical add:', add_ve or 'none'); print('verse add:', add_v or 'none')
    cur_ver=cur.execute("SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1").fetchone()[0]
    print('current schema_version:', cur_ver, '-> target', NEWVER)
    if not LIVE:
        print('\nDRY-RUN. Re-run with --live.'); return
    shutil.copy2(DB, os.path.join('backups','bible_research.pre-schema335.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    for c in add_ve: cur.execute("ALTER TABLE ve_lexical ADD COLUMN %s TEXT"%c)
    for c in add_v: cur.execute("ALTER TABLE verse ADD COLUMN %s TEXT"%c)
    # populate verse.genre from book_id
    n=0
    for r in cur.execute("SELECT id,book_id FROM verse").fetchall():
        cur.execute("UPDATE verse SET genre=? WHERE id=?",(genre(r['book_id']),r['id'])); n+=1
    # schema_version bump
    hist=cur.execute("SELECT migration_history FROM schema_version ORDER BY id DESC LIMIT 1").fetchone()[0]
    try: h=json.loads(hist)
    except Exception: h=[]
    h.append({"version":"M61","description":"Verse-first lexical model: passage table + verse.passage_id/is_passage_anchor/process_marker/genre (consecutive-run passages); ve_lexical pair/event columns (from_span,to_span,direction,resolution,pair_kind); related_tier deprecated. Schema 3.34.0 -> 3.35.0.","applied_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')})
    cur.execute("INSERT INTO schema_version (version_code,applied_at,migration_history) VALUES (?,?,?)",
                (NEWVER, datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), json.dumps(h)))
    conn.commit()
    print('genre populated on %d verses'%n)
    print('ve_lexical cols now:', [r[1] for r in cur.execute("PRAGMA table_info(ve_lexical)").fetchall()])
    print('verse.genre distinct:', [dict(r) for r in cur.execute("SELECT genre,COUNT(*) n FROM verse GROUP BY genre ORDER BY n DESC").fetchall()])
    print('schema_version now:', cur.execute("SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1").fetchone()[0])

if __name__=='__main__': main()
