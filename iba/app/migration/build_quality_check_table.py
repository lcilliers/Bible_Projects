"""build_quality_check_table.py — ONE-OFF, idempotent: creates `cfg_quality_check`, config-defined
reasonability/existence checks for each debate-pipeline step.

**Trigger.** Researcher, 2026-08-06: *"the controls should include self check quality control...
does this HIB refer to a human being as defined, does it make sense... the quality reasonability
test must be applied. Test for existence and non-existence. The test will differ depending what is
being tested. The control rules must be defined in config."*

**Shape.** One row per named check: which step it applies to, a short key, the check's own
question (the thing a self-check pass must actually ask itself), a `test_kind` (existence |
non_existence | reasonableness — the three kinds the researcher named), and whether it's currently
`required` (blocks a write if unanswered/failed) or advisory. Same reference-table shape as
`cfg_method_rule`/`cfg_enum` — DDL carve-out, same standard.

**Deliberately NOT wired into any writer's enforcement yet.** `hib_set`/`phenomenon_set`/
`operation_set` do not currently require answers to these checks. Two of the checks below
(`hib.set/enum-membership`, already live as of today's `_valid_hib_kinds`) ARE mechanically
enforced — named here for completeness, `enforced_by` filled in. The rest are seeded as concrete,
reviewable DRAFT content — deliberately not force-wired into the writers' payload contracts this
same pass, because unlike `cfg_method_rule` (transcribing already-approved method-doc wording),
the exact CONTENT of a reasonability check ("does this make sense") is itself a methodology
judgement specific to this study's standards, not a mechanical wiring decision — the researcher's
own call, not mine to default past. Building the schema and drafting real content now so it's
ready to review/tune/approve for enforcement, not starting from a blank page.

    python -m iba.app.migration.build_quality_check_table
"""
from __future__ import annotations

import sqlite3

DB_PATH = "iba/app/db/iba.db"

DDL = """
    CREATE TABLE cfg_quality_check (
        id           INTEGER PRIMARY KEY,
        step         TEXT NOT NULL,
        check_key    TEXT NOT NULL,
        question     TEXT NOT NULL,
        test_kind    TEXT NOT NULL,
        required     INTEGER NOT NULL DEFAULT 0,
        enforced_by  TEXT,
        ordinal      INTEGER NOT NULL DEFAULT 0,
        active       INTEGER NOT NULL DEFAULT 1
    )"""

COLUMNS = [
    ("cfg_quality_check", "id", 0, "INTEGER", 1, 1, 0, None, None, "surrogate PK", None, None, None),
    ("cfg_quality_check", "step", 1, "TEXT", 0, 1, 0, None, None,
     "which pipeline step this check applies to", None, None, None),
    ("cfg_quality_check", "check_key", 2, "TEXT", 0, 1, 0, None, None,
     "short slug, unique within a step", None, None, None),
    ("cfg_quality_check", "question", 3, "TEXT", 0, 1, 0, None, None,
     "the actual self-check question a reading pass must ask itself for each candidate item",
     None, None, None),
    ("cfg_quality_check", "test_kind", 4, "TEXT", 0, 1, 0, None, None,
     "'existence' | 'non_existence' | 'reasonableness' (researcher's own three kinds, 2026-08-06)",
     None, None, None),
    ("cfg_quality_check", "required", 5, "INTEGER", 0, 1, 0, "0", None,
     "1 = should eventually block a write until answered; 0 = advisory only. NOT YET ENFORCED for "
     "any row by any writer -- see module docstring", None, None, None),
    ("cfg_quality_check", "enforced_by", 6, "TEXT", 0, 0, 0, None, None,
     "code location that mechanically checks this, if any", None, None, None),
    ("cfg_quality_check", "ordinal", 7, "INTEGER", 0, 1, 0, "0", None, None, None, None, None),
    ("cfg_quality_check", "active", 8, "INTEGER", 0, 1, 0, "1", None,
     "supersede by setting 0 and inserting a new row -- history kept", None, None, None),
]

TABLE = ("cfg_quality_check",
        "Config-defined reasonability/existence self-check questions per debate-pipeline step "
        "(researcher, 2026-08-06). Draft content, not yet wired to any writer's enforcement.",
        "cfg_quality_check")

UNIQUES = [("cfg_quality_check", "step", 0), ("cfg_quality_check", "check_key", 1)]

