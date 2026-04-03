"""Programme progress report."""
import sqlite3, os
from datetime import date

conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row
today = date.today().isoformat()
today_c = date.today().strftime('%Y%m%d')

lines = []
def p(s=''): lines.append(s)

p(f'# Programme Status Report — {today}')
p()
p('> Schema v3.8.0 | VCB-001 through VCB-012 applied (+ VCB-006 diff + VCB-012 H2617A supplemental)')
p()

# 1. Overview
total = conn.execute('SELECT COUNT(*) FROM word_registry').fetchone()[0]
active = conn.execute("SELECT COUNT(*) FROM word_registry WHERE phase1_status = 'Complete' AND phase1_term_count > 0").fetchone()[0]
excluded = conn.execute("SELECT COUNT(*) FROM word_registry WHERE phase1_status = 'Excluded'").fetchone()[0]
p('## 1. Programme Overview')
p()
p('| Metric | Count |')
p('|--------|-------|')
p(f'| Total registries | {total} |')
p(f'| Active | {active} |')
p(f'| Excluded | {excluded} |')
p()

# 2. Status Matrix
p('## 2. Pipeline Status')
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

# 3. Verse Context
p('## 3. Verse Context — Stage 1 Progress')
p()
vc_complete = conn.execute("SELECT COUNT(*) FROM word_registry WHERE verse_context_status = 'Complete'").fetchone()[0]
vc_progress = conn.execute("SELECT COUNT(*) FROM word_registry WHERE verse_context_status = 'In Progress'").fetchone()[0]
groups = conn.execute('SELECT COUNT(*) FROM verse_context_group WHERE delete_flagged = 0').fetchone()[0]
vc_total = conn.execute('SELECT COUNT(*) FROM verse_context WHERE delete_flagged = 0').fetchone()[0]
anchors = conn.execute('SELECT COUNT(*) FROM verse_context WHERE is_anchor = 1 AND delete_flagged = 0').fetchone()[0]
relevant = conn.execute('SELECT COUNT(*) FROM verse_context WHERE is_relevant = 1 AND delete_flagged = 0').fetchone()[0]
set_aside = conn.execute('SELECT COUNT(*) FROM verse_context WHERE is_relevant = 0 AND delete_flagged = 0').fetchone()[0]

p('| Metric | Count |')
p('|--------|-------|')
p(f'| Registries Complete | **{vc_complete}** / 181 ({vc_complete/181*100:.1f}%) |')
p(f'| Registries In Progress | {vc_progress} |')
p(f'| Batches processed | 12 + 2 supplemental/differential |')
p(f'| verse_context_group records | {groups:,} |')
p(f'| verse_context records | {vc_total:,} |')
p(f'| --- Anchors | {anchors:,} |')
p(f'| --- Related | {relevant - anchors:,} |')
p(f'| --- Set aside | {set_aside:,} |')
p()

# Completed registries - compact list
p('### 3.1 Completed Registries')
p()
completed = conn.execute('''
    SELECT no, word FROM word_registry
    WHERE verse_context_status = 'Complete' ORDER BY no
''').fetchall()
items = [f'{r["no"]}-{r["word"]}' for r in completed]
for i in range(0, len(items), 4):
    chunk = items[i:i+4]
    p('  ' + '  |  '.join(f'{item:>20s}' for item in chunk))
p()

# Remaining
eligible = conn.execute('''
    SELECT COUNT(DISTINCT mt.id) FROM mti_terms mt
    JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
      AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
    WHERE mt.delete_flagged = 0 AND mt.status IN ('extracted', 'extracted_thin')
      AND (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0) > 0
      AND NOT EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0)
''').fetchone()[0]
remaining_vr = conn.execute('''
    SELECT SUM(sub.vc) FROM (
        SELECT COUNT(vr.id) as vc FROM wa_term_inventory ti
        JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number AND mt.delete_flagged = 0
        JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
        WHERE ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
          AND mt.status IN ('extracted', 'extracted_thin')
          AND NOT EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0)
        GROUP BY ti.id
    ) sub
''').fetchone()[0] or 0

p('### 3.2 Remaining Work')
p()
p('| Metric | Count |')
p('|--------|-------|')
p(f'| Terms unclassified | {eligible:,} |')
p(f'| Verses to classify | {remaining_vr:,} |')
p(f'| Estimated batches remaining | ~{remaining_vr // 2250} |')
p()

# Partial registries
p('### 3.3 Partial Registries')
p()
partials = conn.execute('''
    SELECT wr.no, wr.word,
           COUNT(DISTINCT mt.id) as total_owner,
           SUM(CASE WHEN EXISTS (
               SELECT 1 FROM verse_context vc WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
           ) THEN 1 ELSE 0 END) as classified
    FROM word_registry wr
    JOIN wa_file_index fi ON fi.word_registry_fk = wr.id
    JOIN wa_term_inventory ti ON ti.file_id = fi.id AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
    JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number AND mt.delete_flagged = 0
      AND mt.status IN ('extracted', 'extracted_thin')
    WHERE wr.verse_context_status = 'In Progress'
      AND EXISTS (SELECT 1 FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0)
    GROUP BY wr.no
    HAVING classified > 0 AND classified < COUNT(DISTINCT mt.id)
    ORDER BY wr.no
''').fetchall()
if partials:
    p('| Reg | Word | Classified | Total | Remaining |')
    p('|-----|------|-----------|-------|-----------|')
    for r in partials:
        p(f'| {r["no"]} | {r["word"]} | {r["classified"]} | {r["total_owner"]} | {r["total_owner"] - r["classified"]} |')
