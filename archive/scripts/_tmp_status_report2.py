"""Generate programme status report — 2026-03-31."""
import sqlite3
from datetime import date

conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row
today = date.today().isoformat()
today_compact = date.today().strftime('%Y%m%d')

lines = []
def p(s=''): lines.append(s)

p(f'# Programme Status Report — {today}')
p()
p('> Schema v3.8.0 | Post mti_terms dedup + OWNER/XREF fix | VCB-001 + VCB-002 applied')
p()

# 1. Programme Overview
p('## 1. Programme Overview')
p()
total = conn.execute('SELECT COUNT(*) FROM word_registry').fetchone()[0]
active = conn.execute("SELECT COUNT(*) FROM word_registry WHERE phase1_status = 'Complete' AND phase1_term_count > 0").fetchone()[0]
excluded = conn.execute("SELECT COUNT(*) FROM word_registry WHERE phase1_status = 'Excluded'").fetchone()[0]
zero = total - active - excluded
p('| Metric | Count |')
p('|--------|-------|')
p(f'| Total registries | {total} |')
p(f'| Active (Phase 1 Complete, has terms) | {active} |')
p(f'| Excluded (Phase 1) | {excluded} |')
p(f'| Zero-term / other | {zero} |')
p()

# 2. Pipeline Status
p('## 2. Pipeline Status')
p()
p('### 2.1 Combined Status Matrix')
p()
p('| session_b_status | verse_context_status | Count |')
p('|-----------------|---------------------|-------|')
for r in conn.execute('''
    SELECT COALESCE(session_b_status, 'NULL') as sb,
           COALESCE(verse_context_status, 'NULL') as vc, COUNT(*) as c
    FROM word_registry GROUP BY session_b_status, verse_context_status ORDER BY c DESC
'''):
    p(f'| {r["sb"]} | {r["vc"]} | {r["c"]} |')
p()

# 3. Verse Context Progress
p('## 3. Verse Context — Stage 1 Progress')
p()
vc_complete = conn.execute("SELECT COUNT(*) FROM word_registry WHERE verse_context_status = 'Complete'").fetchone()[0]
vc_progress = conn.execute("SELECT COUNT(*) FROM word_registry WHERE verse_context_status = 'In Progress'").fetchone()[0]
vc_null = conn.execute('SELECT COUNT(*) FROM word_registry WHERE verse_context_status IS NULL').fetchone()[0]
groups = conn.execute('SELECT COUNT(*) FROM verse_context_group WHERE delete_flagged = 0').fetchone()[0]
vc_total = conn.execute('SELECT COUNT(*) FROM verse_context WHERE delete_flagged = 0').fetchone()[0]
anchors = conn.execute('SELECT COUNT(*) FROM verse_context WHERE is_anchor = 1 AND delete_flagged = 0').fetchone()[0]
related = conn.execute('SELECT COUNT(*) FROM verse_context WHERE is_related = 1 AND delete_flagged = 0').fetchone()[0]
set_aside = conn.execute('SELECT COUNT(*) FROM verse_context WHERE is_relevant = 0 AND delete_flagged = 0').fetchone()[0]
relevant = conn.execute('SELECT COUNT(*) FROM verse_context WHERE is_relevant = 1 AND delete_flagged = 0').fetchone()[0]

p('| Metric | Count |')
p('|--------|-------|')
p(f'| Registries Complete | **{vc_complete}** / 181 ({vc_complete/181*100:.1f}%) |')
p(f'| Registries In Progress | {vc_progress} |')
p(f'| Registries outside scope (NULL) | {vc_null} |')
p(f'| Batches processed | 2 (VCB-001, VCB-002) |')
p(f'| verse_context_group records | {groups} |')
p(f'| verse_context records | {vc_total:,} |')
p(f'| --- Anchor verses | {anchors} |')
p(f'| --- Related verses | {related} |')
p(f'| --- Set aside | {set_aside:,} |')
p(f'| --- Total relevant | {relevant} |')
p()

# Completed registries
p('### 3.1 Completed Registries')
p()
completed = conn.execute('''
    SELECT no, word, cluster_assignment FROM word_registry
    WHERE verse_context_status = 'Complete' ORDER BY no
''').fetchall()
vcb1_regs = {1,2,3,4,5}
p('| Reg | Word | Cluster | Batch |')
p('|-----|------|---------|-------|')
for r in completed:
    batch = 'VCB-001' if r['no'] in vcb1_regs else 'VCB-002'
    p(f'| {r["no"]} | {r["word"]} | {r["cluster_assignment"]} | {batch} |')
p()

# Remaining
eligible = conn.execute('''
    SELECT COUNT(DISTINCT mt.id) as terms
    FROM mti_terms mt
    JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
      AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
    WHERE mt.delete_flagged = 0 AND mt.status IN ('extracted', 'extracted_thin')
      AND (SELECT COUNT(*) FROM wa_verse_records vr
           WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0) > 0
      AND NOT EXISTS (
          SELECT 1 FROM verse_context vc
          WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
      )
''').fetchone()[0]

