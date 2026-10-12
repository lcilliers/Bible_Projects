"""backfill_cfg_change_detail_2000_v1_20261012.py -- escalation #2000: the config audit trail for
the Developer Mode writes that bypassed it.

Three #2000 migrations wrote cfg_* rows directly on 2026-10-12 with no cfg_change_detail row
(escalation_open_threads_v1, escalation_thread_reassign_keeps_state_v1,
escalation_thread_lifecycle_v1). Developer Mode removes configmaint.propose's approval gate, never
the audit; from now on Developer Mode config writes go through configmaint.apply_logged().

This records what those writes did, exactly: every cfg_* row that differs between a baseline copy
of iba.db taken before the work (NAS db_backups iba_20261011T171049Z.db; nothing was logged to
cfg_change_detail after it) and the live database. Inserts carry the full new row; updates carry
the changed columns and the full prior row (before_json). cfg_change_log and cfg_change_detail
themselves are not compared. Writes nothing to any cfg_* table except cfg_change_detail.

Guarded: refuses to run twice (looks for its own run_id). One transaction.

Usage:
    python iba/app/migration/backfill_cfg_change_detail_2000_v1_20261012.py --baseline PATH [--db PATH] [--dry-run]
"""
import argparse
import datetime
import json
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2000-BACKFILL-20261012"
SKIP = {"cfg_change_log", "cfg_change_detail"}
# natural keys for the tables whose rows were updated (where_json, as propose records it)
KEYS = {"cfg_behaviour_rule": ["id"], "cfg_escalation": ["id"],
        "cfg_status_flow": ["entity", "status"], "cfg_utility": ["module"]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    old = sqlite3.connect(f"file:{args.baseline}?mode=ro", uri=True)
    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    if cur.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"{RUN_ID} already recorded -- nothing written")
        return 0
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    counts: dict[str, int] = {}
    try:
        cur.execute("BEGIN")
        tables = [r[0] for r in cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'cfg\\_%' ESCAPE '\\' "
            "ORDER BY name").fetchall()]
        for t in tables:
            if t in SKIP:
                continue
            cols = [r[1] for r in cur.execute(f'PRAGMA table_info("{t}")')]
            if not old.execute("SELECT 1 FROM sqlite_master WHERE name=?", (t,)).fetchone():
                raise RuntimeError(f"{t} is new since the baseline -- not expected; check by hand")
            ocols = [r[1] for r in old.execute(f'PRAGMA table_info("{t}")')]
            if ocols != cols:
                raise RuntimeError(f"{t} columns changed since the baseline -- check by hand")
            sel = ",".join(f'"{c}"' for c in cols)
            o = {r[0]: dict(zip(cols, r[1:])) for r in old.execute(f'SELECT rowid,{sel} FROM "{t}"')}
            n = {r[0]: dict(zip(cols, r[1:])) for r in cur.execute(f'SELECT rowid,{sel} FROM "{t}"')}
            for rid in sorted(set(o) | set(n)):
                if rid not in o:
                    row = (t, "insert", "{}", json.dumps(n[rid]), None)
                elif rid not in n:
                    row = (t, "delete", json.dumps(o[rid]), None, json.dumps(o[rid]))
                elif o[rid] != n[rid]:
                    if t not in KEYS:
                        raise RuntimeError(f"update on {t} rowid {rid} has no natural key mapped")
                    where = {k: n[rid][k] for k in KEYS[t]}
                    set_ = {c: n[rid][c] for c in cols if o[rid][c] != n[rid][c]}
                    row = (t, "update", json.dumps(where), json.dumps(set_), json.dumps(o[rid]))
                else:
                    continue
                cur.execute("INSERT INTO cfg_change_detail (run_id, table_name, op, where_json, "
                            "set_json, before_json, applied_at) VALUES (?,?,?,?,?,?,?)",
                            (RUN_ID, *row, now))
                counts[f"{row[1]} {t}"] = counts.get(f"{row[1]} {t}", 0) + 1
        if args.dry_run:
            conn.rollback()
        else:
            conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
        old.close()
    for k, v in sorted(counts.items()):
        print(f"{v:>3}  {k}")
    print(f"{sum(counts.values())} row(s) {'would be' if args.dry_run else ''} recorded under "
          f"{RUN_ID}{' -- DRY RUN, rolled back' if args.dry_run else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
