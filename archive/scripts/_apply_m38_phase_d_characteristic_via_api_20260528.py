"""M38 Salvation — Phase D characteristic findings via Claude API.

Runs the full 189-prompt T0–T7 catalogue against ONE characteristic's evidence.
Segmented by tier-pair (T0+T1, T2+T3, T4+T5, T6+T7) to keep responses parser-safe.

Per v3_0 §8 — produces 189 cluster_finding rows per characteristic with
  characteristic_id={N}, cluster_subgroup_id=NULL, vcg_scope=NULL.

Usage:
    python scripts/_apply_m38_phase_d_characteristic_via_api_20260528.py --char-seq N
"""
from __future__ import annotations
import argparse, json, os, sqlite3, sys, time
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
DB = "database/bible_research.db"
OUT_DIR = Path("Sessions/Session_Clusters/M38")
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")

# Tier-pair segments per v3_0 §8.7
SEGMENTS = [
    ("seg1", ["T0", "T1"]),
    ("seg2", ["T2", "T3"]),
    ("seg3", ["T4", "T5"]),
    ("seg4", ["T6", "T7"]),
]


def fetch_characteristic(conn, char_seq: int) -> dict:
    row = conn.execute("""
        SELECT id, cluster_code, char_seq, short_name, definition
        FROM characteristic
        WHERE cluster_code=? AND char_seq=? AND COALESCE(delete_flagged,0)=0
    """, (CLUSTER, char_seq)).fetchone()
    if not row:
        raise SystemExit(f"No characteristic for {CLUSTER} char_seq={char_seq}")
    return dict(row)


def fetch_characteristic_evidence(conn, characteristic_id: int) -> tuple[dict, list[dict]]:
    """Get the sub-group + VCGs + verses + meanings for the characteristic."""
    sg = conn.execute("""
        SELECT cs.id, cs.subgroup_code, cs.label, cs.core_description
        FROM characteristic_subgroup csg
        JOIN cluster_subgroup cs ON cs.id = csg.cluster_subgroup_id
        WHERE csg.characteristic_id=? AND COALESCE(csg.delete_flagged,0)=0 AND COALESCE(cs.delete_flagged,0)=0
    """, (characteristic_id,)).fetchone()
    if not sg:
        raise SystemExit(f"No cluster_subgroup linked to characteristic_id={characteristic_id}")
    sg = dict(sg)

    # All IB verses in this sub-group, with VCG and meaning
    verses = list(conn.execute("""
        SELECT vc.id AS vc_id, vr.reference, vr.verse_text,
               mt.strongs_number, mt.transliteration, mt.gloss,
               vc.analysis_note, vc.keywords, vc.is_anchor,
               vcg.id AS vcg_id, vcg.group_code, vcg.context_description
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id AND COALESCE(vcg.delete_flagged,0)=0
        WHERE vc.cluster_subgroup_id=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
        ORDER BY vcg.group_code, vr.book_id, vr.chapter, vr.verse_num
    """, (sg["id"],)))
    return sg, [dict(v) for v in verses]


def fetch_catalogue_prompts(conn, tiers: list[str]) -> list[dict]:
    placeholders = ",".join("?" * len(tiers))
    rows = list(conn.execute(f"""
        SELECT obs_id, tier, component_code, component_title, question_text, prompt_seq
        FROM wa_obs_question_catalogue
        WHERE tier IN ({placeholders}) AND COALESCE(deleted,0)=0
        ORDER BY tier, prompt_seq, obs_id
    """, tiers))
    return [dict(r) for r in rows]


