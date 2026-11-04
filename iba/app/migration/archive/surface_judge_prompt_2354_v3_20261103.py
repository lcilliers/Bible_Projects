"""surface_judge_prompt_2354_v3_20261103.py -- escalation #2354 (researcher, chat 2026-11-03: "In the next briefing
pack, avoid using the word 'being' to refer to human, natural entities such as plants or animals, god in all its
forms, unseen powers such as spirits, angels, and similar entities. include words that refer to parts of the above
entities"; and, 2026-11-02, mighty, power and destroyed are inner_being_state).

The group stored as `being` is named `entity` to the model: cfg_setting surface_judge.groups becomes the names the
model is given, the new surface_judge.group_stored_as maps entity to being, and surface_judge.word_prompt is
replaced (version 3): an entity is a human, a natural entity such as a plant or an animal, God in all its forms, an
unseen power such as a spirit or an angel, or a similar entity, and a word for a part of any of them; a state is a
standing condition or characteristic of the person or the inner being, not limited to moral status. The enums and
the stored values keep `being`. The writes go through configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/surface_judge_prompt_2354_v3_20261103.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2354-SURFACE-JUDGE-PROMPT-V3-20261103"
MODULE = "surface_judge_prompt_2354_v3_20261103"
GROUPS = ["behaviour", "inner_being_state", "entity", "other"]
STORED_AS = {"entity": "being"}
GROUPS_USE = ("the groups of the first split of the concept surfaces (#2354) as the model is told them: behaviour, "
              "inner_being_state, entity (stored as being, see surface_judge.group_stored_as), or other. The model "
              "answers one of them; the surface goes to the first three only when it definitely belongs there, "
              "otherwise to other, which the researcher cleans up in a later pass")
STORED_USE = ("the groups whose name given to the model differs from the group stored (#2354, researcher 2026-11-03: "
              "the word being is not used in the briefing for the group of entities): {name given to the model: "
              "group stored}, each key one of surface_judge.groups")
PROMPT = """You classify one English word or phrase as the ESV Bible uses it, for a study of how Scripture describes the human inner being.
English: "{surface}"

Answer with exactly one group:
- behaviour: something a person does or undergoes, inwardly or outwardly: an act, a feeling, a thought, a speech, a choice. It names the doing or the experience.
- inner_being_state: a standing condition or characteristic of a person or of a person's inner being: what the person is like or is in (righteous, wicked, wise, proud, humble, able, weak, broken). It is a condition the person is in or has, not an act and not a thing.
- entity: a thing that exists: a human, a natural entity such as a plant or an animal, God in all the forms the Bible gives, an unseen power such as a spirit or an angel, or any similar entity; and a word that names a part of any of these (for example a part of a person, of a plant or of an animal). A word that says what an entity does, is like or has undergone is not an entity, even when it describes one.
- other: everything else

Give behaviour, inner_being_state or entity only when the English definitely belongs there as the Bible uses it. If it does not definitely belong in one of those three, or you cannot tell, answer other. Words that only describe, locate or link something (pronouns, prepositions, adverbs, conjunctions, articles, numerals, degree words) and words with no bearing on a person's inner being are other.
Answer JSON only: {"group":"...","reason":null}
"reason" only for other, under 10 words (else null)."""


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for key, want, use in (("surface_judge.groups", GROUPS, GROUPS_USE), ("surface_judge.word_prompt", PROMPT, None)):
        row = conn.execute("SELECT value, use FROM cfg_setting WHERE key=?", (key,)).fetchone()
        if row is None:
            raise SystemExit(f"REFUSED, nothing written: cfg_setting {key} is missing (run the #2354 tool migration)")
        if json.loads(row[0]) != want:
            ops.append(("cfg_setting", "update", {"key": key},
                        {"value": json.dumps(want)} | ({"use": use} if use else {})))
    if not has("SELECT 1 FROM cfg_setting WHERE key='surface_judge.group_stored_as'"):
        ops.append(("cfg_setting", "insert", {}, {"key": "surface_judge.group_stored_as",
                                                  "value": json.dumps(STORED_AS), "use": STORED_USE,
                                                  "module": "surface_judge", "inactive": 0}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2354: the surface judging prompt v3 and the group name "
                       f"entity; run_id {RUN_ID}.", "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
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
            print(f"  {t} {op} {where.get('key') or set_.get('key') or set_.get('module')}")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    try:
        conn.execute("SAVEPOINT sj_prompt3")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE sj_prompt3")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO sj_prompt3")
        conn.execute("RELEASE sj_prompt3")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
