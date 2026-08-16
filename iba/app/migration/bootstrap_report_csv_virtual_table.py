"""bootstrap_report_csv_virtual_table.py — ONE-OFF: closes a false-positive `configmaint.validate`
finding that has been re-raised three times (escalations #591, #597, #642) over five days without
ever being fixed, each time against a different mutated table_name as someone tried to patch the
symptom rather than the check.

**Root cause, confirmed by reading the actual code, not guessed:** `find_bad_report_csv_table_references`
(`lib/cfgquality.py`) requires every `cfg_report_csv_table.table_name` to be a real SQL table.  Two
rows aren't — `report.registry`/`word_registry_strong_pairing` and `report.cluster`/
`strong_without_cluster` — but they were never broken: `reportkit.write_csv_pairing` accepts a
`row_filter` dict that supplies pre-computed rows for a `table_name` INSTEAD of running
`SELECT * FROM {table_name}`, and both `lib/registryreport.py` and `lib/clusterreport.py` already
pass exactly these two keys in their own `row_filter` calls. The CSV export has always worked
correctly at runtime; only the STATIC validator couldn't see the `row_filter` escape hatch and
flagged it every single `configmaint.validate` run.

**Fix:** a `virtual` column on `cfg_report_csv_table` — a row_filter-supplied CSV pairing, not a
literal table dump, still required to carry a `join_note` explaining what it is. The validator skips
the known-table check for `virtual=1` rows but still requires the `join_note`, so an actually-wrong
future entry can't hide behind this exemption silently.

    python -m iba.app.migration.bootstrap_report_csv_virtual_table
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_VIRTUAL_ROWS = [
    ("report.registry", "word_registry_strong_pairing"),
    ("report.cluster", "strong_without_cluster"),
]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    cols = [r[1] for r in conn.execute("PRAGMA table_info(cfg_report_csv_table)")]
    if "virtual" not in cols:
        conn.execute(
            "ALTER TABLE cfg_report_csv_table ADD COLUMN virtual INTEGER NOT NULL DEFAULT 0")
        report.append("cfg_report_csv_table.virtual column added")
    else:
        report.append("cfg_report_csv_table.virtual column already present")

    for step, table_name in _VIRTUAL_ROWS:
        row = conn.execute(
            "SELECT join_note, virtual FROM cfg_report_csv_table WHERE step=? AND table_name=?",
            (step, table_name)).fetchone()
        if row is None:
            report.append(f"MISSING ROW ({step}, {table_name!r}) — nothing to mark, check by hand")
            continue
        if row[0] is None:
            report.append(f"REFUSING ({step}, {table_name!r}) — no join_note, would hide a real "
                          f"gap behind the exemption; not marked virtual")
            continue
        if row[1] == 1:
            report.append(f"({step}, {table_name!r}) already virtual")
        else:
            conn.execute(
                "UPDATE cfg_report_csv_table SET virtual=1 WHERE step=? AND table_name=?",
                (step, table_name))
            report.append(f"({step}, {table_name!r}) marked virtual")

    conn.commit()
    conn.close()

    print("report-csv virtual-table bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
