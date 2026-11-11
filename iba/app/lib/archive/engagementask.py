"""engagementask.py -- small closed questions to the Ollama model about one surface in one verse (escalation #2412, design D).

The engagement step (lib/engagement.py, USER-GUIDE 8.18) asks of each surface item whether, in its verse, the surface does anything for the inner
being. Here that one judgement is put to the model as a narrow closed question, through the one route (lib/aiclient.py), with versioned prompts
(cfg_ai_prompt keys engagement.triage and engagement.triage_b) and one ai_call row for every attempt. Nothing is written to any other table: the
answers are read back from ai_call by the comparison; writing them into an assessment is a later, separate step.

An item is a verse_lexical row (its id is the key). The question carries the reference, the ESV text, the surface, its Strong's code and gloss.
Every answer is inferential (B:4)."""
from __future__ import annotations

BEARINGS = ("inner_being", "outward_act", "none")
PROMPT_KEYS = ("engagement.triage", "engagement.triage_b")
MODULE = "engagementask"


class EngagementAskError(Exception):
    """A usage problem: the item does not exist, so no question is made."""


def check_triage(a):
    """Reasons the answer is not usable (empty = usable): a bearing from the closed set and a non-empty quote from the verse is asked for."""
    if not isinstance(a, dict):
        return ["the answer is not a JSON object"]
    bad = []
    if a.get("bearing") not in BEARINGS:
        bad.append(f"bearing {a.get('bearing')!r} is not one of {list(BEARINGS)}")
    q = a.get("quote")
    if not isinstance(q, str) or not q.strip():
        bad.append("quote is empty")
    return bad


def result_of(a) -> str:
    return a["bearing"]


def gloss_of(conn, strong: str | None) -> str:
    """The STEP gloss of a Strong's code: exact code, else its base without the suffix letter; empty when there is none."""
    if not strong:
        return ""
    for code in (strong, strong[:5]):
        r = conn.execute("SELECT stepGloss FROM strong WHERE strongNumber=? AND deleted=0", (code,)).fetchone()
        if r and r[0]:
            return r[0]
    return ""


def item(conn, vl_id: int) -> dict:
    """The variables of the question for one verse_lexical row."""
    r = conn.execute("SELECT vl.id, lower(trim(vl.surface)), vl.strong, v.reference, v.text FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
                     "WHERE vl.id=? AND vl.deleted=0", (vl_id,)).fetchone()
    if r is None:
        raise EngagementAskError(f"verse_lexical {vl_id} does not exist")
    return {"reference": r[3], "text": r[4], "surface": r[1], "strong": r[2] or "none", "gloss": gloss_of(conn, r[2]) or "no gloss"}


def ask_triage(conn, client, vl_id: int, key: str = "engagement.triage") -> dict:
    """One triage question. Returns the client's result: {call_id, outcome, answer, error}."""
    if key not in PROMPT_KEYS:
        raise EngagementAskError(f"{key!r} is not an engagement triage prompt {list(PROMPT_KEYS)}")
    return client.call("judge", key, item(conn, vl_id), ("verse_lexical", vl_id), check=check_triage, result_of=result_of, step="triage")
