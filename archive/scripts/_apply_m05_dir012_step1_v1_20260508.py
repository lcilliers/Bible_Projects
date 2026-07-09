"""_apply_m05_dir012_step1_v1_20260508.py — DB-modifying.

DIR-20260507-M05-012, Step 1 — Structural loader.

Creates 1,512 stub rows in cluster_finding for M05:
  - 7 substantive sub-groups (M05-A..M05-G) x 189 catalogue prompts
    = 1,323 sub-group-scoped stubs
  - 189 cluster-level synthesis stubs (cluster_subgroup_id = NULL)

All stubs:
  - finding_status = 'finding'
  - finding_text   = '[Sub-group not separately addressed in source —
                      see cluster-level finding for this prompt]'
  - source_file    = '[stub-loader-step1]'
  - version        = 'v1'

Step 2 (separate script) parses the four consolidated parts and
promotes / overwrites authored rows.

Idempotent: uses UNIQUE (obs_id, cluster_code, cluster_subgroup_id,
version) — INSERT OR IGNORE skips rows that already exist.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")

CATALOGUE_VERSION = "v2-2026-04-29"
CLUSTER_CODE = "M05"
PATCH_VERSION = "v1"
SOURCE_FILE_STUB = "[stub-loader-step1]"

PLACEHOLDER_TEXT = (
    "[Sub-group not separately addressed in source — see cluster-level "
    "finding for this prompt]"
)

SUBSTANTIVE_SUBGROUPS = (
    "M05-A", "M05-B", "M05-C",
    "M05-D", "M05-E", "M05-F", "M05-G",
)


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    print(f"DB: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Resolve catalogue obs_ids for the directive's catalogue version
    obs_rows = list(conn.execute(
        "SELECT obs_id, question_code, tier "
        "  FROM wa_obs_question_catalogue "
        " WHERE catalogue_version=? AND COALESCE(deleted,0)=0 "
        " ORDER BY obs_id",
        (CATALOGUE_VERSION,),
    ))
    print(f"Catalogue rows for version {CATALOGUE_VERSION!r}: {len(obs_rows)}")
    if len(obs_rows) != 189:
        print(f"[err] expected 189 catalogue rows, got {len(obs_rows)}")
        return 1

    # Resolve substantive sub-group ids
    sg_id_by_code = {}
    for code in SUBSTANTIVE_SUBGROUPS:
        r = conn.execute(
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

    n_sg_inserted = 0
    n_cluster_inserted = 0
    n_skipped = 0
    ts = now_iso()

    try:
        conn.execute("BEGIN")

        # 1,323 sub-group-scoped stubs
        for obs in obs_rows:
            for code, sg_id in sg_id_by_code.items():
                cur = conn.execute(
                    "INSERT OR IGNORE INTO cluster_finding "
                    "  (obs_id, cluster_code, cluster_subgroup_id, "
                    "   finding_status, finding_text, source_file, "
                    "   version, created_at, last_updated_date, "
                    "   delete_flagged) "
                    "VALUES (?, ?, ?, 'finding', ?, ?, ?, ?, ?, 0)",
                    (obs["obs_id"], CLUSTER_CODE, sg_id,
                     PLACEHOLDER_TEXT, SOURCE_FILE_STUB,
                     PATCH_VERSION, ts, ts),
                )
                if cur.rowcount:
                    n_sg_inserted += 1
                else:
                    n_skipped += 1

        # 189 cluster-level stubs (cluster_subgroup_id = NULL)
        for obs in obs_rows:
            cur = conn.execute(
                "INSERT OR IGNORE INTO cluster_finding "
                "  (obs_id, cluster_code, cluster_subgroup_id, "
                "   finding_status, finding_text, source_file, "
                "   version, created_at, last_updated_date, "
                "   delete_flagged) "
                "VALUES (?, ?, NULL, 'finding', ?, ?, ?, ?, ?, 0)",
                (obs["obs_id"], CLUSTER_CODE,
                 PLACEHOLDER_TEXT, SOURCE_FILE_STUB,
                 PATCH_VERSION, ts, ts),
            )
            if cur.rowcount:
                n_cluster_inserted += 1
            else:
                n_skipped += 1

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    total = n_sg_inserted + n_cluster_inserted
    print()
    print(f"Sub-group stubs inserted:    {n_sg_inserted:5d}  "
          f"(expected 1,323)")
    print(f"Cluster-level stubs inserted: {n_cluster_inserted:5d}  "
          f"(expected   189)")
    print(f"Total inserted:               {total:5d}  "
          f"(expected 1,512)")
    print(f"Already-present (skipped):    {n_skipped:5d}")

    # Verification
    print()
    print("Verification — M05 cluster_finding row counts:")
    for r in conn.execute(
        "SELECT "
        "  CASE WHEN cluster_subgroup_id IS NULL THEN 'CLUSTER-LEVEL' "
        "       ELSE (SELECT subgroup_code FROM cluster_subgroup "
        "             WHERE id=cluster_finding.cluster_subgroup_id) END "
        "    AS scope, "
        "  finding_status, COUNT(*) AS n "
        "  FROM cluster_finding "
        " WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 "
        " GROUP BY scope, finding_status "
        " ORDER BY scope, finding_status",
        (CLUSTER_CODE,),
    ):
        print(f"  {r['scope']:15s} {r['finding_status']:20s} {r['n']:5d}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
