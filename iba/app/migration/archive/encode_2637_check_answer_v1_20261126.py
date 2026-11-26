"""encode_2637_check_answer_v1_20261126.py -- escalation #2637, plan v3 X3 (outputs/escalation/2637-build-plan-v3-20261126.md).

On boast (#2620) Claude checked its answers with scratch scripts before recording (interventions A3, C2, D1, E3 in
outputs/escalation/2637-manual-interventions-boast-boasting-v1-20261126.md), because a Record command stops at the first stage that fails and
shows the next stage's problems only on the next attempt. CheckAnswer runs every check of the answer's Record command at once (the `collect`
mode of lib/readcommands.py, lib/layerreading.py, lib/layerinner.py, lib/collectionvalidate.py) and writes nothing. This migration:
  cfg_step         collection.check_answer (handlers/collectionbuild.py check_answer), with its refused routing and its write grants: the
                   tables the Record commands write, written only inside savepoints that are rolled back, and read_failure
  cfg_setting      layer.refusals: `site_reads` and `reads_order` (the reads of each refusal site, so the registry is rebuilt from config by
                   refusalrules.build), check_answer among the scanned handler functions, its own refusal keyed
  cfg_setting      layer.read_types: each read's last `write` line names CheckAnswer before its Record command
  cfg_utility      this migration
Refuses (nothing written) where a refusal site is keyed by no entry or an entry keys no site. Through configmaint.apply_logged; named snapshot
before a live apply; archived after it. Idempotent.
Usage: python iba/app/migration/encode_2637_check_answer_v1_20261126.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib import refusalrules  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2637-CHECKANSWER-20261126"
MODULE = "encode_2637_check_answer_v1_20261126"
STEP = "collection.check_answer"
DOES = ("check a filled answer of any read with every check of its Record command at once (the answer's own checks, the recorder's rules, the "
        "write tried in rolled-back savepoints, the check of the written rows), each problem with its rule; nothing written -- see "
        "handlers/collectionbuild.py check_answer (escalation #2637 X3)")
MESSAGE = ("refused, nothing written -- the reason follows (a usage outcome kept in read_failure for learning, not recorded as an escalation; "
           "#2637)")
GRANTS = ["collection_layer_item", "ib_node", "ib_observation", "ib_observation_change", "read_failure"]

ALL = ["words", "senses", "enrichment", "structure", "sweep", "evidence", "elements", "behaviours"]
STAGE1 = ["words", "senses", "enrichment", "structure"]
INNER = ["elements", "behaviours"]
SITE_READS = {  # module.function -> the reads whose commands reach it; a module name alone is the default for its functions
    "readcommands": ALL,
    "readcommands.read_words": ["words"], "readcommands.record_words": ["words"],
    "readcommands.read_senses": ["senses"], "readcommands.record_senses": ["senses"],
    "readcommands.read_enrichment": ["enrichment"], "readcommands.record_enrichment": ["enrichment"],
    "readcommands.read_structure": ["structure"], "readcommands.record_structure": ["structure"],
    "readcommands.read_sweep": ["sweep"], "readcommands.record_sweep": ["sweep"],
    "readcommands.read_evidence": ["evidence"], "readcommands.record_evidence": ["evidence"],
    "readcommands.read_elements": ["elements"], "readcommands.record_elements": ["elements"],
    "readcommands.read_behaviours": ["behaviours"], "readcommands.record_behaviours": ["behaviours"],
    "layerreading": ALL,
    "layerreading.record": STAGE1, "layerreading._text_rules": STAGE1, "layerreading.settle_nodes": STAGE1,
    "layerreading.sweep_superseded": ["sweep"],
    "layerinner": INNER,
    "observationrecord": ALL,
    "observationrecord.check": INNER, "observationrecord.check_item_parts": INNER,
    "buildvalidate": ALL, "buildvalidate.sweep": ["sweep"],
    "validationactions": ALL,
    "recordingpass": ALL,
    "collectionvalidate": ["evidence"], "layerloop": ALL, "scanguard": ALL,
    "collectionbuild": ALL,
    "collectionbuild.read_words": ["words"], "collectionbuild.record_words": ["words"],
    "collectionbuild.read_senses": ["senses"], "collectionbuild.record_senses": ["senses"],
    "collectionbuild.read_enrichment": ["enrichment"], "collectionbuild.record_enrichment": ["enrichment"],
    "collectionbuild.read_structure": ["structure"], "collectionbuild.record_structure": ["structure"],
    "collectionbuild.read_behaviours": ["behaviours"], "collectionbuild.sweep_superseded": ["sweep"],
}
NEW_ENTRIES = [{"key": "PC-02", "match": "this is not the answer of a read"}]
THEN = re.compile(r"^Then: Collection-Build\.ps1 -Action (Record\w+) -File <the answer file> \(-Check to preview\)")


def registry(conn):
    reg = refusalrules.load(conn)
    if not reg.get("entries"):
        raise SystemExit("cfg_setting layer.refusals is not set: apply encode_2637_refusal_keys_v1_20261126 first")
    reg = json.loads(json.dumps(reg))
    reg["site_reads"], reg["reads_order"] = SITE_READS, ALL
    only = reg["scan"].setdefault("only", {}).setdefault("handlers/collectionbuild", [])
    if "check_answer" not in only:
        only.append("check_answer")
    have = {(e["key"], e["match"]) for e in reg["entries"]}
    reg["entries"] += [e for e in NEW_ENTRIES if (e["key"], e["match"]) not in have]
    reg, unkeyed, dead, n = refusalrules.build(ROOT, reg)
    if unkeyed or dead:
        raise SystemExit("refused, nothing written:\n" + "\n".join(f"  no entry keys {s['site']}:{s['line']} {s['template'][:100]!r}" for s in unkeyed)
                         + "".join(f"\n  entry keys no site: {e}" for e in dead))
    return reg, n


def plan(conn):
    ops = []
    if not conn.execute("SELECT 1 FROM cfg_step WHERE step=?", (STEP,)).fetchone():
        ordinal = conn.execute("SELECT coalesce(max(ordinal),0)+1 FROM cfg_step WHERE work_package='collection-build'").fetchone()[0]
        ops.append(("cfg_step", "insert", {}, {"work_package": "collection-build", "ordinal": ordinal, "step": STEP,
                                               "handler": "iba.app.handlers.collectionbuild:check_answer", "scope": "none", "does": DOES, "inactive": 0, "kind": "operations"}))
    if not conn.execute("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition='refused'", (STEP,)).fetchone():
        ops.append(("cfg_on_fail", "insert", {}, {"step": STEP, "condition": "refused", "path": "report-continue", "resolver": None, "message": MESSAGE,
                                                  "route": "terminal", "inactive": 0}))
    for t in GRANTS:
        if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", (STEP, t)).fetchone():
            ops.append(("cfg_write_grant", "insert", {}, {"writer": STEP, "table_name": t, "database": "iba", "inactive": 0}))
    reg, n = registry(conn)
    value = json.dumps(reg, ensure_ascii=False)
    if conn.execute("SELECT value FROM cfg_setting WHERE key=?", (refusalrules.SETTING,)).fetchone()[0] != value:
        ops.append(("cfg_setting", "update", {"key": refusalrules.SETTING}, {"value": value}))
    rt = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.read_types'").fetchone()[0])
    changed = False
    for read in ALL:
        need = sorted({e["key"] for e in reg["entries"] if read in e["reads"]} - set(rt[read]["rules"]))
        if need:
            rt[read]["rules"] += need
            changed = True
        w = rt[read]["write"]
        for k, line in enumerate(w):
            m = THEN.match(line)
            if m:
                w[k] = (f"Then: Collection-Build.ps1 -Action CheckAnswer -File <the answer file>: every problem at once, each with its rule, nothing "
                        f"written; correct the answer until it finds none, then -Action {m.group(1)} -File <the answer file>" + line[m.end():])
                changed = True
    if changed:
        ops.append(("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps(rt, ensure_ascii=False)}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of #2637 X3: collection.check_answer registered; the refusal registry rebuilt from config with its site_reads; CheckAnswer named in each read's write lines",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    live = pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops, n = plan(conn)
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s); {n} refusal sites keyed")
        for t, op, where, set_ in ops:
            print(" ", t, op, where or {k: str(set_[k])[:60] for k in list(set_)[:3]})
        return 0
    if live and not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2637-checkanswer-apply', named=True)}")
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
    print(f"applied (run {RUN_ID}): {len(ops)} write(s); {n} refusal sites keyed")
    if live:
        print(f"archived: {archive_migration(conn, RUN_ID, __file__)}")
        conn.commit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
