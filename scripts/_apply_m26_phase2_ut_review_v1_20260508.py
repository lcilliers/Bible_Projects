"""_apply_m26_phase2_ut_review_v1_20260508.py — Claude API + DB read.

Phase 2 (UT verse review) automation prototype for M26 cluster.

Per wa-sessionb-cluster-instruction-v1_1-20260507 §5: every UT verse
must be read, term-spans noted, and classified as relevant /
set-aside / borderline. Standard process is human-in-chat; this
script automates the per-verse classification via the Claude API.

Architecture (one API call per UT verse):
  - System prompt: M26 cluster context + classification rubric + JSON schema
  - User message: the verse text + the M26 term being classified
  - Output: structured JSON decision per term

Outputs:
  1. Raw API results JSON
       outputs/markdown/m26-phase2-ut-router-results-{model}-{date}.json
  2. Review document (markdown, per Phase 2 §5 deliverable spec)
       Sessions/Session_Clusters/M26/files phase 2/
       WA-M26-UT-verse-review-v1-{date}.md
  3. Canonical-format VCREVISE patch (ready for apply_session_patch)
       Sessions/Session_Clusters/M26/files phase 2/
       wa-cluster-M26-patch-vcrevise-utreview-canonical-v1-{date}.json

DB writes: NONE. The patch is written but not applied — you apply via
scripts/apply_session_patch.py after reviewing the output.

Cost target: ~$0.05 - $0.20 with claude-sonnet-4-6 + prompt caching.
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone

try:
    from dotenv import load_dotenv
    load_dotenv(".env")
except ImportError:
    pass

DB_PATH = os.path.join("database", "bible_research.db")
CLUSTER_CODE = "M26"
CLUSTER_DESC = "Righteousness and Justice"

OUT_DIR_PHASE2 = os.path.join(
    "Sessions", "Session_Clusters", "M26", "files phase 2"
)
OUT_DIR_RESULTS = os.path.join("outputs", "markdown")


SYSTEM_PROMPT = f"""You are a Bible-verse classifier for the Soul Word Analysis Programme — a research project studying ~214 English words for the inner life of mankind, each mapped to Hebrew (OT) and Greek (NT) terms via Strong's numbers.

Cluster context: **M26 — {CLUSTER_DESC}**.
This cluster covers terms that name righteousness, justice, judgment, condemnation, vengeance, and uprightness as inner-being characteristics — qualities held within the person, faculties operative in moral assessment, or judicial conditions in which the inner being stands. The cluster is concerned with how these characteristics are constituted, expressed, and recognised in the inner life — not with external legal procedure, civic governance, or accounting.

Each call gives you ONE verse with the ONE M26 term whose extraction produced that verse_record (the term being classified). Your task: decide whether THIS verse, through THIS term, evidences inner-being content for the M26 cluster's characteristics.

Output exactly one of three decisions:

(A) **RELEVANT** — the verse evidences righteousness/justice/judgment/condemnation/uprightness as an inner-being characteristic of a person, God, or community. Set `decision = "relevant"`, write a 1-sentence brief (≤25 words) describing what THIS verse says about the characteristic via THIS term.

(B) **SET ASIDE** — the verse uses the term in a sense unrelated to the M26 cluster's inner-being characteristic. Set `decision = "set_aside"` and pick the closest reason:
  - `no_inner_being` — external conduct, event, legal procedure, civic action, or accounting that does not engage inner-being content
  - `physical_only` — body part, physical process, or material object
  - `lexical_only` — word used in a definitional/grammatical sense without engaging the characteristic
  - `unclear_context` — ambiguous; needs deeper analysis or researcher review
  Provide a one-clause reason in `reason_detail`.

(C) **BORDERLINE** — the verse may engage the characteristic but the call is not clear from the verse alone. Set `decision = "borderline"`. Provide `reason_detail` explaining the ambiguity. These will be reviewed by the researcher; no DB write occurs for borderlines.

Discipline:
- Decide based on what THIS verse evidences via THIS term. Do not import context from other verses, other clusters, or general theological knowledge.
- The test for "relevant" is: can you point to language in the verse that engages an inner-being condition (a state, faculty, judgment, or quality held within the person/God)? If yes → relevant. If only external action, civic outcome, or technical accounting is in view → set_aside.
- For BOUNDARY-style terms (e.g. accountable, causer, cause/charge), the test is whether the term-in-verse engages the inner-being state of someone or just names an external role. The role-only use is set_aside.
- Brief and consistent matters more than exhaustive. No morphological analysis, no parallels, no speculation.
- Fluency is not a quality signal. If you cannot point to verse language that grounds the decision, lean to set_aside or borderline.

