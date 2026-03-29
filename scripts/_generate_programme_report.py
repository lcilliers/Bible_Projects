"""
Generate a comprehensive programme status report for Claude AI handoff.
Includes database status, distribution analysis, and next-step priorities.
"""
import sqlite3
import json
import os
from datetime import datetime, timezone
from collections import Counter, defaultdict

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
IMG_DIR = OUT_DIR


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    L = []

    L.append("# Programme Status Report — Handoff to Claude AI")
    L.append("")
    L.append(f"> Generated: {now}")
    L.append(f"> Schema version: 3.7.0")
    L.append(f"> Purpose: Comprehensive database status for Session B analysis planning")
    L.append("")
    L.append("---")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 1: PROGRAMME OVERVIEW
    # ═══════════════════════════════════════════════════════════════════════
    L.append("# 1. Programme Overview")
    L.append("")

    total_reg = conn.execute("SELECT COUNT(*) FROM word_registry").fetchone()[0]
    excluded = conn.execute("SELECT COUNT(*) FROM word_registry WHERE phase1_status = 'Excluded'").fetchone()[0]
    active_reg = total_reg - excluded

    L.append(f"| Metric | Value |")
    L.append(f"|--------|-------|")
    L.append(f"| Total registries | {total_reg} |")
    L.append(f"| Active (non-excluded) | {active_reg} |")
    L.append(f"| Excluded (Phase 1) | {excluded} |")

    # Active data
    active_terms = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 0").fetchone()[0]
    active_verses = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE delete_flagged = 0").fetchone()[0]
    owner_terms = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 0 AND term_owner_type = 'OWNER'").fetchone()[0]
    xref_terms = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 0 AND term_owner_type = 'XREF'").fetchone()[0]
    del_terms = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 1").fetchone()[0]
    del_verses = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE delete_flagged = 1").fetchone()[0]

    L.append(f"| Active terms (OWNER) | {owner_terms} |")
    L.append(f"| Active terms (XREF) | {xref_terms} |")
    L.append(f"| Active verses | {active_verses} |")
    L.append(f"| delete_flagged terms | {del_terms} |")
    L.append(f"| delete_flagged verses | {del_verses} |")
    L.append("")

    L.append("**Note on delete_flagged records:** These remain in the database but are excluded from all standard queries and exports. They include: confirmed-delete terms (particles, function words), XREF verse duplicates, and terms flagged by the engine during audit. No physical deletion has occurred.")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 2: SESSION B STATUS
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 2. Session B Status")
    L.append("")

    sb_rows = conn.execute("""
        SELECT session_b_status, COUNT(*) as c
        FROM word_registry GROUP BY session_b_status ORDER BY session_b_status
    """).fetchall()

    L.append("| Session B Status | Count |")
    L.append("|-----------------|-------|")
    for r in sb_rows:
        L.append(f"| {r['session_b_status'] or 'NULL (not started)'} | {r['c']} |")
    L.append("")

    # v5.2 completion
    v52 = conn.execute("SELECT COUNT(*) FROM wa_session_b_dimensions").fetchone()[0]
    findings = conn.execute("SELECT COUNT(*) FROM wa_session_b_findings").fetchone()[0]
    sd_pointers = conn.execute("SELECT COUNT(*) FROM wa_session_research_flags WHERE flag_code = 'SD_POINTER'").fetchone()[0]
    ev_count = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE evidential_status IS NOT NULL AND delete_flagged = 0").fetchone()[0]

    L.append("### v5.2 Extraction Cycle Completion")
    L.append("")
    L.append(f"| Metric | Value |")
    L.append(f"|--------|-------|")
    L.append(f"| Registries with dimensional profile | {v52} |")
    L.append(f"| Key findings recorded | {findings} |")
    L.append(f"| Session D pointers | {sd_pointers} |")
    L.append(f"| Terms with evidential_status | {ev_count} |")
    L.append("")
    L.append("Only registries with a dimensional profile in `wa_session_b_dimensions` have completed the v5.2 extraction cycle. All others at 'Analysis Complete' were completed under the old workflow and need v5.2 extraction.")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 3: TERM INVENTORY STATUS
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 3. Term Inventory Status")
    L.append("")

    L.append("## 3.1 Term Ownership")
    L.append("")
    L.append("Each term in `wa_term_inventory` is marked as OWNER (primary location for this Strong's number) or XREF (cross-reference copy belonging to another registry).")
    L.append("")
    L.append("| term_owner_type | Active Terms | delete_flagged Terms |")
    L.append("|----------------|-------------|---------------------|")
    for tot in conn.execute("""
        SELECT term_owner_type,
               SUM(CASE WHEN delete_flagged = 0 THEN 1 ELSE 0 END) as active,
               SUM(CASE WHEN delete_flagged = 1 THEN 1 ELSE 0 END) as deleted
        FROM wa_term_inventory GROUP BY term_owner_type ORDER BY term_owner_type
    """).fetchall():
        L.append(f"| {tot[0] or 'NULL'} | {tot[1]} | {tot[2]} |")
    L.append("")
    L.append("**XREF verses are delete_flagged.** The active verse set contains only OWNER verses. XREF term records remain active for cross-registry linkage queries but their verses are excluded from exports.")
    L.append("")

    L.append("## 3.2 MTI Status Distribution")
    L.append("")
    L.append("The `mti_terms.status` field classifies each term's relevance to its owning registry.")
    L.append("")
    mti_rows = conn.execute("""
        SELECT m.status, COUNT(*) as c
        FROM mti_terms m GROUP BY m.status ORDER BY c DESC
    """).fetchall()
    L.append("| mti_terms.status | Count |")
    L.append("|-----------------|-------|")
    for r in mti_rows:
        L.append(f"| {r['status'] or 'NULL'} | {r['c']} |")
    L.append("")

    L.append("## 3.3 Evidential Status (where assigned)")
    L.append("")
    L.append("Assigned during v5.2 Session B extraction. Only populated for registries that have completed the v5.2 cycle.")
    L.append("")
    ev_rows = conn.execute("""
        SELECT evidential_status, COUNT(*) as c
        FROM wa_term_inventory WHERE evidential_status IS NOT NULL AND delete_flagged = 0
        GROUP BY evidential_status ORDER BY c DESC
    """).fetchall()
    L.append("| evidential_status | Count |")
    L.append("|------------------|-------|")
    for r in ev_rows:
        L.append(f"| {r['evidential_status']} | {r['c']} |")
    L.append("")

    L.append("## 3.4 Quality Flags")
    L.append("")
    qf_rows = conn.execute("""
        SELECT qft.flag_code, COUNT(*) as c
        FROM wa_data_quality_flags dqf
        JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
        GROUP BY qft.flag_code ORDER BY c DESC
    """).fetchall()
    L.append("| Quality Flag | Count | Notes |")
    L.append("|-------------|-------|-------|")
    for r in qf_rows:
        note = ""
        if r['flag_code'] == 'CONCRETE_PHYSICAL':
            note = "Concrete nouns — flagged, not excluded. Verse analysis may reveal inner-being usage."
        L.append(f"| {r['flag_code']} | {r['c']} | {note} |")
    L.append("")

    L.append("## 3.5 Phase 2 Flags")
    L.append("")
    L.append("Researcher-owned analytical flags on terms. These are **Claude AI's responsibility** — set during Session B analysis.")
    L.append("")
    ph2_rows = conn.execute("""
        SELECT ft.flag_code, COUNT(*) as c
        FROM wa_term_phase2_flags pf
        JOIN phase2_flag_types ft ON ft.id = pf.flag_id
        GROUP BY ft.flag_code ORDER BY c DESC
    """).fetchall()
    L.append("| PH2 Flag | Count |")
    L.append("|----------|-------|")
    for r in ph2_rows:
        L.append(f"| {r['flag_code']} | {r['c']} |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 4: COLUMNS REQUIRING CLAUDE AI ACTION
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 4. Columns Requiring Claude AI Action")
    L.append("")
    L.append("These fields are either NULL or incomplete and require Claude AI analytical judgement to populate. Claude Code cannot derive these from data alone.")
    L.append("")

    L.append("## 4.1 word_registry")
    L.append("")
    L.append("| Column | Populated | NULL | Claude AI Action |")
    L.append("|--------|-----------|------|-----------------|")

    for col, action in [
        ("sb_classification", "Assign inner being standing classification during Session B extraction"),
        ("sb_classification_reasoning", "Provide reasoning for non-confirmed classifications"),
        ("session_b_status", "Updated via patch after analysis completion"),
        ("source_category", "Repurpose as multi-value dimensions field (v5.1 Section 4.3). Currently single-value."),
    ]:
        pop = conn.execute(f"SELECT COUNT(*) FROM word_registry WHERE {col} IS NOT NULL AND phase1_status != 'Excluded'").fetchone()[0]
        null = active_reg - pop
        L.append(f"| {col} | {pop} | {null} | {action} |")
    L.append("")

    L.append("## 4.2 wa_term_inventory")
    L.append("")
    L.append("| Column | Populated | NULL (active) | Claude AI Action |")
    L.append("|--------|-----------|---------------|-----------------|")

    for col, action in [
        ("evidential_status", "Assign confirmed/plausible/uncertain/instrumental/relational_only during v5.2 extraction"),
        ("retention_note", "Provide note for non-confirmed terms explaining retention reasoning"),
    ]:
        pop = conn.execute(f"SELECT COUNT(*) FROM wa_term_inventory WHERE {col} IS NOT NULL AND delete_flagged = 0").fetchone()[0]
        null = active_terms - pop
        L.append(f"| {col} | {pop} | {null} | {action} |")
    L.append("")

    L.append("## 4.3 wa_term_phase2_flags (Claude AI owned)")
    L.append("")
    terms_with_ph2 = conn.execute("SELECT COUNT(DISTINCT term_inv_id) FROM wa_term_phase2_flags").fetchone()[0]
    terms_without = owner_terms - terms_with_ph2
    L.append(f"- {terms_with_ph2} OWNER terms have at least one PH2 flag")
    L.append(f"- {terms_without} OWNER terms have no PH2 flags")
    L.append(f"- PH2 flags are set during Session B DataPrep and Analysis — not by Claude Code")
    L.append("")

    L.append("## 4.4 wa_session_b_dimensions / wa_session_b_findings")
    L.append("")
    L.append(f"- {v52} registries have dimensional profiles (only mind and Soul completed v5.2)")
    L.append(f"- {findings} key findings recorded across those registries")
    L.append(f"- All other registries at Analysis Complete need v5.2 extraction to populate these tables")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 5: TERM SHARING ANALYSIS
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 5. Term Sharing Analysis")
    L.append("")
    L.append("## 5.1 Distribution")
    L.append("")
    L.append("![Cross-Registry Term Analysis](cross_registry_term_analysis_20260328.png)")
    L.append("")
    L.append("**Key findings:**")
    L.append("- 2,045 terms are unique to one registry; 1,740 are shared across 2+ registries")
    L.append("- High-bleed particles (ki, asher, al, im) have been delete_flagged — they appeared in 10-18 registries")
    L.append("- Genuine shared terms (chesed, nephesh, kardia) remain active as they carry analytical value across registries")
    L.append("")

    L.append("## 5.2 Root Family Analysis")
    L.append("")
    L.append("![Cross-Registry Root Analysis](cross_registry_root_analysis_20260328.png)")
    L.append("")
    L.append("**Key findings:**")
    L.append("- Root families are much more discriminating than individual terms — 296 of 305 roots are unique to one registry")
    L.append("- Only 19 roots are shared across registries")
    L.append("- Root family data is sparse — only 31 of 181 registries have root records. This is a known gap.")
    L.append("")

    L.append("## 5.3 Sharing Ratio Distribution")
    L.append("")
    sharing = conn.execute("""
        SELECT
            CASE
                WHEN term_sharing_ratio = 0.0 THEN '0% (all unique)'
                WHEN term_sharing_ratio < 0.5 THEN '1-49% shared'
                WHEN term_sharing_ratio < 0.8 THEN '50-79% shared'
                WHEN term_sharing_ratio < 1.0 THEN '80-99% shared'
                ELSE '100% shared'
            END as bucket,
            COUNT(*) as c
        FROM word_registry
        WHERE phase1_status != 'Excluded' AND phase1_term_count > 0
        GROUP BY bucket
        ORDER BY MIN(term_sharing_ratio)
    """).fetchall()
    L.append("| Sharing Ratio | Registries |")
    L.append("|--------------|-----------|")
    for r in sharing:
        L.append(f"| {r[0]} | {r[1]} |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 6: CLUSTER STATUS
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 6. Cluster Status")
    L.append("")

    clusters = conn.execute("""
        SELECT cluster_assignment, COUNT(*) as total,
               SUM(CASE WHEN session_b_status IN ('Analysis Complete', 'Session B Complete') THEN 1 ELSE 0 END) as complete,
               SUM(CASE WHEN session_b_status IS NULL THEN 1 ELSE 0 END) as not_started,
               SUM(CASE WHEN phase1_status = 'Excluded' THEN 1 ELSE 0 END) as excluded_count
        FROM word_registry GROUP BY cluster_assignment ORDER BY cluster_assignment
    """).fetchall()

    L.append("| Cluster | Total | Complete | Not Started | Excluded | Maturity |")
    L.append("|---------|-------|----------|-------------|----------|----------|")
    for c in clusters:
        active_in_cluster = c['total'] - c['excluded_count']
        pct = int(c['complete'] / active_in_cluster * 100) if active_in_cluster > 0 else 0
        L.append(f"| {c['cluster_assignment']} | {c['total']} | {c['complete']} | {c['not_started']} | {c['excluded_count']} | {pct}% |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 7: NOT-SHARED WORDS — PRIORITY FOR ANALYSIS
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 7. Not-Shared Words — Priority for Independent Analysis")
    L.append("")
    L.append("These 17 registries have `term_sharing_ratio = 0.0` — every term is unique to this word. They can be analysed completely independently with no cross-registry verse overlap. These are the recommended starting point for the next batch of Session B analyses.")
    L.append("")

    not_shared = conn.execute("""
        SELECT wr.no, wr.word, wr.cluster_assignment, wr.session_b_status,
               wr.unique_term_count, wr.phase1_verse_count
        FROM word_registry wr
        WHERE wr.phase1_status != 'Excluded'
        AND wr.term_sharing_ratio = 0.0
        AND wr.phase1_term_count > 0
        ORDER BY wr.cluster_assignment, wr.no
    """).fetchall()

    L.append("| No | Word | Cluster | Terms | Verses | Session B Status |")
    L.append("|----|------|---------|-------|--------|-----------------|")
    total_terms_ns = 0
    total_verses_ns = 0
    for r in not_shared:
        L.append(f"| {r['no']} | {r['word']} | {r['cluster_assignment']} | {r['unique_term_count']} | {r['phase1_verse_count']} | {r['session_b_status'] or 'NULL'} |")
        total_terms_ns += r['unique_term_count']
        total_verses_ns += r['phase1_verse_count']
    L.append(f"| **Total** | **17 words** | | **{total_terms_ns}** | **{total_verses_ns}** | |")
    L.append("")

    L.append("### Recommended batching for analysis:")
    L.append("")
    L.append("These 17 words span 12 different clusters. For Session B analysis, they can be batched by cluster proximity:")
    L.append("")

    # Group by cluster
    by_cluster = defaultdict(list)
    for r in not_shared:
        by_cluster[r['cluster_assignment']].append(r)

    batch_num = 1
    current_batch = []
    for cl in sorted(by_cluster.keys()):
        words = by_cluster[cl]
        if len(current_batch) + len(words) > 5 and current_batch:
            word_list = ", ".join(f"{w['word']} ({w['no']})" for w in current_batch)
            L.append(f"- **Batch {batch_num}**: {word_list}")
            batch_num += 1
            current_batch = []
        current_batch.extend(words)
    if current_batch:
        word_list = ", ".join(f"{w['word']} ({w['no']})" for w in current_batch)
        L.append(f"- **Batch {batch_num}**: {word_list}")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 8: TWO-WORD CLUSTERS — NEXT PRIORITY
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 8. Small Clusters — Next Priority After Not-Shared Words")
    L.append("")
    L.append("After the not-shared words, the next simplest registries are those in clusters with only 2 active (non-excluded) words. These have limited cross-registry complexity.")
    L.append("")

    small_clusters = conn.execute("""
        SELECT cluster_assignment,
               COUNT(*) as total,
               SUM(CASE WHEN phase1_status != 'Excluded' THEN 1 ELSE 0 END) as active
        FROM word_registry
        GROUP BY cluster_assignment
        HAVING active <= 3
        ORDER BY active, cluster_assignment
    """).fetchall()

    if small_clusters:
        for sc in small_clusters:
            words = conn.execute("""
                SELECT no, word, phase1_status, session_b_status, phase1_term_count, phase1_verse_count, term_sharing_ratio
                FROM word_registry WHERE cluster_assignment = ? ORDER BY no
            """, (sc['cluster_assignment'],)).fetchall()
            L.append(f"### {sc['cluster_assignment']} ({sc['active']} active words)")
            L.append("")
            L.append("| No | Word | Status | Terms | Verses | Sharing |")
            L.append("|----|------|--------|-------|--------|---------|")
            for w in words:
                status = w['phase1_status']
                if status == 'Excluded':
                    status = 'Excluded'
                else:
                    status = w['session_b_status'] or 'Ready'
                L.append(f"| {w['no']} | {w['word']} | {status} | {w['phase1_term_count']} | {w['phase1_verse_count']} | {w['term_sharing_ratio']:.0%} |")
            L.append("")
    else:
        L.append("No clusters with 3 or fewer active words.")
        L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 9: DATA INTEGRITY NOTES
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 9. Data Integrity Notes")
    L.append("")

    # Unparsed meanings
    unparsed = conn.execute("""
        SELECT COUNT(*) FROM wa_term_inventory
        WHERE meaning IS NOT NULL AND parsed_meaning_id IS NULL AND delete_flagged = 0
    """).fetchone()[0]
    L.append(f"- **{unparsed} terms** have raw `meaning` text but no `parsed_meaning_id` — meaning parser migration incomplete")

    # CONCRETE_PHYSICAL flagged
    concrete = conn.execute("""
        SELECT COUNT(DISTINCT dqf.term_id)
        FROM wa_data_quality_flags dqf
        JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
        WHERE qft.flag_code = 'CONCRETE_PHYSICAL'
    """).fetchone()[0]
    L.append(f"- **{concrete} terms** flagged as CONCRETE_PHYSICAL — retained for verse analysis, flagged as unlikely inner-being vocabulary")

    # Null span
    null_span = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE delete_flagged = 0 AND span_strong_match IS NULL").fetchone()[0]
    L.append(f"- **{null_span} verses** have NULL span_strong_match — pre-v9 records, could be backfilled with STEP re-query")

    # Root family coverage
    with_roots = conn.execute("""
        SELECT COUNT(DISTINCT fi.registry_id)
        FROM wa_term_root_family rf
        JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE rf.delete_flagged = 0
    """).fetchone()[0]
    L.append(f"- **Root family data** populated for {with_roots} of {active_reg} registries — sparse coverage, planned for future backfill")

    # source_category rename pending
    L.append(f"- **source_category -> dimensions rename** pending (schema migration M17). Currently writing multi-value dimensions to source_category field.")

    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 10: HOUSEKEEPING SUMMARY
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 10. Housekeeping Completed This Session")
    L.append("")
    L.append("| Action | Impact |")
    L.append("|--------|--------|")
    L.append("| Particle terms delete_flagged (ki, asher, al, im + 5 more) | 113 terms, 20,665 verses removed from active set |")
    L.append("| mti_status=delete synced to term_inventory | 130 terms, 7,100 verses flagged |")
    L.append("| Orphan verse cleanup (under delete_flagged terms) | 1,288 verses flagged |")
    L.append("| XREF verses delete_flagged | 59,120 verses removed from active set |")
    L.append("| CONCRETE_PHYSICAL quality flag created | 315 terms flagged (not excluded, queryable filter) |")
    L.append("| term_owner_type added to wa_term_inventory | 5,518 OWNER + 1,470 XREF populated |")
    L.append("| testament NULLs fixed | 495 records corrected |")
    L.append("| VTL backfill | 33,335 wa_verse_term_links records created — 100% coverage |")
    L.append("| Sharing ratio added to word_registry | unique_term_count, shared_term_count, term_sharing_ratio populated |")
    L.append("| 140 registries extracted + audited | STEP data pulled, audit_word run, JSON exports produced |")
    L.append("")
    L.append("### Net effect on active dataset:")
    L.append("")
    L.append("| Metric | Before | After | Reduction |")
    L.append("|--------|--------|-------|-----------|")
    L.append(f"| Active terms | 7,233 | {active_terms} | {7233 - active_terms} |")
    L.append(f"| Active verses | 221,357 | {active_verses} | {221357 - active_verses} ({(221357 - active_verses)/221357*100:.0f}%) |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # WRITE
    # ═══════════════════════════════════════════════════════════════════════
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, f"wa-programme-status-report-{now.replace('-', '')}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    print(f"Report written: {out_path}")
    print(f"Sections: 10")
    print(f"Lines: {len(L)}")

    conn.close()


if __name__ == "__main__":
    main()
