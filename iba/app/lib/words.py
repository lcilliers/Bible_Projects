"""words.py — registry word normalisation. Config-governed.

A word enters as free text on the command line. Before anything looks it up or stores
it, it is normalised HERE, once, at the dispatch boundary, so every handler and every
lookup sees the same canonical form. The strip pattern is a config setting, not a
constant — what counts as 'stray' at the ends of a word is a rule, not a fact.

Normalisation: collapse internal whitespace, then strip runs of the configured class
from BOTH ends. It does NOT change case — the researcher's capitalisation is preserved
in storage; word matching is done case-insensitively instead (so 'Fear' and 'fear' are
one word without forcing a stored form).
"""

from __future__ import annotations

import re

from .cfg import Cfg


def normalise(word: str, cfg: Cfg) -> str:
    strip = cfg.setting("registry.strip_ends_pattern", r"[^A-Za-z]")
    w = re.sub(r"\s+", " ", word or "").strip()
    w = re.sub(rf"^(?:{strip})+", "", w)
    w = re.sub(rf"(?:{strip})+$", "", w)
    return w
