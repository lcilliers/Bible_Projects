"""M46 Phase 2 UT review via Claude API.

Classifies all 197 UT verses across M46's 14 terms that have UT load.
Produces a VCNEW patch + a borderline/decision log for researcher review.

Per cluster instruction §5:
  - relevant → vc INSERT with is_relevant=1, group_id=null
  - set_aside → vc INSERT with is_relevant=0, set_aside_reason populated
  - borderline → held in log only (no DB write)

Uses Anthropic SDK with prompt caching on the system prompt.
"""
from __future__ import annotations
import argparse, json, os, sqlite3, sys, time
from datetime import datetime, timezone
from pathlib import Path

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

DB = "database/bible_research.db"
CLUSTER = "M46"
MODEL = "claude-sonnet-4-6"  # current Sonnet 4.6
OUT_DIR = Path("Sessions/Session_Clusters/M46")
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
PATCH_PATH = OUT_DIR / f"wa-cluster-M46-patch-vcnew-utreview-api-v1-{DATE}.json"
LOG_PATH = OUT_DIR / f"WA-M46-UT-verse-review-api-v1-{DATE}.md"
RAW_PATH = OUT_DIR / f"WA-M46-UT-api-raw-responses-{DATE}.json"


SYSTEM_PROMPT = """You are Claude AI performing Phase 2 (UT verse review) of the Session B cluster analysis for cluster M46 (Abundance, Prosperity and Wealth).

CLUSTER M46 — DOMAIN

M46's characteristic-bearing scope: the inner-being engagement of wealth, prosperity, and material abundance — and their opposite, poverty. This cluster names the inner posture toward material possession (orientation toward what one has, what one lacks, what one accumulates, what one trusts in) as a constitutional inner-being characteristic. It includes:
  - Wealth as inner orientation (trust in riches; the rich young ruler dynamic).
  - Poverty as inner-being condition (poor in spirit; the widow's two coins; the gospel for the poor).
  - The wealth/poverty contrast pair as a constitutional axis of the inner life.
  - Material sufficiency and contentment as inner posture (autarkeia register).
  - Generative blessing/prospering as God-toward-creature movement (the increase, the fatness, the goodly produce).
  - Hoarding, complacency, and false security as inner-being corruptions of wealth.

T1 FRAMEWORK — what a characteristic-bearing inner-being verse must show

A verse evidences M46's characteristic when its content names one or more of:
  1. Constitutional location — heart/mind/soul orientation toward wealth/poverty/abundance.
  2. Inner faculties engaged — desire, trust, complacency, contentment, attachment.
  3. Inner impact — wealth's effect on the person (forms the heart; corrupts; humbles; enables generosity).
  4. Structural opposite — rich/poor; abundance/lack; trust/anxiety.
  5. Direction or object — toward God or away; toward neighbour or grasping inward.

PHASE 2 RUBRIC — three classifications

You assign each verse exactly ONE classification:

  **relevant** — the verse evidences the term's characteristic for M46.
      Examples: 1Tim 6:9 (those who desire to be rich fall into temptation) for G4147 ploutēō.
      Examples: Pro 11:28 (whoever trusts in his riches will fall) for o.sher.

  **set_aside** — the term appears in this verse but does NOT carry inner-being content
      within the M46 register. The verse uses the term in an unrelated sense (e.g.
      literal-material narrative with no inner-being engagement; metaphorical use
      in a non-wealth register; figurative reference).
      Examples: a list of names where someone is "rich Jones the son of..." — surface
      occurrence with no inner content.

  **borderline** — the verse meaning is ambiguous and needs researcher decision.
      Use sparingly. Borderline entries are HELD for researcher review and NOT
      written to the database. Default to relevant or set_aside when the evidence
      is clear; reserve borderline for genuinely unresolvable cases.

OUTPUT FORMAT — strict JSON

Respond with exactly one JSON array. One object per verse, in the same order the verses were given. Each object MUST have these fields:

  {
    "vr_id": <integer — copy from input>,
    "reference": "<string — copy from input>",
    "classification": "relevant" | "set_aside" | "borderline",
    "rationale": "<one-sentence reason, max 250 chars>",
    "set_aside_reason": "<populated only if classification='set_aside', otherwise empty string>"
  }

Do not include any text outside the JSON array. No prose, no preamble, no markdown fence. Just the JSON.

CRITICAL — set_aside_reason format

When classification is "set_aside", the set_aside_reason field must:
  - Be a one-line plain-English reason (max 200 chars).
  - Name the verse's actual sense of the term (e.g. "physical fat/oil context — no inner orientation").
  - End with: " — outside M46 inner-being scope."
"""


