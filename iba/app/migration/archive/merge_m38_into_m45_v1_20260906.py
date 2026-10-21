"""merge_m38_into_m45_v1_20260906.py — ONE-OFF. Escalation #1525, researcher instruction verbatim,
2026-09-06: "merge M38 into M45 and mark M38 as deleted." Found in the same member-overlap scan
that surfaced M29/M18 (BUILD.md #241): `M38` (Restoration & Revival, 53 members) and `M45`
(Renewal & Transformation, 22 members) share 4 members outright (18.2% of the smaller cluster).

What this does, in iba.db, one transaction, direct write (`cluster`/`cluster_strong` are
`category='data'` tables with `writer='migration'` grants — same regime as the M10b/M58 and
M29/M18 merges this follows the exact pattern of):

  1. For M38's live members NOT already tagged to M45: REASSIGN (UPDATE in place, not a new row)
     to M45, `rationale` appended not overwritten.
  2. For M38's live members ALREADY also tagged to M45 (the overlap strongs): the M38 row is
     simply retired (soft-deleted) — no duplicate M45 row created.
  3. M45's `description`/`gloss` absorb M38's own text (appended, not overwritten).
  4. RETIRE M38: `cluster.deleted=1`. No physical delete, per project convention.

Idempotent: checks M38's live/deleted state and no-ops if already retired.

    python -m iba.app.migration.merge_m38_into_m45_v1_20260906
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_FROM, _INTO = "M38", "M45"


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    report: list[str] = []
    try:
        src = conn.execute(
            "SELECT cluster_code, description, gloss, deleted FROM cluster "
            f"WHERE cluster_code='{_FROM}'").fetchone()
        if src is None:
            report.append(f"{_FROM}: no cluster row found -- nothing to merge, aborting")
            print("merge_m38_into_m45_v1_20260906:")
            for line in report:
                print(f"  - {line}")
            return 1
        if src["deleted"] == 1:
            report.append(f"{_FROM} already retired (deleted=1) -- no-op")
            print("merge_m38_into_m45_v1_20260906:")
            for line in report:
                print(f"  - {line}")
            return 0

        dst = conn.execute(
            "SELECT description, gloss FROM cluster "
            f"WHERE cluster_code='{_INTO}'").fetchone()
        if dst is None:
            report.append(f"{_INTO}: no cluster row found -- cannot merge into it, aborting")
            print("merge_m38_into_m45_v1_20260906:")
            for line in report:
                print(f"  - {line}")
            return 1

        dst_strongs = {r["strong"] for r in conn.execute(
            "SELECT strong FROM cluster_strong WHERE cluster_code=? AND deleted=0", (_INTO,))}

        rows = conn.execute(
            "SELECT id, strong, rationale FROM cluster_strong "
            "WHERE cluster_code=? AND deleted=0", (_FROM,)).fetchall()
        relocated = 0
        already_overlapped = 0
        for row in rows:
            if row["strong"] in dst_strongs:
                conn.execute(
                    "UPDATE cluster_strong SET deleted=1, rationale=? WHERE id=?",
                    ((row["rationale"] or "") + (
                        f" | retired 2026-09-06 (escalation #1525): merged {_FROM}->{_INTO}, "
                        f"already had a live {_INTO} row for this strong -- no duplicate created"),
                     row["id"]))
                already_overlapped += 1
                report.append(f"{row['strong']}: already in {_INTO} -- {_FROM} row retired, no duplicate")
            else:
                new_rationale = (row["rationale"] or "") + (
                    f" | relocated {_FROM}->{_INTO} 2026-09-06 (escalation #1525: "
                    f"'merge {_FROM} into {_INTO} and mark {_FROM} as deleted', researcher verbatim)")
                conn.execute(
                    "UPDATE cluster_strong SET cluster_code=?, rationale=? WHERE id=?",
                    (_INTO, new_rationale, row["id"]))
                relocated += 1
                report.append(f"{row['strong']}: relocated {_FROM} -> {_INTO} (id={row['id']})")

        merged_description = dst["description"]
        if src["description"] and src["description"] not in (merged_description or ""):
            merged_description = f"{merged_description} (absorbed {_FROM}: {src['description']})"
        merged_gloss = dst["gloss"] or ""
        if src["gloss"] and src["gloss"] not in merged_gloss:
            merged_gloss = (merged_gloss + ", " if merged_gloss else "") + src["gloss"]

        conn.execute(
            "UPDATE cluster SET description=?, gloss=? WHERE cluster_code=?",
            (merged_description, merged_gloss, _INTO))
        report.append(f"{_INTO}: description/gloss updated to absorb {_FROM}'s evidence base")

        conn.execute("UPDATE cluster SET deleted=1 WHERE cluster_code=?", (_FROM,))
        report.append(
            f"{_FROM}: retired (deleted=1) -- {relocated} member(s) relocated to {_INTO}, "
            f"{already_overlapped} already-overlapping member(s) retired without duplication")

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print("merge_m38_into_m45_v1_20260906:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
