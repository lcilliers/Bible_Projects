"""delete_blank_tag_candidates.py — ONE-OFF: soft-delete candidate_seed rows the researcher ruled
invalid, 2026-07-22 DB review: "There are a large number of blank tags - this is a straight fail
error - should not happen. these rows must be deleted." Also covers the narrower case explicitly
called out the same review: "Blank registry and blank tag is an error - false row" (169 of these
280 are also registry_match IS NULL — a strict subset, same disposition).

Scope: `decision='candidate' AND tag IS NULL AND deleted=0` — a candidate that was seeded but
never got a real, single-concept label. Soft-delete only (`deleted=1`), per this app's universal
soft-delete convention (no physical deletes anywhere else) — reversible and still inspectable.

Does NOT touch `decision='rejected'`/`'undecided'` rows with a null tag — a rejected lemma is
correctly tagless (it was never meant to carry an IB label), and undecided rows are still pending
assessment, not "should not happen."

    python -m iba.app.migration.delete_blank_tag_candidates --dry-run
    python -m iba.app.migration.delete_blank_tag_candidates
"""

from __future__ import annotations

import argparse
import datetime
import sqlite3
import sys

from ..lib.cfg import DB_PATH


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _target_rows(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    conn.row_factory = sqlite3.Row
    return conn.execute("""
        SELECT id, lemma_key, strong_variant, layer, registry_match FROM candidate_seed
        WHERE decision='candidate' AND tag IS NULL AND deleted=0
    """).fetchall()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    rows = _target_rows(conn)
    also_blank_registry = sum(1 for r in rows if r["registry_match"] is None)
    by_layer: dict[str, int] = {}
    for r in rows:
        by_layer[r["layer"]] = by_layer.get(r["layer"], 0) + 1

    print(f"{len(rows)} candidate_seed row(s) to soft-delete (decision='candidate', tag IS NULL):")
    print(f"  of which also registry_match IS NULL (the 'false row' case): {also_blank_registry}")
    print(f"  by layer: {by_layer}")

    if a.dry_run:
        print("\n--dry-run: no changes made.")
        conn.close()
        return 0

    now = _now()
    ids = [r["id"] for r in rows]
    conn.executemany("UPDATE candidate_seed SET deleted=1, assessed_at=? WHERE id=?",
                     [(now, i) for i in ids])
    conn.commit()
    print(f"\nsoft-deleted {len(ids)} row(s) (deleted=1, assessed_at={now}).")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
