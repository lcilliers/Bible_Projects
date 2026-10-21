"""repair_dan8_daniel_phenomenon_hib_id_20260808.py — ONE-OFF, idempotent: repoints Dan 8 passage
37465's 17 orphaned `phenomenon.hib_id=22` rows to the live "Daniel" hib row (`hib_id=47`).

**Background.** Found live, 2026-08-08, as a side effect of the `operation.set` no-op regression
test (BUILD.md §82): all 17 of Dan 8's "Daniel" phenomenon rows pointed at `hib_id=22`, a
soft-deleted ("Daniel", `deleted=1`) row — not the current live Daniel (`hib_id=47`). Residue from
an older `hib.set` correction, before the 2026-08-07 update-in-place fix, that changed Daniel's id
without repointing the phenomena already written against the old one. Reported as escalation
`MANUAL-20260808_052156_904168` rather than silently patched (this touches real analytical content,
not just mechanism) — **answered `approve`, "repair now"**. This script is that repair.

**Scope, exact.** `UPDATE phenomenon SET hib_id=47 WHERE hib_id=22 AND deleted=0` — 17 rows,
confirmed live before running. Nothing else touched: `operation`/`operation_party` reference
`phenomenon_id`, not `hib_id`, directly, so they need no change; `operation_party.hib_id` already
had zero orphaned references (checked live, same investigation).

**Audited like every other debate-table write this session** (BUILD.md §81/§82,
`lib/debateaudit.py`) — logs one `debate_change_detail` row per repointed phenomenon, `writer=
'repair.dan8_daniel_hib_id'`, so this repair is traceable the same way a real `hib.set`/
`phenomenon.set` call would be, not a silent raw UPDATE.

    python -m iba.app.migration.repair_dan8_daniel_phenomenon_hib_id_20260808
"""

from __future__ import annotations

import datetime
import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

OLD_HIB_ID, NEW_HIB_ID = 22, 47
RUN_ID = "MIGRATION-repair-dan8-daniel-hib-id-20260808"
WRITER = "repair.dan8_daniel_hib_id"


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run(conn: sqlite3.Connection) -> list[str]:
    report: list[str] = []

    # Idempotency: has this exact repair already run? Check the audit trail, not just row state
    # (row state alone can't distinguish "never needed" from "already repaired").
    already = conn.execute(
        "SELECT COUNT(*) FROM debate_change_detail WHERE run_id=?", (RUN_ID,)).fetchone()[0]
    if already:
        report.append(f"already applied ({already} debate_change_detail row(s) from a prior run) "
                      "-- nothing to do")
        return report

    rows = conn.execute(
        "SELECT id FROM phenomenon WHERE hib_id=? AND deleted=0 AND passage_id=37465",
        (OLD_HIB_ID,)).fetchall()
    if not rows:
        report.append(f"no live phenomenon rows with hib_id={OLD_HIB_ID} in passage 37465 -- "
                      "nothing to repair (already fixed some other way, or the finding was stale)")
        return report

    now = _now()
    for (phen_id,) in rows:
        conn.execute("UPDATE phenomenon SET hib_id=? WHERE id=?", (NEW_HIB_ID, phen_id))
        conn.execute(
            "INSERT INTO debate_change_detail (run_id, writer, table_name, op, where_json, "
            "set_json, before_json, applied_at) VALUES (?,?,?,?,?,?,?,?)",
            (RUN_ID, WRITER, "phenomenon", "update", json.dumps({"id": phen_id}),
             json.dumps({"hib_id": NEW_HIB_ID}), json.dumps({"hib_id": OLD_HIB_ID}), now))
    report.append(f"{len(rows)} phenomenon row(s) repointed hib_id {OLD_HIB_ID} -> {NEW_HIB_ID} "
                 f"(passage 37465, Dan 8), logged to debate_change_detail under run_id={RUN_ID!r}")

    conn.commit()
    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report = run(conn)
    conn.close()
    print("Dan 8 Daniel phenomenon.hib_id repair (escalation MANUAL-20260808_052156_904168, "
         "approved 'repair now'):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
