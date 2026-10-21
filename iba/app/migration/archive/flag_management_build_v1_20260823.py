"""flag_management_build_v1_20260823.py — ONE-OFF, idempotent: builds escalation #833's approved
proposal (`iba/docs/flag-management-proposal-v1-20260823.md`).

Two databases, one build:

`bible_research.db` (`wa_quality_flag_types`/`wa_data_quality_flags` repurpose) — the destructive
part of this migration was already executed live, interactively, with a verified pre-op backup
(`backups/bible_research_pre_flagmgmt_<timestamp>.db`) and the full test-plan cases run and
confirmed (cascade trigger, no-false-positive, optional columns) before this script was written.
The DDL below is reproduced here for a real, re-runnable, idempotent artifact — each step checks
live state first and is a no-op if already applied, so re-running this script is always safe.

`iba.db` (governance) — the non-destructive, first-time-run part: `cfg_column.inactive` (a new
column, mirroring `cfg_table.inactive`'s own `add_cfg_table_inactive_column.py` bootstrap exactly),
`cfg_table`/`cfg_column` re-catalogue for the repurposed pair, `phase2_flag_types.inactive=1`,
`cfg_column.inactive=1` on the two dead columns named in escalation #833, and a `cfg_behaviour_rule`
row recording `wa_session_research_flags`' deliberate as-is retention.

    python -m iba.app.migration.flag_management_build_v1_20260823
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import Cfg, DB_PATH


def _bible_research_side(report: list[str]) -> None:
    cfg = Cfg()
    path = cfg.database_path("bible_research")
    cfg.close()
    conn = sqlite3.connect(path)

    cols_types = {r[1] for r in conn.execute('PRAGMA table_info("wa_quality_flag_types")')}
    already_repurposed = "delete_flagged" in cols_types and "deprecated" not in cols_types
    if already_repurposed:
        report.append("bible_research.db: wa_quality_flag_types/wa_data_quality_flags already "
                       "repurposed (delete_flagged present, deprecated absent) -- no-op")
    else:
        conn.execute("DELETE FROM wa_data_quality_flags")
        conn.execute("DELETE FROM wa_quality_flag_types")
        conn.execute("DROP TABLE wa_quality_flag_types")
        conn.execute("""
            CREATE TABLE wa_quality_flag_types (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                flag_group    TEXT NOT NULL,
                flag_code     TEXT NOT NULL UNIQUE,
                description   TEXT,
                delete_flagged INTEGER NOT NULL DEFAULT 0,
                deprecation_note TEXT,
                category      TEXT,
                research_actions TEXT
            )
        """)
        conn.execute("DROP TABLE wa_data_quality_flags")
        conn.execute("""
            CREATE TABLE wa_data_quality_flags (
                id               INTEGER PRIMARY KEY AUTOINCREMENT,
                strong_id        TEXT,
                verse_id         INTEGER,
                flag_id          INTEGER NOT NULL REFERENCES wa_quality_flag_types(id),
                description      TEXT,
                corrective_action TEXT,
                correction_date  TEXT,
                delete_flagged   INTEGER NOT NULL DEFAULT 0,
                last_changed     TEXT
            )
        """)
        conn.executemany(
            "INSERT INTO wa_quality_flag_types (flag_group, flag_code, description) "
            "VALUES (?,?,?)",
            [
                ("PROSE_QUALITY", "Terminology change",
                 "Prose text uses terminology superseded by a later methodology/naming decision."),
                ("PROSE_QUALITY", "Methodology change",
                 "Prose describes a process or method that has since changed."),
                ("PROSE_QUALITY", "Style change",
                 "Prose doesn't conform to the current style/authoring convention."),
            ],
        )
        report.append("bible_research.db: wa_quality_flag_types/wa_data_quality_flags hard-deleted"
                       " and rebuilt to the prose-quality shape, 3 types reseeded")

    if not conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type='trigger' "
            "AND name='wa_quality_flag_types_cascade_delete'").fetchone():
        conn.execute("""
            CREATE TRIGGER wa_quality_flag_types_cascade_delete
            AFTER UPDATE OF delete_flagged ON wa_quality_flag_types
            WHEN NEW.delete_flagged = 1 AND OLD.delete_flagged = 0
            BEGIN
                UPDATE wa_data_quality_flags SET delete_flagged = 1 WHERE flag_id = NEW.id;
            END
        """)
        report.append("bible_research.db: wa_quality_flag_types_cascade_delete trigger created")
    else:
        report.append("bible_research.db: cascade trigger already present")

    conn.commit()
    conn.close()


def _cfg_column_inactive(conn: sqlite3.Connection, report: list[str]) -> None:
    """Mirrors add_cfg_table_inactive_column.py's (#678) exact pattern for cfg_table."""
    cols = {r[1] for r in conn.execute('PRAGMA table_info("cfg_column")')}
    if "inactive" not in cols:
        conn.execute('ALTER TABLE "cfg_column" ADD COLUMN inactive INTEGER NOT NULL DEFAULT 0')
        report.append("iba.db: cfg_column.inactive column added (physical ALTER)")
    else:
        report.append("iba.db: cfg_column.inactive already present")

    if not conn.execute(
            "SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='cfg_column' "
            "AND name='inactive'").fetchone():
        ordinal = conn.execute(
            "SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_column "
            "WHERE database='iba' AND table_name='cfg_column'").fetchone()[0]
        conn.execute(
            'INSERT INTO cfg_column (database, table_name, name, ordinal, "type", is_pk, '
            '"notnull", is_unique, dflt, fk, "use", expectation, source, filled_by) '
            "VALUES ('iba','cfg_column','inactive',?,'INTEGER',0,1,0,'0',NULL,?,NULL,NULL,"
            "'migration/flag_management_build_v1_20260823.py')",
            (ordinal,
             "a column that is declared but dead (never populated, or the concept it served is "
             "retired) is marked inactive=1 here -- symmetric with cfg_table.inactive (escalation "
             "#678), not DB-enforced (nothing stops a write to it), but makes the fact "
             "config-known and queryable. Escalation #833, researcher: 'this may not be DB "
             "enforceable, but at least it sets the config that the column is not used.'"))
        report.append("iba.db: cfg_column row for cfg_column.inactive added (self-documenting)")
    else:
        report.append("iba.db: cfg_column row for cfg_column.inactive already present")


