"""Deletes existing `ib_observation` rows whose `question_code` doesn't match a real, live
catalogue leaf question -- found live 2026-09-17, researcher spotted it directly: "there is a data
quality error in ib_node with M0.1 and M0.5 not showing the next level so the question cannot be
bound with the node." Investigated: 76 rows (38 strongs, 2 each) filed under the bare component
code (`M0.1`/`M0.5`) instead of a real leaf code, under M67's front-loaded #1723 redo -- ALL 38
affected strongs had ZERO properly-coded word-level battery answers otherwise, just these two
unbindable blobs each. Worse than a binding gap: the front-loading skip-check
(`_strongs_needing_battery`) treats "any observation exists" as covered, so these strongs would
never have been properly re-asked.

Root cause fixed separately, same turn (`recordingpass.py`: `_validate_question_code`/
`InvalidQuestionCode`, wired into `record_one_observation` -- refuses to write a phantom
observation under an invalid question_code going forward). This migration is the data-side cleanup
only: deletes the existing bad rows (and their `ib_node` children) so the 38 affected strongs
correctly show as not-yet-covered and get properly re-asked on the next real run.

Safe to re-run: idempotent (no-ops once clean).

Usage:
    python iba/app/migration/clean_invalid_question_code_observations_v1_20260917.py [--db PATH] [--dry-run]
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

    bad = conn.execute(
        "SELECT o.id, o.cluster_code, o.strong, o.question_code FROM ib_observation o "
        "WHERE o.question_code IS NOT NULL AND NOT EXISTS "
        "(SELECT 1 FROM wa_obs_question_catalogue c WHERE c.question_code=o.question_code "
        "AND c.deleted=0 AND c.status='active')").fetchall()

    print(f"{len(bad)} ib_observation row(s) with an invalid question_code:")
    by_code: dict[str, int] = {}
    for r in bad:
        by_code[r["question_code"]] = by_code.get(r["question_code"], 0) + 1
    for code, n in sorted(by_code.items()):
        print(f"  {code!r}: {n}")

    if args.dry_run or not bad:
        print("--dry-run or nothing to do: no changes made.")
        conn.close()
        return 0

    bad_ids = [r["id"] for r in bad]
    ph = ",".join("?" * len(bad_ids))
    conn.execute(f"DELETE FROM ib_node WHERE observation_id IN ({ph})", bad_ids)
    conn.execute(f"DELETE FROM ib_observation WHERE id IN ({ph})", bad_ids)
    conn.commit()

    remaining = conn.execute(
        "SELECT COUNT(*) n FROM ib_observation o WHERE o.question_code IS NOT NULL "
        "AND NOT EXISTS (SELECT 1 FROM wa_obs_question_catalogue c "
        "WHERE c.question_code=o.question_code AND c.deleted=0 AND c.status='active')"
    ).fetchone()["n"]
    print(f"Deleted {len(bad_ids)} observation(s) + their ib_node children. "
         f"Remaining invalid: {remaining}.")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
