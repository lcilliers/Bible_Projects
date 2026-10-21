"""lexicalenrichgenerate.py — the LLM-calling half of `lexical.run`'s Layer 2 path (#1549).
Batches the resolved verse list into `passage.max_verses`-sized chunks (never a full cluster in one
call); for each chunk assembles a package, estimates its cost, calls the Anthropic Messages API,
parses the reply into the JSON shape `lexicalenrich.enrich_passage` expects, and logs real usage.

**Config-driven**: URL, API version, chars-per-token, model, token limits, rates, cost cap and log
path are `cfg_setting` rows (module `lexical`).

**System prompt built from the DB**: the catalogue `_notes_payload_dict` uses (`cfg_method_rule`,
the `cfg_enum` note_type/resolution_status values), so it cannot drift from config. Only
lexical.enrich's own rules are included. The prompt carries STRICT BOUNDARIES: the verse list is
closed, positions/code_ordinals come from the given codes, note volume is bounded, no prose
outside the JSON.

**Lean payload** (`_lean_code`): only fields a lexical.enrich rule uses; `existing_notes` omitted
when empty. Function-role codes are still sent: `connective` and `polarity` notes apply to them
(mechanical-columns-run-on-every-code-no-selection).
"""

from __future__ import annotations

import json
import os
import pathlib
import re


class ApiKeyMissing(Exception):
    """ANTHROPIC_API_KEY not found in the environment or repo-root .env."""


class ApiCallFailed(Exception):
    """The Messages API returned a non-2xx response."""


def _api_key() -> str:
    """ANTHROPIC_API_KEY from the environment, else from the repo-root .env (shared by every
    LLM-calling stage)."""
    key = os.getenv("ANTHROPIC_API_KEY")
    if key:
        return key
    env_path = pathlib.Path(".env")
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("ANTHROPIC_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
                if key:
                    return key
    raise ApiKeyMissing("ANTHROPIC_API_KEY not set in the environment or found in .env at the "
                        "repo root -- add it there (never commit it)")


class CostCapExceeded(Exception):
    """A single batch's estimated cost exceeds lexical.llm_max_cost_per_batch."""


class BadModelResponse(Exception):
    """The model's reply doesn't contain a parseable JSON object with a 'notes' or 'remove' key."""


_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*\})\s*```", re.DOTALL)


def _instructions(cfg, note_type_values: list[str], resolution_status_values: list[str],
                  method_rules: list[dict], verse_refs: list[str]) -> str:
    # only lexical.enrich's own rules; lexical.build's mechanical rules describe work already done
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
    """LLM projection of `_notes_payload_dict`'s code row: drops fields no lexical.enrich rule uses
    (`cluster`, kept in the human briefing) and omits `existing_notes` when empty."""
    return {k: v for k, v in c.items() if k not in ("cluster", "existing_notes", "resolved_sense")} \
        | ({"existing_notes": c["existing_notes"]} if c.get("existing_notes") else {})


def assemble_batch_package(ctx, verse_ids: list[int]) -> dict:
    """One chunk (capped to <= passage.max_verses by the caller). Returns the package plus a pre-call
    cost estimate; never calls the network. Builds the lean shape (`_lean_code`), not the human
    briefing shape."""
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
    """One live Messages API call. Returns {"text", "input_tokens", "output_tokens"}. URL/version are
    cfg_setting. Extended thinking is disabled explicitly (the API otherwise defaults to it and can
    spend the whole output budget on thinking), so `lexical.llm_max_output_tokens` is the answer's own
    budget, as the cost estimate assumes."""
    import requests
    key = _api_key()
    url = ctx.cfg.required_setting("lexical.llm_api_url")
    version = ctx.cfg.required_setting("lexical.llm_api_version")
    resp = requests.post(
        url,
        headers={"x-api-key": key, "anthropic-version": version, "content-type": "application/json"},
        json={"model": package["model"], "max_tokens": package["max_output_tokens"],
             "thinking": {"type": "disabled"},
             "system": package["instructions"],
             "messages": [{"role": "user", "content": package["content"]}]},
        timeout=600)
    if resp.status_code != 200:
        raise ApiCallFailed(f"Messages API returned {resp.status_code}: {resp.text[:500]}")
    data = resp.json()
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    usage = data.get("usage", {})
    if not text and data.get("stop_reason") == "max_tokens":
        raise ApiCallFailed(
            f"response hit max_tokens ({package['max_output_tokens']}) with no text content "
            f"produced (usage={usage}) -- the answer itself needs more room than "
            f"lexical.llm_max_output_tokens currently allows, raise it via configmaint.propose")
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
        # strict=False: tolerate raw control characters inside note text (#1826)
        parsed = json.loads(candidate, strict=False)
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
