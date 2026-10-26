"""large_subgroup_segment_2298_v1_20261026.py -- escalation #2298 (#2286 U8), the researcher's ruling Q3 a of
2026-10-26 on outputs/escalation/2298-bulk-surface-map-v1-20261026.md: the 30% size check stays as it is, and a large
subgroup is segmented by a pre-analysis when it comes into focus for reading.

1. cfg_method_rule on reading.open: RO13 segment-large-subgroup.

Delivered as context with reading.open's rules; no code enforces it. cfg_* writes through configmaint.apply_logged().
Registers itself (inactive, at its own archive path). Idempotent.

Usage:
    python iba/app/migration/large_subgroup_segment_2298_v1_20261026.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2298-LARGE-SUBGROUP-20261026"
MODULE = "large_subgroup_segment_2298_v1_20261026"
RULE = {"step": "reading.open", "rule_key": "RO13 segment-large-subgroup", "ordinal": 68, "active": 1,
        "rule_text": "A large subgroup (one the surface-map size check flags, over 30% of its cluster's hits) is not "
                     "read as one scope. When it comes into focus, a pre-analysis first segments it into logical "
                     "units, and the reading scope is set on those units. The segmenting is done then, not in advance.",
        "source_doc": "#2298 Q3 a, researcher 2026-10-26 (outputs/escalation/2298-bulk-surface-map-v1-20261026.md)",
        "enforced_by": None}


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_method_rule WHERE step=? AND rule_key=?", RULE["step"], RULE["rule_key"]):
        ops.append(("cfg_method_rule", "insert", {}, RULE))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2298 Q3 a: reading.open method rule RO13 "
                       f"segment-large-subgroup; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run:
        for t, op, where, set_ in ops:
            print(f"  {op:6} {t:20} {where or set_.get('rule_key') or set_.get('module')}")
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
