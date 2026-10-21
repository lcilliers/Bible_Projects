"""backfill_foundational_cfg_tables_v1_20260818.py — ONE-OFF, idempotent. Part 1 of `#712`'s
two-part follow-on (researcher instruction, 2026-08-18: "first complete #712, then we can get back
to the sweep for 715"). Registers the 20 foundational `cfg_*` tables — the ones the app has run on
since before `cfg_table`/`governance.tables` existed, so they were never backfilled into their own
registry — in `cfg_table`/`cfg_column`, per `governance.tables`/`governance.table_columns`.

Every `use`/description below is written from this table's OWN live rows (schema + sample data
actually queried, 2026-08-18), not guessed from the table name.

Part 2 (switching `handlers/configmaint.py`'s hardcoded `CFG_TABLES` tuple to derive from
`cfg_table` dynamically, now that this backfill closes the gap that blocked it) is the companion
script, run after this one: `switch_cfg_tables_dynamic_v1_20260818.py`.

    python -m iba.app.migration.backfill_foundational_cfg_tables_v1_20260818
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def _table_and_columns(conn, name, grain, use, columns, report):
    if not conn.execute("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", (name,)).fetchone():
        conn.execute("INSERT INTO cfg_table (database, name, grain, \"use\") VALUES ('iba',?,?,?)",
                    (name, grain, use))
        report.append(f"cfg_table {name!r} added")
    else:
        report.append(f"cfg_table {name!r} already present")
    for ordinal, (col, coltype, ispk, notnull, colnuse) in enumerate(columns):
        if not conn.execute(
                "SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?",
                (name, col)).fetchone():
            conn.execute(
                "INSERT INTO cfg_column (database, table_name, name, ordinal, \"type\", is_pk, "
                "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by) "
                "VALUES ('iba',?,?,?,?,?,?,0,NULL,NULL,?,NULL,NULL,"
                "'migration/backfill_foundational_cfg_tables_v1_20260818.py')",
                (name, col, ordinal, coltype, ispk, notnull, colnuse))
            report.append(f"cfg_column ({name}.{col}) added")
        else:
            report.append(f"cfg_column ({name}.{col}) already present")


# (table, grain, use, [(col, type, is_pk, notnull, use), ...])
_TABLES = [
    ("cfg_meta", "one row per top-level app-identity key",
     "core app-identity facts (which database this cfg_* store belongs to, the seeded "
     "config_version) — read once at startup to confirm identity before anything else runs.",
     [("key", "TEXT", 1, 0, "the identity fact's name, e.g. 'database', 'config_version'"),
      ("value", "TEXT", 0, 0, "the fact's value")]),

    ("cfg_table", "one row per registered table (database, name) — this row",
     "the table-level half of governance.tables — every table across both project databases "
     "(bible_research/research_db and iba), what one row of it represents, and its overall "
     "purpose. Self-referential: this table registers itself.",
     [("database", "TEXT", 1, 1, "which database owns this table — 'iba' or 'research_db'"),
      ("name", "TEXT", 1, 1, "the table's name"),
      ("grain", "TEXT", 0, 0, "what one row of this table represents"),
      ("use", "TEXT", 0, 0, "the table's purpose — why it exists, how it's used"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired (kept for history)")]),

    ("cfg_column", "one row per column of a registered table (database, table_name, name)",
     "the column-level half of governance.table_columns — every column's type, key/nullability "
     "flags, use text, and (for data-driven-enforced settings) the expectation pattern "
     "lib/valuequality.py checks it against. Self-referential: this table registers its own "
     "columns via the rows this very migration writes.",
     [("database", "TEXT", 1, 1, "which database owns the table this column belongs to"),
      ("table_name", "TEXT", 1, 0, "the table this column belongs to"),
      ("name", "TEXT", 1, 0, "the column's name"),
      ("ordinal", "INTEGER", 0, 0, "declaration order within the table"),
      ("type", "TEXT", 0, 0, "the column's SQL type (TEXT/INTEGER/...)"),
      ("is_pk", "INTEGER", 0, 0, "1 if part of the table's primary key"),
      ("notnull", "INTEGER", 0, 0, "1 if the column has a NOT NULL constraint"),
      ("is_unique", "INTEGER", 0, 0, "1 if the column has its own UNIQUE constraint (compound "
       "uniqueness across columns is cfg_unique's job instead)"),
      ("dflt", "TEXT", 0, 0, "the column's declared SQL default, if any"),
      ("fk", "TEXT", 0, 0, "the table.column this column references, if it's a foreign key"),
      ("use", "TEXT", 0, 0, "what this column holds and how it's used"),
      ("expectation", "TEXT", 0, 0, "for a data-driven-enforced value: 'pattern:<cfg_setting "
       "key>' or 'enum.<cfg_enum name>' — lib/valuequality.py's engine checks live values "
       "against this instead of a hardcoded rule"),
      ("source", "TEXT", 0, 0, "where this column's value originates, if not obvious"),
      ("filled_by", "TEXT", 0, 0, "the script/migration that populates this column")]),

    ("cfg_unique", "one row per column participating in a named table's compound-uniqueness rule",
     "documents a compound (multi-column) uniqueness expectation for a table — table_name plus "
     "one row per participating column, ordinal giving the compound-key column order. A "
     "documentation/validation aid, not itself an enforced DB constraint.",
     [("table_name", "TEXT", 1, 0, "the table the uniqueness rule applies to"),
      ("col", "TEXT", 1, 0, "one column participating in the compound unique key"),
      ("ordinal", "INTEGER", 0, 0, "this column's position within the compound key")]),

    ("cfg_enum", "one row per (name, value) enum membership",
     "named controlled-vocabulary groups — lookups/options queried BY NAME at runtime "
     "(cfg.enum(name) or the equivalent raw SQL) rather than hardcoded as string literals in "
     "code, so a membership change is something the app actually notices.",
     [("name", "TEXT", 1, 0, "the enum group's name, e.g. 'config_module'"),
      ("value", "TEXT", 1, 0, "one member of the group"),
      ("ordinal", "INTEGER", 0, 0, "display/insertion order within the group"),
      ("inactive", "INTEGER", 0, 1, "0=active member, 1=retired (kept for history)")]),

    ("cfg_connection", "one row per STEP-server connection parameter",
     "STEP Bible local-server connection parameters (base_url, version, ...) — read at startup "
     "to build the live connection used by every raw.* STEP call.",
     [("key", "TEXT", 1, 0, "the parameter's name, e.g. 'base_url', 'version'"),
      ("value", "TEXT", 0, 0, "the parameter's value"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired")]),

    ("cfg_api", "one row per named STEP REST API call this app is coded to use",
     "the catalogue of STEP Bible REST API calls the app actually issues — route template "
     "(with {placeholders}), what input the caller supplies, and what shape the response "
     "returns. The IBA-side equivalent of scripts/analytics/step_client.py's method list.",
     [("name", "TEXT", 1, 0, "the call's short identifier, e.g. 'call1_meanings'"),
      ("route", "TEXT", 0, 0, "the REST route template, with {placeholder} segments"),
      ("input", "TEXT", 0, 0, "what the caller must supply"),
      ("returns", "TEXT", 0, 0, "what shape the response gives back"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired")]),

    ("cfg_book_order", "one row per Bible book",
     "canonical book ordering (Gen=0 .. Rev=65) for sorting/sequencing verse references "
     "app-wide — the IBA-side equivalent of research_db's books/book_code_variants tables.",
     [("book", "TEXT", 1, 0, "the book's short code, e.g. 'Gen'"),
      ("ordinal", "INTEGER", 0, 0, "0-based canonical Bible order"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired")]),

    ("cfg_candidate_rule", "one row per (kind, value) candidate-inclusion override",
     "accept/reject overrides for candidate Strong's numbers considered during term/HIB "
     "candidate onboarding — kind names the rule type (currently only 'accept' is live), value "
     "is the Strong's number the rule applies to.",
     [("kind", "TEXT", 1, 0, "the rule type — currently only 'accept' is a live value"),
      ("value", "TEXT", 1, 0, "the Strong's number (or other matched value) the rule covers"),
      ("inactive", "INTEGER", 0, 1, "0=active override, 1=retired")]),

    ("cfg_write_grant", "one row per (writer, table_name, database) write permission",
     "governance.config_control's write-grant registry — which writer (a step name, or "
     "'configmaint.propose' for the sanctioned manual-change gate) may write which table in "
     "which database. configmaint.validate's coherence check confirms every cfg_* table has at "
     "least one grant, or nothing could legitimately maintain it.",
     [("writer", "TEXT", 1, 0, "the step/mechanism permitted to write — a dispatcher step name, "
       "or 'configmaint.propose'"),
      ("table_name", "TEXT", 1, 0, "the table this writer may write to"),
      ("database", "TEXT", 1, 1, "which database the table lives in"),
      ("inactive", "INTEGER", 0, 1, "0=active grant, 1=revoked (kept for history)")]),

    ("cfg_work_package", "one row per top-level invokable work package",
     "the dispatcher's top-level package registry — its PowerShell entry script, what it runs "
     "over (a word, a book, 'none', ...), whether its steps chain automatically once triggered, "
     "and the user-facing complete/paused/next-step messages a PS wrapper shows.",
     [("name", "TEXT", 1, 0, "the work package's name, e.g. 'configuration-maintenance'"),
      ("ps_script", "TEXT", 0, 0, "the PowerShell entry-point script for this package"),
      ("runs_over", "TEXT", 0, 0, "what one invocation operates over — a word, a book, a run, "
       "'none', etc."),
      ("chained", "INTEGER", 0, 0, "1 if this package's steps run automatically in sequence "
       "once triggered, 0 if each step is invoked independently"),
      ("complete_message", "TEXT", 0, 0, "message shown to the researcher on successful "
       "completion"),
      ("next_step_hint", "TEXT", 0, 0, "suggested next action shown after completion"),
      ("paused_message", "TEXT", 0, 0, "message shown when a step pauses awaiting a decision"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired")]),

    ("cfg_step", "one row per (work_package, step)",
     "the dispatcher's step registry — which handler function runs for a named step within a "
     "work package, what scope it needs, a human description of what it does, and its kind "
     "('utility' = this app's own running; 'operations' = substantive analytic/study content).",
     [("work_package", "TEXT", 1, 0, "the owning work package"),
      ("ordinal", "INTEGER", 0, 0, "this step's position within its package"),
      ("step", "TEXT", 1, 0, "the step's dotted name, e.g. 'configmaint.validate'"),
      ("handler", "TEXT", 0, 0, "the Python handler function this step dispatches to, as "
       "'module:function'"),
      ("scope", "TEXT", 0, 0, "what this step needs scoped to it to run — a word, 'none', etc."),
      ("does", "TEXT", 0, 0, "a human-readable description of what this step actually does"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired"),
      ("kind", "TEXT", 0, 0, "'utility' (app's own running) or 'operations' (substantive "
       "analytic/study content) — governance.module.config's own classification")]),

    ("cfg_status_flow", "one row per (entity, status) lifecycle stage",
     "the ordered status lifecycle for a named entity (e.g. 'word') — which step sets each "
     "status, and its position in the sequence, so a status transition can be validated against "
     "a declared order rather than assumed.",
     [("entity", "TEXT", 1, 0, "the entity whose lifecycle this describes, e.g. 'word'"),
      ("status", "TEXT", 1, 0, "one status value in that entity's lifecycle"),
      ("set_by", "TEXT", 0, 0, "which step/mechanism sets this status"),
      ("ordinal", "INTEGER", 0, 0, "this status's position in the lifecycle sequence"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired")]),

    ("cfg_on_fail", "one row per (step, condition) failure-routing rule",
     "how a named step should react to a named failure condition — path (the actual routing "
     "outcome: 'report-stop' or 'pause-continue'), an optional resolver, the message shown, and "
     "route (a routing category — currently always 'terminal', reserved for future non-terminal "
     "routing types).",
     [("step", "TEXT", 1, 0, "the step this failure-routing rule applies to"),
      ("condition", "TEXT", 1, 0, "the named failure condition, e.g. 'word-exists'"),
      ("path", "TEXT", 0, 0, "the actual routing outcome — 'report-stop' (hard stop) or "
       "'pause-continue' (escalate and wait for a decision)"),
      ("resolver", "TEXT", 0, 0, "an optional handler that can auto-resolve this condition, if "
       "one exists"),
      ("message", "TEXT", 0, 0, "the message shown to the researcher/Claude for this condition"),
      ("route", "TEXT", 0, 1, "a routing category — currently always 'terminal' across every "
       "live row; reserved for a future non-terminal routing type"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired")]),

    ("cfg_report", "one row per report-producing step's report shape",
     "report-generation shape for a step per governance.reports_must_persist — title, whether "
     "to show a table of contents, output format(s) (md/md+csv), naming scheme (stable = fixed "
     "filename, dated = versioned per governance.oneoff_report_naming_pattern), and archive "
     "folder for superseded versions.",
     [("step", "TEXT", 1, 0, "the report-producing step this shape applies to"),
      ("title", "TEXT", 0, 1, "the report's title"),
      ("show_toc", "INTEGER", 0, 1, "1 if the report includes a table of contents"),
      ("footer_text", "TEXT", 0, 0, "optional footer text appended to the report"),
      ("output_kind", "TEXT", 0, 1, "the output format(s) produced — 'md' or 'md+csv'"),
      ("naming_scheme", "TEXT", 0, 1, "'stable' (fixed filename, overwritten/archived on "
       "regenerate) or 'dated' (versioned filename per report)"),
      ("archive_dir", "TEXT", 0, 1, "where a superseded 'stable'-scheme report is archived"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired")]),

    ("cfg_report_section", "one row per (step, section_key) report section",
     "the section layout of a generated report — ordinal position, the markdown heading text, "
     "an optional shorter table-of-contents label, and whether the section is actually included "
     "in a live regenerate.",
     [("step", "TEXT", 1, 1, "the report-producing step this section belongs to"),
      ("ordinal", "INTEGER", 0, 1, "the section's position in the report"),
      ("section_key", "TEXT", 1, 1, "the section's stable identifier"),
      ("heading", "TEXT", 0, 1, "the markdown heading text rendered for this section"),
      ("toc_label", "TEXT", 0, 0, "a shorter label for the table of contents, if different from "
       "the heading"),
      ("include", "INTEGER", 0, 1, "1 if this section is actually rendered"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired")]),

    ("cfg_report_csv_table", "one row per (step, table_name) CSV-export target within a report",
     "which table(s) a report step's CSV output covers — join_note describes a multi-table join "
     "in plain language where table_name isn't a literal single table, and virtual=1 flags a "
     "computed/derived result set (a name that doesn't resolve to a literal live table — "
     "escalation #642 found two such rows naming non-existent tables, left open for researcher "
     "judgement, not fixed by this backfill).",
     [("step", "TEXT", 1, 1, "the report-producing step this CSV export belongs to"),
      ("table_name", "TEXT", 1, 1, "the table (or, if virtual=1, the named derived result set) "
       "this CSV covers"),
      ("join_note", "TEXT", 0, 0, "plain-language description of a multi-table join, if the "
       "export isn't a single verbatim table"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired"),
      ("virtual", "INTEGER", 0, 1, "1 if table_name is a computed/derived name rather than a "
       "literal live table")]),

    ("cfg_change_log", "one row per whole-store config reload/load event",
     "audit trail of cfg_* seed reloads — config_version and seed_hash (change-detection "
     "fingerprint), when the load happened, and whether it validated clean. Whole-reload events "
     "only; row-level individual changes are cfg_change_detail instead.",
     [("id", "INTEGER", 1, 0, "surrogate key"),
      ("config_version", "TEXT", 0, 0, "the app's config_version string at the time of this load"),
      ("seed_hash", "TEXT", 0, 0, "a hash of the seed content, for change detection"),
      ("loaded_at", "TEXT", 0, 0, "when this load happened"),
      ("validated", "INTEGER", 0, 0, "1 if this load passed validation")]),

    ("cfg_setting", "one row per named setting key",
     "flat key/value application settings, grouped by module (cfg_setting.module) — the app's "
     "primary tunable-configuration store, read at runtime via cfg.setting(key). module="
     "'governance' rows are the special case: process rules for the AI/researcher workflow, not "
     "runtime-applied values.",
     [("key", "TEXT", 1, 0, "the setting's dotted key, e.g. 'governance.reports_must_persist'"),
      ("value", "TEXT", 0, 0, "the setting's value, JSON-encoded"),
      ("use", "TEXT", 0, 0, "what this setting controls and why"),
      ("module", "TEXT", 0, 0, "which module this setting belongs to — a cfg_enum "
       "'config_module' member"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired")]),

    ("cfg_utility", "one row per registered script/library module",
     "the registry of every script/routine in the project per governance.scripts_and_routines — "
     "its file path, purpose (usually from the file's own docstring), whether retired, and "
     "whether it's exempt from the config-usage completeness check (config_exempt=1, with a "
     "required reason) for a legitimate structural reason — e.g. it IS the config reader, or it "
     "writes cfg_* directly via raw sqlite3 rather than reading it.",
     [("module", "TEXT", 1, 0, "the module's registered name"),
      ("file_path", "TEXT", 0, 1, "the file's repo-relative path"),
      ("purpose", "TEXT", 0, 0, "what this script/module does"),
      ("inactive", "INTEGER", 0, 1, "0=active, 1=retired"),
      ("config_exempt", "INTEGER", 0, 1, "1 if legitimately exempt from the zero-Cfg-usage "
       "completeness check"),
      ("config_exempt_reason", "TEXT", 0, 0, "required whenever config_exempt=1 — why this is a "
       "legitimate zero, not a completeness gap")]),
]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    for name, grain, use, columns in _TABLES:
        _table_and_columns(conn, name, grain, use, columns, report)

    conn.commit()
    conn.close()

    print(f"foundational cfg_* backfill ({len(_TABLES)} tables, escalation #712 part 1):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
