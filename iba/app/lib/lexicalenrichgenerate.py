"""lexicalenrichgenerate.py — the LLM-calling half of `lexical.run`'s Layer 2 path (escalation
#1549 continued, 2026-09-07). Researcher, verbatim: "I was expecting to see a routine that
efficiently package the datasets for llm processing. I am aware that layer 2 will consume llm and
it must be part of the routine, rather than parking it." Before this, a Layer 2 call with no
`-PayloadPath` produced the notes briefing pack and stopped — a human/AI reading pass happened
OUTSIDE the routine, by hand. This module closes that gap: batches the resolved verse-list into
`passage.max_verses`-sized chunks (the same bound `lexical.enrich`'s own write path already
enforces — never a full-cluster push in one call, matching `project_api_reads_budget_bounded_small_
batches`), and for each chunk assembles a package, estimates its cost, calls the Anthropic Messages
API, parses the response into the exact JSON shape `lexicalenrich.enrich_passage` already expects,
and logs real usage — same shape as `handlers/reports:run` -> `lib/narrativegenerate.py`
(`report.book_narrative_generate`), the one other place this app makes a live LLM call.

**Config-driven from the start, unlike its own template.** `narrativegenerate.py` is CURRENTLY
flagged non-compliant in `cfg_utility` (escalation #648) for exactly this: `API_URL`/`API_VERSION`/
`CHARS_PER_TOKEN` hardcoded as module constants instead of `cfg_setting` rows. This module does not
repeat that — every one of those, plus model/token/rate/cost-cap/log-path, is `cfg_setting` (module
`lexical`), changeable via `configmaint.propose` with no code change.

**The system prompt is built from the DB, not a static doc.** `narrativegenerate.py` reads two
Markdown files off disk as its instructions. This module instead reuses `_notes_payload_dict`'s own
catalogue (`cfg_method_rule`, `cfg_enum` note_type/resolution_status values) — the same content a
human reading pass gets in the notes briefing — programmatically assembled into the system prompt.
Deliberately NOT a second copy of the payload-guide doc's prose: that doc can drift from the live
config (found live, escalation #1548, same session's own history) — a prompt built from the config
itself cannot drift from it by construction.

**Payload optimization pass, same session** (researcher: "did you optimise the payload... are you
passing more data through than what is necessary... did you do all the preprocessing that can be
done... is the process clear and concise... did you prepare boundaries so it would not drift"):
first version reused `_notes_payload_dict`'s human-briefing shape verbatim, unexamined. Checked
live against real M10c data and found genuinely wasteful: `cluster` (no method rule references it),
`existing_notes: []` sent on every code even though 100% were empty on a fresh cluster, and all 18
method_rules (5 of them `lexical.build`'s own MECHANICAL rules — language/testament derivation, the
H0853 exception — describing work already done, not this call's task) sent regardless of relevance.
`_lean_code`/`_instructions`'s `enrich_rules` filter fix this: ~10% smaller content on a real 20-verse/
531-code chunk, plus 5 irrelevant rules dropped from the prompt entirely. A STRICT BOUNDARIES section
was added to the prompt — verse list is closed and stated explicitly, positions/code_ordinals must
come from the given codes, note volume is bounded to what genuinely applies, no prose outside the
JSON shape. Also found live at the time: `resolved_sense` up to 3,938 chars for 277 strongs, filed
as escalation #1575 and then, per direct researcher instruction the same day ("remove it from the
column for all the lexicals"), removed corpus-wide at the SOURCE (`lib/lexical.py:resolve_code`
no longer writes it, for any code) — BUILD.md #254. `_lean_code` no longer even truncates it; the
field is dropped from the LLM payload entirely, since every row's value is now `None` regardless.

**Preprocessing NOT done, deliberately** — a broader win was considered and rejected: pre-classifying
`role='function'` codes as mechanically `inert` (skipping the LLM for them entirely) would have cut
the batch by ~36% (measured: 2,262 of 6,329 M10c codes are role='function'). Rejected because
`connective` and `polarity`(negation) note_types both legitimately apply to function-role codes —
a blanket role-based filter would silently reintroduce the exact "selective attention" bug this
app's own method rules were built to eliminate (`mechanical-columns-run-on-every-code-no-selection`,
found live 2026-09-03, Gal 5:16-17). A safer, narrower mechanical pre-filter (skip `status=
'unregistered'` codes entirely) is sound in principle but contributed nothing on this particular
cluster (M10c: 0 of 6,329 codes are unregistered) — not built, since there was no real case to prove
it against yet.
"""

from __future__ import annotations

import json
import re

from .narrativegenerate import _api_key, ApiKeyMissing, ApiCallFailed  # reuse, don't duplicate


