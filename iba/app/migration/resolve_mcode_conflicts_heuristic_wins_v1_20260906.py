"""resolve_mcode_conflicts_heuristic_wins_v1_20260906.py — ONE-OFF. Escalation #1525. Researcher
instruction verbatim, 2026-09-06: "I have decided that in each case the heuristic-family-grouping-
v1-20260905 item wins, the other one goes." Checked live before applying: all 120 then-remaining
multi-tagged M-code strongs (the residue after #245/#246/#247's title/synonym/review_flag passes)
have exactly one side tagged `heuristic-family-grouping-v1-20260905` and the other tagged
`llm-allocation-v1_3-20260811` or `auto-precedent` — no anomalies (0 strongs with 0 or 2 heuristic
sides), so the rule is unambiguous for the full remaining set.

What this does, in iba.db, one transaction, direct write (same regime as #239/#245/#246/#247): for
each of the 120 strongs, retires the NON-heuristic cluster's `cluster_strong` row (`rationale`
appended); the `heuristic-family-grouping-v1-20260905` row is untouched. Neither cluster is
merged/retired.

    python -m iba.app.migration.resolve_mcode_conflicts_heuristic_wins_v1_20260906
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_HEURISTIC_SOURCE = "heuristic-family-grouping-v1-20260905"


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        strongs = [r["strong"] for r in conn.execute(
            "SELECT strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%' "
            "GROUP BY strong HAVING COUNT(DISTINCT cluster_code)>1")]

        retired = 0
        skipped_anomaly = 0
        for s in strongs:
            rows = conn.execute(
                "SELECT id, cluster_code, source, rationale FROM cluster_strong "
                "WHERE strong=? AND deleted=0 AND cluster_code LIKE 'M%'", (s,)).fetchall()
            heuristic_rows = [r for r in rows if r["source"] == _HEURISTIC_SOURCE]
            other_rows = [r for r in rows if r["source"] != _HEURISTIC_SOURCE]
            if len(heuristic_rows) != 1 or not other_rows:
                skipped_anomaly += 1
                print(f"{s}: SKIPPED -- not exactly one heuristic side ({len(heuristic_rows)} heuristic, {len(other_rows)} other)")
                continue
            for r in other_rows:
                new_rationale = (r["rationale"] or "") + (
                    f" | retired 2026-09-06 (escalation #1525): superseded by a live "
                    f"heuristic-family-grouping-v1-20260905 tag on the same strong, researcher "
                    f"instruction verbatim: 'in each case the heuristic-family-grouping item "
                    f"wins, the other one goes'")
                conn.execute(
                    "UPDATE cluster_strong SET deleted=1, rationale=? WHERE id=?",
                    (new_rationale, r["id"]))
                retired += 1
                print(f"{s}: retired {r['cluster_code']} (source={r['source']})")
        conn.commit()
        print(f"\nrows retired: {retired}")
        print(f"strongs skipped (anomaly): {skipped_anomaly}")

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
