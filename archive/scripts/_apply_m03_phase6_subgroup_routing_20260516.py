"""Apply M03 Phase 6 — sub-group creation, term-to-sub-group placement, verse routing.

Implements AI's WA-M03-subgroup-design-v1-20260516.md + WA-M03-subgroup-mapping-v1-20260516.json
mechanically per v2_2 §9:
  Op A: INSERT 8 cluster_subgroup rows (M03-A..M03-G + M03-BOUNDARY)
  Op B: INSERT mti_term_subgroup rows (one per (term, sub-group) placement;
        primary + secondary + boundary)
  Op C: UPDATE verse_context.cluster_subgroup_id mechanically from each term's
        primary (or boundary) sub-group via verse_assignments_by_term mapping

cluster.status stays at 'Analysis - In Progress' (already flipped at Phase 4; no Op D).

Notes on AI's Phase 5 output:
  - mti_id 898 (a.na.qah, H0603) has NO primary placement; appears only as
    secondary in M03-A and M03-E. The mapping routes verses to M03-A —
    Op C honours that routing without injecting a synthetic primary placement.
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
MAPPING_JSON = (
    REPO / "Sessions" / "Session_Clusters" / "M03"
         / "files phase 5" / "WA-M03-subgroup-mapping-v1-20260516.json"
)
DIRECTIVE = "DIR-20260516-016"
CLUSTER = "M03"
EXPECTED_SUBGROUPS = 8


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%SZ')}] {msg}")


def backup_db() -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    name = f"bible_research_backup_{ts}_{DIRECTIVE}.db"
    out = REPO / "backups" / name
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(DB, out)
    return out


def precheck(conn, design: dict) -> dict:
    log("Pre-flight checks...")

    cluster = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    if not cluster or cluster["status"] != "Analysis - In Progress":
        raise RuntimeError(
            f"cluster.status expected 'Analysis - In Progress', "
            f"got {cluster and cluster['status']!r}"
        )
    log(f"  cluster.status = {cluster['status']} ✓")

    mapping = design["verse_assignments_by_term"]["mti_term_id_to_subgroup"]
    map_term_ids = set(int(k) for k in mapping.keys())
    db_term_ids = {
        r[0] for r in conn.execute("""
            SELECT id FROM mti_terms WHERE cluster_code=?
              AND status IN ('extracted','extracted_thin')
              AND COALESCE(delete_flagged,0)=0
        """, (CLUSTER,))
    }
    missing = db_term_ids - map_term_ids
    extra = map_term_ids - db_term_ids
    log(f"  DB M03 terms: {len(db_term_ids)} · mapped: {len(map_term_ids)}")
    if missing: raise RuntimeError(f"DB terms not in mapping: {sorted(missing)}")
    if extra: raise RuntimeError(f"Mapping has unknown terms: {sorted(extra)}")
    log(f"  term coverage 1:1 ✓")

    # No pre-existing M03 sub-groups
    r = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_subgroup WHERE cluster_code=? "
        "AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchone()
    if r["n"] != 0:
        raise RuntimeError(f"M03 already has {r['n']} active sub-groups; aborting")
    log(f"  no pre-existing active M03 sub-groups ✓")

    # Sub-group count sanity
    sg_count = len(design["subgroups"])
    if sg_count != EXPECTED_SUBGROUPS:
        raise RuntimeError(
            f"Expected {EXPECTED_SUBGROUPS} sub-groups in design; got {sg_count}"
        )
    codes = {sg["subgroup_code"] for sg in design["subgroups"]}
    expected_codes = {f"M03-{c}" for c in ("A","B","C","D","E","F","G","BOUNDARY")}
    if codes != expected_codes:
        raise RuntimeError(
            f"Sub-group codes mismatch. Got {sorted(codes)}; expected {sorted(expected_codes)}"
        )
    log(f"  sub-group codes ✓ ({sg_count} total)")

    # Pre-state vc count
    r = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND vc.is_relevant=1
          AND COALESCE(vc.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()
    log(f"  Active is_relevant vc rows to route: {r['n']}")

    return {"mapping": mapping, "pre_vc_count": r["n"]}


def apply(conn, design: dict, dry_run: bool) -> dict:
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # ---- Op A — INSERT cluster_subgroup rows ----
    log(f"\n{'='*60}")
    log(f"Op A — INSERT cluster_subgroup rows")
    log(f"{'='*60}")
    subgroups = design["subgroups"]
    sg_code_to_id: dict[str, int] = {}
    for sg in subgroups:
        log(f"  {sg['subgroup_code']:<14} {sg.get('label','')[:60]}")
        if not dry_run:
            cur = conn.execute("""
                INSERT INTO cluster_subgroup
                    (cluster_code, subgroup_code, label, core_description, sort_order,
                     status, version, source, created_at, last_updated_date)
                VALUES (?, ?, ?, ?, ?, 'active', 'v1', ?, ?, ?)
            """, (CLUSTER, sg["subgroup_code"], sg.get("label",""),
                  sg.get("core_description",""), sg.get("sort_order"),
                  DIRECTIVE, now_iso, now_iso))
            sg_code_to_id[sg["subgroup_code"]] = cur.lastrowid
        else:
            sg_code_to_id[sg["subgroup_code"]] = -1
    if not dry_run:
        log(f"  INSERTed {len(sg_code_to_id)} cluster_subgroup rows")

    # ---- Op B — INSERT mti_term_subgroup rows ----
    log(f"\n{'='*60}")
    log(f"Op B — INSERT mti_term_subgroup rows")
    log(f"{'='*60}")
    placement_rows: list[tuple[int, int, str]] = []
    for sg in subgroups:
        sg_id = sg_code_to_id[sg["subgroup_code"]]
        for tp in sg.get("term_placements", []):
            mti_id = tp["mti_term_id"]
            placement = tp.get("placement", "primary")
            placement_note = (
                f"{DIRECTIVE} [{placement}]: "
                f"per AI WA-M03-subgroup-design-v1-20260516.md"
            )
            placement_rows.append((mti_id, sg_id, placement_note))

    log(f"  Rows to insert: {len(placement_rows)}")
    primary_count   = sum(1 for _,_,n in placement_rows if "[primary]"   in n)
    secondary_count = sum(1 for _,_,n in placement_rows if "[secondary]" in n)
    boundary_count  = sum(1 for _,_,n in placement_rows if "[boundary]"  in n)
    log(f"  Primary: {primary_count} · Secondary: {secondary_count} "
        f"· Boundary: {boundary_count}")
    if not dry_run:
        for mti_id, sg_id, note in placement_rows:
            conn.execute("""
                INSERT INTO mti_term_subgroup
                    (mti_term_id, cluster_subgroup_id, placement_note,
                     created_at, last_updated_date)
                VALUES (?, ?, ?, ?, ?)
            """, (mti_id, sg_id, note, now_iso, now_iso))

    # ---- Op C — UPDATE verse_context.cluster_subgroup_id ----
    log(f"\n{'='*60}")
    log(f"Op C — UPDATE verse_context.cluster_subgroup_id (verse routing)")
    log(f"{'='*60}")
    mapping = design["verse_assignments_by_term"]["mti_term_id_to_subgroup"]
    total_updated = 0
    per_sg: dict[str, int] = {}
    for mti_id_str, sg_code in mapping.items():
        mti_id = int(mti_id_str)
        sg_id = sg_code_to_id[sg_code]
        r = conn.execute("""
            SELECT COUNT(*) AS n FROM verse_context
            WHERE mti_term_id=? AND is_relevant=1
              AND COALESCE(delete_flagged,0)=0
        """, (mti_id,)).fetchone()
        n = r["n"]
        per_sg[sg_code] = per_sg.get(sg_code, 0) + n
        total_updated += n
        if not dry_run and n > 0:
            conn.execute("""
                UPDATE verse_context
                SET cluster_subgroup_id=?
                WHERE mti_term_id=? AND is_relevant=1
                  AND COALESCE(delete_flagged,0)=0
            """, (sg_id, mti_id))

    log(f"  Verses to route: {total_updated}")
    for sg_code, n in sorted(per_sg.items()):
        log(f"    {sg_code}: {n}")

    return {
        "subgroups_inserted": len(sg_code_to_id),
        "term_placements_inserted": len(placement_rows),
        "primary_placements": primary_count,
        "secondary_placements": secondary_count,
        "boundary_placements": boundary_count,
        "verses_routed": total_updated,
        "per_subgroup_verse_counts": per_sg,
    }


def healthcheck(conn, expected_vc: int) -> None:
    log(f"\n{'='*60}")
    log(f"Health checks")
    log(f"{'='*60}")

    r = conn.execute("""
        SELECT COUNT(*) AS n FROM cluster_subgroup
        WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()
    log(f"  H1 active M03 sub-groups: {r['n']} "
        f"(expected {EXPECTED_SUBGROUPS}) "
        f"{'✓' if r['n']==EXPECTED_SUBGROUPS else '✗'}")
    assert r["n"] == EXPECTED_SUBGROUPS

    r = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
          AND vc.is_relevant=1 AND vc.cluster_subgroup_id IS NULL
    """, (CLUSTER,)).fetchone()
    log(f"  H2 is_relevant verses without cluster_subgroup_id: {r['n']} "
        f"{'✓' if r['n']==0 else '✗'}")
    assert r["n"] == 0

    r = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
          AND vc.is_relevant=1 AND vc.cluster_subgroup_id IS NOT NULL
    """, (CLUSTER,)).fetchone()
    log(f"  H3 is_relevant verses routed: {r['n']} (expected {expected_vc}) "
        f"{'✓' if r['n']==expected_vc else '✗'}")
    assert r["n"] == expected_vc

    r = conn.execute("""
        SELECT COUNT(*) AS n FROM mti_term_subgroup mts
        JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
        WHERE cs.cluster_code=? AND COALESCE(mts.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()
    log(f"  H4 active mti_term_subgroup placements: {r['n']}")

    # H5: every BOUNDARY-routed verse points to M03-BOUNDARY sub-group
    r = conn.execute("""
        SELECT cs.subgroup_code, COUNT(*) AS n
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        WHERE mt.cluster_code=? AND vc.is_relevant=1
          AND COALESCE(vc.delete_flagged,0)=0
        GROUP BY cs.subgroup_code
        ORDER BY cs.subgroup_code
    """, (CLUSTER,)).fetchall()
    log(f"  H5 verse routing distribution:")
    for row in r:
        log(f"    {row['subgroup_code']}: {row['n']}")

    r = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)).fetchone()
    log(f"  H6 cluster.status: {r['status']} "
        f"{'✓' if r['status']=='Analysis - In Progress' else '✗'}")
    assert r["status"] == "Analysis - In Progress"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    dry_run = not args.live

    log(f"Phase 6 sub-group routing — cluster={CLUSTER} directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")
    log(f"Mapping JSON: {MAPPING_JSON.relative_to(REPO)}")

    design = json.loads(MAPPING_JSON.read_text(encoding="utf-8"))

    if not dry_run:
        backup_path = backup_db()
        log(f"Backup: {backup_path.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        conn.execute("BEGIN")
        pre = precheck(conn, design)
        result = apply(conn, design, dry_run=dry_run)
        if dry_run:
            log("\nDRY-RUN — rolling back")
            conn.execute("ROLLBACK")
        else:
            log("\nCommitting...")
            conn.execute("COMMIT")
            healthcheck(conn, expected_vc=pre["pre_vc_count"])
        log(f"\nDONE — {'simulated' if dry_run else 'applied'}: "
            f"sub-groups={result['subgroups_inserted']} "
            f"term_placements={result['term_placements_inserted']} "
            f"(primary={result['primary_placements']} "
            f"secondary={result['secondary_placements']} "
            f"boundary={result['boundary_placements']}) "
            f"verses_routed={result['verses_routed']}")
    except Exception as e:
        log(f"ERROR: {e}")
        try: conn.execute("ROLLBACK")
        except: pass
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
