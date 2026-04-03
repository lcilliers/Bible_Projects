# Framework B — Soul Word Analysis Programme

# Registry Management Guide

**Version 5.5 | March 2026 | Reference guide — not an operational instruction**

| **Document** | **Value** |
| --- | --- |
| Filename | WA-Registry-Management-Guide-v5.6-20260330.md |
| Supersedes | WA-Registry-Management-Guide-v5.5-20260329.md |
| Purpose | Terminology, structure, maintenance, and periodic review of the word registry |
| Audience | Researcher and both AI systems — reference when questions arise about registry meaning, state, or structure |
| Not covered | Transactional operations — see WA-VerseContext-Instruction-v1.2 and WA-SessionB-DataPrep-Instruction-v5.4 |

**Change Control — v5.6**

| **Change** | **Detail** |
| --- | --- |
| Section 2 | Engine-derived fields note added to phase1_term_count, phase1_verse_count, unique_term_count, shared_term_count, term_sharing_ratio: these reflect Phase 1 state only and are not updated by the Session B pipeline |

---

## 1. What the Registry Is

The word registry (`word_registry` table in `bible_research.db`) is the master list of all words in the Framework B Soul Word Analysis Programme. It defines the scope of the research — every word that has been or will be analysed through Sessions A, B, and D is registered here.

The registry is not a classification system. It is a scope instrument.

> **Total registry size: 212 words.** This includes words whose Phase 1 status is Excluded.

---

## 2. Registry Fields — Meaning and Use

| **Field** | **Meaning and use** |
| --- | --- |
| id | Internal database primary key. Not displayed. |
| no | Registry number — the human-readable identifier. Used in all file naming and cross-references. |
| word | The English word label for this registry. Not a translation — a programme label. |
| source_list | How this word entered the registry: High Confidence │ Low Confidence / Inferred │ Missing Inner Being Words │ Programme Addition |
| category_hint | Broad semantic category as a navigational aid. Not analytical classification. |
| phase1_status | Whether Phase 1 extraction is complete: Complete │ Excluded │ In Progress |
| phase1_term_count | Number of terms extracted in Phase 1. **Engine-derived — Phase 1 state only. Not updated by Session B pipeline.** |
| phase1_verse_count | Number of verses in the Phase 1 extract. **Engine-derived — Phase 1 state only. Not updated by Session B pipeline.** |
| session_b_status | Current Session B pipeline progress. Values: NULL │ Verse Context Reset │ Ready for Analysis │ Pre-Analysis Complete │ Analysis Complete │ Session B Complete |
| verse_context_status | Verse Context completion state. Set by Claude Code. Values: NULL │ In Progress │ Complete. See Section 3. |
| origin | original_list │ programme_addition |
| dimensions | Multi-value semantic category field (formerly source_category, renamed M17). Comma-delimited. Populated at Session B extraction. Valid values in WA-Reference Section 4.3. |
| notes | Free text notes about this registry. |
| cluster_assignment | Cluster this word belongs to. Format: C01–C22. |
| sb_classification | Inner being standing classification from Session B. |
| sb_classification_reasoning | Reasoning for non-confirmed classifications. |
| carry_forward | Whether this word carries to Session D: 1 / 0. |
| unique_term_count | Terms unique to this registry. **Engine-derived — Phase 1 state only. Not updated by Session B pipeline. Use live query against wa_term_inventory for current counts.** |
| shared_term_count | Terms shared with other registries. **Engine-derived — Phase 1 state only. Not updated by Session B pipeline. Use live query for current counts.** |
| term_sharing_ratio | 0.0 (all unique) to 1.0 (all shared). **Engine-derived — Phase 1 state only. Not updated by Session B pipeline.** |

Note: `anchor_verses` field was removed in migration M17 (2026-03-29). It is superseded by the `verse_context` anchor mechanism at term level.

---

## 3. Registry Status Lifecycle

Every word moves through two parallel status tracks:

### 3.1 `session_b_status` — Session B pipeline track

| **Status** | **What it means** |
| --- | --- |
| NULL | Phase 1 excluded or not yet audited. No Session B work started. |
| Verse Context Reset | Prior Session B work exists but has been superseded — registry must reprocess through Verse Context and pool-based Session B. Existing analytical documents are parked but not deleted. |
| Ready for Analysis | Verse Context complete AND term inventory classified and clean. Ready for Session B DataPrep. |
| Pre-Analysis Complete | Pre-analysis patch applied. Term classifications in database. |
| Analysis Complete | Session B narrative complete. Analysis patch applied. |
| Session B Complete | Full Session B cycle complete — narrative, JSON, patches, final extract, sdpointers. |

