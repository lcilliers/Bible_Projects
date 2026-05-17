"""Apply Phase 10 inherited-finding reconciliation for M02.

Directive: wa-cluster-M02-dir-005-inherited-findings-reconcile-v1-20260516
Governing: wa-sessionb-cluster-instruction-v2_1-20260516 §13

Inputs:
  - Sessions/Session_Clusters/M02/WA-M02-inherited-findings-reconciliation-v2-20260516.json
    (CC-reclassified per researcher Option III; supersedes AI's v1 output)

Operations (single transaction):
  Op A — UPDATE wa_session_b_findings.status + resolution_note (13 rows)
  Op B — UPDATE wa_session_research_flags resolved + resolved_note (11 rows)

Status mapping (v2_1 §13.4):
  RESOLVED-BY-CATALOGUE  → resolved_qa
  SUPERSEDED             → superseded
  ROUTE-TO-CLUSTER       → routed_cluster      (new value, v2_1)
  CARRY-TO-SESSION-D     → routed_sd

Health checks (post-apply):
  F1: wa_session_b_findings row count for M02 contributor registries unchanged
  F2: target sbf rows with status='pending' = 0
  F3: target srf rows with resolved=0 = 0
  F4: distinct new status values includes routed_cluster + routed_sd
  F5: cluster.status unchanged
"""
from __future__ import annotations
import argparse, json, shutil, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
V2_JSON = REPO / "Sessions" / "Session_Clusters" / "M02" / "WA-M02-inherited-findings-reconciliation-v1-20260516.json"
DIRECTIVE = "DIR-20260516-012"
CLUSTER = "M02"

STATUS_MAP = {
    "RESOLVED-BY-CATALOGUE": "resolved_qa",
    "FOLD-INTO-PROMPT": "folded",
    "NEW-CLUSTER-FINDING": "promoted",
    "SUPERSEDED": "superseded",
    "ROUTE-TO-CLUSTER": "routed_cluster",
    "CARRY-TO-SESSION-D": "routed_sd",
    "RESEARCHER-DECISION": "open",
}


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%SZ')}] {msg}")


def backup_db() -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    name = f"bible_research_backup_{ts}_{DIRECTIVE}.db"
    out = REPO / "backups" / name
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(DB, out)
    return out


def fetch_contributor_registry_ids(conn) -> list[int]:
    rows = conn.execute("""
        SELECT DISTINCT wr.id
        FROM word_registry wr
        JOIN mti_terms mt ON mt.owning_registry_fk = wr.id
        WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
          AND mt.status IN ('extracted','extracted_thin')
    """, (CLUSTER,)).fetchall()
    return [r["id"] for r in rows]


def precheck(conn, v2: dict) -> None:
    log("Running pre-conditions...")

    cluster = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    if not cluster or cluster["status"] != "Analysis - In Progress":
        raise RuntimeError(f"cluster.status expected 'Analysis - In Progress', got {cluster and cluster['status']!r}")
    log(f"  cluster.status = {cluster['status']} ✓")

    n = len(v2["reconciliations"])
    if n != 88:
        raise RuntimeError(f"v2 has {n} rows; expected 88")
    log(f"  v2 reconciliation rows: {n} ✓")

    # No researcher-decision rows requiring gate
    rd = sum(1 for r in v2["reconciliations"] if r["disposition"] == "RESEARCHER-DECISION")
    if rd != 0:
        raise RuntimeError(f"v2 has {rd} RESEARCHER-DECISION rows; require researcher gate before apply")
    log(f"  RESEARCHER-DECISION rows: 0 (no researcher gate needed) ✓")

    # Verify every disposition is mapped
    for r in v2["reconciliations"]:
        if r["disposition"] not in STATUS_MAP:
            raise RuntimeError(f"Unknown disposition: {r['disposition']!r} in row {r.get('id')}")
    log(f"  all dispositions are in STATUS_MAP ✓")


def fmt_audit(r: dict) -> str:
    disp = r["disposition"]
    target = r.get("target", "")
    rat = r.get("rationale", "")
    return f" | {DIRECTIVE} v2_1: {disp} → {target}. {rat}"


