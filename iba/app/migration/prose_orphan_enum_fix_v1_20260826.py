"""prose_orphan_enum_fix_v1_20260826.py — ONE-OFF, idempotent: closes escalations
#896/#900/#901/#902 (the 7 orphan `cfg_enum` groups found across #829/#836's builds) per the
researcher's own direct rule, verbatim (2026-08-26): *"if the config is enforced but the
validation does[n't] pick it up, then the validation must be adjusted; if the config is not used,
then adjust the script to make use of it; if the config is useless then remove it."*

Full analysis: `iba/app/reports/orphan-enum-findings-896-900-901-902-20260826.md`. None of the 7
are useless — all document live, populated vocabularies — so branch 3 doesn't apply to any of
them. Two real branches, both closed here:

  BRANCH 1 (config enforced, checker blind to it) — `prose_section.status`/`.author`,
  `record_change_log.change_type`/`.status`: already `CHECK`-constrained live. Fix the checker:
  `cfg_column.expectation = 'enum.<name>'` on each backing column — the documented, already-used-
  elsewhere exemption mechanism (matches `cfg_setting`'s own `pattern:<key>` exemption). This also
  ACTIVATES `find_enum_violations` for these 4 going forward — real, structural, live-data
  checking, not just orphan-silencing.

  BRANCH 2 (config genuinely unused) — `prose_section_type.source_stage`/`.lifecycle_tag`/
  `.book_label`: no `CHECK`, no code call site, nothing. Fix the code: add real `CHECK`
  constraints to `prose_section_type` matching each enum's live values (SQLite has no
  `ALTER TABLE ... ADD CONSTRAINT` — rebuilt via the standard create-new/copy/drop/rename
  technique, in one transaction, row count verified before/after). Then the SAME
  `cfg_column.expectation` wiring as branch 1, so these 3 get the identical real enforcement the
  other 4 already had, not a second-class version of it.

    python -m iba.app.migration.prose_orphan_enum_fix_v1_20260826
"""
from __future__ import annotations

import datetime
import os
import shutil
import sqlite3
import sys

from ..lib.cfg import Cfg, DB_PATH

_ENUM_VALUES = {
    "prose_section_type_source_stage": [
        "programme", "session_a", "session_b", "session_b_phase9", "session_c", "session_d",
        "synthesis", "verse-analysis", "findings", "essay", "contributor",
    ],
    "prose_section_type_lifecycle_tag": ["source", "v1", "v2", "v3"],
    "prose_section_type_book_label": ["Programme", "Detail design", "Findings", "Essays"],
}


def _backup_bible_research(report: list[str]) -> None:
    src = Cfg().database_path("bible_research")
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d_%H%M%S")
    project_root = os.path.abspath(os.path.join(os.path.dirname(src), ".."))
    backups_dir = os.path.join(project_root, "backups")
    os.makedirs(backups_dir, exist_ok=True)
    dest = os.path.join(backups_dir, f"bible_research_backup_{stamp}_PROSE-ORPHAN-ENUM-FIX.db")
    shutil.copy2(src, dest)
    report.append(f"[BACKUP] {os.path.basename(dest)}")


