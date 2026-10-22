"""rule81_general_2209_v1_20261022.py -- escalation #2209 part (b), rows 1 to 3 (researcher approval
2026-10-22): the start routine delivers and the compliance file restates the general rules only; an
operation's rules reach Claude at its point of use. cfg_behaviour_rule 81
(session-compliance-restated-and-proved) still said every active rule, so its text is amended to
match.

Registers itself (inactive, at its own archive path) in the same transaction. Written through
configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/rule81_general_2209_v1_20261022.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2209-RULE81-GENERAL-20261022"
MODULE = "rule81_general_2209_v1_20261022"
TEXT = ("At every session start Claude writes the session compliance file (Compliance.ps1 -Action "
        "Template, compliance.dir): for every general rule delivered in the session's mode (a "
        "governance setting, behaviour rule or escalation rule with a `general` link in "
        "cfg_rule_scope), what it requires in this session in Claude's own words, or 'not engaged' "
        "with the reason; the acknowledgement (compliance.acknowledgement); and, by id, every rule "
        "in conflict or not followed. Every other rule reaches Claude at the first use of an "
        "operation it governs (.claude/hooks/rules_at_point_of_use.py) and is not restated. "
        "start-project does not end until Compliance.ps1 -Action Check -Phase Start passes. During "
        "the session each engaged rule gains its evidence (a file, #nnnn vN, a commit, a command "
        "output); session-close (SC6) fails on an engaged rule with no evidence or with evidence "
        "that does not check.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = []
    row = conn.execute("SELECT rule_text FROM cfg_behaviour_rule WHERE id=81").fetchone()
    if row and row[0] != TEXT:
        ops.append(("cfg_behaviour_rule", "update", {"id": 81}, {"rule_text": TEXT}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2209: rule 81 text to general-rule delivery, "
                       f"through configmaint.apply_logged under run_id {RUN_ID}. inactive=1 once applied."}))
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    if not ops:
        print("already applied -- skipped")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
