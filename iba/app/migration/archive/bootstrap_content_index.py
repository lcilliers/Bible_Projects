"""bootstrap_content_index.py — ONE-OFF, idempotent: registers `content_index.rebuild` and
`content_index.search` (file-content concordance search over `.md` files, keyed on Strong's
numbers/glosses/words) as real dispatcher work packages/steps — round 2 of the manifest +
content-search plan (governance-alignment register item #6, escalation #691, researcher: "process
as planned" 2026-08-17).

Two work packages (same shape as `file-manifest-rebuild`/`file-manifest-search`, §3 of the plan —
each independently invokable, not one chained package):

  - `content-index-rebuild` / `content_index.rebuild` — full rescan, writes `content_index` +
    `content_index_scan` from scratch.
  - `content-index-search`  / `content_index.search`  — incremental refresh + read-only query.

Both `kind='utility'` (`GOVERNANCE.md` §27) — this app's own running, not the study's substantive
analytic content, same classification as `manifest.rebuild`/`manifest.search`.

Schema is DDL (two new tables), same class of exception as `bootstrap_file_manifest.py`'s new
table — a direct, documented, idempotent bootstrap, not a `configmaint.propose` call. The only
genuine `cfg_setting` decision here is `content_index.search_report_path` (where search results
land) — the key SOURCES (`strong`, `word_registry`) and the matching approach (tokenize + n-gram +
set lookup, not a regex alternation — tested live, see `lib/contentindex.py`'s own docstring) are
project-structural facts, not settings, per the same fact-vs-choice distinction `manifest.py`
already draws.

    python -m iba.app.migration.bootstrap_content_index
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_DDL = """
CREATE TABLE IF NOT EXISTS content_index (
    key_type     TEXT NOT NULL,
    key_value    TEXT NOT NULL,
    file_path    TEXT NOT NULL,
    line_number  INTEGER NOT NULL,
    snippet      TEXT NOT NULL,
    indexed_at   TEXT NOT NULL,
    PRIMARY KEY (key_type, key_value, file_path, line_number)
);
CREATE INDEX IF NOT EXISTS ix_content_index_key ON content_index(key_type, key_value);
CREATE INDEX IF NOT EXISTS ix_content_index_file ON content_index(file_path);

