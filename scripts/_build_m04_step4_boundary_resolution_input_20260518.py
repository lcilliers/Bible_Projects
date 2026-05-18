"""M04 retrofit Step 4: build BOUNDARY-resolution input document for AI (Phase 8.5).

Per v2_5 §11A.1, the input includes:
1. BOUNDARY content report — per BOUNDARY term, verse list + Pass A meanings + current placement
2. Co-occurrence list — for each BOUNDARY verse, other clusters' active terms at same verse_record_id
3. Programme cluster catalogue — every cluster's characteristic statement
4. Cluster's current sub-group + VCG structure (PROMOTE-TO-SUBGROUP targets)

AI is then asked to propose, per BOUNDARY vc_id, one of three §18.2 dispositions:
- SET-ASIDE (no inner-being state; §4.5.1-valid reason required)
- ROUTE-TO-CLUSTER (verse's primary content belongs to another cluster; requires
  target-cluster term at same verse_record_id)
- PROMOTE-TO-SUBGROUP (verse carries inner-being content; assign to existing
  M04 sub-group or propose new)

Output: Sessions/Session_Clusters/M04/WA-M04-step4-boundary-resolution-input-v1-{date}.md
"""
from __future__ import annotations
import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
OUT = Path(f"Sessions/Session_Clusters/M04/WA-M04-step4-boundary-resolution-input-v1-{TODAY}.md")


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # 1. BOUNDARY verses with Pass A meaning, grouped by term
    rows = conn.execute(
        """
        SELECT vc.id AS vc_id, vc.mti_term_id, vc.analysis_note,
               mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
               vr.id AS vr_id, vr.reference, vr.book_id, vr.chapter, vr.verse_num,
               vr.verse_text, vr.context_before, vr.context_after
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE cs.cluster_code = 'M04' AND cs.subgroup_code = 'M04-BOUNDARY'
          AND vc.is_relevant = 1 AND COALESCE(vc.delete_flagged, 0) = 0
        ORDER BY mt.strongs_number, vr.book_id, vr.chapter, vr.verse_num
        """
    ).fetchall()
    by_term = defaultdict(list)
    for r in rows:
        by_term[(r["strongs_number"], r["transliteration"], r["gloss"])].append(dict(r))

    print(f"M04-BOUNDARY relevant verses to disposition: {len(rows)}")
    print(f"BOUNDARY terms: {len(by_term)}")

    # 2. Co-occurrence: for each BOUNDARY vr_id, find other-cluster active terms
    vr_ids = list({r["vr_id"] for r in rows})
    placeholders = ",".join("?" * len(vr_ids))
    cooccur_rows = conn.execute(
        f"""
        SELECT vc.verse_record_id AS vr_id, mt.strongs_number, mt.transliteration,
               mt.cluster_code, vr.reference,
               (SELECT cluster_code FROM cluster WHERE cluster_code = mt.cluster_code) AS exists_check,
               c.short_name AS cluster_short, c.gloss AS cluster_gloss
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN cluster c ON c.cluster_code = mt.cluster_code
        WHERE vc.verse_record_id IN ({placeholders})
          AND mt.cluster_code != 'M04'
          AND mt.cluster_code IS NOT NULL
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
        """,
        vr_ids,
    ).fetchall()
    cooccur = defaultdict(list)
    for r in cooccur_rows:
        cooccur[r["vr_id"]].append({
            "strongs": r["strongs_number"],
            "translit": r["transliteration"],
            "cluster": r["cluster_code"],
            "cluster_short": r["cluster_short"],
        })

    # 3. Programme cluster catalogue (active clusters with characteristic-ish text)
    clusters = conn.execute(
        """
        SELECT cluster_code, COALESCE(short_name, cluster_code) AS short_name,
               description, gloss, status
        FROM cluster
        WHERE cluster_code LIKE 'M%' AND status NOT LIKE '%Not started%'
        ORDER BY cluster_code
        """
    ).fetchall()

    # 4. M04 substantive sub-groups (PROMOTE-TO-SUBGROUP targets)
    m04_subgroups = conn.execute(
        """
        SELECT id, subgroup_code, label, core_description,
               (SELECT COUNT(*) FROM verse_context vc2
                WHERE vc2.cluster_subgroup_id = cs.id AND vc2.is_relevant=1
                AND COALESCE(vc2.delete_flagged,0)=0) AS verse_count
        FROM cluster_subgroup cs
        WHERE cluster_code='M04' AND COALESCE(delete_flagged,0)=0
          AND subgroup_code != 'M04-BOUNDARY'
        ORDER BY sort_order
        """
    ).fetchall()

    # Build document
    L = []
    L.append("# M04 Step 4 — Phase 8.5 BOUNDARY resolution input for AI")
    L.append("")
    L.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
    L.append(f"**Governing instruction:** wa-sessionb-cluster-instruction-v2_5-20260518 §11A (Phase 8.5) + §18.2 verse-level dispositions")
    L.append(f"**Task:** propose a per-verse disposition (SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP) for every BOUNDARY verse listed below.")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Your task")
    L.append("")
    L.append(f"For each of the **{len(rows)} BOUNDARY vc_ids** below, propose one of:")
    L.append("")
    L.append("- **SET-ASIDE** — the verse evidences no inner-being state. Give an evidence-based §4.5.1-valid reason (verse-specific; not 'physical_only' or 'no_inner_being' terse strings). Example: \"'good appearance' in Dan 1:4 describes external physical attractiveness, not an inner-being state.\"")
    L.append("- **ROUTE-TO-CLUSTER {code}** — the verse's primary inner-being content belongs to another cluster. **Eligibility check (§18.2):** the target cluster MUST have an active term at the same `verse_record_id`. Use the co-occurrence list to verify. If no target-cluster term exists, the disposition is SET-ASIDE, not ROUTE-TO-CLUSTER.")
    L.append("- **PROMOTE-TO-SUBGROUP {code}** — the verse carries M04 inner-being content. Assign to an existing M04 sub-group (M04-A through M04-P) OR propose a new one with `core_description`.")
    L.append("")
    L.append("**Output format:** one line per vc_id, like `vc=12345 PROMOTE-TO-SUBGROUP M04-K — rationale...` or `vc=12345 SET-ASIDE — rationale...` or `vc=12345 ROUTE-TO-CLUSTER M22 — rationale (target term: H1234 at this verse).`")
    L.append("")
    L.append("**Forbidden:** PARK, DEFER, HOLD, RESEARCHER-DECISION-LATER — every vc_id must receive one of the three.")
    L.append("")
    L.append("**Read every verse individually.** Do not bulk-classify by term. Each vc_id deserves a per-verse decision rooted in its specific Pass A meaning and verse text.")
    L.append("")
    L.append("**Be alert to v2_5 §1.1 scope:** inner being covers the entire human inner life — vertical, horizontal, sensory, evaluative, illicit. Do NOT set-aside because the verse \"lacks God-directed framing\" or \"is too sensory/material.\" Only set-aside if no inner-being state is evidenced at all.")
    L.append("")
    L.append("---")
    L.append("")

    L.append("## M04 substantive sub-groups (PROMOTE-TO-SUBGROUP targets)")
    L.append("")
    L.append("| Code | Verses | Label |")
    L.append("|---|---:|---|")
    for sg in m04_subgroups:
        L.append(f"| **{sg['subgroup_code']}** | {sg['verse_count']} | {sg['label']} |")
    L.append("")
    L.append("### Sub-group core_descriptions")
    L.append("")
    for sg in m04_subgroups:
        L.append(f"**{sg['subgroup_code']}** — {sg['label']}")
        L.append("")
        L.append(f"> {sg['core_description']}")
        L.append("")
    L.append("---")
    L.append("")

    L.append("## Programme cluster catalogue (ROUTE-TO-CLUSTER targets)")
    L.append("")
    L.append("Use to validate ROUTE-TO-CLUSTER target eligibility. Routing is only valid when the target cluster has an active term at the same `verse_record_id` (see co-occurrence list per verse below).")
    L.append("")
    L.append("| Code | Short name | Description excerpt |")
    L.append("|---|---|---|")
    for c in clusters:
        desc = (c["description"] or c["gloss"] or "")[:120].replace("|", "\\|")
        L.append(f"| {c['cluster_code']} | {c['short_name']} | {desc} |")
    L.append("")
    L.append("---")
    L.append("")

    L.append("## BOUNDARY verses (per term)")
    L.append("")

    for (strongs, translit, gloss), verses in sorted(by_term.items()):
        L.append(f"### {strongs} {translit} — {gloss} ({len(verses)} verses)")
        L.append("")
        for v in verses:
            L.append(f"#### vc={v['vc_id']} — {v['reference']}")
            L.append("")
            text = (v["verse_text"] or "").strip()
            ctx_before = (v["context_before"] or "").strip()
            ctx_after = (v["context_after"] or "").strip()
            if ctx_before:
                L.append(f"> _… {ctx_before}_")
            L.append(f"> **{text}**")
            if ctx_after:
                L.append(f"> _{ctx_after} …_")
            L.append("")
            L.append(f"**Pass A meaning:** {v['analysis_note']}")
            L.append("")
            # Co-occurrence (other clusters' terms at this vr)
            co_list = cooccur.get(v["vr_id"], [])
            if co_list:
                co_str = ", ".join(f"{c['cluster']}/{c['strongs']} {c['translit']}" for c in co_list[:8])
                more = f" (+{len(co_list)-8} more)" if len(co_list) > 8 else ""
                L.append(f"**Co-occurring other-cluster terms (eligibility for ROUTE-TO-CLUSTER):** {co_str}{more}")
            else:
                L.append(f"**Co-occurring other-cluster terms:** _none — ROUTE-TO-CLUSTER not eligible; choose SET-ASIDE or PROMOTE-TO-SUBGROUP._")
            L.append("")
            L.append(f"**Disposition:** _[SET-ASIDE / ROUTE-TO-CLUSTER {{code}} / PROMOTE-TO-SUBGROUP {{code}}]_")
            L.append("**Rationale:** _[verse-specific evidence ground]_")
            L.append("")
            L.append("---")
            L.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"Input doc written: {OUT}")
    conn.close()


if __name__ == "__main__":
    main()
