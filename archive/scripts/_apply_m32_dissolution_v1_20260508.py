"""_apply_m32_dissolution_v1_20260508.py — DB-modifying.

DIR-20260508-005 — M32 dissolution (researcher-amended path).

Researcher decision (2026-05-08, overriding the directive's preservation
instructions): "I do not want any reference in the analytic and term
results to M32. It should for all practical purposes non exist. The
analytic work of M15 and M26 will pick up and redo the analytics that
is lost in the process."

Therefore:
  - 6 active terms move to M15 / M26 with cluster_subgroup_id cleared
  - 15 delete-flagged historical mti_terms rows have cluster_code cleared
  - All 575 cluster_finding rows on M32 are HARD-DELETED
  - All 3 cluster_subgroup rows on M32 are HARD-DELETED
  - The 1 cluster row for M32 is HARD-DELETED
  - verse_context / verse_context_group / wa_verse_records etc. untouched
    (no cluster_code reference; travel with terms via mti_term_id)

Single transaction with PRAGMA foreign_keys = ON for safety.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")

# (mti_id, strongs, target_cluster_code)
TERM_REASSIGNMENTS = [
    (454,  "G4894",  "M15"),  # suneidō → cognitive awareness
    (3578, "H7896K", "M15"),  # shit → deliberate inner attending
    (3392, "G1760",  "M15"),  # enthumeomai → sustained inner deliberation
    (2739, "G6083",  "M26"),  # sunoida → moral self-assessment in judicial frame
    (599,  "G2589",  "M26"),  # kardiognōstēs → divine heart-knowing as forensic ground
    (4848, "G0843",  "M26"),  # autokatakritos → self-condemnation as judicial verdict
]

ACTIVE_MTI_IDS = [r[0] for r in TERM_REASSIGNMENTS]


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()
    ts = now_iso()

    # ── Pre-flight ────────────────────────────────────────────────────────
    print("=" * 65)
    print("PRE-FLIGHT")
    print("=" * 65)

    halts = []

    # 1. All 6 active mti_ids exist with cluster_code='M32'
    for mti_id, strongs, _ in TERM_REASSIGNMENTS:
        r = cur.execute(
            "SELECT id, cluster_code, COALESCE(delete_flagged,0) AS df "
            "  FROM mti_terms WHERE id=?",
            (mti_id,),
        ).fetchone()
        if r is None:
            halts.append(f"mti_id {mti_id} ({strongs}) not found")
        elif r["cluster_code"] != "M32":
            halts.append(
                f"mti_id {mti_id} cluster_code is {r['cluster_code']!r}, "
                f"expected 'M32'"
            )
        elif r["df"] != 0:
            halts.append(
                f"mti_id {mti_id} is delete_flagged — should be active"
            )

    # 2. M15 and M26 destination clusters exist
    for code in ("M15", "M26"):
        r = cur.execute(
            "SELECT cluster_code FROM cluster WHERE cluster_code=?",
            (code,),
        ).fetchone()
        if r is None:
            halts.append(f"destination cluster {code} not found")

    # 3. Snapshot counts for verification later
    pre_counts = {}
    for table, where in (
        ("mti_terms_active",
         "cluster_code='M32' AND COALESCE(delete_flagged,0)=0"),
        ("mti_terms_deleted",
         "cluster_code='M32' AND delete_flagged=1"),
        ("cluster_subgroup",
         "cluster_code='M32'"),
        ("cluster_finding",
         "cluster_code='M32'"),
        ("cluster",
         "cluster_code='M32'"),
    ):
        if "_active" in table or "_deleted" in table:
            tbl = "mti_terms"
        else:
            tbl = table
        pre_counts[table] = cur.execute(
            f"SELECT COUNT(*) FROM {tbl} WHERE {where}"
        ).fetchone()[0]

    # 4. Verse_context / verse_context_group baseline (must remain unchanged)
    pre_vc = cur.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE mti_term_id IN ({})".format(
            ",".join("?" * len(ACTIVE_MTI_IDS))
        ),
        ACTIVE_MTI_IDS,
    ).fetchone()[0]
    pre_vcg = cur.execute(
        "SELECT COUNT(*) FROM verse_context_group "
        " WHERE mti_term_id IN ({})".format(
            ",".join("?" * len(ACTIVE_MTI_IDS))
        ),
        ACTIVE_MTI_IDS,
    ).fetchone()[0]

    print()
    print("Baseline:")
    for k, v in pre_counts.items():
        print(f"  {k:25s} {v}")
    print(f"  verse_context (term-linked) {pre_vc}")
    print(f"  verse_context_group (term-linked) {pre_vcg}")

    if halts:
        print()
        print("HALT — pre-flight failed:")
        for h in halts:
            print(f"  {h}")
        return 1

    # ── Execute ───────────────────────────────────────────────────────────
    print()
    print("=" * 65)
    print("EXECUTE")
    print("=" * 65)

    counts = {
        "active_terms_reassigned": 0,
        "deleted_terms_cluster_cleared": 0,
        "subgroup_id_cleared": 0,
        "cluster_finding_deleted": 0,
        "cluster_subgroup_deleted": 0,
        "cluster_deleted": 0,
    }

    try:
        cur.execute("BEGIN")

        # 1a. Reassign 6 active terms; clear cluster_subgroup_id
        for mti_id, strongs, new_code in TERM_REASSIGNMENTS:
            rc = cur.execute(
                "UPDATE mti_terms "
                "   SET cluster_code=?, cluster_subgroup_id=NULL, "
                "       last_changed=? "
                " WHERE id=? AND cluster_code='M32' "
                "   AND COALESCE(delete_flagged,0)=0",
                (new_code, ts, mti_id),
            ).rowcount
            if rc != 1:
                raise RuntimeError(
                    f"mti_terms reassign mti={mti_id} expected 1 row, got {rc}"
                )
            counts["active_terms_reassigned"] += 1
            counts["subgroup_id_cleared"] += 1
            print(f"  ~ mti_terms UPDATE {strongs} (mti={mti_id}) "
                  f"M32 -> {new_code}, sg_id=NULL")

        # 1b. Clear cluster_code on the 15 delete_flagged historical rows
        rc = cur.execute(
            "UPDATE mti_terms "
            "   SET cluster_code=NULL, last_changed=? "
            " WHERE cluster_code='M32' AND delete_flagged=1",
            (ts,),
        ).rowcount
        counts["deleted_terms_cluster_cleared"] = rc
        print(f"  ~ mti_terms UPDATE {rc} delete_flagged rows: "
              f"cluster_code 'M32' -> NULL")

        # 2. DELETE all cluster_finding rows on M32
        rc = cur.execute(
            "DELETE FROM cluster_finding WHERE cluster_code='M32'"
        ).rowcount
        counts["cluster_finding_deleted"] = rc
        print(f"  - cluster_finding DELETE {rc} rows")

        # 3. DELETE all cluster_subgroup rows on M32
        rc = cur.execute(
            "DELETE FROM cluster_subgroup WHERE cluster_code='M32'"
        ).rowcount
        counts["cluster_subgroup_deleted"] = rc
        print(f"  - cluster_subgroup DELETE {rc} rows")

        # 4. DELETE the M32 cluster row
        rc = cur.execute(
            "DELETE FROM cluster WHERE cluster_code='M32'"
        ).rowcount
        counts["cluster_deleted"] = rc
        print(f"  - cluster DELETE {rc} rows")

        cur.execute("COMMIT")
        print()
        print("COMMIT successful.")
    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"\n[err] rolled back: {e}")
        raise

    # ── Post-write verification ──────────────────────────────────────────
    print()
    print("=" * 65)
    print("POST-WRITE VERIFICATION")
    print("=" * 65)

    print()
    print("Counts (target: 0 anywhere except expected):")
    expected_zero = [
        ("mti_terms cluster_code='M32'",
         "SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M32'"),
        ("mti_terms cluster_subgroup_id IN (17,18,19)",
         "SELECT COUNT(*) FROM mti_terms WHERE cluster_subgroup_id IN (17,18,19)"),
        ("cluster_subgroup cluster_code='M32'",
         "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M32'"),
        ("cluster_subgroup id IN (17,18,19)",
         "SELECT COUNT(*) FROM cluster_subgroup WHERE id IN (17,18,19)"),
        ("cluster_finding cluster_code='M32'",
         "SELECT COUNT(*) FROM cluster_finding WHERE cluster_code='M32'"),
        ("cluster_finding cluster_subgroup_id IN (17,18,19)",
         "SELECT COUNT(*) FROM cluster_finding WHERE cluster_subgroup_id IN (17,18,19)"),
        ("cluster cluster_code='M32'",
         "SELECT COUNT(*) FROM cluster WHERE cluster_code='M32'"),
    ]
    for label, sql in expected_zero:
        n = cur.execute(sql).fetchone()[0]
        marker = "✓" if n == 0 else "✗ FAIL"
        print(f"  {label:55s} {n}  {marker}")

    print()
    print("Term redistribution:")
    for r in cur.execute(
        "SELECT cluster_code, COUNT(*) AS n "
        "  FROM mti_terms "
        " WHERE id IN ({}) GROUP BY cluster_code".format(
            ",".join("?" * len(ACTIVE_MTI_IDS))
        ),
        ACTIVE_MTI_IDS,
    ):
        print(f"  cluster_code={r['cluster_code']!r:10s} n={r['n']}")

    for mti_id, strongs, target in TERM_REASSIGNMENTS:
        r = cur.execute(
            "SELECT cluster_code, cluster_subgroup_id "
            "  FROM mti_terms WHERE id=?", (mti_id,)
        ).fetchone()
        ok = (r["cluster_code"] == target and r["cluster_subgroup_id"] is None)
        marker = "✓" if ok else "✗ FAIL"
        print(f"  mti={mti_id:5d} {strongs:8s} -> "
              f"cc={r['cluster_code']!r:6s} sg={r['cluster_subgroup_id']!s:5s}  {marker}")

    print()
    print("Term-linked tables (must be unchanged):")
    post_vc = cur.execute(
        "SELECT COUNT(*) FROM verse_context "
        " WHERE mti_term_id IN ({})".format(
            ",".join("?" * len(ACTIVE_MTI_IDS))
        ),
        ACTIVE_MTI_IDS,
    ).fetchone()[0]
    post_vcg = cur.execute(
        "SELECT COUNT(*) FROM verse_context_group "
        " WHERE mti_term_id IN ({})".format(
            ",".join("?" * len(ACTIVE_MTI_IDS))
        ),
        ACTIVE_MTI_IDS,
    ).fetchone()[0]
    print(f"  verse_context: pre={pre_vc} post={post_vc} "
          f"({'unchanged ✓' if pre_vc==post_vc else 'CHANGED ✗'})")
    print(f"  verse_context_group: pre={pre_vcg} post={post_vcg} "
          f"({'unchanged ✓' if pre_vcg==post_vcg else 'CHANGED ✗'})")

    print()
    print("Operations applied:")
    for k, v in counts.items():
        print(f"  {k:35s} {v}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
