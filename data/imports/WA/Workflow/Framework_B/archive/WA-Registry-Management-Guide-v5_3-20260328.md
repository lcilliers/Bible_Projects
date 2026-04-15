# Framework B — Soul Word Analysis Programme

# Registry Management Guide

**Version 5.3  |  March 2026  |  Reference guide — not an operational instruction**

| **Document** | **Value** |
| --- | --- |
| Filename | WA-Registry-Management-Guide-v5.3-20260328.docx |
| Supersedes | WA-Registry-Management-Guide-v5.2-20260327.docx |
| Purpose | Terminology, structure, maintenance, and periodic review of the word registry |
| Audience | Researcher and both AI systems — reference when questions arise about registry meaning, state, or structure |
| Not covered | Transactional operations — see WA-Implementation-Instruction-v5 |

---

## 1. What the Registry Is

The word registry (`word_registry` table in `bible_research.db`) is the master list of all words in the Framework B Soul Word Analysis Programme. It defines the scope of the research — every word that has been or will be analysed through Sessions A, B, and D is registered here.

The registry is not a classification system. It is a scope instrument. A word is in the registry because it has a plausible connection to the inner being of the human person as defined in the programme. The registry does not claim that every word in it is equally significant or equally well evidenced — those distinctions are made during Session B analysis.

> **Total registry size: 212 words.** This includes words whose Phase 1 status is Excluded — excluded words still receive a Session B treatment to document why they were excluded.

---

## 2. Registry Fields — Meaning and Use

| **Field** | **Meaning and use** |
| --- | --- |
| id | Internal database primary key. Not displayed. |
| no | Registry number — the human-readable identifier. Used in all file naming and cross-references. Format: integer, e.g. 97. |
| word | The English word label for this registry. Not a translation — a programme label identifying the semantic domain being investigated. |
| source_list | How this word entered the registry: High Confidence │ Low Confidence / Inferred │ Missing Inner Being Words │ Programme Addition |
| category_hint | Broad semantic category as a navigational aid. Not analytical classification. Values: see WA-Reference-v5. |
| phase1_status | Whether Phase 1 extraction is complete: Complete │ Excluded │ In Progress |
| phase1_term_count | Number of terms extracted in Phase 1. |
| phase1_verse_count | Number of verses in the Phase 1 extract. |
| session_b_status | Current Session B progress. Governs what work can be done. Values: NULL │ Ready for Analysis │ Pre-Analysis Complete │ Analysis Complete │ Session B Complete |
| origin | Whether the word was in the original list or added during the programme: original_list │ programme_addition |
| source_category | Semantic category. Values: see WA-Reference-v5. |
| notes | Free text notes about this registry — anomalies, researcher observations, decisions. |
| anchor_verses | Key verses identified as particularly significant for this word. |
| cluster_assignment | Cluster this word belongs to. Format: C01, C02, etc. See Section 5. |
| sb_classification | Inner being standing classification from Session B analysis: confirmed_characteristic / plausible / uncertain / instrumental / relational_only |
| sb_classification_reasoning | Reasoning for non-confirmed classifications. NULL for confirmed. |
| carry_forward | Whether this word carries forward to Session D: 1 (yes) / 0 (no). Default 1. |
| unique_term_count | Number of terms unique to this registry (not shared with any other word). Engine-derived. |
| shared_term_count | Number of terms that also appear in other registries. Engine-derived. |
| term_sharing_ratio | Proportion of shared terms: 0.0 (all unique) to 1.0 (all shared). Engine-derived. |

---

## 3. Registry Status Lifecycle

Every word in the registry moves through a defined status lifecycle. Understanding this lifecycle is essential for programme management.

