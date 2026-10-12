"""escalation_open_threads_import_v1_20261012.py -- escalation #2000, build step 7: import the open
threads register into the escalation table, from the APPROVED preview JSON only.

Researcher, round 6 (verbatim): "approve the preview, proceed with the build". Preview:
`_analytics/cross-cluster-web/escalation-2000-open-threads-register-import-preview-v1-20261012.json`
(built read-only by `escalation-2000-open-threads-import-preview-v1-20261012.py`; re-run
2026-10-12 before this import, output identical). Needs the schema from
`escalation_open_threads_v1_20261012.py` first.

What it writes, in one transaction, in OT-number order (so escalation ids ascend with OT numbers):
  - one `escalation` row + its v1 `escalation_history` row per thread: the 100 register rows plus
    the 2 threads rebuilt from closed escalations (OT-101, OT-102). Rows keep their historical
    raised_at; answered_at is the preview's answered_at, else raised_at. run_id
    MANUAL-IMPORT-2000-OT-nn, at_step 'manual'.
  - every item (escalation_thread_item) with its item_no, and every response
    (escalation_thread_item_response). '#nnnn' references become integer escalation ids.
Direct inserts, not raise_new(): the rows carry their historical dates and states (9 completed),
which no Raise could give them -- the same reason every escalation export/import before used a
migration.

Checks before commit (any failure rolls everything back): 102 threads, 284 items, 50 responses
(48 closed, 2 forward); every thread has an item; every title passes the title check; no completed
thread has an open item; every kind is a cfg_enum member; no alias already in the table.

Usage:
    python iba/app/migration/escalation_open_threads_import_v1_20261012.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
PREVIEW = (ROOT / "_analytics" / "cross-cluster-web" /
           "escalation-2000-open-threads-register-import-preview-v1-20261012.json")
EXPECT = {"threads": 102, "items": 284, "responses": 50, "closed": 48, "forward": 2}

sys.path.insert(0, str(ROOT))
from iba.app.lib.escalation import _title_shape_error  # noqa: E402  (the one title rule, #759)


def _ref(v):
    """'#1998' -> 1998; None stays None."""
    if v in (None, ""):
        return None
    return int(str(v).lstrip("#"))


def _enum(cur, name):
    return {r[0] for r in cur.execute("SELECT value FROM cfg_enum WHERE name=? AND inactive=0",
                                      (name,))}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--json", default=str(PREVIEW))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    doc = json.loads(pathlib.Path(args.json).read_text(encoding="utf-8"))
    threads = doc["threads"] + doc["rebuilt_from_closed_escalations"]["proposed"]
    threads.sort(key=lambda t: int(t["escalation"]["alias"][3:]))

    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    report, problems = [], []
    n_items = n_resp = 0
    by_kind: dict[str, int] = {}
    try:
        cur.execute("BEGIN")
        if not any(r[1] == "alias" for r in cur.execute("PRAGMA table_info(escalation)")):
            raise SystemExit("schema missing: run escalation_open_threads_v1_20261012.py first")
        aliases = [t["escalation"]["alias"] for t in threads]
        ph = ",".join("?" * len(aliases))
        clash = cur.execute(f"SELECT alias FROM escalation WHERE alias IN ({ph})", aliases).fetchall()
        if clash:
            raise SystemExit(f"already imported ({len(clash)} alias(es) present, e.g. "
                             f"{clash[0][0]}) -- nothing written")
        item_kinds = _enum(cur, "escalation_thread_item_kind")
        resp_kinds = _enum(cur, "escalation_thread_item_response_kind")
        states = _enum(cur, "escalation_state")

        for t in threads:
            e = t["escalation"]
            alias = e["alias"]
            if _title_shape_error(e["short_description"]):
                problems.append(f"{alias}: {_title_shape_error(e['short_description'])}")
            if e["state"] not in states:
                problems.append(f"{alias}: state {e['state']!r} not in cfg_enum escalation_state")
            if not t["items"]:
                problems.append(f"{alias}: no items (T7)")
            row = {
                "version": 1, "run_id": f"MANUAL-IMPORT-2000-{alias}", "source": e["source"],
                "at_step": "manual", "type": "thread", "short_description": e["short_description"],
                "context": json.dumps(e["context"], ensure_ascii=False), "comment": e["comment"],
                "tried": e.get("tried"), "state": e["state"], "next_action": e.get("next_action"),
                "next_action_assigned_to": e["next_action_assigned_to"],
                "originator": e["originator"], "resolution": e.get("resolution"),
                "raised_at": e["raised_at"], "answered_at": e.get("answered_at") or e["raised_at"],
                "resolution_kind": e["resolution_kind"], "needs_claude_followup": 0,
                "alias": alias, "comes_back_when": e["comes_back_when"]}
            cols = list(row)
            cur.execute(f"INSERT INTO escalation ({','.join(cols)}) VALUES "
                        f"({','.join('?' * len(cols))})", [row[c] for c in cols])
            esc_id = cur.lastrowid
            hist = {k: v for k, v in row.items() if k != "version"}
            hcols = ["escalation_id", "version"] + list(hist)
            cur.execute(f"INSERT INTO escalation_history ({','.join(hcols)}) VALUES "
                        f"({','.join('?' * len(hcols))})", [esc_id, 1] + list(hist.values()))
            for it in t["items"]:
                if it["kind"] not in item_kinds:
                    problems.append(f"{it['ref']}: kind {it['kind']!r} not in cfg_enum")
                if e["state"] == "completed" and it["status"] != "closed":
                    problems.append(f"{it['ref']}: open item on a completed thread (T6)")
                cur.execute("INSERT INTO escalation_thread_item (escalation_id, item_no, kind, "
                            "value, status, note, opened_at, opened_by) VALUES (?,?,?,?,?,?,?,?)",
                            (esc_id, it["item_no"], it["kind"], it["value"], it["status"],
                             it["note"], it["opened_at"], _ref(it["opened_by"])))
                item_id = cur.lastrowid
                n_items += 1
                for r in it["responses"]:
                    if r["kind"] not in resp_kinds:
                        problems.append(f"{it['ref']}: response kind {r['kind']!r} not in cfg_enum")
                    cur.execute("INSERT INTO escalation_thread_item_response (item_id, "
                                "escalation_id, kind, text, via_escalation, responded_by, "
                                "responded_at, files) VALUES (?,?,?,?,?,?,?,?)",
                                (item_id, esc_id, r["kind"], r["text"], _ref(r["via_escalation"]),
                                 r["responded_by"], r["responded_at"],
                                 json.dumps(r["files"], ensure_ascii=False) if r.get("files")
                                 else None))
                    n_resp += 1
                    by_kind[r["kind"]] = by_kind.get(r["kind"], 0) + 1
            report.append(f"{alias} -> #{esc_id} [{e['state']}] {len(t['items'])} item(s)")

        got = {"threads": len(threads), "items": n_items, "responses": n_resp,
               "closed": by_kind.get("closed", 0), "forward": by_kind.get("forward", 0)}
        if got != EXPECT:
            problems.append(f"counts {got} != expected {EXPECT}")
        if problems:
            conn.rollback()
            print("REFUSED -- rolled back, nothing written:\n  " + "\n  ".join(problems))
            return 1
        if args.dry_run:
            conn.rollback()
            report.append("DRY RUN -- rolled back, nothing written")
        else:
            conn.commit()
            report.append("committed")
        report.append(f"counts: {got}")
    except BaseException:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
