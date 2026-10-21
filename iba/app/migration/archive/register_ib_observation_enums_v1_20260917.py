"""Register `ib_observation.tag`/`status`/`meaning_source` cfg_enum values (escalation #1706,
tag-taxonomy consolidation, 2026-09-17). All three columns were signposted across design docs
(#1691 SS5's M10 prototype data, #1682's process spec) but never actually registered -- checked
live: cfg_enum had zero groups for any of the three, despite `tag`/`status` being NOT NULL.

Researcher decisions this round (iba/docs/1706-tag-taxonomy-consolidation-v1-20260917.md):
SS2.1 `cross-family`/`cross_family_or_cluster_flags` consolidated into one tag, normalized to
`cross-cluster-significance`. SS2.2 `no-human-context` (definitive: no IB significance) and
`could-not-resolve` (provisional: unresolved, but a signal suggests it's resolvable) kept as two
distinct tags. SS2.3 hyphen-case standard. SS3 CORRECTED per researcher instruction: one flat
cfg_enum group per COLUMN, not per stage -- `ib_observation` is one record set, most tags apply
across stages. `meaning_source`'s 3 values resolved same round: the M10 prototype's own literal
usage (`"meaning_source": "strong_meaning_tree"`, #1682 doc) plus the two `strong_lexicon` columns,
kept as literal schema references (not hyphen-cased -- they name real tables/columns).

Also corrects two stale `cfg_column.use` texts that scoped `tag`/`meaning_source` to a single
stage ("reading stage only") -- the same mistake the researcher corrected in SS3, since
`verse_meaning` also reads the same 3 sources and most tags aren't reading-exclusive either.

Deliberately NOT registered here (still open, per the doc's own SS5.3): the `answer`-stage plain
"nothing flagged" baseline tag value, and the `ib_observation.stage` rename proposal -- both
pending the researcher's confirmation on how `subgroup` fits the new verse-reading/char-reading/
char-answers/char-synergy naming scheme.

Safe to re-run: every insert is guarded, no-ops if already present.

Usage:
    python iba/app/migration/register_ib_observation_enums_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

TAG_VALUES = [
    "instance-meaning", "verse-grouping", "difference-inference", "surface-gloss-divergence",
    "no-human-context", "cross-cluster-significance", "data-error", "alternative-meaning",
    "could-not-resolve",
]
STATUS_VALUES = ["resolved", "needs-corroboration", "open", "silent"]
MEANING_SOURCE_VALUES = ["strong_meaning_tree", "strong_lexicon.lsj", "strong_lexicon.mounce"]

TAG_USE_TEXT = (
    "enum, cfg_enum-governed (ib_observation.tag) -- shared across all stages, not partitioned "
    "per stage; most tags apply wherever the relevant condition arises (e.g. data-error, "
    "cross-cluster-significance, could-not-resolve are not reading-exclusive). Corrected "
    "2026-09-17, escalation #1706: previously read 'stage-specific enum', which the researcher "
    "identified as the wrong model -- ib_observation is one unified record set populated across "
    "stages, not fragmented enum groups per stage."
)
MEANING_SOURCE_USE_TEXT = (
    "which of the 3 meaning tables/columns (strong_meaning_tree, strong_lexicon.lsj, "
    "strong_lexicon.mounce) an observation drew its data from -- any meaning-reading stage "
    "(verse_meaning and reading both read all 3 as complementary evidence), not reading-only. "
    "Corrected 2026-09-17, escalation #1706: previously read 'reading stage only', the same "
    "stage-scoping mistake corrected for `tag`."
)


def row_exists(cur, sql, params) -> bool:
    return cur.execute(sql, params).fetchone() is not None


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

        for group, values in (
            ("ib_observation.tag", TAG_VALUES),
            ("ib_observation.status", STATUS_VALUES),
            ("ib_observation.meaning_source", MEANING_SOURCE_VALUES),
        ):
            for ordinal, value in enumerate(values):
                if not row_exists(cur, "SELECT 1 FROM cfg_enum WHERE name=? AND value=?",
                                  (group, value)):
                    cur.execute(
                        "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
                        (group, value, ordinal))
                    report.append(f"cfg_enum {group}={value!r} inserted")
                else:
                    report.append(f"cfg_enum {group}={value!r} already present — skipped")

        for table, col, use_text in (
            ("ib_observation", "tag", TAG_USE_TEXT),
            ("ib_observation", "meaning_source", MEANING_SOURCE_USE_TEXT),
        ):
            cur.execute(
                "UPDATE cfg_column SET use=? WHERE table_name=? AND name=?",
                (use_text, table, col))
            report.append(f"cfg_column {table}.{col}.use corrected ({cur.rowcount} row)")

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
