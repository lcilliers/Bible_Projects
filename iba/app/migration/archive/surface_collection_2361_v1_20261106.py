"""surface_collection_2361_v1_20261106.py -- escalation #2361, stage 5: registers module 5 of 5, collection-build.

  work package   collection-build, entry Collection-Build.ps1, steps collection.status, collection.links, collection.show, collection.export,
                 collection.set, collection.merge, their 'refused' conditions, the write grants (collection.links -> collection_link, surface_term;
                 collection.set -> collection, surface_event; collection.merge -> collection, collection_link, surface_event), the utility rows
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.
Records the 18 associated-true pairs the prototype left out while the researcher reviewed (2026-11-05) as REMOVED links (deleted = 1, no
superseded_by_id, reason says so): the rule respects a removal, so a Links run does not link them. Refuses, writing nothing, unless it finds exactly 18.
Writes no other collection row: the stored links equal what the judgements decide, so the first Links run changes nothing.

Usage:
    python iba/app/migration/surface_collection_2361_v1_20261106.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2361-SURFACE-COLLECTION-20261106"
MODULE = "surface_collection_2361_v1_20261106"
WP = "collection-build"
H = "iba.app.handlers.collectionbuild"
STEPS = [
    ("collection.status", "status", "utility", "how the stored members of the collections stand against what the AI judgements decide (read-only) -- see lib/collectionbuild.py (escalation #2361)"),
    ("collection.links", "links", "operations", "decide the members of each collection from the AI judgements and write the difference: new links, tier changes (old row deleted, superseded_by), shared flags, word states; -Check previews, -Associate links the associated pairs the prototype left out -- see lib/collectionbuild.py (escalation #2361)"),
    ("collection.show", "show", "utility", "one collection with its members by tier, with -Collection (read-only) -- see lib/collectionbuild.py (escalation #2361)"),
    ("collection.export", "export", "utility", "write a CSV of the collections and their members from the tables to the exports folder, with -Name (a view, never an input) -- see lib/collectionbuild.py (escalation #2361)"),
    ("collection.set", "set_status", "operations", "set the status of a collection (indicative, confirmed, retired) on the researcher's instruction, with -Reason and a surface_event -- see lib/collectionbuild.py (escalation #2361)"),
    ("collection.merge", "merge", "operations", "merge one collection into another on the researcher's instruction, with -Reason and a surface_event; links move or are deleted with superseded_by -- see lib/collectionbuild.py (escalation #2361)"),
]
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
GRANTS = [("collection.links", "collection_link"), ("collection.links", "surface_term"), ("collection.set", "collection"), ("collection.set", "surface_event"),
          ("collection.merge", "collection"), ("collection.merge", "collection_link"), ("collection.merge", "surface_event")]
UTILITIES = [
    ("collectionbuild", "iba/app/lib/collectionbuild.py", 0, "collectionbuild.py -- module 5 of 5 of the surface cycle: the members of each collection decided from the AI "
     "judgements, reproducing the five recorded runs of 2026-11-05 (escalation #2361).", 1, "the rule has no tunable value: the tiers follow from the recorded relations of the judge prompts"),
    ("handlers_collectionbuild", "iba/app/handlers/collectionbuild.py", 0, "handlers/collectionbuild.py -- the run.py handlers for work package collection-build "
     "(Collection-Build.ps1, escalation #2361).", 1, "thin adapter over lib/collectionbuild.py; the exports folder is read with Cfg.setting"),
    ("Collection-Build.ps1", "iba/app/ps/Collection-Build.ps1", 0, "PS entry point for module 5 of 5 of the surface cycle (escalation #2361): Status, Links, Show, Export, Set, Merge; "
     "dispatches through run.py, work package collection-build.", 1, "thin wrapper; config is read by the handlers through run.py"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2361 stage 5: registers module collection-build; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Collection-Build.ps1", "runs_over": "none", "chained": 0,
                                                       "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for i, (step, fn, kind, does) in enumerate(STEPS):
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": i, "step": step, "handler": f"{H}:{fn}", "scope": "none", "does": does,
                                                   "inactive": 0, "kind": kind}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", step):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": "refused", "path": "report-continue", "resolver": None, "message": REFUSED,
                                                      "route": "terminal", "inactive": 0}))
    for w, t in GRANTS:
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", w, t):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": w, "table_name": t, "database": "iba", "inactive": 0}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def withheld(conn):
    """The associated pairs the judgements decide that have no link row at all: the 18 the prototype left out."""
    from iba.app.lib import collectionbuild as cb
    have = cb.stored(conn)
    gone = cb.removed_pairs(conn)
    decided = cb.decide(cb.load(conn))
    return [(k, v[1]) for k, v in sorted(decided.items()) if v[0] == "associated" and k not in have and k not in gone]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    wh = withheld(conn)
    if wh and len(wh) != 18:
        print(f"REFUSED, nothing written: found {len(wh)} associated pairs the prototype left out, expected 18")
        return 2
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s); {len(wh)} removed link(s) to record")
        return 0
    if not ops and not wh:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2361-collection', named=True)}")
    try:
        conn.execute("SAVEPOINT surface_collection")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for (col, term), call in wh:
            conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, ai_call_id, reason, run_id, created_by, deleted, load_ref) VALUES "
                         "(?,?,'associated',?, ?, ?, 'migration', 1, ?)",
                         (col, term, call, "left out by the prototype of 2026-11-05: associated by the judge, not linked while the researcher reviewed", RUN_ID,
                          f"withheld:{col}:{term}"))
        conn.execute("RELEASE surface_collection")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_collection")
        conn.execute("RELEASE surface_collection")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); {len(wh)} removed link(s) recorded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
