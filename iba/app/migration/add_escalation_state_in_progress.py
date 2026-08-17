"""add_escalation_state_in_progress.py — ONE-OFF: adds `'in-progress'` to `cfg_enum`
`escalation_state` (escalations #673/#674, researcher: *"create new escalation state 'in progress',
this is to keep tasks open that is not yet signed off or busy working on such as engine"*).

Code-paired, not a standalone value tweak — `_terminal_state_for()`/`complete_run()` (`lib/
escalation.py`) only make sense with this enum row present, same reasoning `bootstrap_step_kind.py`
used for `operations`/`utility`. Migration script, not `configmaint.propose`.

    python -m iba.app.migration.add_escalation_state_in_progress
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)

    existing = conn.execute(
        "SELECT 1 FROM cfg_enum WHERE name='escalation_state' AND value='in-progress'").fetchone()
    if existing:
        print("cfg_enum escalation_state already has 'in-progress' — nothing to do.")
        conn.close()
        return 0

    ordinal = conn.execute(
        "SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_enum WHERE name='escalation_state'"
    ).fetchone()[0]
    conn.execute(
        "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES "
        "('escalation_state', 'in-progress', ?, 0)", (ordinal,))
    conn.commit()
    conn.close()

    print(f"cfg_enum escalation_state 'in-progress' added, ordinal={ordinal}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
