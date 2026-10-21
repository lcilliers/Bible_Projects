"""folder_purpose_build_v1_20260828.py — ONE-OFF, idempotent: builds the `folder_purpose`
mechanism (escalation #971, `iba/docs/folder-purpose-governance-plan-v5-20260828.md` and successors
— the researcher's own instruction, 2026-08-28, to combine #929/#736's carried-forward filing gaps
into one mechanism, corrected across 5 plan revisions: a reference/data table like `books`, not a
`cfg_*` table; full coverage of all 793 census folders, not a curated subset; three named processing
methods; and one new `filing` behaviour rule closing the tool-report-vs-deliverable ambiguity the
plan's own filing surfaced (escalation #971 chat, researcher: "yes the refiling of escalation files
is for 976" — confirming the broader reading: an escalation-linked deliverable belongs under
`outputs/escalation/` in principle, with the actual re-filing of already-misplaced files split into
escalation #976, not done here).

Per the `bootstrap_file_manifest.py` precedent this migration follows: schema (new table), cfg_table/
cfg_column/cfg_enum/cfg_utility/cfg_work_package/cfg_step registration are all a direct, documented,
idempotent bootstrap for a NEW module — not a `configmaint.propose` call (that gate is for changing
an EXISTING setting's value later, not for a new module's initial config footprint).

Also closes a real, separately-found compliance gap (`governance.tables`/`governance.table_columns`):
`file_manifest` (18,653 live rows) was never registered in `cfg_table`/`cfg_column` at all — fixed
here, ahead of `folder_purpose`'s own registration, so the table this mechanism extends is compliant
first.

    python -m iba.app.migration.folder_purpose_build_v1_20260828
"""

from __future__ import annotations

import datetime
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

_DDL = """
CREATE TABLE IF NOT EXISTS folder_purpose (
    folder_path             TEXT PRIMARY KEY,
    top_level_root          TEXT NOT NULL,
    depth                   INTEGER NOT NULL,
    parent_path             TEXT NOT NULL,
    direct_file_count       INTEGER NOT NULL DEFAULT 0,
    recursive_file_count    INTEGER NOT NULL DEFAULT 0,
    direct_subfolder_count  INTEGER NOT NULL DEFAULT 0,
    top_ext_direct          TEXT,
    last_modified_direct    TEXT,
    governed_by_setting     TEXT,
    manifest_category       TEXT,
    manifest_currency       TEXT,
    type                    TEXT,
    status                  TEXT,
    usage_description       TEXT,
    added_at                TEXT NOT NULL,
    last_reviewed_at        TEXT
);
CREATE INDEX IF NOT EXISTS ix_folder_purpose_top_level_root ON folder_purpose(top_level_root);
CREATE INDEX IF NOT EXISTS ix_folder_purpose_status ON folder_purpose(status);
CREATE INDEX IF NOT EXISTS ix_folder_purpose_type ON folder_purpose(type);
"""