SYSTEM_PROMPT_TMPL = """You are Claude AI performing Phase D — analytical findings — for cluster {cluster} Salvation, characteristic {char_seq}: {short_name}. Per wa-sessionb-cluster-instruction-v3_0-20260527 §8.

YOUR TASK

Answer every prompt in this segment's tier-pair (T#-T#) for the named characteristic's evidence. Produce one finding per prompt in parser-safe markdown form.

CHARACTERISTIC

Characteristic id: {char_seq} — {short_name}

Definition:
{definition}

EVIDENCE BLOCK

{evidence_block}

DISCIPLINE — PARSER-SAFE FORM (mandatory per §8.4)

For each prompt:

  1. Write a prompt header line: `**T#.#.# — {{component_title}} — {{question_text}}**`
  2. Empty line
  3. Outcome marker line, exactly: `**[CHAR-{char_seq}]** {{E|S|G}} — {{finding_text}}`
     where:
       E = empirical finding — cite specific verse references and VCG codes
       S = silent — explicitly note absence of evidence in the corpus for this prompt
       G = gap — evidence is needed but unavailable; do not invent
  4. The finding text may be multi-paragraph but starts on the same line as the marker (no line break between marker and text).
  5. Empty line
  6. `---` separator on its own line

Repeat for every prompt in this segment.

DISCIPLINE — finding quality

  - Cite specific verse references (e.g. "Mat 1:21", "Isa 25:9") with brief content excerpts
  - Reference VCGs by their codes (M{char_seq_letter}-VCG-NN) when the evidence is concentrated in one VCG
  - Use the actual Pass A meanings as the basis — quote or paraphrase the inner-being content evidenced
  - Refuse template-imposition: if the prompt's question has no evidence in this characteristic's corpus, mark it S (silent) or G (gap) honestly rather than forcing an E
  - Reach for the same vocabulary across prompts (faith exercised, conscience cleansed, etc.) so findings can be aggregated downstream

DISCIPLINE — refuse integration-bias (researcher direction 2026-05-28)

If a prompt's evidence in this characteristic is genuinely partial or disjointed, say so. Do not force a coherent inner-being narrative the verses do not support. The verse meaning is the data and rules all analytics; observations however disjointed must be recorded.

OUTPUT FORMAT

A single markdown document containing ONLY the prompt blocks. No header. No self-check section (CC adds that). Just blocks separated by `---`.

Start with the first prompt block. No prose preamble.
"""


def build_evidence_block(sg: dict, verses: list[dict]) -> str:
    """Build the characteristic's evidence block (sub-group description + VCGs + verses)."""
    parts = []
    parts.append(f"Sub-group {sg['subgroup_code']} — {sg['label']} ({len(verses)} IB verses)")
    parts.append("")
    parts.append(f"Sub-group core description:")
    parts.append(sg["core_description"])
    parts.append("")
    # Group verses by VCG
    from collections import defaultdict
    by_vcg = defaultdict(list)
    for v in verses:
        by_vcg[v.get("group_code") or "NO-VCG"].append(v)
    for vcg_code in sorted(by_vcg.keys()):
        members = by_vcg[vcg_code]
        first = members[0]
        ctx_desc = first.get("context_description") or ""
        parts.append(f"### {vcg_code} ({len(members)} verses)")
        parts.append("")
        if ctx_desc:
            parts.append(f"Context: {ctx_desc}")
            parts.append("")
        for v in members:
            kw = json.loads(v["keywords"]) if v["keywords"] else []
            anchor = " [ANCHOR]" if v.get("is_anchor") else ""
            parts.append(f"- vc_id={v['vc_id']}{anchor} **{v['reference']}** ({v['strongs_number']} {v['transliteration'] or ''})")
            parts.append(f"  meaning: {v['analysis_note']}")
            parts.append(f"  kw: {kw}")
        parts.append("")
    return "\n".join(parts)


def build_user_message(prompts: list[dict], char_seq: int) -> str:
    parts = [
        f"Tier-pair: {prompts[0]['tier']}+{prompts[-1]['tier']} — {len(prompts)} prompts.",
        "",
        "Answer each prompt below in parser-safe form per the system prompt's discipline section.",
        "",
        "===  PROMPTS  ===",
        "",
    ]
    for p in prompts:
        parts.append(f"### {p['component_code']} — {p['component_title']}")
        parts.append(f"obs_id={p['obs_id']} tier={p['tier']}")
        parts.append(f"prompt: {p['question_text']}")
        parts.append("")
    parts.append("=== END PROMPTS ===")
    parts.append("")
    parts.append("Produce the findings now. One block per prompt. Use the exact prompt header form: `**T#.#.# — component_title — question_text**`. The question_text and component_title in the header should match the prompt's content. The component_code in the prompt header is `T#.#.#` derived from the tier + component (e.g. T0.1, T0.2). Use the catalogue's obs_id order.")
    parts.append("")
    parts.append("Important: use the component_code value as the T#.#.# code in the header. E.g. if component_code='T0.1' and prompt_seq=1, the header is `**T0.1.1 — Component Title — question text**`.")
    return "\n".join(parts)


