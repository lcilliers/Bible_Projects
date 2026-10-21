"""bootstrap_cluster_strong_evidence_columns_20260812.py — ONE-OFF: add the evidence columns
`cluster_strong` needs to carry an LLM-allocation pass's own review signal, not just the bare
assignment — same class of exception as bootstrap_inactive_column.py (ALTER TABLE is DDL,
configmaint.propose can't do it).

WHY. wa-global-cluster-alloc-final-v1_3-20260811.json (researcher's own LLM-assisted allocation
round, per the design already scoped this session — F3 in its own meta.decisions block: "schema
incl. cluster_code, confidence, operation, alt_clusters, review_flag, rationale") carries real
review evidence per assignment — 574/1612 items flagged `review_flag=true` (confidence='low').
`cluster_strong` as built (bootstrap_cluster_tables_20260811.py) only had `(strong, cluster_code,
source)` — enough for the old-system migration, not enough to keep this pass's evidence trail.
Honoring the source file's own schema design rather than discarding fields on write.

  confidence     TEXT     'high' | 'medium' | 'low' (NULL for old-system-migration rows)
  operation      INTEGER  1 if the code denotes a human operation/movement (candidate for T3)
  alt_clusters   TEXT     JSON list of alternate cluster_code candidates considered
  review_flag    INTEGER  1 if this assignment needs researcher review before being trusted
  rationale      TEXT     free-text reasoning for the assignment

All nullable/default-0 — old-system-migration rows (source='old-system-migration') simply carry
NULL/0 for these, no backfill attempted (there is no equivalent evidence to backfill from).

    python -m iba.app.migration.bootstrap_cluster_strong_evidence_columns_20260812 --dry-run
    python -m iba.app.migration.bootstrap_cluster_strong_evidence_columns_20260812
"""
from __future__ import annotations

import argparse
import sqlite3
import sys

from ..lib.cfg import DB_PATH

NEW_COLUMNS = [
    ("confidence", "TEXT", None,
     "'high' | 'medium' | 'low' -- an allocation pass's own confidence in this assignment; NULL "
     "for old-system-migration rows (no equivalent signal)."),
    ("operation", "INTEGER", "0",
     "1 if the code denotes a human operation/movement (a T3 'Operations' candidate), 0/NULL "
     "otherwise."),
    ("alt_clusters", "TEXT", None,
     "JSON list of alternate cluster_code candidates an allocation pass considered besides the "
     "one it picked."),
    ("review_flag", "INTEGER", "0",
     "1 if this specific assignment needs researcher review before being trusted as final."),
    ("rationale", "TEXT", None,
     "free-text reasoning for the assignment, as given by whatever process produced it."),
]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []
    cols = {r[1] for r in conn.execute('PRAGMA table_info("cluster_strong")')}

    if a.dry_run:
        for name, type_, dflt, use in NEW_COLUMNS:
            print(f"  - cluster_strong.{name} "
                  f"{'already present' if name in cols else 'would be added (ALTER TABLE)'}")
        conn.close()
        return 0

    ordinal_base = conn.execute(
        "SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_column WHERE table_name='cluster_strong'"
    ).fetchone()[0]

    for i, (name, type_, dflt, use) in enumerate(NEW_COLUMNS):
        if name not in cols:
            dflt_clause = f" DEFAULT {dflt}" if dflt is not None else ""
            conn.execute(f'ALTER TABLE "cluster_strong" ADD COLUMN "{name}" {type_}{dflt_clause}')
            report.append(f"cluster_strong.{name} column added (physical ALTER)")
        else:
            report.append(f"cluster_strong.{name} already present")

        if not conn.execute(
                "SELECT 1 FROM cfg_column WHERE table_name='cluster_strong' AND name=?",
                (name,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_column VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                ("cluster_strong", name, ordinal_base + i, type_, 0, 0, 0, dflt, None, use,
                 None, None, None))
            report.append(f"cfg_column row for cluster_strong.{name} added")
        else:
            report.append(f"cfg_column row for cluster_strong.{name} already present")

    conn.commit()
    conn.close()
    print("cluster_strong evidence-columns bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
