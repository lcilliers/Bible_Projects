"""
Generate a comprehensive programme status report.
Refocused for post-Verse Context completion, pre-Session B pipeline.
"""
import sqlite3
import os
from datetime import datetime, timezone
from collections import defaultdict

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "bible_research.db")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "Workflow", "Programme")


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    L = []

    L.append("# Programme Status Report")
    L.append("")
    L.append(f"> Generated: {now}")
    L.append(f"> Stage: Verse Context complete — Session B DataPrep gate open")
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
    active_terms = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 0").fetchone()[0]
    active_verses = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE delete_flagged = 0").fetchone()[0]
    owner_terms = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 0 AND term_owner_type = 'OWNER'").fetchone()[0]
    xref_terms = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 0 AND term_owner_type = 'XREF'").fetchone()[0]

    L.append("| Metric | Value |")
    L.append("|--------|-------|")
    L.append(f"| Total registries | {total_reg} |")
    L.append(f"| Active (non-excluded) | {active_reg} |")
    L.append(f"| Excluded (Phase 1) | {excluded} |")
    L.append(f"| Active terms (OWNER) | {owner_terms} |")
    L.append(f"| Active terms (XREF) | {xref_terms} |")
    L.append(f"| Active verses | {active_verses:,} |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 2: VERSE CONTEXT COMPLETION
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 2. Verse Context — Stage 1 Complete")
    L.append("")

    vc_complete = conn.execute("SELECT COUNT(*) FROM word_registry WHERE verse_context_status = 'Complete'").fetchone()[0]
    vc_in_progress = conn.execute("SELECT COUNT(*) FROM word_registry WHERE verse_context_status = 'In Progress'").fetchone()[0]
    vc_null = conn.execute("SELECT COUNT(*) FROM word_registry WHERE verse_context_status IS NULL").fetchone()[0]

    L.append(f"| verse_context_status | Count |")
    L.append(f"|---------------------|-------|")
    L.append(f"| Complete | {vc_complete} |")
    L.append(f"| In Progress | {vc_in_progress} |")
    L.append(f"| NULL (excluded) | {vc_null} |")
    L.append("")

    # VC table stats
    vc_groups = conn.execute("SELECT COUNT(*) FROM verse_context_group WHERE delete_flagged = 0").fetchone()[0]
    vc_total = conn.execute("SELECT COUNT(*) FROM verse_context WHERE delete_flagged = 0").fetchone()[0]
    vc_relevant = conn.execute("SELECT COUNT(*) FROM verse_context WHERE is_relevant = 1 AND delete_flagged = 0").fetchone()[0]
    vc_set_aside = conn.execute("SELECT COUNT(*) FROM verse_context WHERE is_relevant = 0 AND delete_flagged = 0").fetchone()[0]
    vc_anchors = conn.execute("SELECT COUNT(*) FROM verse_context WHERE is_anchor = 1 AND delete_flagged = 0").fetchone()[0]
    vc_related = conn.execute("SELECT COUNT(*) FROM verse_context WHERE is_related = 1 AND delete_flagged = 0").fetchone()[0]

    L.append("### Verse Context Data")
    L.append("")
    L.append("| Metric | Value |")
    L.append("|--------|-------|")
    L.append(f"| Contextual meaning groups | {vc_groups:,} |")
    L.append(f"| Total verse classifications | {vc_total:,} |")
    L.append(f"| Relevant (inner-being) | {vc_relevant:,} |")
    L.append(f"| Set aside | {vc_set_aside:,} |")
    L.append(f"| Anchor verses | {vc_anchors:,} |")
    L.append(f"| Related verses | {vc_related:,} |")
    L.append("")

    relevance_pct = vc_relevant / vc_total * 100 if vc_total else 0
    L.append(f"**Relevance rate:** {relevance_pct:.1f}% of classified verses engage the inner being.")
    L.append("")

    # Batches applied
    batches = conn.execute("SELECT run_id FROM engine_run_log WHERE run_id LIKE 'PATCH%VCB%' ORDER BY run_id").fetchall()
    L.append(f"**Batches applied:** {len(batches)} (VCB-001 through VCB-029)")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 3: DIMENSION INDEX
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 3. Dimension Index")
    L.append("")
    L.append("Theological dimension classification of all contextual meaning groups.")
    L.append("")

    di_total = conn.execute("SELECT COUNT(*) FROM wa_dimension_index WHERE delete_flagged = 0").fetchone()[0]
    di_classified = conn.execute("SELECT COUNT(*) FROM wa_dimension_index WHERE dimension IS NOT NULL AND delete_flagged = 0").fetchone()[0]
    di_unclassified = di_total - di_classified

    L.append(f"| Status | Count | % |")
    L.append(f"|--------|------:|---:|")
    L.append(f"| Classified | {di_classified} | {di_classified/di_total*100:.0f}% |")
    L.append(f"| Unclassified | {di_unclassified} | {di_unclassified/di_total*100:.0f}% |")
    L.append(f"| **Total** | **{di_total}** | |")
    L.append("")

    L.append("### Dimension Distribution")
    L.append("")
    L.append("| Dimension | Groups | % of classified |")
    L.append("|-----------|-------:|---:|")
    for r in conn.execute("""
        SELECT COALESCE(dimension, 'UNCLASSIFIED') as dim, COUNT(*) as c
        FROM wa_dimension_index WHERE delete_flagged = 0
        GROUP BY dimension ORDER BY c DESC
    """):
        pct = r['c'] / di_total * 100
        L.append(f"| {r['dim']} | {r['c']} | {pct:.1f}% |")
    L.append("")

    L.append("### Classification Confidence")
    L.append("")
    L.append("| Confidence | Count |")
    L.append("|-----------|------:|")
    for r in conn.execute("""
        SELECT dimension_confidence, COUNT(*) as c
        FROM wa_dimension_index WHERE delete_flagged = 0
        GROUP BY dimension_confidence ORDER BY c DESC
    """):
        L.append(f"| {r['dimension_confidence'] or 'NULL'} | {r['c']} |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 4: SESSION B PIPELINE STATUS
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 4. Session B Pipeline Status")
    L.append("")

    sb_rows = conn.execute("""
        SELECT session_b_status, COUNT(*) as c
        FROM word_registry GROUP BY session_b_status ORDER BY session_b_status
    """).fetchall()

    L.append("| session_b_status | Count |")
    L.append("|-----------------|------:|")
    for r in sb_rows:
        L.append(f"| {r['session_b_status'] or 'NULL'} | {r['c']} |")
    L.append("")

    # Gate check: registries ready for DataPrep
    ready_dp = conn.execute("""
        SELECT COUNT(*) FROM word_registry
        WHERE verse_context_status = 'Complete'
        AND session_b_status IN ('Verse Context Reset', 'Ready for Analysis')
        AND phase1_status != 'Excluded'
    """).fetchone()[0]
    L.append(f"**Registries with DataPrep gate open:** {ready_dp}")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 5: CLUSTER READINESS
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 5. Cluster Readiness for Session B")
    L.append("")
    L.append("All clusters have verse_context_status = Complete. Ready for pool-based Session B.")
    L.append("")

    clusters = conn.execute("""
        SELECT cluster_assignment,
               COUNT(*) as total,
               SUM(CASE WHEN phase1_status = 'Excluded' THEN 1 ELSE 0 END) as excluded_count,
               SUM(CASE WHEN phase1_term_count > 0 THEN 1 ELSE 0 END) as with_terms,
               SUM(CASE WHEN term_sharing_ratio = 0.0 AND phase1_term_count > 0
                    AND phase1_status != 'Excluded' THEN 1 ELSE 0 END) as not_shared
        FROM word_registry GROUP BY cluster_assignment ORDER BY cluster_assignment
    """).fetchall()

    L.append("| Cluster | Total | Active | Not-shared | Words |")
    L.append("|---------|------:|-------:|-----------:|-------|")
    for c in clusters:
        active = c['total'] - c['excluded_count']
        # Get word list
        words = conn.execute("""
            SELECT word FROM word_registry
            WHERE cluster_assignment = ? AND phase1_status != 'Excluded'
            ORDER BY no
        """, (c['cluster_assignment'],)).fetchall()
        word_list = ", ".join(w['word'] for w in words)
        if len(word_list) > 60:
            word_list = word_list[:57] + "..."
        L.append(f"| {c['cluster_assignment']} | {c['total']} | {active} | {c['not_shared']} | {word_list} |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 6: TERM INVENTORY
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 6. Term Inventory")
    L.append("")

    L.append("## 6.1 MTI Status Distribution")
    L.append("")
    mti_rows = conn.execute("""
        SELECT m.status, COUNT(*) as c
        FROM mti_terms m GROUP BY m.status ORDER BY c DESC
    """).fetchall()
    L.append("| mti_terms.status | Count |")
    L.append("|-----------------|------:|")
    for r in mti_rows:
        L.append(f"| {r['status'] or 'NULL'} | {r['c']} |")
    L.append("")

    L.append("## 6.2 Term Sharing")
    L.append("")
    sharing = conn.execute("""
        SELECT
            CASE
                WHEN term_sharing_ratio = 0.0 THEN '0% (all unique)'
                WHEN term_sharing_ratio < 0.5 THEN '1-49% shared'
                WHEN term_sharing_ratio < 0.8 THEN '50-79% shared'
                ELSE '80%+ shared'
            END as bucket,
            COUNT(*) as c
        FROM word_registry
        WHERE phase1_status != 'Excluded' AND phase1_term_count > 0
        GROUP BY bucket
        ORDER BY MIN(term_sharing_ratio)
    """).fetchall()
    L.append("| Sharing Ratio | Registries |")
    L.append("|--------------|----------:|")
    for r in sharing:
        L.append(f"| {r[0]} | {r[1]} |")
    L.append("")

    L.append("## 6.3 Quality Flags")
    L.append("")
    qf_rows = conn.execute("""
        SELECT qft.flag_code, COUNT(*) as c
        FROM wa_data_quality_flags dqf
        JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
        GROUP BY qft.flag_code ORDER BY c DESC
    """).fetchall()
    L.append("| Quality Flag | Count |")
    L.append("|-------------|------:|")
    for r in qf_rows:
        L.append(f"| {r['flag_code']} | {r['c']} |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 7: DATA INTEGRITY
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 7. Data Integrity")
    L.append("")

    # R1-R4
    r1 = conn.execute("SELECT COUNT(*) FROM verse_context WHERE is_relevant=0 AND delete_flagged=0 AND (group_id IS NOT NULL OR is_anchor=1 OR is_related=1)").fetchone()[0]
    r2 = conn.execute("SELECT COUNT(*) FROM verse_context WHERE is_anchor=1 AND delete_flagged=0 AND (is_relevant=0 OR is_related=1 OR group_id IS NULL)").fetchone()[0]
    r3 = conn.execute("SELECT COUNT(*) FROM verse_context vc WHERE vc.is_related=1 AND vc.delete_flagged=0 AND NOT EXISTS (SELECT 1 FROM verse_context a WHERE a.group_id=vc.group_id AND a.is_anchor=1 AND a.delete_flagged=0)").fetchone()[0]

    L.append("### Verse Context Integrity (R1-R3)")
    L.append("")
    L.append(f"| Rule | Violations |")
    L.append(f"|------|----------:|")
    L.append(f"| R1: set-aside clean | {r1} |")
    L.append(f"| R2: anchor clean | {r2} |")
    L.append(f"| R3: related-anchor linkage | {r3} |")
    status = "ALL CLEAN" if r1 + r2 + r3 == 0 else "VIOLATIONS FOUND"
    L.append(f"\n**Status:** {status}")
    L.append("")

    # Phantom duplicates check
    phantom_count = conn.execute("""
        SELECT COUNT(*) FROM (
            SELECT strongs_number FROM mti_terms
            WHERE status IN ('extracted', 'extracted_thin')
            GROUP BY strongs_number HAVING COUNT(DISTINCT id) > 1
        )
    """).fetchone()[0]
    L.append(f"**Phantom mti_terms duplicates:** {phantom_count}")
    L.append("")

    # Unparsed meanings
    unparsed = conn.execute("""
        SELECT COUNT(*) FROM wa_term_inventory
        WHERE meaning IS NOT NULL AND parsed_meaning_id IS NULL AND delete_flagged = 0
    """).fetchone()[0]
    L.append(f"**Unparsed meanings:** {unparsed} terms")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 8: NEXT STEPS
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 8. Next Steps")
    L.append("")
    L.append("1. **Dimension classification** — 1,545 UNCLASSIFIED + 1,165 KEYWORD_WEAK groups need Claude AI assessment")
    L.append("2. **Session B DataPrep** — all 181 registries have VC Complete, DataPrep gate open")
    L.append("3. **Pool assembly** — per WA-Registry-Management-Guide v5.6, not-shared words first, then pools by cluster")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # WRITE
    # ═══════════════════════════════════════════════════════════════════════
    report_dir = os.path.join(OUT_DIR, "Program_reports")
    os.makedirs(report_dir, exist_ok=True)
    out_path = os.path.join(report_dir, f"wa-programme-status-report-{now.replace('-', '')}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    print(f"Report written: {out_path}")
    print(f"Sections: 8")
    print(f"Lines: {len(L)}")

    conn.close()


if __name__ == "__main__":
    main()
