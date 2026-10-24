"""style_guide_2272_v1_20261024.py -- escalation #2272 (#2268 W-2): the narrative style guide
(Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md) as method rules RN-08 to RN-15 on
reading.apply and four quality checks on reading.check; cfg_setting narrative.inner_being_style_guide_path and its
scope link retired; B:69's enforced_by and the control map's study_method no longer name the guide; the guide is
then archived (#2268 R1, R4).

Carried: sec 1 (the 'I read' limit; the rest of sec 1 is B:69), sec 2 to 7, 7a, and the checks of sec 8. Not carried:
sec 0 and 10 to 11 (history), sec 8.5 records (version bump, structure log: the register keeps them), sec 9 (chapter
drafts as files and Claude not writing narrative: superseded by R4, RN-01, RN-02). The withdrawn examples of sec 1.2
go to the worked examples (build B10).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Refuses to
run twice.

Usage:
    python iba/app/migration/style_guide_2272_v1_20261024.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2272-STYLE-GUIDE-20261024"
MODULE = "style_guide_2272_v1_20261024"
SRC = "Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md (archived); #2272, #2268 R1, R4"

RULES = [
    ("RN-08 i-read-limit", "A narrator's reading ('I read this as …') restates or paraphrases what the cited text "
     "itself says, and is never a licence for synthesis. A new insight found while writing goes to an observation "
     "first (B:69).", "guide sec 1"),
    ("RN-09 five-prohibited-patterns", "Five patterns are never written: (1) literary framing with no source (render "
     "the verse, drop the framing); (2) a superlative not counted (omit it, or state the count made and its scope); "
     "(3) a comparative claim with no evidence (omit the comparative half); (4) premature closure, 'this verse settles "
     "it' (present it as evidence, the question stays open); (5) a claim that conflicts with the data, a wrong verse, "
     "word or sense (correct the source first).", "guide sec 2"),
    ("RN-10 voice", "First person singular ('I', never 'we'), personal, direct, easy to read. Testimony, not report: "
     "grounded and morally serious, never clinical; reverent without being devotional; no sermon, no liturgical "
     "phrasing. Plain short declaratives, no padding or signposting. Confident where the verse is plain; open where it "
     "is open ('the text does not say', 'we are not told why'), never hedging plain evidence. Written for a general "
     "reader who knows no Hebrew or Greek and has no interest in how the work was done.", "guide sec 3"),
    ("RN-11 words-and-terms", "Never in the narrative: cluster, M-code, characteristic code, tier, phase, batch, "
     "strand, stream, ledger, node, observation, finding, Strong's number, sub-group, seat-sense, 'this study found', "
     "'our analysis', or anything describing how the work was done. Write 'the verses show' or 'Scripture says' for a "
     "finding; heart, soul or spirit for a seat; 'commanded', 'forbidden', 'good', 'evil' for valence; plain "
     "quantifiers for counts ('in almost every instance', 'the single exception'), and only where counted. A Hebrew or "
     "Greek word always appears with its gloss.", "guide sec 4"),
    ("RN-12 evidence-and-citation", "Every claim rests on a cited verse: a claim with no citable ground is not written. "
     "References give the full book name in the text ('Proverbs 15:1'), then verse numbers alone after the first "
     "reference to a chapter ('(15:18)'); several witnesses are separated by semicolons. A lone occurrence is stated as "
     "such; convergence across verses is what lets a point stand. Open threads stay open, and where two passages pull "
     "opposite ways both are shown.", "guide sec 5"),
    ("RN-13 silence", "A silence is named only when it carries weight: an expectation set and not met, or an absence "
     "that gives the thing its shape. A routine absence needs no comment, and silences are never listed as an "
     "inventory.", "guide sec 6"),
    ("RN-14 structure-and-format", "The narrative's shape follows the evidence, not a template; an activity section "
     "has no fixed sub-headings and ends with Connections. Prose supported by bullets: a passage opens in prose with "
     "the point in a sentence or two, bullets then carry its applications (the verses, cases, faces), a bullet list "
     "never stands without its prose introduction, and argument and connection stay in the prose. A title names the "
     "subject only ('The soul', 'Thinking'), never a label that characterises it, since a characterisation is a "
     "statement that must be founded on Scripture in the text.", "guide sec 7"),
    ("RN-15 external-parties", "Any external party a verse brings in (God, the Spirit, other spirits, angels, another "
     "person, a crowd, food, wine, a place, an object, an event) is dealt with in relation to the phenomenon the verse "
     "describes, each in its own terms and with its role as the verse gives it (God hardens, gives, stirs, strikes, "
     "restrains; the Spirit rushes upon, is put within, is grieved; an angel stands in the way; a brother provokes; "
     "wine makes the heart merry), never merged into a generic outside influence and never watered down. It is named "
     "in the observation's parties and appears in the block with the phenomenon. A chapter on other entities may grow "
     "from what the readings record; it is not started as a whole-scope task.", "guide sec 7a"),
]
CHECKS = [
    ("let-scripture-speak-pass", "Has every 'I read / I take / I find', every 'so', 'therefore', 'this shows', every "
     "superlative, and every sentence that joins two verses into a claim been kept only where a cited verse says it?",
     "reasonableness"),
    ("external-party-check", "For each verse used, has every external party it brings in been dealt with in relation "
     "to the phenomenon, in its own terms (RN-15)?", "existence"),
    ("format-check", "Does every bullet list have its prose introduction, and is every title a plain subject (RN-14)?",
     "existence"),
    ("self-review", "Is the text free of repetition, overreach (a claim beyond what the cited verse carries), padding "
     "and tonal drift (devotional phrasing, project words)?", "reasonableness"),
]
CONTROL_HOME = ("cfg_method_rule (steps reading.open, reading.record, reading.check, reading.apply; word.read and "
                "cluster.read when built), cfg_quality_check (reading.check), cfg_setting reading.*, with "
                "cfg_prose_concept pointers to the glossary")


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    nid = one("SELECT max(id) FROM cfg_method_rule")[0]
    base = one("SELECT coalesce(max(ordinal),0) FROM cfg_method_rule WHERE step='reading.apply'")[0]
    for i, (key, text, sec) in enumerate(RULES, 1):
        if not one("SELECT 1 FROM cfg_method_rule WHERE rule_key=?", key):
            nid += 1
            ops.append(("cfg_method_rule", "insert", {}, {"id": nid, "step": "reading.apply", "rule_key": key,
                                                          "rule_text": text, "source_doc": f"{sec}; {SRC}",
                                                          "enforced_by": None, "ordinal": base + i, "active": 1}))
    qid = one("SELECT max(id) FROM cfg_quality_check")[0]
    qbase = one("SELECT coalesce(max(ordinal),0) FROM cfg_quality_check WHERE step='reading.check'")[0]
    for i, (key, q, kind) in enumerate(CHECKS, 1):
        if not one("SELECT 1 FROM cfg_quality_check WHERE step='reading.check' AND check_key=?", key):
            qid += 1
            ops.append(("cfg_quality_check", "insert", {}, {"id": qid, "step": "reading.check", "check_key": key,
                                                            "question": q, "test_kind": kind, "required": 1,
                                                            "enforced_by": None, "ordinal": qbase + i, "active": 1}))
    ops.append(("cfg_setting", "update", {"key": "narrative.inner_being_style_guide_path"}, {"inactive": 1}))
    for (sid,) in conn.execute("SELECT id FROM cfg_rule_scope WHERE rule_ref='G:narrative.inner_being_style_guide_path' "
                               "AND inactive=0").fetchall():
        ops.append(("cfg_rule_scope", "update", {"id": sid}, {"inactive": 1}))
    ops.append(("cfg_behaviour_rule", "update", {"id": 69}, {
        "enforced_by": "Context-delivered at session start (rule 81) and at first use of Reading.ps1 (cfg_rule_scope); "
                       "the narrative form is method rules RN-08 to RN-15 and the let-scripture-speak quality check on "
                       "reading.check (#2272)."}))
    ops.append(("cfg_control_home", "update", {"kind": "study_method"}, {"home": CONTROL_HOME}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2272 (#2268 W-2): the narrative style guide as method rules "
                       f"RN-08 to RN-15 and four quality checks; its setting retired; run_id {RUN_ID}."}))
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
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
