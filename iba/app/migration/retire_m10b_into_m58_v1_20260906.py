"""retire_m10b_into_m58_v1_20260906.py — ONE-OFF. Escalation #1525 (cluster membership/readiness):
M58 and M10b were found to be the ONLY duplicate `short_name` ("Wickedness") among all 85 live
M-clusters. M58 (5 strongs, all `source='heuristic-family-grouping-v1-20260905'`,
`rationale='family=wickedness-ungodliness'`) and M10b (43 strongs, description "Wickedness, Evil
and Abomination", a pre-existing gloss list already covering wicked/wickedness/evil/abomination)
occupy the same semantic territory with zero member-strong overlap — the 2026-09-05
family-reallocation heuristic minted a new "wickedness" family without checking it against the
pre-existing M10b. Researcher's own verdict, verbatim, this chat turn: "I suggest we retire M10b
and keep M58."

What this does, in iba.db, all in one transaction, direct writes (`cluster`/`cluster_strong` are
`category='data'` tables with `writer='migration'` grants — not `configmaint.propose` territory,
same regime as the 2026-09-05 `add_adversarial_cluster` and `family_reallocation` scripts this
follows the exact pattern of):

  1. REASSIGN (UPDATE in place, not a new row) M10b's 43 live `cluster_strong` members to M58,
     `rationale` appended not overwritten — same "relocated" pattern as the 2026-08-13 M10->M10b
     refinement and the 2026-09-05 T4 adversarial reallocation.
  2. Carry M10b's gloss list forward onto the surviving M58 row (M58's own `gloss` is empty today —
     the 43 relocated members' evidence base would otherwise be lost) — appended, not silently
     discarded, and M58's `description` gains M10b's wording alongside its own so the merge is
     traceable from the cluster row itself, not only from `cluster_strong.rationale`.
  3. RETIRE M10b: `cluster.deleted=1`. No physical delete, per project convention (soft-delete
     only).

Idempotent: checks M10b's live/deleted state and no-ops if already retired.

    python -m iba.app.migration.retire_m10b_into_m58_v1_20260906
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
        m10b = conn.execute(
            "SELECT cluster_code, description, gloss, deleted FROM cluster "
            "WHERE cluster_code='M10b'").fetchone()
        if m10b is None:
            report.append("M10b: no cluster row found at all -- nothing to retire, aborting")
            print("retire_m10b_into_m58_v1_20260906:")
            for line in report:
                print(f"  - {line}")
            return 1
        if m10b["deleted"] == 1:
            report.append("M10b already retired (deleted=1) -- no-op, nothing further done")
            print("retire_m10b_into_m58_v1_20260906:")
            for line in report:
                print(f"  - {line}")
            return 0

        m58 = conn.execute(
            "SELECT description, gloss FROM cluster WHERE cluster_code='M58'").fetchone()
        if m58 is None:
            report.append("M58: no cluster row found -- cannot merge into it, aborting")
            print("retire_m10b_into_m58_v1_20260906:")
            for line in report:
                print(f"  - {line}")
            return 1

        rows = conn.execute(
            "SELECT id, strong, rationale FROM cluster_strong "
            "WHERE cluster_code='M10b' AND deleted=0").fetchall()
        for row in rows:
            new_rationale = (row["rationale"] or "") + (
                " | relocated M10b->M58 2026-09-06 (escalation #1525: M58/M10b confirmed the only "
                "duplicate short_name 'Wickedness' among live M-clusters, zero member overlap; "
                "researcher verdict verbatim: 'retire M10b and keep M58')")
            conn.execute(
                "UPDATE cluster_strong SET cluster_code='M58', rationale=? WHERE id=?",
                (new_rationale, row["id"]))
            report.append(f"{row['strong']}: reallocated M10b -> M58 (id={row['id']})")

        merged_description = m58["description"]
        if m10b["description"] and m10b["description"] not in (merged_description or ""):
            merged_description = f"{merged_description} (absorbed M10b: {m10b['description']})"
        merged_gloss = m58["gloss"] or ""
        if m10b["gloss"] and m10b["gloss"] not in merged_gloss:
            merged_gloss = (merged_gloss + ", " if merged_gloss else "") + m10b["gloss"]

        conn.execute(
            "UPDATE cluster SET description=?, gloss=? WHERE cluster_code='M58'",
            (merged_description, merged_gloss))
        report.append("M58: description/gloss updated to absorb M10b's evidence base")

        conn.execute("UPDATE cluster SET deleted=1 WHERE cluster_code='M10b'")
        report.append(f"M10b: retired (deleted=1), {len(rows)} member(s) relocated to M58")

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print("retire_m10b_into_m58_v1_20260906:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
