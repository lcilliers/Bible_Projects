"""Roll back M04 Phase 6 (DIR-20260517-005) — sub-group routing.

Trigger: M04 Phase 5 failed the §8.6 distribution hard gate (M04-A held 81% of
substantive verses). Phase 5 rejected; Phase 6 must be undone to allow Phase 5 re-submission.

What gets rolled back:
  Op A reverse — soft-delete 7 cluster_subgroup rows for M04
  Op B reverse — soft-delete 86 mti_term_subgroup rows
  Op C reverse — NULL out 1138 verse_context.cluster_subgroup_id values for M04 terms

What is preserved:
  - cluster.status M04 stays at 'Analysis - In Progress' (Phase 4 outcome — still valid)
  - mti_terms.cluster_code unchanged (Phase 4 transfers were valid; 5 transferred terms stay in M28/M23/M08/M33)
  - 86 inherited verse_context_groups (pre-Phase-7; never touched by Phase 6)
  - verse_context.analysis_note (Phase 2 meanings) untouched
  - verse_context.is_anchor (provisional Phase 1 anchors) untouched
  - 0 cluster_finding rows existed for M04 — nothing to undo there

Directive: DIR-20260517-006 (rollback of DIR-20260517-005)
"""
from __future__ import annotations
import argparse, shutil, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
DIRECTIVE = "DIR-20260517-006"
CLUSTER = "M04"
EXPECTED_SUBGROUPS_TO_DELETE = 7
EXPECTED_PLACEMENTS_TO_DELETE = 86
EXPECTED_VC_TO_NULL = 1138


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%SZ')}] {msg}")


def backup_db() -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    name = f"bible_research_backup_{ts}_{DIRECTIVE}.db"
    out = REPO / "backups" / name
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(DB, out)
    return out


