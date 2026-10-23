"""temp_2212_apply_patch_test.py -- test plan cases 8c-8l for prose.apply_patch (#2212), each on a
fresh copy of bible_research.db (lib/dbsnapshot.copy_db); the live file is opened read-only only.

    python -m iba.app.tools.temp_2212_apply_patch_test <scratch dir>
"""
from __future__ import annotations

import gzip
import json
import sqlite3
import sys
from pathlib import Path

from ..lib import prosestore
from ..lib.cfg import Cfg
from ..lib.dbsnapshot import copy_db

RESULTS = []


def check(case: str, cond: bool, detail: str):
    RESULTS.append((case, "PASS" if cond else "FAIL", detail))


def fresh(cfg, scratch: Path, name: str) -> sqlite3.Connection:
    dest = copy_db(scratch / f"br-{name}.db", src=cfg.database_path("bible_research"))
    conn = sqlite3.connect(dest)
    conn.row_factory = sqlite3.Row
    conn.isolation_level = None
    return conn


def counts(conn) -> tuple:
    return (conn.execute("SELECT COUNT(*) FROM record_change_log").fetchone()[0],
            conn.execute("SELECT COUNT(*), SUM(LENGTH(body)), GROUP_CONCAT(status) FROM prose_section").fetchone()[:])


def refused(conn, patch, granted) -> str | None:
    try:
        prosestore.apply_patch(conn, patch, granted)
    except prosestore.PatchRefused as e:
        return str(e)
    return None


def main(scratch: Path) -> int:
    scratch.mkdir(parents=True, exist_ok=True)
    cfg = Cfg()
    granted = cfg.may_write(prosestore.PATCH_WRITER, database="bible_research")
    live = sqlite3.connect(f"file:{Path(cfg.database_path('bible_research')).as_posix()}?mode=ro", uri=True)
    live.row_factory = sqlite3.Row
    sec = live.execute("SELECT id, status, heading, body FROM prose_section WHERE COALESCE(delete_flagged,0)=0 "
                       "AND author <> 'claude_code' ORDER BY id LIMIT 1").fetchone()
    live.close()
    new_status = "in_review" if sec["status"] != "in_review" else "draft"

    # a real SetStatus patch, from the live generator (it only reads the live database)
    sp = prosestore.run_set_status(cfg, [sec["id"]], new_status, out=str(scratch / "set-status.json"))
    set_patch = json.loads(Path(sp["path"]).read_text(encoding="utf-8"))
    pid = set_patch["_patch_meta"]["patch_id"]

    # 8c dry run
    conn = fresh(cfg, scratch, "8c")
    before = counts(conn)
    r = prosestore.apply_patch(conn, set_patch, granted, dry_run=True)
    check("8c dry run", counts(conn) == before and r["counts"] == {"prose_section_status_set": 1},
          f"counts {r['counts']}; tables unchanged: {counts(conn) == before}")

    # 8d live, 8e again
    r = prosestore.apply_patch(conn, set_patch, granted)
    row = conn.execute("SELECT status, version FROM prose_section WHERE id = ?", (sec["id"],)).fetchone()
    log = conn.execute("SELECT id, payload, change_type FROM record_change_log WHERE change_source = ?", (pid,)).fetchall()
    prior = json.loads(gzip.decompress(log[0]["payload"])) if log else {}
    check("8d live set_status", row["status"] == new_status and len(log) == 1 and row["version"] == log[0]["id"]
          and prior.get("status") == sec["status"],
          f"status {sec['status']} -> {row['status']}; log rows {len(log)}; version {row['version']} = log id "
          f"{log[0]['id'] if log else None}; payload prior status {prior.get('status')!r}")
    msg = refused(conn, set_patch, granted)
    check("8e re-apply", bool(msg and "already applied" in msg), msg or "not refused")
    conn.close()

    # 8f supersede, the import_chapter / flag_fix_apply shape
    conn = fresh(cfg, scratch, "8f")
    new_body = sec["body"] + " TEST-2212"
    sup = {"_patch_meta": {"patch_id": "PATCH-TEST-2212-SUPERSEDE", "patch_type": "PROSE"},
           "operations": [{"op_id": "T1", "table": "prose_section", "operation": "supersede",
                           "supersedes_id": sec["id"], "record": {"body": new_body, "author": "researcher",
                                                                  "status": "draft"}}]}
    prosestore.apply_patch(conn, sup, granted)
    row = conn.execute("SELECT body, heading, word_count FROM prose_section WHERE id = ?", (sec["id"],)).fetchone()
    log = conn.execute("SELECT payload FROM record_change_log WHERE change_source = 'PATCH-TEST-2212-SUPERSEDE'").fetchone()
    prior = json.loads(gzip.decompress(log["payload"]))
    check("8f supersede", row["body"] == new_body and row["heading"] == sec["heading"]
          and row["word_count"] == len(new_body.split()) and prior["body"] == sec["body"],
          f"body changed, heading kept: {row['heading'] == sec['heading']}, word_count {row['word_count']}, "
          f"payload holds old body: {prior['body'] == sec['body']}")
    conn.close()

    # 8g-8l refusals, each checked for nothing written
    cases = {
        "8g ungranted table": ({"patch_id": "P-8g"}, [{"op_id": "T", "table": "prose_section_dimension_link",
                                                       "operation": "insert", "record": {}}], "no cfg_write_grant"),
        "8h good then bad": ({"patch_id": "P-8h"}, [set_patch["operations"][0],
                             {"op_id": "T2", "table": "prose_section", "operation": "supersede",
                              "supersedes_id": 999999999, "record": {"body": "x", "author": "researcher"}}],
                             "not found"),
        "8i unknown operation": ({"patch_id": "P-8i"}, [{"op_id": "T", "table": "prose_section",
                                                         "operation": "explode"}], "not supported"),
        "8j immutable type field": ({"patch_id": "P-8j"}, [{"op_id": "T", "table": "prose_section_type",
                                                            "operation": "update", "match": {"id": 99},
                                                            "set": {"code": "zz"}}], "immutable"),
        "8k session_a_replace author gate": ({"patch_id": "P-8k"}, [{"op_id": "T", "table": "prose_section",
                                              "operation": "session_a_replace", "id": sec["id"],
                                              "record": {"body": "x"}}], "not a claude_code row"),
        "8l no patch id": ({}, [set_patch["operations"][0]], "no _patch_meta.patch_id"),
        "8l no operations": ({"patch_id": "P-8l"}, [], "no operations"),
    }
    for case, (meta, ops, expect) in cases.items():
        conn = fresh(cfg, scratch, case.split()[0] + str(len(RESULTS)))
        before = counts(conn)
        msg = refused(conn, {"_patch_meta": meta, "operations": ops}, granted)
        check(case, bool(msg and expect in msg) and counts(conn) == before,
              f"{msg or 'not refused'}; nothing written: {counts(conn) == before}")
        conn.close()

    for case, verdict, detail in RESULTS:
        print(f"{verdict}  {case}: {detail}")
    failed = sum(1 for _, v, _ in RESULTS if v == "FAIL")
    print(f"{len(RESULTS) - failed}/{len(RESULTS)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1])))
