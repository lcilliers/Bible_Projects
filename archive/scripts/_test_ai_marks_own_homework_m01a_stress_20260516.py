"""Stress test: AI marks own homework on M01-A with full M01 corpus as distractors.

Target: M01-A (Reverential Fear / Fear of God as Governing Orientation)
  - 128 finding-status='finding' rows in scope
  - 320 is_relevant verses routed to M01-A primary
  - 7 substantive VCGs (M01-A-VCG-01..07)

Corpus: full M01 cluster
  - 941 is_relevant verses across 8 sub-groups (M01-A target + B/C/D/E/F/G/BOUNDARY distractors)
  - Target verses are 34% of corpus; distractors are 66%

This is the hardest test:
  - Stress-tests AI's ability to distinguish reverential-fear content from acute fear,
    terror, dismay, trembling, anticipatory dread, timidity, and BOUNDARY content
  - Stress-tests AI's narrative coherence — if AI fabricated findings to maintain
    storyline, the blind verse pick will reveal the gap

Strict signals:
  - Pure-target rate (% findings with 100% picks in M01-A)
  - Per-finding precision (% of picks per finding that land in M01-A)
  - Distractor distribution (where do non-target picks go? Are they analytically
    defensible — e.g. M01-B for acute-fear bridges, M01-E for somatic prompts?)
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
INPUT_JSON = M01 / f"WA-M01-A-stress-test-input-{DATE}.json"
OUTPUT_JSON = M01 / f"WA-M01-A-stress-test-output-{DATE}.json"
ANALYSIS_MD = M01 / f"WA-M01-A-stress-test-analysis-{DATE}.md"

MODEL = "claude-sonnet-4-6"
TARGET_SUBGROUP_ID = 58  # M01-A
CORPUS_SUBGROUP_IDS = [58, 59, 60, 61, 62, 63, 64, 65]  # all M01 sub-groups
SG_ID_TO_CODE = {58: "M01-A", 59: "M01-B", 60: "M01-C", 61: "M01-D",
                  62: "M01-E", 63: "M01-F", 64: "M01-G", 65: "M01-BOUNDARY"}

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
        "You are Claude AI completing an inverted-validation stress test.",
        "",
        "Below is a verse corpus. Each verse is given with reference, term, verse text, "
        "and a one-line meaning summary written in a prior analytical pass.",
        "",
        "Your task: for each finding statement in the user message, identify the verses "
        "from this corpus that support or evidence the finding.",
        "",
        "Rules:",
        "  - Pick verses whose meaning genuinely supports the finding.",
        "  - You may pick 0, 1, or many verses per finding. There is no expected count.",
        "  - If no verse supports a finding, return an empty list — that is acceptable.",
        "  - You are not told which subset the findings were authored for. Identify "
        "support purely from the finding's analytical content.",
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
        f"FINDINGS — {len(findings)} statements. For each, identify the supporting vc_ids.",
        "",
        "Respond with exactly one JSON array. One object per finding, in input order:",
        "",
        "  {",
        '    "finding_id": <integer>,',
        '    "question_code": "<string>",',
        '    "supporting_vc_ids": [<vc_id>, <vc_id>, ...],',
        '    "rationale": "<one-sentence reason, max 200 chars>"',
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


def call_api_with_streaming(client, system_prompt: str, user_message: str) -> tuple[list[dict], dict, str]:
    """Use streaming because the large input may push past the 10-min SDK heuristic."""
    full_text = []
    usage = {"input_tokens": 0, "output_tokens": 0, "cache_creation": 0, "cache_read": 0}
    with client.messages.stream(
        model=MODEL,
        max_tokens=32000,
        system=[{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_message}],
    ) as stream:
        for ev in stream.text_stream:
            full_text.append(ev)
        msg = stream.get_final_message()
        usage = {
            "input_tokens": msg.usage.input_tokens,
            "output_tokens": msg.usage.output_tokens,
            "cache_creation": getattr(msg.usage, "cache_creation_input_tokens", 0),
            "cache_read": getattr(msg.usage, "cache_read_input_tokens", 0),
        }
    text = "".join(full_text).strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"): text = text[4:]
        text = text.strip("`").strip()
    # Save raw text for debugging before parse
    (M01 / f"WA-M01-A-stress-test-raw-{DATE}.txt").write_text(text, encoding="utf-8")
    try:
        results = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"JSON parse error at char {e.pos}: {e.msg}")
        print(f"Context: ...{text[max(0,e.pos-100):e.pos+100]}...")
        raise
    return results, usage, text


def analyze_results(findings: list[dict], picks_by_finding: dict[int, list[int]],
                     verses: list[dict]) -> str:
    vc_to_meta: dict[int, dict] = {v["vc_id"]: v for v in verses}

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
                sg_dist[SG_ID_TO_CODE.get(sg_id, "?")] += 1
                vcg_dist[vc_to_meta[vc].get("vcg_code", "?")] += 1
            else:
                invalid_picks.append(vc)

        qc = f["question_code"]
        is_relational = qc.startswith("T6.") or qc.startswith("T7.3.")
        is_clusterwide_t0 = qc.startswith("T0.")
        in_target_n = sg_dist.get("M01-A", 0)
        n_valid = len(valid_picks)
        per_finding.append({
            "finding_id": f["id"], "question_code": qc,
            "is_relational": is_relational,
            "is_clusterwide_t0": is_clusterwide_t0,
            "n_picks": len(picks), "n_valid": n_valid, "n_invalid": len(invalid_picks),
            "sg_distribution": dict(sg_dist),
            "vcg_distribution": dict(vcg_dist),
            "in_target_pct": (in_target_n / n_valid * 100) if n_valid > 0 else 0.0,
            "in_target_n": in_target_n,
        })

    total_valid = sum(r["n_valid"] for r in per_finding)
    total_in_target = sum(r["sg_distribution"].get("M01-A", 0) for r in per_finding)
    total_invalid = sum(r["n_invalid"] for r in per_finding)

    pure_target = [r for r in per_finding if r["n_valid"] > 0 and r["in_target_pct"] == 100]
    mixed = [r for r in per_finding if r["n_valid"] > 0 and r["in_target_pct"] < 100]
    empty = [r for r in per_finding if r["n_picks"] == 0]

    relational_mixed = [r for r in mixed if r["is_relational"]]
    t0_mixed = [r for r in mixed if r["is_clusterwide_t0"] and not r["is_relational"]]
    other_mixed = [r for r in mixed if not r["is_relational"] and not r["is_clusterwide_t0"]]

    # Per-VCG concentration within M01-A
    vcg_target_focus: Counter = Counter()
    for r in per_finding:
        for vcg_code, n in r["vcg_distribution"].items():
            if vcg_code and vcg_code.startswith("M01-A-VCG-"):
                vcg_target_focus[vcg_code] += n

    # Findings with low target rate (suspect)
    low_target = [r for r in per_finding if r["n_valid"] > 0 and r["in_target_pct"] < 50
                  and not r["is_relational"] and not r["is_clusterwide_t0"]]

    lines = [
        "# M01-A stress test — Inverted-validation against full M01 corpus",
        "",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"**Test design:** Hardest blind-verification — M01-A findings against the FULL M01 cluster corpus (8 sub-groups). Stress-tests AI's narrative discipline.",
        "",
        f"**Corpus:** {len(verses)} verses ({sum(1 for v in verses if v['cluster_subgroup_id']==58)} target M01-A · "
        f"{sum(1 for v in verses if v['cluster_subgroup_id']!=58)} distractors across 7 other sub-groups)",
        f"**Findings tested:** {len(findings)}",
        "",
        "---",
        "",
        "## Headline result",
        "",
        f"- Total picks: **{sum(r['n_picks'] for r in per_finding)}**",
        f"- Valid picks (in corpus): **{total_valid}**",
        f"- Invalid picks (hallucinated): **{total_invalid}**",
        f"- Empty pick lists (AI returned []): **{len(empty)}**",
        "",
        "### Target precision",
        "",
        f"- Picks in M01-A target: **{total_in_target} / {total_valid} = {100*total_in_target/max(total_valid,1):.1f}%**",
        f"- Pure-target findings (100% picks in M01-A): **{len(pure_target)} / {len(findings)} = {100*len(pure_target)/len(findings):.0f}%**",
        f"- Mixed findings: **{len(mixed)}**",
        f"  - Of which T6.x / T7.3.x (relational — cross-sub-group OK): **{len(relational_mixed)}**",
        f"  - Of which T0.x (cluster-wide divine-image prompts — cross-sub-group OK): **{len(t0_mixed)}**",
        f"  - Of which **other prompts with cross-sub-group picks (diagnostic)**: **{len(other_mixed)}**",
        f"- Empty pick lists (AI found no support): **{len(empty)}** — investigate for fabricated findings",
        "",
        "---",
        "",
        f"## Per-VCG distribution within M01-A (across all picks)",
        "",
        "| M01-A VCG | Picks |",
        "|---|---:|",
    ]
    for k in sorted(vcg_target_focus):
        lines.append(f"| `{k}` | {vcg_target_focus[k]} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    if empty:
        lines.append("## ⚠ Empty pick lists (suspect for fabrication)")
        lines.append("")
        lines.append("Findings where AI couldn't find ANY supporting verse from the 941-verse corpus.")
        lines.append("These warrant inspection — if no verse supports the finding, the finding may be unsubstantiated.")
        lines.append("")
        lines.append("| Finding | Q | Question excerpt |")
        lines.append("|---:|---|---|")
        for r in empty:
            f = next(x for x in findings if x["id"] == r["finding_id"])
            qx = (f["question_text"] or "")[:80]
            lines.append(f"| {r['finding_id']} | {r['question_code']} | {qx} |")
        lines.append("")
        lines.append("---")
        lines.append("")

    if low_target:
        lines.append("## ⚠ Low-target findings (non-relational, non-T0, <50% in M01-A)")
        lines.append("")
        lines.append("Most diagnostic — AI's picks for these prompts skew outside M01-A despite the finding being authored for M01-A scope.")
        lines.append("")
        lines.append("| Finding | Q | n_valid | %M01-A | Top non-target sub-group |")
        lines.append("|---:|---|---:|---:|---|")
        for r in sorted(low_target, key=lambda x: x["in_target_pct"]):
            d = r["sg_distribution"]
            non_t = {k: v for k, v in d.items() if k != "M01-A"}
            top_nt = max(non_t.items(), key=lambda x: x[1]) if non_t else ("—", 0)
            lines.append(f"| {r['finding_id']} | {r['question_code']} | {r['n_valid']} | "
                         f"{r['in_target_pct']:.0f}% | {top_nt[0]} ({top_nt[1]}) |")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## Per-finding distribution (full table)")
    lines.append("")
    lines.append("| Finding | Q | Type | n_valid | %M01-A | Distribution |")
    lines.append("|---:|---|---|---:|---:|---|")
    for r in per_finding:
        d = r["sg_distribution"]
        if not d:
            dist = "_(empty)_"
        else:
            dist = " · ".join(f"{k}:{v}" for k, v in sorted(d.items(), key=lambda x: -x[1])[:5])
        ftype = "T6+" if r["is_relational"] else ("T0" if r["is_clusterwide_t0"] else "")
        lines.append(f"| {r['finding_id']} | {r['question_code']} | {ftype} | "
                     f"{r['n_valid']} | {r['in_target_pct']:.0f}% | {dist} |")
    lines.append("")

    return "\n".join(lines)


def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    findings = fetch_findings(conn)
    verses = fetch_verse_corpus(conn)
    print(f"M01-A stress test: {len(findings)} findings, {len(verses)} verses")
    by_sg = Counter(SG_ID_TO_CODE.get(v["cluster_subgroup_id"], "?") for v in verses)
    print(f"  Corpus distribution: {dict(by_sg)}")

    system_prompt = build_system_prompt(verses)
    user_message = build_user_message(findings)
    print(f"System prompt: {len(system_prompt)} chars")
    print(f"User message: {len(user_message)} chars")

    test_input = {
        "test_design": "M01-A stress test — full M01 corpus distractors",
        "target": "M01-A (hidden from AI)",
        "n_findings": len(findings),
        "n_verses": len(verses),
        "corpus_distribution": dict(by_sg),
    }
    INPUT_JSON.write_text(json.dumps(test_input, indent=2, ensure_ascii=False), encoding="utf-8")

    client = anthropic.Anthropic()
    print(f"Model: {MODEL}\n")
    t0 = time.time()
    results, usage, raw = call_api_with_streaming(client, system_prompt, user_message)
    elapsed = time.time() - t0
    print(f"API: {elapsed:.1f}s, in={usage['input_tokens']} out={usage['output_tokens']} "
          f"cache_create={usage['cache_creation']} cache_read={usage['cache_read']}")

    picks_by_finding: dict[int, list[int]] = {}
    for r in results:
        fid = r.get("finding_id")
        if fid is not None:
            picks_by_finding[fid] = r.get("supporting_vc_ids", [])

    OUTPUT_JSON.write_text(json.dumps({
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "api_usage": usage, "elapsed_seconds": elapsed, "results": results,
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Output: {OUTPUT_JSON.relative_to(REPO)}")

    analysis_md = analyze_results(findings, picks_by_finding, verses)
    ANALYSIS_MD.write_text(analysis_md, encoding="utf-8")
    print(f"Analysis: {ANALYSIS_MD.relative_to(REPO)}")


if __name__ == "__main__":
    main()