def precheck(conn) -> dict:
    log("Pre-flight checks...")

    cluster = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    if not cluster or cluster["status"] != "Analysis - In Progress":
        raise RuntimeError(
            f"cluster.status expected 'Analysis - In Progress', "
            f"got {cluster and cluster['status']!r}"
        )
    log(f"  cluster.status {CLUSTER} = {cluster['status']} ✓")

    sgs = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_subgroup WHERE cluster_code=? "
        "AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchone()["n"]
    log(f"  active {CLUSTER} sub-groups: {sgs} (expected {EXPECTED_SUBGROUPS_TO_DELETE})")
    assert sgs == EXPECTED_SUBGROUPS_TO_DELETE, "sub-group count mismatch — aborting"

    placements = conn.execute("""
        SELECT COUNT(*) AS n FROM mti_term_subgroup mts
        JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
        WHERE cs.cluster_code=? AND COALESCE(mts.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()["n"]
    log(f"  active mti_term_subgroup rows: {placements} (expected {EXPECTED_PLACEMENTS_TO_DELETE})")
    assert placements == EXPECTED_PLACEMENTS_TO_DELETE, "placement count mismatch"

    routed = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id=vc.mti_term_id
        WHERE mt.cluster_code=? AND vc.cluster_subgroup_id IS NOT NULL
          AND COALESCE(vc.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()["n"]
    log(f"  vc rows with cluster_subgroup_id set: {routed} (expected {EXPECTED_VC_TO_NULL})")
    assert routed == EXPECTED_VC_TO_NULL, "routed vc count mismatch"

    # Defensive: ensure no Phase 7 cluster_finding rows for M04
    cf = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_finding WHERE cluster_code=? "
        "AND COALESCE(delete_flagged,0)=0", (CLUSTER,)
    ).fetchone()["n"]
    log(f"  cluster_finding rows for {CLUSTER}: {cf}")
    if cf > 0:
        raise RuntimeError(
            f"{cf} cluster_finding rows exist for {CLUSTER} — Phase 11 has been "
            f"applied; rollback is unsafe without unwinding Phase 11 first."
        )


def apply(conn, dry_run: bool) -> dict:
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    audit = f" | {DIRECTIVE} rollback of DIR-20260517-005 (Phase 5 distribution gate trip)"

    log(f"\n{'='*60}\nOp C reverse — NULL out verse_context.cluster_subgroup_id\n{'='*60}")
    rc1 = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id=vc.mti_term_id
        WHERE mt.cluster_code=? AND vc.cluster_subgroup_id IS NOT NULL
          AND COALESCE(vc.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()["n"]
    log(f"  Will NULL out cluster_subgroup_id on {rc1} vc rows")
    if not dry_run:
        conn.execute("""
            UPDATE verse_context
            SET cluster_subgroup_id=NULL
            WHERE id IN (
                SELECT vc.id FROM verse_context vc
                JOIN mti_terms mt ON mt.id=vc.mti_term_id
                WHERE mt.cluster_code=? AND vc.cluster_subgroup_id IS NOT NULL
                  AND COALESCE(vc.delete_flagged,0)=0
            )
        """, (CLUSTER,))

    log(f"\n{'='*60}\nOp B reverse — Soft-delete mti_term_subgroup rows\n{'='*60}")
    rc2 = conn.execute("""
        SELECT COUNT(*) AS n FROM mti_term_subgroup mts
        JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
        WHERE cs.cluster_code=? AND COALESCE(mts.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()["n"]
    log(f"  Will soft-delete {rc2} mti_term_subgroup rows")
    if not dry_run:
        conn.execute(f"""
            UPDATE mti_term_subgroup
            SET delete_flagged=1, last_updated_date=?,
                placement_note=COALESCE(placement_note,'')||?
            WHERE id IN (
                SELECT mts.id FROM mti_term_subgroup mts
                JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
                WHERE cs.cluster_code='{CLUSTER}' AND COALESCE(mts.delete_flagged,0)=0
            )
        """, (now_iso, audit))

    log(f"\n{'='*60}\nOp A reverse — Soft-delete cluster_subgroup rows\n{'='*60}")
    rc3 = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_subgroup WHERE cluster_code=? "
        "AND COALESCE(delete_flagged,0)=0", (CLUSTER,)
    ).fetchone()["n"]
    log(f"  Will soft-delete {rc3} cluster_subgroup rows")
    if not dry_run:
        conn.execute("""
            UPDATE cluster_subgroup
            SET delete_flagged=1, last_updated_date=?,
                notes=COALESCE(notes,'')||?
            WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
        """, (now_iso, audit, CLUSTER))

    return {"vc_nulled": rc1, "placements_deleted": rc2, "subgroups_deleted": rc3}


def healthcheck(conn) -> None:
    log(f"\n{'='*60}\nPost-rollback health checks\n{'='*60}")

    sgs = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_subgroup WHERE cluster_code=? "
        "AND COALESCE(delete_flagged,0)=0", (CLUSTER,)
    ).fetchone()["n"]
    log(f"  R1 active {CLUSTER} sub-groups: {sgs} (expected 0) {'✓' if sgs==0 else '✗'}")
    assert sgs == 0

    placements = conn.execute("""
        SELECT COUNT(*) AS n FROM mti_term_subgroup mts
        JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
        WHERE cs.cluster_code=? AND COALESCE(mts.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()["n"]
    log(f"  R2 active mti_term_subgroup rows: {placements} (expected 0) "
        f"{'✓' if placements==0 else '✗'}")
    assert placements == 0

    routed = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id=vc.mti_term_id
        WHERE mt.cluster_code=? AND vc.cluster_subgroup_id IS NOT NULL
          AND COALESCE(vc.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()["n"]
    log(f"  R3 vc rows with cluster_subgroup_id set: {routed} (expected 0) "
        f"{'✓' if routed==0 else '✗'}")
    assert routed == 0

    # cluster.status stays
    st = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    log(f"  R4 cluster.status {CLUSTER}: {st['status']} "
        f"({'✓' if st['status']=='Analysis - In Progress' else '✗'})")
    assert st["status"] == "Analysis - In Progress"

    # Active term count unchanged (58)
    n = conn.execute("""
        SELECT COUNT(*) AS n FROM mti_terms WHERE cluster_code=?
          AND status IN ('extracted','extracted_thin') AND COALESCE(delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()["n"]
    log(f"  R5 active {CLUSTER} terms: {n} (expected 58) {'✓' if n==58 else '✗'}")
    assert n == 58


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    dry_run = not args.live

    log(f"Phase 6 rollback — cluster={CLUSTER} directive={DIRECTIVE}")
    log(f"Reason: Phase 5 distribution hard gate trip (M04-A held 81% of substantive)")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    if not dry_run:
        backup_path = backup_db()
        log(f"Backup: {backup_path.relative_to(REPO)}")

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        conn.execute("BEGIN")
        precheck(conn)
        result = apply(conn, dry_run=dry_run)
        if dry_run:
            log("\nDRY-RUN — rolling back")
            conn.execute("ROLLBACK")
        else:
            log("\nCommitting...")
            conn.execute("COMMIT")
            healthcheck(conn)
        log(f"\nDONE — {'simulated' if dry_run else 'applied'}: "
            f"vc_nulled={result['vc_nulled']} "
            f"placements_deleted={result['placements_deleted']} "
            f"subgroups_deleted={result['subgroups_deleted']}")
    except Exception as e:
        log(f"ERROR: {e}")
        try: conn.execute("ROLLBACK")
        except: pass
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
