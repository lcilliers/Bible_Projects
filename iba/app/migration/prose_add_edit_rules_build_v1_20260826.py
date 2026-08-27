"""prose_add_edit_rules_build_v1_20260826.py — ONE-OFF, idempotent: builds escalation #890's
approved proposal (`iba/docs/prose-add-edit-rules-proposal-v1-20260826.md`), decisions D1-D6.

D1 (leave `prose_section_finding_link`'s FK as-is) needs no build action -- a decision to not act,
not a build item.

Covers:
  D2  cfg_behaviour_rule -- new prose_section_type-creation gate (discipline rule, not code --
      matches the existing prose-quality-flag-on-upstream-change precedent)
  D4  prose_section_verse_link -- bible_research.db table + iba.db cfg_table/cfg_column (4 rows) +
      cfg_write_grant (the apply_session_patch.py write op itself is code, applied separately)
  D5  cfg_step -- prose.flag_fix_propose / prose.flag_fix_apply (2 new rows under the existing
      'prose' work package; the handler/prosestore code is applied separately)
  D6  cfg_prose.book_stage_map's `use` text corrected -- D10 turned out to be a stale docstring/
      config claim, not a real filtering bug (extract_programme_prose already reads book_label
      directly); see iba/app/lib/prosestore.py:book_stage_map()'s own corrected docstring

    python -m iba.app.migration.prose_add_edit_rules_build_v1_20260826
"""
from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import Cfg, DB_PATH


def _bible_research_schema(report: list[str]) -> None:
    conn = sqlite3.connect(Cfg().database_path("bible_research"))
    conn.row_factory = sqlite3.Row
    try:
        if not conn.execute(
                "SELECT 1 FROM sqlite_master WHERE type='table' "
                "AND name='prose_section_verse_link'").fetchone():
            conn.execute("""
                CREATE TABLE prose_section_verse_link (
                    prose_section_id INTEGER NOT NULL REFERENCES prose_section(id),
                    verse_reference   TEXT NOT NULL,
                    link_type         TEXT NOT NULL DEFAULT 'discusses',
                    created_at        TEXT NOT NULL DEFAULT (datetime('now')),
                    PRIMARY KEY (prose_section_id, verse_reference, link_type)
                )
            """)
            report.append("bible_research.db: prose_section_verse_link table created")
        else:
            report.append("bible_research.db: prose_section_verse_link table already present")
        conn.commit()
    finally:
        conn.close()


