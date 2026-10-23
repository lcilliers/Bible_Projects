"""open_item_2236_v1_20261023.py -- escalation #2236: open items registered to a clear purpose, as config and
schema (design outputs/escalation/2236-open-item-design-v2-20261023.md; researcher's decisions 2026-10-23).

- escalation_thread_item gains origin_escalation_id, anchor, source_terms, target_cluster, target_terms,
  read_for, why, comes_back_when, target_verses, worded_at (cfg_column, then ALTER TABLE); new table
  escalation_thread_item_verse (an item's target verses); item kind 'scope' (a worded item).
- work package open-item (iba/app/ps/Open-Item.ps1): steps add, reword, split (write grants on the item and its
  verses), due, review (cfg_report); settings open_item.max_verses (200), open_item.review_age_days (60),
  open_item.output_dir; module open_item.
- cfg_behaviour_rule open-item-has-a-clear-purpose (the researcher's description), at point of use for
  Open-Item.ps1, Escalation.ps1 and Strand-Reading.ps1.
- cfg_utility for the three new files and this migration.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path) in the
same transaction. Idempotent. One transaction.

Usage:
    python iba/app/migration/open_item_2236_v1_20261023.py [--db PATH] [--dry-run]
"""
import argparse
import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import table_ddl  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2236-OPEN-ITEM-20261023"
MODULE = "open_item_2236_v1_20261023"
SOURCE = "escalation #2236, open-item design v2 (outputs/escalation/2236-open-item-design-v2-20261023.md)"
FILLED = "iba/app/lib/openitem.py (add, reword, split)"
NOW = "(strftime('%Y-%m-%dT%H:%M:%SZ','now'))"
WP = "open-item"
ITEM_COLS = [
    ("origin_escalation_id", "INTEGER", "the task or issue of the analysis that raised the item", "escalation.id"),
    ("anchor", "TEXT", "where in that analysis: strong:, verse:, observation:, claim: or block:<chapter / heading>", None),
    ("source_terms", "TEXT", "the source analysis's strong(s), comma-separated, for a cluster item", None),
    ("target_cluster", "TEXT", "the cluster the further work reads (the item's home: it comes back when that cluster is worked)", "cluster.cluster_code"),
    ("target_terms", "TEXT", "the related term(s) in the target cluster, comma-separated", None),
    ("read_for", "TEXT", "what the further reading is to look for", None),
    ("why", "TEXT", "why it is an open item: what the origin found that leaves it open", None),
    ("comes_back_when", "TEXT", "the trigger that brings the item back", None),
    ("target_verses", "INTEGER", "how many verses the target holds (escalation_thread_item_verse); at most open_item.max_verses", None),
    ("worded_at", "TEXT", "when the item was worded to the #2236 rules (kind 'scope'); NULL: not yet worded", None),
]
VERSE_TABLE = "escalation_thread_item_verse"
RULE_KEY = "open-item-has-a-clear-purpose"
RULE_TEXT = ("An open item is a pointer from the analysis in hand to related work, made so as not to interrupt that "
             "analysis: a record of related analysis to do, always cleared at some point, and always related to the "
             "core analysis that raised it. It is registered through Open-Item.ps1 with its origin and anchor, a target "
             "scoped to specific verses (a cluster item reads the target cluster's related term against the source "
             "analysis's strong, never the cluster as a whole), what to read for, why it is open, and when it comes "
             "back. One purpose per item: a wider target is split into separate items. An item without a clear "
             "purpose is not raised; open items are reviewed for stragglers (Open-Item.ps1 -Action Review).")
RULE_SOURCE = ("Researcher, chat 2026-10-23 (verbatim, #2236): \"In my view open items is designed to be pointers into "
               "further work, without interupting the current flow of analysis.  it creates a record of related analysis "
               "to do and should always be cleared at some point.  open items must always relate to the core underlying "
               "analysis to give it context.\" and (#2236 v3) \"read cluster xx for the strong/verse xx (the source analysis "
               "strong) and how the source strong interacts with the the related term xxx from the target cluster ... "
               "I would tend to split the open item into separate open items, rather than bundle multiple purposes into "
               "one open item ... open items without a clear purpose should be avoided.\"")