else:
    p('No partial registries.')
p()

# 4. Data Health
p('## 4. Data Health')
p()
active_mti = conn.execute('SELECT COUNT(*) FROM mti_terms WHERE delete_flagged = 0').fetchone()[0]
owner_ti = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE term_owner_type = 'OWNER' AND delete_flagged = 0").fetchone()[0]
xref_ti = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE term_owner_type = 'XREF' AND delete_flagged = 0").fetchone()[0]
active_vr = conn.execute('SELECT COUNT(*) FROM wa_verse_records WHERE delete_flagged = 0').fetchone()[0]
dupes = conn.execute("SELECT COUNT(*) FROM (SELECT strongs_number FROM mti_terms WHERE delete_flagged = 0 GROUP BY strongs_number HAVING COUNT(*) > 1)").fetchone()[0]
multi_own = conn.execute("SELECT COUNT(*) FROM (SELECT strongs_number FROM wa_term_inventory WHERE term_owner_type='OWNER' AND delete_flagged=0 GROUP BY strongs_number HAVING COUNT(DISTINCT file_id) > 1)").fetchone()[0]

p('| Check | Value | Status |')
p('|-------|-------|--------|')
p(f'| Active mti_terms | {active_mti:,} | {"CLEAN" if dupes == 0 else "ISSUE"} |')
p(f'| Multi-OWNER strongs | {multi_own} | {"CLEAN" if multi_own == 0 else "ISSUE"} |')
p(f'| OWNER ti | {owner_ti:,} | |')
p(f'| XREF ti | {xref_ti:,} | |')
p(f'| Active verses | {active_vr:,} | |')
p()

# 5. Cluster Progress
p('## 5. Cluster Progress')
p()
p('| Cluster | Words | VC Complete | In Progress | Excluded |')
p('|---------|-------|-------------|-------------|----------|')
for c in conn.execute('''
    SELECT cluster_assignment, COUNT(*) as total,
           SUM(CASE WHEN verse_context_status = 'Complete' THEN 1 ELSE 0 END) as done,
           SUM(CASE WHEN verse_context_status = 'In Progress' THEN 1 ELSE 0 END) as ip,
           SUM(CASE WHEN verse_context_status IS NULL THEN 1 ELSE 0 END) as ex
    FROM word_registry
    WHERE cluster_assignment IS NOT NULL AND cluster_assignment != 'unassigned'
    GROUP BY cluster_assignment ORDER BY cluster_assignment
'''):
    p(f'| {c["cluster_assignment"]} | {c["total"]} | {c["done"]} | {c["ip"]} | {c["ex"]} |')
p()

# 6. Batch History
p('## 6. Batch History')
p()
p('| Batch | Terms | Registries completed | Notes |')
p('|-------|-------|---------------------|-------|')
p('| VCB-001 | 178 | abomination, agony, ambition, anger, anguish (5) | |')
p('| VCB-002 | 65 | anointing, anxiety, appetite, awe, bitterness, boldness, bondage, brokenness (8) | |')
p('| VCB-003 | 112 | calling, character, compassion, condemnation, consecration, contentment, corruption (7) | |')
p('| VCB-004 | 119 | conscience, courage, covenant, covetousness, debauchery, deceit, defilement, delight (8) | 2 errors fixed |')
p('| VCB-005 | 81 | despair, devotion, dignity, diligence, discernment, disobedience (6) | |')
p('| VCB-006 | 135 | distress, division, dread, endurance, envy (5) | + diff correction |')
p('| VCB-007 | 74 | evil, experience, faith, faithfulness (4) | |')
p('| VCB-008 | 112 | fear, fellowship, foolishness, forgiveness, generosity, gentleness, goodness, grace, gratitude, greed, grief, groaning (12) | |')
p('| VCB-009 | 100 | hardness, hatred, holiness, honesty, hope, humility, hypocrisy, idolatry, imagination, impurity, indignation (11) | 1 deferred term |')
p('| VCB-010 | 91 | iniquity, innocence, insight, integrity, intercession, jealousy, joy (7) | |')
p('| VCB-011 | 25 | justice (1) | kindness partial |')
p('| VCB-012 | 120 | kindness, knowledge, longing, love, lust, meaning, meditation (7) | + H2617A supplemental |')
p(f'| **Total** | **1,212** | **{vc_complete} registries** | |')
p()

p('---')
p(f'*Produced {today} by Claude Code. Schema v3.8.0.*')

outpath = f'outputs/reports/programme/wa-programme-status-report-{today_c}.md'
if os.path.exists(outpath):
    outpath = f'outputs/reports/programme/wa-programme-status-report-{today_c}-v2.md'
with open(outpath, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f'Written: {outpath} ({len(lines)} lines)')
conn.close()
