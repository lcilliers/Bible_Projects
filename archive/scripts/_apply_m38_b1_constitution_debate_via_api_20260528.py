"""M38 Salvation — Phase B B.1 Constitution debate via Claude API.

Per v3_0 §6.1 — produces per-term STAYS / TRANSFERS-TO-{cluster} / BOUNDARY
verdicts with rationale rooted in specific Pass A meanings.

Inputs:
  - Sessions/Session_Clusters/M38/wa-cluster-M38-constitution-v1-20260528.md

Outputs (Sessions/Session_Clusters/M38/):
  - WA-M38-constitution-debate-v1-20260528.md       (human-readable debate)
  - WA-M38-constitution-debate-v1-20260528.json     (structured verdicts for validator)
  - WA-M38-b1-api-raw-response-20260528.json        (raw API response)
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
CONSTITUTION_PATH = OUT_DIR / "wa-cluster-M38-constitution-v1-20260528.md"
DEBATE_MD_PATH = OUT_DIR / f"WA-M38-constitution-debate-v1-{DATE}.md"
DEBATE_JSON_PATH = OUT_DIR / f"WA-M38-constitution-debate-v1-{DATE}.json"
RAW_PATH = OUT_DIR / f"WA-M38-b1-api-raw-response-{DATE}.json"


SYSTEM_PROMPT = """You are Claude AI performing Phase B B.1 — Constitution debate — for cluster M38 Salvation, per wa-sessionb-cluster-instruction-v3_0-20260527 §6.1.

YOUR TASK

For each of the 13 mti_terms in M38, produce a verdict:

  - STAYS — the term's meaning corpus aligns with M38's cluster characteristic. Optional cross-register flag if the meaning corpus also evidences relationship with another cluster's characteristic.
  - TRANSFERS-TO-{cluster_code} — the meaning corpus aligns with another cluster's characteristic AND no verse evidences relationship with M38's characteristic. Cite the verse-level relationship test (§6.1.5).
  - BOUNDARY — the meaning corpus is undecided and needs researcher decision. Must cite one of the three valid §6.1.4 reasons.

DISCIPLINE — verdict grounding

Every verdict must be grounded in specific Pass A meanings from §2 of the constitution report. Cite at least 2-3 verse references with brief meaning excerpts as evidence.

The verdict is formed from the meaning corpus in §2. The cross-term signals in §3 are observations; they inform but do not authorise verdicts.

DISCIPLINE — forbidden BOUNDARY grounds (§6.1.4)

BOUNDARY may NOT be assigned solely because:

  - The term's meaning corpus is predominantly horizontal (human-to-human) rather than vertical (God-directed)
  - The meanings describe sensory / material / circumstantial rather than overtly spiritual content
  - The meanings include morally-negative inner-being content
  - You would prefer the term not be in scope

Valid BOUNDARY reasons (must cite one):

  1. Cluster-membership undecided — borderline between this cluster's characteristic and another's; researcher decision needed
  2. Homonymic / polysemic spread — corpus covers two or more distinct registers; term may need sense-split treatment
  3. Supportive / qualifying register — meanings describe an enhancing/qualifying state without itself carrying a primary characteristic

DISCIPLINE — TRANSFERS verse-level relationship test (§6.1.5)

A TRANSFERS-TO-{cluster} verdict requires the verse-by-verse check:

  For each verse in the term's meaning corpus, ask: does this verse evidence ANY relationship with M38's characteristic? Relationship is broad — direct evidence, structural opposite, instrument-of-the-characteristic, response-to-the-characteristic, protective-against, produced-by, in-tension-with.

  If ANY verse evidences source-cluster relationship → STAYS with cross-register flag (naming primary destination + relationship).
  If NO verse evidences source-cluster relationship → TRANSFERS-TO-{cluster}.

DISCIPLINE — refuse template-imposition (researcher direction 2026-05-28)

