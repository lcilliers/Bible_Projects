"""reading_gate_2294_v1_20261025.py -- escalation #2294 (#2286 U4; decision G-a of #2294 v4, outputs/escalation/
2294-reading-gate-decision-v1-20261025.md): the config of the stale and unallocated pair check.

1. cfg_report_section 'surface_mapping' on cluster.validate's report.
2. cluster.validate's description, current only (its dated history is in BUILD.md and the escalations it names).
3. Behaviour rule B:118 surface-mapping-conditions: its enforcement recorded.

The code is lib/surfacemap.py (stale, unallocated, overview, reading_refusal, retire_stale), lib/reading.py open_ and
handlers/cluster.py validate. cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own
archive path). Idempotent.

Usage:
    python iba/app/migration/reading_gate_2294_v1_20261025.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2294-READING-GATE-20261025"
MODULE = "reading_gate_2294_v1_20261025"
SECTION = {"step": "cluster.validate", "ordinal": 3, "section_key": "surface_mapping",
           "heading": "## Surface mapping (#2294)", "toc_label": "Surface mapping", "include": 1, "inactive": 0}
DOES = ("Read-only DB-wide coverage and exception report, persisted every run: unclassified strongs; backfill non-T2 "
        "codes not yet promoted; the two named exception shapes (a cluster with no word; a backfill code with an "
        "active or clustered sibling); and the surface mapping of the M clusters (#2294): stale pairs and partly "
        "mapped clusters are findings, unmapped clusters are counted. Escalates on any finding unless the counts fall "
        "within a prior run's approved baseline (escalation.answered_baseline_for_step); any increase escalates again.")
B118 = ("partially_enforced",
        "iba/app/lib/surfacemap.py: reason per pair, head in session, tail by the API, two-sense flag, anomaly group, "
        "size check (#2293); stale pairs found and retired by Surface-Map.ps1 -Step Apply, counted by "
        "cluster.validate, and reading.open refuses an M home cluster with unallocated or stale pairs (#2294). That "
        "the analytic phase treats an allocation as provisional is delivered as context.")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    if not has("SELECT 1 FROM cfg_report_section WHERE step=? AND section_key=?", SECTION["step"],
               SECTION["section_key"]):
        ops.append(("cfg_report_section", "insert", {}, SECTION))
    if one("SELECT does FROM cfg_step WHERE step='cluster.validate'")[0] != DOES:
        ops.append(("cfg_step", "update", {"step": "cluster.validate"}, {"does": DOES}))
    r = one("SELECT id, enforcement_status, enforced_by FROM cfg_behaviour_rule WHERE class='study_method' AND "
            "rule_key='surface-mapping-conditions'")
    if (r[1], r[2]) != B118:
        ops.append(("cfg_behaviour_rule", "update", {"id": r[0]}, {"enforcement_status": B118[0],
                                                                   "enforced_by": B118[1]}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2294 (#2286 U4): cluster.validate's surface mapping section "
                       f"and description, B:118's enforcement; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run:
        for t, op, where, set_ in ops:
            print(f"  {op:6} {t:20} {where or set_.get('section_key') or set_.get('module')}")
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