_FILE_MANIFEST_COLUMNS = [
    ("path", "TEXT", 1, 0, 1, None,
     "Project-root-relative path (POSIX slashes) of the file. Primary key -- one row per file."),
    ("category", "TEXT", 0, 1, 0, None,
     "Coarse classification (iba/session/script/cluster/discovery/workflow/investigation/patch/"
     "report/doc/log/directive/code/export/import/backup/other) -- computed by "
     "lib/manifest.py:classify_category() from the path's leading folder segments, project-naming "
     "FACT not cfg_setting. folder_purpose.manifest_category (escalation #971) will become the "
     "primary source once built, this classifier the fallback for any folder not yet registered."),
    ("file_type", "TEXT", 0, 1, 0, None,
     "Finer-grained type within category, e.g. 'iba-lib', 'analysis-patch' -- "
     "lib/manifest.py:classify_type()."),
    ("currency", "TEXT", 0, 1, 0, None,
     "current/archived/cross-reference/historical/backup/other -- "
     "lib/manifest.py:compute_currency(), same fallback relationship to folder_purpose."),
    ("archived", "INTEGER", 0, 1, 0, None, "1 iff currency='archived' (path contains an archive/ "
     "segment) -- redundant with currency, kept for cheap WHERE archived=1 filtering."),
    ("registry", "INTEGER", 0, 0, 0, None,
     "word_registry id extracted from the filename, when the naming pattern carries one -- NULL "
     "for files not tied to a specific word registry."),
    ("word", "TEXT", 0, 0, 0, None, "English word extracted from the filename, when present."),
    ("cluster", "TEXT", 0, 0, 0, None, "M-code cluster extracted from the filename, when present."),
    ("vcb_batch", "INTEGER", 0, 0, 0, None, "Verse-context-batch number extracted from the "
     "filename, when present -- legacy Session B naming."),
    ("version", "TEXT", 0, 0, 0, None, "The -v{n} version suffix extracted from the filename, "
     "when present."),
    ("date", "TEXT", 0, 0, 0, None, "Date extracted from the filename (compact or hyphenated), "
     "when present."),
    ("ext", "TEXT", 0, 0, 0, None, "File extension, lowercase, including the leading dot."),
    ("size_bytes", "INTEGER", 0, 1, 0, None, "File size in bytes at scan time."),
    ("modified_at", "TEXT", 0, 1, 0, None, "The file's own filesystem mtime, UTC ISO-8601."),
    ("scanned_at", "TEXT", 0, 1, 0, None,
     "When this row was written by manifest.rebuild() -- identical across every row from the same "
     "run; a full rebuild replaces the table's contents rather than updating in place."),
]

_FOLDER_PURPOSE_COLUMNS = [
    ("folder_path", "TEXT", 1, 0, 1, None,
     "Project-root-relative folder prefix, POSIX slashes, no trailing slash. Primary key -- one "
     "row per governed folder, seeded from a full census of every directory in the tree."),
    ("top_level_root", "TEXT", 0, 1, 0, None,
     "First path segment (or '(repo root)' for the root itself) -- cheap grouping/filter key."),
    ("depth", "INTEGER", 0, 1, 0, None, "Path segment count; 0 = repo root."),
    ("parent_path", "TEXT", 0, 1, 0, None, "This folder's immediate parent's folder_path."),
    ("direct_file_count", "INTEGER", 0, 1, 0, "0",
     "Files directly in this folder, not counting subfolders -- refreshed by the manifest-validate "
     "method (Method A) on every manifest rebuild, never hand-edited."),
    ("recursive_file_count", "INTEGER", 0, 1, 0, "0",
     "Files in this folder and everything under it -- Method A-refreshed."),
    ("direct_subfolder_count", "INTEGER", 0, 1, 0, "0", "Immediate child folders -- Method A-refreshed."),
    ("top_ext_direct", "TEXT", 0, 0, 0, None,
     "Up to 5 file extensions by count among this folder's direct files -- Method A-refreshed."),
    ("last_modified_direct", "TEXT", 0, 0, 0, None,
     "Latest mtime among this folder's direct files, UTC ISO-8601 -- Method A-refreshed."),
    ("governed_by_setting", "TEXT", 0, 0, 0, None,
     "Which cfg_setting key(s) already point at this exact folder path (semicolon-joined if more "
     "than one) -- refreshed by the configmaint cross-check (Method B), config-side truth, distinct "
     "from Method A's disk-side truth because a setting can change with no file moving."),
    ("manifest_category", "TEXT", 0, 0, 0, None,
     "What file_manifest.category a file in this folder should get once folder_purpose becomes the "
     "manifest's primary classification source (escalation #971 Part D) -- NULL until set."),
    ("manifest_currency", "TEXT", 0, 0, 0, None, "Same, for file_manifest.currency -- NULL until set."),
    ("type", "TEXT", 0, 0, 0, None,
     "archive|operations|results (cfg_enum folder_purpose_type) -- the researcher-facing coarse "
     "classification, hand-set via FolderPurpose.ps1 (Method C), never touched by Methods A/B."),
    ("status", "TEXT", 0, 0, 0, None,
     "authoritative|mixed|reallocate|stale|deleted (cfg_enum folder_purpose_status) -- 'deleted' is "
     "set by Method A when a folder no longer exists on disk (soft delete, row never removed); the "
     "other four values are hand-set via Method C."),
    ("usage_description", "TEXT", 0, 0, 0, None,
     "Free-text description of what this folder is actually for, in the cfg_table.use/"
     "cfg_column.use style, scoped to a folder -- hand-set via Method C."),
    ("added_at", "TEXT", 0, 1, 0, None, "When this row was first created."),
    ("last_reviewed_at", "TEXT", 0, 0, 0, None,
     "When type/status/usage_description were last confirmed accurate via Method C -- lets Method "
     "A/B flag a row whose judgement fields haven't been reviewed since its disk facts changed."),
]


