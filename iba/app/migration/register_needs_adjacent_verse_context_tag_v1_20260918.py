"""Registers the missing `needs_adjacent_verse_context` value for `ib_observation.tag`.

Found live 2026-09-18 building Stage 4 (`cluster.reading` process d): checklist §0 rule 5a / §2
rule (Stage 1 prompt) / §3 rule 4 (Stage 4's own precondition) all tell the LLM by name to use this
exact tag when a verse's own content is insufficient and an adjacent verse would help -- but it was
never actually registered in `cfg_enum`. Confirmed live: 0 rows anywhere carry it, and no past run's
outcome mentions an `invalid-tag` skip for it either -- so nothing has been silently lost yet, but
the FIRST time any stage's LLM call genuinely needed to raise this flag, `recordingpass.
_validate_tag` would have rejected it outright (`InvalidTag`), silently dropping a real,
instruction-mandated finding with no error surfaced anywhere. Root-fixed here (the shared cause,
not a per-stage patch) before Stage 4 -- which explicitly needs this tag for its own precondition
(checklist §3 rule 4) -- goes live.

Safe to re-run: idempotent (checks existence before insert).

Usage:
    python iba/app/migration/register_needs_adjacent_verse_context_tag_v1_20260918.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

TAG_NAME = "ib_observation.tag"
TAG_VALUE = "needs_adjacent_verse_context"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    existing = conn.execute(
        "SELECT inactive FROM cfg_enum WHERE name=? AND value=?", (TAG_NAME, TAG_VALUE)).fetchone()
    if existing:
        print(f"already registered (inactive={existing['inactive']}) -- nothing to do.")
        conn.close()
        return 0

    max_ordinal = conn.execute(
        "SELECT COALESCE(MAX(ordinal), 0) m FROM cfg_enum WHERE name=?", (TAG_NAME,)).fetchone()["m"]
    next_ordinal = max_ordinal + 1

    print(f"1 pending action: insert cfg_enum {TAG_NAME}={TAG_VALUE!r} at ordinal {next_ordinal}")
    if args.dry_run:
        print("--dry-run: no changes made.")
        conn.close()
        return 0

    conn.execute("INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
                (TAG_NAME, TAG_VALUE, next_ordinal))
    conn.commit()
    print("Applied.")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
