# Assessment: wa_session_b_findings

> Analysis date: 2026-04-14
> Table row count: 171 findings across 109 registries
>
> **2026-04-15 update — structural changes applied:**
> - DIR-20260415-004: Added 9 lifecycle fields (pass_ref, study_segment, delete_flag, obsolete_reason, obsolete_date, superseded_by_id, related_finding_id, resolution_note, thin_evidence). Table now 18 fields.
> - DIR-20260415-006: `finding_type` normalised to UPPER_SNAKE_CASE controlled vocabulary. 24 rows updated. 7 distinct values post-normalisation (DIMENSION_REVIEW=146, THEOLOGICAL_NOTE=8, VERSE_PATTERN=6, TERM_BEHAVIOUR=4, GROUP_INTEGRITY=3, ETYMOLOGY=2, DIMENSION_PATTERN=2).
> - DIR-20260415-005: New companion junction table `wa_finding_entity_links` created for linking findings to entities.
>
> Row content (171 rows) preserved intact. The "naming inconsistency" issue from Section 4.1 of this assessment is resolved.

---

## 1. Table Purpose

`wa_session_b_findings` captures structured analytical findings from Session B analysis and Dimension Review work. Each row is a discrete insight — a dimensional pattern, a theological note, an etymology observation, a group integrity concern — tied to a specific registry, dated, and attributed to the instruction version under which it was raised.

---

## 2. Field-Level Summary

### finding_id

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Distinct values | 171 (all unique) |
| Duplicates | 0 |

Format: `{registry_no}-F{seq}` (e.g. "112-F001", "112-F013"). Every finding has a unique, stable identifier. Clean.

### registry_id (FK to word_registry)

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Distinct registries | 109 |
| Orphaned (no matching word_registry) | 0 |

109 of 214 registries (51%) have at least one finding. Top registries by finding count:

| Registry | Word | Findings |
|----------|------|--------:|
| 182 | soul | 13 |
| 112 | mind | 13 |
| 210 | deadness | 4 |
| 2 | agony | 4 |
| 128 | rebellion | 3 |
| 98 | justice | 3 |
| 97 | joy | 3 |
| 52 | division | 3 |
| 51 | distress | 3 |
| 43 | desire | 3 |
| 42 | delight | 3 |

Soul and mind are the most extensively documented, reflecting their centrality to the inner-life research. Most registries (73 of 109) have exactly 1 finding.

### file_id (FK to wa_file_index)

| Metric | Value |
|--------|-------|
| NULL | 151 (88%) |
| Populated | 20 (12%) |

The high NULL rate is by design — most findings are raised at **registry level** during Dimension Review, not at file level. The 20 populated rows come from early Session B extraction work (v5.1/v5.2 instructions) which operated at the file level.

### finding_type

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Distinct types | 8 |

Distribution:

| finding_type | Count | % | Source |
|-------------|------:|--:|--------|
| DIMENSION_REVIEW | 142 | 83% | Dimension Review sessions (C01-C22 cluster work) |
| theological_note | 8 | 5% | Session B extraction (v5.1/v5.2) |
| verse_pattern | 6 | 4% | Session B extraction |
| term_behaviour | 4 | 2% | Session B extraction |
| C22 | 4 | 2% | Cluster C22 specific findings |
| GROUP_INTEGRITY | 3 | 2% | Verse Context group consistency checks |
| etymology | 2 | 1% | Session B extraction |
| DIMENSION_PATTERN | 2 | 1% | Cross-dimensional pattern observations |

**83% of findings come from Dimension Review** — the cluster-level review process that assesses how each registry's verse context groups map to inner-being dimensions. The remaining 17% come from earlier Session B extraction work and carry more varied type labels (theological_note, verse_pattern, term_behaviour, etymology).

