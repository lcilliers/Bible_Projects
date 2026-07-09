"""_apply_m26_phase456_v1_20260509.py — Claude API + DB read.

Script 2 of M26 Phase 4 sequence. Per-sub-group API calls that combine:

  Phase 4: verse-level validation of sub-group placement
  Phase 5: 250-word sub-group summary (a side-effect of the call)
  Phase 6: full group-verse mapping per sub-group (the main deliverable)

Architecture (one API call per sub-group):
  - Each sub-group's terms + all their non-set-aside verses go to one
    API call — the verse-to-sub-group link is already in the DB
    (mti_terms.cluster_subgroup_id), so the API only needs to do
    intra-sub-group meaning-clustering.
  - Output: structured JSON mapping → converted to an M15-Phase-7-
    compatible markdown document so the existing apply pipeline can
    consume it.

Outputs (NO DB writes):
  Sessions/Session_Clusters/M26/files phase 4-6/
    WA-M26-{X}-group-verse-mapping-v1-{date}.md  (×8)
    WA-M26-control-read-and-summaries-v1-{date}.md
  outputs/markdown/
    m26-phase456-results-{model}-{date}.json
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(".env")
except ImportError:
    pass

DB_PATH = os.path.join("database", "bible_research.db")
CLUSTER_CODE = "M26"
CLUSTER_DESC = "Righteousness and Justice"

OUT_DIR_DOCS = os.path.join(
    "Sessions", "Session_Clusters", "M26", "files phase 4-6"
)
OUT_DIR_RESULTS = os.path.join("outputs", "markdown")


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact():
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def fetch_subgroup_data(conn, subgroup_code: str) -> dict:
    sg = conn.execute(
        "SELECT id, subgroup_code, label, core_description "
        "  FROM cluster_subgroup "
        " WHERE cluster_code='M26' AND subgroup_code=? "
        "   AND COALESCE(delete_flagged,0)=0",
        (subgroup_code,),
    ).fetchone()
    if not sg:
        raise RuntimeError(f"sub-group {subgroup_code} not found")

    terms = list(conn.execute(
        "SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration, "
        "       mt.gloss, mt.language, "
        "       ti.short_def_mounce, ti.testament, ti.occurrence_count "
        "  FROM mti_terms mt "
        "  LEFT JOIN wa_term_inventory ti "
        "    ON ti.strongs_number=mt.strongs_number "
        "    AND COALESCE(ti.delete_flagged,0)=0 "
        "    AND COALESCE(ti.term_owner_type,'OWNER')='OWNER' "
        " WHERE mt.cluster_subgroup_id=? "
        "   AND COALESCE(mt.delete_flagged,0)=0 "
        " ORDER BY mt.language, mt.strongs_number",
        (sg["id"],),
    ))

    # Verses for each term, with current group state
    verses = []
    for t in terms:
        for v in conn.execute(
            "SELECT vc.id AS vc_id, vc.verse_record_id AS vr_id, "
            "       vr.reference, vr.verse_text, vr.testament, "
            "       vc.is_relevant, vc.is_anchor, vc.group_id, "
            "       vc.analysis_note, vcg.group_code, "
            "       vcg.context_description AS group_desc, "
            "       mt.strongs_number, mt.transliteration "
            "  FROM verse_context vc "
            "  JOIN mti_terms mt ON mt.id=vc.mti_term_id "
            "  JOIN wa_verse_records vr ON vr.id=vc.verse_record_id "
            "  LEFT JOIN verse_context_group vcg "
            "    ON vcg.id=vc.group_id "
            "    AND COALESCE(vcg.delete_flagged,0)=0 "
            " WHERE vc.mti_term_id=? "
            "   AND COALESCE(vc.delete_flagged,0)=0 "
            "   AND (vc.set_aside_reason IS NULL "
            "        OR vc.set_aside_reason='') "
            " ORDER BY vr.reference",
            (t["mti_id"],),
        ):
            verses.append(dict(v))

    # Existing verse_context_group rows for these terms (for "RETAINED"
    # candidate identification in the API output)
    mti_ids = [t["mti_id"] for t in terms]
    existing_groups = []
    if mti_ids:
        ph = ",".join("?" * len(mti_ids))
        for vcg in conn.execute(
            f"SELECT id, group_code, mti_term_id, context_description "
            f"  FROM verse_context_group "
            f" WHERE mti_term_id IN ({ph}) "
            f"   AND COALESCE(delete_flagged,0)=0 "
            f" ORDER BY group_code",
            tuple(mti_ids),
        ):
            existing_groups.append(dict(vcg))

    return {
        "subgroup": dict(sg),
        "terms": [dict(t) for t in terms],
        "verses": verses,
        "existing_groups": existing_groups,
    }


SYSTEM_PROMPT_TEMPLATE = """You are an analyst on the Soul Word Analysis Programme — Session B Phase 6 (Group-verse mapping) for cluster **M26 — {cluster_desc}**.

