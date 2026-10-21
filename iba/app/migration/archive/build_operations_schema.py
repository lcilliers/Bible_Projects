"""build_operations_schema.py — ONE-OFF, idempotent: creates the core B3 schema for the debate
analytic process (`debate-analytic-process-digest-20260805.md` Step 6; full design record:
`iba/app/reports/b3-b5-operations-schema-design-20260805.md`).

**Why a direct migration, not `configmaint.propose`.** New tables are DDL — `configmaint.propose`
can only write rows on already-existing tables/columns, not create either (same carve-out class as
`bootstrap_span_reading.py`/`rename_span_reading_to_lexical.py`, GOVERNANCE.md §9B/§14): a direct,
documented, idempotent bootstrap. The researcher's own extensive review of the design doc across
this session, and explicit "proceed"/"must conform with app governance" direction, is the up-front
design approval that carve-out requires.

**Scope — deliberately narrower than the full design doc.** Builds ONLY the core six tables
(`hib`, `hib_referent_option`, `verse_hib`, `phenomenon`, `operation`, `operation_party`) plus the
one control column (`passage.phenomena_complete_at`) — the part of the design doc that was fully
specified and not itself an open question. **Explicitly NOT built here** (both flagged as open in
the design doc, neither resolved by the researcher yet):

  1. The Step-7 closing-section tables (`passage_linkage`, `passage_insufficiency`,
     `passage_emergent_question`, `passage_validation_note`, `passage.open_decisions_note`) — the
     design doc itself named these the easiest tier to cut/defer.
  2. Any writer for these tables. **No `cfg_write_grant` rows are registered by this migration** —
     there is deliberately no writer yet (the "how does an AI analytical pass actually get written
     into these tables" question, design doc's closing section, is unresolved). An unwritable table
     is the correct, safe state until that's decided — not an oversight.

Every table follows this app's own standard convention exactly (`id INTEGER PRIMARY KEY`,
`created_at TEXT NOT NULL`, `deleted INTEGER NOT NULL DEFAULT 0`, version-aware soft-delete on
rewrite — same as `verse`/`span`/`strong`/`verse_lexical`). FK relationships are documented via
`cfg_column.fk` metadata only, not declared as SQL `FOREIGN KEY` constraints — matching
`verse_lexical`'s own precedent (the most recent comparable table), not `passage`'s older,
inconsistent one.

    python -m iba.app.migration.build_operations_schema
"""

from __future__ import annotations

import sqlite3

DB_PATH = "iba/app/db/iba.db"

DDL = {
    "hib": """
        CREATE TABLE hib (
            id             INTEGER PRIMARY KEY,
            book           TEXT NOT NULL,
            label          TEXT NOT NULL,
            kind           TEXT NOT NULL,
            first_verse_id INTEGER,
            created_at     TEXT NOT NULL,
            deleted        INTEGER NOT NULL DEFAULT 0
        )""",
    "hib_referent_option": """
        CREATE TABLE hib_referent_option (
            id               INTEGER PRIMARY KEY,
            hib_id           INTEGER NOT NULL,
            reading_text     TEXT NOT NULL,
            textual_grounds  TEXT,
            adopted          INTEGER NOT NULL DEFAULT 0,
            ordinal          INTEGER NOT NULL DEFAULT 0,
            created_at       TEXT NOT NULL,
            deleted          INTEGER NOT NULL DEFAULT 0
        )""",
    "verse_hib": """
        CREATE TABLE verse_hib (
            id         INTEGER PRIMARY KEY,
            verse_id   INTEGER NOT NULL,
            hib_id     INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            deleted    INTEGER NOT NULL DEFAULT 0
        )""",
    "phenomenon": """
        CREATE TABLE phenomenon (
            id               INTEGER PRIMARY KEY,
            passage_id       INTEGER NOT NULL,
            verse_id         INTEGER NOT NULL,
            hib_id           INTEGER NOT NULL,
            description      TEXT NOT NULL,
            textual_warrant  TEXT,
            status           TEXT NOT NULL,
            ordinal          INTEGER NOT NULL DEFAULT 0,
            created_at       TEXT NOT NULL,
            deleted          INTEGER NOT NULL DEFAULT 0
        )""",
    "operation": """
        CREATE TABLE operation (
            id               INTEGER PRIMARY KEY,
            phenomenon_id    INTEGER NOT NULL,
            process          TEXT,
            action_type      TEXT,
            decision         TEXT,
            observation_text TEXT,
            description_text TEXT,
            created_at       TEXT NOT NULL,
            deleted          INTEGER NOT NULL DEFAULT 0
        )""",
    "operation_party": """
        CREATE TABLE operation_party (
            id               INTEGER PRIMARY KEY,
            operation_id     INTEGER NOT NULL,
            role             TEXT NOT NULL,
            kind             TEXT NOT NULL,
            detail           TEXT,
            enablement_only  INTEGER NOT NULL DEFAULT 0,
            ordinal          INTEGER NOT NULL DEFAULT 0,
            created_at       TEXT NOT NULL,
            deleted          INTEGER NOT NULL DEFAULT 0
        )""",
}

