"""_exploratory_brief_meaning_router_v1_20260504.py — read-only.

Stripped-down meaning router. Per (verse, term) pair, asks the model:
  a) one-sentence plain-English statement of what THIS verse says about
     the inner being via THIS term, OR
  b) set-aside (term doesn't engage the inner being, or the verse is
     unclear and needs deeper analysis).

No morphology essay, no §3 framing, no unresolved pointers — just the
brief summary needed to group verses with similar meaning.

Inputs:
  --input   path to unclassified-sample-{N}-pairs-{date}.json
  --model   default: claude-sonnet-4-6
  --effort  default: medium
  --limit   stop after N pairs (for cheap test run)
  --dry-run skip API; emit prompt previews only

Outputs:
  brief-meaning-router-results-{model}-{date}.json
  brief-meaning-router-results-{model}-{date}.md
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

Your job for each (verse, term) pair is ONE of two things:

(A) BRIEF SUMMARY — one short plain-English sentence (≤25 words) saying what THIS verse says about the inner-being characteristic via THIS term. Concrete, not abstract. Just the sense of the verse on this term — not a theology essay.

(B) SET ASIDE — if the term in this verse does NOT engage inner-being content, or the verse is genuinely unclear, mark it set_aside=true with one of these reasons:
  - "no_inner_being" — the term here is about external conduct/event with no inner-life window
  - "physical_only" — body part, physical process, material object
  - "spatial_only" — location/geography
  - "wrong_face" — verse has inner-being content but a different term carries it (name the carrier in the note)
  - "unclear" — needs deeper analysis to decide

The point of this pass is to GROUP verses with similar meaning. Brief and consistent matters more than exhaustive. Do NOT analyse morphology, do NOT cite parallels, do NOT speculate. If you can read the verse and see the gist, write it. If not, set aside.

Filter test: does this verse, through this term, say something about how a person thinks, feels, chooses, relates, or is oriented toward meaning, others, or God? If yes, summarise. If no or unclear, set aside.

Output JSON shape — exactly:
{
  "summary": "<≤25 words plain English, OR null if set_aside=true>",
  "set_aside": <true|false>,
  "set_aside_reason": "<one of the categories above, OR null if set_aside=false>",
  "note": "<optional one-line note, or null>"
}
"""


OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {"type": ["string", "null"]},
        "set_aside": {"type": "boolean"},
        "set_aside_reason": {"type": ["string", "null"]},
        "note": {"type": ["string", "null"]},
    },
    "required": ["summary", "set_aside", "set_aside_reason", "note"],
    "additionalProperties": False,
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def build_user_msg(verse_record: dict, term_extract: dict) -> str:
    spans_brief = []
    for sp in verse_record.get("spans_decoded", []):
        spans_brief.append({
            "strong": sp["strong"],
            "original": sp["original_text"],
            "pos": sp["morph_decoded"]["pos"],
            "gloss": sp["gloss"],
            "registry": sp.get("owning_registry"),
        })
    pkg = {
        "reference": verse_record["reference"],
        "verse_text": verse_record["verse_text"],
        "term_being_analysed": {
            "strong": term_extract["strong"],
            "transliteration": term_extract["transliteration"],
            "gloss": term_extract["gloss"],
            "language": term_extract["language"],
            "owning_registry": term_extract.get("owning_registry"),
            "step_search_gloss": term_extract.get("step_search_gloss"),
            "short_def_mounce": term_extract.get("short_def_mounce"),
            "meaning_excerpt": (term_extract.get("meaning") or "")[:600],
        },
        "all_spans_in_verse": spans_brief,
    }
    return (
        f"(verse, term) pair to classify:\n\n"
        f"```json\n{json.dumps(pkg, ensure_ascii=False, indent=2)}\n```\n\n"
        f"Return the JSON in the schema above. No prose outside the JSON."
    )


