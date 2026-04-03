"""Remaining work analysis for Verse Context Stage 1."""
import sqlite3, os
from datetime import date

conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

lines = []
def p(s=''): lines.append(s)

p('# Verse Context -- Remaining Work Analysis')
p()
p('> Produced 2026-04-02 by Claude Code for researcher + Claude AI planning')
p('> 81/181 registries complete. This report analyses the remaining terms and verses.')
p()

# 1. The Skew
p('## 1. The Skew Problem')
p()
p('We are ~50% through terms but have ~67% of verses remaining. A small number of')
p('high-frequency terms dominate the remaining verse count.')
p()
p('| Verse bucket | Terms | % of terms | Verses | % of verses |')
p('|-------------|-------|-----------|--------|------------|')
dist = conn.execute('''
    SELECT
        CASE
            WHEN vc <= 10 THEN '1-10'
            WHEN vc <= 50 THEN '11-50'
            WHEN vc <= 100 THEN '51-100'
            WHEN vc <= 250 THEN '101-250'
            WHEN vc <= 500 THEN '251-500'
            ELSE '500+'
        END as bucket,
        COUNT(*) as terms,
        SUM(vc) as verses
    FROM (
        SELECT mt.id, COUNT(vr.id) as vc
        FROM mti_terms mt
        JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
          AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
        JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
        WHERE mt.delete_flagged = 0 AND mt.status IN ('extracted', 'extracted_thin')
          AND NOT EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0)
        GROUP BY mt.id
    )
    GROUP BY bucket ORDER BY MIN(vc)
''').fetchall()
total_terms = sum(r['terms'] for r in dist)
total_verses = sum(r['verses'] for r in dist)
for r in dist:
    tpct = r['terms'] / total_terms * 100
    vpct = r['verses'] / total_verses * 100
    p(f'| {r["bucket"]:>10s} | {r["terms"]:>5d} | {tpct:>8.1f}% | {r["verses"]:>6d} | {vpct:>9.1f}% |')
p(f'| **Total** | **{total_terms:,}** | | **{total_verses:,}** | |')
p()
p('**Key insight:** 71 terms (6% of remaining) with 100+ verses hold 46.6% of the remaining verse load.')
p('Many are grammatical particles, function words, and physical nouns -- processable quickly as')
p('bulk set-asides without deep analytical work.')
p()

# 2. High-frequency terms
p('## 2. High-Frequency Remaining Terms (100+ verses)')
p()

big_terms = conn.execute('''
    SELECT mt.id as mti_id, mt.strongs_number, mt.transliteration, mt.gloss,
           wr.no as reg_no, wr.word,
           COUNT(vr.id) as verse_count
    FROM mti_terms mt
    JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
      AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
    JOIN wa_file_index fi ON fi.id = ti.file_id
    JOIN word_registry wr ON wr.id = fi.word_registry_fk
    JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
    WHERE mt.delete_flagged = 0
      AND mt.status IN ('extracted', 'extracted_thin')
      AND NOT EXISTS (
          SELECT 1 FROM verse_context vc
          WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
      )
    GROUP BY mt.id
    HAVING COUNT(vr.id) >= 100
    ORDER BY COUNT(vr.id) DESC
''').fetchall()

def categorise(gloss, strongs):
    g = (gloss or '').lower()
    if any(w in g for w in ['also', 'till', 'because', 'nothing', 'much',
                             'you [', 'before', 'not']):
        return 'Particle/function word'
    if any(w in g for w in ['hand', 'foot', 'flesh', 'place', 'name', 'enemy',
                             'head', 'rotten']):
        return 'Physical/spatial noun'
    if any(w in g for w in ['to come', 'to go', 'to find', 'to die', 'to make',
                             'to dwell', 'to multiply', 'to keep']):
        return 'Generic verb'
    if any(w in g for w in ['to bless', 'to exalt', 'to remember', 'to hear',
                             'heart', 'obey', 'pray', 'to sanctify', 'holy']):
        return 'Likely inner-being use'
    return 'Needs assessment'

p('| Verses | Strong | Transliteration | Gloss | Registry | Likely category |')
p('|--------|--------|----------------|-------|----------|----------------|')
cats = {}
for r in big_terms:
    cat = categorise(r['gloss'], r['strongs_number'])
    if cat not in cats:
        cats[cat] = {'terms': 0, 'verses': 0}
    cats[cat]['terms'] += 1
    cats[cat]['verses'] += r['verse_count']
    p(f'| {r["verse_count"]:>6d} | {r["strongs_number"]} | {r["transliteration"]} | {r["gloss"]} | {r["reg_no"]}-{r["word"]} | {cat} |')
