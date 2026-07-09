"""Validate a cluster's completion state and (optionally) sync stale vc_status.

Designed to run as part of the cluster completion checklist (Phase 10 onward).
Reports discrepancies between the cluster's actual analytical state and the
per-term tracking fields, and can backfill stale fields where the underlying
work is demonstrably complete.

Checks performed:
  C1. VC-coverage gap — terms placed in a sub-group but with NO active
      verse_context rows in any cluster VCG. This is a real analytical gap
      and must be addressed (placement without VC means the term entered the
      cluster without verse-level work being done for it).
  C2. vc_status sync — terms with active VC rows in cluster VCGs but whose
      `mti_terms.vc_status` is not at a canonical complete value. The field
      is stale (the legacy per-word VC workflow tracking field was not
      updated when VC happened via the cluster pipeline). Safe to backfill.

Usage:
    # Read-only validation (default)
    python scripts/_validate_cluster_completion_v1_20260513.py --cluster M15

    # Apply the vc_status sync (writes to DB)
    python scripts/_validate_cluster_completion_v1_20260513.py --cluster M15 --fix

Exit codes:
    0   no discrepancies
    1   real gaps found (C1) — must be addressed before completion
    2   stale-only discrepancies found (C2 only) — can be auto-fixed
"""
import sqlite3, sys, os, json, argparse
from datetime import datetime, timezone
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"
VC_COMPLETE_VALUES = ("vc_completed", "Complete")


def get_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def check_c1_vc_coverage_gap(conn, cluster_code):
    """Cluster terms placed in a sub-group but with NO active verse_context
    rows tied to any of the cluster's sub-groups. A real gap means VC was
    not performed for the term at all — neither into a VCG nor as a set-aside.

    NOTE: set-aside rows (group_id IS NULL but cluster_subgroup_id IS set,
    with set_aside_reason populated) ARE counted as VC done — they represent
    a completed analytical judgement that the term carries no inner-being
    phenomenon in the verse evidence."""
    return [dict(r) for r in conn.execute("""
        SELECT mt.id AS mt_id, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.vc_status,
               GROUP_CONCAT(DISTINCT cs.subgroup_code) AS placements
          FROM mti_terms mt
          JOIN mti_term_subgroup mts ON mts.mti_term_id = mt.id
                AND COALESCE(mts.delete_flagged,0)=0
          JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
                AND COALESCE(cs.delete_flagged,0)=0
         WHERE mt.cluster_code = ? AND COALESCE(mt.delete_flagged,0)=0
           AND cs.cluster_code = ?
           AND NOT EXISTS (
               SELECT 1 FROM verse_context vc
                 JOIN cluster_subgroup cs2 ON cs2.id = vc.cluster_subgroup_id
                WHERE vc.mti_term_id = mt.id
                  AND cs2.cluster_code = ?
                  AND COALESCE(vc.delete_flagged,0)=0
           )
         GROUP BY mt.id, mt.strongs_number, mt.transliteration, mt.gloss, mt.vc_status
         ORDER BY mt.strongs_number
    """, (cluster_code, cluster_code, cluster_code)).fetchall()]


def check_c2_stale_vc_status(conn, cluster_code):
    """Cluster terms with active VC rows tied to a cluster sub-group (including
    set-aside rows) but vc_status not at a canonical complete value. Backfill
    candidates."""
    placeholders = ",".join("?" * len(VC_COMPLETE_VALUES))
    return [dict(r) for r in conn.execute(f"""
        SELECT mt.id AS mt_id, mt.strongs_number, mt.transliteration, mt.gloss,
               COALESCE(mt.vc_status,'(NULL)') AS current_vc_status,
               COUNT(DISTINCT vc.id) AS n_vc_rows
          FROM mti_terms mt
          JOIN verse_context vc ON vc.mti_term_id = mt.id
                AND COALESCE(vc.delete_flagged,0)=0
          JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
                AND cs.cluster_code = ?
         WHERE mt.cluster_code = ? AND COALESCE(mt.delete_flagged,0)=0
           AND (mt.vc_status IS NULL
                OR mt.vc_status NOT IN ({placeholders}))
         GROUP BY mt.id, mt.strongs_number, mt.transliteration, mt.gloss, mt.vc_status
         ORDER BY mt.strongs_number
    """, (cluster_code, cluster_code, *VC_COMPLETE_VALUES)).fetchall()]