# Operating principle (non-negotiable)

> Read every verse. Do not sample. Read what they say. Let the structure and analysis emerge from what is found. No assumptions from memory. No jumping to conclusions.

You will receive ALL verses for one sub-group. Read every one. Group them by what the verse text actually shows about the inner-being characteristic — not by gloss labels, not by registry-era codes, not by general theological knowledge.

# T1 Characteristic framework

A distinct inner-being characteristic has identifiable constitutional location, engages a distinguishable set of inner faculties, produces recognisable impact, has a structural opposite, and can be distinguished by causal direction or directional object.

# Your task — three combined deliverables in one call

**Phase 4 — Validation:** Confirm that the sub-group's verses, in their actual usage, evidence the inner-being characteristic the sub-group names. If the verses point elsewhere, surface that as a concern (don't silently re-classify).

**Phase 6 — Group-verse mapping:** Within the sub-group, identify the distinct meaning-groups (verse_context_groups). Each group is a coherent set of verses sharing one inner-being phenomenon, with one anchor verse. Use the existing verse_context_groups (provided in the input) as the working hypothesis — but read the verses to confirm or revise:
  - **RETAINED** — existing group description matches the verses; keep it
  - **RETAINED_REFINED** — keep the group_id but revise the description to better match the verses
  - **NEW** — verses suggest a phenomenon not captured by any existing group; propose a new group with `existing_db_group_id: null`
  - **SPLIT** — an existing group's verses contain genuinely distinct inner-being phenomena (different anchors needed for different subsets); split into multiple groups, each with `existing_db_group_id: null` (the original group will be retired by the apply pipeline if it ends up with 0 verses)

**Phase 5 — 250-word summary:** Once the groups are settled, write one summary describing what the sub-group's verses, taken together, evidence about the characteristic.

# Conglomerate-split test (decisive)

If a single group's verses cannot be answered uniformly by ONE anchor verse — i.e., different verse subsets need different anchors to express the same prompt — split the group. This test is decisive; if it fires, do not bundle.

# Dual assignments

A single verse can carry more than one inner-being phenomenon. When it does, list it under its primary group (full row) and add a `secondary_group_code` reference to the second group (use the analytical code like "A-2", not the DB id). The apply pipeline will create a second vc row.

# Anchor designation

Every group must have exactly one anchor verse — the verse that most directly and definitionally evidences the group's named phenomenon. Mark the verse's `is_anchor` true; the apply pipeline ensures one anchor per group.

# Discipline

