# Assessment: wa_session_research_flags

> Analysis date: 2026-04-14
> Table row count: 327 flags across 72 registries
> Zero flags resolved
>
> **2026-04-15 updates:**
> - DIR-20260415-003: 19 rows with `flag_code='VOLUME_LIMITATION'` consolidated to `'PH2_VOLUME_LIMITATION'`. Distinct codes now 15 (was 16). The "naming duplication" issue from Section 4.1 of this assessment is resolved.
> - DIR-20260415-002: 15 missing reference rows added to `wa_quality_flag_types`. Every in-use code now has a reference entry with `category` classification. The "codes without reference entry" problem (Section 4 verdict point 4) is resolved — but note the relationship remains a loose string match, no FK constraint was added.
> - DIR-20260415-001: Three deprecated Session B codes in `wa_quality_flag_types` (SB_FINDING/SB_DIMENSION/SB_INNER_BEING) were not used in this table; no impact.
>
> The table's 327 rows, 229 SD_POINTERs, and all analytical content are preserved. `session_raised` format inconsistency (Section 4.2) was not addressed.

---

## 1. Table Purpose

`wa_session_research_flags` captures research observations, data quality notes, cross-registry pointers, and analytical forward-references raised during Session B, Dimension Review, and Verse Context work. Unlike `wa_session_b_findings` (which records analytical conclusions), this table records **matters requiring future action** — things Session D needs to investigate, data quality issues to address, cross-registry connections to trace, and volume limitations to acknowledge.

Every flag carries a `session_target` (B or D) indicating which session should resolve it, a `priority` (HIGH/MEDIUM/LOW), and a `resolved` field (currently all 0 — none resolved yet).

---

## 2. Field-Level Summary

### registry_id (FK to word_registry)

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Distinct registries | 72 (34% of 214) |
| Orphaned | 0 |

Top registries by flag count:

| Registry | Word | Flags |
|----------|------|------:|
| 68 | grace | 55 |
| 103 | love | 35 |
| 23 | compassion | 34 |
| 64 | forgiveness | 23 |
| 98 | justice | 16 |
| 111 | mercy | 16 |
| 112 | mind | 15 |
| 182 | soul | 14 |
| 4 | anger | 6 |
| 26 | conscience | 6 |
| 34 | covenant | 6 |
| 42 | delight | 6 |
| 197 | authority | 6 |
| 73 | guilt | 5 |
| 211 | being | 5 |

Heavily concentrated in the Session B completed registries (grace, love, compassion, forgiveness, mercy) which account for 163 of 327 flags (50%). The soul/mind flags come from earlier Session B extraction work.

### file_id (FK to wa_file_index)

| Metric | Value |
|--------|-------|
| NULL | 202 (62%) |
| Populated | 125 (38%) |

By design — SD_POINTER flags from Session B are typically raised at registry level, not file level. The populated rows come from earlier PH2 flags and data quality observations tied to specific file imports.

### flag_code

| flag_code | Count | % | Nature |
|-----------|------:|--:|--------|
| SD_POINTER | 229 | 70% | Cross-registry pointer for Session D synthesis |
| PH2_VOLUME_LIMITATION | 33 | 10% | Term has low verse coverage — synthesis conclusions provisional |
| VOLUME_LIMITATION | 19 | 6% | Same as above (naming variant) |
| PH2_DATA_ERROR | 11 | 3% | Data quality error identified (homonyms, function words, extraction anomalies) |
| DIMREVIEW_SESSION_D | 8 | 2% | Dimension Review observation forwarded to Session D |
| PH2_CROSS_REGISTRY_REQUIRED | 7 | 2% | Cross-registry analysis needed before synthesis |
| PH2_CROSS_REF_ENRICHMENT | 6 | 2% | Cross-reference enrichment opportunity |
| PH2_THEOLOGICAL_DEPTH_REQUIRED | 4 | 1% | Verse/passage needs dedicated theological study |
| PH2_DATA_QUALITY | 3 | 1% | Data quality concern (root bleed, missing verses) |
| GROUP_INTEGRITY (and others) | 7 | 2% | Miscellaneous (1 each of 7 types) |

**16 distinct flag codes** in three functional categories:

1. **SD_POINTER (229 / 70%)** — Cross-registry synthesis pointers. These say: "when analysing registry X in Session D, look at the connection to registry Y through term Z." These are the primary feedstock for Session D work.

2. **PH2_* flags (65 / 20%)** — Data quality and research depth flags raised during Session B pre-analysis. These identify volume limitations, data errors, cross-registry requirements, and passages needing deeper study. Targeted at Session D (mostly) or Session B (9 flags).

3. **DIMREVIEW_SESSION_D and others (33 / 10%)** — Dimension Review observations, thematic links, integrity checks, and one candidate registry word proposal.

**Naming inconsistency:** `PH2_VOLUME_LIMITATION` (33 rows) and `VOLUME_LIMITATION` (19 rows) describe the same thing. This appears to be a naming drift between instruction versions.

### flag_label

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Distinct values | 327 (all unique) |

