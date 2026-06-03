"""M38 Salvation — Phase A UT review via Claude API (rigorous path).

Per v3_0 §5.1 — classifies each active verse in the M38 cluster's term set for
inner-being relevance under the M38 lens. Differs from prior cluster-split UT
review scripts in that it operates on BOTH gap verses (no verse_context row)
AND existing verses (inherited verse_context from prior registry-level work).

Rigorous-path rationale (researcher direction 2026-05-28):
  The 320 inherited verse_context records came from 6 different owning registries
  (mercy, debauchery, division, yielding, strength, power) each with its own
  inner-being lens. The is_relevant=1 verdict under those lenses may not equate
  to is_relevant=1 under M38's salvation/atonement/gift lens. Re-classify all.

Usage:
  python scripts/_apply_m38_ut_review_via_api_20260528.py [--limit N] [--dry-run-fetch]

Outputs (under Sessions/Session_Clusters/M38/):
  - wa-cluster-M38-patch-utreview-api-v1-20260528.json         (combined VCNEW + VCREVISE)
  - wa-cluster-M38-ut-verse-review-api-v1-20260528.md          (per-term log)
  - wa-cluster-M38-ut-api-raw-responses-v1-20260528.json       (raw API responses)
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
CLUSTER = "M38"
MODEL = "claude-sonnet-4-6"
CHUNK_SIZE = 50
MAX_TOKENS = 12000
OUT_DIR = Path("Sessions/Session_Clusters/M38")
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
PATCH_PATH = OUT_DIR / f"wa-cluster-M38-patch-utreview-api-v1-{DATE}.json"
LOG_PATH = OUT_DIR / f"wa-cluster-M38-ut-verse-review-api-v1-{DATE}.md"
RAW_PATH = OUT_DIR / f"wa-cluster-M38-ut-api-raw-responses-v1-{DATE}.json"


SYSTEM_PROMPT = """You are Claude AI performing Phase A UT (Universe of Terms) review for the v3_0 Session B cluster analysis of M38 — Salvation.

CLUSTER M38 — TERM INVENTORY AND PROVISIONAL CHARACTERISTIC

M38's 13 active mti_terms span three related semantic registers. Phase A UT review classifies whether each verse evidences inner-being content relevant to any of these registers — without pre-judging whether the three integrate into one cluster characteristic (that is a Phase B question).

  1. Salvation / rescue / deliverance vocabulary
     - G4982 sōzō (to save), G4990 sōtēr (savior), G4991 soteria (salvation), G4992 sōtērion (saving)
     - H3444 ye.shu.ah (salvation), H6299 pa.dah (to ransom)
     The rescue, deliverance, salvation proper — what God does in saving the person; the inner-being state of being saved/rescued/ransomed.

  2. Propitiation / atonement vocabulary
     - G2433 hilaskomai (to propitiate), G2434 hilasmos (propitiation), G2435 hilastērios (propitiation/mercy-seat), G2436 hileōs (propitious/gracious)
     - H3722B ka.phar (to cover/atone)
     The means by which salvation is effected — atonement covering sin; the inner-being state of being atoned-for; mercy received through propitiation.

  3. Giving / gift vocabulary where context is salvation-relevant
     - G1431 dōrea (free gift), G1434 dōrēma (free gift)
     Where the giving carries a salvation-relevant inner-being signal (e.g., the gift of salvation, the gift of righteousness, the gift of the Spirit). NOT general giving — only where the gift's inner-being content concerns salvation, redemption, or the salvific economy.

A VERSE IS M38-RELEVANT (IB) WHEN ITS CONTENT NAMES

The inner-being content of being saved, ransomed, rescued, atoned-for, covered, or receiving salvation as gift. This includes:

  - The state of the person who has been delivered or rescued (from danger, enemies, sin, death)
  - The state of the person being healed/saved in a spiritually-significant sense
  - The inner-being condition of being propitiated/atoned-for, of having sin covered
  - God's saving action affecting the inner being of the person saved
  - The inner-being state of receiving a salvation-relevant gift
  - The hope, expectation, or assurance of salvation as an inner-being reality
  - The inner-being response to deliverance (gratitude, trust, joy at being saved)
  - The community's collective inner-being state of being a saved/redeemed people
  - Constitutional location named: heart/soul/conscience saved, atoned, covered, ransomed
  - Mechanism of salvation: how the rescue/atonement reaches the inner being

