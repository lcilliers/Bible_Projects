"""surface_collection_ask_2361_v1_20261106.py -- escalation #2361, stage 5b: registers the collection seeding and asking steps and their settings.

  settings   collection.shortlist_size 60, collection.score_threshold 8, collection.embed_cache "collection/embeddings", collection.embed_role "embed",
             collection.list_max 20, ai.embed_batch 64
  steps      collection.seed (Collection-Build.ps1 -Action Seed) and collection.ask (-Action Ask), with refused and halted conditions
  grants     collection.seed -> collection, collection_listing, ai_call, run_batch; collection.ask -> collection_listing, ai_call, run_batch
  utility    collectionask (lib/collectionask.py) and this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/surface_collection_ask_2361_v1_20261106.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2361-SURFACE-COLLECTION-ASK-20261106"
MODULE = "surface_collection_ask_2361_v1_20261106"
WP = "collection-build"
H = "iba.app.handlers.collectionbuild"
SETTINGS = [
    ("collection.shortlist_size", 60, "how many words nearest the core word by embedding are judged as candidates when a collection is asked (module 5 of 5, #2361); the listed words come on top", "collection"),
    ("collection.score_threshold", 8, "the score (0 to 10, prompt collection.score) from which a word the judge called distinct counts as a synonym (#2361); 8 is 'nearly the same, a little milder or stronger'. Read by Links and by the judging", "collection"),
    ("collection.embed_cache", "collection/embeddings", "the folder, under surfaces.working_files_root, of the cache of embedding vectors (#2361): regenerable, one file per model digest, used only to rank candidates", "collection"),
    ("collection.embed_role", "embed", "the cfg_ai_model role of the embedding model used to rank candidates (#2361)", "collection"),
    ("collection.list_max", 20, "the most words taken from each list (synonyms, opposites) the model names for a new collection (#2361)", "collection"),
    ("ai.embed_batch", 64, "how many texts the AI client sends in one embedding call (#2361); one ai_call row per batch", "ai"),
]
STEPS = [
    ("collection.seed", "seed", 6, "make a collection of a core word: the AI client names its pole (real word, reciprocal) and lists synonyms and opposites into collection_listing; -Word -- see lib/collectionask.py (escalation #2361)"),
    ("collection.ask", "ask", 7, "judge the candidates of a collection through the AI client (the words nearest the core by embedding, and the listed words): candidate, score, pole check, association; one ai_call row each; -Collection, -Limit -- see lib/collectionask.py (escalation #2361)"),
]
REFUSED = "refused, nothing written -- the reason follows (a usage outcome, not recorded as an escalation)"
HALTED = ("halted, what was answered is kept in ai_call -- the set number of questions in a row got no usable answer (the server or the ssh tunnel stopped answering); "
          "fix the cause and run again, it carries on with the words not yet judged (a usage outcome, not recorded as an escalation)")
GRANTS = [("collection.seed", "collection"), ("collection.seed", "collection_listing"), ("collection.seed", "ai_call"), ("collection.seed", "run_batch"),
          ("collection.ask", "collection_listing"), ("collection.ask", "ai_call"), ("collection.ask", "run_batch")]
UTILITIES = [
    ("collectionask", "iba/app/lib/collectionask.py", 0, "collectionask.py -- the front of module 5 of 5: seeding a collection (pole, real-word check, the model's list) and judging its candidates "
     "(embedding shortlist, synonym, score, pole check, association) through the AI client (escalation #2361).", 0, None),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2361 stage 5b: registers collection.seed and collection.ask and their settings; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='collection'"):
        nxt = conn.execute("SELECT COALESCE(MAX(ordinal),0)+1 FROM cfg_enum WHERE name='config_module'").fetchone()[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "config_module", "value": "collection", "ordinal": nxt, "inactive": 0}))
    for key, value, use, module in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": module, "inactive": 0}))
    for step, fn, ordinal, does in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {"work_package": WP, "ordinal": ordinal, "step": step, "handler": f"{H}:{fn}", "scope": "none", "does": does,
                                                   "inactive": 0, "kind": "operations"}))
        for cond, msg in (("refused", REFUSED), ("halted", HALTED)):
            if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", step, cond):
                ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": cond, "path": "report-continue", "resolver": None, "message": msg,
                                                          "route": "terminal", "inactive": 0}))
    for w, t in GRANTS:
        if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", w, t):
            ops.append(("cfg_write_grant", "insert", {}, {"writer": w, "table_name": t, "database": "iba", "inactive": 0}))
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
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2361-collection-ask', named=True)}")
    try:
        conn.execute("SAVEPOINT collection_ask")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE collection_ask")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO collection_ask")
        conn.execute("RELEASE collection_ask")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