def apply_fix_c2(conn, cluster_code, stale_terms, dry_run=True):
    """Backfill vc_status='vc_completed' for terms identified by check C2.
    Takes a JSON backup of each row before update."""
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    backup_dir = "backups/row_backups"
    os.makedirs(backup_dir, exist_ok=True)
    backup_path = os.path.join(
        backup_dir,
        f"mti_terms_{cluster_code}_vc_status_sync_"
        f"{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
    )

    # Capture full before-state for backup (filter to the affected rows)
    mt_ids = [t["mt_id"] for t in stale_terms]
    if not mt_ids:
        return None, None
    qmarks = ",".join("?" * len(mt_ids))
    before_rows = [dict(r) for r in conn.execute(
        f"SELECT * FROM mti_terms WHERE id IN ({qmarks})", mt_ids
    ).fetchall()]

    with open(backup_path, "w", encoding="utf-8") as f:
        json.dump({"timestamp": now_utc, "cluster_code": cluster_code,
                   "row_count": len(before_rows), "rows": before_rows},
                  f, indent=2, ensure_ascii=False)

    note = f"vc_status synced from stale value by validate_cluster_completion ({cluster_code}, {now_utc})"

    if dry_run:
        return backup_path, "dry-run"

    conn.execute(
        f"UPDATE mti_terms SET vc_status='vc_completed', "
        f"       vc_status_updated_at=?, "
        f"       vc_status_note = COALESCE(vc_status_note || ' | ', '') || ? "
        f" WHERE id IN ({qmarks})",
        (now_utc, note, *mt_ids)
    )
    conn.commit()
    return backup_path, "committed"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True, help="Cluster code, e.g. M15")
    ap.add_argument("--fix", action="store_true",
                    help="Apply the vc_status sync (writes to DB). Without this "
                         "flag, runs in read-only validation mode.")
    args = ap.parse_args()

    conn = get_conn()
    code = args.cluster

    cluster = conn.execute(
        "SELECT cluster_code, short_name, description, status FROM cluster WHERE cluster_code=?",
        (code,)
    ).fetchone()
    if not cluster:
        raise SystemExit(f"Cluster {code} not found")

    print(f"Validating cluster {code} ({cluster['short_name']}) — current status: {cluster['status']}")
    print()

    # --- C1: VC-coverage gap ---
    c1 = check_c1_vc_coverage_gap(conn, code)
    print(f"C1. VC-coverage gap — placed terms with no VC rows: {len(c1)}")
    if c1:
        print(f"   ⚠ This is a real analytical gap. The term has been placed in "
              f"a sub-group but verse-level work has not been done.")
        for t in c1:
            print(f"     - {t['strongs_number']:8s} {t['transliteration']:20s} "
                  f"({(t['gloss'] or '')[:30]:30s}) placed in {t['placements']} "
                  f"  vc_status={t['vc_status']}")

    print()

    # --- C2: Stale vc_status ---
    c2 = check_c2_stale_vc_status(conn, code)
    print(f"C2. Stale vc_status — terms with VC rows but non-complete status: {len(c2)}")
    if c2:
        # Group by current value for compactness
        by_val = {}
        for t in c2:
            by_val.setdefault(t["current_vc_status"], []).append(t)
        for val, terms in by_val.items():
            print(f"   - vc_status='{val}': {len(terms)} terms")
        print(f"   Total VC rows backing these terms: {sum(t['n_vc_rows'] for t in c2)}")
        print(f"   ℹ Safe to backfill to 'vc_completed' — VC work is demonstrably done.")

    print()

    # --- Apply fix if requested ---
    if c2 and args.fix:
        print("Applying C2 fix (--fix specified)…")
        backup_path, status = apply_fix_c2(conn, code, c2, dry_run=False)
        print(f"  Backup: {backup_path}")
        print(f"  Status: {status}")
        # Re-check
        c2_after = check_c2_stale_vc_status(conn, code)
        print(f"  C2 after fix: {len(c2_after)} stale terms remaining")
    elif c2 and not args.fix:
        print("To apply the C2 backfill: re-run with --fix")
        # Take a backup anyway so it's ready
        backup_path, _ = apply_fix_c2(conn, code, c2, dry_run=True)
        print(f"  (Backup pre-captured at: {backup_path})")

    print()
    print("Summary:")
    print(f"  Real gaps (C1):         {len(c1)}  {'(must address before completion)' if c1 else ''}")
    print(f"  Stale-only (C2):        {len(c2)}  {'(safe to auto-fix)' if c2 else ''}")

    conn.close()
    if c1:
        sys.exit(1)
    if c2:
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
