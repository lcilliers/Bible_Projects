"""analysis_phase_1_2329_v1_20261030.py -- escalation #2329: Phase 1 observations fit for purpose.

Design: outputs/escalation/2329-phase-1-fit-for-purpose-design-v1-20261030.md (approved by the researcher, chat 2026-10-30:
'Approve #2329'; build: '#2329 build'). Config first (governance.rules_must_be_config_driven), then the code that reads it:
- reading.observation_parts: the parts of an observation of a relevant surface gain `before` (what the verse states of the prompt, state or
  purpose before the act) and `after` (what follows the act, cited by reference when it is in the next verse); `party_form` names the shape
  of a stated party: the sentence and the kind of the one who acts and of the one acted on, from cfg_enum party_kind;
- reading.sheet_meaning (new): the meaning data the Observe sheet carries for each surface (tree, sense head, STEP gloss, related words,
  and for Greek the lexicon);
- cfg_method_rule RS-08 restated to name the new parts.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.

Usage:
    python iba/app/migration/analysis_phase_1_2329_v1_20261030.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2329-PHASE1-FIT-FOR-PURPOSE-20261030"
MODULE = "analysis_phase_1_2329_v1_20261030"
SRC = "#2329 (researcher, chat 2026-10-30)"

NEW_PARTS = {"before": "content", "after": "enactment"}      # the new part, placed after this existing one
PARTY_FORM = {"keys": ["text", "acts", "acted_on"], "kind_keys": ["acts", "acted_on"], "kind_enum": "party_kind"}
SHEET_MEANING = {
    "tree": True,
    "sense": True,
    "step_gloss": True,
    "related": True,
    "lexicon": {"testaments": ["NT"], "columns": ["lsj", "mounce"]},
}
SHEET_MEANING_USE = (
    "the meaning data the Observe sheet of Analysis_phase_1 carries for each surface of a verse (#2329): tree = the meaning tree rows "
    "(strong_meaning_tree, by the exact code); sense = the sense head (strong_sense); step_gloss = the STEP gloss (strong.stepGloss); "
    "related = the related words (strong_related); lexicon = the lexicon columns (strong_lexicon) for the testaments named (Greek). One "
    "set-based query per table over the codes of the verses in hand (B:71). Read by iba/app/lib/reading.py _sheets")
RS08_ADD = (" The observation also holds `before` (what the verse states of the prompt, state or purpose before the act) and `after` (what "
            "follows the act: the answer, result or response, cited by reference when it is in the next verse), each in words or stated "
            "absent with the reason; a stated party holds the sentence and the kind of the one who acts and of the one acted on "
            "(reading.observation_parts party_form; cfg_enum party_kind) (#2329).")


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    cur = json.loads(one("SELECT value FROM cfg_setting WHERE key='reading.observation_parts'")[0])
    parts = list(cur["parts"])
    changed = False
    for new, after_ in NEW_PARTS.items():
        if new not in parts:
            parts.insert(parts.index(after_) + 1, new)
            changed = True
    if "party_form" not in cur:
        cur["party_form"] = PARTY_FORM
        changed = True
    if changed:
        cur["parts"] = parts
        ops.append(("cfg_setting", "update", {"key": "reading.observation_parts"}, {"value": json.dumps(cur)}))
    if not one("SELECT 1 FROM cfg_setting WHERE key='reading.sheet_meaning'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "reading.sheet_meaning", "value": json.dumps(SHEET_MEANING),
                                                  "use": SHEET_MEANING_USE, "module": "reading", "inactive": 0}))
    row = one("SELECT id, rule_text FROM cfg_method_rule WHERE rule_key LIKE 'RS-08 %' AND active=1")
    if row and "`before`" not in row[1]:
        ops.append(("cfg_method_rule", "update", {"id": row[0]}, {"rule_text": row[1] + RS08_ADD, "source_doc": SRC}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class "
                                    "as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2329: the before and after parts, the typed party and the meaning data on the "
                       f"Observe sheet; run_id {RUN_ID}. inactive=1 once applied."}))
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
