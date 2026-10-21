"""fix_from_id_mutability_20260821.py — escalation #763: `from_id` was built immutable-after-Raise,
directly contradicting the researcher's own recorded instruction (`escalation` #6 v5, 2026-08-20):
*"both fields are available as an optional pair on BOTH Raise and Update (not immutable-after-raise
-- researcher confirmed it can be re-pointed/corrected later, which also lets legacy messy chains
... be retrofitted after the fact)"*.

**Root cause, investigated, not guessed**: register v7 (`escalation-design-decision-
register-v7-20260821.md`) recorded D14 in full, correctly — its own `cfg_column.use` text says
*"optional, mutable (settable on Raise or Update alike)"*, and all 4 `cfg_escalation_requirement`
rows are written `action='raise'/'update'`. The v9 consolidation pass (superseding v1-v8) summarised
D14 more tersely and silently dropped the mutability/dual-action detail. The code (this same
session, same day) was then written from v9's thinner text, without checking back against v7 or
the `#6` history already read multiple times that same session -- filling the gap with the wrong
default (modelled on `run_id`'s immutability) instead.

**This migration's job**: bring `cfg_column`/`cfg_escalation_requirement` in line with what was
actually decided. The code fix (from_id moved from `_IMMUTABLE_COLS` to `_REPLACE_COLS`, `update()`
gained a `from_id` parameter) is in `lib/escalation.py`, this same commit.

    python -m iba.app.migration.fix_from_id_mutability_20260821
"""

from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # ── cfg_column.use corrected, both tables ─────────────────────────────────────────────────
    conn.execute(
        "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='escalation' AND "
        "name='from_id'",
        ("The id of the escalation this item builds on -- optional, MUTABLE (settable on Raise or "
         "Update alike, D14, register v7's own recorded wording -- corrected 2026-08-21, escalation "
         "#763, after being built immutable-after-Raise the first time, contradicting the "
         "researcher's own recorded instruction, escalation #6 v5). Paired with related_activity "
         "describing the relationship. State of the referenced item is irrelevant -- any state is "
         "a valid target.",))
    conn.execute(
        "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='escalation_history' AND "
        "name='from_id'",
        ("Delta: NULL unless THIS version's own transaction set/changed from_id -- mutable (D14, "
         "corrected 2026-08-21, escalation #763), not structural/immutable like run_id/source/"
         "at_step/type/raised_at.",))
    print("cfg_column: escalation/escalation_history .from_id.use corrected (mutable, not "
         "structural)")

    # ── cfg_escalation_requirement: duplicate the 3 from_id checks under action='update' too ───
    new_reqs = [
        ("update", "from_id", "always", "exists",
         "from_id, if set, must reference an existing escalation id (D14)."),
        ("update", "from_id", "always", "not_self",
         "from_id, if set, must not equal this item's own id (D14)."),
        ("update", "related_activity", "from_id_set", "field_required",
         "from_id is set this transaction -- related_activity must be paired with it (the current "
         "value counts), naming what the relationship documents (D14)."),
    ]
    for action, field, condition_key, check_kind, message in new_reqs:
        conn.execute("DELETE FROM cfg_escalation_requirement WHERE action=? AND field=? AND "
                     "check_kind=?", (action, field, check_kind))
        conn.execute(
            "INSERT INTO cfg_escalation_requirement (action, field, condition_key, check_kind, "
            "message, active) VALUES (?,?,?,?,?,1)",
            (action, field, condition_key, check_kind, message))
    print(f"cfg_escalation_requirement: {len(new_reqs)} new row(s) (action='update', mirroring "
         f"the 3 action='raise' from_id checks)")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