### 3.2 `verse_context_status` — Verse Context track

| **Status** | **What it means** |
| --- | --- |
| NULL | Phase 1 excluded or zero-term registry — outside Verse Context scope. |
| In Progress | Verse Context work pending or underway. OWNER terms have not all been classified yet. |
| Complete | All OWNER terms with verses have verse_context records. Registry may proceed to DataPrep. |

### 3.3 Full pipeline sequence

```
Phase 1 complete
      │
      ▼
verse_context_status: In Progress
session_b_status: Verse Context Reset (or NULL)
      │
      ▼  (Verse Context batches run — all OWNER terms classified)
verse_context_status: Complete
      │
      ▼  (Claude Code advances session_b_status)
session_b_status: Ready for Analysis
      │
      ▼  (Pre-analysis patch applied)
session_b_status: Pre-Analysis Complete
      │
      ▼  (Session B analysis patch applied)
session_b_status: Analysis Complete
      │
      ▼  (Full Session B cycle complete)
session_b_status: Session B Complete
```

> ⚠ **`Ready for Analysis` is only reachable when `verse_context_status = Complete`. DataPrep must not begin unless both conditions are met.**

---

## 4. The 212-Word Scope

The programme scope is 212 words. Current state (post-setup, 2026-03-29):
- 181 active registries — `session_b_status = Verse Context Reset`, `verse_context_status = In Progress`
- 31 excluded registries — Phase 1 Excluded, zero terms, outside Verse Context scope
- Total active OWNER terms: 5,518 | Active verses: 133,353

---

## 5. Cluster Assignments

Clusters are the programme's organisational entity for Session B processing and Session D preparation. They remain unchanged.

### 5.1 Cluster Principles

- Maximum approximately 10 words per cluster
- Clusters group words with broad semantic synergy
- Not an analytical classification — a management tool
- Clusters drive Session D generation when they reach maturity

### 5.2 Processing Sequence — Pool-Based

Within the cluster structure, the term sharing pools from the programme analysis (March 2026) define the processing sequence for Stage 2 (Session B Analysis). This sequence optimises for early throughput and builds cross-word context progressively.

**Stage 1 — Verse Context sweep (current priority)**
Run Verse Context across all OWNER terms in term-based batches until all 5,518 terms are classified. No cluster ordering — pure term throughput.

**Stage 2 — Session B Analysis in pool/cluster batches**

| **Order** | **Type** | **Words** | **Notes** |
| --- | --- | --- | --- |
| 1 | Independent | 17 not-shared words (term_sharing_ratio = 0) | Zero XREF complexity — any order |
| 2 | Near-independent | 47 unconnected words (below 15-term threshold) | Group by cluster |
| 3 | Pool 2 | 11 suffering/fear words | Single simultaneous batch |
| 4 | Pool 3 | envy, jealousy, zeal | Single session |
| 5 | Pool 4 | compassion, mercy | Single session |
| 6 | Pool 5 | justice, righteousness | Single session |
| 7 | Pool 6 | shame, contempt | Single session |
| 8 | Pool 7 | surrender, flesh | Single session |
| 9 | Pool 8 | consecration, holiness | Single session |
| 10 | Pool 1 — Anger pair | anger, wrath | 51 shared terms |
| 11 | Pool 1 — Love pair | kindness, love | 33 shared terms |
| 12 | Pool 1 — Heart-spirit | heart, spirit | 41 shared terms |
| 13 | Pool 1 — Wisdom pair | goodness, meditation | 30 shared terms |
| 14 | Pool 1 — Power axis | courage, strength, power, authority, dominion | ~25 avg shared |
| 15 | Pool 1 — Volitional Core | desire, faith, guilt, hope, purpose, thought, trust, will, pray | Most complex — 9 words |
| 16 | Pool 1 — Isolates | 41 words grouped by gravitational attractor | After attractor sub-pool |

### 5.3 Cluster Status

| **Status** | **Meaning** |
| --- | --- |
| not started | No words in cluster at Session B Complete |
| in progress | At least one word at Session B Complete, cluster not finished |
| extraction ready | All words at Analysis Complete |
| complete | All words at Session B Complete — Session D may be triggered |

