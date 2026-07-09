"""M03 Phase 1 UT review via Claude API.

Classifies the ~481 UT verses across M03's 89 terms with UT load.
Produces a VCNEW patch + a borderline/decision log for researcher review.

Modeled on scripts/_apply_m02_ut_review_via_api_20260516.py.
Per cluster-instruction v2_2 §4.
Provisional-anchor rule (v2_2 §4.4) enforced at build time.
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

DB = "database/bible_research.db"
CLUSTER = "M03"
MODEL = "claude-sonnet-4-6"
CHUNK_SIZE = 50  # max verses per API call to stay under max_tokens
MAX_TOKENS = 12000
OUT_DIR = Path("Sessions/Session_Clusters/M03")
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
PATCH_PATH = OUT_DIR / f"wa-cluster-M03-patch-vcnew-utreview-api-v1-{DATE}.json"
LOG_PATH = OUT_DIR / f"WA-M03-UT-verse-review-api-v1-{DATE}.md"
RAW_PATH = OUT_DIR / f"WA-M03-UT-api-raw-responses-{DATE}.json"


SYSTEM_PROMPT = """You are Claude AI performing Phase 1 (UT verse review) of the Session B cluster analysis for cluster M03 (Grief, Sorrow and Mourning).

CLUSTER M03 — DOMAIN

M03's characteristic-bearing scope: the inner-being engagement of grief, sorrow, lament, mourning, anguish, and bitterness — the inner weight, ache, dissolution, and lament that arises within the person under loss, suffering, sin, injustice, or sympathy for others' suffering. The cluster names how the inner being is wounded, weighed down, broken, embittered, troubled, depleted, and brought to tears. It includes:

  - Grief and sorrow (luperō, lupē, ya.gon, e.tsev, ka.as-as-vexation) — the inner ache of distress over loss, sin, wrong, or unfulfilled hope.
  - Anguish and pressure (odunē, sunochē, tsu.qah, tsa.rah-distress) — the constricting, pressing inner experience of acute distress, often physical-like in intensity.
  - Mourning (e.vel, mis.ped, koptō, pentheō) — the outer expression of inner grief; ritual lament, funeral lament, communal sorrow.
  - Weeping and tears (ba.khah, dakruō, daluō, klaiō, dim.ah) — the somatic discharge of inner sorrow; tears as expression and as sign.
  - Bitterness (pikros, pikria, ma.ror, mar, me.rir) — inner sourness arising from prolonged distress, hurt, or resentment; bitterness as a soured inner condition.
  - Lament and complaint (si.ach as complaint, an.aq, ke.var groaning, stenazō) — speech act of inner sorrow before God or before the community.
  - Groaning (stenagmos, ne.um as deep utterance, han.in, ne.hi) — wordless or near-wordless expression of inner distress.
  - Inner trouble and faintness (a.gam, dav.va, cha.lah-grieved, cha.val-be in labor, ōdinō labour pains) — the inner weakening, sickening, faintness produced by sustained grief.
  - Birth-pain imagery (ōdinō, cha.val) — sometimes literal labour, sometimes metaphorical inner travail.
  - Crushing inner weight (ka.as as vexation, e.gem) — inner sorrow as load that presses down.
  - Inner contrition over sin (the grief-of-godly-sorrow register — 2 Cor 7:9-10 lupē kata theon) — sorrow that produces repentance.
  - Inner sorrow attributed to God (divine grief at human sin / divine compassion-pathos — Eph 4:30 grieving the Holy Spirit, Hos 11:8 inner-being yearning).
  - The structural opposites in view: joy, gladness, consolation, comfort, hope.

T1 FRAMEWORK — what a characteristic-bearing inner-being verse must show

A verse evidences M03's characteristic when its content names one or more of:
  1. Constitutional location — heart/mind/soul/spirit/bones experiencing grief, sorrow, anguish, bitterness, faintness, or related wounded inner state.
  2. Inner faculties engaged — the will being broken or weighed; perception of loss / injustice / sin; movement toward lament, tears, or repentance.
  3. Inner impact — grief's effect on the person (paralyses, drives to God, drives to despair, motivates repentance, depletes vitality, produces wisdom).
  4. Structural opposite — sorrow vs joy; mourning vs comfort; anguish vs peace; bitterness vs sweetness; weeping vs laughter; groaning vs praise.
  5. Direction or object — grief over personal sin; over loss of loved one; over enemy's destruction (compassion-grief); over God's grief; pastoral grief over disciples; communal lament; God's grief.

