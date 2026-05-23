"""Interim keyword-discovery pass for an under-digested sub-group.

For each is_relevant verse in the target sub-group, the API returns 3-7 keywords or
short phrases naming what is happening at the inner-being level of the person in
that verse. The keywords emerge from the verse text + Pass A meaning, not from any
pre-built taxonomy. Output feeds a downstream clustering step that surfaces
characteristic-level distinctions Phase 5 missed.

Usage:
  python scripts/_keyword_discovery_subgroup_v1_20260523.py --cluster M10 --subgroup M10-A
  python scripts/_keyword_discovery_subgroup_v1_20260523.py --cluster M10 --subgroup M10-A --batch-size 25
  python scripts/_keyword_discovery_subgroup_v1_20260523.py --cluster M10 --subgroup M10-A --dry-run-fetch

Outputs (under Sessions/Session_Clusters/{cluster}/files phase 5/):
  - wa-cluster-{CLUSTER}-{SG}-keywords-v1-{YYYYMMDD}.json — {vc_id: keywords[]}
  - wa-cluster-{CLUSTER}-{SG}-keywords-v1-{YYYYMMDD}.md   — flat ref|keywords lines
  - wa-cluster-{CLUSTER}-{SG}-keywords-raw-{YYYYMMDD}.json — raw API responses
"""
from __future__ import annotations
import argparse
import io
import json
import os
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

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
DEFAULT_BATCH_SIZE = 25
MAX_TOKENS = 8000


SYSTEM_PROMPT = """You are running an INNER-BEING KEYWORD DISCOVERY pass on a set of biblical verses that have already been studied (each verse comes with its Pass A meaning, a one-line summary of what the verse says about its term's inner-being content).

YOUR TASK

For each verse provided, output **3 to 7 short keywords** that name, at a fine-grained level, what is happening at the INNER-BEING level of the person in this verse. The keywords are the operational vocabulary of *what the inner person is doing, suffering, becoming, registering, or being moved toward* — not what the verse is about at the gloss / theme / doctrine level.

These keywords will be **aggregated across hundreds of verses** to surface inner-being-faculty distinctions that an earlier gloss-level reading missed. For the aggregation to work, keywords MUST be atomic and compositional — they have to cluster across verses.

KEYWORD FORMAT — STRICT

Each keyword is **ONE word OR a TWO-word combination**.

1. **One word**: a single verb, noun, or pronoun (e.g. `conscience`, `will`, `hardening`, `surfacing`, `silence`, `atonement`, `defection`).
2. **Two-word combination**: exactly the two open-class words that combine to name one inner-being notion. Separated by a single space (NOT a hyphen). Examples: `conscience violation`, `will refusing`, `guilt surfacing`, `heart hardening`, `silence willful`, `defection covenant`, `restraint divine`.

ABSOLUTE RULES (every keyword must obey)

- **No particles.** Do NOT use: of, to, as, with, by, the, a, an, in, on, for, from, into, onto, upon, against (and the like). Strip every preposition / article / conjunction.
- **Mainly verbs and nouns.** Pronouns OK. Adjectives OK if they describe an inner state (`hardened`, `defiant`, `silent`). No adverbs.
- **No proper names.** Never `Cain`, `Pharaoh`, `Israel`, `Sodom`, `Moses`, `Jacob`, `David`, etc. Likewise no place names. The keyword names the *operation* or *faculty*, not the actor or location.
- **Two words max.** A keyword like `will refusing through God awareness` is TOO LONG — split it into the operative pairs (`will refusing`, `awareness divine`).
- **No sentences.** No keyword should read like a clause or mini-explanation.
- **No bland gloss labels alone.** `sin`, `transgression`, `guilt`, `wickedness` alone tell us nothing new — pair them or replace them: `sin objective`, `guilt surfacing`, `transgression unintentional`.
- **Discriminate.** Two verses about "sin against God" get different keywords if the inner mechanism differs: one might be `defection wilful`, another `defection habitual`, another `conscience strike`.

EXAMPLES (correct form)

Gen 39:9 (Joseph refusing temptation):
  ["conscience naming", "will refusing", "awareness divine", "clarity moral", "pressure resisted"]

Exo 9:34 (Pharaoh hardening again):
  ["hardening", "will stiffening", "heart closing", "defection repeated", "truth resisted"]

Lev 4:2 (inadvertent sin):
  ["unintentional", "transgression objective", "violation inadvertent", "ignorance", "sin real"]

Lev 5:1 (silence as sin):
  ["silence willful", "truth withheld", "conscience suppressed", "omission", "inaction wrong"]

EXAMPLES (incorrect form — what NOT to do)

- "will-insufficient-without-divine-restraint" — too long, sentence-like, contains particle
- "Joseph refusing temptation" — proper name
- "conscience-naming-act-as-violation" — too long, contains particles
- "of God awareness" — leading particle
- "sin" alone — bland gloss
- "the will is hardened" — full clause

OUTPUT FORMAT — STRICT JSON

Respond with exactly one JSON array. One object per verse, in the order the verses were given. Each object MUST have these fields:

  {
    "vc_id": <integer — copy from input>,
    "reference": "<string — copy from input>",
    "keywords": ["<keyword 1>", "<keyword 2>", ...]
  }

3 to 7 keywords per verse. No prose outside the array. No markdown fence.

REMINDERS

- Lowercase keywords (except where a noun is conventionally capitalised — but no proper names anyway).
- Keywords from the verse's own register where it sharpens the inner-being notion.
- Reach for the SAME word across verses when the same inner-being operation is in view (so the clustering works). Don't paraphrase "will refusing" as "will declines" in another verse if the operation is the same.
"""


