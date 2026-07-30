"""lexiconparse.py — the governed parse of the raw lexicon layer (strong_meaning_tree.sense_text,
strong_lexicon.lsj, strong_lexicon.mounce) into strong_meaning_parsed / strong_lsj_parsed /
strong_mounce_parsed (handlers/lexicon.py:parse). This is the single source of truth for these
rules going forward — ported here, corrected, from this session's exploratory work in
iba/app/tools/build_meaning_tree_extract.py / build_lsj_sense_extract.py /
build_mounce_lexicon_extract.py (which found and fixed the underlying bugs first, against
outputs/csv exports; those tools scripts remain as independent, standalone-runnable copies —
"exploratory, not wired into the app" by their own docstrings — this module is the one the app
itself calls, not a shared import between the two, to keep that boundary real, not just stated).

Corrected rules, all confirmed against live data / a live STEP re-fetch before being trusted:

  - comma/semicolon/colon are NOT sense separators in strong_meaning_tree.sense_text or
    strong_lexicon.lsj/mounce — a <b> span like "to celebrate, praise;" (G0021) or
    "goodness, virtue, beneficence," (G0019) is ONE sense as STEP itself displays it. The only
    sense-separator recognised is a literal line break (mounce's <br> tags; none exist in
    meaning_tree/lsj's sources today, so those two currently never explode a gloss further).
  - a source row's refs/notes are SCOPED to the exact <b> span they followed (SegmentParser),
    not pooled across the whole row — the bug that misattributed one span's verse citation onto
    an unrelated sibling gloss in the same row (e.g. G0019's Gal.5.22 landing on "goodness" too).

Unlike the tools/ extract scripts (which split strong into base+variant for a common join key
across sources), these functions keep each table's NATURAL source key as-is: strong_meaning_tree.
lemma_key is base-only (it never carries a sub-entry letter — confirmed 3169/3169) AND (2026-07-26,
migration/fix_strong_meaning_tree_collapse.py) carries its own `strong_variant` column recording
the EXACT code a given tree row's content actually came from; strong_lexicon.strong is already the
full code (matching strong.strongNumber exactly) — no splitting/reconstruction needed for a DB
table that's simply parsing IN PLACE, one raw row's HTML into several clean rows under the same key.

Every regex/threshold/tag-set that decides a classification or parse boundary is config-driven
(cfg_setting, module='lexicon') — added 2026-07-30 per the researcher's correction: "the core of
the app says all configurable elements of code must NOT be hard coded, but included in configs,"
directly analogous to `candidate.py`'s own config-driven patterns (`candidate.tag_max_words`,
`candidate.transliteration_pattern`, etc.) which this module had not been following. `load_rules()`
reads every one of them ONCE per top-level call (`meaning_tree_rows`/`lsj_rows`/`mounce_rows`),
each with a fallback default matching the original hardcoded behaviour exactly (`migration/
add_lexicon_parse_settings.py` seeds the live rows with the same values) — a missing setting never
changes behaviour, it just stops being config-governed until the row exists.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass
from html.parser import HTMLParser


# ── config-driven rules (cfg_setting, module='lexicon') ────────────────────────────────────────
# Fallback defaults below match this module's original hardcoded values exactly — used only when
# a setting is (not yet, or no longer) present; `migration/add_lexicon_parse_settings.py` seeds the
# live cfg_setting rows with these same values so behaviour is unchanged until a researcher tunes
# one via configmaint.propose.
_DEFAULTS = {
    "lexicon.non_latin_script_pattern": r"[Ͱ-Ͽἀ-῿֐-׿]",
    "lexicon.classify_lookup_max_words": 3,
    "lexicon.outline_code_pattern": r"^(\d+[a-zA-Z0-9]*\))\s*(.*)$",
    "lexicon.ref_tag_pattern": r"""<ref=['"]([^'"]*)['"]>""",
    "lexicon.linebreak_pattern": r"[\r\n]+",
    "lexicon.lsj_level_tags": ["level1", "level2", "level3", "level4"],
    "lexicon.lsj_top_level_label_pattern": r"^[IVXLCDM]+$",
    "lexicon.lsj_sublabel_pattern": r"^\d+[a-z]*$",
    "lexicon.bracket_pairs": {"(": ")", "[": "]", "{": "}"},
}


@dataclass(frozen=True)
class Rules:
    """Every compiled/resolved parsing rule for one call — read once via `load_rules(cfg)`, then
    threaded through every function below rather than re-reading cfg_setting per row."""
    non_latin_script_re: re.Pattern
    lookup_max_words: int
    outline_code_re: re.Pattern
    ref_tag_re: re.Pattern
    linebreak_re: re.Pattern
    lsj_level_tags: frozenset
    lsj_top_level_label_re: re.Pattern
    lsj_sublabel_re: re.Pattern
    open_brackets: str
    close_brackets: str


def load_rules(cfg) -> Rules:
    d = _DEFAULTS
    pairs = cfg.setting("lexicon.bracket_pairs", d["lexicon.bracket_pairs"])
    return Rules(
        non_latin_script_re=re.compile(
            cfg.setting("lexicon.non_latin_script_pattern", d["lexicon.non_latin_script_pattern"])),
        lookup_max_words=int(cfg.setting(
            "lexicon.classify_lookup_max_words", d["lexicon.classify_lookup_max_words"])),
        outline_code_re=re.compile(
            cfg.setting("lexicon.outline_code_pattern", d["lexicon.outline_code_pattern"]), re.S),
        ref_tag_re=re.compile(cfg.setting("lexicon.ref_tag_pattern", d["lexicon.ref_tag_pattern"])),
        linebreak_re=re.compile(cfg.setting("lexicon.linebreak_pattern", d["lexicon.linebreak_pattern"])),
        lsj_level_tags=frozenset(cfg.setting("lexicon.lsj_level_tags", d["lexicon.lsj_level_tags"])),
        lsj_top_level_label_re=re.compile(
            cfg.setting("lexicon.lsj_top_level_label_pattern", d["lexicon.lsj_top_level_label_pattern"])),
        lsj_sublabel_re=re.compile(
            cfg.setting("lexicon.lsj_sublabel_pattern", d["lexicon.lsj_sublabel_pattern"])),
        open_brackets="".join(pairs.keys()),
        close_brackets="".join(pairs.values()),
    )


def strip_bracketed(text: str, rules: Rules) -> str:
    out = []
    depth = 0
    for ch in text:
        if ch in rules.open_brackets:
            depth += 1
            continue
        if ch in rules.close_brackets:
            depth = max(0, depth - 1)
            continue
        if depth == 0:
            out.append(ch)
    return "".join(out)


def classify_row(text: str, rules: Rules) -> str:
    """not applicable (empty, or wholly one bracket pair) / lookup (<=lookup_max_words words,
    Latin script) / description (more words, or any non-Latin script regardless of length)."""
    stripped = (text or "").strip()
    if not stripped:
        return "not applicable"
    if stripped[0] in rules.open_brackets and stripped[-1] in rules.close_brackets:
        if strip_bracketed(stripped, rules).strip() == "":
            return "not applicable"
    words = [w for w in stripped.split() if re.search(r"[A-Za-z]", w)]
    if not words:
        return "not applicable"
    if rules.non_latin_script_re.search(stripped):
        return "description"
    return "lookup" if len(words) <= rules.lookup_max_words else "description"


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip().strip(",").strip()


def _dedupe_preserve_order(items):
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


# ── strong_meaning_tree.sense_text -> strong_meaning_parsed ────────────────────────────────────

def _split_by_linebreak(text: str, rules: Rules) -> list[str]:
    if not text:
        return []
    return [p for p in (_clean(part) for part in rules.linebreak_re.split(text)) if p]


def _normalize_refs(text: str, rules: Rules) -> str:
    # <ref='Act.14.17'>display</ref> uses a nameless '=value' pseudo-attribute HTMLParser can't
    # parse as a real attribute — rewrite to a well-formed <ref key="..."> so the key survives
    # into the segment it belongs to, instead of being pulled out via a separate whole-string pass.
    def repl(m):
        return '<ref key="%s">' % html.escape(m.group(1), quote=True)

    return rules.ref_tag_re.sub(repl, text)


class _MeaningSegmentParser(HTMLParser):
    """One segment per <b> span (leading text before the first <b> folds into that first
    segment) — so verse_refs/note stay scoped to the gloss they actually followed."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.segments = [{"gloss": [], "refs": [], "note": []}]
        self.cur = self.segments[0]
        self.in_bold = False
        self.in_ref = False

    def handle_starttag(self, tag, attrs):
        if tag == "b":
            if not self.in_bold:
                self.in_bold = True
                if self.cur["gloss"]:
                    self.cur = {"gloss": [], "refs": [], "note": []}
                    self.segments.append(self.cur)
        elif tag == "ref":
            self.in_ref = True
            self.cur["refs"].append(dict(attrs).get("key", ""))

    def handle_endtag(self, tag):
        if tag == "b":
            self.in_bold = False
        elif tag == "ref":
            self.in_ref = False

    def handle_data(self, data):
        if self.in_ref:
            return
        if self.in_bold:
            self.cur["gloss"].append(data)
        else:
            self.cur["note"].append(data)


