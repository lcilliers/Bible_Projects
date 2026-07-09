"""_apply_m26_phase3_debate_v1_20260509.py — Claude API + DB read.

Phase 3 (Characteristic debate from the gloss list) automation
prototype for M26 cluster.

Per wa-sessionb-cluster-instruction-v1_1-20260507 §6: subdivide the
cluster's terms into provisional sub-groups based on distinct
characteristics. Read all glosses against the T1 framework and propose
groupings — characteristic-bearing, supportive/BOUNDARY, or flagged
for researcher review.

Architecture (single API call for the whole cluster):
  - System prompt: cluster context + T1 characteristic definition +
    onion-principle reminder + provisional-by-definition guard +
    JSON output schema
  - User message: all 39 M26 terms with gloss, transliteration,
    language, mounce, meaning excerpt
  - Output: structured JSON with proposed sub-groups + assigned terms
    + rationale per sub-group + boundary set + flagged terms

Outputs:
  1. Raw API result JSON
       outputs/markdown/m26-phase3-debate-results-{model}-{date}.json
  2. Characteristic-debate document (markdown, per Phase 3 §6 spec)
       Sessions/Session_Clusters/M26/files phase 3/
       WA-M26-characteristic-debate-v1-{date}.md

DB writes: NONE. Phase 3 output is a hypothesis; Phase 4 control read
confirms. The instruction is explicit: "Phase 3 output is hypothesis,
not a finding" (§6 Provisional-by-definition guard).
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone

try:
    from dotenv import load_dotenv
    load_dotenv(".env")
except ImportError:
    pass

DB_PATH = os.path.join("database", "bible_research.db")
CLUSTER_CODE = "M26"
CLUSTER_DESC = "Righteousness and Justice"

OUT_DIR_PHASE3 = os.path.join(
    "Sessions", "Session_Clusters", "M26", "files phase 3"
)
OUT_DIR_RESULTS = os.path.join("outputs", "markdown")


SYSTEM_PROMPT = f"""You are an analyst on the Soul Word Analysis Programme — a research project studying ~214 English words for the inner life of mankind, each mapped to Hebrew (OT) and Greek (NT) terms via Strong's numbers.

You are working on Phase 3 (characteristic debate) of cluster **M26 — {CLUSTER_DESC}**.

# T1 Characteristic framework

