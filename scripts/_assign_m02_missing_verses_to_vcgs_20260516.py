"""Assign M02 missing-verse VCGs via Claude API (atomic-per-row).

39 verses missing from AI's Phase 7 VCG creation JSON (37 in M02-B, 2 in M02-A).
Each verse must be assigned to one of the existing VCGs within its sub-group.

Modelled on _assign_m01_missing_verses_to_vcgs_20260516.py but cluster-specific.
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
MODEL = "claude-sonnet-4-6"
OUT_DIR = Path("Sessions/Session_Clusters/M02")
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
OUT_JSON = OUT_DIR / f"WA-M02-vcg-missing-verse-assignments-v1-{DATE}.json"
RAW_PATH = OUT_DIR / f"WA-M02-vcg-missing-verse-api-raw-{DATE}.json"

VCG_DESIGN = json.loads(
    (Path("Sessions/Session_Clusters/M02/WA-M02-vcg-creation-v1-20260516.json")).read_text(encoding="utf-8")
)

# Subgroup characteristic statements
SUBGROUP_DESCRIPTIONS = {
    "M02-A": "Divine Wrath as Judicial Force — Anger understood as settled, purposeful, and judicially operative — a divine inner disposition that responds to moral failure with binding consequence.",
    "M02-B": "Burning Rage and Inner Heat — Anger as inner fire/heat/kindling that rises and erupts; the dominant register is intensity, ignition, eruption.",
}


def build_system_prompt(sg_code: str) -> str:
    vcgs = VCG_DESIGN["subgroup_vcgs"][sg_code]["vcgs"]
    vcg_list_lines = []
    for v in vcgs:
        vcg_list_lines.append(f"- **{v['provisional_code']}**: {v.get('description','')}")
    vcg_block = "\n".join(vcg_list_lines)

    return f"""You are Claude AI completing M02 Phase 7 VCG assignment for verses missed in the main design pass.

CLUSTER M02 — Anger, Wrath and Indignation
SUB-GROUP {sg_code} — {SUBGROUP_DESCRIPTIONS[sg_code]}

EXISTING VCGs IN THIS SUB-GROUP

{vcg_block}

YOUR TASK

For each verse below, assign it to ONE of the existing VCGs above based on its Phase 2 meaning. The verse's term is in this sub-group; choose the VCG whose description best fits the verse's specific inner-being content.

Each verse gets exactly one VCG assignment. If a verse's meaning genuinely doesn't fit any existing VCG (rare), use `"vcg": "NEW-NEEDED"` and propose a one-line description in `proposed_description`.

OUTPUT FORMAT — strict JSON

Respond with exactly one JSON array. One object per verse, in input order:

  {{
    "vc_id": <integer — copy from input>,
    "reference": "<string — copy from input>",
    "vcg": "<one of the existing VCG codes>",
    "rationale": "<one-sentence reason naming the VCG match, max 200 chars>"
  }}