A VERSE IS NOT M38-RELEVANT (SET_ASIDE) WHEN

  (a) Physical-only deliverance with no inner-being state — e.g., a battle-rescue narrative with no inner-being content beyond the bare physical act.
  (b) The term in this verse means something outside the three registers — e.g., ka.phar used in a non-atonement architectural sense ("covered with pitch"); pa.dah of a non-salvation legal redemption transaction without inner content; sōzō purely physical-medical without spiritual register.
  (c) The gift terms (dōrea, dōrēma) where the giving is general (e.g., spiritual gifts to the church for service, NOT salvation; or material gifts; or gifts to fulfil prophecy with no salvation-specific inner content). NAME the actual sense.
  (d) Title-only use of "Savior" with no inner-being content (e.g., a doxological greeting that names the title but does not engage the inner-being state).
  (e) Reference to salvation as historical-narrative reportage with no inner-being content named.

CLASSIFICATION RUBRIC — three values

  relevant — the verse evidences inner-being content within one of M38's three registers.

  set_aside — the term appears but the verse does NOT carry M38's inner-being content. Valid grounds:
    (a) "No inner-being state evidenced — verse describes only external/physical/procedural content."
    (b) "Term here means X (literal non-salvation sense) — outside M38 scope." Name the verse's actual sense.
    (c) "Out-of-scope by design — verse evidences general giving / general healing / titular doxology without salvation-specific inner-being content."

  borderline — the verse meaning is genuinely ambiguous and needs researcher decision. Use sparingly; do NOT use as a hedge when the evidence is clear.

FORBIDDEN GROUNDS for set_aside

You may NOT use any of the following as a reason for SET_ASIDE or BORDERLINE:
  - "Not God-directed" / "no clear vertical framing" — horizontal salvation/rescue is in scope
  - "Lacks theological depth" — depth is not the gate; inner-being content is
  - "Too narratively concrete" — concrete narrative inner-being states are in scope
  - "Too physical" — physical rescue WITH inner-being content (fear, hope, gratitude, trust) is in scope; only pure-physical-without-inner-being is set_aside
  - "Too OT" / "Too NT" — both testaments equally in scope
  - "Inner state too negative" — inner-being state of being unsaved/perishing is also in scope when it provides the structural opposite that the salvation-state implies

INNER BEING — full scope reminder

Inner being covers the ENTIRE range of human interior states — vertical and horizontal, positive and negative, theological and ordinary. M38 is the cluster about salvation/atonement/gift as inner-being realities. Do NOT set_aside because the salvation is "too physical" or "too narrative" — the inner being of the rescued person is exactly the cluster's content.

A SPECIFIC TENSION TO WATCH

The OT corpus (sōzō LXX background, ye.shu.ah, pa.dah, ka.phar) frequently describes physical rescue from physical enemies. Many such verses ALSO carry inner-being content: the inner state of the rescued (relief, trust, gratitude), the inner state before rescue (fear, desperation), the corporate inner-being of the saved community. Classify these as RELEVANT when the verse evidences ANY inner-being content alongside the physical rescue, even if the inner-being content is implicit in the narrative texture.

Classify as SET_ASIDE only when the verse contains no inner-being content at all — pure physical event narration, formal lists, or technical procedural matter.

OUTPUT FORMAT — strict JSON

Respond with exactly one JSON array. One object per verse, in the same order the verses were given. Each object MUST have these fields:

  {
    "vr_id": <integer — copy from input>,
    "reference": "<string — copy from input>",
    "classification": "relevant" | "set_aside" | "borderline",
    "rationale": "<one-sentence reason, max 250 chars>",
    "set_aside_reason": "<populated only if classification='set_aside', otherwise empty string>"
  }

Do not include any text outside the JSON array. No prose, no preamble, no markdown fence.

When classification is "set_aside", the set_aside_reason field must:
  - Be one line, plain English, max 200 chars
  - Name the verse's actual sense of the term
  - End with " — outside M38 salvation/atonement/gift scope."
"""


def fetch_all_m38_verses(conn) -> list[dict]:
    """Fetch all active verses for M38 terms, plus their existing vc state if any."""
    rows = list(conn.execute("""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.md_version,
               vr.id AS vr_id, vr.reference, vr.verse_text, vr.target_word,
               vr.context_before, vr.context_after, vr.translation,
               vc.id AS existing_vc_id, vc.is_relevant AS existing_is_rel,
               vc.is_anchor AS existing_is_anchor, vc.is_related AS existing_is_related
          FROM mti_terms mt
          JOIN wa_verse_records vr ON vr.mti_term_id = mt.id
          LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id
                                     AND vc.mti_term_id = mt.id
                                     AND COALESCE(vc.delete_flagged,0)=0
         WHERE mt.cluster_code = ?
           AND COALESCE(mt.delete_flagged,0) = 0
           AND COALESCE(vr.delete_flagged,0) = 0
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
            "existing_vc_id": r["existing_vc_id"],
            "existing_is_rel": r["existing_is_rel"],
            "existing_is_anchor": r["existing_is_anchor"],
            "existing_is_related": r["existing_is_related"],
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
        parts.append(f"target_word: {v['target_word']}")
        parts.append(f"context_before: {v['context_before']}")
        parts.append(f"verse_text ({v['translation']}): {v['verse_text']}")
        parts.append(f"context_after: {v['context_after']}")
        parts.append("")
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


