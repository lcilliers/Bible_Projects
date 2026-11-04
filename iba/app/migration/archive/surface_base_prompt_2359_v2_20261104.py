"""surface_base_prompt_2359_v2_20261104.py -- escalation #2359 (researcher, chat 2026-11-04: "Amend, then run").

Amends the question of the base-form step (cfg_setting surface_judge.base_prompt) after the pilot of 20 words
(base-form-pilot-v1-20261104.jsonl): beloved gave belove (not a word), strife gave strive as an inflection (a
different word form, not an ending), undoing gave undo (the meaning has moved). The amended question says: the base
must be a real English word in ordinary use; an inflection is a change of the ending alone, a different word form is a
derivation; a word whose meaning has moved from its base answers none. Registers this script in cfg_utility
(inactive, at its archive path). cfg_* writes go through configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/surface_base_prompt_2359_v2_20261104.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2359-SURFACE-BASE-PROMPT-20261104"
MODULE = "surface_base_prompt_2359_v2_20261104"
KEY = "surface_judge.base_prompt"
PROMPT = """You give the base form of one English word as the ESV Bible uses it, for a study of how Scripture describes the human inner being.
English: "{surface}"

Give a base word only when the English is an inflected or derived form of it AND the two share the same root meaning. The base must be a real English word in ordinary use.
- inflection: only the grammatical ending changes (tense, plural, participle, comparative), including irregular forms (sought: seek; wept: weep; grew: grow).
- derivation: a different word form made with a suffix or prefix, such as a noun from a verb or an adjective, and the core meaning stays the same (wonderful: wonder; strife: strive).
- none, with the word itself as the base: an opposite (unfaithful, faithless), a different word that only looks similar (lying is not lye), a word whose meaning has moved away from its base (undoing is not undo), a word with no base, and any base that is not a real word.
Answer JSON only: {"base":"...","relation":"inflection|derivation|none","reason":null}
"reason" only when relation is none and the word looks derived: under 10 words (else null)."""


def plan(conn) -> list[tuple]:
    ops = []
    row = conn.execute("SELECT value FROM cfg_setting WHERE key=?", (KEY,)).fetchone()
    if row is None:
        raise SystemExit(f"cfg_setting {KEY} does not exist: run surface_base_2359_v1_20261104 first")
    if json.loads(row[0]) != PROMPT:
        ops.append(("cfg_setting", "update", {"key": KEY}, {"value": json.dumps(PROMPT)}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "purpose":
            f"ONE-OFF migration -- escalation #2359: amends the base-form question after the pilot; run_id {RUN_ID}.",
            "inactive": 1, "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        for t, op, where, set_ in ops:
            print(f"  {t} {op} {where or set_.get('module')}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT surface_base_prompt")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE surface_base_prompt")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_base_prompt")
        conn.execute("RELEASE surface_base_prompt")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
