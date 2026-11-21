"""stage2_surface_grouping_2526_v1_20261121.py -- escalation #2526 (proposal outputs/escalation/2526-grouping-and-subgrouping-proposal-v1-20261121.md, sections 4.10 and 6; researcher's answers Q1 to Q6).

Stage 2 is reshaped: the unit is the surface, placed whole in one subgroup; the evidence is the meaning of the surface in context (its verses, its codes as possible hidden meanings, stage 1 results),
with the dictionary as a pointer; no split by Strong's code and no concept test (a concept comes into play in stage 4). Written to:
  - cfg_setting group.reading: new `asks`, and sample_verses, max_codes_shown, verse_chars for the working file;
  - cfg_method_rule GP-01 to GP-04 (rule_text only; the keys are kept so that nothing that names them breaks).
Every write is apply_logged. Idempotent.

Usage:
    python iba/app/migration/stage2_surface_grouping_2526_v1_20261121.py [--db PATH]
After a live run, move this file to iba/app/migration/archive/ (rule 96).
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2526-STAGE2-SURFACE-GROUPING-20261121"
ASKS = ("Place each surface, whole, in the subgroup of its meaning: read the surface in its verses (the spread shown), with its codes as possible hidden meanings and, where recorded, the stage 1 "
        "results; the dictionary sense is a pointer, not the basis. Name each subgroup for the kind of meaning its surfaces share and define it in a sentence. Start from the word family "
        "(a family stays together unless its forms differ in meaning). A small collection is one subgroup unless its surfaces differ in kind of meaning. Membership of the collection is settled: "
        "set a surface aside only where it is plainly not a member in meaning, with the reason, and the change procedure moves it out. A surface is never split by Strong's code. Mark a placement "
        "that is open as uncertain and say what is unsettled. Nothing here judges what a word does for the inner being: a concept (a behaviour) comes into play only in stage 4.")
NEW = {"sample_verses": 6, "max_codes_shown": 8, "verse_chars": 300}
RULES = {
    "GP-01": ("The surfaces of a collection are grouped into subgroups by their meaning in context. The unit is the surface (the ESV word); a word family is the default gathering and a form may go to another "
              "subgroup where its meaning differs. The meaning is read from the surface in its verses; a surface may carry a hidden meaning in the different Strong's codes used for it, so the codes are "
              "evidence, and the dictionary meaning (strong_sense, strong_meaning_tree, the lexicons) is a pointer and not the basis. Stage 1 results, where recorded, are part of the evidence. "
              "Membership of the collection is settled and is not re-judged. Nothing in the grouping judges what a word does for the inner being; a concept comes into play only in stage 4 "
              "(researcher, #2463 v16, #2515 v20, #2526 Q1 to Q6, 2026-11-21)."),
    "GP-02": ("A grouping file is checked whole and written in one transaction, or refused: every surface of the collection answered once, every subgroup named once with the meaning it holds and holding a "
              "surface, a surface placed whole in one subgroup (never by Strong's code), a surface set aside with its reason. Each change is a surface_event with its reason."),
    "GP-03": ("A surface plainly not a member of the collection in meaning (a different word that happens to share the spelling, a preposition) is set aside in the index (state isolated) with the reason and is "
              "not grouped; the change procedure moves it out of the collection. A surface whose codes carry different meanings is NOT split and NOT set aside: it stays whole in one subgroup and its codes "
              "are its hidden meanings, recorded in stage 1 and step 1.2. A word that is a function word in every occurrence needs no placement (RG-22)."),
    "GP-04": ("A placement that is open between two subgroups is marked uncertain with what is unsettled and listed in the scrutiny report. The researcher's Subgroup instruction corrects a placement and "
              "wins over Claude's. A small collection is one subgroup by default; a split needs a stated difference in kind of meaning."),
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        row = conn.execute("SELECT value, use FROM cfg_setting WHERE key='group.reading'").fetchone()
        val = json.loads(row[0])
        new = dict(val, asks=ASKS, **NEW)
        if new != val:
            use = row[1] or ""
            if "#2526" not in use:
                use += " Reshaped by #2526 (2026-11-21): a row for each surface, the evidence is the meaning in context (sample_verses verses spread over the codes, at most max_codes_shown codes shown, verse_chars of each verse)."
            apply_logged(conn, RUN_ID, "cfg_setting", "update", {"key": "group.reading"}, {"value": json.dumps(new, ensure_ascii=False), "use": use})
            n += 1
        for key, text in RULES.items():
            r = conn.execute("SELECT id, rule_text FROM cfg_method_rule WHERE rule_key LIKE ? AND step LIKE 'collection.group_record'", (key + " %",)).fetchone()
            if r is None:
                r = conn.execute("SELECT id, rule_text FROM cfg_method_rule WHERE rule_text IS NOT NULL AND id IN (SELECT id FROM cfg_method_rule WHERE rule_key=?)", (key,)).fetchone()
            if r is None:
                raise SystemExit(f"rule {key} not found")
            if r[1] != text:
                apply_logged(conn, RUN_ID, "cfg_method_rule", "update", {"id": r[0]}, {"rule_text": text})
                n += 1
    print(f"{n} cfg write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
