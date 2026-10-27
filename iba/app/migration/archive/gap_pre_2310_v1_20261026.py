"""gap_pre_2310_v1_20261026.py -- escalation #2310: 0.GAP pre no longer reads documents, and an open item shows the
subgroups it reaches (outputs/escalation/2310-gap-pre-open-item-hooks-v1-20261026.md section 4), approved by the
researcher 2026-10-26: "4.1 approve; 4.2 option B".

The gap type read_in_files_only goes inactive in cfg_enum reading_gap_type and leaves cfg_setting reading.gap_types
(the same way as hit_unread); the open_item guide says the record shows the subgroups the item reaches. The code
change (iba/app/lib/reading.py: the read_in_files_only detector removed, _item_subgroups added) is in the same unit.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own path) in the same
transaction. Refuses to run twice (its run_id in cfg_change_detail).

Usage:
    python iba/app/migration/archive/gap_pre_2310_v1_20261026.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2310-GAP-PRE-20261026"
MODULE = "gap_pre_2310_v1_20261026"
OPEN_ITEM_GUIDE = ("An open item that matches the scope: read for what it asks, and record what the reading found. "
                   "The item shows the subgroups it reaches (its target cluster and terms through surface_subgroup); "
                   "an item with none is pulled by its verses or its cluster only. It is settled at the claim step.")


class Refused(Exception):
    pass


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    row = one("SELECT value FROM cfg_setting WHERE key='reading.gap_types'")
    spec = json.loads(row[0])
    if "open_item" not in spec:
        raise Refused("reading.gap_types has no open_item")
    spec.pop("read_in_files_only", None)
    spec["open_item"]["guide"] = OPEN_ITEM_GUIDE
    ops.append(("cfg_setting", "update", {"key": "reading.gap_types"}, {"value": json.dumps(spec, ensure_ascii=False)}))
    if not one("SELECT 1 FROM cfg_enum WHERE name='reading_gap_type' AND value='read_in_files_only'"):
        raise Refused("cfg_enum reading_gap_type has no read_in_files_only")
    ops.append(("cfg_enum", "update", {"name": "reading_gap_type", "value": "read_in_files_only"}, {"inactive": 1}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2310: 0.GAP pre drops document reading, open items show "
                       f"their subgroups; run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID} is in cfg_change_detail)")
        return 0
    try:
        ops = plan(conn)
    except Refused as exc:
        print(f"REFUSED, nothing written: {exc}")
        return 2
    summary = ", ".join(f"{t} {op}" for t, op, _, _ in ops)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s): {summary}")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail): {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
