"""build_closing_sections_schema.py — ONE-OFF, idempotent: creates the Step 7 closing-section
schema for the debate analytic process (`debate-analytic-process-digest-20260805.md` Step 7;
`WA-interpretation-questions-v1.4` Part C, sections 4-8; full design record: `iba/app/reports/
b3-b5-operations-schema-design-20260805.md`, "Closing-section tables (Step 7) — lighter tier").

**Why a direct migration, not `configmaint.propose`.** New tables are DDL — `configmaint.propose`
can only write rows on already-existing tables/columns, not create either (same carve-out class as
`build_operations_schema.py`/`rename_span_reading_to_lexical.py`, GOVERNANCE.md §9B/§14). The design
doc's own text is explicit that this carve-out already covers this exact remaining piece: *"this
design document, once you've reviewed it, is the up-front approval that carve-out requires"* — B3
(2026-08-05) already built the core six tables off this same reviewed document; this migration
completes the remaining, explicitly-deferred "easiest tier to cut" half of the same design, under
the researcher's 2026-08-06 build-phase direction ("all the initial key controls... must be built
into the code... get it done").

**Scope.** The four Step-7 closing-section tables (`passage_linkage`, `passage_insufficiency`,
`passage_emergent_question`, `passage_validation_note`) plus `passage.open_decisions_note` — exactly
as the design doc specified, with one addition not in the original sketch: an `ordinal` column on
each of the four tables. Needed because these are ordered lists attached to a passage (Part C
sections 4-6-7 render them as such), and — more importantly — because the writer built alongside
this migration (`closing.set`, `handlers/operations.py`) reconciles them the same
read-compare-adjudicate-correct way `hib`/`phenomenon`/`operation` already are (BUILD.md §64):
`ordinal` is each row's natural key within its passage, the thing a reconciliation payload
addresses an existing row BY.

Every table follows this app's own standard convention exactly (`id INTEGER PRIMARY KEY`,
`created_at TEXT NOT NULL`, `deleted INTEGER NOT NULL DEFAULT 0`). FK relationships are documented
via `cfg_column.fk` metadata only, matching `verse_lexical`/`hib`/`phenomenon`'s own precedent.

    python -m iba.app.migration.build_closing_sections_schema
"""

from __future__ import annotations

import sqlite3

DB_PATH = "iba/app/db/iba.db"

DDL = {
    "passage_linkage": """
        CREATE TABLE passage_linkage (
            id                INTEGER PRIMARY KEY,
            passage_id        INTEGER NOT NULL,
            from_operation_id INTEGER NOT NULL,
            to_operation_id   INTEGER NOT NULL,
            note              TEXT NOT NULL,
            ordinal           INTEGER NOT NULL DEFAULT 0,
            created_at        TEXT NOT NULL,
            deleted           INTEGER NOT NULL DEFAULT 0
        )""",
    "passage_insufficiency": """
        CREATE TABLE passage_insufficiency (
            id          INTEGER PRIMARY KEY,
            passage_id  INTEGER NOT NULL,
            verse_id    INTEGER,
            note        TEXT NOT NULL,
            ordinal     INTEGER NOT NULL DEFAULT 0,
            created_at  TEXT NOT NULL,
            deleted     INTEGER NOT NULL DEFAULT 0
        )""",
    "passage_emergent_question": """
        CREATE TABLE passage_emergent_question (
            id            INTEGER PRIMARY KEY,
            passage_id    INTEGER NOT NULL,
            verse_id      INTEGER,
            question_text TEXT NOT NULL,
            kind          TEXT NOT NULL,
            ordinal       INTEGER NOT NULL DEFAULT 0,
            created_at    TEXT NOT NULL,
            deleted       INTEGER NOT NULL DEFAULT 0
        )""",
    "passage_validation_note": """
        CREATE TABLE passage_validation_note (
            id            INTEGER PRIMARY KEY,
            passage_id    INTEGER NOT NULL,
            phenomenon_id INTEGER,
            finding_text  TEXT NOT NULL,
            corrected     INTEGER NOT NULL DEFAULT 0,
            ordinal       INTEGER NOT NULL DEFAULT 0,
            created_at    TEXT NOT NULL,
            deleted       INTEGER NOT NULL DEFAULT 0
        )""",
}