Output JSON shape — exactly:
{{
  "verse_record_id": <int>,
  "mti_term_id": <int>,
  "strong": "<copied from input>",
  "decision": "relevant" | "set_aside" | "borderline",
  "set_aside_reason": "no_inner_being" | "physical_only" | "lexical_only" | "unclear_context" | null,
  "brief_summary": "<≤25 words plain English; required for relevant; null otherwise>",
  "reason_detail": "<one-clause reason; required for set_aside and borderline; null for relevant>",
  "verse_evidence_quote": "<short quote from the verse that grounded the decision (≤15 words); null if borderline or fully set_aside>"
}}
"""

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "verse_record_id": {"type": "integer"},
        "mti_term_id": {"type": "integer"},
        "strong": {"type": "string"},
        "decision": {"type": "string",
                     "enum": ["relevant", "set_aside", "borderline"]},
        "set_aside_reason": {"type": ["string", "null"]},
        "brief_summary": {"type": ["string", "null"]},
        "reason_detail": {"type": ["string", "null"]},
        "verse_evidence_quote": {"type": ["string", "null"]},
    },
    "required": ["verse_record_id", "mti_term_id", "strong", "decision",
                 "set_aside_reason", "brief_summary",
                 "reason_detail", "verse_evidence_quote"],
    "additionalProperties": False,
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def fetch_ut_verses(conn) -> list[dict]:
    """Return M26 UT verses with the term metadata we'll prompt with."""
    rows = list(conn.execute("""
        SELECT vr.id AS vr_id,
               vr.verse_record_id_alt,
               vr.mti_term_id,
               vr.reference,
               vr.verse_text,
               vr.testament,
               mt.strongs_number,
               mt.transliteration,
               mt.gloss,
               mt.language,
               ti.short_def_mounce,
               ti.step_search_gloss,
               ti.meaning
          FROM (
            SELECT vr.id, vr.id AS verse_record_id_alt, vr.mti_term_id,
                   vr.reference, vr.verse_text, vr.testament
              FROM wa_verse_records vr
              JOIN mti_terms mt2 ON mt2.id=vr.mti_term_id
             WHERE mt2.cluster_code='M26'
               AND COALESCE(vr.delete_flagged,0)=0
               AND COALESCE(mt2.delete_flagged,0)=0
               AND NOT EXISTS (
                   SELECT 1 FROM verse_context vc
                    WHERE vc.verse_record_id=vr.id
                      AND vc.mti_term_id=vr.mti_term_id
                      AND COALESCE(vc.delete_flagged,0)=0
               )
          ) vr
          JOIN mti_terms mt ON mt.id=vr.mti_term_id
          LEFT JOIN wa_term_inventory ti
                 ON ti.strongs_number=mt.strongs_number
                AND COALESCE(ti.delete_flagged,0)=0
                AND COALESCE(ti.term_owner_type,'OWNER')='OWNER'
         ORDER BY vr.reference, vr.id
    """))
    return [dict(r) for r in rows]


def build_user_msg(verse: dict) -> str:
    pkg = {
        "verse": {
            "verse_record_id": verse["vr_id"],
            "reference": verse["reference"],
            "testament": verse["testament"],
            "verse_text": verse["verse_text"],
        },
        "term": {
            "mti_term_id": verse["mti_term_id"],
            "strong": verse["strongs_number"],
            "transliteration": verse["transliteration"],
            "gloss": verse["gloss"],
            "language": verse["language"],
            "short_def_mounce": verse["short_def_mounce"],
            "step_search_gloss": verse["step_search_gloss"],
            "meaning_excerpt": (verse["meaning"] or "")[:600] or None,
        },
    }
    return (
        "Classify this verse-and-term for inclusion in M26 (Righteousness "
        "and Justice). Return JSON in the schema above.\n\n"
        f"```json\n{json.dumps(pkg, ensure_ascii=False, indent=2)}\n```"
    )


def call_claude(client, verse, model: str, effort: str):
    user_msg = build_user_msg(verse)
    response = client.messages.create(
        model=model,
        max_tokens=1500,
        thinking={"type": "adaptive"},
        output_config={
            "effort": effort,
            "format": {"type": "json_schema", "schema": OUTPUT_SCHEMA},
        },
        system=[{
            "type": "text",
            "text": SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }],
        messages=[{"role": "user", "content": user_msg}],
    )
    text_blocks = [b.text for b in response.content
                   if hasattr(b, "text") and b.text]
    raw = "".join(text_blocks).strip()
    parsed = json.loads(raw)
    return parsed, response


