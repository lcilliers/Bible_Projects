"""fix_ib_node_verse_reference_doc_v1_20260922.py -- ONE-OFF, idempotent. Escalation #1824,
researcher instruction 2026-09-22: pushed on a claim that ib_node.verse_reference "is the same
format as verse" and found it imprecise -- investigating found the REAL bug is in the existing
documentation, not the data.

`cfg_column.use` for `ib_node.verse_reference` reads: "resolved FRESH against iba.db.verse.reference
at load time" -- but the actual write path (recordingpass.py:resolve_occurrence) returns
`r["osisId"]`, never `r["reference"]`. Confirmed live: `ib_node.verse_reference` values are the
dotted osisId format ("Matt.12.36"), not verse.reference's space-separated STEP-abbreviated format
("Mat 12:36") -- 0 of 10,115 non-null values fail to join against verse.osisId. The documented
`use` text has been factually wrong since #1693, and is very likely exactly what caused the
researcher's own hand-written query bug this same session (`WHERE v.reference = 'Mark.6.25'`
against a column that actually holds 'Mar 6:25', not the osisId-style value the query expected).

No live application code was found relying on the WRONG (documented) behaviour -- the two grep
hits for `v.reference` (strongversereport.py, wordregistryspanreport.py) both SELECT it for
display only, never compare/join against ib_node.verse_reference. This is a documentation-only fix.

**Second occurrence found the same pass**: `cluster_subgroup.anchor_verse_reference`'s own `use`
text explicitly says "same convention as ib_node.verse_reference" -- inheriting the identical wrong
claim. Confirmed live: 0 of 13 non-null values fail to join against `verse.osisId` either (same
dotted format, e.g. "Matt.20.6"). Fixed here too, same correction.

    python -m iba.app.migration.fix_ib_node_verse_reference_doc_v1_20260922
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

CORRECT_USE = (
    "resolved FRESH against iba.db.verse.osisId at load time (recordingpass.py:resolve_occurrence "
    "returns v.osisId, never v.reference), never trusted from the LLM's JSON directly (#1693's own "
    "fix). CORRECTED 2026-09-22 (escalation #1824) -- this text previously said 'verse.reference', "
    "which was factually wrong (verse.reference is a different, space-separated STEP-abbreviated "
    "format, e.g. 'Mar 6:25', vs. osisId's dotted 'Mark.6.25'; confirmed live: 0 of 10,115 non-null "
    "ib_node.verse_reference values fail to join against verse.osisId) and is the likely cause of a "
    "real hand-written query bug this same session that joined against verse.reference expecting "
    "the dotted format."
)

CORRECT_USE_SUBGROUP = (
    "ADDED 2026-09-16 (#1526). One representative verse per subgroup, selected by process (b)'s "
    "own LLM session as the verse that best describes the subgroup's shared characteristic "
    "(researcher, verbatim). Resolved fresh against iba.db.verse.osisId (CORRECTED 2026-09-22, "
    "escalation #1824 -- previously said verse.reference, the same wrong claim ib_node."
    "verse_reference carried, inherited via this text's own 'same convention as' reference; "
    "confirmed live: 0 of 13 non-null values fail to join against verse.osisId), same convention "
    "as ib_node.verse_reference; written in the SAME DB update as the rest of the subgroup row "
    "(#1693's recording pass), never a separate pass or left null-then-backfilled."
)


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

        cur.execute(
            "SELECT use FROM cfg_column WHERE database='iba' AND table_name='ib_node' "
            "AND name='verse_reference'")
        row = cur.fetchone()
        if row is None:
            report.append("cfg_column iba.ib_node.verse_reference not found — nothing to fix")
        elif row[0] == CORRECT_USE:
            report.append("cfg_column iba.ib_node.verse_reference already correct — skipped")
        else:
            cur.execute(
                "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='ib_node' "
                "AND name='verse_reference'", (CORRECT_USE,))
            report.append("cfg_column iba.ib_node.verse_reference use text corrected "
                          "(verse.reference -> verse.osisId)")

        cur.execute(
            "SELECT use FROM cfg_column WHERE database='iba' AND table_name='cluster_subgroup' "
            "AND name='anchor_verse_reference'")
        row = cur.fetchone()
        if row is None:
            report.append("cfg_column iba.cluster_subgroup.anchor_verse_reference not found — nothing to fix")
        elif row[0] == CORRECT_USE_SUBGROUP:
            report.append("cfg_column iba.cluster_subgroup.anchor_verse_reference already correct — skipped")
        else:
            cur.execute(
                "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='cluster_subgroup' "
                "AND name='anchor_verse_reference'", (CORRECT_USE_SUBGROUP,))
            report.append("cfg_column iba.cluster_subgroup.anchor_verse_reference use text corrected "
                          "(verse.reference -> verse.osisId)")

        self_path = "iba/app/migration/fix_ib_node_verse_reference_doc_v1_20260922.py"
        if cur.execute("SELECT 1 FROM cfg_utility WHERE file_path=?", (self_path,)).fetchone() is None:
            cur.execute(
                "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt) "
                "VALUES (?,?,?,1,0)",
                ("fix_ib_node_verse_reference_doc_v1_20260922", self_path,
                 "ONE-OFF migration, escalation #1824 -- corrects cfg_column.use for "
                 "ib_node.verse_reference, which wrongly claimed resolution against verse.reference "
                 "when the real write path uses verse.osisId. inactive=1 once applied."))
            report.append("cfg_utility (self) added")
        else:
            report.append("cfg_utility (self) already present")

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
