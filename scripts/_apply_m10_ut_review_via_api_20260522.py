"""M10 Phase 1 UT review via Claude API.

Classifies the 43 UT verse-term pairs (verse_records without verse_context rows)
for cluster M10 — Sin, Guilt and Transgression (post-split, 2026-05-22). 13 OWNER
terms remaining in the act/state-of-moral-failure track.

UT load (per inventory 2026-05-22): H5771I a.von 16, H0205H a.ven 7, H2254B
cha.val 6, H0816 a.sham 3, G1311 diaftheirō 2, H8397 te.vel 2, H2256D che.vel 1,
H2403I chat.tat 1, H4603 ma.al 1, H4604 ma.al 1, H5557 sa.laph 1, H5753A a.vah
1, H5766A a.vel 1 — total 43 verses.

The 1,436 verses already carrying verse_context rows pass by inheritance (all
remaining M10 terms are sin/guilt-track; none crossed the split boundary).
Modeled on scripts/_apply_m09_ut_review_via_api_20260521.py.
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
CLUSTER = "M10"
MODEL = "claude-sonnet-4-6"
CHUNK_SIZE = 50
MAX_TOKENS = 12000
OUT_DIR = Path("Sessions/Session_Clusters/M10")
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
PATCH_PATH = OUT_DIR / f"wa-cluster-M10-patch-vcnew-utreview-api-v1-{DATE}.json"
LOG_PATH = OUT_DIR / f"WA-M10-UT-verse-review-api-v1-{DATE}.md"
RAW_PATH = OUT_DIR / f"WA-M10-UT-api-raw-responses-{DATE}.json"


SYSTEM_PROMPT = """You are Claude AI performing Phase 1 (UT verse review) of the Session B cluster analysis for cluster M10 — Sin, Guilt and Transgression (post-split, 2026-05-22).

CLUSTER M10 — DOMAIN (POST-SPLIT)

M10 has been narrowed by a 2026-05-22 split. The cluster now names the inner-being experience of moral failure as ACT, STATE and EXPERIENCE — what was done, the guilt incurred by it, the standing before God it produced, the inner state of one who has transgressed. M10's characteristic-bearing scope:

  - **Sin as act / sin-incurred state** (hamartanō, cha.ta, hamartia, hamartēma, chet, cha.ta.ah, chat.ta.ah, chat.tat, hamartōlos, chat.ta, rish.ah).
  - **Guilt — both the legal/moral standing of having transgressed and the felt state of having done so** (a.sham, a.shem, ash.mah, a.von in its guilt/iniquity/punishment senses).
  - **Iniquity / crookedness — the moral twist that produces wrong acts** (a.vah, a.vel, a.vil, al.vah, av.lah, av.val, a.von, sa.laph "to pervert/twist", ho.phekh, la.zut, tah.pu.khah, mut.teh).
  - **Transgression as boundary-crossing** (parabainō, parabasis, parabatēs, paraptōma, pe.sha "to step over", pa.sha "to rebel/step across").
  - **Rebellion — the willful defiance dimension of transgression** (sa.rah, sur, apostasia).
  - **Unfaithfulness / treachery** (ba.gad "to act treacherously"; ma.al "to be unfaithful/break trust" — covenant or marital faithlessness).
  - **Corruption-as-act** (diaftheirō / ftheirō / fthora when of moral corruption produced by transgression; mash.chit / mash.chet / ma.she.chat as destructive corrupting acts).
  - **Slander / blasphemy as sinful act of speech** (blasfēmia / blasfēmos as the act and the speaker; not the same as blasfēmeō, which has been moved to M10b as evil-character expression).
  - **Injustice as a moral-failure act** (adikēma "crime"; adikos / mut.teh when of unjust act before God or neighbour).
  - **Atonement / cover-for-sin** (kip.pu.rim) — paired conceptually with sin as its remedy in the priestly system.
  - **Deceit / entrapment as sinful act** (deleazō "to entice/lure into sin").
  - **Hypocrisy — sin of false-appearance** (sunupokrinomai "to join in hypocrisy").
  - **Trouble / wickedness as state/condition of one who has sinned** (a.ven in its "trouble/iniquity" sense — when the inner state is that of one in moral collapse, NOT the abstract evil-as-character sense, which has moved to M10b).
  - **Writhing-in-guilt / pain of sin-aftermath** (cha.val, che.vel when of the inner agony produced by guilt — not all destruction senses).
  - **Lewdness / contempt as moral failure** (nav.lut).
  - **Perversion / pollution as moral-act** (te.vel "perversion of the right order" — confusion, defiling-act sense, NOT ritual impurity sense which is now M10c).
  - **Decay / dissolution of the inner being under sin** (cha.loph in moral-decay sense; pu.qah as grief-of-guilt; sin-grief).
  - Structural opposites in view: righteousness, innocence, integrity, faithfulness, repentance, restoration.

