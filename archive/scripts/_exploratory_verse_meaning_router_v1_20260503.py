"""_exploratory_verse_meaning_router_v1_20260503.py — read-only prototype.

The new verse-interpretation routine. For each (verse, term) pair, calls
Claude Opus 4.7 with the verse-context-record JSON and the §3 filter framing,
and produces:

  (a) Meaning statement — atomic, unsorted, not consolidated against other
      verses; what THIS verse says about the inner-being characteristic via
      THIS term.
  (b) Unresolved interpretation pointers — tangible questions the verse
      raises that cannot be answered from the verse itself.

Output is parallelisable: one Claude call per (verse, term). No grouping or
anchor decisions are made here — those are downstream consolidation passes.

Inputs:
  - Verse-context-record JSON (from _exploratory_verse_context_record_v1_*.py)
  - Optional --verse / --term filters

Outputs:
  - outputs/markdown/verse-meaning-router-results-{date}.json
  - outputs/markdown/verse-meaning-router-results-{date}.md  (readable summary)

Required:
  ANTHROPIC_API_KEY in environment or .env
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

try:
    from dotenv import load_dotenv
    load_dotenv(".env")
except ImportError:
    pass

import anthropic

INPUT_JSON = os.path.join("outputs", "markdown",
                          "verse-context-records-sample-20260503.json")
OUT_DIR = os.path.join("outputs", "markdown")
DEFAULT_MODEL = "claude-opus-4-7"

# Pricing per 1M tokens (input, output, cache_create, cache_read) — for cost estimates
PRICING = {
    "claude-opus-4-7":   (5.00, 25.00, 6.25, 0.50),
    "claude-opus-4-6":   (5.00, 25.00, 6.25, 0.50),
    "claude-sonnet-4-6": (3.00, 15.00, 3.75, 0.30),
    "claude-haiku-4-5":  (1.00,  5.00, 1.25, 0.10),
}

# Output schema for structured output — matches the design doc shape
OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "meaning": {
            "type": "string",
            "description": (
                "One atomic statement of what THIS verse says about the inner-being "
                "characteristic via THIS term. Not consolidated against other verses; "
                "not a group description. If the term does not engage the inner being "
                "in this verse, briefly state that and name the set-aside category "
                "(no_inner_being / physical_only / spatial_only / wrong_face / other) "
                "with one-line justification."
            ),
        },
        "unresolved_pointers": {
            "type": "array",
            "description": (
                "Tangible questions the verse raises that cannot be answered from "
                "the verse alone. Each pointer must name a specific external thing "
                "(parallel verse, translation crux, rhetorical attribution, "
                "programme-level concept). 'More research needed' / 'this is uncertain' "
                "do not qualify. May be empty."
            ),
            "items": {
                "type": "object",
                "properties": {
                    "pointer": {
                        "type": "string",
                        "description": "Short identifier in snake_case, e.g. 'be-ir_translation_crux'.",
                    },
                    "description": {
                        "type": "string",
                        "description": (
                            "What the pointer names, what specifically it requires "
                            "(parallel passage, lexical check, etc.), and why the "
                            "verse alone cannot answer it."
                        ),
                    },
                },
                "required": ["pointer", "description"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["meaning", "unresolved_pointers"],
    "additionalProperties": False,
}

SYSTEM_PROMPT = """You are a verse-interpretation classifier for the Soul Word Analysis Programme — a structured Bible research project.

For each (verse, term) pair, your job is to produce exactly two things:

(a) MEANING — one atomic statement of what THIS verse says about the inner-being characteristic via THIS term.

(b) UNRESOLVED POINTERS — tangible questions raised by the verse that cannot be answered from the verse alone.

THE GOVERNING FILTER (§3 of the Verse Context instruction):

> Does this verse, through the use of this term, say something about the inner being — understood as the non-physical, internal states, capacities, and expressions that constitute a person's invisible life: how a person thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God?

A verse PASSES when the term's use engages one or more of:
- An internal state — emotion, feeling, disposition, attitude
- A capacity of the inner life — will, intention, thought, belief, desire
- A relational orientation — how the person is oriented inwardly toward God, others, or themselves
- A moral or character quality of the whole person
- A spiritual characteristic — responsiveness to God, spiritual condition, worship disposition

A verse DOES NOT pass when the term's use is:
- physical_only — body part, physical process, material object
- no_inner_being — external conduct/events with no window into inner life through this term
- spatial_only — locational/geographical with no inner-being engagement
- wrong_face — verse has inner-being content but a DIFFERENT term carries it (not this one)
- other — none of the above; explain in meaning text

CRITICAL DISTINCTIONS:

- Filter at TERM level, not verse level. A verse can have inner-being content carried by a different term; this term's specific use may still be physical/spatial. Always check what THIS term is doing in this verse.
- For grammatical particles (pronouns, conjunctions, adverbs): assess whether the particle directs/intensifies/qualifies/discloses inner-being content. Mere presence in an inner-being verse is not sufficient.
- For expressions (cries, calls, groans): the filter passes if the act plausibly originates in an inner state, even if no inner-state word is named. Force/character of the expression implies inner origin.
- For wrong_face cases: the verse has genuine inner-being content but a different term carries it. Identify the carrier term in the meaning text.

