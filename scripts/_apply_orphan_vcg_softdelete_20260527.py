"""Soft-delete orphan VCGs — active verse_context_group rows that have no
active is_relevant verses linked to them.

Per researcher direction 2026-05-27: "remove the VCGs that have no verses."

Orphan definition (Def 1):
  verse_context_group.delete_flagged = 0
  AND vcg.id NOT IN (DISTINCT vc.group_id from active is_relevant verse_context
                      via active mti_terms)

Such VCGs cannot be cited by the verse→VCG derivation (no verses to derive
from) and contribute no analytical value. Their descriptions are preserved
under delete_flagged=1 for historical inspection.

Operations (single transaction):
- Op A: UPDATE verse_context_group SET delete_flagged=1, notes=...
- Op B: UPDATE vcg_term SET delete_flagged=1 for any vcg_term rows pointing
        at the soft-deleted VCGs
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
NOTE = f"Orphan soft-delete {NOW}: no active is_relevant verse linked via active mti_term. Per researcher direction 2026-05-27."


def main(live: bool) -> int:
    print(f"=== Orphan VCG soft-delete — mode={'LIVE' if live else 'DRY-RUN'} ===")

    if live:
        # Reuse one of the existing backups; the DB hasn't changed since
        latest_backup = sorted((REPO / "backups").glob("bible_research_backup_*.db"))
        if latest_backup:
            print(f"Backup (pre-existing): {latest_backup[-1].relative_to(REPO)}")
        else:
            ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            backup = REPO / "backups" / f"bible_research_backup_{ts}_orphan-vcg-softdelete.db"
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(DB, backup)
            print(f"Backup (fresh): {backup.relative_to(REPO)}")

    conn = sqlite3.connect(DB, timeout=120.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout = 120000")

    orphans = [r[0] for r in conn.execute("""
        SELECT vcg.id FROM verse_context_group vcg
        WHERE COALESCE(vcg.delete_flagged,0)=0
          AND vcg.id NOT IN (
            SELECT DISTINCT vc.group_id FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE vc.group_id IS NOT NULL AND vc.is_relevant=1
              AND COALESCE(vc.delete_flagged,0)=0 AND COALESCE(mt.delete_flagged,0)=0
          )
    """).fetchall()]
    print(f"Orphan VCGs to soft-delete: {len(orphans)}")

    n_vcg_before = conn.execute("SELECT COUNT(*) FROM verse_context_group WHERE COALESCE(delete_flagged,0)=0").fetchone()[0]
    n_vcgterm_before = conn.execute("SELECT COUNT(*) FROM vcg_term WHERE COALESCE(delete_flagged,0)=0").fetchone()[0]
    print(f"Pre: active VCGs = {n_vcg_before:,}, active vcg_term = {n_vcgterm_before:,}")

    if not live:
        print("[DRY-RUN — no writes]")
        # Sample 10
        if orphans:
            qm = ",".join("?" * min(10, len(orphans)))
            print("\nSample orphans:")
            for r in conn.execute(f"SELECT id, group_code, context_description FROM verse_context_group WHERE id IN ({qm})", orphans[:10]):
                desc = (r["context_description"] or "")[:60]
                print(f"  vcg.id={r['id']:5d} code={r['group_code']!r:20s} {desc!r}")
        conn.close()
        return 0

    cur = conn.cursor()
    cur.execute("BEGIN IMMEDIATE")
    try:
        chunk = 500
        n_vcg_upd = 0
        n_vcgterm_upd = 0
        for i in range(0, len(orphans), chunk):
            batch = orphans[i:i+chunk]
            qm = ",".join("?" * len(batch))
            cur.execute(
                f"UPDATE verse_context_group SET delete_flagged=1, notes=? "
                f"WHERE id IN ({qm}) AND COALESCE(delete_flagged,0)=0",
                [NOTE, *batch],
            )
            n_vcg_upd += cur.rowcount
            cur.execute(
                f"UPDATE vcg_term SET delete_flagged=1, last_updated_date=? "
                f"WHERE vcg_id IN ({qm}) AND COALESCE(delete_flagged,0)=0",
                [NOW, *batch],
            )
            n_vcgterm_upd += cur.rowcount
        print(f"\nOp A: soft-deleted {n_vcg_upd} verse_context_group rows")
        print(f"Op B: soft-deleted {n_vcgterm_upd} vcg_term rows")

        n_vcg_after = conn.execute("SELECT COUNT(*) FROM verse_context_group WHERE COALESCE(delete_flagged,0)=0").fetchone()[0]
        n_vcgterm_after = conn.execute("SELECT COUNT(*) FROM vcg_term WHERE COALESCE(delete_flagged,0)=0").fetchone()[0]
        assert n_vcg_before - n_vcg_after == n_vcg_upd
        print(f"\nPost: active VCGs = {n_vcg_after:,} (delta: -{n_vcg_upd:,})")
        print(f"Post: active vcg_term = {n_vcgterm_after:,} (delta: -{n_vcgterm_upd:,})")

        # Confirm no remaining orphans
        n_remaining_orphans = conn.execute("""
            SELECT COUNT(*) FROM verse_context_group vcg
            WHERE COALESCE(vcg.delete_flagged,0)=0
              AND vcg.id NOT IN (
                SELECT DISTINCT vc.group_id FROM verse_context vc
                JOIN mti_terms mt ON mt.id = vc.mti_term_id
                WHERE vc.group_id IS NOT NULL AND vc.is_relevant=1
                  AND COALESCE(vc.delete_flagged,0)=0 AND COALESCE(mt.delete_flagged,0)=0
              )
        """).fetchone()[0]
        assert n_remaining_orphans == 0, f"Post-check failed: {n_remaining_orphans} orphans still active"
        print(f"Post-check: 0 remaining orphans ✓")

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
