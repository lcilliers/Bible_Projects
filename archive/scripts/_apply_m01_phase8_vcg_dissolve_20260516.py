"""Apply Phase 8 (Dissolve old VCGs) for M01.

Directive: wa-cluster-M01-dir-004-vcg-dissolve-v1-20260516
Governing: wa-sessionb-cluster-instruction-v2_0-20260515 §11

Operations (single transaction):
  Op A — Soft-delete vcg_term rows linking inherited VCGs to terms (115 rows)
  Op B — Soft-delete the inherited verse_context_group rows themselves (115 rows)

Pre-conditions:
  - M01 cluster status = 'Analysis - In Progress'
  - 0 active is_relevant vc rows pointing to any inherited VCG

Health checks (post-apply):
  D1: active vcg_term rows pointing to dissolved VCGs = 0
  D2: active verse_context_group rows in M01 with id < new-vcg-min-id = 0
  D3: active is_relevant vc rows in M01 with group_id IS NULL = 0 (unchanged)
  D4: active is_relevant vc rows in M01 with group_id pointing to a delete_flagged VCG = 0
  D5: active VCGs reachable from M01 via vcg_term = 36
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
DIRECTIVE = "DIR-20260516-004"
CLUSTER = "M01"
NEW_VCG_MIN_ID = 3726
EXPECTED_INHERITED = 115
EXPECTED_NEW_VCGS = 36


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%SZ')}] {msg}")


def backup_db() -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    name = f"bible_research_backup_{ts}_{DIRECTIVE}.db"
    out = REPO / "backups" / name
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(DB, out)
    return out


def fetch_inherited_vcgs(conn) -> list[int]:
    rows = conn.execute("""
        SELECT DISTINCT vcg.id
        FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code = ?
          AND vcg.id < ?
          AND COALESCE(vcg.delete_flagged, 0) = 0
        ORDER BY vcg.id
    """, (CLUSTER, NEW_VCG_MIN_ID)).fetchall()
    return [r["id"] for r in rows]


def precheck(conn) -> None:
    log("Running pre-conditions...")
    cluster = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    if not cluster or cluster["status"] != "Analysis - In Progress":
        raise RuntimeError(f"cluster.status expected 'Analysis - In Progress', got {cluster and cluster['status']!r}")
    log(f"  cluster.status = {cluster['status']} ✓")

    inherited = fetch_inherited_vcgs(conn)
    if len(inherited) != EXPECTED_INHERITED:
        raise RuntimeError(f"Expected {EXPECTED_INHERITED} inherited VCGs, found {len(inherited)}")
    log(f"  inherited VCGs to dissolve: {len(inherited)} ✓")

    r = conn.execute(f"""
        SELECT COUNT(*) AS n FROM verse_context
        WHERE COALESCE(delete_flagged,0)=0 AND is_relevant=1
          AND group_id IN ({','.join(str(i) for i in inherited)})
    """).fetchone()
    if r["n"] != 0:
        raise RuntimeError(f"Pre-cond fail: {r['n']} active is_relevant vc rows still point to inherited VCGs")
    log(f"  active is_relevant vc rows still pointing to inherited VCGs: 0 ✓")
    return inherited


def apply(conn, inherited: list[int], dry_run: bool) -> dict:
    ids_str = ",".join(str(i) for i in inherited)
    audit_suffix = f" | {DIRECTIVE} dissolved (superseded by DIR-20260516-003 new VCGs)"

    log(f"\n{'='*60}")
    log(f"Op A — Soft-delete vcg_term rows")
    log(f"{'='*60}")
    count_vcg_term = conn.execute(
        f"SELECT COUNT(*) AS n FROM vcg_term WHERE vcg_id IN ({ids_str}) AND COALESCE(delete_flagged,0)=0"
    ).fetchone()["n"]
    log(f"  Will soft-delete {count_vcg_term} vcg_term rows")
    if not dry_run:
        conn.execute(
            f"UPDATE vcg_term SET delete_flagged=1 WHERE vcg_id IN ({ids_str}) AND COALESCE(delete_flagged,0)=0"
        )

    log(f"\n{'='*60}")
    log(f"Op B — Soft-delete verse_context_group rows")
    log(f"{'='*60}")
    count_vcg = conn.execute(
        f"SELECT COUNT(*) AS n FROM verse_context_group WHERE id IN ({ids_str}) AND COALESCE(delete_flagged,0)=0"
    ).fetchone()["n"]
    log(f"  Will soft-delete {count_vcg} verse_context_group rows")
    if not dry_run:
        conn.execute(
            f"""UPDATE verse_context_group
                SET delete_flagged=1,
                    notes = COALESCE(notes,'') || ?
                WHERE id IN ({ids_str}) AND COALESCE(delete_flagged,0)=0""",
            (audit_suffix,)
        )

    return {"vcg_term_soft_deleted": count_vcg_term, "vcg_soft_deleted": count_vcg}


def healthcheck(conn, inherited: list[int]) -> None:
    log(f"\n{'='*60}")
    log(f"Health checks")
    log(f"{'='*60}")
    ids_str = ",".join(str(i) for i in inherited)

    # D1
    r = conn.execute(
        f"SELECT COUNT(*) AS n FROM vcg_term WHERE vcg_id IN ({ids_str}) AND COALESCE(delete_flagged,0)=0"
    ).fetchone()
    log(f"  D1 active vcg_term rows pointing to dissolved VCGs: {r['n']} ({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0, "D1 failed"

    # D2
    r = conn.execute(f"""
        SELECT COUNT(DISTINCT vcg.id) AS n
        FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code=? AND vcg.id < {NEW_VCG_MIN_ID} AND COALESCE(vcg.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()
    log(f"  D2 active VCGs in M01 with id < {NEW_VCG_MIN_ID}: {r['n']} ({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0, "D2 failed"

    # D3
    r = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0 AND vc.is_relevant=1 AND vc.group_id IS NULL
    """, (CLUSTER,)).fetchone()
    log(f"  D3 active is_relevant vc rows in M01 with group_id IS NULL: {r['n']} ({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0, "D3 failed"

    # D4
    r = conn.execute("""
        SELECT COUNT(*) AS n
        FROM verse_context vc
        JOIN verse_context_group vcg ON vcg.id = vc.group_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0 AND vc.is_relevant=1
          AND vcg.delete_flagged=1
    """, (CLUSTER,)).fetchone()
    log(f"  D4 active is_relevant vc rows pointing to a delete_flagged VCG: {r['n']} ({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0, "D4 failed"

    # D5
    r = conn.execute("""
        SELECT COUNT(DISTINCT vcg.id) AS n
        FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vcg.delete_flagged,0)=0 AND COALESCE(vt.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()
    log(f"  D5 active VCGs reachable from M01 via vcg_term: {r['n']} (expected {EXPECTED_NEW_VCGS}) ({'✓' if r['n']==EXPECTED_NEW_VCGS else '✗'})")
    assert r["n"] == EXPECTED_NEW_VCGS, "D5 failed"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="Apply changes (default: dry-run)")
    args = ap.parse_args()
    dry_run = not args.live

    log(f"Phase 8 dissolution — cluster={CLUSTER} directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    if not dry_run:
        backup_path = backup_db()
        log(f"Backup: {backup_path.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        conn.execute("BEGIN")
        inherited = precheck(conn)
        result = apply(conn, inherited, dry_run=dry_run)
        if dry_run:
            log("\nDRY-RUN — rolling back")
            conn.execute("ROLLBACK")
        else:
            log("\nCommitting...")
            conn.execute("COMMIT")
            healthcheck(conn, inherited)
        log(f"\nDONE — {'simulated' if dry_run else 'applied'}: "
            f"vcg_term soft-deleted = {result['vcg_term_soft_deleted']} · "
            f"verse_context_group soft-deleted = {result['vcg_soft_deleted']}")
    except Exception as e:
        log(f"ERROR: {e}")
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