def get_md_versions(conn, mti_ids: set[int]) -> dict[int, int]:
    out = {}
    if not mti_ids:
        return out
    placeholders = ",".join("?" * len(mti_ids))
    for r in conn.execute(
        f"SELECT id, md_version FROM mti_terms WHERE id IN ({placeholders})",
        tuple(mti_ids),
    ):
        out[r[0]] = int(r[1] or 1)
    return out


def existing_anchors_for(conn, mti_ids: set[int]) -> dict[int, int]:
    """Return per-term anchor count (is_anchor=1, active vc rows)."""
    out: dict[int, int] = {tid: 0 for tid in mti_ids}
    if not mti_ids:
        return out
    placeholders = ",".join("?" * len(mti_ids))
    for r in conn.execute(
        f"SELECT mti_term_id, SUM(is_anchor) AS n FROM verse_context "
        f" WHERE mti_term_id IN ({placeholders}) "
        f"   AND COALESCE(delete_flagged,0)=0 "
        f" GROUP BY mti_term_id",
        tuple(mti_ids),
    ):
        out[r[0]] = int(r[1] or 0)
    return out


def write_review_doc(verses, decisions, out_path):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    relevants = [(v, d) for v, d in zip(verses, decisions)
                 if d.get("decision") == "relevant"]
    set_asides = [(v, d) for v, d in zip(verses, decisions)
                  if d.get("decision") == "set_aside"]
    borderlines = [(v, d) for v, d in zip(verses, decisions)
                   if d.get("decision") == "borderline"]
    errors = [(v, d) for v, d in zip(verses, decisions) if "error" in d]

    lines = []
    lines.append(f"# WA-M26-UT-verse-review-v1-{today.replace('-','')}")
    lines.append("")
    lines.append(f"> Framework B Soul Word Analysis Programme — Session B Phase 2 (UT verse review)")
    lines.append(f"> Cluster: M26 — {CLUSTER_DESC}")
    lines.append(f"> Date: {today}")
    lines.append(f"> Method: Claude API per-verse classification (sonnet-4-6 + prompt caching)")
    lines.append(f"> Companion patch: wa-cluster-M26-patch-vcrevise-utreview-canonical-v1-{today.replace('-','')}.json")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Decision | Count | % |")
    lines.append(f"|---|---:|---:|")
    n = len(verses)
    lines.append(f"| Relevant (confirmed) | {len(relevants)} | {100*len(relevants)/max(n,1):.1f}% |")
    lines.append(f"| Set aside | {len(set_asides)} | {100*len(set_asides)/max(n,1):.1f}% |")
    lines.append(f"| Borderline (researcher review) | {len(borderlines)} | {100*len(borderlines)/max(n,1):.1f}% |")
    lines.append(f"| Errors (re-run needed) | {len(errors)} | {100*len(errors)/max(n,1):.1f}% |")
    lines.append(f"| **Total** | **{n}** | 100% |")
    lines.append("")

    # Set-aside reasons breakdown
    if set_asides:
        from collections import Counter
        reasons = Counter(d.get("set_aside_reason") for _, d in set_asides)
        lines.append("**Set-aside reason breakdown:**")
        lines.append("")
        for r, c in reasons.most_common():
            lines.append(f"- `{r}`: {c}")
        lines.append("")

    lines.append("---")
    lines.append("")

    def fmt(verse, d, show_evidence=True):
        evid = (d.get("verse_evidence_quote") or "").strip()
        evid_str = f' Evidence: "{evid}"' if evid and show_evidence else ""
        return (
            f"**{verse['reference']}** — {verse['strongs_number']} "
            f"*{verse['transliteration']}* (mti={verse['mti_term_id']}, "
            f"vr={verse['vr_id']})\n"
            f"  Verse: {verse['verse_text'][:200]}\n"
        )

    if relevants:
        lines.append(f"## §1. Relevant — confirmed inner-being content ({len(relevants)})")
        lines.append("")
        for v, d in relevants:
            lines.append(fmt(v, d).rstrip())
            lines.append(f"  Brief: {d.get('brief_summary')}")
            evid = (d.get("verse_evidence_quote") or "").strip()
            if evid:
                lines.append(f"  Evidence: \"{evid}\"")
            lines.append("")

    if set_asides:
        lines.append(f"## §2. Set aside ({len(set_asides)})")
        lines.append("")
        for v, d in set_asides:
            lines.append(fmt(v, d).rstrip())
            lines.append(f"  Reason: `{d.get('set_aside_reason')}` — {d.get('reason_detail')}")
            lines.append("")

    if borderlines:
        lines.append(f"## §3. Borderline — researcher review required ({len(borderlines)})")
        lines.append("")
        for v, d in borderlines:
            lines.append(fmt(v, d).rstrip())
            lines.append(f"  Ambiguity: {d.get('reason_detail')}")
            lines.append("")

    if errors:
        lines.append(f"## §4. Errors — re-run needed ({len(errors)})")
        lines.append("")
        for v, d in errors:
            lines.append(f"- {v['reference']} mti={v['mti_term_id']} — {d.get('error')}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"*WA-M26-UT-verse-review-v1-{today.replace('-','')} — "
                 f"Phase 2 UT review automated via Claude API*")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_canonical_patch(verses, decisions, conn, out_path):
    """Write the VCREVISE patch in canonical format (insert ops; R4-anchor
    on first relevant op for terms with no pre-existing anchor)."""
    today = datetime.now(timezone.utc).strftime("%Y%m%d")

    # Build operations list from relevant + set-aside decisions only
    # (borderlines are excluded; errors are excluded)
    ops = []
    op_seq = 0
    relevant_first_op_per_term: dict[int, int] = {}  # mti_id -> idx in ops

    for v, d in zip(verses, decisions):
        if d.get("decision") not in ("relevant", "set_aside"):
            continue
        op_seq += 1
        mti = v["mti_term_id"]
        vr_id = v["vr_id"]

        if d["decision"] == "relevant":
            record = {
                "verse_record_id": vr_id,
                "mti_term_id": mti,
                "group_id": None,
                "is_anchor": 0,
                "is_relevant": 1,
                "is_related": 0,
                "set_aside_reason": None,
                "analysis_note": d.get("brief_summary"),
                "delete_flagged": 0,
            }
            if mti not in relevant_first_op_per_term:
                relevant_first_op_per_term[mti] = len(ops)
        else:
            evidence = d.get("reason_detail") or ""
            record = {
                "verse_record_id": vr_id,
                "mti_term_id": mti,
                "group_id": None,
                "is_anchor": 0,
                "is_relevant": 0,
                "is_related": 0,
                "set_aside_reason": d.get("set_aside_reason") or "no_inner_being",
                "analysis_note": evidence or None,
                "delete_flagged": 0,
            }

        ops.append({
            "op_id": f"OP-{op_seq:04d}",
            "operation": "insert",
            "table": "verse_context",
            "record": record,
            "description": (
                f"Phase2 | {v['reference']} | "
                f"{v['strongs_number']} {v['transliteration']} | "
                f"{d['decision']}"
            ),
        })

    # R4 anchor safety: for any term whose first relevant op exists and
    # which has no pre-existing anchor, mark that op's record as anchor.
    relevant_mti_ids = set(relevant_first_op_per_term.keys())
    pre_anchors = existing_anchors_for(conn, relevant_mti_ids)
    r4_provisional = []
    for mti, idx in relevant_first_op_per_term.items():
        if pre_anchors.get(mti, 0) == 0:
            ops[idx]["record"]["is_anchor"] = 1
            r4_provisional.append((mti, ops[idx]["record"]["verse_record_id"]))

    # terms_covered + input_versions
    referenced_terms = sorted({op["record"]["mti_term_id"] for op in ops})
    md_versions = get_md_versions(conn, set(referenced_terms))
    input_versions = {str(t): md_versions.get(t, 1) for t in referenced_terms}

    meta = {
        "patch_id": f"PATCH-{today}-M26-VCREVISE-UTREVIEW-CANONICAL-V1",
        "patch_type": "VCREVISE",
        "produced_date": today,
        "produced_by": "_apply_m26_phase2_ut_review_v1_20260508.py (Claude API)",
        "description": (
            f"M26 Phase 2 UT verse review — automated via Claude API. "
            f"{len(ops)} operations: relevant + set-aside decisions. "
            "Borderlines and errors not included. R4 provisional anchors "
            f"set on {len(r4_provisional)} term(s) with no pre-existing "
            "anchor."
        ),
        "session_b_status": None,
        "terms_covered": referenced_terms,
        "input_versions": input_versions,
        "operations_count": len(ops),
        "governing_instruction":
            "wa-sessionb-cluster-instruction-v1_1-20260507.md §5",
        "companion_document":
            f"WA-M26-UT-verse-review-v1-{today}.md",
        "r4_provisional_anchors": [
            {"mti_term_id": tid, "verse_record_id": vr}
            for tid, vr in r4_provisional
        ],
    }

    patch = {"_patch_meta": meta, "operations": ops}
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(patch, f, indent=2, ensure_ascii=False)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="claude-sonnet-4-6")
    ap.add_argument("--effort", default="medium")
    ap.add_argument("--limit", type=int, default=None,
                    help="stop after N verses (for smoke testing)")
    ap.add_argument("--dry-run", action="store_true",
                    help="show prompt + first verse without API call")
    args = ap.parse_args()

    if not args.dry_run and not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set in environment.", file=sys.stderr)
        return 2

    os.makedirs(OUT_DIR_PHASE2, exist_ok=True)
    os.makedirs(OUT_DIR_RESULTS, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    verses = fetch_ut_verses(conn)
    if args.limit:
        verses = verses[: args.limit]
    print(f"M26 UT verses to classify: {len(verses)}")

    if args.dry_run:
        sample_msg = build_user_msg(verses[0])
        print()
        print("=== DRY-RUN: SYSTEM PROMPT ===")
        print(SYSTEM_PROMPT[:2000])
        print()
        print("=== DRY-RUN: SAMPLE USER MSG (verse 1) ===")
        print(sample_msg[:2000])
        print()
        print(f"Would process {len(verses)} verses against {args.model} "
              f"(effort={args.effort}).")
        return 0

    from anthropic import Anthropic
    client = Anthropic()

    decisions = []
    in_tot = out_tot = cache_r_tot = 0
    print(f"Calling {args.model} (effort={args.effort})...\n")
    for i, v in enumerate(verses, 1):
        try:
            parsed, resp = call_claude(client, v, args.model, args.effort)
        except Exception as e:
            print(f"  [{i}/{len(verses)}] {v['reference']:<14} "
                  f"ERROR {type(e).__name__}: {e}")
            decisions.append({"error": f"{type(e).__name__}: {e}",
                              "verse_record_id": v["vr_id"],
                              "mti_term_id": v["mti_term_id"]})
            continue
        usage = resp.usage
        in_tot += usage.input_tokens
        out_tot += usage.output_tokens
        cache_r_tot += getattr(usage, "cache_read_input_tokens", 0) or 0
        decisions.append(parsed)
        decision_str = parsed.get("decision", "?")
        marker = {"relevant": "+", "set_aside": "-",
                  "borderline": "?"}.get(decision_str, "x")
        print(f"  [{i:3d}/{len(verses)}] {marker} {v['reference']:<14} "
              f"{v['strongs_number']:8s} {v['transliteration']:18s} "
              f"-> {decision_str}")

    # Cost
    if "opus" in args.model:
        in_price, out_price = 15.0, 75.0
    elif "haiku" in args.model:
        in_price, out_price = 1.0, 5.0
    else:
        in_price, out_price = 3.0, 15.0
    cost = (in_tot / 1_000_000) * in_price + (out_tot / 1_000_000) * out_price

    today = today_compact()
    raw_path = os.path.join(
        OUT_DIR_RESULTS,
        f"m26-phase2-ut-router-results-{args.model}-{today}.json",
    )
    review_path = os.path.join(
        OUT_DIR_PHASE2, f"WA-M26-UT-verse-review-v1-{today}.md"
    )
    patch_path = os.path.join(
        OUT_DIR_PHASE2,
        f"wa-cluster-M26-patch-vcrevise-utreview-canonical-v1-{today}.json",
    )

    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump({
            "meta": {
                "generated_at": now_iso(),
                "model": args.model,
                "effort": args.effort,
                "n_verses": len(verses),
                "tokens": {
                    "input": in_tot, "output": out_tot,
                    "cache_read": cache_r_tot,
                    "estimated_cost_usd": round(cost, 4),
                },
            },
            "verses": [
                {**dict(v), "decision": d}
                for v, d in zip(verses, decisions)
            ],
        }, f, indent=2, ensure_ascii=False)

    write_review_doc(verses, decisions, review_path)
    write_canonical_patch(verses, decisions, conn, patch_path)

    # Summary
    from collections import Counter
    decisions_by_kind = Counter(d.get("decision", "error") for d in decisions)
    print()
    print("=" * 60)
    print(f"  SUMMARY — {len(verses)} verses classified")
    print("=" * 60)
    for k, n in decisions_by_kind.most_common():
        print(f"  {k:18s} {n}")
    print()
    print(f"Tokens — in: {in_tot:,} out: {out_tot:,} "
          f"cache_read: {cache_r_tot:,}")
    print(f"Estimated cost: ${cost:.4f}")
    print()
    print(f"Outputs:")
    print(f"  raw:    {raw_path}")
    print(f"  review: {review_path}")
    print(f"  patch:  {patch_path}")
    print()
    print(f"To apply the patch:")
    print(f"  python scripts/apply_session_patch.py \"{patch_path}\"")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
