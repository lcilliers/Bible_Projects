"""collection_evidence_report_2477_v1_20261111.py -- escalation #2477: the collection evidence report becomes a reading (Markdown) plus an Excel workbook.

  settings   collection.evidence_catalogue_stages (the retired catalogue observation stages, counted not listed in the Markdown), collection.evidence_text_chars
             (the length a long text is cut to in the Markdown)
  step       collection.evidence: description brought up to date (Markdown report and workbook, no CSV, no -ByType)
  utilities  lib/collectionevidencereport.py, this migration; the purpose of lib/collectionevidence.py brought up to date
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/collection_evidence_report_2477_v1_20261111.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2477-COLLECTION-EVIDENCE-REPORT-20261111"
MODULE = "collection_evidence_report_2477_v1_20261111"
SETTINGS = [
    ("collection.evidence_catalogue_stages", ["verse-reading", "char-subgroup", "char-reading", "char-answers", "char-synergy"],
     "the stages of ib_observation that are the retired September catalogue (cfg_enum ib_observation.stage); the collection evidence report counts their live observations by stage "
     "and tag and lists them only in its workbook (#2477)", "collection"),
    ("collection.evidence_text_chars", 700,
     "the length a long text (an observation, a claim) is cut to in the collection evidence report's Markdown; the workbook holds the whole text (#2477)", "collection"),
]
STEP_DOES = ("write the evidence report of one collection or a comma list (-Collection), or of a verse or list of verses (-Verse, items separated by a semicolon): a Markdown report "
             "(the Strong's codes behind the members, what the study recorded for their occurrences, the claims and the narrative, the phrases, the faults) and an Excel workbook (every "
             "listing in full, one sheet each) under surfaces.exports_root, versioned by the filing rule, the previous live versions archived; verses in Scripture order; no evaluation, "
             "nothing inferred, nothing written to a table; -Check writes no file -- see lib/collectionevidence.py and lib/collectionevidencereport.py (escalations #2464, #2467, #2469, #2477)")
EV_PURPOSE = ("collectionevidence.py -- the data of the evidence report of one collection, a list or a verse list: the stored entries from the base data through observations and claims "
              "into the narrative, read-only on the tables (escalations #2464, #2467, #2477); lib/collectionevidencereport.py writes the Markdown and the workbook from it.")
UTILITIES = [
    ("collectionevidencereport", "iba/app/lib/collectionevidencereport.py", 0, "collectionevidencereport.py -- the Markdown report and the Excel workbook of the collection evidence data: "
     "built up from the Strong's codes behind the members to the observations, claims, narrative, phrases and faults; one workbook sheet for each listing (escalation #2477).", 1,
     "the tunable values (catalogue stages, engagement stage, text length) are read from cfg_setting by the handler; the code holds no tunable value"),
    (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2477: the collection evidence report as a reading plus a workbook; run_id {RUN_ID}.", 1,
     "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations"),
]


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for key, value, use, module in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": json.dumps(value), "use": use, "module": module, "inactive": 0}))
    if not has("SELECT 1 FROM cfg_step WHERE step='collection.evidence' AND does=?", STEP_DOES):
        ops.append(("cfg_step", "update", {"step": "collection.evidence"}, {"does": STEP_DOES}))
    if not has("SELECT 1 FROM cfg_utility WHERE module='collectionevidence' AND purpose=?", EV_PURPOSE):
        ops.append(("cfg_utility", "update", {"module": "collectionevidence"}, {"purpose": EV_PURPOSE}))
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
        for t, op, where, set_ in ops:
            print(" ", t, op, where or set_.get("key") or set_.get("step") or set_.get("module"))
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2477-collection-evidence-report', named=True)}")
    try:
        conn.execute("SAVEPOINT collection_evidence_report")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE collection_evidence_report")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO collection_evidence_report")
        conn.execute("RELEASE collection_evidence_report")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
