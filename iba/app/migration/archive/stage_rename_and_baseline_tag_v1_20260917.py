"""Resolve 3 of the 6 items previously left open (escalation #1706, 2026-09-17), on the researcher
challenging why they weren't just decided: "what prevents you from completing all the preparatory
work?" On review, these three had enough grounding already on record to resolve directly, not
genuine researcher-only judgment calls:

1. Stage renaming, including `subgroup`. Completes the naming scheme proposed and left half-open
   in `1706-tag-taxonomy-consolidation-v1-20260917.md` SS5.3 -- all 5 stages now describe an
   activity at a grain (verse vs. characteristic), so `subgroup` (family/subgroup FORMATION, a
   char-grain activity like the others) becomes `char-subgroup`, completing the pattern:
   `verse-reading` / `char-subgroup` / `char-reading` / `char-answers` / `char-synergy`. Safe:
   checked live, `ib_observation` is still 0 rows.

2. The `char-answers` baseline tag, unblocked by (1) -- every `ib_observation` row needs a `tag`,
   and `answer`-stage rows had no "nothing flagged" value, only the placeholder `slant`.

3. `needs_adjacent_verse_context` at `verse_meaning` -- cross-cutting checklist rule 5a already
   states the flag "governs every flag-shaped observation this pipeline raises," not a
   process-(d)-only rule. Applying that already-stated principle directly, not deciding anew.

The other 3 of the original 6 (role-driven-walk enforcement rigidity, #729 ownership, #1714
sequencing) are NOT touched here -- the first is a judgement the researcher explicitly reserved
for themselves in #1705's own closing words ("I may revisit this judgement... will hold my
judgement until we had some results out of the new pipeline"), and the other two are genuine
resourcing/sequencing calls, not content decisions this script can resolve.

Safe to re-run: idempotent.

Usage:
    python iba/app/migration/stage_rename_and_baseline_tag_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

STAGE_RENAMES = {
    "verse_meaning": "verse-reading",
    "subgroup": "char-subgroup",
    "reading": "char-reading",
    "answer": "char-answers",
    "synthesis": "char-synergy",
}


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

        # Safety: confirm 0 live rows before renaming stage values.
        n = cur.execute("SELECT COUNT(*) c FROM ib_observation").fetchone()["c"]
        if n:
            raise RuntimeError(f"ib_observation has {n} live rows -- stage rename is not safe, abort")

        for old, new in STAGE_RENAMES.items():
            row = cur.execute(
                "SELECT ordinal FROM cfg_enum WHERE name='ib_observation.stage' AND value=?",
                (old,)).fetchone()
            if row is None:
                report.append(f"stage {old!r}: not found (already renamed?) -- skipped")
                continue
            cur.execute(
                "UPDATE cfg_enum SET value=? WHERE name='ib_observation.stage' AND value=?",
                (new, old))
            report.append(f"stage {old!r} -> {new!r}")

        cur.execute(
            "UPDATE cfg_column SET use=? WHERE table_name='ib_observation' AND name='stage'",
            ("cfg_enum-governed (ib_observation.stage): verse-reading (pre-subgroup Layer 2, "
             "#1711) | char-subgroup (subgroup/family formation, process b) | char-reading "
             "(process c) | char-answers (process d) | char-synergy (process e, cross-cluster). "
             "Renamed 2026-09-17, escalation #1706, completing the naming scheme -- every value "
             "now names an activity at a grain (verse vs. characteristic), subgroup formation "
             "included.",))
        report.append("cfg_column ib_observation.stage.use updated")

        exists = cur.execute(
            "SELECT 1 FROM cfg_enum WHERE name='ib_observation.tag' AND value='answered-no-flag'"
        ).fetchone()
        if not exists:
            max_ord = cur.execute(
                "SELECT COALESCE(MAX(ordinal),-1) m FROM cfg_enum WHERE name='ib_observation.tag'"
            ).fetchone()["m"]
            cur.execute(
                "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
                ("ib_observation.tag", "answered-no-flag", max_ord + 1))
            report.append("cfg_enum ib_observation.tag='answered-no-flag' inserted "
                         "(char-answers baseline -- a question answered with nothing flagged)")
        else:
            report.append("cfg_enum ib_observation.tag='answered-no-flag' already present")

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
