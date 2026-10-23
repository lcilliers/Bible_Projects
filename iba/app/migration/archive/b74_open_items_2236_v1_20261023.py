"""b74_open_items_2236_v1_20261023.py -- escalation #2236: rule B:74 (open threads carried as escalations) brought in
line with B:115 and the researcher's instruction of 2026-10-23 ("Adjust esclations to make the management of the
open items more productive.  The last think we need is to have to approve each and every open item through a
standard escalation process."): items are registered and reworded through Open-Item.ps1, one read purpose each,
and no thread or item has an approval step.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path) in the same
transaction. Idempotent.

Usage:
    python iba/app/migration/b74_open_items_2236_v1_20261023.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2236-B74-20261023"
MODULE = "b74_open_items_2236_v1_20261023"
OLD = [("Its items (escalation_thread_item; cluster, Strong's, verse, strand, chapter, event, researcher, escalation) are "
        "what a strand or task is matched against (Escalation.ps1 -Action Match).",
        "Its items (escalation_thread_item) are registered and reworded through Open-Item.ps1, each to one read purpose "
        "(rule B:115: a face or perspective, its target scoped to the verses and strongs of that purpose, what to read "
        "for, why it is open, when it comes back); items of the older kinds (cluster, Strong's, verse, strand, chapter, "
        "event, researcher, escalation) are reworded to that form. Items are what a strand, task or reading is matched "
        "against (Escalation.ps1 -Action Match; a worded item on its target verses)."),
       ("and there is no approval step.", "and there is no approval step, for a thread or for any item.")]


def plan(conn) -> list[tuple]:
    ops = []
    text = conn.execute("SELECT rule_text FROM cfg_behaviour_rule WHERE id=74").fetchone()[0]
    new = text
    for a, b in OLD:
        if b not in new:
            if a not in new:
                raise SystemExit(f"B:74 does not hold the expected text: {a[:60]!r}")
            new = new.replace(a, b)
    if new != text:
        ops.append(("cfg_behaviour_rule", "update", {"id": 74}, {"rule_text": new}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same "
                                    "class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2236: rule B:74 text in line with B:115 (items through "
                       f"Open-Item.ps1, no approval step for any item); run_id {RUN_ID}. inactive=1 once applied."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run or not ops:
        print(f"{'DRY RUN -- ' if a.dry_run else 'already applied -- '}{len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
