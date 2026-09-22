"""subgroupgenerate.py — the LLM-calling half of `cluster.subgroup` (process b, the `char-subgroup`
stage, escalation #1706 Phase F / design #1690, built 2026-09-17). Sibling to
`versereadinggenerate.py`, same separation: this module only assembles the payload and calls the
API; `recordingpass.py` is the only thing that ever writes `cluster_subgroup`/
`cluster_subgroup_strong` (single-writer discipline, checklist rule 0.1).

**Whole-cluster, ONE call, never batched** (`full-cluster-read-before-assignment`, #1690 §2(a)) —
unlike `lexical.meaning`'s per-`passage.max_verses` chunking, subgroup formation is a holistic
judgement over the cluster's ENTIRE member-strong set at once; splitting it into batches would
mean no batch ever sees the full picture rule (a) requires. If a cluster's estimated cost/token
count is too large for one call, the run refuses (cost-cap, same discipline as every other stage)
rather than silently chunking against the rule's own intent.

**Input, per member strong:** `strong.stepGloss`/`stepTransliteration` (the gloss/surface reading
rule (a) requires), its Stage 1 (`verse-reading`) `ib_observation` rows already captured in the DB
(the real analytical grounding — this is what makes subgroup formation MEANING-based rather than a
cold read of dictionary glosses alone, #1690 §2(b)), and its distinct surface forms actually
occurring in the corpus (deduped, capped — never a full occurrence dump, `project_api_reads_budget_
bounded_small_batches`).

**`placement_note` vs `observations` — corrected 2026-09-17, researcher's own words this session:**
*"the mechanism is not undecided, the capture program for the ib_observation from the llm must
place the item on the observation... it sounds to me that the llm instructions does not include
the flag [tag] types, with the result that llm is not actually helping to identify the observation.
a placement note is by definition a comment about the observation, and not the observation
itself."* The first version of this module gave the LLM no `observations` output at all and no
`tag` vocabulary — so every substantive analytical claim it wanted to make had nowhere to go except
`placement_note`, which is structurally the wrong place for it. Fixed: the LLM now gets the SAME
`ib_observation.tag` vocabulary Stage 1 already uses and a dedicated `observations` array in its
output shape, captured by the exact same `recordingpass.record_batch` mechanism Stage 1's
`ib_observation`/`ib_node` capture already uses (`stage='char-subgroup'`) — no separate
classification heuristic needed, because the LLM now states directly which output is which.
`placement_note` is redefined strictly as a short pointer/rationale for the placement decision
itself (why this strong is in this subgroup, or why it's FLAGged) — never the substantive claim.
"""

from __future__ import annotations

import json
import re

from .narrativegenerate import ApiKeyMissing, ApiCallFailed  # noqa: F401 -- re-exported
from .lexicalenrichgenerate import call_api, log_usage  # reuse, don't duplicate
from .lexicalenrichgenerate import CostCapExceeded, BadModelResponse  # noqa: F401 -- re-exported
from .versereadinggenerate import _meaning_sources  # reuse, don't duplicate
from .taggingguidance import tags_for_stage, guidance_block  # reuse, don't duplicate


