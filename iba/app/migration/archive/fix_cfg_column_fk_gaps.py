"""fix_cfg_column_fk_gaps.py — ONE-OFF, idempotent: closes the two places `cfg_column` itself was
incomplete, found during the 2026-08-07 schema remediation (`schema-remediation-design-20260807.md`
§2) before the FK/index retrofit can proceed.

1. `strong_meaning_parsed.strong_variant` / `strong_meaning_tree.strong_variant` — an FK-shaped
   column (same convention as `span.strong_variant`, which already has `fk='strong.strongNumber'`)
   that was never declared as one at all, not even in metadata. Fixed: `cfg_column.fk` set.

2. `operation_party` has no way to link a source/target party back to `hib` when the party IS a
   previously-registered HIB — currently only a free-text `detail` column (Finding 2 of
   `debate-schema-traceability-gap-findings-20260807.md`: only 3 of 42 live `detail` values match a
   `hib.label` even as *text*, let alone structurally). Fixed: new nullable `hib_id INTEGER` column,
   `cfg_column.fk='hib.id'`. Nullable because a party can be `self`/`non_human`/`object_situation`/
   `none`, which genuinely has no HIB to link. `detail` is kept as-is (a human-readable gloss
   alongside the real FK, not replaced by it).

   The actual `ALTER TABLE operation_party ADD COLUMN hib_id INTEGER` (config-then-code, same order
   `governance.rules_must_be_config_driven` requires) and the back-fill of the 3 exact-label matches
   both happen in `retrofit_debate_lexicon_tables.py`, not here — this script only touches config.

    python -m iba.app.migration.fix_cfg_column_fk_gaps
"""
from __future__ import annotations

import sqlite3

DB_PATH = "iba/app/db/iba.db"

OPERATION_PARTY_HIB_ID_COLUMN = (
    "operation_party", "hib_id", 7, "INTEGER", 0, 0, 0, None, "hib.id",
    "which registered HIB this source/target party IS, when it is one -- nullable: "
    "self/non_human/object_situation/none parties genuinely have no HIB to link. Added "
    "2026-08-07 (Finding 2, debate-schema-traceability-gap-findings-20260807.md): 'detail' alone "
    "gave no structural traceability back to the hib register.",
    None, None, None,
)


def run(conn: sqlite3.Connection) -> None:
    fixed_strong_variant = []
    for table in ("strong_meaning_parsed", "strong_meaning_tree"):
        row = conn.execute(
            "SELECT fk FROM cfg_column WHERE table_name=? AND name='strong_variant'",
            (table,)).fetchone()
        if row is not None and row["fk"] is None:
            conn.execute(
                "UPDATE cfg_column SET fk='strong.strongNumber' "
                "WHERE table_name=? AND name='strong_variant'", (table,))
            fixed_strong_variant.append(table)

    added_operation_party_hib_id = False
    exists = conn.execute(
        "SELECT 1 FROM cfg_column WHERE table_name='operation_party' AND name='hib_id'"
    ).fetchone() is not None
    if not exists:
        conn.execute(
            'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", is_unique, '
            "dflt, fk, use, expectation, source, filled_by) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            OPERATION_PARTY_HIB_ID_COLUMN)
        added_operation_party_hib_id = True

    conn.commit()
    print(f"strong_variant.fk set this run on: {fixed_strong_variant or '(none, already set)'}")
    print(f"operation_party.hib_id cfg_column row added this run: {added_operation_party_hib_id}")


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    run(conn)
    conn.close()
