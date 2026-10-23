"""guard_review_sc16_2228_2220_v1_20261023.py -- two decided changes, researcher 2026-10-23:

- #2228 decision (1): "any verse selection above 2500 should be subject to a review before proceeding".
  cfg_setting verse_scope.max_verses 4000 -> 2500, its use rewritten: a larger result is held for review and
  proceeds only with -Reviewed "<the review>", recorded in the answer.
- #2220 decision B: SC16 does not count a designed stop as a failure. New cfg_setting
  session_close.sc16_designed_stops (module validation, as the other session_close settings): the texts by
  which a designed stop is known.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path)
in the same transaction. Idempotent.

Usage:
    python iba/app/migration/guard_review_sc16_2228_2220_v1_20261023.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2228-2220-GUARD-SC16-20261023"
MODULE = "guard_review_sc16_2228_2220_v1_20261023"
GUARD_USE = ("size guard on the scope resolver: a request whose result has more verses is held for review before it "
             "proceeds (researcher 2026-10-23, #2228: 'any verse selection above 2500 should be subject to a review "
             "before proceeding'). It proceeds only with -Reviewed \"<the review>\", given after the researcher has "
             "reviewed it, and the review is recorded in the answer. Clusters above it: M72 (3,972), M47 (2,841), "
             "M65 (2,568)")
STOPS = ["COMMIT BLOCKED", "NOT PASSED", "a config change needs researcher approval"]
STOPS_USE = ("SC16 (repeated failures, iba/app/handlers/session_close.py): a failed tool result carrying one of these "
             "texts is a tool stopping by design, not a failure, and is not counted -- Session-Close.ps1 'COMMIT "
             "BLOCKED', Compliance.ps1 'NOT PASSED', configmaint.propose 'a config change needs researcher approval' "
             "(cfg_on_fail needs-approval). A real hard error, also exit 3, is still counted (#2220 decision B, "
             "researcher 2026-10-23)")


def plan(conn) -> list[tuple]:
    ops = []
    row = conn.execute("SELECT value, use FROM cfg_setting WHERE key='verse_scope.max_verses'").fetchone()
    if row and (json.loads(row[0]), row[1]) != (2500, GUARD_USE):
        ops.append(("cfg_setting", "update", {"key": "verse_scope.max_verses"}, {"value": "2500", "use": GUARD_USE}))
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key='session_close.sc16_designed_stops'").fetchone():
        ops.append(("cfg_setting", "insert", {}, {"key": "session_close.sc16_designed_stops", "value": json.dumps(STOPS),
                                                  "module": "validation", "inactive": 0, "use": STOPS_USE}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- #2228 (verse_scope.max_verses 2500, held for review) and #2220 B "
                       f"(session_close.sc16_designed_stops); run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run or not ops:
        print(f"{'DRY RUN -- ' if a.dry_run else 'already applied -- '}{len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
