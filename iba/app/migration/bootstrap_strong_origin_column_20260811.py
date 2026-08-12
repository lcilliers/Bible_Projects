"""bootstrap_strong_origin_column_20260811.py — ONE-OFF: add `strong.origin` ('word' | 'backfill'),
distinguishing the two ways a `strong` row comes to exist — same class of exception as
bootstrap_inactive_column.py (adding a COLUMN to an existing physical table is DDL, which
configmaint.propose cannot do — it only writes/updates/deletes ROWS on already-existing columns).

WHY. Researcher direction, 2026-08-11 (same session as the cluster-adoption work): there are two
kinds of `strong` row, and they must not be conflated.
  'word'      — deliberately onboarded for a registry word (`raw.discover` -> `word_strong` ->
                `raw.detail`/`detail_one`). These must carry the FULL chain: meaning tables,
                `strong_verse`, `span`, etc. — the raw-data-integrity plan's rows 1-7 apply to
                these, and only these.
  'backfill'  — onboarded by `raw.backfill_meaning`'s book-scoped completeness sweep
                (`handlers/raw.py:backfill_meaning_for()`), which pulls meaning for every code
                appearing anywhere in a book's `span.strong_variant` data, independent of any
                word. Confirmed this session: 11,835 of 11,837 `strong` rows with no
                `word_strong` link (99.98%) are exactly explained by this mechanism. These
                should NOT be taken into account for cluster/meaning-relevance mapping — "they
                are effectively only used in the lexicals" (researcher's own words) — they exist
                so verse-level lexical resolution has SOMETHING for every code in the text, not
                because they are themselves inner-being study subjects.

One-time backfill rule for the 15,293 pre-existing rows: 'word' if the code has EVER had a
`word_strong` row (active OR soft-deleted — checked this session: 0 of the current no-link rows
have a soft-deleted word_strong row either, so "ever" and "currently active" agree completely on
live data), else 'backfill'.

Going forward, this is NOT re-derived by a live join each time — it is stamped once, at row
creation, in `handlers/raw.py:detail_one()` (now takes an `origin` parameter; `detail()` passes
'word', `backfill_meaning_for()` passes 'backfill'). 'word' is STICKY: if a code that started as
'backfill' is later legitimately claimed by a word (raw.discover finds it as a real seed),
`detail_one()`'s existing "already exists, skip" path now upgrades 'backfill' -> 'word' instead of
silently doing nothing — never the reverse (a real word-origin code doesn't lose that status just
because a later book-backfill sweep also happens to touch it).

    python -m iba.app.migration.bootstrap_strong_origin_column_20260811 --dry-run
    python -m iba.app.migration.bootstrap_strong_origin_column_20260811
"""
from __future__ import annotations

import argparse
import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    cols = {r[1] for r in conn.execute('PRAGMA table_info("strong")')}
    has_column = "origin" in cols

    if a.dry_run:
        n_word = conn.execute(
            "SELECT COUNT(*) FROM strong s WHERE s.deleted=0 AND EXISTS "
            "(SELECT 1 FROM word_strong ws WHERE ws.strong=s.strongNumber)").fetchone()[0]
        n_backfill = conn.execute(
            "SELECT COUNT(*) FROM strong s WHERE s.deleted=0 AND NOT EXISTS "
            "(SELECT 1 FROM word_strong ws WHERE ws.strong=s.strongNumber)").fetchone()[0]
        print("--dry-run (no write):")
        print(f"  - strong.origin column {'already present' if has_column else 'would be added (ALTER TABLE)'}")
        print(f"  - would classify {n_word} row(s) as 'word', {n_backfill} row(s) as 'backfill'")
        conn.close()
        return 0

    if not has_column:
        conn.execute("ALTER TABLE strong ADD COLUMN origin TEXT NOT NULL DEFAULT 'word'")
        report.append("strong.origin column added (physical ALTER, default 'word')")
    else:
        report.append("strong.origin already present")

    if not conn.execute(
            "SELECT 1 FROM cfg_column WHERE table_name='strong' AND name='origin'").fetchone():
        ordinal = conn.execute(
            "SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_column WHERE table_name='strong'"
        ).fetchone()[0]
        conn.execute(
            "INSERT INTO cfg_column VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            ("strong", "origin", ordinal, "TEXT", 0, 1, 0, "'word'", None,
             "'word' = deliberately onboarded for a registry word (raw.discover -> word_strong -> "
             "raw.detail); must carry the full raw-data-integrity chain. 'backfill' = onboarded by "
             "raw.backfill_meaning's book-scoped completeness sweep, independent of any word; not "
             "in scope for cluster/meaning-relevance mapping, used only to support lexical "
             "resolution. Sticky: an upgrade backfill->word can happen (a later word legitimately "
             "claims the code); never downgraded.",
             None, "migrated:one-time classification, then stamped by detail_one() going forward",
             "raw.detail_one"))
        report.append("cfg_column row for strong.origin added")
    else:
        report.append("cfg_column row for strong.origin already present")

    conn.execute(
        "UPDATE strong SET origin='word' WHERE deleted=0 AND EXISTS "
        "(SELECT 1 FROM word_strong ws WHERE ws.strong=strong.strongNumber)")
    n_word = conn.execute("SELECT changes()").fetchone()[0]
    conn.execute(
        "UPDATE strong SET origin='backfill' WHERE deleted=0 AND NOT EXISTS "
        "(SELECT 1 FROM word_strong ws WHERE ws.strong=strong.strongNumber)")
    n_backfill = conn.execute("SELECT changes()").fetchone()[0]
    report.append(f"classified {n_word} row(s) 'word', {n_backfill} row(s) 'backfill'")

    conn.commit()
    conn.close()

    print("strong.origin bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