WHAT IS NO LONGER M10 (SPLIT-OFF SIBLINGS)

After the 2026-05-22 split, M10 NO LONGER includes:

  - **M10b — Wickedness, Evil and Abomination** (character-of-evil track): kakia, ponēria, ponēros, faulos, kakopoios, atopos, blasfēmeō, adikia, re.sha, ra.sha, mir.sha.at, to.e.vah, shiq.quts, bdelugma, bdeluktos, a.ven (in evil-character sense), ro.a. If a verse evidences EVIL/WICKEDNESS AS CHARACTER (what kind of person the agent is, what kind of nature this conduct has), it belongs to M10b — not M10. M10 owns the act-of-failure side; M10b owns the character-of-evil side.

  - **M10c — Defilement and Impurity** (ritual/moral-defilement track): ta.me, nid.dah, akatharsia, akathartos, molunō, molusmos, miasmos. If a verse evidences DEFILEMENT / IMPURITY / UNCLEANNESS (the state rendered to a person or thing through contact with what defiles), it belongs to M10c — not M10.

For Phase 1 the practical relevance is small: the M10 UT load does not include any M10b or M10c terms. The split-line still matters because some M10 terms (e.g. te.vel "perversion", a.ven "trouble") sit close to the M10b/M10c boundary, and ambiguous verses should be set_aside (with a reason pointing to the sibling cluster) rather than forced into M10.

CRITICAL DISAMBIGUATION

Several M10 UT terms operate across distinct senses:

  - **te.vel (H8397 "perversion / pollution")**: appears twice in OT. M10 owns the MORAL-ACT sense (a perverse mixing, a defiling act of intentional moral perversion — e.g. Lev 18:23, 20:12 of bestiality/incest "it is te.vel"). It does NOT cover the abstract ritual-impurity state (which is M10c territory). Both Lev 18:23 and Lev 20:12 are M10-relevant (moral perversion-act).

  - **diaftheirō (G1311 "to destroy / corrupt")**: M10 owns the MORAL-CORRUPTION sense — to corrupt one's heart, mind, or way (e.g. 1Ti 6:5, 2Co 7:2 "we have corrupted no one"). It does NOT own physical destruction (city destroyed; physical decay), which is set_aside as outside the moral-failure register.

  - **a.von (H5771I "iniquity: crime/guilt/punishment")**: H5771I is the sub-entry for the guilt-and-punishment branch of a.von's three senses. M10 owns it. Every Phase 1 UT verse for H5771I should be a guilt/iniquity verse — confirm relevance unless the verse uses a.von purely abstractly (rare).

  - **a.ven (H0205H "trouble / iniquity")**: H0205H is the sub-entry for the trouble/distress branch. M10 owns it when the verse evidences moral-trouble-as-state-of-one-who-has-sinned (the inner condition of one in moral collapse). It does NOT own a.ven when used of mere physical trouble / calamity without moral-failure framing. Note: H0205G (the parallel a.ven sub-entry) has moved to M10b in the split.

  - **cha.val (H2254B "to writhe / be in agony")**: M10 owns it when the verse evidences GUILT-AGONY — the inner writhing produced by transgression (e.g. Ezekiel "the soul writhes"). Mere physical pain or labour-pain (chol "to bring forth") is set_aside.

  - **che.vel (H2256D "destruction / pang")**: small sub-entry; M10 owns it when the verse names destruction-of-one-under-judgment-for-sin or birth-pang-as-image-of-guilt. Mere rope/measuring-line uses are set_aside (different lexical sense).

  - **a.sham (H0816 "to be guilty / incur guilt")**: M10 owns the inner-being side — being guilty before God, bearing guilt. Ritual guilt-offering uses (sacrificial-context) are still M10 if they evidence the guilty-state; pure cultic vocabulary without state-content is set_aside.

  - **chat.tat (H2403I "sin: punishment")**: H2403I is the punishment sub-entry of chat.tat. M10 owns it when the verse names the consequence of sin borne by the sinner.

  - **ma.al (H4603/H4604 "to act unfaithfully / unfaithfulness")**: M10 owns the act/state of covenant-breaking, marital-faithlessness, sacrilege (Achan's ma.al at Jericho; Israel's ma.al against God). External lists / formal-cultic mentions without inner-failure content are set_aside.

  - **sa.laph (H5557 "to pervert")**: M10 owns it when the verse names the perverting of justice, way, or word. Physical "twist/distort" without moral content is set_aside.

  - **a.vah (H5753A "to commit iniquity / twist")**: M10 owns the moral-twisting sense. Pure physical bending/twisting is set_aside.

  - **a.vel (H5766A "injustice")**: M10 owns it when of moral injustice / unrighteous act. Pure measurement-injustice (false balances) is still M10 if framed as moral failure; flat lexical mentions are set_aside.

