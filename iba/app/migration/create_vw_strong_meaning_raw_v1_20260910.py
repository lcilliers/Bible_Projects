"""Create `vw_strong_meaning_raw` -- a uniform view of the RAW, UNPARSED meaning source text
across all three source tables (`strong_meaning_tree`, `strong_lexicon.lsj`,
`strong_lexicon.mounce`), keyed by strong. Sibling to `vw_strong_gloss` (which unions the three
PARSED tables) -- same shape, same purpose, but sitting one layer further upstream: the raw
material the parse is supposed to represent, not the parse's own output.

Why, escalation #1668-cont., 2026-09-10, researcher instruction verbatim: "this is fundamentally
flawed. prepare a view that pulls the raw meaning tables into one listing for a strong -- similar
to what you have done for the parse." Prompted by comparing G3551's `vw_strong_gloss` rows (7
disconnected `strong_meaning_parsed` fragments, one of them the bare word "the") against its own
`strong_meaning_tree` source (ONE coherent paragraph) side by side -- "how on earth is the parse a
representation of the source?" This view makes that side-by-side comparison a single query instead
of two, for any strong, without going through the parse layer at all.

Columns:
  strong      the full Strong's code (`strong_meaning_tree.strong_variant` -- the exact code a row
              actually came from, not `lemma_key`; `strong_lexicon.strong`, already the full code)
  source      the literal source table.column name, not a short alias -- same convention as
              `vw_strong_gloss.source`
  sense_code  `strong_meaning_tree.sense_code` (its own outline marker, e.g. '1)', '2a)', often
              empty) -- NULL for the lsj/mounce rows, which carry no per-row outline marker of
              their own (the outline lives INSIDE their raw HTML, not as a separate column)
  raw_text    the actual unparsed text/HTML -- `sense_text` for the tree source, `lsj`/`mounce`
              for the lexicon source, verbatim, no tag-stripping, no segment-splitting
  ord         `strong_meaning_tree.sort` for that source (its own real per-strong sequence,
              multiple rows per strong); `0` for lsj/mounce, which are one row per strong in their
              own source table -- there is no internal ranking to expose at this raw grain, the
              whole entry (numbering included) is inside the one `raw_text` blob
  row_id      the source row's own id/rowid, for tracing back to the exact row

Deliberately NOT a parse: no HTML stripped, no <b>-span segmentation, no sense boundaries decided,
nothing merged or dropped. Read `raw_text` as-is. Same non-negotiable boundary `vw_strong_gloss`
itself was built under -- this view is upstream of resolution, not a second attempt at it.

    python -m iba.app.migration.create_vw_strong_meaning_raw_v1_20260910 [--replace]
"""

from __future__ import annotations

import argparse
import sqlite3

DEFAULT_DB = "iba/app/db/iba.db"
VIEW_NAME = "vw_strong_meaning_raw"

VIEW_SQL = f"""
CREATE VIEW {VIEW_NAME} AS
SELECT strong_variant AS strong, 'strong_meaning_tree' AS source, sense_code,
       sense_text AS raw_text, sort AS ord, id AS row_id
FROM strong_meaning_tree WHERE deleted=0
UNION ALL
SELECT strong AS strong, 'strong_lexicon.lsj' AS source, NULL AS sense_code,
       lsj AS raw_text, 0 AS ord, rowid AS row_id
FROM strong_lexicon WHERE deleted=0 AND lsj IS NOT NULL AND lsj != ''
UNION ALL
SELECT strong AS strong, 'strong_lexicon.mounce' AS source, NULL AS sense_code,
       mounce AS raw_text, 0 AS ord, rowid AS row_id
FROM strong_lexicon WHERE deleted=0 AND mounce IS NOT NULL AND mounce != ''
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

        cur.execute(f"SELECT COUNT(*) FROM {VIEW_NAME}")
        n = cur.fetchone()[0]
        report.append(f"{VIEW_NAME} row count: {n}")
        cur.execute(f"SELECT DISTINCT source FROM {VIEW_NAME} ORDER BY source")
        sources = [r[0] for r in cur.fetchall()]
        report.append(f"distinct source values: {sources}")

        # sanity: G3551 (the researcher's own live example) should show exactly 3 rows, one per
        # source, with its strong_meaning_tree row's raw_text intact as ONE paragraph.
        cur.execute(f"SELECT source, length(raw_text) FROM {VIEW_NAME} WHERE strong='G3551'")
        g3551 = cur.fetchall()
        report.append(f"G3551 sanity check: {g3551}")

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
