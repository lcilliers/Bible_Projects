"""add_obs_catalogue_source_last_modified_and_update_tool_v1_20260831.py — ONE-OFF, idempotent.
Escalation #1007. Researcher instruction (verbatim, this chat turn): add two columns to
`wa_obs_question_catalogue` (bible_research.db) --

1. `source` TEXT, default NULL -- "Describe how the answer to the question is sourced."
2. `last_modified` -- "record when row was last updated."

-- then build the table's update tool. Schema is DDL (2 new columns), so -- same class of
exception as every other schema addition in `iba/app/migration/` (`bootstrap_inactive_column.py`,
`add_cfg_table_purpose_and_success_columns_20260830.py`, ...) -- a direct, documented, idempotent
bootstrap, not a `configmaint.propose` call (that gate governs changing an EXISTING row's value in
a `cfg_*` table; `wa_obs_question_catalogue` is ordinary content, not `cfg_*`, and DDL itself is
outside `configmaint.propose`'s scope either way). Targets `bible_research.db` via
`database.bible_research.path`, not the `iba.db` `DB_PATH` constant every prior schema migration in
this directory used -- first migration script to do so, following the exact cross-database pattern
`cataloguereport.py`/`prosestore.py` already established for READS/writes at runtime
(`cfg.database_path('bible_research')`); a standalone migration script has no live `Cfg` instance,
so the setting is read directly here with the same fallback `Cfg.database_path()` itself documents
(`iba.db` bootstraps via the hardcoded constant; every other database is a genuine config read).

`last_modified` stored as TEXT ISO-8601 UTC, matching the project's universal date convention
(SQLite has no native DATETIME type; every other `*_at`/`date_*` column in the schema is TEXT
ISO-8601) -- "datetime" in the instruction names the semantic type, not a SQLite column affinity.

Also registers the `catalogue-update` work package / `obs_catalogue.update` step / write grant /
utility rows for the new update tool (`iba/app/lib/cataloguewrite.py` +
`iba/app/handlers/catalogue.py` + `iba/app/ps/Catalogue-Update.ps1`), following the exact pattern
`bootstrap_catalogue_overview_report_v1_20260829.py` established for this same escalation's
read-side tool (`report.obs_catalogue`) -- work_package/step/utility rows bootstrapped directly
here, not proposed, matching that precedent and `fix_missing_write_grants_v1_20260818.py`'s
established exemption for `cfg_write_grant` (one-off migration scripts write cfg_* rows directly,
same class as `cfgload.py`).

    python -m iba.app.migration.add_obs_catalogue_source_last_modified_and_update_tool_v1_20260831
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_TABLE = "wa_obs_question_catalogue"
_WP = "catalogue-update"
_STEP = "obs_catalogue.update"
_HANDLER = "iba.app.handlers.catalogue:update"
_PS_SCRIPT = "iba/app/ps/Catalogue-Update.ps1"
_LIB_PATH = "iba/app/lib/cataloguewrite.py"
_HANDLER_PATH = "iba/app/handlers/catalogue.py"


def _has_column(conn: sqlite3.Connection, table: str, col: str) -> bool:
    return any(r[1] == col for r in conn.execute(f'PRAGMA table_info("{table}")'))


def _research_db_path(iba_conn: sqlite3.Connection) -> str:
    """Same resolution `Cfg.database_path('bible_research')` performs at runtime, done here with
    raw SQL because a standalone migration script has no live `Cfg` instance to call it on."""
    row = iba_conn.execute(
        "SELECT value FROM cfg_setting WHERE key='database.bible_research.path'").fetchone()
    if not row:
        raise RuntimeError("no database.bible_research.path setting -- run Start-Iba.ps1 first")
    rel = json.loads(row[0])
    repo_root = DB_PATH.resolve().parent.parent.parent.parent
    return str(repo_root / rel)


def main() -> int:
    iba_conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    # ── 1. Schema DDL on bible_research.db ──────────────────────────────────────────────────
    research_path = _research_db_path(iba_conn)
    rconn = sqlite3.connect(research_path)
    try:
        if _has_column(rconn, _TABLE, "source"):
            report.append(f"{_TABLE}.source already exists — skipped")
        else:
            rconn.execute(f'ALTER TABLE "{_TABLE}" ADD COLUMN "source" TEXT')
            report.append(f"{_TABLE}.source added (TEXT, default NULL)")

        if _has_column(rconn, _TABLE, "last_modified"):
            report.append(f"{_TABLE}.last_modified already exists — skipped")
        else:
            rconn.execute(f'ALTER TABLE "{_TABLE}" ADD COLUMN "last_modified" TEXT')
            report.append(f"{_TABLE}.last_modified added (TEXT, ISO-8601 UTC, default NULL)")
        rconn.commit()
    finally:
        rconn.close()

    # ── 2. cfg_column rows for the 2 new columns (database='bible_research') ───────────────
    for name, use_text in (
        ("source", "Free-text description of how the answer to this question is sourced -- "
                    "e.g. which table/field, or that it requires interpretive reading/judgment. "
                    "Populated per escalation #1007's tier-catalogue-to-IBA-raw-data mapping "
                    "(Workflow/Catalogue/1007-tier-catalogue-iba-raw-data-mapping-v2-20260831.md) for "
                    "the 126 live tiered questions; NULL elsewhere until reviewed."),
        ("last_modified", "ISO-8601 UTC timestamp of this row's last update via "
                          "obs_catalogue.update (iba/app/ps/Catalogue-Update.ps1). Auto-set by "
                          "that tool on every write unless the caller explicitly overrides it; "
                          "NULL on a row never touched by the tool."),
    ):
        exists = iba_conn.execute(
            "SELECT 1 FROM cfg_column WHERE database='bible_research' AND table_name=? "
            "AND name=?", (_TABLE, name)).fetchone()
        if exists:
            report.append(f"cfg_column row for {_TABLE}.{name} already exists — skipped")
            continue
        ordinal = iba_conn.execute(
            "SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_column WHERE database='bible_research' "
            "AND table_name=?", (_TABLE,)).fetchone()[0]
        iba_conn.execute(
            "INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "
            "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by, inactive) "
            "VALUES ('bible_research',?,?,?,'TEXT',0,0,0,NULL,NULL,?,NULL,?,?,0)",
            (_TABLE, name, ordinal, use_text, "escalation #1007, 2026-08-31",
             "this migration (DDL) + obs_catalogue.update (values)"))
        report.append(f"cfg_column row for {_TABLE}.{name} added")

    # ── 3. cfg_work_package ──────────────────────────────────────────────────────────────
    if not iba_conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (_WP,)).fetchone():
        iba_conn.execute(
            "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained) VALUES (?,?,'none',0)",
            (_WP, _PS_SCRIPT))
        report.append(f"cfg_work_package {_WP!r} added")
    else:
        report.append(f"cfg_work_package {_WP!r} already present")

    # ── 4. cfg_step ──────────────────────────────────────────────────────────────────────
    if not iba_conn.execute("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?",
                            (_WP, _STEP)).fetchone():
        iba_conn.execute(
            "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, inactive, "
            "kind) VALUES (?,?,?,?,?,?,?,?)",
            (_WP, 0, _STEP, _HANDLER, "none",
             "Partial UPDATE of one wa_obs_question_catalogue row (bible_research.db), keyed by "
             "obs_id. Every column except obs_id is settable; columns not named in -Set are left "
             "untouched. Auto-fills last_modified (now, UTC) and catalogue_version (v2-<today>) "
             "when the caller doesn't supply them explicitly -- either is still overridable by "
             "naming it in -Set. No history/audit table -- researcher's own call, escalation "
             "#1007: 'I dont think there is any history control on this table and I don't think "
             "it is necessary.'",
             0, "utility"))
        report.append(f"cfg_step {_STEP!r} added")
    else:
        report.append(f"cfg_step {_STEP!r} already present")

    # ── 5. cfg_write_grant ───────────────────────────────────────────────────────────────
    if not iba_conn.execute(
            "SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='bible_research'",
            (_STEP, _TABLE)).fetchone():
        iba_conn.execute(
            "INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
            "VALUES (?,?,'bible_research',0)", (_STEP, _TABLE))
        report.append(f"cfg_write_grant ({_STEP!r}, {_TABLE!r}, bible_research) added")
    else:
        report.append(f"cfg_write_grant ({_STEP!r}, {_TABLE!r}, bible_research) already present")

    # ── 6. cfg_utility rows (the new lib file, the new handler file, and this migration) ───
    for module, path, purpose, inactive in (
        ("cataloguewrite", _LIB_PATH,
         f"{_STEP} -- validated partial UPDATE of wa_obs_question_catalogue by obs_id, "
         "auto-filling last_modified/catalogue_version where not explicitly given. Escalation #1007.",
         0),
        ("handlers_catalogue", _HANDLER_PATH,
         f"Thin dispatcher adapter over cataloguewrite.py, registers {_STEP} as a work-package step.",
         0),
    ):
        if not iba_conn.execute("SELECT 1 FROM cfg_utility WHERE file_path=?", (path,)).fetchone():
            iba_conn.execute(
                "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt) "
                "VALUES (?,?,?,?,0)", (module, path, purpose, inactive))
            report.append(f"cfg_utility {path!r} added")
        else:
            report.append(f"cfg_utility {path!r} already present")

    _self_path = ("iba/app/migration/"
                 "add_obs_catalogue_source_last_modified_and_update_tool_v1_20260831.py")
    if not iba_conn.execute("SELECT 1 FROM cfg_utility WHERE file_path=?", (_self_path,)).fetchone():
        iba_conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt) "
            "VALUES (?,?,?,1,0)",
            ("add_obs_catalogue_source_last_modified_and_update_tool_v1_20260831", _self_path,
             "ONE-OFF migration, escalation #1007 -- adds wa_obs_question_catalogue.source/"
             "last_modified (bible_research.db DDL) and registers the catalogue-update work "
             "package/step/write-grant/utility rows. inactive=1 once applied -- a one-off, not a "
             "reusable routine."))
        report.append(f"cfg_utility (self) {_self_path!r} added")
    else:
        report.append(f"cfg_utility (self) {_self_path!r} already present")

    iba_conn.commit()
    iba_conn.close()

    print("obs_catalogue source/last_modified + catalogue-update tool bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
