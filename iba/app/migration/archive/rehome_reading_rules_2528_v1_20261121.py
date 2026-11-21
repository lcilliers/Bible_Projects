"""rehome_reading_rules_2528_v1_20261121.py -- escalation #2528 (build brief B6, follow-on of retire_cluster_reading_2528_v1_20261121).

Retiring the steps reading.open, reading.observe, reading.record and reading.reopen left 57 method rules active on steps that are not active, which configmaint.validate refuses (find_rule_scope_gaps).
They are settled by what each is:
  - the rules of how a verse is read and a finding is written, which stage 4 still follows (RG-01 to RG-25, RW-01 to RW-11, RO11, RS-02, RS-04, RS-05, RS-08, RS-10), move to the step
    collection.layer_record, where the stage 4 recorder reads them and the working file carries them;
  - the rules of the retired mechanics (opening a reading on a scope and its objective, the scope JSON, the surface evaluation kept in the JSON, the open items of Analysis_phase_1, reopening a verse;
    RM-01, RM-02, RM-04, RO1 to RO6, RO10, RS-01, RS-03, RS-06, RS-07, RS-09) are made inactive. The evaluation of a surface is replaced by the role of each node (IB-02).
It also registers the two new modules lib/layerinner.py and lib/verseevidence.py in cfg_utility (governance.new_utility_registration_timing).
Every write is apply_logged. Idempotent.

Usage:
    python iba/app/migration/rehome_reading_rules_2528_v1_20261121.py [--db PATH]
After a live run, move this file to iba/app/migration/archive/ (rule 96).
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2528-REHOME-READING-RULES-20261121"
OLD_STEPS = ("reading.open", "reading.observe", "reading.record", "reading.reopen")
MOVE_PREFIX = ("RG-", "RW-", "RO11 ", "RS-02 ", "RS-04 ", "RS-05 ", "RS-08 ", "RS-10 ")
RETIRE_PREFIX = ("RM-01 ", "RM-02 ", "RM-04 ", "RO1 ", "RO2 ", "RO3 ", "RO4 ", "RO5 ", "RO6 ", "RO10 ", "RS-01 ", "RS-03 ", "RS-06 ", "RS-07 ", "RS-09 ")
TARGET = "collection.layer_record"
UTILITIES = (
    ("layerinner", "iba/app/lib/layerinner.py", "layerinner.py -- stage 4 of the study, the inner-being analysis, as steps 3.1 to 3.3 of the layered reading (escalation #2528): the rows, the working file, the recorder and the check of a row.",
     "the steps, items, the observation items each uses, thresholds and the interventions are read from cfg_setting layer.reading, reading.observation_items, reading.observation_rules, reading.node_roles and layer.interventions; the code holds no tunable value"),
    ("verseevidence", "iba/app/lib/verseevidence.py", "verseevidence.py -- the evidence a reader needs on a verse, read from the tables (escalation #2528): the meaning sources of the codes, the verse in its passage and the flags on an earlier observation.",
     "the meaning sources are read from cfg_setting reading.sheet_meaning and the kinds and rules from reading.observation_parts and reading.observation_rules; the code holds no tunable value"),
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = moved = retired = 0
    with conn:
        for rid, step, key, active in conn.execute(f"SELECT id, step, rule_key, active FROM cfg_method_rule WHERE step IN ({','.join('?' * len(OLD_STEPS))}) AND active=1", OLD_STEPS).fetchall():
            if key.startswith(MOVE_PREFIX):
                apply_logged(conn, RUN_ID, "cfg_method_rule", "update", {"id": rid}, {"step": TARGET})
                moved += 1
            elif key.startswith(RETIRE_PREFIX):
                apply_logged(conn, RUN_ID, "cfg_method_rule", "update", {"id": rid}, {"active": 0})
                retired += 1
            else:
                print(f"NOT SETTLED: {rid} {step} {key}")
        for mod, path, purpose, why in UTILITIES:
            if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (mod,)).fetchone():
                apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, {"module": mod, "file_path": path, "purpose": purpose, "inactive": 0, "config_exempt": 1, "config_exempt_reason": why,
                                                                          "crash_escalation_reviewed": 0})
                n += 1
    print(f"{moved} rule(s) moved to {TARGET}, {retired} retired, {n} utility row(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
