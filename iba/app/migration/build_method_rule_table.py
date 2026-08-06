"""build_method_rule_table.py — ONE-OFF, idempotent: creates `cfg_method_rule`, a generic
reference/citation table so the debate pipeline's analytical rules live in config, not only in
prose instruction documents (`WA-passage-read-guidance-v1.5`, `WA-interpretation-questions-v1.4`,
`debate-analytic-process-digest-20260805.md`).

**Trigger.** Researcher, 2026-08-06: *"I would prefer if the rules are in the config, rather than
hidden in instruction documents. This means that the exact rule can be enacted at the right place,
and the specific rule can be tuned if there are interpretation issues."* Also, directly: *"Step 3:
codify the rules into configs and make them visible in this reference. this cannot be hidden away
in documents."*

**Why a direct migration, not `configmaint.propose`.** `cfg_method_rule` is a new table — DDL.
Same carve-out class as `cfg_enum`/`hib`/`phenomenon` (GOVERNANCE.md §9B/§14). Unlike those, there
is no prior reviewed design doc for THIS specific table — it's being cut in direct, immediate
response to today's explicit instruction, which is itself the up-front direction this carve-out
needs (same standard as B3's own "researcher's own extensive review... and explicit 'proceed'
direction is the up-front design approval").

**Shape, deliberately simple — a citation/reference table, same spirit as `cfg_enum`.** One row
per discrete, nameable rule: which step it governs, a short key, the rule's own exact wording
(transcribed faithfully from its source, not paraphrased), and where it was transcribed FROM (for
provenance — this table is now the rule's canonical *operational* form, but the source doc is not
deleted or contradicted; if the two ever disagree, that disagreement is itself a finding to
resolve, not something to paper over). `active` allows a rule to be tuned/superseded by
`configmaint.propose` (an ordinary data UPDATE from here on — no more DDL needed to adjust a rule's
wording) without losing its history (superseded rows are `inactive=1`, not deleted).

**What this does NOT do.** It does not make every rule mechanically ENFORCED by code — many of
these rules (the Q1-Q12 interrogative, most of Part B's discipline notes) are judgment the
analytical pass applies while reading, not a SQL-checkable condition. What it DOES do: make the
exact wording of every rule this pipeline runs on a live, queryable, tunable database fact, cited
by the technical reference verbatim from here rather than paraphrased from a doc — and, where a
rule IS mechanically checkable (the six-type `hib_kind` enum, the phase-separation control total,
the decision/action-type shape), the code path that enforces it is named in `enforced_by`.

    python -m iba.app.migration.build_method_rule_table
"""

from __future__ import annotations

import sqlite3

DB_PATH = "iba/app/db/iba.db"

DDL = """
    CREATE TABLE cfg_method_rule (
        id           INTEGER PRIMARY KEY,
        step         TEXT NOT NULL,
        rule_key     TEXT NOT NULL,
        rule_text    TEXT NOT NULL,
        source_doc   TEXT,
        enforced_by  TEXT,
        ordinal      INTEGER NOT NULL DEFAULT 0,
        active       INTEGER NOT NULL DEFAULT 1
    )"""

COLUMNS = [
    ("cfg_method_rule", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("cfg_method_rule", "step", 1, "TEXT", 0, 1, 0, None, None,
     "which pipeline step this rule governs, e.g. 'hib.set', 'phenomenon.set'", None, None, None),
    ("cfg_method_rule", "rule_key", 2, "TEXT", 0, 1, 0, None, None,
     "short slug, unique within a step, e.g. 'presumptive-candidate'", None, None, None),
    ("cfg_method_rule", "rule_text", 3, "TEXT", 0, 1, 0, None, None,
     "the rule's own exact wording -- the operational source of truth from here on", None, None, None),
    ("cfg_method_rule", "source_doc", 4, "TEXT", 0, 0, 0, None, None,
     "provenance -- which doc/section this was transcribed from", None, None, None),
    ("cfg_method_rule", "enforced_by", 5, "TEXT", 0, 0, 0, None, None,
     "code location that mechanically checks this rule, if any -- NULL if it's analyst judgement, "
     "not a SQL-checkable condition", None, None, None),
    ("cfg_method_rule", "ordinal", 6, "INTEGER", 0, 1, 0, "0", None,
     "display order within a step", None, None, None),
    ("cfg_method_rule", "active", 7, "INTEGER", 0, 1, 0, "1", None,
     "supersede by setting 0 and inserting a new row, rather than editing/deleting -- history kept",
     None, None, None),
]

TABLE = ("cfg_method_rule",
        "One row per discrete, nameable analytical rule governing a debate-pipeline step -- "
        "config, not only prose docs (researcher, 2026-08-06).",
        "cfg_method_rule")

UNIQUES = [("cfg_method_rule", "step", 0), ("cfg_method_rule", "rule_key", 1)]


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone() is not None


def _registered(conn: sqlite3.Connection, table: str) -> bool:
    return conn.execute("SELECT 1 FROM cfg_table WHERE name=?", (table,)).fetchone() is not None


def run(conn: sqlite3.Connection) -> None:
    created = False
    if not _table_exists(conn, "cfg_method_rule"):
        conn.execute(DDL)
        created = True

    registered = _registered(conn, "cfg_method_rule")
    if not registered:
        conn.execute("INSERT INTO cfg_table (name, grain, use) VALUES (?,?,?)",
                    (TABLE[0], TABLE[2], TABLE[1]))
        conn.executemany(
            'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", is_unique, '
            "dflt, fk, use, expectation, source, filled_by) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            COLUMNS)
        conn.executemany(
            "INSERT INTO cfg_unique (table_name, col, ordinal) VALUES (?,?,?)", UNIQUES)

    conn.commit()
    print(f"table created this run: {created}")
    print(f"cfg_table/cfg_column/cfg_unique registered this run: {not registered}")
    print("NOTE: no cfg_write_grant registered -- rows are seeded by this migration/a follow-up "
          "populate script directly (DML on a brand-new table, same convention as cfg_enum's own "
          "seed rows); ongoing edits go through configmaint.propose like every other cfg_* row.")


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    run(conn)
    conn.close()
