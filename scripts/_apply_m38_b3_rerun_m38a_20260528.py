"""Re-run M38-A B.3 VCG design specifically — original run failed JSON parse.

Same logic as the main B.3 script but isolated to M38-A and with larger output budget.
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

DB = "database/bible_research.db"
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
OUT_DIR = Path("Sessions/Session_Clusters/M38")
MAPPING_PATH = OUT_DIR / "WA-M38-subgroup-mapping-v2-20260528.json"

# Higher budget for the 121-verse sub-group
MAX_TOKENS = 24000
MODEL = "claude-sonnet-4-6"


SYSTEM_PROMPT = """You are Claude AI performing Phase B B.3 — VCG design — for cluster M38 Salvation, sub-group M38-A (Eschatological salvation received by faith), per wa-sessionb-cluster-instruction-v3_0-20260527 §6.3.

YOUR TASK

Read every verse-meaning in this sub-group. Cluster the 121 verses into Verse Context Groups (VCGs).

CONSTRAINTS

- Read every verse. No sampling.
- VCGs cluster meanings by inner-being similarity within this sub-group's characteristic (eschatological/spiritual salvation received by faith).
- Each VCG must have ONE anchor verse (must be in the VCG's verses array).
- For a 121-verse sub-group, expect 6 to 10 VCGs.
- Every vc_id in the input must appear in exactly one VCG. No duplicates (unless explicitly flagged as dual-membership).
- Keep descriptions tight (2-4 sentences per VCG context_description) so the JSON output stays compact.

OUTPUT FORMAT — strict JSON

{
  "subgroup_code": "M38-A",
  "subgroup_label": "Eschatological salvation received by faith",
  "verse_count": 121,
  "vcgs": [
    {
      "provisional_code": "M38-A-VCG-01",
      "context_description": "<2-4 sentences>",
      "verses": [<vc_id>, ...],
      "anchor_vc_id": <int>
    },
    ...
  ],
  "dual_memberships": [...]
}

CRITICAL: Sum of verse counts across VCGs MUST equal 121. Output valid JSON only. No prose outside the JSON. No markdown fences.
"""


def main():
    mapping = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
    sg_a = next((sg for sg in mapping["subgroups"] if sg["subgroup_code"] == "M38-A"), None)
    if not sg_a:
        print("ERROR: M38-A not found in mapping", file=sys.stderr)
        sys.exit(1)

    vc_ids = sg_a["verses"]
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    placeholders = ",".join("?" * len(vc_ids))
    rows = list(conn.execute(f"""
        SELECT vc.id AS vc_id, vr.reference, vr.book_id, vr.chapter, vr.verse_num,
               vc.analysis_note, vc.keywords,
               mt.strongs_number, mt.transliteration
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE vc.id IN ({placeholders})
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, vc_ids))

    parts = [
        f"Sub-group M38-A — {sg_a['label']}",
        "",
        f"Core description: {sg_a['core_description']}",
        "",
        f"All 121 verses (vc_id, reference, Strong's term, Pass A meaning, keywords):",
        "",
    ]
    for r in rows:
        kw = json.loads(r["keywords"]) if r["keywords"] else []
        parts.append(f"vc_id={r['vc_id']} {r['reference']} ({r['strongs_number']} {r['transliteration'] or ''})")
        parts.append(f"  meaning: {r['analysis_note']}")
        parts.append(f"  kw: {kw}")
    parts.append("")
    parts.append("Design 6-10 VCGs now. Return clean JSON. Sum must = 121.")
    user_msg = "\n".join(parts)

    print(f"Calling {MODEL} for M38-A (121 verses, max_tokens={MAX_TOKENS}, streaming)...")
    client = anthropic.Anthropic()
    t0 = time.time()
    chunks = []
    with client.messages.stream(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=[{"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_msg}],
    ) as stream:
        for tc in stream.text_stream:
            chunks.append(tc)
        final = stream.get_final_message()
    text = "".join(chunks).strip()
    dt = time.time() - t0

    raw_path = OUT_DIR / f"WA-M38-M38-A-rerun-raw-{DATE}.txt"
    raw_path.write_text(text, encoding="utf-8")

    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip("`").strip()

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"\nJSON parse error: {e}")
        print(f"Raw saved to {raw_path} for manual inspection")
        sys.exit(2)

    vcgs = data.get("vcgs", [])
    all_v = []
    for v in vcgs:
        all_v.extend(v.get("verses", []))
    distinct = set(all_v)
    expected_set = set(vc_ids)
    missing = expected_set - distinct
    extra = distinct - expected_set
    from collections import Counter
    dup_counter = Counter(all_v)
    undeclared_dups = [vc for vc, n in dup_counter.items() if n > 1
                       and vc not in {d.get("vc_id") for d in data.get("dual_memberships", [])}]

    print(f"\n[done {dt:.1f}s] in={final.usage.input_tokens:,} out={final.usage.output_tokens:,}")
    print(f"VCGs: {len(vcgs)}")
    print(f"sum: {len(all_v)} | distinct: {len(distinct)} | expected: 121")
    print(f"missing: {len(missing)} {sorted(missing)[:10]}")
    print(f"extras: {len(extra)} {sorted(extra)[:10]}")
    print(f"undeclared dups: {len(undeclared_dups)} {undeclared_dups[:10]}")

    # Save the data
    out_json_path = OUT_DIR / f"WA-M38-M38-A-vcg-rerun-{DATE}.json"
    out_json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSaved: {out_json_path}")


if __name__ == "__main__":
    main()