# (table, name, ordinal, type, is_pk, notnull, is_unique, dflt, fk, use, expectation, source, filled_by)
COLUMNS = [
    ("hib", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("hib", "book", 1, "TEXT", 0, 1, 0, None, None,
     "OSIS book code, same convention as verse.osisId's book segment", None, None, None),
    ("hib", "label", 2, "TEXT", 0, 1, 0, None, None,
     "e.g. 'Daniel', 'the four youths', 'King Belshazzar'", None, None, None),
    ("hib", "kind", 3, "TEXT", 0, 1, 0, None, None,
     "'named' | 'collective' | 'referential' -- debate digest Step 1 (presumptive-candidate / "
     "collective / referential rules)", None, None, None),
    ("hib", "first_verse_id", 4, "INTEGER", 0, 0, 0, None, "verse.id",
     "anchor -- where this HIB was first identified", None, None, None),
    ("hib", "created_at", 5, "TEXT", 0, 1, 0, None, None, "ISO-8601 UTC", None, None, None),
    ("hib", "deleted", 6, "INTEGER", 0, 1, 0, "0", None,
     "version-aware soft-delete, standard convention", None, None, None),

    ("hib_referent_option", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("hib_referent_option", "hib_id", 1, "INTEGER", 0, 1, 0, None, "hib.id",
     "the HIB this referent-crux reading belongs to", None, None, None),
    ("hib_referent_option", "reading_text", 2, "TEXT", 0, 1, 0, None, None,
     "one grammatically-live candidate reading (T4) -- e.g. one option for 'we' in Obad 1",
     None, None, None),
    ("hib_referent_option", "textual_grounds", 3, "TEXT", 0, 0, 0, None, None,
     "why this reading is live", None, None, None),
    ("hib_referent_option", "adopted", 4, "INTEGER", 0, 1, 0, "0", None,
     "exactly one row per hib_id should be 1 -- the explicit choice (T4: 'adopt one explicitly')",
     None, None, None),
    ("hib_referent_option", "ordinal", 5, "INTEGER", 0, 1, 0, "0", None, None, None, None, None),
    ("hib_referent_option", "created_at", 6, "TEXT", 0, 1, 0, None, None, "ISO-8601 UTC", None, None, None),
    ("hib_referent_option", "deleted", 7, "INTEGER", 0, 1, 0, "0", None,
     "version-aware soft-delete", None, None, None),

    ("verse_hib", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("verse_hib", "verse_id", 1, "INTEGER", 0, 1, 0, None, "verse.id", None, None, None, None),
    ("verse_hib", "hib_id", 2, "INTEGER", 0, 1, 0, None, "hib.id",
     "this HIB is present/a presumptive candidate in this verse (debate digest Step 1) -- also "
     "the table B4's future HIB-continuity passage-boundary rule reads from", None, None, None),
    ("verse_hib", "created_at", 3, "TEXT", 0, 1, 0, None, None, "ISO-8601 UTC", None, None, None),
    ("verse_hib", "deleted", 4, "INTEGER", 0, 1, 0, "0", None,
     "version-aware soft-delete", None, None, None),

    ("phenomenon", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("phenomenon", "passage_id", 1, "INTEGER", 0, 1, 0, None, "passage.id", None, None, None, None),
    ("phenomenon", "verse_id", 2, "INTEGER", 0, 1, 0, None, "verse.id", None, None, None, None),
    ("phenomenon", "hib_id", 3, "INTEGER", 0, 1, 0, None, "hib.id", None, None, None, None),
    ("phenomenon", "description", 4, "TEXT", 0, 1, 0, None, None,
     "the phenomenon: a state, disposition, or characteristic of this HIB's inner life (debate "
     "digest Step 3)", None, None, None),
    ("phenomenon", "textual_warrant", 5, "TEXT", 0, 0, 0, None, None,
     "the verb/clause/stated-silence that grounds it (WA-passage-read-guidance step 3b)",
     None, None, None),
    ("phenomenon", "status", 6, "TEXT", 0, 1, 0, None, None,
     "'stated' | 'inferred' | 'silent' -- 'no phenomenon found, silent' is itself a valid row "
     "(WA-interpretation-questions Part B.4), never an omitted one", None, None, None),
    ("phenomenon", "ordinal", 7, "INTEGER", 0, 1, 0, "0", None,
     "allows more than one phenomenon for the same HIB in the same verse (v1.5 step3 note c)",
     None, None, None),
    ("phenomenon", "created_at", 8, "TEXT", 0, 1, 0, None, None, "ISO-8601 UTC", None, None, None),
    ("phenomenon", "deleted", 9, "INTEGER", 0, 1, 0, "0", None,
     "version-aware soft-delete", None, None, None),

    ("operation", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("operation", "phenomenon_id", 1, "INTEGER", 0, 1, 0, None, "phenomenon.id",
     "NOT NULL by design -- the DB-level enforcement of WA-interpretation-questions Part B.12: an "
     "operation may only originate from an already-registered phenomenon", None, None, None),
    ("operation", "process", 2, "TEXT", 0, 0, 0, None, None,
     "state/status, or a movement (come from/go to/impact on/emerge/go away/become evident) -- "
     "v1.4 Q6", None, None, None),
    ("operation", "action_type", 3, "TEXT", 0, 0, 0, None, None,
     "short verb-based label (Q11) -- a label, not a controlled vocabulary (Part B.10)",
     None, None, None),
    ("operation", "decision", 4, "TEXT", 0, 0, 0, None, None,
     "'retain' | 'set_aside' | 'retain_referential' | 'recorded_silence'", None, None, None),
    ("operation", "observation_text", 5, "TEXT", 0, 0, 0, None, None,
     "what the text/span-data states, Strong's codes cited", None, None, None),
    ("operation", "description_text", 6, "TEXT", 0, 0, 0, None, None,
     "debate digest Step 5's descriptive write-up", None, None, None),
    ("operation", "created_at", 7, "TEXT", 0, 1, 0, None, None, "ISO-8601 UTC", None, None, None),
    ("operation", "deleted", 8, "INTEGER", 0, 1, 0, "0", None,
     "version-aware soft-delete", None, None, None),

    ("operation_party", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("operation_party", "operation_id", 1, "INTEGER", 0, 1, 0, None, "operation.id", None, None, None, None),
    ("operation_party", "role", 2, "TEXT", 0, 1, 0, None, None, "'source' | 'target'", None, None, None),
    ("operation_party", "kind", 3, "TEXT", 0, 1, 0, None, None,
     "'self' | 'human' | 'non_human' | 'object_situation' | 'none'", None, None, None),
    ("operation_party", "detail", 4, "TEXT", 0, 0, 0, None, None,
     "which human/object, if named", None, None, None),
    ("operation_party", "enablement_only", 5, "INTEGER", 0, 1, 0, "0", None,
     "role='source' rows only -- Part B.5's source-of-state vs source-of-enablement distinction, "
     "kept structurally separate rather than folded into kind", None, None, None),
    ("operation_party", "ordinal", 6, "INTEGER", 0, 1, 0, "0", None,
     "a phenomenon's operation can have multiple sources/targets (v1.5 step1 note a)",
     None, None, None),
    ("operation_party", "created_at", 7, "TEXT", 0, 1, 0, None, None, "ISO-8601 UTC", None, None, None),
    ("operation_party", "deleted", 8, "INTEGER", 0, 1, 0, "0", None,
     "version-aware soft-delete", None, None, None),
]

TABLES = [
    ("hib", "one row per Human Inner Being identified in a scope (debate digest Step 1) -- "
            "scope-wide, not passage-scoped: the same HIB recurs across many passages of a book.",
     "hib"),
    ("hib_referent_option",
     "one row per grammatically-live referent-crux reading (T4), child of hib.",
     "hib_referent_option"),
    ("verse_hib",
     "one row per HIB present/a presumptive candidate in a given verse (Step 1's per-verse sweep) "
     "-- the input B4's future HIB-continuity passage-boundary rule reads from.",
     "verse_hib"),
    ("phenomenon",
     "the phenomena register (Step 3 output) -- one row per HIB per verse per passage.",
     "phenomenon"),
    ("operation",
     "the operation for a registered phenomenon (Step 4-5 output) -- phenomenon_id NOT NULL "
     "enforces Part B.12 at the DB level.",
     "operation"),
    ("operation_party",
     "one row per source/target of an operation (plural-capable, v1.5 step1 note a), child of "
     "operation.",
     "operation_party"),
]

UNIQUES = [
    ("verse_hib", "verse_id", 0),
    ("verse_hib", "hib_id", 1),
    ("phenomenon", "passage_id", 0),
    ("phenomenon", "verse_id", 1),
    ("phenomenon", "hib_id", 2),
    ("phenomenon", "ordinal", 3),
]


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone() is not None


def _column_exists(conn: sqlite3.Connection, table: str, col: str) -> bool:
    return any(r[1] == col for r in conn.execute(f"PRAGMA table_info({table})").fetchall())


def _registered(conn: sqlite3.Connection, table: str) -> bool:
    return conn.execute("SELECT 1 FROM cfg_table WHERE name=?", (table,)).fetchone() is not None


def run(conn: sqlite3.Connection) -> None:
    """Resumable by design, not just by accident: table creation (DDL, auto-commits in sqlite3's
    default isolation mode) and cfg_* registration (DML) are tracked and resumed INDEPENDENTLY —
    found necessary the hard way, first run of this exact script: it created all 6 tables + the
    `passage` column, then hit a real `"notnull"`-quoting bug in the cfg_column INSERT and crashed
    before registering anything. A naive 'skip what already exists' re-run would then have seen
    every table already present, added nothing to `created`, and silently skipped cfg_*
    registration forever — an unregistered but real table, worse than not existing at all
    (governance.rules_must_be_config_driven). Registration state is checked against `cfg_table`
    directly, not inferred from whether this run just created the table."""
    created, skipped = [], []
    for name, ddl in DDL.items():
        if _table_exists(conn, name):
            skipped.append(name)
            continue
        conn.execute(ddl)
        created.append(name)

    if not _column_exists(conn, "passage", "phenomena_complete_at"):
        conn.execute("ALTER TABLE passage ADD COLUMN phenomena_complete_at TEXT")
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
        "SELECT 1 FROM cfg_column WHERE table_name='passage' AND name='phenomena_complete_at'"
    ).fetchone() is not None
    if not passage_col_registered:
        conn.execute(
            "INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, \"notnull\", is_unique, "
            "dflt, fk, use, expectation, source, filled_by) VALUES "
            "('passage','phenomena_complete_at',NULL,'TEXT',0,0,0,NULL,NULL,"
            "'NULL until the debate digest Step 3 phase gate is confirmed complete for the whole "
            "passage (every verse_hib pair for this passage has a matching phenomenon row); set "
            "only by an explicit control check, never by trust. operation writes are blocked in "
            "code while this is NULL (schema built, gate-enforcing writer not yet built -- see "
            "b3-b5-operations-schema-design-20260805.md).',NULL,NULL,NULL)")

    conn.commit()
    print(f"tables created this run: {created or '(none)'}")
    print(f"tables already present: {skipped or '(none)'}")
    print(f"cfg_table/cfg_column/cfg_unique registered this run: {to_register or '(none)'}")
    print(f"passage.phenomena_complete_at column added: {passage_col_added}")
    print(f"passage.phenomena_complete_at cfg_column registered this run: "
          f"{not passage_col_registered}")
    print("NOTE: no cfg_write_grant rows registered -- no writer exists yet for these tables "
          "(deliberate, see module docstring).")


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    run(conn)
    conn.close()
