"""add_healing_word_strong_20260810.py — ONE-OFF: link the curated healing-domain Strong's list to
the new `healing` registry word (id 184, created via `registry.create` this same session — see
`iba/app/reports/healing-words-in-study-check-20260810.md` for how this exact list was derived).

Deliberately NOT run through `raw.discover` (STEP's own `call1_meanings("healing")` auto-search) —
the researcher's own curated Hebrew+Greek list is the source of truth here, not whatever STEP's
reverse-dictionary search for the English string "healing" would independently return (which was
never checked and could easily diverge from this list). `strong`/`span`/`verse_lexical` already
carry full data for every code below (confirmed live before writing this — this DB's lexical layer
is a whole-Bible build, not scoped to word-registry onboarding, so no `raw.detail_one`/
`verses_one` pull is needed the way `allocate_strongs.py` needed one for its own, different case).

Two groups, per the researcher's own instruction ("add all the missing hebrew and greek words to
it... create the cross registry items for the strong already in other registries also"):
  - NEW: codes with no existing registry link at all before this.
  - CROSS: codes already linked to one or more OTHER registry words — this adds a second (or
    further) `word_strong` row under `healing`, the same overlap pattern already documented for
    880 other Strong's codes (`strongs-shared-across-registry-words-20260810.md`).

Two deliberately NOT included, flagged rather than guessed:
  - The other 10 sub-lettered forms of H5414 ("na.tan") — the researcher's list named ONE specific
    sense ("to give: do", H5414P) in a "(14 forms)" family; only 11 forms exist in this DB and
    only H5414P's own gloss matches what was asked for. Including the other 10 (H5414G's "to
    give: give" at 1,324x down to H5414Q at 25x) would fold in one of the single most common verbs
    in the Hebrew Bible under "healing" on a very thin thread.
  - G4990 (sōtēr, 46x) / G4992 (sōtērion, 122x) — the researcher's list said "sōtēria etc. (2
    forms)" but no pairing of the Greek "salvation" family cleanly resolves to the given 49x. Only
    G4991 (sōtēria itself, the term actually named) is included.

    python -m iba.app.migration.add_healing_word_strong_20260810           # dry-run: show the plan
    python -m iba.app.migration.add_healing_word_strong_20260810 --apply    # do it
"""

from __future__ import annotations

import argparse
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db

WORD = "healing"

# (strong, gloss, "NEW" | "CROSS <existing words>") — for the printed plan only; the write itself
# only needs the strong code.
CODES: list[tuple[str, str, str]] = [
    # Hebrew — NEW (9)
    ("H7499", "remedy", "NEW"),
    ("H1455", "to cure", "NEW"),
    ("H5324", "to stand", "NEW"),
    ("H2280", "to saddle/tie", "NEW"),
    ("H1277", "fat", "NEW"),
    ("H1274", "fat", "NEW"),
    ("H1879", "fat", "NEW"),
    ("H8585B", "healing", "NEW"),
    ("H3545", "easing", "NEW"),
    ("H2418", "to live", "NEW (cha.ya, sibling of cha.yah — no existing link, verified directly)"),
    ("H2425", "to live", "NEW (cha.yay, sibling of cha.yah — no existing link, verified directly)"),
    # Hebrew — CROSS (18)
    ("H7495", "to heal", "CROSS renewal"),
    ("H2421", "to live", "CROSS appetite,being"),
    ("H7965G", "peace", "CROSS peace"),
    ("H7965H", "Peace [God]", "CROSS peace"),
    ("H7965I", "peace: well-being", "CROSS peace,being"),
    ("H7965J", "peace: friendship", "CROSS peace,trust"),
    ("H7965K", "peace: greeting", "CROSS peace"),
    ("H7965L", "peace: completely", "CROSS peace"),
    ("H4832", "healing", "CROSS gentleness,yielding"),
    ("H5414P", "to give: do", "CROSS slander"),
    ("H0724", "health", "CROSS renewal"),
    ("H4974", "soundness", "CROSS integrity"),
    ("H2492A", "be healthy", "CROSS being"),
    ("H4010", "cheer", "CROSS comfort,joy"),
    ("H7500", "healing", "CROSS renewal"),
    ("H8644", "healing", "CROSS renewal"),
    ("H0820", "strong", "CROSS strength"),
    ("H2949", "tender care", "CROSS compassion"),
    # Greek — NEW (6)
    ("G2390", "to heal", "NEW"),
    ("G2392", "healing", "NEW"),
    ("G5199", "healthy", "NEW"),
    ("G2386", "healing", "NEW"),
    ("G2322", "service", "NEW"),
    ("G3647", "wholeness", "NEW"),
    # Greek — CROSS (9)
    ("G1295", "to save", "CROSS salvation"),
    ("G2323", "to serve/heal", "CROSS worship"),
    ("G0018", "good", "CROSS generosity,goodness,kindness"),
    ("G4982", "to save", "CROSS salvation"),
    ("G4991", "salvation", "CROSS salvation,strength"),
    ("G2480", "be strong", "CROSS being,power,strength"),
    ("G5198", "be healthy", "CROSS being"),
    ("G0573", "sound", "CROSS integrity"),
    ("G7534", "to enjoy good health", "CROSS goodness"),
]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="apply (default is dry-run)")
    a = ap.parse_args()

    cfg = Cfg()
    db = Db(cfg)
    if "word_strong" not in cfg.may_write("migration"):
        print("write-grant violation: 'migration' may not write 'word_strong'", file=sys.stderr)
        db.close(); cfg.close()
        return 1

    wrow = db.get("word_registry", word=WORD)
    if not wrow or wrow["deleted"]:
        print(f"{WORD!r} not found in word_registry (or deleted) — run registry.create first "
              f"(see this script's own docstring for the exact command used).", file=sys.stderr)
        db.close(); cfg.close()
        return 1
    wid = wrow["id"]

    already = {r["strong"] for r in db.rows(
        "SELECT strong FROM word_strong WHERE word_id=? AND deleted=0", (wid,))}
    todo = [(s, g, k) for s, g, k in CODES if s not in already]

    print(f"'{WORD}' = word_registry id {wid}")
    print(f"{len(CODES)} codes in the curated list, {len(already)} already linked, "
         f"{len(todo)} to add")
    for s, g, k in todo:
        print(f"  {s:8} {g:24} {k}")

    if not a.apply:
        print("\nDRY-RUN — re-run with --apply to write these word_strong rows.")
        db.close(); cfg.close()
        return 0

    n = 0
    for s, g, k in todo:
        db.upsert("word_strong", {"word_id": wid, "strong": s, "deleted": 0})
        n += 1
    db.conn.commit()
    db.close()
    cfg.close()
    print(f"\napplied: {n} word_strong row(s) added under '{WORD}' (id {wid}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
