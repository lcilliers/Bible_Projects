"""lexical_alignment_2507_v4_20261115.py -- escalation #2507 (design v4 decision D9): the stored alignment check of the lexical work, and the leftovers it found.

  setting     alignment.retired_lexical: the names the study has retired (read by lib/lexicalalignment.py, run by configmaint.validate)
  utility     lexicalalignment (lib/lexicalalignment.py)
  texts       cfg_step report.lexical_exceptions (no longer "from the latest lexical.enrich run", no longer reads verse_lexical_note); cfg_utility lexicalscope (its users)
  scope       B:7, B:8 and B:9 are no longer delivered at VerseLexical.ps1 (it makes no API call; the rules stay for any future API call, their own enforced_by)
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage: python iba/app/migration/lexical_alignment_2507_v4_20261115.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2507-ALIGNMENT-20261115"
MODULE = "lexical_alignment_2507_v4_20261115"
NAMES = ["lexical.meaning", "lexical.relational", "lexical.enrich", "lexical.run", "lexical.notes", "report.lexical_extract", "VerseReading.ps1", "RelationalReading.ps1", "Run-Stage1Batch.ps1",
         "versereadinggenerate", "stage1coverage", "lexicalenrichgenerate", "charanswergenerate", "charreadinggenerate", "subgroupgenerate", "verse_lexical_note"]
USE = ("the names the study has retired in the lexical work (#2507): steps, scripts, generators and the table of the retired Layer 2 notes. The stored alignment check "
       "(lib/lexicalalignment.py, run by configmaint.validate) finds an active config row, a line of USER-GUIDE, GOVERNANCE or CHARTER, or a live module that names one of them without saying it is "
       "retired, and a layer.reading item with no `asks` or a prompt that is not an active catalogue question. A name is added here when something is retired.")
EXCEPTIONS_DOES = ("self-audit of the lexical work over a verse range (#1383, re-founded on the lexical observations, #2507): a tally of the structure (verse_lexical), the observations of "
                   "stage lexical with a node in the range by kind and status, the observations whose basis is read, and the faults in their nodes; read-only against verse_lexical and the lexical observations")
SCOPE_PURPOSE = ("Selector-to-verse-id resolution: a cluster, word, Strong's list or verse list resolves to verse ids via span.strong_variant (exact-token match), never strong_verse. "
                 "Used by lib/clusterstatus.py and handlers/cluster.py (the retired steps lexical.meaning, lexical.relational and cluster.subgroup no longer call it).")


def plan(conn) -> list[tuple]:
    ops = []
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    if not one("SELECT 1 FROM cfg_setting WHERE key='alignment.retired_lexical'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "alignment.retired_lexical", "value": json.dumps(NAMES), "use": USE, "module": "lexical", "inactive": 0}))
    if not one("SELECT 1 FROM cfg_utility WHERE module='lexicalalignment'"):
        ops.append(("cfg_utility", "insert", {}, {"module": "lexicalalignment", "file_path": "iba/app/lib/lexicalalignment.py",
                                                  "purpose": "lexicalalignment.py -- the stored alignment check of the lexical work (#2507, D9): retired names still described as live by config, guidance or code; layer.reading items without asks or with a missing prompt.",
                                                  "inactive": 0, "config_exempt": 1, "config_exempt_reason": "reads its retired names from cfg_setting alignment.retired_lexical; the search patterns and the folders searched are the check itself",
                                                  "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    if one("SELECT does FROM cfg_step WHERE step='report.lexical_exceptions'")[0] != EXCEPTIONS_DOES:
        ops.append(("cfg_step", "update", {"step": "report.lexical_exceptions"}, {"does": EXCEPTIONS_DOES}))
    if one("SELECT purpose FROM cfg_utility WHERE module='lexicalscope'")[0] != SCOPE_PURPOSE:
        ops.append(("cfg_utility", "update", {"module": "lexicalscope"}, {"purpose": SCOPE_PURPOSE}))
    for ref in ("B:7", "B:8", "B:9"):
        r = one("SELECT inactive FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind='ps' AND scope_value='VerseLexical.ps1'", ref)
        if r and not r[0]:
            ops.append(("cfg_rule_scope", "update", {"rule_ref": ref, "scope_kind": "ps", "scope_value": "VerseLexical.ps1"}, {"inactive": 1}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {"module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py",
                                                  "purpose": f"ONE-OFF migration -- escalation #2507: the stored alignment check and the leftovers it found; run_id {RUN_ID}.", "inactive": 1, "config_exempt": 1,
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
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2507-alignment', named=True)}")
    try:
        conn.execute("SAVEPOINT align_2507")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE align_2507")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO align_2507")
        conn.execute("RELEASE align_2507")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