| **Status** | **What it means** |
| --- | --- |
| NULL (absent) | Phase 1 complete or in progress. No Session B work has started. This is the starting state for all registries. |
| Ready for Analysis | Data preparation has been run. Term inventory is classified and clean. Ready for Session B analysis chat. |
| Pre-Analysis Complete | Pre-analysis patch applied. Term classifications are in the database. Analysis can proceed. |
| Analysis Complete | Session B narrative analysis is complete. Analysis patch applied. The Session B JSON has been extracted and the analysis report is produced. |
| Session B Complete | Full Session B cycle complete — analysis done, JSON extracted, patches applied. |

> ⚠ **`session_b_status` governs which operations are permitted on a registry. Attempting data preparation on a registry at Pre-Analysis Complete or higher will be rejected. Always check status before starting any session.**

---

## 4. The 212-Word Scope

The programme scope is 212 words. This number includes:

- Words with Phase 1 status **Complete** — full term extraction done, ready for Session B
- Words with Phase 1 status **Excluded** — excluded from Phase 1 extraction but still require Session B documentation of the exclusion reasoning
- Words with Phase 1 status **In Progress** — extraction underway
- **Zero-term registries** — 13 registries currently showing no terms (ambition, consciousness, distress, meekness, pride, resolve, sensuality, sorrow, wisdom, wrath, energy, resentment, being). Several are likely data linkage issues, not genuine gaps. Require investigation.

> Excluded words receive Session B treatment because exclusion reasoning must be documented. A word may be excluded from Phase 1 extraction (no Hebrew/Greek terms extracted) but the Session B document records why it was excluded and whether it should be carried forward to Session D as a Conceptual Word Register entry.

---

## 5. Cluster Assignments

Cluster assignments group registry words into logical batches for Session B processing and Session D preparation. Clusters are a programme management tool, not an analytical classification.

### 5.1 Cluster Principles

- Maximum approximately 10 words per cluster
- Clusters are formed on the basis of broad semantic synergy — words that will be more productive to analyse in proximity to each other
- Clusters are not named in ways that imply classification or theoretical commitment
- Unknown and multi-dimensional are valid cluster assignments — not edge cases to be minimised
- Clusters drive Session D JSON generation — Session D discovery runs are triggered when a cluster reaches maturity (researcher-declared)

### 5.2 Cluster Status

| **Cluster status** | **Meaning** |
| --- | --- |
| unassigned | Word has not yet been assigned to a cluster. Default state. |
| assigned:{label} | Word assigned to a named cluster. Label is a neutral identifier, not a classification. |
| in progress | Session B work has started on one or more words in the cluster but the cluster is not yet complete. |
| complete | All words in this cluster have reached Session B Complete status. Session D discovery run may be triggered. |

### 5.3 The Clustering Run

All 212 words have been assigned to clusters. Cluster assignments are recorded in the `word_registry` table and reflected in the registry overview export. Session B analysis is prioritised by cluster — complete one cluster before moving to the next.

### 5.4 Current Cluster Assignments and Status

Sourced from `wa-registry-overview-20260327.json`. Status is as of 2026-03-27.

