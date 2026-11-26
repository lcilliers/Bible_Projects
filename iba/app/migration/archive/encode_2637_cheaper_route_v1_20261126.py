"""encode_2637_cheaper_route_v1_20261126.py -- cfg_behaviour_rule 20 made the default, not a flag (researcher 2026-11-26, Developer Mode, #2637).

Researcher, verbatim: "set the rules that you will ALWAYS use the cheaper route by default". Through configmaint.apply_logged; archived after
the live apply. Idempotent. Usage: python iba/app/migration/encode_2637_cheaper_route_v1_20261126.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2637-CHEAPERROUTE-20261126"
MODULE = "encode_2637_cheaper_route_v1_20261126"
TEXT = ("The cheaper route is the default, taken without being asked, wherever it gives the same outcome: a targeted search or a line range "
        "instead of a whole file, a list or a dump read into the conversation; a direct query instead of a subagent; one dry run, then the run; "
        "a test that prints only its failures and a count, and after a fix a re-run of only the failing case; a cheaper model for routine work. "
        "A dearer route is taken only where the cheaper one cannot give the outcome, and the reason is stated before it is taken.")
SOURCE = "researcher 2026-11-26 (Developer Mode, #2637), verbatim: \"set the rules that you will ALWAYS use the cheaper route by default\""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    cur = conn.execute("SELECT rule_text FROM cfg_behaviour_rule WHERE id=20").fetchone()
    ops = [] if cur[0] == TEXT else [("cfg_behaviour_rule", "update", {"id": 20}, {"rule_text": TEXT, "source": SOURCE})]
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py", "purpose": "B:20 made the default cheaper route",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        return 0
    for t, op, where, set_ in ops:
        apply_logged(conn, RUN_ID, t, op, where, set_)
    conn.commit()
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    if pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve():
        print(f"archived: {archive_migration(conn, RUN_ID, __file__)}")
        conn.commit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