def fetch_subgroup_verses(conn, cluster_code: str, subgroup_code: str) -> list[dict]:
    """Pull every is_relevant verse in the target sub-group, with Pass A meaning + span."""
    rows = list(conn.execute("""
        SELECT vc.id AS vc_id, vr.reference,
               vr.verse_text, vr.context_before, vr.context_after, vr.translation,
               vr.target_word AS span,
               mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
               vc.analysis_note AS meaning
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        WHERE mt.cluster_code = ?
          AND cs.cluster_code = ? AND cs.subgroup_code = ?
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND COALESCE(mt.delete_flagged, 0) = 0
          AND COALESCE(vr.delete_flagged, 0) = 0
          AND COALESCE(cs.delete_flagged, 0) = 0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num, mt.strongs_number, vc.id
    """, (cluster_code, cluster_code, subgroup_code)))
    return [dict(r) for r in rows]


def build_batch_message(batch_num: int, total_batches: int, verses: list[dict]) -> str:
    parts = [
        f"Batch {batch_num} of {total_batches} — {len(verses)} verses.",
        "",
        "For each verse below, return 3 to 7 inner-being keywords per the rubric.",
        "",
    ]
    for v in verses:
        parts.append("---")
        parts.append(f"vc_id: {v['vc_id']}")
        parts.append(f"reference: {v['reference']}")
        parts.append(f"strongs: {v['strongs_number']}")
        parts.append(f"transliteration: {v['transliteration']}")
        parts.append(f"gloss: {v['gloss']}")
        if v.get('span'):
            parts.append(f"span (specific word in verse for this term): {v['span']!r}")
        parts.append(f"verse_text ({v.get('translation') or 'ESV'}): {v['verse_text'] or ''}")
        parts.append(f"pass_a_meaning: {v.get('meaning') or ''}")
    parts.append("")
    parts.append("Return the JSON array now. No prose.")
    return "\n".join(parts)


def call_batch(client, batch_num: int, total: int, verses: list[dict], max_retries: int = 2):
    user_msg = build_batch_message(batch_num, total, verses)
    for attempt in range(max_retries + 1):
        try:
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
            results = json.loads(text)
            if not isinstance(results, list):
                raise ValueError("response is not a JSON array")
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


