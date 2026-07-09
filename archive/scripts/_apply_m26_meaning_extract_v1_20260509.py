"""_apply_m26_meaning_extract_v1_20260509.py — Claude API + DB read.

Step A of the M26 redesigned approach (per researcher 2026-05-09):
per-verse meaning extraction. NO clustering, NO sub-group reasoning,
NO grouping decisions. Just: for each verse, what does it say about
the term it's bound to.

Atomic per-verse calls. Resumable. Incremental save (JSONL).

For each active (G or P) verse_context row in M26:
  - Input: verse_text + term metadata (gloss, mounce, transliteration)
  - Output: {vr_id, mti_term_id, meaning, evidence_quote}

The term -> sub-group link is already in the DB; this step does not
re-derive it.

Design choices that come from prior Phase 4/Phase 5 lessons:
  - NO `thinking` mode (it consumed 32K tokens with no output on the
    Phase 4+5+6 attempt).
  - Streaming with small max_tokens (each call is ~150 output tokens).
  - System prompt cached so subsequent calls cost ~$0.002 each.
  - Per-verse JSONL append: each successful call flushes one line to
    disk. Re-running skips (vr_id, mti_term_id) pairs already in the
    file — fully resumable on Ctrl-C, network blip, or any failure.

Output:
  outputs/markdown/m26-meanings-{model}-{date}.jsonl  (one JSON per line)
  outputs/markdown/m26-meanings-errors-{model}-{date}.jsonl  (per-verse errors)
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(".env")
except ImportError:
    pass

DB_PATH = os.path.join("database", "bible_research.db")
CLUSTER_CODE = "M26"
CLUSTER_DESC = "Righteousness and Justice"

OUT_DIR = os.path.join("outputs", "markdown")


SYSTEM_PROMPT = f"""You are an analyst on the Soul Word Analysis Programme — Step A (per-verse meaning extraction) for cluster **M26 — {CLUSTER_DESC}**.

# Operating principle (non-negotiable)

Read the verse. State what THIS verse says about the inner-being characteristic via THIS term. Do not interpret beyond what the text shows. Do not import context from other verses or from general theological knowledge.

# Your task — atomic, one verse at a time

You will receive ONE verse + ONE term occurring in that verse. Produce two outputs:

(1) `meaning` — one short sentence (≤25 words) stating what THIS verse evidences about the term's inner-being characteristic. Plain English. Concrete. No theological elaboration. If the verse uses the term in a sense unrelated to inner-being content (set-aside-style), say so plainly.

(2) `evidence_quote` — a short verbatim phrase from the verse (≤15 words) that grounds the meaning. The exact text the meaning rests on.

Discipline:
- Each call is independent. Do not assume continuity with prior verses.
- Use the verse text and the term's gloss/mounce as your only input.
- Brief is good. Vague is bad. If the verse is dense, prioritise what it shows about the term over comprehensive paraphrase.
- The cluster name (M26 — Righteousness and Justice) is context — not a constraint on what you say. If the verse evidences something different from the cluster's characteristic, say what the verse actually evidences.

# Output JSON shape — exactly

