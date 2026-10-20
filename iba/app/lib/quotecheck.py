"""quotecheck.py -- the narrative quote check, moved into the app (escalation #2173 G14).

Before this, four copies sat in cluster folders (M01, M25, M08 x2) against
governance.scripts_and_routines, and whether it ran at close depended on memory. This is the M08
version (#2156), the most complete: every double-quoted part of a line, split at an ellipsis (... or
the ellipsis character), with [bracketed] insertions blanked, must occur in the ESV text of iba.db
`verse` joined in canonical order (cfg_book_order, chapter, verse), so a quotation running across a
verse boundary is found. Case and punctuation are normalised. Parts under
narrative.quote_min_words words are not checked. Read-only.

check_lines() is used by the narrative_register.quote_check step (Narrative-Register.ps1 -Action
QuoteCheck) and by session-close SC5(b) on every chapter file changed in the session, against the
chapter's previous version (only the lines the session added are checked).
"""

from __future__ import annotations

import difflib
import re

_NORM_RX = re.compile(r"[“”‘’\"'—–,;:.!?()\[\]*_-]")
_ELLIPSIS_RX = re.compile(r"\s*(?:…|\.\.\.)\s*")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", _NORM_RX.sub(" ", s or "")).strip().lower()


class Corpus:
    """The ESV text, normalised and joined in canonical order. Build once per run."""

    def __init__(self, conn):
        order = {b: o for b, o in conn.execute("SELECT book, ordinal FROM cfg_book_order")}
        rows = []
        for osis, text in conn.execute("SELECT osisId, text FROM verse WHERE deleted=0"):
            b, ch, v = osis.rsplit(".", 2)
            rows.append((order.get(b, 999), int(ch), int(v), norm(text or "")))
        self.text = " " + " ".join(r[3] for r in sorted(rows)) + " "

    def has(self, part: str) -> bool:
        return f" {norm(part)} " in self.text


_GLOSS_RX = re.compile(r'\*[^*\n]+\*\*?\s*[,(:]?\s*$')


def parts_of(line: str, min_words: int, skip: set[str] | None = None) -> list[str]:
    """The quoted parts of one line. Quote marks are paired in order (so a short quote such as
    "I" does not shift the pairing). Not checked: a gloss (a quote straight after an italic
    transliteration, *nephesh* ("soul") or *lun*, "to grumble"), a quote that is a section or
    chapter title (`skip`, normalised), and parts under min_words words."""
    out = []
    pos = [i for i, ch in enumerate(line) if ch == '"']
    for a, b in zip(pos[0::2], pos[1::2]):
        q = line[a + 1:b]
        if _GLOSS_RX.search(line[max(0, a - 60):a]):
            continue
        if skip and norm(q) in skip:
            continue
        for p in _ELLIPSIS_RX.split(q):
            p = re.sub(r"\[[^\]]*\]", " ", p)
            if len(norm(p).split()) >= min_words:
                out.append(p.strip())
    return out


def titles(conn) -> set[str]:
    """Section headings and chapter titles, normalised: a quote of one is not a verse quote."""
    t = {norm(h) for (h,) in conn.execute("SELECT heading FROM narrative_section")}
    return t | {norm(x) for (x,) in conn.execute("SELECT title FROM narrative_chapter")}


def added_lines(old_text: str | None, new_text: str) -> list[str]:
    new = new_text.splitlines()
    if old_text is None:
        return new
    old = old_text.splitlines()
    return [l[1:] for l in difflib.unified_diff(old, new, lineterm="", n=0)
            if l.startswith("+") and not l.startswith("+++")]


def check_lines(corpus: Corpus, lines: list[str], min_words: int,
                skip: set[str] | None = None) -> tuple[int, list[str]]:
    """(parts checked, failing parts)."""
    n, bad = 0, []
    for line in lines:
        for p in parts_of(line, min_words, skip):
            n += 1
            if not corpus.has(p):
                bad.append(p)
    return n, bad
