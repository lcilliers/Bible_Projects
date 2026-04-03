"""Generate comprehensive programme status report."""
import sqlite3
from datetime import date

conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row
today = date.today().isoformat()
today_compact = date.today().strftime('%Y%m%d')

lines = []
def p(s=""): lines.append(s)

p(f"# Programme Status Report — {today}")
p()
p("> Produced by Claude Code. Schema v3.8.0. Post mti_terms deduplication and OWNER/XREF fix.")
p()

# 1. Programme Overview
p("## 1. Programme Overview")
p()
total_reg = conn.execute("SELECT COUNT(*) FROM word_registry").fetchone()[0]
active_reg = conn.execute("SELECT COUNT(*) FROM word_registry WHERE phase1_status = 'Complete' AND phase1_term_count > 0").fetchone()[0]
excluded = conn.execute("SELECT COUNT(*) FROM word_registry WHERE phase1_status = 'Excluded'").fetchone()[0]
zero_term = conn.execute("SELECT COUNT(*) FROM word_registry WHERE phase1_status = 'Complete' AND (phase1_term_count = 0 OR phase1_term_count IS NULL)").fetchone()[0]

p("| Metric | Count |")
p("|--------|-------|")
p(f"| Total registries | {total_reg} |")
p(f"| Active (Phase 1 Complete, has terms) | {active_reg} |")
p(f"| Excluded | {excluded} |")
p(f"| Zero-term (Complete but no terms) | {zero_term} |")
p()

# 2. Pipeline Status
p("## 2. Pipeline Status — Dual Track")
p()
p("### 2.1 session_b_status")
p()
p("| Status | Count |")
p("|--------|-------|")
for r in conn.execute("SELECT COALESCE(session_b_status, 'NULL') as s, COUNT(*) as c FROM word_registry GROUP BY session_b_status ORDER BY c DESC"):
    p(f"| {r['s']} | {r['c']} |")
p()

p("### 2.2 verse_context_status")
p()
p("| Status | Count |")
p("|--------|-------|")
for r in conn.execute("SELECT COALESCE(verse_context_status, 'NULL') as s, COUNT(*) as c FROM word_registry GROUP BY verse_context_status ORDER BY c DESC"):
    p(f"| {r['s']} | {r['c']} |")
p()

p("### 2.3 Combined Status Matrix")
p()
p("| session_b_status | verse_context_status | Count |")
p("|-----------------|---------------------|-------|")
for r in conn.execute("""
    SELECT COALESCE(session_b_status, 'NULL') as sb,
           COALESCE(verse_context_status, 'NULL') as vc,
           COUNT(*) as c
    FROM word_registry GROUP BY session_b_status, verse_context_status
    ORDER BY c DESC
"""):
    p(f"| {r['sb']} | {r['vc']} | {r['c']} |")
p()

# 3. Term Index
p("## 3. Term Index — mti_terms")
p()
active_mti = conn.execute("SELECT COUNT(*) FROM mti_terms WHERE delete_flagged = 0").fetchone()[0]
deleted_mti = conn.execute("SELECT COUNT(*) FROM mti_terms WHERE delete_flagged = 1").fetchone()[0]
p("| Metric | Count |")
p("|--------|-------|")
p(f"| Active terms | {active_mti} |")
p(f"| Deleted (flagged) | {deleted_mti} |")
p(f"| Total rows | {active_mti + deleted_mti} |")
p()

p("### 3.1 Status Distribution (active only)")
p()
p("| Status | Count | % |")
p("|--------|-------|---|")
for r in conn.execute("SELECT COALESCE(status, 'NULL') as s, COUNT(*) as c FROM mti_terms WHERE delete_flagged = 0 GROUP BY status ORDER BY c DESC"):
    pct = r['c'] / active_mti * 100
    p(f"| {r['s']} | {r['c']} | {pct:.1f}% |")
p()

p("### 3.2 Language Distribution")
p()
p("| Language | Count |")
p("|----------|-------|")
for r in conn.execute("SELECT language, COUNT(*) as c FROM mti_terms WHERE delete_flagged = 0 GROUP BY language ORDER BY c DESC"):
    p(f"| {r['language']} | {r['c']} |")
p()

p("### 3.3 Data Quality — Key Fields")
p()
p("| Field | NULL count | Status |")
p("|-------|-----------|--------|")
for field in ['strongs_number', 'transliteration', 'gloss', 'language', 'owning_registry_fk', 'owning_word', 'status', 'extraction_date']:
    n = conn.execute(f'SELECT COUNT(*) FROM mti_terms WHERE delete_flagged = 0 AND "{field}" IS NULL').fetchone()[0]
    status = "CLEAN" if n == 0 else f"**{n} NULL**"
    p(f"| {field} | {n} | {status} |")
p()

p("### 3.4 Integrity")
p()
dupes = conn.execute("SELECT COUNT(*) FROM (SELECT strongs_number FROM mti_terms WHERE delete_flagged = 0 GROUP BY strongs_number HAVING COUNT(*) > 1)").fetchone()[0]
p(f"- Duplicate Strong's (active): **{dupes}**")
p(f"- 1 row per Strong's: **{'YES' if dupes == 0 else 'NO'}**")
p()

# 4. Term Inventory
p("## 4. Term Inventory — wa_term_inventory")
p()
active_ti = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 0").fetchone()[0]
owner_ti = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE term_owner_type = 'OWNER' AND delete_flagged = 0").fetchone()[0]
xref_ti = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE term_owner_type = 'XREF' AND delete_flagged = 0").fetchone()[0]
p("| Metric | Count |")
p("|--------|-------|")
p(f"| Active records | {active_ti} |")
p(f"| OWNER | {owner_ti} |")
p(f"| XREF | {xref_ti} |")
p()

