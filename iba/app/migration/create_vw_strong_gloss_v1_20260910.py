"""Create `vw_strong_gloss` -- a uniform view of `gloss` across all three parse tables
(`strong_meaning_parsed`, `strong_lsj_parsed`, `strong_mounce_parsed`), researcher instruction,
verbatim, 2026-09-10: "join verse, with span get all the strongs per verse from span, join with a
parse construct (that consist of all three parse tables) and return the gloss column in the
construct. I would recommend we prepare a fixed view in IBA that provides a uniform view of gloss
from all three parse tables."

Why: the three parse tables don't share a column shape -- `strong_meaning_parsed`/`strong_lsj_
parsed` both call it `gloss`; `strong_mounce_parsed` calls it `mounce_parsed`. This view aliases
all three onto one `gloss` column, keyed by `strong` (the full code, `strong_meaning_parsed` via
its own `strong_variant` column -- NOT `lemma_key`, so a query joining on an exact span code gets
that code's own senses, not the whole base lemma's), tagged with which table it came from
(`source` -- the literal source table name, `strong_meaning_parsed`/`strong_lsj_parsed`/
`strong_mounce_parsed`, not a short alias, so a reader can trace a row straight back to its table
without a lookup; researcher instruction, verbatim, 2026-09-10: "adjust the view to show the label
for the source table is a column") and each table's own sense-position column (`sense_label` --
`sense_code` for meaning, `sense_label` for lsj, NULL for mounce, which has no per-sense label of
its own).

Deliberately NOT a resolution/selection mechanism: every live sense row from every table is
present, no stem/voice narrowing, no ambiguity handling, no base-lemma fallback. That selection
logic lives in `lib/lexical.py:resolve_code()` and is explicitly out of scope here -- researcher
instruction, verbatim: "without going through any of the faulty code, configs and pointers." This
view is the raw join surface underneath any future resolution layer, not a replacement for one.

**Fixed 2026-09-10 (escalation #1668-cont.), `ord` for the LSJ/Mounce branches:** was `id AS ord`
-- the row's own raw, globally-unique auto-increment primary key (e.g. 4184987), not a rank within
that strong's own senses at all. Confirmed a real defect, not a display quirk: querying
`WHERE strong='G1375'` returned `ord` values like `4184987`/`658136` sitting alongside
`strong_meaning_parsed`'s genuinely 0-indexed `sort` values, reading as nonsense next to each
other. Still no selection/resolution logic added (the view's own stated boundary) -- `ord` is now
`ROW_NUMBER() OVER (PARTITION BY strong ORDER BY id) - 1`, a pure display-ordering convenience
(0-indexed, matching `strong_meaning_parsed.sort`'s own convention), not a filter: every row from
every source is still present, none dropped, none re-selected.
"""

from __future__ import annotations

import argparse
import sqlite3

DEFAULT_DB = "iba/app/db/iba.db"
VIEW_NAME = "vw_strong_gloss"

VIEW_SQL = f"""
CREATE VIEW {VIEW_NAME} AS
SELECT strong_variant AS strong, 'strong_meaning_parsed' AS source, sense_code AS sense_label,
       gloss, row_type, sort AS ord, id AS parse_id
FROM strong_meaning_parsed WHERE deleted=0
UNION ALL
SELECT strong AS strong, 'strong_lsj_parsed' AS source, sense_label, gloss,
       row_type, ROW_NUMBER() OVER (PARTITION BY strong ORDER BY id) - 1 AS ord, id AS parse_id
FROM strong_lsj_parsed WHERE deleted=0
UNION ALL
SELECT strong AS strong, 'strong_mounce_parsed' AS source, NULL AS sense_label,
       mounce_parsed AS gloss, row_type,
       ROW_NUMBER() OVER (PARTITION BY strong ORDER BY id) - 1 AS ord, id AS parse_id
FROM strong_mounce_parsed WHERE deleted=0
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--replace", action="store_true", help="DROP VIEW IF EXISTS first")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")
        if args.replace:
            cur.execute(f"DROP VIEW IF EXISTS {VIEW_NAME}")
            report.append(f"dropped existing {VIEW_NAME} (--replace)")

        cur.execute(VIEW_SQL)
        report.append(f"{VIEW_NAME} created")

        # sanity: query it, and confirm it resolves at least one known-good code
        cur.execute(f"SELECT COUNT(*) FROM {VIEW_NAME}")
        n = cur.fetchone()[0]
        report.append(f"{VIEW_NAME} row count: {n}")
        cur.execute(f"SELECT DISTINCT source FROM {VIEW_NAME} ORDER BY source")
        sources = [r[0] for r in cur.fetchall()]
        report.append(f"distinct source values: {sources}")

        if args.dry_run:
            conn.rollback()
            report.append("DRY-RUN: rolled back")
        else:
            conn.commit()
            report.append("COMMITTED")

        print("\n".join(report))
        return 0
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