The researcher has explicitly named integration-bias as a risk. If the 13 terms do not genuinely cohere into one cluster characteristic, say so. Do not force coherence. Specific guardrails:

  - The three apparent semantic registers (salvation / atonement / gift) may be one coherent characteristic OR three distinct ones. The verses decide, not the cluster name.
  - The "priest mediating" axis emerging from the keywords may be a distinct characteristic, an aspect of atonement, or evidence for cluster boundary issues. Be open to all three.
  - sōzō's sense-discrimination (eschatological vs physical vs healing-spiritual) may warrant BOUNDARY for polysemic spread.
  - Some terms may genuinely belong to other clusters (M11 Repentance, M31 Faith, M39 Blessing, M02 Anger structural-opposite, etc.).

Where you assess that something does not fit, name it precisely with verse evidence. The researcher will weigh BOUNDARY decisions; do not pre-resolve them by forcing STAYS.

OUTPUT FORMAT — strict JSON

Respond with exactly one JSON object with two top-level fields:

{
  "summary": "<one paragraph synthesising the overall verdict pattern: how many STAYS, TRANSFERS, BOUNDARY; whether the cluster as constituted coheres; what major findings emerged>",
  "verdicts": [
    {
      "strongs": "<Strongs number, e.g. G4982>",
      "transliteration": "<e.g. sōzō>",
      "gloss": "<e.g. to save>",
      "language": "<Greek|Hebrew>",
      "verdict": "STAYS" | "TRANSFERS-TO-Mxx" | "BOUNDARY",
      "cross_register_flag": "<for STAYS only; null if no flag. Format: 'Primary M38; cross-register relationship with Mxx — <brief description>'>",
      "boundary_reason": "<for BOUNDARY only; null otherwise. One of: 'cluster_membership_undecided' | 'homonymic_polysemic' | 'supportive_qualifying'>",
      "transfer_test": "<for TRANSFERS only; null otherwise. Must describe how the verse-level relationship test was satisfied — i.e., that no verse in the corpus evidences M38 relationship.>",
      "rationale": "<2-4 sentences explaining the verdict. Cite specific verse references and meaning excerpts. Plain English.>",
      "evidence_verses": [
        {"reference": "<verse ref>", "meaning_excerpt": "<short Pass A meaning excerpt>"},
        ...  (2-4 verses)
      ]
    },
    ...  (13 terms total)
  ]
}

No prose outside the JSON. No markdown fences. The output must be parseable as a single JSON object.
"""


def build_user_message(constitution_text: str) -> str:
    return f"""Below is the M38 Salvation constitution report (Phase B B.1 input per v3_0 §6.1).

Read the per-term meaning corpora in §2, the cross-term signals in §3, and the programme cluster catalogue in §4. Produce verdicts for all 13 terms per the system prompt's output format.

=== CONSTITUTION REPORT ===

{constitution_text}

=== END CONSTITUTION REPORT ===

