"""reading_index_2228_v1_20261023.py -- escalation #2228 tool 2, the cluster reading index, as config and
schema (design outputs/escalation/2228-cluster-reading-index-design-v1-20261023.md; researcher 2026-10-23:
D1 with a guard on time and size, D2 build it now, D3 bare follow-ons left out).

- tables reading_file, reading_section, reading_ref (cfg_table, cfg_column, cfg_index; built from config
  by lib/db.table_ddl) and their enums (reading_ref.kind, reading_ref.found_by, reading_ref.line_kind).
- work package reading-index (iba/app/ps/Reading-Index.ps1): steps reading_index.build (write grants on the
  three tables) and reading_index.report (cfg_report row).
- settings reading_index.roots, reading_index.output_dir, reading_index.max_seconds; module reading_index.
- the guard on the scope resolver: verse_scope.max_verses, verse_scope.max_seconds; cfg_utility versescope
  is no longer config-exempt (it reads them).
- cfg_utility for the three new files and this migration.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path)
in the same transaction. Idempotent. One transaction.

Usage:
    python iba/app/migration/reading_index_2228_v1_20261023.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import table_ddl  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2228-READING-INDEX-20261023"
MODULE = "reading_index_2228_v1_20261023"
SOURCE = "escalation #2228, cluster reading index design v1 (outputs/escalation/2228-cluster-reading-index-design-v1-20261023.md)"
FILLED = "iba/app/lib/readingindex.py (build)"
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"
WP = "reading-index"


def col(table, name, ordinal, typ, use, *, pk=0, nn=0, dflt=None, fk=None, exp=None):
    return {"database": "iba", "table_name": table, "name": name, "ordinal": ordinal, "type": typ,
            "is_pk": pk, "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use,
            "expectation": exp, "source": SOURCE, "filled_by": FILLED, "inactive": 0}


def cols(table, spec):
    """(name, type, use, options) in column order -> cfg_column rows."""
    return [col(table, n, i, t, u, **(o or {})) for i, (n, t, u, o) in enumerate(spec)]


TABLES = {
    "reading_file": ("one row per indexed study file",
                     "#2228 tool 2: a study file under reading_index.roots read by Reading-Index.ps1 -Step Build; "
                     "re-read only when its sha256 changes", cols("reading_file", [
        ("id", "INTEGER", "surrogate PK", {"pk": 1, "nn": 1}),
        ("path", "TEXT", "the file, repo-relative posix path", {"nn": 1}),
        ("cluster", "TEXT", "the cluster folder it sits in (M02 for 'M02 - anger-wrath'); NULL at a root", None),
        ("size_bytes", "INTEGER", "size when indexed", None),
        ("sha256", "TEXT", "content hash when indexed; a different hash means the file is read again", {"nn": 1}),
        ("indexed_at", "TEXT", "when the file was last indexed or marked removed (ISO-8601 UTC)", {"nn": 1}),
        ("sections", "INTEGER", "heading sections found (the opening counts as one)", None),
        ("refs", "INTEGER", "verse references found, one per verse after range expansion", None),
        ("imported_observations", "INTEGER", "ib_observation rows whose revisit_note names this file: its rows are "
                                             "also in the tables (#2228 D2)", None),
        ("removed", "INTEGER", "1 when the file is gone or archived; its rows are then marked deleted",
         {"nn": 1, "dflt": "0"}),
        ("created_at", "TEXT", "when the row was written (ISO-8601 UTC)", {"nn": 1, "dflt": NOW}),
        ("created_by", "TEXT", WHO, {"nn": 1, "dflt": "'direct edit'"}),
    ])),
    "reading_section": ("one row per heading section of an indexed file",
                        "#2228 tool 2: the sections of a study file (# to #### headings; the opening before the first "
                        "heading is section 0)", cols("reading_section", [
        ("id", "INTEGER", "surrogate PK", {"pk": 1, "nn": 1}),
        ("file_id", "INTEGER", "the file", {"nn": 1, "fk": "reading_file.id"}),
        ("ordinal", "INTEGER", "order in the file, 0 for the opening", {"nn": 1}),
        ("level", "INTEGER", "heading level 1-4, 0 for the opening", {"nn": 1}),
        ("heading", "TEXT", "the heading text", None),
        ("path", "TEXT", "the parent headings, joined with ' > '", None),
        ("line_start", "INTEGER", "first line (1-based)", {"nn": 1}),
        ("line_end", "INTEGER", "last line", {"nn": 1}),
        ("deleted", "INTEGER", "1 once the file is re-read or removed (an earlier reading kept as history)",
         {"nn": 1, "dflt": "0"}),
        ("created_at", "TEXT", "when the row was written (ISO-8601 UTC)", {"nn": 1, "dflt": NOW}),
        ("created_by", "TEXT", WHO, {"nn": 1, "dflt": "'direct edit'"}),
    ])),
    "reading_ref": ("one row per verse a study file names, at a line",
                    "#2228 tool 2: every verse reference in an indexed file, after range expansion, with how it was "
                    "found and the line it stands on; a reference that resolves to nothing kept with its reason",
                    cols("reading_ref", [
        ("id", "INTEGER", "surrogate PK", {"pk": 1, "nn": 1}),
        ("file_id", "INTEGER", "the file", {"nn": 1, "fk": "reading_file.id"}),
        ("section_id", "INTEGER", "the heading section", {"nn": 1, "fk": "reading_section.id"}),
        ("verse_id", "INTEGER", "the verse; NULL for a whole chapter or a reference that resolves to nothing",
         {"fk": "verse.id"}),
        ("book", "TEXT", "the verse.reference book code (Psa)", None),
        ("chapter", "INTEGER", "the chapter, for a whole-chapter reference", None),
        ("ref_as_written", "TEXT", "the reference as the file writes it", None),
        ("ref_normalised", "TEXT", "verse.reference form (Psa 10:2, or Psa 51 for a chapter)", None),
        ("kind", "TEXT", "cfg_enum reading_ref.kind: verse or whole chapter", {"nn": 1, "exp": "enum.reading_ref.kind"}),
        ("found_by", "TEXT", "cfg_enum reading_ref.found_by: explicit (a book named), follow-on c:v, follow-on v.",
         {"nn": 1, "exp": "enum.reading_ref.found_by"}),
        ("line_no", "INTEGER", "the line it stands on (1-based)", {"nn": 1}),
        ("line_kind", "TEXT", "cfg_enum reading_ref.line_kind: heading, table row, bullet, paragraph",
         {"nn": 1, "exp": "enum.reading_ref.line_kind"}),
        ("reason", "TEXT", "why it resolves to nothing; NULL when it resolves", None),
        ("deleted", "INTEGER", "1 once the file is re-read or removed", {"nn": 1, "dflt": "0"}),
        ("created_at", "TEXT", "when the row was written (ISO-8601 UTC)", {"nn": 1, "dflt": NOW}),
        ("created_by", "TEXT", WHO, {"nn": 1, "dflt": "'direct edit'"}),
    ])),
}
INDEXES = {"reading_ref": [("idx_reading_ref_verse_id", "verse_id"), ("idx_reading_ref_file_id", "file_id")],
           "reading_section": [("idx_reading_section_file_id", "file_id")]}
COMPOSITE_INDEXES = [("reading_ref", "idx_reading_ref_book_chapter", ["book", "chapter"])]
ENUMS = [("config_module", "reading_index"),
         ("reading_ref.kind", "verse"), ("reading_ref.kind", "whole chapter"),
         ("reading_ref.found_by", "explicit"), ("reading_ref.found_by", "follow-on c:v"),
         ("reading_ref.found_by", "follow-on v."),
         ("reading_ref.line_kind", "heading"), ("reading_ref.line_kind", "table row"),
         ("reading_ref.line_kind", "bullet"), ("reading_ref.line_kind", "paragraph")]
SEE = "see lib/readingindex.py (escalation #2228)"
STEPS = [("build", "build", "index the study files under reading_index.roots: new and changed files read (sha256), "
          "removed ones marked; every verse reference with its file, section, line and how it was found; stops "
          "between files after reading_index.max_seconds", ["reading_file", "reading_section", "reading_ref"]),
         ("report", "report", "the coverage report from reading_file/reading_section/reading_ref (read-only)", [])]
SETTINGS = [
    ("reading_index.roots", ["_analytics/Clusters"], "reading_index",
     "the folders Reading-Index.ps1 indexes (repo-relative; archive/ folders inside are skipped). Only the cluster "
     "readings, by the researcher's exclusions of 2026-10-22 (#2228)"),
    ("reading_index.output_dir", "outputs/reading-index", "reading_index",
     "where Reading-Index.ps1 -Step Report writes the coverage report (#2228)"),
    ("reading_index.max_seconds", 120, "reading_index",
     "time guard on a build: it stops between files once past this many seconds and the next build carries on "
     "(researcher 2026-10-23, #2228: 'the tool does not work for longer than expected')"),
    ("verse_scope.max_verses", 4000, "verse_scope",
     "size guard on the scope resolver: a request whose result has more verses is refused, to be reformed "
     "(researcher 2026-10-23, #2228). 4000 lets any single M cluster through (the largest, M72, has 3,972) and "
     "refuses a T cluster or a thread of many clusters (OT-108: 29,743)"),
    ("verse_scope.max_seconds", 30, "verse_scope",
     "time guard on the scope resolver: a request still resolving after this many seconds is refused, to be "
     "reformed (researcher 2026-10-23, #2228)"),
]
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
UTILITIES = [
    ("readingindex", "iba/app/lib/readingindex.py", "readingindex.py -- the cluster reading index (escalation "
     "#2228 tool 2): build() reads the study files under reading_index.roots into reading_file, reading_section and "
     "reading_ref (incremental by sha256, time-guarded); report() the coverage report.", 0, None),
    ("handlers_readingindex", "iba/app/handlers/readingindex.py", "handlers/readingindex.py -- the run.py handlers "
     "for work package reading-index (Reading-Index.ps1 -Step Build/Report); the logic is in lib/readingindex.py "
     "(escalation #2228).", 0, None),
    ("Reading-Index.ps1", "iba/app/ps/Reading-Index.ps1", "PS entry point for the cluster reading index (escalation "
     "#2228); dispatches through run.py, work package reading-index.", 1,
     "thin wrapper; config is read by the handlers through run.py"),
]


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for t, (grain, use, cs) in TABLES.items():
        if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", t):
            ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": t, "grain": grain, "use": use,
                                                    "inactive": 0, "category": "data"}))
        for c in cs:
            if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", t, c["name"]):
                ops.append(("cfg_column", "insert", {}, c))
    for t, idx in INDEXES.items():
        for name, c in idx:
            if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=?", t, name):
                ops.append(("cfg_index", "insert", {}, {"table_name": t, "name": name, "col": c, "ordinal": 0}))
    for t, name, cs in COMPOSITE_INDEXES:
        for i, c in enumerate(cs):
            if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=? AND col=?", t, name, c):
                ops.append(("cfg_index", "insert", {}, {"table_name": t, "name": name, "col": c, "ordinal": i}))
    for name, value in ENUMS:
        if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, value):
            o = conn.execute("SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
            ops.append(("cfg_enum", "insert", {}, {"name": name, "value": value, "ordinal": o, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Reading-Index.ps1",
                                                       "runs_over": "none", "chained": 0, "inactive": 0}))
    for i, (step, fn, does, grants) in enumerate(STEPS):
        sid = f"reading_index.{step}"
        if not has("SELECT 1 FROM cfg_step WHERE step=?", sid):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": i, "step": sid,
                                                   "handler": f"iba.app.handlers.readingindex:{fn}", "scope": "none",
                                                   "does": f"{does} -- {SEE}", "inactive": 0, "kind": "utility"}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", sid):
            ops.append(("cfg_on_fail", "insert", {}, {"step": sid, "condition": "refused", "path": "report-continue",
                                                      "resolver": None, "message": REFUSED, "route": "terminal",
                                                      "inactive": 0}))
        for t in grants:
            if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?", sid, t):
                ops.append(("cfg_write_grant", "insert", {}, {"writer": sid, "table_name": t, "database": "iba",
                                                              "inactive": 0}))
    if not has("SELECT 1 FROM cfg_report WHERE step='reading_index.report'"):
        ops.append(("cfg_report", "insert", {}, {"step": "reading_index.report", "title": "Cluster reading index coverage",
                                                 "show_toc": 0, "footer_text": None, "output_kind": "md",
                                                 "naming_scheme": "dated", "archive_dir": "archive", "inactive": 0}))
    for key, value, module, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "module": module,
                                                      "inactive": 0, "use": use}))
    for module, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose,
                                                      "inactive": 0, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0,
                                                      "crash_escalation_note": None}))
    if has("SELECT 1 FROM cfg_utility WHERE module='versescope' AND config_exempt=1"):
        ops.append(("cfg_utility", "update", {"module": "versescope"}, {"config_exempt": 0, "config_exempt_reason": None}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2228 tool 2: the reading index tables, work package "
                       f"reading-index, its settings, and the scope resolver's guard settings; run_id {RUN_ID}. "
                       f"inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    live = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    missing = [t for t in TABLES if t not in live]
    if a.dry_run or (not ops and not missing):
        print(f"{'DRY RUN -- ' if a.dry_run else 'already applied -- '}{len(ops)} write(s); tables to create: {missing}")
        return 0
    try:
        conn.execute("SAVEPOINT reading_index")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for t in missing:
            create_sql, index_sql = table_ddl(cfg, t)
            conn.execute(create_sql)
            for sql in index_sql:
                conn.execute(sql)
        conn.execute("RELEASE reading_index")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO reading_index")
        conn.execute("RELEASE reading_index")
        raise
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail); tables created: {missing}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
