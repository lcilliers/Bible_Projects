"""Apply M04 Phase 8 — soft-delete 86 inherited VCGs + their vcg_term rows.

Directive: wa-cluster-M04-dir-005-vcg-dissolve-v1-20260517 (DIR-20260517-009)
Governing: wa-sessionb-cluster-instruction-v2_4-20260517 §11

Pre-conditions (verified by precheck):
  - cluster.status M04 = 'Analysis - In Progress'
  - 0 active is_relevant vc rows still pointing to inherited M04 VCGs (id < 3813)
  - 86 inherited M04 VCGs (vcg_term-linked, active)

Operations (single transaction):
  Op A — Soft-delete vcg_term rows for inherited VCGs
  Op B — Soft-delete verse_context_group rows + append directive audit note

Trust basis: M01 blind verification methodology validates AI's Phase 7 internal
coherence under v2_4; M04's Phase 7 v2 passed all §10.9 mechanical checks
(1138/1138 verse coverage, 0 phantoms, 0 cross-cluster, 0 cross-VCG dups).
Dissolution comparison report skipped per researcher direction.
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
DIRECTIVE = "DIR-20260517-009"
CLUSTER = "M04"
NEW_VCG_MIN_ID = 3813
EXPECTED_INHERITED = 86
EXPECTED_NEW = 30


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
        SELECT DISTINCT vcg.id FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code=? AND vcg.id < ? AND COALESCE(vcg.delete_flagged,0)=0
        ORDER BY vcg.id
    """, (CLUSTER, NEW_VCG_MIN_ID)).fetchall()
    return [r["id"] for r in rows]


def precheck(conn) -> list[int]:
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

    inherited = fetch_inherited_vcgs(conn)
    log(f"  Inherited {CLUSTER} VCGs to dissolve: {len(inherited)} "
        f"(expected {EXPECTED_INHERITED})")
    if len(inherited) != EXPECTED_INHERITED:
        raise RuntimeError(f"Expected {EXPECTED_INHERITED} inherited; found {len(inherited)}")

    ids_str = ",".join(str(i) for i in inherited)
    r = conn.execute(f"""
        SELECT COUNT(*) AS n FROM verse_context
        WHERE COALESCE(delete_flagged,0)=0 AND is_relevant=1
          AND group_id IN ({ids_str})
    """).fetchone()
    if r["n"] != 0:
        raise RuntimeError(
            f"{r['n']} active is_relevant vc rows still point to inherited VCGs"
        )
    log(f"  Active is_relevant vc rows still pointing to inherited: 0 ✓")
    return inherited


def apply(conn, inherited: list[int], dry_run: bool) -> dict:
    ids_str = ",".join(str(i) for i in inherited)
    audit = (
        f" | {DIRECTIVE} dissolved (superseded by DIR-20260517-008 new VCGs)"
    )

    log(f"\n{'='*60}\nOp A — Soft-delete vcg_term rows\n{'='*60}")
    n_vt = conn.execute(
        f"SELECT COUNT(*) AS n FROM vcg_term "
        f"WHERE vcg_id IN ({ids_str}) AND COALESCE(delete_flagged,0)=0"
    ).fetchone()["n"]
    log(f"  Soft-delete count: {n_vt}")
    if not dry_run:
        conn.execute(
            f"UPDATE vcg_term SET delete_flagged=1 "
            f"WHERE vcg_id IN ({ids_str}) AND COALESCE(delete_flagged,0)=0"
        )

    log(f"\n{'='*60}\nOp B — Soft-delete verse_context_group rows\n{'='*60}")
    n_vcg = conn.execute(
        f"SELECT COUNT(*) AS n FROM verse_context_group "
        f"WHERE id IN ({ids_str}) AND COALESCE(delete_flagged,0)=0"
    ).fetchone()["n"]
    log(f"  Soft-delete count: {n_vcg}")
    if not dry_run:
        conn.execute(
            f"""UPDATE verse_context_group
                SET delete_flagged=1, notes=COALESCE(notes,'') || ?
                WHERE id IN ({ids_str}) AND COALESCE(delete_flagged,0)=0""",
            (audit,)
        )

    return {"vcg_term_soft_deleted": n_vt, "vcg_soft_deleted": n_vcg}


def healthcheck(conn, inherited: list[int]) -> None:
    log(f"\n{'='*60}\nHealth checks\n{'='*60}")
    ids_str = ",".join(str(i) for i in inherited)

    r = conn.execute(
        f"SELECT COUNT(*) AS n FROM vcg_term "
        f"WHERE vcg_id IN ({ids_str}) AND COALESCE(delete_flagged,0)=0"
    ).fetchone()
    log(f"  D1 active vcg_term pointing to dissolved: {r['n']} "
        f"({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0

    r = conn.execute(f"""
        SELECT COUNT(DISTINCT vcg.id) AS n FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code=? AND vcg.id < ? AND COALESCE(vcg.delete_flagged,0)=0
    """, (CLUSTER, NEW_VCG_MIN_ID)).fetchone()
    log(f"  D2 active inherited {CLUSTER} VCGs (id < {NEW_VCG_MIN_ID}): {r['n']} "
        f"({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0

    r = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
          AND vc.is_relevant=1 AND vc.group_id IS NULL
    """, (CLUSTER,)).fetchone()
    log(f"  D3 active is_relevant vc with group_id NULL: {r['n']} "
        f"({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0

    r = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN verse_context_group vcg ON vcg.id = vc.group_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
          AND vc.is_relevant=1 AND vcg.delete_flagged=1
    """, (CLUSTER,)).fetchone()
    log(f"  D4 active is_relevant vc pointing to delete_flagged VCG: {r['n']} "
        f"({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0

    r = conn.execute("""
        SELECT COUNT(DISTINCT vcg.id) AS n FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vcg.delete_flagged,0)=0
          AND COALESCE(vt.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()
    log(f"  D5 active {CLUSTER} VCGs reachable via vcg_term: {r['n']} "
        f"(expected {EXPECTED_NEW}) {'✓' if r['n']==EXPECTED_NEW else '✗'}")
    assert r["n"] == EXPECTED_NEW


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    dry_run = not args.live

    log(f"Phase 8 dissolution — cluster={CLUSTER} directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    if not dry_run:
        backup_path = backup_db()
        log(f"Backup: {backup_path.relative_to(REPO)}")

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
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
        log(f"\nDONE — vcg_term={result['vcg_term_soft_deleted']} · "
            f"vcg={result['vcg_soft_deleted']}")
    except Exception as e:
        log(f"ERROR: {e}")
        try: conn.execute("ROLLBACK")
        except: pass
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
