"""Backfills `ib_observation.cluster_subgroup_id`/`ib_node.cluster_subgroup_code` for existing
`char-reading`/`char-answers` rows written BEFORE the 2026-09-18 `recordingpass.py` fix (both
columns are real, already-registered `cfg_column` entries that were simply never populated by any
of the 4 live stages until today). Found live -- researcher's own review of the data.

Scope: `stage`/`source_stage` IN ('char-reading', 'char-answers') only -- `verse-reading` and
`char-subgroup` correctly stay NULL per both columns' own `cfg_column.use` text (pre-subgroup, and
"process (b)'s own cluster-level observations", respectively). Derives each row's subgroup from
its own `strong` (observation) or `ib_node.strong` (node) via `cluster_subgroup_strong` -- every
strong belongs to exactly one live subgroup by construction (checklist §1 rule 9), so this is a
safe, unambiguous backfill, not a guess.

Safe to re-run: idempotent (only touches rows where the column is currently NULL and a subgroup is
resolvable).

Usage:
    python iba/app/migration/backfill_subgroup_columns_char_reading_answers_v1_20260918.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

STAGES = ("char-reading", "char-answers")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    # `strong` may be NULL on the observation itself (a Stage 4 subgroup-wide slant) -- fall back
    # to any of its own ib_node rows' strong (all of which belong to the same subgroup in practice,
    # since Stage 3/4 are scoped to exactly one subgroup per run).
    obs_rows = conn.execute(
        f"SELECT o.id, COALESCE(o.strong, (SELECT n.strong FROM ib_node n "
        f"WHERE n.observation_id = o.id AND n.strong IS NOT NULL LIMIT 1)) AS strong "
        f"FROM ib_observation o WHERE o.stage IN ({','.join('?' * len(STAGES))}) "
        f"AND o.cluster_subgroup_id IS NULL", STAGES).fetchall()
    obs_rows = [r for r in obs_rows if r["strong"] is not None]
    node_rows = conn.execute(
        f"SELECT id, strong FROM ib_node WHERE source_stage IN ({','.join('?' * len(STAGES))}) "
        f"AND cluster_subgroup_code IS NULL AND strong IS NOT NULL", STAGES).fetchall()

    def subgroup_for(strong: str) -> tuple[int | None, str | None]:
        row = conn.execute(
            "SELECT g.id, g.subgroup_code FROM cluster_subgroup_strong s "
            "JOIN cluster_subgroup g ON g.id = s.cluster_subgroup_id "
            "WHERE s.strong=? AND s.delete_flagged=0 AND g.delete_flagged=0", (strong,)).fetchone()
        return (row["id"], row["subgroup_code"]) if row else (None, None)

    obs_updates = []
    unresolved_obs = []
    for r in obs_rows:
        sid, _ = subgroup_for(r["strong"])
        if sid is not None:
            obs_updates.append((sid, r["id"]))
        else:
            unresolved_obs.append((r["id"], r["strong"]))

    node_updates = []
    unresolved_node = []
    for r in node_rows:
        _, scode = subgroup_for(r["strong"])
        if scode is not None:
            node_updates.append((scode, r["id"]))
        else:
            unresolved_node.append((r["id"], r["strong"]))

    print(f"ib_observation: {len(obs_rows)} candidate row(s), {len(obs_updates)} resolvable, "
         f"{len(unresolved_obs)} unresolved: {unresolved_obs}")
    print(f"ib_node: {len(node_rows)} candidate row(s), {len(node_updates)} resolvable, "
         f"{len(unresolved_node)} unresolved: {unresolved_node}")

    if args.dry_run or not (obs_updates or node_updates):
        print("--dry-run or nothing to do: no changes made.")
        conn.close()
        return 0

    conn.executemany("UPDATE ib_observation SET cluster_subgroup_id=? WHERE id=?", obs_updates)
    conn.executemany("UPDATE ib_node SET cluster_subgroup_code=? WHERE id=?", node_updates)
    conn.commit()
    print(f"Applied: {len(obs_updates)} ib_observation row(s), {len(node_updates)} ib_node row(s).")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
