"""_exploratory_thin_verse_router_v1_20260504.py — read-only.

Thinnest router. One call per verse, one plain-English summary per verse.
No per-term decisions, no set-aside enum, no taxonomy. Just: read the
verse, write what it says (≤25 words).

Inputs:
  --input   path to unclassified-verse-sample-{N}-verses-{date}.json
  --model   default: claude-sonnet-4-6
  --effort  default: medium
  --limit   stop after N verses
  --dry-run skip API; emit prompt previews

Outputs:
  thin-verse-router-results-{model}-{date}.json
  thin-verse-router-results-{model}-{date}.md
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


SYSTEM_PROMPT = """You are a Bible-verse classifier for the Soul Word Analysis Programme — a research project studying ~214 English words for the inner life of mankind, each mapped to Hebrew (OT) and Greek (NT) terms via Strong's numbers.

Each call gives you ONE verse with all its spans and a list of programme-relevant terms occurring in that verse (`terms_present`). Your job is one of two things:

(A) SUMMARY — if at least one term in `terms_present` engages inner-being content, WRITE ONE SHORT PLAIN-ENGLISH SENTENCE (≤25 words) of what the verse says, naming whichever terms in `terms_present` actually contribute to that meaning.

If multiple terms contribute, name them together in the same sentence:
  - "Thanksgiving and praise were established in Israel's worship from David's day."
  - "A husband's silence after hearing his wife's vows ratifies them through inaction."

If a term is incidental (body part in passing, geography, material object), do not need to name it — the natural-language summary IS the routing signal.

(B) SET ASIDE — if NONE of the terms in `terms_present` engage inner-being content (the verse is wholly narrative/material/geographic with no inner-life window), mark `set_aside=true` with one reason:
  - `no_inner_being` — external conduct/event/narrative, no inner-life window
  - `physical_only` — body parts, physical process, material objects dominate
  - `spatial_only` — location/geography dominates
  - `unclear` — verse needs deeper analysis to decide

Filter test (per term, but verse-level outcome): does this verse, through any of the listed terms, say something about how a person thinks, feels, chooses, relates, or is oriented toward meaning, others, or God? If yes for at least one term → summary. If no for all terms → set aside.

Discipline:
- ≤25 words for summaries. One sentence.
- Concrete, plain English. No theology essay, no morphology, no parallels.
- Treat each verse atomically. Do not consolidate phrasing across calls.
- When set aside, summary is null.

Output JSON — exactly:
{
  "reference": "<copied from input>",
  "summary": "<≤25 words plain English, OR null if set_aside=true>",
  "set_aside": <true|false>,
  "set_aside_reason": "<one of the categories above, OR null if set_aside=false>"
}

