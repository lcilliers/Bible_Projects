"""add_lexicon_header_pos_tags_setting_v1_20260910.py — ONE-OFF: seed `cfg_setting`
(lexicon.header_pos_tags) with the vocabulary `lib/lexiconparse.py:is_header_only_line()` uses,
per the module's own established rule (`add_lexicon_parse_settings.py`, 2026-07-30): every
regex/threshold/tag-set is config-driven, not hard-coded.

Escalation #1668, 2026-09-10, researcher instruction verbatim: "the code that run the parse ...
can rerun at any time, that this code [must be] producing sensible results — which at this moment
it is not. So the fixing of the parse routine is priority nr 1." STEP's own mediumDef places a
bare part-of-speech abbreviation ('v', 'n m', 'adj', ...) ahead of a numbered sense group as a
header, not a sense — confirmed live against STEP's own call2_getInfo for H0503/H6310. Fixed in
lib/lexiconparse.py:meaning_tree_rows()/is_header_only_line() (excludes header-only lines,
including a match against the code's own strong.stepTransliteration — H6310's 'peh' case — and
renumbers `sort` contiguously per (lemma_key, strong_variant) so the excluded line never leaves a
permanent gap at sort=0).

Same class of exception as every other bootstrap_*/add_* migration — a one-time backfill of a
single setting row, not `configmaint.propose` (the "don't approve mechanical infrastructure
row-by-row" rule).

    python -m iba.app.migration.add_lexicon_header_pos_tags_setting_v1_20260910
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_KEY = "lexicon.header_pos_tags"
_VALUE = [
    "v", "vb", "n", "a", "adj", "adv", "prep", "subst", "conj", "interj", "pron", "num",
    "part", "n m", "n f", "n c", "nm", "nf", "nc", "n pr m", "n pr f", "n pr loc",
]
_USE = ("meaning_tree_rows()/is_header_only_line(): a strong_meaning_tree row with no sense_code "
        "of its own, whose entire (tag-stripped) text exact-matches one of these bare "
        "part-of-speech abbreviations, is a STEP-source section header for the numbered sense "
        "group that follows, not a sense itself — excluded before it ever becomes a "
        "strong_meaning_parsed row. Escalation #1668, 2026-09-10.")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    existing = conn.execute("SELECT value FROM cfg_setting WHERE key=?", (_KEY,)).fetchone()
    if existing:
        print(f"{_KEY!r} already present — left alone")
        conn.close()
        return 0
    conn.execute(
        "INSERT INTO cfg_setting (key, value, module, use, inactive) VALUES (?,?,?,?,0)",
        (_KEY, json.dumps(_VALUE, ensure_ascii=False), "lexicon", _USE))
    conn.commit()
    conn.close()
    print(f"{_KEY!r} added ({len(_VALUE)} values)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
