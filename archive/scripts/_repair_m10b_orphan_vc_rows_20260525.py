"""Soft-delete 19 orphan verse_context rows in M10b whose parent
wa_verse_records were delete_flagged upstream.

Discovered post-Phase 2 (2026-05-25): the §5.6 hard gate query returned 19
rows with `analysis_note IS NULL` despite Phase 2 completing 514/514 verses.
Root cause: 19 verse_context rows (5 for H0205G a.ven; 14 for H7455 ro.a)
point at verse_records that have `delete_flagged=1`. The Pass A loader
correctly skipped them via the wa_verse_records JOIN, but they still count
against the hard-gate query (which doesn't join verse_records).

Fix: set delete_flagged=1 on these orphan vc rows, with set_aside_reason
naming the cause. No data loss — the underlying verse_records are already
deleted; these vc rows have been zombie since the upstream verse_record
cleanup.

Idempotent: re-running finds 0 rows because they're already delete_flagged.
"""
from __future__ import annotations
import shutil, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
REASON = (
    "Orphan vc row — parent wa_verse_record delete_flagged upstream "
    "(soft-deleted 2026-05-25 to clear §5.6 hard gate)."
)


def main(live: bool) -> int:
    print(f"=== M10b orphan vc soft-delete — mode={'LIVE' if live else 'DRY-RUN'} ===")

    if live:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        backup = REPO / "backups" / f"bible_research_backup_{ts}_M10b-orphan-vc-cleanup.db"
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DB, backup)
        print(f"Backup: {backup.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Identify orphans (re-run safe — only finds active vc rows pointing at deleted vrs)
    orphans = conn.execute("""
        SELECT vc.id AS vc_id, vc.verse_record_id, mt.strongs_number, vr.reference
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code = 'M10b'
          AND mt.delete_flagged = 0
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND vr.delete_flagged = 1
        ORDER BY mt.strongs_number, vc.verse_record_id
    """).fetchall()
    print(f"Orphan vc rows found: {len(orphans)}")
    for r in orphans:
        print(f"  vc_id={r['vc_id']:6d} {r['strongs_number']:8s} {r['reference']}")

    if not orphans:
        print("\nNothing to do.")
        conn.close()
        return 0

    if not live:
        print("\n[DRY-RUN — no writes]")
        conn.close()
        return 0

    conn.execute("BEGIN")
    try:
        n = 0
        for r in orphans:
            cur = conn.execute(
                "UPDATE verse_context SET delete_flagged=1, set_aside_reason=? "
                "WHERE id=? AND COALESCE(delete_flagged,0)=0",
                (REASON, r["vc_id"]),
            )
            n += cur.rowcount
        conn.commit()
        print(f"\nCOMMITTED — soft-deleted {n} orphan rows")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        # Post: verify gate clears
        gate = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.cluster_code = 'M10b'
              AND vc.is_relevant = 1
              AND COALESCE(vc.delete_flagged, 0) = 0
              AND vc.analysis_note IS NULL
        """).fetchone()[0]
        print(f"§5.6 hard gate post: {gate} (expect 0)")
        conn.close()

    return 0


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    sys.exit(main(args.live))