There is a **naming inconsistency**: the Dimension Review findings use UPPER_SNAKE_CASE (DIMENSION_REVIEW, GROUP_INTEGRITY, DIMENSION_PATTERN) while the Session B extraction findings use lower_snake_case (theological_note, verse_pattern, term_behaviour, etymology). The "C22" type is a cluster code used as a finding type, which breaks the convention.

### finding (text content)

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Empty | 0 |
| Populated | 171 (100%) |
| Min length | 210 chars |
| Avg length | 457 chars |
| Max length | 1,055 chars |

Every finding has substantive analytical content. These are not stubs — the average finding is a solid paragraph of analysis. Samples by type:

**DIMENSION_REVIEW:**
> "sha.mar family (H8104) spans four dimensions across Registry 112: Volitional/Will (G, covenantal obedience), Theological/Divine-Human (H, God's guardi..."

**theological_note:**
> "The mind is a moral organ before it is an intellectual one. It can be debased, blinded, corrupted, renewed, and transferred (mind of Christ). Romans 1..."

**verse_pattern:**
> "The cha.shav root documents that the same mental faculty produces artistic design, moral reasoning, and malicious plotting -- there is no separate crea..."

**GROUP_INTEGRITY:**
> "Group 7423-004 (H4194 ma.vet) contains two anchor verses in potential tension: Psa 6:5 (in death there is no remembrance of you; in Sheol who will giv..."

**term_behaviour:**
> "Memory in biblical vocabulary is an active, covenantal, morally significant act -- not passive cognitive retrieval. God's remembering produces redempti..."

**etymology:**
> "The ye.tser (formed inclination) is the OT anthropology's closest approach to a foundational moral disposition. Gen 6:5 and 8:21 establish it as bent..."

The findings represent genuine analytical work with specific textual grounding.

### anchor_verses

| Metric | Value |
|--------|-------|
| NULL | 112 (65%) |
| Populated | 59 (35%) |

65% of findings have no anchor verse references. This splits clearly by finding_type:

- **Dimension Review findings** (142 rows): mostly NULL — these describe dimensional patterns across groups, not individual verse observations
- **Session B extraction findings** (29 rows): mostly populated — these ground claims in specific verse references

Sample populated values:
- "Exo 31:17, Isa 42:1, Jer 32:41, Eze 18:4"
- "Rom 1:21; Phili 4:6; Col 3:15; 1Th 5:18"
- "Genesis 1:26-27; 1 Corinthians 11:7"
- "1Co 2:14, 1Co 15:44, 1Co 15:45, Jude 19"

Reference format is inconsistent — some use abbreviated book codes ("Rom", "1Co"), some use full names ("Genesis"), some use semicolons as separators, some use commas.

### raised_date

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Populated | 171 (100%) |

Date distribution:

| Date | Count | Context |
|------|------:|---------|
| 2026-03-27 | 10 | Session B extraction (v5.1) |
| 2026-03-28 | 10 | Session B extraction (v5.2) |
| 2026-04-06 | 13 | Dimension Review start (C01/C02) |
| 2026-04-07 | 103 | Dimension Review bulk (C03-C19) |
| 2026-04-08 | 22 | Dimension Review (C20) |
| 2026-04-09 | 9 | Dimension Review (C21/C22) |
| 2026-04-10 | 1 | Dimension Review (C17 late) |
| 2026-04-11 | 3 | Session B (grace/mercy/compassion) |

**60% of all findings** were raised on a single date (2026-04-07) during the main Dimension Review push across clusters C03-C19. The earlier Session B extraction work (2026-03-27/28) produced 20 findings from the soul and mind registries.

### session_b_instruction

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Populated | 171 (100%) |
| Distinct values | 9 |

Distribution:

