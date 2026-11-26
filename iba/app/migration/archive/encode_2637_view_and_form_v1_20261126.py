"""encode_2637_view_and_form_v1_20261126.py -- escalation #2637, plan v3 X1 and X2 (outputs/escalation/2637-build-plan-v3-20261126.md).

cfg_setting layer.read_types: limits.view_max_chars (the size of one part of a package's readable view, lib/readcommands.py view), and the
write instruction of the reads gains the judgement-only form: "all" for every occurrence of a row's subject (stage 1 and 2.1 reads,
layerreading.record), and rests_on with role in place of nodes (3.1 and 3.2, layerinner._expand_nodes). Through configmaint.apply_logged;
archived after the live apply. Idempotent. Usage: python iba/app/migration/encode_2637_view_and_form_v1_20261126.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged, archive_migration  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-2637-VIEWFORM-20261126"
MODULE = "encode_2637_view_and_form_v1_20261126"
VIEW_MAX = 60000
ALL_LINE = ('Where a reading, sense, enrichment or finding holds every occurrence of the row\'s subject, `occurrences` may be "all": the recorder '
            'names them.')
NODES_LINE = ('In place of writing `nodes`, a finding may name `rests_on` (the observations it rests on) and `role` (the node role of the words '
              'they cover; `roles` {occurrence: role, or "" to leave one out} for the exceptions): the recorder writes a traced node on each and an '
              'occurrence node on each occurrence they cover (each observation\'s `covers` or `occurrences` lists them). Nodes written by hand are kept.')
ADD = {"words": ALL_LINE, "senses": ALL_LINE, "enrichment": ALL_LINE, "structure": ALL_LINE, "elements": NODES_LINE, "behaviours": NODES_LINE}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    rt = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='layer.read_types'").fetchone()[0])
    changed = False
    if rt["limits"].get("view_max_chars") != VIEW_MAX:
        rt["limits"]["view_max_chars"] = VIEW_MAX
        changed = True
    for read, line in ADD.items():
        w = rt[read]["write"]
        if line not in w:
            w.insert(len(w) - 1, line)      # before the closing "Then: ..." line
            changed = True
    ops = [("cfg_setting", "update", {"key": "layer.read_types"}, {"value": json.dumps(rt, ensure_ascii=False)})] if changed else []
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py",
                                                  "purpose": "migration of #2637 X1/X2: view_max_chars and the judgement-only form in the write instructions",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "a one-off migration; its values are the config it writes",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if a.dry_run or not ops:
        print(("DRY RUN: " if a.dry_run else "already applied: ") + f"{len(ops)} write(s)")
        return 0
    for t, op, where, set_ in ops:
        apply_logged(conn, RUN_ID, t, op, where, set_)
    conn.commit()
    print(f"applied (run {RUN_ID}): {len(ops)} write(s)")
    if pathlib.Path(a.db).resolve() == DEFAULT_DB.resolve():
        print(f"archived: {archive_migration(conn, RUN_ID, __file__)}")
        conn.commit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
