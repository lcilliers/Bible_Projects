"""M38 Phase D Stage B — cluster synthesis findings via Claude API.

Per v3_0 §8.6 — for each of the 189 catalogue prompts, read all 7 characteristics'
findings stacked, then author ONE cluster-scope finding examining what surfaces
when the characteristics are compared.

Output: 189 cluster_finding rows with characteristic_id=NULL,
finding_status='cluster_synthesis'.

Segmented by tier-pair like Stage A.
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

SEGMENTS = [
    ("seg1", ["T0", "T1"]),
    ("seg2", ["T2", "T3"]),
    ("seg3", ["T4", "T5"]),
    ("seg4", ["T6", "T7"]),
]


def fetch_synthesis_input(conn, tiers: list[str]) -> tuple[list[dict], dict[int, list[dict]]]:
    """For each prompt in the tier-pair, gather the 7 characteristics' findings."""
    placeholders = ",".join("?" * len(tiers))
    prompts = list(conn.execute(f"""
        SELECT obs_id, tier, component_code, component_title, question_text, prompt_seq
        FROM wa_obs_question_catalogue
        WHERE tier IN ({placeholders}) AND COALESCE(deleted,0)=0
        ORDER BY tier, prompt_seq, obs_id
    """, tiers))
    prompts = [dict(p) for p in prompts]

    obs_ids = [p["obs_id"] for p in prompts]
    placeholders2 = ",".join("?" * len(obs_ids))
    findings_rows = list(conn.execute(f"""
        SELECT cf.obs_id, cf.characteristic_id, ch.char_seq, ch.short_name,
               cf.finding_text, cf.finding_status
        FROM cluster_finding cf
        JOIN characteristic ch ON ch.id = cf.characteristic_id
        WHERE cf.cluster_code='M38'
          AND cf.obs_id IN ({placeholders2})
          AND cf.characteristic_id IS NOT NULL
          AND COALESCE(cf.delete_flagged,0)=0
        ORDER BY cf.obs_id, ch.char_seq
    """, obs_ids))
    findings_by_obs: dict[int, list[dict]] = {}
    for r in findings_rows:
        findings_by_obs.setdefault(r["obs_id"], []).append(dict(r))

    return prompts, findings_by_obs


SYSTEM_PROMPT = """You are Claude AI performing Phase D Stage B — cluster synthesis — for cluster M38 Salvation. Per wa-sessionb-cluster-instruction-v3_0-20260527 §8.6.

YOUR TASK

For each prompt in this tier-pair segment, read the 7 characteristics' findings (stacked verbatim from cluster_finding). Author ONE cluster-scope finding examining what surfaces when the characteristics are compared.

Do NOT restate per-char findings. The cluster-scope row is the integration across them — patterns, divergences, shared anchors, asymmetries.

CLUSTER M38 — SALVATION

7 characteristics under v3_0:
  1. Eschatological salvation received by faith (M38-A, 121 verses)
  2. Physical rescue from mortal danger (M38-B, 15 verses)
  3. Healing wholeness through faith exercised (M38-C, 12 verses)
  4. Conscience cleansed through atonement received (M38-D, 39 verses)
  5. Priestly mediation machinery of atonement (M38-E, 44 verses)
  6. Salvation anticipated and hope sustained (M38-F, 37 verses)
  7. Ransomed identity gratitude and memory (M38-G, 42 verses)

DISCIPLINE — PARSER-SAFE FORM (mandatory)

For each prompt:

  1. Prompt header: `**T#.#.# — {component_title} — {question_text}**`
  2. Empty line
  3. `**[CLUSTER]** {E|S|G} — {synthesis_text}`
     - E = empirical synthesis finding — name the cross-characteristic pattern
     - S = silent — the prompt's question genuinely has no cross-char synthesis available
     - G = gap — synthesis needed but evidence stack does not support it
  4. Empty line
  5. `---` separator

DISCIPLINE — synthesis quality

  - Name the pattern across characteristics, not within one
  - Compare/contrast: where do characteristics converge? where do they diverge?
  - Surface shared verse anchors that appear in multiple characteristics
  - Surface structural asymmetries (e.g., divine vs creaturely; OT vs NT; primary vs secondary)
  - Refuse template-imposition: if 5 of 7 characteristics say one thing and 2 contradict, name the partition honestly rather than smoothing to consensus
  - Refer to characteristics by their short names or as M38-A/B/C/D/E/F/G

DISCIPLINE — refuse integration-bias (researcher direction 2026-05-28)

If the 7 characteristics' findings on a prompt do not synthesise into a unified picture, say so. The cluster-scope finding can legitimately be: "The characteristics divide along axis X; M38-A/D/F engage prompt Y in mode Z; M38-B/C/E do not engage at all." Honesty over forced coherence.

OUTPUT FORMAT

Markdown blocks only. No header, no preamble. Just blocks separated by `---`.
"""


