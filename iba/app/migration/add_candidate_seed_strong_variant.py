"""add_candidate_seed_strong_variant.py — ONE-OFF: add candidate_seed.strong_variant, the
column found missing 2026-07-22 (researcher's DB review: "many of these words are actually sub
strong terms... I do not believe we anywhere else have a list of tags to sub strong key").

Confirmed live: 173 of 3,178 base lemma_keys have multiple sub-lettered `strong` variants with
GENUINELY DIFFERENT glosses (e.g. G0769G "weakness: weak" vs G0769H "weakness: ill"). candidate_
seed.lemma_key is base-only by design (candidate.lemma_base_pattern strips the sub-letter on
purpose) — there was no way to record which specific sub-strong a seed row's tag/gloss actually
came from, and no way to give ONE base lemma multiple clean, single-concept tags (one per
sub-sense) as the researcher's tag-cleanliness principle requires ("each word must be a single
concept").

Design: `strong_variant` defaults to the LEMMA_KEY ITSELF (not NULL) when a row applies to the
whole base lemma (the case for virtually all 2,086 existing rows — no split needed/decided yet).
NULL was deliberately avoided: SQLite/SQL treats NULL <> NULL for UNIQUE-constraint purposes, and
lib/db.py's Db.upsert() dedups via a plain `=` comparison (not NULL-safe `IS`) — a NULL default
would have silently broken upsert's existing-row lookup for every current row, inserting a
duplicate on every future candidate.seed() re-run. Using lemma_key-as-default keeps the existing
dedup behaviour exactly as it was, and the FK to lemma_key encodes "row for a not-yet-split lemma"
without a NULL special case anywhere else in the codebase.

Dedup key changes from (lemma_key) alone to (lemma_key, strong_variant) — SQLite cannot ALTER a
UNIQUE constraint in place, so this rebuilds the table (create new, copy, drop, rename), same
technique as any SQLite constraint migration.

This migration does the PHYSICAL table change only. The cfg_column/cfg_unique config rows that
describe it are registered separately via configmaint.propose (the governed path for tables it can
already express row-level changes on) — see the companion configmaint.propose calls run alongside
this script, not duplicated here.

    python -m iba.app.migration.add_candidate_seed_strong_variant --dry-run
    python -m iba.app.migration.add_candidate_seed_strong_variant
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
    cols = {r[1] for r in conn.execute("PRAGMA table_info(candidate_seed)")}
    if "strong_variant" in cols:
        print("candidate_seed.strong_variant already present — nothing to do")
        conn.close()
        return 0

    n = conn.execute("SELECT COUNT(*) FROM candidate_seed").fetchone()[0]
    print(f"candidate_seed: {n} row(s) to migrate — add strong_variant (default = lemma_key), "
          f"rebuild UNIQUE(lemma_key, strong_variant)")
    if a.dry_run:
        print("--dry-run: no changes made.")
        conn.close()
        return 0

    conn.execute("""
        CREATE TABLE candidate_seed_new (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lemma_key TEXT NOT NULL,
            decision TEXT,
            layer TEXT,
            registry_match TEXT,
            tag TEXT,
            strong_variant TEXT NOT NULL,
            assessed_at TEXT,
            deleted INTEGER DEFAULT 0,
            FOREIGN KEY (lemma_key) REFERENCES lemma_inventory(lemma_key),
            UNIQUE (lemma_key, strong_variant)
        )
    """)
    conn.execute("""
        INSERT INTO candidate_seed_new
            (id, lemma_key, decision, layer, registry_match, tag, strong_variant, assessed_at, deleted)
        SELECT id, lemma_key, decision, layer, registry_match, tag, lemma_key, assessed_at, deleted
        FROM candidate_seed
    """)
    conn.execute("DROP TABLE candidate_seed")
    conn.execute("ALTER TABLE candidate_seed_new RENAME TO candidate_seed")
    conn.commit()

    check = conn.execute("SELECT COUNT(*) FROM candidate_seed").fetchone()[0]
    variant_eq_lemma = conn.execute(
        "SELECT COUNT(*) FROM candidate_seed WHERE strong_variant = lemma_key").fetchone()[0]
    print(f"migrated {check} row(s); {variant_eq_lemma} carry strong_variant = lemma_key (the default, "
         f"no split yet) — should equal the original row count ({n})")
    conn.close()
    return 0 if check == n == variant_eq_lemma else 1


if __name__ == "__main__":
    sys.exit(main())
