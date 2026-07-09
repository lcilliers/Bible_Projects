"""Apply Phase 4 — M04 term transfers + status transition.

Directive: wa-cluster-M04-dir-001-term-transfer-v1-20260517 (DIR-20260517-004)
Governing: wa-sessionb-cluster-instruction-v2_2-20260516 §7

Operations (single transaction):
  Op A — UPDATE mti_terms.cluster_code for 5 transferred terms
  Op N — UPDATE cluster.status for M04: Data - In Progress → Analysis - In Progress

BOUNDARY terms (15) recorded in directive; no DB write at Phase 4 (per §7.4).

Source: AI's Phase 3 debate
  Sessions/Session_Clusters/M04/files phase 3/wa-cluster-M04-debate-v1-20260517.md
  Cross-routing flags: WA-M04-phase3-cross-routing-flags-v1-20260517.md
  Obslog: wa-obslog-M04-phase3-debate-v1-20260517.md

Verdict tally (63 total):
  STAYS:                                 43
  TRANSFERS:                              5
  BOUNDARY:                              15
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
DIRECTIVE = "DIR-20260517-004"
SOURCE_CLUSTER = "M04"

# 5 transfers per AI's Phase 3 debate
TRANSFERS = [
    # (mti_id, strongs, translit, dest_cluster, dest_name, rationale)
    (3090, "G2237", "hēdonē",     "M28", "Envy",
     "Pleasure as enslaving self-seeking sensual drive; pleasures at war within. "
     "Holding route — review when M29 Desire activates (per cross-routing flag 1)."),
    ( 601, "G2292", "tharseō",    "M23", "Strength",
     "Take-heart as courage-cheer; inner-strength register more than joy."),
    ( 763, "G2293", "tharseō",    "M23", "Strength",
     "Take-heart as courage-cheer; same register as G2292 (separate mti_id, R033 courage origin)."),
    ( 100, "H1361", "ga.vah",     "M08", "Pride",
     "Exult-up corpus dominantly pride-elevation register (heart-lifted-up in pride)."),
    (2594, "H4774", "mar.ge.ah",  "M33", "Peace",
     "Repose / resting-place register; quietness-of-soul rather than active joy."),
]

# 15 BOUNDARY designations from AI Phase 3 debate
BOUNDARY_TERMS = [
    # (mti_id, strongs, translit, source_registry_note, rationale_snippet)
    ( 500, "G0701",  "arestos",     "R042 delight",     "Pleasing register — to please/be pleasing; verb register more than inner-pleasure"),
    ( 891, "G2169",  "eucharistia", "R069 gratitude",   "Thanksgiving register — joy-toned vs ritual mixed; researcher decision at P12"),
    (5481, "G2170",  "eucharistos", "R069 gratitude",   "Thankful — register split same as G2169"),
    (5124, "G2284",  "thambeō",     "R051 distress",    "Astonish — wonder mixed with shock/fear; mixed register"),
    (1247, "G2295",  "thauma",      "R175 wonder",      "Marvel — descriptive of marvellous event vs inner-being marvelling"),
    (1246, "G2296",  "thaumazō",    "R175 wonder",      "To marvel — same descriptive vs inner-being split as G2295"),
    (1300, "G3108",  "makarismos",  "R194 blessing",    "Blessedness — blessed-as-state register; may go to M39 Blessing"),
    ( 457, "H2531",  "che.med",     "R042 delight",     "Desire/delight — register split (M28 Envy or M04)"),
    ( 884, "H2896A", "tov",         "R067 goodness",    "230 verses; 4 sub-registers (creation-assessment / inner-delight / "
                                                        "wellbeing / moral-quality / volitional-deference / property). "
                                                        "Researcher decision at P12 with sub-register map (cross-routing flag 4)."),
    (2584, "H5207",  "ni.cho.ach",  "R117 peace",       "Soothing/pleasing aroma — 40+ priestly formula instances; may go to M21 Prayer"),
    (1096, "H5951",  "a.li.tsut",   "R132 rejoicing",   "Single-verse predatory exultation (Hab 3:14) — M06 Hate adjacent"),
    ( 797, "H5965",  "a.las",       "R042 delight",     "Rejoice register — mixed; researcher decision"),
    (3843, "H6028",  "a.nog",       "R042 delight",     "Dainty/refinement luxury register — may go to M46 Abundance"),
    (1731, "H8540",  "te.mah",      "R061 fear",        "Aramaic wonder — empty active corpus (all 3 verses set-aside at P1)"),
    ( 792, "H8588",  "ta.a.nug",    "R042 delight",     "Luxury / refined ease register — may go to M46 Abundance (cross-routing flag 7)"),
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
        raise RuntimeError(
            f"cluster.status expected 'Data - In Progress', "
            f"got {cluster and cluster['status']!r}"
        )
    log(f"  cluster.status {SOURCE_CLUSTER} = {cluster['status']} ✓")

    for _, _, _, dest, _, _ in TRANSFERS:
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

    for mti_id, strongs, _, _, _, _ in TRANSFERS:
        r = conn.execute("""
            SELECT cluster_code, status FROM mti_terms
            WHERE id=? AND COALESCE(delete_flagged,0)=0
        """, (mti_id,)).fetchone()
        if not r:
            raise RuntimeError(f"mti_id={mti_id} ({strongs}) not found / soft-deleted")
        if r["cluster_code"] != SOURCE_CLUSTER:
            raise RuntimeError(
                f"mti_id={mti_id} ({strongs}) cluster_code is "
                f"{r['cluster_code']!r}, expected {SOURCE_CLUSTER}"
            )
        if r["status"] not in ("extracted", "extracted_thin"):
            raise RuntimeError(
                f"mti_id={mti_id} ({strongs}) status is {r['status']!r}, "
                f"expected extracted/extracted_thin"
            )
    log(f"  all {len(TRANSFERS)} transferred terms present in {SOURCE_CLUSTER} "
        f"with valid status ✓")

    for mti_id, strongs, _, _, _ in BOUNDARY_TERMS:
        r = conn.execute("""
            SELECT cluster_code FROM mti_terms WHERE id=? AND COALESCE(delete_flagged,0)=0
        """, (mti_id,)).fetchone()
        if not r:
            raise RuntimeError(f"BOUNDARY mti_id={mti_id} ({strongs}) not found")
        if r["cluster_code"] != SOURCE_CLUSTER:
            raise RuntimeError(
                f"BOUNDARY mti_id={mti_id} ({strongs}) cluster_code is "
                f"{r['cluster_code']!r}, expected {SOURCE_CLUSTER}"
            )
    log(f"  all {len(BOUNDARY_TERMS)} BOUNDARY terms present in {SOURCE_CLUSTER} ✓")

    return {"pre_counts": pre_counts}


def apply(conn, dry_run: bool) -> dict:
    log(f"\n{'='*60}")
    log(f"Op A — UPDATE mti_terms.cluster_code ({len(TRANSFERS)} term transfers)")
    log(f"{'='*60}")
    for mti_id, strongs, translit, dest, dest_name, _ in TRANSFERS:
        log(f"  mti={mti_id} {strongs} {translit} → {dest} ({dest_name})")
        if not dry_run:
            conn.execute(
                "UPDATE mti_terms SET cluster_code=?, last_changed=? WHERE id=?",
                (dest, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), mti_id)
            )

    log(f"\n{'='*60}")
    log(f"Op N — UPDATE cluster.status for {SOURCE_CLUSTER}")
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
    expected_post_M04 = 63 - len(TRANSFERS)  # 58
    r = conn.execute("""
        SELECT COUNT(*) AS n FROM mti_terms
        WHERE cluster_code=? AND status IN ('extracted','extracted_thin')
          AND COALESCE(delete_flagged,0)=0
    """, (SOURCE_CLUSTER,)).fetchone()
    log(f"  Source {SOURCE_CLUSTER} active terms: {r['n']} (expected {expected_post_M04})")
    assert r["n"] == expected_post_M04

    transferred_ids = [t[0] for t in TRANSFERS]
    placeholders = ",".join("?" * len(transferred_ids))
    by_dest = {}
    for r in conn.execute(
        f"SELECT cluster_code, COUNT(*) AS n FROM mti_terms "
        f"WHERE id IN ({placeholders}) GROUP BY cluster_code",
        transferred_ids
    ):
        by_dest[r["cluster_code"]] = r["n"]
    log(f"  Transferred terms by destination: {by_dest}")

    expected_dest = {}
    for _, _, _, dest, _, _ in TRANSFERS:
        expected_dest[dest] = expected_dest.get(dest, 0) + 1
    for dest, expected_n in expected_dest.items():
        actual = by_dest.get(dest, 0)
        assert actual == expected_n, f"destination {dest} expected {expected_n}, got {actual}"

    r = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (SOURCE_CLUSTER,)
    ).fetchone()
    log(f"  cluster.status {SOURCE_CLUSTER}: {r['status']} "
        f"({'✓' if r['status']=='Analysis - In Progress' else '✗'})")
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
            f"transferred={result['transferred']}, BOUNDARY recorded={len(BOUNDARY_TERMS)}")
    except Exception as e:
        log(f"ERROR: {e}")
        try: conn.execute("ROLLBACK")
        except: pass
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
