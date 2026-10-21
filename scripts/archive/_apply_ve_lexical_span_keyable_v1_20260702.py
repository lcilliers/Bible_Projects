"""
_apply_ve_lexical_span_keyable_v1_20260702.py

Make ve_lexical SPAN-KEYABLE so the build can be index-driven (span is the unit). Fixes the
"second gate" storage blocker: verse_context_id was NOT NULL, forcing every lexical to hang off a
pre-tagged term — which is exactly why untagged content spans were skipped.

Rebuild (preserves all 507,857 rows + indexes):
  - verse_context_id  -> NULLABLE (tagged terms still set it; untagged content spans leave it NULL)
  - + verse_span_id INTEGER  -> verse_span_index.id (the span home for ANY span)
  - + gate TEXT             -> '1-primary' | '2-relevant' | NULL(legacy)
Schema 3.35.0 -> 3.36.0 (M62).

Safe: backs up; single transaction; row-count verified; dry-run default.
Usage: python scripts/_apply_ve_lexical_span_keyable_v1_20260702.py [--live]
"""
import sqlite3, os, sys, shutil, json
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
NEW="""CREATE TABLE ve_lexical (
  id INTEGER PRIMARY KEY,
  verse_context_id INTEGER REFERENCES verse_context(id),
  verse_span_id INTEGER REFERENCES verse_span_index(id),
  gate TEXT,
  ve_nr INTEGER, ve_label TEXT, related_tier TEXT, value TEXT, notes TEXT,
  source_provenance TEXT, delete_flagged INTEGER NOT NULL DEFAULT 0, created_at TEXT,
  from_span TEXT, to_span TEXT, direction TEXT, resolution TEXT, pair_kind TEXT)"""
COLS="id,verse_context_id,ve_nr,ve_label,related_tier,value,notes,source_provenance,delete_flagged,created_at,from_span,to_span,direction,resolution,pair_kind"

def main():
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    before=cur.execute("SELECT COUNT(*) FROM ve_lexical").fetchone()[0]
    print("ve_lexical rows:", before, "| adding: verse_span_id, gate; verse_context_id -> nullable")
    if not LIVE:
        print("DRY-RUN. Re-run with --live."); return
    shutil.copy2(DB,os.path.join('backups','bible_research.pre-velex-spankey.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    cur.execute("PRAGMA foreign_keys=OFF")
    cur.executescript(f"""
      BEGIN;
      ALTER TABLE ve_lexical RENAME TO ve_lexical_old;
      {NEW};
      INSERT INTO ve_lexical ({COLS}) SELECT {COLS} FROM ve_lexical_old;
      DROP TABLE ve_lexical_old;
      CREATE INDEX ix_ve_lexical_vc ON ve_lexical(verse_context_id);
      CREATE INDEX ix_ve_lexical_ve ON ve_lexical(ve_nr);
      CREATE INDEX ix_velex_vc ON ve_lexical(verse_context_id);
      CREATE INDEX ix_ve_lexical_span ON ve_lexical(verse_span_id);
      COMMIT;
    """)
    cur.execute("PRAGMA foreign_keys=ON")
    after=cur.execute("SELECT COUNT(*) FROM ve_lexical").fetchone()[0]
    cols=[r[1] for r in cur.execute("PRAGMA table_info(ve_lexical)").fetchall()]
    vc_nn=[r['notnull'] for r in cur.execute("PRAGMA table_info(ve_lexical)").fetchall() if r['name']=='verse_context_id'][0]
    # schema bump
    hist=json.loads(cur.execute("SELECT migration_history FROM schema_version ORDER BY id DESC LIMIT 1").fetchone()[0])
    hist.append({"version":"M62","description":"ve_lexical span-keyable: verse_context_id nullable + verse_span_id (->verse_span_index) + gate. Enables index-driven build (untagged content spans lexicalised). 3.35.0->3.36.0.","applied_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')})
    cur.execute("INSERT INTO schema_version (version_code,applied_at,migration_history) VALUES (?,?,?)",("3.36.0",datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),json.dumps(hist)))
    conn.commit()
    print("rows before/after: %d / %d  %s"%(before,after,"OK" if before==after else "!! MISMATCH"))
    print("verse_context_id notnull now:", vc_nn, "(0=nullable ✓)")
    print("cols:", cols)
    print("schema_version:", cur.execute("SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1").fetchone()[0])

if __name__=='__main__': main()
