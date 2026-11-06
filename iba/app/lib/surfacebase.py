"""surfacebase.py -- the shape of an AI base answer (escalation #2359, #2361).

The base of a surface word is asked of the AI through lib/aiclient.py (Surface-Base.ps1 -Action Ask, prompt base.word); this module holds the check of the
answer: a known relation (cfg_setting surface_judge.base_relations: inflection, derivation, none), and for inflection or derivation a base that is one word
of the configured pattern (surface_judge.base_form_pattern) and is not the word itself. The rule of similar root meaning is in the prompt. The file route of
the earlier prototype (an input list and a batch file) was retired in stage 6 of #2361; its answers are loaded into ai_call and surface_derivation.
"""
from __future__ import annotations

import re

from . import surfacejudge as sj

BaseError = sj.JudgeError


def check_answer(ans: dict, word: str, vals: dict) -> list[str]:
    """Reasons the answer is not usable (empty list when it is). The rule of similar root meaning is in the
    question; here the shape is held: a known relation, and for inflection or derivation a base that is one
    word of the configured pattern and is not the word itself."""
    if not isinstance(ans, dict):
        return ["not an object"]
    rel = ans.get("relation")
    if rel not in vals["base_relations"]:
        return [f"relation {rel!r}"]
    base = ans.get("base")
    if rel == "none":
        if base not in (None, "", word):
            return [f"relation none but base {base!r} is not the word"]
        return []
    if not isinstance(base, str) or not re.fullmatch(vals["base_form_pattern"], base):
        return [f"base {base!r} does not match the pattern"]
    if base == word:
        return [f"relation {rel} but base is the word itself"]
    return []
