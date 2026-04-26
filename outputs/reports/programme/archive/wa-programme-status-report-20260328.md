# Programme Status Report — Handoff to Claude AI

> Generated: 2026-03-28
> Schema version: 3.7.0
> Purpose: Comprehensive database status for Session B analysis planning

---

# 1. Programme Overview

| Metric | Value |
|--------|-------|
| Total registries | 212 |
| Active (non-excluded) | 181 |
| Excluded (Phase 1) | 31 |
| Active terms (OWNER) | 5518 |
| Active terms (XREF) | 1470 |
| Active verses | 133353 |
| delete_flagged terms | 367 |
| delete_flagged verses | 91176 |

**Note on delete_flagged records:** These remain in the database but are excluded from all standard queries and exports. They include: confirmed-delete terms (particles, function words), XREF verse duplicates, and terms flagged by the engine during audit. No physical deletion has occurred.

---

# 2. Session B Status

| Session B Status | Count |
|-----------------|-------|
| NULL (not started) | 33 |
| Analysis Complete | 35 |
| Ready for Analysis | 144 |

### v5.2 Extraction Cycle Completion

| Metric | Value |
|--------|-------|
| Registries with dimensional profile | 2 |
| Key findings recorded | 20 |
| Session D pointers | 18 |
| Terms with evidential_status | 155 |

Only registries with a dimensional profile in `wa_session_b_dimensions` have completed the v5.2 extraction cycle. All others at 'Analysis Complete' were completed under the old workflow and need v5.2 extraction.

---

# 3. Term Inventory Status

## 3.1 Term Ownership

