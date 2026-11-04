"""surface_judge_prompt_2354_v2_20261102.py -- escalation #2354 (researcher, chat 2026-11-02, after the pilot of 20:
"designating an entity as a being is being confused with the action of an inner being to be something ... mind is a
difficult one. it could be both. perhaps inner being state must be strengthened to say it designates a particular
status of the inner being. then mind will fall into parts of the human being").

Replaces the text of cfg_setting surface_judge.word_prompt: a being is the entity itself, including a part of the
human being (the heart, the mind, the soul, the spirit), and a word that says what something does, is or undergoes is
not one; an inner_being_state designates a particular status of the inner being itself. The write goes through
configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/surface_judge_prompt_2354_v2_20261102.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2354-SURFACE-JUDGE-PROMPT-20261102"
MODULE = "surface_judge_prompt_2354_v2_20261102"
KEY = "surface_judge.word_prompt"
PROMPT = """You classify one English word or phrase as the ESV Bible uses it, for a study of how Scripture describes the human inner being.
English: "{surface}"

Answer with exactly one group:
- behaviour: something a person does or undergoes, inwardly or outwardly: an act, a feeling, a thought, a speech, a choice. It names the doing or the experience.
- inner_being_state: a word that designates a particular status of the person's inner being itself: a standing condition or characteristic that the inner being is in or has (righteous, wicked, wise, proud, ashamed). It must name a status of the inner being; a word that only says how strong, large, harmful or good something is does not.
- being: an entity, a thing that exists: a person, God, a spirit, an angel, or a part of the human being such as the heart, the mind, the soul or the spirit. A word that says what an entity does, is like or has undergone (mighty, destroyed, made) is not a being, even when it describes one.
- other: everything else

Give behaviour, inner_being_state or being only when the English definitely belongs there as the Bible uses it. If it does not definitely belong in one of those three, or you cannot tell, answer other. Words that only describe, locate or link something (pronouns, prepositions, adverbs, conjunctions, articles, numerals, degree words) and words with no bearing on a person's inner being are other.
Answer JSON only: {"group":"...","reason":null}
"reason" only for other, under 10 words (else null)."""


def plan(conn) -> list[tuple]:
    ops = []
    row = conn.execute("SELECT value FROM cfg_setting WHERE key=?", (KEY,)).fetchone()
    if row is None:
        raise SystemExit(f"REFUSED, nothing written: cfg_setting {KEY} is missing (run the #2354 tool migration first)")
    if json.loads(row[0]) != PROMPT:
        ops.append(("cfg_setting", "update", {"key": KEY}, {"value": json.dumps(PROMPT)}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2354: the surface judging prompt, v2; run_id {RUN_ID}.",
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
            print(f"  {t} {op} {where.get('key') or set_.get('module')}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT sj_prompt")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE sj_prompt")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO sj_prompt")
        conn.execute("RELEASE sj_prompt")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