def _iba_side(report: list[str]) -> None:
    conn = sqlite3.connect(DB_PATH)

    _cfg_column_inactive(conn, report)

    # wa_quality_flag_types/wa_data_quality_flags re-catalogue -- was term-quality, now prose-quality.
    conn.execute(
        "UPDATE cfg_table SET use=?, inactive=0 WHERE database='bible_research' "
        "AND name='wa_quality_flag_types'",
        ("Repurposed 2026-08-23 (escalation #833) as the prose-quality-check flag vocabulary -- "
         "prior term-quality content (29 codes) hard-deleted, no data carried over. flag_group is "
         "a free descriptive label (PROSE_QUALITY for now); flag_code names the kind of prose "
         "issue (e.g. 'Terminology change'); delete_flagged (renamed from deprecated) retiring a "
         "type here cascades (trigger wa_quality_flag_types_cascade_delete) to soft-delete every "
         "wa_data_quality_flags row that uses it.",))
    conn.execute(
        "UPDATE cfg_table SET use=?, inactive=0 WHERE database='bible_research' "
        "AND name='wa_data_quality_flags'",
        ("Repurposed 2026-08-23 (escalation #833) as prose-quality-check instances -- prior "
         "term-quality content (19,866 rows) hard-deleted, no data carried over. strong_id "
         "(renamed from term_id) and verse_id (renamed from file_id) are both optional, "
         "documented-only references (no enforced FK -- strong_id's natural target is iba.db's "
         "own strong table, which SQLite cannot FK across database files to); description states "
         "the issue, corrective_action states the remedy, correction_date when it was applied.",))
    report.append("iba.db: cfg_table.use rewritten for the repurposed pair; "
                   "wa_data_quality_flags.inactive -> 0")

    for col, use in [
        ("id", "Surrogate primary key for the prose-quality flag type."),
        ("flag_group", "Free descriptive grouping label; 'PROSE_QUALITY' for every type seeded so "
                        "far (escalation #833) -- a real taxonomy may emerge as more types do."),
        ("flag_code", "The prose-quality issue this type names, e.g. 'Terminology change'. Unique."),
        ("description", "What the type covers, in prose."),
        ("delete_flagged", "Soft-delete for the type -- renamed from the retired term-quality "
                            "'deprecated' column (escalation #833) for project-wide naming "
                            "consistency. Setting this to 1 cascades to every wa_data_quality_flags "
                            "row using the type (trigger wa_quality_flag_types_cascade_delete)."),
        ("deprecation_note", "Why a type was retired, if delete_flagged=1. Carried over unchanged "
                              "from the pre-repurpose schema."),
        ("category", "Legacy column, unused by the prose-quality vocabulary so far."),
        ("research_actions", "Legacy column, unused by the prose-quality vocabulary so far."),
    ]:
        conn.execute(
            "UPDATE cfg_column SET use=? WHERE database='bible_research' "
            "AND table_name='wa_quality_flag_types' AND name=?", (use, col))

    for col, use in [
        ("id", "Surrogate primary key for the prose-quality flag instance."),
        ("strong_id", "Optional. Renamed from term_id (escalation #833) -- the Strong's number "
                       "this flag concerns, where relevant. Documented-only reference to iba.db's "
                       "own strong table; not an enforced FK (SQLite cannot enforce a foreign key "
                       "across two separate database files)."),
        ("verse_id", "Optional. Renamed from file_id (escalation #833) -- the verse this flag "
                      "concerns, where relevant. No enforced FK; target table not yet settled."),
        ("flag_id", "FK to wa_quality_flag_types -- which prose-quality issue this is."),
        ("description", "The specific issue -- what needs to change and why."),
        ("corrective_action", "New (escalation #833). What was/should be done to correct the "
                               "issue named in description."),
        ("correction_date", "New (escalation #833). When the corrective action was taken."),
        ("delete_flagged", "New (escalation #833). Soft-delete; also set automatically when the "
                            "row's flag_id type is itself soft-deleted."),
        ("last_changed", "Carried over unchanged from the pre-repurpose schema."),
    ]:
        conn.execute(
            "UPDATE cfg_column SET use=? WHERE database='bible_research' "
            "AND table_name='wa_data_quality_flags' AND name=?", (use, col))
    report.append("iba.db: cfg_column.use rewritten for both repurposed tables' columns")

    # phase2_flag_types -> inactive=1, matching its junctions (already inactive).
    conn.execute(
        "UPDATE cfg_table SET inactive=1 WHERE database='bible_research' "
        "AND name='phase2_flag_types'")
    report.append("iba.db: cfg_table phase2_flag_types.inactive -> 1")

    # The two dead columns named in escalation #833.
    for tbl, col in [("passage", "review_flag"), ("session_d_observations", "researcher_flag")]:
        conn.execute(
            "UPDATE cfg_column SET inactive=1 WHERE database='bible_research' "
            "AND table_name=? AND name=?", (tbl, col))
        report.append(f"iba.db: cfg_column {tbl}.{col}.inactive -> 1")

    # wa_session_research_flags -- kept exactly as-is, recorded as deliberate.
    if not conn.execute(
            "SELECT 1 FROM cfg_behaviour_rule WHERE class='sqlite' "
            "AND rule_key='wa-session-research-flags-retained-as-is'").fetchone():
        conn.execute(
            "INSERT INTO cfg_behaviour_rule (class, rule_key, rule_text, source, enforced_by, "
            "added_at, active) VALUES ('sqlite','wa-session-research-flags-retained-as-is',?,?,?,"
            "'2026-08-23T00:00:00Z',1)",
            ("wa_session_research_flags (bible_research.db, 715 rows) is the live, deliberately "
             "unchanged analysis-phase flag/pointer mechanism -- researcher, escalation #833: "
             "'wa_session_research_flags are analysis phase, and at this point stay as is, and "
             "should be alive and incorporated in IBA.' No cfg_write_grant exists yet because "
             "nothing in governed code currently writes to it; one gets added when analytics work "
             "actually resumes and a real writer exists, not invented ahead of need. Known "
             "data-quality issues (priority/session_target vocabulary drift, cluster_link as a "
             "non-junction string) are deferred to the analytics-phase restart, not fixed here.",
             "escalation #833 (Flag Management), iba/docs/flag-management-proposal-v1-20260823.md "
             "section 3b",
             "not mechanically enforced -- a recorded governance fact, not a validated rule"))
        report.append("iba.db: cfg_behaviour_rule wa-session-research-flags-retained-as-is added")
    else:
        report.append("iba.db: cfg_behaviour_rule for wa_session_research_flags already present")

    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?",
                         ("flag_management_build_v1_20260823",)).fetchone():
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive) VALUES (?,?,?,1)",
            ("flag_management_build_v1_20260823",
             "iba/app/migration/flag_management_build_v1_20260823.py",
             "ONE-OFF migration, escalation #833 (Flag Management) -- repurposes "
             "wa_quality_flag_types/wa_data_quality_flags for prose-quality checks, adds "
             "cfg_column.inactive, retires phase2_flag_types, marks 2 dead columns inactive, "
             "records wa_session_research_flags' retention. inactive=1 once applied -- a one-off, "
             "not a reusable routine."))
        report.append("iba.db: cfg_utility row for this migration registered")

    conn.commit()
    conn.close()


def main() -> int:
    report: list[str] = []
    _bible_research_side(report)
    _iba_side(report)
    print("Flag Management build (escalation #833):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
