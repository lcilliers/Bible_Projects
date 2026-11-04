"""external_service_access_2354_v1_20261103.py -- escalation #2354 (researcher, chat 2026-11-03: "you are suppose to
create configs for it, and update the governance"; and "why are you re-inventing the wheel every time we chat";
"i have no problem to login with my ssh credential - so your configs are not right"; "how can you run a routine
without hardening it with a check that the connection is working. that is really poor coding standards").

How the Ollama server is reached was only in a session log and a compliance file (the batch ssh key
~/.ssh/id_ed25519_iba and the user, Logs/compliance/COMPLIANCE-20261101-9ee0965a.md SC16). This puts it in config:
cfg_setting ollama.ssh_target and ollama.ssh_key, and adds the behaviour rule external-service-access-in-config-and-
checked-first (id 124, general scope link): a routine that uses a service outside the app reads how it is reached
from settings, checks the service before its first call and refuses naming the address and the configured way in,
and halts after a run of failures. The writes go through configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/external_service_access_2354_v1_20261103.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2354-EXTERNAL-SERVICE-ACCESS-20261103"
MODULE = "external_service_access_2354_v1_20261103"
SETTINGS = [
    ("ollama.ssh_target", "leroux@192.168.83.114",
     "user and address for ssh to the machine that runs the Ollama server (the same machine as ollama.host); the "
     "server was reached over ssh in #2354, and the researcher can log in to it with their own ssh credential "
     "(#2354, researcher 2026-11-03). Named in the message when the server check before a run fails"),
    ("ollama.ssh_key", "~/.ssh/id_ed25519_iba",
     "the key file for ssh to that machine in a batch call: the researcher's own key has a passphrase and cannot be "
     "used in a batch call, so a separate key was made and authorised (Logs/compliance/COMPLIANCE-20261101-"
     "9ee0965a.md, SC16). The file is never read or printed; only its path is named"),
]
RULE_KEY = "external-service-access-in-config-and-checked-first"
RULE_TEXT = (
    "A routine that uses a service outside the app (today the Ollama server) reads how the service is reached from "
    "cfg_setting, in the module named for the service: its address, how long to wait for it and, where it is "
    "reached over ssh, the user and the key file. Before its first call it checks that the service answers and has "
    "what the routine needs (for Ollama, the configured model) and, if not, refuses at once, naming the address and "
    "the configured way in, writing nothing; a run halts after a configured number of calls in a row with no usable "
    "answer. Before a route to a service is tried or a new one asked of the researcher, the settings and the written "
    "record (iba/app/BUILD.md, the session logs, the compliance files) are read for how it was reached before.")
RULE_SOURCE = (
    "Researcher, chat 2026-11-03 (verbatim, #2354): \"how can you run a routine with hardnessing it it a check that "
    "the connection is working. that is really poor coding standards\"; \"i have no problem to login with my ssh "
    "credential - so your configs are not right\"; \"why are you re-inventing the wheel every time we chat\"; \"you "
    "are suppose to create configs for it, and update the governance.\"")
RULE_ENFORCED = ("Context-delivered at session start (rule 81); for the Ollama server the check is lib/surfacejudge.py "
                 "preflight() and the halt after surface_judge.max_consecutive_failures.")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use,
                                                      "module": "ollama", "inactive": 0}))
    row = conn.execute("SELECT id FROM cfg_behaviour_rule WHERE rule_key=?", (RULE_KEY,)).fetchone()
    rid = row[0] if row else conn.execute("SELECT MAX(id) FROM cfg_behaviour_rule").fetchone()[0] + 1
    if row is None:
        ops.append(("cfg_behaviour_rule", "insert", {}, {
            "id": rid, "class": "development", "rule_key": RULE_KEY, "rule_text": RULE_TEXT, "source": RULE_SOURCE,
            "enforced_by": RULE_ENFORCED, "added_at": "2026-11-03T00:00:00Z", "active": 1,
            "enforcement_status": "context_delivered", "deliver_when": "always"}))
    if not has("SELECT 1 FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind='general'", f"B:{rid}"):
        ops.append(("cfg_rule_scope", "insert", {}, {
            "id": conn.execute("SELECT MAX(id) FROM cfg_rule_scope").fetchone()[0] + 1, "rule_ref": f"B:{rid}",
            "scope_kind": "general", "scope_value": "general", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2354: how the Ollama server is reached, and the rule that "
                       f"a service is read from config and checked first; run_id {RUN_ID}.",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(f"  {t} {op} {set_.get('key') or set_.get('rule_key') or set_.get('rule_ref') or set_.get('module')}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT ext_access")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE ext_access")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO ext_access")
        conn.execute("RELEASE ext_access")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