Produce the JSON object now. No prose outside the JSON."""


def call_api(constitution_text: str) -> tuple[dict, dict, str]:
    client = anthropic.Anthropic()
    user_msg = build_user_message(constitution_text)
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=[
            {"type": "text", "text": SYSTEM_PROMPT,
             "cache_control": {"type": "ephemeral"}},
        ],
        messages=[{"role": "user", "content": user_msg}],
    )
    text = resp.content[0].text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip("`").strip()
    data = json.loads(text)
    usage = {
        "input_tokens": resp.usage.input_tokens,
        "output_tokens": resp.usage.output_tokens,
        "cache_creation": getattr(resp.usage, "cache_creation_input_tokens", 0),
        "cache_read": getattr(resp.usage, "cache_read_input_tokens", 0),
    }
    return data, usage, text


def write_debate_md(data: dict, path: Path, usage: dict) -> None:
    summary = data.get("summary", "")
    verdicts = data.get("verdicts", [])
    counts = {"STAYS": 0, "TRANSFERS": 0, "BOUNDARY": 0}
    for v in verdicts:
        ver = v.get("verdict", "")
        if ver == "STAYS":
            counts["STAYS"] += 1
        elif ver.startswith("TRANSFERS"):
            counts["TRANSFERS"] += 1
        elif ver == "BOUNDARY":
            counts["BOUNDARY"] += 1

    lines = [
        f"# M38 Salvation — Phase B B.1 Constitution Debate",
        "",
        f"**Date:** 2026-05-28",
        f"**Cluster:** M38 Salvation",
        f"**Source:** API call to Sonnet 4.6 over constitution report wa-cluster-M38-constitution-v1-20260528.md",
        f"**Instruction governing:** wa-sessionb-cluster-instruction-v3_0-20260527 §6.1",
        "",
        "## Decision summary",
        "",
        f"- STAYS: {counts['STAYS']}",
        f"- TRANSFERS: {counts['TRANSFERS']}",
        f"- BOUNDARY: {counts['BOUNDARY']}",
        f"- Total verdicts: {len(verdicts)}",
        "",
        "## Cluster-level summary",
        "",
        summary,
        "",
        "## Per-term verdicts",
        "",
    ]
    for v in verdicts:
        lines.append(f"### {v.get('strongs')} {v.get('transliteration')} — {v.get('gloss')} ({v.get('language')})")
        lines.append("")
        lines.append(f"**Verdict:** {v.get('verdict')}")
        if v.get("cross_register_flag"):
            lines.append(f"**Cross-register flag:** {v.get('cross_register_flag')}")
        if v.get("boundary_reason"):
            lines.append(f"**BOUNDARY reason:** {v.get('boundary_reason')}")
        if v.get("transfer_test"):
            lines.append(f"**Transfer verse-level test:** {v.get('transfer_test')}")
        lines.append("")
        lines.append(f"**Rationale:** {v.get('rationale', '')}")
        lines.append("")
        ev = v.get("evidence_verses", [])
        if ev:
            lines.append("**Evidence verses cited:**")
            lines.append("")
            for e in ev:
                lines.append(f"- {e.get('reference', '')} — {e.get('meaning_excerpt', '')}")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Verdict summary table")
    lines.append("")
    lines.append("| Strongs | Translit | Gloss | Verdict | Flag/reason |")
    lines.append("|---|---|---|---|---|")
    for v in verdicts:
        flag = v.get("cross_register_flag") or v.get("boundary_reason") or v.get("transfer_test") or ""
        flag = (flag[:80] + "…") if len(flag) > 80 else flag
        lines.append(f"| {v.get('strongs')} | {v.get('transliteration')} | {v.get('gloss')} | {v.get('verdict')} | {flag} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## API usage")
    lines.append("")
    lines.append(f"- Input: {usage['input_tokens']:,}")
    lines.append(f"- Output: {usage['output_tokens']:,}")
    lines.append(f"- Cache creation: {usage['cache_creation']:,}")
    lines.append(f"- Cache read: {usage['cache_read']:,}")
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    if not CONSTITUTION_PATH.exists():
        print(f"ERROR: Constitution report not found at {CONSTITUTION_PATH}", file=sys.stderr)
        sys.exit(1)

    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY not in env or .env", file=sys.stderr)
        sys.exit(1)

    constitution_text = CONSTITUTION_PATH.read_text(encoding="utf-8")
    print(f"Loaded constitution report: {len(constitution_text):,} chars")
    print(f"Calling {MODEL}...")
    t0 = time.time()
    try:
        data, usage, raw_text = call_api(constitution_text)
    except json.JSONDecodeError as e:
        print(f"ERROR: JSON parse failed — {e}", file=sys.stderr)
        sys.exit(2)
    dt = time.time() - t0

    DEBATE_JSON_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    RAW_PATH.write_text(raw_text, encoding="utf-8")
    write_debate_md(data, DEBATE_MD_PATH, usage)

    verdicts = data.get("verdicts", [])
    print(f"\n[done in {dt:.1f}s]")
    print(f"API tokens: input={usage['input_tokens']:,} output={usage['output_tokens']:,} "
          f"cache_create={usage['cache_creation']:,} cache_read={usage['cache_read']:,}")
    print(f"Verdicts: {len(verdicts)}")
    counts = {}
    for v in verdicts:
        ver = v.get("verdict", "?")
        counts[ver] = counts.get(ver, 0) + 1
    for ver, n in sorted(counts.items()):
        print(f"  {ver}: {n}")
    print(f"\nDebate MD:    {DEBATE_MD_PATH}")
    print(f"Debate JSON:  {DEBATE_JSON_PATH}")
    print(f"Raw response: {RAW_PATH}")


if __name__ == "__main__":
    main()
