"""M38 Salvation — Phase B B.2 Sub-group design via Claude API.

Per v3_0 §6.2 — produces sub-group design (codes, descriptions, verse-to-sub-group mapping)
honouring researcher-mandated BOUNDARY resolutions (sōzō sense-split, ka.phar register-split).
"""
from __future__ import annotations
import json, os, sys, time
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

env_path = Path(".env")
if env_path.exists():
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("ANTHROPIC_API_KEY=") and "ANTHROPIC_API_KEY" not in os.environ:
            os.environ["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip()
            break

import anthropic

CLUSTER = "M38"
MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 16000
OUT_DIR = Path("Sessions/Session_Clusters/M38")
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
B2_INPUT_PATH = OUT_DIR / "wa-cluster-M38-b2-input-v1-20260528.md"
DESIGN_MD_PATH = OUT_DIR / f"WA-M38-subgroup-design-v1-{DATE}.md"
MAPPING_JSON_PATH = OUT_DIR / f"WA-M38-subgroup-mapping-v1-{DATE}.json"
RAW_PATH = OUT_DIR / f"WA-M38-b2-api-raw-response-{DATE}.json"


SYSTEM_PROMPT = """You are Claude AI performing Phase B B.2 — Sub-group design — for cluster M38 Salvation, per wa-sessionb-cluster-instruction-v3_0-20260527 §6.2.

YOUR TASK

Design the sub-group structure for M38. Each sub-group represents a single characteristic — a single inner-being faculty/state the cluster expresses. Default: 1 sub-group : 1 characteristic.

The 13 STAYS terms with their 310 IB-relevant verses are provided in the B.2 input report. Read every verse-meaning. Group verses into sub-groups that carry distinct inner-being characteristics.

MANDATORY DESIGN CONSTRAINTS (per researcher direction)

The B.2 input report §3 documents two BOUNDARY resolutions that constrain your design:

1. **sōzō (G4982) — 93 verses across three discriminable senses must be operationally distinct in your sub-group design.**
   - Sense 1: eschatological/spiritual salvation (~57 verses)
   - Sense 2: physical rescue from mortal danger (~27 verses, inner content: terror, panic, urgent faith-cry)
   - Sense 3: healing with spiritual overtone (~9 verses)

   At minimum, sense 1 and sense 2 must NOT be in the same sub-group. Sense 3 may merge with sense 1 or sense 2 OR be its own sub-group — let the meaning evidence decide. sōzō verses may join sub-groups containing other terms' verses (e.g., sense 1 with soteria).

2. **ka.phar (H3722B) — 77 verses divide into two distinct registers that must be operationally distinct in your sub-group design.**
   - Register A: atoned-state inner-being (~45 verses, the person at the receiving end of atonement)
   - Register B: priestly-mediation machinery (~30 verses, what the priest does on behalf of others — ordination ritual, Day of Atonement mechanics)

   These two registers must be in different sub-groups.

OTHER DESIGN GUIDELINES

- Total cluster: 310 IB-relevant verses.
- No substantive sub-group may exceed 40% of total = 124 verses (volume hard gate, §6.2.7). If a single characteristic's natural verse volume exceeds 124, split it along a named axis (OT vs NT-distinctive, present vs eschatological, communal vs solitary, etc.) and document the split-axis.
- BOUNDARY sub-group: M38 has no BOUNDARY-verdict terms post-resolution, so no BOUNDARY sub-group is needed.
- Cross-register flags from B.1 may motivate sub-group naming (e.g., a "salvation-as-hope-anticipated" sub-group named around M38↔M18 Hope).
- Multi-faceted terms: a term's verses may span multiple sub-groups. That is expected. Record each verse's primary sub-group assignment.

DISCIPLINE — refuse template-imposition

The researcher has named integration-bias as a risk. Sub-groups must emerge from the meaning evidence, not from a presumed cluster-shape. Specific guardrails:

- Do NOT design sub-groups around the cluster name's three nouns ("salvation, redemption, deliverance") if the meanings show a different inner-life topology.
- Do NOT force every sub-group into a Christological/eschatological frame if some sub-groups are more naturally OT-narrative or wisdom-instructional.
- DO let unexpected axes from the keyword analytics inform sub-group design — particularly "priest mediating" (29 keywords), "faith exercised" (41), "conscience cleansed" (16), "will turning" (18), "hope sustained" (25).
- If a characteristic is more naturally about the inner-being faculty engaged (e.g., faith-as-reception-of-salvation) than about a salvation-mode, name it that way.

DELIVERABLES

Sub-group count: typically 4 to 8 sub-groups for a 310-verse cluster. Each sub-group should hold between 15 and 124 verses (40% ceiling). Each is named with:
- subgroup_code: "M38-A", "M38-B", "M38-C", ... in order of design
- label: short noun phrase naming the characteristic (3-7 words)
- core_description: one paragraph describing the inner-being characteristic the sub-group represents, drawn from the verse meanings
- evidence_basis: brief note on which terms contribute and which keywords cluster here

OUTPUT FORMAT — strict JSON

Respond with exactly one JSON object:

{
  "summary": "<one paragraph synthesising: how many sub-groups, what overall topology emerged, how sōzō's three senses landed, how ka.phar's two registers landed, what unexpected axes (if any) drove the design>",
  "subgroups": [
    {
      "subgroup_code": "M38-A",
      "label": "<3-7 word label naming the characteristic>",
      "core_description": "<one paragraph (~4-8 sentences) describing the inner-being characteristic this sub-group represents, drawn from the verse meanings>",
      "evidence_basis": "<one sentence: contributing terms and dominant keywords>",
      "split_axis": "<if this sub-group is part of a volume-split, name the axis; otherwise null>",
      "verses": [<vc_id>, <vc_id>, ...]
    },
    ...
  ],
  "cross_subgroup_terms": [
    {"strongs": "<e.g. G4982 sōzō>", "subgroups": ["M38-A", "M38-B", "M38-C"], "note": "<brief explanation of why this term's verses span multiple sub-groups>"}
  ]
}

Important:
- Every vc_id in the input (all 310) MUST appear in exactly one subgroup's verses array. No duplicates, no omissions.
- The verses array contains integer vc_ids, not references.
- Sub-group counts should sum to 310.
- The cross_subgroup_terms field flags terms whose verses span multiple sub-groups (sōzō and ka.phar at minimum, per the BOUNDARY resolutions).

No prose outside the JSON. No markdown fences. The output must be parseable as a single JSON object.
"""


def build_user_message(input_text: str) -> str:
    return f"""Below is the M38 B.2 input package per v3_0 §6.2.1. It contains:
- §1 cluster characteristic statement (post-B.1)
- §2 post-B.1 verdicts with cross-register flags
- §3 MANDATORY researcher direction on sōzō and ka.phar BOUNDARY resolutions
- §4 per-term meaning corpus (all 310 IB verses with vc_id, Pass A meaning, keywords)
- §5 keyword analytics report

Design the M38 sub-groups per the system prompt. Read every verse-meaning in §4 before designing.

=== B.2 INPUT PACKAGE ===

{input_text}

=== END B.2 INPUT PACKAGE ===

Produce the JSON now. No prose outside the JSON. Confirm in the summary field that you have read every verse-meaning and that the sub-group verse-counts sum to 310."""


def call_api(input_text: str) -> tuple[dict, dict, str]:
    client = anthropic.Anthropic()
    user_msg = build_user_message(input_text)
    # Use streaming for long responses (required by SDK for max_tokens >= ~16K)
    chunks = []
    usage_info = {"input_tokens": 0, "output_tokens": 0, "cache_creation": 0, "cache_read": 0}
    with client.messages.stream(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=[
            {"type": "text", "text": SYSTEM_PROMPT,
             "cache_control": {"type": "ephemeral"}},
        ],
        messages=[{"role": "user", "content": user_msg}],
    ) as stream:
        for text_chunk in stream.text_stream:
            chunks.append(text_chunk)
        final = stream.get_final_message()
    text = "".join(chunks).strip()
    usage_info["input_tokens"] = final.usage.input_tokens
    usage_info["output_tokens"] = final.usage.output_tokens
    usage_info["cache_creation"] = getattr(final.usage, "cache_creation_input_tokens", 0)
    usage_info["cache_read"] = getattr(final.usage, "cache_read_input_tokens", 0)
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip("`").strip()
    data = json.loads(text)
    return data, usage_info, text


def write_design_md(data: dict, path: Path, usage: dict, total_input_verses: int) -> None:
    subgroups = data.get("subgroups", [])
    total_assigned = sum(len(sg.get("verses", [])) for sg in subgroups)
    cross_terms = data.get("cross_subgroup_terms", [])

    lines = [
        f"# M38 Salvation — Phase B B.2 Sub-group Design",
        "",
        f"**Date:** 2026-05-28",
        f"**Cluster:** M38 Salvation",
        f"**Source:** API call to Sonnet 4.6 over B.2 input report",
        f"**Instruction:** wa-sessionb-cluster-instruction-v3_0-20260527 §6.2",
        "",
        "## Design summary",
        "",
        f"- Sub-groups designed: {len(subgroups)}",
        f"- Total verses assigned: {total_assigned} (input had {total_input_verses})",
        f"- Cross-subgroup terms: {len(cross_terms)}",
        "",
        "## Cluster-level synthesis",
        "",
        data.get("summary", ""),
        "",
        "## Sub-groups",
        "",
    ]
    for sg in subgroups:
        n = len(sg.get("verses", []))
        pct = (n / max(total_input_verses, 1)) * 100
        lines.append(f"### {sg.get('subgroup_code')} — {sg.get('label')}")
        lines.append("")
        lines.append(f"- Verses: {n} ({pct:.1f}% of cluster)")
        if sg.get('split_axis'):
            lines.append(f"- Split axis: {sg.get('split_axis')}")
        lines.append("")
        lines.append(f"**Core description:**")
        lines.append("")
        lines.append(sg.get('core_description', ''))
        lines.append("")
        lines.append(f"**Evidence basis:** {sg.get('evidence_basis', '')}")
        lines.append("")

    if cross_terms:
        lines.append("## Cross-subgroup terms")
        lines.append("")
        lines.append("| Term | Sub-groups spanned | Note |")
        lines.append("|---|---|---|")
        for ct in cross_terms:
            sgs = ", ".join(ct.get("subgroups", []))
            note = (ct.get("note", "") or "")[:200]
            lines.append(f"| {ct.get('strongs')} | {sgs} | {note} |")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Verse coverage check")
    lines.append("")
    if total_assigned == total_input_verses:
        lines.append(f"✓ All {total_input_verses} input verses accounted for in sub-group assignments.")
    else:
        lines.append(f"⚠ Total assigned ({total_assigned}) ≠ input count ({total_input_verses}). CC stage-gate validator will name the delta.")
    lines.append("")
    lines.append("## API usage")
    lines.append("")
    lines.append(f"- Input: {usage['input_tokens']:,}")
    lines.append(f"- Output: {usage['output_tokens']:,}")
    lines.append(f"- Cache creation: {usage['cache_creation']:,}")
    lines.append(f"- Cache read: {usage['cache_read']:,}")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_mapping_json(data: dict, path: Path) -> None:
    """Flatten subgroups into vc_id -> subgroup_code mapping for downstream apply."""
    mapping = {}
    for sg in data.get("subgroups", []):
        code = sg.get("subgroup_code")
        for vc_id in sg.get("verses", []):
            mapping[str(vc_id)] = code
    path.write_text(json.dumps({
        "_meta": {
            "cluster_code": "M38",
            "subgroups": [
                {"code": sg.get("subgroup_code"), "label": sg.get("label"),
                 "core_description": sg.get("core_description"), "split_axis": sg.get("split_axis"),
                 "evidence_basis": sg.get("evidence_basis"), "verse_count": len(sg.get("verses", []))}
                for sg in data.get("subgroups", [])
            ],
            "cross_subgroup_terms": data.get("cross_subgroup_terms", []),
        },
        "vc_to_subgroup": mapping,
    }, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    if not B2_INPUT_PATH.exists():
        print(f"ERROR: B.2 input not found at {B2_INPUT_PATH}", file=sys.stderr)
        sys.exit(1)

    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY not in env or .env", file=sys.stderr)
        sys.exit(1)

    input_text = B2_INPUT_PATH.read_text(encoding="utf-8")
    print(f"Loaded B.2 input: {len(input_text):,} chars")
    print(f"Calling {MODEL}...")
    t0 = time.time()
    try:
        data, usage, raw_text = call_api(input_text)
    except json.JSONDecodeError as e:
        print(f"ERROR: JSON parse failed — {e}", file=sys.stderr)
        sys.exit(2)
    dt = time.time() - t0

    MAPPING_JSON_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    RAW_PATH.write_text(raw_text, encoding="utf-8")

    # Count input verses for verification
    import sqlite3
    conn = sqlite3.connect("database/bible_research.db")
    n_input = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code='M38' AND COALESCE(mt.delete_flagged,0)=0
          AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """).fetchone()[0]

    write_design_md(data, DESIGN_MD_PATH, usage, n_input)
    write_mapping_json(data, MAPPING_JSON_PATH)

    subgroups = data.get("subgroups", [])
    total_assigned = sum(len(sg.get("verses", [])) for sg in subgroups)
    print(f"\n[done in {dt:.1f}s]")
    print(f"API tokens: input={usage['input_tokens']:,} output={usage['output_tokens']:,} "
          f"cache_create={usage['cache_creation']:,} cache_read={usage['cache_read']:,}")
    print(f"Sub-groups designed: {len(subgroups)}")
    for sg in subgroups:
        n = len(sg.get("verses", []))
        pct = (n / max(n_input, 1)) * 100
        print(f"  {sg.get('subgroup_code'):8s} {n:4d} verses ({pct:5.1f}%) — {sg.get('label')}")
    print(f"Total assigned: {total_assigned} / input {n_input} {'✓' if total_assigned == n_input else '⚠ DELTA'}")
    print(f"\nDesign MD:   {DESIGN_MD_PATH}")
    print(f"Mapping JSON: {MAPPING_JSON_PATH}")
    print(f"Raw response: {RAW_PATH}")


if __name__ == "__main__":
    main()
