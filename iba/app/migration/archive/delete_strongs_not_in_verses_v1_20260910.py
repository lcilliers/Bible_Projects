"""Soft-delete `strong` rows that never anchor to a real verse occurrence -- researcher
instruction, verbatim, 2026-09-10: "delete strongs not in verses." Part of the #1613 spine audit's
follow-on work (with fix_no_vocab_shells_v1_20260910.py and the raw.backfill_meaning sweep across
the 38 span/strong-desync books).

**Investigated before deleting, not applied blind** (see escalation #1613 and memory
project_base_data_spine_verse_span_strong_parse): 250 live `strong` rows have ZERO live `span`
reference AND zero `strong_verse` row -- confirmed this is NOT explained by
`governance.verse_gap_by_design` (a hidden-verse exception would still show up via `strong_verse`,
STEP's own CALL3 masterSearch result, since that's independent of which verses got onboarded as
`span` rows; none of the 250 have even that). `strong.count` (STEP's own token frequency) is 0 or
~1 for nearly all of them -- consistent with a registered word's STEP search surfacing
semantically-related entries that don't actually occur in the corpus, not data corruption.
248/250 are `origin='word'` (discovered via a registered study word's search), 2 are
`origin='backfill'`.

Per `governance.base_data_spine`: `strong` is the operative anchor precisely because it's the only
table that chains to `span`/`verse`, the actual foundation. A `strong` row with no such chain
anywhere isn't legitimately in scope.

**Cascade** (soft-delete `deleted=1` everywhere a live dependent row exists for one of these 250
codes, so no live child row is left pointing at a deleted parent -- the same kind of orphan this
whole audit thread has been finding elsewhere):
  strong, strong_sense, strong_lexicon, strong_related (both as source `strong` and as
  `related_strong` target -- a related-term row naming one of these codes as the RELATED side is
  left alone, `related_strong` is documented unconstrained, this is not a break), strong_lsj_parsed,
  strong_mounce_parsed, strong_meaning_tree (by `strong_variant`), strong_meaning_parsed (by
  `strong_variant`), cluster_strong, word_strong.

(First draft of this docstring wrongly claimed `word_strong` has no `deleted` column -- checked
again before running: it does. Corrected; `word_strong` is soft-deleted like everything else in
the cascade.)

Idempotent: only touches rows that are currently live (`deleted=0` where applicable).
"""

from __future__ import annotations

import argparse
import sqlite3
from datetime import datetime, timezone

DEFAULT_DB = "iba/app/db/iba.db"


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def find_target_codes(cur: sqlite3.Cursor) -> list[str]:
    span_codes: set[str] = set()
    for (sv,) in cur.execute(
            "SELECT strong_variant FROM span WHERE deleted=0 AND strong_variant IS NOT NULL "
            "AND strong_variant != ''"):
        span_codes.update(sv.split())
    live_strong = {r[0] for r in cur.execute("SELECT strongNumber FROM strong WHERE deleted=0")}
    never_span = live_strong - span_codes
    with_strong_verse = {r[0] for r in cur.execute("SELECT DISTINCT strong FROM strong_verse")}
    return sorted(never_span - with_strong_verse)


def apply(cur: sqlite3.Cursor, codes: list[str], report: list[str]) -> None:
    ph = ",".join("?" * len(codes))
    tables = ["strong", "strong_sense", "strong_lexicon", "strong_lsj_parsed",
              "strong_mounce_parsed"]
    for t in tables:
        col = "strongNumber" if t == "strong" else "strong"
        cur.execute(f"UPDATE {t} SET deleted=1 WHERE {col} IN ({ph}) AND deleted=0", codes)
        report.append(f"{t}: {cur.rowcount} row(s) soft-deleted")

    cur.execute(f"UPDATE strong_related SET deleted=1 WHERE strong IN ({ph}) AND deleted=0", codes)
    report.append(f"strong_related (source side): {cur.rowcount} row(s) soft-deleted")

    cur.execute(f"UPDATE strong_meaning_tree SET deleted=1 WHERE strong_variant IN ({ph}) "
                f"AND deleted=0", codes)
    report.append(f"strong_meaning_tree: {cur.rowcount} row(s) soft-deleted")

    cur.execute(f"UPDATE strong_meaning_parsed SET deleted=1 WHERE strong_variant IN ({ph}) "
                f"AND deleted=0", codes)
    report.append(f"strong_meaning_parsed: {cur.rowcount} row(s) soft-deleted")

    cur.execute(f"UPDATE cluster_strong SET deleted=1 WHERE strong IN ({ph}) AND deleted=0", codes)
    report.append(f"cluster_strong: {cur.rowcount} row(s) soft-deleted")

    cur.execute(f"UPDATE word_strong SET deleted=1 WHERE strong IN ({ph}) AND deleted=0", codes)
    report.append(f"word_strong: {cur.rowcount} row(s) soft-deleted")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")
        codes = find_target_codes(cur)
        report.append(f"{len(codes)} target code(s): {codes[:10]}{'...' if len(codes) > 10 else ''}")
        if not codes:
            report.append("nothing to do")
        else:
            apply(cur, codes, report)

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