def _cfg_table(conn, database, name, grain, use, report):
    if not conn.execute("SELECT 1 FROM cfg_table WHERE database=? AND name=?",
                        (database, name)).fetchone():
        conn.execute("INSERT INTO cfg_table (database, name, grain, use, inactive) "
                    "VALUES (?,?,?,?,0)", (database, name, grain, use))
        report.append(f"cfg_table {database}.{name} added")
    else:
        report.append(f"cfg_table {database}.{name} already present")


def _cfg_columns(conn, database, table_name, columns, report):
    added = 0
    for ordinal, (name, type_, is_pk, notnull, is_unique, dflt, use) in enumerate(columns):
        if conn.execute("SELECT 1 FROM cfg_column WHERE database=? AND table_name=? AND name=?",
                        (database, table_name, name)).fetchone():
            continue
        conn.execute(
            'INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "notnull", '
            'is_unique, dflt, fk, use, expectation, source, filled_by, inactive) '
            "VALUES (?,?,?,?,?,?,?,?,?,NULL,?,NULL,NULL,NULL,0)",
            (database, table_name, name, ordinal, type_, is_pk, notnull, is_unique, dflt, use))
        added += 1
    report.append(f"cfg_column {database}.{table_name}: {added} added, "
                  f"{len(columns) - added} already present")


