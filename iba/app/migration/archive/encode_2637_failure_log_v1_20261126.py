"""encode_2637_failure_log_v1_20261126.py -- escalation #2637, plan v3 X5 and X8 (outputs/escalation/2637-build-plan-v3-20261126.md).

Researcher 2026-11-26: "adequate debugging and error trapping to allow for learning and fixing the code before the next time that it runs".
The read and record steps of the layered reading had no `refused` row in cfg_on_fail, so every refusal of an answer, and every message
that only named the next command, fell to report-stop and raised an escalation (68 since 2026-11-08; catalogue K7,
outputs/escalation/2637-known-failures-catalogue-v1-20261126.md). This migration:
  cfg_table / cfg_column / cfg_index  read_failure: one row per refusal or crash of a read or record command, kept for learning
  cfg_enum           read_failure_kind: refused, crash
  cfg_on_fail        a `refused` row for each read/record step of the loop: report-continue, kept in read_failure, no escalation
  cfg_write_grant    each of those steps may write read_failure
  cfg_utility        this migration's own row
then creates the table from config (lib/db.build_data_tables). Written through configmaint.apply_logged. Named snapshot before a live
apply; after the live apply the file archives itself (configmaint.archive_migration). Idempotent.
Usage: python iba/app/migration/encode_2637_failure_log_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2637-FAILURELOG-20261126"
MODULE = "encode_2637_failure_log_v1_20261126"
SRC = "escalation #2637, plan v3 X8 (outputs/escalation/2637-build-plan-v3-20261126.md)"
BY = "iba/app/handlers/collectionbuild.py (_refused, on every refusal or crash of a read or record command)"
TABLE = ("read_failure", "one row per refusal or crash of a read or record command",
         "#2637 X8: what a read or record command refused or where it crashed, kept for learning, so that a failure seen once is fixed in the code "
         "before the next run; the cycle view and the run audit read it. A refusal is a usage outcome (cfg_on_fail refused, report-continue) and "
         "raises no escalation; a crash still raises one (run.py).")
COLUMNS = [  # name, type, pk, notnull, dflt, fk, use, expectation
    ("id", "INTEGER", 1, 1, None, None, "surrogate PK", None),
    ("run_id", "TEXT", 0, 1, None, None, "the run of the command that failed", None),
    ("step", "TEXT", 0, 1, None, None, "the step of the command (collection.read_words, collection.record_elements, ...)", None),
    ("collection", "TEXT", 0, 0, None, None, "the collection named by the command or its answer file", None),
    ("subgroup", "TEXT", 0, 0, None, None, "the subgroup named by the command or its answer file; NULL for a collection-level row (3.2)", None),
    ("kind", "TEXT", 0, 1, None, None, "refused (the command checked its input and wrote nothing) or crash (an exception the command did not route)", "enum.read_failure_kind"),
    ("file", "TEXT", 0, 0, None, None, "the answer file a record command was given, as given", None),
    ("problems", "TEXT", 0, 1, None, None, "the full message: every problem the command listed, or the exception and its traceback", None),
    ("rule_keys", "TEXT", 0, 0, None, None, "the rule keys the message names (B:nn, RS-08, RW-04, ...), comma-separated, for the count of failures by rule", None),
    ("created_at", "TEXT", 0, 1, "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))", None, "when (ISO-8601 UTC)", None),
]
INDEX = ("ix_read_failure_scope", "collection,subgroup,step")
KINDS = ["refused", "crash"]
STEPS = ["collection.layer_next", "collection.read_words", "collection.record_words", "collection.read_senses", "collection.record_senses",
         "collection.read_enrichment", "collection.record_enrichment", "collection.read_structure", "collection.record_structure",
         "collection.read_sweep", "collection.record_sweep", "collection.read_evidence", "collection.record_evidence",
         "collection.read_elements", "collection.record_elements", "collection.read_behaviours", "collection.record_behaviours",
         "collection.release_dead_traces", "collection.sweep_superseded"]
MESSAGE = ("refused, nothing written -- the reason follows (a usage outcome kept in read_failure for learning, not recorded as an escalation; "
           "#2637)")


def plan(conn):
    ops = []
    if not conn.execute("SELECT 1 FROM cfg_table WHERE name=?", (TABLE[0],)).fetchone():
        ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": TABLE[0], "grain": TABLE[1], "use": TABLE[2], "inactive": 0, "category": "data"}))
    for k, (name, typ, pk, nn, dflt, fk, use, exp) in enumerate(COLUMNS):
        if not conn.execute("SELECT 1 FROM cfg_column WHERE table_name=? AND name=?", (TABLE[0], name)).fetchone():
            ops.append(("cfg_column", "insert", {}, {"database": "iba", "table_name": TABLE[0], "name": name, "ordinal": k, "type": typ, "is_pk": pk,
                                                     "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use, "expectation": exp,
                                                     "source": SRC, "filled_by": BY, "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_index WHERE table_name=? AND name=?", (TABLE[0], INDEX[0])).fetchone():
        for k, col in enumerate(INDEX[1].split(",")):
            ops.append(("cfg_index", "insert", {}, {"table_name": TABLE[0], "name": INDEX[0], "col": col, "ordinal": k, "partial_where": None}))
    for k, v in enumerate(KINDS):
        if not conn.execute("SELECT 1 FROM cfg_enum WHERE name='read_failure_kind' AND value=?", (v,)).fetchone():
            ops.append(("cfg_enum", "insert", {}, {"name": "read_failure_kind", "value": v, "ordinal": k, "inactive": 0}))
    for st in STEPS:
        if not conn.execute("SELECT 1 FROM cfg_step WHERE step=?", (st,)).fetchone():
            raise SystemExit(f"cfg_step {st} is not registered: the migration names a step that does not exist")
        if not conn.execute("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", (st,)).fetchone():
            ops.append(("cfg_on_fail", "insert", {}, {"step": st, "condition": "refused", "path": "report-continue", "resolver": None,
                                                      "message": MESSAGE, "route": "terminal", "inactive": 0}))
        if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", (st, TABLE[0])).fetchone():
            ops.append(("cfg_write_grant", "insert", {}, {"writer": st, "table_name": TABLE[0], "database": "iba", "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of #2637 X5/X8: read_failure registered and built, refused routed to report-continue for the read and record steps",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    live = pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or {k: set_[k] for k in list(set_)[:3]})
        return 0
    if live and not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2637-failurelog-apply', named=True)}")
    try:
        conn.execute("SAVEPOINT rel")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE rel")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO rel")
        conn.execute("RELEASE rel")
        raise
    from iba.app.lib.db import table_ddl
    create_sql, index_sql = table_ddl(Cfg(pathlib.Path(a.db)), TABLE[0])
    conn.execute(create_sql.replace("CREATE TABLE ", "CREATE TABLE IF NOT EXISTS ", 1))
    for sql in index_sql:
        conn.execute(sql.replace("CREATE INDEX ", "CREATE INDEX IF NOT EXISTS ", 1))
    conn.commit()
    print(f"applied (run {RUN_ID}): {len(ops)} write(s); table {TABLE[0]} built")
    if live:
        new = archive_migration(conn, RUN_ID, __file__)
        conn.commit()
        print(f"archived: {new}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
