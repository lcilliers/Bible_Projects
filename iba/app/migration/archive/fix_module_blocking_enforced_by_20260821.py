"""fix_module_blocking_enforced_by_20260821.py — escalation #746: cfg_escalation's 7(now 10) rule
rows checked against today's live model, per direct instruction ("proceed to check if this is
still relevant, if so then fix").

Checked all 10 active rows individually against the real, current code (not assumed): 9 of 10 are
accurate as written -- several explicitly document their own 2026-08-20 corrections
(`source_classification`, `document_reference_grouping`), the rest correctly self-describe as
"session practice, not mechanically enforced" where that's true (`resolution_precedence`,
`chat_routing`, `document_reference_grouping`, `full_path_file_references`), or name a real,
existing function (`duplicate_suppression` -> `escalation.open_duplicate`). One row, `module_blocking`,
is genuinely stale: `enforced_by` reads "not yet wired -- scheduled as a task escalation, see the
reset's backlog pass", but the mechanism has been live since 2026-08-17 --
`run.py:run_step()`'s third dispatch gate, citing escalation #646 explicitly (confirmed by reading
the code directly, lines ~135-154). `escalations_old` #646 itself (completed, frozen, not in the
live table) is literally the item that did the wiring -- its own recorded text says "enforced_by
currently says 'not yet wired'", meaning the correction was simply never carried back to
`cfg_escalation` once #646 closed.

    python -m iba.app.migration.fix_module_blocking_enforced_by_20260821
"""

from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "UPDATE cfg_escalation SET enforced_by=? WHERE rule_key='module_blocking'",
        ("run.py:run_step()'s third dispatch gate (escalation #646, 2026-08-17) -- checks for an "
         "unresolved escalation (state IN raised/re-assigned) against either the exact step "
         "(at_step=step_id) or the owning module (source=<module prefix>), refuses to dispatch if "
         "found. Live and wired; corrected 2026-08-21 (escalation #746) -- was stale, still read "
         "'not yet wired' after #646 (the item that built this) closed.",))
    conn.commit()
    conn.close()
    print("cfg_escalation: module_blocking.enforced_by corrected")


if __name__ == "__main__":
    main()
