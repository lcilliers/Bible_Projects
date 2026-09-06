"""resolve_mcode_conflicts_review_flag_v1_20260906.py — ONE-OFF. Escalation #1525. Researcher
instruction verbatim, 2026-09-06: "the csv ... have a 1 in the review_flag column to set M-code
for every row. where the review_flag = 0, the row must be removed from the M-code." Checked live
before applying: of the 134 then-remaining multi-tagged strongs, only 14 actually carry the
pattern this rule needs (exactly one side `review_flag=1`, the other `0`) — the other 120 have
`review_flag=0` on BOTH conflicting rows, so the rule as stated can't resolve them (it would strip
both M-code tags, not pick one). This script applies ONLY the 14 clean cases; the 120 ambiguous
ones are untouched, left for the researcher's direction.

What this does, in iba.db, one transaction, direct write (same regime as #245/#246): for each of
the 14 strongs, retires the `review_flag=0` cluster's `cluster_strong` row (`rationale` appended);
the `review_flag=1` row is untouched. Neither cluster is merged/retired.

    python -m iba.app.migration.resolve_mcode_conflicts_review_flag_v1_20260906
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        strongs = [r["strong"] for r in conn.execute(
            "SELECT strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%' "
            "GROUP BY strong HAVING COUNT(DISTINCT cluster_code)>1")]

        retired = 0
        skipped_ambiguous = 0
        for s in strongs:
            rows = conn.execute(
                "SELECT id, cluster_code, review_flag, rationale FROM cluster_strong "
                "WHERE strong=? AND deleted=0 AND cluster_code LIKE 'M%'", (s,)).fetchall()
            flags = sorted(r["review_flag"] for r in rows)
            if flags != [0, 1]:
                skipped_ambiguous += 1
                continue
            for r in rows:
                if r["review_flag"] == 0:
                    new_rationale = (r["rationale"] or "") + (
                        " | retired 2026-09-06 (escalation #1525): review_flag=0 vs. the "
                        "review_flag=1 tag on the same strong, researcher instruction verbatim")
                    conn.execute(
                        "UPDATE cluster_strong SET deleted=1, rationale=? WHERE id=?",
                        (new_rationale, r["id"]))
                    retired += 1
                    print(f"{s}: retired {r['cluster_code']} (review_flag=0)")
        conn.commit()
        print(f"\nrows retired: {retired}")
        print(f"strongs skipped (both review_flag=0, ambiguous, not a clean 0/1 pair): {skipped_ambiguous}")

        remaining = conn.execute(
            "SELECT COUNT(*) c FROM ("
            "SELECT strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%' "
            "GROUP BY strong HAVING COUNT(DISTINCT cluster_code)>1)").fetchone()["c"]
        print(f"total multi-tagged M-code strongs remaining corpus-wide: {remaining}")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
