"""Apply Phase 4 — M03 term transfers + status transition.

Directive: wa-global-dir-001-M03-term-transfer-v1-20260516 (DIR-20260516-015)
Governing: wa-sessionb-cluster-instruction-v2_2-20260516 §7

Operations (single transaction):
  Op A — UPDATE mti_terms.cluster_code for 11 transferred terms
  Op N — UPDATE cluster.status for M03: Data - In Progress → Analysis - In Progress

BOUNDARY terms (28) recorded in directive; no DB write at Phase 4 (per §7.4).

CC default: H6869B tsa.rah was missing from AI's debate. CC defaults to STAYS
(per brief §discipline #4 — STAYS is default for borderline). tsa.rah's
Phase 1 corpus is dominantly relevant (48 of 55 verses = 87%) — squarely M03.
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
DIRECTIVE = "DIR-20260516-015"
SOURCE_CLUSTER = "M03"

# 11 transfers per AI's Phase 3 debate
TRANSFERS = [
    # (mti_id, strongs, translit, dest_cluster, dest_name)
    (1094, "G0580",  "apobolē",     "M11", "Repentance"),
    (4683, "G0929",  "basanismos",  "M35", "Testing"),
    (4685, "G0930",  "basanistēs",  "M27", "Evil"),
    ( 744, "G1312",  "diafthora",   "M25", "Life"),
    ( 705, "G4088",  "pikria",      "M02", "Anger"),
    (4784, "G4089",  "pikros",      "M28", "Envy"),
    (1153, "H0928",  "be.ha.lah",   "M01", "Fear"),
    ( 105, "H1670",  "de.a.vah",    "M01", "Fear"),
    (7558, "H1795",  "dak.kah",     "M24", "Weakness"),
    ( 237, "H7451I", "ra.ah",       "M27", "Evil"),
    (5162, "H8383",  "te.u.nim",    "M36", "Service"),
]


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
        "SELECT status FROM cluster WHERE cluster_code=?", (SOURCE_CLUSTER,)
    ).fetchone()
    if not cluster or cluster["status"] != "Data - In Progress":
        raise RuntimeError(f"cluster.status expected 'Data - In Progress', got {cluster and cluster['status']!r}")
    log(f"  cluster.status M03 = {cluster['status']} ✓")

    for _, _, _, dest, _ in TRANSFERS:
        r = conn.execute("SELECT 1 FROM cluster WHERE cluster_code=?", (dest,)).fetchone()
        assert r, f"destination cluster {dest} does not exist"
    log(f"  destination clusters exist: {sorted({t[3] for t in TRANSFERS})} ✓")

    pre_counts = {}
    for cluster_code in [SOURCE_CLUSTER] + sorted({t[3] for t in TRANSFERS}):
        r = conn.execute("""
            SELECT COUNT(*) AS n FROM mti_terms
            WHERE cluster_code=? AND status IN ('extracted','extracted_thin')
              AND COALESCE(delete_flagged,0)=0
        """, (cluster_code,)).fetchone()
        pre_counts[cluster_code] = r["n"]
    log(f"  pre-state term counts: {pre_counts}")

    for mti_id, strongs, _, _, _ in TRANSFERS:
        r = conn.execute("""
            SELECT cluster_code, status FROM mti_terms WHERE id=? AND COALESCE(delete_flagged,0)=0
        """, (mti_id,)).fetchone()
        if not r:
            raise RuntimeError(f"mti_id={mti_id} ({strongs}) not found / soft-deleted")
        if r["cluster_code"] != SOURCE_CLUSTER:
            raise RuntimeError(f"mti_id={mti_id} ({strongs}) cluster_code is {r['cluster_code']!r}, expected M03")
        if r["status"] not in ("extracted", "extracted_thin"):
            raise RuntimeError(f"mti_id={mti_id} ({strongs}) status is {r['status']!r}, expected extracted/extracted_thin")
    log(f"  all 11 transferred terms present in M03 with valid status ✓")
    return {"pre_counts": pre_counts}


def apply(conn, dry_run: bool) -> dict:
    log(f"\n{'='*60}")
    log(f"Op A — UPDATE mti_terms.cluster_code (11 term transfers)")
    log(f"{'='*60}")
    for mti_id, strongs, translit, dest, dest_name in TRANSFERS:
        log(f"  mti={mti_id} {strongs} {translit} → {dest} ({dest_name})")
        if not dry_run:
            conn.execute(
                "UPDATE mti_terms SET cluster_code=?, last_changed=? WHERE id=?",
                (dest, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), mti_id)
            )

    log(f"\n{'='*60}")
    log(f"Op N — UPDATE cluster.status for M03")
    log(f"{'='*60}")
    log(f"  Data - In Progress → Analysis - In Progress")
    if not dry_run:
        conn.execute("""
            UPDATE cluster SET status='Analysis - In Progress', last_updated_date=?
            WHERE cluster_code=? AND status='Data - In Progress'
        """, (datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), SOURCE_CLUSTER))

    return {"transferred": len(TRANSFERS), "status_flipped": True}


def healthcheck(conn) -> None:
    log(f"\n{'='*60}\nPost-apply health checks\n{'='*60}")
    r = conn.execute("""
        SELECT COUNT(*) AS n FROM mti_terms
        WHERE cluster_code='M03' AND status IN ('extracted','extracted_thin')
          AND COALESCE(delete_flagged,0)=0
    """).fetchone()
    log(f"  Source M03 active terms: {r['n']} (expected 78)")
    assert r["n"] == 78

    transferred_ids = [t[0] for t in TRANSFERS]
    placeholders = ",".join("?" * len(transferred_ids))
    by_dest: dict[str, int] = {}
    for r in conn.execute(
        f"SELECT cluster_code, COUNT(*) AS n FROM mti_terms WHERE id IN ({placeholders}) GROUP BY cluster_code",
        transferred_ids
    ):
        by_dest[r["cluster_code"]] = r["n"]
    log(f"  Transferred terms by destination: {by_dest}")

    expected_dest: dict[str, int] = {}
    for _, _, _, dest, _ in TRANSFERS:
        expected_dest[dest] = expected_dest.get(dest, 0) + 1
    for dest, expected_n in expected_dest.items():
        actual = by_dest.get(dest, 0)
        assert actual == expected_n, f"destination {dest} expected {expected_n}, got {actual}"

    r = conn.execute("SELECT status FROM cluster WHERE cluster_code='M03'").fetchone()
    log(f"  cluster.status M03: {r['status']} ({'✓' if r['status']=='Analysis - In Progress' else '✗'})")
    assert r["status"] == "Analysis - In Progress"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    dry_run = not args.live

    log(f"Phase 4 term transfer — cluster={SOURCE_CLUSTER} directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    if not dry_run:
        backup_path = backup_db()
        log(f"Backup: {backup_path.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
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
        log(f"\nDONE — {'simulated' if dry_run else 'applied'}: transferred={result['transferred']}")
    except Exception as e:
        log(f"ERROR: {e}")
        try: conn.execute("ROLLBACK")
        except: pass
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
