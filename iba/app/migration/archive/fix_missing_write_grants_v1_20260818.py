"""fix_missing_write_grants_v1_20260818.py — ONE-OFF, idempotent. Two small housekeeping fixes
surfaced live by `configmaint.validate` while verifying `bootstrap_behaviour_rules_v1_20260818.py`:

1. Closes escalation #716 (hard coherence error): `cfg_method_rule` and `cfg_quality_check` had no
   `cfg_write_grant` row for writer `configmaint.propose`, so nothing could maintain them through
   the sanctioned gate (`governance.config_control`). Pre-existing gap, unrelated to the behaviour-
   rules bootstrap -- same one-line pattern used for every other cfg_* table.

2. Closes the `bootstrap_behaviour_rules` zero-Cfg-method-call-sites finding (CONFIG-REPORT
   item #118, advisory not blocking): marks `cfg_utility.config_exempt=1` for it. It's a one-off
   migration script that writes directly into cfg_* tables via raw sqlite3 (creates + populates
   them) -- the exact same class already exempted for `cfgload`
   ("writes the seed INTO the cfg_* tables ... same class as migration/ scripts, already excluded
   from usage-checks for the same reason"). Applying an already-established exemption class to a
   new instance, not a new judgement call.

    python -m iba.app.migration.fix_missing_write_grants_v1_20260818
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    for table in ("cfg_method_rule", "cfg_quality_check"):
        if not conn.execute(
                "SELECT 1 FROM cfg_write_grant WHERE writer='configmaint.propose' "
                "AND table_name=? AND database='iba'", (table,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
                "VALUES ('configmaint.propose', ?, 'iba', 0)", (table,))
            report.append(f"cfg_write_grant ('configmaint.propose', {table!r}) added")
        else:
            report.append(f"cfg_write_grant ('configmaint.propose', {table!r}) already present")

    exempt_reason = ("one-off migration script -- writes directly into cfg_* tables via raw "
                     "sqlite3 (creates + populates them), same class as cfgload.py, already "
                     "exempted from usage-checks for the same reason.")
    row = conn.execute(
        "SELECT config_exempt FROM cfg_utility WHERE module='bootstrap_behaviour_rules'").fetchone()
    if row and row[0] != 1:
        conn.execute(
            "UPDATE cfg_utility SET config_exempt=1, config_exempt_reason=? "
            "WHERE module='bootstrap_behaviour_rules'", (exempt_reason,))
        report.append("cfg_utility 'bootstrap_behaviour_rules' marked config_exempt=1")
    elif row:
        report.append("cfg_utility 'bootstrap_behaviour_rules' already config_exempt=1")
    else:
        report.append("cfg_utility 'bootstrap_behaviour_rules' not found -- skipped")

    conn.commit()
    conn.close()

    print("missing write-grant + config-exempt fix (escalation #716 / CONFIG-REPORT #118):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