CHECKS = [
    # (step, check_key, question, test_kind, required, enforced_by, ordinal)
    ("hib.set", "kind-enum-membership",
     "Is hib.kind one of the six live enum.hib_kind values (not free text)?",
     "existence", 1, "cfg_enum 'hib_kind' + operations.py:_valid_hib_kinds", 0),
    ("hib.set", "is-genuinely-human",
     "Does this candidate actually refer to a human being as Step 1 defines it -- not a "
     "non-human being whose state happens to be described in human-like terms, and not a place, "
     "object, or abstraction personified only grammatically?",
     "reasonableness", 0, None, 1),
    ("hib.set", "not-already-excluded",
     "Has this exact referent already been recorded as out-of-scope for this book/passage (e.g. "
     "explicitly set aside per step 2 note d), and is this entry silently reintroducing it without "
     "new textual grounds?",
     "non_existence", 0, None, 2),
    ("hib.set", "verse-actually-supports-it",
     "Does the cited verse's own text (lexical row-level data, not the paraphrased English gloss) "
     "actually support this HIB being present, or is the entry drifting from what the verse itself "
     "states?",
     "reasonableness", 0, None, 3),

    ("phenomenon.set", "genuinely-inner-being",
     "Is this phenomenon actually a state, disposition, or characteristic of the HIB's inner "
     "life -- not a purely outward/administrative fact restated without any interior content "
     "identified?",
     "reasonableness", 0, None, 0),
    ("phenomenon.set", "not-a-literary-pattern",
     "Is this entry a genuine per-verse, per-HIB phenomenon -- not a textual/structural pattern "
     "(recurring formula, book-wide thesis) smuggled in as if it were one (Part B.12)?",
     "non_existence", 0, None, 1),
    ("phenomenon.set", "warrant-is-specific",
     "Does textual_warrant name an actual verb/clause/stated silence in this verse, not a vague "
     "restatement of the description field?",
     "existence", 0, None, 2),

    ("operation.set", "phenomenon-actually-underlies-it",
     "Having written this operation, does a genuine phenomenon actually underlie it -- or has "
     "writing the operation revealed the Step 3 entry was mis-identified and needs correcting "
     "(Part B.12)?",
     "reasonableness", 0, None, 0),
    ("operation.set", "source-target-not-invented",
     "Are the source/target parties actually named or clearly identifiable in the verse/passage, "
     "not invented to complete the operation's shape?",
     "non_existence", 0, None, 1),

    ("passage.build", "boundary-not-arbitrary",
     "Does this passage's boundary fall where the HIB continuity genuinely breaks, or has it been "
     "stretched/shrunk to fit a convenient chapter/verse-count (failure mode b)?",
     "reasonableness", 0, None, 0),
]


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone() is not None


def run(conn: sqlite3.Connection) -> None:
    created = False
    if not _table_exists(conn, "cfg_quality_check"):
        conn.execute(DDL)
        created = True

    registered = conn.execute(
        "SELECT 1 FROM cfg_table WHERE name='cfg_quality_check'").fetchone() is not None
    if not registered:
        conn.execute("INSERT INTO cfg_table (name, grain, use) VALUES (?,?,?)",
                    (TABLE[0], TABLE[2], TABLE[1]))
        conn.executemany(
            'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", is_unique, '
            "dflt, fk, use, expectation, source, filled_by) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            COLUMNS)
        conn.executemany(
            "INSERT INTO cfg_unique (table_name, col, ordinal) VALUES (?,?,?)", UNIQUES)

    existing = {(r["step"], r["check_key"]) for r in conn.execute(
        "SELECT step, check_key FROM cfg_quality_check").fetchall()}
    to_insert = [c for c in CHECKS if (c[0], c[1]) not in existing]
    if to_insert:
        conn.executemany(
            "INSERT INTO cfg_quality_check (step, check_key, question, test_kind, required, "
            "enforced_by, ordinal, active) VALUES (?,?,?,?,?,?,?,1)", to_insert)

    conn.commit()
    print(f"table created this run: {created}")
    print(f"cfg_table/cfg_column/cfg_unique registered this run: {not registered}")
    print(f"check rows inserted this run: {len(to_insert)}")
    print(f"check rows already present: {len(CHECKS) - len(to_insert)}")


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    run(conn)
    conn.close()