### 5.4 Current Cluster Assignments

As of 2026-03-29. All active registries reset to Verse Context Reset pending Stage 1 completion.

| **Cluster** | **Words (registry no — word)** |
| --- | --- |
| C01 | 112 mind, 182 Soul, 183 heart, 184 spirit, 185 flesh, 211 being |
| C02 | 32 counsel, 49 discernment, 85 imagination, 91 insight, 93 intention, 100 knowledge, 108 meditation, 110 memory, 126 purpose, 127 reasoning, 160 thought, 166 understanding, 174 wisdom |
| C03 | 11 awe, 29 contentment, 42 delight, 69 gratitude, 97 joy, 132 rejoicing, 175 wonder, 186 gladness, 192 comfort |
| C04 | 8 appetite, 43 desire, 78 hope, 102 longing, 115 passion, 179 yearning, 193 craving |
| C05 | 2 agony, 5 anguish, 18 brokenness, 51 distress, 71 grief, 72 groaning, 113 mourning, 151 sorrow, 188 weeping |
| C06 | 7 anxiety, 44 despair, 53 dread, 61 fear, 79 hopelessness†, 146 shame, 158 terror, 190 contempt |
| C07 | 4 anger, 13 bitterness, 56 envy, 75 hatred, 87 indignation, 96 jealousy, 136 resentment†, 178 wrath, 181 zeal, 205 resentment |
| C08 | 16 boldness, 33 courage, 46 devotion, 48 diligence, 55 endurance, 65 generosity, 66 gentleness, 80 humility, 109 meekness, 116 patience, 142 self-control |
| C09 | 15 boastfulness, 36 cowardice†, 74 hardness, 101 laziness†, 123 pride, 128 rebellion, 133 reliability†, 153 stubbornness, 170 weakness, 208 sloth |
| C10 | 14 blamelessness†, 60 faithfulness, 67 goodness, 77 honesty, 90 innocence, 92 integrity, 125 purity, 139 righteousness, 148 sincerity, 164 truthfulness, 168 uprightness |
| C11 | 31 corruption, 40 deceit, 57 evil, 81 hypocrisy, 89 iniquity, 120 perverseness, 147 sin, 162 transgression, 172 wickedness, 203 treachery |
| C12 | 1 abomination, 39 debauchery, 41 defilement, 86 impurity, 105 lust, 144 sensuality, 149 slander, 157 temptation, 171 whoredom, 189 malice |
| C13 | 24 condemnation, 26 conscience, 30 contrition†, 35 covetousness, 50 disobedience, 70 greed, 73 guilt, 98 justice, 135 repentance |
| C14 | 17 bondage, 21 commitment†, 25 conformity†, 45 determination†, 114 obedience, 137 resolve, 155 submission, 156 surrender, 173 will, 180 yielding |
| C15 | 59 faith, 94 intercession, 121 praise, 122 prayer, 138 reverence, 140 seeking, 163 trust, 176 worship, 212 pray |
| C16 | 6 anointing, 28 consecration, 76 holiness, 83 idolatry, 124 prophecy, 150 sorcery, 159 testimony, 165 unbelief, 191 doubt, 194 blessing |
| C17 | 22 communion†, 23 compassion, 34 covenant, 62 fellowship, 64 forgiveness, 68 grace, 99 kindness, 103 love, 111 mercy, 117 peace, 130 reconciliation |
| C18 | 12 betrayal†, 52 division, 104 loyalty, 106 manipulation†, 131 rejection, 152 strife, 167 unity |
| C19 | 19 calling, 47 dignity, 82 identity†, 84 image of God†, 107 meaning, 119 personhood†, 141 self-awareness†, 177 worth, 201 image, 204 name, 209 likeness |
| C20 | 187 strength, 195 spiritual powers†, 196 power, 197 authority, 198 might, 199 dominion, 200 energy |
| C21 | 37 darkening†, 38 deadness†, 134 renewal, 154 stupor†, 161 transformation†, 202 transformation, 207 blindness (spiritual), 210 deadness |
| C22 | 3 ambition, 9 assent†, 10 awareness†, 20 character, 27 consciousness, 54 emotion†, 58 experience, 63 foolishness, 88 ingratitude†, 95 intuition†, 118 personality†, 129 recognition, 143 sensitivity†, 145 sexuality†, 169 vulnerability†, 206 vulnerability |

