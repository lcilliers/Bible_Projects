"""register_active_app_files_v1_20261021.py -- escalation #2198 / #2200 (element of the IBA app reset,
#2177): the app files in active use that had no cfg_utility row are registered, so the
unregistered-script check in configmaint.validate can be a hard error.

Each file is reached from an active entry point (run.py, an active cfg_step handler, or a PS script
dispatching an active work package). iba/app/lib/narrativegenerate.py and
iba/app/lib/wordregistryspanreport.py, used by the active book-narrative and
word-registry-span-report work packages, are set active again; their NON-COMPLIANT purpose stays
until #2201 fixes them.

Registers itself (inactive, at its own archive path) in the same transaction. Written through
configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/register_active_app_files_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2198-REGISTER-ACTIVE-FILES-20261021"
MODULE = "register_active_app_files_v1_20261021"
CORE = "app core, outside the utility config-density check"
FILES = {
    "iba/app/run.py": ("run", "The dispatcher and run-state machine: cfg_step handler, cfg_on_fail path, run rows."),
    "iba/app/init.py": ("init", "The app bootstrap: config check and load, data tables, STEP preflight, rule delivery."),
    "iba/app/report.py": ("report_word_raw", "The word-raw report, called by handlers/reports.py and its CLI."),
    "iba/app/validation.py": ("validation", "Word/book validation reports, called by handlers/reports.py."),
    "iba/app/handlers/base.py": ("handlers_base", "Handler contract: Ctx, Outcome, ok/fail/escalate, used by every handler."),
    "iba/app/tools/build_debate_report.py": ("build_debate_report", "Step 6 debate report for one hib-continuity passage, run by Debate-Run.ps1."),
    "iba/app/tools/export_tables_csv.py": ("export_tables_csv", "CSV dump of data tables, used by the table-export work package."),
    "iba/app/ps/_lib/Notify.ps1": ("ps_lib_notify", "PS helper library: completion notifications for the PS front doors."),
    "iba/app/ps/CharAnswer.ps1": ("ps_charanswer", "Front door for the char-answers stage (cluster-reading work package)."),
    "iba/app/ps/CharReading.ps1": ("ps_charreading", "Front door for the char-reading stage (cluster-reading work package)."),
    "iba/app/ps/Lexical-Readiness.ps1": ("ps_lexical_readiness", "Front door for lexical.readiness (verse-lexical work package)."),
    "iba/app/ps/RelationalReading.ps1": ("ps_relationalreading", "Front door for lexical.relational (verse-lexical work package)."),
    "iba/app/ps/Run-Stage1Batch.ps1": ("ps_run_stage1batch", "Runs the Stage 1 verse-reading steps over a cluster (verse-lexical work package)."),
    "iba/app/ps/VerseReading.ps1": ("ps_versereading", "Front door for lexical.meaning (verse-lexical work package)."),
}
REACTIVATE = ("iba/app/lib/narrativegenerate.py", "iba/app/lib/wordregistryspanreport.py")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    rows = {r[0]: (r[1], r[2]) for r in conn.execute("SELECT file_path, module, inactive FROM cfg_utility")}
    modules = {r[0] for r in conn.execute("SELECT module FROM cfg_utility")}
    ops = []
    for path, (mod, purpose) in FILES.items():
        if path in rows:
            if rows[path][1] != 0:
                ops.append(("update", {"module": rows[path][0]}, {"inactive": 0}))
            continue
        if mod in modules:
            print(f"module name {mod!r} already taken -- nothing done")
            return 1
        ops.append(("insert", {}, {"module": mod, "file_path": path, "purpose": purpose, "inactive": 0,
                                   "config_exempt": 1, "config_exempt_reason": CORE}))
    for path in REACTIVATE:
        if path in rows and rows[path][1] != 0:
            ops.append(("update", {"module": rows[path][0]}, {"inactive": 0}))
    if MODULE not in modules:
        ops.append(("insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2198/#2200: registers the active app files "
                       f"with no cfg_utility row, through configmaint.apply_logged under run_id "
                       f"{RUN_ID}. inactive=1 once applied."}))
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    if not ops:
        print("already applied -- skipped")
        return 0
    with conn:
        for op, where, set_ in ops:
            apply_logged(conn, RUN_ID, "cfg_utility", op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
