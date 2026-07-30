"""add_lexicon_parse_settings.py — ONE-OFF: seed `cfg_setting` (module='lexicon') with every
regex/threshold/tag-set `lib/lexiconparse.py` used to hard-code, so its classification and parse-
boundary rules are config-governed like every other rule of this kind in the app (`candidate.py`'s
`candidate.tag_max_words`/`candidate.transliteration_pattern` etc.).

Researcher's correction, 2026-07-30: "why would you think lexiconparse.py would not use configs
for defining the regex if all other regex codes are driven through configs for other routines...
the core of the app says all configurable elements of code must NOT be hard coded, but included in
configs." `find_utility_config_density` had flagged lexiconparse as the one real "zero config
usage" gap; treating it as an open judgement call was itself the mistake — the app already has an
established, applied standard for exactly this class of rule.

Every value seeded here is IDENTICAL to `lexiconparse.py`'s previous hardcoded constant — this is a
config-governance move, not a behaviour change. `lib/lexiconparse.Rules`/`load_rules()` read these
with the same literal values as their fallback default, so even a missing row wouldn't change
output; this migration just makes the values live, editable via `configmaint.propose` from here on.

Ordinary `cfg_setting` row inserts (no DDL) — still a direct migration, not `configmaint.propose`,
per the standing "don't approve mechanical infrastructure row-by-row" rule (this is a one-time
backfill of 9 rows from an already-detailed researcher instruction, the same class of exception as
every other `bootstrap_*`/`add_*` migration).

    python -m iba.app.migration.add_lexicon_parse_settings
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

# key -> (value, use) — value is the RAW Python value; JSON-encoded on insert (cfg_setting.value is
# always a JSON-decoded read via cfg.setting()).
_SETTINGS = {
    "lexicon.non_latin_script_pattern": (
        r"[Ͱ-Ͽἀ-῿֐-׿]",
        "classify_row: any match forces 'description' regardless of word count — Greek/Hebrew "
        "Unicode block ranges STEP's lexicon text uses."),
    "lexicon.classify_lookup_max_words": (
        3,
        "classify_row: a gloss/description with at most this many space-separated words is "
        "'lookup', more is 'description' — same shape as candidate.tag_max_words's word-count "
        "threshold."),
    "lexicon.outline_code_pattern": (
        r"^(\d+[a-zA-Z0-9]*\))\s*(.*)$",
        "strong_meaning_tree.sense_text: matches a leading outline code (e.g. '1)', '2a)') when "
        "sense_code itself is empty, splitting it from the remaining gloss text."),
    "lexicon.ref_tag_pattern": (
        r"""<ref=['"]([^'"]*)['"]>""",
        "matches STEP's <ref='Act.14.17'>display</ref> markup (a nameless '=value' pseudo-"
        "attribute HTMLParser can't parse as a real attribute) so it can be rewritten to a "
        "well-formed <ref key=\"...\"> before parsing."),
    "lexicon.linebreak_pattern": (
        r"[\r\n]+",
        "the only recognised sense-separator in strong_meaning_tree.sense_text/strong_lexicon.lsj/"
        "mounce — commas/semicolons/colons are NOT separators (STEP itself displays them as one "
        "sense)."),
    "lexicon.lsj_level_tags": (
        ["level1", "level2", "level3", "level4"],
        "LSJ's own HTML tag names marking an explicit outline-level boundary (<LevelN>)."),
    "lexicon.lsj_top_level_label_pattern": (
        r"^[IVXLCDM]+$",
        "LSJ top-level sense labels are Roman numerals (I, II, III, ...) — matched to track the "
        "current top-level for building compound sublabels like 'I.2'."),
    "lexicon.lsj_sublabel_pattern": (
        r"^\d+[a-z]*$",
        "LSJ sublabels are a bare number + optional letter (e.g. '2', '2a') — combined with the "
        "current top-level Roman numeral into 'I.2a'."),
    "lexicon.bracket_pairs": (
        {"(": ")", "[": "]", "{": "}"},
        "open->close bracket pairs classify_row/strip_bracketed treat as nestable — a gloss that "
        "is wholly one bracketed aside (e.g. '(obsolete)') classifies as 'not applicable'."),
}


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    for key, (value, use) in _SETTINGS.items():
        existing = conn.execute(
            "SELECT value FROM cfg_setting WHERE key=?", (key,)).fetchone()
        if existing:
            report.append(f"{key!r} already present — left alone")
            continue
        conn.execute(
            "INSERT INTO cfg_setting (key, value, module, use, inactive) VALUES (?,?,?,?,0)",
            (key, json.dumps(value, ensure_ascii=False), "lexicon", use))
        report.append(f"{key!r} added")

    conn.commit()
    conn.close()

    print("lexicon parse-rule settings bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
