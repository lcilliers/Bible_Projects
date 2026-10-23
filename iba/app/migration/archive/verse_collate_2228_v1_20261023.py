"""verse_collate_2228_v1_20261023.py -- escalation #2228 tools 3-5, collating what is known and the gaps for a
scope, as config (design outputs/escalation/2228-verse-collate-design-v1-20261023.md).

- work package verse-collate (iba/app/ps/Verse-Collate.ps1), step verse_collate.collate and its 'refused' route;
  no write grant (it writes no table).
- settings verse_collate.output_dir and verse_collate.max_seconds; module verse_collate.
- an index on ib_node.verse_reference (cfg_index, and created), so observations are found by verse.
- cfg_utility for the three new files and this migration.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path)
in the same transaction. Idempotent.

Usage:
    python iba/app/migration/verse_collate_2228_v1_20261023.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2228-VERSE-COLLATE-20261023"
MODULE = "verse_collate_2228_v1_20261023"
WP = "verse-collate"
STEP = "verse_collate.collate"
DOES = ("what is known and what is missing for a scope: the scope resolved as verse_scope.resolve does (its guard "
        "applies), then per verse its text, inner-being words, observations, strand hits, claims and their tellings, "
        "citing blocks, matching open items and the cluster-file lines naming it; the lexicon per strong; the gaps "
        "per verse (read-only) -- see lib/versecollate.py (escalation #2228)")
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
SETTINGS = [
    ("verse_collate.output_dir", "outputs/verse-collate",
     "where Verse-Collate.ps1 writes <label>-<YYYYMMDD>.json (the record) and .md (the summary) (escalation #2228)"),
    ("verse_collate.max_seconds", 120,
     "time guard on collating: past this many seconds the run is refused, to be reformed to a narrower scope "
     "(researcher 2026-10-23, #2228)"),
]
UTILITIES = [
    ("versecollate", "iba/app/lib/versecollate.py", "versecollate.py -- what is known and what is missing for a scope "
     "(escalation #2228 tools 3-5): collate() per verse from every table source and the cluster reading index, the "
     "lexicon once per strong, and the gaps; markdown() the summary. Read-only.", 0, None),
    ("handlers_versecollate", "iba/app/handlers/versecollate.py", "handlers/versecollate.py -- the run.py handler for "
     "work package verse-collate (Verse-Collate.ps1); writes the JSON and .md under verse_collate.output_dir; the "
     "logic is in lib/versecollate.py (escalation #2228).", 0, None),
    ("Verse-Collate.ps1", "iba/app/ps/Verse-Collate.ps1", "PS entry point for collating a scope (escalation #2228); "
     "dispatches through run.py, work package verse-collate.", 1,
     "thin wrapper; config is read by the handler through run.py"),
]
INDEX = ("ib_node", "idx_ib_node_verse_reference", "verse_reference")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='verse_collate'"):
        n = conn.execute("SELECT coalesce(max(ordinal), 0) + 1 FROM cfg_enum WHERE name='config_module'").fetchone()[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "config_module", "value": "verse_collate", "ordinal": n,
                                               "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Verse-Collate.ps1",
                                                       "runs_over": "none", "chained": 0, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_step WHERE step=?", STEP):
        ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": 0, "step": STEP,
                                               "handler": "iba.app.handlers.versecollate:collate", "scope": "none",
                                               "does": DOES, "inactive": 0, "kind": "utility"}))
    if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", STEP):
        ops.append(("cfg_on_fail", "insert", {}, {"step": STEP, "condition": "refused", "path": "report-continue",
                                                  "resolver": None, "message": REFUSED, "route": "terminal",
                                                  "inactive": 0}))
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "module": "verse_collate",
                                                      "inactive": 0, "use": use}))
    if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=?", INDEX[0], INDEX[1]):
        ops.append(("cfg_index", "insert", {}, {"table_name": INDEX[0], "name": INDEX[1], "col": INDEX[2], "ordinal": 0}))
    for module, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose,
                                                      "inactive": 0, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0,
                                                      "crash_escalation_note": None}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2228 tools 3-5: work package verse-collate, its step, route "
                       f"and settings, the ib_node verse index, the three new files; run_id {RUN_ID}. inactive=1 once "
                       f"applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    has_index = conn.execute("SELECT 1 FROM sqlite_master WHERE type='index' AND name=?", (INDEX[1],)).fetchone()
    if a.dry_run or (not ops and has_index):
        print(f"{'DRY RUN -- ' if a.dry_run else 'already applied -- '}{len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        if not has_index:
            conn.execute(f'CREATE INDEX "{INDEX[1]}" ON "{INDEX[0]}" ("{INDEX[2]}")')
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail); index {INDEX[1]} "
          f"{'present' if has_index else 'created'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