WRITING DISCIPLINE FOR MEANING:

- Write atomically. Do not consolidate against other verses or generalise.
- Name the inner-being characteristic the term engages in THIS verse.
- State the term's role: seat / channel / expression / mechanism / obstacle / counterpart / etc.
- Quote or reference the original-language form when the spans data shows morphology that matters (e.g. construct chain, suffix, stem).
- For set-asides, state the category and one-line justification — that IS the meaning statement for this verse.

WRITING DISCIPLINE FOR POINTERS:

- Each pointer must name something specific and external — a parallel verse reference, a translation crux, a rhetorical attribution question, a programme-level concept.
- "More research needed" or "this is uncertain" are NOT pointers — they are silence.
- A pointer is for "I cannot answer this without [external resource X]" — not "this is interesting".
- Empty pointer list is the correct answer when the verse is fully resolved by reading.
- Use snake_case identifiers like 'speaker_attribution_uncertain', 'be-ir_translation_crux'.

WHAT YOU DO NOT DO:

- Do not group verses (downstream pass)
- Do not designate anchors (downstream pass)
- Do not write group descriptions (downstream pass)
- Do not consolidate meanings across verses (downstream pass)
- Do not propose group structure (downstream pass)
- Do not draw conclusions about the broader word being studied (Session B work)

