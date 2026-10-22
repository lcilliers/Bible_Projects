"""narrative_home_2172_v1_20261022.py -- escalation #2172: the governance ruling the reading process
design v2 option B needs (design sec 4: "needs a governance setting: the study's narrative is kept
with its claims in iba.db"), approved by the researcher on 2026-10-22 ("sounds good to proceed with
the build", with the note that prose_section's programme and glossary prose stay live).

- cfg_setting governance.narrative_home states it; linked in cfg_rule_scope to the two tools that
  write the narrative and to the narrative folder.
- cfg_control_home: study_state names the narrative's blocks as part of its home; study_output no
  longer calls the chapter files "the narrative itself" (they are exports).

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path).
Idempotent.

Usage:
    python iba/app/migration/narrative_home_2172_v1_20261022.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2172-NARRATIVE-HOME-20261022"
MODULE = "narrative_home_2172_v1_20261022"
KEY = "governance.narrative_home"
VALUE = ("The inner-being narrative is kept in iba.db with its claims: each chapter as blocks "
         "(narrative_section.block_text, a heading and its text) and each claim told by a block "
         "(narrative_claim_telling). The chapter files in narrative.copy_source_dir are exports written from the "
         "database; the narrative is written through Strand-Reading.ps1 -Step Rewrite and the block actions of "
         "Narrative-Register.ps1, never in a chapter file. bible_research.db prose_section keeps the programme and "
         "glossary prose, which stay live.")
USE = ("researcher 2026-10-22 on escalation #2172 (reading process design v2, option B, approved: \"sounds good to "
       "proceed with the build\"; prose_section's programme and glossary prose are not dead)")
SCOPES = [("ps", "Narrative-Register.ps1"), ("ps", "Strand-Reading.ps1"), ("path", "_analytics/essay/**")]
HOMES = {
    "study_state": {"home": "escalation (strand escalations and type=thread items), narrative_chapter, the narrative "
                            "claim register tables, the narrative's blocks (narrative_section.block_text; "
                            "governance.narrative_home), the reading_strand tables"},
    "study_output": {"description": "The study's working files, and the narrative chapters as exported from iba.db "
                                    "(governance.narrative_home).",
                     "home": "_analytics/ (cluster folders per report.cluster_folder_naming_convention; the exported "
                             "narrative chapters in _analytics/essay/spirit_soul_body/inner-being-narrative/); "
                             "outputs/strand-reading/ (each strand's context, gather and account files)"},
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    ops = []
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (KEY,)).fetchone():
        ops.append(("cfg_setting", "insert", {}, {"key": KEY, "value": json.dumps(VALUE), "use": USE,
                                                  "module": "governance", "inactive": 0}))
    for kind, value in SCOPES:
        if not conn.execute("SELECT 1 FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind=? AND scope_value=?",
                            (f"G:{KEY}", kind, value)).fetchone():
            ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": f"G:{KEY}", "scope_kind": kind,
                                                         "scope_value": value, "inactive": 0}))
    for kind, sets in HOMES.items():
        cur = conn.execute("SELECT * FROM cfg_control_home WHERE kind=?", (kind,)).fetchone()
        change = {k: v for k, v in sets.items() if cur[k] != v}
        if change:
            ops.append(("cfg_control_home", "update", {"kind": kind}, change))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2172: governance.narrative_home, its rule links, the "
                       f"control map's study rows; run_id {RUN_ID}. inactive=1 once applied."}))
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
