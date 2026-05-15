"""Apply WA-M46-subgroup-restructure-v1-20260514.

Stage 1 of 2 in the M46 verse-reading-driven restructure.

Operations (single transaction):
  1. UPDATE M46-A/B/C: new label + new core_description (3 RENAME_UPDATE)
  2. INSERT M46-D: new sub-group
  3. Soft-delete all existing M46 mti_term_subgroup rows (collapsing the prior
     multi-placement model from the directive-subgroups-v1 pass)
  4. INSERT 21 new mti_term_subgroup rows (one per term — primary placement)
  5. Set is_anchor=1 on the 4 sub-group anchor verses
  6. R4 satisfaction check: every M46 term with relevant verses has ≥1 anchor

Flagged: G3045 liparos (mti=4702) is not in the restructure spec; no placement.
"""
from __future__ import annotations
import argparse, json, os, shutil, sqlite3, sys
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = "database/bible_research.db"
BACKUP_DIR = "backups"
CLUSTER = "M46"
DIRECTIVE_ID = "DIR-20260514-M46-restructure"
INPUT_JSON = "Sessions/Session_Clusters/M46/WA-M46-subgroup-restructure-v1-20260514.json"

ANCHOR_VERSE_PATTERNS = {
    "M46-A": ("Rev 3:17",   7577),  # G4145 plousios
    "M46-B": ("Luk 16:19",  7577),  # G4145 plousios (range Luk 16:19-21; pick 16:19)
    "M46-C": ("Pro 13:4",   111),   # H1878 da.shen
    "M46-D": ("2Cor 8:9",   7582),  # G4433 ptōcheuō
}


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        spec = json.load(f)

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    ts = now_iso()

    print("=" * 72)
    print(f"  M46 SUBGROUP_RESTRUCTURE — stage 1 of 2")
    print(f"  Mode: {'LIVE' if args.live else 'DRY-RUN'}")
    print("=" * 72)

    # ── PRE-FLIGHT ────────────────────────────────────────────────────────
    print("\nPRE-FLIGHT")
    print("-" * 72)
    ok = True

    cluster_row = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    print(f"  cluster.status: {cluster_row['status']!r}")
    if cluster_row["status"] != "Analysis - In Progress":
        print(f"  ⚠ expected 'Analysis - In Progress' — restructure proceeds anyway")

    # Existing sub-groups
    existing_sgs = list(conn.execute(
        "SELECT id, subgroup_code, label FROM cluster_subgroup "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 ORDER BY sort_order",
        (CLUSTER,)
    ))
    print(f"  Existing sub-groups: {[(r['subgroup_code'], r['label']) for r in existing_sgs]}")
    existing_sg_codes = {r["subgroup_code"]: r["id"] for r in existing_sgs}

    # Check expected codes
    for expected in ("M46-A", "M46-B", "M46-C"):
        if expected not in existing_sg_codes:
            print(f"  ✗ expected sub-group {expected} not found"); ok = False
    if "M46-D" in existing_sg_codes:
        print(f"  ✗ M46-D already exists — restructure assumes it's new"); ok = False

    # Existing mti_term_subgroup count for M46
    n_existing_pl = conn.execute("""
        SELECT COUNT(*) FROM mti_term_subgroup mts
          JOIN mti_terms mt ON mt.id=mts.mti_term_id
         WHERE mt.cluster_code=? AND COALESCE(mts.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()[0]
    print(f"  Existing M46 mti_term_subgroup rows: {n_existing_pl} (will be soft-deleted)")

    # Validate each term in assignments
    assignments = spec["term_subgroup_reassignments"]["assignments"]
    seen_mti = set()
    plan_assignments = []
    for a in assignments:
        mti = a["mti_id"]
        if mti in seen_mti:
            # duplicate entry (e.g. sha.a.nan 413-002 routing note) — skip
            continue
        seen_mti.add(mti)
        r = conn.execute(
            "SELECT id, strongs_number, cluster_code FROM mti_terms WHERE id=?", (mti,)
        ).fetchone()
        if not r or r["cluster_code"] != CLUSTER:
            print(f"  ✗ mti={mti} not in M46"); ok = False; continue
        plan_assignments.append((mti, r["strongs_number"], a["primary"], a.get("rationale", "")))

    print(f"  Unique term primary assignments: {len(plan_assignments)}")

    # Flag missing M46 active terms
    m46_active = list(conn.execute(
        "SELECT id, strongs_number, transliteration FROM mti_terms "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)
    ))
    missing = [t for t in m46_active if t["id"] not in seen_mti]
    if missing:
        print(f"\n  ⚠ {len(missing)} active M46 term(s) not in restructure (no placement):")
        for t in missing:
            print(f"      mti={t['id']} {t['strongs_number']} '{t['transliteration']}'")

    # Resolve anchor vc_ids
    anchor_vc_ids = {}
    for sg_code, (ref, mti) in ANCHOR_VERSE_PATTERNS.items():
        r = conn.execute("""
            SELECT vc.id AS vc_id, vc.is_anchor, vr.reference
              FROM verse_context vc
              JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
             WHERE vc.mti_term_id = ?
               AND TRIM(vr.reference) = ?
               AND COALESCE(vc.delete_flagged,0) = 0
             LIMIT 1
        """, (mti, ref)).fetchone()
        if not r:
            # Try LIKE to handle whitespace/padding
            r = conn.execute("""
                SELECT vc.id AS vc_id, vc.is_anchor, vr.reference
                  FROM verse_context vc
                  JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                 WHERE vc.mti_term_id = ?
                   AND vr.reference LIKE ?
                   AND COALESCE(vc.delete_flagged,0) = 0
                 LIMIT 1
            """, (mti, f"%{ref}%")).fetchone()
        if not r:
            print(f"  ✗ {sg_code} anchor not found: ref='{ref}' mti={mti}"); ok = False; continue
        anchor_vc_ids[sg_code] = r["vc_id"]
        current = "(already anchor)" if r["is_anchor"] else "(not yet anchor)"
        print(f"  ✓ {sg_code} anchor: vc_id={r['vc_id']} '{r['reference']}' mti={mti} {current}")

    if not ok:
        print("\nPRE-FLIGHT FAILED")
        return 1

    if not args.live:
        print("\n[DRY-RUN] no changes. Re-run with --live.")
        return 0

    # ── LIVE APPLY ────────────────────────────────────────────────────────
    os.makedirs(BACKUP_DIR, exist_ok=True)
    bp = os.path.join(BACKUP_DIR,
                      f"bible_research_pre_m46_subgroup_restructure_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db")
    shutil.copy2(DB, bp)
    print(f"\nBackup: {bp}\n")

    try:
        conn.execute("BEGIN")
        cur = conn.cursor()

        # 1. RENAME_UPDATE M46-A/B/C
        rename_ops = [op for op in spec["subgroup_operations"] if op["op"] == "RENAME_UPDATE"]
        for op in rename_ops:
            cur.execute(
                "UPDATE cluster_subgroup SET label=?, core_description=?, "
                "       version='v2', source=?, last_updated_date=? "
                " WHERE cluster_code=? AND subgroup_code=?",
                (op["new_label"], op["new_description"], DIRECTIVE_ID, ts,
                 CLUSTER, op["subgroup_code"])
            )
            if cur.rowcount != 1:
                raise RuntimeError(f"RENAME {op['subgroup_code']}: {cur.rowcount} rows")
            print(f"  ✓ RENAMED {op['subgroup_code']}: {op['old_label']!r} → {op['new_label']!r}")

        # 2. CREATE M46-D
        create_ops = [op for op in spec["subgroup_operations"] if op["op"] == "CREATE"]
        for op in create_ops:
            cur.execute(
                "INSERT INTO cluster_subgroup "
                "  (cluster_code, subgroup_code, label, core_description, sort_order, "
                "   status, version, source, delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, 4, 'active', 'v1', ?, 0, ?, ?)",
                (CLUSTER, op["subgroup_code"], op["label"], op["description"],
                 DIRECTIVE_ID, ts, ts)
            )
            new_sg_id = cur.lastrowid
            print(f"  ✓ CREATED {op['subgroup_code']} id={new_sg_id} '{op['label']}'")

        # Re-read sg_id_map (now including M46-D)
        sg_id_map = {}
        for r in conn.execute(
            "SELECT id, subgroup_code FROM cluster_subgroup "
            "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)
        ):
            sg_id_map[r["subgroup_code"]] = r["id"]

        # 3. Hard-delete existing M46 mti_term_subgroup rows.
        # Soft-delete does not release the UNIQUE(mti_term_id, cluster_subgroup_id)
        # constraint, so an INSERT in step 4 would collide where the new primary
        # matches a prior placement. Backup covers audit trail. Placements
        # were created the same day under the directive-subgroups-v1 pass and
        # are being entirely replaced.
        cur.execute("""
            DELETE FROM mti_term_subgroup
             WHERE id IN (
               SELECT mts.id FROM mti_term_subgroup mts
                 JOIN mti_terms mt ON mt.id=mts.mti_term_id
                WHERE mt.cluster_code=?
             )
        """, (CLUSTER,))
        print(f"  ✓ Hard-deleted {cur.rowcount} prior mti_term_subgroup rows")

        # 4. INSERT 21 new primary-only placements
        for mti, strong, primary_sg, rationale in plan_assignments:
            sg_id = sg_id_map[primary_sg]
            placement_note = f"{DIRECTIVE_ID} restructure: primary={primary_sg}. {rationale}"[:500]
            cur.execute(
                "INSERT INTO mti_term_subgroup "
                "  (mti_term_id, cluster_subgroup_id, placement_note, "
                "   delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, 0, ?, ?)",
                (mti, sg_id, placement_note, ts, ts)
            )
        print(f"  ✓ Inserted {len(plan_assignments)} new primary-only mti_term_subgroup rows")

        # 5. Set is_anchor=1 on 4 canonical sub-group anchors (additive — keeps existing)
        for sg_code, vc_id in anchor_vc_ids.items():
            cur.execute(
                "UPDATE verse_context SET is_anchor=1 WHERE id=? AND is_anchor=0",
                (vc_id,)
            )
            status = "set" if cur.rowcount == 1 else "(already 1)"
            print(f"  ✓ {sg_code} anchor vc_id={vc_id} is_anchor=1 {status}")

        # FK check + commit
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {fkv[:3]}")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"\nROLLED BACK: {e}")
        return 1

    # ── VERIFICATION ──────────────────────────────────────────────────────
    print("\nVERIFICATION")
    print("-" * 72)
    print("\n  Sub-groups post-restructure:")
    for r in conn.execute("""
        SELECT cs.subgroup_code, cs.label,
               COUNT(mts.id) AS n_placements
          FROM cluster_subgroup cs
          LEFT JOIN mti_term_subgroup mts ON mts.cluster_subgroup_id=cs.id
                                          AND COALESCE(mts.delete_flagged,0)=0
         WHERE cs.cluster_code=? AND COALESCE(cs.delete_flagged,0)=0
         GROUP BY cs.id, cs.subgroup_code, cs.label
         ORDER BY cs.sort_order
    """, (CLUSTER,)):
        print(f"    {r['subgroup_code']:<10} '{r['label']}'  placements={r['n_placements']}")

    # R4 check: every M46 term with relevant verses has ≥1 anchor
    print("\n  R4 anchor check:")
    bad = list(conn.execute("""
        SELECT mt.id, mt.strongs_number, mt.transliteration
          FROM mti_terms mt
         WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
           AND EXISTS (SELECT 1 FROM verse_context vc
                        WHERE vc.mti_term_id=mt.id AND vc.is_relevant=1
                          AND COALESCE(vc.delete_flagged,0)=0)
           AND NOT EXISTS (SELECT 1 FROM verse_context vc
                            WHERE vc.mti_term_id=mt.id AND vc.is_anchor=1
                              AND COALESCE(vc.delete_flagged,0)=0)
    """, (CLUSTER,)))
    if bad:
        print(f"    ⚠ {len(bad)} term(s) with relevant verses but no anchor:")
        for r in bad:
            print(f"      mti={r['id']} {r['strongs_number']} {r['transliteration']}")
    else:
        print(f"    ✓ R4 clean — every M46 term with relevant verses has ≥1 anchor")

    n_anchors = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN mti_terms mt ON mt.id=vc.mti_term_id
         WHERE mt.cluster_code=? AND vc.is_anchor=1
           AND COALESCE(vc.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()[0]
    print(f"  Total is_anchor=1 rows in M46: {n_anchors}")

    print(f"\n  ⚠ FLAGGED — not in restructure (no placement):")
    for t in missing:
        print(f"      mti={t['id']} {t['strongs_number']} {t['transliteration']}")

    conn.close()
    print(f"\n[LIVE] M46 SUBGROUP_RESTRUCTURE applied.")
    print(f"\nNext: apply WA-M46-patch-vcg-from-reading-v1-20260514.json (stage 2)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