Each term in `wa_term_inventory` is marked as OWNER (primary location for this Strong's number) or XREF (cross-reference copy belonging to another registry).

| term_owner_type | Active Terms | delete_flagged Terms |
|----------------|-------------|---------------------|
| NULL | 0 | 367 |
| OWNER | 5518 | 0 |
| XREF | 1470 | 0 |

**XREF verses are delete_flagged.** The active verse set contains only OWNER verses. XREF term records remain active for cross-registry linkage queries but their verses are excluded from exports.

## 3.2 MTI Status Distribution

The `mti_terms.status` field classifies each term's relevance to its owning registry.

| mti_terms.status | Count |
|-----------------|-------|
| NULL | 3078 |
| delete | 1903 |
| extracted | 1873 |
| extracted_thin | 521 |
| candidate_delete | 71 |
| extracted_theological_anchor | 17 |
| excluded | 9 |
| phase2_enrichment | 5 |
| xref_distress | 3 |
| xref_anger | 2 |
| xref_desire | 2 |
| xref_sorrow | 2 |
| xref_wisdom | 1 |

## 3.3 Evidential Status (where assigned)

Assigned during v5.2 Session B extraction. Only populated for registries that have completed the v5.2 cycle.

| evidential_status | Count |
|------------------|-------|
| confirmed | 106 |
| plausible | 44 |
| uncertain | 5 |

## 3.4 Quality Flags (OWNER terms, active, non-excluded registries)

| Quality Flag | Count | Notes |
|-------------|-------|-------|
| CONCRETE_PHYSICAL | 310 | Concrete nouns — flagged, not excluded. Verse analysis may reveal inner-being usage. |

**Note:** The engine-derived quality flags (NO_WORD_ANALYSIS, PROSE_ONLY_MEANING, THIN_DATA, SMALL_VERSE_SAMPLE, NO_VERSES, HIGH_FREQUENCY_ANCHOR) exist in the database but apply overwhelmingly to XREF copies and delete_flagged terms. When filtered to OWNER-only active terms in non-excluded registries, only CONCRETE_PHYSICAL remains as a meaningful quality indicator.

## 3.5 Phase 2 Flags (OWNER terms, active, non-excluded registries)

Researcher-owned analytical flags on terms. These are **Claude AI's responsibility** — set during Session B analysis.

| PH2 Flag | Count |
|----------|-------|
| SEMANTIC_RANGE_BREADTH | 180 |
| GOD_AS_SUBJECT | 177 |
| CAUSATIVE_OF_INNER_STATE | 166 |
| DIVINE_HUMAN_PARALLEL | 141 |
| SOMATIC_INNER_LINK | 134 |
| VOLITIONAL_COMPONENT | 80 |
| METAPHOR_ROOT | 79 |
| RELATIONAL_DIRECTION | 62 |
| WISDOM_LITERATURE_CONCENTRATION | 56 |
| GENERATION_RESOLUTION_PAIR | 49 |
| THIN_DATA | 47 |
| ESCHATOLOGICAL_USAGE | 34 |
| BODY_INNER_EXPRESSION | 22 |
| SOMATIC_EXPRESSION | 19 |
| CROSS_PART_ROOT | 17 |
| HIGH_FREQUENCY_ANCHOR | 13 |
| NT_FACULTY_NAMING | 9 |
| SMALL_VERSE_SAMPLE | 5 |
| CROSS_TESTAMENT_SHIFT | 5 |
| MULTI_REGISTRY_ANCHOR | 4 |
| ARAMAIC_FORM | 4 |
| NO_WORD_ANALYSIS | 3 |
| CONSOLIDATION_CANDIDATE | 3 |
| THEOLOGICAL_ANCHOR | 1 |
| DUPLICATE_RESOLVED | 1 |

----------|-------|
| SEMANTIC_RANGE_BREADTH | 180 |
| GOD_AS_SUBJECT | 177 |
| CAUSATIVE_OF_INNER_STATE | 166 |
| DIVINE_HUMAN_PARALLEL | 141 |
| SOMATIC_INNER_LINK | 134 |
| VOLITIONAL_COMPONENT | 80 |
| METAPHOR_ROOT | 79 |
| RELATIONAL_DIRECTION | 62 |
| WISDOM_LITERATURE_CONCENTRATION | 56 |
| GENERATION_RESOLUTION_PAIR | 49 |
| THIN_DATA | 47 |
| ESCHATOLOGICAL_USAGE | 34 |
| BODY_INNER_EXPRESSION | 22 |
| SOMATIC_EXPRESSION | 19 |
| CROSS_PART_ROOT | 17 |
| HIGH_FREQUENCY_ANCHOR | 13 |
| NT_FACULTY_NAMING | 9 |
| SMALL_VERSE_SAMPLE | 5 |
| CROSS_TESTAMENT_SHIFT | 5 |
| MULTI_REGISTRY_ANCHOR | 4 |
| ARAMAIC_FORM | 4 |
| NO_WORD_ANALYSIS | 3 |
| CONSOLIDATION_CANDIDATE | 3 |
| THEOLOGICAL_ANCHOR | 1 |
| DUPLICATE_RESOLVED | 1 |

---

# 4. Columns Requiring Claude AI Action

These fields are either NULL or incomplete and require Claude AI analytical judgement to populate. Claude Code cannot derive these from data alone.

## 4.1 word_registry

| Column | Populated | NULL | Claude AI Action |
|--------|-----------|------|-----------------|
| sb_classification | 2 | 179 | Assign inner being standing classification during Session B extraction |
| sb_classification_reasoning | 0 | 181 | Provide reasoning for non-confirmed classifications |
| session_b_status | 179 | 2 | Updated via patch after analysis completion |
| source_category | 173 | 8 | Repurpose as multi-value dimensions field (v5.1 Section 4.3). Currently single-value. |

## 4.2 wa_term_inventory

| Column | Populated | NULL (active) | Claude AI Action |
|--------|-----------|---------------|-----------------|
| evidential_status | 155 | 6833 | Assign confirmed/plausible/uncertain/instrumental/relational_only during v5.2 extraction |
| retention_note | 53 | 6935 | Provide note for non-confirmed terms explaining retention reasoning |

## 4.3 wa_term_phase2_flags (Claude AI owned)

- 883 OWNER terms have at least one PH2 flag
- 4635 OWNER terms have no PH2 flags
- PH2 flags are set during Session B DataPrep and Analysis — not by Claude Code

## 4.4 wa_session_b_dimensions / wa_session_b_findings

- 2 registries have dimensional profiles (only mind and Soul completed v5.2)
- 20 key findings recorded across those registries
- All other registries at Analysis Complete need v5.2 extraction to populate these tables

---

# 5. Term Sharing Analysis

## 5.1 Distribution

![Cross-Registry Term Analysis](cross_registry_term_analysis_20260328.png)

**Key findings:**
- 2,045 terms are unique to one registry; 1,740 are shared across 2+ registries
- High-bleed particles (ki, asher, al, im) have been delete_flagged — they appeared in 10-18 registries
- Genuine shared terms (chesed, nephesh, kardia) remain active as they carry analytical value across registries

## 5.2 Root Family Analysis

![Cross-Registry Root Analysis](cross_registry_root_analysis_20260328.png)

**Key findings:**
- Root families are much more discriminating than individual terms — 296 of 305 roots are unique to one registry
- Only 19 roots are shared across registries
- Root family data is sparse — only 31 of 181 registries have root records. This is a known gap.

## 5.3 Sharing Ratio Distribution

| Sharing Ratio | Registries |
|--------------|-----------|
| 0% (all unique) | 17 |
| 1-49% shared | 30 |
| 50-79% shared | 54 |
| 80-99% shared | 45 |
| 100% shared | 35 |
| **Total (non-excluded, with terms)** | **181** |

## 5.4 Term Sharing Pools — Natural Groupings

At a threshold of 15+ shared terms, the registries form 8 natural pools of interconnected words. These pools emerge from the data — they are not pre-assigned clusters. Words within a pool share substantial vocabulary and cannot be fully understood in isolation from each other.

| Pool | Size | Words | Pattern |
|------|------|-------|---------|
| **Pool 1** | 51 words | anger, desire, trust, faith, hope, heart, spirit, mind, Soul, will, purpose, thought, love, kindness, strength, power, authority, dominion, courage, generosity, delight, covenant, joy, conscience, guilt, repentance, sin, wisdom, knowledge, understanding, meditation, division, goodness, praise, insight, recognition, slander, lust, craving, despair, doubt, faithfulness, transformation, resentment, likeness, pray, ambition, dignity, discernment, wrath, might | Core inner-being megapool — everything connects through shared Hebrew/Greek vocabulary |
| **Pool 2** | 11 words | agony, anguish, awe, distress, dread, experience, fear, grief, reverence, sorrow, terror | Suffering/fear cluster — tightly interconnected through shared pain and dread vocabulary |
| **Pool 3** | 3 words | envy, jealousy, zeal | Tight triad sharing the Hebrew qana root family |
| **Pool 4** | 2 words | compassion, mercy | chesed/racham family |
| **Pool 5** | 2 words | justice, righteousness | tsedeq family |
| **Pool 6** | 2 words | shame, contempt | Shared dishonour vocabulary |
| **Pool 7** | 2 words | surrender, flesh | Shared submission/body vocabulary |
| **Pool 8** | 2 words | consecration, holiness | qodesh family |
| **Unconnected** | 47 words | | Not connected to any other registry at the 15-term threshold |

**Analytical implications:**

- **Pool 1 is the core challenge.** 51 words forming a single interconnected network. The existing cluster assignments (C01-C22) are the programme's strategy for breaking this megapool into manageable analysis batches.
- **Pool 2 is a natural analysis unit.** 11 suffering/fear words sharing vocabulary internally with limited external connections. Already spread across C05 and C06.
- **Pools 3-8 are the simplest shared-word analyses.** Each is 2-3 words sharing a specific root family. Can be analysed together in a single session.
- **The top 5 strongest pairwise connections** (anguish-distress 79, sorrow-anguish 70, sorrow-distress 66, sorrow-grief 56, wrath-anger 51) are all within Pool 2 or within obvious semantic families — confirming pools reflect genuine semantic structure.

## 5.5 Pool 1 Deep Dive — Sub-Structure of the 51-Word Megapool

At threshold 30+ shared terms, Pool 1 fragments into 6 sub-pools and 41 isolates:

### Sub-pools (strong internal bonds, 30+ shared terms)

| Sub-pool | Words | Semantic axis |
|----------|-------|--------------|
| **Volitional core** (9) | desire, faith, guilt, hope, purpose, thought, trust, will, pray | The will/intention/belief axis — strongest interconnection in the programme |
| **Power axis** (5) | courage, strength, power, authority, dominion | Physical/spiritual capacity vocabulary |
| **Heart-spirit** (2) | heart, spirit | The two primary inner-being seats (41 shared terms) |
| **Wisdom pair** (2) | goodness, meditation | Moral/contemplative vocabulary (30 shared terms) |
| **Love pair** (2) | kindness, love | chesed family (33 shared terms) |
| **Anger pair** (2) | anger, wrath | Rage vocabulary (51 shared terms — strongest pair in programme) |

### Isolates (41 words) — Gravitational Analysis

Each isolate is connected to Pool 1 at 15-29 shared terms but not at 30+. Their strongest connection reveals which sub-pool they gravitate toward:

**Gravitate toward purpose/thought axis:**
- might (27 shared with purpose), delight (26), mind (23), recognition (23), knowledge (21)

**Gravitate toward trust/faith axis:**
- faithfulness (28 shared with faith), despair (18 shared with trust), doubt (17), covenant (15), sorrow (13)
- The faith/trust/hope triad pulls in its opposite (despair, doubt) and its relational expression (covenant)

**Gravitate toward heart/spirit centre:**
- conscience (26 shared with heart), Soul (24 shared with heart and spirit)

**Gravitate toward love/kindness axis:**
- ambition (26 shared with love), compassion (13), devotion (6), worth (11 shared with kindness)

**Gravitate toward strength/power axis:**
- generosity (22 shared with strength), appetite (11), weakness (8)

**Gravitate toward desire axis:**
- craving (23 shared with desire), lust (18), covetousness (9), flesh (9)

**Gravitate toward wisdom axis:**
- wisdom (23 shared with insight), understanding (22), discernment (21)

**Other gravitational links:**
- envy/zeal (21 each — mutual pair), repentance/transformation/likeness (15-16 mutual — renewal vocabulary)
- joy (16 with delight), reasoning (12 with pray), sin (16 with guilt), resentment (15 with anger)
- praise (19 with power), slander (18 with might), malice (9 with sorrow)
- condemnation (1 with thought — near-isolate), contentment (5 with hope — near-isolate)

### Analytical implications for analysis ordering

1. **The Volitional Core (9 words)** should be analysed as a group or in close sequence — they are too interconnected to analyse independently.

2. **Natural analysis batches emerging from gravitational patterns:**
   - Wisdom sub-group: discernment, insight, understanding, wisdom, knowledge (all C02)
   - Desire sub-group: desire, craving, lust, appetite, covetousness, flesh
   - Trust sub-group: trust, faith, hope, faithfulness, despair, doubt, covenant
   - Love sub-group: love, kindness, compassion, mercy, devotion, worth
   - Power sub-group: strength, power, authority, dominion, courage, might, generosity

3. **Near-isolates** (condemnation with 1 connection, contentment with 5) could be analysed with the not-shared words — their cross-registry dependence is minimal.



---

# 6. Cluster Status

| Cluster | Total | Complete | Not Started | Excluded | Maturity |
|---------|-------|----------|-------------|----------|----------|
| C01 | 6 | 6 | 0 | 0 | 100% |
| C02 | 13 | 2 | 1 | 0 | 15% |
| C03 | 9 | 2 | 0 | 0 | 22% |
| C04 | 7 | 2 | 0 | 0 | 28% |
| C05 | 9 | 1 | 0 | 0 | 11% |
| C06 | 8 | 3 | 1 | 1 | 42% |
| C07 | 10 | 2 | 1 | 1 | 22% |
| C08 | 11 | 2 | 0 | 0 | 18% |
| C09 | 10 | 0 | 3 | 3 | 0% |
| C10 | 11 | 0 | 1 | 1 | 0% |
| C11 | 10 | 0 | 0 | 0 | 0% |
| C12 | 10 | 0 | 0 | 0 | 0% |
| C13 | 9 | 4 | 1 | 1 | 50% |
| C14 | 10 | 1 | 3 | 3 | 14% |
| C15 | 9 | 3 | 0 | 0 | 33% |
| C16 | 10 | 0 | 0 | 0 | 0% |
| C17 | 11 | 5 | 1 | 1 | 50% |
| C18 | 7 | 0 | 2 | 2 | 0% |
| C19 | 11 | 0 | 4 | 4 | 0% |
| C20 | 7 | 2 | 2 | 1 | 33% |
| C21 | 8 | 0 | 4 | 4 | 0% |
| C22 | 16 | 0 | 9 | 9 | 0% |

---

# 7. Not-Shared Words — Priority for Independent Analysis

These 17 registries have `term_sharing_ratio = 0.0` — every term is unique to this word. They can be analysed completely independently with no cross-registry verse overlap. These are the recommended starting point for the next batch of Session B analyses.

| No | Word | Cluster | Terms | Verses | Session B Status |
|----|------|---------|-------|--------|-----------------|
| 69 | gratitude | C03 | 3 | 54 | Ready for Analysis |
| 125 | purity | C10 | 12 | 206 | Ready for Analysis |
| 164 | truthfulness | C10 | 5 | 161 | Ready for Analysis |
| 81 | hypocrisy | C11 | 5 | 31 | Ready for Analysis |
| 120 | perverseness | C11 | 16 | 146 | Ready for Analysis |
| 41 | defilement | C12 | 2 | 4 | Ready for Analysis |
| 17 | bondage | C14 | 8 | 158 | Ready for Analysis |
| 114 | obedience | C14 | 2 | 16 | Ready for Analysis |
| 155 | submission | C14 | 2 | 36 | Ready for Analysis |
| 150 | sorcery | C16 | 5 | 15 | Ready for Analysis |
| 62 | fellowship | C17 | 2 | 27 | Ready for Analysis |
| 64 | forgiveness | C17 | 7 | 190 | Ready for Analysis |
| 130 | reconciliation | C17 | 2 | 9 | Ready for Analysis |
| 131 | rejection | C18 | 3 | 5 | Ready for Analysis |
| 167 | unity | C18 | 7 | 562 | Ready for Analysis |
| 210 | deadness | C21 | 13 | 789 | Ready for Analysis |
| 20 | character | C22 | 4 | 36 | Ready for Analysis |
| **Total** | **17 words** | | **98** | **2445** | |

### Recommended batching for analysis:

These 17 words span 12 different clusters. For Session B analysis, they can be batched by cluster proximity:

- **Batch 1**: gratitude (69), purity (125), truthfulness (164), hypocrisy (81), perverseness (120)
- **Batch 2**: defilement (41), bondage (17), obedience (114), submission (155), sorcery (150)
- **Batch 3**: fellowship (62), forgiveness (64), reconciliation (130), rejection (131), unity (167)
- **Batch 4**: deadness (210), character (20)

---

# 8. Small Clusters — Next Priority After Not-Shared Words

After the not-shared words, the next simplest registries are those in clusters with only 2 active (non-excluded) words. These have limited cross-registry complexity.

No clusters with 3 or fewer active words.

---

# 9. Data Integrity Notes

- **71 terms** have raw `meaning` text but no `parsed_meaning_id` — meaning parser migration incomplete
- **315 terms** flagged as CONCRETE_PHYSICAL — retained for verse analysis, flagged as unlikely inner-being vocabulary
- **0 verses** have NULL span_strong_match — pre-v9 records, could be backfilled with STEP re-query
- **Root family data** populated for 31 of 181 registries — sparse coverage, planned for future backfill
- **source_category -> dimensions rename** pending (schema migration M17). Currently writing multi-value dimensions to source_category field.

---

# 10. Housekeeping Completed This Session

| Action | Impact |
|--------|--------|
| Particle terms delete_flagged (ki, asher, al, im + 5 more) | 113 terms, 20,665 verses removed from active set |
| mti_status=delete synced to term_inventory | 130 terms, 7,100 verses flagged |
| Orphan verse cleanup (under delete_flagged terms) | 1,288 verses flagged |
| XREF verses delete_flagged | 59,120 verses removed from active set |
| CONCRETE_PHYSICAL quality flag created | 315 terms flagged (not excluded, queryable filter) |
| term_owner_type added to wa_term_inventory | 5,518 OWNER + 1,470 XREF populated |
| testament NULLs fixed | 495 records corrected |
| VTL backfill | 33,335 wa_verse_term_links records created — 100% coverage |
| Sharing ratio added to word_registry | unique_term_count, shared_term_count, term_sharing_ratio populated |
| 140 registries extracted + audited | STEP data pulled, audit_word run, JSON exports produced |

### Net effect on active dataset:

| Metric | Before | After | Reduction |
|--------|--------|-------|-----------|
| Active terms | 7,233 | 6988 | 245 |
| Active verses | 221,357 | 133353 | 88004 (40%) |