def _cfg_table_and_columns(conn: sqlite3.Connection, report: list[str]) -> None:
    if not conn.execute(
            "SELECT 1 FROM cfg_table WHERE database='bible_research' "
            "AND name='prose_section_verse_link'").fetchone():
        conn.execute(
            "INSERT INTO cfg_table (database, name, grain, use, inactive) "
            "VALUES ('bible_research','prose_section_verse_link',"
            "'one row per (prose_section_id, verse_reference, link_type)',?,0)",
            ("The verse-grounding link for prose sections (escalation #890 D4, resolving #784 "
             "sec13's 'verse is king' structural gap) -- which verse(s) a section cites, "
             "supplied explicitly by the writer, not text-mined from body. Loose "
             "verse_reference string (matches wa_verse_records.reference format, e.g. "
             "'Ps 32:1'), not an FK -- bible_research.db cannot FK to iba.db's own canonical "
             "verse table, and no single one-row-per-verse table exists inside "
             "bible_research.db itself to target instead.",))
        report.append("iba.db: cfg_table row for prose_section_verse_link inserted")
    else:
        report.append("iba.db: cfg_table row for prose_section_verse_link already present")

    # is_pk=0 on all 4, even though the live table has a real 3-column composite PK
    # (prose_section_id/verse_reference/link_type) -- matches the EXACT established convention
    # of the two precedent link tables (prose_section_finding_link/prose_section_dimension_link,
    # checked live: both catalogue is_pk=0 across every column despite their own composite PKs).
    # configmaint.validate's schema-integrity check treats cfg_column.is_pk COUNT>1 as a hard
    # coherence error with no exemption for legitimate composite-key junction tables (checked
    # live, iba/app/handlers/configmaint.py:_validate_live) -- following the precedent already
    # established for this exact table shape, not inventing a different one.
    cols = [
        ("prose_section_id", 0, "INTEGER", 1, 0, "prose_section.id",
         "Identifies the citing prose section, with an FK to prose_section. Part of the live "
         "3-column composite PK (prose_section_id, verse_reference, link_type) -- is_pk=0 here "
         "matches the established cfg_column convention for this table shape (see "
         "prose_section_finding_link/prose_section_dimension_link, escalation #829/#890)."),
        ("verse_reference", 1, "TEXT", 1, 0, None,
         "The cited verse, as a loose reference string matching wa_verse_records.reference's "
         "own format (e.g. 'Ps 32:1') -- not an FK (see cfg_table.use for why). Part of the "
         "composite PK, see prose_section_id's note."),
        ("link_type", 2, "TEXT", 1, 0, None,
         "Qualifies the relationship, defaulting to 'discusses' -- same convention as "
         "prose_section_finding_link/prose_section_dimension_link. Part of the composite PK, "
         "see prose_section_id's note."),
        ("created_at", 3, "TEXT", 1, 0, None,
         "Insertion timestamp, defaulting to datetime('now')."),
    ]
    for name, ordinal, typ, notnull, is_pk, fk, use in cols:
        if conn.execute(
                "SELECT 1 FROM cfg_column WHERE database='bible_research' "
                "AND table_name='prose_section_verse_link' AND name=?", (name,)).fetchone():
            continue
        conn.execute(
            "INSERT INTO cfg_column (database, table_name, name, ordinal, \"type\", is_pk, "
            "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by) "
            "VALUES ('bible_research','prose_section_verse_link',?,?,?,?,?,0,NULL,?,?,NULL,NULL,"
            "'migration/prose_add_edit_rules_build_v1_20260826.py')",
            (name, ordinal, typ, is_pk, notnull, fk, use))
    report.append("iba.db: cfg_column rows for prose_section_verse_link's 4 columns "
                   "inserted/confirmed")

    if not conn.execute(
            "SELECT 1 FROM cfg_write_grant WHERE writer='apply_session_patch' "
            "AND table_name='prose_section_verse_link' AND database='bible_research'").fetchone():
        conn.execute(
            "INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
            "VALUES ('apply_session_patch','prose_section_verse_link','bible_research',0)")
        report.append("iba.db: cfg_write_grant 'apply_session_patch'->'prose_section_verse_link' "
                       "inserted")
    else:
        report.append("iba.db: cfg_write_grant 'apply_session_patch'->'prose_section_verse_link' "
                       "already present")


def _cfg_behaviour_rule(conn: sqlite3.Connection, report: list[str]) -> None:
    rule_key = "prose-section-type-creation-requires-researcher-instruction"
    rule_text = (
        "A new prose_section_type row may only be inserted on explicit researcher instruction "
        "naming the new code and its book_label/source_stage placement -- it is controlled "
        "vocabulary (prose_section_type's own cfg_table.use text: 'the only real enforcement "
        "behind prose_section.section_type_id'), not Claude-originated content, the same "
        "standard already applied project-wide to cfg_enum and other controlled-vocabulary "
        "tables. Governs WHO may trigger the first half of the existing two-patch "
        "(CATALOGUE_POPULATION then PROSE) creation pattern -- that pattern's own ORDERING is "
        "unchanged, governed separately by cfg_behaviour_rule "
        "'prose-section-two-patch-ordering'."
    )
    if conn.execute(
            "SELECT 1 FROM cfg_behaviour_rule WHERE class='sqlite' AND rule_key=?",
            (rule_key,)).fetchone():
        report.append(f"iba.db: cfg_behaviour_rule {rule_key!r} already present")
        return
    conn.execute(
        "INSERT INTO cfg_behaviour_rule (class, rule_key, rule_text, source, enforced_by, "
        "added_at, active) VALUES ('sqlite',?,?,?,?,'2026-08-26T00:00:00Z',1)",
        (rule_key, rule_text, "Researcher, 2026-08-26, escalation #890",
         "Not mechanically enforced -- a discipline rule, made real and queryable via "
         "cfg_behaviour_rule, matching the prose-quality-flag-on-upstream-change precedent "
         "(escalation #829)."))
    report.append(f"iba.db: cfg_behaviour_rule {rule_key!r} inserted")


