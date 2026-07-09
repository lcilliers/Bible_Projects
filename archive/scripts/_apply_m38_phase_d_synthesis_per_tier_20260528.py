"""M38 Phase D Stage B — cluster synthesis findings, one tier at a time.

Previous 4-segment approach hit max_tokens output limit. Splitting per-tier
keeps each API call's output well within budget.

8 tier calls: T0 (12), T1 (24), T2 (31), T3 (33), T4 (24), T5 (21), T6 (24), T7 (20)
"""
from __future__ import annotations
import json, os, re, sqlite3, sys, time
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
TIERS = ["T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7"]


def fetch_synthesis_input(conn, tier):
    prompts = list(conn.execute("""
        SELECT obs_id, question_code, tier, component_code, component_title, question_text, prompt_seq
        FROM wa_obs_question_catalogue
        WHERE tier=? AND COALESCE(deleted,0)=0
        ORDER BY tier, prompt_seq, obs_id
    """, (tier,)))
    obs_ids = [p[0] for p in prompts]
    placeholders = ",".join("?" * len(obs_ids))
    findings = list(conn.execute(f"""
        SELECT cf.obs_id, ch.char_seq, ch.short_name, cf.finding_text, cf.finding_status
        FROM cluster_finding cf
        JOIN characteristic ch ON ch.id = cf.characteristic_id
        WHERE cf.cluster_code='M38' AND cf.obs_id IN ({placeholders})
          AND cf.characteristic_id IS NOT NULL AND COALESCE(cf.delete_flagged,0)=0
        ORDER BY cf.obs_id, ch.char_seq
    """, obs_ids))
    by_obs = {}
    for r in findings:
        by_obs.setdefault(r[0], []).append(r)
    return prompts, by_obs


SYSTEM_PROMPT = """You are Claude AI performing Phase D Stage B — cluster synthesis — for cluster M38 Salvation. Per wa-sessionb-cluster-instruction-v3_0-20260527 §8.6.

YOUR TASK

For each prompt in this tier, read the 7 characteristics' findings (stacked verbatim), then author ONE cluster-scope finding examining what surfaces when the characteristics are compared.

Do NOT restate per-char findings. The cluster-scope row is the integration across them — patterns, divergences, shared anchors, asymmetries.

CLUSTER M38 — SALVATION

7 characteristics:
  1. Eschatological salvation received by faith (M38-A)
  2. Physical rescue from mortal danger (M38-B)
  3. Healing wholeness through faith exercised (M38-C)
  4. Conscience cleansed through atonement received (M38-D)
  5. Priestly mediation machinery of atonement (M38-E)
  6. Salvation anticipated and hope sustained (M38-F)
  7. Ransomed identity gratitude and memory (M38-G)

PARSER-SAFE FORM (mandatory)

For each prompt:
  1. Header: `**{q_code} — {component_title} — {question_text}**`
     Use the EXACT q_code value as given in the prompt list.
  2. Empty line
  3. `**[CLUSTER]** {E|S|G} — {synthesis_text}`
  4. Empty line
  5. `---` separator

DISCIPLINE — synthesis quality

  - Name the pattern across characteristics, not within one
  - Compare/contrast: where do characteristics converge? where do they diverge?
  - Surface shared verse anchors that appear in multiple characteristics
  - Surface structural asymmetries (e.g., divine vs creaturely; OT vs NT)
  - Refuse template-imposition: if 5 of 7 characteristics say one thing and 2 contradict, name the partition honestly
  - Synthesis text 200-400 words per prompt is typical; do not exceed 500 words

OUTPUT FORMAT

Markdown blocks only. No header, no preamble.
"""


def build_user_message(prompts, findings_by_obs):
    parts = [
        f"Tier {prompts[0][2]} — {len(prompts)} prompts.",
        "",
        "For each prompt below: read the 7 stacked characteristic findings, then author one **[CLUSTER]** synthesis block. Use the q_code value EXACTLY as given.",
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
        for f_obs, char_seq, sn, ftext, fstatus in findings_by_obs.get(obs_id, []):
            parts.append(f"  [CHAR-{char_seq} {sn} status={fstatus}] {(ftext or '')[:800]}")
        parts.append("")
        parts.append("---")
        parts.append("")
    parts.append("=== END PROMPTS ===")
    parts.append("")
    parts.append(f"Produce {len(prompts)} **[CLUSTER]** blocks. Use exact q_code values.")
    return "\n".join(parts)


def main():
    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)
    conn = sqlite3.connect(DB)
    client = anthropic.Anthropic()
    total_usage = {"input_tokens": 0, "output_tokens": 0, "cache_read": 0}

    for tier in TIERS:
        prompts, by_obs = fetch_synthesis_input(conn, tier)
        print(f"\n=== synthesis {tier} ({len(prompts)} prompts) ===")
        user_msg = build_user_message(prompts, by_obs)
        print(f"  user msg: {len(user_msg):,} chars")

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
        u = final.usage
        total_usage["input_tokens"] += u.input_tokens
        total_usage["output_tokens"] += u.output_tokens
        total_usage["cache_read"] += getattr(u, "cache_read_input_tokens", 0)
        print(f"  [{dt:.1f}s] in={u.input_tokens:,} out={u.output_tokens:,} cache_read={getattr(u,'cache_read_input_tokens',0):,}")

        out_path = OUT_DIR / f"WA-M38-phase-d-cluster-synthesis-findings-{tier}-v1-{DATE}.md"
        header = (
            f"# M38 Phase D Stage B — cluster synthesis — {tier} findings\n\n"
            f"**Cluster:** M38\n**Tier:** {tier} — {len(prompts)} prompts\n"
            f"**Authored:** {DATE} via Sonnet 4.6 API\n\n---\n\n"
        )
        out_path.write_text(header + text, encoding="utf-8")
        n_blocks = len(re.findall(r'^\*\*T\d+\.\d+\.\d+ —', text, re.MULTILINE))
        print(f"  blocks parsed: {n_blocks} / expected {len(prompts)}")

    print(f"\nTotal: in={total_usage['input_tokens']:,} out={total_usage['output_tokens']:,} cache_read={total_usage['cache_read']:,}")


if __name__ == "__main__":
    main()
