"""charanswergenerate.py — the LLM-calling half of `cluster.answer` (the `char-answers` stage,
process (d), escalation #1706 Phase F stage 4, built 2026-09-18). Sibling to
`charreadinggenerate.py`, same separation: this module only assembles the payload and calls the
API; `recordingpass.py` is the only thing that ever writes `ib_observation`/`ib_node`.

**Scope grain: per-subgroup, never the whole cluster** (`#1682` §4A rule 1 / checklist §3 rule 1) —
one LLM call per `cluster_subgroup`, answering the catalogue's "characteristic-grain" battery
against that subgroup's accumulated evidence (Stage 1/2/3's own observations plus full occurrence
data). Same output shape as Stages 1–3 ({"observations": [...]}) -- the only real difference from
Stage 3 is that `question_code` is now genuinely populated with catalogue leaf codes, and an
observation may be grounded in the SUBGROUP as a whole (`strong: null`, each occurrence carrying
its OWN `strong`) rather than one specific member strong.

**Battery scope, deliberately narrowed, both exclusions already-documented gaps, not new
judgement calls of this build:**
1. Every active leaf question whose `scope` is `Characteristic (HIB behaviour)` /
   `Characteristic relational` / `The HIB` / `Other non-human beings` -- the four scope values
   `#1682` §4A itself names as "answered across the family's evidence as a whole" (as opposed to
   `Word/term (lexical)`/`Verse-context`, which Stage 1 already substantially covers at occurrence
   grain).
2. `D7.7.1` excluded -- despite carrying scope `Characteristic (HIB behaviour)` in the catalogue,
   this exact code is ALREADY answered by Stage 1 (`versereadinggenerate.py`'s own catalogue
   linkage, per-verse/per-home-strong) -- answering it again here would duplicate, not extend,
   existing live data. The scope-label vs. actual-answering-stage mismatch is a real, noted
   discrepancy, not silently resolved by picking one side.
3. Science-extract-dependent questions excluded (`question_text LIKE '%science extract%'` --
   currently `D9.1.1`/`D9.2.1`/`D11.2.1`/`D12.1.1`) -- the checklist's own Stage 4 status names this
   wiring "not decided or built" (`BUILD.md` #287's own carried-forward checklist). Answering these
   without the science-extract file actually wired in would either invent an unsupported claim or
   silently ignore the question's own explicit instruction -- neither is this build's call to make.
4. `cross_family_or_cluster_flags` (checklist §3 rule 5) is NOT requested from the model this
   build -- its own `tag` value is explicitly still unchosen (checklist "still-open items" list),
   unlike `needs_adjacent_verse_context` (registered this same session, #1706 v36) which IS ready
   to use. Inventing a tag name here would bake a design decision into a code build, not apply one
   already made.
"""

from __future__ import annotations

import json
import re

from .narrativegenerate import ApiKeyMissing, ApiCallFailed  # noqa: F401 -- re-exported
from .lexicalenrichgenerate import call_api, log_usage  # reuse, don't duplicate
from .lexicalenrichgenerate import CostCapExceeded, BadModelResponse  # noqa: F401 -- re-exported
from .versereadinggenerate import _meaning_sources  # reuse, don't duplicate
from .charreadinggenerate import _full_occurrences  # reuse, don't duplicate