def fetch_ut_load(conn) -> list[dict]:
    """Group UT verses by term."""
    rows = list(conn.execute("""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.md_version,
               vr.id AS vr_id, vr.reference, vr.verse_text, vr.target_word,
               vr.context_before, vr.context_after, vr.translation
          FROM mti_terms mt
          JOIN wa_verse_records vr ON vr.mti_term_id = mt.id
          LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id
                                     AND vc.mti_term_id = mt.id
         WHERE mt.cluster_code = ?
           AND COALESCE(mt.delete_flagged,0) = 0
           AND COALESCE(vr.delete_flagged,0) = 0
           AND vc.id IS NULL
         ORDER BY mt.strongs_number, vr.book_id, vr.chapter, vr.verse_num
    """, (CLUSTER,)))

    by_term: dict[int, dict] = {}
    for r in rows:
        mti = r["mti_id"]
        if mti not in by_term:
            by_term[mti] = {
                "mti_id": mti,
                "strongs": r["strongs_number"],
                "translit": r["transliteration"],
                "gloss": r["gloss"],
                "language": r["language"],
                "md_version": r["md_version"],
                "verses": [],
            }
        by_term[mti]["verses"].append({
            "vr_id": r["vr_id"],
            "reference": r["reference"],
            "verse_text": r["verse_text"] or "",
            "target_word": r["target_word"] or "",
            "context_before": (r["context_before"] or "")[:300],
            "context_after": (r["context_after"] or "")[:300],
            "translation": r["translation"] or "ESV",
        })
    return list(by_term.values())


def build_user_message(term: dict) -> str:
    """Per-term user message: term info + verses to classify."""
    parts = [
        f"TERM: {term['strongs']} {term['translit']} — {term['gloss']} ({term['language']})",
        f"Verses to classify: {len(term['verses'])}",
        "",
        "For each verse below, classify per the rubric in the system prompt.",
        "",
    ]
    for v in term["verses"]:
        parts.append(f"---")
        parts.append(f"vr_id: {v['vr_id']}")
        parts.append(f"reference: {v['reference']}")
        parts.append(f"target_word: {v['target_word']!r}")
        parts.append(f"verse_text ({v['translation']}): {v['verse_text']}")
        if v["context_before"]:
            parts.append(f"context_before: {v['context_before']}")
        if v["context_after"]:
            parts.append(f"context_after: {v['context_after']}")
    parts.append("")
    parts.append("Return the JSON array now. No prose.")
    return "\n".join(parts)


def classify_term(client, term: dict, max_retries: int = 2) -> list[dict]:
    """One API call per term. Returns parsed JSON array."""
    user_msg = build_user_message(term)
    last_err = None
    for attempt in range(max_retries + 1):
        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=8000,
                system=[
                    {"type": "text", "text": SYSTEM_PROMPT,
                     "cache_control": {"type": "ephemeral"}},
                ],
                messages=[{"role": "user", "content": user_msg}],
            )
            text = resp.content[0].text.strip()
            # Strip markdown fences if present
            if text.startswith("```"):
                text = text.split("```", 2)[1]
                if text.startswith("json"):
                    text = text[4:]
                text = text.strip("`").strip()
            results = json.loads(text)
            if not isinstance(results, list):
                raise ValueError("response is not a JSON array")
            # Usage tally
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
                time.sleep(2)
                continue
            raise


def build_vcnew_patch(by_term: list[dict], classifications: dict[int, list[dict]]) -> dict:
    """Aggregate relevant + set_aside into a VCNEW patch."""
    ops = []
    seq = 1
    terms_covered = []
    input_versions = {}
    for term in by_term:
        terms_covered.append(term["mti_id"])
        input_versions[str(term["mti_id"])] = term["md_version"] or 1
        results = classifications.get(term["mti_id"], [])
        # Map results by vr_id for lookup
        by_vr = {r.get("vr_id"): r for r in results}
        for v in term["verses"]:
            r = by_vr.get(v["vr_id"])
            if not r:
                continue
            cls = r.get("classification")
            if cls == "relevant":
                ops.append({
                    "op_id": f"OP-{seq:03d}",
                    "table": "verse_context",
                    "operation": "insert",
                    "record": {
                        "verse_record_id": v["vr_id"],
                        "mti_term_id": term["mti_id"],
                        "group_id": None,
                        "is_anchor": 0,
                        "is_relevant": 1,
                        "is_related": 0,
                    }
                })
                seq += 1
            elif cls == "set_aside":
                reason = r.get("set_aside_reason") or "outside M46 inner-being scope"
                ops.append({
                    "op_id": f"OP-{seq:03d}",
                    "table": "verse_context",
                    "operation": "insert",
                    "record": {
                        "verse_record_id": v["vr_id"],
                        "mti_term_id": term["mti_id"],
                        "group_id": None,
                        "is_anchor": 0,
                        "is_relevant": 0,
                        "is_related": 0,
                        "set_aside_reason": reason,
                    }
                })
                seq += 1
            # borderline → not in patch
    return {
        "_patch_meta": {
            "patch_type": "VCNEW",
            "patch_name": f"wa-cluster-M46-patch-vcnew-utreview-api-v1-{DATE}",
            "cluster": "M46",
            "session_ref": "M46 Phase 2 UT review via Claude API",
            "date": DATE,
            "terms_covered": terms_covered,
            "input_versions": input_versions,
            "operation_count": len(ops),
            "source": "Claude API classification",
        },
        "operations": ops,
    }