SEE = "see lib/openitem.py (escalation #2236)"
STEPS = [("add", "an item registered to a clear purpose: origin and anchor, a target scoped to verses, read for, why, comes back when", True),
         ("reword", "an existing item reworded to the same rules; the earlier wording to its history", True),
         ("split", "one wide item replaced by several, one purpose each; the old one superseded by them", True),
         ("due", "the worded items that come back when a cluster is worked (read-only)", False),
         ("review", "the stragglers report: items not worded, worded items past the review age (read-only)", False)]
SETTINGS = [("open_item.max_verses", 200, "an open item's target holds at most this many verses; a wider one is refused, to be split into separate items, one purpose each (researcher 2026-10-23, #2236 D3)"),
            ("open_item.review_age_days", 60, "Open-Item.ps1 -Action Review lists worded items older than this as stragglers to deal with (#2236 D4)"),
            ("open_item.output_dir", "outputs/open-items", "where Open-Item.ps1 -Action Review writes the stragglers report (#2236)")]
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
UTILITIES = [
    ("openitem", "iba/app/lib/openitem.py", "openitem.py -- open items registered to a clear purpose (escalation #2236): "
     "add, reword, split (target scoped to verses, at most open_item.max_verses), due, review.", 0, None),
    ("handlers_openitem", "iba/app/handlers/openitem.py", "handlers/openitem.py -- the run.py handlers for work package "
     "open-item (Open-Item.ps1), one per action; the logic is in lib/openitem.py (escalation #2236).", 0, None),
    ("Open-Item.ps1", "iba/app/ps/Open-Item.ps1", "PS entry point for registering open items (escalation #2236); "
     "dispatches through run.py, work package open-item.", 1, "thin wrapper; config is read by the handlers through run.py"),
]


def col(table, name, ordinal, typ, use, *, pk=0, nn=0, dflt=None, fk=None):
    return {"database": "iba", "table_name": table, "name": name, "ordinal": ordinal, "type": typ, "is_pk": pk,
            "notnull": nn, "is_unique": 0, "dflt": dflt, "fk": fk, "use": use, "expectation": None, "source": SOURCE,
            "filled_by": FILLED, "inactive": 0}


