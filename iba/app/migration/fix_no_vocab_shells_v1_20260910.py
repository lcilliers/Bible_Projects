"""Create explicit "no known meaning" shell rows for H3673 and H3674 -- escalation #1647
(spine.check's 2 remaining FATAL findings after the #1613 409-item sweep, 2026-09-10).

Both are real words with real surface text (H3673 = Aramaic "gather"/"gathered", Dan.3.2/3.3/3.27;
H3674 = Hebrew "associates", Ezra.4.7) but STEP's own local module returns genuinely empty
`vocabInfos` for both -- confirmed live by querying `rest/module/getInfo/ESV_th//H3673//` and
`//H3674//` directly (a control query on H0430 in the same call returned full data, ruling out a
connection/format problem). `raw.detail_one()` skips creating a `strong` row when that happens, so
these two re-appear FATAL on every `spine.check` run with no way to backfill -- there is no meaning
to pull.

Researcher decision, verbatim, 2026-09-10: "make a single line entry in strong_meaning with the
explanation of the meaning finding for H3673 and H3674 and the [related] parse entry - as no known
meaning."

What this does, per code:
  1. A shell `strong` row (origin='backfill' -- discovered via book-scoped span, not a word search;
     language derived from the H/G prefix; every STEP-sourced field left NULL since STEP supplied
     nothing -- not a hedge, an accurate NULL).
  2. A `strong_sense` row, head="no known meaning" -- not named in the researcher's instruction, but
     added to keep the one check that had been 100% clean all session (every live `strong` row has
     exactly one `strong_sense` row) from gaining a new gap; flagged here, not silently decided.
  3. A `strong_meaning_tree` row, sense_text="no known meaning" (the raw layer, per the instruction).
  4. Does NOT hand-write the matching `strong_meaning_parsed` row -- `lexicon.parse` (already
     approved, writer='lexicon.parse') is run separately, right after this script, so the parsed
     layer is generated through the normal mechanism and survives future clear-and-rebuilds instead
     of drifting out of sync as a one-off fake.

Idempotent: skips a code if its `strong` row already exists live.
"""

from __future__ import annotations

import argparse
import sqlite3
from datetime import datetime, timezone

DEFAULT_DB = "iba/app/db/iba.db"

REASON = "no known meaning"
NOTE = ("STEP's own module returns no vocabulary data for this code (confirmed live 2026-09-10, "
        "escalation #1647) -- not a project-side gap.")

CODES = ["H3673", "H3674"]


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _language_for(code: str) -> str:
    return "Hebrew" if code.startswith("H") else "Greek"


def apply_code(cur: sqlite3.Cursor, code: str, report: list[str]) -> None:
    existing = cur.execute("SELECT 1 FROM strong WHERE strongNumber=? AND deleted=0", (code,)).fetchone()
    if existing:
        report.append(f"{code}: strong row already exists live -- skipped (idempotent)")
        return

    now = _now()
    cur.execute(
        "INSERT INTO strong (strongNumber, accentedUnicode, stepGloss, stepTransliteration, "
        "language, count, freqList, created_at, deleted, origin) "
        "VALUES (?, NULL, NULL, NULL, ?, 0, NULL, ?, 0, 'backfill')",
        (code, _language_for(code), now))
    report.append(f"{code}: strong row created (language={_language_for(code)}, origin=backfill)")

    cur.execute(
        "INSERT INTO strong_sense (strong, head, is_own_lemma, deleted) VALUES (?, ?, NULL, 0)",
        (code, REASON))
    report.append(f"{code}: strong_sense row created (head={REASON!r})")

    cur.execute(
        "INSERT INTO strong_meaning_tree (lemma_key, sense_code, sense_text, sort, deleted, "
        "strong_variant) VALUES (?, NULL, ?, 0, 0, ?)",
        (code, f"{REASON} -- {NOTE}", code))
    report.append(f"{code}: strong_meaning_tree row created (sense_text={REASON!r} + note)")


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
        for code in CODES:
            apply_code(cur, code, report)

        if args.dry_run:
            conn.rollback()
            report.append("DRY-RUN: rolled back")
        else:
            conn.commit()
            report.append("COMMITTED -- run Lexicon-Parse.ps1 -Step Parse next to generate the "
                          "matching strong_meaning_parsed rows through the normal pipeline")

        print("\n".join(report))
        return 0
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
