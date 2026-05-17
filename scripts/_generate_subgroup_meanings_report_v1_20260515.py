"""Generate the per-sub-group verse+meaning report (Phase 7 input).

Per wa-sessionb-cluster-instruction-v2_0-20260515 §9.7 — for each sub-group of the
cluster (post-Phase-6 verse-to-sub-group routing), list every routed verse with its
term and Phase 2 meaning, in canonical Bible order. This is AI's Phase 7 input:
the only material it uses to design new VCGs within each sub-group.

Suppressed by design: inherited VCG references, group_id values, anchor designations,
prior session findings. Per §2.3 the inherited-structure contamination guard is
structurally enforced — none of these appear in the report.

Usage:
  python scripts/_generate_subgroup_meanings_report_v1_20260515.py --m-cluster M01

Output:
  Sessions/Session_Clusters/{code}/wa-cluster-{code}-subgroup-meanings-v{N}-{date}.md
"""
from __future__ import annotations
import argparse, re, sqlite3, sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"


def next_version_for(out_dir: Path, prefix: str, date_str: str) -> str:
    pat = re.compile(rf"^{re.escape(prefix)}-v(\d+)-{date_str}\.md$")
    max_v = 0
    if out_dir.exists():
        for p in out_dir.iterdir():
            m = pat.match(p.name)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return f"v{max_v + 1}"


