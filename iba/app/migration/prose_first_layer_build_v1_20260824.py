"""prose_first_layer_build_v1_20260824.py — ONE-OFF, idempotent: builds escalation #829's approved
consolidated proposal (`iba/docs/prose-management-iba-first-layer-proposal-v9-20260824.md`).

Everything below writes to `iba.db` only — no schema change to `bible_research.db` in this build
(the two dropped/added columns on `prose_section`/`prose_section_type` were #836's build, already
applied). Covers, per the approved proposal's §5/§9:

  (IV)  cfg_prose table + 4 rows
  (V)   cfg_column -- fill 4 blank prose_section_type rows, correct 4 prose_section citation texts
        (the 3 stale prose_section rows need no action -- already cfg_column.inactive=1, §1.3d)
  (I/III/V) cfg_enum -- status(4), author(3), source_stage(11), lifecycle_tag(4), book_label(4)
  (III) cfg_status_flow -- 4 rows, entity='prose_section'
  (III) cfg_behaviour_rule -- 2 rows (session_a_replace gate, two-patch ordering) + 1 row
        (prose-quality-flag-on-upstream-change, §12.3)
  (III) cfg_write_grant -- 3 rows, database='bible_research'
  (II)  cfg_work_package 'prose' + 5 cfg_step rows (incl. prose.flag)
  (I)   cfg_utility -- reactivate the 4 original scripts, superseded-pointer purpose text

D10 (prose.book_stage_map vs. book_label, §6) is explicitly DEFERRED per researcher instruction
(2026-08-24: "D10 will be edited in prose edit stage, not in this IBA processing build") -- no code
change to book_stage_map's filter logic in this build; the known 1-row limitation stays documented
in cfg_prose.use text only.

    python -m iba.app.migration.prose_first_layer_build_v1_20260824
"""
from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def _cfg_prose(conn: sqlite3.Connection, report: list[str]) -> None:
    if not conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='cfg_prose'").fetchone():
        conn.execute("""
            CREATE TABLE cfg_prose (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                use TEXT NOT NULL,
                inactive INTEGER NOT NULL DEFAULT 0
            )
        """)
        report.append("iba.db: cfg_prose table created")
    else:
        report.append("iba.db: cfg_prose table already present")

    # Self-registration (governance.tables/governance.table_columns) -- cfg_prose is itself a
    # table and needs cataloguing, same as every other table in the project. Matches cfg_passage's
    # own precedent exactly (escalation #798/#799). Found live 2026-08-24, configmaint.validate
    # report-stop: cfg_prose had no cfg_write_grant row for writer 'configmaint.propose' either --
    # fixed together with this, same root cause (the table's own governance rows were never
    # written when the table was created).
    if not conn.execute(
            "SELECT 1 FROM cfg_table WHERE database='iba' AND name='cfg_prose'").fetchone():
        conn.execute(
            "INSERT INTO cfg_table (database, name, grain, use, inactive) "
            "VALUES ('iba','cfg_prose','one row per key',?,0)",
            ("Module-specific settings for the prose module (governance.module.config) -- "
             "chapter_names/book_stage_map/search_default_limit/edit_file_dir, escalation #829.",))
        report.append("iba.db: cfg_table row for cfg_prose inserted")
    else:
        report.append("iba.db: cfg_table row for cfg_prose already present")

    prose_cols = [
        ("key", 0, "TEXT",
         "the setting's key, e.g. 'prose.book_stage_map' -- kept identical to the pre-#829 "
         "cfg_setting key text so no caller string changes, only the table read from"),
        ("value", 1, "TEXT", "JSON-encoded value, same convention as cfg_setting.value"),
        ("use", 2, "TEXT", "what the setting controls and why"),
        ("inactive", 3, "INTEGER", "soft-disable flag, same convention as cfg_setting"),
    ]
    for col, ordinal, typ, use in prose_cols:
        if not conn.execute(
                "SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='cfg_prose' "
                "AND name=?", (col,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_column (database, table_name, name, ordinal, \"type\", is_pk, "
                "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by) "
                "VALUES ('iba','cfg_prose',?,?,?,?,1,0,NULL,NULL,?,NULL,NULL,"
                "'migration/prose_first_layer_build_v1_20260824.py')",
                (col, ordinal, typ, 1 if col == "key" else 0, use))
    report.append("iba.db: cfg_column rows for cfg_prose's 4 columns inserted/confirmed")

    if not conn.execute(
            "SELECT 1 FROM cfg_write_grant WHERE writer='configmaint.propose' "
            "AND table_name='cfg_prose' AND database='iba'").fetchone():
        conn.execute(
            "INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
            "VALUES ('configmaint.propose','cfg_prose','iba',0)")
        report.append("iba.db: cfg_write_grant 'configmaint.propose'->'cfg_prose' inserted")
    else:
        report.append("iba.db: cfg_write_grant 'configmaint.propose'->'cfg_prose' already present")

    rows = [
        ("prose.chapter_names",
         '{"0":"Preamble","1":"Programme purpose","2":"Research methodology","3":"Research '
         'approach","4":"Data architecture","5":"Data integrity & governance","6":"Instruction '
         'corpus"}',
         "Chapter-number -> readable-name lookup for the extract's Markdown/Word output. Read by "
         "prosestore.py:chapter_names(cfg). Fixes build_programme_prose_extract.py's "
         "NON-COMPLIANT (#648) flag."),
        ("prose.book_stage_map",
         '{"Programme":["programme"],"Detail design":["session_a","session_b","session_b_phase9",'
         '"session_c","session_d"],"Findings":["synthesis","verse-analysis","findings"],'
         '"Essays":["essay"]}',
         "Allowed --book values + source_stage filter set for prose.extract/Prose.ps1. "
         "'contributor' (2 types) deliberately excluded -- a staging area, not a book. KNOWN "
         "LIMITATION (escalation #829 D10, researcher decision 2026-08-24: deferred to the prose "
         "edit stage, not fixed in this build): 1 of 949 prose_section_type rows "
         "(prog_purp_observations_framework, id 78) has source_stage='programme' but "
         "book_label='Detail design' -- this stage-based map will file it under 'Programme', "
         "disagreeing with its own book_label. Read by prosestore.py:book_stage_map(cfg)."),
        ("prose.search_default_limit", "100",
         "Default result cap for search_prose.py/prose.search. Read by "
         "prosestore.py:search_default_limit(cfg). Fixes search_prose.py's #648 flag."),
        ("prose.edit_file_dir", '"outputs/markdown/prose-edits"',
         "Directory export_chapter writes editable .md into, and import_chapter archives from "
         "({value}/archive/) on success. Replaces the hardcoded CHAPTER_EDIT_OUT_DIR constant. "
         "Read by prosestore.py:edit_file_dir(cfg)."),
    ]
    for key, value, use in rows:
        if not conn.execute("SELECT 1 FROM cfg_prose WHERE key=?", (key,)).fetchone():
            conn.execute("INSERT INTO cfg_prose (key, value, use, inactive) VALUES (?,?,?,0)",
                         (key, value, use))
            report.append(f"iba.db: cfg_prose row {key!r} inserted")
        else:
            report.append(f"iba.db: cfg_prose row {key!r} already present")


def _cfg_column_fixes(conn: sqlite3.Connection, report: list[str]) -> None:
    fill = [
        ("prose_section_type", "book_order",
         "Display order of the 4 live books: 1=Programme, 2=Detail design, 3=Findings, 4=Essays. "
         "Paired 1:1 with book_label."),
        ("prose_section_type", "book_label",
         "Which of the 4 live books this type belongs to -- see cfg_enum group "
         "prose_section_type_book_label. NULL on 5 types (contributor pair + the 3 unbooked "
         "findings-stage types, escalation #832). See escalation #829 D10 for the one row where "
         "this disagrees with prose.book_stage_map's stage-based derivation."),
        ("prose_section_type", "section_order",
         "Ordering of the named sub-groupings within a book (e.g. within Detail design: Session "
         "A=1, Session B=2, ... Session B Phase 9=5, Observation framework=6) -- a level between "
         "book and chapter."),
        ("prose_section_type", "section_label",
         "The named sub-grouping itself (e.g. Session A, Verse analysis, Synthesis, Observation "
         "framework) -- human label for section_order's position."),
        ("prose_section", "registry_id",
         "The word_registry entry the section is about, where word-scoped. 15% populated "
         "(141/949) -- most sections are chapter- or cluster-scoped rather than word-scoped. "
         "Citation column (researcher, 2026-08-24): belongs in a future index table (book 5, "
         "Concordance), not directly on prose_section -- not acted on now, Concordance is out of "
         "scope for this build; likely to become redundant once that index table exists."),
        ("prose_section", "cluster_code",
         "The M-code cluster the section belongs to, where cluster-scoped. 18% populated "
         "(175/949), free text, no FK to cluster (0 live orphans, checked). Citation column "
         "(researcher, 2026-08-24): belongs in a future index table (book 5, Concordance), same "
         "reasoning as registry_id -- not hardened with an FK now, not acted on now (escalation "
         "#832)."),
        ("prose_section", "characteristic_id",
         "The characteristic the section discusses, where characteristic-scoped. 13% populated "
         "(124/949). Citation column (researcher, 2026-08-24): belongs in a future index table "
         "(book 5, Concordance), same reasoning as registry_id/cluster_code -- not acted on now."),
        ("prose_section", "cluster_subgroup_id",
         "Declared and indexed to scope a section to a cluster subgroup. 100% NULL -- never used. "
         "Citation column (researcher, 2026-08-24): belongs in a future index table (book 5, "
         "Concordance), same reasoning as its siblings -- not dropped now, not acted on now "
         "(escalation #832)."),
    ]
    for table, col, use in fill:
        conn.execute(
            "UPDATE cfg_column SET use=? WHERE database='bible_research' "
            "AND table_name=? AND name=?", (use, table, col))
    report.append("iba.db: cfg_column.use written for 4 prose_section_type + 4 prose_section "
                   "citation columns")


def _cfg_enum(conn: sqlite3.Connection, report: list[str]) -> None:
    groups: dict[str, list[str]] = {
        "prose_section_status": ["draft", "in_review", "approved", "archived"],
        "prose_section_author": ["claude_ai", "claude_code", "researcher"],
        "prose_section_type_source_stage": [
            "programme", "session_a", "session_b", "session_b_phase9", "session_c", "session_d",
            "synthesis", "verse-analysis", "findings", "essay", "contributor",
        ],
        "prose_section_type_lifecycle_tag": ["source", "v1", "v2", "v3"],
        "prose_section_type_book_label": ["Programme", "Detail design", "Findings", "Essays"],
    }
    for name, values in groups.items():
        if conn.execute("SELECT 1 FROM cfg_enum WHERE name=?", (name,)).fetchone():
            report.append(f"iba.db: cfg_enum group {name!r} already present")
            continue
        conn.executemany(
            "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
            [(name, v, i) for i, v in enumerate(values)],
        )
        report.append(f"iba.db: cfg_enum group {name!r} inserted ({len(values)} values)")


def _cfg_status_flow(conn: sqlite3.Connection, report: list[str]) -> None:
    rows = [
        ("draft", "apply_session_patch.py: prose_section insert/supersede/bulk_supersede "
                  "(caller-supplied, the default when omitted)", 0),
        ("in_review", "apply_session_patch.py: prose_section insert/supersede (caller-supplied "
                      "status -- no dedicated transition op exists; 0 rows currently at this "
                      "status)", 1),
        ("approved", "apply_session_patch.py: prose_section approve (the one dedicated transition "
                     "op -- also stamps approved_at/approved_by)", 2),
        ("archived", "apply_session_patch.py: prose_section insert (caller-supplied status only "
                     "-- 11 existing rows were archived at insert time, not via a transition op)",
         3),
    ]
    if conn.execute(
            "SELECT 1 FROM cfg_status_flow WHERE entity='prose_section'").fetchone():
        report.append("iba.db: cfg_status_flow rows for prose_section already present")
        return
    conn.executemany(
        "INSERT INTO cfg_status_flow (entity, status, set_by, ordinal, inactive) "
        "VALUES ('prose_section',?,?,?,0)",
        rows,
    )
    report.append("iba.db: cfg_status_flow -- 4 rows inserted, entity='prose_section'")


def _cfg_behaviour_rule(conn: sqlite3.Connection, report: list[str]) -> None:
    rules = [
        ("prose-section-session-a-replace-author-gate",
         "The session_a_replace operation updates a prose_section row in place. Code-gated on "
         "author='claude_code'; permitted only for Session A mechanical extracts, because they "
         "are reproducible from structured data rather than analytical judgement. Under Model A "
         "(escalation #836) every write is in-place, so this is one of several in-place write "
         "paths, distinguished by its author-gate, not by being uniquely non-supersede.",
         "docs/prose-store-architecture.md sec5.2/sec6.1; escalation #784/#829; reworded per #836",
         "apply_session_patch.py's UPDATE ... WHERE id=? AND author='claude_code' clause"),
        ("prose-section-two-patch-ordering",
         "A new prose chapter reaches the database in two ordered patches: CATALOGUE_POPULATION "
         "first (creates prose_section_type handles), then PROSE (content, referencing handles "
         "by section_type_id_lookup: {code}). Applying PROSE before its CATALOGUE_POPULATION "
         "fails at the code lookup, by design.",
         "docs/prose-store-architecture.md sec7; escalation #784/#829",
         "apply_session_patch.py's section_type_id_lookup resolution"),
        ("prose-quality-flag-on-upstream-change",
         "When a methodology, terminology, or finding change makes existing prose content stale, "
         "the obligation is to raise a wa_data_quality_flags entry (flag_group='PROSE_QUALITY') "
         "against the affected prose_section row(s) -- not to stop and rewrite the prose in "
         "place. Prose gets fixed later, in its own pass; the flag is what prevents the drift "
         "from being silently lost in the meantime.",
         "Researcher, 2026-08-23, escalation #829",
         "Not mechanically enforced -- a discipline rule, made real and queryable via "
         "cfg_behaviour_rule, not automated."),
    ]
    for rule_key, rule_text, source, enforced_by in rules:
        if conn.execute(
                "SELECT 1 FROM cfg_behaviour_rule WHERE class='sqlite' AND rule_key=?",
                (rule_key,)).fetchone():
            report.append(f"iba.db: cfg_behaviour_rule {rule_key!r} already present")
            continue
        conn.execute(
            "INSERT INTO cfg_behaviour_rule (class, rule_key, rule_text, source, enforced_by, "
            "added_at, active) VALUES ('sqlite',?,?,?,?,'2026-08-24T00:00:00Z',1)",
            (rule_key, rule_text, source, enforced_by))
        report.append(f"iba.db: cfg_behaviour_rule {rule_key!r} inserted")


def _cfg_write_grant(conn: sqlite3.Connection, report: list[str]) -> None:
    grants = [
        ("apply_session_patch", "prose_section"),
        ("apply_session_patch", "prose_section_type"),
        ("prose_flag", "wa_data_quality_flags"),
    ]
    for writer, table in grants:
        if conn.execute(
                "SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? "
                "AND database='bible_research'", (writer, table)).fetchone():
            report.append(f"iba.db: cfg_write_grant {writer!r}->{table!r} already present")
            continue
        conn.execute(
            "INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
            "VALUES (?,?,'bible_research',0)", (writer, table))
        report.append(f"iba.db: cfg_write_grant {writer!r}->{table!r} inserted")


def _dispatcher(conn: sqlite3.Connection, report: list[str]) -> None:
    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name='prose'").fetchone():
        conn.execute(
            "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, "
            "complete_message, next_step_hint, paused_message, inactive) "
            "VALUES ('prose','iba/app/ps/Prose.ps1','none',0,NULL,NULL,NULL,0)")
        report.append("iba.db: cfg_work_package 'prose' inserted")
    else:
        report.append("iba.db: cfg_work_package 'prose' already present")

    steps = [
        (0, "prose.extract", "iba.app.handlers.prose:extract", "utility",
         "Programme-prose extract (JSON/MD/DOCX)"),
        (1, "prose.search", "iba.app.handlers.prose:search", "utility",
         "FTS/plain search over prose_section"),
        (2, "prose.export_chapter", "iba.app.handlers.prose:export_chapter", "utility",
         "Export a chapter to editable .md"),
        (3, "prose.import_chapter", "iba.app.handlers.prose:import_chapter", "utility",
         "Turn an edited .md into a patch file (writes no DB row itself)"),
        (4, "prose.flag", "iba.app.handlers.prose:flag", "utility",
         "Raise one wa_data_quality_flags instance (escalation #829 sec12.4, angle a) -- "
         "--flag-code, --description (required), no prose-section reference"),
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


def _reactivate_scripts(conn: sqlite3.Connection, report: list[str]) -> None:
    scripts = {
        "scripts/build_programme_prose_extract.py":
            "Superseded by iba/app/lib/prosestore.py (escalation #784) -- logic now lives there, "
            "exercised via prose.extract (Prose.ps1 -Step Extract). Kept as the documented CLI "
            "entry point (docs/prose-store-architecture.md sec8), reactivated (escalation #829).",
        "scripts/export_prose_chapter_edit.py":
            "Superseded by iba/app/lib/prosestore.py (escalation #784) -- logic now lives there, "
            "exercised via prose.export_chapter (Prose.ps1 -Step ExportChapter). Kept as the "
            "documented CLI entry point, reactivated (escalation #829).",
        "scripts/import_prose_chapter_edit.py":
            "Superseded by iba/app/lib/prosestore.py (escalation #784) -- logic now lives there, "
            "exercised via prose.import_chapter (Prose.ps1 -Step ImportChapter). Kept as the "
            "documented CLI entry point, reactivated (escalation #829).",
        "scripts/search_prose.py":
            "Superseded by iba/app/lib/prosestore.py (escalation #784) -- logic now lives there, "
            "exercised via prose.search (Prose.ps1 -Step Search). Kept as the documented CLI "
            "entry point, reactivated (escalation #829).",
    }
    for path, purpose in scripts.items():
        row = conn.execute(
            "SELECT inactive, purpose FROM cfg_utility WHERE file_path=?", (path,)).fetchone()
        if row is None:
            report.append(f"iba.db: WARNING -- no cfg_utility row for {path!r}, skipped")
            continue
        if row["inactive"] == 0 and row["purpose"] == purpose:
            report.append(f"iba.db: cfg_utility {path!r} already reactivated with current text")
            continue
        conn.execute(
            "UPDATE cfg_utility SET inactive=0, purpose=? WHERE file_path=?", (purpose, path))
        report.append(f"iba.db: cfg_utility {path!r} reactivated (inactive->0), purpose text "
                       "updated")


def _register_self(conn: sqlite3.Connection, report: list[str]) -> None:
    if conn.execute("SELECT 1 FROM cfg_utility WHERE module=?",
                     ("prose_first_layer_build_v1_20260824",)).fetchone():
        return
    conn.execute(
        "INSERT INTO cfg_utility (module, file_path, purpose, inactive) VALUES (?,?,?,1)",
        ("prose_first_layer_build_v1_20260824",
         "iba/app/migration/prose_first_layer_build_v1_20260824.py",
         "ONE-OFF migration, escalation #829 (Prose management IBA first-layer) -- builds "
         "cfg_prose, fills/corrects cfg_column use text, cfg_enum (5 groups), cfg_status_flow, "
         "cfg_behaviour_rule (3 rows), cfg_write_grant (3 rows), the prose work package + 5 "
         "cfg_step rows, reactivates the 4 original scripts. D10 (book_stage_map vs. book_label) "
         "deliberately deferred, not built here. inactive=1 once applied -- a one-off, not a "
         "reusable routine."))
    report.append("iba.db: cfg_utility row for this migration registered")


def main() -> int:
    report: list[str] = []
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    _cfg_prose(conn, report)
    _cfg_column_fixes(conn, report)
    _cfg_enum(conn, report)
    _cfg_status_flow(conn, report)
    _cfg_behaviour_rule(conn, report)
    _cfg_write_grant(conn, report)
    _dispatcher(conn, report)
    _reactivate_scripts(conn, report)
    _register_self(conn, report)
    conn.commit()
    conn.close()
    print("Prose first-layer build (escalation #829):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