Do not include any text outside the JSON array. No prose, no preamble, no markdown fence.
"""


def fetch_missing_verses(conn) -> dict[str, list[dict]]:
    """Return {sg_code: [verse rows]} for verses in M02 is_relevant but missing from VCG JSON."""
    expected_vcs: set[int] = set()
    for sg_code, sg_data in VCG_DESIGN["subgroup_vcgs"].items():
        for vcg in sg_data.get("vcgs", []):
            expected_vcs.update(vcg.get("verses", []))

    rows = conn.execute("""
        SELECT vc.id AS vc_id, cs.subgroup_code,
               vr.reference, vr.verse_text, vr.target_word,
               mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
               vc.analysis_note
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        WHERE mt.cluster_code='M02' AND mt.status IN ('extracted','extracted_thin')
          AND COALESCE(mt.delete_flagged,0)=0 AND COALESCE(vc.delete_flagged,0)=0
          AND vc.is_relevant=1
        ORDER BY cs.subgroup_code, vr.book_id, vr.chapter, vr.verse_num
    """).fetchall()
    by_sg: dict[str, list[dict]] = {}
    for r in rows:
        if r["vc_id"] in expected_vcs:
            continue
        by_sg.setdefault(r["subgroup_code"], []).append({
            "vc_id": r["vc_id"], "reference": r["reference"],
            "verse_text": r["verse_text"] or "",
            "strongs": r["strongs_number"], "translit": r["transliteration"],
            "gloss": r["gloss"], "language": r["language"],
            "meaning": r["analysis_note"] or "",
        })
    return by_sg


def build_user_message(sg_code: str, verses: list[dict]) -> str:
    parts = [
        f"Sub-group: {sg_code}",
        f"Verses to assign: {len(verses)}",
        "",
        "Assign each verse to one of the existing VCGs in the system prompt. Output JSON array.",
        "",
    ]
    for v in verses:
        parts.append("---")
        parts.append(f"vc_id: {v['vc_id']}")
        parts.append(f"reference: {v['reference']}")
        parts.append(f"term: {v['strongs']} {v['translit']} — {v['gloss']} ({v['language']})")
        parts.append(f"meaning: {v['meaning']}")
        parts.append(f"verse_text: {v['verse_text']}")
    parts.append("")
    parts.append("Return the JSON array now. No prose.")
    return "\n".join(parts)


def call_api(client, sg_code: str, verses: list[dict], max_retries: int = 2) -> tuple[list[dict], dict, str]:
    system_prompt = build_system_prompt(sg_code)
    user_msg = build_user_message(sg_code, verses)
    for attempt in range(max_retries + 1):
        try:
            resp = client.messages.create(
                model=MODEL, max_tokens=12000,
                system=[{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}],
                messages=[{"role": "user", "content": user_msg}],
            )
            text = resp.content[0].text.strip()
            if text.startswith("```"):
                text = text.split("```", 2)[1]
                if text.startswith("json"): text = text[4:]
                text = text.strip("`").strip()
            results = json.loads(text)
            usage = {
                "input_tokens": resp.usage.input_tokens,
                "output_tokens": resp.usage.output_tokens,
                "cache_creation": getattr(resp.usage, "cache_creation_input_tokens", 0),
                "cache_read": getattr(resp.usage, "cache_read_input_tokens", 0),
            }
            return results, usage, text
        except (json.JSONDecodeError, ValueError):
            if attempt < max_retries:
                time.sleep(2)
                continue
            raise


def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    by_sg = fetch_missing_verses(conn)
    total = sum(len(v) for v in by_sg.values())
    print(f"M02 missing-verse assignment load:")
    for sg, vs in by_sg.items():
        print(f"  {sg}: {len(vs)} verses")
    print(f"  TOTAL: {total}")

    if total == 0:
        print("\nNo missing verses. Nothing to do.")
        return 0

    client = anthropic.Anthropic()
    print(f"\nModel: {MODEL}\n")

    all_assignments: dict[int, dict] = {}
    raw: list[dict] = []
    totals = {"input": 0, "output": 0, "cache_create": 0, "cache_read": 0}

    for sg_code, verses in by_sg.items():
        print(f"[{sg_code}] {len(verses)} verses ...", end=" ", flush=True)
        t0 = time.time()
        results, usage, raw_text = call_api(client, sg_code, verses)
        elapsed = time.time() - t0
        for r in results:
            all_assignments[r.get("vc_id")] = {
                "vc_id": r.get("vc_id"),
                "reference": r.get("reference"),
                "sg_code": sg_code,
                "vcg": r.get("vcg"),
                "rationale": r.get("rationale"),
            }
        totals["input"] += usage["input_tokens"]
        totals["output"] += usage["output_tokens"]
        totals["cache_create"] += usage["cache_creation"]
        totals["cache_read"] += usage["cache_read"]
        print(f"OK ({elapsed:.1f}s, in={usage['input_tokens']} out={usage['output_tokens']} cache_read={usage['cache_read']})")
        raw.append({"sg_code": sg_code, "usage": usage, "response": raw_text})

    print(f"\nTotal usage: input={totals['input']:,} output={totals['output']:,} cache_read={totals['cache_read']:,}")

    out = {
        "cluster_code": "M02",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "Claude API atomic per-row assignment (Sonnet 4.6)",
        "purpose": "Fill in 39 verses missing from AI's Phase 7 VCG creation pass",
        "total_assigned": len(all_assignments),
        "assignments": list(all_assignments.values()),
    }
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote: {OUT_JSON}")

    RAW_PATH.write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Raw responses: {RAW_PATH}")

    # Quick distribution summary
    from collections import Counter
    dist = Counter(a["vcg"] for a in all_assignments.values())
    print(f"\nAssignment distribution:")
    for vcg, n in sorted(dist.items()):
        print(f"  {vcg}: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
