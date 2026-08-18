"""bootstrap_prose_authority_v1_20260818.py — ONE-OFF, idempotent. Escalation #714
(GR-PROG-001 reframed + GR-PROG-002 superseded, both researcher-approved 2026-08-18): the
programme prose (`Workflow/Programme/programme_prose/`) is the project's canonical authority on
what the project is about, currently undefined/unscoped/uncontrolled in IBA. Parts (a)/(b)/(c)/(e)
of the six-part plan (full text: `iba/app/reports/gr-prog-001-prose-canonical-authority-plan-
20260818.md`), executed here:

  (a) `governance.prose_canonical_authority` -- the entry-point anchor.
  (b)/(c) `cfg_prose_chapter` (one row per programme-prose chapter) and `cfg_prose_concept` (a
      pointer index -- "this key concept lives at this chapter/section", not a copy of the prose
      itself) -- both registered in cfg_table/cfg_column.
  (e) Two concept rows seeded, both direct successors of the two `wa_rule_registry` rows folded
      into this escalation: `verse_primacy` (GR-PROG-001, "the verse always leads") points at
      chapter 1; `inner_being_definition` (GR-PROG-002, the governing question, superseded by the
      prose per researcher decision) points at chapter 1's "Defining Inner Being"/"This
      Inner-Being Programme" sections, confirmed present in the live 2026-08-14 extract.

Chapter status (0-3 reviewed/final, 4-6 not yet aligned) is per the researcher's direct statement
2026-08-18 -- NOT re-derived from the prose extract file's own per-section `status` metadata, which
still shows `draft` on every section including 0-3 as of the 2026-08-14 export (flagged, not
resolved, in the plan doc's discrepancy note). Part (d) (an escalation to align chapters 4-6) and
part (f) (methodology-change-flags-prose-staleness) are separate follow-on items, not built here --
see the module's own `main()` for exactly what this script does and doesn't do.

    python -m iba.app.migration.bootstrap_prose_authority_v1_20260818
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_DDL = """
CREATE TABLE IF NOT EXISTS cfg_prose_chapter (
    chapter      INTEGER PRIMARY KEY,
    title        TEXT NOT NULL,
    status       TEXT NOT NULL,
    source_doc   TEXT NOT NULL,
    description  TEXT,
    added_at     TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cfg_prose_concept (
    concept_key  TEXT PRIMARY KEY,
    chapter      INTEGER NOT NULL REFERENCES cfg_prose_chapter(chapter),
    section_hint TEXT NOT NULL,
    description  TEXT NOT NULL,
    source       TEXT NOT NULL,
    added_at     TEXT NOT NULL
);
"""

_NOW = "2026-08-18T08:15:00Z"
_SOURCE_DOC = "Workflow/Programme/programme_prose/wa-programme-prose-programme-20260814.md"

_CHAPTERS = [
    (0, "Preamble", "reviewed",
     "Programme preamble -- what the study is, framed for a reader coming to it fresh."),
    (1, "Programme purpose", "reviewed",
     "Mission, scope, this inner-being programme, defining inner being, science and the Bible, "
     "expected outcome -- the project's governing question lives here."),
    (2, "Research methodology", "reviewed",
     "Research method overview, word selection/registry construction, programme flow, science "
     "in action, publishing, key methodological principles and constraints."),
    (3, "Research approach", "reviewed",
     "Traceability and evidential warrant, the two-AI division of responsibility, session "
     "continuity and memory discipline."),
    (4, "Data architecture", "not_yet_aligned",
     "Escalation pending (part (d), separate item) -- content not yet checked against the live "
     "iba.db/bible_research.db split this file itself documents (2026-08-15 architecture "
     "correction postdates this chapter's last prose revision)."),
    (5, "Data integrity & governance", "not_yet_aligned",
     "Escalation pending (part (d)) -- likely superseded in places by iba/app/GOVERNANCE.md's "
     "live config-driven model."),
    (6, "Instruction corpus", "not_yet_aligned",
     "Escalation pending (part (d)) -- likely stale against the current Workflow/Instructions/ "
     "[current]-token document set."),
]

_CONCEPTS = [
    ("verse_primacy", 1, "Defining Inner Being / This Inner-Being Programme sections",
     "The verse is the primary unit of evidence; findings and dimensions emerge from verse "
     "evidence, never bent to fit a pre-existing category. Direct successor of wa_rule_registry "
     "GR-PROG-001 (obsolete 2026-08-17) -- this pointer replaces the rule's own restated text.",
     "wa_rule_registry GR-PROG-001; escalation #714"),
    ("inner_being_definition", 1, "Defining Inner Being / This Inner-Being Programme sections",
     "The programme's governing question: what does Scripture reveal about the characteristics, "
     "operations, and interrelationships of the human inner being (spirit, soul, body)? "
     "Supersedes wa_rule_registry GR-PROG-002 (obsolete 2026-08-17) per researcher decision "
     "2026-08-18 -- GR-PROG-002 is retired as a rule; this pointer to the prose is now the "
     "canonical reference, not a restated rule text.",
     "wa_rule_registry GR-PROG-002 (superseded); escalation #714"),
]


def _setting(conn, key, value, use, module, report):
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
        conn.execute("INSERT INTO cfg_setting (key, value, use, module) VALUES (?,?,?,?)",
                    (key, value, use, module))
        report.append(f"cfg_setting {key!r} added")
    else:
        report.append(f"cfg_setting {key!r} already present")


def _enum(conn, name, value, report):
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, value)).fetchone():
        n = conn.execute("SELECT COUNT(*) FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
        conn.execute("INSERT INTO cfg_enum VALUES (?,?,?,0)", (name, value, n))
        report.append(f"cfg_enum {name} += {value!r}")
    else:
        report.append(f"cfg_enum {name} already has {value!r}")


def _write_grant(conn, writer, table_name, report):
    if not conn.execute(
            "SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'",
            (writer, table_name)).fetchone():
        conn.execute("INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
                    "VALUES (?,?,'iba',0)", (writer, table_name))
        report.append(f"cfg_write_grant ({writer!r}, {table_name!r}) added")
    else:
        report.append(f"cfg_write_grant ({writer!r}, {table_name!r}) already present")


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
                "'migration/bootstrap_prose_authority_v1_20260818.py')",
                (name, col, ordinal, coltype, ispk, notnull, colnuse))
            report.append(f"cfg_column ({name}.{col}) added")
        else:
            report.append(f"cfg_column ({name}.{col}) already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    conn.executescript(_DDL)
    report.append("cfg_prose_chapter + cfg_prose_concept tables ensured")

    _enum(conn, "config_module", "prose", report)
    _enum(conn, "prose_chapter_status", "reviewed", report)
    _enum(conn, "prose_chapter_status", "not_yet_aligned", report)

    _setting(conn, "governance.prose_canonical_authority",
             '"The programme prose (Workflow/Programme/programme_prose/) is the canonical '
             'authority on what the project is about -- researcher, 2026-08-18. Chapters 0-3 '
             'are reviewed and final; chapters 4-6 are not yet aligned (escalation pending, '
             'part (d)). cfg_prose_chapter names each chapter and its status; cfg_prose_concept '
             'points a key project concept (e.g. verse primacy, the inner-being definition) at '
             'the prose section that defines it, rather than restating the definition as a '
             'separate rule. A methodology/approach change that touches a concept named in '
             'cfg_prose_concept should flag whether the prose needs updating (part (f) -- the '
             'flagging MECHANISM is not yet built, this states the principle only)."',
             "entry-point anchor for the prose-as-canonical-authority work -- part (a) of "
             "escalation #714", "governance", report)

    for chapter, title, status, description in _CHAPTERS:
        if not conn.execute("SELECT 1 FROM cfg_prose_chapter WHERE chapter=?", (chapter,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_prose_chapter (chapter, title, status, source_doc, description, "
                "added_at) VALUES (?,?,?,?,?,?)",
                (chapter, title, status, _SOURCE_DOC, description, _NOW))
            report.append(f"cfg_prose_chapter {chapter} ({title!r}) added, status={status}")
        else:
            report.append(f"cfg_prose_chapter {chapter} already present")

    for concept_key, chapter, section_hint, description, source in _CONCEPTS:
        if not conn.execute(
                "SELECT 1 FROM cfg_prose_concept WHERE concept_key=?", (concept_key,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_prose_concept (concept_key, chapter, section_hint, description, "
                "source, added_at) VALUES (?,?,?,?,?,?)",
                (concept_key, chapter, section_hint, description, source, _NOW))
            report.append(f"cfg_prose_concept {concept_key!r} added -> chapter {chapter}")
        else:
            report.append(f"cfg_prose_concept {concept_key!r} already present")

    _write_grant(conn, "configmaint.propose", "cfg_prose_chapter", report)
    _table_and_columns(conn, "cfg_prose_chapter",
                       "one row per programme-prose chapter",
                       "the chapter-level registry for governance.prose_canonical_authority -- "
                       "which chapters exist, their review status, and which live prose extract "
                       "file is their source. Does not hold the prose text itself (that stays in "
                       "Workflow/Programme/programme_prose/ and/or bible_research.db's "
                       "prose_section) -- this is the index, not a copy.",
                       [("chapter", "INTEGER", 1, 1, "the chapter number (0-6 currently)"),
                        ("title", "TEXT", 0, 1, "the chapter's title"),
                        ("status", "TEXT", 0, 1, "'reviewed' (final, per researcher 2026-08-18) "
                        "or 'not_yet_aligned' (per cfg_enum prose_chapter_status) -- NOT derived "
                        "from the prose extract file's own per-section status metadata, which is "
                        "known stale (still shows 'draft' everywhere as of 2026-08-14)"),
                        ("source_doc", "TEXT", 0, 1, "the live prose extract file this chapter's "
                        "content comes from"),
                        ("description", "TEXT", 0, 0, "what this chapter covers"),
                        ("added_at", "TEXT", 0, 1, "when this chapter was registered")],
                       report)
    _write_grant(conn, "configmaint.propose", "cfg_prose_concept", report)
    _table_and_columns(conn, "cfg_prose_concept",
                       "one row per key project concept pointed at its defining prose location",
                       "a pointer index: 'this concept is DEFINED at this chapter/section of the "
                       "prose' -- not a copy of the definition. Direct replacement mechanism for "
                       "wa_rule_registry rows like GR-PROG-001/GR-PROG-002 that used to restate a "
                       "definition as rule text; this points at the authoritative prose instead, "
                       "per cfg_behaviour_rule 'documentation.single-authority-pointer-not-copy'.",
                       [("concept_key", "TEXT", 1, 1, "short kebab/snake-case identifier, e.g. "
                        "'verse_primacy'"),
                        ("chapter", "INTEGER", 0, 1, "which cfg_prose_chapter defines this "
                        "concept"),
                        ("section_hint", "TEXT", 0, 1, "which section(s) within the chapter, in "
                        "plain language (prose sections aren't independently keyed yet)"),
                        ("description", "TEXT", 0, 1, "a short gloss of the concept, for "
                        "discoverability -- the prose itself remains authoritative for the full "
                        "definition"),
                        ("source", "TEXT", 0, 1, "provenance -- which prior rule/decision this "
                        "concept pointer replaces or derives from"),
                        ("added_at", "TEXT", 0, 1, "when this concept was registered")],
                       report)

    conn.commit()
    conn.close()

    print("prose-canonical-authority bootstrap (escalation #714, parts a/b/c/e):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
