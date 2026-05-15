"""Apply DIR-20260514-001 — M39 sub-group assignment (Phase 4, v1_9 packaged).

Per wa-sessionb-cluster-instruction-v1_9 §7.7: single packaged directive carrying
  Operation A — cluster_subgroup CREATE + term placement (3 subgroups, 16 terms)
  Operation B — cluster_code rebind (NOT REQUIRED for M39)
  Operation C — cluster.status 'Data - In Progress' → 'Analysis - In Progress'

Directive source: Sessions/Session_Clusters/M39/wa-cluster-M39-dir-001-subgroup-assign-v1-20260514.md

Schema deviations from the directive text (applied per M20/M26 precedent + actual schema):
  1. mti_terms.cluster_subgroup_id does not exist — placements use mti_term_subgroup join table
  2. cluster_subgroup.is_boundary does not exist — BOUNDARY is identified by subgroup_code='M39-BOUNDARY'
  3. cluster_subgroup.description does not exist — actual column is core_description

Backup → dry-run → live.
"""
import sqlite3, sys, os, json, argparse
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = "database/bible_research.db"
DIRECTIVE_ID = "DIR-20260514-001"
CLUSTER_CODE = "M39"

SUBGROUPS = [
    # (subgroup_code, label, sort_order, core_description)
    ("M39-A", "Blessing and Grace", 1,
     "The sovereign, initiated movement of the greater toward the lesser — God's blessing, grace, and favour as dispositioned gift; the inner-being characteristic in which one person (primarily God) constitutes favour, standing, and inner transformation in another who cannot earn or generate it. Terms span the act of blessing (ba.rakh), the noun of grace-disposition (charis, chen), the verbal act of being gracious (cha.nan), the act of grace-giving (charizō), the completed standing-in-grace (charitoō), the divine inner pleasure as ground of blessing (eudokia), the character-type of graciousness (chan.nun), the grace-endowment (charisma), and the acceptance/delight face of the grace dynamic (ra.tsah)."),
    ("M39-B", "Goodness", 2,
     "The inner moral-affective quality of being good — the character of the person or act assessed as genuinely good, morally right, and producing goodness in community and relationship. Includes the moral evaluation faculty, the affective gladness-at-good, and the volitional preference for what is genuinely beneficial. Terms: ya.tav (bridging moral goodness, affective gladness, and approval-of-good) and tov (the broadest OT goodness term covering moral rightness, covenantal reliability, and volitional preference)."),
    ("M39-BOUNDARY", "BOUNDARY", 3,
     "Temporary holding group for terms that are supportive, descriptive, qualifying, or undecided pending verse-level analysis. Per programme BOUNDARY conventions, terms here are re-evaluated during Phase 10 and must exit BOUNDARY before cluster closure."),
]

# (mti_id, subgroup_code)
TERM_PLACEMENTS = [
    (1299, "M39-A"),
    (888,  "M39-A"),
    (984,  "M39-A"),
    (889,  "M39-A"),
    (5470, "M39-A"),
    (5471, "M39-A"),
    (494,  "M39-A"),
    (2330, "M39-A"),
    (1301, "M39-A"),
    (989,  "M39-A"),
    (795,  "M39-A"),
    (632,  "M39-B"),
    (542,  "M39-B"),
    (6837, "M39-BOUNDARY"),
    (2976, "M39-BOUNDARY"),
    (633,  "M39-BOUNDARY"),
]