_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*\})\s*```", re.DOTALL)

_MAX_SURFACE_FORMS_PER_STRONG = 8


def parse_response(text: str) -> dict:
    """This stage's own shape ({"subgroups": [...], "observations": [...]}) -- observations may be
    an empty list (not every cluster necessarily yields a standalone observation beyond its
    placements) but the key itself must be present, same discipline as 'subgroups'."""
    candidate = text.strip()
    m = _JSON_FENCE_RE.search(candidate)
    if m:
        candidate = m.group(1)
    try:
        # strict=False: escalation #1826 -- tolerate raw control characters inside obs_text
        # (Python's own documented leniency), not a custom sanitizer.
        parsed = json.loads(candidate, strict=False)
    except json.JSONDecodeError as e:
        raise BadModelResponse(f"model reply is not valid JSON: {e} -- first 300 chars: {text[:300]!r}")
    if "subgroups" not in parsed:
        raise BadModelResponse(f"model reply has no 'subgroups' key: {list(parsed.keys())}")
    if "observations" not in parsed:
        raise BadModelResponse(f"model reply has no 'observations' key: {list(parsed.keys())}")
    return parsed


def _strong_profile(conn, strong: str) -> dict:
    row = conn.execute(
        "SELECT stepGloss, stepTransliteration FROM strong WHERE strongNumber=?", (strong,)
    ).fetchone()
    surfaces = [r["surface"] for r in conn.execute(
        "SELECT DISTINCT surface FROM verse_lexical WHERE strong=? AND deleted=0 "
        "AND surface IS NOT NULL AND surface != '' LIMIT ?",
        (strong, _MAX_SURFACE_FORMS_PER_STRONG))]
    observations = [
        {"question_code": r["question_code"], "tag": r["tag"], "obs_text": r["obs_text"]}
        for r in conn.execute(
            "SELECT question_code, tag, obs_text FROM ib_observation "
            "WHERE strong=? AND stage='verse-reading' ORDER BY id", (strong,))]
    profile = {
        "gloss": row["stepGloss"] if row else None,
        "transliteration": row["stepTransliteration"] if row else None,
        "surface_forms": surfaces,
        "verse_reading_observations": observations,
    }
    profile["meaning_sources"] = _meaning_sources(conn, strong)
    return profile


def assemble_cluster_package(ctx, cluster_code: str, member_strongs: list[str]) -> dict:
    """One whole-cluster payload -- never calls the network itself, returns the package plus a
    pre-call cost estimate (same two-step separation every other stage already uses)."""
    conn = ctx.db.conn

    strong_profiles = {s: _strong_profile(conn, s) for s in sorted(member_strongs)}

    rules = conn.execute(
        "SELECT rule_key, rule_text FROM cfg_method_rule WHERE step='cluster.subgroup' "
        "AND active=1 ORDER BY ordinal, rule_key").fetchall()
    rules_text = "\n".join(f"- {r['rule_key']}: {r['rule_text']}" for r in rules)

    tag_values = tags_for_stage("char-subgroup", [r["value"] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='ib_observation.tag' AND inactive=0 "
        "ORDER BY ordinal")])

    instructions = _instructions(cluster_code, rules_text, sorted(member_strongs), tag_values)
    content = json.dumps({"cluster_code": cluster_code, "strongs": strong_profiles},
                         ensure_ascii=False)

    chars_per_token = float(ctx.cfg.setting("lexical.llm_chars_per_token", 4))
    est_input_tokens = int((len(instructions) + len(content)) / chars_per_token)
    max_output_tokens = int(ctx.cfg.setting("cluster.subgroup_llm_max_output_tokens", 8000))
    rate_in = float(ctx.cfg.setting("lexical.llm_rate_input_per_million", 3.00))
    rate_out = float(ctx.cfg.setting("lexical.llm_rate_output_per_million", 15.00))
    est_cost = (est_input_tokens / 1_000_000 * rate_in) + (max_output_tokens / 1_000_000 * rate_out)

    return {
        "instructions": instructions, "content": content, "cluster_code": cluster_code,
        "strong_count": len(member_strongs), "est_input_tokens": est_input_tokens,
        "max_output_tokens": max_output_tokens, "est_cost_usd": round(est_cost, 4),
        "model": ctx.cfg.required_setting("lexical.llm_model"),
    }


def _instructions(cluster_code: str, rules_text: str, member_strongs: list[str],
                  tag_values: list[str]) -> str:
    return (
        f"You are forming meaning-based subgroups (families) of the strongs belonging to cluster "
        f"{cluster_code}, the char-subgroup stage (process b) of the cluster-reading pipeline. You "
        f"are given, per strong: its dictionary gloss/transliteration, a sample of its distinct "
        f"surface forms as they actually occur in the corpus, its already-captured verse-reading "
        f"observations (real analytical grounding from a prior stage -- read these as primary "
        f"evidence of what the word actually means in context, not just the dictionary gloss), and "
        f"its meaning_sources (strong_meaning_tree/strong_lexicon.lsj/strong_lexicon.mounce).\n\n"
        f"Method rules governing this task:\n{rules_text}\n\n"
        f"TWO DIFFERENT OUTPUTS -- do not confuse them:\n"
        f"- `placement_note` is ONLY a short rationale for the placement decision itself -- why "
        f"this strong belongs in this subgroup, or why it's FLAGged. It is a comment ABOUT a "
        f"placement, never the analytical claim itself.\n"
        f"- `observations` is where any substantive analytical finding goes -- anything you notice "
        f"about a strong's meaning, usage, or relationship to others while forming subgroups that "
        f"is worth recording in its own right (a real insight, a distinction from a similar word, "
        f"a structural-opposite pairing, etc.). If you have something to say beyond 'why I placed "
        f"it here,' it belongs in `observations`, not `placement_note`.\n\n"
        f"STRICT BOUNDARIES -- do not exceed this task:\n"
        f"- You must place every one of these {len(member_strongs)} strongs into exactly one "
        f"subgroup, no exceptions: {member_strongs}\n"
        f"- A strong that doesn't fit any real subgroup goes under subgroup_code \"FLAG\" -- state "
        f"the reason in that member's placement_note (required for FLAG, optional otherwise).\n"
        f"- Every non-FLAG subgroup needs: a stable subgroup_code (short, descriptive, e.g. "
        f"\"A_diligence\"), a label true to its essence (not a word list), a one-sentence "
        f"core_description, and an anchor_verse_reference -- the one verse (drawn from an "
        f"occurrence of one of its own member strongs, from that strong's verse_reading_"
        f"observations or surface_forms context) that best represents the subgroup's shared "
        f"characteristic.\n"
        f"- FLAG needs no label/core_description/anchor_verse_reference -- it is a signpost, not a "
        f"real subgroup.\n"
        f"- Valid `tag` values for observations: {tag_values}\n"
        f"{guidance_block(tag_values)}\n"
        f"- Each observation's `strong` must be one of this cluster's own member strongs.\n"
        f"- Do not add fields beyond the shape below, no prose before or after the JSON.\n\n"
        "Respond with ONLY a JSON object, no other text, shaped exactly:\n"
        '{"subgroups": [{"subgroup_code": "...", "label": "..." or null, "core_description": '
        '"..." or null, "anchor_verse_reference": "..." or null, '
        '"members": [{"strong": "...", "placement_note": "..." or null}]}], '
        '"observations": [{"strong": "...", "tag": "...", "obs_text": "...", '
        '"question_code": null, "meaning_source": "..." or null, '
        '"occurrences": [{"verse": "...", "surface": "...", "morph_code": "..."}]}]}'
    )
