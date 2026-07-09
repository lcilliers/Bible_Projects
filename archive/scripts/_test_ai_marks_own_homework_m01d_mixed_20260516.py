"""Inverted-validation test (b): Mixed-corpus M01-D test.

Same methodology as test (a), but the verse corpus is mixed across THREE sub-groups
(M01-B Acute Fear + M01-C Terror as Force + M01-D Dismay/Collapse). Findings are
all M01-D-scope. Question: does AI correctly pick only M01-D verses, or does it
mistakenly pull from M01-B and M01-C?

Strong test:
  - If AI's picks remain 100% in M01-D → strong evidence AI distinguishes
    dismay/collapse content from acute fear / terror content when blind to labels.
  - If AI pulls from M01-B/C → diagnostic. For T6.x (relational/distinction)
    prompts, some cross-sub-group picks are analytically appropriate. For other
    prompts, cross-sub-group picks indicate mis-routing or boundary issues.

Inputs: M01-D findings + verses from M01-B/C/D (mixed, no labels)
Outputs: input/output/analysis JSON + markdown.
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
INPUT_JSON = M01 / f"WA-M01-D-mixed-verification-test-input-{DATE}.json"
OUTPUT_JSON = M01 / f"WA-M01-D-mixed-verification-test-output-{DATE}.json"
ANALYSIS_MD = M01 / f"WA-M01-D-mixed-verification-test-analysis-{DATE}.md"

MODEL = "claude-sonnet-4-6"
TARGET_SUBGROUP_ID = 61  # M01-D (findings come from here)
CORPUS_SUBGROUP_IDS = [59, 60, 61]  # M01-B, M01-C, M01-D (corpus drawn from)

# Stripping regexes (same as test a)
VERSE_REF_RE = re.compile(
    r"\b(?:[1-3]?(?:Gen|Exo|Lev|Num|Deu|Jos|Judg|Rut|Sa|Ki|Ch|Ezr|Neh|Est|Job|"
    r"Psa|Pro|Ecc|Sng|Isa|Jer|Lam|Eze|Dan|Hos|Joe|Amo|Oba|Jon|Mic|Nah|Hab|Zep|"
    r"Hag|Zec|Mal|Mat|Mar|Luk|Joh|Act|Rom|Cor|Gal|Eph|Phil|Col|Th|Ti|Tit|Phm|"
    r"Heb|Jam|Pe|Jo|Jud|Rev))\s+\d+:\d+(?:[-–]\d+(?::\d+)?)?(?:[a-z])?"
    r"(?:\s*\(?(?:anchor|VCG-\d+)\)?)?",
    re.IGNORECASE
)
SUBGROUP_CODE_RE = re.compile(r"\bM\d{2}-[A-Z]+(?:-VCG-\d+)?\b")
BARE_VCG_RE = re.compile(r"\bVCG-?\d+\b")
ANCHOR_MARKER_RE = re.compile(r"\b\(?(?:anchor)\)?\b", re.IGNORECASE)


def strip_structural_cues(text: str) -> str:
    s = VERSE_REF_RE.sub("[ref]", text)
    s = SUBGROUP_CODE_RE.sub("[scope]", s)
    s = BARE_VCG_RE.sub("[scope]", s)
    s = ANCHOR_MARKER_RE.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def fetch_findings(conn) -> list[dict]:
    rows = conn.execute("""
        SELECT cf.id, cf.obs_id, cf.vcg_scope, cf.finding_status, cf.finding_text,
               oqc.question_code, oqc.question_text
        FROM cluster_finding cf
        JOIN wa_obs_question_catalogue oqc ON oqc.obs_id = cf.obs_id
        WHERE cf.cluster_code='M01' AND cf.cluster_subgroup_id=? AND cf.version='v1-20260516'
          AND cf.finding_status='finding' AND COALESCE(cf.delete_flagged,0)=0
        ORDER BY oqc.question_code
    """, (TARGET_SUBGROUP_ID,)).fetchall()
    return [dict(r) for r in rows]


def fetch_verse_corpus(conn) -> list[dict]:
    """Fetch verses from B, C, D combined, no sub-group label exposed."""
    placeholders = ",".join("?" * len(CORPUS_SUBGROUP_IDS))
    rows = conn.execute(f"""
        SELECT vc.id AS vc_id, vc.group_id, vc.cluster_subgroup_id,
               vr.reference, vr.verse_text,
               mt.strongs_number, mt.transliteration,
               vcg.group_code AS vcg_code, vc.analysis_note AS meaning
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
        WHERE vc.cluster_subgroup_id IN ({placeholders}) AND vc.is_relevant=1
          AND COALESCE(vc.delete_flagged,0)=0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, CORPUS_SUBGROUP_IDS).fetchall()
    return [dict(r) for r in rows]


