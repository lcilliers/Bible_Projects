"""M10c Phase 1 UT review via Claude API.

Classifies the 58 UT verse-term pairs (verse_records without verse_context rows)
for cluster M10c — Defilement and Impurity (post-split, 2026-05-22).
8 terms total; 2 with UT > 0 (both ta.me — the verb H2930A and the adjective H2931).

UT load per inventory 2026-05-26: H2930A ta.me (verb) 19, H2931 ta.me (unclean) 39
— total 58 verses across 2 terms (other 6 terms UT=0).

Inherited: 217 verse_context rows already exist (all is_relevant=1) — these were
classified under the pre-split M10 cluster and travelled with the terms when the
split assigned them to M10c. Per §4.1 they are NOT re-classified by Phase 1.

Modeled on scripts/_apply_m10b_ut_review_via_api_20260525.py.
Per cluster-instruction v2_8 §4.
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
CLUSTER = "M10c"
MODEL = "claude-sonnet-4-6"
CHUNK_SIZE = 50
MAX_TOKENS = 12000
OUT_DIR = Path("Sessions/Session_Clusters/M10c")
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
PATCH_PATH = OUT_DIR / f"wa-cluster-M10c-patch-vcnew-utreview-api-v1-{DATE}.json"
LOG_PATH = OUT_DIR / f"wa-cluster-M10c-ut-verse-review-api-v1-{DATE}.md"
RAW_PATH = OUT_DIR / f"wa-cluster-M10c-ut-api-raw-responses-v1-{DATE}.json"


SYSTEM_PROMPT = """You are Claude AI performing Phase 1 (UT verse review) for the Session B cluster analysis of M10c — Defilement and Impurity (post-split, 2026-05-22).

CLUSTER M10c — DOMAIN

M10c owns the STATE of UNCLEANNESS — the inner-being condition produced by ritual or moral defilement, and the response to it (cleansing). M10c sits between two sibling clusters created by the same 2026-05-22 split:

  - M10 (Sin, Guilt and Transgression) — owns the ACT/STATE/EXPERIENCE of moral failure. Sinning produces guilt; defilement renders unclean. Distinct registers: sin = something I have done; uncleanness = a state I am in.
  - M10b (Wickedness, Evil and Abomination) — owns the CHARACTER of evil. Abomination as moral-character judgement (to.e.vah, shiq.quts, bdelugma) belongs to M10b. Ritual abomination (dietary lists, cultic taboo) overlaps with M10c.

M10c is the verse's home when the verse's content names:

  - Ritual / cultic uncleanness rendered by contact: corpses, leprosy, menstruation (nid.dah), bodily emissions, unclean animals, sin-offerings — what defiles, what is defiled, the process of defilement, the period of separation.
  - Unclean as state-condition: the person or thing in their rendered-unclean state (ta.me adjective, akathartos). The separation from the holy, the time-bounded exclusion.
  - Inner moral defilement (NT-distinctive register): heart-defilement (Mat 15:18–20 "what comes out of the heart defiles"), conscience-defilement (Tit 1:15 "to the defiled both their mind and conscience are defiled"), moral-impurity-as-defilement (akatharsia in NT vice lists), 2Cor 7:1 "let us cleanse ourselves from every defilement of body and spirit."
  - Defilement of land, sanctuary, name, covenant — extended ritual-and-moral defilement where the unclean state crosses from individual to corporate.
  - Cleansing / purification — the response to defilement: washing, sacrifice, time-passage, eventually Christ's cleansing. Verses where cleansing is the focus are M10c-relevant when they presuppose the defiled state.

WHAT IS NOT M10c (sibling clusters)

If a verse evidences a SINFUL ACT — what someone DID — it belongs to M10, not M10c. Example: "cha.ta" (sinned) of a specific act is M10's territory; "ta.me" (became unclean) of the resulting state is M10c.

If a verse evidences EVIL CHARACTER — the moral kind of a person/conduct — it belongs to M10b, not M10c. Example: ra.sha (the wicked person), to.e.vah as moral-abomination judgement (idolatry as detestable) belong to M10b.

If a verse uses a defilement term in a purely literal NON-religious sense (an ordinary physical stain with no ritual or moral framing), it is outside M10c.

CLASSIFICATION RUBRIC — three values

  relevant — the verse evidences the term's inner-being content within M10c's defilement-state register.

  set_aside — the term appears in this verse but does NOT carry M10c's defilement-state content. Valid grounds (per instruction v2_8 §4.5.1):
    (a) "No inner-being state evidenced — verse describes external ritual procedure / dietary list / formulaic phrasing only without inner-state content."
    (b) "Term here means X (literal non-defilement sense) — outside M10c scope." Name the verse's actual sense.
    (c) "Out-of-scope by design — verse evidences ACT-of-moral-failure (→ M10) or EVIL-CHARACTER (→ M10b), not defilement-state." Name which sibling.

  borderline — the verse meaning is genuinely ambiguous and needs researcher decision. Use sparingly; do NOT use as a hedge when the evidence is clear.

FORBIDDEN GROUNDS for set_aside (instruction §4.5.1)