def _cfg_step(conn: sqlite3.Connection, report: list[str]) -> None:
    steps = [
        (5, "prose.flag_fix_propose", "iba.app.handlers.prose:flag_fix_propose", "utility",
         "Search active prose for a literal match, write a review report of proposed "
         "replacements (escalation #890 D5, flag-fix angle b, propose step -- no DB write)"),
        (6, "prose.flag_fix_apply", "iba.app.handlers.prose:flag_fix_apply", "utility",
         "Generate a PROSE supersede patch for researcher-approved section ids from a "
         "flag_fix_propose report (escalation #890 D5, angle b, apply step -- no DB write, "
         "apply via scripts/apply_session_patch.py)"),
    ]
    for ordinal, step, handler, kind, does in steps:
        if conn.execute(
                "SELECT 1 FROM cfg_step WHERE work_package='prose' AND step=?",
                (step,)).fetchone():
            report.append(f"iba.db: cfg_step 'prose'/{step!r} already present")
            continue
        conn.execute(
            "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
            "inactive, kind) VALUES ('prose',?,?,?,'none',?,0,?)",
            (ordinal, step, handler, does, kind))
        report.append(f"iba.db: cfg_step 'prose'/{step!r} inserted")


def _cfg_prose_d10_correction(conn: sqlite3.Connection, report: list[str]) -> None:
    # D10/D6: the claim that book_stage_map drives filtering (and that id 78 would therefore be
    # misfiled) was checked against the actual call sites this round and found false --
    # extract_programme_prose already queries WHERE book_label = ? directly; book_stage_map is
    # used ONLY to validate the --book CLI argument against the list of real book names. No
    # filtering logic changed (none was needed) -- only the config's own use text, which
    # repeated the same stale claim as the pre-fix docstring.
    new_use = (
        "Allowed --book values for prose.extract/Prose.ps1's CLI validation only "
        "(run_extract's 'book not in book_stage_map(cfg)' check) -- NOT the filter that "
        "decides which prose_section_type rows land in which book; that filter "
        "(extract_programme_prose) already queries book_label directly. D10 RESOLVED "
        "(escalation #890 D6, 2026-08-26): the previous text here claimed a stage-based "
        "filtering behaviour and a resulting 1-row misfile (id 78, "
        "prog_purp_observations_framework) -- checked against the live call sites and found "
        "false; id 78 was already correctly filed under its own book_label ('Detail design'), "
        "not 'Programme'. No functional bug, only a stale claim; see "
        "iba/app/lib/prosestore.py:book_stage_map()'s own corrected docstring. Read by "
        "prosestore.py:book_stage_map(cfg)."
    )
    conn.execute(
        "UPDATE cfg_prose SET use=? WHERE key='prose.book_stage_map'", (new_use,))
    report.append("iba.db: cfg_prose.book_stage_map use text corrected (D10 resolved -- no "
                   "filtering bug, stale claim only)")


def _register_self(conn: sqlite3.Connection, report: list[str]) -> None:
    module = "prose_add_edit_rules_build_v1_20260826"
    if conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone():
        return
    conn.execute(
        "INSERT INTO cfg_utility (module, file_path, purpose, inactive) VALUES (?,?,?,1)",
        (module, f"iba/app/migration/{module}.py",
         "ONE-OFF migration, escalation #890 (Prose add/edit operational rules layer) -- "
         "cfg_behaviour_rule (D2, prose_section_type creation gate), "
         "prose_section_verse_link table + cfg_table/cfg_column/cfg_write_grant (D4), "
         "cfg_step for prose.flag_fix_propose/.flag_fix_apply (D5), cfg_prose.book_stage_map "
         "use-text correction (D6, no filtering bug found). D1 (leave "
         "prose_section_finding_link's FK as-is), D3 (edit-file delete refusal) are code-only, "
         "not this migration. inactive=1 once applied -- a one-off, not a reusable routine."))
    report.append("iba.db: cfg_utility row for this migration registered")


def main() -> int:
    report: list[str] = []
    _bible_research_schema(report)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    _cfg_table_and_columns(conn, report)
    _cfg_behaviour_rule(conn, report)
    _cfg_step(conn, report)
    _cfg_prose_d10_correction(conn, report)
    _register_self(conn, report)
    conn.commit()
    conn.close()
    print("Prose add/edit operational rules build (escalation #890):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
