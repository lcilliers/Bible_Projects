"""M10b Phase 1 UT review via Claude API.

Classifies the 134 UT verse-term pairs (verse_records without verse_context rows)
for cluster M10b — Wickedness, Evil and Abomination (post-split, 2026-05-22).
17 terms total; 7 with UT > 0.

UT load per inventory 2026-05-25: H8441 to.e.vah 87, H8251 shiq.quts 22,
G4190 ponēros 10, H7455 ro.a 5, H7563 ra.sha 3, G0946 bdelugma 3, G0824 atopos 2,
G0093 adikia 2 — total 134 verses across 7 terms (others UT=0).

Inherited: 422 verse_context rows already exist (all is_relevant=1) — these were
classified under the pre-split M10 cluster and travelled with the terms when the
split assigned them to M10b. Per §4.1 they are NOT re-classified by Phase 1.

Modeled on scripts/_apply_m10_ut_review_via_api_20260522.py.
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
CLUSTER = "M10b"
MODEL = "claude-sonnet-4-6"
CHUNK_SIZE = 50
MAX_TOKENS = 12000
OUT_DIR = Path("Sessions/Session_Clusters/M10b")
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
PATCH_PATH = OUT_DIR / f"wa-cluster-M10b-patch-vcnew-utreview-api-v1-{DATE}.json"
LOG_PATH = OUT_DIR / f"wa-cluster-M10b-ut-verse-review-api-v1-{DATE}.md"
RAW_PATH = OUT_DIR / f"wa-cluster-M10b-ut-api-raw-responses-v1-{DATE}.json"


SYSTEM_PROMPT = """You are Claude AI performing Phase 1 (UT verse review) for the Session B cluster analysis of M10b — Wickedness, Evil and Abomination (post-split, 2026-05-22).

CLUSTER M10b — DOMAIN

M10b owns the CHARACTER of evil — the moral nature of a person, conduct, or thing as named by the term. M10b sits between two sibling clusters created by the same 2026-05-22 split:

  - M10 (Sin, Guilt and Transgression) — owns the ACT/STATE/EXPERIENCE of moral failure. What was done (the sinful act, the transgression, the iniquitous deed), the guilt incurred by it, the inner state of one who has transgressed.
  - M10c (Defilement and Impurity) — owns the RITUAL/CULTIC UNCLEANNESS register. Uncleanness rendered through contact with what defiles (corpses, leprosy, menstruation, dietary taboo, ritual taboo).

M10b is the verse's home when the verse's content names:

  - A wicked person — the moral character of the agent: ra.sha (the wicked one), mir.sha.at (the wicked-collective), kakopoios (an evildoer).
  - Evil as the abstract nature of conduct or being — kakia, ponēria, ponēros, faulos, re.sha, ro.a, adikia, atopos: what KIND of conduct or character this is, not what specific act was done.
  - Trouble/iniquity as the character of evildoing — a.ven (H0205G, the evil-character sub-entry; distinct from a.ven H0205H which stayed in M10 for the moral-collapse-state sense).
  - Abomination — what is named as detestable to God or to the moral order: to.e.vah, shiq.quts, bdelugma, bdeluktos. M10b owns the MORAL-CHARACTER side of abomination — what makes the practice / object / person detestable in moral terms.
  - Blasphemy as character expression — blasfēmeō (the verb, moved here from M10 as evil-character expression): speech that CHARACTERISES the speaker as evil-towards-God. (Note: the noun forms blasfēmia/blasfēmos remain in M10 as act-of-sin and act-doer-of-sin.)

WHAT IS NOT M10b (sibling clusters)

If a verse evidences an ACT of moral failure / a GUILTY STATE / the EXPERIENCE of one who has transgressed (without making the agent's CHARACTER the point), it belongs to M10, not M10b. Example: "all have sinned" — that is M10 (act of failure), not M10b (character of evil).

If a verse evidences RITUAL/CULTIC UNCLEANNESS — what is rendered unclean by contact, what is forbidden as ritually impure — it belongs to M10c, not M10b. The Hebrew abomination terms (especially to.e.vah and shiq.quts) sit on this boundary because abomination can be moral-character (idolatry as detestable, lying-lips as detestable) OR ritual-cultic (dietary lists, ritual taboo). Read each verse for which register dominates.

CLASSIFICATION RUBRIC — three values

  relevant — the verse evidences the term's inner-being content within M10b's evil-character register.

  set_aside — the term appears in this verse but does NOT carry M10b's evil-character content. Valid grounds (per instruction v2_8 §4.5.1):
    (a) "No inner-being state evidenced — the verse describes external events / lists / formulaic ritual only."
    (b) "Term here means X (literal, non-moral sense) — outside M10b evil-character scope." Name the verse's actual sense.
    (c) "Out-of-scope by design — verse evidences ACT-of-moral-failure (→ M10) or RITUAL DEFILEMENT (→ M10c), not evil-character." Name which sibling.

  borderline — the verse meaning is genuinely ambiguous and needs researcher decision. Use sparingly; do NOT use as a hedge when the evidence is clear.

FORBIDDEN GROUNDS for set_aside (instruction §4.5.1)

You may NOT use any of the following as a reason for SET_ASIDE or BORDERLINE:
  - "Not God-directed" / "no clear vertical framing"
  - "Lacks theological depth" / "no spiritual category named"
  - "Inner state too mundane" / "too circumstantial"
  - "Inner state too negative" / "too corrupt to be inner being"
  - "Inner state is bodily / sensory rather than spiritual"

INNER BEING — full scope reminder

Inner being covers the ENTIRE range of human interior states — vertical and horizontal, positive and negative, righteous and corrupt, sensory and volitional. For M10b specifically, the cluster IS about negative character — do not let "too negative" be a set_aside ground. Classify SET_ASIDE only when no inner-being state of any kind is evidenced in the verse, or when the term's sense in this verse falls outside M10b's evil-character register (act/ritual/literal/lexical).

T1 FRAMEWORK — what an M10b-relevant verse must show

A verse evidences M10b's characteristic when its content names one or more of:

  1. Constitutional location — heart / soul / will / mouth / disposition described as evil, wicked, abominable, perverse, harbouring corruption.
  2. Inner faculties engaged in evil — will choosing evil; cognition delighting in evil; affect harbouring corruption; conscience seared; speech expressing the evil-character of the speaker.
  3. Inner character or nature — the moral kind of person, conduct, or thing (a wicked agent; an abominable practice; an evil device; an unrighteous person).
  4. Structural opposite — wickedness vs righteousness; evil vs good; abomination vs holiness; unrighteousness vs justice.
  5. Direction or object — evil towards neighbour; abomination to YHWH; wicked against the poor; blasphemy against God.

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
  - Name the verse's actual sense of the term (e.g. "to.e.vah used of dietary taboo, not moral abomination"; "atopos meaning 'amiss' descriptively, not morally").
  - End with one of:
      " — outside M10b evil-character scope."
      " — belongs to M10 act-of-moral-failure."
      " — belongs to M10c ritual defilement."
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
                reason = r.get("set_aside_reason") or "outside M10b evil-character scope"
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
            "patch_id": f"wa-cluster-M10b-patch-vcnew-utreview-api-v1-{DATE}",
            "cluster_code": CLUSTER,
            "session_ref": "M10b Phase 1 UT review via Claude API (post-split)",
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
        f"# wa-cluster-M10b-ut-verse-review-api-v1-{DATE}",
        "",
        f"Phase 1 UT review for cluster M10b (Wickedness, Evil and Abomination — post-split). "
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
    print(f"M10b UT load: {len(by_term)} terms · {n_verses} verses")
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