| **Cluster** | **Status** | **Maturity** | **Words (registry no — word)** |
| --- | --- | --- | --- |
| C01 | complete | 100% | 112 mind, 182 Soul, 183 heart, 184 spirit, 185 flesh, 211 being |
| C02 | in progress | 15% | 32 counsel, 49 discernment, 85 imagination, 91 insight, 93 intention, 100 knowledge, 108 meditation, 110 memory, 126 purpose ✓, 127 reasoning, 160 thought ✓, 166 understanding, 174 wisdom |
| C03 | in progress | 22% | 11 awe, 29 contentment, 42 delight ✓, 69 gratitude, 97 joy ✓, 132 rejoicing, 175 wonder, 186 gladness, 192 comfort |
| C04 | in progress | 29% | 8 appetite, 43 desire ✓, 78 hope ✓, 102 longing, 115 passion, 179 yearning, 193 craving |
| C05 | in progress | 11% | 2 agony, 5 anguish, 18 brokenness, 51 distress, 71 grief ✓, 72 groaning, 113 mourning, 151 sorrow, 188 weeping |
| C06 | in progress | 38% | 7 anxiety ✓, 44 despair, 53 dread, 61 fear ✓, 79 hopelessness†, 146 shame ✓, 158 terror, 190 contempt |
| C07 | in progress | 20% | 4 anger ✓, 13 bitterness, 56 envy ✓, 75 hatred, 87 indignation, 96 jealousy, 136 resentment†, 178 wrath, 181 zeal, 205 resentment |
| C08 | in progress | 18% | 16 boldness, 33 courage, 46 devotion, 48 diligence, 55 endurance, 65 generosity, 66 gentleness, 80 humility ✓, 109 meekness, 116 patience ✓, 142 self-control |
| C09 | not started | 0% | 15 boastfulness, 36 cowardice†, 74 hardness, 101 laziness†, 123 pride, 128 rebellion, 133 reliability†, 153 stubbornness, 170 weakness, 208 sloth |
| C10 | not started | 0% | 14 blamelessness†, 60 faithfulness, 67 goodness, 77 honesty, 90 innocence, 92 integrity, 125 purity, 139 righteousness, 148 sincerity, 164 truthfulness, 168 uprightness |
| C11 | not started | 0% | 31 corruption, 40 deceit, 57 evil, 81 hypocrisy, 89 iniquity, 120 perverseness, 147 sin, 162 transgression, 172 wickedness, 203 treachery |
| C12 | not started | 0% | 1 abomination, 39 debauchery, 41 defilement, 86 impurity, 105 lust, 144 sensuality, 149 slander, 157 temptation, 171 whoredom, 189 malice |
| C13 | in progress | 44% | 24 condemnation, 26 conscience ✓, 30 contrition†, 35 covetousness, 50 disobedience, 70 greed, 73 guilt ✓, 98 justice ✓, 135 repentance ✓ |
| C14 | in progress | 10% | 17 bondage, 21 commitment†, 25 conformity†, 45 determination†, 114 obedience, 137 resolve, 155 submission, 156 surrender, 173 will ✓, 180 yielding |
| C15 | in progress | 33% | 59 faith ✓, 94 intercession, 121 praise, 122 prayer, 138 reverence, 140 seeking, 163 trust ✓, 176 worship, 212 pray ✓ |
| C16 | not started | 0% | 6 anointing, 28 consecration, 76 holiness, 83 idolatry, 124 prophecy, 150 sorcery, 159 testimony, 165 unbelief, 191 doubt, 194 blessing |
| C17 | in progress | 45% | 22 communion†, 23 compassion ✓, 34 covenant ✓, 62 fellowship, 64 forgiveness, 68 grace, 99 kindness, 103 love ✓, 111 mercy ✓, 117 peace ✓, 130 reconciliation |
| C18 | not started | 0% | 12 betrayal†, 52 division, 104 loyalty, 106 manipulation†, 131 rejection, 152 strife, 167 unity |
| C19 | not started | 0% | 19 calling, 47 dignity, 82 identity†, 84 image of God†, 107 meaning, 119 personhood†, 141 self-awareness†, 177 worth, 201 image, 204 name, 209 likeness |
| C20 | in progress | 29% | 187 strength, 195 spiritual powers†, 196 power, 197 authority ✓, 198 might, 199 dominion ✓, 200 energy |
| C21 | not started | 0% | 37 darkening†, 38 deadness†, 134 renewal, 154 stupor†, 161 transformation†, 202 transformation, 207 blindness (spiritual), 210 deadness |
| C22 | not started | 0% | 3 ambition, 9 assent†, 10 awareness†, 20 character, 27 consciousness, 54 emotion†, 58 experience, 63 foolishness, 88 ingratitude†, 95 intuition†, 118 personality†, 129 recognition, 143 sensitivity†, 145 sexuality†, 169 vulnerability†, 206 vulnerability |

**Key:** ✓ = Session B Complete | † = Phase 1 Excluded | no mark = Session B not yet started

---

## 6. Reading Programme State