def call_claude(client, verse_record, term_extract, model, effort):
    user_msg = build_user_msg(verse_record, term_extract)
    response = client.messages.create(
        model=model,
        max_tokens=800,
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
        f"brief-meaning-router-results-{args.model}-{today_compact()}"
    )
    out_json = prefix + ".json"
    out_md = prefix + ".md"

    if args.dry_run:
        sample = build_user_msg(verses[0], term_extracts[verses[0]["strong_being_analysed"]])
        print("=== DRY-RUN: SYSTEM PROMPT ===")
        print(SYSTEM_PROMPT)
        print("\n=== DRY-RUN: SAMPLE USER MSG (verse 1) ===")
        print(sample[:3000])
        print(f"\nWould process {len(verses)} pairs against {args.model} (effort={args.effort}).")
        return 0

    from anthropic import Anthropic
    client = Anthropic()

    results = []
    in_tot = out_tot = cache_r_tot = 0
    print(f"Processing {len(verses)} (verse, term) pairs against {args.model} (effort={args.effort})...")
    for i, vr in enumerate(verses, 1):
        strong = vr["strong_being_analysed"]
        term_ext = term_extracts.get(strong)
        if not term_ext:
            results.append({
                "verse_record_id": vr["verse_record_id"],
                "reference": vr["reference"],
                "strong": strong,
                "error": "term_extract_missing",
            })
            continue
        try:
            parsed, resp = call_claude(client, vr, term_ext, args.model, args.effort)
        except Exception as e:
            results.append({
                "verse_record_id": vr["verse_record_id"],
                "reference": vr["reference"],
                "strong": strong,
                "error": f"{type(e).__name__}: {e}",
            })
            print(f"  [{i}/{len(verses)}] {vr['reference']:<14} {strong:<10} ERROR {e}")
            continue
        usage = resp.usage
        in_tot += usage.input_tokens
        out_tot += usage.output_tokens
        cache_r_tot += getattr(usage, "cache_read_input_tokens", 0) or 0
        decision = "set_aside" if parsed["set_aside"] else "summary"
        results.append({
            "verse_record_id": vr["verse_record_id"],
            "mti_term_id": vr["mti_term_id"],
            "reference": vr["reference"],
            "strong": strong,
            "decision": decision,
            "summary": parsed["summary"],
            "set_aside": parsed["set_aside"],
            "set_aside_reason": parsed["set_aside_reason"],
            "note": parsed.get("note"),
            "usage": {
                "input_tokens": usage.input_tokens,
                "output_tokens": usage.output_tokens,
                "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", 0) or 0,
            },
        })
        print(f"  [{i}/{len(verses)}] {vr['reference']:<14} {strong:<10} "
              f"{decision:<10} in={usage.input_tokens} out={usage.output_tokens} "
              f"cache_r={getattr(usage, 'cache_read_input_tokens', 0) or 0}")

    # Pricing per 1M (Sonnet 4.6 = $3 in, $15 out; Opus 4.7 = $5 in, $25 out)
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
            "n_pairs": len(results),
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
        f"# Brief meaning router results — {args.model}",
        "",
        f"**Generated:** {out_payload['meta']['generated_at']}",
        f"**Model:** {args.model} (effort={args.effort})",
        f"**Input:** `{args.input}`",
        f"**Pairs processed:** {len(results)} "
        f"(summary={out_payload['meta']['n_summary']} · "
        f"set_aside={out_payload['meta']['n_set_aside']} · "
        f"error={out_payload['meta']['n_error']})",
        f"**Tokens:** in={in_tot}, out={out_tot}, cache_read={cache_r_tot}",
        f"**Estimated cost:** ${cost:.4f}",
        "",
        "---",
        "",
        "| # | reference | strong | decision | summary / reason |",
        "|---|---|---|---|---|",
    ]
    for i, r in enumerate(results, 1):
        if "error" in r:
            md_lines.append(
                f"| {i} | {r['reference']} | {r['strong']} | ERROR | {r['error']} |"
            )
            continue
        cell = (r["summary"] or "").replace("|", "\\|").replace("\n", " ")
        if r["set_aside"]:
            note = (r.get("note") or "").replace("|", "\\|").replace("\n", " ")
            cell = f"**{r['set_aside_reason']}** — {note}" if note else f"**{r['set_aside_reason']}**"
        md_lines.append(
            f"| {i} | {r['reference']} | {r['strong']} | {r['decision']} | {cell} |"
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
