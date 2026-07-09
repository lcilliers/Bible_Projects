"""Assign M01's 109 unassigned is_relevant verses to existing Phase 7 VCGs via Claude API.

After AI's Phase 7 design landed 838 of 951 is_relevant verses into VCGs across 8
sub-groups, 109 verses remained unassigned (context-overflow on the high-corpus
ya.re and cha.tat terms). Per v2_0 §2.7 (atomic per-row work via JSON template,
not chat synthesis), this script:

  1. Loads AI's VCG design JSON.
  2. Identifies the 109 missing is_relevant verses (still in their sub-group via
     verse_context.cluster_subgroup_id, but absent from the VCG creation JSON).
  3. For each verse: sends (meaning, list of candidate VCGs in its sub-group with
     their descriptions) to the Claude API; receives a chosen VCG provisional_code.
  4. Builds an assignment JSON that CC merges into the main creation JSON.

The 4 set-aside candidates AI flagged (Deu 32:27, Eze 16:43, Job 39:16, Job 25:2)
are excluded from the missing-verse set — they're handled separately by the Phase 7
apply script as is_relevant=0 + set_aside_reason.

Usage:
  python scripts/_assign_m01_missing_verses_to_vcgs_20260516.py [--batch-size 30] [--dry-run-fetch]

Outputs (under Sessions/Session_Clusters/M01/files vcg phase 7/):
  - WA-M01-vcg-missing-verse-assignments-v1-20260516.json
  - WA-M01-vcg-missing-verse-assignments-applied-v1-20260516.md
  - WA-M01-vcg-missing-verse-assignments-raw-responses-20260516.json
"""
from __future__ import annotations
import argparse, json, os, sys, time
from datetime import datetime, timezone
from pathlib import Path
import sqlite3

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Load .env for ANTHROPIC_API_KEY
env_path = Path(".env")
if env_path.exists():
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("ANTHROPIC_API_KEY=") and "ANTHROPIC_API_KEY" not in os.environ:
            os.environ["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip()
            break

import anthropic

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
MODEL = "claude-sonnet-4-6"
DEFAULT_BATCH_SIZE = 30

OUT_DIR = REPO / "Sessions" / "Session_Clusters" / "M01" / "files vcg phase 7"
JSON_IN = OUT_DIR / "WA-M01-vcg-creation-v1-20260516.json"
JSON_OUT = OUT_DIR / "WA-M01-vcg-missing-verse-assignments-v1-20260516.json"
LOG_OUT = OUT_DIR / "WA-M01-vcg-missing-verse-assignments-applied-v1-20260516.md"
RAW_OUT = OUT_DIR / "WA-M01-vcg-missing-verse-assignments-raw-responses-20260516.json"

SET_ASIDE_VC_IDS = {14968, 1846, 64529, 13958}


def build_system_prompt(subgroup_code: str, subgroup_label: str,
                         vcgs_in_subgroup: list[dict]) -> str:
    """Per-sub-group system prompt with the candidate VCG list and descriptions."""
    vcg_block = "\n\n".join(
        f"**{v['provisional_code']}** — {v['description'][:600]}"
        for v in vcgs_in_subgroup
    )
    return f"""You are Claude AI performing Phase 7 VCG-assignment classification for cluster M01, sub-group {subgroup_code} ({subgroup_label}), under wa-sessionb-cluster-instruction-v2_0-20260515 §10.

CONTEXT

You designed the {len(vcgs_in_subgroup)} VCGs for this sub-group in WA-M01-vcg-design-v1-20260516.md. A small number of high-corpus verses (ya.re, cha.tat, etc.) were unassigned due to context limits during the first pass. This focused pass closes the gap: for each verse below, choose the single best-fit VCG from the {len(vcgs_in_subgroup)} candidates.

CANDIDATE VCGs in {subgroup_code}:

{vcg_block}

YOUR TASK

For each verse below, return the provisional_code of the VCG whose description best matches the verse's meaning. One VCG per verse. If the verse's meaning fits multiple VCGs roughly equally, pick the closest match — Phase 7 design allows secondary dual-membership which CC will surface separately.

If no VCG fits well, choose `NEW` and propose a new VCG description (in the rationale). Use this sparingly; the existing VCGs should cover most cases.

OUTPUT FORMAT — strict JSON

Respond with exactly one JSON array. One object per verse, in the same order the verses were given. Each object must have:

  {{
    "vc_id": <integer — copy from input>,
    "reference": "<string — copy from input>",
    "vcg_code": "<provisional_code from the candidate list, or 'NEW'>",
    "rationale": "<one-line reason, max 200 chars>"
  }}

No prose, no preamble, no markdown fence. Just the JSON.
"""


def build_user_message(verses: list[dict]) -> str:
    parts = [f"Verses to assign ({len(verses)}):", ""]
    for v in verses:
        parts.append(f"---")
        parts.append(f"vc_id: {v['vc_id']}")
        parts.append(f"reference: {v['reference']}")
        parts.append(f"strongs: {v['strongs']}")
        parts.append(f"transliteration: {v['transliteration']}")
        parts.append(f"meaning: {v['meaning']}")
    parts.append("")
    parts.append("Return the JSON array now. No prose.")
    return "\n".join(parts)


def classify_batch(client, system_prompt, verses, max_retries=2):
    user = build_user_message(verses)
    last_err = None
    for attempt in range(max_retries + 1):
        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=4000,
                system=[
                    {"type": "text", "text": system_prompt,
                     "cache_control": {"type": "ephemeral"}},
                ],
                messages=[{"role": "user", "content": user}],
            )
            text = resp.content[0].text.strip()
            if text.startswith("```"):
                text = text.split("```", 2)[1]
                if text.startswith("json"):
                    text = text[4:]
                text = text.strip("`").strip()
            results = json.loads(text)
            if not isinstance(results, list):
                raise ValueError("not a JSON array")
            usage = {
                "input_tokens": resp.usage.input_tokens,
                "output_tokens": resp.usage.output_tokens,
                "cache_creation": getattr(resp.usage, "cache_creation_input_tokens", 0),
                "cache_read": getattr(resp.usage, "cache_read_input_tokens", 0),
            }
            return results, usage, text
        except (json.JSONDecodeError, ValueError) as e:
            last_err = e
            if attempt < max_retries:
                time.sleep(2); continue
            raise


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    ap.add_argument("--dry-run-fetch", action="store_true")
    args = ap.parse_args()

    # Load AI's creation JSON
    data = json.loads(JSON_IN.read_text(encoding="utf-8"))

    # Build {sg_code: [vcg dicts]}
    vcgs_by_sg: dict[str, list[dict]] = {sg: sg_data.get("vcgs", []) for sg, sg_data in data.items()}

    # Build {vc_id: (sg_code, vcg_provisional_code)} from JSON
    vc_to_vcg: dict[int, tuple[str, str]] = {}
    for sg, sg_data in data.items():
        for vcg in sg_data.get("vcgs", []):
            for v in vcg.get("verses", []):
                vc_to_vcg.setdefault(v, (sg, vcg["provisional_code"]))

    # Identify the 109 missing verses
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    missing = []
    for r in conn.execute("""
SELECT vc.id AS vc_id, vc.mti_term_id, vc.analysis_note,
       vr.reference, vr.book_id, vr.chapter, vr.verse_num,
       cs.subgroup_code,
       mt.strongs_number, mt.transliteration
FROM verse_context vc
JOIN mti_terms mt ON mt.id=vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id
LEFT JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
WHERE mt.cluster_code='M01' AND mt.status IN ('extracted','extracted_thin')
  AND COALESCE(mt.delete_flagged,0)=0 AND COALESCE(vc.delete_flagged,0)=0
  AND vc.is_relevant=1
ORDER BY cs.subgroup_code, vr.book_id, vr.chapter, vr.verse_num, vc.id
"""):
        if r["vc_id"] in SET_ASIDE_VC_IDS:
            continue
        if r["vc_id"] in vc_to_vcg:
            continue
        missing.append({
            "vc_id": r["vc_id"],
            "subgroup": r["subgroup_code"],
            "reference": r["reference"],
            "strongs": r["strongs_number"],
            "transliteration": r["transliteration"],
            "meaning": r["analysis_note"] or "(no meaning available)",
        })
    conn.close()

    print(f"Missing verses to assign: {len(missing)}")
    # Group by sub-group for processing
    by_sg: dict[str, list[dict]] = {}
    for v in missing:
        by_sg.setdefault(v["subgroup"], []).append(v)
    for sg, vs in by_sg.items():
        print(f"  {sg}: {len(vs)} verses")

    if args.dry_run_fetch:
        print("[--dry-run-fetch] No API calls made.")
        return 0

    client = anthropic.Anthropic()
    print(f"\nModel: {MODEL}\n")

    assignments: dict[int, dict] = {}
    raw_archive = []
    totals = {"input": 0, "output": 0, "cache_create": 0, "cache_read": 0}
    batch_num = 0
    total_batches = sum((len(vs) + args.batch_size - 1) // args.batch_size for vs in by_sg.values())

    for sg in sorted(by_sg.keys()):
        vs = by_sg[sg]
        if not vs:
            continue
        sg_label = next((s for s in [
            ("M01-A","Reverential Fear / Fear of God as Governing Orientation"),
            ("M01-B","Acute Fear and Alarm"),
            ("M01-C","Terror as Overwhelming Force"),
            ("M01-D","Dismay and Inner Collapse"),
            ("M01-E","Trembling / Fear Made Somatic"),
            ("M01-F","Anticipatory Dread and Anxiety"),
        ] if s[0]==sg), (sg, sg))[1]
        sys_prompt = build_system_prompt(sg, sg_label, vcgs_by_sg.get(sg, []))
        # Per-batch
        for i in range(0, len(vs), args.batch_size):
            batch_num += 1
            batch = vs[i : i + args.batch_size]
            print(f"[{batch_num}/{total_batches}] {sg} batch {len(batch)} verses ...", end=" ", flush=True)
            t0 = time.time()
            results, usage, raw = classify_batch(client, sys_prompt, batch)
            elapsed = time.time() - t0
            totals["input"] += usage["input_tokens"]
            totals["output"] += usage["output_tokens"]
            totals["cache_create"] += usage["cache_creation"]
            totals["cache_read"] += usage["cache_read"]
            for r in results:
                if r.get("vc_id"):
                    assignments[r["vc_id"]] = {
                        "vc_id": r["vc_id"],
                        "subgroup": sg,
                        "vcg_code": r.get("vcg_code"),
                        "rationale": r.get("rationale", ""),
                    }
            print(f"assigned {len(results)} ({elapsed:.1f}s, in={usage['input_tokens']} out={usage['output_tokens']} cache_read={usage['cache_read']})")
            raw_archive.append({"sg": sg, "batch": batch_num, "usage": usage, "response": raw})

    print(f"\nTotal usage: input={totals['input']:,} output={totals['output']:,} cache_read={totals['cache_read']:,}")

    JSON_OUT.write_text(json.dumps({
        "_meta": {
            "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "cluster": "M01",
            "source": "AI Phase 7 missing-verse assignment via Claude API (Sonnet 4.6)",
            "count": len(assignments),
            "usage": totals,
        },
        "assignments": list(assignments.values()),
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote: {JSON_OUT}")

    RAW_OUT.write_text(json.dumps(raw_archive, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Raw: {RAW_OUT}")

    # Summary log
    from collections import Counter
    vcg_count = Counter(a["vcg_code"] for a in assignments.values())
    lines = [
        f"# WA-M01-vcg-missing-verse-assignments-applied-v1-20260516",
        "",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"**Source:** Phase 7 missing-verse assignment via Claude API (Sonnet 4.6)",
        f"**Count:** {len(assignments)} verses assigned",
        "",
        "## Assignment distribution by VCG",
        "",
        "| VCG code | Count |",
        "|---|---:|",
    ]
    for code, n in sorted(vcg_count.items()):
        lines.append(f"| `{code}` | {n} |")
    new_count = vcg_count.get("NEW", 0)
    lines.append("")
    if new_count:
        lines.append(f"**Note:** {new_count} verses received `NEW` — AI proposed new VCGs rather than fitting into existing ones. These need review before apply. See raw responses for the AI's proposed descriptions.")
    else:
        lines.append("All verses fit into existing VCGs. No new VCGs proposed.")
    lines.append("")
    lines.append("## Per-sub-group distribution")
    lines.append("")
    sg_count = Counter(a["subgroup"] for a in assignments.values())
    for sg, n in sorted(sg_count.items()):
        lines.append(f"- {sg}: {n} verses")
    LOG_OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Log: {LOG_OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
