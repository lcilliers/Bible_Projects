"""_apply_m32_dir002_v1_20260508.py — DB-modifying.

DIR-20260508-001: M32 sub-group assignment (Phase 4).

Operations (single transaction):
  1. INSERT 3 cluster_subgroup rows: M32-A, M32-B, M32-BOUNDARY
  2. UPDATE 6 mti_terms rows: cluster_subgroup_id assignments
  3. UPDATE cluster.status for M32 -> 'Analysis - In Progress'

Pre-flight verifies all 6 target mti_ids exist with cluster_code='M32'.
Halts (rolls back) on any pre-flight failure or insert/update error.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
CLUSTER_CODE = "M32"

SUBGROUPS = [
    ("M32-A", "Conscience",
     "The faculty by which the person assesses their own moral state — "
     "inner knowing of one's own moral standing, complicity, or condition; "
     "operating under the awareness that God's judgment is the higher court"),
    ("M32-B", "Self-Awareness / Inner Attention",
     "The directed inner act of setting attention — deliberate cognitive "
     "engagement and attending carefully to a matter, person, or situation; "
     "the attentiveness capacity that underlies conscience"),
    ("M32-BOUNDARY", "BOUNDARY",
     "Supporting terms that contextualise the conscience and self-awareness "
     "characteristics without themselves being T1 characteristic-bearing: "
     "the reflective capacity (enthumeomai), the terminal conscience-state "
     "(autokatakritos), and the divine epistemological frame (kardiognōstēs)"),
]

# (mti_id, strongs, target_subgroup_code)
ASSIGNMENTS = [
    (454,  "G4894",  "M32-A"),
    (2739, "G6083",  "M32-A"),
    (3578, "H7896K", "M32-B"),
    (3392, "G1760",  "M32-BOUNDARY"),
    (4848, "G0843",  "M32-BOUNDARY"),
    (599,  "G2589",  "M32-BOUNDARY"),
]

NEW_STATUS = "Analysis - In Progress"
DIRECTIVE_ID = "DIR-20260508-001"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    print(f"DB: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    ts = now_iso()

    # Pre-flight
    halts = []
    for mti_id, strongs, _ in ASSIGNMENTS:
        r = cur.execute(
            "SELECT id, cluster_code FROM mti_terms WHERE id=?", (mti_id,)
        ).fetchone()
        if r is None:
            halts.append(f"mti_id {mti_id} ({strongs}) not found")
        elif r["cluster_code"] != CLUSTER_CODE:
            halts.append(
                f"mti_id {mti_id} ({strongs}) cluster_code is "
                f"{r['cluster_code']!r}, expected {CLUSTER_CODE!r}"
            )
    if halts:
        print("[HALT] Pre-flight failed:")
        for h in halts:
            print(f"  {h}")
        return 1

    n_subgroups_inserted = 0
    n_terms_updated = 0
    n_cluster_updated = 0
    sg_ids: dict[str, int] = {}

    try:
        cur.execute("BEGIN")

        # 1. Insert 3 cluster_subgroup rows
        for code, label, desc in SUBGROUPS:
            cur.execute(
                "INSERT INTO cluster_subgroup "
                "  (cluster_code, subgroup_code, label, core_description, "
                "   sort_order, status, version, source, "
                "   delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, 'Active', 'v1', ?, 0, ?, ?)",
                (CLUSTER_CODE, code, label, desc,
                 list(c[0] for c in SUBGROUPS).index(code) + 1,
                 DIRECTIVE_ID, ts, ts),
            )
            sg_ids[code] = cur.lastrowid
            n_subgroups_inserted += 1
            print(f"  + cluster_subgroup INSERT {code} -> id={cur.lastrowid}")

        # 2. Update 6 mti_terms with cluster_subgroup_id
        for mti_id, strongs, target_code in ASSIGNMENTS:
            sg_id = sg_ids[target_code]
            rc = cur.execute(
                "UPDATE mti_terms "
                "   SET cluster_subgroup_id=?, last_changed=? "
                " WHERE id=? AND cluster_code=?",
                (sg_id, ts, mti_id, CLUSTER_CODE),
            ).rowcount
            if rc != 1:
                raise RuntimeError(
                    f"mti_terms UPDATE for id={mti_id} expected 1 row, got {rc}"
                )
            n_terms_updated += 1
            print(f"  ~ mti_terms UPDATE {strongs} (mti={mti_id}) "
                  f"-> sg_id={sg_id} ({target_code})")

        # 3. Update cluster.status
        rc = cur.execute(
            "UPDATE cluster "
            "   SET status=?, last_updated_date=? WHERE cluster_code=?",
            (NEW_STATUS, ts, CLUSTER_CODE),
        ).rowcount
        if rc != 1:
            raise RuntimeError(
                f"cluster UPDATE for {CLUSTER_CODE} expected 1 row, got {rc}"
            )
        n_cluster_updated = 1
        print(f"  ~ cluster UPDATE M32 status -> {NEW_STATUS!r}")

        cur.execute("COMMIT")
    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    print()
    print(f"cluster_subgroup rows inserted: {n_subgroups_inserted}")
    print(f"mti_terms rows updated:         {n_terms_updated}")
    print(f"cluster row updated:            {n_cluster_updated}")

    # ──── Completion confirmation ────
    print()
    print("=== Q1 — Sub-group counts ===")
    for r in cur.execute(
        "SELECT cs.subgroup_code, COUNT(mt.id) AS term_count "
        "  FROM cluster_subgroup cs "
        "  LEFT JOIN mti_terms mt ON mt.cluster_subgroup_id=cs.id "
        "    AND COALESCE(mt.delete_flagged,0)=0 "
        " WHERE cs.cluster_code=? "
        "   AND COALESCE(cs.delete_flagged,0)=0 "
        " GROUP BY cs.subgroup_code "
        " ORDER BY cs.subgroup_code",
        (CLUSTER_CODE,),
    ):
        print(f"  {r['subgroup_code']:14s} {r['term_count']}")

    print()
    print("=== Q2 — All terms assigned (no nulls) ===")
    for r in cur.execute(
        "SELECT mt.id, mt.strongs_number, mt.transliteration, "
        "       cs.subgroup_code "
        "  FROM mti_terms mt "
        "  LEFT JOIN cluster_subgroup cs ON cs.id=mt.cluster_subgroup_id "
        " WHERE mt.cluster_code=? "
        "   AND COALESCE(mt.delete_flagged,0)=0 "
        " ORDER BY cs.subgroup_code, mt.strongs_number",
        (CLUSTER_CODE,),
    ):
        print(f"  mti={r['id']:5d} {r['strongs_number']:8s} "
              f"{r['transliteration']:20s} -> {r['subgroup_code']}")

    print()
    print("=== Q3 — Cluster status ===")
    r = cur.execute(
        "SELECT cluster_code, status, last_updated_date FROM cluster "
        " WHERE cluster_code=?", (CLUSTER_CODE,)
    ).fetchone()
    print(f"  {r['cluster_code']}  status={r['status']!r}  "
          f"updated={r['last_updated_date']}")

    print()
    print("=== Q4 — wa_session_b_findings (term_id) for M32 terms ===")
    n = cur.execute(
        "SELECT COUNT(*) FROM wa_session_b_findings "
        " WHERE term_id IN (454, 2739, 3578, 3392, 4848, 599)"
    ).fetchone()[0]
    print(f"  count: {n} (baseline was 0; expected 0)")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