def _extract_sense_code(sense_code: str, sense_text: str, rules: Rules) -> tuple[str, str]:
    if sense_code:
        return _clean(sense_code), sense_text
    m = rules.outline_code_re.match(sense_text)
    if m:
        return m.group(1), m.group(2)
    return "", sense_text


def parse_meaning_tree_row(lemma_key: str, strong_variant: str, sort: int, sense_code: str,
                           sense_text: str, rules: Rules) -> list[tuple]:
    """-> [(lemma_key, strong_variant, sort, sense_code, gloss, verse_refs, note, row_type), ...]

    `strong_variant` (2026-07-26, migration/fix_strong_meaning_tree_collapse.py) is a straight
    pass-through of strong_meaning_tree's own new column — parsing never decides it, it just
    carries the source row's key forward so a reader can look up a SPECIFIC sibling code's own
    parsed gloss instead of only ever the shared base row (see BUILD.md sec24/sec25)."""
    code, remaining = _extract_sense_code(sense_code, sense_text, rules)

    p = _MeaningSegmentParser()
    p.feed(_normalize_refs(remaining, rules))

    rows = []
    for seg in p.segments:
        gloss_parts = _dedupe_preserve_order([_clean(g) for g in seg["gloss"] if _clean(g)])
        gloss = ", ".join(gloss_parts)
        note = _clean(" ".join(seg["note"]))
        verse_refs = "; ".join(r for r in seg["refs"] if r)

        if not gloss and note:
            gloss, note = note, ""

        for part in (_split_by_linebreak(gloss, rules) or [gloss]):
            rows.append((lemma_key, strong_variant, sort, code, part, verse_refs, note,
                        classify_row(part, rules)))
    return rows


