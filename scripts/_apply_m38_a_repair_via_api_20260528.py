"""Repair M38-A VCG design (the 121-verse sub-group that failed JSON parsing).

Strategy:
  1. Parse the partial output (10 provisional VCGs with descriptions + verses)
  2. Strip invalid entries (non-integer vc_ids, vc_ids outside the sub-group)
  3. Find missing vc_ids (in expected set but not in any VCG)
  4. Find duplicates across VCGs
  5. API call: pass the 10 VCG descriptions + the affected vc_ids (missing + duplicated)
     and ask for SINGLE clean assignment per affected vc_id.
  6. Emit clean M38-A VCG JSON.
"""
from __future__ import annotations
import json, os, re, sqlite3, sys, time
from collections import Counter
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

DB = "database/bible_research.db"
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
OUT_DIR = Path("Sessions/Session_Clusters/M38")
MAPPING_PATH = OUT_DIR / "WA-M38-subgroup-mapping-v2-20260528.json"
RAW_PATH = OUT_DIR / "WA-M38-M38-A-rerun-raw-20260528.txt"
OUT_JSON_PATH = OUT_DIR / f"WA-M38-M38-A-vcg-repaired-{DATE}.json"

MODEL = "claude-sonnet-4-6"


def parse_partial_vcgs(text: str) -> list[dict]:
    """Extract VCG descriptions and verses arrays from partial output."""
    # Find each VCG block
    vcg_re = re.compile(
        r'"provisional_code"\s*:\s*"([^"]+)"\s*,\s*'
        r'"context_description"\s*:\s*"([^"]*)"\s*,\s*'
        r'"verses"\s*:\s*\[([^\]]*)\]\s*,\s*'
        r'"anchor_vc_id"\s*:\s*(\d+|null)',
        re.DOTALL
    )
    vcgs = []
    for m in vcg_re.finditer(text):
        code, desc, verses_str, anchor = m.groups()
        # Parse verses: keep only integers
        items = [s.strip() for s in verses_str.split(",")]
        verses = []
        for it in items:
            if it.isdigit():
                verses.append(int(it))
        anchor_id = int(anchor) if anchor.isdigit() else None
        vcgs.append({
            "provisional_code": code,
            "context_description": desc,
            "verses": verses,
            "anchor_vc_id": anchor_id,
        })
    return vcgs