def write_log(by_term, classifications, patch, log_path):
    lines = [
        f"# WA-M46-UT-verse-review-api-v1-{DATE}",
        "",
        "Phase 2 UT review for cluster M46 — Claude API classification of 197 UT verses across 14 terms.",
        "",
        "## Per-term counts",
        "",
        "| Strong's | Translit | Gloss | UT | Relevant | Set aside | Borderline |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    total_rel = total_sa = total_bd = 0
    for term in by_term:
        results = classifications.get(term["mti_id"], [])
        rel = sum(1 for r in results if r.get("classification") == "relevant")
        sa = sum(1 for r in results if r.get("classification") == "set_aside")
        bd = sum(1 for r in results if r.get("classification") == "borderline")
        total_rel += rel; total_sa += sa; total_bd += bd
        lines.append(f"| {term['strongs']} | {term['translit']} | {term['gloss']} | "
                     f"{len(term['verses'])} | {rel} | {sa} | {bd} |")
    lines.append(f"| **TOTAL** | | | | **{total_rel}** | **{total_sa}** | **{total_bd}** |")

    # Borderline section
    lines.append("")
    lines.append("## Borderline entries — held for researcher decision (not in patch)")
    lines.append("")
    any_bd = False
    for term in by_term:
        results = classifications.get(term["mti_id"], [])
        by_vr = {v["vr_id"]: v for v in term["verses"]}
        for r in results:
            if r.get("classification") == "borderline":
                any_bd = True
                v = by_vr.get(r.get("vr_id"))
                lines.append(f"- **{term['strongs']} {term['translit']}** "
                             f"vr={r.get('vr_id')} {r.get('reference')} — "
                             f"{r.get('rationale','')}")
                if v:
                    lines.append(f"  > {v['verse_text']}")
    if not any_bd:
        lines.append("_(none)_")

    lines.append("")
    lines.append(f"## Patch")
    lines.append("")
    lines.append(f"- File: `{patch['_patch_meta']['patch_name']}.json`")
    lines.append(f"- Operations: {patch['_patch_meta']['operation_count']}")
    lines.append(f"- Terms covered: {len(patch['_patch_meta']['terms_covered'])}")
    log_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0,
                    help="Limit to first N terms (0=all). Useful for smoke test.")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    by_term = fetch_ut_load(conn)
    if args.limit:
        by_term = by_term[: args.limit]
    n_verses = sum(len(t["verses"]) for t in by_term)
    print(f"M46 UT load: {len(by_term)} terms · {n_verses} verses")
    for t in by_term:
        print(f"  {t['strongs']:<8} {t['translit']:<14} {len(t['verses'])} UT verses")

    client = anthropic.Anthropic()
    print(f"\nModel: {MODEL}\n")

    classifications: dict[int, list[dict]] = {}
    raw: list[dict] = []
    totals_u = {"input": 0, "output": 0, "cache_create": 0, "cache_read": 0}

    for i, term in enumerate(by_term, 1):
        print(f"[{i}/{len(by_term)}] {term['strongs']} {term['translit']} "
              f"({len(term['verses'])} verses) ...", end=" ", flush=True)
        t0 = time.time()
        results, usage, raw_text = classify_term(client, term)
        elapsed = time.time() - t0
        classifications[term["mti_id"]] = results
        totals_u["input"] += usage["input_tokens"]
        totals_u["output"] += usage["output_tokens"]
        totals_u["cache_create"] += usage["cache_creation"]
        totals_u["cache_read"] += usage["cache_read"]
        rel = sum(1 for r in results if r.get("classification") == "relevant")
        sa = sum(1 for r in results if r.get("classification") == "set_aside")
        bd = sum(1 for r in results if r.get("classification") == "borderline")
        print(f"R={rel} S={sa} B={bd} ({elapsed:.1f}s, in={usage['input_tokens']} "
              f"out={usage['output_tokens']} cache_read={usage['cache_read']})")
        raw.append({"mti_id": term["mti_id"], "strongs": term["strongs"],
                    "usage": usage, "response": raw_text})

    print(f"\nTotal usage: input={totals_u['input']:,}  output={totals_u['output']:,}  "
          f"cache_create={totals_u['cache_create']:,}  cache_read={totals_u['cache_read']:,}")

    # Build patch + log + raw
    patch = build_vcnew_patch(by_term, classifications)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PATCH_PATH.write_text(json.dumps(patch, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nPatch: {PATCH_PATH}  ({patch['_patch_meta']['operation_count']} ops)")

    RAW_PATH.write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Raw responses: {RAW_PATH}")

    write_log(by_term, classifications, patch, LOG_PATH)
    print(f"Log: {LOG_PATH}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
