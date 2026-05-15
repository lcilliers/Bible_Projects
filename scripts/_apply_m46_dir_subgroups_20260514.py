"""Apply WA-M46-directive-subgroups-v1-20260514 — Phase 4 SUBGROUP_CREATE.

Per v1_13 §7.7: packaged directive — Operation A (sub-group create +
mti_term_subgroup assign) + Operation C (cluster.status transition).

Operation A: 3 cluster_subgroup rows (M46-A/B/C); 31 mti_term_subgroup rows
  (multi-placement: terms can appear in multiple sub-groups per directive).
Operation B: not required (no out-of-cluster rebinds).
Operation C: cluster.status 'Data - In Progress' → 'Analysis - In Progress'.

Schema deviations checked against v1_13 §A1:
  cluster_subgroup: subgroup_code, label, core_description ✓
  mti_term_subgroup: mti_term_id, cluster_subgroup_id, placement_note ✓

Flagged but NOT applied: G3045 liparos (mti=4702) is not in the directive;
recommended placement is M46-A but requires explicit researcher direction.
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
DIRECTIVE_ID = "DIR-20260514-M46-subgroups"
CLUSTER = "M46"
INPUT_JSON = "Sessions/Session_Clusters/M46/WA-M46-directive-subgroups-v1-20260514.json"


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
    print(f"  M46 Phase 4 SUBGROUP_CREATE — {len(spec['subgroups'])} sub-groups")
    print(f"  Mode: {'LIVE' if args.live else 'DRY-RUN'}")
    print("=" * 72)

    # ── PRE-FLIGHT ────────────────────────────────────────────────────────
    print("\nPRE-FLIGHT")
    print("-" * 72)
    ok = True

    # Cluster status
    cluster_row = conn.execute(
        "SELECT cluster_code, status FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    if not cluster_row:
        print(f"  ✗ cluster {CLUSTER} not found"); ok = False
    elif cluster_row["status"] != "Data - In Progress":
        print(f"  ✗ cluster.status={cluster_row['status']!r} (expected 'Data - In Progress')"); ok = False
    else:
        print(f"  ✓ cluster.status = 'Data - In Progress'")

    # No existing sub-groups
    n_existing_sg = conn.execute(
        "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code=? "
        "AND COALESCE(delete_flagged,0)=0", (CLUSTER,)
    ).fetchone()[0]
    print(f"  cluster_subgroup rows for {CLUSTER}: {n_existing_sg} (expected 0)")
    if n_existing_sg:
        ok = False

    # No existing placements
    n_existing_pl = conn.execute("""
        SELECT COUNT(*) FROM mti_term_subgroup mts
          JOIN mti_terms mt ON mt.id=mts.mti_term_id
         WHERE mt.cluster_code=? AND COALESCE(mts.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()[0]
    print(f"  Existing mti_term_subgroup rows for M46 terms: {n_existing_pl} (expected 0)")
    if n_existing_pl:
        ok = False

    # Verify each term exists in M46
    all_pairs = []
    for sg in spec["subgroups"]:
        for term in sg["primary_terms"]:
            all_pairs.append((term["mti_id"], term["strong"], sg["subgroup_code"], term.get("note", "")))

    print(f"\n  Validating {len(all_pairs)} (term, sub-group) pairs:")
    by_term = {}
    for mti, strong, sg_code, note in all_pairs:
        r = conn.execute(
            "SELECT id, strongs_number, transliteration, cluster_code "
            "FROM mti_terms WHERE id=? AND COALESCE(delete_flagged,0)=0", (mti,)
        ).fetchone()
        if not r:
            print(f"    ✗ mti={mti} {strong} NOT FOUND"); ok = False; continue
        if r["strongs_number"] != strong:
            print(f"    ✗ mti={mti} expected {strong} got {r['strongs_number']}"); ok = False; continue
        if r["cluster_code"] != CLUSTER:
            print(f"    ✗ mti={mti} {strong} cluster={r['cluster_code']}"); ok = False; continue
        by_term.setdefault(mti, []).append(sg_code)

    # Active M46 terms NOT in directive
    m46_active = list(conn.execute(
        "SELECT id, strongs_number, transliteration FROM mti_terms "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)
    ))
    missing = [t for t in m46_active if t["id"] not in by_term]
    if missing:
        print(f"\n  ⚠ {len(missing)} active M46 term(s) not in directive (flagged, not auto-assigned):")
        for t in missing:
            print(f"      mti={t['id']} {t['strongs_number']} '{t['transliteration']}'")

    if not ok:
        print("\nPRE-FLIGHT FAILED")
        return 1

    # Summary
    print(f"\n  Operation A:")
    print(f"    cluster_subgroup INSERTs: {len(spec['subgroups'])}")
    print(f"    mti_term_subgroup INSERTs: {len(all_pairs)}")
    print(f"    Unique terms covered: {len(by_term)}")
    multi = [m for m, sgs in by_term.items() if len(sgs) > 1]
    print(f"    Multi-placed terms: {len(multi)}")
    print(f"  Operation B: 0 (no rebinds)")
    print(f"  Operation C: cluster.status → 'Analysis - In Progress'")

    if not args.live:
        print("\n[DRY-RUN] no changes. Re-run with --live.")
        return 0

    # Backup
    os.makedirs(BACKUP_DIR, exist_ok=True)
    bp = os.path.join(BACKUP_DIR,
                      f"bible_research_pre_m46_dir_subgroups_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db")
    shutil.copy2(DB, bp)
    print(f"\nBackup: {bp}\n")

    try:
        conn.execute("BEGIN")
        cur = conn.cursor()

        # Operation A1 — INSERT cluster_subgroup rows
        sg_id_map = {}
        for idx, sg in enumerate(spec["subgroups"], 1):
            cur.execute(
                "INSERT INTO cluster_subgroup "
                "  (cluster_code, subgroup_code, label, core_description, sort_order, "
                "   status, version, source, delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, 'active', 'v1', ?, 0, ?, ?)",
                (CLUSTER, sg["subgroup_code"], sg["short_label"],
                 sg["full_description"], idx, DIRECTIVE_ID, ts, ts)
            )
            sg_id_map[sg["subgroup_code"]] = cur.lastrowid

        # Operation A2 — INSERT mti_term_subgroup rows
        for mti, strong, sg_code, note in all_pairs:
            sg_id = sg_id_map[sg_code]
            placement_note = f"{DIRECTIVE_ID} Phase 4 SUBGROUP_CREATE: {note}"[:500]
            cur.execute(
                "INSERT INTO mti_term_subgroup "
                "  (mti_term_id, cluster_subgroup_id, placement_note, "
                "   delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, 0, ?, ?)",
                (mti, sg_id, placement_note, ts, ts)
            )

        # Operation C — status transition
        cur.execute(
            "UPDATE cluster SET status='Analysis - In Progress', last_updated_date=? "
            "WHERE cluster_code=?", (ts, CLUSTER)
        )
        if cur.rowcount != 1:
            raise RuntimeError(f"status UPDATE affected {cur.rowcount} rows")

        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {fkv[:3]}")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"\nROLLED BACK: {e}")
        return 1

    # ── VERIFICATION ──────────────────────────────────────────────────────
    print("VERIFICATION")
    print("-" * 72)

    print("\n  Sub-group rows + per-sub-group placement counts:")
    for r in conn.execute("""
        SELECT cs.subgroup_code, cs.label,
               COUNT(mts.id) AS n_placements,
               COUNT(DISTINCT mts.mti_term_id) AS n_distinct_terms
          FROM cluster_subgroup cs
          LEFT JOIN mti_term_subgroup mts ON mts.cluster_subgroup_id=cs.id
                                          AND COALESCE(mts.delete_flagged,0)=0
         WHERE cs.cluster_code=? AND COALESCE(cs.delete_flagged,0)=0
         GROUP BY cs.id, cs.subgroup_code, cs.label
         ORDER BY cs.sort_order
    """, (CLUSTER,)):
        print(f"    {r['subgroup_code']:<10} '{r['label']}'  placements={r['n_placements']}  distinct_terms={r['n_distinct_terms']}")

    n_total = conn.execute("""
        SELECT COUNT(*) FROM mti_term_subgroup mts
          JOIN mti_terms mt ON mt.id=mts.mti_term_id
         WHERE mt.cluster_code=? AND COALESCE(mts.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()[0]
    print(f"\n  Total mti_term_subgroup rows for M46 terms: {n_total}")

    print(f"\n  Multi-placed terms (placement in >1 sub-group):")
    for r in conn.execute("""
        SELECT mt.id, mt.strongs_number, mt.transliteration, COUNT(*) AS n_sg
          FROM mti_term_subgroup mts
          JOIN mti_terms mt ON mt.id=mts.mti_term_id
          JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
         WHERE cs.cluster_code=? AND COALESCE(mts.delete_flagged,0)=0
         GROUP BY mt.id, mt.strongs_number, mt.transliteration
        HAVING n_sg > 1
         ORDER BY n_sg DESC, mt.strongs_number
    """, (CLUSTER,)):
        sgs = list(conn.execute("""SELECT cs.subgroup_code FROM mti_term_subgroup mts
                                   JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
                                   WHERE mts.mti_term_id=? AND COALESCE(mts.delete_flagged,0)=0
                                   ORDER BY cs.sort_order""", (r['id'],)))
        sg_list = ', '.join(s['subgroup_code'] for s in sgs)
        print(f"    mti={r['id']:<5} {r['strongs_number']:<8} {r['transliteration']:<14} ({r['n_sg']}: {sg_list})")

    # Final status
    cs = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)).fetchone()
    print(f"\n  cluster.status: {cs['status']!r}")

    print(f"\n  ⚠ FLAGGED — not in directive, no placement created:")
    for t in missing:
        print(f"      mti={t['id']} {t['strongs_number']} {t['transliteration']}")

    conn.close()
    print(f"\n[LIVE] M46 Phase 4 SUBGROUP_CREATE applied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
