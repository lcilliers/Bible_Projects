# Assessment: wa_term_phase2_flags

> Analysis date: 2026-04-13
> Table row count: 1,580 flags across 891 terms (of 7,165 active)
>
> **2026-04-15 update:** This table was NOT modified by the flag remediation directives. The related reference table `wa_quality_flag_types` was extended (see `assessment-wa-session-research-flags.md` for context). The 99% unverifiable-flag problem identified in this assessment remains unresolved — cleanup is a separate decision pending researcher direction.

---

## 1. Table Purpose

`wa_term_phase2_flags` assigns analytical flags to individual term inventory records. These flags are intended to mark semantic and analytical properties of terms — properties that require interpretation beyond what the engine can derive mechanically. They are owned by Claude AI (the analytical engine) and are not touched by the automation engine.

The flag types are defined in `phase2_flag_types` (25 codes). Flags are linked to `wa_term_inventory` rows via `term_inv_id` and to flag type definitions via `flag_id`.

---

## 2. Data Origin — Three Layers

| Source | Date | Count | % | How created |
|--------|------|------:|--:|-------------|
| `bulk_patch` | 2026-03-19T18:18:06Z | 1,102 | 70% | Single bulk import — all applied at once, no per-term justification |
| NULL (unknown) | NULL | 461 | 29% | No source or date recorded |
| Session B v4.7 Pass 2/4 | 2026-04-11 | 17 | 1% | Legitimate Session B analytical work (grace, mercy, compassion) |

**99% of flags have no verifiable analytical provenance.** Only 17 flags (1%) come from verified Session B work with proper source attribution.

---

## 3. Flag Type Distribution

| Flag Code | Count | Description |
|-----------|------:|-------------|
| CAUSATIVE_OF_INNER_STATE | 208 | Causative grammatical form (Hiphil/Piel) or stated causative sense |
| SEMANTIC_RANGE_BREADTH | 201 | Term covers 4+ distinct semantic domains |
| GOD_AS_SUBJECT | 196 | God experiences or enacts this inner state in at least one context |
| SOMATIC_INNER_LINK | 168 | Inner state connected to bodily organ or physical process |
| DIVINE_HUMAN_PARALLEL | 156 | God and humans appear as subject in parallel contexts |
| METAPHOR_ROOT | 108 | Meaning grounded in concrete physical/sensory metaphor |
| VOLITIONAL_COMPONENT | 105 | Carries dimension of will, choice, or intention |
| RELATIONAL_DIRECTION | 93 | Inherently directed toward another person, group, or God |
| WISDOM_LITERATURE_CONCENTRATION | 67 | Predominant in Proverbs, Job, or Ecclesiastes |
| GENERATION_RESOLUTION_PAIR | 63 | Hebrew-Aramaic or Hebrew-Greek pair resolving to same referent |
| THIN_DATA | 47 | Fewer than 5 verse records; dataset too thin |
| ESCHATOLOGICAL_USAGE | 36 | Predominant in eschatological/apocalyptic passages |
| BODY_INNER_EXPRESSION | 34 | Inner state manifests through visible physical behaviour |
| SOMATIC_EXPRESSION | 19 | Inner state expressed through somatic/body-language patterns |
| CROSS_PART_ROOT | 17 | Root family spans a split registry part boundary |
| HIGH_FREQUENCY_ANCHOR | 13 | 200+ occurrences; primary anchor for semantic field |
| NT_FACULTY_NAMING | 11 | Greek term directly names an inner faculty (kardia, pneuma, etc.) |
| MULTI_REGISTRY_ANCHOR | 8 | Cross-reference in 3+ registries |
| CROSS_TESTAMENT_SHIFT | 6 | Meaningful semantic shift between OT and NT usage |
| THEOLOGICAL_ANCHOR | 6 | Framework A/B intersection term |
| SMALL_VERSE_SAMPLE | 6 | Verse count < 20% of occurrence count |
| ARAMAIC_FORM | 4 | Aramaic form in Daniel/Ezra/post-exilic contexts |
| NO_WORD_ANALYSIS | 4 | No STEP word analysis data available |
| CONSOLIDATION_CANDIDATE | 3 | Likely to merge with related entry during Session B |
| DUPLICATE_RESOLVED | 1 | Duplicate entry resolved to single record |

---

## 4. Coverage

| Metric | Value |
|--------|------:|
| Active terms in programme | 7,165 |
| Terms with at least one PH2 flag | 891 |
| Coverage | 12.4% |

Coverage is heavily concentrated in a few large registries:

| Registry | Word | Flag count | Terms flagged |
|----------|------|----------:|-------------:|
| 187 | strength | 150 | 55 |
| 97 | joy | 96 | 25 |
| 61 | fear | 71 | 38 |
| 43 | desire | 68 | 30 |
| 71 | grief | 66 | 25 |
| 51 | distress | 60 | 33 |
| 5 | anguish | 57 | 24 |
| 183 | heart | 45 | 19 |
| 117 | peace | 44 | 23 |
| 146 | shame | 39 | 17 |

Most registries have zero or very few flags. This is not a systematic assessment — it is selective and unevenly applied.

---

## 5. Integrity Problems