EXPECTED_COUNTS = {"M39-A": 11, "M39-B": 2, "M39-BOUNDARY": 3}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true",
                    help="Apply changes. Without this flag, dry-run only.")
    args = ap.parse_args()

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    ts = datetime.now().strftime("%Y%m%dT%H%M%S")

    backup_dir = "backups/row_backups"
    os.makedirs(backup_dir, exist_ok=True)
    backup_path = os.path.join(backup_dir, f"M39_dir001_subgroup_assign_pre_{ts}.json")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    print(f"DIRECTIVE: {DIRECTIVE_ID}")
    print(f"CLUSTER:   {CLUSTER_CODE}")
    print(f"MODE:      {'LIVE' if args.live else 'DRY-RUN'}")
    print()

    # ── Pre-flight checks ─────────────────────────────────────────────────
    print("Pre-flight:")

    # Cluster exists, status is Data - In Progress
    cluster_row = conn.execute(
        "SELECT cluster_code, status FROM cluster WHERE cluster_code=?", (CLUSTER_CODE,)
    ).fetchone()
    if not cluster_row:
        raise SystemExit(f"❌ Cluster {CLUSTER_CODE} not found")
    if cluster_row["status"] != "Data - In Progress":
        raise SystemExit(
            f"❌ Cluster {CLUSTER_CODE} status={cluster_row['status']!r} "
            f"(expected 'Data - In Progress')"
        )
    print(f"  ✓ cluster.status = {cluster_row['status']!r}")

    # No existing cluster_subgroup rows for M39
    existing_sg = conn.execute(
        "SELECT COUNT(*) c FROM cluster_subgroup WHERE cluster_code=?", (CLUSTER_CODE,)
    ).fetchone()["c"]
    if existing_sg:
        raise SystemExit(
            f"❌ {existing_sg} existing cluster_subgroup rows for {CLUSTER_CODE} "
            f"— directive expects 0 (re-run scenario not auto-handled)"
        )
    print(f"  ✓ cluster_subgroup rows for {CLUSTER_CODE} = 0 (no pre-existing)")

    # No existing mti_term_subgroup rows for any M39 term
    existing_pl = conn.execute("""
        SELECT COUNT(*) c FROM mti_term_subgroup mts
          JOIN mti_terms mt ON mt.id=mts.mti_term_id
         WHERE mt.cluster_code=?
    """, (CLUSTER_CODE,)).fetchone()["c"]
    if existing_pl:
        raise SystemExit(
            f"❌ {existing_pl} existing mti_term_subgroup rows for {CLUSTER_CODE} terms"
        )
    print(f"  ✓ mti_term_subgroup rows for {CLUSTER_CODE} terms = 0")

    # Resolve and verify each (mti_id, subgroup) placement
    for mti_id, sg_code in TERM_PLACEMENTS:
        r = conn.execute(
            "SELECT id, strongs_number, transliteration, cluster_code, "
            "       COALESCE(delete_flagged,0) deleted "
            "FROM mti_terms WHERE id=?", (mti_id,)
        ).fetchone()
        if not r:
            raise SystemExit(f"❌ mti_id={mti_id} not found")
        if r["cluster_code"] != CLUSTER_CODE:
            raise SystemExit(
                f"❌ mti_id={mti_id} cluster_code={r['cluster_code']!r} "
                f"(expected {CLUSTER_CODE!r})"
            )
        if r["deleted"]:
            raise SystemExit(f"❌ mti_id={mti_id} is delete_flagged")
    print(f"  ✓ {len(TERM_PLACEMENTS)} terms verified in cluster {CLUSTER_CODE}")

    # ── Pre-state backup ──────────────────────────────────────────────────
    pre_state = {
        "directive_id": DIRECTIVE_ID,
        "timestamp": now_utc,
        "cluster_pre": dict(cluster_row),
        "cluster_subgroup_pre": [
            dict(r) for r in conn.execute(
                "SELECT * FROM cluster_subgroup WHERE cluster_code=?", (CLUSTER_CODE,)
            )
        ],
        "mti_term_subgroup_pre": [
            dict(r) for r in conn.execute("""
                SELECT mts.* FROM mti_term_subgroup mts
                  JOIN mti_terms mt ON mt.id=mts.mti_term_id
                 WHERE mt.cluster_code=?
            """, (CLUSTER_CODE,))
        ],
    }
    with open(backup_path, "w", encoding="utf-8") as f:
        json.dump(pre_state, f, indent=2, ensure_ascii=False)
    print(f"\nPre-state backup → {backup_path}")

    print(f"\nProposed operations:")
    print(f"  Operation A: 3 cluster_subgroup INSERTs + {len(TERM_PLACEMENTS)} mti_term_subgroup INSERTs")
    print(f"  Operation B: 0 (not required — no out-of-cluster rebinds)")
    print(f"  Operation C: cluster.status 'Data - In Progress' → 'Analysis - In Progress'")

    if not args.live:
        print("\n[DRY-RUN] no changes. Re-run with --live to apply.")
        return

    # ── LIVE APPLY ────────────────────────────────────────────────────────
    placement_note = f"{DIRECTIVE_ID} — Phase 4 subgroup-assign"
    sg_id_map = {}

    try:
        # Operation A1 — INSERT cluster_subgroup rows
        for sg_code, label, sort_order, core_desc in SUBGROUPS:
            cur = conn.execute(
                "INSERT INTO cluster_subgroup "
                "  (cluster_code, subgroup_code, label, core_description, sort_order, "
                "   status, version, source, delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, 'active', 'v1', ?, 0, ?, ?)",
                (CLUSTER_CODE, sg_code, label, core_desc, sort_order,
                 DIRECTIVE_ID, now_utc, now_utc)
            )
            sg_id_map[sg_code] = cur.lastrowid

        # Operation A2 — INSERT mti_term_subgroup rows
        for mti_id, sg_code in TERM_PLACEMENTS:
            conn.execute(
                "INSERT INTO mti_term_subgroup "
                "  (mti_term_id, cluster_subgroup_id, placement_note, "
                "   delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, 0, ?, ?)",
                (mti_id, sg_id_map[sg_code], placement_note, now_utc, now_utc)
            )

        # Operation C — cluster.status transition
        conn.execute(
            "UPDATE cluster SET status='Analysis - In Progress', last_updated_date=? "
            "WHERE cluster_code=?",
            (now_utc, CLUSTER_CODE)
        )

        conn.commit()
    except Exception as e:
        conn.rollback()
        raise SystemExit(f"❌ Transaction failed: {e}")

    # ── COMPLETION CONFIRMATION ───────────────────────────────────────────
    print("\nCOMPLETION CONFIRMATION:")

    # Query 1 — Sub-group counts by subgroup_code
    print("\n  Query 1: Sub-group counts by subgroup_code")
    actual_counts = {}
    for r in conn.execute("""
        SELECT cs.subgroup_code, cs.label, COUNT(mts.id) AS term_count
          FROM cluster_subgroup cs
          LEFT JOIN mti_term_subgroup mts ON mts.cluster_subgroup_id=cs.id
                                          AND COALESCE(mts.delete_flagged,0)=0
         WHERE cs.cluster_code=? AND COALESCE(cs.delete_flagged,0)=0
         GROUP BY cs.subgroup_code, cs.label
         ORDER BY cs.sort_order
    """, (CLUSTER_CODE,)):
        actual_counts[r["subgroup_code"]] = r["term_count"]
        print(f"    {r['subgroup_code']:<14}  {r['term_count']}  {r['label']}")
    if actual_counts != EXPECTED_COUNTS:
        raise SystemExit(f"❌ Count mismatch: got {actual_counts}, expected {EXPECTED_COUNTS}")
    print(f"    ✓ Counts match expected {EXPECTED_COUNTS}")

    # Query 2 — All M39 terms with their assigned subgroup_code (no NULLs)
    print("\n  Query 2: All M39 terms with assigned subgroup_code")
    null_count = 0
    for r in conn.execute("""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration,
               cs.subgroup_code
          FROM mti_terms mt
          LEFT JOIN mti_term_subgroup mts ON mts.mti_term_id=mt.id
                                          AND COALESCE(mts.delete_flagged,0)=0
          LEFT JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
         WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
           AND mt.status IN ('extracted', 'extracted_thin')
         ORDER BY cs.sort_order, mt.strongs_number
    """, (CLUSTER_CODE,)):
        marker = "✓" if r["subgroup_code"] else "❌"
        print(f"    {marker} mti={r['mti_id']:<5} {r['strongs_number']:<7} "
              f"{r['transliteration']:<14} → {r['subgroup_code'] or '!! NULL !!'}")
        if r["subgroup_code"] is None:
            null_count += 1
    if null_count:
        raise SystemExit(f"❌ {null_count} terms with NULL subgroup_code")
    print(f"    ✓ All 16 M39 terms have a subgroup assignment")

    # Query 3 — Cluster status
    print("\n  Query 3: Cluster status")
    r = conn.execute(
        "SELECT cluster_code, status FROM cluster WHERE cluster_code=?", (CLUSTER_CODE,)
    ).fetchone()
    print(f"    {r['cluster_code']}: status={r['status']!r}")
    if r["status"] != "Analysis - In Progress":
        raise SystemExit(f"❌ Cluster status not transitioned correctly")
    print(f"    ✓ cluster.status = 'Analysis - In Progress'")

    # Query 4 — VC connectivity (baseline, not a gate)
    print("\n  Query 4: verse_context rows without cluster_subgroup_id (baseline)")
    r = conn.execute("""
        SELECT COUNT(*) c FROM verse_context vc
          JOIN mti_terms mt ON mt.id=vc.mti_term_id
         WHERE mt.cluster_code=?
           AND mt.status IN ('extracted', 'extracted_thin')
           AND vc.cluster_subgroup_id IS NULL
    """, (CLUSTER_CODE,)).fetchone()
    print(f"    unrouted_vc_rows: {r['c']} (expected > 0 at this phase; Phase 7 populates)")

    print(f"\n[LIVE] {DIRECTIVE_ID} applied successfully.")
    conn.close()


if __name__ == "__main__":
    main()
