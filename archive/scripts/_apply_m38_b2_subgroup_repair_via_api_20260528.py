"""M38 Salvation — Phase B B.2 sub-group coverage repair via Claude API.

The initial B.2 run produced 7 sub-groups but with coverage issues:
  - 46 vc_ids assigned to multiple sub-groups (need consolidation to one)
  - 15 vc_ids missing (need explicit assignment)
  - 1 vc_id spurious (not in cluster — drop)

This repair script:
  1. Reads the original B.2 design (sub-group definitions stay).
  2. Sends the AI a small repair prompt with:
     - The 7 sub-group definitions
     - The 15 missing verses with their Pass A meanings
     - The 46 duplicated vc_ids with their current multi-assignment + meanings
  3. AI returns: single sub-group assignment per affected vc_id.
  4. Writes a fixed mapping JSON + delta report.
"""
from __future__ import annotations
import json, os, sqlite3, sys, time
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

CLUSTER = "M38"
MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 8000
DB = "database/bible_research.db"
OUT_DIR = Path("Sessions/Session_Clusters/M38")
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
RAW_RESPONSE_PATH = OUT_DIR / "WA-M38-b2-api-raw-response-20260528.json"
FIXED_MAPPING_PATH = OUT_DIR / f"WA-M38-subgroup-mapping-v2-{DATE}.json"
REPAIR_LOG_PATH = OUT_DIR / f"WA-M38-b2-repair-log-v1-{DATE}.md"
REPAIR_RAW_PATH = OUT_DIR / f"WA-M38-b2-repair-raw-response-{DATE}.json"


SYSTEM_PROMPT = """You are Claude AI repairing a Phase B.2 sub-group design output for cluster M38 Salvation.

The original B.2 design produced 7 well-designed sub-groups but with coverage issues:
- Some vc_ids were assigned to MULTIPLE sub-groups (need consolidation to one)
- Some vc_ids were MISSING from the design (need explicit assignment)

YOUR TASK

For each vc_id presented (both DUPLICATES and MISSING), assign it to EXACTLY ONE sub-group based on the verse's Pass A meaning and keywords, matching it against the sub-group core descriptions provided.

DISCIPLINE

- Read each verse's Pass A meaning and keywords carefully.
- Match against the 7 sub-group core descriptions.
- For DUPLICATES: choose the SINGLE BEST sub-group (the one whose core description most directly maps the verse's primary inner-being content).
- For MISSING: assign to the most appropriate sub-group.
- No new sub-groups. No splits. No new BOUNDARY decisions. Just clean assignment.

OUTPUT FORMAT — strict JSON

{
  "assignments": [
    {"vc_id": <int>, "subgroup": "<M38-X>", "reasoning": "<1 short sentence>"},
    ...
  ]
}

Every vc_id from the input must appear in assignments exactly once. No prose outside the JSON.
"""


