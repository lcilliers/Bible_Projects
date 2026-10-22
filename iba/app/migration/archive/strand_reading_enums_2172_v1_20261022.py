"""strand_reading_enums_2172_v1_20261022.py -- escalation #2172 (and #2215): what
strand_reading_steps_2172_v1_20261022 left out, as configmaint.validate reported -- cfg_enum
config_module gains strand_reading (the module of strand_reading.output_dir) and
escalation_requirement_check_kind gains strand_account_clean (the close gate); the Tell and Untell
step descriptions name the block (-Section), not the passage. cfg_* writes through
configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Idempotent.

Usage:
    python iba/app/migration/strand_reading_enums_2172_v1_20261022.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2172-STRAND-ENUMS-20261022"
MODULE = "strand_reading_enums_2172_v1_20261022"
ENUMS = [("config_module", "strand_reading"), ("escalation_requirement_check_kind", "strand_account_clean")]
DOES = {
    "narrative_register.tell": "links a claim to the block that tells it (-Chapter -Section <heading>|<Parent > "
                               "Heading>) -- see lib/narrativeregister.py (escalation #2110, #2172)",
    "narrative_register.untell": "removes a claim's telling from a block (status removed; the row stays) -- see "
                                 "lib/narrativeregister.py (escalation #2110, #2172)",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = []
    for name, value in ENUMS:
        if not conn.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, value)).fetchone():
            o = conn.execute("SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
            ops.append(("cfg_enum", "insert", {}, {"name": name, "value": value, "ordinal": o, "inactive": 0}))
    for step, does in DOES.items():
        if conn.execute("SELECT does FROM cfg_step WHERE step=?", (step,)).fetchone()[0] != does:
            ops.append(("cfg_step", "update", {"step": step}, {"does": does}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2172/#2215: enum values config_module strand_reading and "
                       f"check kind strand_account_clean; Tell/Untell step text; run_id {RUN_ID}. inactive=1 once "
                       f"applied."}))
    if a.dry_run or not ops:
        print(f"{'DRY RUN -- ' if a.dry_run else 'already applied -- '}{len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
