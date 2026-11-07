"""surface_group_entity_2372_v1_20261107.py -- escalation #2372 (researcher, 2026-11-07: "use entity throughout - the use of the
term being is confusing. fix it in the configs and in the data").

The group of the things that exist (humans, plants and animals, God in all forms, unseen powers, parts of these) was told to the
model as `entity` and stored as `being` (cfg_setting surface_judge.group_stored_as, #2354 v3). It is now `entity` everywhere:

  config (through configmaint.apply_logged, Developer Mode migration):
    - cfg_enum surface_term.surface_group: the value being becomes entity (same ordinal);
    - cfg_setting surface_judge.group_stored_as: the entity -> being map is emptied (the stored name is the name given);
    - cfg_setting surfaces.scope_groups: collection b is ["entity"];
    - cfg_column use of iba.surface_term.surface_group and iba.surface_term.base_state: the word being, where it names the group,
      is entity;
    - cfg_utility: this migration is registered.
  data (one transaction with the config):
    - surface_term.surface_group being -> entity (one surface_event set_group per surface, the revision record);
    - ai_call.result being -> entity for the group judgements (the stored group of each call); ai_call.answer, the model's own
      words of earlier prompt versions, is not changed.
  A before-image of every changed row is written to outputs/escalation/2372-group-before-image-v1-20261107.csv first.

Idempotent: with nothing left to change it writes nothing. Usage:
    python iba/app/migration/surface_group_entity_2372_v1_20261107.py [--db PATH] [--dry-run]
"""
import argparse
import csv
import datetime
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
BEFORE_IMAGE = ROOT / "outputs" / "escalation" / "2372-group-before-image-v1-20261107.csv"
RUN_ID = "DEVMODE-2372-SURFACE-GROUP-ENTITY-20261107"
MODULE = "surface_group_entity_2372_v1_20261107"
STORED_USE = ("the groups whose name given to the model differs from the group stored: {name given to the model: group stored}, "
              "each key one of surface_judge.groups. Empty since #2372: the groups are stored under the names given to the model")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan_cfg(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if has("SELECT 1 FROM cfg_enum WHERE name='surface_term.surface_group' AND value='being'"):
        if has("SELECT 1 FROM cfg_enum WHERE name='surface_term.surface_group' AND value='entity'"):
            raise SystemExit("REFUSED, nothing written: cfg_enum surface_term.surface_group holds both being and entity")
        ops.append(("cfg_enum", "update", {"name": "surface_term.surface_group", "value": "being"}, {"value": "entity"}))
    row = conn.execute("SELECT value FROM cfg_setting WHERE key='surface_judge.group_stored_as'").fetchone()
    if row is None:
        raise SystemExit("REFUSED, nothing written: cfg_setting surface_judge.group_stored_as is missing")
    if json.loads(row[0]) != {}:
        ops.append(("cfg_setting", "update", {"key": "surface_judge.group_stored_as"}, {"value": "{}", "use": STORED_USE}))
    row = conn.execute("SELECT value FROM cfg_setting WHERE key='surfaces.scope_groups'").fetchone()
    scope = json.loads(row[0])
    if scope.get("b") != ["entity"]:
        if scope.get("b") != ["being"]:
            raise SystemExit(f"REFUSED, nothing written: surfaces.scope_groups b is {scope.get('b')!r}, expected ['being']")
        ops.append(("cfg_setting", "update", {"key": "surfaces.scope_groups"}, {"value": json.dumps(dict(scope, b=["entity"]))}))
    for col, old, rep in (("surface_group", "being is the entities (collection b)", "entity is the entities (collection b)"),
                          ("base_state", "(the group is being or other,", "(the group is entity or other,")):
        r = conn.execute("SELECT use FROM cfg_column WHERE database='iba' AND table_name='surface_term' AND name=?", (col,)).fetchone()
        if old in r[0]:
            ops.append(("cfg_column", "update", {"database": "iba", "table_name": "surface_term", "name": col}, {"use": r[0].replace(old, rep)}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py", "inactive": 0,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2372: the surface group being is entity in config and data; run_id {RUN_ID}.",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def data_rows(conn):
    terms = conn.execute("SELECT id, surface, surface_group FROM surface_term WHERE surface_group='being' ORDER BY id").fetchall()
    calls = conn.execute("SELECT id, subject_id, result FROM ai_call WHERE module='group' AND step='group' AND result='being' ORDER BY id").fetchall()
    return terms, calls


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan_cfg(conn)
    terms, calls = data_rows(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s), {len(terms)} surface_term row(s), {len(calls)} ai_call row(s)")
        for t, op, where, set_ in ops:
            print(f"  {t} {op} {where or set_.get('module')}")
        return 0
    if not ops and not terms and not calls:
        print("already applied: nothing changed")
        return 0
    if terms or calls:
        BEFORE_IMAGE.parent.mkdir(parents=True, exist_ok=True)
        with open(BEFORE_IMAGE, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["table", "id", "subject_or_surface", "column", "value_before"])
            for r in terms:
                w.writerow(["surface_term", r[0], r[1], "surface_group", r[2]])
            for r in calls:
                w.writerow(["ai_call", r[0], r[1], "result", r[2]])
    now = _now()
    try:
        conn.execute("SAVEPOINT sg_entity")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for r in terms:
            conn.execute("UPDATE surface_term SET surface_group='entity', updated_at=?, run_id=? WHERE id=? AND surface_group='being'", (now, RUN_ID, r[0]))
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES ('surface_term',?,'set_group','surface_group','being','entity','researcher instruction 2026-11-07 (#2372)',"
                         "'the group of entities is named entity throughout; the stored name being is retired',?, 'migration')", (r[0], RUN_ID))
        for r in calls:
            conn.execute("UPDATE ai_call SET result='entity', updated_at=? WHERE id=? AND result='being'", (now, r[0]))
        conn.execute("RELEASE sg_entity")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO sg_entity")
        conn.execute("RELEASE sg_entity")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s), {len(terms)} surface_term row(s), {len(calls)} ai_call row(s); "
          f"before-image {BEFORE_IMAGE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