def main():
    raw = json.loads(RAW_RESPONSE_PATH.read_text(encoding="utf-8"))
    subgroups_info = {sg["subgroup_code"]: sg for sg in raw["subgroups"]}

    # Find duplicates and missing
    all_assignments = []
    for sg in raw["subgroups"]:
        for v in sg["verses"]:
            all_assignments.append((v, sg["subgroup_code"]))
    c = Counter(v for v, _ in all_assignments)
    dups = {vc: n for vc, n in c.items() if n > 1}

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    expected = set(r[0] for r in conn.execute("""
        SELECT vc.id FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id
        WHERE mt.cluster_code='M38' AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
          AND COALESCE(mt.delete_flagged,0)=0
    """))
    present = set(c.keys())
    missing = expected - present
    extra = present - expected

    print(f"Cluster expected: {len(expected)}")
    print(f"Currently in B.2 output: {len(present)}")
    print(f"Duplicates: {len(dups)}; Missing: {len(missing)}; Extra: {len(extra)}")

    # Build by_id for duplicate analysis
    by_id = {}
    for v, sg in all_assignments:
        by_id.setdefault(v, []).append(sg)

    # Fetch meanings for missing + duplicates
    target_ids = sorted(missing) + sorted(dups.keys())
    placeholders = ",".join("?" * len(target_ids))
    rows = list(conn.execute(f"""
        SELECT vc.id AS vc_id, vr.reference, vc.analysis_note, vc.keywords,
               mt.strongs_number, mt.transliteration
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE vc.id IN ({placeholders})
        ORDER BY vc.id
    """, target_ids))

    # Build prompt
    user_msg_parts = ["Sub-group definitions (7 sub-groups):\n"]
    for code in sorted(subgroups_info.keys()):
        sg = subgroups_info[code]
        user_msg_parts.append(f"\n**{code} — {sg['label']}**")
        user_msg_parts.append(f"  {sg['core_description']}")
        user_msg_parts.append("")

    user_msg_parts.append("\n=== VERSES TO ASSIGN ===\n")
    user_msg_parts.append(f"\nMISSING verses ({len(missing)}) — assign one sub-group each:\n")
    miss_set = set(missing)
    for r in rows:
        if r["vc_id"] in miss_set:
            kw = json.loads(r["keywords"]) if r["keywords"] else []
            user_msg_parts.append(f"- vc_id={r['vc_id']} {r['strongs_number']} {r['transliteration']} {r['reference']}")
            user_msg_parts.append(f"  meaning: {r['analysis_note']}")
            user_msg_parts.append(f"  kw: {kw}")

    user_msg_parts.append(f"\nDUPLICATED verses ({len(dups)}) — pick ONE sub-group:\n")
    for r in rows:
        if r["vc_id"] in dups:
            kw = json.loads(r["keywords"]) if r["keywords"] else []
            user_msg_parts.append(f"- vc_id={r['vc_id']} {r['strongs_number']} {r['transliteration']} {r['reference']} — currently in {by_id[r['vc_id']]}")
            user_msg_parts.append(f"  meaning: {r['analysis_note']}")
            user_msg_parts.append(f"  kw: {kw}")

    user_msg_parts.append("\nReturn the JSON now.")
    user_msg = "\n".join(user_msg_parts)

    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY not in env or .env", file=sys.stderr)
        sys.exit(1)

    print(f"\nCalling {MODEL} for repair...")
    client = anthropic.Anthropic()
    t0 = time.time()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=[{"type": "text", "text": SYSTEM_PROMPT,
                 "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_msg}],
    )
    text = resp.content[0].text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip("`").strip()
    data = json.loads(text)
    dt = time.time() - t0

    REPAIR_RAW_PATH.write_text(text, encoding="utf-8")

    # Build the fixed mapping
    assignments = data.get("assignments", [])
    repair_by_id = {a["vc_id"]: a["subgroup"] for a in assignments}

    # Start from current best-effort: take first sub-group for non-duplicate non-missing
    fixed_mapping = {}  # vc_id -> sg
    for v, sg in all_assignments:
        if v in expected and v not in dups and v not in miss_set:
            fixed_mapping[v] = sg
    # Apply repair assignments
    for vc, sg in repair_by_id.items():
        if vc in expected:
            fixed_mapping[vc] = sg

    # Final sanity check
    final_counts = Counter(fixed_mapping.values())
    missing_after = expected - set(fixed_mapping.keys())
    extra_after = set(fixed_mapping.keys()) - expected

    # Rebuild full design output with fixed verses arrays
    fixed_subgroups = []
    for sg_orig in raw["subgroups"]:
        code = sg_orig["subgroup_code"]
        new_verses = sorted([vc for vc, s in fixed_mapping.items() if s == code])
        fixed_subgroups.append({
            **{k: v for k, v in sg_orig.items() if k != "verses"},
            "verses": new_verses,
        })

    full_fixed = {
        "summary": raw.get("summary", "") + f"\n\n[Coverage repair v2 — 2026-05-28: resolved {len(repair_by_id)} ambiguous assignments. Final coverage: {len(fixed_mapping)} verses across {len(fixed_subgroups)} sub-groups.]",
        "subgroups": fixed_subgroups,
        "cross_subgroup_terms": raw.get("cross_subgroup_terms", []),
        "_repair_meta": {
            "original_duplicates": len(dups),
            "original_missing": len(missing),
            "original_extras": len(extra),
            "repaired_count": len(repair_by_id),
            "final_coverage": len(fixed_mapping),
            "final_distinct": len(set(fixed_mapping.keys())),
        },
    }
    FIXED_MAPPING_PATH.write_text(json.dumps(full_fixed, indent=2, ensure_ascii=False), encoding="utf-8")

    # Repair log
    log_lines = [
        f"# M38 B.2 sub-group repair log (v2)",
        f"",
        f"**Date:** 2026-05-28",
        f"**Trigger:** Initial B.2 output had coverage issues — 46 duplicates, 15 missing, 1 extra.",
        f"**Resolution:** Targeted API repair preserving the 7 sub-group design and assigning each affected vc_id to exactly one sub-group.",
        f"",
        f"## Coverage stats",
        f"",
        f"- Expected cluster vc_ids: {len(expected)}",
        f"- Final assigned vc_ids: {len(fixed_mapping)}",
        f"- Missing after repair: {len(missing_after)} {sorted(missing_after)}",
        f"- Extras after repair: {len(extra_after)} {sorted(extra_after)}",
        f"- Repair API call: {len(repair_by_id)} vc_id assignments returned",
        f"",
        f"## Final sub-group counts",
        f"",
    ]
    for sg in fixed_subgroups:
        n = len(sg["verses"])
        pct = (n / len(expected)) * 100
        log_lines.append(f"- **{sg['subgroup_code']}** — {sg['label']}: {n} verses ({pct:.1f}%)")
    log_lines.append("")
    log_lines.append(f"Sum: {sum(len(sg['verses']) for sg in fixed_subgroups)} ({'✓ matches' if sum(len(sg['verses']) for sg in fixed_subgroups) == len(expected) else '⚠ mismatch'})")
    log_lines.append("")
    log_lines.append("## API usage")
    log_lines.append(f"")
    log_lines.append(f"- Input: {resp.usage.input_tokens:,}")
    log_lines.append(f"- Output: {resp.usage.output_tokens:,}")
    log_lines.append(f"- Duration: {dt:.1f}s")
    REPAIR_LOG_PATH.write_text("\n".join(log_lines), encoding="utf-8")

    print(f"\n[done in {dt:.1f}s]")
    print(f"API tokens: input={resp.usage.input_tokens:,} output={resp.usage.output_tokens:,}")
    print(f"Repair assignments returned: {len(repair_by_id)}")
    print(f"Final coverage: {len(fixed_mapping)} / {len(expected)} expected")
    print(f"Missing after repair: {len(missing_after)}")
    print(f"Extras after repair: {len(extra_after)}")
    print(f"")
    print(f"Final sub-group counts:")
    for sg in fixed_subgroups:
        n = len(sg["verses"])
        pct = (n / len(expected)) * 100
        print(f"  {sg['subgroup_code']:8s} {n:4d} ({pct:5.1f}%) — {sg['label']}")
    print(f"\nFixed mapping: {FIXED_MAPPING_PATH}")
    print(f"Repair log:    {REPAIR_LOG_PATH}")


if __name__ == "__main__":
    main()
