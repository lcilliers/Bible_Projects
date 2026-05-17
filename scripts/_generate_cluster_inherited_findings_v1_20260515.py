"""Generate the inherited-findings report for Phase 10 reconciliation.

Per wa-sessionb-cluster-instruction-v2_0-20260515 §13.1 — extracts every inherited
Session B finding, research flag, and Session D pointer attached to the cluster's
contributor registries that has not yet been resolved. AI's Phase 10 task is to
assign a disposition per row.

Linkage path: cluster's mti_terms → owning_registry_fk → word_registry → matching
rows in wa_session_b_findings / wa_session_research_flags / session_d_term_links.

Findings/flags with status='resolved_*' or resolved=1 are excluded — Phase 10 only
processes the unresolved set.

Usage:
  python scripts/_generate_cluster_inherited_findings_v1_20260515.py --m-cluster M01

Output:
  Sessions/Session_Clusters/{code}/WA-{code}-inherited-findings-for-reconciliation-v{N}-{date}.md
"""
from __future__ import annotations
import argparse, re, sqlite3, sys
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"

# Statuses considered "unresolved" — Phase 10 only processes these
SBF_UNRESOLVED_STATUSES = ("open", "pending", "confirmed")


def next_version_for(out_dir: Path, prefix: str, date_str: str) -> str:
    pat = re.compile(rf"^{re.escape(prefix)}-v(\d+)-{date_str}\.md$")
    max_v = 0
    if out_dir.exists():
        for p in out_dir.iterdir():
            m = pat.match(p.name)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return f"v{max_v + 1}"


def fetch_contributor_registries(conn, cluster_code: str) -> list[dict]:
    """Distinct word_registry rows that contributed terms to this cluster."""
    return list(conn.execute("""
        SELECT DISTINCT wr.no, wr.id AS registry_id, wr.word
        FROM word_registry wr
        JOIN mti_terms mt ON mt.owning_registry_fk = wr.id
        WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
          AND mt.status IN ('extracted','extracted_thin')
        ORDER BY wr.no
    """, (cluster_code,)))


def fetch_unresolved_findings(conn, registry_ids: list[int]) -> list[dict]:
    """wa_session_b_findings rows for the given registries, unresolved status."""
    if not registry_ids:
        return []
    placeholders = ",".join("?" * len(registry_ids))
    status_placeholders = ",".join("?" * len(SBF_UNRESOLVED_STATUSES))
    rows = list(conn.execute(f"""
        SELECT sbf.id, sbf.finding_id, sbf.registry_id, sbf.finding_type,
               sbf.finding, sbf.anchor_verses, sbf.raised_date, sbf.session_b_instruction,
               sbf.pass_ref, sbf.study_segment, sbf.status, sbf.thin_evidence,
               sbf.synthesis_outcome, sbf.tiers_engaged, sbf.structural_relationship,
               sbf.session_c_chapter, sbf.sd_pointer_ref, sbf.term_id,
               wr.no AS registry_no, wr.word AS registry_word
        FROM wa_session_b_findings sbf
        LEFT JOIN word_registry wr ON wr.id = sbf.registry_id
        WHERE sbf.registry_id IN ({placeholders})
          AND sbf.status IN ({status_placeholders})
          AND COALESCE(sbf.delete_flag, 0) = 0
        ORDER BY wr.no, sbf.id
    """, registry_ids + list(SBF_UNRESOLVED_STATUSES)))
    return [dict(r) for r in rows]


def fetch_unresolved_flags(conn, registry_ids: list[int]) -> list[dict]:
    """wa_session_research_flags rows for the given registries, not resolved."""
    if not registry_ids:
        return []
    placeholders = ",".join("?" * len(registry_ids))
    rows = list(conn.execute(f"""
        SELECT srf.id, srf.registry_id, srf.file_id, srf.flag_code, srf.flag_label,
               srf.strongs_reference, srf.cross_registry_id, srf.priority,
               srf.session_target, srf.description, srf.session_raised, srf.raised_date,
               srf.resolved, srf.resolved_date, srf.resolved_note,
               wr.no AS registry_no, wr.word AS registry_word
        FROM wa_session_research_flags srf
        LEFT JOIN word_registry wr ON wr.id = srf.registry_id
        WHERE srf.registry_id IN ({placeholders})
          AND COALESCE(srf.resolved, 0) = 0
        ORDER BY wr.no, srf.id
    """, registry_ids))
    return [dict(r) for r in rows]


def fetch_session_d_links(conn, cluster_code: str) -> list[dict]:
    """session_d_term_links rows for this cluster's terms (joined by Strong's, since the
    table uses strongs_id (text) rather than mti_term_id)."""
    rows = list(conn.execute("""
        SELECT sdtl.*, mt.transliteration, mt.gloss
        FROM session_d_term_links sdtl
        JOIN mti_terms mt ON mt.strongs_number = sdtl.strongs_id
        WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
          AND mt.status IN ('extracted','extracted_thin')
        ORDER BY sdtl.id
    """, (cluster_code,)))
    return [dict(r) for r in rows]


