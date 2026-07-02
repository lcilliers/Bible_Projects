"""
_apply_ve_lexical_phase1_archive_legacy_20260702.py  (M63, schema -> 3.37.0)

ve_lexical Phase 1 optimisation (architecture review v1, 2026-07-02):
  1. Archive all NON-live rows (source_provenance != 'lexical-model-2026', incl NULL) into ve_lexical_legacy.
     -> ve_lexical becomes the live model only (~1,990 rows). Legacy retained per catalogue §7 (not deleted).
  2. Drop the duplicate index ix_velex_vc (identical to ix_ve_lexical_vc on verse_context_id).
  3. Record schema_version 3.37.0 / M63.
  4. VACUUM to reclaim freed pages.

Safe: backup, dry-run default, count-verified. Usage: python scripts/_apply_ve_lexical_phase1_archive_legacy_20260702.py [--live]
"""
import sqlite3, os, sys, shutil, json
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
LEGACY_WHERE="(source_provenance IS NULL OR source_provenance<>'lexical-model-2026')"

def main():
    size0=os.path.getsize(DB)
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    tot=cur.execute("SELECT COUNT(*) n FROM ve_lexical").fetchone()['n']
    keep=cur.execute("SELECT COUNT(*) n FROM ve_lexical WHERE source_provenance='lexical-model-2026'").fetchone()['n']
    move=cur.execute("SELECT COUNT(*) n FROM ve_lexical WHERE "+LEGACY_WHERE).fetchone()['n']
    print("=== PLAN (M63 / schema 3.37.0) ===")
    print(" ve_lexical total    :", tot)
    print(" keep (live model)   :", keep)
    print(" move (legacy)       :", move, "(sum check:", keep+move==tot, ")")
    print(" drop index          : ix_velex_vc")
    print(" DB size MB          : %.1f"%(size0/1e6))
    if not LIVE:
        print("\nDRY-RUN. Re-run with --live."); return
    shutil.copy2(DB,os.path.join('backups','bible_research.pre-velex-phase1.%s.db'%datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    # 1. archive -- mirror schema exactly, then move rows
    ddl=cur.execute("SELECT sql FROM sqlite_master WHERE name='ve_lexical'").fetchone()['sql']
    cur.execute(ddl.replace('CREATE TABLE ve_lexical','CREATE TABLE ve_lexical_legacy',1))
    cur.execute("INSERT INTO ve_lexical_legacy SELECT * FROM ve_lexical WHERE "+LEGACY_WHERE)
    moved=cur.execute("SELECT COUNT(*) n FROM ve_lexical_legacy").fetchone()['n']
    assert moved==move, "archive count mismatch %d != %d"%(moved,move)
    cur.execute("DELETE FROM ve_lexical WHERE "+LEGACY_WHERE)
    remain=cur.execute("SELECT COUNT(*) n FROM ve_lexical").fetchone()['n']
    assert remain==keep, "remaining count mismatch %d != %d"%(remain,keep)
    # 2. drop duplicate index
    cur.execute("DROP INDEX IF EXISTS ix_velex_vc")
    # 3. schema_version bump
    prev=cur.execute("SELECT migration_history,engine_min_version FROM schema_version ORDER BY id DESC LIMIT 1").fetchone()
    hist=json.loads(prev['migration_history']) if prev['migration_history'] else []
    hist.append({"version":"M63","description":"ve_lexical Phase 1: archive %d legacy rows -> ve_lexical_legacy (live table = live model only); drop duplicate index ix_velex_vc; schema -> 3.37.0"%move,"applied_at":NOW})
    cur.execute("INSERT INTO schema_version (version_code,applied_at,migration_history,engine_min_version) VALUES (?,?,?,?)",
                ('3.37.0',NOW,json.dumps(hist),prev['engine_min_version']))
    conn.commit()
    # verify indexes remaining
    idx=[r['name'] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='ve_lexical'").fetchall()]
    print("after move: ve_lexical=%d  ve_lexical_legacy=%d  indexes=%s"%(remain,moved,idx))
    # 4. VACUUM (outside txn)
    conn.isolation_level=None
    conn.execute("VACUUM")
    conn.close()
    size1=os.path.getsize(DB)
    print("VACUUM done. DB size %.1f MB -> %.1f MB (reclaimed %.1f MB)."%(size0/1e6,size1/1e6,(size0-size1)/1e6))
    print("schema_version -> 3.37.0 (M63).")

if __name__=='__main__': main()
