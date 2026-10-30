"""analysis_phase_1_2329_v2_20261030.py -- escalation #2329: the specification of Analysis_phase_1 is v5.

Spec 4.2 gained the before and after parts, the typed party and the meaning data on the sheet
(outputs/escalation/2318-analysis-phase-1-specification-v5-20261030.md); v4 is in outputs/escalation/archive/. The ten cfg_method_rule rows
whose source_doc named v4 name v5. cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/analysis_phase_1_2329_v2_20261030.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2329-SPEC-V5-SOURCE-DOC-20261030"
MODULE = "analysis_phase_1_2329_v2_20261030"
OLD = "2318-analysis-phase-1-specification-v4-20261027"
NEW = "2318-analysis-phase-1-specification-v5-20261030"


def plan(conn) -> list[tuple]:
    ops = [("cfg_method_rule", "update", {"id": i}, {"source_doc": d.replace(OLD, NEW)})
           for i, d in conn.execute("SELECT id, source_doc FROM cfg_method_rule WHERE source_doc LIKE ?", (f"%{OLD}%",))]
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
                                    "as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2329: the source_doc of the Analysis_phase_1 method rules names specification "
                       f"v5; run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID} is in cfg_change_detail)")
        return 0
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s): " + ", ".join(f"{t} {op}" for t, op, _, _ in ops))
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
