"""retire_old_migration_mcode_conflicts_v1_20260906.py — ONE-OFF. Escalation #1525, researcher
instruction verbatim, 2026-09-06: "a single m-code word should never appear twice in different
clusters." Investigation found 675 distinct strongs carrying 2+ live M-code `cluster_strong` tags;
413 of them pair an unverified `old-system-migration` tag (no confidence score, never
independently checked in IBA) with a newer, evidence-based `heuristic-family-grouping-v1-20260905`
tag. A 20-row sample review found the old tag conflicting with the new one is wrong far more often
than not (e.g. "holy" tagged M22 Praise&Song by the old migration vs. correctly M61 Purity&Holiness
by the new pass; "to choose" tagged M37 Firstborn&Foreknowledge vs. correctly M64 Will&Resolve).

Scope of THIS script: only the 413 old-system-migration-vs-heuristic-family-grouping conflicts —
the confident, near-uniformly-one-sided case. The other two conflict shapes found in the same
investigation (176 llm-allocation-vs-heuristic-family-grouping conflicts; 65 auto-precedent-vs-
heuristic-family-grouping conflicts) are explicitly NOT touched here — a sample of the
llm-allocation pairs showed at least one case (G1476 "steadfast") where the OLDER tag looks like
the better fit, so a blanket "newer wins" rule is not safe there without a closer look. Those stay
open, flagged separately on escalation #1525.

What this does, in iba.db, one transaction, direct write (`cluster_strong` is a `category='data'`
table with `writer='migration'` grants): for every strong carrying both an `old-system-migration`
M-code tag and a `heuristic-family-grouping-v1-20260905` M-code tag, soft-deletes the
`old-system-migration` row(s) (`deleted=1`, `rationale` appended not overwritten) and leaves the
newer tag untouched. Idempotent — re-running finds no remaining old+new conflict pairs and does
nothing further.

    python -m iba.app.migration.retire_old_migration_mcode_conflicts_v1_20260906
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_NOTE = (
    " | retired 2026-09-06 (escalation #1525): superseded by a live "
    "heuristic-family-grouping-v1-20260905 tag on the same strong -- sample review found "
    "old-system-migration tags conflicting with a newer evidence-based tag are wrong far more "
    "often than not (e.g. 'holy'->Praise&Song instead of Purity&Holiness). Researcher instruction "
    "verbatim: 'a single m-code word should never appear twice in different clusters.'"
)


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        strongs = [r["strong"] for r in conn.execute(
            "SELECT strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%' "
            "AND source='old-system-migration' "
            "INTERSECT "
            "SELECT strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%' "
            "AND source='heuristic-family-grouping-v1-20260905'")]
        print(f"strongs with an old-migration + heuristic-rebuild M-code conflict: {len(strongs)}")

        retired = 0
        for s in strongs:
            rows = conn.execute(
                "SELECT id, cluster_code, rationale FROM cluster_strong WHERE strong=? "
                "AND deleted=0 AND cluster_code LIKE 'M%' AND source='old-system-migration'",
                (s,)).fetchall()
            for r in rows:
                conn.execute(
                    "UPDATE cluster_strong SET deleted=1, rationale=? WHERE id=?",
                    ((r["rationale"] or "") + _NOTE, r["id"]))
                retired += 1
        conn.commit()
        print(f"rows retired (soft-deleted): {retired}")

        remaining = conn.execute(
            "SELECT COUNT(*) c FROM ("
            "SELECT strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%' "
            "AND source='old-system-migration' "
            "INTERSECT "
            "SELECT strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%' "
            "AND source='heuristic-family-grouping-v1-20260905')").fetchone()["c"]
        print(f"remaining old+new conflicts after fix: {remaining}")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
