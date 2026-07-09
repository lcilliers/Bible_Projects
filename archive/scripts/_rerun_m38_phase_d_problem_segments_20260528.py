"""Re-run 3 problem segments with explicit q_codes in the user message.

Affected:
  - char 1 seg4 (T6+T7) — 43 blocks instead of 44
  - char 5 seg1 (T0+T1) — 37 blocks instead of 36 (extra)
  - char 7 seg1 (T0+T1) — 35 blocks instead of 36
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
MAX_TOKENS = 16000
DB = "database/bible_research.db"
OUT_DIR = Path("Sessions/Session_Clusters/M38")
DATE = "20260528"

SEGMENTS_INFO = {
    "seg1": ["T0", "T1"],
    "seg2": ["T2", "T3"],
    "seg3": ["T4", "T5"],
    "seg4": ["T6", "T7"],
}

# Problem cases: (char_seq, seg_name, short_name_in_filename)
PROBLEMS = [
    (1, "seg4", "Eschatological-salvation-received-by-fai"),
    (5, "seg1", "Priestly-mediation-machinery-of-atonemen"),
    (7, "seg1", "Ransomed-identity-gratitude-and-memory"),
]


def fetch_characteristic(conn, char_seq):
    row = conn.execute("SELECT id, short_name, definition FROM characteristic WHERE cluster_code=? AND char_seq=? AND COALESCE(delete_flagged,0)=0", (CLUSTER, char_seq)).fetchone()
    return row


def fetch_evidence(conn, char_seq):
    sg = conn.execute("""
        SELECT cs.id, cs.subgroup_code, cs.label, cs.core_description
        FROM characteristic ch
        JOIN characteristic_subgroup csg ON csg.characteristic_id = ch.id
        JOIN cluster_subgroup cs ON cs.id = csg.cluster_subgroup_id
        WHERE ch.cluster_code='M38' AND ch.char_seq=?
          AND COALESCE(ch.delete_flagged,0)=0 AND COALESCE(csg.delete_flagged,0)=0 AND COALESCE(cs.delete_flagged,0)=0
    """, (char_seq,)).fetchone()
    verses = list(conn.execute("""
        SELECT vc.id AS vc_id, vr.reference, mt.strongs_number, mt.transliteration,
               vc.analysis_note, vc.keywords, vc.is_anchor,
               vcg.group_code, vcg.context_description
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
        WHERE vc.cluster_subgroup_id=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
        ORDER BY vcg.group_code, vr.book_id, vr.chapter, vr.verse_num
    """, (sg[0],)))
    return sg, [tuple(v) for v in verses]


def fetch_prompts(conn, tiers):
    placeholders = ",".join("?" * len(tiers))
    return list(conn.execute(f"""
        SELECT obs_id, question_code, tier, component_code, component_title, question_text, prompt_seq
        FROM wa_obs_question_catalogue
        WHERE tier IN ({placeholders}) AND COALESCE(deleted,0)=0
        ORDER BY tier, component_code, prompt_seq, obs_id
    """, tiers))


def build_system_prompt(char_seq, short_name, definition, sg, verses):
    parts = [
        f"You are Claude AI performing Phase D — analytical findings — for cluster M38 Salvation, characteristic {char_seq}: {short_name}. Per wa-sessionb-cluster-instruction-v3_0-20260527 §8.",
        "",
        f"CHARACTERISTIC {char_seq}: {short_name}",
        "",
        f"Definition: {definition}",
        "",
        f"SUB-GROUP {sg[1]} — {sg[2]} ({len(verses)} verses)",
        sg[3],
        "",
        "EVIDENCE BLOCK (all IB verses with Pass A meanings + keywords):",
        "",
    ]
    from collections import defaultdict
    by_vcg = defaultdict(list)
    for v in verses:
        vc_id, ref, st, tr, an, kw_json, ia, vcg_code, ctx = v
        by_vcg[vcg_code or "NO-VCG"].append(v)
    for vcg_code in sorted(by_vcg.keys()):
        members = by_vcg[vcg_code]
        ctx_desc = members[0][8] or ""
        parts.append(f"### {vcg_code} ({len(members)} verses)")
        if ctx_desc:
            parts.append(f"Context: {ctx_desc}")
        for vc_id, ref, st, tr, an, kw_json, ia, vcg_code, ctx in members:
            kw = json.loads(kw_json) if kw_json else []
            anchor = " [ANCHOR]" if ia else ""
            parts.append(f"- vc_id={vc_id}{anchor} {ref} ({st} {tr or ''})")
            parts.append(f"  meaning: {an}")
            parts.append(f"  kw: {kw}")
        parts.append("")
    parts.append("")
    parts.append("DISCIPLINE — PARSER-SAFE FORM")
    parts.append("")
    parts.append("For each prompt, produce a block in this exact form:")
    parts.append("")
    parts.append("**{q_code} — {component_title} — {question_text}**")
    parts.append("")
    parts.append("**[CHAR-{char_seq}]** {{E|S|G}} — {{finding_text}}")
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("CRITICAL: Use the q_code value EXACTLY as provided in the prompt list. Do NOT invent new codes. Do NOT renumber. The q_code value provided is the catalogue's question_code.")
    parts.append("")
    parts.append("DISCIPLINE — finding quality")
    parts.append("  - Cite specific verse references (e.g. \"Mat 1:21\") with brief content excerpts")
    parts.append("  - Use the actual Pass A meanings as the basis")
    parts.append("  - Refuse template-imposition: mark S (silent) or G (gap) honestly rather than forcing E")
    parts.append("  - Refuse integration-bias: if evidence is disjointed, name it that way")
    parts.append("")
    parts.append("OUTPUT FORMAT")
    parts.append("Markdown blocks only. No header, no preamble.")
    return "\n".join(parts)


def build_user_message(prompts, char_seq):
    parts = [
        f"Tier-pair: {len(prompts)} prompts to answer for characteristic {char_seq}.",
        "",
        "Use the EXACT q_code value below in each block header. Order: produce one block per prompt in the order given.",
        "",
        "=== PROMPTS ===",
        "",
    ]
    for p in prompts:
        obs_id, qcode, tier, ccode, ctitle, qtext, pseq = p
        parts.append(f"q_code: **{qcode}** (obs_id={obs_id})")
        parts.append(f"component_title: {ctitle}")
        parts.append(f"question_text: {qtext}")
        parts.append("")
    parts.append("=== END PROMPTS ===")
    parts.append("")
    parts.append(f"Produce {len(prompts)} blocks. Use each q_code EXACTLY as given. Each block starts with `**{{q_code}} — {{component_title}} — {{question_text}}**`.")
    return "\n".join(parts)


def main():
    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)
    conn = sqlite3.connect(DB)

    client = anthropic.Anthropic()

    for char_seq, seg_name, short in PROBLEMS:
        tiers = SEGMENTS_INFO[seg_name]
        print(f"\n=== char {char_seq} {seg_name} ({'+'.join(tiers)}) ===")
        char = fetch_characteristic(conn, char_seq)
        sg, verses = fetch_evidence(conn, char_seq)
        prompts = fetch_prompts(conn, tiers)
        print(f"  Prompts: {len(prompts)}")

        sys_prompt = build_system_prompt(char_seq, char[1], char[2], sg, verses)
        user_msg = build_user_message(prompts, char_seq)

        t0 = time.time()
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
        dt = time.time() - t0
        usage = final.usage
        print(f"  [{dt:.1f}s] in={usage.input_tokens:,} out={usage.output_tokens:,} cache_read={getattr(usage,'cache_read_input_tokens',0):,}")

        # Save (overwrite the existing seg file)
        out_path = OUT_DIR / f"WA-M38-phase-d-char{char_seq}-{short}-findings-{seg_name}-{'+'.join(tiers)}-v1-{DATE}.md"
        header = (
            f"# M38 Phase D — Char {char_seq} ({char[1]}) — {'+'.join(tiers)} findings (re-run with explicit q_codes)\n\n"
            f"**Cluster:** M38\n"
            f"**Characteristic:** {char[1]} (char_seq={char_seq})\n"
            f"**Tier-segment:** {'+'.join(tiers)} — {len(prompts)} prompts\n"
            f"**Authored:** {DATE} via Sonnet 4.6 API (re-run)\n\n"
            f"---\n\n"
        )
        out_path.write_text(header + text, encoding="utf-8")
        import re
        n_blocks = len(re.findall(r'^\*\*T\d+\.\d+\.\d+ —', text, re.MULTILINE))
        print(f"  blocks parsed: {n_blocks} (expected {len(prompts)})")
        print(f"  saved: {out_path.name}")


if __name__ == "__main__":
    main()