def build_patch(by_term, classifications):
    """Build mixed patch.

    For each classified verse, decide:
      - GAP + relevant  → INSERT vc row with is_relevant=1
      - GAP + set_aside → INSERT vc row with is_relevant=0 + set_aside_reason
      - EXISTING + relevant + already is_relevant=1 → NO-OP
      - EXISTING + set_aside + currently is_relevant=1 → UPDATE to is_relevant=0 + set_aside_reason
      - EXISTING + set_aside + currently is_relevant=0 → NO-OP (already set aside)
      - borderline → held back from patch for researcher review
    """
    ops = []
    seq = 1
    terms_covered = []
    input_versions = {}
    stats = {
        "inserts_relevant": 0,
        "inserts_set_aside": 0,
        "updates_to_set_aside": 0,
        "no_op_existing_relevant": 0,
        "no_op_existing_set_aside": 0,
        "borderlines": 0,
    }

    for term in by_term:
        mti = term["mti_id"]
        terms_covered.append(mti)
        input_versions[str(mti)] = term["md_version"] or 1
        results = classifications.get(mti, [])
        by_vr = {r.get("vr_id"): r for r in results}

        for v in term["verses"]:
            r = by_vr.get(v["vr_id"])
            if not r:
                continue
            cls = r.get("classification")
            existing_vc_id = v["existing_vc_id"]
            existing_is_rel = v["existing_is_rel"]

            if cls == "borderline":
                stats["borderlines"] += 1
                continue

            if cls == "relevant":
                if existing_vc_id is None:
                    # Gap verse — insert
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
                            "is_relevant": 1,
                            "is_related": 0,
                            "delete_flagged": 0,
                            "vertical_pass_flag": 0,
                        }
                    })
                    seq += 1
                    stats["inserts_relevant"] += 1
                elif existing_is_rel == 1:
                    # Existing row already is_relevant=1 — no op
                    stats["no_op_existing_relevant"] += 1
                else:
                    # Existing row is_relevant=0 but new verdict is relevant — update
                    ops.append({
                        "op_id": f"OP-{seq:03d}",
                        "table": "verse_context",
                        "operation": "update",
                        "match": {"id": existing_vc_id},
                        "set": {
                            "is_relevant": 1,
                            "set_aside_reason": None,
                        }
                    })
                    seq += 1
                    stats["updates_to_set_aside"] += 1  # reused counter; will rename

            elif cls == "set_aside":
                reason = r.get("set_aside_reason") or "outside M38 salvation/atonement/gift scope"
                if existing_vc_id is None:
                    # Gap verse — insert as set_aside
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
                    stats["inserts_set_aside"] += 1
                elif existing_is_rel == 1:
                    # Existing row is_relevant=1 but new verdict is set_aside — update
                    ops.append({
                        "op_id": f"OP-{seq:03d}",
                        "table": "verse_context",
                        "operation": "update",
                        "match": {"id": existing_vc_id},
                        "set": {
                            "is_relevant": 0,
                            "set_aside_reason": reason,
                        }
                    })
                    seq += 1
                    stats["updates_to_set_aside"] += 1
                else:
                    # Existing row already is_relevant=0 — no op
                    stats["no_op_existing_set_aside"] += 1

    return {
        "_patch_meta": {
            "patch_type": "VCREVISE",
            "patch_id": f"wa-cluster-M38-patch-utreview-api-v1-{DATE}",
            "cluster_code": CLUSTER,
            "session_ref": "M38 Phase A UT review (rigorous re-classification across cluster + gap verses)",
            "governing_instruction": "wa-sessionb-cluster-instruction-v3_0-20260527",
            "date": DATE,
            "terms_covered": terms_covered,
            "input_versions": input_versions,
            "op_count": len(ops),
            "source": "Claude API classification (Sonnet 4.6)",
            "stats": stats,
        },
        "operations": ops,
    }


