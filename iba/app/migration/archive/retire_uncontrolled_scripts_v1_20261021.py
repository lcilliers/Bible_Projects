"""retire_uncontrolled_scripts_v1_20261021.py -- escalation #2200 (element of the IBA app reset,
#2177): every script not in a utility or module is retired.

Reads outputs/escalation/2200-retire-list-v1-20261021.json (keep + retire lists, plan
outputs/escalation/2200-retire-uncontrolled-scripts-plan-v1-20261021.md). For each retired file,
moved into its folder's archive/ by git mv: its cfg_utility row is pointed at the archive path and
set inactive, or a row is added inactive. The kept, in-use scripts get an active row. The
ps_script of an inactive work package and the handler of an inactive cfg_step that name a moved
file are pointed at its archive path. The researcher's approval gates any later use of a retired
script (.claude/hooks/gate_retired_script.py).

Registers itself (inactive, at its own archive path) in the same transaction. Written through
configmaint.apply_logged(). Idempotent: a row already in the target state is skipped. One
transaction.

Usage:
    python iba/app/migration/retire_uncontrolled_scripts_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import re
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2200-RETIRE-SCRIPTS-20261021"
LIST = ROOT / "outputs/escalation/2200-retire-list-v1-20261021.json"
MODULE = "retire_uncontrolled_scripts_v1_20261021"
EXEMPT = "retired script (#2200): kept for reference only; use needs the researcher's approval"
KEEP_PURPOSE = {
    "iba/app/ps/Start-Iba.ps1": "Session bootstrap: runs iba.app.init (config check, load, tables, STEP preflight, rule delivery).",
    "iba/app/ps/Behaviour.ps1": "Front end of lib/behaviour.py: lists cfg_behaviour_class / cfg_behaviour_rule.",
    "iba/app/ps/Debate-Run.ps1": "Orchestrates the debate pipeline steps (operations-ingest) using lib/debaterun.py readiness checks.",
    "scripts/backup_db_to_nas.py": "Daily NAS backup of bible_research.db and iba.db, run by Windows scheduled tasks (cfg_setting backup.nas_db_backup_schedule).",
    "scripts/backup_watchdog.ps1": "Watchdog over the NAS backup jobs, run by the scheduled task 'BibleResearch Backup Watchdog'.",
    "scripts/mirror_to_nas.ps1": "Daily full project mirror to the NAS, run by the scheduled task 'BibleResearch Full Mirror to NAS'.",
    "scripts/notify_backup_alert.ps1": "Alert sink for the NAS backup jobs and the watchdog (backup.alerting_policy).",
    "scripts/install_backup_watchdog_task.ps1": "Installs the backup watchdog scheduled task.",
    "scripts/apply_session_patch.py": "Applies reviewed PROSE / CATALOGUE_POPULATION patch files to bible_research.db (cfg_write_grant writer apply_session_patch).",
}


def slug(rel: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", rel.rsplit(".", 1)[0].lower()).strip("_")


def plan(conn) -> list[tuple]:
    data = json.loads(LIST.read_text(encoding="utf8"))
    rows = {r[0]: (r[1], r[2]) for r in conn.execute("SELECT file_path, module, inactive FROM cfg_utility")}
    modules = {r[0] for r in conn.execute("SELECT module FROM cfg_utility")}
    ops = []
    for item in data["retire"]:
        old, new = item["from"], item["to"]
        if new in rows:
            if rows[new][1] != 1:
                ops.append(("cfg_utility", "update", {"module": rows[new][0]}, {"inactive": 1}))
            continue
        if old in rows:
            ops.append(("cfg_utility", "update", {"module": rows[old][0]},
                        {"file_path": new, "inactive": 1}))
            continue
        mod = slug(new)
        while mod in modules:
            mod += "_r"
        modules.add(mod)
        ops.append(("cfg_utility", "insert", {}, {
            "module": mod, "file_path": new, "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": EXEMPT,
            "purpose": f"Retired (#2200): not in a utility or module. Was {old}."}))
    for rel in data["keep"]:
        if rel in rows:
            if rows[rel][1] != 0:
                ops.append(("cfg_utility", "update", {"module": rows[rel][0]}, {"inactive": 0}))
            continue
        mod = slug(rel)
        while mod in modules:
            mod += "_k"
        modules.add(mod)
        ops.append(("cfg_utility", "insert", {}, {
            "module": mod, "file_path": rel, "inactive": 0, "config_exempt": 1,
            "config_exempt_reason": "operational script outside the dispatcher (#2200)",
            "purpose": KEEP_PURPOSE[rel]}))
    moved = {i["from"]: i["to"] for i in data["retire"]}
    for name, ps in conn.execute("SELECT name, ps_script FROM cfg_work_package WHERE inactive=1"):
        p = (ps or "").replace("\\", "/")
        if p in moved:
            ops.append(("cfg_work_package", "update", {"name": name}, {"ps_script": moved[p]}))
    for wp, step, handler in conn.execute(
            "SELECT work_package, step, handler FROM cfg_step WHERE inactive=1 AND handler IS NOT NULL"):
        mod_path = handler.split(":")[0].replace(".", "/") + ".py"
        if mod_path in moved:
            new_mod = moved[mod_path][:-3].replace("/", ".")
            ops.append(("cfg_step", "update", {"work_package": wp, "step": step},
                        {"handler": new_mod + ":" + handler.split(":", 1)[1]}))
    self_path = f"iba/app/migration/archive/{MODULE}.py"
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": self_path, "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
                                    "configmaint.apply_logged, same class as the other Developer "
                                    "Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2200: retires every script not in a utility "
                       f"or module, through configmaint.apply_logged under run_id {RUN_ID}. "
                       f"inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    counts = {}
    for t, op, _, _ in ops:
        counts[f"{t} {op}"] = counts.get(f"{t} {op}", 0) + 1
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s): {counts}")
        return 0
    if not ops:
        print("already applied -- skipped")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail): {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