def main():
    mapping = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
    sg_a = next(sg for sg in mapping["subgroups"] if sg["subgroup_code"] == "M38-A")
    expected_set = set(sg_a["verses"])
    print(f"M38-A expected: {len(expected_set)} verses")

    text = RAW_PATH.read_text(encoding="utf-8")
    vcgs = parse_partial_vcgs(text)
    print(f"Parsed {len(vcgs)} VCGs from partial output")
    for v in vcgs:
        print(f"  {v['provisional_code']}: {len(v['verses'])} verses, anchor={v['anchor_vc_id']}")

    # Coverage analysis (across all VCGs)
    all_v = []
    for v in vcgs:
        for vc in v["verses"]:
            if vc in expected_set:  # drop spurious
                all_v.append((vc, v["provisional_code"]))
    c = Counter(vc for vc, _ in all_v)
    distinct = set(c.keys())
    missing = expected_set - distinct
    duplicates = {vc: n for vc, n in c.items() if n > 1}
    print(f"\nAfter dropping spurious:")
    print(f"  distinct vc_ids in any VCG: {len(distinct)}")
    print(f"  missing from VCGs: {len(missing)}")
    print(f"  duplicates (in 2+ VCGs): {len(duplicates)}")

    if not missing and not duplicates:
        print("\nNo repair needed.")
        return

    # Build repair API call: pass VCG descriptions + affected verses
    affected = sorted(missing) + sorted(duplicates.keys())
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    placeholders = ",".join("?" * len(affected))
    rows = list(conn.execute(f"""
        SELECT vc.id AS vc_id, vr.reference, vc.analysis_note, vc.keywords,
               mt.strongs_number, mt.transliteration
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE vc.id IN ({placeholders})
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, affected))

    sys_prompt = """You are Claude AI repairing a Phase B.3 VCG design output for sub-group M38-A (Eschatological salvation received by faith). The original output had coverage gaps:
- Some vc_ids appeared in multiple VCGs (need consolidation to one)
- Some vc_ids were missing from all VCGs (need assignment)

For each presented vc_id, assign it to EXACTLY ONE existing VCG based on the verse's Pass A meaning. No new VCGs. No splits. Just clean assignment.

OUTPUT FORMAT (strict JSON):

{
  "assignments": [
    {"vc_id": <int>, "vcg": "M38-A-VCG-XX", "reasoning": "<1 short sentence>"},
    ...
  ]
}

Every affected vc_id must appear in assignments exactly once.
"""

    user_parts = ["Existing 10 VCG descriptions:\n"]
    for v in vcgs:
        user_parts.append(f"**{v['provisional_code']}** ({len(v['verses'])} current verses): {v['context_description']}\n")
    user_parts.append(f"\n=== Verses to repair-assign ({len(affected)}) ===\n")

    missing_set = set(missing)
    by_id = {}
    for vc, sg in all_v:
        by_id.setdefault(vc, []).append(sg)
    for r in rows:
        kw = json.loads(r["keywords"]) if r["keywords"] else []
        flag = "MISSING" if r["vc_id"] in missing_set else f"DUPLICATED in {by_id[r['vc_id']]}"
        user_parts.append(f"vc_id={r['vc_id']} ({flag}) {r['strongs_number']} {r['transliteration'] or ''} {r['reference']}")
        user_parts.append(f"  meaning: {r['analysis_note']}")
        user_parts.append(f"  kw: {kw}")

    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: API key not set", file=sys.stderr)
        sys.exit(1)

    print(f"\nCalling {MODEL} for repair...")
    client = anthropic.Anthropic()
    t0 = time.time()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        system=[{"type": "text", "text": sys_prompt}],
        messages=[{"role": "user", "content": "\n".join(user_parts)}],
    )
    text2 = resp.content[0].text.strip()
    if text2.startswith("```"):
        text2 = text2.split("```", 2)[1]
        if text2.startswith("json"):
            text2 = text2[4:]
        text2 = text2.strip("`").strip()
    data = json.loads(text2)
    dt = time.time() - t0
    print(f"[done {dt:.1f}s] in={resp.usage.input_tokens:,} out={resp.usage.output_tokens:,}")

    repair_assignments = {a["vc_id"]: a["vcg"] for a in data.get("assignments", [])}
    print(f"Repair assignments returned: {len(repair_assignments)}")

    # Apply repair: rebuild VCG members
    final_assign = {}  # vc_id -> vcg_code
    for v in vcgs:
        for vc in v["verses"]:
            if vc in expected_set and vc not in repair_assignments:
                # If vc was a non-duplicated non-missing, keep its assignment
                final_assign.setdefault(vc, v["provisional_code"])
    for vc, code in repair_assignments.items():
        if vc in expected_set:
            final_assign[vc] = code

    # Build final VCGs
    final_vcgs = []
    for v in vcgs:
        new_verses = sorted([vc for vc, code in final_assign.items() if code == v["provisional_code"]])
        anchor = v["anchor_vc_id"]
        if anchor not in new_verses and new_verses:
            anchor = new_verses[0]  # fallback
        final_vcgs.append({
            "provisional_code": v["provisional_code"],
            "context_description": v["context_description"],
            "verses": new_verses,
            "anchor_vc_id": anchor,
        })

    final_doc = {
        "subgroup_code": "M38-A",
        "subgroup_label": "Eschatological salvation received by faith",
        "verse_count": len(expected_set),
        "vcgs": final_vcgs,
        "dual_memberships": [],
        "_repair_meta": {
            "original_parsed_vcgs": len(vcgs),
            "missing_resolved": len(missing),
            "duplicates_resolved": len(duplicates),
            "final_distinct": len(final_assign),
        },
    }
    OUT_JSON_PATH.write_text(json.dumps(final_doc, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nFinal coverage: {len(final_assign)} / {len(expected_set)}")
    for v in final_vcgs:
        print(f"  {v['provisional_code']}: {len(v['verses'])} verses")
    print(f"\nSaved: {OUT_JSON_PATH}")


if __name__ == "__main__":
    main()