When in doubt: ask whether the verse evidences MORAL FAILURE AS ACT / STATE / EXPERIENCE (M10 territory), or only physical / cultic / lexical use of the term (set_aside). Where the verse points to evil-character or defilement, set_aside with a one-line reason noting the sibling cluster.

T1 FRAMEWORK — what a characteristic-bearing inner-being verse must show

A verse evidences M10's characteristic when its content names one or more of:
  1. Constitutional location — heart / soul / conscience described as guilty, sinful, transgressing, perverted, broken under sin; or as harbouring iniquity.
  2. Inner faculties engaged — will choosing wrong; cognition recognising the failure; affect bearing guilt/shame; conscience accusing.
  3. Inner impact — sin's effect on the person (cuts off from God, brings judgment, requires atonement, produces grief / writhing / decay).
  4. Structural opposite — sin vs righteousness; guilt vs innocence; transgression vs covenant-keeping; perversion vs uprightness; unfaithfulness vs faithfulness.
  5. Direction or object — sin against God; sin against neighbour; unfaithfulness to covenant; transgression of law; iniquity borne / forgiven / atoned for.

PHASE 1 RUBRIC — three classifications

You assign each verse exactly ONE classification:

  **relevant** — the verse evidences the term's inner-being content within M10's register.
      Examples: Rom 3:23 "all have sinned" for hamartanō.
      Examples: Psa 51:5 "in iniquity (a.von) was I born" for a.von.
      Examples: Lev 5:17 "he is guilty (a.sham) and shall bear his iniquity" for a.sham.
      Examples: Eze 18:24 "in the trespass (ma.al) he has committed" for ma.al.
      Examples: Lev 18:23 "it is perversion (te.vel)" for te.vel.

  **set_aside** — the term appears in this verse but does NOT carry M10's act/state/experience-of-moral-failure content
      within the cluster register. The verse uses the term in an unrelated sense:
        - cha.val used of physical labour-pain or pregnancy (not guilt-agony);
        - diaftheirō used of physical destruction of a city / object (not moral corruption);
        - sa.laph used of physical twisting (not moral perversion);
        - flat lexical mention in a list / genealogy / dimension;
        - the verse evidences evil-as-character (→ M10b) or defilement (→ M10c) rather than M10's act-of-failure content;
        - the term here belongs to a different semantic domain entirely.

  **borderline** — the verse meaning is ambiguous and needs researcher decision.
      Use sparingly. Borderline entries are HELD for researcher review and NOT written
      to the database. Default to relevant or set_aside when the evidence is clear;
      reserve borderline for genuinely unresolvable cases.

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
  - Name the verse's actual sense of the term (e.g. "diaftheirō used of physical destruction of city, not moral corruption"; "cha.val used of labour-pain, not guilt-agony").
  - End with: " — outside M10 sin/guilt/transgression scope." (or, if relevant, " — belongs to M10b evil-character." / " — belongs to M10c defilement.")
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
                reason = r.get("set_aside_reason") or "outside M10 sin/guilt/transgression scope"
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
            "patch_id": f"wa-cluster-M10-patch-vcnew-utreview-api-v1-{DATE}",
            "cluster_code": CLUSTER,
            "session_ref": "M10 Phase 1 UT review via Claude API (post-split)",
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
        f"# WA-M10-UT-verse-review-api-v1-{DATE}",
        "",
        f"Phase 1 UT review for cluster M10 (Sin, Guilt and Transgression — post-split). "
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
    print(f"M10 UT load: {len(by_term)} terms · {n_verses} verses")
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
