"""_apply_m26_phase3_to_db_v1_20260509.py — DB-modifying.

Script 1 of M26 Phase 4 sequence. Commits the Phase 3 hypothesis
(provisional sub-group structure from
outputs/markdown/m26-phase3-debate-results-claude-sonnet-4-6-20260509.json)
to the database so subsequent phases can use the FK chain
verse_context.mti_term_id -> mti_terms.cluster_subgroup_id ->
cluster_subgroup.

Operations (single transaction, foreign_keys=ON):
  1. INSERT 8 cluster_subgroup rows (M26-A..G + M26-BOUNDARY)
  2. UPDATE mti_terms.cluster_subgroup_id for 38 placed terms
     (1 FLAGGED term left at NULL, awaiting researcher decision)

Idempotent: pre-flight aborts if any sub-group already exists.

NO API calls. ~2 sec wall time. No cost.
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
PHASE3_JSON = os.path.join(
    "outputs", "markdown",
    "m26-phase3-debate-results-claude-sonnet-4-6-20260509.json"
)


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    if not Path(PHASE3_JSON).exists():
        print(f"[err] Phase 3 result not found: {PHASE3_JSON}")
        return 2

    with open(PHASE3_JSON, encoding="utf-8") as f:
        p3 = json.load(f)
    result = p3["result"]

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()
    ts = now_iso()

    # ── Pre-flight ────────────────────────────────────────────────────
    print("=" * 65)
    print("PRE-FLIGHT")
    print("=" * 65)

    n_existing = cur.execute(
        "SELECT COUNT(*) FROM cluster_subgroup "
        " WHERE cluster_code='M26' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    if n_existing > 0:
        print(f"[err] {n_existing} M26 sub-groups already exist in DB. "
              "Script is idempotent — re-running will halt; manual cleanup "
              "needed if state is bad.")
        return 1

    # All Phase 3 strongs must resolve to mti_term_ids in M26
    strongs_in_p3 = set()
    for sg in result["subgroups"]:
        for t in sg["terms"]:
            strongs_in_p3.add(t["strong"])
    for t in result["boundary"]["terms"]:
        strongs_in_p3.add(t["strong"])
    for t in result["flagged"]:
        strongs_in_p3.add(t["strong"])

    db_terms = {
        r["strongs_number"]: r["id"]
        for r in cur.execute(
            "SELECT id, strongs_number FROM mti_terms "
            " WHERE cluster_code='M26' AND COALESCE(delete_flagged,0)=0"
        )
    }

    missing = strongs_in_p3 - set(db_terms.keys())
    extra = set(db_terms.keys()) - strongs_in_p3
    print(f"  Phase 3 strongs: {len(strongs_in_p3)}")
    print(f"  M26 active mti_terms: {len(db_terms)}")
    if missing:
        print(f"  [err] Phase 3 strongs not in M26 DB: {sorted(missing)}")
        return 2
    if extra:
        print(f"  [warn] M26 DB strongs not in Phase 3: {sorted(extra)}")
        # Don't halt — these would just keep cluster_subgroup_id=NULL
    print("  OK — proceeding.")

    # ── Execute ──────────────────────────────────────────────────────
    print()
    print("=" * 65)
    print("EXECUTE")
    print("=" * 65)

    counts = {"subgroups_inserted": 0, "terms_assigned": 0,
              "terms_flagged": 0}
    sg_id_by_code: dict[str, int] = {}

    try:
        cur.execute("BEGIN")

        # Insert sub-groups (M26-A through G in order, then BOUNDARY)
        for i, sg in enumerate(result["subgroups"], start=1):
            cur.execute(
                "INSERT INTO cluster_subgroup "
                "  (cluster_code, subgroup_code, label, core_description, "
                "   sort_order, status, version, source, "
                "   delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, 'Active', 'v1', "
                "        'M26 Phase 3 hypothesis (claude-sonnet-4-6)', "
                "        0, ?, ?)",
                (
                    "M26", sg["code"], sg["label"],
                    sg["characteristic_definition"],
                    i, ts, ts,
                ),
            )
            sg_id_by_code[sg["code"]] = cur.lastrowid
            counts["subgroups_inserted"] += 1
            print(f"  + cluster_subgroup INSERT {sg['code']} -> "
                  f"id={cur.lastrowid}")

        # BOUNDARY
        cur.execute(
            "INSERT INTO cluster_subgroup "
            "  (cluster_code, subgroup_code, label, core_description, "
            "   sort_order, status, version, source, "
            "   delete_flagged, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, 'Active', 'v1', "
            "        'M26 Phase 3 hypothesis (claude-sonnet-4-6)', "
            "        0, ?, ?)",
            (
                "M26", "M26-BOUNDARY", "BOUNDARY",
                result["boundary"]["rationale"],
                len(result["subgroups"]) + 1, ts, ts,
            ),
        )
        sg_id_by_code["M26-BOUNDARY"] = cur.lastrowid
        counts["subgroups_inserted"] += 1
        print(f"  + cluster_subgroup INSERT M26-BOUNDARY -> "
              f"id={cur.lastrowid}")

        # Update mti_terms.cluster_subgroup_id per Phase 3 placement
        for sg in result["subgroups"]:
            sg_id = sg_id_by_code[sg["code"]]
            for t in sg["terms"]:
                mti_id = db_terms[t["strong"]]
                rc = cur.execute(
                    "UPDATE mti_terms "
                    "   SET cluster_subgroup_id=?, last_changed=? "
                    " WHERE id=? AND cluster_code='M26' "
                    "   AND COALESCE(delete_flagged,0)=0",
                    (sg_id, ts, mti_id),
                ).rowcount
                if rc != 1:
                    raise RuntimeError(
                        f"mti_terms UPDATE for {t['strong']} (mti={mti_id}) "
                        f"expected 1 row, got {rc}"
                    )
                counts["terms_assigned"] += 1

        for t in result["boundary"]["terms"]:
            mti_id = db_terms[t["strong"]]
            rc = cur.execute(
                "UPDATE mti_terms "
                "   SET cluster_subgroup_id=?, last_changed=? "
                " WHERE id=? AND cluster_code='M26' "
                "   AND COALESCE(delete_flagged,0)=0",
                (sg_id_by_code["M26-BOUNDARY"], ts, mti_id),
            ).rowcount
            if rc != 1:
                raise RuntimeError(
                    f"BOUNDARY mti_terms UPDATE for {t['strong']} "
                    f"expected 1 row, got {rc}"
                )
            counts["terms_assigned"] += 1

        # FLAGGED terms — leave cluster_subgroup_id at NULL
        for t in result["flagged"]:
            print(f"  - {t['strong']} ({t['transliteration']}) FLAGGED — "
                  f"cluster_subgroup_id stays NULL: {t['issue']}")
            counts["terms_flagged"] += 1

        cur.execute("COMMIT")
        print()
        print("COMMIT successful.")
    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"\n[err] rolled back: {e}")
        raise

    # ── Verification ─────────────────────────────────────────────────
    print()
    print("=" * 65)
    print("POST-WRITE VERIFICATION")
    print("=" * 65)
    print()
    print("Sub-group → term counts:")
    for r in cur.execute(
        "SELECT cs.subgroup_code, cs.label, COUNT(mt.id) AS n "
        "  FROM cluster_subgroup cs "
        "  LEFT JOIN mti_terms mt ON mt.cluster_subgroup_id=cs.id "
        "    AND COALESCE(mt.delete_flagged,0)=0 "
        " WHERE cs.cluster_code='M26' "
        "   AND COALESCE(cs.delete_flagged,0)=0 "
        " GROUP BY cs.subgroup_code "
        " ORDER BY cs.sort_order"
    ):
        print(f"  {r['subgroup_code']:14s} {r['label'][:40]:40s} {r['n']}")

    n_unassigned = cur.execute(
        "SELECT COUNT(*) FROM mti_terms "
        " WHERE cluster_code='M26' AND cluster_subgroup_id IS NULL "
        "   AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print()
    print(f"M26 active terms with cluster_subgroup_id=NULL "
          f"(FLAGGED): {n_unassigned}")
    if n_unassigned != counts["terms_flagged"]:
        print(f"  [warn] expected {counts['terms_flagged']} flagged, "
              f"got {n_unassigned}")

    print()
    print("Operations applied:")
    for k, v in counts.items():
        print(f"  {k:30s} {v}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
