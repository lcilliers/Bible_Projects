"""Pre-analysis of Phase 9 findings distribution before cluster-synthesis.

Reads cluster_finding rows for a cluster and produces a report:
  §1 E/S/G distribution per characteristic
  §2 E/S/G distribution per tier
  §3 E/S/G distribution per prompt — sorted by "synthesis weight"
      (high weight = many chars evidenced; low weight = mostly silent)
  §4 Buckets of prompts by synthesis weight:
      - "broad evidence" (≥75% chars evidenced E)
      - "broad silence" (≥75% chars silent S/G)
      - "divergent" (mixed E and S — the interesting tension cases)
  §5 Per-characteristic strength (% of 189 prompts with E findings)
  §6 Tier × E-count crosstab

Output: Sessions/Session_Clusters/{CODE}/wa-cluster-{CODE}-phase9-findings-distribution-v{N}-{date}.md
"""
from __future__ import annotations
import argparse, re, sqlite3, sys, io
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"


# Candidate primary-characteristic grouping for M10
# (CC's preliminary proposal — to be validated/refined by AI clustering session)
# Maps primary characteristic short_name → list of aspect char_seq values
M10_PRIMARY_GROUPING: dict[str, dict] = {
    "Sin as act / will": {
        "definition": (
            "The volitional dimension of moral failure — the will in the moment of, "
            "or in the pattern of, sinning. Covers the act-quality of sin (deliberate "
            "vs unintentional), the will's persistence in sin (habitual vs occasional), "
            "and its refusal to turn back, plus transgression as the wilful crossing "
            "of a known boundary."
        ),
        "members": [1, 2, 5, 6, 19],
    },
    "Sin as state / condition": {
        "definition": (
            "The ontological dimension of sin — what the inner person IS under sin's "
            "weight, rather than what they did. Universal human condition, enslaving "
            "power, the divine record of accumulated wrongdoing, the sinner as moral "
            "category, iniquity as moral-spiritual debt before God."
        ),
        "members": [11, 12, 13, 16, 18],
    },
    "Sin's social transmission": {
        "definition": (
            "Sin's spread through social, relational, and covenantal bonds — leadership "
            "corrupting those under authority, political revolt as breaking submission, "
            "sin transmitted generationally, faithlessness as covenant-betrayal."
        ),
        "members": [7, 8, 15, 20],
    },
    "Specific sinful expressions": {
        "definition": (
            "Sin expressed in distinct surface forms identified by the cluster — sinful "
            "speech (blasphemy/slander), specialised inner mechanisms (enticement, "
            "hypocrisy, apostasy), perversion as moral inversion, and injustice as "
            "moral failure toward persons."
        ),
        "members": [9, 10, 21, 22],
    },
    "Conscience response to sin": {
        "definition": (
            "The inner-being responses to one's own sin — the conscience naming sin "
            "(confession), the conscience denying sin (suppression / self-deception), "
            "the felt experience of being guilty, and the movement toward divine "
            "forgiveness and its reception."
        ),
        "members": [3, 4, 14, 17],
    },
}


