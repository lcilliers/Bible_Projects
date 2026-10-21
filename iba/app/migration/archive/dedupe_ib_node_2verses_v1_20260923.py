"""dedupe_ib_node_2verses_v1_20260923.py — ONE-OFF migration, escalation #1847.

Residue from the #1832/#1834 dedup rework earlier the same day (2026-09-22), before that fix's
final form: 27 (observation_id, strong, verse_reference, question_code) groups across 2 verses
(2Cor.8.16, 2Pet.1.5) each carry 2-3 `ib_node` rows citing the IDENTICAL occurrence under the SAME
already-correct, already-consolidated observation -- ~30 redundant node rows total, larger than the
escalation's original "2 rows" estimate (checked precisely, not re-guessed).

Not a content bug -- every affected observation is already the correct, canonical one. Purely
redundant citation pointers. `ib_node` has no soft-delete/status column (checked: id,
observation_id, cluster_code, cluster_subgroup_code, strong, verse_reference, surface, morph_code,
question_code, traced_observation_id, source_stage, seq, created_at) -- unlike every other fix this
session, there is no withdraw option here; cleanup requires a physical DELETE. Confirmed a rerun
(even -Force) will not do this on its own: `record_one_observation` skips re-adding a node when the
occurrence already has one, but has no step that removes existing redundant ones.

Keeps the lowest `id` (earliest-created) node in each duplicate group as canonical, deletes the
rest. No `traced_observation_id` in this table points AT an `ib_node.id` (it references
`ib_observation.id`), so no other row can be citing a node by its id -- safe to delete outright.

Idempotent (only touches groups with >1 row) -- a second run is a no-op.

    python -m iba.app.migration.dedupe_ib_node_2verses_v1_20260923
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_VERSES = ('2Cor.8.16', '2Pet.1.5')


def apply_fix(conn: sqlite3.Connection) -> list[str]:
    ph = ",".join("?" * len(_VERSES))
    groups = conn.execute(
        f"SELECT observation_id, strong, verse_reference, question_code, "
        f"GROUP_CONCAT(id) ids FROM ib_node WHERE verse_reference IN ({ph}) "
        f"GROUP BY observation_id, strong, verse_reference, question_code "
        f"HAVING COUNT(*) > 1", _VERSES).fetchall()
    report = []
    total_deleted = 0
    for g in groups:
        ids = sorted(int(x) for x in g["ids"].split(","))
        keep, drop = ids[0], ids[1:]
        conn.execute(f"DELETE FROM ib_node WHERE id IN ({','.join('?'*len(drop))})", drop)
        total_deleted += len(drop)
        report.append(f"{g['verse_reference']} strong={g['strong']} q={g['question_code']} "
                     f"obs={g['observation_id']}: kept node {keep}, deleted {drop}")
    report.append(f"TOTAL: {len(groups)} groups deduplicated, {total_deleted} redundant nodes deleted")
    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        report = apply_fix(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