_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*\})\s*```", re.DOTALL)

_EXCLUDED_QUESTION_CODES = ("D7.7.1",)


def parse_response(text: str) -> dict:
    """Same shape as Stages 1-3 ({"observations": [...]})."""
    candidate = text.strip()
    m = _JSON_FENCE_RE.search(candidate)
    if m:
        candidate = m.group(1)
    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError as e:
        raise BadModelResponse(f"model reply is not valid JSON: {e} -- first 300 chars: {text[:300]!r}")
    if "observations" not in parsed:
        raise BadModelResponse(f"model reply has no 'observations' key: {list(parsed.keys())}")
    return parsed


def battery_questions(conn) -> list[dict]:
    """The characteristic-grain catalogue battery this stage answers -- see module docstring for
    the 3 deliberate exclusions. Queried live, never hardcoded, so a catalogue change is picked up
    automatically (same discipline every other stage's own question list already follows)."""
    rows = conn.execute(
        "SELECT question_code, question_text, scope FROM wa_obs_question_catalogue "
        "WHERE deleted=0 AND status='active' AND scope IN ("
        "'Characteristic (HIB behaviour)', 'Characteristic relational', 'The HIB', "
        "'Other non-human beings') AND question_text NOT LIKE '%science extract%' "
        "AND question_code NOT IN ({}) ORDER BY question_code".format(
            ",".join("?" * len(_EXCLUDED_QUESTION_CODES))),
        _EXCLUDED_QUESTION_CODES).fetchall()
    return [{"question_code": r["question_code"], "question_text": r["question_text"],
            "scope": r["scope"]} for r in rows]


def _strong_answer_profile(conn, strong: str) -> dict:
    row = conn.execute(
        "SELECT stepGloss, stepTransliteration FROM strong WHERE strongNumber=?", (strong,)
    ).fetchone()

    def _obs(stage: str) -> list[dict]:
        return [{"question_code": r["question_code"], "tag": r["tag"], "obs_text": r["obs_text"]}
                for r in conn.execute(
                    "SELECT question_code, tag, obs_text FROM ib_observation "
                    "WHERE strong=? AND stage=? ORDER BY id", (strong, stage))]

    return {
        "gloss": row["stepGloss"] if row else None,
        "transliteration": row["stepTransliteration"] if row else None,
        "occurrences": _full_occurrences(conn, strong),
        "meaning_sources": _meaning_sources(conn, strong),
        "verse_reading_observations": _obs("verse-reading"),
        "char_subgroup_observations": _obs("char-subgroup"),
        "char_reading_observations": _obs("char-reading"),
        "prior_char_answer_observations": _obs("char-answers"),  # re-read rule, empty on first run
    }


def assemble_subgroup_package(ctx, cluster_code: str, subgroup_row: dict,
                              member_strongs: list[str]) -> dict:
    """One subgroup's payload -- never calls the network itself, returns the package plus a
    pre-call cost estimate (same two-step separation every other stage already uses)."""
    conn = ctx.db.conn

    strong_profiles = {s: _strong_answer_profile(conn, s) for s in sorted(member_strongs)}
    questions = battery_questions(conn)

    rules = conn.execute(
        "SELECT rule_key, rule_text FROM cfg_method_rule WHERE step='cluster.answer' "
        "AND active=1 ORDER BY ordinal, rule_key").fetchall()
    rules_text = "\n".join(f"- {r['rule_key']}: {r['rule_text']}" for r in rules)

    tag_values = [r["value"] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='ib_observation.tag' AND inactive=0 "
        "ORDER BY ordinal")]

    instructions = _instructions(cluster_code, subgroup_row, rules_text, sorted(member_strongs),
                                 questions, tag_values)
    content = json.dumps({
        "cluster_code": cluster_code, "subgroup_code": subgroup_row["subgroup_code"],
        "label": subgroup_row["label"], "core_description": subgroup_row["core_description"],
        "anchor_verse_reference": subgroup_row["anchor_verse_reference"],
        "strongs": strong_profiles,
    }, ensure_ascii=False)

    chars_per_token = float(ctx.cfg.setting("lexical.llm_chars_per_token", 4))
    est_input_tokens = int((len(instructions) + len(content)) / chars_per_token)
    max_output_tokens = int(ctx.cfg.setting("lexical.llm_max_output_tokens", 40000))
    rate_in = float(ctx.cfg.setting("lexical.llm_rate_input_per_million", 3.00))
    rate_out = float(ctx.cfg.setting("lexical.llm_rate_output_per_million", 15.00))
    est_cost = (est_input_tokens / 1_000_000 * rate_in) + (max_output_tokens / 1_000_000 * rate_out)

    return {
        "instructions": instructions, "content": content, "cluster_code": cluster_code,
        "subgroup_code": subgroup_row["subgroup_code"], "strong_count": len(member_strongs),
        "question_count": len(questions), "est_input_tokens": est_input_tokens,
        "max_output_tokens": max_output_tokens, "est_cost_usd": round(est_cost, 4),
        "model": ctx.cfg.required_setting("lexical.llm_model"),
    }


def compute_question_checks(conn, cluster_code: str, member_strongs: list[str],
                            question_codes: list[str]) -> list[dict]:
    """Stage 4's own completeness check, code-computed after the write, same discipline as Stage
    3's `compute_strong_checks` -- but the unit here is a CATALOGUE QUESTION, not an occurrence
    (this stage answers questions, it doesn't scan occurrences fresh). `ib_observation` has no
    subgroup identifier column at all (checked live, schema fixed, not this build's call to
    change) -- a subgroup's own coverage is recovered via its member strongs' `ib_node` rows
    instead, since every strong belongs to exactly one subgroup by construction (checklist §1 rule
    9): a question counts as answered for this subgroup if some `char-answers` observation for it
    has at least one `ib_node` row citing one of this subgroup's own member strongs (works whether
    the observation's own `strong` is set directly, or null with per-occurrence strong, per the
    2026-09-18 `recordingpass.py` fix)."""
    if not member_strongs:
        return [{"question_code": q, "answered": False} for q in question_codes]
    ph = ",".join("?" * len(member_strongs))
    answered = {r["question_code"] for r in conn.execute(
        f"SELECT DISTINCT o.question_code FROM ib_observation o "
        f"JOIN ib_node n ON n.observation_id = o.id "
        f"WHERE o.stage='char-answers' AND o.cluster_code=? AND n.strong IN ({ph})",
        [cluster_code] + member_strongs)}
    return [{"question_code": q, "answered": q in answered} for q in question_codes]


def _instructions(cluster_code: str, subgroup_row: dict, rules_text: str,
                  member_strongs: list[str], questions: list[dict],
                  tag_values: list[str]) -> str:
    q_text = "\n".join(f"- {q['question_code']} ({q['scope']}): {q['question_text']}"
                       for q in questions)
    return (
        f"You are answering the characteristic-grain catalogue battery (process d, char-answers) "
        f"for subgroup {subgroup_row['subgroup_code']!r} of cluster {cluster_code} -- "
        f"\"{subgroup_row['label']}\" ({subgroup_row['core_description']}). This subgroup's own "
        f"member strongs are {member_strongs}. You are given, per strong: gloss, EVERY occurrence "
        f"corpus-wide, all meaning sources, and its own observations already captured at every "
        f"prior stage (verse-reading, char-subgroup, char-reading -- real analytical grounding, "
        f"read this as your primary evidence, do not re-derive it from scratch) plus any of its "
        f"own prior char-answer observations (if this is a re-read).\n\n"
        f"Method rules governing this task:\n{rules_text}\n\n"
        f"CORE RULE — MULTIPLE SLANTS, NOT ONE DISTILLED ANSWER: where the subgroup's own strongs "
        f"or evidence genuinely point to different answers to the same question, produce a SEPARATE "
        f"observation for EACH distinct slant, all under the SAME question_code -- never flatten "
        f"into one 'the characteristic means X' answer. A single slant is correct only when the "
        f"evidence actually is uniform across every member strong, not a default.\n\n"
        f"EVIDENCE TRAIL, per scope: for a slant grounded in ONE specific member strong, set "
        f"`strong` to that strong's code and cite its own occurrences. For a slant grounded in the "
        f"SUBGROUP AS A WHOLE (evidence spanning several member strongs), leave `strong` null on "
        f"the observation itself, but EVERY element of `occurrences` MUST carry its own `strong` "
        f"field naming which member strong that specific citation belongs to -- an occurrence "
        f"without its own strong cannot be resolved and will be silently dropped.\n\n"
        f"Answer these catalogue questions (one or more observations per question_code, per the "
        f"multiple-slants rule above):\n{q_text}\n\n"
        f"Valid `tag` values: {tag_values}\n"
        f"Use `needs_adjacent_verse_context` where a verse's own content is insufficient and an "
        f"adjacent verse would help -- state explicitly in obs_text what's outstanding and what "
        f"the follow-up cross-check needs to establish (never a bare flag). Use "
        f"`could-not-resolve` where a genuine can't-resolve case arises, stating what signal "
        f"suggests it should be resolvable with further analysis. Use `answered-no-flag` for a "
        f"plain, substantive answer with nothing else to categorise.\n\n"
        f"STRICT BOUNDARIES — do not exceed this task:\n"
        f"- `question_code` MUST be one of the exact leaf codes listed above -- never a bare "
        f"component code, never a code not in this list.\n"
        f"- Do NOT attempt cross-family/cross-cluster comparison or flagging in this run -- that "
        f"belongs to a later synergy stage, out of scope here.\n"
        f"- Every `strong` value you write (on an observation or an occurrence) must be one of "
        f"{member_strongs}.\n"
        f"- Every `verse` value in `occurrences` must be one you were actually given for that "
        f"strong.\n"
        f"- Do not add fields beyond the shape below, no prose before or after the JSON.\n\n"
        "Respond with ONLY a JSON object, no other text, shaped exactly:\n"
        '{"observations": [{"strong": "..." or null, "question_code": "...", "tag": "...", '
        '"obs_text": "...", "meaning_source": "..." or null, "occurrences": [{"strong": "...", '
        '"verse": "...", "surface": "...", "morph_code": "..."}]}]}'
    )
