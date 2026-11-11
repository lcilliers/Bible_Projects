"""cfg_cleanup_2465_v1_20261111.py -- escalation #2465: clears the three coherence errors left by the stopped #2412 Ollama triage test.

  enum values  surface_cycle_module = engagementask and surface_subject_kind = verse_lexical, so the 77 ai_call rows of that test (kept, never deleted) carry registered values
  utility      iba/app/lib/engagementask.py retired: moved to iba/app/lib/archive/ (done by the session, not here) and recorded as an inactive cfg_utility row
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/cfg_cleanup_2465_v1_20261111.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2465-CFG-CLEANUP-20261111"
MODULE = "cfg_cleanup_2465_v1_20261111"
ENUMS = [("surface_cycle_module", "engagementask", 5), ("surface_subject_kind", "verse_lexical", 4)]
UTILITIES = [
    ("engagementask", "iba/app/lib/archive/engagementask.py", 1,
     "RETIRED (#2465): the Ollama triage test of #2412 (two closed questions asked of each surface in each verse), stopped at 71 of 662 questions; the researcher ruled against a bulk "
     "Ollama route for the study result (B:127). Kept in archive/; its 77 ai_call rows (module engagementask) stay as history.", 1,
     "retired module, kept in archive/ for reading"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2465: registers the enum values of the stopped #2412 triage test's ai_call rows and "
     f"records the retired module engagementask; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for name, value, ordinal in ENUMS:
        if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, value):
            ops.append(("cfg_enum", "insert", {}, {"name": name, "value": value, "ordinal": ordinal, "inactive": 0}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, set_.get("module") or f"{set_.get('name')}={set_.get('value')}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2465-cfg-cleanup', named=True)}")
    try:
        conn.execute("SAVEPOINT cfg_cleanup")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE cfg_cleanup")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO cfg_cleanup")
        conn.execute("RELEASE cfg_cleanup")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