def _enum(conn, name, value, report):
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, value)).fetchone():
        n = conn.execute("SELECT COUNT(*) FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
        conn.execute("INSERT INTO cfg_enum VALUES (?,?,?,0)", (name, value, n))
        report.append(f"cfg_enum {name} += {value!r}")
    else:
        report.append(f"cfg_enum {name} already has {value!r}")


def _behaviour_class(conn, cls, doc, desc, report):
    if not conn.execute("SELECT 1 FROM cfg_behaviour_class WHERE class=?", (cls,)).fetchone():
        conn.execute("INSERT INTO cfg_behaviour_class (class, authoritative_doc, description, "
                    "added_at, inactive) VALUES (?,?,?,?,0)", (cls, doc, desc, _NOW))
        report.append(f"cfg_behaviour_class {cls!r} added")
    else:
        report.append(f"cfg_behaviour_class {cls!r} already present")


def _behaviour_rule(conn, cls, key, text, source, report):
    if not conn.execute("SELECT 1 FROM cfg_behaviour_rule WHERE class=? AND rule_key=?",
                        (cls, key)).fetchone():
        conn.execute("INSERT INTO cfg_behaviour_rule (class, rule_key, rule_text, source, "
                    "enforced_by, added_at, active) VALUES (?,?,?,?,NULL,?,1)",
                    (cls, key, text, source, _NOW))
        report.append(f"cfg_behaviour_rule {cls}.{key} added")
    else:
        report.append(f"cfg_behaviour_rule {cls}.{key} already present")


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
    else:
        report.append(f"cfg_step {step!r} already present")


def _utility(conn, module, file_path, purpose, report):
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone():
        conn.execute("INSERT INTO cfg_utility (module, file_path, purpose, inactive) "
                    "VALUES (?,?,?,0)", (module, file_path, purpose))
        report.append(f"cfg_utility {module!r} added")
    else:
        report.append(f"cfg_utility {module!r} already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    # --- compliance fix: file_manifest was never registered (governance.tables violation) ---
    _cfg_table(conn, "iba", "file_manifest", "one row per file",
              "Filename/path metadata for every file in the project tree (18,653 rows at "
              "registration time, 2026-08-28) -- built by lib/manifest.py:rebuild(), a full-tree "
              "walk. Content is never read, only path/name/size/mtime facts. Was live and "
              "populated for 13 days before being registered here (escalation #972's own orphan "
              "check caught the gap while grounding escalation #971).", report)
    _cfg_columns(conn, "iba", "file_manifest", _FILE_MANIFEST_COLUMNS, report)

    # --- folder_purpose: schema + registration ---
    conn.executescript(_DDL)
    report.append("folder_purpose table + indexes ensured")
    _cfg_table(conn, "iba", "folder_purpose", "one row per governed folder",
              "Reference/data table (like bible_research.db's books, NOT a cfg_* rule table) -- "
              "one row per folder in the project tree, seeded from a full census "
              "(outputs/folder-census-20260828.csv, 793 folders). Gives the researcher visibility "
              "into every live folder's purpose/status and lets folder-classifying code (lib/"
              "manifest.py) read a governed source instead of hardcoded prefix rules. Escalation "
              "#971, iba/docs/folder-purpose-governance-plan-v5-20260828.md.", report)
    _cfg_columns(conn, "iba", "folder_purpose", _FOLDER_PURPOSE_COLUMNS, report)

    _enum(conn, "folder_purpose_type", "archive", report)
    _enum(conn, "folder_purpose_type", "operations", report)
    _enum(conn, "folder_purpose_type", "results", report)
    _enum(conn, "folder_purpose_status", "authoritative", report)
    _enum(conn, "folder_purpose_status", "mixed", report)
    _enum(conn, "folder_purpose_status", "reallocate", report)
    _enum(conn, "folder_purpose_status", "stale", report)
    _enum(conn, "folder_purpose_status", "deleted", report)

    _utility(conn, "folderpurpose", "iba/app/lib/folderpurpose.py",
            "folderpurpose.py -- folder_purpose table: seed/refresh from a live directory scan "
            "(Method A), cross-check against cfg_setting *_dir/*_path values (Method B), and "
            "hand-edit type/status/usage_description (Method C). Escalation #971.", report)

    _work_package(conn, "folder-purpose", "iba/app/ps/FolderPurpose.ps1", report)
    _step(conn, "folder-purpose", 0, "folderpurpose.seed",
         "iba.app.handlers.folderpurpose:folder_purpose_seed",
         "Method A -- full reconciliation of folder_purpose against the live directory tree: new "
         "folders inserted, missing folders soft-deleted, disk-derived columns refreshed for every "
         "row.", "utility", report)
    _step(conn, "folder-purpose", 1, "folderpurpose.crosscheck",
         "iba.app.handlers.folderpurpose:folder_purpose_crosscheck",
         "Method B -- syncs governed_by_setting from live cfg_setting values, pre-fills type/status "
         "where unambiguous, reports the operations-needs-a-setting invariant's anomalies.",
         "utility", report)
    _step(conn, "folder-purpose", 2, "folderpurpose.set",
         "iba.app.handlers.folderpurpose:folder_purpose_set",
         "Method C -- hand-set type/status/usage_description for one folder.", "utility", report)
    _step(conn, "folder-purpose", 3, "folderpurpose.list",
         "iba.app.handlers.folderpurpose:folder_purpose_list",
         "Method C -- list folder_purpose rows, optionally filtered.", "utility", report)
    _step(conn, "folder-purpose", 4, "folderpurpose.show",
         "iba.app.handlers.folderpurpose:folder_purpose_show",
         "Method C -- full detail for one folder.", "utility", report)

    # --- Part A: filing behaviour class + rules (v1 items 1-4, unchanged; item 5 = Part E, this
    # round's correction reflecting the researcher's confirmed answer that escalation-linked
    # deliverables DO belong under outputs/escalation/ in principle -- the re-filing of ALREADY-
    # MISFILED documents (including every escalation-tied plan doc that predates this rule,
    # this one included) is escalation #976's job, not a rule violation to fix retroactively here) ---
    _behaviour_class(conn, "filing",
                     "iba/docs/file-naming-and-location-governance-plan-v1-20260826.md",
                     "Where a file goes, how it's named, and when it's archived -- general "
                     "principles applying to any file in any folder, project-wide. Distinct from "
                     "`documentation` (single-authority content referencing) and from any one "
                     "methodology's own artefact-specific filename templates, which stay legacy "
                     "prose in docs/file-organisation-rules.md, not encoded here. Added 2026-08-28, "
                     "escalation #971 (carries forward #863/#736's unbuilt scope).", report)

    _behaviour_rule(conn, "filing", "naming-shape",
                   "A filename uses lowercase, hyphens (not underscores/spaces), a compact "
                   "YYYYMMDD date where a date is part of the name, a -v{n} version suffix with no "
                   "leading zero, and zero-padded numeric ids where an id is part of the name.",
                   "docs/file-organisation-rules.md sec2.1, adopted via "
                   "iba/docs/file-naming-and-location-governance-plan-v1-20260826.md sec2.1",
                   report)
    _behaviour_rule(conn, "filing", "snapshot-vs-living-document",
                   "A snapshot (a report, an extract, a point-in-time analysis) gets filename "
                   "versioning: -v{n}-{date}, same-day revisions bump {n}, prior versions archived "
                   "promptly, only the latest stays at the live path. A living document (a guide, an "
                   "instruction doc meant to be edited in place) keeps one stable filename, with "
                   "its version tracked in its own metadata and git history, never archived copies.",
                   "docs/file-organisation-rules.md sec2.3/2.3a, adopted via "
                   "iba/docs/file-naming-and-location-governance-plan-v1-20260826.md sec2.1", report)
    _behaviour_rule(conn, "filing", "archiving-trigger",
                   "A superseded snapshot is archived (moved to the folder's archive/ subfolder, "
                   "never deleted) in the same unit of work that supersedes it -- findable again "
                   "via the manifest, not left live alongside its replacement.",
                   "docs/file-organisation-rules.md sec4/4.1, adopted via "
                   "iba/docs/file-naming-and-location-governance-plan-v1-20260826.md sec2.1", report)
    _behaviour_rule(conn, "filing", "claude-code-filing-obligations",
                   "Before writing a new file: determine its correct folder first (don't default to "
                   "the working directory); archive any file it supersedes; never leave a file "
                   "sitting at a folder's root when a subfolder convention exists for its type; "
                   "follow the naming-shape and snapshot-vs-living rules above without being asked "
                   "each time; and confirm the destination when genuinely unclear rather than "
                   "guessing (docs/interaction-preferences.md's own protocol).",
                   "docs/file-organisation-rules.md sec5, adopted via "
                   "iba/docs/file-naming-and-location-governance-plan-v1-20260826.md sec2.1", report)
    _behaviour_rule(conn, "filing", "tool-report-path-vs-deliverable-document",
                   "A tool's own auto-generated report output (an escalation list/history export, "
                   "CONFIG-REPORT.md, a validation run's report, a content-index rebuild report -- "
                   "anything a *.report_path/*.output_dir cfg_setting names) stays exactly where "
                   "that setting points. An authored deliverable document -- a plan, a design doc, a "
                   "gap analysis, an investigation write-up -- follows "
                   "governance.engineering_documentation_folder (iba/docs/ for IBA-side work) or the "
                   "main-project equivalent instead, even when it is produced while working, and "
                   "linked from, one specific escalation's comment/resolution. This resolves an "
                   "ambiguity GOVERNANCE.md sec59 left open ('a second, larger design item') and "
                   "confirms the researcher's original intent for that section was the broader "
                   "reading: an escalation-linked deliverable DOES belong under outputs/escalation/ "
                   "in principle -- but re-filing every document that predates this rule (every "
                   "escalation-tied plan doc currently in iba/docs/, including the "
                   "folder-purpose-governance-plan series itself) is a physical migration, tracked "
                   "and executed under escalation #976, not a retroactive violation to silently fix "
                   "here.",
                   "researcher, 2026-08-28, escalation #971 chat: \"yes the refiling of escalation "
                   "files is for 976\" -- iba/docs/folder-purpose-governance-plan-v5-20260828.md "
                   "Part E", report)

    conn.commit()
    conn.close()

    print("folder_purpose build bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
