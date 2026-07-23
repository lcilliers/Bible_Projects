"""add_candidate_seed_referent_columns.py — ONE-OFF: the `candidate.load` schema/config bundle.

Built for the JSON-driven candidate_seed create/update/validate tool (`candidate.load`,
`Candidate-Curate.ps1 -Mode Load`). Three physical changes, one real table rebuild:

  1. `candidate_seed.sense_seq` INTEGER NOT NULL DEFAULT 0 — extends the dedup key from
     (lemma_key, strong_variant) to (lemma_key, strong_variant, sense_seq). Resolves escalation
     #228 (the anger/spirit dual-characteristic overlap): a lemma whose ONE Strong's code
     genuinely carries two IB concepts at once — no distinct sub-strong to split onto — now gets
     a second row via sense_seq=1, exactly the same reasoning as the strong_variant migration one
     level up (see add_candidate_seed_strong_variant.py). SQLite cannot ALTER a UNIQUE constraint
     in place, so this is a table rebuild (create new, copy, drop, rename), same technique.
  2. `candidate_seed.step_status` TEXT (enum candidate_step_status) — in_strong / step_no_verses /
     not_in_step / step_has_verses_pending. Read-only STEP cross-reference state; `candidate.load`
     populates it, never writes to `strong` itself (that stays raw.detail's job, its own grant).
  3. `candidate_seed.ib_referent_type` TEXT (enum candidate_ib_referent) — characteristic /
     other_being / body_part. Informational marker requested alongside #228's resolution: a
     lemma that could be interpreted as another being (third party impacting IB) or a body part
     (idiomatically IB-relevant) gets flagged, not gated.
  4. `candidate_decision` enum gains a 4th value, `exception` — an item that failed load-time
     validation is WRITTEN as a real, inspectable row (decision='exception'), not silently dropped
     or held only in a transient escalation payload.

Also registers (all bootstrap-direct, per the same exception as every prior column addition this
session — DDL and the enum/column/setting/step rows that describe brand-new mechanism are not
`configmaint.propose`-able, since propose only writes rows on already-existing columns/tables):
cfg_column rows for the 3 new columns, cfg_enum groups `candidate_step_status`/
`candidate_ib_referent` + the `exception` value on `candidate_decision`, three new cfg_setting
rows (module `candidate`): `candidate.concept_delimiter_pattern`, `candidate.tag_max_words`,
`candidate.transliteration_pattern`, the `candidate.load` cfg_step row under the existing
`candidate-curation` work package, and a `cfg_write_grant` row so `candidate.load` may write
`candidate_seed` (mirrors `candidate.curate`'s existing grant).

Deliberately NOT seeded here: any actual `other-being`/`body-part` cfg_candidate_rule VALUES (the
`kind` column is free text, no schema change needed to use it) — those are curated content
decisions for the researcher via `configmaint.propose`, not something to invent in a migration.

    python -m iba.app.migration.add_candidate_seed_referent_columns --dry-run
    python -m iba.app.migration.add_candidate_seed_referent_columns
"""

from __future__ import annotations

import argparse
import sqlite3
import sys

from ..lib.cfg import DB_PATH

NEW_ENUMS = {
    "candidate_step_status": ["in_strong", "step_no_verses", "not_in_step", "step_has_verses_pending"],
    "candidate_ib_referent": ["characteristic", "other_being", "body_part"],
}

NEW_SETTINGS = [
    # key, value (JSON-encoded), use, module
    ("candidate.concept_delimiter_pattern", '"[:/]"',
     "a character in a candidate.load input word signalling more than one concept -- split into "
     "one sub-item per piece before validating, rather than reject or guess which half is right",
     "candidate"),
    ("candidate.tag_max_words", "5",
     "a candidate.load input word/tag longer than this many space-separated tokens is treated as "
     "a sentence, not a concept, and written as an exception row",
     "candidate"),
    ("candidate.transliteration_pattern", r'"^(?=.*[a-z])[a-z]{2,10}$"',
     "STARTER heuristic, tune via configmaint.propose as real cases are seen: a bare lowercase "
     "token with no space is a plausible transliteration (e.g. 'asah', 'halak') and gets written "
     "as an exception for a human read, not silently accepted -- it cannot distinguish a genuine "
     "single-word English gloss ('hearing') from a transliteration by shape alone, so this is a "
     "conservative flag-for-review test, not a hard linguistic classifier",
     "candidate"),
]


