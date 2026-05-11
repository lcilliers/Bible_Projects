"""_apply_m26_phase4_control_read_v1_20260509.py — Claude API + DB read.

Phase 4 (Control read — verse-level validation of Phase 3 hypothesis)
automation prototype for M26 cluster.

Per wa-sessionb-cluster-instruction-v1_1-20260507 §7: validate the
provisional sub-groups via a bidirectional control read. Researcher
extension (2026-05-09): also produce a per-verse → sub-group association
to drive Phase 6 group-verse mapping.

Architecture (one API call per term):
  - System prompt: cluster context, all 7 sub-group definitions from
    Phase 3, validation criteria, JSON schema (system prompt cached)
  - User message: term metadata + ALL its active verses (up to a cap)
    + Phase 3 proposed placement
  - Output per term:
    * confirm placement (yes/no)
    * if no: proposed alternative sub-group + rationale
    * per-verse association: which sub-group(s) the verse evidences
    * open questions (OQ-NNN format)

Outputs:
  1. Raw API result JSON
       outputs/markdown/m26-phase4-control-read-results-{model}-{date}.json
  2. Phase 4 control-read document (markdown, per Phase 4 §7 deliverable)
       Sessions/Session_Clusters/M26/files phase 4/
       WA-M26-control-read-v1-{date}.md

DB writes: NONE. Phase 4 produces directives for Phase 5+ — those come
after researcher resolves any open questions.
"""
from __future__ import annotations

import argparse
import glob
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

OUT_DIR_PHASE4 = os.path.join(
    "Sessions", "Session_Clusters", "M26", "files phase 4"
)
OUT_DIR_RESULTS = os.path.join("outputs", "markdown")

MAX_VERSES_PER_CALL = 60  # cap so single-call input stays bounded


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def load_phase3_result() -> dict:
    """Find the most recent Phase 3 debate result JSON."""
    candidates = sorted(glob.glob(
        os.path.join(OUT_DIR_RESULTS,
                     "m26-phase3-debate-results-*.json")
    ))
    if not candidates:
        raise FileNotFoundError(
            "No Phase 3 debate result found. Run Phase 3 first."
        )
    with open(candidates[-1], encoding="utf-8") as f:
        return json.load(f)


