"""strand_items_2219_v1_20261022.py -- escalation #2219, option A (design
outputs/escalation/2219-open-item-handling-in-strand-reading-v1-20261022.md section 3; researcher
2026-10-22: "#2219: approve option A. Build and test it on a copy first, then run catch-up B for #2172.").

1. reading_strand_item: one row per open thread item a strand must answer ('matched' by Context) or
   has raised ('raised' by Record, Map or Derive); enum reading_strand_item_source.
2. reading_strand.thread_id: the strand's own thread for the items it raises (raised on first use).
3. Write grants: Context writes reading_strand_item; Record, Map and Derive write reading_strand_item
   and reading_strand (thread_id). The thread rows themselves are written by lib/escalation.py under
   its own grants.
4. The close gate strand_account_clean also refuses while a matched item has no response since it was
   matched (its message restated); the step descriptions of Context, Record, Map, Derive and Account
   restated.

Tables are built from their cfg_column rows (lib/db.table_ddl). cfg_* writes through
configmaint.apply_logged(). Registers itself (inactive, at its own archive path) in the same
transaction. Idempotent. One transaction.

Usage:
    python iba/app/migration/strand_items_2219_v1_20261022.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import table_ddl  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2219-STRAND-ITEMS-20261022"
MODULE = "strand_items_2219_v1_20261022"
SOURCE = "escalation #2219, option A (outputs/escalation/2219-open-item-handling-in-strand-reading-v1-20261022.md)"
FILLED = "iba/app/lib/strandreading.py"
SEE = " -- see lib/strandreading.py (escalation #2172, #2219)"
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WHO = "who wrote the row: Claude, Researcher, migration, or 'direct edit' (the default, a row inserted outside the tool)"


def col(table, name, ordinal, typ, use, *, pk=0, nn=0, dflt=None, fk=None, exp=None):
    return {"database": "iba", "table_name": table, "name": name, "ordinal": ordinal, "type": typ,
            "is_pk": pk, "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use,
            "expectation": exp, "source": SOURCE, "filled_by": FILLED, "inactive": 0}


T = "reading_strand_item"
TABLE = ("one row per open thread item a strand must answer or has raised",
         "#2219: the open items of a strand -- 'matched' (Strand-Reading Context: an open item matching the "
         "strand's words, their clusters, its verses or its code; the close gate refuses while one has no thread "
         "response since it was matched) or 'raised' (found in the strand's reading, on its own thread)", [
    col(T, "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
    col(T, "strand_id", 1, "INTEGER", "the strand", nn=1, fk="reading_strand.id"),
    col(T, "item_id", 2, "INTEGER", "the open item (escalation_thread_item)", nn=1, fk="escalation_thread_item.id"),
    col(T, "source", 3, "TEXT", "cfg_enum reading_strand_item_source: matched (to answer) or raised (found in "
        "the reading)", nn=1, exp="enum.reading_strand_item_source"),
    col(T, "matched_on", 4, "TEXT", "matched: the strand's words, clusters, verses or code it matched; raised: the "
        "step that raised it"),
    col(T, "created_at", 5, "TEXT", "when the item was recorded against the strand (ISO-8601 UTC); a matched item "
        "is answered by a thread response at or after this", nn=1, dflt=NOW),
    col(T, "created_by", 6, "TEXT", WHO, nn=1, dflt="'direct edit'"),
])
UNIQUE = ["strand_id", "item_id"]
INDEX = [("idx_reading_strand_item_item_id", "item_id")]
ENUMS = [("reading_strand_item_source", "matched"), ("reading_strand_item_source", "raised")]
GRANTS = {"strand_reading.context": [T], "strand_reading.record": [T, "reading_strand"],
          "strand_reading.map": [T, "reading_strand"], "strand_reading.derive": [T, "reading_strand"]}
DOES = {
    "strand_reading.context": "step 1: every hit with its text and lexical data, the observations already on those "
    "words and verses, each verse's coverage; every open thread item matching the strand's words, their clusters, "
    "its verses or its code recorded as an item to answer -> the context file",
    "strand_reading.record": "step 2: the reading recorded -- observations (grounded, quote-checked), a face or a "
    "reason per hit read, new open items found (raised on the strand's thread); read verses marked analysed",
    "strand_reading.map": "step 4: each related block's statements mapped to the claims register; an unclaimed "
    "statement becomes a new claim or an open item on the strand's thread",
    "strand_reading.derive": "step 5: new, adjusted and withdrawn claims, each resting on observations or verses; "
    "each observation's disposition (held: an existing open item or a new one raised on the strand's thread)",
    "strand_reading.account": "step 7: the strand from the tables, gaps as text (read-only), its open items with "
    "their answers; the same facts are the close gate",
}
GATE = ("the escalation that records a strand reaches completed or closed only when every hit has a face or a "
        "reason, every observation a disposition, and every open item matched by Context a thread response since "
        "it was matched -- #2172 safeguard 5, #2219 (Strand-Reading.ps1 -Step Account lists the gaps)")


def plan(conn) -> list[tuple]:
    """Every cfg_* write, in order; each guarded so a re-run finds nothing to do."""
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='reading_strand' AND name='thread_id'"):
        n = conn.execute("SELECT MAX(ordinal) FROM cfg_column WHERE database='iba' AND "
                         "table_name='reading_strand'").fetchone()[0]
        ops.append(("cfg_column", "insert", {}, col("reading_strand", "thread_id", n + 1, "INTEGER",
                    "the strand's own thread (type thread) for the open items its reading raises; set when the "
                    "first is raised, and again if that thread has completed (#2219)", fk="escalation.id")))
    grain, use, cols = TABLE
    if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", T):
        ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": T, "grain": grain, "use": use,
                                                "inactive": 0, "category": "data"}))
    for c in cols:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", T, c["name"]):
            ops.append(("cfg_column", "insert", {}, c))
    for i, c in enumerate(UNIQUE):
        if not has("SELECT 1 FROM cfg_unique WHERE database='iba' AND table_name=? AND col=?", T, c):
            ops.append(("cfg_unique", "insert", {}, {"database": "iba", "table_name": T, "col": c, "ordinal": i}))
    for name, c in INDEX:
        if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=?", T, name):
            ops.append(("cfg_index", "insert", {}, {"table_name": T, "name": name, "col": c, "ordinal": 0}))
    for name, value in ENUMS:
        if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, value):
            o = conn.execute("SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
            o += sum(1 for op in ops if op[0] == "cfg_enum" and op[3]["name"] == name)
            ops.append(("cfg_enum", "insert", {}, {"name": name, "value": value, "ordinal": o, "inactive": 0}))
    for writer, tables in GRANTS.items():
        for t in tables:
            if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?", writer, t):
                ops.append(("cfg_write_grant", "insert", {}, {"writer": writer, "table_name": t, "database": "iba",
                                                              "inactive": 0}))
    for step, does in DOES.items():
        if not has("SELECT 1 FROM cfg_step WHERE step=? AND does=?", step, does + SEE):
            ops.append(("cfg_step", "update", {"step": step}, {"does": does + SEE}))
    for action in ("update", "resolve_self_correctable"):
        if not has("SELECT 1 FROM cfg_escalation_requirement WHERE action=? AND check_kind='strand_account_clean' "
                   "AND message=?", action, GATE):
            ops.append(("cfg_escalation_requirement", "update",
                        {"action": action, "check_kind": "strand_account_clean"}, {"message": GATE}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2219 option A: reading_strand_item, "
                       f"reading_strand.thread_id, the strand steps' grants, the close gate on open items; "
                       f"run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    live = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    rs_cols = {r[1] for r in conn.execute("PRAGMA table_info(reading_strand)")}
    print(f"{len(ops)} cfg write(s); {T} live: {T in live}; reading_strand.thread_id live: {'thread_id' in rs_cols}")
    for t, op, where, set_ in ops:
        print(f"  {op} {t} {where or ''} {', '.join(f'{k}={v}' for k, v in set_.items() if k in ('name', 'value', 'writer', 'table_name', 'step', 'module', 'action'))}")
    if a.dry_run:
        return 0
    try:
        conn.execute("SAVEPOINT strand_items")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        if "thread_id" not in rs_cols:
            conn.execute('ALTER TABLE reading_strand ADD COLUMN "thread_id" INTEGER REFERENCES "escalation"("id")')
        if T not in live:
            create_sql, index_sql = table_ddl(cfg, T)
            conn.execute(create_sql)
            for sql in index_sql:
                conn.execute(sql)
        conn.execute("RELEASE strand_items")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO strand_items")
        conn.execute("RELEASE strand_items")
        raise
    print(f"applied (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
