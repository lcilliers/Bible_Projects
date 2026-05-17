"""Apply Phase 12 — M02 cluster closure.

Directive: wa-cluster-M02-dir-007-closure-v1-20260516
Governing: wa-sessionb-cluster-instruction-v2_2-20260516 §15

Pre-flight checks:
  C1 — is_relevant verses must all have group_id AND cluster_subgroup_id
  C2 — every active term has vc_status='vc_completed'
  R4 — every term with is_relevant verses has ≥1 active anchor
  P1 — cluster_finding rows exist for M02 v1-20260516 (Phase 11 applied)
  P2 — distinct prompts covered = 189
  B1 — BOUNDARY terms have an exit disposition (flagged-for-decision is acceptable)

Operations (single transaction):
  Op A — BOUNDARY exit via flagged-for-decision: INSERT one wa_session_research_flags
         row per BOUNDARY term with flag_code='BOUNDARY_DECISION_PENDING'. Points to
         the Phase 9 per-term structural characterisation in part4.
  Op B — UPDATE cluster.status = 'Analysis Completed' (FROM 'Analysis - In Progress')
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
DIRECTIVE = "DIR-20260516-014"
CLUSTER = "M02"
VERSION = "v1-20260516"
BOUNDARY_SG_ID = 72  # M02-BOUNDARY

# Default characterisation source (where researcher can find each term's Phase 9 notes)
PART4_FILE = "WA-M02-consolidated-findings-v1-20260516-part4-T5-T7.md"


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
        "SELECT status, version FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    if not cluster or cluster["status"] != "Analysis - In Progress":
        raise RuntimeError(f"cluster.status expected 'Analysis - In Progress', got {cluster and cluster['status']!r}")
    log(f"  cluster.status = {cluster['status']} ✓")

    # C1
    r = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
          AND vc.is_relevant=1 AND (vc.group_id IS NULL OR vc.cluster_subgroup_id IS NULL)
    """, (CLUSTER,)).fetchone()
    log(f"  C1 (is_relevant w/o group_id OR sg_id): {r['n']} ({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0, "C1 failed"

    # C2
    r = conn.execute("""
        SELECT COUNT(*) AS n FROM mti_terms mt
        WHERE mt.cluster_code=? AND mt.status IN ('extracted','extracted_thin')
          AND COALESCE(mt.delete_flagged,0)=0
          AND COALESCE(mt.vc_status, '') != 'vc_completed'
    """, (CLUSTER,)).fetchone()
    log(f"  C2 (terms not vc_completed): {r['n']} ({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0, "C2 failed"

    # R4
    r = conn.execute("""
        SELECT COUNT(*) AS n FROM mti_terms mt
        WHERE mt.cluster_code=? AND mt.status IN ('extracted','extracted_thin')
          AND COALESCE(mt.delete_flagged,0)=0
          AND mt.id IN (SELECT DISTINCT mti_term_id FROM verse_context
                         WHERE is_relevant=1 AND COALESCE(delete_flagged,0)=0)
          AND mt.id NOT IN (SELECT DISTINCT mti_term_id FROM verse_context
                             WHERE is_anchor=1 AND COALESCE(delete_flagged,0)=0)
    """, (CLUSTER,)).fetchone()
    log(f"  R4 (relevant w/o anchor): {r['n']} ({'✓' if r['n']==0 else '✗'})")
    assert r["n"] == 0, "R4 failed"

    # P1 + P2
    r = conn.execute("""
        SELECT COUNT(*) AS n, COUNT(DISTINCT obs_id) AS prompts FROM cluster_finding
        WHERE cluster_code=? AND version=?
    """, (CLUSTER, VERSION)).fetchone()
    log(f"  P1/P2 cluster_finding rows={r['n']} distinct prompts={r['prompts']}")
    assert r["n"] >= 189 and r["prompts"] == 189, "P1/P2 failed"
    log(f"     ({r['n']} rows, all 189 prompts covered) ✓")

    # B1 — BOUNDARY exit needed
    bnd = conn.execute("""
        SELECT mt.id, mt.strongs_number, mt.transliteration, mt.owning_registry_fk,
               wr.no AS reg_no, wr.word AS reg_word
        FROM mti_term_subgroup mts
        JOIN mti_terms mt ON mt.id = mts.mti_term_id
        LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
        WHERE mts.cluster_subgroup_id=? AND COALESCE(mts.delete_flagged,0)=0
          AND COALESCE(mt.delete_flagged,0)=0
          AND mts.placement_note LIKE '%[primary]%'
        ORDER BY mt.strongs_number
    """, (BOUNDARY_SG_ID,)).fetchall()
    log(f"  B1 BOUNDARY terms: {len(bnd)} (will flag for researcher decision)")
    return {"boundary_terms": [dict(b) for b in bnd]}


def apply(conn, dry_run: bool, boundary_terms: list[dict]) -> dict:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Op A — BOUNDARY exit (flagged-for-decision)
    log(f"\n{'='*60}")
    log(f"Op A — BOUNDARY exit via flagged-for-decision")
    log(f"{'='*60}")
    log(f"  Flagging {len(boundary_terms)} BOUNDARY terms with BOUNDARY_DECISION_PENDING")
    a_count = 0
    for b in boundary_terms:
        flag_label = f"M02-BOUNDARY-{b['strongs_number']}"
        description = (
            f"M02 closure (DIR-20260516-014): BOUNDARY term {b['strongs_number']} "
            f"({b['transliteration']}) reached closure without exit decision. "
            f"Phase 9 per-term structural characterisation in part4 "
            f"({PART4_FILE}) under marker [BOUNDARY — {b['strongs_number']} "
            f"{b['transliteration']}]. Pending researcher disposition: set-aside / "
            f"promote-to-M02-subgroup / reassign-to-other-cluster / retain-BOUNDARY-with-extended-rationale. "
            f"Source registry: R{b['reg_no']} ({b['reg_word']})."
        )
        if not dry_run:
            conn.execute("""
                INSERT INTO wa_session_research_flags
                    (registry_id, flag_code, flag_label, strongs_reference, priority,
                     session_target, description, session_raised, raised_date, resolved)
                VALUES (?, 'BOUNDARY_DECISION_PENDING', ?, ?, 'MEDIUM', 'Researcher',
                        ?, 'B', ?, 0)
            """, (b["owning_registry_fk"], flag_label, b["strongs_number"], description, today))
        a_count += 1
    log(f"  INSERTed {a_count} BOUNDARY_DECISION_PENDING flags")

    # Op B — status transition
    log(f"\n{'='*60}")
    log(f"Op B — Cluster status transition")
    log(f"{'='*60}")
    if not dry_run:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        conn.execute("""
            UPDATE cluster
            SET status='Analysis Completed', last_updated_date=?
            WHERE cluster_code=? AND status='Analysis - In Progress'
        """, (ts, CLUSTER))
        log(f"  UPDATEd cluster.status: 'Analysis - In Progress' → 'Analysis Completed'")
    else:
        log(f"  (dry-run) Would UPDATE cluster.status → 'Analysis Completed'")

    return {"boundary_flags_inserted": a_count}


def healthcheck(conn) -> None:
    log(f"\n{'='*60}")
    log(f"Post-closure health checks")
    log(f"{'='*60}")
    r = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)).fetchone()
    log(f"  Z1 cluster.status: {r['status']} ({'✓' if r['status']=='Analysis Completed' else '✗'})")
    assert r["status"] == "Analysis Completed"

    r = conn.execute("""
        SELECT COUNT(*) AS n FROM wa_session_research_flags
        WHERE flag_code='BOUNDARY_DECISION_PENDING' AND resolved=0
          AND description LIKE '%M02 closure (DIR-20260516-014)%'
    """).fetchone()
    log(f"  Z2 BOUNDARY_DECISION_PENDING flags raised by this directive: {r['n']}")
    assert r["n"] == 6

    # Health summary
    r = conn.execute("""
        SELECT COUNT(*) AS n_active_terms FROM mti_terms
        WHERE cluster_code='M02' AND status IN ('extracted','extracted_thin')
          AND COALESCE(delete_flagged,0)=0
    """).fetchone()
    log(f"  Active terms: {r['n_active_terms']}")
    r = conn.execute("""
        SELECT COUNT(DISTINCT vcg.id) AS n_vcgs FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code='M02' AND COALESCE(vcg.delete_flagged,0)=0
          AND COALESCE(vt.delete_flagged,0)=0
    """).fetchone()
    log(f"  Active VCGs: {r['n_vcgs']}")
    r = conn.execute("""
        SELECT COUNT(*) AS n FROM cluster_finding
        WHERE cluster_code='M02' AND version='v1-20260516'
    """).fetchone()
    log(f"  cluster_finding rows: {r['n']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    dry_run = not args.live

    log(f"Phase 12 closure — cluster={CLUSTER} directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    if not dry_run:
        backup_path = backup_db()
        log(f"Backup: {backup_path.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        conn.execute("BEGIN")
        pre = precheck(conn)
        result = apply(conn, dry_run=dry_run, boundary_terms=pre["boundary_terms"])
        if dry_run:
            log("\nDRY-RUN — rolling back")
            conn.execute("ROLLBACK")
        else:
            log("\nCommitting...")
            conn.execute("COMMIT")
            healthcheck(conn)
        log(f"\nDONE — {'simulated' if dry_run else 'applied'}: boundary flags={result['boundary_flags_inserted']}")
    except Exception as e:
        log(f"ERROR: {e}")
        try: conn.execute("ROLLBACK")
        except: pass
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