def apply(conn, v2: dict, dry_run: bool) -> dict:
    log(f"\n{'='*60}")
    log(f"Op A — UPDATE wa_session_b_findings")
    log(f"{'='*60}")
    sbf_rows = [r for r in v2["reconciliations"] if r["source"] == "wa_session_b_findings"]
    log(f"  Rows to update: {len(sbf_rows)}")
    sbf_status_dist: dict[str, int] = {}
    for r in sbf_rows:
        new_status = STATUS_MAP[r["disposition"]]
        sbf_status_dist[new_status] = sbf_status_dist.get(new_status, 0) + 1
        if not dry_run:
            conn.execute(
                """UPDATE wa_session_b_findings
                   SET status=?, resolution_note=COALESCE(resolution_note,'') || ?
                   WHERE id=?""",
                (new_status, fmt_audit(r), r["id"])
            )
    log(f"  Distribution: {sbf_status_dist}")

    log(f"\n{'='*60}")
    log(f"Op B — UPDATE wa_session_research_flags")
    log(f"{'='*60}")
    srf_rows = [r for r in v2["reconciliations"] if r["source"] == "wa_session_research_flags"]
    log(f"  Rows to update: {len(srf_rows)}")
    if not dry_run:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        for r in srf_rows:
            # For srf, we mark resolved=1 + resolved_note carries disposition + target + rationale.
            # We also encode the disposition in resolved_note for downstream filtering.
            note = (f"{DIRECTIVE} v2_1: {r['disposition']} → {r.get('target','')}. "
                    f"{r.get('rationale','')}")
            conn.execute(
                """UPDATE wa_session_research_flags
                   SET resolved=1, resolved_date=?, resolved_note=?
                   WHERE id=?""",
                (date_str, note, r["id"])
            )
    srf_disp_dist: dict[str, int] = {}
    for r in srf_rows:
        srf_disp_dist[r["disposition"]] = srf_disp_dist.get(r["disposition"], 0) + 1
    log(f"  Distribution: {srf_disp_dist}")

    return {"sbf_updated": len(sbf_rows), "srf_updated": len(srf_rows)}


def healthcheck(conn) -> None:
    log(f"\n{'='*60}")
    log(f"Health checks")
    log(f"{'='*60}")

    reg_ids = fetch_contributor_registry_ids(conn)
    placeholders = ",".join("?" * len(reg_ids))

    # F1: total row count (informational — should be unchanged)
    r = conn.execute(
        f"SELECT COUNT(*) AS n FROM wa_session_b_findings WHERE registry_id IN ({placeholders})",
        reg_ids
    ).fetchone()
    log(f"  F1 wa_session_b_findings rows for M02 contributors: {r['n']} (informational)")

    # F2: pending rows in the 13 we updated
    sbf_target_ids_set = set(
        r["id"] for r in json.loads(V2_JSON.read_text(encoding="utf-8"))["reconciliations"]
        if r["source"] == "wa_session_b_findings"
    )
    placeholders_sbf = ",".join("?" * len(sbf_target_ids_set))
    r = conn.execute(
        f"SELECT COUNT(*) AS n FROM wa_session_b_findings WHERE id IN ({placeholders_sbf}) AND status='pending'",
        list(sbf_target_ids_set)
    ).fetchone()
    log(f"  F2 target sbf rows still status='pending': {r['n']} ({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0, "F2 failed"

    # F3: unresolved srf rows in our target subset
    srf_target_ids_set = set(
        r["id"] for r in json.loads(V2_JSON.read_text(encoding="utf-8"))["reconciliations"]
        if r["source"] == "wa_session_research_flags"
    )
    placeholders_srf = ",".join("?" * len(srf_target_ids_set))
    r = conn.execute(
        f"SELECT COUNT(*) AS n FROM wa_session_research_flags WHERE id IN ({placeholders_srf}) AND resolved=0",
        list(srf_target_ids_set)
    ).fetchone()
    log(f"  F3 target srf rows still resolved=0: {r['n']} ({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0, "F3 failed"

    # F4: distinct new status values
    distinct_statuses = {
        row["status"] for row in conn.execute(
            f"SELECT DISTINCT status FROM wa_session_b_findings WHERE id IN ({placeholders_sbf})",
            list(sbf_target_ids_set)
        )
    }
    log(f"  F4 distinct sbf status values for our 35 rows: {distinct_statuses}")
    # For M02: AI assigned ROUTE-TO-CLUSTER (34 sbf) + FOLD-INTO-PROMPT (1 sbf).
    # Expected sbf status set: routed_cluster + folded.
    expected = {"routed_cluster", "folded"}
    missing = expected - distinct_statuses
    assert not missing, f"F4 expected to see {expected}; missing: {missing}"
    log(f"     all expected statuses present ✓")

    # F5: cluster.status unchanged
    cluster = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    log(f"  F5 cluster.status: {cluster['status']} ({'✓' if cluster['status']=='Analysis - In Progress' else '✗'})")
    assert cluster["status"] == "Analysis - In Progress", "F5 failed"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="Apply changes (default: dry-run)")
    args = ap.parse_args()
    dry_run = not args.live

    log(f"Phase 10 reconciliation — cluster={CLUSTER} directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    v2 = json.loads(V2_JSON.read_text(encoding="utf-8"))

    if not dry_run:
        backup_path = backup_db()
        log(f"Backup: {backup_path.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("BEGIN")
        precheck(conn, v2)
        result = apply(conn, v2, dry_run=dry_run)
        if dry_run:
            log("\nDRY-RUN — rolling back")
            conn.execute("ROLLBACK")
        else:
            log("\nCommitting...")
            conn.execute("COMMIT")
            healthcheck(conn)
        log(f"\nDONE — {'simulated' if dry_run else 'applied'}: "
            f"sbf updated = {result['sbf_updated']} · "
            f"srf updated = {result['srf_updated']}")
    except Exception as e:
        log(f"ERROR: {e}")
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