Format: `{registry}-SD{seq}` for SD_POINTERs (e.g. "068-SD001"), `PH2-{registry}-{seq}` for PH2 flags (e.g. "PH2-182-001"), `DIM-{registry}-SD{seq}` for dim review flags. Every flag has a unique, stable identifier.

### strongs_reference

| Metric | Value |
|--------|-------|
| NULL | 167 (51%) |
| Populated | 160 (49%) |
| Distinct Strong's numbers | 119 |
| Resolvable to mti_terms | 153 (96% of populated) |
| Not resolvable | 7 |

The 7 unresolvable values are **multi-value comma-separated lists** (e.g. "H6419,H8605") or **semicolon-separated** (e.g. "H6754; H1823; G1504") — the field holds multiple Strong's numbers in a single string rather than one per row. These would need to be split before joining to mti_terms.

The 51% NULL rate is by design — many SD_POINTERs describe registry-level or cluster-level connections rather than term-specific observations.

### cross_registry_id (FK to word_registry)

| Metric | Value |
|--------|-------|
| NULL | 176 (54%) |
| Populated | 151 (46%) |
| Distinct target registries | 70 |
| Orphaned | 0 |

When populated, this identifies which registry the flag points TO. The 54% NULL rate includes:
- PH2 flags that are self-referential (about the source registry's own data quality)
- VOLUME_LIMITATION flags (about the source registry's verse coverage)
- Some SD_POINTERs that describe internal patterns without a specific target registry

FK integrity is clean — all populated values resolve to valid registries.

### priority

| Priority | Count | % |
|----------|------:|--:|
| MEDIUM | 200 | 61% |
| HIGH | 98 | 30% |
| LOW | 29 | 9% |

The 98 HIGH priority flags represent the most critical cross-registry connections and data quality issues. These should be addressed first in Session D.

### session_target

| Target | Count | % |
|--------|------:|--:|
| D | 318 | 97% |
| B | 9 | 3% |

97% of flags target **Session D** — cross-registry synthesis work. Only 9 flags target Session B, all being data quality or split issues requiring pre-analysis correction.

### description

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Populated | 327 (100%) |
| Min length | 41 chars |
| Avg length | 524 chars |
| Max length | 2,216 chars |

Every flag has a substantive description. Samples by category:

**SD_POINTER (cross-registry synthesis):**
> "G3340 metanoeō, G3341 metanoia, G3338 metamellomai, and H5162H na.cham (relent) all present in Reg 112 and Reg 135 (repentance). Structural overlap at intersection of cognitive reorientation and mind-change."

**PH2_VOLUME_LIMITATION:**
> "G5590G (psuchē: soul) has 825 occurrences but only 46 verses in the export (ratio 0.056). Synthesis-level conclusions about the NT use of psuchē must be held provisional."

**PH2_DATA_ERROR:**
> "H7110B (qe.tseph: splinter, Joel 1:7) carries a verse count of 28 erroneously shared with H7110A (qe.tseph: wrath). H7110B is a homonym with no anger content."

**PH2_CROSS_REF_ENRICHMENT:**
> "Grace-Forgiveness formal connection: G5483 charizō carries both 'give grace' and 'forgive/cancel debt' as primary senses. Eph 4:32 makes forgiveness the named expression of grace received."

**CANDIDATE_REGISTRY_WORD:**
> "Condemnation (katakrima/katakrinō family) is a candidate for a new registry entry. G2631 katakrima and root family G2632 katakrinō constitute a distinct inner-being vocabulary cluster."

### session_raised

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Distinct values | 34 |

34 different session identifiers spanning multiple instruction versions:

| Session source | Flags | Period |
|---------------|------:|--------|
| Session B extraction (v5.1/v5.2) | 18 | 2026-03-27/28 |
| Session B DataPrep (v5/v5.1) | 8 | 2026-03-26/27 |
| Session B analysis (v3.0-v4.7) | 139 | 2026-03-24 to 2026-04-12 |
| Dimension Review (v1.1-v2.2) | 76 | 2026-04-06 to 2026-04-11 |
| Early pre-analysis | 86 | 2026-03-24 to 2026-03-26 |

The `session_raised` format is **highly inconsistent** — some entries are instruction version references, some include full filenames, some include pass numbers. This reflects the evolving instruction framework across 34 distinct sessions.

### raised_date

| Metric | Value |
|--------|-------|
| NULL | 0 |
| Populated | 327 (100%) |

Date distribution:

| Date | Count | Context |
|------|------:|---------|
| 2026-03-24 | 18 | Early Session B (soul, mind, justice) |
| 2026-03-25 | 17 | Early Session B (joy, anger, guilt) |
| 2026-03-26 | 41 | Session B DataPrep + extraction |
| 2026-03-27 | 18 | Session B extraction (v5.1) |
| 2026-03-28 | 8 | Session B extraction (v5.2) |
| 2026-04-06 | 7 | Dimension Review start |
| 2026-04-07 | 41 | Dimension Review bulk |
| 2026-04-08 | 9 | Dimension Review |
| 2026-04-09 | 15 | Dimension Review |
| 2026-04-10 | 50 | Session B (grace, mercy) |
| 2026-04-11 | 23 | Session B (compassion, grace final) |
| 2026-04-12 | 77 | Session B (love, forgiveness, compassion) |
| 2026-04-13 | 3 | Session B (fellowship VC) |

Two production peaks: 2026-03-26 (41 early PH2 flags) and 2026-04-12 (77 flags from the love/forgiveness/compassion Session B completion).

### resolved / resolved_date / resolved_note

| Field | Value |
|-------|-------|
| resolved | All 0 (327/327) |
| resolved_date | All NULL |
| resolved_note | All NULL |

**No flags have been resolved.** This is expected — flag resolution is a Session D activity, and Session D has not started. The resolution mechanism is ready but unused.

---

## 3. Functional Categories

The 327 flags serve three distinct purposes:

### 3.1 Session D Synthesis Pointers (SD_POINTER + DIMREVIEW_SESSION_D + THEMATIC_LINK) — 238 flags

These are the **primary output** of this table. Each pointer identifies a specific cross-registry connection that Session D should investigate during synthesis work. They name:
- Which registries share terms, root families, or theological patterns
- Which Strong's numbers create the bridge
- What the analytical significance of the connection is

These are not problems — they are **research directives** produced by Session B analysis. They represent verified analytical judgements about where cross-registry synthesis will be most productive.

### 3.2 Data Quality and Volume Flags (PH2_* + VOLUME_LIMITATION + DATA_INTEGRITY) — 80 flags

These identify **limitations and errors** in the underlying data:
- Volume limitations (terms with low verse coverage relative to total occurrences)
- Data errors (homonyms, function word contamination, extraction anomalies)
- Cross-registry requirements (analysis that cannot be completed within a single registry)
- Passages requiring deeper study

These ARE matters to address — some before Session D (the 9 targeting Session B), most as part of Session D's preparatory work.

### 3.3 Research Depth and Boundary Flags — 9 flags

Single-instance flags identifying:
- A candidate new registry word (condemnation)
- Boundary questions (terms that operate both positively and negatively)
- Exegetical study requirements (e.g. Heb 4:12 soul-spirit division)
- Eschatological study requirements (ne.phesh and Sheol vocabulary)
- A required data split (H6293 pa.ga — three distinct senses in one entry)

---

## 4. Data Quality Issues

### 4.1 flag_code naming duplication

`PH2_VOLUME_LIMITATION` (33 rows) and `VOLUME_LIMITATION` (19 rows) are the same concept with different names. This appears to be a naming drift between instruction versions (v5.1/v5.2 used the PH2_ prefix; later sessions dropped it).

### 4.2 session_raised format inconsistency

34 distinct formats including:
- `WA-DimensionReview-Instruction-v1.3`
- `Session B Stage 2 -- wa-068-grace-sessionB-observations-v3.2`
- `WA-SessionB-Instruction-v4.7 Pass 3`
- `WA-097-joy-analysis-20260325.md`
- `Pre-analysis v1`

No standardised format exists. The field carries enough information to trace provenance, but is not programmatically parseable.

### 4.3 strongs_reference multi-value entries

7 rows contain multiple Strong's numbers in a single field (comma or semicolon separated). These cannot be joined to mti_terms without splitting. The field was designed for single values.

### 4.4 No FK to wa_session_b_findings

Some research flags reference the same registries and analytical work as findings in `wa_session_b_findings`, but there is no structural link between the two tables. A finding and its associated research flags can only be correlated by matching `registry_id` and approximate dates.

---

## 5. Verdict

This table is the **forward-looking counterpart** to `wa_session_b_findings`. Where findings record what was learned, research flags record **what needs to happen next**:

| Aspect | Status |
|--------|--------|
| Attribution | 100% — every flag has date, session, and unique label |
| Content quality | High — avg 524 chars, substantive descriptions with specific terms and verses |
| FK integrity | Clean — no orphans on registry_id or cross_registry_id |
| Coverage | 72 registries (34%), concentrated in Session B completed words |
| Resolution state | All open (0/327 resolved) — awaiting Session D |

**This table is healthy and operationally important.** The 229 SD_POINTERs are the primary input for Session D synthesis work. The 80 data quality flags identify real issues that should be addressed.

Minor cleanup opportunities:
- Merge `PH2_VOLUME_LIMITATION` and `VOLUME_LIMITATION` to a single code
- Normalise `session_raised` format
- Split multi-value `strongs_reference` entries

None of these are blocking.

---

## 6. Growth Projection

Currently 327 flags across 72 registries (4.5 per registry average). The five Session B completed registries alone generated 163 flags. As Session B completes across all 214 registries:

- Expected SD_POINTERs: ~1,500-2,000 (based on current rate of ~30 per completed registry)
- Expected PH2 flags: ~400-500 (many are shared across registries and raised once)
- Expected total at programme completion: ~2,000-2,500 flags

The `resolved` / `resolved_date` / `resolved_note` fields will activate during Session D.
