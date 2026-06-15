"""morph_util.py — canonical morphology-code helpers (STEP / OSHB + Robinson Greek).

One place for "what language/category/mode is this morph_code", so checks and reports stop
re-implementing (and re-bugging) the H / A / Greek discrimination. Used by the mode visual and
the consistency checks. Pure functions, no DB.

Key gotchas this encodes:
- Greek codes are either hyphenated (`N-DSF`, `A-NSM`, `V-PAN`) OR all-caps indeclinables
  (`ADV`, `CONJ`, `PREP`, `PRT`). `A-NSM` is a Greek ADJECTIVE, `ADV` a Greek ADVERB — neither is Aramaic.
- Hebrew/Aramaic codes start with the language letter `H`/`A`, then an UPPER category letter,
  then lowercase features (`HNcfsa`, `AVqp3ms`) — or a 2-letter form (`HR`, `AC`).
- mti_terms.language is an intentional Hebrew/Greek binary (derived from the Strong's prefix in
  step_client and consumed as a binary by meaning_parser); Aramaic OT words are folded under
  "Hebrew" there. The Aramaic distinction lives HERE, in the morph code, not in that field.
"""

GREEK_INDECL = {"ADV", "CONJ", "COND", "PRT", "PREP", "INJ", "ARAM", "HEB", "N-LI", "N-OI"}
GREEK_INDECL_CAT = {"ADV": "adverb", "CONJ": "conjunction", "COND": "conditional",
                    "PRT": "particle", "PREP": "preposition", "INJ": "interjection",
                    "ARAM": "transliterated-Aramaic", "HEB": "transliterated-Hebrew"}
HEBCAT = {"V": "verb", "N": "noun", "A": "adjective", "C": "conjunction", "R": "preposition",
          "T": "particle", "P": "pronoun", "D": "adverb", "S": "suffix"}
GRKCAT = {"N": "noun", "V": "verb", "A": "adjective", "R": "pronoun", "C": "conjunction",
          "P": "preposition", "D": "adverb", "T": "article", "X": "particle", "I": "interjection"}

HEB_STEM = {"q": "Qal", "N": "Niphal", "p": "Piel", "P": "Pual", "h": "Hiphil", "H": "Hophal",
            "t": "Hithpael", "o": "Polel", "O": "Polal", "r": "Hithpolel", "v": "Hithpael",
            "c": "Tiphil", "u": "Polpal", "D": "Nithpael"}
ARAMAIC_STEM = {"q": "Peal", "Q": "Peil", "u": "Hithpeel", "p": "Pael", "P": "Pual",
                "M": "Hithpaal", "a": "Aphel", "h": "Haphel", "s": "Saphel", "e": "Shaphel",
                "H": "Hophal", "i": "Hithaphel", "t": "Hishtaphel"}


def morph_language(mc):
    """'Hebrew' | 'Aramaic' | 'Greek' | None (blank) | 'Unknown'."""
    if not mc:
        return None
    if "-" in mc or mc in GREEK_INDECL:
        return "Greek"
    if mc[0] == "H":
        return "Hebrew"
    if mc[0] == "A":
        return "Aramaic"
    return "Unknown"


def morph_category(mc):
    """coarse part of speech, e.g. 'verb' / 'noun' / 'adjective' / 'preposition'."""
    if not mc:
        return None
    if mc in GREEK_INDECL_CAT:
        return GREEK_INDECL_CAT[mc]
    if "-" in mc:                                   # Greek hyphenated: category is the first letter
        return GRKCAT.get(mc[0], "?")
    if mc[0] in "HA" and len(mc) > 1:               # Hebrew/Aramaic: category is the 2nd letter
        return HEBCAT.get(mc[1], "?")
    return "?"


def morph_stem(mc):
    """verb binyan, or '' if not an applicable verb form (Greek/nominal/function word)."""
    if not mc or mc[0] not in ("H", "A"):
        return ""
    body = mc[1:].lstrip("-")
    if body[:1] == "V" and len(body) > 1:
        table = HEB_STEM if mc[0] == "H" else ARAMAIC_STEM
        return table.get(body[1], "")
    return ""


def morph_readable(mc, stem=None):
    """human-readable mode, e.g. 'Hebrew verb · Piel', 'Greek adjective', 'Aramaic preposition'."""
    if not mc:
        return "— (no morphology — function word)"
    lang = morph_language(mc)
    cat = morph_category(mc)
    st = stem if stem is not None else morph_stem(mc)
    return f"{lang} {cat}" + (f" · {st}" if st else "")


def term_language(morph_codes):
    """A term's authoritative language from its occurrences' morph codes — the linguistic fact.

    Returns the dominant 'Hebrew' / 'Aramaic' / 'Greek' across the morph-bearing occurrences.
    Returns None when NO occurrence carries a morph: we make **no assertion** rather than guess,
    because the only other signal (the Strong's H/G prefix) is blind to Aramaic (Aramaic words carry
    H-numbers). The caller leaves such terms' existing language untouched. The morph is the truth;
    when morph changes, the term language (and stem, and the mode finding) must be re-derived from it.
    """
    from collections import Counter
    c = Counter()
    for mc in (morph_codes or []):
        ml = morph_language(mc)
        if ml in ("Hebrew", "Aramaic", "Greek"):
            c[ml] += 1
    return c.most_common(1)[0][0] if c else None
