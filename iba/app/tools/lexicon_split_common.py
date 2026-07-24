"""
Shared gloss-splitting and row-classification helpers for the
strong_lexicon/strong_meaning_tree extract scripts
(build_mounce_lexicon_extract.py, build_lsj_sense_extract.py,
build_meaning_tree_extract.py):

- split_multi_gloss(): explodes a comma/semicolon-delimited gloss string
  into one entry per sense. Commas/semicolons inside ( ) [ ] { } still
  protect the clause from splitting (so a nested parenthetical explanation
  stays on one row). Double quotes are stripped before splitting and colons
  are normalized to spaces, matching build_mounce_lexicon_extract.py's
  original pipeline.
- classify_row(): the word-count heuristic build_mounce_lexicon_extract.py
  originated - not applicable (empty, or wholly one bracket pair) / lookup
  (<=3 words) / description (4+ words) - plus one addition: any row
  containing Greek or Hebrew script is never "lookup" (a Hebrew or Greek
  original-language form or cross-reference sitting in an otherwise-English
  gloss is not itself an English lookup term, however short).
"""
import re

OPEN_BRACKETS = "([{"
CLOSE_BRACKETS = ")]}"

# Greek (incl. polytonic Greek Extended) and Hebrew (incl. points/cantillation) blocks.
NON_LATIN_SCRIPT_RE = re.compile(r"[Ͱ-Ͽἀ-῿֐-׿]")


def bracket_aware_split(text, delim):
    """Split text on delim, except where delim falls inside ( )/[ ]/{ }."""
    parts = []
    current = []
    depth = 0
    for ch in text:
        if ch in OPEN_BRACKETS:
            depth += 1
        elif ch in CLOSE_BRACKETS:
            depth = max(0, depth - 1)
        if ch == delim and depth == 0:
            parts.append("".join(current))
            current = []
        else:
            current.append(ch)
    parts.append("".join(current))
    return [p.strip() for p in parts]


def split_multi_gloss(text):
    """
    Explode a single gloss string into one entry per comma/semicolon-
    delimited sense. Returns [] for empty input, or if splitting/cleanup
    leaves nothing behind.
    """
    if not text:
        return []
    parts = [text.replace('"', "")]
    for delim in (",", ";"):
        exploded = []
        for part in parts:
            exploded.extend(bracket_aware_split(part, delim))
        parts = exploded
    parts = [re.sub(r"\s+", " ", p.replace(":", " ")).strip() for p in parts]
    return [p for p in parts if p]


def strip_bracketed(text):
    """Remove all bracketed spans (any nesting depth), keeping only the outside text."""
    out = []
    depth = 0
    for ch in text:
        if ch in OPEN_BRACKETS:
            depth += 1
            continue
        if ch in CLOSE_BRACKETS:
            depth = max(0, depth - 1)
            continue
        if depth == 0:
            out.append(ch)
    return "".join(out)


def classify_row(text):
    stripped = text.strip()
    if not stripped:
        return "not applicable"
    if stripped[0] in OPEN_BRACKETS and stripped[-1] in CLOSE_BRACKETS:
        if strip_bracketed(stripped).strip() == "":
            return "not applicable"
    words = [w for w in stripped.split() if re.search(r"[A-Za-z]", w)]
    if not words:
        return "not applicable"
    if NON_LATIN_SCRIPT_RE.search(stripped):
        return "description"
    return "lookup" if len(words) <= 3 else "description"