Programme state can be assessed at any time by querying the `word_registry` table. The following queries give the key programme state indicators. These are intended to be run by Claude Code.

### 6.1 Session B Progress by Status

```sql
SELECT session_b_status, COUNT(*) as count
FROM word_registry
GROUP BY session_b_status
ORDER BY session_b_status;
```
Returns: how many registries are at each status level.

### 6.2 Words Ready for Analysis

```sql
SELECT no, word
FROM word_registry
WHERE session_b_status IN ('Ready for Analysis', 'Pre-Analysis Complete')
ORDER BY no;
```
Returns: registries that can be analysed immediately.

### 6.3 Words Not Yet Started

```sql
SELECT no, word, phase1_status
FROM word_registry
WHERE session_b_status IS NULL
ORDER BY no;
```
Returns: registries where Session B has not started.

### 6.4 Zero-Term Registries

```sql
SELECT no, word
FROM word_registry
WHERE phase1_term_count = 0 OR phase1_term_count IS NULL
ORDER BY no;
```
Returns: registries requiring investigation for missing term data.

### 6.5 Cluster Progress

```sql
SELECT cluster_assignment, COUNT(*) as total,
  SUM(CASE WHEN session_b_status = 'Session B Complete' THEN 1 ELSE 0 END) as complete
FROM word_registry
GROUP BY cluster_assignment;
```
Returns: cluster completion status. Requires cluster field — see WA-Implementation-Instruction-v5.

### 6.6 Term Sharing — Not-Shared Words

Words with `term_sharing_ratio = 0` have no cross-registry term overlap. These words can be analysed independently — their term inventories and verse sets do not intersect with any other registry. This makes them the simplest candidates for Session B analysis.

```sql
SELECT no, word, cluster_assignment, unique_term_count,
       phase1_term_count, phase1_verse_count, session_b_status
FROM word_registry
WHERE term_sharing_ratio = 0.0
  AND phase1_status != 'Excluded'
  AND phase1_term_count > 0
ORDER BY no;
```
Returns: registries with no shared terms — can be analysed without cross-registry considerations.

### 6.7 Term Sharing — Ownership Distribution

The `term_owner_type` field on `wa_term_inventory` marks whether each term record is the primary owner (OWNER) or a cross-reference copy (XREF). XREF verse records are delete_flagged and excluded from standard queries and exports.

```sql
SELECT term_owner_type, COUNT(*) as terms
FROM wa_term_inventory
WHERE delete_flagged = 0
GROUP BY term_owner_type;
```
Returns: owner vs cross-reference term distribution.

---

## 7. Periodic Review Protocol

The registry should be reviewed periodically — approximately every 25 completed Session B analyses — to validate that the programme is on track and the registry structure remains sound.

### 7.1 What a Periodic Review Covers

- Programme state snapshot — how many words at each status
- Cluster progress — which clusters are near completion, which have barely started
- Zero-term registry investigation — are the 13 zero-term registries data issues or genuine gaps?
- Registry anomalies — any words whose status is inconsistent or whose data looks incorrect
- Scope validation — are there words in the registry that, in light of completed analyses, appear to fall outside the inner-being scope? Document the question — do not remove words.

### 7.2 What a Periodic Review Does Not Do

- Remove words from the registry — scope questions are documented, not acted on unilaterally
- Reclassify completed Session B analyses — those are fixed unless explicitly re-run
- Make synthesis claims — periodic review is about programme state, not analytical conclusions

### 7.3 Review Output

A periodic review produces a brief programme state document. Naming convention:

```
wa-programme-review-{YYYYMMDD}.docx
```

---

## 8. Terminology Reference

