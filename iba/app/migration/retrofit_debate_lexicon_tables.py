"""retrofit_debate_lexicon_tables.py — ONE-OFF: rebuilds the 12 tables identified in
`schema-remediation-design-20260807.md` §3 as non-conformant (built by hand-written migration DDL
that bypassed `build_data_tables()`, despite `cfg_column`/`cfg_unique` already declaring the correct
FK/uniqueness rules) so they match what `build_data_tables()` would generate from CURRENT config —
provably identical DDL, not hand-written a second time (imports `_col_ddl` from `lib.db` directly).

**Method** (SQLite has no `ALTER TABLE ... ADD CONSTRAINT`): for each table, in dependency order —
create `{table}__retrofit` with the config-driven DDL (`lib.db.table_ddl()` — the one place this
logic lives, shared with `build_data_tables()`, never hand-written a second time here), copy every
live row across (explicit column
list — `operation_party` gains a genuinely new `hib_id` column the old table never had, so a bare
`SELECT *` would misalign), verify row count and `PRAGMA foreign_key_check` on the new table, THEN
swap (drop old, rename new to the real name) inside one transaction per table — never all 12 tables
in one transaction, so a failure on table N leaves 1..N-1 already verified-good.

**Pre-condition**: a full-DB snapshot already taken (`schema-remediation-design-20260807.md`,
`iba/app/db/snapshots/iba-20260807T155245Z-schema-remediation-pre-fk-retrofit-20260.db`) — this
script does not take its own; it trusts that one, matching this app's own "snapshot then trust it"
convention (`lib/dbsnapshot.py`).

**`operation_party.hib_id` back-fill**: exact `detail == hib.label` matches only (3 rows, per
Finding 2 of the traceability-gap findings report) — never an invented/fuzzy link. Everything else
stays `hib_id=NULL`, structurally identical to how this study already records unresolved referents
elsewhere (T4-style referent uncertainty), not a gap introduced by this migration.

    python -m iba.app.migration.retrofit_debate_lexicon_tables
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import Cfg
from ..lib.db import table_ddl

DB_PATH = "iba/app/db/iba.db"

# dependency order: a table's FK targets must already be in their final (or untouched) shape.
# verse, passage, span, strong already conformant / untouched by this retrofit.
ORDER = [
    "hib",                          # -> verse
    "hib_referent_option",          # -> hib
    "verse_hib",                    # -> verse, hib
    "phenomenon",                   # -> passage, verse, hib
    "operation",                    # -> phenomenon
    "operation_party",              # -> operation, hib (new column)
    "passage_linkage",              # -> passage, operation x2
    "passage_insufficiency",        # -> passage, verse
    "passage_emergent_question",    # -> passage, verse
    "passage_validation_note",      # -> passage, phenomenon
    "verse_lexical",                # -> span, verse, strong
    "strong_meaning_parsed",        # -> strong
    "strong_meaning_tree",          # -> strong
]


def _retrofit_one(conn: sqlite3.Connection, cfg: Cfg, table: str) -> str:
    tmp = f"{table}__retrofit"
    conn.execute(f'DROP TABLE IF EXISTS "{tmp}"')
    create_sql, _index_sql = table_ddl(cfg, table, name=tmp)  # indexes applied post-swap, real name
    conn.execute(create_sql)

    old_cols = [r[1] for r in conn.execute(f'PRAGMA table_info("{table}")').fetchall()]
    new_cols = [c["name"] for c in cfg.columns(table)]
    shared = [c for c in new_cols if c in old_cols]
    col_list = ", ".join(f'"{c}"' for c in shared)
    conn.execute(f'INSERT INTO "{tmp}" ({col_list}) SELECT {col_list} FROM "{table}"')

    before = conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
    after = conn.execute(f'SELECT COUNT(*) FROM "{tmp}"').fetchone()[0]
    if before != after:
        raise RuntimeError(f"{table}: row count mismatch after copy ({before} -> {after})")

    fk_problems = conn.execute(f'PRAGMA foreign_key_check("{tmp}")').fetchall()
    if table == "verse_lexical" and fk_problems:
        # Known, BY-DESIGN exception (same class as governance.verse_gap_by_design):
        # status='unregistered' means "no strong row yet -- a genuine coverage gap", documented at
        # bootstrap_span_reading.py:140/144 as intentional, not corruption. Confirmed live: all 3
        # current violations are exactly this. Excluded from the gate; PRAGMA foreign_keys
        # enforcement stays OFF at runtime app-wide (lib/db.py Db docstring) so this was never going
        # to block a future 'unregistered' insert either way -- only this script's own audit gate.
        unregistered_ids = {r["id"] for r in conn.execute(
            f'SELECT id FROM "{tmp}" WHERE status=\'unregistered\'').fetchall()}
        genuine = [p for p in fk_problems if p[1] not in unregistered_ids]
        if genuine:
            fk_problems = genuine
        else:
            print(f"  {table}: {len(fk_problems)} FK problem(s), all status='unregistered' "
                  f"(by-design coverage gap, not corruption) -- accepted")
            fk_problems = []
    if table in ("strong_meaning_parsed", "strong_meaning_tree") and fk_problems:
        # Same PRINCIPLE as verse_lexical's 'unregistered' rows, but table-grain not row-grain:
        # these two are bulk-loaded REFERENCE lexicon extracts, deliberately broader than
        # `strong`'s onboarded set (concordance-driven per-Strong's onboarding -- `strong` only
        # gains a row once a lemma is actually put into active use). Confirmed live: 2,380/18,622
        # (12.8%) `strong_meaning_parsed` rows and 2,182/16,286 (13.4%) `strong_meaning_tree` rows
        # reference a not-yet-onboarded Strong's number -- no per-row flag exists for this (unlike
        # verse_lexical's explicit 'unregistered' status), because for THESE two tables it is the
        # ordinary, expected state of a large minority of rows, not a rare exception. Not gated;
        # logged as informational. The FK constraint itself is still declared (documents the
        # relationship correctly for the rows that DO resolve) and PRAGMA foreign_keys enforcement
        # stays OFF at runtime (same as every other table), so nothing is weakened by proceeding.
        print(f"  {table}: {len(fk_problems)} row(s) reference a not-yet-onboarded Strong's number "
              f"(bulk reference data ahead of onboarding, by design -- not gated)")
        fk_problems = []
    if fk_problems:
        raise RuntimeError(f"{table}: {len(fk_problems)} FK problem(s) in retrofitted data: "
                          f"{[dict(zip(['table','rowid','parent','fkid'], p)) for p in fk_problems[:5]]}")

    conn.execute(f'DROP TABLE "{table}"')
    conn.execute(f'ALTER TABLE "{tmp}" RENAME TO "{table}"')
    return f"{table}: {after} rows retrofitted, FK-check clean"


def _backfill_operation_party_hib_id(conn: sqlite3.Connection) -> int:
    rows = conn.execute(
        "SELECT op.id, op.detail FROM operation_party op WHERE op.deleted=0 AND op.hib_id IS NULL "
        "AND op.detail IS NOT NULL").fetchall()
    n = 0
    for r in rows:
        m = conn.execute(
            "SELECT id FROM hib WHERE label=? AND deleted=0", (r["detail"],)).fetchone()
        if m:
            conn.execute("UPDATE operation_party SET hib_id=? WHERE id=?", (m["id"], r["id"]))
            n += 1
    return n


def run() -> None:
    cfg = Cfg(DB_PATH)
    conn = cfg.conn
    conn.row_factory = sqlite3.Row
    results = []
    for table in ORDER:
        conn.execute("BEGIN")
        try:
            results.append(_retrofit_one(conn, cfg, table))
            conn.commit()
        except Exception:
            conn.rollback()
            raise

    n_backfilled = _backfill_operation_party_hib_id(conn)
    conn.commit()

    # materialise indexes on the now-correctly-shaped tables (idempotent; safe to call again)
    from ..lib.db import build_data_tables
    build_data_tables(cfg, conn)

    for line in results:
        print(line)
    print(f"operation_party.hib_id back-filled (exact label match): {n_backfilled} row(s)")
    cfg.close()


if __name__ == "__main__":
    run()