def build_user_message(prompts: list[dict], findings_by_obs: dict[int, list[dict]]) -> str:
    parts = [
        f"Tier-pair segment — {len(prompts)} prompts.",
        "",
        "For each prompt below: read the 7 stacked characteristic findings, then author one **[CLUSTER]** synthesis block.",
        "",
        "=== PROMPTS WITH STACKED CHAR FINDINGS ===",
        "",
    ]
    for p in prompts:
        parts.append(f"### Prompt {p['component_code']}.{p['prompt_seq']} (obs_id={p['obs_id']}, tier={p['tier']})")
        parts.append(f"Component title: {p['component_title']}")
        parts.append(f"Question: {p['question_text']}")
        parts.append("")
        char_findings = findings_by_obs.get(p["obs_id"], [])
        if char_findings:
            for cf in char_findings:
                parts.append(f"**[CHAR-{cf['char_seq']}] ({cf['short_name']}) — status={cf['finding_status']}:**")
                parts.append(cf["finding_text"][:1200])  # cap length
                parts.append("")
        else:
            parts.append("(no characteristic findings on file for this prompt)")
            parts.append("")
        parts.append("---")
        parts.append("")
    parts.append("=== END PROMPTS ===")
    parts.append("")
    parts.append("Produce one **[CLUSTER]** synthesis block per prompt. Use the exact prompt header form. Order doesn't matter.")
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
    return text, {
        "input_tokens": final.usage.input_tokens,
        "output_tokens": final.usage.output_tokens,
        "cache_creation": getattr(final.usage, "cache_creation_input_tokens", 0),
        "cache_read": getattr(final.usage, "cache_read_input_tokens", 0),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--segments", default="all")
    args = ap.parse_args()

    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Pre-check: all 7 chars have 189 findings loaded
    n_findings = conn.execute("""
        SELECT COUNT(*) FROM cluster_finding cf
        WHERE cf.cluster_code='M38' AND cf.characteristic_id IS NOT NULL
          AND COALESCE(cf.delete_flagged,0)=0
    """).fetchone()[0]
    print(f"Pre-check: M38 has {n_findings} characteristic-scope findings (expected 1323 = 7×189)")
    if n_findings < 7 * 189:
        print(f"ABORT: synthesis requires all 7 characteristics loaded first")
        sys.exit(2)

    segments_to_run = [s for s in SEGMENTS if args.segments == "all" or s[0] == args.segments]
    total_usage = {"input_tokens": 0, "output_tokens": 0, "cache_creation": 0, "cache_read": 0}

    import re
    for seg_name, tiers in segments_to_run:
        print(f"\n=== synthesis {seg_name} ({'+'.join(tiers)}) ===")
        prompts, findings_by_obs = fetch_synthesis_input(conn, tiers)
        print(f"  Prompts: {len(prompts)}")

        user_msg = build_user_message(prompts, findings_by_obs)
        print(f"  User msg size: {len(user_msg):,} chars")

        t0 = time.time()
        try:
            text, usage = call_api(SYSTEM_PROMPT, user_msg)
        except Exception as e:
            print(f"  ERROR: {e}")
            continue
        dt = time.time() - t0
        for k in total_usage:
            total_usage[k] += usage[k]
        print(f"  [{dt:.1f}s] in={usage['input_tokens']:,} out={usage['output_tokens']:,} cache_read={usage['cache_read']:,}")

        out_path = OUT_DIR / f"WA-M38-phase-d-cluster-synthesis-findings-{seg_name}-{'+'.join(tiers)}-v1-{DATE}.md"
        header = (
            f"# M38 Phase D Stage B — cluster synthesis — {'+'.join(tiers)} findings\n\n"
            f"**Cluster:** M38\n"
            f"**Scope:** CLUSTER (synthesis of 7 characteristics' findings)\n"
            f"**Tier-segment:** {'+'.join(tiers)} — {len(prompts)} prompts\n"
            f"**Authored:** {DATE} via Sonnet 4.6 API\n\n"
            f"---\n\n"
        )
        out_path.write_text(header + text, encoding="utf-8")
        n_blocks = len(re.findall(r'^\*\*T\d+\.\d+\.\d+ —', text, re.MULTILINE))
        print(f"  Prompt blocks parsed: {n_blocks} / expected {len(prompts)}")
        print(f"  Saved: {out_path.name}")

    print(f"\n=== TOTAL ===")
    print(f"Tokens: input={total_usage['input_tokens']:,} output={total_usage['output_tokens']:,} cache_read={total_usage['cache_read']:,}")


if __name__ == "__main__":
    main()
