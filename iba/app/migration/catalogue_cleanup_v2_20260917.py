"""Second cleanup pass on `wa_obs_question_catalogue`, same day as the dimension realignment
(escalation #1712, 2026-09-17). Researcher, verbatim, this chat turn: "It looks like the
pattern_type column in catalogue can be dropped." and "I notice some of the question_text refers
to 'T' codes - is that correct, will LLM know where to find it."

1. `pattern_type` dropped. Checked live: no code references it anywhere (`grep`'d
   `iba/app/handlers`, `iba/app/lib` -- nothing); it was #1704's own "event-cross-reference"
   placeholder, 100% NULL except T2.11's now-superseded value, and `dimension`/`data_mechanism`
   (this session's own new columns) do its job properly.

2. Real bug found checking the researcher's second point: 4 of the 88 remapped questions carry a
   STALE internal cross-reference in their own TEXT -- pointing at the OLD pre-renumbering code
   (e.g. "T0.1.2a", "(T1.5)") that the dimension-realignment migration correctly updated on the
   `question_code` column but never updated inside the question's own prose. Fixed here: each
   cross-reference rewritten to the new code.

3. A second, different issue in the same search: `D7.7.1` (one of THIS session's own new
   questions) names the role-classification scheme directly in its own text ("(role-T3)") --
   correct and traceable, but not self-contained: an LLM answering this question in isolation has
   no guarantee it knows what "role-T3" means or where that tag lives. Rewritten to describe the
   concept in plain language first, with the code kept only as a parenthetical traceability
   anchor, not the load-bearing term.

Safe to re-run: every update is idempotent (checks current text/column state first).

Usage:
    python iba/app/migration/catalogue_cleanup_v2_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

TEXT_FIXES: list[tuple[str, str, str]] = [
    # (question_code, old_text, new_text) -- exact substring replace, checked unique before applying
    ("D5.1.2",
     "What does the pattern of presence/absence found in T0.1.2a indicate",
     "What does the pattern of presence/absence found in D5.1.1 indicate"),
    ("D5.3.1",
     "From the characteristic's God-relation (T0.1) and its role (T0.2), what aspect",
     "From the characteristic's God-relation (D5.1/D7.6) and its role (D10.1/D11.1), what aspect"),
    ("D10.3.2",
     "How does the sustained effect differ from the immediate response (T1.5)?",
     "How does the sustained effect differ from the immediate response (D10.2)?"),
    ("D6.2.1",
     "Where a body link exists (from the T2.1.1 audit), in which direction does it run",
     "Where a body link exists (from the D6.1.1 audit), in which direction does it run"),
    ("D7.7.1",
     "Where an action/operation word (role-T3) appears in this verse alongside the characteristic, "
     "what is that operation's relation to the parties present",
     "Where this verse contains an action or movement word tagged as an Operation in the "
     "cluster's role classification (the tag is `role-T3` in `cluster.cluster_code` -- consult "
     "that tagging directly, not this question's own memory of it), what is that word's relation "
     "to the parties present"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")

        for code, old, new in TEXT_FIXES:
            row = cur.execute(
                "SELECT question_text FROM wa_obs_question_catalogue WHERE question_code=? AND deleted=0",
                (code,)).fetchone()
            if row is None:
                raise RuntimeError(f"{code}: no live row found")
            if new in row["question_text"]:
                report.append(f"{code}: already fixed -- skipped")
                continue
            if old not in row["question_text"]:
                raise RuntimeError(f"{code}: expected old text not found -- text has changed "
                                   f"since this script was written, check manually")
            fixed = row["question_text"].replace(old, new)
            cur.execute(
                "UPDATE wa_obs_question_catalogue SET question_text=? WHERE question_code=? AND deleted=0",
                (fixed, code))
            report.append(f"{code}: stale/opaque reference fixed")

        cols = {r[1] for r in cur.execute("PRAGMA table_info(wa_obs_question_catalogue)")}
        if "pattern_type" in cols:
            cur.execute("ALTER TABLE wa_obs_question_catalogue DROP COLUMN pattern_type")
            report.append("column 'pattern_type' dropped")
        else:
            report.append("column 'pattern_type' already absent")

        remaining = cur.execute(
            "SELECT question_code, question_text FROM wa_obs_question_catalogue WHERE deleted=0"
        ).fetchall()
        import re
        pat = re.compile(r'\bT\d+\b')
        # D7.7.1 deliberately keeps `role-T3` as an explained, defined traceability anchor
        # ("the tag is role-T3 in cluster.cluster_code -- consult that tagging directly") --
        # not an unexplained bare code, so it's excluded from the opaque-reference check.
        leftover = [r["question_code"] for r in remaining
                   if pat.search(r["question_text"] or "") and r["question_code"] != "D7.7.1"]
        report.append(f"remaining bare/opaque T-code references in question_text: {leftover or 'none'}")
        if leftover:
            raise RuntimeError(f"still-opaque T-code references remain: {leftover}")

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
    sys.exit(main())
