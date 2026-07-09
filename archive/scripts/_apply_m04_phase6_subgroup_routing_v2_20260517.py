"""Apply M04 Phase 6 (v2) — sub-group creation, placement, verse routing.

Phase 5 v2 (after distribution gate v1 rejection) per WA-M04-subgroup-design-v2-20260517.md
+ WA-M04-subgroup-mapping-v2-20260517.json. v2 passes §8.6 distribution gate cleanly
(biggest SG 33.5%, ratio 1.9×; no multi-primary, no mapping mismatch, no missing terms).

  Op A: INSERT 11 cluster_subgroup rows (M04-A..M04-J + M04-BOUNDARY)
  Op B: INSERT mti_term_subgroup rows (one per (term, sub-group) placement)
  Op C: UPDATE verse_context.cluster_subgroup_id from verse_assignments_by_term

Directive: DIR-20260517-007
Supersedes: DIR-20260517-005 (Phase 6 v1, rolled back via DIR-20260517-006)
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
    REPO / "Sessions" / "Session_Clusters" / "M04"
         / "files phase 5" / "WA-M04-subgroup-mapping-v2-20260517.json"
)
DIRECTIVE = "DIR-20260517-007"
CLUSTER = "M04"
EXPECTED_SUBGROUPS = 11  # M04-A..M04-J (10 substantive) + M04-BOUNDARY


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
    log(f"  DB {CLUSTER} terms: {len(db_term_ids)} · mapped: {len(map_term_ids)}")
    if missing: raise RuntimeError(f"DB terms not in mapping: {sorted(missing)}")
    if extra: raise RuntimeError(f"Mapping has unknown terms: {sorted(extra)}")
    log(f"  term coverage 1:1 ✓")

    r = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_subgroup WHERE cluster_code=? "
        "AND COALESCE(delete_flagged,0)=0", (CLUSTER,)
    ).fetchone()
    if r["n"] != 0:
        raise RuntimeError(f"{CLUSTER} already has {r['n']} active sub-groups; aborting")
    log(f"  no pre-existing active {CLUSTER} sub-groups (post-rollback) ✓")

    sg_count = len(design["subgroups"])
    if sg_count != EXPECTED_SUBGROUPS:
        raise RuntimeError(f"Expected {EXPECTED_SUBGROUPS} sub-groups; got {sg_count}")
    codes = {sg["subgroup_code"] for sg in design["subgroups"]}
    expected_codes = {f"M04-{c}" for c in ("A","B","C","D","E","F","G","H","I","J","BOUNDARY")}
    if codes != expected_codes:
        raise RuntimeError(
            f"Sub-group codes mismatch. Got {sorted(codes)}; expected {sorted(expected_codes)}"
        )
    log(f"  sub-group codes ✓ ({sg_count} total)")

    r = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND vc.is_relevant=1
          AND COALESCE(vc.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()
    log(f"  Active is_relevant vc rows to route: {r['n']}")
    return {"pre_vc_count": r["n"]}


def apply(conn, design: dict, dry_run: bool) -> dict:
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    log(f"\n{'='*60}\nOp A — INSERT cluster_subgroup rows\n{'='*60}")
    sg_code_to_id = {}
    for sg in design["subgroups"]:
        log(f"  {sg['subgroup_code']:<14} {sg.get('label','')[:60]}")
        if not dry_run:
            cur = conn.execute("""
                INSERT INTO cluster_subgroup
                    (cluster_code, subgroup_code, label, core_description, sort_order,
                     status, version, source, created_at, last_updated_date)
                VALUES (?, ?, ?, ?, ?, 'active', 'v2', ?, ?, ?)
            """, (CLUSTER, sg["subgroup_code"], sg.get("label",""),
                  sg.get("core_description",""), sg.get("sort_order"),
                  DIRECTIVE, now_iso, now_iso))
            sg_code_to_id[sg["subgroup_code"]] = cur.lastrowid
        else:
            sg_code_to_id[sg["subgroup_code"]] = -1
    if not dry_run:
        log(f"  INSERTed {len(sg_code_to_id)} cluster_subgroup rows")

    log(f"\n{'='*60}\nOp B — INSERT mti_term_subgroup rows\n{'='*60}")
    # Dedup (mti, sg) pairs: if AI listed a term twice within the same sub-group
    # (e.g. primary AND secondary), keep the strongest placement (boundary > primary > secondary).
    placement_strength = {"boundary": 3, "primary": 2, "secondary": 1}
    seen: dict[tuple[int, int], tuple[str, str]] = {}
    for sg in design["subgroups"]:
        sg_id = sg_code_to_id[sg["subgroup_code"]]
        for tp in sg.get("term_placements", []):
            mti_id = tp["mti_term_id"]
            placement = tp.get("placement", "primary")
            note = (
                f"{DIRECTIVE} [{placement}]: "
                f"per AI WA-M04-subgroup-design-v2-20260517.md"
            )
            key = (mti_id, sg_id)
            if key in seen:
                existing_plc = seen[key][0]
                if placement_strength.get(placement, 0) > placement_strength.get(existing_plc, 0):
                    seen[key] = (placement, note)
                    log(f"  DEDUP: mti={mti_id} sg={sg['subgroup_code']}: upgraded {existing_plc} → {placement}")
                else:
                    log(f"  DEDUP: mti={mti_id} sg={sg['subgroup_code']}: kept {existing_plc} over {placement}")
            else:
                seen[key] = (placement, note)
    placement_rows = [(mti, sgid, note) for (mti, sgid), (plc, note) in seen.items()]
    log(f"  Rows to insert: {len(placement_rows)}")
    primary_count   = sum(1 for _,_,n in placement_rows if "[primary]"   in n)
    secondary_count = sum(1 for _,_,n in placement_rows if "[secondary]" in n)
    boundary_count  = sum(1 for _,_,n in placement_rows if "[boundary]"  in n)
    log(f"  Primary: {primary_count} · Secondary: {secondary_count} · Boundary: {boundary_count}")
    if not dry_run:
        for mti_id, sg_id, note in placement_rows:
            conn.execute("""
                INSERT INTO mti_term_subgroup
                    (mti_term_id, cluster_subgroup_id, placement_note,
                     created_at, last_updated_date)
                VALUES (?, ?, ?, ?, ?)
            """, (mti_id, sg_id, note, now_iso, now_iso))

    log(f"\n{'='*60}\nOp C — UPDATE verse_context.cluster_subgroup_id\n{'='*60}")
    mapping = design["verse_assignments_by_term"]["mti_term_id_to_subgroup"]
    total_updated = 0
    per_sg = {}
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
    }


def healthcheck(conn, expected_vc: int) -> None:
    log(f"\n{'='*60}\nHealth checks\n{'='*60}")
    r = conn.execute("""
        SELECT COUNT(*) AS n FROM cluster_subgroup
        WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()
    log(f"  H1 active sub-groups: {r['n']} (expected {EXPECTED_SUBGROUPS}) "
        f"{'✓' if r['n']==EXPECTED_SUBGROUPS else '✗'}")
    assert r["n"] == EXPECTED_SUBGROUPS

    r = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
          AND vc.is_relevant=1 AND vc.cluster_subgroup_id IS NULL
    """, (CLUSTER,)).fetchone()
    log(f"  H2 unrouted is_relevant vc: {r['n']} {'✓' if r['n']==0 else '✗'}")
    assert r["n"] == 0

    r = conn.execute("""
        SELECT COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
          AND vc.is_relevant=1 AND vc.cluster_subgroup_id IS NOT NULL
    """, (CLUSTER,)).fetchone()
    log(f"  H3 routed is_relevant vc: {r['n']} (expected {expected_vc}) "
        f"{'✓' if r['n']==expected_vc else '✗'}")
    assert r["n"] == expected_vc

    r = conn.execute("""
        SELECT cs.subgroup_code, COUNT(*) AS n FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        WHERE mt.cluster_code=? AND vc.is_relevant=1
          AND COALESCE(vc.delete_flagged,0)=0
        GROUP BY cs.subgroup_code ORDER BY cs.subgroup_code
    """, (CLUSTER,)).fetchall()
    log(f"  H4 verse routing distribution:")
    for row in r:
        log(f"    {row['subgroup_code']}: {row['n']}")

    r = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)).fetchone()
    log(f"  H5 cluster.status: {r['status']} "
        f"({'✓' if r['status']=='Analysis - In Progress' else '✗'})")
    assert r["status"] == "Analysis - In Progress"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    dry_run = not args.live

    log(f"Phase 6 v2 sub-group routing — cluster={CLUSTER} directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")
    log(f"Mapping JSON: {MAPPING_JSON.relative_to(REPO)}")

    design = json.loads(MAPPING_JSON.read_text(encoding="utf-8"))

    if not dry_run:
        backup_path = backup_db()
        log(f"Backup: {backup_path.relative_to(REPO)}")

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
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