PHASE 1 RUBRIC — three classifications

You assign each verse exactly ONE classification:

  **relevant** — the verse evidences the term's inner-being content within M03's register.
      Examples: Joh 11:35 (Jesus wept — somatic-inner expression of grief at Lazarus's death) for dakruō.
      Examples: Psa 6:6 (I am weary with my groaning; all night I make my bed swim with tears) for ba.khah.
      Examples: Eze 21:6 (sigh with breaking of loins, with bitterness sigh before their eyes) for me.rir.
      Examples: 2Co 7:10 (godly grief produces repentance leading to salvation) for lupē.

  **set_aside** — the term appears in this verse but does NOT carry inner-being content
      within the M03 register. The verse uses the term in an unrelated sense:
        - literal-physical context with no inner-being engagement (e.g. "ma.ror" meaning
          literal bitter herbs of the Passover meal, not bitterness of soul);
        - figurative use outside the grief/sorrow register (e.g. "cha.val" meaning literal
          to be in labor for childbirth without the inner-grief metaphorical reading;
          or "stenazō" meaning the groaning of literal physical effort, not inner distress);
        - surface occurrence in a list, genealogy, place-name with no inner content
          (some Strong's homonyms cover physical-bitter taste vs inner-bitterness;
          physical labor-pains vs inner travail);
        - the term's lexical form here belongs to a different semantic domain entirely
          (e.g. "ka.as" used in its anger register, not its vexation-as-sorrow register).

  **borderline** — the verse meaning is ambiguous and needs researcher decision.
      Use sparingly. Borderline entries are HELD for researcher review and NOT written
      to the database. Default to relevant or set_aside when the evidence is clear;
      reserve borderline for genuinely unresolvable cases (e.g. labor-pains metaphor
      that could read either as literal childbirth or as inner travail-grief).

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
  - Name the verse's actual sense of the term (e.g. "ma.ror used as Passover bitter herbs, not inner bitterness").
  - End with: " — outside M03 inner-being scope."
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
           AND mt.status IN ('extracted','extracted_thin')
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


def _call_api_once(client, term: dict, verses_chunk: list[dict], max_retries: int = 2) -> tuple[list[dict], dict, str]:
    """Single API call for one chunk of verses for one term."""
    sub_term = {**term, "verses": verses_chunk}
    user_msg = build_user_message(sub_term)
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


def classify_term(client, term: dict, max_retries: int = 2) -> tuple[list[dict], dict, str]:
    """Classify all verses for a term — chunks into CHUNK_SIZE-verse batches.

    Returns combined results, summed usage, and concatenated raw text (one per chunk)."""
    verses = term["verses"]
    if len(verses) <= CHUNK_SIZE:
        return _call_api_once(client, term, verses, max_retries)

    # Chunk
    combined_results: list[dict] = []
    combined_usage = {"input_tokens": 0, "output_tokens": 0, "cache_creation": 0, "cache_read": 0}
    raw_chunks: list[str] = []
    n_chunks = (len(verses) + CHUNK_SIZE - 1) // CHUNK_SIZE
    for i in range(0, len(verses), CHUNK_SIZE):
        chunk = verses[i:i+CHUNK_SIZE]
        chunk_num = (i // CHUNK_SIZE) + 1
        print(f" [chunk {chunk_num}/{n_chunks}: {len(chunk)} verses]", end="", flush=True)
        results, usage, text = _call_api_once(client, term, chunk, max_retries)
        combined_results.extend(results)
        for k in ("input_tokens", "output_tokens", "cache_creation", "cache_read"):
            combined_usage[k] += usage[k]
        raw_chunks.append(text)
    raw_text = "\n---CHUNK SEP---\n".join(raw_chunks)
    return combined_results, combined_usage, raw_text


def _existing_anchor_count(conn, mti_id: int) -> int:
    return conn.execute(
        "SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND is_anchor=1 AND COALESCE(delete_flagged,0)=0",
        (mti_id,)
    ).fetchone()[0]


def build_vcnew_patch(conn, by_term: list[dict], classifications: dict[int, list[dict]]) -> dict:
    """Aggregate relevant + set_aside into a VCNEW patch (provisional-anchor per v2_2 §4.4)."""
    ops = []
    seq = 1
    terms_covered = []
    input_versions = {}
    provisional_anchor_promotions = []

    for term in by_term:
        mti = term["mti_id"]
        terms_covered.append(mti)
        input_versions[str(mti)] = term["md_version"] or 1
        existing_anchors = _existing_anchor_count(conn, mti)
        first_relevant_emitted = False

        results = classifications.get(mti, [])
        by_vr = {r.get("vr_id"): r for r in results}
        for v in term["verses"]:
            r = by_vr.get(v["vr_id"])
            if not r:
                continue
            cls = r.get("classification")
            if cls == "relevant":
                is_anchor = 0
                if existing_anchors == 0 and not first_relevant_emitted:
                    is_anchor = 1
                    provisional_anchor_promotions.append({
                        "op_id": f"OP-{seq:03d}",
                        "mti_term_id": mti,
                        "strongs": term["strongs"],
                        "verse_record_id": v["vr_id"],
                        "reference": v["reference"],
                    })
                    first_relevant_emitted = True
                op = {
                    "op_id": f"OP-{seq:03d}",
                    "table": "verse_context",
                    "operation": "insert",
                    "record": {
                        "verse_record_id": v["vr_id"],
                        "mti_term_id": mti,
                        "group_id": None,
                        "cluster_subgroup_id": None,
                        "is_anchor": is_anchor,
                        "is_relevant": 1,
                        "is_related": 0,
                        "delete_flagged": 0,
                        "vertical_pass_flag": 0,
                    }
                }
                if is_anchor == 1:
                    op["_provisional_anchor"] = (
                        "Set per v2_2 §4.4 — term had no existing anchor; first relevant op promoted."
                    )
                ops.append(op)
                seq += 1
            elif cls == "set_aside":
                reason = r.get("set_aside_reason") or "outside M03 inner-being scope"
                ops.append({
                    "op_id": f"OP-{seq:03d}",
                    "table": "verse_context",
                    "operation": "insert",
                    "record": {
                        "verse_record_id": v["vr_id"],
                        "mti_term_id": mti,
                        "group_id": None,
                        "cluster_subgroup_id": None,
                        "is_anchor": 0,
                        "is_relevant": 0,
                        "is_related": 0,
                        "delete_flagged": 0,
                        "vertical_pass_flag": 0,
                        "set_aside_reason": reason,
                    }
                })
                seq += 1

    return {
        "_patch_meta": {
            "patch_type": "VCNEW",
            "patch_id": f"wa-cluster-M03-patch-vcnew-utreview-api-v1-{DATE}",
            "cluster_code": CLUSTER,
            "session_ref": "M03 Phase 1 UT review via Claude API",
            "governing_instruction": "wa-sessionb-cluster-instruction-v2_2-20260516",
            "date": DATE,
            "terms_covered": terms_covered,
            "input_versions": input_versions,
            "op_count": len(ops),
            "source": "Claude API classification (Sonnet 4.6)",
            "provisional_anchor_promotions": provisional_anchor_promotions,
            "provisional_anchor_count": len(provisional_anchor_promotions),
        },
        "operations": ops,
    }


def write_log(by_term, classifications, patch, log_path):
    lines = [
        f"# WA-M03-UT-verse-review-api-v1-{DATE}",
        "",
        f"Phase 1 UT review for cluster M03 — Claude API classification of {sum(len(t['verses']) for t in by_term)} UT verses across {len(by_term)} terms.",
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
    lines.append("## Patch")
    lines.append("")
    lines.append(f"- File: `{patch['_patch_meta']['patch_id']}.json`")
    lines.append(f"- Operations: {patch['_patch_meta']['op_count']}")
    lines.append(f"- Terms covered: {len(patch['_patch_meta']['terms_covered'])}")
    log_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0,
                    help="Limit to first N terms (0=all). Useful for smoke test.")
    ap.add_argument("--dry-run-fetch", action="store_true",
                    help="Fetch + print UT load; do not call API.")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    by_term = fetch_ut_load(conn)
    if args.limit:
        by_term = by_term[: args.limit]
    n_verses = sum(len(t["verses"]) for t in by_term)
    print(f"M03 UT load: {len(by_term)} terms · {n_verses} verses")
    for t in by_term:
        print(f"  {t['strongs']:<8} {t['translit']:<18} {len(t['verses'])} UT verses")

    if args.dry_run_fetch:
        print("\n[--dry-run-fetch] No API calls made.")
        return 0

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

    patch = build_vcnew_patch(conn, by_term, classifications)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PATCH_PATH.write_text(json.dumps(patch, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nPatch: {PATCH_PATH}  ({patch['_patch_meta']['op_count']} ops)")

    RAW_PATH.write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Raw responses: {RAW_PATH}")

    write_log(by_term, classifications, patch, LOG_PATH)
    print(f"Log: {LOG_PATH}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