CREATE TABLE IF NOT EXISTS content_index_scan (
    file_path    TEXT PRIMARY KEY,
    mtime        TEXT NOT NULL,
    scanned_at   TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cfg_content_index_exclude (
    pattern      TEXT PRIMARY KEY,
    reason       TEXT NOT NULL,
    added_at     TEXT NOT NULL,
    inactive     INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS cfg_content_index_size_override (
    pattern      TEXT PRIMARY KEY,
    reason       TEXT NOT NULL,
    added_at     TEXT NOT NULL,
    inactive     INTEGER NOT NULL DEFAULT 0
);
"""


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


def _work_package(conn, name, ps_script, report):
    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (name,)).fetchone():
        conn.execute("INSERT INTO cfg_work_package (name, ps_script, runs_over, chained) "
                    "VALUES (?,?,'none',0)", (name, ps_script))
        report.append(f"cfg_work_package {name!r} added")
    else:
        report.append(f"cfg_work_package {name!r} already present")


def _step(conn, wp, ordinal, step, handler, does, kind, report):
    existing = conn.execute(
        "SELECT handler, kind FROM cfg_step WHERE work_package=? AND step=?", (wp, step)).fetchone()
    if not existing:
        conn.execute(
            "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, inactive, "
            "kind) VALUES (?,?,?,?,?,?,0,?)", (wp, ordinal, step, handler, "none", does, kind))
        report.append(f"cfg_step {step!r} added (kind={kind})")
    elif existing[0] != handler or existing[1] != kind:
        conn.execute("UPDATE cfg_step SET handler=?, kind=? WHERE work_package=? AND step=?",
                    (handler, kind, wp, step))
        report.append(f"cfg_step {step!r} handler/kind corrected")
    else:
        report.append(f"cfg_step {step!r} already present")


def _utility(conn, module, file_path, purpose, report):
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone():
        conn.execute("INSERT INTO cfg_utility (module, file_path, purpose, inactive) "
                    "VALUES (?,?,?,0)", (module, file_path, purpose))
        report.append(f"cfg_utility {module!r} added")
    else:
        report.append(f"cfg_utility {module!r} already present")


def _write_grant(conn, writer, table_name, report):
    """A cfg_* table needs a cfg_write_grant row for 'configmaint.propose' or nothing can
    maintain it through the sanctioned gate (governance.config_control) — the exact gap found
    live earlier tonight for cfg_method_rule/cfg_quality_check (escalations #695/#700, still
    unresolved elsewhere). Not repeated here."""
    if not conn.execute(
            "SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'",
            (writer, table_name)).fetchone():
        conn.execute("INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
                    "VALUES (?,?,'iba',0)", (writer, table_name))
        report.append(f"cfg_write_grant ({writer!r}, {table_name!r}) added")
    else:
        report.append(f"cfg_write_grant ({writer!r}, {table_name!r}) already present")


def _table_and_columns(conn, name, grain, use, columns, report):
    """Registers a cfg_* table + its columns in cfg_table/cfg_column, per governance.tables/
    governance.table_columns — the same discipline #653/#678 applied to every research_db table."""
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
                "'migration/bootstrap_content_index.py')",
                (name, col, ordinal, coltype, ispk, notnull, colnuse))
            report.append(f"cfg_column ({name}.{col}) added")
        else:
            report.append(f"cfg_column ({name}.{col}) already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    conn.executescript(_DDL)
    report.append("content_index + content_index_scan tables + indexes ensured")

    _enum(conn, "config_module", "content_index", report)

    _work_package(conn, "content-index-rebuild", "iba/app/ps/ContentIndex-Rebuild.ps1", report)
    _step(conn, "content-index-rebuild", 0, "content_index.rebuild",
         "iba.app.handlers.reports:content_index_rebuild",
         "full rescan of every .md file in file_manifest — clears and rebuilds content_index + "
         "content_index_scan from scratch; see lib/contentindex.py", "utility", report)

    _work_package(conn, "content-index-search", "iba/app/ps/ContentIndex-Search.ps1", report)
    _step(conn, "content-index-search", 0, "content_index.search",
         "iba.app.handlers.reports:content_index_search",
         "incremental refresh (mtime-based, only changed .md files) then a key_type:value or "
         "bare-value lookup against content_index, enriched with file_manifest metadata; results "
         "persisted via reportkit.oneoff_path, per governance.reports_must_persist",
         "utility", report)

    _setting(conn, "content_index.report_path",
             json.dumps("iba/app/reports/content-index-rebuild.md"),
             "where content_index.rebuild writes its summary report", "content_index", report)
    _setting(conn, "content_index.size_profile_report_path",
             json.dumps("iba/app/reports/content-index-size-profile.md"),
             "where content_index.size_profile writes its .md-file-size report", "content_index",
             report)

    _utility(conn, "contentindex", "iba/app/lib/contentindex.py",
            "contentindex.py — file-content concordance search over .md files, keyed on Strong's "
            "numbers/glosses/words sourced from strong/word_registry. Round 2 of the manifest + "
            "content-search plan; file_manifest (round 1) is its coverage baseline.", report)

    # cfg_content_index_exclude -- researcher, 2026-08-17, after a live finding that some .md files
    # (large generated prose/verse-analysis dumps) produce pathological hit density: "we should
    # definitely exclude the prose files. but there may be others also we want to exclude... the
    # rule being include all md except." A governed table, not a JSON file -- cfg.py's own rule is
    # "never opens a JSON file," the DB is the only config source app-wide.
    _write_grant(conn, "configmaint.propose", "cfg_content_index_exclude", report)
    _table_and_columns(conn, "cfg_content_index_exclude",
                       "one row per exclude pattern",
                       "governs content_index.rebuild/.refresh's file scope: any .md file whose "
                       "path starts with an ACTIVE pattern here is skipped. Default is 'include "
                       "all .md except' -- an empty table excludes nothing.",
                       [("pattern", "TEXT", 1, 1, "a file path or folder-path prefix (posix-style, "
                        "project-root-relative) -- e.g. 'iba/app/verse-analysis/' excludes the "
                        "whole folder, a full file path excludes just that file"),
                        ("reason", "TEXT", 0, 1, "why this is excluded -- required, not a bare flag"),
                        ("added_at", "TEXT", 0, 1, "when the pattern was added"),
                        ("inactive", "INTEGER", 0, 1, "0=active (excludes), 1=retired (no longer "
                        "excludes, kept for history per governance.tables' own convention)")],
                       report)

    _work_package(conn, "content-index-size-profile", "iba/app/ps/ContentIndex-SizeProfile.ps1", report)
    _step(conn, "content-index-size-profile", 0, "content_index.size_profile",
         "iba.app.handlers.reports:content_index_size_profile",
         "read-only report of every .md file in file_manifest by size, largest first — file name, "
         "folder, size — for visual review before adding to cfg_content_index_exclude; see "
         "lib/contentindex.py", "utility", report)

    # Size-threshold default exclusion + override -- researcher, 2026-08-17: "you can add all
    # above 50MB by default into the exclusions. to be manually released if needed." A code-level
    # RULE (checked against file_manifest.size_bytes at scan time), not per-file exclude rows --
    # cfg_content_index_size_override is the symmetric "manually released" mechanism: a file
    # matching an active override pattern is included even if it exceeds the threshold.
    _setting(conn, "content_index.exclude_size_threshold_bytes", json.dumps(52428800),
             "a .md file this size or larger (bytes; default 50MB) is excluded from "
             "content_index.rebuild/.refresh by default, unless it matches an active "
             "cfg_content_index_size_override pattern", "content_index", report)
    _write_grant(conn, "configmaint.propose", "cfg_content_index_size_override", report)
    _table_and_columns(conn, "cfg_content_index_size_override",
                       "one row per manually-released large file/folder",
                       "overrides content_index.exclude_size_threshold_bytes: a .md file matching "
                       "an ACTIVE pattern here is included even if it's at or above the size "
                       "threshold. 'Manually released if needed' (researcher, 2026-08-17) -- "
                       "empty by default, nothing released until named here.",
                       [("pattern", "TEXT", 1, 1, "a file path or folder-path prefix (posix-style, "
                        "project-root-relative), same matching rule as cfg_content_index_exclude"),
                        ("reason", "TEXT", 0, 1, "why this large file is still wanted in the index"),
                        ("added_at", "TEXT", 0, 1, "when the override was added"),
                        ("inactive", "INTEGER", 0, 1, "0=active (releases it), 1=retired")],
                       report)

    conn.commit()
    conn.close()

    print("content-index registration bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