| Instruction Version | Count | % |
|---------------------|------:|--:|
| WA-DimensionReview-Instruction-v1.3-2026-04-07 | 103 | 60% |
| WA-DimensionReview-Instruction-v1.6-2026-04-08 | 13 | 8% |
| WA-SessionB-Extraction-Instruction-v5.2 | 10 | 6% |
| WA-SessionB-Extraction-Instruction-v5.1 | 10 | 6% |
| WA-DimensionReview-Instruction-v1.4-2026-04-08 | 9 | 5% |
| WA-DimensionReview-Instruction-v1.9-2026-04-09 | 8 | 5% |
| WA-DimensionReview-Instruction-v1.1-2026-04-06 | 8 | 5% |
| WA-DimensionReview-Instruction-v1.8-2026-04-09 | 5 | 3% |
| WA-DimensionReview-Instruction-v1.2-2026-04-06 | 5 | 3% |

**9 different instruction versions** — 7 Dimension Review versions (v1.1 through v1.9) and 2 Session B Extraction versions (v5.1, v5.2). The Dimension Review instruction iterated rapidly through 7 versions in 4 days (2026-04-06 to 2026-04-09) as the review methodology was refined.

---

## 3. Provenance

All 171 findings come from two distinct sources:

| Source | Period | Findings | Registries | Notes |
|--------|--------|--------:|----------:|-------|
| Session B Extraction (v5.1/v5.2) | 2026-03-27 to 2026-03-28 | 20 | 2 (soul, mind) | Early pilot. Detailed theological/etymological findings with anchor verses. |
| Dimension Review (v1.1 to v1.9) | 2026-04-06 to 2026-04-11 | 151 | 109 | Cluster-level review. Broader coverage, dimensional pattern findings. |

The data is entirely legitimate analytical output — produced during structured Claude AI sessions with proper instruction versioning and date attribution.

---

## 4. Data Quality Issues

### 4.1 finding_type naming inconsistency

Two naming conventions coexist:
- UPPER_SNAKE_CASE: DIMENSION_REVIEW, GROUP_INTEGRITY, DIMENSION_PATTERN
- lower_snake_case: theological_note, verse_pattern, term_behaviour, etymology
- Raw cluster code: C22

A normalisation pass would improve queryability.

### 4.2 anchor_verses format inconsistency

Where populated, verse references use mixed formats:
- "Rom 1:21" vs "Romans 1:21"
- Comma separators vs semicolon separators
- Some include ranges ("Genesis 1:26-27"), some don't

Not blocking, but would need normalisation before any programmatic verse-level joining.

### 4.3 file_id sparseness (88% NULL)

This is by design for Dimension Review findings (registry-level, not file-level), but means the `file_id` field is not useful as a filter or join target for the majority of the table.

### 4.4 No link to verse_context or wa_dimension_index

Dimension Review findings describe patterns in verse context groups and dimensions, but there is no FK linking a finding to the specific `verse_context_group` or `wa_dimension_index` rows it describes. The finding text references group codes and Strong's numbers, but these are embedded in prose, not structured as joinable fields.

---

## 5. Verdict

This table contains **genuine, well-attributed analytical work**:

1. **100% attribution** — every finding has a date, instruction version, and unique ID
2. **Substantive content** — average 457 chars per finding, no stubs or placeholders
3. **Broad coverage** — 109 of 214 registries (51%)
4. **Clean FK integrity** — no orphans, no NULL on required fields

The main limitations are structural:
- finding_type naming is inconsistent
- anchor_verses format is inconsistent
- No FK to the verse context or dimension data the findings describe

**This table is healthy.** It will grow significantly as Session B progresses through more registries. The naming and format issues are minor and could be normalised in a targeted cleanup if needed.

---

## 6. Growth Projection

Currently 171 findings across 109 registries (1.6 per registry average). As Session B completes:
- The 5 Analysis Complete registries (compassion, forgiveness, grace, love, mercy) will add Session B extraction findings similar to the soul/mind pilot
- Remaining Dimension Review clusters (17 of 22 still to complete) will add ~500+ DIMENSION_REVIEW findings
- Session D synthesis work will likely introduce new finding_type values

Expected table size at programme completion: **500-800 findings**.