Return ONLY the JSON. No prose around it.
"""


OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "reference": {"type": "string"},
        "summary": {"type": ["string", "null"]},
        "set_aside": {"type": "boolean"},
        "set_aside_reason": {"type": ["string", "null"]},
    },
    "required": ["reference", "summary", "set_aside", "set_aside_reason"],
    "additionalProperties": False,
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def build_user_msg(verse_record, term_extracts):
    spans_brief = []
    for sp in verse_record.get("all_spans", []):
        spans_brief.append({
            "strong": sp["strong"],
            "original": sp["original_text"],
            "pos": sp["morph_decoded"]["pos"],
            "gloss": sp["gloss"],
            "registry": sp.get("owning_registry"),
        })
    terms_present = []
    for t in verse_record["terms_to_classify"]:
        ext = term_extracts.get(t["strong"]) or {}
        terms_present.append({
            "strong": t["strong"],
            "owning_registry": t["owning_registry"],
            "transliteration": ext.get("transliteration"),
            "gloss": ext.get("gloss"),
            "language": ext.get("language"),
            "step_search_gloss": ext.get("step_search_gloss"),
            "short_def_mounce": ext.get("short_def_mounce"),
        })
    pkg = {
        "reference": verse_record["reference"],
        "verse_text": verse_record["verse_text"],
        "all_spans_in_verse": spans_brief,
        "terms_present": terms_present,
    }
    return (
        f"Summarise this verse:\n\n"
        f"```json\n{json.dumps(pkg, ensure_ascii=False, indent=2)}\n```\n\n"
        f"Return the JSON in the schema above."
    )


def call_claude(client, verse_record, term_extracts, model, effort):
    user_msg = build_user_msg(verse_record, term_extracts)
    response = client.messages.create(
        model=model,
        max_tokens=400,
        thinking={"type": "adaptive"},
        output_config={
            "effort": effort,
            "format": {"type": "json_schema", "schema": OUTPUT_SCHEMA},
        },
        system=[
            {"type": "text", "text": SYSTEM_PROMPT,
             "cache_control": {"type": "ephemeral"}},
        ],
        messages=[{"role": "user", "content": user_msg}],
    )
    text_blocks = [b.text for b in response.content if hasattr(b, "text") and b.text]
    raw = "".join(text_blocks).strip()
    parsed = json.loads(raw)
    return parsed, response


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--model", default="claude-sonnet-4-6")
    ap.add_argument("--effort", default="medium")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--out-prefix", default=None)
    args = ap.parse_args()

    if not args.dry_run and not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set in environment.", file=sys.stderr)
        return 2

    with open(args.input, encoding="utf-8") as f:
        payload = json.load(f)

    verses = payload["verses"]
    term_extracts = payload["term_extracts"]
    if args.limit:
        verses = verses[:args.limit]

    prefix = args.out_prefix or os.path.join(
        "outputs", "markdown",
        f"thin-verse-router-results-{args.model}-{today_compact()}"
    )
    out_json = prefix + ".json"
    out_md = prefix + ".md"

    if args.dry_run:
        sample = build_user_msg(verses[0], term_extracts)
        print("=== DRY-RUN: SYSTEM PROMPT ===")
        print(SYSTEM_PROMPT)
        print("\n=== DRY-RUN: SAMPLE USER MSG (verse 1) ===")
        print(sample[:3000])
        print(f"\nWould process {len(verses)} verses against {args.model} (effort={args.effort}).")
        return 0

    from anthropic import Anthropic
    client = Anthropic()

    results = []
    in_tot = out_tot = cache_r_tot = 0
    print(f"Processing {len(verses)} verses against {args.model} (effort={args.effort})...")
    for i, vr in enumerate(verses, 1):
        try:
            parsed, resp = call_claude(client, vr, term_extracts, args.model, args.effort)
        except Exception as e:
            print(f"  [{i}/{len(verses)}] {vr['reference']:<14} ERROR {e}")
            results.append({"reference": vr["reference"], "error": f"{type(e).__name__}: {e}"})
            continue
        usage = resp.usage
        in_tot += usage.input_tokens
        out_tot += usage.output_tokens
        cache_r_tot += getattr(usage, "cache_read_input_tokens", 0) or 0
        n_terms = len(vr["terms_to_classify"])
        decision = "set_aside" if parsed.get("set_aside") else "summary"
        results.append({
            "reference": vr["reference"],
            "n_terms_present": n_terms,
            "terms_present": [t["strong"] for t in vr["terms_to_classify"]],
            "summary": parsed.get("summary"),
            "set_aside": parsed.get("set_aside", False),
            "set_aside_reason": parsed.get("set_aside_reason"),
            "decision": decision,
            "usage": {
                "input_tokens": usage.input_tokens,
                "output_tokens": usage.output_tokens,
                "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", 0) or 0,
            },
        })
        print(f"  [{i}/{len(verses)}] {vr['reference']:<14} terms={n_terms:<2} "
              f"{decision:<10} in={usage.input_tokens} out={usage.output_tokens} "
              f"cache_r={getattr(usage, 'cache_read_input_tokens', 0) or 0}")

    if "opus" in args.model:
        in_price, out_price = 5.0, 25.0
    elif "haiku" in args.model:
        in_price, out_price = 1.0, 5.0
    else:
        in_price, out_price = 3.0, 15.0
    cost = (in_tot / 1_000_000) * in_price + (out_tot / 1_000_000) * out_price

    out_payload = {
        "meta": {
            "generated_at": now_iso(),
            "model": args.model,
            "effort": args.effort,
            "input_file": args.input,
            "n_verses": len(results),
            "n_summary": sum(1 for r in results if r.get("decision") == "summary"),
            "n_set_aside": sum(1 for r in results if r.get("decision") == "set_aside"),
            "n_error": sum(1 for r in results if "error" in r),
            "tokens": {
                "input": in_tot, "output": out_tot,
                "cache_read": cache_r_tot,
                "estimated_cost_usd": round(cost, 4),
            },
        },
        "results": results,
    }

    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(out_payload, f, indent=2, ensure_ascii=False)

    md_lines = [
        f"# Thin verse router results — {args.model}",
        "",
        f"**Generated:** {out_payload['meta']['generated_at']}",
        f"**Model:** {args.model} (effort={args.effort})",
        f"**Input:** `{args.input}`",
        f"**Verses:** {out_payload['meta']['n_verses']} "
        f"(summary={out_payload['meta']['n_summary']} · "
        f"set_aside={out_payload['meta']['n_set_aside']} · "
        f"error={out_payload['meta']['n_error']})",
        f"**Tokens:** in={in_tot}, out={out_tot}, cache_read={cache_r_tot}",
        f"**Estimated cost:** ${cost:.4f}",
        "",
        "---",
        "",
        "| # | reference | terms_present | decision | summary / reason |",
        "|---|---|---|---|---|",
    ]
    for i, r in enumerate(results, 1):
        if "error" in r:
            md_lines.append(f"| {i} | {r['reference']} | — | ERROR | {r['error']} |")
            continue
        terms_cell = ", ".join(r["terms_present"])
        if r.get("set_aside"):
            cell = f"**{r.get('set_aside_reason') or 'unclear'}**"
        else:
            cell = (r.get("summary") or "").replace("|", "\\|").replace("\n", " ")
        md_lines.append(
            f"| {i} | {r['reference']} | {terms_cell} | {r.get('decision', '?')} | {cell} |"
        )

    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines) + "\n")

    print(f"\nWrote: {out_json}")
    print(f"Wrote: {out_md}")
    print(f"Total tokens: {in_tot} in, {out_tot} out, {cache_r_tot} cache read")
    print(f"Estimated cost: ${cost:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