def meaning_tree_rows(cfg) -> list[tuple]:
    """All of strong_meaning_tree, parsed. -> [(lemma_key, strong_variant, sort, sense_code,
    gloss, verse_refs, note, row_type), ...]"""
    rules = load_rules(cfg)
    cur = cfg.conn.execute(
        "SELECT lemma_key, strong_variant, sort, sense_code, sense_text FROM strong_meaning_tree "
        "WHERE deleted=0 ORDER BY lemma_key, sort")
    rows = []
    for lemma_key, strong_variant, sort, sense_code, sense_text in cur.fetchall():
        rows.extend(parse_meaning_tree_row(
            lemma_key, strong_variant, sort, sense_code, sense_text, rules))
    return rows


# ── strong_lexicon.lsj -> strong_lsj_parsed ─────────────────────────────────────────────────────

class _LsjSenseParser(HTMLParser):
    """LSJ almost always leaves the first sense ("I") without an explicit <LevelN> tag — <br> is
    also treated as a block boundary; empty blocks are dropped, and the first surviving unlabeled
    block after the headword is relabeled "I" (see parse_lsj_row)."""

    def __init__(self, rules: Rules):
        super().__init__(convert_charrefs=True)
        self._level_tags = rules.lsj_level_tags
        self.blocks = [{"label": "headword", "gloss": [], "note": []}]
        self.in_bold = False
        self.in_link = False
        self.in_level_label = False

    def handle_starttag(self, tag, attrs):
        if tag in self._level_tags:
            self.blocks.append({"label": "", "gloss": [], "note": []})
            self.in_level_label = True
        elif tag == "br":
            self.blocks.append({"label": "", "gloss": [], "note": []})
        elif tag == "b":
            self.in_bold = True
        elif tag == "a":
            self.in_link = True

    def handle_endtag(self, tag):
        if tag in self._level_tags:
            self.in_level_label = False
        elif tag == "b":
            self.in_bold = False
        elif tag == "a":
            self.in_link = False

    def handle_data(self, data):
        if self.in_link:
            return
        if self.in_level_label:
            self.blocks[-1]["label"] += data
        elif self.in_bold:
            self.blocks[-1]["gloss"].append(data)
        else:
            self.blocks[-1]["note"].append(data)


