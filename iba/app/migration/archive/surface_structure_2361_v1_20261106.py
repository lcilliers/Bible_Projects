"""surface_structure_2361_v1_20261106.py -- escalation #2361, stage 2: registers module 2 of 5, surface-structure.

  config_module  new value `structure`
  settings       structure.min_base_length 3, min_computed_base_length 4, min_starts_with_length 3, possessive_pattern, tested_form
                 (the values that reproduced the recorded control of 2026-11-04 exactly; see lib/surfacestructure.py)
  cfg_base_construct.result_kind  new column (ALTER TABLE + cfg_column + enum): what a hit of the construct is recorded as in
                 surface_derivation.kind. The 79 rows are set from the rule the loader used (a negating construct is a lead_opposite, another
                 prefix a lead_other, an ending that only inflects an inflection, any other word form a derivation), so the rule is data
  work package   surface-structure, entry Surface-Structure.ps1, steps structure.status, structure.match, structure.show, their
                 'refused' conditions, the write grant of structure.match on surface_derivation, the utility rows
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.
Writes no evidence row: the first run of structure.match does (it supersedes the 152 loaded sibling rows with the finer evidence that
names the construct, and changes nothing else).

Usage:
    python iba/app/migration/surface_structure_2361_v1_20261106.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2361-SURFACE-STRUCTURE-20261106"
MODULE = "surface_structure_2361_v1_20261106"
WP = "surface-structure"
H = "iba.app.handlers.surfacestructure"
SETTINGS = [
    ("structure.min_base_length", 3, "the shortest base a construct may give (module 2 of 5, structure, #2361): a stem plus the added text of fewer letters is not "
     "a base (so doing is not matched to do). 3 reproduced the recorded control of 2026-11-04 exactly"),
    ("structure.min_computed_base_length", 4, "the shortest computed base two unmatched words may share to be siblings (#2361): shorter shared stems join "
     "unrelated words (drive and dry). 4 reproduced the 47 recorded sibling groups exactly"),
    ("structure.min_starts_with_length", 3, "the fewest letters an unmatched word needs for the words that begin with it to be listed as starts-with leads (#2361)"),
    ("structure.possessive_pattern", "[\u2019']s$", "a regular expression for the possessive ending removed when a surface is normalised (#2361); a possessive "
     "form is not tested itself and takes the result of its normalised twin"),
    ("structure.tested_form", "word", "the value of surface_term.form that the structure module tests (#2361): a phrase is not tested and is assigned last"),
]
RESULT_KINDS = ["inflection", "derivation", "lead_opposite", "lead_other"]
INFLECTION_KINDS = ("plural", "past tense", "present participle", "comparative", "superlative")
COL_USE = ("Module 2 of 5, structure (#2361): what a hit of this construct is recorded as in surface_derivation.kind: inflection (only the ending changes: "
           "plural, tense, participle, comparative, superlative), derivation (another word form of the same root: agent, adverb, adjective, noun), "
           "lead_opposite (a negating prefix or suffix: a possible opposite, never a base), lead_other (another prefix kept as a lead). Read by the "
           "structure module; derived from direction and kind when the rules were loaded")
STEPS = [
    ("structure.status", "status", "operations", "how the structure of the surfaces of collection a stands and how far the evidence rows in surface_derivation are "
     "from it (read-only) -- see lib/surfacestructure.py (escalation #2361)"),
    ("structure.match", "match", "operations", "match every surface of collection a to a base by the shape of the word and write the difference to "
     "surface_derivation: new evidence rows added, rows no longer produced set to deleted; -Check previews; a second run with the same inputs changes nothing "
     "-- see lib/surfacestructure.py (escalation #2361)"),
    ("structure.show", "show", "utility", "one surface's structure record and its evidence rows, with -Surface (read-only) -- see lib/surfacestructure.py "
     "(escalation #2361)"),
]
REFUSED = "refused, nothing written -- a setting or a surface is missing, or -Surface is not a surface of collection a (a usage outcome, not recorded as an escalation)"
UTILITIES = [
    ("surfacestructure", "iba/app/lib/surfacestructure.py", 0, "surfacestructure.py -- module 2 of 5 of the surface cycle: matching a surface to a base by the "
     "shape of the word, rebuilt from the recorded control of 2026-11-04 and reproducing it exactly (escalation #2361).", 0, None),
    ("handlers_surfacestructure", "iba/app/handlers/surfacestructure.py", 0, "handlers/surfacestructure.py -- the run.py handlers for work package "
     "surface-structure (Surface-Structure.ps1, escalation #2361).", 0, None),
    ("Surface-Structure.ps1", "iba/app/ps/Surface-Structure.ps1", 0, "PS entry point for module 2 of 5 of the surface cycle (escalation #2361): Status, Match, "
     "Show; dispatches through run.py, work package surface-structure.", 1, "thin wrapper; config is read by the handlers through run.py"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2361 stage 2: registers module surface-structure, its settings "
     f"and the result_kind column of cfg_base_construct; run_id {RUN_ID}.", 1, "one-off migration script -- writes cfg_* rows through "
     "configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def result_kind(c) -> str:
    if c["direction"] == "opposite":
        return "lead_opposite"
    if c["direction"] == "candidate":
        return "lead_other"
    return "inflection" if c["kind"].startswith(INFLECTION_KINDS) else "derivation"


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='structure'"):
        nxt = conn.execute("SELECT COALESCE(MAX(ordinal),0)+1 FROM cfg_enum WHERE name='config_module'").fetchone()[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "config_module", "value": "structure", "ordinal": nxt, "inactive": 0}))
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": "structure", "inactive": 0}))
    for i, v in enumerate(RESULT_KINDS):
        if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", "cfg_base_construct.result_kind", v):
            ops.append(("cfg_enum", "insert", {}, {"name": "cfg_base_construct.result_kind", "value": v, "ordinal": i, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_column WHERE table_name='cfg_base_construct' AND name='result_kind'"):
        top = conn.execute("SELECT MAX(ordinal) FROM cfg_column WHERE table_name='cfg_base_construct'").fetchone()[0]
        ops.append(("cfg_column", "insert", {}, {
            "database": "iba", "table_name": "cfg_base_construct", "name": "result_kind", "ordinal": top + 1, "type": "TEXT", "is_pk": 0, "notnull": 0,
            "is_unique": 0, "dflt": None, "fk": None, "use": COL_USE, "expectation": "enum.cfg_base_construct.result_kind",
            "source": "escalation #2361 stage 2", "filled_by": f"iba/app/migration/archive/{MODULE}.py for the 79 recorded rules; a new rule by configmaint.propose",
            "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Surface-Structure.ps1", "runs_over": "none", "chained": 0,
                                                       "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for i, (step, fn, kind, does) in enumerate(STEPS):
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": i, "step": step, "handler": f"{H}:{fn}", "scope": "none", "does": does,
                                                   "inactive": 0, "kind": kind}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", step):
            ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": "refused", "path": "report-continue", "resolver": None, "message": REFUSED,
                                                      "route": "terminal", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_write_grant WHERE writer='structure.match' AND table_name='surface_derivation' AND database='iba'"):
        ops.append(("cfg_write_grant", "insert", {}, {"writer": "structure.match", "table_name": "surface_derivation", "database": "iba", "inactive": 0}))
    for module, path, inactive, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def kinds_to_set(conn):
    have_col = "result_kind" in {r[1] for r in conn.execute("PRAGMA table_info(cfg_base_construct)")}
    out = []
    for r in conn.execute("SELECT id, kind, direction" + (", result_kind" if have_col else "") + " FROM cfg_base_construct").fetchall():
        c = {"id": r[0], "kind": r[1], "direction": r[2]}
        want = result_kind(c)
        if not have_col or r[3] != want:
            out.append((r[0], want))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    kinds = kinds_to_set(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s), {len(kinds)} construct(s) to give a result_kind")
        return 0
    if not ops and not kinds:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2361-structure', named=True)}")
    try:
        conn.execute("SAVEPOINT surface_structure")
        if "result_kind" not in {r[1] for r in conn.execute("PRAGMA table_info(cfg_base_construct)")}:
            conn.execute("ALTER TABLE cfg_base_construct ADD COLUMN result_kind TEXT")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for cid, kind in kinds_to_set(conn):
            apply_logged(conn, RUN_ID, "cfg_base_construct", "update", {"id": cid}, {"result_kind": kind})
        left = conn.execute("SELECT count(*) FROM cfg_base_construct WHERE result_kind IS NULL").fetchone()[0]
        if left:
            raise RuntimeError(f"{left} construct(s) without a result_kind")
        conn.execute("RELEASE surface_structure")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_structure")
        conn.execute("RELEASE surface_structure")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); result_kind set on {len(kinds)} construct(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
