"""M38 Salvation — Phase B B.3 VCG design via Claude API (staged per sub-group).

Per v3_0 §6.3 — for each sub-group, design Verse Context Groups (VCGs):
  - Cluster meanings into provisional VCGs with substantively similar inner-being content
  - Name each VCG with provisional_code, context_description
  - Designate ONE anchor verse per VCG
  - Verify sum per sub-group (§6.3.3 step 5)

Staged write-out: each sub-group processed sequentially; per-sub-group file written
to disk immediately; sum verified before next sub-group fires.

After all sub-groups: unified VCG creation JSON.
"""
from __future__ import annotations
import json, os, sqlite3, sys, time
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
MAX_TOKENS = 12000
DB = "database/bible_research.db"
OUT_DIR = Path("Sessions/Session_Clusters/M38")
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
MAPPING_PATH = OUT_DIR / "WA-M38-subgroup-mapping-v2-20260528.json"
UNIFIED_PATH = OUT_DIR / f"WA-M38-vcg-creation-v1-{DATE}.json"


SYSTEM_PROMPT_TEMPLATE = """You are Claude AI performing Phase B B.3 — VCG design — for cluster M38 Salvation, sub-group {subgroup_code} ({subgroup_label}), per wa-sessionb-cluster-instruction-v3_0-20260527 §6.3.

YOUR TASK

Read every verse-meaning in this sub-group. Cluster verses into Verse Context Groups (VCGs) — verses with substantively similar inner-being content within this sub-group's register.

CONSTRAINTS

- Read every verse. No sampling. No "representative members." No "rest follow the same pattern."
- VCGs cluster meanings by inner-being similarity within the sub-group's characteristic. Not by language, not by Strong's number, not by Testament — by what the verse evidences about the inner being.
- Each VCG must have ONE anchor verse — the verse that most directly and definitionally evidences the phenomenon the VCG names. Anchor must be one of the verses in the VCG.
- A typical sub-group has 2–7 VCGs depending on its size and internal diversity. Larger sub-groups (40+ verses) typically warrant more VCGs.
- Every vc_id in the input must appear in exactly one VCG. No duplicates, no omissions.
- Dual-membership is allowed but must be flagged explicitly (a verse genuinely belonging in two VCGs within the same sub-group).

VCG NAMING

- provisional_code: "{subgroup_code}-VCG-01", "{subgroup_code}-VCG-02", ... in numbered order
- context_description: one paragraph (3-6 sentences) describing the inner-being phenomenon the VCG names, drawn from the verses' meanings

DISCIPLINE — refuse template-imposition

Researcher direction 2026-05-28: integration-bias is a real risk. If the verses in this sub-group genuinely cluster around 5 distinct registers, name 5 VCGs. If they cluster around 2, name 2. Do not force more or fewer than the meaning evidence supports. If a single VCG contains 80% of the sub-group's verses with one outlier-VCG, name it that way honestly.

OUTPUT FORMAT — strict JSON

{{
  "subgroup_code": "{subgroup_code}",
  "subgroup_label": "{subgroup_label}",
  "verse_count": {verse_count},
  "vcgs": [
    {{
      "provisional_code": "{subgroup_code}-VCG-01",
      "context_description": "<one paragraph>",
      "verses": [<vc_id>, <vc_id>, ...],
      "anchor_vc_id": <int — must be in verses>
    }},
    ...
  ],
  "dual_memberships": [
    {{"vc_id": <int>, "primary": "{subgroup_code}-VCG-XX", "secondary": "{subgroup_code}-VCG-YY", "rationale": "<brief>"}}
  ]
}}

Confirm in your output structure that:
- Sum of len(vcgs[i].verses) equals {verse_count}
- Every anchor_vc_id is in its VCG's verses array
- No vc_id appears in two VCGs unless declared in dual_memberships

No prose outside the JSON.
"""


def build_user_message(subgroup_code: str, subgroup_label: str, core_description: str, verses_data: list[dict]) -> str:
    parts = [
        f"Sub-group {subgroup_code} — {subgroup_label}",
        f"",
        f"Sub-group core description (from B.2):",
        core_description,
        f"",
        f"All {len(verses_data)} verses in this sub-group (vc_id, reference, Strong's term, Pass A meaning, keywords):",
        f"",
    ]
    for v in verses_data:
        kw = json.loads(v["keywords"]) if v["keywords"] else []
        parts.append(f"vc_id={v['vc_id']} {v['reference']} ({v['strongs_number']} {v['transliteration'] or ''})")
        parts.append(f"  meaning: {v['analysis_note']}")
        parts.append(f"  kw: {kw}")
    parts.append("")
    parts.append("Design the VCGs now. Return the JSON.")
    return "\n".join(parts)