You see one verse and one term. Produce one meaning + N pointers. That is all."""


def build_user_message(verse_record: dict, term_strong: str,
                       term_extracts: dict) -> str:
    """Construct the per-call user message."""
    term_extract = term_extracts.get(term_strong, {})
    # Get the spans where this term appears in the verse
    spans_for_term = [
        s for s in verse_record.get("spans_decoded", [])
        if s["strong"] == term_strong
    ]
    return json.dumps({
        "task": "produce meaning + unresolved pointers per the system prompt",
        "verse": {
            "verse_record_id": verse_record["verse_record_id"],
            "reference": verse_record["reference"],
            "verse_text_english": verse_record["verse_text"],
            "all_spans": verse_record["spans_decoded"],
        },
        "term_being_analysed": {
            "strong": term_strong,
            "transliteration": term_extract.get("transliteration"),
            "gloss": term_extract.get("gloss"),
            "language": term_extract.get("language"),
            "owning_registry": term_extract.get("owning_registry"),
            "occurrences_in_this_verse": spans_for_term,
        },
        "term_full_extract": term_extract,
    }, indent=2, ensure_ascii=False)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def call_claude(client, verse_record, term_strong, term_extracts,
                model: str, effort: str = "high") -> dict:
    """One Claude invocation per (verse, term)."""
    user_msg = build_user_message(verse_record, term_strong, term_extracts)
    response = client.messages.create(
        model=model,
        max_tokens=4000,
        thinking={"type": "adaptive"},
        output_config={
            "effort": effort,
            "format": {"type": "json_schema", "schema": OUTPUT_SCHEMA},
        },
        system=[{
            "type": "text",
            "text": SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }],
        messages=[{"role": "user", "content": user_msg}],
    )
    # Extract text block
    text = next((b.text for b in response.content if b.type == "text"), "")
    parsed = json.loads(text) if text else {}
    return {
        "result": parsed,
        "usage": {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "cache_creation_input_tokens": getattr(
                response.usage, "cache_creation_input_tokens", 0),
            "cache_read_input_tokens": getattr(
                response.usage, "cache_read_input_tokens", 0),
        },
        "stop_reason": response.stop_reason,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default=INPUT_JSON,
                    help="verse-context-records JSON path")
    ap.add_argument("--limit-pairs", type=int, default=None,
                    help="Max (verse, term) pairs to process")
    ap.add_argument("--only-strongs", nargs="*",
                    help="Restrict to these Strong's numbers")
    ap.add_argument("--effort", default="high",
                    choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--model", default=DEFAULT_MODEL,
                    help="Model ID (e.g. claude-opus-4-7, claude-sonnet-4-6)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Show what would be called without making API calls")
    args = ap.parse_args()

    if not args.dry_run and not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set in environment or .env",
              file=sys.stderr)
        return 2

    with open(args.input, encoding="utf-8") as f:
        data = json.load(f)
    verses = data["verses"]
    term_extracts = data["term_extracts"]

    # Build (verse, term) pairs
    pairs = []
    for v in verses:
        if "error" in v:
            continue
        # Get unique Strong's referenced in this verse
        strongs_in_verse = sorted(set(s["strong"] for s in v.get("spans_decoded", [])))
        for s in strongs_in_verse:
            if args.only_strongs and s not in args.only_strongs:
                continue
            pairs.append((v, s))
    if args.limit_pairs:
        pairs = pairs[:args.limit_pairs]

    print(f"Processing {len(pairs)} (verse, term) pairs...")

    if args.dry_run:
        for v, s in pairs:
            tx = term_extracts.get(s, {})
            print(f"  {v['reference']:<14} {s:<10} '{(tx.get('gloss') or '')[:30]}'")
        return 0

    client = anthropic.Anthropic()
    results = []
    total_input = 0
    total_output = 0
    total_cache_read = 0
    total_cache_create = 0

    for i, (v, s) in enumerate(pairs, 1):
        tx = term_extracts.get(s, {})
        print(f"  [{i}/{len(pairs)}] {v['reference']:<14} {s:<10} "
              f"'{(tx.get('gloss') or '')[:30]:<30}' ", end="", flush=True)
        try:
            res = call_claude(client, v, s, term_extracts,
                              model=args.model, effort=args.effort)
            results.append({
                "verse_record_id": v["verse_record_id"],
                "reference": v["reference"],
                "strong": s,
                "term_summary": {
                    "transliteration": tx.get("transliteration"),
                    "gloss": tx.get("gloss"),
                    "language": tx.get("language"),
                    "owning_registry": tx.get("owning_registry"),
                },
                **res["result"],
                "_usage": res["usage"],
                "_stop_reason": res["stop_reason"],
            })
            u = res["usage"]
            total_input += u["input_tokens"]
            total_output += u["output_tokens"]
            total_cache_read += u["cache_read_input_tokens"]
            total_cache_create += u["cache_creation_input_tokens"]
            n_pointers = len(res["result"].get("unresolved_pointers", []))
            print(f"in={u['input_tokens']} out={u['output_tokens']} "
                  f"cache_r={u['cache_read_input_tokens']} ptr={n_pointers}")
        except Exception as e:
            print(f"ERROR: {e}")
            results.append({
                "verse_record_id": v["verse_record_id"],
                "reference": v["reference"],
                "strong": s,
                "error": str(e),
            })

    # Cost estimate per the model's pricing tier
    p_in, p_out, p_cc, p_cr = PRICING.get(args.model, PRICING[DEFAULT_MODEL])
    cost = (total_input / 1_000_000 * p_in
            + total_output / 1_000_000 * p_out
            + total_cache_create / 1_000_000 * p_cc
            + total_cache_read / 1_000_000 * p_cr)

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "model": args.model,
            "effort": args.effort,
            "n_pairs": len(pairs),
            "n_results": len(results),
            "total_input_tokens": total_input,
            "total_output_tokens": total_output,
            "total_cache_read_tokens": total_cache_read,
            "total_cache_create_tokens": total_cache_create,
            "estimated_cost_usd": round(cost, 4),
        },
        "results": results,
    }

    # Tag output filenames with model + label so re-runs don't overwrite
    model_tag = args.model.replace("claude-", "")
    out_json = os.path.join(OUT_DIR,
        f"verse-meaning-router-results-{model_tag}-{today_compact()}.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    # Markdown summary
    out_md = os.path.join(OUT_DIR,
        f"verse-meaning-router-results-{model_tag}-{today_compact()}.md")
    L = []
    L.append("# Verse Meaning Router — Results")
    L.append("")
    L.append(f"_Generated {now_iso()}_  ·  model: `{args.model}`  ·  effort: `{args.effort}`")
    L.append("")
    L.append(f"**Pairs processed:** {len(pairs)}  ·  "
             f"**Estimated cost:** ${cost:.4f}  ·  "
             f"**Cache hit:** {total_cache_read} read / {total_cache_create} created tokens")
    L.append("")
    for r in results:
        if "error" in r:
            L.append(f"## {r['reference']} — `{r['strong']}` — ERROR")
            L.append("")
            L.append(f"`{r['error']}`")
            L.append("")
            continue
        L.append(f"## {r['reference']} — `{r['strong']}` "
                 f"({r['term_summary'].get('transliteration') or ''}) "
                 f"\"{r['term_summary'].get('gloss') or ''}\"")
        L.append("")
        L.append(f"_Owning registry: {r['term_summary'].get('owning_registry') or '(none)'}_")
        L.append("")
        L.append("**Meaning:**")
        L.append("")
        L.append("> " + (r.get("meaning") or "").replace("\n", "\n> "))
        L.append("")
        ptrs = r.get("unresolved_pointers", [])
        if ptrs:
            L.append(f"**Unresolved pointers ({len(ptrs)}):**")
            L.append("")
            for p in ptrs:
                L.append(f"- **{p['pointer']}** — {p['description']}")
        else:
            L.append("**Unresolved pointers:** none — verse fully resolved by reading.")
        L.append("")
        L.append(f"_tokens in/out: {r['_usage']['input_tokens']}/{r['_usage']['output_tokens']} · "
                 f"cache read: {r['_usage']['cache_read_input_tokens']}_")
        L.append("")
        L.append("---")
        L.append("")
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    print()
    print(f"Wrote: {out_json}")
    print(f"Wrote: {out_md}")
    print(f"Total tokens: {total_input} in, {total_output} out, "
          f"{total_cache_read} cache read, {total_cache_create} cache created")
    print(f"Estimated cost: ${cost:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
