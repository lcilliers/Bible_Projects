"""retire_lexical_chain_2507_v1_20261115.py -- escalation #2507 (researcher, 2026-11-15: "you still need to process the replaced or retired stuff"; design
outputs/escalation/2507-lexical-observations-by-collection-alignment-and-design-v4-20261115.md sections 5 and 10).

Retires the cluster-based lexical steps and the generation chain that only they and the retired cluster stages (#2299) used:
  steps       lexical.meaning, lexical.relational (inactive)
  grants      the six write grants of those two steps (inactive)
  settings    lexical.meaning_max_verses_per_batch, lexical.relational_max_verses_per_batch, report.stage1_coverage_validation_pattern and the nine lexical.llm_*
              keys, read only by the retired generators (inactive)
  utilities   versereadinggenerate, stage1coverage, lexicalenrichgenerate, charanswergenerate, charreadinggenerate, subgroupgenerate and the three front doors
              ps_versereading, ps_relationalreading, ps_run_stage1batch: inactive, their path pointing into archive/ (the files are moved by the same run)
The import trace before this migration (2026-11-15): the six libraries are imported only by one another, by handlers/lexical.py meaning and relational and by handlers/cluster.py
subgroup, reading and answer, all removed in the same unit of work; lexicalscope, clusterstatus, recordingpass and batchcontrol are used elsewhere and stay.
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage: python iba/app/migration/retire_lexical_chain_2507_v1_20261115.py [--db PATH] [--dry-run] [--no-snapshot] [--no-move]
"""
import argparse
import pathlib
import shutil
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2507-RETIRE-LEXICAL-CHAIN-20261115"
MODULE = "retire_lexical_chain_2507_v1_20261115"
STEPS = ["lexical.meaning", "lexical.relational"]
GRANTS = [(w, t) for w in STEPS for t in ("ib_node", "ib_observation", "run_batch")]
SETTINGS = ["lexical.meaning_max_verses_per_batch", "lexical.relational_max_verses_per_batch", "report.stage1_coverage_validation_pattern",
            "lexical.llm_api_url", "lexical.llm_api_version", "lexical.llm_chars_per_token", "lexical.llm_model", "lexical.llm_max_output_tokens",
            "lexical.llm_rate_input_per_million", "lexical.llm_rate_output_per_million", "lexical.llm_max_cost_per_batch", "lexical.llm_usage_log_path"]
UTILITIES = {"versereadinggenerate": "lib", "stage1coverage": "lib", "lexicalenrichgenerate": "lib", "charanswergenerate": "lib", "charreadinggenerate": "lib", "subgroupgenerate": "lib",
             "ps_versereading": "ps", "ps_relationalreading": "ps", "ps_run_stage1batch": "ps"}
FILES = [("lib", "versereadinggenerate.py"), ("lib", "stage1coverage.py"), ("lib", "lexicalenrichgenerate.py"), ("lib", "charanswergenerate.py"),
         ("lib", "charreadinggenerate.py"), ("lib", "subgroupgenerate.py"), ("ps", "VerseReading.ps1"), ("ps", "RelationalReading.ps1"), ("ps", "Run-Stage1Batch.ps1")]


def plan(conn) -> list[tuple]:
    ops = []
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    for s in STEPS:
        r = one("SELECT inactive FROM cfg_step WHERE step=?", s)
        if r and not r[0]:
            ops.append(("cfg_step", "update", {"step": s}, {"inactive": 1}))
    for w, t in GRANTS:
        r = one("SELECT inactive FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", w, t)
        if r and not r[0]:
            ops.append(("cfg_write_grant", "update", {"writer": w, "table_name": t, "database": "iba"}, {"inactive": 1}))
    for k in SETTINGS:
        r = one("SELECT inactive FROM cfg_setting WHERE key=?", k)
        if r and not r[0]:
            ops.append(("cfg_setting", "update", {"key": k}, {"inactive": 1}))
    for m, kind in UTILITIES.items():
        r = one("SELECT file_path, purpose, inactive FROM cfg_utility WHERE module=?", m)
        if r and not r[2]:
            name = pathlib.PurePosixPath(r[0]).name
            ops.append(("cfg_utility", "update", {"module": m}, {"inactive": 1, "file_path": f"iba/app/{kind}/archive/{name}",
                                                                 "purpose": f"Retired (#2507): not in a utility or module. Was {r[0]}. " + (r[1] or "")[:300]}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py",
                                                  "purpose": f"ONE-OFF migration -- escalation #2507: the cluster-based lexical steps and their generation chain retired; run_id {RUN_ID}.",
                                                  "inactive": 1, "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    ap.add_argument("--no-move", action="store_true", help="for a test copy: do not move the files")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    moves = [(ROOT / "iba" / "app" / d / f, ROOT / "iba" / "app" / d / "archive" / f) for d, f in FILES if (ROOT / "iba" / "app" / d / f).exists()]
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s); {len(moves)} file(s) to move")
        for t, op, where, set_ in ops:
            print(" ", t, op, where)
        return 0
    if not ops and not moves:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2507-retire', named=True)}")
    try:
        conn.execute("SAVEPOINT retire_2507")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE retire_2507")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO retire_2507")
        conn.execute("RELEASE retire_2507")
        raise
    if not a.no_move:
        for src, dst in moves:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s); {0 if a.no_move else len(moves)} file(s) moved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