def fetch_verses_for_subgroup(conn, vc_ids: list[int]) -> list[dict]:
    if not vc_ids:
        return []
    placeholders = ",".join("?" * len(vc_ids))
    rows = list(conn.execute(f"""
        SELECT vc.id AS vc_id, vr.reference, vr.book_id, vr.chapter, vr.verse_num,
               vc.analysis_note, vc.keywords,
               mt.strongs_number, mt.transliteration, mt.gloss
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE vc.id IN ({placeholders})
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, vc_ids))
    return [dict(r) for r in rows]


def call_api(subgroup_code: str, subgroup_label: str, core_description: str, verses_data: list[dict]) -> tuple[dict, dict, str]:
    client = anthropic.Anthropic()
    sys_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        subgroup_code=subgroup_code,
        subgroup_label=subgroup_label,
        verse_count=len(verses_data),
    )
    user_msg = build_user_message(subgroup_code, subgroup_label, core_description, verses_data)
    chunks = []
    with client.messages.stream(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=[{"type": "text", "text": sys_prompt, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_msg}],
    ) as stream:
        for tc in stream.text_stream:
            chunks.append(tc)
        final = stream.get_final_message()
    text = "".join(chunks).strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip("`").strip()
    data = json.loads(text)
    usage = {
        "input_tokens": final.usage.input_tokens,
        "output_tokens": final.usage.output_tokens,
        "cache_creation": getattr(final.usage, "cache_creation_input_tokens", 0),
        "cache_read": getattr(final.usage, "cache_read_input_tokens", 0),
    }
    return data, usage, text


def write_subgroup_design_md(sg_code: str, sg_label: str, vcg_data: dict, expected_count: int, path: Path) -> tuple[bool, str]:
    vcgs = vcg_data.get("vcgs", [])
    all_verses = []
    for vcg in vcgs:
        all_verses.extend(vcg.get("verses", []))
    n_sum = len(all_verses)
    distinct = len(set(all_verses))
    duplicates = n_sum - distinct
    dual_declared = {(d.get("vc_id"), d.get("primary"), d.get("secondary")) for d in vcg_data.get("dual_memberships", [])}

    ok = n_sum == expected_count and distinct == expected_count

    lines = [
        f"# {sg_code} — {sg_label} — VCG Design",
        "",
        f"**Date:** 2026-05-28",
        f"**Phase:** B.3",
        f"**Expected verse count:** {expected_count}",
        f"**Sum of VCG members:** {n_sum}",
        f"**Distinct vc_ids:** {distinct}",
        f"**Duplicates in members:** {duplicates}",
        f"**Verification:** {'✓ matches' if ok else '⚠ DELTA'}",
        f"",
        f"## VCGs",
        f"",
    ]
    for vcg in vcgs:
        n = len(vcg.get("verses", []))
        lines.append(f"### {vcg.get('provisional_code')}")
        lines.append("")
        lines.append(f"- Verse count: {n}")
        lines.append(f"- Anchor vc_id: {vcg.get('anchor_vc_id')}")
        lines.append("")
        lines.append(f"**Context description:** {vcg.get('context_description', '')}")
        lines.append("")
        if n <= 12:
            lines.append(f"**Member vc_ids:** {vcg.get('verses', [])}")
            lines.append("")

    if vcg_data.get("dual_memberships"):
        lines.append("## Dual-membership flags")
        lines.append("")
        for d in vcg_data["dual_memberships"]:
            lines.append(f"- vc_id={d.get('vc_id')} primary={d.get('primary')} secondary={d.get('secondary')}: {d.get('rationale', '')}")
        lines.append("")

    msg = f"Verification: VCG member sums = {n_sum}, matches {sg_code} input count of {expected_count} {'✓' if ok else '⚠'}"
    lines.append(f"**{msg}**")

    path.write_text("\n".join(lines), encoding="utf-8")
    return ok, msg


def main():
    mapping = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
    subgroups = mapping.get("subgroups", [])

    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY not in env or .env", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    unified = {}
    total_usage = {"input_tokens": 0, "output_tokens": 0, "cache_creation": 0, "cache_read": 0}
    failures = []

    for sg in subgroups:
        code = sg["subgroup_code"]
        label = sg["label"]
        core_desc = sg["core_description"]
        vc_ids = sg["verses"]
        if not vc_ids:
            print(f"[{code}] skipped (no verses)")
            continue

        print(f"\n=== {code} ({len(vc_ids)} verses) — {label} ===")
        verses_data = fetch_verses_for_subgroup(conn, vc_ids)
        t0 = time.time()
        try:
            data, usage, raw_text = call_api(code, label, core_desc, verses_data)
        except Exception as e:
            print(f"  ERROR: {e}")
            failures.append((code, str(e)))
            continue
        dt = time.time() - t0
        for k in total_usage:
            total_usage[k] += usage[k]

        # Write per-sub-group design file
        design_path = OUT_DIR / f"WA-M38-{code}-vcg-design-v1-{DATE}.md"
        ok, msg = write_subgroup_design_md(code, label, data, len(vc_ids), design_path)
        print(f"  [{dt:.1f}s] in={usage['input_tokens']:,} out={usage['output_tokens']:,}")
        print(f"  {msg}")
        print(f"  VCGs: {len(data.get('vcgs', []))}; dual memberships: {len(data.get('dual_memberships', []))}")

        unified[code] = data

        if not ok:
            failures.append((code, msg))

    # Write unified JSON
    UNIFIED_PATH.write_text(json.dumps({
        "_meta": {
            "cluster_code": CLUSTER,
            "date": DATE,
            "subgroups_processed": list(unified.keys()),
            "total_usage": total_usage,
            "failures": failures,
        },
        "subgroups": unified,
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n=== B.3 COMPLETE ===")
    print(f"Sub-groups processed: {len(unified)} / {len(subgroups)}")
    print(f"Total API tokens: input={total_usage['input_tokens']:,} output={total_usage['output_tokens']:,}")
    print(f"Unified JSON: {UNIFIED_PATH}")
    if failures:
        print(f"\n⚠ {len(failures)} failures:")
        for code, msg in failures:
            print(f"  {code}: {msg}")
        sys.exit(2)


if __name__ == "__main__":
    main()