def call_api(system_prompt: str, user_msg: str) -> tuple[str, dict]:
    client = anthropic.Anthropic()
    chunks = []
    with client.messages.stream(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=[{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_msg}],
    ) as stream:
        for tc in stream.text_stream:
            chunks.append(tc)
        final = stream.get_final_message()
    text = "".join(chunks).strip()
    usage = {
        "input_tokens": final.usage.input_tokens,
        "output_tokens": final.usage.output_tokens,
        "cache_creation": getattr(final.usage, "cache_creation_input_tokens", 0),
        "cache_read": getattr(final.usage, "cache_read_input_tokens", 0),
    }
    return text, usage


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--char-seq", type=int, required=True)
    ap.add_argument("--segments", default="all", help="all | seg1 | seg2 | seg3 | seg4")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    char = fetch_characteristic(conn, args.char_seq)
    sg, verses = fetch_characteristic_evidence(conn, char["id"])

    # Short name for filenames
    short = char["short_name"].replace(" ", "-").replace("/", "-")[:40]
    print(f"Characteristic {args.char_seq}: {char['short_name']} ({sg['subgroup_code']}, {len(verses)} verses)")
    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    evidence_block = build_evidence_block(sg, verses)
    system_prompt = SYSTEM_PROMPT_TMPL.format(
        cluster=CLUSTER,
        char_seq=args.char_seq,
        short_name=char["short_name"],
        definition=char["definition"],
        evidence_block=evidence_block,
        char_seq_letter=sg["subgroup_code"][-1],  # e.g. M38-A → A
    )
    print(f"System prompt size: {len(system_prompt):,} chars")
    print(f"Evidence block size: {len(evidence_block):,} chars")

    segments_to_run = [s for s in SEGMENTS if args.segments == "all" or s[0] == args.segments]
    total_usage = {"input_tokens": 0, "output_tokens": 0, "cache_creation": 0, "cache_read": 0}

    for seg_name, tiers in segments_to_run:
        print(f"\n=== {seg_name} ({'+'.join(tiers)}) ===")
        prompts = fetch_catalogue_prompts(conn, tiers)
        print(f"  Prompts: {len(prompts)}")
        user_msg = build_user_message(prompts, args.char_seq)

        t0 = time.time()
        try:
            text, usage = call_api(system_prompt, user_msg)
        except Exception as e:
            print(f"  ERROR: {e}")
            continue
        dt = time.time() - t0
        for k in total_usage:
            total_usage[k] += usage[k]
        print(f"  [{dt:.1f}s] in={usage['input_tokens']:,} out={usage['output_tokens']:,} cache_read={usage['cache_read']:,}")

        # Save segment file
        out_path = OUT_DIR / f"WA-{CLUSTER}-phase-d-char{args.char_seq}-{short}-findings-{seg_name}-{'+'.join(tiers)}-v1-{DATE}.md"
        # Prepend a header
        header = (
            f"# {CLUSTER} Phase D — Char {args.char_seq} ({char['short_name']}) — {'+'.join(tiers)} findings\n\n"
            f"**Cluster:** {CLUSTER}\n"
            f"**Characteristic:** {char['short_name']} (char_seq={args.char_seq})\n"
            f"**Tier-segment:** {'+'.join(tiers)} — {len(prompts)} prompts\n"
            f"**Authored:** {DATE} via Sonnet 4.6 API\n\n"
            f"---\n\n"
        )
        out_path.write_text(header + text, encoding="utf-8")
        # Quick count of prompt blocks
        import re
        n_blocks = len(re.findall(r'^\*\*T\d+\.\d+\.\d+ —', text, re.MULTILINE))
        print(f"  Prompt blocks parsed: {n_blocks} / expected {len(prompts)}")
        print(f"  Saved: {out_path.name}")

    print(f"\n=== TOTAL ===")
    print(f"Tokens: input={total_usage['input_tokens']:,} output={total_usage['output_tokens']:,} cache_read={total_usage['cache_read']:,}")


if __name__ == "__main__":
    main()
