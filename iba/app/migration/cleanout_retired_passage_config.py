"""cleanout_retired_passage_config.py — ONE-OFF: hard-deletes config rows for the retired
HIB-continuity passage algorithm (superseded 2026-08-06 by the input-scope redefinition, BUILD.md
§67), rather than leaving them soft-deleted/inactive as permanent clutter.

**Authorization.** Researcher, 2026-08-06, direct chat instruction: *"go ahead and cleanout the
configs - I am OK with you hard deleting stuff that was added at some point and then replaced, and
then softdeleted."* This is the up-front, explicit authorization this carve-out needs — scoped
narrowly to rows that were added, then genuinely replaced by the redesign, matching exactly what
the researcher described. NOT treated as blanket approval for the separate, still-pending
`configmaint.propose` batches that ADD new capability (the `hib_kind` enum, `closing.set`'s
registration) — those are a different kind of decision and are left pending, untouched.

**What this removes, and why each one qualifies:**

1. `cfg_setting` — `passage.default_rule`, `passage.cross_chapter`, `passage.min_shared_hibs`,
   `passage.review_over`. The HIB-continuity run-forming algorithm these configured no longer
   exists in `handlers/passage.py` (confirmed: no `.setting()` call for any of the four remains in
   that file). `passage.quality_report_path`/`passage.debate_session_chapter_guideline` are NOT
   touched — both are still genuinely read (`passage.validate`, `Chapter-Generate.ps1`).
2. `cfg_enum` — both `passage_rule` values (`hib-continuity`, `maximal`). The whole enum is
   obsolete, not just one value: `passage.rule` is now a hardcoded literal (`"input-scope"`) set
   by the code itself, never a payload-supplied value an analyst chooses — unlike `hib_kind`,
   nothing will ever need to validate an incoming `rule` against this set again. The earlier
   `RUN-ADD-ENUM-INPUTSCOPE` proposal (insert an `input-scope` value) is rejected alongside this,
   not applied — adding a value to an enum nothing checks against anymore would be its own kind of
   clutter.
3. `cfg_method_rule` — the 5 original `passage.build` rows from the HIB-continuity build
   (`hib-continuity-boundary`, `min-shared-hibs`, `no-cross-chapter`, `review-over-threshold`,
   `protect-content-on-rebuild`) — superseded by the 5 rows the redesign already inserted
   (`input-scope-is-the-passage`, `story-synthesis-required`, `feasibility-self-assessment`,
   `one-passage-per-verse`, `legacy-superseded-unconditionally`). **Corrects a real doc/DB
   mismatch, caught while scoping this cleanup**: `debate-pipeline-technical-reference-
   20260806.md` already claimed these five were "now active=0, superseded not deleted" — they were
   never actually deactivated in the DB at all. This migration is what makes that claim true,
   rather than leaving the reference document ahead of the database it's supposed to describe.

**Not covered by this authorization, deliberately left alone:** the 5 pending `configmaint.propose`
retirement escalations this cleanup makes moot (`RUN-RETIRE-passage-min_shared_hibs/cross_chapter/
default_rule/review_over`, `RUN-RETIRE-ENUM-1`, `RUN-ADD-ENUM-INPUTSCOPE`) are answered `reject`
via `Escalation.ps1` in the same session, pointing at this migration, so the queue doesn't carry a
stale "soft-deactivate" request for a row that's already gone.

    python -m iba.app.migration.cleanout_retired_passage_config
"""
from __future__ import annotations

import sqlite3

DB_PATH = "iba/app/db/iba.db"

SETTINGS_TO_DELETE = [
    "passage.default_rule", "passage.cross_chapter",
    "passage.min_shared_hibs", "passage.review_over",
]
ENUM_NAME = "passage_rule"
METHOD_RULE_STEP = "passage.build"
METHOD_RULE_KEYS_TO_DELETE = [
    "hib-continuity-boundary", "min-shared-hibs", "no-cross-chapter",
    "review-over-threshold", "protect-content-on-rebuild",
]


def run(conn: sqlite3.Connection) -> None:
    before = {
        "cfg_setting": conn.execute(
            f"SELECT COUNT(*) FROM cfg_setting WHERE key IN "
            f"({','.join('?' * len(SETTINGS_TO_DELETE))})", SETTINGS_TO_DELETE).fetchone()[0],
        "cfg_enum": conn.execute(
            "SELECT COUNT(*) FROM cfg_enum WHERE name=?", (ENUM_NAME,)).fetchone()[0],
        "cfg_method_rule": conn.execute(
            f"SELECT COUNT(*) FROM cfg_method_rule WHERE step=? AND rule_key IN "
            f"({','.join('?' * len(METHOD_RULE_KEYS_TO_DELETE))})",
            (METHOD_RULE_STEP, *METHOD_RULE_KEYS_TO_DELETE)).fetchone()[0],
    }

    conn.execute(
        f"DELETE FROM cfg_setting WHERE key IN ({','.join('?' * len(SETTINGS_TO_DELETE))})",
        SETTINGS_TO_DELETE)
    conn.execute("DELETE FROM cfg_enum WHERE name=?", (ENUM_NAME,))
    conn.execute(
        f"DELETE FROM cfg_method_rule WHERE step=? AND rule_key IN "
        f"({','.join('?' * len(METHOD_RULE_KEYS_TO_DELETE))})",
        (METHOD_RULE_STEP, *METHOD_RULE_KEYS_TO_DELETE))
    conn.commit()

    print(f"cfg_setting rows deleted: {before['cfg_setting']} (of {len(SETTINGS_TO_DELETE)} named)")
    print(f"cfg_enum '{ENUM_NAME}' rows deleted: {before['cfg_enum']}")
    print(f"cfg_method_rule '{METHOD_RULE_STEP}' rows deleted: {before['cfg_method_rule']} "
          f"(of {len(METHOD_RULE_KEYS_TO_DELETE)} named)")


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    run(conn)
    conn.close()
