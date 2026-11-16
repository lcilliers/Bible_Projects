"""lexical_reports_2507_v3_20261115.py -- escalation #2507: the two lexical reports of Window 1 Layer 2 after the retirement of lexical.enrich.

  report.lexical_exceptions   adjusted, not retired (the self-audit of Window 1, #1383 (g)): its sections now read the lexical observations (stage lexical) and their nodes in place
                              of the retired verse_lexical_note; title and section headings reworded (handlers/reports.py lexical_exceptions_report)
  report.lexical_extract      retired: the downstream input by collection is the collection evidence report, which lists every live observation with a node on the verses of a
                              collection (sheet Verse observations); its step and its two output settings inactive (the handler is removed from handlers/reports.py)
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage: python iba/app/migration/lexical_reports_2507_v3_20261115.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2507-LEXICAL-REPORTS-20261115"
MODULE = "lexical_reports_2507_v3_20261115"
SECTIONS = {"layer1_tally": ("## Structure tally (verse_lexical, mechanical, complete enumeration)", "Structure tally"),
            "layer2_dispositions": ("## Lexical observations with a node in this range (by kind and status)", "Lexical observations"),
            "judgement_calls": ("## Judgement calls: the observations whose basis is read", "Judgement calls"),
            "integrity": ("## Integrity check (nodes of the lexical observations)", "Integrity check")}


def plan(conn) -> list[tuple]:
    ops = []
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    title = "{book} {range} -- lexical exceptions report (the lexical work: structure and observations)"
    if one("SELECT title FROM cfg_report WHERE step='report.lexical_exceptions'")[0] != title:
        ops.append(("cfg_report", "update", {"step": "report.lexical_exceptions"}, {"title": title}))
    for key, (heading, toc) in SECTIONS.items():
        r = one("SELECT heading, toc_label FROM cfg_report_section WHERE step='report.lexical_exceptions' AND section_key=?", key)
        if r and (r[0] != heading or r[1] != toc):
            ops.append(("cfg_report_section", "update", {"step": "report.lexical_exceptions", "section_key": key}, {"heading": heading, "toc_label": toc}))
    r = one("SELECT inactive FROM cfg_step WHERE step='report.lexical_extract'")
    if r and not r[0]:
        ops.append(("cfg_step", "update", {"step": "report.lexical_extract"}, {"inactive": 1}))
    for k in ("report.lexical_extract_output_dir", "report.lexical_extract_output_pattern"):
        r = one("SELECT inactive FROM cfg_setting WHERE key=?", k)
        if r and not r[0]:
            ops.append(("cfg_setting", "update", {"key": k}, {"inactive": 1}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py",
                                                  "purpose": f"ONE-OFF migration -- escalation #2507: the lexical reports adjusted and retired; run_id {RUN_ID}.", "inactive": 1, "config_exempt": 1,
                                                  "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(" ", t, op, where)
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2507-reports', named=True)}")
    try:
        conn.execute("SAVEPOINT reports_2507")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE reports_2507")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO reports_2507")
        conn.execute("RELEASE reports_2507")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