**Key:** † = Phase 1 Excluded

---

## 6. Reading Programme State

### 6.1 Session B Progress by Status
```sql
SELECT session_b_status, COUNT(*) as count
FROM word_registry
GROUP BY session_b_status
ORDER BY session_b_status;
```

### 6.2 Words Ready for DataPrep
```sql
SELECT no, word
FROM word_registry
WHERE session_b_status = 'Ready for Analysis'
ORDER BY no;
```

### 6.3 Words Not Yet Started
```sql
SELECT no, word, phase1_status
FROM word_registry
WHERE session_b_status IS NULL
ORDER BY no;
```

### 6.4 Zero-Term Registries
```sql
SELECT no, word
FROM word_registry
WHERE phase1_term_count = 0 OR phase1_term_count IS NULL
ORDER BY no;
```

### 6.5 Cluster Progress
```sql
SELECT cluster_assignment,
  COUNT(*) as total,
  SUM(CASE WHEN session_b_status = 'Session B Complete' THEN 1 ELSE 0 END) as complete
FROM word_registry
GROUP BY cluster_assignment;
```

### 6.6 Not-Shared Words (term_sharing_ratio = 0)
```sql
SELECT no, word, cluster_assignment, unique_term_count, phase1_verse_count, verse_context_status
FROM word_registry
WHERE term_sharing_ratio = 0.0
  AND phase1_status != 'Excluded'
  AND phase1_term_count > 0
ORDER BY no;
```

### 6.7 Ownership Distribution
```sql
SELECT term_owner_type, COUNT(*) as terms
FROM wa_term_inventory
WHERE delete_flagged = 0
GROUP BY term_owner_type;
```

### 6.8 Verse Context Stage Monitoring
```sql
-- Progress by verse_context_status
SELECT verse_context_status, COUNT(*) as count
FROM word_registry
GROUP BY verse_context_status;

-- Registries where Verse Context is complete and DataPrep can begin
SELECT no, word, cluster_assignment
FROM word_registry
WHERE verse_context_status = 'Complete'
  AND session_b_status != 'Ready for Analysis'
ORDER BY no;
```

### 6.9 Pool Processing Readiness (Stage 2)
```sql
-- Not-shared words ready for independent Session B
SELECT no, word, cluster_assignment, verse_context_status
FROM word_registry
WHERE term_sharing_ratio = 0.0
  AND phase1_status = 'Complete'
  AND phase1_term_count > 0
  AND verse_context_status = 'Complete'
ORDER BY no;
```

---

## 7. Periodic Review Protocol

Review approximately every 25 completed Session B analyses. Additional review trigger: when Stage 1 (Verse Context sweep) is complete across all active registries.

### 7.1 What a Periodic Review Covers

- Programme state snapshot (both status tracks)
- Verse Context completion progress
- Stage 2 pool batch readiness
- Cluster progress toward Session D triggers
- Zero-term registry status
- Registry anomalies

### 7.2 What a Periodic Review Does Not Do

- Remove words from the registry
- Reclassify completed analyses
- Make synthesis claims

---

## 7a. Pool ID Controlled Vocabulary

Pool IDs are used in pool analysis dataset filenames (`wa-pool-{pool_id}-analysis-{date}.json`) and in Session B Analysis, Extraction, and DataPrep output references. The pool_id must be agreed between researcher and Claude Code before pool dataset construction begins.

| **pool_id** | **Words** | **Processing notes** |
| --- | --- | --- |
| not-shared | 17 words with term_sharing_ratio = 0 | Analysed independently, one word per session |
| unconnected | 47 words with minimal sharing (below 15-term threshold) | Near-independent, group by cluster |
| pool2-suffering | 11 suffering/fear words | Single simultaneous batch |
| pool3-zeal | envy, jealousy, zeal | qana root — single session |
| pool4-mercy | compassion, mercy | chesed/racham — single session |
| pool5-justice | justice, righteousness | tsedeq — single session |
| pool6-shame | shame, contempt | dishonour vocab — single session |
| pool7-surrender | surrender, flesh | submission vocab — single session |
| pool8-holiness | consecration, holiness | qodesh — single session |
| pool1-anger-pair | anger, wrath | 51 shared terms — sub-pool 1 |
| pool1-love-pair | kindness, love | 33 shared terms — sub-pool 2 |
| pool1-heart-spirit | heart, spirit | 41 shared terms — sub-pool 3 |
| pool1-wisdom-pair | goodness, meditation | 30 shared terms — sub-pool 4 |
| pool1-power-axis | courage, strength, power, authority, dominion | sub-pool 5 |
| pool1-volitional | desire, faith, guilt, hope, purpose, thought, trust, will, pray | 9 words — sub-pool 6 |
| pool1-isolates | 41 isolate words grouped by gravitational attractor | After their attractor sub-pool |

