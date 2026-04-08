# Framework B — Soul Word Analysis Programme

# Registry Management Guide

**Version 5.7 | April 2026 | Reference guide — not an operational instruction**

| **Document** | **Value** |
| --- | --- |
| Filename | WA-Registry-Management-Guide-v5.7-2026-04-06.md |
| Supersedes | WA-Registry-Management-Guide-v5.6-20260330.md |
| Purpose | Terminology, structure, maintenance, and periodic review of the word registry |
| Audience | Researcher and both AI systems — reference when questions arise about registry meaning, state, or structure |
| Not covered | Transactional operations — see WA-VerseContext-Instruction-v2.4 and WA-SessionB-DataPrep-Instruction-v5.6 |

**Change Control — v5.7**

| **Change** | **Detail** |
| --- | --- |
| Section 2 | Runtime-computed fields added: `live_verse_count`, `live_owner_count`, `live_xref_count`, `vc_groups`, `vc_relevant`, `vc_set_aside`, `vc_anchors`, `dimension_profile` — definitions, source queries, and audit interpretation for each |
| Section 2 | `phase1_verse_count` query documented explicitly |
| Section 3.2 | Pure XREF registry pattern documented; correct anomaly test stated; zero-owner Complete clarification |
| Section 3a | **New section: OWNER and XREF Terms — The Core Distinction.** Covers the fundamental rule (one OWNER per Strong's number programme-wide); per-field behaviour table contrasting OWNER and XREF; pure XREF registry definition with full expected field value table; correct anomaly test sequence (including invisible-terms VCB gap); FK rule for XREF terms. Added because repeated misinterpretation of XREF behaviour caused incorrect audit conclusions during Dimension Review. |
| Section 6a | New section: Audit integrity rules — what constitutes an audit-clean registry record, REVIEW resolution requirements, FK integrity check queries, post-restructuring verification procedure |
| Section 6c (new) | Corrected verse count queries: VCB-scope verse count (6c.1), special-status verse count (6c.2), and CC directive to add `vcb_scope_verse_count` and `special_status_verse_count` fields to the registry overview export (6c.3). Programme-wide accounting note updated with full breakdown of the 27,017-verse gap. |
| Section 8 | OWNER term, XREF term, and Pure XREF registry definitions substantially expanded with field-level consequences and FK rule |

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
| phase1_verse_count | Number of verses with confirmed span matches in the Phase 1 extract. **Engine-derived — Phase 1 state only. Not updated by Session B pipeline.** Source query: `SELECT COUNT(*) FROM wa_verse_records WHERE file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk=?) AND span_strong_match=1 AND (delete_flagged=0 OR delete_flagged IS NULL)`. Counts verses where the Strong's number was confirmed as a span match — higher quality filter than `live_verse_count`. For registries with all-unique terms and no XREF sharing, `phase1_verse_count` and `live_verse_count` will match. For registries with shared terms, `phase1_verse_count` will be larger because it counts all verses in the registry's file_ids including verses attributable to shared terms from other registries. |
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

### 2a. Runtime-Computed Fields in Registry Overview Exports

The following fields appear in registry overview JSON exports (e.g. `wa-registry-overview-{date}.json`) but are **not stored columns in `word_registry`**. They are computed at export time by the registry overview script. They must not be assumed to be current between exports — always check the `exported_date` of the file.

| **Field** | **Source query and meaning** |
| --- | --- |
| `live_verse_count` | `SELECT COUNT(*) FROM wa_verse_records WHERE file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk=?) AND delete_flagged=0`. Counts ALL active (non-delete-flagged) verses in the registry's file_ids — **regardless of `term_owner_type`, `span_strong_match`, or `mti_terms.status`**. This is broader than the VCB-classified verse set. It includes verses belonging to terms with `mti_terms.status` of `delete`, `NULL`, `candidate_delete`, or other non-extracted values. The difference between `live_verse_count` and `vc_relevant + vc_set_aside` is therefore expected and does not indicate missing classification — see audit interpretation below. |
| `live_owner_count` | Count of active OWNER terms: `wa_term_inventory WHERE term_owner_type='OWNER' AND delete_flagged=0` joined via `wa_file_index` to this registry. |
| `live_xref_count` | Count of active XREF terms: `wa_term_inventory WHERE term_owner_type='XREF' AND delete_flagged=0` joined via `wa_file_index` to this registry. |
| `vc_groups` | Count of `verse_context_group` records for OWNER terms of this registry where `delete_flagged=0`. |
| `vc_relevant` | Count of `verse_context` records where `is_relevant=1` and `delete_flagged=0` for OWNER terms of this registry. |
| `vc_set_aside` | Count of `verse_context` records where `is_relevant=0` and `delete_flagged=0` for OWNER terms of this registry. Includes AVF (All-Verses-Fail) term verses — AVF terms receive verse_context records with `is_relevant=0` for every verse. |
| `vc_anchors` | Count of `verse_context` records where `is_anchor=1` and `delete_flagged=0` for OWNER terms of this registry. |
| `dimension_profile` | JSON summary of dimension label distribution across `wa_dimension_index` groups for this registry. |

**Audit interpretation of `live_verse_count` vs `vc_relevant + vc_set_aside`:**

The gap between `live_verse_count` and `vc_relevant + vc_set_aside` has three possible states, each with a specific meaning:

| Gap state | Definition | Meaning |
| --- | --- | --- |
| Zero (within ±2) | `live_verse_count ≈ vc_relevant + vc_set_aside` | VCB accounting correct. All OWNER verses in scope are classified. |
| Positive gap | `live_verse_count > vc_relevant + vc_set_aside` | Expected. The excess represents verses belonging to terms deliberately excluded from VCB classification. These fall into two groups: (1) terms with non-extracted `mti_terms.status` (`delete`, `NULL`, `candidate_delete`, legacy statuses) — excluded by the VCB batch builder filter; (2) terms with legitimate special statuses (`extracted_theological_anchor`, `phase2_enrichment`) — deliberately outside VCB scope and handled separately in Session B. The gap closes for group 1 if those verses are delete_flagged in `wa_verse_records`. Group 2 verses remain active by design. **Does not indicate missing classification.** |
| Negative gap | `live_verse_count < vc_relevant + vc_set_aside` | Anomalous. VCB has classified more verses than the registry's active verse set. Primary cause: FK-misattributed terms from other registries whose verse_context records were assigned to this registry. Requires investigation. See Section 6b. |

Programme-wide accounting (as of 2026-04-06): 27,017 active verses belong to non-extracted or special-status terms across all registries, producing the aggregate positive gap. Breakdown: 23,515 verses from `delete` status terms (housekeeping gap — verses should be delete_flagged, pending CC action); 2,149 from `candidate_delete` terms (pending researcher decision); 823 from `extracted_theological_anchor` terms (peace #117 — active by design); 5 from `phase2_enrichment` terms (soul #182 — active by design); 525 from legacy statuses (`xref_*`, `extracted_theological_anchor` overlap, and other). The 828 special-status verses are not data errors and must not be delete-flagged. The registry overview export query (`live_verse_count`) counts all of these because it does not filter on `mti_terms.status`. A corrected verse count query that reflects only VCB-scope verses is documented in Section 6c below.

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

**Pure XREF registries:** A registry where every `wa_term_inventory` row is `term_owner_type = XREF` and `live_owner_count = 0` is a legitimate and complete programme state. Its verse context is inherited through the OWNER registries via the shared `mti_term_id` path. The following fields are all correct for a pure XREF registry:

| Field | Expected value | Reason |
| --- | --- | --- |
| `live_owner_count` | 0 | All terms are cross-references |
| `live_xref_count` | > 0 | XREF terms exist |
| `live_verse_count` | 0 | No verses attached to XREF rows directly |
| `vc_groups` | 0 | Groups are generated from OWNER terms only |
| `vc_relevant` | 0 | No OWNER verses to classify |
| `vc_set_aside` | 0 | No OWNER verses to classify |
| `verse_context_status` | Complete | Correct — nothing to classify |
| `wa_dimension_index` entries | 0 | Index is populated from OWNER terms only |

During Session B, a pure XREF registry accesses its dimension data through the shared `mti_term_id` path from the OWNER registries. Known pure XREF registries as of 2026-04-06: consciousness (27), loyalty (104), meekness (109), recognition (129), resolve (137), reverence (138), sensuality (144), energy (200), resentment (205).

**Audit anomaly test for zero-owner registries:** The genuine anomaly signal is `live_owner_count = 0` AND `live_xref_count = 0` simultaneously — a registry with no terms of any kind. This indicates a programme gap. A registry with `live_owner_count = 0` and `live_xref_count > 0` is a pure XREF registry and requires no corrective action.

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

## 3a. OWNER and XREF Terms — The Core Distinction

This section exists because the OWNER/XREF distinction has caused repeated misinterpretation during programme analysis. Every AI session must read and apply this section correctly before reasoning about any registry's state.

### 3a.1 The Fundamental Rule

**Every Strong's number in the programme has exactly one OWNER registry.** That registry is the analytical home for the term — the place where its verses are active, classified, and grouped.

A term may also appear as an XREF in one or more other registries. The XREF row signals analytical relevance to that registry, but it carries no active verses and generates no independent analytical output of any kind.

> **The presence of an XREF row for a term in registry X does not mean registry X has classified or owns that term. It means registry X has a relationship with a term that is owned and classified elsewhere.**

### 3a.2 What Each Term Type Controls

| Property | OWNER term | XREF term |
| --- | --- | --- |
| `wa_verse_records.delete_flagged` | 0 — verses active | 1 — verses inactive |
| Verse Context classification | Yes — verses classified here | No — inherits from OWNER |
| `verse_context_group` records generated | Yes | No |
| `wa_dimension_index` entries generated | Yes | No |
| `mti_terms.owning_registry_fk` | Must point to this registry | Must point to the OWNER registry (not this registry) |
| Active in `live_owner_count` | Yes | No |
| Active in `live_xref_count` | No | Yes |
| Active in `live_verse_count` | Yes (verses counted) | No (verses delete_flagged) |
| Session B participation | Direct — via own groups | Indirect — via OWNER's `mti_term_id` path |

### 3a.3 The Pure XREF Registry

A registry where every term is `term_owner_type = XREF` is called a **pure XREF registry**. This is a legitimate and complete programme state — not an error, not a gap. The registry's analytical content is entirely contributed by terms owned in other registries.

**Expected field values for a pure XREF registry:**

| Field | Expected value | Why |
| --- | --- | --- |
| `live_owner_count` | 0 | No OWNER terms |
| `live_xref_count` | > 0 | XREF terms exist |
| `live_verse_count` | 0 | All verses are delete_flagged (XREF) |
| `vc_relevant` | 0 | Nothing to classify |
| `vc_set_aside` | 0 | Nothing to classify |
| `vc_groups` | 0 | No groups generated |
| `vc_anchors` | 0 | No anchors generated |
| `verse_context_status` | Complete | Correct — vacuously complete |
| `wa_dimension_index` entries | 0 | Index populated from OWNER terms only |

**None of these zeros are anomalies.** They are the correct and expected state of a pure XREF registry. Do not flag them, do not raise them as gaps, do not treat them as pipeline failures.

Known pure XREF registries as of 2026-04-06: consciousness (27), loyalty (104), meekness (109), recognition (129), resolve (137), reverence (138), sensuality (144), energy (200), resentment (205).

### 3a.4 The Correct Anomaly Test

When examining a registry's state, apply these tests in order:

| Test | Signal | Action |
| --- | --- | --- |
| `live_owner_count = 0` AND `live_xref_count = 0` | No terms of any kind | Genuine programme gap — investigate |
| `live_owner_count = 0` AND `live_xref_count > 0` | Pure XREF registry | Expected — no action required on vc or group fields |
| `live_owner_count > 0` AND `vc_groups = 0` AND `vc_set_aside = 0` AND `verse_context_status = Complete` | OWNER terms exist but zero VCB output — terms may be invisible to VCB pipeline due to non-extracted `mti_terms.status` | Critical anomaly — check `mti_terms.status` for all OWNER terms; see Section 6b.2 |
| `live_owner_count > 0` AND `vc_set_aside > 0` AND `vc_groups = 0` | All verses set aside (AVF) | Valid outcome — confirm intentional |
| `vc_relevant + vc_set_aside > live_verse_count` | Negative gap | FK contamination — investigate (Section 6b.1) |

### 3a.5 The FK Rule for XREF Terms

The field `mti_terms.owning_registry_fk` must always point to the **OWNER registry** — the registry where `term_owner_type = OWNER` for that Strong's number.

This rule holds regardless of how many XREF rows exist for the same term. The FK is not "which registries reference this term" — it is "which registry owns this term." Setting the FK to a registry where only an XREF row exists is incorrect and causes systematic misattribution in the dimension index populate script, which joins on this FK.

This was the cause of the Mechanism 3 FK mismatch documented in Section 6b: 36 terms had their FK set to a registry where they had an XREF row rather than to their OWNER registry.

---

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

## 6a. Audit Integrity Rules

This section defines what constitutes an audit-clean registry record and the verification steps required at programme checkpoints.

### 6a.1 Audit-Clean Definition

A registry is audit-clean when all of the following hold:

| Check | Requirement |
| --- | --- |
| Status consistency | `verse_context_status` and `session_b_status` are consistent with each other and with the pipeline sequence in Section 3.3 |
| Pure XREF integrity | If `live_owner_count = 0` and `live_xref_count > 0`: registry is a pure XREF registry — Complete and vc_groups=0 are correct. If `live_owner_count = 0` AND `live_xref_count = 0`: registry has no terms of any kind — genuine programme gap requiring investigation |
| VCB pipeline visibility | If `live_owner_count > 0` and `verse_context_status = Complete`: confirm that at least one `mti_terms` entry for the registry's OWNER terms has `status IN ('extracted', 'extracted_thin')`. If none exist, the terms were invisible to the VCB pipeline and `verse_context_status = Complete` is incorrect — see Section 6b.2 |
| REVIEW resolution | If `word_registry.notes` contains `result=REVIEW`, a subsequent note records the resolution decision and date |
| FK integrity | `mti_terms.owning_registry_fk` matches the OWNER path through `wa_term_inventory → wa_file_index → word_registry` for all active terms (see Section 6b) |
| Verse accounting | `live_verse_count - (vc_relevant + vc_set_aside)` is zero or positive. A negative gap is an anomaly requiring investigation |
| No stale status on new entries | New programme entries (notes contain "New entry" or "Replaces") must not carry `verse_context_status = Complete` until Session A has been run |

### 6a.2 REVIEW Resolution Requirement

When an audit run records `result=REVIEW` in `word_registry.notes`, a resolution decision is required before the registry is treated as audit-clean. The resolution note must state:

- What was reviewed
- What the decision was (e.g. "AVF confirmed — all verses correctly set aside", "zero-owner state correct — all terms are XREF in this registry", "session A required before VCB")
- The date of the decision

Until the resolution note is present, the registry carries an open audit flag.

### 6a.3 FK Integrity Check Queries

Run after every registry merge, restructuring event, or any operation that re-links terms between registries.

**Mechanism 2 — Merged/defunct registry check:**
```sql
-- Terms whose owning_registry_fk points to a registry with no active files
SELECT mt.id, mt.strongs_number, mt.transliteration, mt.owning_registry_fk,
       wr.word as fk_registry_word, wr.no as fk_registry_no
FROM mti_terms mt
JOIN word_registry wr ON wr.id = mt.owning_registry_fk
WHERE mt.status IN ('extracted', 'extracted_thin')
  AND mt.delete_flagged = 0
  AND NOT EXISTS (
      SELECT 1 FROM wa_file_index fi WHERE fi.word_registry_fk = wr.id
  );
```
Expected result: zero rows. Any row indicates a term whose FK points to a defunct or file-less registry.

**Mechanism 3 — XREF vs OWNER FK mismatch:**
```sql
-- Terms where owning_registry_fk does not match the OWNER wa_term_inventory path
-- but the text field owning_registry is correct
SELECT mt.id, mt.strongs_number, mt.transliteration,
       mt.owning_registry as text_field_registry,
       mt.owning_registry_fk,
       wr_fk.word as fk_registry_word,
       wr_owner.word as owner_path_word,
       wr_owner.no as correct_registry_no
FROM mti_terms mt
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr_owner ON wr_owner.id = fi.word_registry_fk
JOIN word_registry wr_fk ON wr_fk.id = mt.owning_registry_fk
WHERE mt.status IN ('extracted', 'extracted_thin')
  AND mt.delete_flagged = 0
  AND mt.owning_registry_fk != fi.word_registry_fk;
```
Expected result: zero rows after fix is applied. Any row indicates a term whose FK points to an XREF registry rather than the OWNER registry.

### 6a.4 Post-Restructuring Verification Procedure

After any registry merge, split, renaming, or re-linking of terms between registries:

1. Run both FK integrity queries above — confirm zero rows
2. Run the negative-gap check: `live_verse_count < vc_relevant + vc_set_aside` — confirm zero registries
3. Update `word_registry.notes` for any affected registry with the date and nature of the change
4. If `mti_terms.owning_registry_fk` was updated, trigger dimension index repopulation for affected registries
5. Confirm post-repopulation that `wa_dimension_index` group registry attributions match the corrected FK values

---

## 6b. Known Data Integrity Issues

### 6b.1 FK Mismatch — Status as of 2026-04-06

**Identified:** 2026-04-06 during Dimension Review audit (C02 session). Registry 93 (intention) showed zero groups in cluster extract despite 2 groups in registry overview. Root cause: extract populate script joins on `mti_terms.owning_registry_fk`; registry overview queries via `wa_term_inventory` OWNER path. The two paths diverge for 58 terms across two mechanisms.

**Mechanism 2 — Registry merge (22 terms):**
Reg 154 (stupor) was merged into Reg 151 (sorrow) on 2026-03-19. `wa_term_inventory` rows were re-linked to Reg 151. `mti_terms.owning_registry_fk` was not updated and still points to Reg 154 (now defunct — 0 files, 0 active terms). Procedure gap: registry merge procedure did not include an `mti_terms.owning_registry_fk` update step.

**Mechanism 3 — XREF FK mismatch (36 terms):**
36 terms have `owning_registry_fk` pointing to a registry where they have an XREF row, not the registry where they have their OWNER row. The text field `owning_registry` is correct in all 36 cases. Concentrated in: Reg 112 (mind, 20 terms), Reg 197 (authority, 16 terms). Cause: the script that set `owning_registry_fk` used the XREF row's registry as its source rather than the OWNER row's registry.

**Impact:**
- 58 terms' groups attributed to wrong registry in `wa_dimension_index`
- Reg 93 (intention, C02): 2 groups exist but show as 0 in cluster extract
- C01 Dimension Review (completed): 30 groups reviewed under wrong registry; 29 anchored (`manual_override=1`)
- 12 registries show negative gap (vc_sum > live_verse_count) — excess caused by FK-misattributed verse_context records

**Fix status:** Approved in principle. Not yet applied as of 2026-04-06.

**Approved fix procedure:**
1. Update `mti_terms.owning_registry_fk` for all 58 terms to match OWNER `wa_term_inventory` path
2. For Mechanism 2 (22 terms): also update text field `owning_registry` to match Reg 151 (sorrow)
3. Repopulate `wa_dimension_index` in two steps:
   - Step A: For 29 anchored rows (`manual_override=1`) moving out of C01: update `owning_registry_no`, `owning_registry_word`, `cluster_assignment` only — preserve `dimension`, `dimension_confidence`, `manual_override`, `notes`
   - Step B: For all non-override rows: `populate_dimension_index.py --clear` (preserves override rows by design)
4. Run both FK integrity queries (Section 6a.3) to confirm zero residual mismatches
5. Add FK integrity check to standard post-restructuring procedure going forward

**Open question:** The 29 anchored dimensions in C01 were assessed in the wrong cluster context. Whether they require re-examination in their correct cluster is deferred pending the outcome of the Level 1 and Level 2 data audit.

### 6b.2 VCB Pipeline Gap — Registry 15 (Boastfulness) — Status as of 2026-04-06

**Identified:** 2026-04-06 during Level 0 registry audit.

**State:** Registry 15 (boastfulness, C09) has 9 active OWNER terms with 247 active verses. No verse_context records, no verse_context_group records, and no wa_dimension_index entries exist for any of these terms. `verse_context_status = Complete` — incorrectly set.

**Root cause:** Every `mti_terms` entry for these terms carries `status = delete` or `status = NULL, delete_flagged = 1`. The VCB batch builder filters on `mti_terms.status IN ('extracted', 'extracted_thin')` — making all boastfulness terms invisible to the pipeline. The registry was advanced to `verse_context_status = Complete` during a sweep that treated it as a pure XREF registry, which it is not. It has 9 active OWNER terms with verses that have never been classified.

**This is a new class of pipeline gap:** a registry with active OWNER terms that are invisible to VCB because their `mti_terms.status` was never set to `extracted` or `extracted_thin`. The audit check for this gap is: `live_owner_count > 0` AND `vc_groups = 0` AND `vc_set_aside = 0` AND `verse_context_status = Complete` — which signals OWNER terms exist but produced no VCB output of any kind (not even set-aside records).

**Required remediation — in order:**
1. Determine correct `mti_terms.status` for each of the 9 OWNER terms — `extracted` or `extracted_thin` as appropriate based on term data and Session A decisions (researcher / Claude Code determination)
2. Reset `word_registry.verse_context_status` to `In Progress` for Reg 15
3. Run a targeted VCB batch for Reg 15's OWNER terms
4. Repopulate dimension index for Reg 15 after VCB completes
5. Reset `verse_context_status` to `Complete` once VCB output is confirmed

**Fix status:** Not yet applied as of 2026-04-06. Pending `mti_terms.status` determination.

**Detection query for this class of gap:**
```sql
-- Registries with active OWNER terms but zero VCB output despite Complete status
-- Signals terms invisible to the VCB pipeline due to non-extracted mti_terms.status
-- Excludes terms with legitimate special statuses that are deliberately outside VCB scope
SELECT wr.no, wr.word, wr.cluster_assignment,
       COUNT(DISTINCT ti.id) as owner_terms,
       COUNT(DISTINCT vr.id) as active_verses
FROM word_registry wr
JOIN wa_file_index fi ON fi.word_registry_fk = wr.id
JOIN wa_term_inventory ti ON ti.file_id = fi.id
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
WHERE wr.verse_context_status = 'Complete'
AND NOT EXISTS (
    SELECT 1 FROM mti_terms mt
    WHERE mt.strongs_number = ti.strongs_number
    AND mt.status IN ('extracted', 'extracted_thin',
                      'extracted_theological_anchor',
                      'phase2_enrichment')
    AND mt.delete_flagged = 0
)
GROUP BY wr.no, wr.word
HAVING COUNT(DISTINCT vr.id) > 0;
```

**Legitimate special statuses excluded from this query:**

| Status | Meaning | VCB treatment | Session B/D treatment |
| --- | --- | --- | --- |
| `extracted_theological_anchor` | Term retained as theological frame reference, not as direct inner-being vocabulary | Deliberately excluded from VCB — no verse_context records expected | Available for Session B consultation via status_note documentation and active verse records. Known registries: peace (#117) — 15 divine name and attribute terms. |
| `phase2_enrichment` | Term added for Session B enrichment as metaphorical or contextual support vocabulary | Deliberately excluded from VCB — no verse_context records expected | Available for Session B consultation via status_note documentation and active verse records. Known registries: soul (#182) — 1 term (H5317 nophet/honey, Pro 27:7 appetite metaphor). |

These statuses produce an expected positive gap between `live_verse_count` and `vc_relevant + vc_set_aside`. They are not pipeline errors. Any registry returning rows from this query after these exclusions is a genuine gap requiring investigation.

Run this query as part of the post-VCB-sweep verification to confirm no other registries share this condition.

---

## 6c. Corrected Verse Count Queries

The `live_verse_count` field in the registry overview export counts **all** active verses in a registry's files regardless of `mti_terms.status`. This is deliberately broad — it reflects total data presence. For audit and programme state purposes, two narrower queries are more useful.

### 6c.1 VCB-scope verse count (per registry)

Counts only verses whose terms are in scope for VCB classification — `extracted` or `extracted_thin` status only. This is the verse set that VCB is expected to have classified.

```sql
SELECT wr.no, wr.word,
       COUNT(DISTINCT vr.id) as vcb_scope_verses
FROM word_registry wr
JOIN wa_file_index fi ON fi.word_registry_fk = wr.id
JOIN wa_term_inventory ti ON ti.file_id = fi.id
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
    AND mt.status IN ('extracted', 'extracted_thin')
    AND mt.delete_flagged = 0
WHERE wr.no = ?  -- replace with registry number
GROUP BY wr.no, wr.word;
```

For this count: `vcb_scope_verses` should equal `vc_relevant + vc_set_aside` when VCB is complete. A gap indicates genuine unclassified verses.

### 6c.2 Special-status verse count (per registry)

Counts verses belonging to `extracted_theological_anchor` and `phase2_enrichment` terms — the verses that are active by design but outside VCB scope.

```sql
SELECT wr.no, wr.word, mt.status,
       COUNT(DISTINCT vr.id) as special_status_verses
FROM word_registry wr
JOIN wa_file_index fi ON fi.word_registry_fk = wr.id
JOIN wa_term_inventory ti ON ti.file_id = fi.id
    AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
    AND mt.status IN ('extracted_theological_anchor', 'phase2_enrichment')
    AND mt.delete_flagged = 0
WHERE wr.no = ?  -- replace with registry number
GROUP BY wr.no, wr.word, mt.status;
```

Known results as of 2026-04-06:
- Peace (#117): 818 verses across 15 `extracted_theological_anchor` terms
- Soul (#182): 5 verses across 1 `phase2_enrichment` term

### 6c.3 Registry overview export — recommended update

**Claude Code directive:** The `_generate_registry_overview` script currently uses this query for `live_verse_count`:

```sql
SELECT COUNT(*) FROM wa_verse_records
WHERE file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
AND delete_flagged = 0
```

This produces a count that includes special-status verses and makes the positive gap appear larger than is meaningful for audit purposes. Two additional fields should be added to the registry overview export:

| New field | Query | Purpose |
| --- | --- | --- |
| `vcb_scope_verse_count` | Count of verses for `extracted/extracted_thin` OWNER terms only | The verse set VCB is expected to classify. Should equal `vc_relevant + vc_set_aside` when complete. |
| `special_status_verse_count` | Count of verses for `extracted_theological_anchor` and `phase2_enrichment` OWNER terms | Verses active by design outside VCB scope. |

Until the export is updated, use Section 6c.1 and 6c.2 queries directly against the database when precise verse accounting is needed.

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
| OWNER term | `term_owner_type = OWNER` in `wa_term_inventory` — the primary analytical home for this Strong's number in this registry. OWNER terms have active verses (`wa_verse_records.delete_flagged = 0`). OWNER terms are classified during Verse Context. OWNER terms generate `verse_context_group` records and appear in `wa_dimension_index`. Every Strong's number has exactly one OWNER registry programme-wide. |
| XREF term | `term_owner_type = XREF` in `wa_term_inventory` — a cross-reference copy indicating that this Strong's number is analytically relevant to this registry but is owned by a different registry. XREF terms have their verses `delete_flagged = 1` in `wa_verse_records` — inactive, never classified. XREF terms do not generate verse_context records, verse_context_group records, or wa_dimension_index entries of their own. Their verse context and dimension data is accessed through the shared `mti_term_id` path from the OWNER registry during Session B. The `mti_terms.owning_registry_fk` for any term — whether accessed via an OWNER or XREF row — must point to the OWNER registry, not to a registry where only an XREF row exists. See Section 6b for the known FK mismatch where this rule was violated. |
| Pure XREF registry | A registry where every `wa_term_inventory` row is `term_owner_type = XREF` — `live_owner_count = 0` and `live_xref_count > 0`. A valid and complete programme state. The registry has no verses to classify, no groups to generate, no dimension index entries of its own. It participates in Session B through its XREF terms' OWNER registries. See Section 3.2 for full field expectations. Do not treat `vc_groups = 0` or `live_verse_count = 0` as anomalies for a pure XREF registry. |
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

*WA-Registry-Management-Guide-v5.7 | 2026-04-06 | Supersedes v5.6-20260330 | Section 2: runtime-computed field definitions and query sources; Section 3.2: pure XREF registry expected fields and anomaly test; Section 3a (new): OWNER/XREF core distinction — fundamental rule, per-field behaviour, pure XREF registry, anomaly test sequence including invisible-terms VCB gap, FK rule; Section 6a: audit integrity rules; Section 6b.1: FK mismatch; Section 6b.2: VCB pipeline gap — Reg 15 boastfulness, detection query updated to exclude legitimate special statuses; Section 6c (new): corrected verse count queries and CC directive for registry overview export update; Section 8: OWNER/XREF/pure XREF registry definitions expanded*