- Every verse in `verses` must appear exactly once across `groups[*].verses` (or as a secondary in another group's `secondary_group_code`).
- For each verse, `analysis_note` is ≤25 words plain English describing what THIS verse shows.
- Fluency is not a quality signal. Each grouping decision must be grounded in verse text, not gloss labels.
- If you cannot confidently group a verse, raise it as an open question rather than guess.

# Sub-group context for THIS call

**Sub-group code:** {subgroup_code}
**Label:** {subgroup_label}
**T1 definition (from Phase 3):**

{subgroup_definition}

# Output JSON schema (return exactly this shape)

```
{{
  "subgroup_code": "{subgroup_code}",
  "validation": "confirmed" | "concerns",
  "validation_notes": "<2-3 sentences on whether the verse evidence supports the sub-group's stated characteristic>",
  "groups": [
    {{
      "code": "<analytical code, e.g. A-1, A-2 — within this sub-group>",
      "status": "RETAINED" | "RETAINED_REFINED" | "NEW" | "SPLIT",
      "existing_db_group_id": <int | null>,
      "label": "<≤8 words>",
      "description": "<the canonical description of this group, grounded in verse evidence>",
      "anchor_vr_id": <int>,
      "anchor_rationale": "<1-2 sentences on why this verse is the anchor>",
      "verses": [
        {{
          "vr_id": <int>,
          "reference": "<copied>",
          "strong": "<copied>",
          "is_anchor": <bool>,
          "secondary_group_code": "<analytical code in this sub-group | null>",
          "analysis_note": "<≤25 words on what this verse shows>"
        }}
      ]
    }}
  ],
  "open_questions": [
    {{
      "id": "OQ-001",
      "question": "<the unresolved question>",
      "proposed_disposition": "<your proposed answer>"
    }}
  ],
  "summary_250w": "<one paragraph, target 200-280 words, summarising what the sub-group's verses collectively evidence about the characteristic>"
}}
```
"""

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "subgroup_code": {"type": "string"},
        "validation": {"type": "string",
                       "enum": ["confirmed", "concerns"]},
        "validation_notes": {"type": "string"},
        "groups": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "code": {"type": "string"},
                    "status": {"type": "string",
                               "enum": ["RETAINED", "RETAINED_REFINED",
                                        "NEW", "SPLIT"]},
                    "existing_db_group_id": {"type": ["integer", "null"]},
                    "label": {"type": "string"},
                    "description": {"type": "string"},
                    "anchor_vr_id": {"type": "integer"},
                    "anchor_rationale": {"type": "string"},
                    "verses": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "vr_id": {"type": "integer"},
                                "reference": {"type": "string"},
                                "strong": {"type": "string"},
                                "is_anchor": {"type": "boolean"},
                                "secondary_group_code": {
                                    "type": ["string", "null"]
                                },
                                "analysis_note": {"type": "string"},
                            },
                            "required": ["vr_id", "reference", "strong",
                                         "is_anchor",
                                         "secondary_group_code",
                                         "analysis_note"],
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["code", "status", "existing_db_group_id",
                             "label", "description", "anchor_vr_id",
                             "anchor_rationale", "verses"],
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
        "summary_250w": {"type": "string"},
    },
    "required": ["subgroup_code", "validation", "validation_notes",
                 "groups", "open_questions", "summary_250w"],
    "additionalProperties": False,
}


def build_user_msg(sg_data: dict) -> str:
    pkg = {
        "subgroup": sg_data["subgroup"],
        "terms": [
            {
                "mti_term_id": t["mti_id"],
                "strong": t["strongs_number"],
                "transliteration": t["transliteration"],
                "gloss": t["gloss"],
                "language": t["language"],
                "testament": t["testament"],
                "short_def_mounce": t.get("short_def_mounce"),
                "occurrence_count": t.get("occurrence_count"),
            }
            for t in sg_data["terms"]
        ],
        "existing_verse_context_groups": [
            {
                "id": g["id"],
                "group_code": g["group_code"],
                "mti_term_id": g["mti_term_id"],
                "description": g["context_description"],
            }
            for g in sg_data["existing_groups"]
        ],
        "verses": [
            {
                "vr_id": v["vr_id"],
                "reference": v["reference"],
                "testament": v["testament"],
                "verse_text": v["verse_text"],
                "strong": v["strongs_number"],
                "transliteration": v["transliteration"],
                "current_group_id": v["group_id"],
                "current_group_code": v["group_code"],
                "current_analysis_note": v["analysis_note"],
                "currently_anchor": bool(v["is_anchor"]),
            }
            for v in sg_data["verses"]
        ],
    }
    return (
        f"Process sub-group {sg_data['subgroup']['subgroup_code']} per the "
        "system prompt. Return JSON in the schema. Every verse in `verses` "
        "must appear exactly once across `groups[*].verses` (with optional "
        "`secondary_group_code` for dual assignments).\n\n"
        f"```json\n{json.dumps(pkg, ensure_ascii=False, indent=2)}\n```"
    )


def call_claude(client, sg_data, model, effort):
    sg = sg_data["subgroup"]
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        cluster_desc=CLUSTER_DESC,
        subgroup_code=sg["subgroup_code"],
        subgroup_label=sg["label"],
        subgroup_definition=sg["core_description"],
    )
    user_msg = build_user_msg(sg_data)

    text_parts = []
    response = None
    with client.messages.stream(
        model=model,
        max_tokens=32000,
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
            f"m26-phase456-truncated-{sg['subgroup_code']}-"
            f"{today_compact()}.txt"
        )
        with open(dump_path, "w", encoding="utf-8") as f:
            f.write(raw)
        raise RuntimeError(
            f"JSON decode failed for {sg['subgroup_code']}: {e}. "
            f"Stop reason: {getattr(response, 'stop_reason', '?')}. "
            f"Raw output dumped to {dump_path}."
        ) from e
    return parsed, response


def write_mapping_doc(sg_data: dict, parsed: dict, out_path: str) -> None:
    """Write an M15-Phase-7-compatible mapping document."""
    sg = sg_data["subgroup"]
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    today_c = today.replace("-", "")

    lines = []
    lines.append(f"# WA-M26-{sg['subgroup_code'].split('-')[-1]}-"
                 f"group-verse-mapping-v1-{today_c}")
    lines.append("")
    lines.append(f"**Sub-group:** {sg['subgroup_code']} — {sg['label']}")
    lines.append(f"**Cluster:** M26 — {CLUSTER_DESC}")
    lines.append(f"**Phase:** 6 — Group-verse mapping (per-verse, API-produced)")
    lines.append(f"**Date:** {today}")
    lines.append(f"**Method:** Claude API single-call per sub-group "
                 f"(claude-sonnet-4-6, structured JSON output)")
    lines.append(f"**Total non-set-aside verses:** {len(sg_data['verses'])}")
    lines.append(f"**Phase 6 produces no DB writes.**")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Phase 4 validation")
    lines.append("")
    lines.append(f"**Result:** `{parsed['validation']}`")
    lines.append("")
    lines.append(parsed["validation_notes"])
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Phase 5 summary (250 words)")
    lines.append("")
    lines.append(parsed["summary_250w"])
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Group inventory")
    lines.append("")
    lines.append("| Code | Label | Status | Existing gid | Verses |")
    lines.append("|---|---|---|---:|---:|")
    for g in parsed["groups"]:
        gid = g.get("existing_db_group_id")
        gid_str = str(gid) if gid is not None else "—"
        lines.append(
            f"| {g['code']} | {g['label']} | {g['status']} "
            f"| {gid_str} | {len(g['verses'])} |"
        )
    lines.append("")

    # Per-group sections in M15-Phase-7-compatible format
    for g in parsed["groups"]:
        gid = g.get("existing_db_group_id")
        heading_codes = f" (code {gid})" if gid else ""
        lines.append("---")
        lines.append("")
        lines.append(f"## Group {g['code']}{heading_codes} — {g['label']}")
        lines.append("")
        lines.append(f"**Status:** {g['status']}")
        lines.append(f"**Description from verses:** {g['description']}")
        lines.append(f"**Anchor verse:** vr={g['anchor_vr_id']} — "
                     f"{g['anchor_rationale']}")
        lines.append("")
        lines.append("| vr_id | Reference | Term | What the verse shows |")
        lines.append("|---|---|---|---|")
        for v in g["verses"]:
            note = (v["analysis_note"] or "").replace("|", "\\|")
            anchor_marker = "**ANCHOR** — " if v["is_anchor"] else ""
            secondary = ""
            if v.get("secondary_group_code"):
                secondary = (f" (DUAL — secondary group "
                             f"{v['secondary_group_code']})")
            lines.append(
                f"| {v['vr_id']} | {v['reference']} | {v['strong']} "
                f"| {anchor_marker}{note}{secondary} |"
            )
        lines.append("")

    if parsed.get("open_questions"):
        lines.append("---")
        lines.append("")
        lines.append("## Open questions for researcher")
        lines.append("")
        for oq in parsed["open_questions"]:
            lines.append(f"### {oq['id']}")
            lines.append("")
            lines.append(f"**Question:** {oq['question']}")
            lines.append("")
            lines.append(f"**Proposed disposition:** "
                         f"{oq['proposed_disposition']}")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"*WA-M26-{sg['subgroup_code'].split('-')[-1]}-"
                 f"group-verse-mapping-v1-{today_c} — "
                 f"Phase 4+5+6 combined output via Claude API*")
    lines.append("")
    lines.append("**Next step:** researcher reviews; once approved, the "
                 "Phase 7 apply pipeline (`_apply_m15_phase7_v1_*.py`) "
                 "consumes this document.")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_summaries_doc(all_results: list[tuple[str, dict]], out_path: str):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    today_c = today.replace("-", "")
    lines = []
    lines.append(f"# WA-M26-control-read-and-summaries-v1-{today_c}")
    lines.append("")
    lines.append("**Cluster:** M26 — Righteousness and Justice")
    lines.append("**Phase:** 4 (validation) + 5 (summaries)")
    lines.append(f"**Date:** {today}")
    lines.append("**Method:** Claude API per-sub-group calls "
                 "(claude-sonnet-4-6)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Phase 4 validation roll-up")
    lines.append("")
    lines.append("| Sub-group | Result | Notes |")
    lines.append("|---|---|---|")
    for code, parsed in all_results:
        notes = (parsed.get("validation_notes") or "").replace("|", "\\|")
        lines.append(f"| {code} | `{parsed.get('validation','?')}` | {notes} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    for code, parsed in all_results:
        lines.append(f"## {code} — Phase 5 summary (250 words)")
        lines.append("")
        lines.append(parsed.get("summary_250w", "(no summary returned)"))
        lines.append("")
        if parsed.get("open_questions"):
            lines.append(f"### {code} open questions")
            lines.append("")
            for oq in parsed["open_questions"]:
                lines.append(f"- **{oq['id']}** — {oq['question']}")
                lines.append(f"  - Proposed: {oq['proposed_disposition']}")
            lines.append("")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="claude-sonnet-4-6")
    ap.add_argument("--effort", default="medium")
    ap.add_argument("--subgroup", default=None,
                    help="Only one sub-group code (e.g. M26-A); "
                         "default: all 8")
    ap.add_argument("--dry-run", action="store_true",
                    help="show prompts; no API calls")
    args = ap.parse_args()

    if not args.dry_run and not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set in environment.",
              file=sys.stderr)
        return 2

    os.makedirs(OUT_DIR_DOCS, exist_ok=True)
    os.makedirs(OUT_DIR_RESULTS, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Discover all M26 sub-groups
    sg_codes = [r["subgroup_code"] for r in conn.execute(
        "SELECT subgroup_code FROM cluster_subgroup "
        " WHERE cluster_code='M26' AND COALESCE(delete_flagged,0)=0 "
        " ORDER BY sort_order"
    )]
    if args.subgroup:
        sg_codes = [c for c in sg_codes if c == args.subgroup]
        if not sg_codes:
            print(f"sub-group {args.subgroup} not found")
            return 2

    print(f"Sub-groups to process: {sg_codes}")

    if args.dry_run:
        sg_data = fetch_subgroup_data(conn, sg_codes[0])
        sg = sg_data["subgroup"]
        sp = SYSTEM_PROMPT_TEMPLATE.format(
            cluster_desc=CLUSTER_DESC,
            subgroup_code=sg["subgroup_code"],
            subgroup_label=sg["label"],
            subgroup_definition=sg["core_description"],
        )
        user = build_user_msg(sg_data)
        print()
        print(f"=== DRY RUN — sub-group {sg_codes[0]} ===")
        print(f"Terms: {len(sg_data['terms'])}")
        print(f"Verses: {len(sg_data['verses'])}")
        print(f"Existing groups: {len(sg_data['existing_groups'])}")
        print(f"System prompt length: {len(sp)} chars")
        print(f"User msg length: {len(user)} chars")
        print()
        print("=== USER MSG (first 1500 chars) ===")
        print(user[:1500])
        return 0

    from anthropic import Anthropic
    client = Anthropic()

    all_results = []
    in_tot = out_tot = cache_r_tot = 0
    today = today_compact()

    for code in sg_codes:
        print()
        print(f"== {code} ==")
        sg_data = fetch_subgroup_data(conn, code)
        n_verses = len(sg_data["verses"])
        if n_verses == 0:
            print(f"  0 verses — skipping")
            continue
        print(f"  Terms: {len(sg_data['terms'])}  "
              f"Verses: {n_verses}  "
              f"Existing groups: {len(sg_data['existing_groups'])}")
        print(f"  Calling {args.model} (streaming)...")
        try:
            parsed, resp = call_claude(client, sg_data, args.model,
                                       args.effort)
        except Exception as e:
            print(f"  [ERR] {type(e).__name__}: {e}")
            continue
        usage = resp.usage
        in_tot += usage.input_tokens
        out_tot += usage.output_tokens
        cache_r_tot += getattr(usage, "cache_read_input_tokens", 0) or 0

        # Coverage check
        declared_vrs = set()
        for g in parsed["groups"]:
            for v in g["verses"]:
                declared_vrs.add(v["vr_id"])
        expected_vrs = {v["vr_id"] for v in sg_data["verses"]}
        missing = expected_vrs - declared_vrs
        extra = declared_vrs - expected_vrs

        n_groups = len(parsed["groups"])
        n_anchors = sum(
            1 for g in parsed["groups"]
            for v in g["verses"] if v["is_anchor"]
        )
        n_oqs = len(parsed.get("open_questions", []))
        print(f"  groups={n_groups}  verses_placed={len(declared_vrs)}/"
              f"{len(expected_vrs)}  anchors={n_anchors}  "
              f"OQs={n_oqs}  validation={parsed['validation']}")
        if missing:
            print(f"  [warn] {len(missing)} verses NOT placed (showing first "
                  f"5): {sorted(missing)[:5]}")
        if extra:
            print(f"  [warn] {len(extra)} extra vr_ids in output: "
                  f"{sorted(extra)[:5]}")
        print(f"  tokens in={usage.input_tokens} out={usage.output_tokens} "
              f"cache_r={getattr(usage, 'cache_read_input_tokens', 0) or 0}")

        # Write the per-sub-group mapping doc
        suffix = code.split("-")[-1]
        doc_path = os.path.join(
            OUT_DIR_DOCS,
            f"WA-M26-{suffix}-group-verse-mapping-v1-{today}.md"
        )
        write_mapping_doc(sg_data, parsed, doc_path)
        print(f"  wrote: {doc_path}")
        all_results.append((code, parsed))

    # Summaries doc
    summaries_path = os.path.join(
        OUT_DIR_DOCS,
        f"WA-M26-control-read-and-summaries-v1-{today}.md"
    )
    write_summaries_doc(all_results, summaries_path)
    print(f"\nwrote: {summaries_path}")

    # Raw results JSON
    raw_path = os.path.join(
        OUT_DIR_RESULTS,
        f"m26-phase456-results-{args.model}-{today}.json"
    )
    if "opus" in args.model:
        in_price, out_price = 15.0, 75.0
    elif "haiku" in args.model:
        in_price, out_price = 1.0, 5.0
    else:
        in_price, out_price = 3.0, 15.0
    cost = (in_tot / 1_000_000) * in_price + (out_tot / 1_000_000) * out_price

    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump({
            "meta": {
                "generated_at": now_iso(),
                "model": args.model,
                "effort": args.effort,
                "n_subgroups": len(all_results),
                "tokens": {
                    "input": in_tot, "output": out_tot,
                    "cache_read": cache_r_tot,
                    "estimated_cost_usd": round(cost, 4),
                },
            },
            "subgroups": {code: parsed for code, parsed in all_results},
        }, f, indent=2, ensure_ascii=False)
    print(f"wrote: {raw_path}")
    print()
    print(f"Total tokens — in: {in_tot:,} out: {out_tot:,} "
          f"cache_read: {cache_r_tot:,}")
    print(f"Estimated cost: ${cost:.4f}")
    print()
    print("Next step: researcher review. No DB writes performed.")
    print("After approval, apply via _apply_m15_phase7_v1_20260509.py "
          "(generalised for M26).")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
