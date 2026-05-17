"""Inverted-validation test: AI marks its own homework on M01-D.

Methodology (researcher design):
  - Take the 72 E findings authored for M01-D scope and the 76 is_relevant verses
    routed to M01-D in Phase 6.
  - Strip from findings: sub-group codes (M01-X), VCG codes (M01-X-VCG-NN), inline
    verse references, anchor markers.
  - Present to AI a single list of findings + a flat verse corpus (vc_id, reference,
    term, verse_text, Phase 2 meaning) with NO structural labels.
  - Ask AI: for each finding, identify the vc_ids that support / evidence it.
  - CC then checks: do AI's blind verse picks cluster within the VCG that the
    finding was authored under?

If AI's picks consistently fall within the structural scope, the structure is
validated. Misalignment is diagnostic.

Inputs: M01-D findings + verses (queried from DB)
Outputs:
  - WA-M01-D-blind-verification-test-input-20260516.json (what AI sees)
  - WA-M01-D-blind-verification-test-output-20260516.json (AI's picks)
  - WA-M01-D-blind-verification-test-analysis-20260516.md (CC's analysis)
"""
from __future__ import annotations
import json, os, re, sqlite3, sys, time
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict, Counter

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

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
M01 = REPO / "Sessions" / "Session_Clusters" / "M01"
DATE = datetime.now(timezone.utc).strftime("%Y%m%d")
INPUT_JSON = M01 / f"WA-M01-D-blind-verification-test-input-{DATE}.json"
OUTPUT_JSON = M01 / f"WA-M01-D-blind-verification-test-output-{DATE}.json"
ANALYSIS_MD = M01 / f"WA-M01-D-blind-verification-test-analysis-{DATE}.md"

MODEL = "claude-sonnet-4-6"
SUBGROUP_ID = 61  # M01-D

# Regex catalogue for stripping structural / referential cues
# Verse refs: Book Chap:Verse [-Verse] [anchor]
VERSE_REF_RE = re.compile(
    r"\b(?:[1-3]?(?:Gen|Exo|Lev|Num|Deu|Jos|Judg|Rut|Sa|Ki|Ch|Ezr|Neh|Est|Job|"
    r"Psa|Pro|Ecc|Sng|Isa|Jer|Lam|Eze|Dan|Hos|Joe|Amo|Oba|Jon|Mic|Nah|Hab|Zep|"
    r"Hag|Zec|Mal|Mat|Mar|Luk|Joh|Act|Rom|Cor|Gal|Eph|Phil|Col|Th|Ti|Tit|Phm|"
    r"Heb|Jam|Pe|Jo|Jud|Rev))\s+\d+:\d+(?:[-–]\d+(?::\d+)?)?(?:[a-z])?"
    r"(?:\s*\(?(?:anchor|VCG-\d+)\)?)?",
    re.IGNORECASE
)
# Sub-group codes & VCG codes
SUBGROUP_CODE_RE = re.compile(r"\bM\d{2}-[A-Z]+(?:-VCG-\d+)?\b")
BARE_VCG_RE = re.compile(r"\bVCG-?\d+\b")
ANCHOR_MARKER_RE = re.compile(r"\b\(?(?:anchor)\)?\b", re.IGNORECASE)


def strip_structural_cues(text: str) -> str:
    """Strip structural and referential cues from finding text."""
    s = VERSE_REF_RE.sub("[ref]", text)
    s = SUBGROUP_CODE_RE.sub("[scope]", s)
    s = BARE_VCG_RE.sub("[scope]", s)
    s = ANCHOR_MARKER_RE.sub("", s)
    # Collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s


def fetch_findings(conn) -> list[dict]:
    rows = conn.execute("""
        SELECT cf.id, cf.obs_id, cf.vcg_scope, cf.finding_status, cf.finding_text,
               oqc.question_code, oqc.question_text
        FROM cluster_finding cf
        JOIN wa_obs_question_catalogue oqc ON oqc.obs_id = cf.obs_id
        WHERE cf.cluster_code='M01' AND cf.cluster_subgroup_id=? AND cf.version='v1-20260516'
          AND cf.finding_status='finding'
          AND COALESCE(cf.delete_flagged,0)=0
        ORDER BY oqc.question_code
    """, (SUBGROUP_ID,)).fetchall()
    return [dict(r) for r in rows]


