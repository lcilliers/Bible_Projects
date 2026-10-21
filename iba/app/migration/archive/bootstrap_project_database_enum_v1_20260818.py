"""bootstrap_project_database_enum_v1_20260818.py — ONE-OFF, idempotent: escalation #723's core
fix. Decomposes `governance.project_databases` (prose, unstructured) into a queryable source:

  - `cfg_enum` group `project_database` — member rows `iba`, `bible_research`.
  - `cfg_setting database.iba.path` / `database.bible_research.path` — each database's file path.

`governance.project_databases` itself is left in place (human-readable orientation, includes
`bible_research.db`'s "aka research_db" alias which these structured facts don't need to carry) —
per `documentation.single-authority-pointer-not-copy` (cfg_behaviour_rule), the two are not
duplicates: the prose is for a human reading GOVERNANCE.md, these are for code that needs to
iterate over "every known project database" without parsing a sentence.

Researcher's refinement of the original sketch (chat, 2026-08-18): named `database.<name>.path`
rather than a flatter key, matching the `<module>.<key>` convention already used throughout
`cfg_setting` (`backup.*`, `content_index.*`, ...) instead of inventing a new shape.

    python -m iba.app.migration.bootstrap_project_database_enum_v1_20260818
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH


def _enum(conn, name, value, report):
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, value)).fetchone():
        n = conn.execute("SELECT COUNT(*) FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
        conn.execute("INSERT INTO cfg_enum VALUES (?,?,?,0)", (name, value, n))
        report.append(f"cfg_enum {name} += {value!r}")
    else:
        report.append(f"cfg_enum {name} already has {value!r}")


def _setting(conn, key, value, use, module, report):
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
        conn.execute("INSERT INTO cfg_setting (key, value, use, module) VALUES (?,?,?,?)",
                    (key, value, use, module))
        report.append(f"cfg_setting {key!r} added")
    else:
        report.append(f"cfg_setting {key!r} already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    for db in ("iba", "bible_research"):
        _enum(conn, "project_database", db, report)

    _enum(conn, "config_module", "database", report)

    _setting(conn, "database.iba.path", json.dumps("iba/app/db/iba.db"),
             "iba.db's file path, project-root-relative -- structured counterpart to "
             "governance.project_databases' prose, part of escalation #723's project_database "
             "enum + path settings.", "database", report)
    _setting(conn, "database.bible_research.path", json.dumps("database/bible_research.db"),
             "bible_research.db's file path, project-root-relative (aka research_db in prose "
             "elsewhere -- that alias isn't repeated here, see governance.project_databases). "
             "Structured counterpart, escalation #723.", "database", report)

    conn.commit()
    conn.close()

    print("project_database enum + path settings bootstrap (escalation #723):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
