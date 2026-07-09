"""Re-run M38 synthesis for problem tiers (T2, T3, T7) with explicit q_codes."""
from __future__ import annotations
import json, os, re, sqlite3, sys, time
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
OUT_DIR = Path("Sessions/Session_Clusters/M38")
DATE = "20260528"
MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 24000  # raised to avoid truncation
TIERS_TO_RERUN = ["T2", "T3", "T7"]


def fetch(conn, tier):
    prompts = list(conn.execute("""
        SELECT obs_id, question_code, tier, component_code, component_title, question_text, prompt_seq
        FROM wa_obs_question_catalogue
        WHERE tier=? AND COALESCE(deleted,0)=0
        ORDER BY tier, prompt_seq, obs_id
    """, (tier,)))
    obs_ids = [p[0] for p in prompts]
    ph = ",".join("?" * len(obs_ids))
    findings = list(conn.execute(f"""
        SELECT cf.obs_id, ch.char_seq, ch.short_name, cf.finding_text, cf.finding_status
        FROM cluster_finding cf
        JOIN characteristic ch ON ch.id = cf.characteristic_id
        WHERE cf.cluster_code='M38' AND cf.obs_id IN ({ph})
          AND cf.characteristic_id IS NOT NULL AND COALESCE(cf.delete_flagged,0)=0
        ORDER BY cf.obs_id, ch.char_seq
    """, obs_ids))
    by_obs = {}
    for r in findings:
        by_obs.setdefault(r[0], []).append(r)
    return prompts, by_obs


SYSTEM_PROMPT = """You are Claude AI performing Phase D Stage B — cluster synthesis — for cluster M38 Salvation.

For each prompt, read the 7 characteristics' findings (stacked) and author ONE cluster-scope finding examining what surfaces when the characteristics are compared. Do not restate per-char findings.

PARSER-SAFE FORM:

  **{q_code} — {component_title} — {question_text}**

  **[CLUSTER]** {E|S|G} — {synthesis_text}

  ---

Use the EXACT q_code provided. Keep each synthesis under 350 words. No header. Just blocks.
"""


def main():
    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: no API key")
        sys.exit(1)
    conn = sqlite3.connect(DB)
    client = anthropic.Anthropic()

    for tier in TIERS_TO_RERUN:
        prompts, by_obs = fetch(conn, tier)
        print(f"\n=== {tier} ({len(prompts)} prompts) ===")

        parts = [f"Tier {tier} — {len(prompts)} prompts. Use exact q_codes.", "", "=== PROMPTS ==="]
        for p in prompts:
            obs_id, qcode, t, ccode, ctitle, qtext, pseq = p
            parts.append("")
            parts.append(f"q_code: **{qcode}** (obs_id={obs_id})")
            parts.append(f"component_title: {ctitle}")
            parts.append(f"question_text: {qtext}")
            parts.append("")
            for fobs, char_seq, sn, ftext, fstatus in by_obs.get(obs_id, []):
                parts.append(f"  [CHAR-{char_seq} {sn} {fstatus}]: {(ftext or '')[:600]}")
            parts.append("---")
        parts.append("")
        parts.append(f"Produce {len(prompts)} **[CLUSTER]** blocks using EXACT q_code values.")

        t0 = time.time()
        chunks = []
        with client.messages.stream(
            model=MODEL, max_tokens=MAX_TOKENS,
            system=[{"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": "\n".join(parts)}],
        ) as stream:
            for tc in stream.text_stream:
                chunks.append(tc)
            final = stream.get_final_message()
        text = "".join(chunks).strip()
        dt = time.time() - t0
        print(f"  [{dt:.1f}s] in={final.usage.input_tokens:,} out={final.usage.output_tokens:,}")

        out_path = OUT_DIR / f"WA-M38-phase-d-cluster-synthesis-findings-{tier}-v1-{DATE}.md"
        header = (
            f"# M38 Phase D Stage B — cluster synthesis — {tier} findings (re-run)\n\n"
            f"**Tier:** {tier} — {len(prompts)} prompts\n\n---\n\n"
        )
        out_path.write_text(header + text, encoding="utf-8")
        n = len(re.findall(r'^\*\*T\d+\.\d+\.\d+ —', text, re.MULTILINE))
        print(f"  blocks: {n} (expected {len(prompts)})")


if __name__ == "__main__":
    main()