def _rebuild_prose_section_type(report: list[str]) -> None:
    """Branch 2 -- add the 3 missing CHECK constraints via the standard SQLite rebuild technique.
    PRAGMA foreign_keys enforcement is OFF app-wide at runtime (lib/db.py Db docstring; confirmed
    live, no connection in this codebase enables it for bible_research.db), so DROP+RENAME here
    doesn't need special FK handling -- prose_section.section_type_id keeps resolving correctly
    afterward because every id is copied across unchanged."""
    conn = sqlite3.connect(Cfg().database_path("bible_research"))
    conn.row_factory = sqlite3.Row
    try:
        already_done = conn.execute(
            "SELECT sql FROM sqlite_master WHERE name='prose_section_type'").fetchone()
        if already_done and "CHECK (source_stage IN" in (already_done["sql"] or ""):
            report.append("bible_research.db: prose_section_type already has the 3 CHECK "
                           "constraints -- skipped")
            return

        before_count = conn.execute("SELECT COUNT(*) c FROM prose_section_type").fetchone()["c"]

        stage_list = ",".join(f"'{v}'" for v in _ENUM_VALUES["prose_section_type_source_stage"])
        lifecycle_list = ",".join(
            f"'{v}'" for v in _ENUM_VALUES["prose_section_type_lifecycle_tag"])
        book_list = ",".join(f"'{v}'" for v in _ENUM_VALUES["prose_section_type_book_label"])

        conn.execute("BEGIN")
        conn.execute(f"""
            CREATE TABLE prose_section_type_new (
                id                   INTEGER PRIMARY KEY,
                code                 TEXT    NOT NULL UNIQUE,
                label                TEXT    NOT NULL,
                source_stage         TEXT    NOT NULL,
                lifecycle_tag        TEXT,
                chapter_no           INTEGER,
                description          TEXT,
                expected_length_min  INTEGER,
                expected_length_max  INTEGER,
                sort_order           INTEGER NOT NULL DEFAULT 0,
                delete_flagged       INTEGER NOT NULL DEFAULT 0,
                created_at           TEXT    NOT NULL DEFAULT (datetime('now')),
                book_order           INTEGER,
                book_label           TEXT,
                section_order        INTEGER,
                section_label        TEXT,
                version              INTEGER,
                updated_at           TEXT,
                CHECK (source_stage IN ({stage_list})),
                CHECK (lifecycle_tag IS NULL OR lifecycle_tag IN ({lifecycle_list})),
                CHECK (book_label IS NULL OR book_label IN ({book_list}))
            )
        """)
        conn.execute("""
            INSERT INTO prose_section_type_new
            SELECT id, code, label, source_stage, lifecycle_tag, chapter_no, description,
                   expected_length_min, expected_length_max, sort_order, delete_flagged,
                   created_at, book_order, book_label, section_order, section_label, version,
                   updated_at
            FROM prose_section_type
        """)
        after_count = conn.execute(
            "SELECT COUNT(*) c FROM prose_section_type_new").fetchone()["c"]
        if after_count != before_count:
            conn.execute("ROLLBACK")
            raise RuntimeError(
                f"row count mismatch during prose_section_type rebuild: {before_count} -> "
                f"{after_count} -- rolled back, nothing changed")
        conn.execute("DROP TABLE prose_section_type")
        # legacy_alter_table=ON: without it, SQLite's modern ALTER TABLE RENAME tries to
        # recompile every OTHER trigger that references the target name as part of its own
        # reference-fixup pass -- prose_section_ai/_au (FTS sync triggers on prose_section, both
        # already correctly say 'prose_section_type', not the temp '_new' name) get recompiled
        # mid-statement, at the exact moment the target name doesn't exist yet (the rename hasn't
        # completed), and the whole ALTER fails: "no such table: main.prose_section_type". Found
        # live, not assumed -- reproduced once before this fix. legacy_alter_table skips that
        # unneeded fixup pass entirely (the trigger bodies already say the right name), which is
        # exactly what's needed here. Connection-scoped, not persisted to the DB file.
        conn.execute("PRAGMA legacy_alter_table = ON")
        conn.execute("ALTER TABLE prose_section_type_new RENAME TO prose_section_type")
        conn.execute("PRAGMA legacy_alter_table = OFF")
        conn.execute("""
            CREATE INDEX idx_pst_stage_lifecycle
            ON prose_section_type(source_stage, lifecycle_tag)
            WHERE delete_flagged = 0
        """)
        conn.commit()
        report.append(
            f"bible_research.db: prose_section_type rebuilt with 3 new CHECK constraints "
            f"(source_stage/lifecycle_tag/book_label) -- {after_count} rows preserved "
            f"({before_count} before), idx_pst_stage_lifecycle recreated")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def _wire_expectations(conn: sqlite3.Connection, report: list[str]) -> None:
    """Both branches converge here -- every one of the 7 gets the same real, checked link."""
    targets = [
        ("prose_section", "status", "prose_section_status"),
        ("prose_section", "author", "prose_section_author"),
        ("record_change_log", "change_type", "record_change_log_change_type"),
        ("record_change_log", "status", "record_change_log_status"),
        ("prose_section_type", "source_stage", "prose_section_type_source_stage"),
        ("prose_section_type", "lifecycle_tag", "prose_section_type_lifecycle_tag"),
        ("prose_section_type", "book_label", "prose_section_type_book_label"),
    ]
    for table, col, enum_name in targets:
        cur = conn.execute(
            "UPDATE cfg_column SET expectation=? WHERE database='bible_research' "
            "AND table_name=? AND name=? AND (expectation IS NULL OR expectation != ?)",
            (f"enum.{enum_name}", table, col, f"enum.{enum_name}"))
        if cur.rowcount:
            report.append(f"iba.db: cfg_column {table}.{col}.expectation = 'enum.{enum_name}' set")
        else:
            report.append(f"iba.db: cfg_column {table}.{col}.expectation already set")

    # The 3 branch-2 columns' own cfg_column.use text still says "Uncontrolled: no CHECK or FK
    # constrains..." -- now false, corrected to match the other 4's "CHECK-constrained" wording.
    corrections = {
        ("prose_section_type", "source_stage"): (
            "The programme stage that produces this kind of prose -- 'programme' for "
            "documentation plus the session_a/b/c/d family. CHECK-constrained (escalation #896/"
            "#900/#901/#902, 2026-08-26 -- previously uncontrolled, closed per the researcher's "
            "own rule: 'if the config is not used, adjust the script to make use of it')."),
        ("prose_section_type", "lifecycle_tag"): (
            "Marks the generation of the type, using values like 'v1', 'v2' and 'source'. 77% "
            "NULL, so most types carry no lifecycle marker at all and the tag distinguishes only "
            "the reworked ones. CHECK-constrained (escalation #896/#900/#901/#902, 2026-08-26)."),
        ("prose_section_type", "book_label"): (
            "Which of the 4 live books this type belongs to -- see cfg_enum group "
            "prose_section_type_book_label. NULL on 5 types (contributor pair + the 3 unbooked "
            "findings-stage types, escalation #832). CHECK-constrained (escalation #896/#900/"
            "#901/#902, 2026-08-26 -- previously uncontrolled). See escalation #890 D6 (resolved "
            "as a non-issue) for the one row previously thought to disagree with "
            "prose.book_stage_map's stage-based derivation."),
    }
    for (table, col), use in corrections.items():
        conn.execute(
            "UPDATE cfg_column SET \"use\"=? WHERE database='bible_research' AND table_name=? "
            "AND name=?", (use, table, col))
    report.append("iba.db: cfg_column.use text corrected for the 3 branch-2 columns "
                   "('Uncontrolled' -> 'CHECK-constrained')")


def _register_self(conn: sqlite3.Connection, report: list[str]) -> None:
    module = "prose_orphan_enum_fix_v1_20260826"
    if conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone():
        return
    conn.execute(
        "INSERT INTO cfg_utility (module, file_path, purpose, inactive) VALUES (?,?,?,1)",
        (module, f"iba/app/migration/{module}.py",
         "ONE-OFF migration, escalations #896/#900/#901/#902 -- closes the 7 orphan cfg_enum "
         "findings per the researcher's own rule: fix the validator for the 4 already-CHECK-"
         "enforced groups (cfg_column.expectation wired); fix the code for the 3 genuinely "
         "unenforced prose_section_type groups (real CHECK constraints added, then the same "
         "expectation wiring). inactive=1 once applied -- a one-off, not a reusable routine."))
    report.append("iba.db: cfg_utility row for this migration registered")


def main() -> int:
    report: list[str] = []
    _backup_bible_research(report)
    _rebuild_prose_section_type(report)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    _wire_expectations(conn, report)
    _register_self(conn, report)
    conn.commit()
    conn.close()
    print("Orphan-enum fix (escalations #896/#900/#901/#902):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