def build_report(conn, cluster_code: str) -> str:
    cluster = conn.execute(
        "SELECT * FROM cluster WHERE cluster_code=?", (cluster_code,)
    ).fetchone()
    if not cluster:
        raise RuntimeError(f"cluster {cluster_code} not found")

    contributors = fetch_contributor_registries(conn, cluster_code)
    registry_ids = [c["registry_id"] for c in contributors]
    findings = fetch_unresolved_findings(conn, registry_ids)
    flags = fetch_unresolved_flags(conn, registry_ids)
    sd_links = fetch_session_d_links(conn, cluster_code)

    # Group by registry for readability
    findings_by_reg: dict[int, list[dict]] = defaultdict(list)
    for f in findings:
        findings_by_reg[f["registry_id"]].append(f)
    flags_by_reg: dict[int, list[dict]] = defaultdict(list)
    flag_kinds_total = Counter()
    for fl in flags:
        flags_by_reg[fl["registry_id"]].append(fl)
        flag_kinds_total[fl["flag_code"]] += 1

    finding_types_total = Counter(f["finding_type"] for f in findings)

    # ===== Render =====
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# {cluster_code} {cluster['description']} — Inherited findings for Phase 10 reconciliation")
    lines.append("")
    lines.append(f"**Generated:** {now_iso}  ")
    lines.append(f"**Cluster:** `{cluster_code}` ({cluster['short_name']}) · status={cluster['status']} · version={cluster['version']}  ")
    lines.append(f"**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §13 (Phase 10 — Inherited-finding reconciliation)  ")
    lines.append(f"**Source:** `database/bible_research.db`  ")
    lines.append("")
    lines.append("**Scope:** every inherited Session B finding, research flag, and Session D pointer attached to this cluster's contributor registries that has **not been resolved** by the legacy pipeline. AI's Phase 10 task is to assign a disposition per row (see §13.2 of the instruction). Resolved rows (`status='resolved_*'` or `resolved=1`) are excluded.")
    lines.append("")
    lines.append("**Linkage path:** cluster's `mti_terms` → `owning_registry_fk` → `word_registry` → matching rows in `wa_session_b_findings`, `wa_session_research_flags`, and `session_d_*`.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Source | Total unresolved |")
    lines.append("|---|---:|")
    lines.append(f"| `wa_session_b_findings` (status IN ({', '.join(SBF_UNRESOLVED_STATUSES)})) | **{len(findings)}** |")
    lines.append(f"| `wa_session_research_flags` (resolved=0) | **{len(flags)}** |")
    lines.append(f"| `session_d_term_links` (this cluster's terms) | **{len(sd_links)}** |")
    lines.append("")
    lines.append(f"**Contributor registries:** {len(contributors)}")
    lines.append("")
    if contributors:
        lines.append("| no | registry_id | word |")
        lines.append("|---:|---:|---|")
        for c in contributors:
            lines.append(f"| {c['no']} | {c['registry_id']} | {c['word']} |")
        lines.append("")

    if finding_types_total:
        lines.append("**Finding types in unresolved set:**")
        lines.append("")
        for k, v in finding_types_total.most_common():
            lines.append(f"- `{k}`: {v}")
        lines.append("")
    if flag_kinds_total:
        lines.append("**Flag codes in unresolved set:**")
        lines.append("")
        for k, v in flag_kinds_total.most_common():
            lines.append(f"- `{k}`: {v}")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Disposition options (AI assigns one per row)")
    lines.append("")
    lines.append("Per v2_0 §13.2:")
    lines.append("")
    lines.append("| Disposition | Meaning |")
    lines.append("|---|---|")
    lines.append("| `RESOLVED-BY-CATALOGUE` | finding is already captured in one of the new cluster_finding rows (T0–T7) — name the cluster_finding id(s) |")
    lines.append("| `FOLD-INTO-PROMPT` | finding adds new evidence to an existing cluster_finding — name target prompt + scope |")
    lines.append("| `NEW-CLUSTER-FINDING` | finding is real new evidence that doesn't fit any existing prompt — name a target T-code |")
    lines.append("| `SUPERSEDED` | finding was authored under the pre-cluster-pivot lens and is no longer relevant — name replacing cluster_finding |")
    lines.append("| `CARRY-TO-SESSION-D` | finding is cross-cluster / cross-registry and belongs to Session D, not this cluster |")
    lines.append("| `RESEARCHER-DECISION` | AI cannot decide — surface for researcher |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Findings per registry
    lines.append("## §1. Unresolved Session B findings")
    lines.append("")
    if not findings:
        lines.append("_(None — no unresolved Session B findings tied to this cluster's contributor registries.)_")
        lines.append("")
    else:
        for c in contributors:
            reg_findings = findings_by_reg.get(c["registry_id"], [])
            if not reg_findings:
                continue
            lines.append(f"### R{c['no']:03d} {c['word']} — {len(reg_findings)} unresolved")
            lines.append("")
            for f in reg_findings:
                lines.append(f"#### sbf.id={f['id']} · finding_id={f['finding_id']!r} · status=`{f['status']}` · type=`{f['finding_type']}`")
                lines.append("")
                lines.append(f"- Raised: {f['raised_date']!r}  ·  Pass: {f['pass_ref']!r}  ·  Segment: {f['study_segment']!r}")
                if f.get("session_b_instruction"):
                    lines.append(f"- Instruction version: `{f['session_b_instruction']}`")
                if f.get("synthesis_outcome"):
                    lines.append(f"- Synthesis outcome: {f['synthesis_outcome']!r}")
                if f.get("tiers_engaged"):
                    lines.append(f"- Tiers engaged: {f['tiers_engaged']!r}")
                if f.get("structural_relationship"):
                    lines.append(f"- Structural relationship: {f['structural_relationship']!r}")
                if f.get("anchor_verses"):
                    anchors = (f["anchor_verses"] or "")[:300]
                    lines.append(f"- Anchor verses: {anchors}")
                if f.get("sd_pointer_ref"):
                    lines.append(f"- SD pointer ref: {f['sd_pointer_ref']!r}")
                lines.append("")
                # Finding text in a blockquote
                finding_text = (f["finding"] or "").replace("\r\n", "\n").strip()
                for fl_line in finding_text.split("\n"):
                    lines.append(f"> {fl_line}")
                lines.append("")
                lines.append(f"**Disposition (AI):** ____________  ·  **Target cluster_finding id / T-code:** ____________  ·  **Rationale:** ____________")
                lines.append("")
                lines.append("---")
                lines.append("")

    # Flags per registry
    lines.append("## §2. Unresolved research flags")
    lines.append("")
    if not flags:
        lines.append("_(None — no unresolved research flags tied to this cluster's contributor registries.)_")
        lines.append("")
    else:
        for c in contributors:
            reg_flags = flags_by_reg.get(c["registry_id"], [])
            if not reg_flags:
                continue
            lines.append(f"### R{c['no']:03d} {c['word']} — {len(reg_flags)} unresolved")
            lines.append("")
            for fl in reg_flags:
                lines.append(f"#### srf.id={fl['id']} · flag_code=`{fl['flag_code']}` · priority={fl['priority']!r}")
                lines.append("")
                lines.append(f"- Label: {fl['flag_label']!r}")
                if fl.get("strongs_reference"):
                    lines.append(f"- Strong's ref: `{fl['strongs_reference']}`")
                if fl.get("cross_registry_id"):
                    lines.append(f"- Cross-registry: {fl['cross_registry_id']}")
                lines.append(f"- Raised: {fl['raised_date']!r}  ·  Session target: {fl['session_target']!r}")
                lines.append("")
                desc = (fl["description"] or "").replace("\r\n", "\n").strip()
                for fl_line in desc.split("\n"):
                    lines.append(f"> {fl_line}")
                lines.append("")
                lines.append(f"**Disposition (AI):** ____________  ·  **Rationale:** ____________")
                lines.append("")
                lines.append("---")
                lines.append("")

    # SD pointers
    lines.append("## §3. Session D term links")
    lines.append("")
    if not sd_links:
        lines.append("_(None — no `session_d_term_links` rows reference this cluster's terms.)_")
        lines.append("")
    else:
        lines.append(f"{len(sd_links)} `session_d_term_links` rows reference this cluster's terms. Inspect for dispositions:")
        lines.append("")
        for sdl in sd_links:
            lines.append(f"- sdtl.id={sdl['id']}  ·  run_id={sdl['run_id']!r}  ·  "
                         f"{sdl['strongs_id']} {sdl['transliteration']} ({sdl['gloss']})  ·  "
                         f"gate={sdl['gate']!r}  ·  status_divergence={sdl['status_divergence']}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Output reconciliation document (AI authors this)")
    lines.append("")
    lines.append("AI produces `Sessions/Session_Clusters/{code}/WA-{code}-inherited-findings-reconciliation-v1-{date}.md` carrying the dispositions and rationales per row.")
    lines.append("")
    lines.append("Then CC executes the reconciliation directive `wa-cluster-{code}-dir-NNN-inherited-findings-reconcile-v1-{date}.md` per v2_0 §13.4.")
    lines.append("")
    lines.append("*End of inherited-findings report.*")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    args = ap.parse_args()

    code = args.m_cluster.strip()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    try:
        report = build_report(conn, code)
        out_dir = REPO / "Sessions" / "Session_Clusters" / code
        out_dir.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
        version = next_version_for(out_dir, f"WA-{code}-inherited-findings-for-reconciliation", date_str)
        out_path = out_dir / f"WA-{code}-inherited-findings-for-reconciliation-{version}-{date_str}.md"
        out_path.write_text(report, encoding="utf-8")
        print(f"Wrote: {out_path.relative_to(REPO)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
