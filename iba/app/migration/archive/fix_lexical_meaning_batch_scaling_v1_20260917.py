"""Fixes a real scaling gap in `lexical.meaning`'s batching, found live redoing `M67`'s
verse-reading under the new front-loading design (#1723): `passage.max_verses` (20, shared with
`lexical.enrich`) was sized for the OLD narrower per-cluster-only output -- with front-loading
(every M-code strong in a batch's verses, not just the cluster's own members), a real batch (20
verses, `M67`) needed 55 strongs' worth of answers and truncated mid-response even at
`lexical.llm_max_output_tokens=20000` (`report-stop`, "Unterminated string").

Two changes:
1. New `lexical.meaning_max_verses_per_batch` setting (10, half of `passage.max_verses`) -- a
   dedicated override for this step only; `lexical.enrich` and other `passage.max_verses` consumers
   are unaffected.
2. `lexical.llm_max_output_tokens` raised 20000 -> 40000 as a safety margin on top of the smaller
   batch size, not a replacement for it.

Safe to re-run: idempotent.

Usage:
    python iba/app/migration/fix_lexical_meaning_batch_scaling_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    actions = []

    exists = conn.execute(
        "SELECT 1 FROM cfg_setting WHERE key='lexical.meaning_max_verses_per_batch'").fetchone()
    if not exists:
        actions.append(("insert setting", "lexical.meaning_max_verses_per_batch=10"))

    cur_max = conn.execute(
        "SELECT value FROM cfg_setting WHERE key='lexical.llm_max_output_tokens'").fetchone()
    if cur_max and cur_max["value"] != "40000":
        actions.append(("update setting", f"lexical.llm_max_output_tokens {cur_max['value']} -> 40000"))

    print(f"{len(actions)} pending action(s):")
    for a in actions:
        print(" -", a)

    if args.dry_run or not actions:
        print("--dry-run or nothing to do: no changes made.")
        conn.close()
        return 0

    if not exists:
        conn.execute(
            "INSERT INTO cfg_setting (key, value, use, module, inactive) VALUES "
            "('lexical.meaning_max_verses_per_batch', '10', "
            "'Dedicated batch-size override for lexical.meaning only (#1723) -- front-loading "
            "(every M-code strong in a batch verse-count, not just the cluster''s own members) "
            "multiplies expected output roughly by strong-density-per-batch. The shared "
            "passage.max_verses (20) truncated a real batch (55 strongs) even at "
            "lexical.llm_max_output_tokens=20000. Other passage.max_verses consumers "
            "(lexical.enrich) are unaffected by this override.', 'lexical', 0)")

    if cur_max and cur_max["value"] != "40000":
        conn.execute(
            "UPDATE cfg_setting SET value='40000' WHERE key='lexical.llm_max_output_tokens'")

    conn.commit()
    print("Applied.")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