class CostCapExceeded(Exception):
    """A single batch's estimated cost exceeds lexical.llm_max_cost_per_batch."""


class BadModelResponse(Exception):
    """The model's reply doesn't contain a parseable JSON object with a 'notes' or 'remove' key."""


_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*\})\s*```", re.DOTALL)


def _instructions(cfg, note_type_values: list[str], resolution_status_values: list[str],
                  method_rules: list[dict], verse_refs: list[str]) -> str:
    # Only lexical.enrich's OWN rules -- lexical.build's mechanical rules (language/testament
    # derivation, the H0853 exception, narrative_morph being Hebrew-only, etc.) describe work
    # already done before this call, not this call's own task. Including them was pure noise/token
    # cost the model has no use for -- found live answering the researcher's own "is the payload
    # optimized" question, same turn as #1575.
    enrich_rules = [r for r in method_rules if r["step"] == "lexical.enrich"]
    rules_text = "\n".join(f"- {r['rule_key']}: {r['rule_text']}" for r in enrich_rules)
    return (
        "You are producing a Window 1 Layer 2 payload for `lexical.enrich` — judgement-bearing "
        "findings about a mechanical Layer 1 reading (idioms, related-word families, connective "
        "classification, pronoun resolution, structural patterns, and so on). You will be given, "
        "per verse, the Layer 1 code-by-code reading (strong, role, morph_code, surface, position, "
        "code_ordinal) and the verse's own base text — no pre-computed sense/gloss is supplied "
        "(escalation #1575: that column served no purpose and was removed corpus-wide); reading the "
        "sense from the strong code and its morphology is part of this task. EVERY live code, "
        "regardless of role, needs at least one note row — for a genuinely inert function-role code "
        "with nothing to say, that means writing note_type='inert' explicitly, never skipping it "
        "silently (the completeness-by-code-count rule below checks every code, not just the "
        "content-bearing ones).\n\n"
        f"Valid note_type values: {note_type_values}\n"
        f"Valid resolution_status values: {resolution_status_values}\n\n"
        "Method rules governing this task:\n" + rules_text + "\n\n"
        "Addressing: every note names `verse` (OSIS ref), `position` (the code's own position "
        "within that verse), and `code_ordinal` (default 0 — only non-zero when a span carries "
        "more than one code at the same position). `target_verse`/`target_position` name ONE other "
        "code this note is about (an idiom's other half, a pronoun's antecedent). `related_codes` "
        "is a LIST of `{verse, position, code_ordinal}` for a note relating this code to several "
        "others. Every code needs AT LEAST ONE note row — if truly nothing applies, write one with "
        "note_type='inert' or the relevant type with resolution_status='checked_empty'/"
        "'unresolved'/'not_supported_this_language'. Never guess; where a test cannot resolve from "
        "this block's own data, resolution_status='unresolved' is correct and expected.\n\n"
        "STRICT BOUNDARIES — do not exceed this task:\n"
        f"- You are given exactly {len(verse_refs)} verse(s), listed at the end of this message. "
        "Every `verse` value you write MUST be one of exactly those — never a verse you recall from "
        "training data that isn't in this list, never a neighbouring verse.\n"
        "- Every `position`/`code_ordinal` you write must be one that appears in the `codes` list "
        "given to you — never invented, never guessed at a position not shown.\n"
        "- `target_verse`/`related_codes` MAY point outside this batch's own verse list ONLY when "
        "resolving a genuine cross-verse case your own data supports (e.g. a pronoun's antecedent "
        "one verse back) — never a fabricated reference.\n"
        "- Produce ONE note per note_type that genuinely applies to a code, not a note for every "
        "note_type value on every code, and not speculative commentary beyond what the finding "
        "field needs.\n"
        "- Do not add fields beyond the shape below, do not add prose before or after the JSON, do "
        "not explain your reasoning outside the `finding`/`evidence` fields.\n\n"
        f"Verses in this batch: {verse_refs}\n\n"
        "Respond with ONLY a JSON object, no other text, shaped exactly:\n"
        '{"notes": [{"verse": "...", "position": N, "code_ordinal": 0, "note_type": "...", '
        '"resolution_status": "...", "finding": "...", "evidence": "...", "target_verse": "...", '
        '"target_position": N, "related_codes": [{"verse": "...", "position": N}]}], "remove": []}'
    )


def _lean_code(c: dict) -> dict:
    """LLM-specific projection off `_notes_payload_dict`'s human-facing code row: drops fields with
    no demonstrated bearing on any lexical.enrich method rule (`cluster` — not referenced by any
    rule, kept in the human notes briefing only), omits `existing_notes` entirely when empty rather
    than sending `[]` on every one of potentially thousands of codes (measured live: 100% of a
    fresh cluster's codes have empty existing_notes — pure overhead for a first pass), and drops
    `resolved_sense` entirely — escalation #1575 removed it corpus-wide (it served no purpose,
    `resolve_code()` no longer writes it at all), so every row's value is now `None` and sending the
    key at all would be pure per-code overhead for zero information."""
    return {k: v for k, v in c.items() if k not in ("cluster", "existing_notes", "resolved_sense")} \
        | ({"existing_notes": c["existing_notes"]} if c.get("existing_notes") else {})


def assemble_batch_package(ctx, verse_ids: list[int]) -> dict:
    """One chunk (already capped to <= passage.max_verses by the caller). Returns the package plus
    a pre-call cost estimate — never calls the network itself. Builds a LEAN, LLM-specific content
    shape (`_lean_code`), not `_notes_payload_dict`'s output verbatim — that function's shape is for
    a human reading a briefing file, not for minimizing what an API call pays to transmit."""
    from ..handlers.lexical import _notes_payload_dict   # local import, avoids a circular top-level
    payload = _notes_payload_dict(ctx, verse_ids)
    verse_refs = [v["verse"] for v in payload["verses"]]
    lean_codes = [_lean_code(c) for c in payload["codes"]]
    instructions = _instructions(ctx.cfg, payload["note_type_values"],
                                 payload["resolution_status_values"], payload["method_rules"],
                                 verse_refs)
    content = json.dumps({"verses": payload["verses"], "codes": lean_codes}, ensure_ascii=False)

    chars_per_token = float(ctx.cfg.setting("lexical.llm_chars_per_token", 4))
    est_input_tokens = int((len(instructions) + len(content)) / chars_per_token)
    max_output_tokens = int(ctx.cfg.setting("lexical.llm_max_output_tokens", 8000))
    rate_in = float(ctx.cfg.setting("lexical.llm_rate_input_per_million", 3.00))
    rate_out = float(ctx.cfg.setting("lexical.llm_rate_output_per_million", 15.00))
    est_cost = (est_input_tokens / 1_000_000 * rate_in) + (max_output_tokens / 1_000_000 * rate_out)

    return {
        "instructions": instructions, "content": content, "verse_ids": verse_ids,
        "code_count": len(lean_codes), "est_input_tokens": est_input_tokens,
        "max_output_tokens": max_output_tokens, "est_cost_usd": round(est_cost, 4),
        "model": ctx.cfg.required_setting("lexical.llm_model"),
    }


def call_api(ctx, package: dict) -> dict:
    """One live Messages API call. Returns {"text", "input_tokens", "output_tokens"}. URL/version
    are cfg_setting, not module constants (see module docstring)."""
    import requests
    key = _api_key()
    url = ctx.cfg.required_setting("lexical.llm_api_url")
    version = ctx.cfg.required_setting("lexical.llm_api_version")
    resp = requests.post(
        url,
        headers={"x-api-key": key, "anthropic-version": version, "content-type": "application/json"},
        json={"model": package["model"], "max_tokens": package["max_output_tokens"],
             "system": package["instructions"],
             "messages": [{"role": "user", "content": package["content"]}]},
        timeout=600)
    if resp.status_code != 200:
        raise ApiCallFailed(f"Messages API returned {resp.status_code}: {resp.text[:500]}")
    data = resp.json()
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    usage = data.get("usage", {})
    return {"text": text, "input_tokens": usage.get("input_tokens", 0),
           "output_tokens": usage.get("output_tokens", 0)}


def parse_response(text: str) -> dict:
    """The model is asked for bare JSON but may still fence it in ```json ... ``` — handle both.
    Raises BadModelResponse (never lets a malformed reply reach enrich_passage as if it were a
    valid payload)."""
    candidate = text.strip()
    m = _JSON_FENCE_RE.search(candidate)
    if m:
        candidate = m.group(1)
    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError as e:
        raise BadModelResponse(f"model reply is not valid JSON: {e} -- first 300 chars: {text[:300]!r}")
    if "notes" not in parsed and "remove" not in parsed:
        raise BadModelResponse(f"model reply has neither 'notes' nor 'remove': {list(parsed.keys())}")
    return parsed


def log_usage(cfg, run_id: str, chunk_label: str, model: str, input_tokens: int,
             output_tokens: int, cost_usd: float) -> None:
    import csv
    import datetime
    import pathlib
    log_path = pathlib.Path(cfg.required_setting("lexical.llm_usage_log_path"))
    log_path.parent.mkdir(parents=True, exist_ok=True)
    is_new = not log_path.exists()
    with log_path.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if is_new:
            w.writerow(["run_id", "chunk", "model", "input_tokens", "output_tokens", "cost_usd",
                       "called_at"])
        w.writerow([run_id, chunk_label, model, input_tokens, output_tokens, f"{cost_usd:.4f}",
                   datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")])