def _lsj_clean(s: str) -> str:
    s = re.sub(r"\[\s*\]", "", s or "")  # empty brackets left by a stripped <a> link
    return re.sub(r"\s+", " ", s).strip()


def parse_lsj_row(strong: str, lsj_html: str, rules: Rules) -> list[tuple]:
    """-> [(strong, sense_label, gloss, note, row_type), ...]"""
    if not lsj_html:
        return [(strong, "", "", "", "lookup")]

    p = _LsjSenseParser(rules)
    p.feed(lsj_html)

    parsed = []
    for i, block in enumerate(p.blocks):
        label = _lsj_clean(block["label"]).lstrip("_") or ("headword" if i == 0 else "")
        gloss_parts = _dedupe_preserve_order(
            [_lsj_clean(g).rstrip(",").strip() for g in block["gloss"] if _lsj_clean(g)])
        gloss = ", ".join(gloss_parts)
        note = _lsj_clean(" ".join(block["note"]))
        if not label and not gloss and not note:
            continue
        parsed.append([strong, label, gloss, note])

    for row in parsed[1:]:
        if row[1] == "":
            row[1] = "I"
        break

    current_top = None
    for row in parsed:
        label = row[1]
        if label == "headword":
            continue
        if rules.lsj_top_level_label_re.match(label):
            current_top = label
        elif rules.lsj_sublabel_re.match(label) and current_top:
            row[1] = f"{current_top}.{label}"

    return [(s, label, gloss, note, "headword" if label == "headword" else "lookup")
            for s, label, gloss, note in parsed]


def lsj_rows(cfg) -> list[tuple]:
    """All of strong_lexicon.lsj, parsed. -> [(strong, sense_label, gloss, note, row_type), ...]"""
    rules = load_rules(cfg)
    cur = cfg.conn.execute("SELECT strong, lsj FROM strong_lexicon WHERE deleted=0")
    rows = []
    for strong, lsj in cur.fetchall():
        rows.extend(parse_lsj_row(strong, lsj, rules))
    return rows


# ── strong_lexicon.mounce -> strong_mounce_parsed ───────────────────────────────────────────────

class _MounceRowSplitter(HTMLParser):
    """Strips markup (keeping inner text), treats <br> as the ONLY row break."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.rows = [""]

    def handle_starttag(self, tag, attrs):
        if tag == "br":
            self.rows.append("")

    def handle_data(self, data):
        self.rows[-1] += data


def parse_mounce_row(strong: str, mounce_html: str, rules: Rules) -> list[tuple]:
    """-> [(strong, mounce_parsed, row_type), ...]"""
    if mounce_html is None:
        return [(strong, "", classify_row("", rules))]
    p = _MounceRowSplitter()
    p.feed(mounce_html)
    lines = [re.sub(r"\s+", " ", r).strip() for r in p.rows]
    return [(strong, line, classify_row(line, rules)) for line in lines]


def mounce_rows(cfg) -> list[tuple]:
    """All of strong_lexicon.mounce, parsed. -> [(strong, mounce_parsed, row_type), ...]"""
    rules = load_rules(cfg)
    cur = cfg.conn.execute("SELECT strong, mounce FROM strong_lexicon WHERE deleted=0")
    rows = []
    for strong, mounce in cur.fetchall():
        rows.extend(parse_mounce_row(strong, mounce, rules))
    return rows
