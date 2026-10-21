"""_apply_wipe_ve_lexical_v1.py (2026-06-15) — PERMANENTLY remove all rows from ve_lexical.

Researcher decision: the entire ve_lexical value layer is too corrupt / non-compliant with 01b to
repair; remove it and rebuild from primary inputs. This is a HARD delete (DELETE FROM ve_lexical) —
no soft-delete flag, no in-table archive/shadow copy. The table STRUCTURE + indexes are retained.

Safety net = a file-level DB snapshot taken immediately before the delete (outside the database).
The M59 source findings remain soft-deleted in `finding` as the separate historical baseline.

  python scripts/_apply_wipe_ve_lexical_v1.py --dry-run
  python scripts/_apply_wipe_ve_lexical_v1.py --live
"""
import argparse, os, shutil, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
SNAP = os.path.join("backups", "bible_research_pre-ve_lexical-wipe_20260615.db")


def counts(cur):
    total = cur.execute("SELECT COUNT(*) FROM ve_lexical").fetchone()[0]
    active = cur.execute("SELECT COUNT(*) FROM ve_lexical WHERE COALESCE(delete_flagged,0)=0").fetchone()[0]
    return total, active


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()

    conn = sqlite3.connect(DB, timeout=600); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    total, active = counts(cur)
    idx = [r["name"] for r in cur.execute("PRAGMA index_list(ve_lexical)")]
    cols = [r["name"] for r in cur.execute("PRAGMA table_info(ve_lexical)")]
    findings_sd = cur.execute("SELECT COUNT(*) FROM finding WHERE delete_flagged=1 AND level='VERSE' "
                              "AND provenance IN ('l2_api','l2_mechanical')").fetchone()[0]
    print(f"ve_lexical before : {total:,} rows total ({active:,} active)")
    print(f"  columns         : {len(cols)} ({', '.join(cols)})")
    print(f"  indexes         : {idx}")
    print(f"  finding baseline (soft-deleted VERSE l2_*): {findings_sd:,} (must stay unchanged)")

    if a.dry_run:
        print(f"\nDRY-RUN — would snapshot DB -> {SNAP} then DELETE all {total:,} ve_lexical rows. No writes.")
        return

    # 1. pre-delete file snapshot (close the connection's WAL first via checkpoint)
    cur.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    os.makedirs("backups", exist_ok=True)
    shutil.copy2(DB, SNAP)
    print(f"\nsnapshot written : {SNAP} ({os.path.getsize(SNAP):,} bytes)")

    # 2. hard delete
    cur.execute("DELETE FROM ve_lexical")
    deleted = cur.rowcount
    conn.commit()

    # 3. verify
    after_total, _ = counts(cur)
    findings_after = cur.execute("SELECT COUNT(*) FROM finding WHERE delete_flagged=1 AND level='VERSE' "
                                 "AND provenance IN ('l2_api','l2_mechanical')").fetchone()[0]
    idx_after = [r["name"] for r in cur.execute("PRAGMA index_list(ve_lexical)")]
    print(f"LIVE: deleted {deleted:,} rows")
    print(f"  ve_lexical now  : {after_total:,} rows (expect 0)")
    print(f"  indexes intact  : {idx_after == idx}  {idx_after}")
    print(f"  finding baseline: {findings_after:,} (expect {findings_sd:,} — unchanged: {findings_after == findings_sd})")
    print(f"  snapshot exists : {os.path.exists(SNAP)}")


if __name__ == "__main__":
    main()