p("### 4.1 OWNER/XREF Integrity")
p()
multi_owner = conn.execute("SELECT COUNT(*) FROM (SELECT strongs_number FROM wa_term_inventory WHERE term_owner_type='OWNER' AND delete_flagged=0 GROUP BY strongs_number HAVING COUNT(DISTINCT file_id) > 1)").fetchone()[0]
xref_active_vr = conn.execute("SELECT COUNT(*) FROM wa_verse_records vr JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id WHERE ti.term_owner_type = 'XREF' AND ti.delete_flagged = 0 AND vr.delete_flagged = 0").fetchone()[0]
p(f"- Multi-OWNER Strong's: **{multi_owner}**")
p(f"- XREF with active verses: **{xref_active_vr}**")
p()

p("### 4.2 Data Quality — Key Fields")
p()
p("| Field | NULL count | Status |")
p("|-------|-----------|--------|")
for field in ['file_id', 'language', 'strongs_number', 'transliteration', 'step_search_gloss', 'word_analysis_gloss', 'occurrence_count', 'term_owner_type']:
    n = conn.execute(f'SELECT COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 0 AND "{field}" IS NULL').fetchone()[0]
    status = "CLEAN" if n == 0 else f"**{n} NULL**"
    p(f"| {field} | {n} | {status} |")
p()

# 5. Verse Records
p("## 5. Verse Records")
p()
active_vr = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE delete_flagged = 0").fetchone()[0]
flagged_vr = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE delete_flagged = 1").fetchone()[0]
p("| Metric | Count |")
p("|--------|-------|")
p(f"| Active verses | {active_vr:,} |")
p(f"| Deleted (flagged) | {flagged_vr:,} |")
p(f"| Total | {active_vr + flagged_vr:,} |")
p()

# 6. Verse Context
p("## 6. Verse Context — Stage 1 Progress")
p()
vc_groups = conn.execute("SELECT COUNT(*) FROM verse_context_group WHERE delete_flagged = 0").fetchone()[0]
vc_records = conn.execute("SELECT COUNT(*) FROM verse_context WHERE delete_flagged = 0").fetchone()[0]
p("| Metric | Count |")
p("|--------|-------|")
p(f"| verse_context_group records | {vc_groups} |")
p(f"| verse_context records | {vc_records} |")
p(f"| Registries at VC Complete | 0 / 181 |")
p(f"| Batches processed | 0 |")
p(f"| **Stage 1 status** | **Not started — VCB-001 ready for submission** |")
p()

# 7. Cluster Progress
p("## 7. Cluster Progress")
p()
p("| Cluster | Words | VC Reset | Pre-Analysis | Analysis Complete | SB Complete |")
p("|---------|-------|----------|--------------|-------------------|-------------|")
for c in conn.execute("""
    SELECT cluster_assignment,
           COUNT(*) as total,
           SUM(CASE WHEN session_b_status = 'Verse Context Reset' THEN 1 ELSE 0 END) as vc_reset,
           SUM(CASE WHEN session_b_status = 'Pre-Analysis Complete' THEN 1 ELSE 0 END) as preanalysis,
           SUM(CASE WHEN session_b_status = 'Analysis Complete' THEN 1 ELSE 0 END) as analysis,
           SUM(CASE WHEN session_b_status = 'Session B Complete' THEN 1 ELSE 0 END) as complete
    FROM word_registry
    WHERE cluster_assignment IS NOT NULL AND cluster_assignment != 'unassigned'
    GROUP BY cluster_assignment ORDER BY cluster_assignment
"""):
    p(f"| {c['cluster_assignment']} | {c['total']} | {c['vc_reset']} | {c['preanalysis']} | {c['analysis']} | {c['complete']} |")
p()

# 8. Data Fixes
p("## 8. Data Fixes Applied (2026-03-30)")
p()
p("| Fix | Records | Detail |")
p("|-----|---------|--------|")
p("| mti_terms deduplication | 3,616 flagged | 1 row per Strong's (was 1,780 duplicated) |")
p("| mti_terms orphans | 64 flagged | No inventory reference |")
p("| OWNER/XREF fix | 1,871 flipped | Each Strong's max 1 OWNER |")
p("| XREF verse flagging | 48,237 flagged | XREF verses delete_flagged |")
p("| owning_registry_fk | 1,373 set | All active mti now have FK |")
p("| status NULL | 810 set | Terms with active verses -> extracted |")
p("| owning_word NULL | 1 fixed | Set from gloss |")
p("| extraction_date NULL | 538 set | Set to 2026-03-28 |")
p("| word_analysis_gloss NULL | 16 set | Set from step_search_gloss |")
p("| occurrence_count NULL | 1 fixed | Set from verse count |")
p("| delete_flagged column | added | New column on mti_terms |")
p("| audit_word.py | 3 fixes | Dedup guard, FK on insert, stale field refresh |")
p()

# 9. Next Steps
p("## 9. Next Steps")
p()
p("1. **VCB-001 submitted** — 1st Verse Context batch ready for Claude AI classification")
p(f"2. **Estimated ~{active_vr // 2250} batches** to classify all {active_vr:,} active verses")
p("3. After Stage 1 complete: pool-based Session B per RMG v5.6 processing sequence")
p()

p("---")
p(f"*Produced {today} by Claude Code. Schema v3.8.0.*")

outpath = f"outputs/wa-programme-status-report-{today_compact}.md"
with open(outpath, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f"Written: {outpath} ({len(lines)} lines)")
conn.close()