def fetch_verse_corpus(conn) -> list[dict]:
    rows = conn.execute("""
        SELECT vc.id AS vc_id, vc.group_id, vc.is_anchor,
               vr.reference, vr.verse_text,
               mt.strongs_number, mt.transliteration,
               vcg.group_code AS vcg_code
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
        WHERE vc.cluster_subgroup_id=? AND vc.is_relevant=1
          AND COALESCE(vc.delete_flagged,0)=0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (SUBGROUP_ID,)).fetchall()
    # Add analysis_note
    out = []
    for r in rows:
        d = dict(r)
        m = conn.execute("SELECT analysis_note FROM verse_context WHERE id=?", (d["vc_id"],)).fetchone()
        d["meaning"] = m["analysis_note"] if m else ""
        out.append(d)
    return out


def build_system_prompt(verses: list[dict]) -> str:
    """Verse corpus only — no sub-group / VCG hints."""
    lines = [
        "You are Claude AI completing an inverted-validation experiment.",
        "",
        "Below is a verse corpus drawn from one cohesive analytical area (which "
        "area is intentionally not disclosed to you). Each verse is given with its "
        "reference, term, verse text, and a one-line meaning summary written in a "
        "prior analytical pass.",
        "",
        "Your task: for each finding statement in the user message, identify the "
        "verses from this corpus that support or evidence the finding.",
        "",
        "Rules:",
        "  - Pick verses whose meaning genuinely supports the finding.",
        "  - You may pick 0, 1, or many verses per finding. There is no expected count.",
        "  - If no verse in the corpus supports a finding, return an empty list. That is acceptable.",
        "  - You should not assume which sub-group or VCG these verses belong to. They are all from one analytical area; the structural labels have been removed.",
        "",
        "VERSE CORPUS",
        "",
    ]
    for v in verses:
        meaning = (v.get("meaning") or "").replace("\n", " ").strip()
        verse_text = (v.get("verse_text") or "").replace("\n", " ").strip()
        lines.append(f"vc_id: {v['vc_id']}")
        lines.append(f"  reference: {v['reference']}")
        lines.append(f"  term: {v['strongs_number']} {v['transliteration']}")
        lines.append(f"  verse_text: {verse_text}")
        lines.append(f"  meaning: {meaning}")
        lines.append("")
    return "\n".join(lines)


def build_user_message(findings: list[dict]) -> str:
    """Findings to answer, with structural cues stripped."""
    lines = [
        f"FINDINGS — {len(findings)} statements. For each, identify the supporting vc_ids from the corpus.",
        "",
        "Respond with exactly one JSON array. One object per finding, in input order:",
        "",
        "  {",
        '    "finding_id": <integer>,',
        '    "question_code": "<string>",',
        '    "supporting_vc_ids": [<vc_id>, <vc_id>, ...],',
        '    "rationale": "<one-sentence explanation, max 200 chars>"',
        "  }",
        "",
        "Do not include any text outside the JSON array. No prose, no markdown fence.",
        "",
        "---",
        "",
    ]
    for f in findings:
        stripped = strip_structural_cues(f["finding_text"])
        lines.append(f"finding_id: {f['id']}")
        lines.append(f"question_code: {f['question_code']}")
        lines.append(f"question_text: {f['question_text']}")
        lines.append(f"finding_text: {stripped}")
        lines.append("")
    return "\n".join(lines)


def call_api(client, system_prompt: str, user_message: str, max_retries: int = 2) -> tuple[list[dict], dict, str]:
    for attempt in range(max_retries + 1):
        try:
            resp = client.messages.create(
                model=MODEL, max_tokens=20000,
                system=[{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}],
                messages=[{"role": "user", "content": user_message}],
            )
            text = resp.content[0].text.strip()
            if text.startswith("```"):
                text = text.split("```", 2)[1]
                if text.startswith("json"): text = text[4:]
                text = text.strip("`").strip()
            results = json.loads(text)
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


def analyze_results(findings: list[dict], picks_by_finding: dict[int, list[int]],
                     verses: list[dict]) -> str:
    """Generate analysis markdown comparing AI's blind picks vs structural scope."""
    # Build lookup: vc_id → VCG code, group_id
    vc_to_vcg: dict[int, dict] = {v["vc_id"]: v for v in verses}

    # Per-finding analysis
    per_finding: list[dict] = []
    for f in findings:
        picks = picks_by_finding.get(f["id"], [])
        vcg_dist: Counter = Counter()
        valid_picks: list[int] = []
        invalid_picks: list[int] = []
        for vc in picks:
            if vc in vc_to_vcg:
                valid_picks.append(vc)
                vcg_dist[vc_to_vcg[vc]["vcg_code"]] += 1
            else:
                invalid_picks.append(vc)
        per_finding.append({
            "finding_id": f["id"], "question_code": f["question_code"],
            "vcg_scope_stated": f["vcg_scope"],
            "n_picks": len(picks), "n_valid": len(valid_picks), "n_invalid": len(invalid_picks),
            "vcg_distribution": dict(vcg_dist),
            "picks": picks,
        })

    # Aggregate VCG distribution for VCG-scoped findings
    # If a finding's stated vcg_scope is "M01-D-VCG-02", do AI's picks fall in M01-D-VCG-02?
    vcg_scoped: list[dict] = [r for r in per_finding if r["vcg_scope_stated"]]
    aggregate_match = 0
    aggregate_total_picks = 0
    aggregate_picks_in_stated = 0
    for r in vcg_scoped:
        target_vcg = r["vcg_scope_stated"]
        in_target = r["vcg_distribution"].get(target_vcg, 0)
        aggregate_picks_in_stated += in_target
        aggregate_total_picks += r["n_valid"]
        if r["n_valid"] > 0 and (in_target / r["n_valid"]) >= 0.5:
            aggregate_match += 1

    # Lines
    lines = [
        "# M01-D blind verification test — Analysis",
        "",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"**Test design:** Inverted-validation — AI given findings + corpus, blind to sub-group + VCG labels.",
        f"**Scope:** M01-D — 72 finding-status='finding' rows; 76 is_relevant verses.",
        "",
        "**Stripped from input:** sub-group codes (M01-X), VCG codes (M01-X-VCG-NN), inline verse references, anchor markers.",
        "**Retained in input:** finding text content + question text + verse reference + term + verse text + Phase 2 meaning.",
        "",
        "---",
        "",
        "## Summary",
        "",
        f"- Findings tested: {len(findings)}",
        f"- AI picked verses for: {sum(1 for r in per_finding if r['n_picks'] > 0)} findings",
        f"- AI returned empty pick list: {sum(1 for r in per_finding if r['n_picks'] == 0)} findings",
        f"- Total verse picks: {sum(r['n_picks'] for r in per_finding)}",
        f"- Of which valid (in M01-D corpus): {sum(r['n_valid'] for r in per_finding)}",
        f"- Of which invalid (not in M01-D corpus): {sum(r['n_invalid'] for r in per_finding)}",
        "",
        f"### VCG-scoped findings ({len(vcg_scoped)})",
        "",
        f"- Total picks for VCG-scoped findings: {aggregate_total_picks}",
        f"- Picks landing in the stated VCG: {aggregate_picks_in_stated}",
        f"- Findings where ≥50% of picks fall in the stated VCG: {aggregate_match} / {len(vcg_scoped)} ({100*aggregate_match/max(len(vcg_scoped),1):.0f}%)",
        "",
        "---",
        "",
        "## Per-finding detail (top-level VCG distribution)",
        "",
        "| Finding | Question | Scope stated | Valid picks | VCG distribution |",
        "|---:|---|---|---:|---|",
    ]
    for r in per_finding:
        dist_str = " · ".join(f"{k}: {v}" for k, v in sorted(r["vcg_distribution"].items(), key=lambda x: -x[1])[:5])
        if not dist_str:
            dist_str = "_(none)_"
        scope = r["vcg_scope_stated"] or "(sub-group)"
        lines.append(f"| {r['finding_id']} | {r['question_code']} | {scope} | {r['n_valid']} | {dist_str} |")
    lines.append("")

    return "\n".join(lines)


def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    findings = fetch_findings(conn)
    verses = fetch_verse_corpus(conn)
    print(f"M01-D test: {len(findings)} findings, {len(verses)} verses")

    # Save input
    test_input = {
        "test_design": "Inverted validation — AI marks its own homework",
        "sub_group_hidden": "M01-D (intentionally not disclosed to AI)",
        "n_findings": len(findings),
        "n_verses": len(verses),
        "findings_raw": [dict(f) for f in findings],
        "verses": verses,
        "findings_stripped": [
            {"id": f["id"], "question_code": f["question_code"],
             "question_text": f["question_text"],
             "stripped_text": strip_structural_cues(f["finding_text"])}
            for f in findings
        ],
    }
    INPUT_JSON.write_text(json.dumps(test_input, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Input snapshot: {INPUT_JSON.relative_to(REPO)}")

    # Build prompts
    system_prompt = build_system_prompt(verses)
    user_message = build_user_message(findings)

    print(f"System prompt: {len(system_prompt)} chars")
    print(f"User message: {len(user_message)} chars")

    client = anthropic.Anthropic()
    print(f"Model: {MODEL}\n")
    t0 = time.time()
    results, usage, raw = call_api(client, system_prompt, user_message)
    elapsed = time.time() - t0
    print(f"API call: {elapsed:.1f}s, in={usage['input_tokens']} out={usage['output_tokens']} "
          f"cache_create={usage['cache_creation']} cache_read={usage['cache_read']}")

    # Parse picks
    picks_by_finding: dict[int, list[int]] = {}
    for r in results:
        fid = r.get("finding_id")
        if fid is not None:
            picks_by_finding[fid] = r.get("supporting_vc_ids", [])

    # Save output
    test_output = {
        "test_design": "M01-D blind verification — AI's verse picks per finding",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "api_usage": usage,
        "elapsed_seconds": elapsed,
        "results": results,
        "raw_response_first_500": raw[:500],
    }
    OUTPUT_JSON.write_text(json.dumps(test_output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Output: {OUTPUT_JSON.relative_to(REPO)}")

    # Analyse
    analysis_md = analyze_results(findings, picks_by_finding, verses)
    ANALYSIS_MD.write_text(analysis_md, encoding="utf-8")
    print(f"Analysis: {ANALYSIS_MD.relative_to(REPO)}")


if __name__ == "__main__":
    main()
