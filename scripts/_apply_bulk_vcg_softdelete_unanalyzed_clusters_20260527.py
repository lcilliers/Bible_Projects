"""Bulk soft-delete of VCGs in clusters not yet through current-pipeline analysis.

Per researcher direction 2026-05-27: pre-2026-05-04 legacy VCGs add no analytical
value and are consistently soft-deleted by v2_9 Phase 8 silent dissolution when a
cluster begins active analysis. This script pre-clears the same debris in all
clusters that are NOT in 'Analysis Completed' / 'Analysis Completed (Terms Added)'
status.

Operations (single transaction):
- Op A: UPDATE verse_context_group SET delete_flagged=1, notes='...'
        WHERE id IN (<vcg ids in eligible clusters>)
- Op B: UPDATE vcg_term SET delete_flagged=1
        WHERE vcg_id IN (<same set>)

verse_context.group_id is NOT touched (per v2_9 §11 convention — the pointer
remains pointing at soft-deleted VCG rows; analytical queries already filter
on vcg.delete_flagged=0).

Eligibility rule: cluster.status NOT IN ('Analysis Completed',
'Analysis Completed (Terms Added)').

Closed clusters with legacy VCGs (M05, M06, M15, M20, M26, M39, M46) are NOT
touched — they were closed under their methodology and their analytical
record is preserved as-is.
"""
from __future__ import annotations
import argparse, io, shutil, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
COMPLETED_STATUSES = {"Analysis Completed", "Analysis Completed (Terms Added)"}
NOTE = f"Bulk soft-delete {NOW}: cluster not yet through current-pipeline analysis; legacy VCG cleared per researcher direction 2026-05-27."