# (table, name, ordinal, type, is_pk, notnull, is_unique, dflt, fk, use, expectation, source, filled_by)
COLUMNS = [
    ("passage_linkage", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("passage_linkage", "passage_id", 1, "INTEGER", 0, 1, 0, None, "passage.id", None, None, None, None),
    ("passage_linkage", "from_operation_id", 2, "INTEGER", 0, 1, 0, None, "operation.id",
     "Part C section 4 / Q7 -- a linkage connects two SPECIFIC, already-registered operations in "
     "the same passage, never a pattern across a range", None, None, None),
    ("passage_linkage", "to_operation_id", 3, "INTEGER", 0, 1, 0, None, "operation.id", None,
     None, None, None),
    ("passage_linkage", "note", 4, "TEXT", 0, 1, 0, None, None,
     "what the linkage is -- also where a Q7 SURFACED ABSENCE gets recorded (row with "
     "from=to=the same operation, note explains the absence) rather than passed over silently",
     None, None, None),
    ("passage_linkage", "ordinal", 5, "INTEGER", 0, 1, 0, "0", None,
     "natural key within passage_id for the reconciliation writer", None, None, None),
    ("passage_linkage", "created_at", 6, "TEXT", 0, 1, 0, None, None, "ISO-8601 UTC", None, None, None),
    ("passage_linkage", "deleted", 7, "INTEGER", 0, 1, 0, "0", None,
     "version-aware soft-delete", None, None, None),

    ("passage_insufficiency", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("passage_insufficiency", "passage_id", 1, "INTEGER", 0, 1, 0, None, "passage.id", None,
     None, None, None),
    ("passage_insufficiency", "verse_id", 2, "INTEGER", 0, 0, 0, None, "verse.id",
     "nullable -- an insufficiency can be passage-wide, not always tied to one verse", None, None, None),
    ("passage_insufficiency", "note", 3, "TEXT", 0, 1, 0, None, None,
     "Part C section 5 / Q9 / Part B.7 -- data the base extract does not carry, named not filled "
     "from outside knowledge", None, None, None),
    ("passage_insufficiency", "ordinal", 4, "INTEGER", 0, 1, 0, "0", None,
     "natural key within passage_id for the reconciliation writer", None, None, None),
    ("passage_insufficiency", "created_at", 5, "TEXT", 0, 1, 0, None, None, "ISO-8601 UTC", None, None, None),
    ("passage_insufficiency", "deleted", 6, "INTEGER", 0, 1, 0, "0", None,
     "version-aware soft-delete", None, None, None),

    ("passage_emergent_question", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("passage_emergent_question", "passage_id", 1, "INTEGER", 0, 1, 0, None, "passage.id", None,
     None, None, None),
    ("passage_emergent_question", "verse_id", 2, "INTEGER", 0, 0, 0, None, "verse.id",
     "nullable -- an emergent question can span the whole passage", None, None, None),
    ("passage_emergent_question", "question_text", 3, "TEXT", 0, 1, 0, None, None,
     "Part C section 6 / Q10 -- interpretive forks (Part B.9) and genuine literary/structural "
     "observations (Part B.12, T5) both land here, never in the phenomena register or an operation",
     None, None, None),
    ("passage_emergent_question", "kind", 4, "TEXT", 0, 1, 0, None, None,
     "'interpretive_fork' | 'literary_structural' | 'other'", None, None, None),
    ("passage_emergent_question", "ordinal", 5, "INTEGER", 0, 1, 0, "0", None,
     "natural key within passage_id for the reconciliation writer", None, None, None),
    ("passage_emergent_question", "created_at", 6, "TEXT", 0, 1, 0, None, None, "ISO-8601 UTC", None, None, None),
    ("passage_emergent_question", "deleted", 7, "INTEGER", 0, 1, 0, "0", None,
     "version-aware soft-delete", None, None, None),

    ("passage_validation_note", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("passage_validation_note", "passage_id", 1, "INTEGER", 0, 1, 0, None, "passage.id", None,
     None, None, None),
    ("passage_validation_note", "phenomenon_id", 2, "INTEGER", 0, 0, 0, None, "phenomenon.id",
     "nullable -- a validation finding can be about the passage's debate generally, not always one "
     "phenomenon", None, None, None),
    ("passage_validation_note", "finding_text", 3, "TEXT", 0, 1, 0, None, None,
     "Part C section 7 / Phase 3 step 6 -- is this genuinely an inner-being phenomenon, does its "
     "Phase 1 justification warrant it, does its Phase 2 operation track faithfully back to it",
     None, None, None),
    ("passage_validation_note", "corrected", 4, "INTEGER", 0, 1, 0, "0", None,
     "WA-passage-read-guidance v1.5 step 6: a failure found here is corrected before the debate is "
     "considered filled, not merely logged for later -- this flag records that the correction "
     "actually happened, not just that a finding was noted", None, None, None),
    ("passage_validation_note", "ordinal", 5, "INTEGER", 0, 1, 0, "0", None,
     "natural key within passage_id for the reconciliation writer", None, None, None),
    ("passage_validation_note", "created_at", 6, "TEXT", 0, 1, 0, None, None, "ISO-8601 UTC", None, None, None),
    ("passage_validation_note", "deleted", 7, "INTEGER", 0, 1, 0, "0", None,
     "version-aware soft-delete", None, None, None),
]

TABLES = [
    ("passage_linkage",
     "Part C section 4 (Q7) -- linkages between two specific, already-registered operations in the "
     "same passage, and surfaced non-linkages.",
     "passage_linkage"),
    ("passage_insufficiency",
     "Part C section 5 (Q9/B.7) -- data the base extract does not carry, named not filled.",
     "passage_insufficiency"),
    ("passage_emergent_question",
     "Part C section 6 (Q10/B.9/B.12) -- interpretive forks and genuine literary/structural "
     "observations, tracked per passage, never merged across passages.",
     "passage_emergent_question"),
    ("passage_validation_note",
     "Part C section 7 (Phase 3) -- the closing re-examination of the passage's own phenomena/"
     "operations, corrected before the debate is considered filled.",
     "passage_validation_note"),
]

UNIQUES = [
    ("passage_linkage", "passage_id", 0),
    ("passage_linkage", "ordinal", 1),
    ("passage_insufficiency", "passage_id", 0),
    ("passage_insufficiency", "ordinal", 1),
    ("passage_emergent_question", "passage_id", 0),
    ("passage_emergent_question", "ordinal", 1),
    ("passage_validation_note", "passage_id", 0),
    ("passage_validation_note", "ordinal", 1),
]


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone() is not None


def _column_exists(conn: sqlite3.Connection, table: str, col: str) -> bool:
    return any(r[1] == col for r in conn.execute(f"PRAGMA table_info({table})").fetchall())


def _registered(conn: sqlite3.Connection, table: str) -> bool:
    return conn.execute("SELECT 1 FROM cfg_table WHERE name=?", (table,)).fetchone() is not None


def run(conn: sqlite3.Connection) -> None:
    """Resumable the same way `build_operations_schema.py` is: table creation and cfg_*
    registration tracked and checked independently against actual live state, not against what this
    particular run happened to do (BUILD.md §61's own lesson, applied again here)."""
    created, skipped = [], []
    for name, ddl in DDL.items():
        if _table_exists(conn, name):
            skipped.append(name)
            continue
        conn.execute(ddl)
        created.append(name)

    if not _column_exists(conn, "passage", "open_decisions_note"):
        conn.execute("ALTER TABLE passage ADD COLUMN open_decisions_note TEXT")
        passage_col_added = True
    else:
        passage_col_added = False

    to_register = [n for n, _, _ in TABLES if not _registered(conn, n)]
    if to_register:
        conn.executemany(
            "INSERT INTO cfg_table (name, grain, use) VALUES (?,?,?)",
            [(n, g, u) for n, u, g in TABLES if n in to_register])
        conn.executemany(
            'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", is_unique, '
            "dflt, fk, use, expectation, source, filled_by) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            [c for c in COLUMNS if c[0] in to_register])
        conn.executemany(
            "INSERT INTO cfg_unique (table_name, col, ordinal) VALUES (?,?,?)",
            [u for u in UNIQUES if u[0] in to_register])

    passage_col_registered = conn.execute(
        "SELECT 1 FROM cfg_column WHERE table_name='passage' AND name='open_decisions_note'"
    ).fetchone() is not None
    if not passage_col_registered:
        conn.execute(
            "INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, \"notnull\", is_unique, "
            "dflt, fk, use, expectation, source, filled_by) VALUES "
            "('passage','open_decisions_note',NULL,'TEXT',0,0,0,NULL,NULL,"
            "'Part C section 8 -- short free-text summary of open decisions/next steps for this "
            "passage. Stays a single field, not its own table (design doc: normally short prose, "
            "not a repeating structured list, unlike sections 4-7).',NULL,NULL,NULL)")

    conn.commit()
    print(f"tables created this run: {created or '(none)'}")
    print(f"tables already present: {skipped or '(none)'}")
    print(f"cfg_table/cfg_column/cfg_unique registered this run: {to_register or '(none)'}")
    print(f"passage.open_decisions_note column added: {passage_col_added}")
    print(f"passage.open_decisions_note cfg_column registered this run: {not passage_col_registered}")
    print("NOTE: no cfg_write_grant rows registered here -- see closing.set's own configmaint.propose "
          "batch (handlers/operations.py) for those.")


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    run(conn)
    conn.close()
