"""elementscap_2538_v1_20261126.py -- escalation #2538 (researcher 2026-11-26: "lets continue to complete all the sub groups for thought in this chat").

The elements package of "thinking and thought" (79 words, 212 occurrences) is 369,539 characters: 241 observations to take up, 89 it may rest on, 113 older inner-being
observations, 115 earlier readings, 194 verses. ReadElements refuses it at elements.package_max_chars 160000, and a 3.1 row is recorded whole, so the package cannot be split.
The read material alone (take-up, verses, occurrences, meanings, instruction) is about 250,000 characters, so no trimming brings it under 160,000.
  cfg_setting layer.read_types   elements.package_max_chars 160000 -> 400000, and the `use` text says why; the other reads are kept as they are
  cfg_utility this migration (inactive)
Written through configmaint.apply_logged. Named snapshot before a live apply. Idempotent.
Usage: python iba/app/migration/elementscap_2538_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2538-ELEMENTSCAP-20261126"
MODULE = "elementscap_2538_v1_20261126"
CAP = 400000
USE_ADD = (" The elements cap was raised from 160000 to 400000 on 2026-11-26 (#2538): the 3.1 package of the subgroup 'thinking and thought' (212 occurrences) is 369,539 "
           "characters, and a 3.1 row cannot be split.")


def plan(conn):
    ops = []
    rt_ = conn.execute("SELECT value, use FROM cfg_setting WHERE key='layer.read_types'").fetchone()
    if rt_ is None:
        raise SystemExit("cfg_setting layer.read_types is missing: the earlier #2538 migrations come first")
    types = json.loads(rt_[0])
    if "elements" not in types:
        raise SystemExit("layer.read_types has no elements read: elements_2538_v1_20261126 comes first")
    use = rt_[1] if USE_ADD in (rt_[1] or "") else (rt_[1] or "") + USE_ADD
    if types["elements"].get("package_max_chars") != CAP or use != rt_[1]:
        types["elements"] = {**types["elements"], "package_max_chars": CAP}
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps(types, ensure_ascii=False), "use": use}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of escalation #2538: raises layer.read_types elements.package_max_chars to 400000",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    ops = plan(conn)
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or {k: set_[k] for k in list(set_)[:3]})
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-elementscap-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT rel")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE rel")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO rel")
        conn.execute("RELEASE rel")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