### 5.1 Flags on Dead Terms

| Condition | Count |
|-----------|------:|
| Flags on `wa_term_inventory.delete_flagged = 1` terms | 159 |
| Flags on `mti_terms.status = delete` terms | 341 |

These flags describe properties of terms the programme has already decided are not relevant. They are analytically meaningless and create noise in any query that does not explicitly exclude them.

### 5.2 Flags on Particles and Function Words

The following flags are applied to grammatical particles and function words with no inner-being content:

| Strong's | Gloss | Occ. | Flag | Registries |
|-----------|-------|-----:|------|-----------|
| G2532 | and (kai) | 10,000 | SEMANTIC_RANGE_BREADTH | deceit (40) |
| H0853 | [object marker] (eth) | 10,000 | RELATIONAL_DIRECTION, GENERATION_RESOLUTION_PAIR | awe (11) |
| G1722 | in/on/among (en) | 10,000 | SEMANTIC_RANGE_BREADTH | faith (59) |
| G0846 | it/he (autos) | 10,000 | SEMANTIC_RANGE_BREADTH | purpose (126) |
| H5921A | upon (al) | 5,802 | RELATIONAL_DIRECTION | 10+ registries (counsel, deceit, division, evil, faithfulness, goodness, iniquity, meditation, mercy, sin, terror, trust, understanding) |

Assigning analytical flags like RELATIONAL_DIRECTION or SEMANTIC_RANGE_BREADTH to conjunctions, prepositions, and pronouns is nonsensical. These terms appear in registries because STEP search casts a wide net, but they have no inner-being analytical value.

### 5.3 Cross-Check Against Inventory Fields

Three PH2 flag codes overlap with fields on `wa_term_inventory`. If both sources describe the same property, they should agree. They do not:

**GOD_AS_SUBJECT:**
| Source | Count |
|--------|------:|
| `wa_term_inventory.god_as_subject = 1` (active terms) | 208 |
| PH2 flag GOD_AS_SUBJECT | 196 |
| PH2 flag exists but inventory = 0 | 1 |
| Inventory = 1 but no PH2 flag | 25 |

**CAUSATIVE:**
| Source | Count |
|--------|------:|
| `wa_term_inventory.causative_form_present = 1` (active terms) | 194 |
| PH2 flag CAUSATIVE_OF_INNER_STATE | 208 |
| Excess: 14 more flags than the inventory supports | |

**SOMATIC:**
| Source | Count |
|--------|------:|
| `wa_term_inventory.somatic_link = 1` (active terms) | 162 |
| PH2 flag SOMATIC_INNER_LINK | 168 |
| Excess: 6 more flags than the inventory supports | |

The divergence means either the bulk patch or the inventory field (or both) was populated without careful verification. Two independent sources for the same property that disagree undermine confidence in both.

### 5.4 No Descriptions

| Has description | Count | % |
|-----------------|------:|--:|
| Yes | 17 | 1.1% |
| No (NULL) | 1,563 | 98.9% |

There is no record of *why* a particular term received a particular flag. The only exceptions are 3 THEOLOGICAL_ANCHOR flags on mercy (reg 111) and the 17 Session B flags — both from verified analytical sessions.

Without per-flag reasoning, the flags cannot be audited, challenged, or confirmed. They are assertions without evidence.

---

## 6. What IS Verifiable

The **17 Session B flags** (source = `Session B v4.7 Pass 2` / `Session B v4.7 Pass 4`, date = 2026-04-11) are legitimate analytical output. These were raised during Session B work on grace (68), mercy (111), and compassion (23), where Claude AI read verse data, assessed term properties, and made specific analytical judgements. They have:

- Proper source attribution
- Date stamps
- Analytical context (Session B pass number)
- Descriptions where applicable

These 17 flags are trustworthy.

---

## 7. Verdict

The bulk of this table (99%) is **unverifiable and unreliable**:

1. **No provenance** — 1,563 flags have no source or date, or come from a single undocumented bulk operation
2. **Flags on irrelevant terms** — 341 flags on mti-deleted terms; flags on function words and particles
3. **Internal contradictions** — PH2 flags disagree with the inventory fields they are supposed to match
4. **No reasoning** — 99% of flags have no description explaining why the flag was applied
5. **Uneven coverage** — 12% of terms covered, concentrated in a handful of registries

The 17 Session B flags (1%) are the only verified, trustworthy data in the table.

---

## 8. Cleanup Options

| Option | Action | Consequence |
|--------|--------|-------------|
| **A. Preserve only Session B flags** | Delete all 1,563 flags where `source NOT LIKE 'Session B%'` or source is NULL | Leaves 17 verified flags. Clean baseline for Session B to rebuild from data. |
| **B. Bulk cleanup + advisory** | Delete flags on deleted terms and particles; keep remainder but treat as non-authoritative | Removes the worst noise; ~1,000 flags remain as hypothesis. Session B must re-verify. |
| **C. Keep all, treat as advisory** | No deletions; document that flags are unverified | Avoids data loss but preserves noise. Risk: future sessions may treat flags as authoritative. |

**Recommendation:** Option A or B. The current data actively harms analysis by asserting properties without evidence and flagging irrelevant terms.
