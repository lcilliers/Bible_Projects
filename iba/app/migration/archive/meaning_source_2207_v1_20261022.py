"""meaning_source_2207_v1_20261022.py -- escalation #2207 (researcher, 2026-10-22: "meaning_source:
option B, enum of the real sources; the stored text is left until rows are re-run"). The cfg_enum
group ib_observation.meaning_source holds the real sources; cfg_setting
ib_observation.meaning_source_aliases maps each spelling the model has used to its source.
lib/recordingpass.py normalises every new value through both. Stored rows are not touched (rule 68).

Registers itself (inactive, at its own archive path) in the same transaction. Written through
configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/meaning_source_2207_v1_20261022.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2207-MEANING-SOURCE-20261022"
MODULE = "meaning_source_2207_v1_20261022"
GROUP = "ib_observation.meaning_source"
SOURCES = ["strong_meaning_tree", "strong_lexicon.lsj", "strong_lexicon.mounce", "strong_lexicon",
           "verse-text", "role-tags", "cluster", "observations", "n/a"]
ALIASES = {
    "lsj": "strong_lexicon.lsj", "lexicon.lsj": "strong_lexicon.lsj",
    "lsj cross-reference": "strong_lexicon.lsj",
    "mounce": "strong_lexicon.mounce", "lexicon.mounce": "strong_lexicon.mounce",
    "lexicon": "strong_lexicon",
    "text": "verse-text", "verse": "verse-text", "context": "verse-text", "morph data": "verse-text",
    "roles_in_verse": "role-tags", "role list": "role-tags", "role tags": "role-tags",
    "role-context": "role-tags", "role-tag context": "role-tags", "role-tag reading": "role-tags",
    "m0.5": "cluster", "cluster.cluster_code": "cluster", "cluster_codes": "cluster",
    "verse_reading_observations": "observations", "char_subgroup_observations": "observations",
    "char_reading_observations": "observations",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = []
    have = {r[0] for r in conn.execute("SELECT value FROM cfg_enum WHERE name=?", (GROUP,))}
    for i, v in enumerate(SOURCES):
        if v not in have:
            ops.append(("cfg_enum", "insert", {}, {"name": GROUP, "value": v, "ordinal": i, "inactive": 0}))
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key='ib_observation.meaning_source_aliases'").fetchone():
        ops.append(("cfg_setting", "insert", {}, {
            "key": "ib_observation.meaning_source_aliases", "value": json.dumps(ALIASES, sort_keys=True),
            "module": "cluster", "inactive": 0,
            "use": "#2207: each spelling the model has used for a meaning source, mapped to its value in "
                   "cfg_enum ib_observation.meaning_source; lib/recordingpass.normalise_meaning_source "
                   "applies it to every new observation"}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2207: meaning_source sources and aliases, "
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