| **Term** | **Definition** |
| --- | --- |
| Registry | A single word and its full analytical record — terms, verses, analysis, flags. |
| Registry number (no) | The integer identifier for a registry. Used in all file naming. |
| Session B | The verse-grounded word analysis phase. Produces the narrative document and JSON. |
| Session D | The cross-registry synthesis phase. Not yet underway. Begins when sufficient clusters are complete. |
| MTI (Master Term Inventory) | The full inventory of Hebrew and Greek terms associated with a registry word. |
| MTI status | Classification of a term's relevance to its registry: extracted, extracted_thin, delete, candidate_delete, xref_{word}, phase2_enrichment. |
| Evidential status | Assessment of how well a term's verse corpus supports its inclusion as an inner-being characteristic: confirmed, plausible, uncertain, instrumental, relational_only. |
| Session D pointer | A structural cross-registry observation recorded during Session B for use in Session D synthesis. |
| Cluster | A logical grouping of registry words for Session B processing and Session D preparation. Not an analytical classification. |
| Patch | A JSON file of database operations submitted to Claude Code for application to `bible_research.db`. |
| Term sharing ratio | Proportion of a registry's terms that also appear in other registries. 0.0 = all unique, 1.0 = all shared. Engine-derived from `wa_term_inventory` cross-file analysis. |
| Not-shared word | A registry where `term_sharing_ratio = 0.0` — all terms are unique to this word. Can be analysed independently without cross-registry verse overlap. |
| Owner term | A term_inventory record where `term_owner_type = OWNER` — the primary location for this Strong's number. |
| Cross-reference term | A term_inventory record where `term_owner_type = XREF` — a copy of a term that belongs primarily to another registry. XREF verse records are delete_flagged. |
| PH2 flag | A research flag recorded in `wa_session_research_flags` indicating an issue requiring attention in Session B or Session D. |
| Conceptual Word Register | A supplementary register of modern inner-life concepts that have no direct biblical lexical equivalent. Session D construct. |

---

## 9. File Naming Reference

All programme files follow the `wa-{nnn}-{word}-{scope}-{YYYYMMDD}` pattern. This section summarises the scope tokens used for each file type.

| **Scope token** | **File type** |
| --- | --- |
| analysis | Session B narrative document — `wa-{nnn}-{word}-analysis-{date}.docx` |
| extract | Word JSON export from database — `wa-{nnn}-{word}-extract-{date}.json` |
| json | Session B structured JSON output — `wa-{nnn}-{word}-json-{date}.json` |
| patch | Patch file for Claude Code — `wa-{nnn}-{word}-patch-{date}.json` |
| sessiond | Session D discovery JSON — `wa-{nnn}-{word}-sessiond-{date}.json` (periodic run) |
| clusters | Clustering run output — `wa-clusters-{date}.json` |

Programme instruction documents use the full name pattern without a registry number:

```
WA-{DocumentName}-v{n}-{YYYYMMDD}.docx
Examples:
  WA-SessionB-Analysis-Instruction-v5-20260327.docx
  WA-Registry-Management-Guide-v5-20260327.docx
  WA-Reference-v5-20260327.docx
```

---

## Change Control

**Change control — v7**
Section 5 (Cluster Assignments): Cluster assignments populated from `wa-registry-overview-20260327.json`. All 212 words are now listed under their assigned cluster (C01–C22) with current Session B status indicated. Cluster status field updated to reflect actual programme state (complete / in progress / not started). Section 5.2 updated to include "in progress" as a named cluster status. Section 5.3 updated to reflect that the clustering run is complete.

**Change control — v6**
Section 3 (Registry Status Lifecycle): Analysis Complete description corrected. Previous text stated "Session B JSON not yet extracted." Corrected to: "The Session B JSON has been extracted and the analysis report is produced."

**Change control — v5.3**
Section 2 (Registry Fields): Added `cluster_assignment`, `sb_classification`, `sb_classification_reasoning`, `carry_forward`, `unique_term_count`, `shared_term_count`, `term_sharing_ratio`. Section 6.6 and 6.7 added: term sharing queries for not-shared words and ownership distribution. Section 8 (Terminology): Added term sharing ratio, not-shared word, owner term, cross-reference term. `wa_term_inventory.term_owner_type` column documented. XREF verse records are delete_flagged.
