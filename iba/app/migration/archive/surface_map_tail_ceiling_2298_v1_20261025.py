"""surface_map_tail_ceiling_2298_v1_20261025.py -- escalation #2298 (#2286 U8a pilot): the output ceiling of one tail
call raised from 16000 to 32000. M18's tail of 291 pairs took 14,751 output tokens, so a cluster's tail of up to 375
pairs (the largest) would overrun 16000; at 32000 the per-call estimate stays under lexical.llm_max_cost_per_batch.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Idempotent.

Usage:
    python iba/app/migration/surface_map_tail_ceiling_2298_v1_20261025.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2298-TAIL-CEILING-20261025"
MODULE = "surface_map_tail_ceiling_2298_v1_20261025"
KEY, VALUE = "cluster.surface_map.tail_max_output_tokens", "32000"
USE = ("#2293 D3, #2298: the output ceiling of one tail call (one call per cluster), sized on the M18 pilot (291 pairs "
       "took 14,751 output tokens) for the largest tail (375 pairs); model, rates and the per-call cost cap are the "
       "lexical.llm_* settings")


def plan(conn) -> list[tuple]:
    ops = []
    r = conn.execute("SELECT value, use FROM cfg_setting WHERE key=?", (KEY,)).fetchone()
    if r and (r[0], r[1]) != (VALUE, USE):
        ops.append(("cfg_setting", "update", {"key": KEY}, {"value": VALUE, "use": USE}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2298: {KEY} 16000 -> 32000 after the M18 pilot; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