p()

p('### Category summary (100+ verse terms)')
p()
p('| Category | Terms | Verses | Action |')
p('|----------|-------|--------|--------|')
for cat in sorted(cats.keys()):
    action = ''
    if 'Particle' in cat:
        action = 'Candidate for bulk all-verses-fail'
    elif 'Physical' in cat:
        action = 'Candidate for bulk all-verses-fail'
    elif 'Generic' in cat:
        action = 'Quick assessment needed'
    elif 'inner-being' in cat:
        action = 'Full classification required'
    else:
        action = 'Claude AI assessment needed'
    p(f'| {cat} | {cats[cat]["terms"]} | {cats[cat]["verses"]:,} | {action} |')
p()

# 3. By registry
p('## 3. Remaining Work by Registry')
p()
p('| Registry | Word | Terms | Verses | Status |')
p('|----------|------|-------|--------|--------|')
by_reg = conn.execute('''
    SELECT wr.no, wr.word, wr.verse_context_status,
           COUNT(DISTINCT mt.id) as terms,
           SUM(vc_sub.verse_count) as verses
    FROM mti_terms mt
    JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
      AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
    JOIN wa_file_index fi ON fi.id = ti.file_id
    JOIN word_registry wr ON wr.id = fi.word_registry_fk
    JOIN (
        SELECT term_inv_id, COUNT(*) as verse_count
        FROM wa_verse_records WHERE delete_flagged = 0
        GROUP BY term_inv_id
    ) vc_sub ON vc_sub.term_inv_id = ti.id
    WHERE mt.delete_flagged = 0
      AND mt.status IN ('extracted', 'extracted_thin')
      AND NOT EXISTS (SELECT 1 FROM verse_context vc WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0)
    GROUP BY wr.no
    ORDER BY SUM(vc_sub.verse_count) DESC
''').fetchall()
for r in by_reg:
    p(f'| {r["no"]} | {r["word"]} | {r["terms"]} | {r["verses"]:,} | {r["verse_context_status"]} |')
p()

# 4. Suggested approaches
p('## 4. Suggested Approaches')
p()
p('### Option A: Pre-filter high-frequency particles and function words')
p()
p('Before building batches, have Claude AI do a quick gloss-level triage of the 71 terms with 100+')
p('verses. For terms that are clearly grammatical particles (gam/also, ad/till, atten/you),')
p('function words, or physical nouns with no plausible inner-being use, approve bulk all-verses-fail')
p('classification. Claude Code applies the set-aside inserts directly without needing to pass')
p('the full verse corpus through a classification session.')
p()
p('**Estimated impact:** Could remove 5,000-8,000 verses from the pipeline immediately.')
p()
p('### Option B: Focused single-term batches for large-corpus terms')
p()
p('Terms with 200+ verses (about 15 terms) could be processed in dedicated single-term')
p('batches. Claude AI focuses on one term at a time, with the option to sample rather than')
p('inspect every verse (per the v2.2 all-verses-fail rule for large corpora where individual')
p('inspection confirms the pattern).')
p()
p('### Option C: Continue standard batching')
p()
p('Standard 2,000-2,500 verse batches as before. Large terms naturally consume whole batches.')
p('Safest but slowest -- approximately 25 more batches needed.')
p()
p('### Recommended: Option A + B')
p()
p('1. Claude AI triages the 71 high-frequency terms by gloss (this report provides the list)')
p('2. Researcher approves bulk all-verses-fail for obvious particles/function words')
p('3. Claude Code applies set-aside inserts for approved terms')
p('4. Remaining large-corpus terms processed in focused batches')
p('5. Standard batching continues for the smaller terms')
p()
p('This could reduce remaining work from ~25 batches to ~15-18, concentrating analytical')
p('effort on terms that genuinely engage the inner being.')
p()

p('---')
p('*Produced 2026-04-02 by Claude Code. For researcher + Claude AI planning.*')

outpath = 'outputs/reports/programme/vc-remaining-work-analysis-20260402.md'
with open(outpath, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f'Written: {outpath} ({len(lines)} lines)')
conn.close()