def build_system_prompt(verses: list[dict]) -> str:
    lines = [
        "You are Claude AI completing an inverted-validation experiment.",
        "",
        "Below is a verse corpus drawn from a defined analytical area. Each verse "
        "is given with its reference, term, verse text, and a one-line meaning "
        "summary written in a prior analytical pass.",
        "",
        "Your task: for each finding statement in the user message, identify the "
        "verses from this corpus that support or evidence the finding.",
        "",
        "Rules:",
        "  - Pick verses whose meaning genuinely supports the finding.",
        "  - You may pick 0, 1, or many verses per finding. There is no expected count.",
        "  - If no verse in the corpus supports a finding, return an empty list.",
        "  - You are not told which subset of the corpus the findings were authored for; "
        "you must infer the relevant verses purely from the finding's analytical content.",
        "",
        f"VERSE CORPUS ({len(verses)} verses)",
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


def call_api(client, system_prompt: str, user_message: str, max_retries: int = 2):
    for attempt in range(max_retries + 1):
        try:
            resp = client.messages.create(
                model=MODEL, max_tokens=16000,
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
    # Build lookup
    vc_to_meta: dict[int, dict] = {v["vc_id"]: v for v in verses}
    sg_id_to_code = {59: "M01-B", 60: "M01-C", 61: "M01-D"}

    per_finding: list[dict] = []
    for f in findings:
        picks = picks_by_finding.get(f["id"], [])
        sg_dist: Counter = Counter()
        vcg_dist: Counter = Counter()
        valid_picks: list[int] = []
        invalid_picks: list[int] = []
        for vc in picks:
            if vc in vc_to_meta:
                valid_picks.append(vc)
                sg_id = vc_to_meta[vc].get("cluster_subgroup_id")
                sg_code = sg_id_to_code.get(sg_id, "?")
                sg_dist[sg_code] += 1
                vcg_dist[vc_to_meta[vc].get("vcg_code", "?")] += 1
            else:
                invalid_picks.append(vc)

        # Is this a relational/distinction prompt?
        qc = f["question_code"]
        is_relational = qc.startswith("T6.") or qc.startswith("T7.3.")
        per_finding.append({
            "finding_id": f["id"], "question_code": qc,
            "is_relational": is_relational,
            "n_picks": len(picks), "n_valid": len(valid_picks), "n_invalid": len(invalid_picks),
            "sg_distribution": dict(sg_dist),
            "vcg_distribution": dict(vcg_dist),
            "picks": picks,
            "in_target_pct": (sg_dist.get("M01-D", 0) / len(valid_picks) * 100) if valid_picks else 0.0,
        })

    # Aggregate
    total_valid = sum(r["n_valid"] for r in per_finding)
    total_in_target = sum(r["sg_distribution"].get("M01-D", 0) for r in per_finding)
    total_in_b = sum(r["sg_distribution"].get("M01-B", 0) for r in per_finding)
    total_in_c = sum(r["sg_distribution"].get("M01-C", 0) for r in per_finding)
    total_invalid = sum(r["n_invalid"] for r in per_finding)

    pure_d = [r for r in per_finding if r["n_valid"] > 0 and r["sg_distribution"].get("M01-D", 0) == r["n_valid"]]
    mixed = [r for r in per_finding if r["n_valid"] > 0 and r["sg_distribution"].get("M01-D", 0) != r["n_valid"]]

    relational_mixed = [r for r in mixed if r["is_relational"]]
    non_relational_mixed = [r for r in mixed if not r["is_relational"]]

    lines = [
        "# M01-D mixed-corpus blind verification test — Analysis",
        "",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"**Test design:** Mixed corpus from M01-B (Acute Fear) + M01-C (Terror as Force) + M01-D (Dismay/Collapse).",
        f"  Findings drawn from M01-D scope only. AI must distinguish target verses from distractors.",
        "",
        f"**Corpus:** {len(verses)} verses ({sum(1 for v in verses if v['cluster_subgroup_id']==61)} in M01-D target; "
        f"{sum(1 for v in verses if v['cluster_subgroup_id']==59)} in M01-B distractor; "
        f"{sum(1 for v in verses if v['cluster_subgroup_id']==60)} in M01-C distractor)",
        f"**Findings tested:** {len(findings)}",
        "",
        "---",
        "",
        "## Headline result",
        "",
        f"- AI returned picks for: **{sum(1 for r in per_finding if r['n_picks']>0)} / {len(findings)}** findings",
        f"- Total picks: **{sum(r['n_picks'] for r in per_finding)}**",
        f"- Valid picks (in corpus): **{total_valid}**",
        f"- Invalid picks (not in corpus): **{total_invalid}**",
        "",
        f"### Sub-group distribution of valid picks",
        "",
        f"- In M01-D (target): **{total_in_target}** ({100*total_in_target/max(total_valid,1):.1f}%)",
        f"- In M01-B (distractor): **{total_in_b}** ({100*total_in_b/max(total_valid,1):.1f}%)",
        f"- In M01-C (distractor): **{total_in_c}** ({100*total_in_c/max(total_valid,1):.1f}%)",
        "",
        f"### Finding-level concentration",
        "",
        f"- Pure-target findings (all picks in M01-D): **{len(pure_d)} / {len(findings)}** ({100*len(pure_d)/len(findings):.0f}%)",
        f"- Mixed findings (some picks outside M01-D): **{len(mixed)}**",
        f"  - Of which T6.x or T7.3.x (relational/distinction — cross-sub-group is appropriate): **{len(relational_mixed)}**",
        f"  - Of which non-relational (potentially diagnostic): **{len(non_relational_mixed)}**",
        "",
        "---",
        "",
    ]

    if non_relational_mixed:
        lines.append("## Non-relational findings with cross-sub-group picks (diagnostic)")
        lines.append("")
        lines.append("These are the most informative — if AI's analytical reach pulls from "
                     "M01-B or M01-C verses for a non-T6 finding, the question is whether those "
                     "picks are analytically defensible or whether they indicate boundary issues.")
        lines.append("")
        lines.append("| Finding | Q | n_valid | M01-D | M01-B | M01-C |")
        lines.append("|---:|---|---:|---:|---:|---:|")
        for r in sorted(non_relational_mixed, key=lambda x: -(x["sg_distribution"].get("M01-B",0) + x["sg_distribution"].get("M01-C",0))):
            d = r["sg_distribution"]
            lines.append(f"| {r['finding_id']} | {r['question_code']} | {r['n_valid']} | {d.get('M01-D',0)} | {d.get('M01-B',0)} | {d.get('M01-C',0)} |")
        lines.append("")

    lines.append("## Per-finding distribution (all 72)")
    lines.append("")
    lines.append("| Finding | Q | Type | M01-D | M01-B | M01-C | %Target | Top VCG |")
    lines.append("|---:|---|---|---:|---:|---:|---:|---|")
    for r in per_finding:
        d = r["sg_distribution"]
        top_vcg = "—"
        if r["vcg_distribution"]:
            top_vcg_code, top_n = max(r["vcg_distribution"].items(), key=lambda x: x[1])
            top_vcg = f"{top_vcg_code} ({top_n})"
        ftype = "T6+" if r["is_relational"] else ""
        lines.append(f"| {r['finding_id']} | {r['question_code']} | {ftype} | "
                     f"{d.get('M01-D',0)} | {d.get('M01-B',0)} | {d.get('M01-C',0)} | "
                     f"{r['in_target_pct']:.0f}% | {top_vcg} |")
    lines.append("")

    return "\n".join(lines)


def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    findings = fetch_findings(conn)
    verses = fetch_verse_corpus(conn)
    print(f"M01-D mixed test: {len(findings)} findings, {len(verses)} verses")
    by_sg = Counter(v["cluster_subgroup_id"] for v in verses)
    print(f"  Corpus distribution: M01-B={by_sg.get(59,0)} M01-C={by_sg.get(60,0)} M01-D={by_sg.get(61,0)}")

    test_input = {
        "test_design": "Mixed-corpus inverted validation",
        "target_subgroup_hidden": "M01-D (findings only)",
        "corpus_subgroups": ["M01-B (distractor)", "M01-C (distractor)", "M01-D (target)"],
        "n_findings": len(findings),
        "n_verses": len(verses),
    }
    INPUT_JSON.write_text(json.dumps(test_input, indent=2, ensure_ascii=False), encoding="utf-8")

    system_prompt = build_system_prompt(verses)
    user_message = build_user_message(findings)
    print(f"System prompt: {len(system_prompt)} chars")
    print(f"User message: {len(user_message)} chars")

    client = anthropic.Anthropic()
    print(f"Model: {MODEL}\n")
    t0 = time.time()
    results, usage, raw = call_api(client, system_prompt, user_message)
    elapsed = time.time() - t0
    print(f"API: {elapsed:.1f}s, in={usage['input_tokens']} out={usage['output_tokens']} "
          f"cache_create={usage['cache_creation']} cache_read={usage['cache_read']}")

    picks_by_finding: dict[int, list[int]] = {}
    for r in results:
        fid = r.get("finding_id")
        if fid is not None:
            picks_by_finding[fid] = r.get("supporting_vc_ids", [])

    test_output = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "api_usage": usage, "elapsed_seconds": elapsed,
        "results": results,
    }
    OUTPUT_JSON.write_text(json.dumps(test_output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Output: {OUTPUT_JSON.relative_to(REPO)}")

    analysis_md = analyze_results(findings, picks_by_finding, verses)
    ANALYSIS_MD.write_text(analysis_md, encoding="utf-8")
    print(f"Analysis: {ANALYSIS_MD.relative_to(REPO)}")


if __name__ == "__main__":
    main()