def write_log(by_term, classifications, patch, log_path, total_usage):
    lines = [
        f"# wa-cluster-M38-ut-verse-review-api-v1-{DATE}",
        "",
        f"Phase A UT review for cluster M38 — Salvation (rigorous re-classification path). "
        f"Claude API classification of {sum(len(t['verses']) for t in by_term)} verses across "
        f"{len(by_term)} terms (all active verses, including those with inherited verse_context rows).",
        "",
        "## Per-term counts",
        "",
        "| Strong's | Translit | Gloss | Total | Relevant | Set aside | Borderline |",
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
    lines.append("## Patch summary")
    lines.append("")
    stats = patch["_patch_meta"]["stats"]
    lines.append(f"- Inserts (relevant): {stats['inserts_relevant']}")
    lines.append(f"- Inserts (set_aside): {stats['inserts_set_aside']}")
    lines.append(f"- Updates (existing flipped to set_aside or restored to relevant): {stats['updates_to_set_aside']}")
    lines.append(f"- No-op (existing already correct as relevant): {stats['no_op_existing_relevant']}")
    lines.append(f"- No-op (existing already set_aside): {stats['no_op_existing_set_aside']}")
    lines.append(f"- Borderlines held back: {stats['borderlines']}")
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
                lines.append(f"- **{term['strongs']} {term['translit']}** vr_id={r.get('vr_id')} {r.get('reference')}")
                lines.append(f"  rationale: {r.get('rationale')}")
                if v:
                    lines.append(f"  verse: {v['verse_text']}")
                lines.append("")
    if not any_bd:
        lines.append("(none)")
    lines.append("")
    lines.append("## Set-aside entries — accepted into patch")
    lines.append("")
    for term in by_term:
        results = classifications.get(term["mti_id"], [])
        by_vr = {v["vr_id"]: v for v in term["verses"]}
        term_sas = [r for r in results if r.get("classification") == "set_aside"]
        if not term_sas:
            continue
        lines.append(f"### {term['strongs']} {term['translit']} — {len(term_sas)} set_aside")
        lines.append("")
        for r in term_sas[:20]:  # cap at 20 per term to keep log readable
            v = by_vr.get(r.get("vr_id"))
            ref = v["reference"] if v else r.get("reference")
            lines.append(f"- {ref} — {r.get('set_aside_reason')}")
        if len(term_sas) > 20:
            lines.append(f"  ... and {len(term_sas)-20} more")
        lines.append("")
    lines.append("## API usage")
    lines.append("")
    lines.append(f"- Input tokens: {total_usage['input_tokens']:,}")
    lines.append(f"- Output tokens: {total_usage['output_tokens']:,}")
    lines.append(f"- Cache creation: {total_usage['cache_creation']:,}")
    lines.append(f"- Cache read: {total_usage['cache_read']:,}")
    log_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="Process only first N terms (testing)")
    ap.add_argument("--dry-run-fetch", action="store_true", help="Fetch and report; no API call")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    by_term = fetch_all_m38_verses(conn)
    if args.limit:
        by_term = by_term[:args.limit]

    print(f"Fetched {sum(len(t['verses']) for t in by_term)} verses across {len(by_term)} terms")
    if args.dry_run_fetch:
        for t in by_term:
            existing = sum(1 for v in t['verses'] if v['existing_vc_id'] is not None)
            gap = len(t['verses']) - existing
            print(f"  {t['strongs']:8s} {t['translit'] or '':18s} {len(t['verses']):4d} verses (existing={existing}, gap={gap})")
        return

    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY not in env or .env", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic()
    classifications: dict[int, list] = {}
    raw_responses: dict[int, str] = {}
    total_usage = {"input_tokens": 0, "output_tokens": 0, "cache_creation": 0, "cache_read": 0}

    for i, term in enumerate(by_term, 1):
        print(f"\n[{i}/{len(by_term)}] {term['strongs']} {term['translit']} ({len(term['verses'])} verses)", end="", flush=True)
        try:
            results, usage, raw_text = classify_term(client, term)
            classifications[term["mti_id"]] = results
            raw_responses[term["mti_id"]] = raw_text
            for k in total_usage:
                total_usage[k] += usage[k]
            print(f" — done ({usage['input_tokens']}+{usage['output_tokens']} tokens)")
        except Exception as e:
            print(f" — ERROR: {e}")
            classifications[term["mti_id"]] = []
            raw_responses[term["mti_id"]] = f"ERROR: {e}"

    patch = build_patch(by_term, classifications)
    PATCH_PATH.write_text(json.dumps(patch, indent=2), encoding="utf-8")
    write_log(by_term, classifications, patch, LOG_PATH, total_usage)
    RAW_PATH.write_text(json.dumps(raw_responses, indent=2), encoding="utf-8")

    print(f"\n\nPatch:    {PATCH_PATH}")
    print(f"Log:      {LOG_PATH}")
    print(f"Raw:      {RAW_PATH}")
    print(f"\nTotal API tokens: input={total_usage['input_tokens']:,} output={total_usage['output_tokens']:,} cache_read={total_usage['cache_read']:,}")
    print(f"Patch ops: {patch['_patch_meta']['op_count']}")
    print(f"Stats: {patch['_patch_meta']['stats']}")


if __name__ == "__main__":
    main()