def build_report(conn, cluster_code: str) -> str:
    cluster = conn.execute(
        "SELECT * FROM cluster WHERE cluster_code=?", (cluster_code,)
    ).fetchone()
    if not cluster:
        raise RuntimeError(f"cluster {cluster_code} not found")

    # Sub-groups for the cluster
    subgroups = list(conn.execute("""
        SELECT id, subgroup_code, label, core_description, sort_order
        FROM cluster_subgroup
        WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
        ORDER BY sort_order, subgroup_code
    """, (cluster_code,)))
    if not subgroups:
        raise RuntimeError(f"cluster {cluster_code} has no active sub-groups — Phase 6 must run first")

    # Verses per sub-group (in canonical Bible order)
    by_sg_id: dict[int, list[dict]] = defaultdict(list)
    for r in conn.execute("""
        SELECT vc.id AS vc_id, vc.cluster_subgroup_id, vc.is_relevant, vc.analysis_note,
               vr.book_id, vr.chapter, vr.verse_num, vr.reference,
               mt.strongs_number, mt.transliteration, mt.gloss, mt.language
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
          AND mt.status IN ('extracted','extracted_thin') AND COALESCE(mt.delete_flagged,0)=0
          AND vc.is_relevant=1
          AND vc.cluster_subgroup_id IS NOT NULL
        ORDER BY vc.cluster_subgroup_id, vr.book_id, vr.chapter, vr.verse_num, mt.strongs_number, vc.id
    """, (cluster_code,)):
        by_sg_id[r["cluster_subgroup_id"]].append(dict(r))

    # Term counts per sub-group (from mti_term_subgroup; counts distinct terms)
    term_count_by_sg: dict[int, int] = {}
    for r in conn.execute("""
        SELECT mts.cluster_subgroup_id, COUNT(DISTINCT mts.mti_term_id) AS n
        FROM mti_term_subgroup mts
        JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
        WHERE cs.cluster_code=? AND COALESCE(mts.delete_flagged,0)=0
          AND COALESCE(cs.delete_flagged,0)=0
        GROUP BY mts.cluster_subgroup_id
    """, (cluster_code,)):
        term_count_by_sg[r["cluster_subgroup_id"]] = r["n"]

    # Sanity counts on missing meanings
    missing_meaning_count = 0
    for sg in subgroups:
        for v in by_sg_id.get(sg["id"], []):
            if not v["analysis_note"]:
                missing_meaning_count += 1

    # ===== Render =====
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# {cluster_code} {cluster['description']} — Per-sub-group verses + meanings")
    lines.append("")
    lines.append(f"**Generated:** {now_iso}  ")
    lines.append(f"**Cluster:** `{cluster_code}` ({cluster['short_name']}) · bucket={cluster['bucket']} · status={cluster['status']} · version={cluster['version']}  ")
    lines.append(f"**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §10 (Phase 7 — VCG design within sub-groups)  ")
    lines.append(f"**Source:** `database/bible_research.db`  ")
    lines.append("")
    lines.append("**Scope of this report:** per sub-group, every is_relevant verse routed there, with its term and Phase 2 meaning, in canonical Bible order. This is AI's Phase 7 input — the verse-meaning corpus per sub-group from which the new VCGs are clustered.")
    lines.append("")
    lines.append("**Suppressed by design** (per §2.3 inherited-structure contamination guard): inherited VCG references, group_id, anchor designations, prior session findings. None of these appear in this report.")
    lines.append("")
    if missing_meaning_count > 0:
        lines.append(f"> ⚠ **{missing_meaning_count} verses lack a Pass A meaning.** Phase 2 should be re-run for these before Phase 7 begins (per §5.6 hard gate). They are listed in §END at the end of this report.")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## §1. Summary")
    lines.append("")
    lines.append("| Sub-group | Label | Terms | Verses | Meanings present | Missing meanings |")
    lines.append("|---|---|---:|---:|---:|---:|")
    for sg in subgroups:
        verses = by_sg_id.get(sg["id"], [])
        with_m = sum(1 for v in verses if v["analysis_note"])
        missing = len(verses) - with_m
        lines.append(f"| `{sg['subgroup_code']}` | {sg['label']} | "
                     f"{term_count_by_sg.get(sg['id'], 0)} | {len(verses)} | {with_m} | {missing} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per sub-group section
    section_num = 2
    for sg in subgroups:
        verses = by_sg_id.get(sg["id"], [])
        lines.append(f"## §{section_num}. Sub-group `{sg['subgroup_code']}` — {sg['label']} ({len(verses)} verses)")
        lines.append("")
        lines.append(f"**Sub-group description (from Phase 5):** {sg['core_description'] or '_(no description recorded)_'}")
        lines.append("")
        if not verses:
            lines.append("_(no verses routed to this sub-group)_")
            lines.append("")
            section_num += 1
            continue
        lines.append("**Verses + meanings** (canonical Bible order):")
        lines.append("")
        lines.append("| vc_id | Reference | Strong's | Translit | Meaning |")
        lines.append("|---|---|---|---|---|")
        for v in verses:
            meaning = (v["analysis_note"] or "_(missing — re-run Phase 2)_").replace("|", "\\|").replace("\n", " ").strip()
            translit = (v["transliteration"] or "").strip()
            lines.append(f"| {v['vc_id']} | {v['reference']} | {v['strongs_number']} | {translit} | {meaning} |")
        lines.append("")
        section_num += 1

    if missing_meaning_count > 0:
        lines.append(f"## §END. Missing meanings — Phase 2 re-run required for these {missing_meaning_count} verses")
        lines.append("")
        lines.append("| vc_id | Reference | Strong's | Translit | Sub-group |")
        lines.append("|---|---|---|---|---|")
        for sg in subgroups:
            for v in by_sg_id.get(sg["id"], []):
                if not v["analysis_note"]:
                    lines.append(f"| {v['vc_id']} | {v['reference']} | {v['strongs_number']} | "
                                 f"{v['transliteration']} | `{sg['subgroup_code']}` |")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*End of per-sub-group verses + meanings report. Phase 7 input.*")
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
        version = next_version_for(out_dir, f"wa-cluster-{code}-subgroup-meanings", date_str)
        out_path = out_dir / f"wa-cluster-{code}-subgroup-meanings-{version}-{date_str}.md"
        out_path.write_text(report, encoding="utf-8")
        print(f"Wrote: {out_path.relative_to(REPO)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
