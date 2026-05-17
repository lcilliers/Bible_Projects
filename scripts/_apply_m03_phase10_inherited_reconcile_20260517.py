"""Apply Phase 10 inherited-finding reconciliation for M03.

Directive: wa-cluster-M03-dir-005-inherited-findings-reconcile-v1-20260517
Governing: wa-sessionb-cluster-instruction-v2_2-20260516 §13 (v2_1 catalogue)

Input: Sessions/Session_Clusters/M03/WA-M03-inherited-findings-reconciliation-v1-20260517.json
       (CC-built from AI's markdown + DB facts per researcher routing directive
        2026-05-17 — every row routed to its identified destination cluster.)

Operations (single transaction):
  Op A — UPDATE wa_session_b_findings.status + resolution_note (189 rows)
  Op B — UPDATE wa_session_research_flags.resolved + resolved_note (58 rows)

Status mapping (v2_1 §13.4):
  RESOLVED-BY-CATALOGUE  → resolved_qa
  FOLD-INTO-PROMPT       → folded
  NEW-CLUSTER-FINDING    → promoted
  SUPERSEDED             → superseded
  ROUTE-TO-CLUSTER       → routed_cluster
  CARRY-TO-SESSION-D     → routed_sd
  RESEARCHER-DECISION    → open
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
RECON_JSON = (
    REPO / "Sessions" / "Session_Clusters" / "M03"
         / "WA-M03-inherited-findings-reconciliation-v1-20260517.json"
)
DIRECTIVE = "DIR-20260517-001"
CLUSTER = "M03"
EXPECTED_TOTAL = 247

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


def precheck(conn, doc: dict) -> None:
    log("Running pre-conditions...")

    cluster = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    if not cluster or cluster["status"] != "Analysis - In Progress":
        raise RuntimeError(
            f"cluster.status expected 'Analysis - In Progress', "
            f"got {cluster and cluster['status']!r}"
        )
    log(f"  cluster.status = {cluster['status']} ✓")

    n = len(doc["reconciliations"])
    if n != EXPECTED_TOTAL:
        raise RuntimeError(f"JSON has {n} rows; expected {EXPECTED_TOTAL}")
    log(f"  reconciliation rows: {n} ✓")

    rd = sum(1 for r in doc["reconciliations"] if r["disposition"] == "RESEARCHER-DECISION")
    log(f"  RESEARCHER-DECISION rows: {rd} (proceeding with these as status='open')")

    for r in doc["reconciliations"]:
        if r["disposition"] not in STATUS_MAP:
            raise RuntimeError(f"Unknown disposition: {r['disposition']!r} in row {r.get('id')}")
    log(f"  all dispositions in STATUS_MAP ✓")

    # Verify every row exists in DB
    for r in doc["reconciliations"]:
        if r["source"] == "wa_session_b_findings":
            chk = conn.execute(
                "SELECT 1 FROM wa_session_b_findings WHERE id=?", (r["id"],)
            ).fetchone()
        else:
            chk = conn.execute(
                "SELECT 1 FROM wa_session_research_flags WHERE id=?", (r["id"],)
            ).fetchone()
        if not chk:
            raise RuntimeError(f"Row not in DB: source={r['source']} id={r['id']}")
    log(f"  all 247 row_ids resolve in DB ✓")


def fmt_audit(r: dict) -> str:
    disp = r["disposition"]
    target = r.get("target", "")
    rat = r.get("rationale", "")
    return f" | {DIRECTIVE} v2_1: {disp} → {target}. {rat}"


def apply(conn, doc: dict, dry_run: bool) -> dict:
    log(f"\n{'='*60}\nOp A — UPDATE wa_session_b_findings\n{'='*60}")
    sbf_rows = [r for r in doc["reconciliations"] if r["source"] == "wa_session_b_findings"]
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
    log(f"  Status distribution: {sbf_status_dist}")

    log(f"\n{'='*60}\nOp B — UPDATE wa_session_research_flags\n{'='*60}")
    srf_rows = [r for r in doc["reconciliations"] if r["source"] == "wa_session_research_flags"]
    log(f"  Rows to update: {len(srf_rows)}")
    if not dry_run:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        for r in srf_rows:
            note = (
                f"{DIRECTIVE} v2_1: {r['disposition']} → {r.get('target','')}. "
                f"{r.get('rationale','')}"
            )
            conn.execute(
                """UPDATE wa_session_research_flags
                   SET resolved=1, resolved_date=?, resolved_note=?
                   WHERE id=?""",
                (date_str, note, r["id"])
            )
    srf_disp_dist: dict[str, int] = {}
    for r in srf_rows:
        srf_disp_dist[r["disposition"]] = srf_disp_dist.get(r["disposition"], 0) + 1
    log(f"  Disposition distribution: {srf_disp_dist}")

    return {"sbf_updated": len(sbf_rows), "srf_updated": len(srf_rows)}


def healthcheck(conn) -> None:
    log(f"\n{'='*60}\nHealth checks\n{'='*60}")
    doc = json.loads(RECON_JSON.read_text(encoding="utf-8"))

    sbf_target_ids = sorted(
        r["id"] for r in doc["reconciliations"] if r["source"] == "wa_session_b_findings"
    )
    placeholders = ",".join("?" * len(sbf_target_ids))
    r = conn.execute(
        f"SELECT COUNT(*) AS n FROM wa_session_b_findings "
        f"WHERE id IN ({placeholders}) AND status IN ('open','pending','confirmed')",
        sbf_target_ids
    ).fetchone()
    log(f"  F1 target sbf rows still in open/pending/confirmed: {r['n']} "
        f"({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0

    srf_target_ids = sorted(
        r["id"] for r in doc["reconciliations"] if r["source"] == "wa_session_research_flags"
    )
    placeholders_srf = ",".join("?" * len(srf_target_ids))
    r = conn.execute(
        f"SELECT COUNT(*) AS n FROM wa_session_research_flags "
        f"WHERE id IN ({placeholders_srf}) AND COALESCE(resolved,0)=0",
        srf_target_ids
    ).fetchone()
    log(f"  F2 target srf rows still resolved=0: {r['n']} "
        f"({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0

    distinct_statuses = {
        row["status"] for row in conn.execute(
            f"SELECT DISTINCT status FROM wa_session_b_findings WHERE id IN ({placeholders})",
            sbf_target_ids
        )
    }
    log(f"  F3 distinct sbf status values for target rows: {sorted(distinct_statuses)}")

    cluster = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)).fetchone()
    log(f"  F4 cluster.status: {cluster['status']} "
        f"({'✓' if cluster['status']=='Analysis - In Progress' else '✗'})")
    assert cluster["status"] == "Analysis - In Progress"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    dry_run = not args.live

    log(f"Phase 10 reconciliation — cluster={CLUSTER} directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    doc = json.loads(RECON_JSON.read_text(encoding="utf-8"))

    if not dry_run:
        backup_path = backup_db()
        log(f"Backup: {backup_path.relative_to(REPO)}")

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    try:
        conn.execute("BEGIN")
        precheck(conn, doc)
        result = apply(conn, doc, dry_run=dry_run)
        if dry_run:
            log("\nDRY-RUN — rolling back")
            conn.execute("ROLLBACK")
        else:
            log("\nCommitting...")
            conn.execute("COMMIT")
            healthcheck(conn)
        log(f"\nDONE — {'simulated' if dry_run else 'applied'}: "
            f"sbf={result['sbf_updated']} · srf={result['srf_updated']}")
    except Exception as e:
        log(f"ERROR: {e}")
        try: conn.execute("ROLLBACK")
        except: pass
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
