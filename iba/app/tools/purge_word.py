"""purge_word.py — remove a word's OWN records. For clearing test data.

    python -m iba.app.tools.purge_word --word "[hypocrisy]"          # dry-run (default): show what would go
    python -m iba.app.tools.purge_word --word "[hypocrisy]" --yes    # actually delete

Scope — deliberately NARROW. It removes only rows that BELONG to the word:
    word_registry (the word), word_strong (its discovery links),
    escalation (by word), run (by runs_over), validation_result (by word).

It does NOT touch the shared raw layer — strong, strong_sense, strong_meaning_tree,
strong_lexicon, verse, strong_verse, span — because those are global and de-duplicated:
other words may reference the same strongs and verses. Removing them is a cascade with
its own risks, and belongs to the future 'delete' OPERATION, not this stopgap. Any
strong/verse left with no referencing word is a harmless orphan a later sweep can clear.

The word is matched LITERALLY (case-insensitively), NOT normalised — cleanup must be
able to target malformed residue exactly as it sits in the table (e.g. '[hypocrisy]'),
without the strip-brackets normalisation collapsing it onto a real, different word.
"""

from __future__ import annotations

import argparse
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db
from ..lib.escalation import word_source

# table -> the column that carries the word (or the word's id), for word-scoped deletes
# escalation-reset 2026-08-16: escalation no longer has a `word` column — a word-scoped row's
# `source` carries 'new-word: <word>' (lib.escalation.word_source), matched below via that helper.
WORD_SCOPED = [
    ("validation_result", "word"),
    ("escalation",        "source"),
    ("run",               "runs_over"),
    ("word_strong",       "word_id"),   # by the registry id, resolved below
    ("word_registry",     "id"),        # last — others may resolve against it
]


def _counts(db: Db, word: str, wid: int | None) -> dict[str, int]:
    out: dict[str, int] = {}
    out["word_registry"] = db.rows(
        "SELECT COUNT(*) c FROM word_registry WHERE lower(word)=lower(?)", (word,))[0]["c"]
    out["escalation"] = db.rows(
        "SELECT COUNT(*) c FROM escalation WHERE lower(source)=lower(?)", (word_source(word),))[0]["c"]
    out["run"] = db.rows(
        "SELECT COUNT(*) c FROM run WHERE lower(runs_over)=lower(?)", (word,))[0]["c"]
    out["validation_result"] = db.rows(
        "SELECT COUNT(*) c FROM validation_result WHERE lower(word)=lower(?)", (word,))[0]["c"]
    out["word_strong"] = (db.rows(
        "SELECT COUNT(*) c FROM word_strong WHERE word_id=?", (wid,))[0]["c"] if wid else 0)
    return out


def purge(word: str, do_it: bool) -> int:
    cfg = Cfg()
    db = Db(cfg)

    reg = db.rows("SELECT id, word, status FROM word_registry WHERE lower(word)=lower(?)", (word,))
    wid = reg[0]["id"] if reg else None
    counts = _counts(db, word, wid)
    total = sum(counts.values())

    print(f"purge_word: {word!r}" + (f"  (registry id {wid}, status {reg[0]['status']})" if reg else "  (not in registry)"))
    for t, n in counts.items():
        print(f"  {t:20} {n}")
    if total == 0:
        print("nothing to remove.")
        db.close(); cfg.close(); return 0

    if not do_it:
        print(f"\nDRY-RUN — would remove {total} row(s). Re-run with --yes to delete.")
        print("NOTE: shared raw data (strong/verse/span/strong_verse/*meaning*) is left untouched.")
        db.close(); cfg.close(); return 0

    db.conn.execute("DELETE FROM validation_result WHERE lower(word)=lower(?)", (word,))
    db.conn.execute("DELETE FROM escalation WHERE lower(source)=lower(?)", (word_source(word),))
    db.conn.execute("DELETE FROM run WHERE lower(runs_over)=lower(?)", (word,))
    if wid:
        db.conn.execute("DELETE FROM word_strong WHERE word_id=?", (wid,))
    db.conn.execute("DELETE FROM word_registry WHERE lower(word)=lower(?)", (word,))
    db.close()
    cfg.close()
    print(f"\nremoved {total} row(s) for {word!r}. Shared raw data left untouched.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Remove a word's own records (test-data cleanup).")
    ap.add_argument("--word", required=True)
    ap.add_argument("--yes", action="store_true", help="actually delete (default is dry-run)")
    a = ap.parse_args()
    return purge(a.word, a.yes)


if __name__ == "__main__":
    sys.exit(main())
