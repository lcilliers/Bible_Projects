"""chain_2538_v1_20261126.py -- escalation #2538: IB-07 states the trace chain of stage 4.

Researcher 2026-11-26: "can you confirm that all the corrective and additional work done are now all incorporated in the code, and will be run automatically when the
methods of the package are called." Checking it found the 13 behaviours of thought (3.2) failing IB-07: they trace the 3.1 elements (inner being), as the specification's
trace chain says (C2 to C1), and the check accepted only a direct trace to evidence. validationactions.trace_gaps now follows the chain; this migration writes the rule.
  cfg_method_rule  IB-07 names the chain
  cfg_utility      this migration's own row
Written through configmaint.apply_logged; named snapshot before a live apply; archives itself after. Idempotent.
Usage: python iba/app/migration/chain_2538_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2538-CHAIN-20261126"
MODULE = "chain_2538_v1_20261126"
KEY = "IB-07 inner-being-observations-trace-to-evidence"
OLD = "Every live observation marked inner_being holds at least one live traced node on a live observation marked evidence, unless"
NEW = ("Every live observation marked inner_being holds at least one live traced node on a live observation marked evidence, or on a live inner-being observation that "
       "itself traces to evidence (the trace chain of stage 4: a 3.2 behaviour traces the 3.1 elements it gathers, a 3.3 match the 3.1 and 3.2 observations it comes from; "
       "at most three links), unless")


def plan(conn):
    ops = []
    text = conn.execute("SELECT rule_text FROM cfg_method_rule WHERE rule_key=?", (KEY,)).fetchone()[0]
    if OLD in text and NEW not in text:
        ops.append(("cfg_method_rule", "update", {"rule_key": KEY}, {"rule_text": text.replace(OLD, NEW)}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of #2538: IB-07 names the trace chain of stage 4",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    live = pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve()
    conn = Cfg(pathlib.Path(a.db)).conn
    ops = plan(conn)
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        return 0
    if live and not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2538-chain-apply', named=True)}")
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
    if live:
        print(f"archived: {archive_migration(conn, RUN_ID, __file__)}")
        conn.commit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
