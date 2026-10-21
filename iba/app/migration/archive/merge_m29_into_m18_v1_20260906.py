"""merge_m29_into_m18_v1_20260906.py — ONE-OFF. Escalation #1525, researcher instruction verbatim,
2026-09-06: "merge M29 into M18 and set M29 as deleted." Found while cross-referencing a
member-overlap scan across all 85 live M-clusters: M18 (Desire & Longing, 95 members) and M29
(Desire, 25 members) share 7 members already (`G1372`/`G1373`/`G20833`/`G7114`/`G8013`/`H0404`/
`H6772`), and M29 received zero new members from the 2026-09-05 family-reallocation rebuild — the
same systemic gap already fixed once for M10b/M58 (BUILD.md #237): the rebuild's heuristic pass
never cross-checked its own new "desire" family (absorbed into M18) against the pre-existing,
narrower M29 cluster it already substantially overlapped.

What this does, in iba.db, one transaction, direct write (`cluster`/`cluster_strong` are
`category='data'` tables with `writer='migration'` grants — same regime as the M10b/M58 merge this
follows the exact pattern of):

  1. For M29's live members NOT already tagged to M18: REASSIGN (UPDATE in place, not a new row)
     to M18, `rationale` appended not overwritten — same "relocated" pattern as M10b->M58.
  2. For M29's live members ALREADY also tagged to M18 (the 7 overlap strongs): the M29 row is
     simply retired (soft-deleted) — M18 already has its own row for that strong, so no duplicate
     M18 row is created.
  3. M18's `description`/`gloss` absorb M29's own text (appended, not overwritten) — M29's own
     gloss list (acceptance/be willing/chosen/eagerness/intention/to will/will-desire) would
     otherwise be lost.
  4. RETIRE M29: `cluster.deleted=1`. No physical delete, per project convention.

Idempotent: checks M29's live/deleted state and no-ops if already retired.

    python -m iba.app.migration.merge_m29_into_m18_v1_20260906
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    report: list[str] = []
    try:
        m29 = conn.execute(
            "SELECT cluster_code, description, gloss, deleted FROM cluster "
            "WHERE cluster_code='M29'").fetchone()
        if m29 is None:
            report.append("M29: no cluster row found -- nothing to merge, aborting")
            print("merge_m29_into_m18_v1_20260906:")
            for line in report:
                print(f"  - {line}")
            return 1
        if m29["deleted"] == 1:
            report.append("M29 already retired (deleted=1) -- no-op")
            print("merge_m29_into_m18_v1_20260906:")
            for line in report:
                print(f"  - {line}")
            return 0

        m18 = conn.execute(
            "SELECT description, gloss FROM cluster WHERE cluster_code='M18'").fetchone()
        if m18 is None:
            report.append("M18: no cluster row found -- cannot merge into it, aborting")
            print("merge_m29_into_m18_v1_20260906:")
            for line in report:
                print(f"  - {line}")
            return 1

        m18_strongs = {r["strong"] for r in conn.execute(
            "SELECT strong FROM cluster_strong WHERE cluster_code='M18' AND deleted=0")}

        rows = conn.execute(
            "SELECT id, strong, rationale FROM cluster_strong "
            "WHERE cluster_code='M29' AND deleted=0").fetchall()
        relocated = 0
        already_overlapped = 0
        for row in rows:
            if row["strong"] in m18_strongs:
                conn.execute(
                    "UPDATE cluster_strong SET deleted=1, rationale=? WHERE id=?",
                    ((row["rationale"] or "") + (
                        " | retired 2026-09-06 (escalation #1525): merged M29->M18, "
                        "already had a live M18 row for this strong -- no duplicate created"),
                     row["id"]))
                already_overlapped += 1
                report.append(f"{row['strong']}: already in M18 -- M29 row retired, no duplicate")
            else:
                new_rationale = (row["rationale"] or "") + (
                    " | relocated M29->M18 2026-09-06 (escalation #1525: 'merge M29 into M18 "
                    "and set M29 as deleted', researcher verbatim)")
                conn.execute(
                    "UPDATE cluster_strong SET cluster_code='M18', rationale=? WHERE id=?",
                    (new_rationale, row["id"]))
                relocated += 1
                report.append(f"{row['strong']}: relocated M29 -> M18 (id={row['id']})")

        merged_description = m18["description"]
        if m29["description"] and m29["description"] not in (merged_description or ""):
            merged_description = f"{merged_description} (absorbed M29: {m29['description']})"
        merged_gloss = m18["gloss"] or ""
        if m29["gloss"] and m29["gloss"] not in merged_gloss:
            merged_gloss = (merged_gloss + ", " if merged_gloss else "") + m29["gloss"]

        conn.execute(
            "UPDATE cluster SET description=?, gloss=? WHERE cluster_code='M18'",
            (merged_description, merged_gloss))
        report.append("M18: description/gloss updated to absorb M29's evidence base")

        conn.execute("UPDATE cluster SET deleted=1 WHERE cluster_code='M29'")
        report.append(
            f"M29: retired (deleted=1) -- {relocated} member(s) relocated to M18, "
            f"{already_overlapped} already-overlapping member(s) retired without duplication")

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print("merge_m29_into_m18_v1_20260906:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