VERSE_COLS = [col(VERSE_TABLE, "id", 0, "INTEGER", "surrogate PK", pk=1, nn=1),
              col(VERSE_TABLE, "item_id", 1, "INTEGER", "the open item", nn=1, fk="escalation_thread_item.id"),
              col(VERSE_TABLE, "verse_id", 2, "INTEGER", "a verse of its target", nn=1, fk="verse.id"),
              col(VERSE_TABLE, "deleted", 3, "INTEGER", "1 once the item is reworded (the earlier target kept as history)", nn=1, dflt="0"),
              col(VERSE_TABLE, "created_at", 4, "TEXT", "when the row was written (ISO-8601 UTC)", nn=1, dflt=NOW),
              col(VERSE_TABLE, "created_by", 5, "TEXT", "who wrote the row: Claude, Researcher, migration, or 'direct edit'", nn=1, dflt="'direct edit'")]


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    n = conn.execute("SELECT max(ordinal) FROM cfg_column WHERE database='iba' AND table_name='escalation_thread_item'").fetchone()[0]
    for name, typ, use, fk in ITEM_COLS:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='escalation_thread_item' AND name=?", name):
            n += 1
            ops.append(("cfg_column", "insert", {}, col("escalation_thread_item", name, n, typ, use, fk=fk)))
    if not has("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", VERSE_TABLE):
        ops.append(("cfg_table", "insert", {}, {"database": "iba", "name": VERSE_TABLE, "grain": "one row per verse of an open item's target",
                                                "use": "#2236: the verses an open item is about, so it matches a scope on these verses and never on a whole cluster",
                                                "inactive": 0, "category": "data"}))
    for c in VERSE_COLS:
        if not has("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?", VERSE_TABLE, c["name"]):
            ops.append(("cfg_column", "insert", {}, c))
    for name, c in (("idx_escalation_thread_item_verse_item_id", "item_id"), ("idx_escalation_thread_item_verse_verse_id", "verse_id")):
        if not has("SELECT 1 FROM cfg_index WHERE table_name=? AND name=?", VERSE_TABLE, name):
            ops.append(("cfg_index", "insert", {}, {"table_name": VERSE_TABLE, "name": name, "col": c, "ordinal": 0}))
    for name, value in (("escalation_thread_item_kind", "scope"), ("config_module", "open_item")):
        if not has("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", name, value):
            o = conn.execute("SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
            ops.append(("cfg_enum", "insert", {}, {"name": name, "value": value, "ordinal": o, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {"name": WP, "ps_script": "iba/app/ps/Open-Item.ps1", "runs_over": "none",
                                                       "chained": 0, "inactive": 0}))
    for i, (step, does, writes) in enumerate(STEPS):
        sid = f"open_item.{step}"
        if not has("SELECT 1 FROM cfg_step WHERE step=?", sid):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": i, "step": sid,
                                                   "handler": f"iba.app.handlers.openitem:{step}", "scope": "none",
                                                   "does": f"{does} -- {SEE}", "inactive": 0, "kind": "utility"}))
        if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", sid):
            ops.append(("cfg_on_fail", "insert", {}, {"step": sid, "condition": "refused", "path": "report-continue",
                                                      "resolver": None, "message": REFUSED, "route": "terminal", "inactive": 0}))
        for t in (["escalation_thread_item", VERSE_TABLE] if writes else []):
            if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?", sid, t):
                ops.append(("cfg_write_grant", "insert", {}, {"writer": sid, "table_name": t, "database": "iba", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_report WHERE step='open_item.review'"):
        ops.append(("cfg_report", "insert", {}, {"step": "open_item.review", "title": "Open items review", "show_toc": 0,
                                                 "footer_text": None, "output_kind": "md", "naming_scheme": "dated",
                                                 "archive_dir": "archive", "inactive": 0}))
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "module": "open_item",
                                                      "inactive": 0, "use": use}))
    row = conn.execute("SELECT id FROM cfg_behaviour_rule WHERE rule_key=?", (RULE_KEY,)).fetchone()
    rid = row[0] if row else conn.execute("SELECT max(id) FROM cfg_behaviour_rule").fetchone()[0] + 1
    if not row:
        ops.append(("cfg_behaviour_rule", "insert", {}, {
            "id": rid, "class": "study_method", "rule_key": RULE_KEY, "rule_text": RULE_TEXT, "source": RULE_SOURCE,
            "enforced_by": "iba/app/lib/openitem.py (Add/Reword/Split refuse an item with no target, read-for, why or "
                           "comes-back-when, or over open_item.max_verses); Open-Item.ps1 -Action Review",
            "added_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "active": 1,
            "enforcement_status": "partially_enforced", "deliver_when": "always"}))
    for ps in ("Open-Item.ps1", "Escalation.ps1", "Strand-Reading.ps1"):
        if not has("SELECT 1 FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind='ps' AND scope_value=?", f"B:{rid}", ps):
            ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": f"B:{rid}", "scope_kind": "ps", "scope_value": ps, "inactive": 0}))
    for module, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": 0,
                                                      "config_exempt": exempt, "config_exempt_reason": reason,
                                                      "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same "
                                    "class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2236: open-item columns and verse table, work package open-item, "
                       f"settings, rule {RULE_KEY}; run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    live_cols = {r[1] for r in conn.execute("PRAGMA table_info(escalation_thread_item)")}
    missing_cols = [c for c in ITEM_COLS if c[0] not in live_cols]
    has_table = conn.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (VERSE_TABLE,)).fetchone()
    if a.dry_run or (not ops and not missing_cols and has_table):
        print(f"{'DRY RUN -- ' if a.dry_run else 'already applied -- '}{len(ops)} write(s); columns to add: "
              f"{[c[0] for c in missing_cols]}")
        return 0
    try:
        conn.execute("SAVEPOINT open_item_mig")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        for name, typ, _use, fk in missing_cols:
            ref = f' REFERENCES "{fk.split(".")[0]}"("{fk.split(".")[1]}")' if fk else ""
            conn.execute(f'ALTER TABLE escalation_thread_item ADD COLUMN "{name}" {typ}{ref}')
        if not has_table:
            create_sql, index_sql = table_ddl(cfg, VERSE_TABLE)
            conn.execute(create_sql)
            for sql in index_sql:
                conn.execute(sql)
        conn.execute("RELEASE open_item_mig")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO open_item_mig")
        conn.execute("RELEASE open_item_mig")
        raise
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail); columns added: "
          f"{[c[0] for c in missing_cols]}; table {VERSE_TABLE} {'present' if has_table else 'created'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