def next_version_for(out_dir: Path, prefix: str, date_str: str) -> str:
    pat = re.compile(rf"^{re.escape(prefix)}-v(\d+)-{date_str}\.md$")
    max_v = 0
    if out_dir.exists():
        for p in out_dir.iterdir():
            m = pat.match(p.name)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return f"v{max_v + 1}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    args = ap.parse_args()
    cluster = args.cluster.strip()

    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row

    chars = conn.execute(
        "SELECT id, char_seq, short_name FROM characteristic "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 ORDER BY char_seq",
        (cluster,)
    ).fetchall()
    n_chars = len(chars)
    char_seq_by_id = {c["id"]: c["char_seq"] for c in chars}
    char_name_by_seq = {c["char_seq"]: c["short_name"] for c in chars}

    rows = conn.execute(
        """
        SELECT q.question_code, q.tier, q.component_code,
               cf.characteristic_id, cf.finding_status, cf.finding_text
        FROM cluster_finding cf
        JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
        WHERE cf.cluster_code = ?
          AND cf.characteristic_id IS NOT NULL
          AND COALESCE(cf.delete_flagged, 0) = 0
        ORDER BY q.tier, q.component_code, q.prompt_seq
        """,
        (cluster,)
    ).fetchall()

    # Aggregations
    by_char_status: dict[int, Counter] = defaultdict(Counter)
    by_tier_status: dict[str, Counter] = defaultdict(Counter)
    by_prompt: dict[str, dict] = defaultdict(lambda: {
        "tier": None, "component": None,
        "status_counts": Counter(),
        "chars_E": [], "chars_S": [], "chars_G": [],
        "finding_lengths": []
    })

    for r in rows:
        cseq = char_seq_by_id[r["characteristic_id"]]
        status = r["finding_status"]
        by_char_status[cseq][status] += 1
        by_tier_status[r["tier"]][status] += 1
        p = by_prompt[r["question_code"]]
        p["tier"] = r["tier"]
        p["component"] = r["component_code"]
        p["status_counts"][status] += 1
        if status == "finding":
            p["chars_E"].append(cseq)
        elif status == "silent":
            p["chars_S"].append(cseq)
        elif status == "gap":
            p["chars_G"].append(cseq)
        p["finding_lengths"].append(len(r["finding_text"] or ""))

    n_prompts = len(by_prompt)
    print(f"Loaded {len(rows)} cluster_finding rows across {n_chars} characteristics, {n_prompts} prompts")

    # Build report
    date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
    out_dir = REPO / "Sessions" / "Session_Clusters" / cluster
    version = next_version_for(out_dir, f"wa-cluster-{cluster}-phase9-findings-distribution", date_str)
    out_path = out_dir / f"wa-cluster-{cluster}-phase9-findings-distribution-{version}-{date_str}.md"

    L: list[str] = []
    L.append(f"# {cluster} — Phase 9 findings distribution (pre-synthesis analytics)")
    L.append("")
    L.append(f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    L.append(f"**Source:** `cluster_finding` table — {len(rows)} rows × {n_chars} characteristics × {n_prompts} prompts")
    L.append("")
    L.append("**Purpose:** characterise the findings landscape **before** the cluster-synthesis session so the synthesis is packaged sensibly — e.g. silent-dominated prompts handled separately from evidence-rich ones; per-characteristic synthesis precedes cross-characteristic comparison.")
    L.append("")
    L.append("---")
    L.append("")

    # §0 Candidate primary-characteristic grouping (M10 only)
    if cluster == "M10":
        L.append("## §0. Candidate primary-characteristic grouping (CC preliminary)")
        L.append("")
        L.append(f"CC's preliminary proposal: cluster the {n_chars} aspect-characteristics into "
                 f"**{len(M10_PRIMARY_GROUPING)} primary characteristics** for synthesis purposes. "
                 "The 22 finer aspects remain correct for verse routing; they are *aspects* of these "
                 "5 primaries. Per-primary distillation precedes cross-primary cluster synthesis.")
        L.append("")
        L.append("**Mapping (22 → 5):**")
        L.append("")
        L.append("| Primary | Aspects | Total E | Total S | E % |")
        L.append("|---|---|---:|---:|---:|")
        all_assigned: set[int] = set()
        for pname, pinfo in M10_PRIMARY_GROUPING.items():
            members = pinfo["members"]
            all_assigned.update(members)
            tot_e = sum(by_char_status[m].get("finding", 0) for m in members)
            tot_s = sum(by_char_status[m].get("silent", 0) for m in members)
            tot_g = sum(by_char_status[m].get("gap", 0) for m in members)
            grand = tot_e + tot_s + tot_g
            e_pct = (tot_e / grand * 100) if grand else 0
            aspect_str = ", ".join(
                f"{m} {char_name_by_seq.get(m, '?')}" for m in members
            )
            L.append(f"| **{pname}** ({len(members)}) | {aspect_str} | {tot_e} | {tot_s} | {e_pct:.1f}% |")
        # Sanity check: every aspect mapped
        unmapped = [c["char_seq"] for c in chars if c["char_seq"] not in all_assigned]
        if unmapped:
            L.append("")
            L.append(f"⚠️ **UNMAPPED aspects (CC bug):** {unmapped}")
        L.append("")
        L.append("**Per-primary definitions:**")
        L.append("")
        for pname, pinfo in M10_PRIMARY_GROUPING.items():
            L.append(f"### {pname} ({len(pinfo['members'])} aspects)")
            L.append("")
            L.append(f"> {pinfo['definition']}")
            L.append("")
            aspects_inline = ', '.join(f"CHAR-{m} {char_name_by_seq.get(m, '?')}" for m in pinfo['members'])
            L.append(f"Aspects: {aspects_inline}")
            L.append("")
        L.append("---")
        L.append("")

    # §1 Per-characteristic distribution
    L.append("## §1. E / S / G distribution per characteristic")
    L.append("")
    L.append("| Char | Short name | E | S | G | E % | S % |")
    L.append("|---:|---|---:|---:|---:|---:|---:|")
    for c in chars:
        cnt = by_char_status[c["char_seq"]]
        e, s, g = cnt.get("finding", 0), cnt.get("silent", 0), cnt.get("gap", 0)
        total = e + s + g
        e_pct = (e / total * 100) if total else 0
        s_pct = (s / total * 100) if total else 0
        L.append(f"| {c['char_seq']} | {c['short_name']} | {e} | {s} | {g} | {e_pct:.1f}% | {s_pct:.1f}% |")
    L.append("")
    # Aggregate
    total_e = sum(by_char_status[c["char_seq"]].get("finding", 0) for c in chars)
    total_s = sum(by_char_status[c["char_seq"]].get("silent", 0) for c in chars)
    total_g = sum(by_char_status[c["char_seq"]].get("gap", 0) for c in chars)
    grand = total_e + total_s + total_g
    L.append(f"**Cluster aggregate:** E={total_e} ({total_e/grand*100:.1f}%) · "
             f"S={total_s} ({total_s/grand*100:.1f}%) · "
             f"G={total_g} ({total_g/grand*100:.1f}%) · "
             f"Total={grand}")
    L.append("")
    L.append("---")
    L.append("")

    # §2 Per-tier distribution
    L.append("## §2. E / S / G distribution per tier")
    L.append("")
    L.append("| Tier | E | S | G | E % | S % | Avg E-per-prompt |")
    L.append("|---|---:|---:|---:|---:|---:|---:|")
    prompts_per_tier = {"T0": 12, "T1": 24, "T2": 31, "T3": 33, "T4": 24, "T5": 21, "T6": 24, "T7": 20}
    for tier in ["T0","T1","T2","T3","T4","T5","T6","T7"]:
        cnt = by_tier_status[tier]
        e, s, g = cnt.get("finding", 0), cnt.get("silent", 0), cnt.get("gap", 0)
        total = e + s + g
        if not total:
            continue
        e_pct = (e / total * 100)
        s_pct = (s / total * 100)
        avg_e = e / prompts_per_tier.get(tier, 1)
        L.append(f"| {tier} | {e} | {s} | {g} | {e_pct:.1f}% | {s_pct:.1f}% | {avg_e:.1f} / {n_chars} |")
    L.append("")
    L.append("---")
    L.append("")

    # §3 Bucket prompts by synthesis weight
    L.append("## §3. Prompt buckets by synthesis weight")
    L.append("")
    L.append("Each prompt is bucketed by how many of the cluster's characteristics evidenced it. **Synthesis weight** = number of `E` findings out of the N characteristics. High weight = many independent E findings to compare → rich synthesis work. Low weight (= many silent) = the cluster is broadly silent on this prompt → synthesis is short and structural.")
    L.append("")
    bucket_broad_e = []        # ≥75% E
    bucket_broad_silence = []  # ≥75% S+G
    bucket_divergent = []      # mixed
    threshold_high = int(n_chars * 0.75)
    threshold_low = int(n_chars * 0.25)
    for qc, p in by_prompt.items():
        n_e = len(p["chars_E"])
        if n_e >= threshold_high:
            bucket_broad_e.append((qc, p))
        elif n_e <= threshold_low:
            bucket_broad_silence.append((qc, p))
        else:
            bucket_divergent.append((qc, p))
    L.append(f"- **Broad evidence** (≥{threshold_high}/{n_chars} chars evidenced E): **{len(bucket_broad_e)} prompts**")
    L.append(f"- **Broad silence** (≤{threshold_low}/{n_chars} chars evidenced E): **{len(bucket_broad_silence)} prompts**")
    L.append(f"- **Divergent** (between {threshold_low+1} and {threshold_high-1} chars E): **{len(bucket_divergent)} prompts**")
    L.append("")
    L.append("**Sample broad-evidence prompts (top 15 by E count):**")
    L.append("")
    L.append("| Prompt | E count | E chars (first 8) |")
    L.append("|---|---:|---|")
    bucket_broad_e_sorted = sorted(bucket_broad_e, key=lambda x: -len(x[1]["chars_E"]))
    for qc, p in bucket_broad_e_sorted[:15]:
        sample = ", ".join(f"{cs}" for cs in sorted(p["chars_E"])[:8])
        more = f"... +{len(p['chars_E']) - 8}" if len(p["chars_E"]) > 8 else ""
        L.append(f"| {qc} | {len(p['chars_E'])} | {sample}{more} |")
    L.append("")
    L.append("**Sample broad-silence prompts (top 15 by S count):**")
    L.append("")
    L.append("| Prompt | S count | E count | E chars |")
    L.append("|---|---:|---:|---|")
    bucket_broad_silence_sorted = sorted(bucket_broad_silence, key=lambda x: -len(x[1]["chars_S"]))
    for qc, p in bucket_broad_silence_sorted[:15]:
        e_chars = ", ".join(str(c) for c in sorted(p["chars_E"]))
        L.append(f"| {qc} | {len(p['chars_S'])} | {len(p['chars_E'])} | {e_chars or '(none)'} |")
    L.append("")
    L.append("**Sample divergent prompts (top 15 by S-vs-E spread):**")
    L.append("")
    L.append("| Prompt | E | S | G |")
    L.append("|---|---:|---:|---:|")
    bucket_divergent_sorted = sorted(bucket_divergent, key=lambda x: -abs(len(x[1]["chars_E"]) - len(x[1]["chars_S"])))
    for qc, p in bucket_divergent_sorted[:15]:
        L.append(f"| {qc} | {len(p['chars_E'])} | {len(p['chars_S'])} | {len(p['chars_G'])} |")
    L.append("")
    L.append("---")
    L.append("")

    # §4 Per-tier × bucket
    L.append("## §4. Buckets per tier")
    L.append("")
    L.append("| Tier | Broad evidence | Broad silence | Divergent |")
    L.append("|---|---:|---:|---:|")
    for tier in ["T0","T1","T2","T3","T4","T5","T6","T7"]:
        be = sum(1 for qc, p in bucket_broad_e if p["tier"] == tier)
        bs = sum(1 for qc, p in bucket_broad_silence if p["tier"] == tier)
        dv = sum(1 for qc, p in bucket_divergent if p["tier"] == tier)
        L.append(f"| {tier} | {be} | {bs} | {dv} |")
    L.append("")
    L.append("---")
    L.append("")

    # §5 Per-characteristic strength
    L.append("## §5. Per-characteristic strength (E % across 189 prompts)")
    L.append("")
    L.append("Characteristics with low E % had broadly thin evidence corpora for the catalogue's question-set — their contribution to cluster synthesis is structural ('this characteristic is broadly silent on the catalogue'). Characteristics with high E % drive the cross-characteristic comparison.")
    L.append("")
    L.append("| Char | Short name | E count | E % | Strength |")
    L.append("|---:|---|---:|---:|---|")
    chars_sorted = sorted(chars, key=lambda c: -by_char_status[c["char_seq"]].get("finding", 0))
    for c in chars_sorted:
        e = by_char_status[c["char_seq"]].get("finding", 0)
        pct = e / 189 * 100
        if pct >= 70:
            strength = "HIGH"
        elif pct >= 40:
            strength = "MEDIUM"
        else:
            strength = "LOW"
        L.append(f"| {c['char_seq']} | {c['short_name']} | {e} | {pct:.1f}% | {strength} |")
    L.append("")
    L.append("---")
    L.append("")

    # §6 Synthesis-load summary
    L.append("## §6. Synthesis load summary")
    L.append("")
    L.append("If the cluster synthesis runs in a single session against the full matrix, the AI reads:")
    L.append("")
    avg_len = sum(p["finding_lengths"][0] for p in by_prompt.values() for _ in [p["finding_lengths"]]) / max(len(rows), 1)
    total_chars_to_read = sum(sum(p["finding_lengths"]) for p in by_prompt.values())
    L.append(f"- {len(rows)} finding blocks")
    L.append(f"- Total character count in finding bodies: ~{total_chars_to_read:,}")
    L.append(f"- Equivalent to ~{total_chars_to_read // 4500:,} pages of analytical text")
    L.append("")
    L.append("**Recommended packaging given this distribution:**")
    L.append("")
    if len(bucket_broad_silence) > n_prompts * 0.3:
        L.append(f"- Broad-silence bucket is large ({len(bucket_broad_silence)} / {n_prompts} prompts). These can be synthesised in batch with a brief that authorises a single-line cluster-scope finding ('cluster broadly silent on this prompt; only chars X, Y, Z evidence — see their findings for the residual signal').")
    if len(bucket_broad_e) > 0:
        L.append(f"- Broad-evidence bucket ({len(bucket_broad_e)} prompts) carries the bulk of the comparative work and deserves the most careful per-prompt synthesis.")
    if len(bucket_divergent) > 0:
        L.append(f"- Divergent bucket ({len(bucket_divergent)} prompts) is where the most interesting cross-characteristic tensions live — these warrant dedicated attention.")
    L.append("")
    L.append("**Per-characteristic synthesis (pre-cross-cluster):** each of the 22 characteristics has 189 findings of its own. If a per-characteristic distillation precedes cross-characteristic synthesis, the cluster-scope AI session reads N characteristic-summaries instead of N × 189 raw blocks.")
    L.append("")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote: {out_path.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
