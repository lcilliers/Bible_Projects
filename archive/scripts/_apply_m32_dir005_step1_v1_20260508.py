"""_apply_m32_dir005_step1_v1_20260508.py — DB-modifying.

DIR-20260508-004 (dir-005), Step A — Structural loader for M32.

Inserts stub rows into cluster_finding for M32:
  - 2 substantive sub-groups (M32-A, M32-B) x 189 catalogue prompts
    = 378 sub-group-scoped stubs
  - 189 cluster-level stubs (cluster_subgroup_id = NULL)

All stubs:
  - finding_status = 'finding'
  - finding_text   = '[Sub-group not separately addressed in source —
                      see cluster-level finding for this prompt]'
  - source_file    = '[stub-loader-step1]'
  - version        = 'v1'

BOUNDARY rows are inserted in step3_boundary (separate, T1.2.1 only,
keyed to cluster_subgroup_id of M32-BOUNDARY).

Idempotent: UNIQUE (obs_id, cluster_code, cluster_subgroup_id, version)
+ INSERT OR IGNORE.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")

CATALOGUE_VERSION = "v2-2026-04-29"
CLUSTER_CODE = "M32"
PATCH_VERSION = "v1"
SOURCE_FILE_STUB = "[stub-loader-step1]"

PLACEHOLDER_TEXT = (
    "[Sub-group not separately addressed in source — see cluster-level "
    "finding for this prompt]"
)

SUBSTANTIVE_SUBGROUPS = ("M32-A", "M32-B")


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    obs_rows = list(cur.execute(
        "SELECT obs_id FROM wa_obs_question_catalogue "
        " WHERE catalogue_version=? AND COALESCE(deleted,0)=0 "
        " ORDER BY obs_id",
        (CATALOGUE_VERSION,),
    ))
    print(f"Catalogue rows for {CATALOGUE_VERSION!r}: {len(obs_rows)}")
    if len(obs_rows) != 189:
        print(f"[err] expected 189 catalogue rows, got {len(obs_rows)}")
        return 1

    sg_id_by_code: dict[str, int] = {}
    for code in SUBSTANTIVE_SUBGROUPS:
        r = cur.execute(
            "SELECT id FROM cluster_subgroup "
            " WHERE cluster_code=? AND subgroup_code=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (CLUSTER_CODE, code),
        ).fetchone()
        if not r:
            print(f"[err] sub-group {code} not found")
            return 2
        sg_id_by_code[code] = r["id"]
    print("Sub-group ids:", sg_id_by_code)

    n_sg = 0
    n_cluster = 0
    n_skipped = 0
    ts = now_iso()

    try:
        cur.execute("BEGIN")
        for obs in obs_rows:
            for code, sg_id in sg_id_by_code.items():
                rc = cur.execute(
                    "INSERT OR IGNORE INTO cluster_finding "
                    "  (obs_id, cluster_code, cluster_subgroup_id, "
                    "   finding_status, finding_text, source_file, "
                    "   version, created_at, last_updated_date, "
                    "   delete_flagged) "
                    "VALUES (?, ?, ?, 'finding', ?, ?, ?, ?, ?, 0)",
                    (obs["obs_id"], CLUSTER_CODE, sg_id,
                     PLACEHOLDER_TEXT, SOURCE_FILE_STUB,
                     PATCH_VERSION, ts, ts),
                ).rowcount
                if rc:
                    n_sg += 1
                else:
                    n_skipped += 1
        for obs in obs_rows:
            rc = cur.execute(
                "INSERT OR IGNORE INTO cluster_finding "
                "  (obs_id, cluster_code, cluster_subgroup_id, "
                "   finding_status, finding_text, source_file, "
                "   version, created_at, last_updated_date, "
                "   delete_flagged) "
                "VALUES (?, ?, NULL, 'finding', ?, ?, ?, ?, ?, 0)",
                (obs["obs_id"], CLUSTER_CODE,
                 PLACEHOLDER_TEXT, SOURCE_FILE_STUB,
                 PATCH_VERSION, ts, ts),
            ).rowcount
            if rc:
                n_cluster += 1
            else:
                n_skipped += 1
        cur.execute("COMMIT")
    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    total = n_sg + n_cluster
    print()
    print(f"Sub-group stubs inserted:    {n_sg}  (expected 378)")
    print(f"Cluster-level stubs inserted: {n_cluster}  (expected 189)")
    print(f"Total inserted:              {total}  (expected 567)")
    print(f"Skipped (already existed):   {n_skipped}")

    print()
    print("Verification — M32 cluster_finding row counts:")
    for r in cur.execute(
        "SELECT "
        "  CASE WHEN cluster_subgroup_id IS NULL THEN 'CLUSTER-LEVEL' "
        "       ELSE (SELECT subgroup_code FROM cluster_subgroup "
        "             WHERE id=cluster_finding.cluster_subgroup_id) END "
        "    AS scope, "
        "  COUNT(*) AS n "
        "  FROM cluster_finding "
        " WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 "
        " GROUP BY scope ORDER BY scope",
        (CLUSTER_CODE,),
    ):
        print(f"  {r['scope']:15s} {r['n']:5d}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