def fetch_terms_with_verses(conn) -> list[dict]:
    """Return all M26 active terms with their active (non-set-aside) verses."""
    terms = list(conn.execute("""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration,
               mt.gloss, mt.language,
               ti.short_def_mounce, ti.meaning, ti.testament,
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

    out = []
    for t in terms:
        verses = list(conn.execute("""
            SELECT vr.id AS vr_id, vr.reference, vr.verse_text,
                   vr.testament,
                   vc.is_relevant, vc.is_anchor, vc.group_id,
                   vc.set_aside_reason, vc.analysis_note,
                   vcg.group_code, vcg.context_description AS group_desc
              FROM wa_verse_records vr
              LEFT JOIN verse_context vc
                     ON vc.verse_record_id=vr.id
                    AND vc.mti_term_id=vr.mti_term_id
                    AND COALESCE(vc.delete_flagged,0)=0
              LEFT JOIN verse_context_group vcg
                     ON vcg.id=vc.group_id
                    AND COALESCE(vcg.delete_flagged,0)=0
             WHERE vr.mti_term_id=?
               AND COALESCE(vr.delete_flagged,0)=0
               AND (vc.set_aside_reason IS NULL OR vc.set_aside_reason='')
             ORDER BY vr.reference
        """, (t["mti_id"],)))
        out.append({**dict(t), "verses": [dict(v) for v in verses]})
    return out


def build_system_prompt(phase3: dict) -> str:
    """Build cached system prompt with sub-group definitions."""
    p = phase3["result"]
    sg_lines = []
    for sg in p["subgroups"]:
        sg_lines.append(f"### {sg['code']} — {sg['label']}")
        sg_lines.append("")
        sg_lines.append("**Definition (T1-shaped):** "
                        + sg["characteristic_definition"])
        sg_lines.append("")
        sg_lines.append("**Phase 3 rationale:** " + sg["rationale"])
        sg_lines.append("")
        terms_list = ", ".join(
            f"{t['strong']} ({t['transliteration']})"
            for t in sg["terms"]
        )
        sg_lines.append(f"**Phase 3 term assignments:** {terms_list}")
        sg_lines.append("")
    boundary_terms = ", ".join(
        f"{t['strong']} ({t['transliteration']})"
        for t in p["boundary"]["terms"]
    )

    return f"""You are an analyst on the Soul Word Analysis Programme — Phase 4 (Control read against verse evidence) for cluster **M26 — {CLUSTER_DESC}**.

Phase 3 proposed a provisional sub-group structure based on glosses + meaning excerpts alone. Your task in Phase 4: validate (or revise) those placements by reading the actual verses where each term occurs.

# Bidirectional control criteria

For each term you are given, examine its verses against:

**Direction 1 — sub-group fit:** Do this term's verses, in their actual usage, evidence the inner-being characteristic of the sub-group it was placed in?

**Direction 2 — placement contention:** Does the term's verse evidence resist the proposed sub-group? Does it suggest a different sub-group, BOUNDARY, FLAG, or cluster reassignment?

# Phase 3 sub-group definitions (the working hypothesis)

{chr(10).join(sg_lines)}

### BOUNDARY (Phase 3)

**Phase 3 rationale:** {p["boundary"]["rationale"]}

**Phase 3 term assignments:** {boundary_terms}

# What to produce

For the term I will give you, return JSON in this schema:

{{
  "term_strong": "<copied>",
  "term_transliteration": "<copied>",
  "phase3_placement": "<copied — e.g. M26-A or BOUNDARY or FLAGGED>",
  "phase4_decision": "confirm" | "revise" | "borderline",
  "confirmed_or_proposed_placement": "<sub-group code OR 'BOUNDARY' OR 'FLAG' OR cluster reassignment like 'M11' or 'T2'>",
  "decision_rationale": "<2-4 sentences grounded in the verse evidence — name specific verses>",
  "verse_associations": [
    {{
      "verse_record_id": <int>,
      "reference": "<copied>",
      "primary_subgroup": "<sub-group code OR 'BOUNDARY'>",
      "secondary_subgroup": "<sub-group code OR null — only when verse genuinely bridges>",
      "verse_evidence_quote": "<≤15 word quote from the verse that grounded the call>",
      "brief": "<≤25 words plain English describing what THIS verse evidences>"
    }}
  ],
  "open_questions": [
    {{
      "id": "OQ-001",
      "question": "<the unresolved question>",
      "proposed_disposition": "<your proposed answer / direction>"
    }}
  ]
}}

# Discipline

- Decide `phase4_decision` based on what the verses actually say, not on Phase 3's stated rationale.
- "Confirm" means the verses overwhelmingly support the Phase 3 placement.
- "Revise" means you have a clear case (with verse citations) that a different placement is better.
- "Borderline" means the verses split between two sub-groups roughly equally — flag for researcher.
- Every verse in the input must appear exactly once in `verse_associations` — no omissions, no duplicates.
- `primary_subgroup` MUST be one of the codes from the Phase 3 hypothesis (M26-A through M26-G, or BOUNDARY). Do not invent codes.
- `verse_evidence_quote` is required for every verse — name what in the verse drove the call.
- Keep `open_questions` to genuine ambiguities; do not pad. Empty list is fine if the term is unambiguous.
- Fluency is not a quality signal. If you cannot point to verse text that grounds a claim, lean to "borderline" or surface as open question.
"""


OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "term_strong": {"type": "string"},
        "term_transliteration": {"type": "string"},
        "phase3_placement": {"type": "string"},
        "phase4_decision": {"type": "string",
                            "enum": ["confirm", "revise", "borderline"]},
        "confirmed_or_proposed_placement": {"type": "string"},
        "decision_rationale": {"type": "string"},
        "verse_associations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "verse_record_id": {"type": "integer"},
                    "reference": {"type": "string"},
                    "primary_subgroup": {"type": "string"},
                    "secondary_subgroup": {"type": ["string", "null"]},
                    "verse_evidence_quote": {"type": "string"},
                    "brief": {"type": "string"},
                },
                "required": ["verse_record_id", "reference",
                             "primary_subgroup", "secondary_subgroup",
                             "verse_evidence_quote", "brief"],
                "additionalProperties": False,
            },
        },
        "open_questions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "question": {"type": "string"},
                    "proposed_disposition": {"type": "string"},
                },
                "required": ["id", "question", "proposed_disposition"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["term_strong", "term_transliteration", "phase3_placement",
                 "phase4_decision", "confirmed_or_proposed_placement",
                 "decision_rationale", "verse_associations",
                 "open_questions"],
    "additionalProperties": False,
}


def find_phase3_placement(strong: str, phase3_result: dict) -> str:
    """Look up which Phase 3 group this term landed in."""
    for sg in phase3_result["subgroups"]:
        for t in sg["terms"]:
            if t["strong"] == strong:
                return sg["code"]
    for t in phase3_result["boundary"]["terms"]:
        if t["strong"] == strong:
            return "BOUNDARY"
    for t in phase3_result["flagged"]:
        if t["strong"] == strong:
            return "FLAGGED"
    return "UNPLACED"


def build_user_msg(term: dict, phase3_placement: str) -> str:
    pkg = {
        "term": {
            "mti_term_id": term["mti_id"],
            "strong": term["strongs_number"],
            "transliteration": term["transliteration"],
            "gloss": term["gloss"],
            "language": term["language"],
            "testament": term["testament"],
            "short_def_mounce": term["short_def_mounce"],
            "occurrence_count": term["occurrence_count"],
        },
        "phase3_placement": phase3_placement,
        "verses": [],
    }

    verses = term["verses"]
    if len(verses) > MAX_VERSES_PER_CALL:
        # Sample evenly across the verse list to preserve canonical spread
        step = len(verses) / MAX_VERSES_PER_CALL
        verses = [verses[int(i * step)] for i in range(MAX_VERSES_PER_CALL)]

    for v in verses:
        item = {
            "verse_record_id": v["vr_id"],
            "reference": v["reference"],
            "testament": v["testament"],
            "verse_text": v["verse_text"],
        }
        if v["group_code"]:
            item["existing_group"] = v["group_code"]
            item["existing_group_desc"] = (v["group_desc"] or "")[:200]
        if v["analysis_note"]:
            item["existing_analysis_note"] = v["analysis_note"][:200]
        pkg["verses"].append(item)

    if len(term["verses"]) > MAX_VERSES_PER_CALL:
        pkg["_note"] = (
            f"Showing {MAX_VERSES_PER_CALL} canonically-spread verses out "
            f"of {len(term['verses'])} active. Decision should be safe at "
            "this sample size."
        )

    return (
        f"Validate Phase 3 placement for {term['strongs_number']} "
        f"({term['transliteration']}). Return JSON in the schema above. "
        "Every verse in `verses` must appear exactly once in "
        "`verse_associations`.\n\n"
        f"```json\n{json.dumps(pkg, ensure_ascii=False, indent=2)}\n```"
    )


def call_claude(client, term, phase3_placement, system_prompt, model, effort):
    user_msg = build_user_msg(term, phase3_placement)
    text_parts = []
    response = None
    with client.messages.stream(
        model=model,
        max_tokens=16000,
        thinking={"type": "adaptive"},
        output_config={
            "effort": effort,
            "format": {"type": "json_schema", "schema": OUTPUT_SCHEMA},
        },
        system=[{
            "type": "text",
            "text": system_prompt,
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
        dump_path = os.path.join(
            OUT_DIR_RESULTS,
            f"m26-phase4-truncated-{term['strongs_number']}-"
            f"{today_compact()}.txt"
        )
        with open(dump_path, "w", encoding="utf-8") as f:
            f.write(raw)
        raise RuntimeError(
            f"JSON decode failed for {term['strongs_number']}: {e}. "
            f"Stop reason: {getattr(response, 'stop_reason', '?')}. "
            f"Raw output dumped to {dump_path}."
        ) from e
    return parsed, response


def write_control_read_doc(decisions, terms, phase3, out_path):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    today_c = today.replace("-", "")

    confirmed = [d for d in decisions if d.get("phase4_decision") == "confirm"]
    revised = [d for d in decisions if d.get("phase4_decision") == "revise"]
    borderline = [d for d in decisions if d.get("phase4_decision") == "borderline"]
    errors = [d for d in decisions if "error" in d]

    lines = []
    lines.append(f"# WA-M26-control-read-v1-{today_c}")
    lines.append("")
    lines.append("> Framework B Soul Word Analysis Programme — Session B Phase 4 (Control read)")
    lines.append(f"> Cluster: M26 — {CLUSTER_DESC}")
    lines.append(f"> Date: {today}")
    lines.append("> Method: Claude API per-term verse-level validation against Phase 3 hypothesis (sonnet-4-6, system prompt cached)")
    lines.append("> **Status: PROVISIONAL** — researcher review of revisions and OQs required before sub-group assignment directive is authored.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Summary table
    lines.append("## Phase 3 → Phase 4 transition summary")
    lines.append("")
    lines.append("| Decision | Count |")
    lines.append("|---|---:|")
    lines.append(f"| Confirm placement | {len(confirmed)} |")
    lines.append(f"| Revise placement | **{len(revised)}** |")
    lines.append(f"| Borderline (researcher review) | {len(borderline)} |")
    lines.append(f"| Errors (re-run needed) | {len(errors)} |")
    lines.append(f"| **Total terms** | **{len(decisions)}** |")
    lines.append("")

    # Aggregate revisions
    if revised:
        lines.append("## Proposed revisions to Phase 3 placement")
        lines.append("")
        lines.append("| Strong's | Translit | Phase 3 | Phase 4 proposes | Rationale |")
        lines.append("|---|---|---|---|---|")
        for d in revised:
            rationale = d['decision_rationale'].replace("|", "\\|")
            lines.append(
                f"| {d['term_strong']} | *{d['term_transliteration']}* "
                f"| {d['phase3_placement']} "
                f"| **{d['confirmed_or_proposed_placement']}** "
                f"| {rationale} |"
            )
        lines.append("")

    # Borderlines
    if borderline:
        lines.append("## Borderline terms — researcher decision required")
        lines.append("")
        lines.append("| Strong's | Translit | Phase 3 | Phase 4 proposes | Rationale |")
        lines.append("|---|---|---|---|---|")
        for d in borderline:
            rationale = d['decision_rationale'].replace("|", "\\|")
            lines.append(
                f"| {d['term_strong']} | *{d['term_transliteration']}* "
                f"| {d['phase3_placement']} "
                f"| {d['confirmed_or_proposed_placement']} "
                f"| {rationale} |"
            )
        lines.append("")

    # Open questions roll-up
    all_oqs = []
    for d in decisions:
        for oq in d.get("open_questions", []):
            all_oqs.append((d["term_strong"], d["term_transliteration"], oq))
    if all_oqs:
        lines.append(f"## Open questions ({len(all_oqs)}) — researcher disposition required")
        lines.append("")
        for i, (strong, transl, oq) in enumerate(all_oqs, 1):
            lines.append(f"### OQ-M26-P4-{i:03d}  ·  {strong} *{transl}*")
            lines.append("")
            lines.append(f"**Question:** {oq.get('question')}")
            lines.append("")
            lines.append(f"**Proposed disposition:** {oq.get('proposed_disposition')}")
            lines.append("")

    # Per-term detail
    lines.append("---")
    lines.append("")
    lines.append("## Per-term details")
    lines.append("")
    for d in decisions:
        if "error" in d:
            lines.append(f"### {d.get('term_strong', '?')} *{d.get('term_transliteration','?')}* — ERROR")
            lines.append("")
            lines.append(f"`{d.get('error')}`")
            lines.append("")
            continue
        marker = {
            "confirm": "✓",
            "revise": "✗",
            "borderline": "?",
        }.get(d["phase4_decision"], "·")
        lines.append(
            f"### {marker} {d['term_strong']} *{d['term_transliteration']}* "
            f"— {d['phase4_decision']}"
        )
        lines.append("")
        lines.append(f"**Phase 3 placement:** {d['phase3_placement']}  ·  "
                     f"**Phase 4 placement:** {d['confirmed_or_proposed_placement']}")
        lines.append("")
        lines.append(f"**Rationale:** {d['decision_rationale']}")
        lines.append("")
        # Verse association table
        n_v = len(d.get("verse_associations", []))
        if n_v:
            lines.append(f"**Verse associations ({n_v}):**")
            lines.append("")
            lines.append("| Reference | Primary | Secondary | Evidence | Brief |")
            lines.append("|---|---|---|---|---|")
            for va in d["verse_associations"]:
                evidence = (va["verse_evidence_quote"] or "").replace("|", "\\|")
                brief = (va["brief"] or "").replace("|", "\\|")
                sec = va.get("secondary_subgroup") or "—"
                lines.append(
                    f"| {va['reference']} | {va['primary_subgroup']} "
                    f"| {sec} | \"{evidence}\" | {brief} |"
                )
            lines.append("")
        if d.get("open_questions"):
            lines.append(f"**Open questions:** {len(d['open_questions'])}")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"*WA-M26-control-read-v1-{today_c}*")
    lines.append("")
    lines.append("**Next step:** Researcher reviews revisions, borderlines, and open questions. Once all decisions are confirmed, author the sub-group-assignment directive (with any cluster reassignment directive if applicable).")

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
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.dry_run and not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set in environment.",
              file=sys.stderr)
        return 2

    os.makedirs(OUT_DIR_PHASE4, exist_ok=True)
    os.makedirs(OUT_DIR_RESULTS, exist_ok=True)

    phase3 = load_phase3_result()
    print(f"Phase 3 result loaded: "
          f"{len(phase3['result']['subgroups'])} sub-groups, "
          f"{len(phase3['result']['boundary']['terms'])} BOUNDARY, "
          f"{len(phase3['result']['flagged'])} flagged.")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    terms = fetch_terms_with_verses(conn)
    if args.limit:
        terms = terms[: args.limit]
    n_verses_total = sum(len(t["verses"]) for t in terms)
    print(f"M26 active terms with verses: {len(terms)}  "
          f"(total verses: {n_verses_total})")

    system_prompt = build_system_prompt(phase3)

    if args.dry_run:
        sample_term = terms[0]
        sample_placement = find_phase3_placement(
            sample_term["strongs_number"], phase3["result"]
        )
        sample = build_user_msg(sample_term, sample_placement)
        print()
        print(f"=== DRY-RUN: SYSTEM PROMPT length = {len(system_prompt)} ===")
        print(system_prompt[:1500])
        print()
        print(f"=== SAMPLE USER MSG ({sample_term['strongs_number']}) ===")
        print(sample[:2500])
        print(f"\nTotal user msg length: {len(sample)} chars")
        print(f"Would call {args.model} (effort={args.effort}) for "
              f"{len(terms)} terms.")
        return 0

    from anthropic import Anthropic
    client = Anthropic()

    decisions = []
    in_tot = out_tot = cache_r_tot = 0
    print(f"Calling {args.model} (effort={args.effort})...\n")

    for i, t in enumerate(terms, 1):
        ph3 = find_phase3_placement(t["strongs_number"], phase3["result"])
        n_verses = len(t["verses"])
        if n_verses == 0:
            print(f"  [{i:3d}/{len(terms)}] - {t['strongs_number']:8s} "
                  f"{t['transliteration']:18s} (0 verses — skip)")
            decisions.append({
                "term_strong": t["strongs_number"],
                "term_transliteration": t["transliteration"],
                "phase3_placement": ph3,
                "phase4_decision": "borderline",
                "confirmed_or_proposed_placement": ph3,
                "decision_rationale": "0 active verses — cannot validate via verse evidence; placement deferred.",
                "verse_associations": [],
                "open_questions": [],
            })
            continue
        try:
            parsed, resp = call_claude(
                client, t, ph3, system_prompt, args.model, args.effort
            )
        except Exception as e:
            print(f"  [{i:3d}/{len(terms)}] X {t['strongs_number']:8s} "
                  f"{t['transliteration']:18s} ERROR {type(e).__name__}: {e}")
            decisions.append({
                "term_strong": t["strongs_number"],
                "term_transliteration": t["transliteration"],
                "phase3_placement": ph3,
                "error": f"{type(e).__name__}: {e}",
            })
            continue

        usage = resp.usage
        in_tot += usage.input_tokens
        out_tot += usage.output_tokens
        cache_r_tot += getattr(usage, "cache_read_input_tokens", 0) or 0

        decisions.append(parsed)
        marker = {
            "confirm": "+", "revise": "*", "borderline": "?"
        }.get(parsed["phase4_decision"], "·")
        target = parsed["confirmed_or_proposed_placement"]
        delta = "" if (parsed["phase4_decision"] == "confirm") else f" -> {target}"
        print(f"  [{i:3d}/{len(terms)}] {marker} {t['strongs_number']:8s} "
              f"{t['transliteration']:18s} verses={n_verses:3d}  "
              f"{ph3}{delta}")

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
        f"m26-phase4-control-read-results-{args.model}-{today}.json",
    )
    doc_path = os.path.join(
        OUT_DIR_PHASE4, f"WA-M26-control-read-v1-{today}.md"
    )

    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump({
            "meta": {
                "generated_at": now_iso(),
                "model": args.model,
                "effort": args.effort,
                "phase3_source": phase3.get("meta", {}).get("generated_at"),
                "n_terms": len(terms),
                "tokens": {
                    "input": in_tot, "output": out_tot,
                    "cache_read": cache_r_tot,
                    "estimated_cost_usd": round(cost, 4),
                },
            },
            "decisions": decisions,
        }, f, indent=2, ensure_ascii=False)

    write_control_read_doc(decisions, terms, phase3, doc_path)

    # Console summary
    confirmed = sum(1 for d in decisions if d.get("phase4_decision") == "confirm")
    revised = sum(1 for d in decisions if d.get("phase4_decision") == "revise")
    borderline = sum(1 for d in decisions if d.get("phase4_decision") == "borderline")
    errors = sum(1 for d in decisions if "error" in d)
    n_oqs = sum(len(d.get("open_questions", [])) for d in decisions)

    print()
    print("=" * 60)
    print(f"  PHASE 4 CONTROL READ — {len(decisions)} terms validated")
    print("=" * 60)
    print(f"  confirm     {confirmed}")
    print(f"  revise      {revised}")
    print(f"  borderline  {borderline}")
    print(f"  errors      {errors}")
    print(f"  open_questions  {n_oqs}")
    print()
    print(f"Tokens — in: {in_tot:,} out: {out_tot:,} "
          f"cache_read: {cache_r_tot:,}")
    print(f"Estimated cost: ${cost:.4f}")
    print()
    print(f"Outputs:")
    print(f"  raw:    {raw_path}")
    print(f"  doc:    {doc_path}")
    print()
    print("Status: PROVISIONAL. Researcher review of revisions and OQs.")
    print("No DB writes performed.")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
