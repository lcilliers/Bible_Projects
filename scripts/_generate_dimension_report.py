"""
Generate a dimension index summary report.
Covers: dimension distribution, registry mapping, cluster analysis,
classification status, and refinement priorities.

Output: outputs/reports/programme/wa-dimension-report-{date}.md
"""
import sqlite3
import os
from datetime import datetime, timezone
from collections import defaultdict

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs", "reports", "programme")


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    L = []

    L.append("# Dimension Index Report")
    L.append("")
    L.append(f"> Generated: {now}")
    L.append(f"> Source: wa_dimension_index (populated from verse_context_group)")
    L.append(f"> Purpose: Map contextual meaning groups to theological dimensions for Session B analysis")
    L.append("")
    L.append("---")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 1: OVERVIEW
    # ═══════════════════════════════════════════════════════════════════════
    L.append("# 1. Overview")
    L.append("")

    total = conn.execute("SELECT COUNT(*) FROM wa_dimension_index WHERE delete_flagged=0").fetchone()[0]
    classified = conn.execute("SELECT COUNT(*) FROM wa_dimension_index WHERE dimension IS NOT NULL AND delete_flagged=0").fetchone()[0]
    unclassified = total - classified
    strong = conn.execute("SELECT COUNT(*) FROM wa_dimension_index WHERE dimension_confidence='KEYWORD_STRONG' AND delete_flagged=0").fetchone()[0]
    weak = conn.execute("SELECT COUNT(*) FROM wa_dimension_index WHERE dimension_confidence='KEYWORD_WEAK' AND delete_flagged=0").fetchone()[0]
    claude = conn.execute("SELECT COUNT(*) FROM wa_dimension_index WHERE dimension_confidence='CLAUDE_AI' AND delete_flagged=0").fetchone()[0]
    manual = conn.execute("SELECT COUNT(*) FROM wa_dimension_index WHERE manual_override=1 AND delete_flagged=0").fetchone()[0]
    distinct_terms = conn.execute("SELECT COUNT(DISTINCT mti_term_id) FROM wa_dimension_index WHERE delete_flagged=0").fetchone()[0]
    distinct_regs = conn.execute("SELECT COUNT(DISTINCT owning_registry_no) FROM wa_dimension_index WHERE delete_flagged=0").fetchone()[0]

    L.append("| Metric | Value |")
    L.append("|--------|------:|")
    L.append(f"| Total contextual groups | {total:,} |")
    L.append(f"| Classified | {classified:,} ({classified*100//total}%) |")
    L.append(f"| Unclassified | {unclassified:,} ({unclassified*100//total}%) |")
    L.append(f"| Distinct terms | {distinct_terms:,} |")
    L.append(f"| Distinct registries | {distinct_regs} |")
    L.append("")

    L.append("### Classification Confidence Breakdown")
    L.append("")
    L.append("| Confidence | Count | % | Notes |")
    L.append("|-----------|------:|---:|-------|")
    L.append(f"| KEYWORD_STRONG | {strong} | {strong*100//total}% | High-specificity phrase match — reliable |")
    L.append(f"| KEYWORD_WEAK | {weak} | {weak*100//total}% | Broad keyword match — needs review |")
    L.append(f"| CLAUDE_AI | {claude} | {claude*100//total}% | Claude AI assessed |")
    L.append(f"| Manual override | {manual} | {manual*100//total}% | Researcher corrected |")
    L.append(f"| UNCLASSIFIED | {unclassified} | {unclassified*100//total}% | No match — requires Claude AI |")
    L.append("")

    # Dominant subject distribution
    L.append("### Dominant Subject Distribution")
    L.append("")
    L.append("| Dominant Subject | Count | % |")
    L.append("|-----------------|------:|---:|")
    for r in conn.execute("""
        SELECT COALESCE(dominant_subject, 'NULL (unassigned)') as ds, COUNT(*) as c
        FROM wa_dimension_index WHERE delete_flagged = 0
        GROUP BY dominant_subject ORDER BY c DESC
    """):
        pct = r['c'] * 100 // total
        L.append(f"| {r['ds']} | {r['c']} | {pct}% |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 2: DIMENSION DISTRIBUTION
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 2. Dimension Distribution")
    L.append("")

    dims = conn.execute("""
        SELECT COALESCE(dimension, 'UNCLASSIFIED') as dim, COUNT(*) as groups,
            COUNT(DISTINCT owning_registry_no) as registries,
            COUNT(DISTINCT mti_term_id) as terms,
            SUM(anchor_count) as anchors,
            SUM(related_count) as related,
            SUM(total_verse_count) as verses
        FROM wa_dimension_index WHERE delete_flagged=0
        GROUP BY dimension ORDER BY groups DESC
    """).fetchall()

    L.append("| Dimension | Groups | Terms | Registries | Anchors | Related | Total Verses |")
    L.append("|-----------|-------:|------:|-----------:|--------:|--------:|-------------:|")
    for d in dims:
        L.append(f"| {d['dim']} | {d['groups']} | {d['terms']} | {d['registries']} | {d['anchors']} | {d['related']} | {d['verses']} |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 3: DIMENSION × CLUSTER CROSS-TAB
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 3. Dimension × Cluster Matrix")
    L.append("")
    L.append("Shows how dimensions distribute across clusters. Each cell = group count.")
    L.append("")

    # Get all clusters and dimensions
    clusters = sorted(set(r['cluster_assignment'] for r in conn.execute(
        "SELECT DISTINCT cluster_assignment FROM wa_dimension_index WHERE delete_flagged=0 AND cluster_assignment IS NOT NULL"
    )))
    dim_names = [d['dim'] for d in dims if d['dim'] != 'UNCLASSIFIED']

    cross = conn.execute("""
        SELECT dimension, cluster_assignment, COUNT(*) as c
        FROM wa_dimension_index
        WHERE delete_flagged=0 AND dimension IS NOT NULL
        GROUP BY dimension, cluster_assignment
    """).fetchall()

    matrix = defaultdict(lambda: defaultdict(int))
    for r in cross:
        matrix[r['dimension']][r['cluster_assignment']] = r['c']

    # Header
    header = "| Dimension |" + "|".join(f" {c} " for c in clusters) + "| Total |"
    sep = "|-----------|" + "|".join("---:" for _ in clusters) + "|------:|"
    L.append(header)
    L.append(sep)
    for dim in dim_names:
        cells = [str(matrix[dim].get(c, '')) for c in clusters]
        row_total = sum(matrix[dim].values())
        L.append(f"| {dim} |" + "|".join(f" {v} " for v in cells) + f"| {row_total} |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 4: DIMENSION × REGISTRY MAPPING
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 4. Registry Dimension Profiles")
    L.append("")
    L.append("For each registry: total groups, classified groups, primary dimension, and dimension spread.")
    L.append("")

    reg_profiles = conn.execute("""
        SELECT owning_registry_no as reg, owning_registry_word as word, cluster_assignment as cluster,
            COUNT(*) as total,
            SUM(CASE WHEN dimension IS NOT NULL THEN 1 ELSE 0 END) as classified,
            SUM(CASE WHEN dimension IS NULL THEN 1 ELSE 0 END) as unclassified,
            COUNT(DISTINCT dimension) as dim_count
        FROM wa_dimension_index WHERE delete_flagged=0
        GROUP BY owning_registry_no
        ORDER BY owning_registry_no
    """).fetchall()

    L.append("| Reg | Word | Cluster | Groups | Classified | Unclassified | Primary Dimension | Dim. Spread |")
    L.append("|----:|------|---------|-------:|-----------:|-------------:|-------------------|------------:|")

    for rp in reg_profiles:
        # Find primary dimension
        primary = conn.execute("""
            SELECT dimension, COUNT(*) as c FROM wa_dimension_index
            WHERE owning_registry_no=? AND dimension IS NOT NULL AND delete_flagged=0
            GROUP BY dimension ORDER BY c DESC LIMIT 1
        """, (rp['reg'],)).fetchone()
        prim_dim = primary['dimension'] if primary else "-"
        prim_count = f" ({primary['c']})" if primary else ""

        L.append(f"| {rp['reg']} | {rp['word']} | {rp['cluster']} | {rp['total']} | "
                 f"{rp['classified']} | {rp['unclassified']} | "
                 f"{prim_dim}{prim_count} | {rp['dim_count']} |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 5: CLASSIFICATION PRIORITIES
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 5. Classification Priorities")
    L.append("")
    L.append("Registries ranked by unclassified group count — where Claude AI effort is most needed.")
    L.append("")

    priorities = conn.execute("""
        SELECT owning_registry_no as reg, owning_registry_word as word,
            cluster_assignment as cluster,
            SUM(CASE WHEN dimension IS NULL THEN 1 ELSE 0 END) as unclassified,
            COUNT(*) as total,
            SUM(total_verse_count) as verse_impact
        FROM wa_dimension_index WHERE delete_flagged=0
        GROUP BY owning_registry_no
        HAVING unclassified > 0
        ORDER BY unclassified DESC
    """).fetchall()

    L.append("| Reg | Word | Cluster | Unclassified | Total Groups | Verse Impact | % Unclassified |")
    L.append("|----:|------|---------|-------------:|-------------:|-------------:|---------------:|")
    total_uncl = 0
    for p in priorities:
        pct = p['unclassified'] * 100 // p['total'] if p['total'] else 0
        L.append(f"| {p['reg']} | {p['word']} | {p['cluster']} | {p['unclassified']} | {p['total']} | {p['verse_impact']} | {pct}% |")
        total_uncl += p['unclassified']
    L.append(f"| | **Total** | | **{total_uncl}** | | | |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 6: KEYWORD_WEAK REVIEW CANDIDATES
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 6. KEYWORD_WEAK Review Summary")
    L.append("")
    L.append("These groups were classified by broad keyword matching. The dimension assignment may be correct but should be reviewed by Claude AI.")
    L.append("")

    weak_by_dim = conn.execute("""
        SELECT dimension, COUNT(*) as c, COUNT(DISTINCT owning_registry_no) as regs
        FROM wa_dimension_index
        WHERE dimension_confidence='KEYWORD_WEAK' AND delete_flagged=0
        GROUP BY dimension ORDER BY c DESC
    """).fetchall()

    L.append("| Dimension | KEYWORD_WEAK Groups | Across Registries |")
    L.append("|-----------|--------------------:|------------------:|")
    for w in weak_by_dim:
        L.append(f"| {w['dimension']} | {w['c']} | {w['regs']} |")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 7: LANGUAGE DISTRIBUTION
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 7. Language × Dimension")
    L.append("")

    lang_dims = conn.execute("""
        SELECT language, COALESCE(dimension, 'UNCLASSIFIED') as dim, COUNT(*) as c
        FROM wa_dimension_index WHERE delete_flagged=0
        GROUP BY language, dimension ORDER BY language, c DESC
    """).fetchall()

    lang_totals = defaultdict(lambda: defaultdict(int))
    for r in lang_dims:
        lang_totals[r['language']][r['dim']] = r['c']

    for lang in sorted(lang_totals.keys()):
        L.append(f"### {lang}")
        L.append("")
        L.append("| Dimension | Groups |")
        L.append("|-----------|-------:|")
        for dim, c in sorted(lang_totals[lang].items(), key=lambda x: -x[1]):
            L.append(f"| {dim} | {c} |")
        L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 8: NEXT STEPS
    # ═══════════════════════════════════════════════════════════════════════
    L.append("---")
    L.append("")
    L.append("# 8. Refinement Path")
    L.append("")
    L.append(f"1. **UNCLASSIFIED** ({unclassified} groups): Export to Claude AI for dimension assessment")
    L.append(f"2. **KEYWORD_WEAK** ({weak} groups): Review assignments — confirm or reassign")
    L.append(f"3. **KEYWORD_STRONG** ({strong} groups): Spot-check sample for false positives")
    L.append(f"4. **Multi-dimension registries**: Registries with high dimension spread may need sub-classification")
    L.append("")
    L.append("### Effort Estimate")
    L.append("")
    L.append(f"- {unclassified + weak} groups need Claude AI attention ({(unclassified+weak)*100//total}% of total)")
    L.append(f"- {len(priorities)} registries have unclassified groups")
    L.append(f"- Top 10 registries account for {sum(p['unclassified'] for p in priorities[:10])} of {total_uncl} unclassified")
    L.append("")

    # ═══════════════════════════════════════════════════════════════════════
    # WRITE
    # ═══════════════════════════════════════════════════════════════════════
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, f"wa-dimension-report-{now.replace('-', '')}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    print(f"Report written: {out_path}")
    print(f"Sections: 8")
    print(f"Lines: {len(L)}")

    conn.close()


if __name__ == "__main__":
    main()