def _next_ordinal(conn: sqlite3.Connection, table: str, where: str, params: tuple) -> int:
    return conn.execute(f"SELECT COALESCE(MAX(ordinal), -1) + 1 FROM {table} WHERE {where}",
                        params).fetchone()[0]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    cols = {r[1] for r in conn.execute("PRAGMA table_info(candidate_seed)")}
    needs_rebuild = not {"sense_seq", "step_status", "ib_referent_type"}.issubset(cols)

    n = conn.execute("SELECT COUNT(*) FROM candidate_seed").fetchone()[0]
    if needs_rebuild:
        report.append(f"candidate_seed: {n} row(s) — add sense_seq/step_status/ib_referent_type, "
                      f"rebuild UNIQUE(lemma_key, strong_variant, sense_seq)")
    else:
        report.append("candidate_seed already has sense_seq/step_status/ib_referent_type — table rebuild skipped")

    if a.dry_run:
        for line in report:
            print(f"  - {line}")
        print("--dry-run: no changes made.")
        conn.close()
        return 0

    if needs_rebuild:
        conn.execute("""
            CREATE TABLE candidate_seed_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lemma_key TEXT NOT NULL,
                decision TEXT,
                layer TEXT,
                registry_match TEXT,
                tag TEXT,
                strong_variant TEXT NOT NULL,
                sense_seq INTEGER NOT NULL DEFAULT 0,
                step_status TEXT,
                ib_referent_type TEXT,
                assessed_at TEXT,
                deleted INTEGER DEFAULT 0,
                FOREIGN KEY (lemma_key) REFERENCES lemma_inventory(lemma_key),
                UNIQUE (lemma_key, strong_variant, sense_seq)
            )
        """)
        conn.execute("""
            INSERT INTO candidate_seed_new
                (id, lemma_key, decision, layer, registry_match, tag, strong_variant, sense_seq,
                 step_status, ib_referent_type, assessed_at, deleted)
            SELECT id, lemma_key, decision, layer, registry_match, tag, strong_variant, 0,
                   NULL, NULL, assessed_at, deleted
            FROM candidate_seed
        """)
        conn.execute("DROP TABLE candidate_seed")
        conn.execute("ALTER TABLE candidate_seed_new RENAME TO candidate_seed")
        check = conn.execute("SELECT COUNT(*) FROM candidate_seed").fetchone()[0]
        zero_seq = conn.execute("SELECT COUNT(*) FROM candidate_seed WHERE sense_seq=0").fetchone()[0]
        report.append(f"migrated {check} row(s), all sense_seq=0 ({zero_seq}) — should equal {n}")
        if not (check == n == zero_seq):
            print("MIGRATION FAILED row-count check:")
            for line in report:
                print(f"  - {line}")
            conn.rollback()
            conn.close()
            return 1

    # cfg_unique — rebuild the (lemma_key, strong_variant, sense_seq) declaration
    conn.execute("DELETE FROM cfg_unique WHERE table_name='candidate_seed'")
    for i, col in enumerate(("lemma_key", "strong_variant", "sense_seq")):
        conn.execute("INSERT INTO cfg_unique VALUES (?,?,?)", ("candidate_seed", col, i))
    report.append("cfg_unique(candidate_seed) rebuilt as (lemma_key, strong_variant, sense_seq)")

    # cfg_column — 3 new columns
    existing_cols = {r[0] for r in conn.execute(
        "SELECT name FROM cfg_column WHERE table_name='candidate_seed'")}
    new_cols = [
        ("sense_seq", "INTEGER", 0, 1, 1, "0", None,
         "which concept-sense of this (lemma_key, strong_variant) this row is, when one Strong's "
         "code genuinely carries more than one IB concept and there is no distinct sub-strong to "
         "split onto (0 = the only/first sense)", None, None, "candidate.load"),
        ("step_status", "TEXT", 0, 0, 0, None, None,
         "STEP cross-reference state, read-only (never writes to strong) -- in_strong / "
         "step_no_verses / not_in_step / step_has_verses_pending",
         "enum.candidate_step_status", None, "candidate.load"),
        ("ib_referent_type", "TEXT", 0, 0, 0, None, None,
         "informational signal, not a gate -- could this word be another being (third party "
         "impacting IB) or a body part (idiomatically IB-relevant), vs a direct characteristic",
         "enum.candidate_ib_referent", None, "candidate.load"),
    ]
    ordinal = _next_ordinal(conn, "cfg_column", "table_name=?", ("candidate_seed",))
    for name, typ, is_pk, notnull, is_unique, dflt, fk, use, expectation, source, filled_by in new_cols:
        if name in existing_cols:
            continue
        conn.execute(
            "INSERT INTO cfg_column VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            ("candidate_seed", name, ordinal, typ, is_pk, notnull, is_unique, dflt, fk, use,
             expectation, source, filled_by))
        ordinal += 1
        report.append(f"cfg_column row for candidate_seed.{name} added")

    # cfg_enum — two new groups, plus 'exception' on the existing candidate_decision group
    for name, values in NEW_ENUMS.items():
        if conn.execute("SELECT 1 FROM cfg_enum WHERE name=?", (name,)).fetchone():
            report.append(f"cfg_enum group {name!r} already present")
            continue
        for i, v in enumerate(values):
            conn.execute("INSERT INTO cfg_enum VALUES (?,?,?)", (name, v, i))
        report.append(f"cfg_enum group {name!r} ({len(values)} values) added")

    if not conn.execute(
            "SELECT 1 FROM cfg_enum WHERE name='candidate_decision' AND value='exception'").fetchone():
        next_ord = _next_ordinal(conn, "cfg_enum", "name=?", ("candidate_decision",))
        conn.execute("INSERT INTO cfg_enum VALUES (?,?,?)",
                    ("candidate_decision", "exception", next_ord))
        report.append("cfg_enum candidate_decision gained value 'exception'")
    else:
        report.append("cfg_enum candidate_decision already has 'exception'")

    # cfg_setting — 3 new rows
    for key, value, use, module in NEW_SETTINGS:
        if conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
            report.append(f"cfg_setting {key!r} already present")
            continue
        conn.execute("INSERT INTO cfg_setting VALUES (?,?,?,?)", (key, value, use, module))
        report.append(f"cfg_setting {key!r} added")

    # cfg_step — candidate.load under the existing candidate-curation work package
    if not conn.execute(
            "SELECT 1 FROM cfg_step WHERE work_package='candidate-curation' AND step='candidate.load'").fetchone():
        ordinal = _next_ordinal(conn, "cfg_step", "work_package=?", ("candidate-curation",))
        conn.execute("INSERT INTO cfg_step VALUES (?,?,?,?,?,?)", (
            "candidate-curation", ordinal, "candidate.load", "iba.app.handlers.candidate:load",
            "none",
            "JSON-batch create/update/validate for candidate_seed -- derives lemma/strong_variant "
            "from an input English word (no lemma_key in the input), auto-loads items that pass "
            "every config-driven check, writes anything that doesn't as an inspectable "
            "decision='exception' row, then revalidates the whole existing seed the same way; "
            "one escalation total if unresolved exceptions remain"))
        report.append("cfg_step candidate-curation/candidate.load added")
    else:
        report.append("cfg_step candidate-curation/candidate.load already present")

    # cfg_write_grant — candidate.load may write candidate_seed
    if not conn.execute(
            "SELECT 1 FROM cfg_write_grant WHERE writer='candidate.load' AND table_name='candidate_seed'").fetchone():
        conn.execute("INSERT INTO cfg_write_grant VALUES (?,?)", ("candidate.load", "candidate_seed"))
        report.append("cfg_write_grant candidate.load -> candidate_seed added")
    else:
        report.append("cfg_write_grant candidate.load -> candidate_seed already present")

    # cfg_on_fail — candidate.load's one condition: needs-review -> pause-continue (the single
    # escalation, only raised if unresolved exception rows remain after the run)
    if not conn.execute(
            "SELECT 1 FROM cfg_on_fail WHERE step='candidate.load' AND condition='needs-review'").fetchone():
        conn.execute("INSERT INTO cfg_on_fail VALUES (?,?,?,?,?)", (
            "candidate.load", "needs-review", "pause-continue", None,
            "candidate.load has unresolved exception row(s) in candidate_seed needing researcher judgement"))
        report.append("cfg_on_fail candidate.load/needs-review -> pause-continue added")
    else:
        report.append("cfg_on_fail candidate.load/needs-review already present")

    conn.commit()
    conn.close()

    print("add_candidate_seed_referent_columns:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
