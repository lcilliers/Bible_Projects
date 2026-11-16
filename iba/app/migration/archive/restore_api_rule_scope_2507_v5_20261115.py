"""restore_api_rule_scope_2507_v5_20261115.py -- escalation #2507: B:7, B:8 and B:9 stay delivered at VerseLexical.ps1.

The alignment migration (v4) made their three rule scopes inactive because VerseLexical.ps1 makes no API call; configmaint.validate refuses a rule with no scope, and the researcher's rules are
not dropped (decision v4 section 12: B:7 to B:9 stay unchanged). The scopes are restored. Through configmaint.apply_logged(). Idempotent.
"""
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

RUN_ID = "DEVMODE-2507-RESTORE-API-RULE-SCOPE-20261115"
MODULE = "restore_api_rule_scope_2507_v5_20261115"


def main() -> int:
    cfg = Cfg(pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db"))
    conn = cfg.conn
    n = 0
    conn.execute("SAVEPOINT restore_2507")
    for ref in ("B:7", "B:8", "B:9"):
        r = conn.execute("SELECT inactive FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind='ps' AND scope_value='VerseLexical.ps1'", (ref,)).fetchone()
        if r and r[0]:
            apply_logged(conn, RUN_ID, "cfg_rule_scope", "update", {"rule_ref": ref, "scope_kind": "ps", "scope_value": "VerseLexical.ps1"}, {"inactive": 0})
            n += 1
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py",
                                                                  "purpose": f"ONE-OFF migration -- escalation #2507: the scopes of B:7 to B:9 restored; run_id {RUN_ID}.", "inactive": 1, "config_exempt": 1,
                                                                  "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
                                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None})
        n += 1
    conn.execute("RELEASE restore_2507")
    conn.commit()
    print(f"applied (run {RUN_ID}): {n} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