For not-shared and unconnected words, pool_id may be set to the registry number and word label: e.g. `069-gratitude` for a single-word independent analysis.

---

## 8. Terminology Reference

| **Term** | **Definition** |
| --- | --- |
| Registry | A single word and its full analytical record. |
| Registry number (no) | Integer identifier for a registry. Used in all file naming. |
| Verse Context | The pipeline stage preceding Session B that classifies all verses for all OWNER terms against a governing inner-being relevance filter, groups them by contextual meaning, and designates anchor verses. |
| Anchor verse | The programme's canonical reference verse for a specific contextual meaning group of a term. Serves as Session B Analysis input and programme citation. Every term must have at least one. See WA-Reference Section 16. |
| Contextual meaning group | A set of verses for a term where the term functions in the same way in relation to the inner being, described by a single `context_description`. Stored in `verse_context_group`. |
| Pool | A set of registries connected through shared XREF terms at or above a defined threshold. The 8 pools identified in the March 2026 programme analysis define the Stage 2 processing sequence. Not a database table — a planning tool. |
| Pool/cluster batch | A set of words analysed simultaneously in Session B because they share XREF terms. The shared terms' verse context is already classified — cross-word relationships are visible in a single analysis session. |
| Pool analysis dataset | The JSON input for Session B Analysis. Contains all words in the pool batch, their OWNER term anchor verses grouped by contextual meaning, and XREF term profiles from OWNER registries. File naming: wa-pool-{pool_id}-analysis-{date}.json. |
| Session B | The verse-grounded word analysis phase. Now operates on pool/cluster batches, not isolated words. |
| Session D | Cross-programme synthesis — cross-pool interoperability and conceptual dynamics. Not yet underway. |
| MTI (Master Term Inventory) | `mti_terms` — one record per Strong's number, programme-wide. |
| OWNER term | `term_owner_type = OWNER` in `wa_term_inventory` — primary analytical home for this Strong's number. Verses active. |
| XREF term | `term_owner_type = XREF` — cross-reference copy. Verses delete_flagged. Verse context derived from OWNER. |
| Verse Context Reset | A `session_b_status` value indicating prior Session B work exists but is superseded. Registry must reprocess through Verse Context and pool-based Session B. |
| Cluster | Organisational grouping for Session B processing. 22 clusters, C01–C22. Not an analytical classification. |
| Patch | JSON file of database operations submitted to Claude Code. |
| PH2 flag | Research flag in `wa_session_research_flags`. |
| Conceptual Word Register | Supplementary register of modern inner-life concepts without direct biblical lexical equivalent. Session D construct. |

---

## 9. File Naming Reference

| **Scope token** | **File type** |
| --- | --- |
| analysis | Session B narrative — wa-{nnn}-{word}-analysis-{date}.docx |
| extract | Word JSON export — wa-{nnn}-{word}-extract-{date}.json |
| json | Session B structured JSON — wa-{nnn}-{word}-json-{date}.json |
| patch | Word-level patch file — wa-{nnn}-{word}-patch-{date}.json |
| final | Final registry extract — wa-{nnn}-{word}-final-{date}.json |
| sdpointers | Session D pointers — wa-{nnn}-{word}-sdpointers-{date}.json |
| vcb-extract | Verse Context batch input — wa-vcb-{batch_id}-extract-{date}.json |
| vcb-patch | Verse Context batch patch — wa-vcb-{batch_id}-patch-{date}.json |
| pool-analysis | Pool analysis dataset — wa-pool-{pool_id}-analysis-{date}.json |

---

*WA-Registry-Management-Guide-v5.6 | 20260330 | Supersedes v5.5-20260329 | Section 2: engine-derived fields note added to phase1_term_count, phase1_verse_count, unique_term_count, shared_term_count, term_sharing_ratio*