You may NOT use any of the following as a reason for SET_ASIDE or BORDERLINE:
  - "Not God-directed" / "no clear vertical framing"
  - "Lacks theological depth" / "no spiritual category named"
  - "Inner state too mundane" / "too circumstantial"
  - "Inner state too negative" / "too corrupt to be inner being"
  - "Inner state is bodily / sensory rather than spiritual"   ← CRITICAL for M10c

INNER BEING — full scope reminder (M10c-specific)

Inner being covers the ENTIRE range of human interior states — vertical and horizontal, positive and negative, righteous and corrupt, sensory and volitional. **M10c is the cluster about bodily/material/ritual defilement extending into the inner being.** Do NOT set_aside because the defilement is "merely physical" — bodily defilement OF the inner person is exactly the cluster's content. The unclean state of the body is itself an inner-being state.

Classify SET_ASIDE only when no inner-being state of any kind is evidenced (e.g., the verse is a pure dietary-list entry with no inner content), or when the term's sense in this verse falls outside M10c's defilement-state register (act/moral-character/literal-physical-non-religious/lexical).

T1 FRAMEWORK — what an M10c-relevant verse must show

A verse evidences M10c's characteristic when its content names one or more of:

  1. Constitutional location — heart / soul / conscience / body / land / sanctuary described as defiled, polluted, unclean, made unclean by contact.
  2. Inner-being state — the person in their unclean state, the conscience defiled, the heart that defiles, the inner faculty rendering itself or others unclean.
  3. Source / mechanism of defilement — what causes the unclean state: corpse, leprosy, menstrual flow, bodily emission, unclean animal, idolatrous practice, moral act spreading uncleanness.
  4. Structural opposite — uncleanness vs holiness; defilement vs purity; polluted vs cleansed.
  5. Cleansing response — the act of being made clean, the time-passage of separation, the priest declaring clean, Christ's cleansing.
  6. Corporate defilement — defiling the land, sanctuary, name, covenant, people — where the unclean state extends beyond the individual.

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
  - Name the verse's actual sense of the term (e.g. "ta.me used in a dietary-list entry with no inner-state content"; "ta.me of a literal physical stain unrelated to ritual or moral defilement").
  - End with one of:
      " — outside M10c defilement-state scope."
      " — belongs to M10 act-of-moral-failure."
      " — belongs to M10b evil-character."
"""


def fetch_ut_load(conn) -> list[dict]:
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
        parts.append("---")
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


def _call_api_once(client, term, verses_chunk, max_retries=2):
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


def classify_term(client, term, max_retries=2):
    verses = term["verses"]
    if len(verses) <= CHUNK_SIZE:
        return _call_api_once(client, term, verses, max_retries)
    combined_results = []
    combined_usage = {"input_tokens": 0, "output_tokens": 0, "cache_creation": 0, "cache_read": 0}
    raw_chunks = []
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


def _existing_anchor_count(conn, mti_id):
    return conn.execute(
        "SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND is_anchor=1 "
        "AND COALESCE(delete_flagged,0)=0",
        (mti_id,)
    ).fetchone()[0]


def build_vcnew_patch(conn, by_term, classifications):
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
                reason = r.get("set_aside_reason") or "outside M10c defilement-state scope"
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
            "patch_id": f"wa-cluster-M10c-patch-vcnew-utreview-api-v1-{DATE}",
            "cluster_code": CLUSTER,
            "session_ref": "M10c Phase 1 UT review via Claude API (post-split)",
            "governing_instruction": "wa-sessionb-cluster-instruction-v2_8-20260519",
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
        f"# wa-cluster-M10c-ut-verse-review-api-v1-{DATE}",
        "",
        f"Phase 1 UT review for cluster M10c (Wickedness, Evil and Abomination — post-split). "
        f"Claude API classification of {sum(len(t['verses']) for t in by_term)} fresh UT "
        f"verses across {len(by_term)} terms (only terms with verses lacking verse_context rows).",
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
    lines.append("## Set-aside entries (full list with reasons)")
    lines.append("")
    for term in by_term:
        results = classifications.get(term["mti_id"], [])
        for r in results:
            if r.get("classification") == "set_aside":
                lines.append(f"- **{term['strongs']} {term['translit']}** "
                             f"vr={r.get('vr_id')} {r.get('reference')} — "
                             f"{r.get('set_aside_reason') or r.get('rationale','')}")

    lines.append("")
    lines.append("## Patch")
    lines.append("")
    lines.append(f"- File: `{patch['_patch_meta']['patch_id']}.json`")
    lines.append(f"- Operations: {patch['_patch_meta']['op_count']}")
    lines.append(f"- Terms covered: {len(patch['_patch_meta']['terms_covered'])}")
    log_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run-fetch", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    by_term = fetch_ut_load(conn)
    if args.limit:
        by_term = by_term[: args.limit]
    n_verses = sum(len(t["verses"]) for t in by_term)
    print(f"M10c UT load: {len(by_term)} terms · {n_verses} verses")
    for t in by_term:
        print(f"  {t['strongs']:<8} {t['translit']:<18} {len(t['verses'])} UT verses")

    if args.dry_run_fetch:
        print("\n[--dry-run-fetch] No API calls made.")
        return 0

    client = anthropic.Anthropic()
    print(f"\nModel: {MODEL}\n")

    classifications = {}
    raw = []
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
