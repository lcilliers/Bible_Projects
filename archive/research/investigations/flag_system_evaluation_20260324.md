# Flag System Evaluation — Full Analysis

**Date:** 2026-03-24 (updated 2026-03-24 post-implementation)
**Produced by:** Claude Code (Opus 4.6), for review by Claude.ai + le Roux
**Purpose:** Document the current state, conflicts, and improvement opportunities in the flag subsystem before Session B patches are applied.

---

## 0. Resolution Status (2026-03-24)

All problems identified in this document have been resolved. Implementation was guided by
Claude.ai's review document (`FrameworkB-FlagSystem-Review-20260324.docx`).

| Problem | Resolution | Migration |
|---------|-----------|-----------|
| P1: Duplicate flag codes | TERM_ANALYSIS rows migrated from wa_data_quality_flags to wa_term_phase2_flags; wa_quality_flag_types now contains only DATA_COVERAGE codes | M15 |
| P2: A8 destructive reset | DELETE scoped to DATA_COVERAGE flag_group only (matches flag_engine.py's own idempotency) | Code fix in audit_word.py |
| P3: Session B patch table mismatch | New table `wa_session_research_flags` created with full schema (12 fields incl. priority, session_target, cross_registry_id) | M13 |
| P4: 24 unused flag types | IMPORT_STATUS (8), NOTE (4), REGISTRY_STATUS (2), UNCERTAIN_MEANING, ARAMAIC_EQUIVALENT deleted. TERM_ANALYSIS group retired. | M15 |
| P5: Two concepts called "Phase 2 flags" | Category B (term-level) stays in wa_term_phase2_flags (now extended with description/source/raised_date). Category C (session research) goes in wa_session_research_flags. | M13, M14 |
| P6: No engine writes to wa_term_phase2_flags | Confirmed by design — researcher-owned, engine never touches. Documented. | N/A |
| P7: No write path for mti_term_flags | Left as-is per Claude.ai guidance — 9 active rows preserved, no cleanup. | N/A |

**Schema version:** 3.3.0 → 3.6.0 (M13 + M14 + M15)

**New infrastructure:**
- `scripts/apply_session_patch.py` — generic Session B/C/D patch applicator
- `wa_session_research_flags` table — holds PH2-xxx-xxx research flags
- `wa_term_phase2_flags` extended with description, source, raised_date columns
- `word_export.py` exports `session_research_flags` key

---

## 1. Architecture Overview (Post-Implementation)

The database now has **three clearly separated flag subsystems** with clean ownership boundaries:

```
CATEGORY A: Engine-Derivable Data Coverage Flags
  Owner: Engine (Claude Code)
  wa_quality_flag_types (8 codes, DATA_COVERAGE group only)
      └─ wa_data_quality_flags (~3,000 rows)
  Written by: flag_engine.py (7 derivable codes) + span filter (1 code)
  Reset: A8 in audit_word.py deletes DATA_COVERAGE flags only, then re-derives

CATEGORY B: Term-Level Analytical Flags
  Owner: Researcher (Claude.ai)
  phase2_flag_types (25 codes)
      ├─ wa_term_phase2_flags (~1,500 rows, now with description/source/raised_date)
      └─ mti_term_flags (9 rows)
  Written by: Patch scripts only. Engine NEVER touches.

CATEGORY C: Session Research Flags
  Owner: Researcher (Claude.ai)
  wa_session_research_flags (new table, open vocabulary)
  Written by: apply_session_patch.py
  Labels: PH2-[registry]-[seq] convention
  Fields: flag_code, flag_label, description, priority, session_target,
           cross_registry_id, resolved, resolved_date, resolved_note
```

```
SUBSYSTEM A: Phase 2 Flags (Researcher Judgment)
  phase2_flag_types (25 codes)         ← shared lookup
      ├─ wa_term_phase2_flags (461 rows)   ← junction: term_inv_id + flag_id
      └─ mti_term_flags (9 rows)           ← junction: mti_term_id + flag_id

SUBSYSTEM B: Quality Flags (Engine-Derived + Patch-Imported)
  wa_quality_flag_types (47 codes, 5 groups)
      └─ wa_data_quality_flags (4,136 rows) ← full record: file_id + term_id + flag_id + description
```

### Design Intent (as understood)

- **Phase 2 flags** (`wa_term_phase2_flags`): Simple boolean markers on terms — "this term exhibits GOD_AS_SUBJECT" — set by researcher judgment during analysis. No description, no metadata, just a link.
- **Quality flags** (`wa_data_quality_flags`): Richer records with descriptions, grouped into 5 categories. A mix of engine-derived (automated) and manually-imported (via patch scripts).

---

## 2. Current State — Detailed Inventory

### 2.1 Phase 2 Flag Types (phase2_flag_types)

25 codes, all actively used. These represent **semantic/analytical observations** about terms:

| id | flag_code | Usage in wa_term_phase2_flags | Usage in mti_term_flags |
|----|-----------|-------------------------------|------------------------|
| 1 | GOD_AS_SUBJECT | 105 | 0 |
| 2 | CAUSATIVE_OF_INNER_STATE | 58 | 0 |
| 3 | SOMATIC_INNER_LINK | 80 | 0 |
| 4 | BODY_INNER_EXPRESSION | 18 | 0 |
| 5 | NT_FACULTY_NAMING | 6 | 0 |
| 6 | GENERATION_RESOLUTION_PAIR | 3 | 0 |
| 7 | CROSS_PART_ROOT | 17 | 0 |
| 8 | THIN_DATA | 47 | 0 |
| 9 | SMALL_VERSE_SAMPLE | 6 | 0 |
| 10 | DUPLICATE_RESOLVED | 1 | 0 |
| 11 | NO_WORD_ANALYSIS | 4 | 0 |
| 12 | CONSOLIDATION_CANDIDATE | 3 | 0 |
| 13 | THEOLOGICAL_ANCHOR | 1 | 9 |
| 14 | SOMATIC_EXPRESSION | 10 | 0 |
| 15 | HIGH_FREQUENCY_ANCHOR | 13 | 0 |
| 16 | SEMANTIC_RANGE_BREADTH | 13 | 0 |
| 17 | MULTI_REGISTRY_ANCHOR | 1 | 0 |
| 18 | DIVINE_HUMAN_PARALLEL | 22 | 0 |
| 19 | ESCHATOLOGICAL_USAGE | 4 | 0 |
| 20 | WISDOM_LITERATURE_CONCENTRATION | 4 | 0 |
| 21 | METAPHOR_ROOT | 8 | 0 |
| 22 | RELATIONAL_DIRECTION | 11 | 0 |
| 23 | VOLITIONAL_COMPONENT | 17 | 0 |
| 24 | CROSS_TESTAMENT_SHIFT | 5 | 0 |
| 25 | ARAMAIC_FORM | 4 | 0 |

**Coverage:** Only 15 of 211 registries have any Phase 2 flags: abomination, agony, ambition, anger, anguish, anointing, distress, grief, guilt, hope, humility, joy, patience, pride, strength. These are the original pre-engine-era words.

### 2.2 Quality Flag Types (wa_quality_flag_types)

47 codes across 5 groups. Usage varies dramatically:

**DATA_COVERAGE (10 codes) — 7 engine-derived, 3 unused:**

| id | flag_code | Rows | Source |
|----|-----------|------|--------|
| 1 | NO_VERSES | 252 | Engine-derived |
| 2 | THIN_DATA | 1,062 | Engine-derived |
| 3 | SMALL_VERSE_SAMPLE | 802 | Engine-derived |
| 4 | NO_WORD_ANALYSIS | 398 | Engine-derived |
| 5 | UNCERTAIN_MEANING | 0 | Unused |
| 6 | ARAMAIC_EQUIVALENT | 0 | Unused |
| 23 | SPAN_RESOLUTION_CONFLICT | 0 | Engine-derived (no current instances) |
| 24 | SPAN_FILTER_APPLIED | 12 | Written by span filter step |
| 36 | HIGH_FREQUENCY_ANCHOR | 245 | Engine-derived |
| 47 | PROSE_ONLY_MEANING | 263 | Engine-derived |

**TERM_ANALYSIS (18 codes) — imported via patch script:**

| id | flag_code | Rows |
|----|-----------|------|
| 29 | BODY_INNER_EXPRESSION | 11 |
| 30 | CAUSATIVE_OF_INNER_STATE | 150 |
| 31 | CROSS_TESTAMENT_SHIFT | 1 |
| 32 | DIVINE_HUMAN_PARALLEL | 134 |
| 33 | ESCHATOLOGICAL_USAGE | 32 |
| 34 | GENERATION_RESOLUTION_PAIR | 60 |
| 35 | GOD_AS_SUBJECT | 91 |
| 37 | METAPHOR_ROOT | 100 |
| 38 | MULTI_REGISTRY_ANCHOR | 7 |
| 39 | NT_FACULTY_NAMING | 5 |
| 40 | RELATIONAL_DIRECTION | 82 |
| 41 | SEMANTIC_RANGE_BREADTH | 188 |
| 42 | SOMATIC_EXPRESSION | 9 |
| 43 | SOMATIC_INNER_LINK | 81 |
| 44 | THEOLOGICAL_ANCHOR | 0 |
| 45 | VOLITIONAL_COMPONENT | 88 |
| 46 | WISDOM_LITERATURE_CONCENTRATION | 63 |
| 28 | ARAMAIC_FORM | 0 |

**IMPORT_STATUS (8 codes) — all unused (0 rows each):**
STRONGS_RECONCILED, OCCURRENCE_COUNT_MISMATCH, FORMAT_ERROR_IN_SOURCE, FORMAT_ISSUE_RESOLVED, PARSE_ERROR, TERMS_IN_HEADER_NOT_IN_STEP, DUPLICATE_IN_SOURCE, DUPLICATE_RESOLVED

**NOTE (4 codes) — all unused (0 rows each):**
NOTE, NOTE_ON_ROOT_FAMILY, ANOMALY_NOTE, SPAN_BACK_POPULATED

**REGISTRY_STATUS (2 codes) — all unused (0 rows each):**
NO_FURTHER_ACTION, RESEARCH_REQUIRED

### 2.3 mti_term_flags

Only 9 rows. All use THEOLOGICAL_ANCHOR. 8 from peace (registry 117), 1 from strength (registry 187).

---

## 3. Identified Problems

### PROBLEM 1: Complete Code Duplication Between Type Tables

Every single flag_code in `phase2_flag_types` (25 codes) also exists in `wa_quality_flag_types`. The same analytical concepts live in two places:

| flag_code | phase2_flag_types.id | wa_quality_flag_types.id |
|-----------|---------------------|------------------------|
| GOD_AS_SUBJECT | 1 | 35 |
| CAUSATIVE_OF_INNER_STATE | 2 | 30 |
| SOMATIC_INNER_LINK | 3 | 43 |
| BODY_INNER_EXPRESSION | 4 | 29 |
| NT_FACULTY_NAMING | 5 | 39 |
| GENERATION_RESOLUTION_PAIR | 6 | 34 |
| CROSS_PART_ROOT | 7 | 18 |
| THIN_DATA | 8 | 2 |
| SMALL_VERSE_SAMPLE | 9 | 3 |
| DUPLICATE_RESOLVED | 10 | 10 |
| NO_WORD_ANALYSIS | 11 | 4 |
| CONSOLIDATION_CANDIDATE | 12 | 15 |
| THEOLOGICAL_ANCHOR | 13 | 44 |
| SOMATIC_EXPRESSION | 14 | 42 |
| HIGH_FREQUENCY_ANCHOR | 15 | 36 |
| SEMANTIC_RANGE_BREADTH | 16 | 41 |
| MULTI_REGISTRY_ANCHOR | 17 | 38 |
| DIVINE_HUMAN_PARALLEL | 18 | 32 |
| ESCHATOLOGICAL_USAGE | 19 | 33 |
| WISDOM_LITERATURE_CONCENTRATION | 20 | 46 |
| METAPHOR_ROOT | 21 | 37 |
| RELATIONAL_DIRECTION | 22 | 40 |
| VOLITIONAL_COMPONENT | 23 | 45 |
| CROSS_TESTAMENT_SHIFT | 24 | 31 |
| ARAMAIC_FORM | 25 | 28 |

**Origin:** The original 15 registries had their flags in `wa_term_phase2_flags`. When the bulk `_apply_phase2_flags_patch.py` ran, it mirrored the same codes into `wa_quality_flag_types` (TERM_ANALYSIS group) and wrote flag instances into `wa_data_quality_flags` for later-processed registries. Both systems now coexist for different registries.

**43 terms** have the same flag_code in both tables simultaneously (primarily THIN_DATA and SMALL_VERSE_SAMPLE for distress, grief, joy, strength).

### PROBLEM 2: A8 Audit Reset Destroys Non-Derivable Quality Flags

The `_reset_quality_flags()` function in `audit_word.py` (line 1157) executes:
```sql
DELETE FROM wa_data_quality_flags WHERE file_id IN (...)
```

This deletes **all** quality flags — including the TERM_ANALYSIS flags that were imported via `_apply_phase2_flags_patch.py`. After the reset, `run_flag_engine()` only re-creates the 7 derivable DATA_COVERAGE flags. The 1,114 TERM_ANALYSIS rows are **permanently destroyed** when audit_word runs.

**Impact:** Running `audit_word` on anger (registry 4) today would have wiped any TERM_ANALYSIS flags if they existed (anger currently has none — only DATA_COVERAGE). But for registries like fear (71 TERM_ANALYSIS flags), heart (45), desire (68), running audit_word would destroy those flags with no recovery path.

**Contrast with flag_engine.py's own idempotency:** The flag engine's internal reset (lines 104-112) only deletes its own 7 derivable codes. The A8 wrapper is broader and more destructive.

### PROBLEM 3: Session B Patch Targets Non-Existent Table Structure

The Session B patch (`PATCH-20260324-182-SESSIONB-V1.json`, OP-017 through OP-022) wants to insert Phase 2 flags with this structure:

```json
{
  "registry_id": 182,
  "file_id": 36,
  "flag_code": "PH2_CROSS_REF_ENRICHMENT",
  "flag_label": "PH2-182-001",
  "strongs_reference": "H5317",
  "description": "...(rich analytical prose)...",
  "session_raised": "Session B v3.0",
  "raised_date": "2026-03-24",
  "resolved": 0
}
```

**Three mismatches:**

1. **Table name:** Patch targets `wa_phase2_flags` — this table does not exist. The actual table is `wa_term_phase2_flags`.

2. **Schema:** `wa_term_phase2_flags` has only two columns: `(term_inv_id, flag_id)`. The patch needs 9 fields (registry_id, file_id, flag_code, flag_label, strongs_reference, description, session_raised, raised_date, resolved).

3. **Flag codes:** The 6 codes in the patch don't exist in either type table:
   - PH2_CROSS_REF_ENRICHMENT
   - PH2_VOLUME_LIMITATION
   - PH2_CROSS_REGISTRY_REQUIRED
   - PH2_EXEGETICAL_STUDY_REQUIRED
   - PH2_THEOLOGICAL_DEPTH_REQUIRED
   - PH2_ESCHATOLOGICAL_STUDY_REQUIRED

### PROBLEM 4: 24 Unused Quality Flag Types

Nearly half of `wa_quality_flag_types` (24 of 47 codes) have zero rows:
- All 8 IMPORT_STATUS codes
- All 4 NOTE codes
- Both REGISTRY_STATUS codes
- 2 DATA_COVERAGE codes (UNCERTAIN_MEANING, ARAMAIC_EQUIVALENT)
- 5 TERM_ANALYSIS codes (CONSOLIDATION_CANDIDATE, MULTI_SENSE_ENTRY, CROSS_REGISTRY, CROSS_PART_ROOT, PERIPHERAL_TERM)
- ARAMAIC_FORM, THEOLOGICAL_ANCHOR (TERM_ANALYSIS)

These were defined speculatively but never populated by any code path.

### PROBLEM 5: Two Different Concepts Called "Phase 2 Flags"

The term "Phase 2 flag" means two different things in the system:

1. **Original Phase 2 flags** (`wa_term_phase2_flags`): Simple boolean markers — "this term exhibits this property." No description, no provenance. Applied to the original 15 registries by the researcher.

2. **Session B Phase 2 flags** (patch structure): Rich analytical records — a specific finding with a unique label (PH2-182-001), detailed description, the session that raised it, a resolution status, and a strongs reference. These are research-level annotations, not boolean markers.

These are fundamentally different data structures serving different analytical purposes.

### PROBLEM 6: No Engine Code Writes to wa_term_phase2_flags

Despite the flag_engine.py docstring claiming it writes Phase 2 flags, no engine mode (NEW_WORD, GAP_FILL, AUDIT_WORD) ever inserts into `wa_term_phase2_flags`. The table was populated entirely through legacy processes (pre-engine manual work and throwaway scripts).

Similarly, the engine never reads `wa_term_phase2_flags` for any logic — only for snapshot display in A2 and for export.

### PROBLEM 7: No Write Path for mti_term_flags

The 9 rows in `mti_term_flags` have no documented origin. No engine mode, no apply script, and no workflow instruction produces inserts into this table. Only the two throwaway `_tmp_delete*.py` scripts ever touched it (deletes only).

---

## 4. Registry Coverage Map

### Phase 2 Flags (wa_term_phase2_flags) — 15 registries

| Registry | Word | Flag Count |
|----------|------|-----------|
| 1 | abomination | 21 |
| 2 | agony | 15 |
| 3 | ambition | 3 |
| 4 | anger | 39 |
| 5 | anguish | 16 |
| 6 | anointing | 9 |
| 51 | distress | 38 |
| 71 | grief | 21 |
| 73 | guilt | 8 |
| 78 | hope | 3 |
| 80 | humility | 5 |
| 97 | joy | 73 |
| 116 | patience | 8 |
| 123 | pride | 11 |
| 187 | strength | 191 |

### Quality Flags (wa_data_quality_flags) — 171 registries

Top 10 by total flag count:

| Registry | Word | DATA_COVERAGE | TERM_ANALYSIS | Total |
|----------|------|--------------|---------------|-------|
| 4 | anger | 624 | 0 | 624 |
| 103 | love | 482 | 0 | 482 |
| 61 | fear | 65 | 71 | 136 |
| 43 | desire | 57 | 68 | 125 |
| 183 | heart | 62 | 45 | 107 |
| 187 | strength | 75 | 12 | 87 |
| 51 | distress | 74 | 10 | 84 |
| 182 | Soul | 69 | 0 | 69 |
| 126 | remorse | 47 | 0 | 47 |
| 171 | zeal | 47 | 0 | 47 |

**196 registries** have no Phase 2 flags at all.
**40 registries** have no quality flags (registry-only entries with no term data).

---

## 5. What Needs to Happen — Structural Assessment

### 5.1 The Two Kinds of Flags Going Forward

Based on the actual usage patterns, there are three distinct flag categories that the system needs to support:

**Category A: Engine-Derivable Data Coverage Flags**
- Computed automatically from the data (occurrence counts, verse counts, meaning presence)
- 7 current codes: HIGH_FREQUENCY_ANCHOR, THIN_DATA, SMALL_VERSE_SAMPLE, NO_WORD_ANALYSIS, NO_VERSES, SPAN_RESOLUTION_CONFLICT, PROSE_ONLY_MEANING
- Written by `flag_engine.py`, reset on every audit run
- **Owner: Claude Code (engine)**

**Category B: Term-Level Analytical Flags**
- Semantic/analytical properties of individual terms (GOD_AS_SUBJECT, SOMATIC_INNER_LINK, etc.)
- Currently split across `wa_term_phase2_flags` (15 registries, boolean) and `wa_data_quality_flags` (bulk-imported registries, with descriptions)
- **Owner: Claude.ai (analysis)** — these require interpretive judgment

**Category C: Session-Level Research Flags (NEW)**
- Rich analytical findings from Session B (and future sessions)
- Have labels (PH2-182-001), long descriptions, resolution status, session provenance
- Point to specific terms but are really about research questions and gaps
- No existing table can hold these
- **Owner: Claude.ai (analysis)**, resolved collaboratively

### 5.2 Key Decisions Required

**Decision 1: Consolidate or keep separate?**

The TERM_ANALYSIS flags (Category B) currently live in two places:
- `wa_term_phase2_flags` for the original 15 registries (boolean, no description)
- `wa_data_quality_flags` for later registries (with descriptions, via TERM_ANALYSIS group)

Options:
- (a) Migrate everything into `wa_data_quality_flags` and retire `wa_term_phase2_flags`
- (b) Migrate everything into `wa_term_phase2_flags` (would need schema extension for descriptions)
- (c) Keep both, accept the duplication, document the boundary

**Decision 2: Fix the A8 destructive reset**

The audit_word A8 step deletes ALL quality flags including TERM_ANALYSIS. Options:
- (a) Change A8 to only delete derivable DATA_COVERAGE flags (match flag_engine.py's own behavior)
- (b) Move TERM_ANALYSIS flags to a table the engine doesn't touch
- (c) Both

**Decision 3: Create a table for Session B research flags (Category C)**

The Session B patch needs a home. Proposed schema:

```sql
CREATE TABLE wa_research_flags (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    registry_id     INTEGER NOT NULL,
    file_id         INTEGER,
    flag_code       TEXT NOT NULL,
    flag_label      TEXT NOT NULL UNIQUE,
    strongs_reference TEXT,
    description     TEXT NOT NULL,
    session_raised  TEXT NOT NULL,
    raised_date     TEXT NOT NULL,
    resolved        INTEGER NOT NULL DEFAULT 0,
    resolved_date   TEXT,
    resolved_note   TEXT,
    FOREIGN KEY (registry_id) REFERENCES word_registry(id),
    FOREIGN KEY (file_id) REFERENCES wa_file_index(id)
);
```

This would hold the rich Session B/C/D findings that are research-level rather than term-level.

**Decision 4: Clean up unused flag types**

24 flag types in `wa_quality_flag_types` have zero usage. Options:
- (a) Delete them (clean, but may lose forward-declared intent)
- (b) Keep them, document which are "reserved for future use"
- (c) Archive them (move to a separate reference table)

**Decision 5: Where do the Session B patch's new flag_codes live?**

The 6 new codes (PH2_CROSS_REF_ENRICHMENT, PH2_VOLUME_LIMITATION, etc.) are research-level codes, not term-level analytical codes. If Decision 3 creates `wa_research_flags`, these would be free-text codes in that table. If not, they need a home in one of the existing type tables.

---

## 6. What Claude Code Can Do (Data/Schema)

Pending decisions from the review, Claude Code can implement:

1. **Fix A8 reset** — scope the DELETE to only derivable DATA_COVERAGE flag codes (Problem 2). This is a safety fix and arguably should happen regardless.

2. **Create migration for `wa_research_flags`** table (or whatever name is chosen) — add as M13 in migrate.py.

3. **Write a generic Session B patch applicator** — handles mti_terms updates, word_registry updates, and research flag inserts from the standardised patch format.

4. **Consolidate the dual flag systems** — if decided, migrate `wa_term_phase2_flags` data into `wa_data_quality_flags` (or vice versa) with a migration script.

5. **Clean up unused flag types** — remove or archive the 24 zero-usage codes.

6. **Update word_export.py** — include `wa_research_flags` in the JSON export so Claude.ai can see them.

7. **Apply the 17 non-flag operations** from the Soul Session B patch immediately (mti_terms + word_registry updates).

---

## 7. What Claude.ai Should Weigh In On

1. **Are the 25 existing Phase 2 flag codes still the right analytical vocabulary?** Session B introduces new codes (PH2_CROSS_REF_ENRICHMENT, etc.) that are structurally different. Should the original 25 be extended, or are they a closed set for the original 15 registries?

2. **Should TERM_ANALYSIS flags be owned by Claude.ai going forward?** Currently they exist in the quality flags table which the engine resets. If Claude.ai is the author of these flags, they need protection from engine operations.

3. **What fields does a Session B/C/D research flag need?** The current patch proposes: registry_id, file_id, flag_code, flag_label, strongs_reference, description, session_raised, raised_date, resolved. Is this sufficient? Should there be a priority/severity field? A category beyond flag_code?

4. **Resolution workflow for research flags:** When a PH2 flag like "Heb 4:12 needs dedicated exegetical study" is resolved, what should happen? Just set resolved=1, or should there be a link to the output (e.g., a document path)?

5. **Naming convention for Session B patch files and flag labels:** The current patch uses `PH2-182-001` through `PH2-182-006`. Is this the convention going forward? Should the label encode the session (B/C/D)?

---

## Appendix A: Write Path Summary

| Code Path | wa_term_phase2_flags | wa_data_quality_flags | mti_term_flags |
|-----------|---------------------|----------------------|----------------|
| engine/flag_engine.py | Never | 7 derivable codes (idempotent) | Never |
| engine/audit_word.py A8 | Never (explicitly preserved) | FULL DELETE then re-derive | Never |
| engine/new_word.py N16 | Never | Via flag_engine | Never |
| engine/gap_fill.py S5 | Never | Via flag_engine | Never |
| scripts/_apply_phase2_flags_patch.py | Never | 19 TERM_ANALYSIS codes (2,361 rows) | Never |
| scripts/_realign_quality_flags.py | Never | FULL DELETE then re-derive (destructive) | Never |
| Manual / throwaway scripts | Deletes only | Deletes only | Never |

## Appendix B: Read Path Summary

| Code Path | wa_term_phase2_flags | wa_data_quality_flags | mti_term_flags |
|-----------|---------------------|----------------------|----------------|
| engine/audit_word.py A2 | Snapshot + display | Snapshot + display | Snapshot + display |
| engine/audit.py WR-06/07/10/13/16/17/19 | Never | Multiple checks | Never |
| engine/report.py | Never | Section 4 display | Never |
| analytics/word_export.py | Exported as "phase2_flags" | Exported as "quality_flags" | Exported as "mti.flags" |

## Appendix C: 43 Duplicate Flag Instances (Same Term, Same Code, Both Tables)

All are DATA_COVERAGE flags (THIN_DATA, SMALL_VERSE_SAMPLE, HIGH_FREQUENCY_ANCHOR) for terms in registries that were processed both before and after the bulk patch import: distress (12), grief (1), hope (1), joy (7), strength (22).

---

*Document produced by Claude Code for collaborative review with Claude.ai.*
