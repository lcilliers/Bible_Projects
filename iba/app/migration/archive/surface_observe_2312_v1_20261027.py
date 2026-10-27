"""surface_observe_2312_v1_20261027.py -- escalation #2312: steps 1 to 3 (scope, 0.GAP pre pull, observe) work on the
surface: a word as written in the verse with its Strong (a verse_lexical occurrence), never the word registry. The
researcher, chat 2026-10-27: 'I just want you to build step 1 -3'; 0.GAP pre pulls every existing observation and every
open item for the verses (not filtered by subgroup); Observe adds only what a surface is missing, by the definition agreed
in preparation; the face components are gathered in 0.GAP pre.

Config: reading.focus_words restated (every content word; function words left out by their morph; negators and
connectives kept), reading.surface_requirements (new: what each surface in focus needs), method rules RS-01 and RS-02
on reading.observe, the guides of the gap types open_item and face_not_gathered. The code (iba/app/lib/reading.py,
versecollate.py, observationrecord.py, recordingpass.py) is in the same unit.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive) in the same transaction. Refuses to run
twice (its run_id in cfg_change_detail).

Usage:
    python iba/app/migration/archive/surface_observe_2312_v1_20261027.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2312-SURFACE-OBSERVE-20261027"
MODULE = "surface_observe_2312_v1_20261027"
SRC = "#2312 (researcher, chat 2026-10-27: build steps 1 to 3 on the surface; the observation definition agreed in preparation)"

FOCUS_USE = ("the surfaces in focus at the Observe step (#2312): a surface is a word as written in the verse with its "
             "Strong (a verse_lexical occurrence). In focus: every content word; a function word is left out by its morph "
             "(function_word_morph: OT, the first two letters of the morph code; NT, the part before the first hyphen); "
             "negators and connectives (keep_tags) are kept; every M-coded word and every word in "
             "reading.non_characteristic_strongs is in focus (RG-03, RG-07, RG-22, RG-23, RG-24).")
REQ_USE = ("what each surface in focus needs, #2312: a node with a role (role), a finding of each kind in kinds, or a "
           "silence finding with its reason in place of the kinds in silence_instead_of. Other kinds (party, statement, "
           "link, use, qualification) are recorded where the verse shows them (RG-17). Only what is missing is added.")
RS01 = ("Each surface in focus has a role in the verse, a face and a term reading result (reading.surface_requirements); "
        "a surface with no inner-being bearing has a silence finding with its reason in place of face and term. The Observe "
        "step adds only what a surface is missing; a surface that lacks nothing is not read again.")
RS02 = ("An existing observation counts for a surface when its node names that occurrence (verse_lexical_id), or, with "
        "none, when the node's verse, Strong and surface match one occurrence only. A node that names a verse and no "
        "surface, or matches more than one occurrence, is set aside: it does not count for any surface.")
GUIDE_OPEN_ITEM = ("An open item for the verse, found by the verse and through its surfaces' Strongs and clusters, whatever "
                   "its subgroup; the item shows the subgroups it reaches. Read for what it asks, and record what the "
                   "reading found. It is settled at the claim step.")
GUIDE_FACE = ("A face recorded on a ledger strand hit that no face finding holds on that surface. Link it to the finding "
              "that holds it (the face with its observation), write the face finding, or give the reason. The face story "
              "is built in the claims.")


class Refused(Exception):
    pass


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    row = one("SELECT value FROM cfg_setting WHERE key='reading.focus_words'")
    old = json.loads(row[0])
    ops.append(("cfg_setting", "update", {"key": "reading.focus_words"}, {
        "value": json.dumps({"function_word_morph": old["function_word_morph"], "keep_tags": ["T5", "T6"],
                             "applies": FOCUS_USE}, ensure_ascii=False), "use": FOCUS_USE}))
    if not one("SELECT 1 FROM cfg_setting WHERE key='reading.surface_requirements'"):
        ops.append(("cfg_setting", "insert", {}, {
            "key": "reading.surface_requirements", "module": "reading", "inactive": 0, "use": REQ_USE,
            "value": json.dumps({"role": True, "kinds": ["face", "term"], "silence_instead_of": ["face", "term"]})}))
    gt = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.gap_types'")[0])
    gt["open_item"]["guide"] = GUIDE_OPEN_ITEM
    gt["face_not_gathered"]["guide"] = GUIDE_FACE
    ops.append(("cfg_setting", "update", {"key": "reading.gap_types"}, {"value": json.dumps(gt, ensure_ascii=False)}))
    nid = one("SELECT max(id) FROM cfg_method_rule")[0]
    nord = one("SELECT max(ordinal) FROM cfg_method_rule")[0]
    for key, text in (("RS-01 surface-needs-role-face-term", RS01), ("RS-02 existing-counts-by-occurrence", RS02)):
        if not one("SELECT 1 FROM cfg_method_rule WHERE rule_key=?", key):
            nid += 1
            nord += 1
            ops.append(("cfg_method_rule", "insert", {}, {"id": nid, "step": "reading.observe", "rule_key": key,
                                                          "rule_text": text, "source_doc": SRC, "enforced_by": None,
                                                          "ordinal": nord, "active": 1}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2312: steps 1 to 3 on the surface; run_id {RUN_ID}. "
                       f"inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID} is in cfg_change_detail)")
        return 0
    try:
        ops = plan(conn)
    except Refused as exc:
        print(f"REFUSED, nothing written: {exc}")
        return 2
    summary = ", ".join(f"{t} {op}" for t, op, _, _ in ops)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s): {summary}")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail): {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