A distinct inner-being characteristic, by the programme's working definition:
1. Has an identifiable constitutional location (mind / heart / soul / spirit / faculty named in the verse evidence).
2. Engages a distinguishable set of inner faculties (cognitive, volitional, affective, perceptive, judicial).
3. Produces recognisable impact (on the inner being, on conduct, on relationships).
4. Has a structural opposite (and the opposite shows up in the cluster's vocabulary or its near neighbours).
5. Can be distinguished by causal direction (originating in the person, in God, in covenant condition) or directional object (toward whom or what is the characteristic directed).

# The onion principle

The inner being is not made of separable bricks neatly assignable to sub-groups. It is made of compounds that morph and change character through the person's inner life. Each analytical layer peels without discarding the whole. **Sub-groupings are peels, not divisions.** A term may carry more than one inner-being phenomenon; the analysis names the dominant characteristic each term primarily bears, while acknowledging overlap.

# Provisional-by-definition

This Phase 3 output is a hypothesis, not a finding. Grouping from glosses alone is inherently incomplete — glosses are compressed labels, not readings of the verses themselves. The control read in Phase 4 exists precisely because Phase 3 groupings will need revision. Do not over-commit to the structure you propose; lean toward making it readable, navigable, and easy for a human to test against.

# Your task

You will receive all 39 M26 terms with: Strong's number, transliteration, language, gloss, Mounce short-def (NT), meaning excerpt (where present).

Propose provisional sub-groups. For each term, place it in exactly one of:

(A) A **characteristic-bearing sub-group** — assigned a sub-group code (M26-A, M26-B, …) named by the dominant characteristic the sub-group's terms collectively carry. Each sub-group should have a clear T1-grade characteristic definition: location + faculty + opposite + direction.

(B) The **BOUNDARY** sub-group — supportive / descriptive / qualifying terms that enhance or describe the cluster's characteristics without themselves being inner-being characteristics. Functional roles (causer, accuser, judge as office), legal-procedure terms used outside an inner state, or NT compound qualifiers may sit here.

(C) **Flagged** — terms that may not belong in M26 at all, or whose evidence is insufficient from the gloss alone, or whose placement is genuinely ambiguous between two sub-groups. Flagged terms surface for researcher decision; provide a clear `issue` description and `proposed_action`.

# Sub-group naming and discipline

- Use codes M26-A, M26-B, ... in alphabetical order; A is the most central / definitional sub-group, B-G follow in decreasing centrality.
- Each sub-group's `label` is short (≤8 words). The full T1-shaped definition goes in `characteristic_definition`.
- Each sub-group must have ≥2 terms. If you can only fit one term in a proposed group, either fold it into a related group, move it to BOUNDARY, or flag it.
- Aim for 4–7 substantive sub-groups for M26. Fewer if the evidence collapses; more only if the cluster genuinely has more distinct characteristics.
- For each term assignment, include a one-sentence rationale grounding the placement in the gloss / Mounce / meaning excerpt — not in general theological knowledge.

# Output JSON shape — exactly

{{
  "cluster_overview": "<2-3 sentences orienting the reader to the cluster's analytical shape — what the terms collectively suggest about the inner-being characteristic(s) M26 names>",
  "onion_observation": "<1-2 sentences naming the most prominent overlaps / morphings between the proposed sub-groups — e.g. terms that bridge two sub-groups>",
  "subgroups": [
    {{
      "code": "M26-A",
      "label": "<≤8 words>",
      "characteristic_definition": "<T1-shaped: location, faculty, opposite, direction; 2-4 sentences>",
      "rationale": "<2-3 sentences explaining why these terms cluster here>",
      "terms": [
        {{
          "strong": "<copied>",
          "transliteration": "<copied>",
          "rationale": "<1 sentence grounded in gloss / mounce / meaning>"
        }}
      ]
    }}
  ],
  "boundary": {{
    "rationale": "<1-2 sentences on what role these terms play>",
    "terms": [
      {{ "strong": "...", "transliteration": "...", "rationale": "..." }}
    ]
  }},
  "flagged": [
    {{
      "strong": "...",
      "transliteration": "...",
      "issue": "<what's ambiguous>",
      "proposed_action": "<keep_pending_phase4 | researcher_review | propose_cluster_reassignment_to_<MXX>>"
    }}
  ]
}}

Every term in the input must appear exactly once across `subgroups[*].terms`, `boundary.terms`, or `flagged`. Do not omit any term. Do not duplicate any term.
"""


OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "cluster_overview": {"type": "string"},
        "onion_observation": {"type": "string"},
        "subgroups": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "code": {"type": "string"},
                    "label": {"type": "string"},
                    "characteristic_definition": {"type": "string"},
                    "rationale": {"type": "string"},
                    "terms": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "strong": {"type": "string"},
                                "transliteration": {"type": "string"},
                                "rationale": {"type": "string"},
                            },
                            "required": ["strong", "transliteration", "rationale"],
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["code", "label", "characteristic_definition",
                             "rationale", "terms"],
                "additionalProperties": False,
            },
        },
        "boundary": {
            "type": "object",
            "properties": {
                "rationale": {"type": "string"},
                "terms": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "strong": {"type": "string"},
                            "transliteration": {"type": "string"},
                            "rationale": {"type": "string"},
                        },
                        "required": ["strong", "transliteration", "rationale"],
                        "additionalProperties": False,
                    },
                },
            },
            "required": ["rationale", "terms"],
            "additionalProperties": False,
        },
        "flagged": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "strong": {"type": "string"},
                    "transliteration": {"type": "string"},
                    "issue": {"type": "string"},
                    "proposed_action": {"type": "string"},
                },
                "required": ["strong", "transliteration", "issue",
                             "proposed_action"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["cluster_overview", "onion_observation", "subgroups",
                 "boundary", "flagged"],
    "additionalProperties": False,
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def fetch_terms(conn) -> list[dict]:
    rows = list(conn.execute("""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration,
               mt.gloss, mt.language,
               ti.short_def_mounce, ti.step_search_gloss,
               ti.meaning, ti.lsj_entry, ti.testament,
               ti.occurrence_count
          FROM mti_terms mt
          LEFT JOIN wa_term_inventory ti
                 ON ti.strongs_number=mt.strongs_number
                AND COALESCE(ti.delete_flagged,0)=0
                AND COALESCE(ti.term_owner_type,'OWNER')='OWNER'
         WHERE mt.cluster_code=?
           AND COALESCE(mt.delete_flagged,0)=0
         ORDER BY mt.language, mt.strongs_number
    """, (CLUSTER_CODE,)))
    return [dict(r) for r in rows]


def build_user_msg(terms: list[dict]) -> str:
    pkg = []
    for t in terms:
        item = {
            "mti_term_id": t["mti_id"],
            "strong": t["strongs_number"],
            "transliteration": t["transliteration"],
            "language": t["language"],
            "testament": t["testament"],
            "gloss": t["gloss"],
            "step_search_gloss": t["step_search_gloss"],
            "occurrence_count": t["occurrence_count"],
        }
        if t["short_def_mounce"]:
            item["short_def_mounce"] = t["short_def_mounce"]
        if t["meaning"]:
            item["meaning_excerpt"] = (t["meaning"] or "")[:500]
        if t["lsj_entry"] and t["language"] == "Greek":
            item["lsj_excerpt"] = (t["lsj_entry"] or "")[:300]
        pkg.append(item)
    return (
        f"Cluster: M26 — {CLUSTER_DESC}\n\n"
        f"All {len(terms)} terms in M26:\n\n"
        f"```json\n{json.dumps(pkg, ensure_ascii=False, indent=2)}\n```\n\n"
        "Return the JSON in the schema above. Every term must appear "
        "exactly once across `subgroups[*].terms`, `boundary.terms`, "
        "or `flagged`."
    )


def call_claude(client, terms, model: str, effort: str):
    user_msg = build_user_msg(terms)
    # Streaming required for max_tokens above ~16k (SDK 10-min non-stream cap)
    text_parts = []
    response = None
    with client.messages.stream(
        model=model,
        max_tokens=24000,
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
    ) as stream:
        for text in stream.text_stream:
            text_parts.append(text)
        response = stream.get_final_message()
    raw = "".join(text_parts).strip()
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as e:
        # Dump truncated output for diagnosis
        dump_path = os.path.join(
            OUT_DIR_RESULTS,
            f"m26-phase3-debate-truncated-{today_compact()}.txt"
        )
        with open(dump_path, "w", encoding="utf-8") as f:
            f.write(raw)
        raise RuntimeError(
            f"JSON decode failed: {e}. Stop reason: "
            f"{getattr(response, 'stop_reason', '?')}. "
            f"Raw output dumped to {dump_path} ({len(raw)} chars)."
        ) from e
    return parsed, response


def write_debate_doc(parsed: dict, terms: list[dict], out_path: str):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    today_compact = today.replace("-", "")
    by_strong = {t["strongs_number"]: t for t in terms}

    lines = []
    lines.append(f"# WA-M26-characteristic-debate-v1-{today_compact}")
    lines.append("")
    lines.append("> Framework B Soul Word Analysis Programme — Session B Phase 3 (Characteristic debate)")
    lines.append(f"> Cluster: M26 — {CLUSTER_DESC}")
    lines.append(f"> Date: {today}")
    lines.append(f"> Method: Claude API single-call provisional sub-group proposal (sonnet-4-6 + structured JSON output)")
    lines.append("> **Status: PROVISIONAL** — Phase 3 output is a hypothesis. Phase 4 control read against full meaning text confirms or revises.")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## Cluster overview")
    lines.append("")
    lines.append(parsed["cluster_overview"])
    lines.append("")
    lines.append("**Onion observation:** " + parsed["onion_observation"])
    lines.append("")
    lines.append("---")
    lines.append("")

    # Summary table
    n_sub_terms = sum(len(sg["terms"]) for sg in parsed["subgroups"])
    n_boundary = len(parsed["boundary"]["terms"])
    n_flagged = len(parsed["flagged"])
    lines.append("## Summary")
    lines.append("")
    lines.append("| Sub-group | Label | Term count |")
    lines.append("|---|---|---:|")
    for sg in parsed["subgroups"]:
        lines.append(f"| **{sg['code']}** | {sg['label']} | {len(sg['terms'])} |")
    lines.append(f"| **BOUNDARY** | Supportive / qualifying | {n_boundary} |")
    if n_flagged:
        lines.append(f"| **FLAGGED** | Researcher review required | {n_flagged} |")
    total = n_sub_terms + n_boundary + n_flagged
    lines.append(f"| **Total** | | **{total}** |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per-subgroup detail
    for sg in parsed["subgroups"]:
        lines.append(f"## {sg['code']} — {sg['label']}")
        lines.append("")
        lines.append("**Characteristic definition (T1-shaped):**")
        lines.append("")
        lines.append(sg["characteristic_definition"])
        lines.append("")
        lines.append("**Rationale for grouping:**")
        lines.append("")
        lines.append(sg["rationale"])
        lines.append("")
        lines.append(f"**Terms ({len(sg['terms'])}):**")
        lines.append("")
        lines.append("| Strong's | Translit | Gloss | Rationale |")
        lines.append("|---|---|---|---|")
        for t in sg["terms"]:
            src = by_strong.get(t["strong"], {})
            gloss = (src.get("gloss") or "").replace("|", "\\|")
            lines.append(
                f"| {t['strong']} | *{t['transliteration']}* | {gloss} "
                f"| {t['rationale'].replace('|', chr(92) + '|')} |"
            )
        lines.append("")

    # BOUNDARY
    lines.append("## BOUNDARY — supportive / qualifying terms")
    lines.append("")
    lines.append(parsed["boundary"]["rationale"])
    lines.append("")
    lines.append(f"**Terms ({n_boundary}):**")
    lines.append("")
    lines.append("| Strong's | Translit | Gloss | Rationale |")
    lines.append("|---|---|---|---|")
    for t in parsed["boundary"]["terms"]:
        src = by_strong.get(t["strong"], {})
        gloss = (src.get("gloss") or "").replace("|", "\\|")
        lines.append(
            f"| {t['strong']} | *{t['transliteration']}* | {gloss} "
            f"| {t['rationale'].replace('|', chr(92) + '|')} |"
        )
    lines.append("")

    # FLAGGED
    if n_flagged:
        lines.append("## FLAGGED — researcher review required")
        lines.append("")
        lines.append("| Strong's | Translit | Gloss | Issue | Proposed action |")
        lines.append("|---|---|---|---|---|")
        for t in parsed["flagged"]:
            src = by_strong.get(t["strong"], {})
            gloss = (src.get("gloss") or "").replace("|", "\\|")
            issue = t["issue"].replace("|", "\\|")
            action = t["proposed_action"].replace("|", "\\|")
            lines.append(
                f"| {t['strong']} | *{t['transliteration']}* | {gloss} "
                f"| {issue} | `{action}` |"
            )
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Coverage check")
    lines.append("")
    declared = set()
    for sg in parsed["subgroups"]:
        for t in sg["terms"]:
            declared.add(t["strong"])
    for t in parsed["boundary"]["terms"]:
        declared.add(t["strong"])
    for t in parsed["flagged"]:
        declared.add(t["strong"])
    expected = {t["strongs_number"] for t in terms}
    missing = expected - declared
    extra = declared - expected
    lines.append(f"- Terms expected: **{len(expected)}**")
    lines.append(f"- Terms placed (sub-group + BOUNDARY + FLAGGED): **{len(declared)}**")
    if missing:
        lines.append(f"- ⚠ Missing (not placed): {sorted(missing)}")
    if extra:
        lines.append(f"- ⚠ Extra (not in cluster): {sorted(extra)}")
    if not missing and not extra:
        lines.append("- ✓ Every cluster term is placed exactly once")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"*WA-M26-characteristic-debate-v1-{today_compact} — "
                 f"Phase 3 provisional sub-group proposal via Claude API*")
    lines.append("")
    lines.append("**Next step:** Phase 4 control read against full meaning text; produce sub-group-assignment directive after open questions resolved.")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="claude-sonnet-4-6")
    ap.add_argument("--effort", default="medium")
    ap.add_argument("--dry-run", action="store_true",
                    help="show prompt without API call")
    args = ap.parse_args()

    if not args.dry_run and not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set in environment.",
              file=sys.stderr)
        return 2

    os.makedirs(OUT_DIR_PHASE3, exist_ok=True)
    os.makedirs(OUT_DIR_RESULTS, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    terms = fetch_terms(conn)
    print(f"M26 terms fetched: {len(terms)}")

    if args.dry_run:
        sample = build_user_msg(terms)
        print()
        print("=== DRY-RUN: SYSTEM PROMPT (excerpt) ===")
        print(SYSTEM_PROMPT[:2500])
        print()
        print("=== DRY-RUN: USER MSG (first 2500 chars) ===")
        print(sample[:2500])
        print(f"\nTotal user msg length: {len(sample)} chars")
        print(f"Would call {args.model} (effort={args.effort}).")
        return 0

    from anthropic import Anthropic
    client = Anthropic()

    print(f"Calling {args.model} (effort={args.effort})...")
    parsed, response = call_claude(client, terms, args.model, args.effort)
    usage = response.usage
    in_tot = usage.input_tokens
    out_tot = usage.output_tokens
    cache_r = getattr(usage, "cache_read_input_tokens", 0) or 0

    if "opus" in args.model:
        in_price, out_price = 15.0, 75.0
    elif "haiku" in args.model:
        in_price, out_price = 1.0, 5.0
    else:
        in_price, out_price = 3.0, 15.0
    cost = (in_tot / 1_000_000) * in_price + (out_tot / 1_000_000) * out_price

    today = today_compact()
    raw_path = os.path.join(
        OUT_DIR_RESULTS,
        f"m26-phase3-debate-results-{args.model}-{today}.json",
    )
    debate_path = os.path.join(
        OUT_DIR_PHASE3, f"WA-M26-characteristic-debate-v1-{today}.md"
    )

    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump({
            "meta": {
                "generated_at": now_iso(),
                "model": args.model,
                "effort": args.effort,
                "n_terms": len(terms),
                "tokens": {
                    "input": in_tot, "output": out_tot,
                    "cache_read": cache_r,
                    "estimated_cost_usd": round(cost, 4),
                },
            },
            "result": parsed,
        }, f, indent=2, ensure_ascii=False)

    write_debate_doc(parsed, terms, debate_path)

    # Console summary
    n_sub_terms = sum(len(sg["terms"]) for sg in parsed["subgroups"])
    n_boundary = len(parsed["boundary"]["terms"])
    n_flagged = len(parsed["flagged"])
    print()
    print("=" * 60)
    print(f"  PHASE 3 PROPOSAL — {len(terms)} terms classified")
    print("=" * 60)
    for sg in parsed["subgroups"]:
        print(f"  {sg['code']:8s} {sg['label'][:35]:35s} {len(sg['terms'])} terms")
    print(f"  BOUNDARY                                    {n_boundary} terms")
    if n_flagged:
        print(f"  FLAGGED                                     {n_flagged} terms")
    print()
    print(f"Tokens — in: {in_tot:,} out: {out_tot:,} cache_read: {cache_r:,}")
    print(f"Estimated cost: ${cost:.4f}")
    print()
    print(f"Outputs:")
    print(f"  raw:    {raw_path}")
    print(f"  debate: {debate_path}")
    print()
    print("Status: PROVISIONAL. Phase 4 control read confirms or revises.")
    print("No DB writes performed.")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