{{
  "vr_id": <int — copied from input>,
  "mti_term_id": <int — copied from input>,
  "strong": "<copied from input>",
  "meaning": "<≤25 words plain English>",
  "evidence_quote": "<≤15 word verbatim phrase>"
}}
"""


OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "vr_id": {"type": "integer"},
        "mti_term_id": {"type": "integer"},
        "strong": {"type": "string"},
        "meaning": {"type": "string"},
        "evidence_quote": {"type": "string"},
    },
    "required": ["vr_id", "mti_term_id", "strong", "meaning",
                 "evidence_quote"],
    "additionalProperties": False,
}


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact():
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def fetch_active_verses(conn) -> list[dict]:
    """All active (non-set-aside) M26 vc rows + verse + term metadata."""
    return [dict(r) for r in conn.execute("""
        SELECT vc.id AS vc_id, vc.verse_record_id AS vr_id,
               vc.mti_term_id, vc.is_relevant, vc.is_anchor,
               vr.reference, vr.verse_text, vr.testament,
               mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language,
               ti.short_def_mounce
          FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
          JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
          LEFT JOIN wa_term_inventory ti
                 ON ti.strongs_number = mt.strongs_number
                AND COALESCE(ti.delete_flagged, 0) = 0
                AND COALESCE(ti.term_owner_type, 'OWNER') = 'OWNER'
         WHERE mt.cluster_code = 'M26'
           AND COALESCE(mt.delete_flagged, 0) = 0
           AND COALESCE(vc.delete_flagged, 0) = 0
           AND (vc.set_aside_reason IS NULL OR vc.set_aside_reason = '')
         ORDER BY vr.reference, mt.strongs_number
    """)]


def load_completed_keys(jsonl_path: str) -> set[tuple[int, int]]:
    """Read existing JSONL; return set of (vr_id, mti_term_id) already done."""
    done = set()
    if not Path(jsonl_path).exists():
        return done
    with open(jsonl_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                done.add((obj["vr_id"], obj["mti_term_id"]))
            except Exception:
                pass
    return done


def build_user_msg(v: dict) -> str:
    pkg = {
        "verse": {
            "vr_id": v["vr_id"],
            "reference": v["reference"],
            "testament": v["testament"],
            "verse_text": v["verse_text"],
        },
        "term": {
            "mti_term_id": v["mti_term_id"],
            "strong": v["strongs_number"],
            "transliteration": v["transliteration"],
            "gloss": v["gloss"],
            "language": v["language"],
            "short_def_mounce": v.get("short_def_mounce"),
        },
    }
    return (
        "Extract the meaning of this verse via the named term. "
        "Return JSON in the schema above.\n\n"
        f"```json\n{json.dumps(pkg, ensure_ascii=False, indent=2)}\n```"
    )


def call_claude(client, v, model: str):
    user_msg = build_user_msg(v)
    text_parts = []
    response = None
    with client.messages.stream(
        model=model,
        max_tokens=600,
        # NO thinking — direct output. Keeps per-call cost predictable.
        output_config={
            "format": {"type": "json_schema", "schema": OUTPUT_SCHEMA},
        },
        system=[{
            "type": "text",
            "text": SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }],
        messages=[{"role": "user", "content": user_msg}],
    ) as stream:
        for text in stream.text_stream:
            text_parts.append(text)
        response = stream.get_final_message()
    raw = "".join(text_parts).strip()
    parsed = json.loads(raw)
    return parsed, response


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="claude-sonnet-4-6")
    ap.add_argument("--limit", type=int, default=None,
                    help="Stop after N verses (smoke test)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.dry_run and not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        return 2

    os.makedirs(OUT_DIR, exist_ok=True)
    today = today_compact()
    jsonl_path = os.path.join(
        OUT_DIR, f"m26-meanings-{args.model}-{today}.jsonl"
    )
    err_path = os.path.join(
        OUT_DIR, f"m26-meanings-errors-{args.model}-{today}.jsonl"
    )

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    verses = fetch_active_verses(conn)
    print(f"M26 active verses: {len(verses)}")

    done = load_completed_keys(jsonl_path)
    if done:
        print(f"Resuming — {len(done)} verses already in {jsonl_path}")

    todo = [v for v in verses if (v["vr_id"], v["mti_term_id"]) not in done]
    if args.limit:
        todo = todo[: args.limit]
    print(f"To process this run: {len(todo)}")

    if args.dry_run:
        if todo:
            print()
            print("=== DRY RUN — first verse ===")
            print(build_user_msg(todo[0])[:1500])
        return 0

    from anthropic import Anthropic
    client = Anthropic()

    in_tot = out_tot = cache_r_tot = 0
    n_ok = n_err = 0
    t_start = time.time()

    print(f"Calling {args.model}...\n")
    for i, v in enumerate(todo, 1):
        try:
            parsed, resp = call_claude(client, v, args.model)
        except Exception as e:
            n_err += 1
            err_record = {
                "vr_id": v["vr_id"],
                "mti_term_id": v["mti_term_id"],
                "reference": v["reference"],
                "error": f"{type(e).__name__}: {e}",
                "ts": now_iso(),
            }
            with open(err_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(err_record, ensure_ascii=False) + "\n")
            print(f"  [{i:4d}/{len(todo)}] X {v['reference']:<14s} "
                  f"{v['strongs_number']:8s} ERROR {type(e).__name__}: {e}")
            continue

        usage = resp.usage
        in_tot += usage.input_tokens
        out_tot += usage.output_tokens
        cache_r_tot += getattr(usage, "cache_read_input_tokens", 0) or 0

        # Append to JSONL immediately — resumable from any interrupt
        with open(jsonl_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(parsed, ensure_ascii=False) + "\n")

        n_ok += 1
        meaning_excerpt = (parsed.get("meaning") or "")[:60]
        print(f"  [{i:4d}/{len(todo)}] + {v['reference']:<14s} "
              f"{v['strongs_number']:8s} {meaning_excerpt}")

    elapsed = time.time() - t_start

    if "opus" in args.model:
        in_price, out_price = 15.0, 75.0
    elif "haiku" in args.model:
        in_price, out_price = 1.0, 5.0
    else:
        in_price, out_price = 3.0, 15.0
    cost = (in_tot / 1_000_000) * in_price + (out_tot / 1_000_000) * out_price

    print()
    print("=" * 60)
    print(f"  STEP A SUMMARY")
    print("=" * 60)
    print(f"  Processed this run:     {n_ok + n_err}")
    print(f"  OK:                     {n_ok}")
    print(f"  Errors:                 {n_err}")
    print(f"  Total in JSONL:         {len(done) + n_ok}")
    print(f"  Tokens in/out/cache:    {in_tot:,} / {out_tot:,} / {cache_r_tot:,}")
    print(f"  Cost (this run):        ${cost:.4f}")
    print(f"  Wall time:              {elapsed:.1f}s "
          f"({elapsed / max(n_ok + n_err, 1):.2f}s/verse)")
    print(f"  Output:                 {jsonl_path}")
    if n_err:
        print(f"  Errors log:             {err_path}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