def main(live: bool) -> int:
    print(f"=== Bulk VCG soft-delete (unanalyzed clusters) — mode={'LIVE' if live else 'DRY-RUN'} ===")

    if live:
        # Backup skipped — 5 prior backups exist from earlier failed attempts on
        # 2026-05-27 (Drive-sync lock contention). Reuse those.
        latest_backup = sorted((REPO / "backups").glob("bible_research_backup_*_bulk-vcg-softdelete.db"))
        if latest_backup:
            print(f"Backup (pre-existing): {latest_backup[-1].relative_to(REPO)}")
        else:
            ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            backup = REPO / "backups" / f"bible_research_backup_{ts}_bulk-vcg-softdelete.db"
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(DB, backup)
            print(f"Backup (fresh): {backup.relative_to(REPO)}")

    conn = sqlite3.connect(DB, timeout=120.0)
    conn.row_factory = sqlite3.Row
    # busy_timeout in milliseconds; applies to lock waits at COMMIT too
    conn.execute("PRAGMA busy_timeout = 120000")

    # Eligible clusters = status NOT in completed set
    eligible = [r["cluster_code"] for r in conn.execute(
        "SELECT cluster_code, status FROM cluster ORDER BY cluster_code"
    ).fetchall() if r["status"] not in COMPLETED_STATUSES]
    print(f"Eligible clusters ({len(eligible)}): {eligible}")

    # Collect VCG ids linked to eligible clusters via at least one active is_relevant verse
    qmarks = ",".join("?" * len(eligible))
    target_vcg_ids = [r["group_id"] for r in conn.execute(f"""
        SELECT DISTINCT vc.group_id
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN verse_context_group vcg ON vcg.id = vc.group_id
        WHERE mt.cluster_code IN ({qmarks})
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND COALESCE(mt.delete_flagged, 0) = 0
          AND COALESCE(vcg.delete_flagged, 0) = 0
    """, eligible).fetchall()]
    print(f"VCGs to soft-delete (active, in eligible clusters): {len(target_vcg_ids)}")

    # Pre-counts (active rows)
    n_vcg_before = conn.execute(
        "SELECT COUNT(*) FROM verse_context_group WHERE COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    n_vcgterm_before = conn.execute(
        "SELECT COUNT(*) FROM vcg_term WHERE COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"Pre: active verse_context_group rows = {n_vcg_before:,}")
    print(f"Pre: active vcg_term rows           = {n_vcgterm_before:,}")

    if not live:
        # Sample what would be touched
        print("\n[DRY-RUN — sample VCGs that would be soft-deleted, 10 random]")
        sample_ids = target_vcg_ids[:10]
        if sample_ids:
            qm2 = ",".join("?" * len(sample_ids))
            for r in conn.execute(f"""
                SELECT vcg.id, vcg.group_code, vcg.context_description
                FROM verse_context_group vcg WHERE vcg.id IN ({qm2})
            """, sample_ids):
                desc = (r["context_description"] or "")[:80]
                print(f"  vcg.id={r['id']:5d} group_code={r['group_code']!r:25s} {desc!r}")
        print(f"\nWould soft-delete {len(target_vcg_ids)} verse_context_group rows + their vcg_term links")
        conn.close()
        return 0

    # LIVE: bulk update under single transaction
    # Use BEGIN IMMEDIATE to acquire RESERVED lock upfront — avoids the
    # commit-time deadlock with Google Drive sync readers.
    cur = conn.cursor()
    cur.execute("BEGIN IMMEDIATE")
    try:
        # SQLite has a default sqlite_max_variable_number (often 999). Chunk the IN list.
        chunk = 500
        n_vcg_updated = 0
        n_vcgterm_updated = 0
        for i in range(0, len(target_vcg_ids), chunk):
            batch = target_vcg_ids[i:i+chunk]
            qm = ",".join("?" * len(batch))

            # Op A: soft-delete verse_context_group rows
            cur.execute(f"""
                UPDATE verse_context_group
                SET delete_flagged = 1, notes = ?
                WHERE id IN ({qm}) AND COALESCE(delete_flagged, 0) = 0
            """, [NOTE, *batch])
            n_vcg_updated += cur.rowcount

            # Op B: soft-delete vcg_term links
            cur.execute(f"""
                UPDATE vcg_term
                SET delete_flagged = 1, last_updated_date = ?
                WHERE vcg_id IN ({qm}) AND COALESCE(delete_flagged, 0) = 0
            """, [NOW, *batch])
            n_vcgterm_updated += cur.rowcount

        print(f"\nOp A: soft-deleted {n_vcg_updated} verse_context_group rows")
        print(f"Op B: soft-deleted {n_vcgterm_updated} vcg_term rows")

        # Post-checks
        n_vcg_after = conn.execute(
            "SELECT COUNT(*) FROM verse_context_group WHERE COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        n_vcgterm_after = conn.execute(
            "SELECT COUNT(*) FROM vcg_term WHERE COALESCE(delete_flagged,0)=0"
        ).fetchone()[0]
        assert n_vcg_before - n_vcg_after == n_vcg_updated, \
            f"Verify failed: VCG before={n_vcg_before}, after={n_vcg_after}, updated={n_vcg_updated}"
        print(f"\nPost: active verse_context_group rows = {n_vcg_after:,}  (delta: -{n_vcg_updated:,})")
        print(f"Post: active vcg_term rows           = {n_vcgterm_after:,}  (delta: -{n_vcgterm_updated:,})")

        # No verse_context.group_id should still reference an active VCG in an eligible cluster
        n_dangling_eligible = conn.execute(f"""
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            JOIN verse_context_group vcg ON vcg.id = vc.group_id
            WHERE mt.cluster_code IN ({qmarks})
              AND vc.is_relevant = 1
              AND COALESCE(vc.delete_flagged, 0) = 0
              AND COALESCE(vcg.delete_flagged, 0) = 0
        """, eligible).fetchone()[0]
        assert n_dangling_eligible == 0, f"Expected 0, got {n_dangling_eligible} active VCG refs from eligible clusters"
        print(f"Post-check: 0 active VCG references from is_relevant verses in eligible clusters ✓")

        # Confirm no closed-cluster VCGs touched
        completed_qmarks = ",".join("?" * len(COMPLETED_STATUSES))
        closed_clusters = [r[0] for r in conn.execute(
            f"SELECT cluster_code FROM cluster WHERE status IN ({completed_qmarks})",
            list(COMPLETED_STATUSES)
        ).fetchall()]
        n_closed_vcgs_active = conn.execute(f"""
            SELECT COUNT(DISTINCT vcg.id)
            FROM verse_context_group vcg
            JOIN verse_context vc ON vc.group_id = vcg.id
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.cluster_code IN ({",".join("?" * len(closed_clusters))})
              AND COALESCE(vcg.delete_flagged, 0) = 0
              AND COALESCE(vc.delete_flagged, 0) = 0
              AND vc.is_relevant = 1
        """, closed_clusters).fetchone()[0]
        print(f"Post-check: closed-cluster VCGs still active = {n_closed_vcgs_active} (untouched as expected)")

        conn.commit()
        print(f"\nCOMMITTED at {NOW}")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    sys.exit(main(args.live))
