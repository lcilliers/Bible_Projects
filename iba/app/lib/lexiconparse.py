"""lexiconparse.py — the governed parse of the raw lexicon layer (strong_meaning_tree.sense_text,
strong_lexicon.lsj, strong_lexicon.mounce) into strong_meaning_parsed / strong_lsj_parsed /
strong_mounce_parsed (handlers/lexicon.py:parse) -- the single source of these rules for the app.
The tools/ extract scripts (build_meaning_tree_extract.py, build_lsj_sense_extract.py,
build_mounce_lexicon_extract.py) are separate standalone copies, not imported.

Rules:
  - comma/semicolon/colon are NOT sense separators: a <b> span like "to celebrate, praise;" (G0021)
    is one sense, as STEP displays it. The only sense separator is a literal line break (mounce's
    <br>).
  - a row's refs/notes are scoped to the <b> span they follow (SegmentParser), never pooled across
    the row.

Each table keeps its natural source key: strong_meaning_tree.lemma_key is base-only, with its own
`strong_variant` column naming the exact code a row came from; strong_lexicon.strong is the full
code. Parsing is in place: one raw row's HTML into several clean rows under the same key.

Every regex/threshold/tag-set deciding a classification or parse boundary is config (cfg_setting,
module='lexicon'), read once per top-level call by `load_rules()`; each has a fallback equal to the
seeded value, so a missing setting does not change behaviour.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass
from html.parser import HTMLParser


# ── config-driven rules (cfg_setting, module='lexicon') ────────────────────────────────────────
# Fallbacks below equal the seeded cfg_setting values; used only when a setting is absent.
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
# STEP's mediumDef can place a bare part-of-speech abbreviation ahead of numbered senses as a section
# header (H0503: "v<br>1) to make thousand-fold...<br>n m<br>3) chief, chiliarch"): headers, not
# senses (#1668). See is_header_only_line().
    "lexicon.header_pos_tags": [
        "v", "vb", "n", "a", "adj", "adv", "prep", "subst", "conj", "interj", "pron", "num",
        "part", "n m", "n f", "n c", "nm", "nf", "nc", "n pr m", "n pr f", "n pr loc",
    ],
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
    header_pos_tags: frozenset


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
        header_pos_tags=frozenset(
            t.strip().lower() for t in
            cfg.setting("lexicon.header_pos_tags", d["lexicon.header_pos_tags"])),
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

    `strong_variant` passes through strong_meaning_tree's own column, so a reader can look up a
    specific sibling code's parsed gloss."""
    code, remaining = _extract_sense_code(sense_code, sense_text, rules)

    p = _MeaningSegmentParser()
    p.feed(_normalize_refs(remaining, rules))

    # a <b> span holding only punctuation (STEP bolding a bare comma before a citation) has no gloss:
    # it is folded into the preceding segment's note/refs, not made its own row (#1668)
    real_segments = []
    for seg in p.segments:
        gloss_parts = _dedupe_preserve_order([_clean(g) for g in seg["gloss"] if _clean(g)])
        if not gloss_parts and real_segments:
            prev = real_segments[-1]
            prev["note"] = prev["note"] + seg["note"]
            prev["refs"] = prev["refs"] + seg["refs"]
            continue
        real_segments.append(seg)

    rows = []
    for seg in real_segments:
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


def _strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s or "").strip()


def is_header_only_line(sense_code: str, sense_text: str, transliteration: str | None,
                        rules: Rules) -> bool:
    """True if this `strong_meaning_tree` row is a bare STEP header/label line -- a part-of-speech
    abbreviation ('v', 'n m', 'adj', ...) or the code's own transliteration echoed as a gloss (e.g.
    H6310 'peh') -- ahead of or between the numbered senses (#1668). Only fires for a row with no
    sense_code of its own; a numbered '1)'/'2a)' row is never excluded."""
    if sense_code:
        return False
    stripped = _strip_tags(sense_text).lower()
    if not stripped:
        return False
    if stripped in rules.header_pos_tags:
        return True
    if transliteration and stripped == transliteration.strip().lower():
        return True
    return False


def meaning_tree_rows(cfg) -> list[tuple]:
    """All of strong_meaning_tree, parsed. -> [(lemma_key, strong_variant, sort, sense_code, gloss,
    verse_refs, note, row_type), ...]

    A header-only row (`is_header_only_line()`) is dropped before parsing (#1668), and `sort` is
    renumbered contiguously from 0 per (lemma_key, strong_variant), so sort=0 is always the true first
    sense (#1663)."""
    rules = load_rules(cfg)
    cur = cfg.conn.execute(
        "SELECT smt.lemma_key, smt.strong_variant, smt.sort, smt.sense_code, smt.sense_text, "
        "s.stepTransliteration "
        "FROM strong_meaning_tree smt LEFT JOIN strong s ON smt.strong_variant = s.strongNumber "
        "WHERE smt.deleted=0 ORDER BY smt.lemma_key, smt.strong_variant, smt.sort")

    grouped: dict[tuple[str, str], list[tuple[str, str]]] = {}
    for lemma_key, strong_variant, sort, sense_code, sense_text, translit in cur.fetchall():
        if is_header_only_line(sense_code, sense_text, translit, rules):
            continue
        grouped.setdefault((lemma_key, strong_variant), []).append((sense_code, sense_text))

    rows = []
    for (lemma_key, strong_variant), items in grouped.items():
        next_sort = 0
        for sense_code, sense_text in items:
            for parsed in parse_meaning_tree_row(
                    lemma_key, strong_variant, next_sort, sense_code, sense_text, rules):
                rows.append(parsed)
                next_sort += 1
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