# Get verse count for remaining terms
remaining_verses = conn.execute('''
    SELECT SUM(vc_sub.vcount) as total
    FROM (
        SELECT ti.id, COUNT(vr.id) as vcount
        FROM wa_term_inventory ti
        JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number AND mt.delete_flagged = 0
        JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
        WHERE ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
          AND mt.status IN ('extracted', 'extracted_thin')
          AND NOT EXISTS (
              SELECT 1 FROM verse_context vc
              WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
          )
        GROUP BY ti.id
    ) vc_sub
''').fetchone()[0] or 0

p('### 3.2 Remaining Work')
p()
p('| Metric | Count |')
p('|--------|-------|')
p(f'| OWNER terms still unclassified | {eligible:,} |')
p(f'| Verses to classify | {remaining_verses:,} |')
p(f'| Estimated batches remaining | ~{remaining_verses // 2250} |')
p()

# 4. Data Health
p('## 4. Data Health')
p()
active_mti = conn.execute('SELECT COUNT(*) FROM mti_terms WHERE delete_flagged = 0').fetchone()[0]
deleted_mti = conn.execute('SELECT COUNT(*) FROM mti_terms WHERE delete_flagged = 1').fetchone()[0]
owner_ti = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE term_owner_type = 'OWNER' AND delete_flagged = 0").fetchone()[0]
xref_ti = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE term_owner_type = 'XREF' AND delete_flagged = 0").fetchone()[0]
active_vr = conn.execute('SELECT COUNT(*) FROM wa_verse_records WHERE delete_flagged = 0').fetchone()[0]
dupes = conn.execute('SELECT COUNT(*) FROM (SELECT strongs_number FROM mti_terms WHERE delete_flagged = 0 GROUP BY strongs_number HAVING COUNT(*) > 1)').fetchone()[0]
multi_own = conn.execute("SELECT COUNT(*) FROM (SELECT strongs_number FROM wa_term_inventory WHERE term_owner_type='OWNER' AND delete_flagged=0 GROUP BY strongs_number HAVING COUNT(DISTINCT file_id) > 1)").fetchone()[0]
fk_null = conn.execute('SELECT COUNT(*) FROM mti_terms WHERE delete_flagged = 0 AND owning_registry_fk IS NULL').fetchone()[0]
status_null = conn.execute('SELECT COUNT(*) FROM mti_terms WHERE delete_flagged = 0 AND status IS NULL').fetchone()[0]

p('| Check | Value | Status |')
p('|-------|-------|--------|')
p(f'| Active mti_terms | {active_mti} | |')
p(f'| Deleted mti_terms | {deleted_mti} | |')
p(f'| Duplicate strongs | {dupes} | {"CLEAN" if dupes == 0 else "ISSUE"} |')
p(f'| Multi-OWNER strongs | {multi_own} | {"CLEAN" if multi_own == 0 else "ISSUE"} |')
p(f'| owning_registry_fk NULL | {fk_null} | {"CLEAN" if fk_null == 0 else "ISSUE"} |')
p(f'| mti status NULL | {status_null} | {"CLEAN" if status_null == 0 else "ISSUE"} |')
p(f'| OWNER ti records | {owner_ti} | |')
p(f'| XREF ti records | {xref_ti} | |')
p(f'| Active verses | {active_vr:,} | |')
p()

# Status distribution
p('### 4.1 mti_terms Status Distribution')
p()
p('| Status | Count | % |')
p('|--------|-------|---|')
for r in conn.execute('SELECT COALESCE(status, "NULL") as s, COUNT(*) as c FROM mti_terms WHERE delete_flagged = 0 GROUP BY status ORDER BY c DESC'):
    pct = r['c'] / active_mti * 100
    p(f'| {r["s"]} | {r["c"]} | {pct:.1f}% |')
p()

# 5. Cluster Progress
p('## 5. Cluster Progress')
p()
p('| Cluster | Words | VC Complete | VC In Progress | Excluded/NULL |')
p('|---------|-------|-------------|----------------|---------------|')
for c in conn.execute('''
    SELECT cluster_assignment,
           COUNT(*) as total,
           SUM(CASE WHEN verse_context_status = 'Complete' THEN 1 ELSE 0 END) as vc_done,
           SUM(CASE WHEN verse_context_status = 'In Progress' THEN 1 ELSE 0 END) as vc_ip,
           SUM(CASE WHEN verse_context_status IS NULL THEN 1 ELSE 0 END) as vc_null
    FROM word_registry
    WHERE cluster_assignment IS NOT NULL AND cluster_assignment != 'unassigned'
    GROUP BY cluster_assignment ORDER BY cluster_assignment
'''):
    p(f'| {c["cluster_assignment"]} | {c["total"]} | {c["vc_done"]} | {c["vc_ip"]} | {c["vc_null"]} |')
p()

# 6. Next Steps
p('## 6. Next Steps')
p()
p(f'1. **Continue Stage 1 Verse Context** — ~{remaining_verses // 2250} batches remaining ({eligible:,} terms, {remaining_verses:,} verses)')
p('2. VCB-003 ready for construction')
p(f'3. {vc_complete} registries have DataPrep gate open — DataPrep can begin for these when Verse Context sweep is further along')
p('4. No registries yet at Pre-Analysis Complete')
p()
p('---')
p(f'*Produced {today} by Claude Code. Schema v3.8.0.*')

outpath = f'outputs/reports/wa-programme-status-report-{today_compact}.md'
with open(outpath, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f'Written: {outpath} ({len(lines)} lines)')
conn.close()
