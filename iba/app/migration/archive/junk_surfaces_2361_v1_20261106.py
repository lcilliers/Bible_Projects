"""junk_surfaces_2361_v1_20261106.py -- escalation #2361 (researcher, chat 2026-11-06: "set these surfaces as soft delete").

Sets the junk surfaces of the study's surface list to soft delete. A junk surface is found by a rule held in config
(cfg_setting surfaces.junk_rules: an empty surface, a surface with no letter, a surface with punctuation inside), never by a
list in code. The rule finds four surfaces in surface_subgroup (the empty string, '^', '32,000', 'you, do') on ten pair rows.

Scope: the study's own allocation table, surface_subgroup, only. The corpus tables (verse_lexical, span, ib_node) are NOT touched:
'^', '32,000' and 'you, do' are real renderings in the ESV text (Psalm 56:7, Numbers 31:35, Genesis 21:12) and the rows of the
empty surface are textual variants the ESV does not render. Each surface still has LIVE current rows in the corpus (118 in
verse_lexical, 32 in span, 1 in ib_node; the other half of each surface's verse_lexical rows are superseded versions, which is how
verse_lexical.deleted works); whether those rows go is the researcher's decision (recorded on #2361). No other table references a surface_subgroup row.

Registers surfaces.junk_rules (module surfaces, a new config_module value), the migration's write grant on surface_subgroup and
its own cfg_utility row (inactive, at its archive path), all through configmaint.apply_logged(). A named rollback snapshot is taken
before a live apply (backup.rollback_method). Idempotent. One transaction. The before state of every row is written to Logs/.

Usage:
    python iba/app/migration/junk_surfaces_2361_v1_20261106.py [--db PATH] [--dry-run] [--expect-rows 10] [--no-snapshot]
"""
import argparse
import datetime
import json
import pathlib
import re
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2361-JUNK-SURFACES-20261106"
MODULE = "junk_surfaces_2361_v1_20261106"
RULES = {"empty": r"^\s*$", "no_letter": r"^[^A-Za-z]+$", "punctuation_inside": r"[,;:!?]"}
RULES_USE = ("the rules that find a junk surface in the surface list (#2361): empty (nothing or only space), no_letter (no "
             "letter at all: a symbol or a number), punctuation_inside (a comma, semicolon, colon or mark inside the text, so "
             "the surface is a fragment of a clause, not a word or a phrase). Each value is a regular expression matched "
             "against the surface; a surface that matches any rule is junk and is set to soft delete. Read by "
             "iba/app/migration/archive/junk_surfaces_2361_v1_20261106.py and later by the surface step surface.junk_mark")


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    if not has("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='surfaces'"):
        nxt = conn.execute("SELECT COALESCE(MAX(ordinal),0)+1 FROM cfg_enum WHERE name='config_module'").fetchone()[0]
        ops.append(("cfg_enum", "insert", {}, {"name": "config_module", "value": "surfaces", "ordinal": nxt, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_setting WHERE key='surfaces.junk_rules'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "surfaces.junk_rules", "value": json.dumps(RULES), "use": RULES_USE,
                                                  "module": "surfaces", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_write_grant WHERE writer='migration' AND table_name='surface_subgroup' AND database='iba'"):
        ops.append(("cfg_write_grant", "insert", {}, {"writer": "migration", "table_name": "surface_subgroup",
                                                      "database": "iba", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "purpose": f"ONE-OFF migration -- escalation #2361: soft delete of the junk surfaces in surface_subgroup by the "
                       f"rule surfaces.junk_rules; run_id {RUN_ID}.",
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def find_rows(conn, rules: dict) -> list[tuple]:
    pats = [re.compile(p) for p in rules.values()]
    rows = conn.execute("SELECT id, cluster_code, strong, surface, cluster_subgroup_id, status, deleted "
                        "FROM surface_subgroup WHERE deleted=0").fetchall()
    return [r for r in rows if any(p.search(r[3] or "") for p in pats)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--expect-rows", type=int, default=10)
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    # the rule: from config if it is there, else the one this migration is about to register
    cur = conn.execute("SELECT value FROM cfg_setting WHERE key='surfaces.junk_rules'").fetchone()
    rules = json.loads(cur[0]) if cur else RULES
    rows = find_rows(conn, rules)
    surfaces = sorted({r[3] for r in rows})
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s); {len(rows)} live surface_subgroup row(s) on {len(surfaces)} junk surface(s): {surfaces}")
        for r in rows:
            print(f"  id {r[0]} {r[1]} {r[2]} surface={r[3]!r} subgroup {r[4]} status {r[5]}")
        return 0
    if not rows and not ops:
        print("already applied: nothing changed")
        return 0
    if len(rows) != a.expect_rows and rows:
        print(f"REFUSED, nothing written: the rule finds {len(rows)} row(s), {a.expect_rows} were expected "
              f"(--expect-rows); check the rule and the data")
        return 2
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        snap = dbsnapshot.snapshot("pre-2361-junk-surfaces", named=True)
        print(f"named rollback snapshot: {snap}")
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    log = ROOT / "Logs" / f"2361-junk-surfaces-before-{now.replace(':', '')}.json"
    try:
        conn.execute("SAVEPOINT junk_surfaces")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        ids = [r[0] for r in rows]
        if ids:
            conn.execute(f"UPDATE surface_subgroup SET deleted=1, updated_at=?, run_id=? WHERE id IN ({','.join('?' * len(ids))}) "
                         f"AND deleted=0", [now, RUN_ID] + ids)
        left = conn.execute("SELECT count(*) FROM surface_subgroup WHERE deleted=0").fetchone()[0]
        gone = conn.execute(f"SELECT count(*) FROM surface_subgroup WHERE deleted=1 AND run_id=?", (RUN_ID,)).fetchone()[0]
        if gone != len(ids):
            raise RuntimeError(f"set {gone} row(s) to soft delete, expected {len(ids)}")
        conn.execute("RELEASE junk_surfaces")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO junk_surfaces")
        conn.execute("RELEASE junk_surfaces")
        raise
    log.write_text(json.dumps({"run_id": RUN_ID, "at": now, "rules": rules, "rows_before": [
        {"id": r[0], "cluster_code": r[1], "strong": r[2], "surface": r[3], "cluster_subgroup_id": r[4], "status": r[5],
         "deleted": r[6]} for r in rows]}, indent=1), encoding="utf-8")
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); {len(rows)} surface_subgroup row(s) on {len(surfaces)} "
          f"surface(s) set to soft delete {surfaces}; live rows left {left}; before state in {log}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