def write_outputs(verses: list[dict], all_results: dict[int, dict],
                   out_md: Path, out_json: Path, totals_u: dict, batches: list[dict]) -> None:
    # JSON
    payload = {
        "_meta": {
            "model": MODEL,
            "verses": len(verses),
            "filled": sum(1 for v in verses if v["vc_id"] in all_results and all_results[v["vc_id"]].get("keywords")),
            "batches": len(batches),
            "usage_totals": totals_u,
        },
        "keywords_by_vc_id": {
            str(v["vc_id"]): {
                "reference": v["reference"],
                "strongs": v["strongs_number"],
                "transliteration": v["transliteration"],
                "span": v.get("span") or "",
                "keywords": (all_results.get(v["vc_id"]) or {}).get("keywords") or [],
            }
            for v in verses
        }
    }
    out_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    # Markdown: one line per verse, easy for the researcher to scan
    lines = [
        f"# Inner-being keywords — flat review",
        f"",
        f"Model: {MODEL} · Verses: {len(verses)} · Batches: {len(batches)}",
        f"",
        "Per-verse keywords (canonical Bible order). Keywords emerge from the verse text + Pass A meaning; no external taxonomy imposed.",
        "",
        "| vc_id | Reference | Strongs | Term | Span | Keywords |",
        "|---:|---|---|---|---|---|",
    ]
    for v in verses:
        r = all_results.get(v["vc_id"]) or {}
        kws = r.get("keywords") or []
        kw_cell = ", ".join(kws)
        span_cell = (v.get("span") or "").replace("|", "\\|")
        lines.append(f"| {v['vc_id']} | {v['reference']} | {v['strongs_number']} | "
                     f"{v['transliteration']} | {span_cell} | {kw_cell} |")
    out_md.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True, help="Cluster code, e.g. M10")
    ap.add_argument("--subgroup", required=True, help="Sub-group code, e.g. M10-A")
    ap.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    ap.add_argument("--limit", type=int, default=0, help="Limit to first N batches")
    ap.add_argument("--dry-run-fetch", action="store_true",
                    help="Fetch + print verse count; do not call API.")
    args = ap.parse_args()

    cluster = args.cluster.strip()
    subgroup = args.subgroup.strip()
    date_str = datetime.now(timezone.utc).strftime("%Y%m%d")

    out_dir = REPO / "Sessions" / "Session_Clusters" / cluster / "files phase 5"
    out_dir.mkdir(parents=True, exist_ok=True)
    # Strip the cluster prefix from the subgroup code in the filename so we don't get
    # e.g. wa-cluster-M10-M10-A-keywords-…; we want wa-cluster-M10-A-keywords-…
    if subgroup.upper().startswith(cluster.upper() + "-"):
        sg_tag = subgroup[len(cluster) + 1:]
    else:
        sg_tag = subgroup
    base_name = f"wa-cluster-{cluster}-{sg_tag}-keywords"
    out_md = out_dir / f"{base_name}-v1-{date_str}.md"
    out_json = out_dir / f"{base_name}-v1-{date_str}.json"
    out_raw = out_dir / f"{base_name}-raw-{date_str}.json"

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    verses = fetch_subgroup_verses(conn, cluster, subgroup)
    conn.close()

    if not verses:
        print(f"No is_relevant verses found in {cluster}/{subgroup}.")
        return 1

    n_total = len(verses)
    n_batches = (n_total + args.batch_size - 1) // args.batch_size
    print(f"{cluster}/{subgroup}: {n_total} verses, {n_batches} batches of up to {args.batch_size}")
    print(f"Sample: vc_id={verses[0]['vc_id']} {verses[0]['reference']} "
          f"{verses[0]['strongs_number']} {verses[0]['transliteration']}")

    if args.dry_run_fetch:
        print("[--dry-run-fetch] No API calls made.")
        return 0

    client = anthropic.Anthropic()
    print(f"\nModel: {MODEL}\n")

    all_results: dict[int, dict] = {}
    raw_archive: list[dict] = []
    totals_u = {"input": 0, "output": 0, "cache_create": 0, "cache_read": 0}
    batch_stats: list[dict] = []

    actual_batches = n_batches if not args.limit else min(n_batches, args.limit)
    for i in range(actual_batches):
        batch = verses[i * args.batch_size:(i + 1) * args.batch_size]
        t0 = time.time()
        print(f"[{i + 1}/{actual_batches}] {len(batch)} verses ...", end=" ", flush=True)
        results, usage, raw_text = call_batch(client, i + 1, actual_batches, batch)
        elapsed = time.time() - t0
        totals_u["input"] += usage["input_tokens"]
        totals_u["output"] += usage["output_tokens"]
        totals_u["cache_create"] += usage["cache_creation"]
        totals_u["cache_read"] += usage["cache_read"]
        for r in results:
            vc_id = r.get("vc_id")
            if isinstance(vc_id, int):
                all_results[vc_id] = r
        filled = sum(1 for v in batch if v["vc_id"] in all_results
                     and all_results[v["vc_id"]].get("keywords"))
        print(f"filled={filled}/{len(batch)} ({elapsed:.1f}s, in={usage['input_tokens']} "
              f"out={usage['output_tokens']} cache_read={usage['cache_read']})")
        batch_stats.append({"batch": i + 1, "size": len(batch), "filled": filled,
                             "elapsed_s": round(elapsed, 1), "usage": usage})
        raw_archive.append({"batch": i + 1, "usage": usage, "response": raw_text})

    print(f"\nTotal usage: input={totals_u['input']:,}  output={totals_u['output']:,}  "
          f"cache_create={totals_u['cache_create']:,}  cache_read={totals_u['cache_read']:,}")

    write_outputs(verses, all_results, out_md, out_json, totals_u, batch_stats)
    out_raw.write_text(json.dumps(raw_archive, indent=2, ensure_ascii=False), encoding="utf-8")

    n_filled = sum(1 for v in verses if v["vc_id"] in all_results
                   and all_results[v["vc_id"]].get("keywords"))
    print(f"\nFilled: {n_filled} / {n_total}")
    print(f"Wrote: {out_md.relative_to(REPO)}")
    print(f"Wrote: {out_json.relative_to(REPO)}")
    print(f"Raw  : {out_raw.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
