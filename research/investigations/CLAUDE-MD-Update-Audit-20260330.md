# CLAUDE.md Update Audit — v5.5/v5.6 Instruction Suite

**Date:** 2026-03-30
**Purpose:** Extract all Claude Code tasks, operations, and updates from the upgraded Session_B instruction suite. Compare against current CLAUDE.md and identify what needs updating.

---

## 0. Document Versions Reviewed

| Document | New Version | Old Version (in CLAUDE.md) | Status |
|----------|-------------|---------------------------|--------|
| WA-SessionB-ClaudeCode-Instructions | **v3.2** | v1 (referenced) | **Major upgrade** |
| WA-Reference | **v5.5** | v5.1 | **Major upgrade** |
| WA-Registry-Management-Guide | **v5.6** | v7 (version mismatch in CLAUDE.md) | **Major upgrade** |
| WA-SessionB-DataPrep-Instruction | **v5.6** | v5 | Updated |
| WA-SessionB-Analysis-Instruction | **v5.6** | v5 | Updated |
| WA-SessionB-Extraction-Instruction | **v5.6** | v5.2 | Updated |
| WA-VerseContext-Instruction | **v1.5** | Not referenced | **NEW** |
| WA-VerseContext-SetupInstruction | **v1.1** | Not referenced | **NEW** |
| patch_specification | **v1.5** | Not referenced | **NEW** |

---

## 1. SCHEMA CHANGES — CLAUDE.md Must Update

### 1.1 Schema version: 3.7.0 → 3.8.0

CLAUDE.md Section 3 header says "Schema v3.7.0". Must update to **v3.8.0**.

### 1.2 Migration M17 (applied 2026-03-29)
- **Renamed:** `source_category` → `dimensions` on word_registry
- **Removed:** `anchor_verses` field from word_registry
- CLAUDE.md Section 3 table already mentions dimensions but still references "Schema v3.7.0"

### 1.3 Migration M18 (applied 2026-03-29)
- **New table:** `verse_context_group` (id, mti_term_id, group_code, context_description, notes, delete_flagged)
- **New table:** `verse_context` (id, verse_record_id, mti_term_id, group_id, is_anchor, is_relevant, is_related, notes, delete_flagged)
- **New field:** `word_registry.verse_context_status` (NULL / In Progress / Complete)
- CLAUDE.md Section 3 Table Groups needs new entry for Verse Context tables
- CLAUDE.md Key Relationships diagram needs verse_context chain added

### 1.4 constants.py — EXPECTED_SCHEMA_VERSION
- Currently says `"3.7.0"` in CLAUDE.md Section 4 Key Constants
- Must verify and update to reflect current engine expectation (may need engine update to 3.8.0)

---

## 2. NEW PIPELINE STAGE — Verse Context (entirely new)

CLAUDE.md has no mention of the Verse Context stage. This is a **major addition** that sits between Phase 1 and Session B DataPrep.

### 2.1 Stage Position in Pipeline
```
Phase 1 complete → Verse Context (Stage 1) → Session B DataPrep → Analysis → Extraction → Session D
```

### 2.2 Claude Code's Verse Context Responsibilities

| Task | Description |
|------|-------------|
| **Batch JSON construction** | Query DB for unclassified OWNER terms, accumulate to 2,000–2,500 verses per batch, produce `wa-vcb-{batch_id}-extract-{date}.json` |
| **Patch application** | Apply VERSECONTEXT patches — resolve group_code strings to integer IDs via `last_insert_rowid()` |
| **Consistency validation** | Run rules R1–R4 after every patch (set-aside clean, anchor clean, related-has-anchor, every-term-has-anchor) |
| **XREF coverage check** | Verify all XREF terms have an OWNER that is classified before advancing registry |
| **Double-check verification** | After writing `verse_context_status = Complete`, re-verify both OWNER and XREF checks; reverse if inconsistent |
| **Registry completion check** | When all OWNER + XREF terms classified → set `verse_context_status = Complete` |
| **Re-export** | Re-export full word JSON for each completed registry (opens DataPrep gate) |
| **Completion reporting** | Per-registry and batch-level completion summaries |
| **Stage 1 completion report** | When all 181 registries reach Complete, produce formal completion report |
| **Integrity validation** | After every patch: verify no active verse_context rows exist for deleted/excluded terms |
| **Re-extraction trigger** | After any audit_word re-run: detect new verses missing verse_context records, cascade delete_flags |

### 2.3 Verse Context Patch Types (new)
| Type | Naming | Purpose |
|------|--------|---------|
| VERSECONTEXT | `PATCH-{YYYYMMDD}-VCB{nnn}-VERSECONTEXT-V1` | Full batch classification |
| VCGROUP | `PATCH-{YYYYMMDD}-VCGROUP{group_id}-V1` | Targeted group update |
| VCVERSE | `PATCH-{YYYYMMDD}-VCVERSE{verse_record_id}-V1` | Targeted verse update |

All carry `session_b_status: null` — applicator must not reject.

### 2.4 Batch Construction Rules
- OWNER terms only (`term_owner_type = 'OWNER'`)
- Active terms only (`mti_terms.status IN ('extracted', 'extracted_thin')`)
- Terms with verses only
- Target: 2,000–2,500 unclassified verses per batch
- Never split a term across batches
- Batch ID: sequential VCB-001, VCB-002, etc.
- Output: `data/exports/verse_context/wa-vcb-{batch_id}-extract-{date}.json`

---

## 3. STATUS LIFECYCLE CHANGES — Must Update CLAUDE.md

### 3.1 New status field: `verse_context_status`
| Value | Meaning |
|-------|---------|
| NULL | Phase 1 excluded or zero-term — outside Verse Context scope |
| In Progress | Verse Context work pending or underway |
| Complete | All OWNER terms classified — registry may proceed to DataPrep |

### 3.2 Updated session_b_status vocabulary
| Value | Change |
|-------|--------|
| `Verse Context Reset` | **NEW** — prior Session B work superseded, must reprocess |
| `Ready for Analysis` | Now **legacy** — only set by audit_word COALESCE when status is NULL (new words only); not applicable to existing 181 registries |

### 3.3 Full pipeline sequence (updated)
```
Phase 1 → verse_context_status: In Progress → Verse Context batches →
verse_context_status: Complete → DataPrep → Pre-Analysis Complete →
Analysis → Analysis Complete → Extraction → Session B Complete
```

### 3.4 Ready for Analysis note
- `audit_word` uses COALESCE — only sets this if current status is NULL
- Never overwrites `Verse Context Reset`
- DataPrep treats it as equivalent to `Verse Context Reset`

---

## 4. PATCH SYSTEM CHANGES — Must Update CLAUDE.md

### 4.1 New patch_specification document (v1.5)
CLAUDE.md does not reference this document. It is the authoritative source for all patch applicator rules and should be referenced.

### 4.2 New operation types
| Operation | Table | Purpose |
|-----------|-------|---------|
| `update_evidential_status` | wa_term_inventory | Set evidential_status and retention_note per term |
| `bulk_update` on mti_terms | mti_terms | Two formats: nested match/set or flat strongs+fields |
| `insert/update` on verse_context_group | verse_context_group | Verse Context patch operations |
| `insert/update` on verse_context | verse_context | Verse Context patch operations |

### 4.3 REPAIR patch catalogue (new Section 15 in CC-Instructions v3.2)
Four cascade reset types:

| Scenario | Patch naming | session_b_status target |
|----------|-------------|------------------------|
| STEP extraction re-run | `REPAIR-STEP-RERUN` | NULL |
| audit_word re-run | `REPAIR-AUDITWORD-RERUN` | Verse Context Reset |
| Verse Context re-run | `REPAIR-VC-RERUN` | Verse Context Reset |
| Analysis re-run | `REPAIR-ANALYSIS-RERUN` | Pre-Analysis Complete |

Each has specific field resets and delete_flag cascades documented in CC-Instructions v3.2 Sections 15.1–15.4.

### 4.4 Failure patch protocol (new Section 16 in CC-Instructions v3.2)
- When ANY patch is rejected: produce REPAIR failure patch before any other action
- Naming: `PATCH-{YYYYMMDD}-{nnn}-REPAIR-FAILURE-V1`
- Contains one `registry_note` operation recording the failure
- `session_b_status` carries current (unchanged) value
- Report to researcher with failure details

### 4.5 SESSIONB-COMPLETE patch (from Extraction v5.6)
- Naming: `PATCH-{YYYYMMDD}-{nnn}-SESSIONB-COMPLETE-V1`
- Sets `session_b_status = Session B Complete`
- Applied after all four extraction outputs confirmed

---

## 5. POOL-BASED PROCESSING — Must Update CLAUDE.md

### 5.1 Pool analysis dataset construction
CLAUDE.md does not document this significant Claude Code responsibility:

- **Trigger:** All words in a pool reach Pre-Analysis Complete
- **Pre-construction check:** Verify `verse_context_status = Complete` for all pool registries
- **Pool membership:** From `cluster_assignment` or WA-Registry-Management-Guide v5.6 Section 7a
- **File naming:** `wa-pool-{pool_id}-analysis-{date}.json`
- **Full JSON structure:** Defined in Analysis Instruction Annexure B

### 5.2 Pool membership controlled vocabulary
Pool IDs defined in RMG v5.6 Section 7a. 16 pools from not-shared through pool1-isolates. Claude Code must reference Section 7a directly.

### 5.3 Pool readiness monitoring
After every DataPrep patch:
1. Query all registries in same pool
2. Check if all at Pre-Analysis Complete or beyond
3. If ready: report to researcher (pool assembly is not automatic)

### 5.4 Processing sequence
Defined in RMG v5.6 Section 5.2 — 16-step sequence from independent words through Pool 1 Isolates.

---

## 6. AUDIT_WORD CHANGES — Must Update CLAUDE.md

### 6.1 Re-run requirements (new in CC-Instructions v3.2 Section 2.4)
When audit_word detects re-run for an existing registry:
1. **REPAIR patch verification (mandatory gate):** Check for `REPAIR-AUDITWORD-RERUN` patch. If not found: halt.
2. **STALE_TERM mechanism:** Authoritative path for wa_term_inventory updates on re-run. No delete/re-insert.
3. **Post-run NULL-status check:** After A6b, check for terms with `mti_terms.status = NULL`. Report to researcher.

### 6.2 Ready for Analysis COALESCE behaviour
- `audit_word` Step A10 sets `Ready for Analysis` only via COALESCE (when current status is NULL)
- Does NOT overwrite `Verse Context Reset`
- Important for existing 181 registries

---

## 7. EXPORT CHANGES — Must Update CLAUDE.md

### 7.1 New export command: `--export-registry`
```bash
python -m engine.engine --export-registry
```
- Produces: `word_registry.json`
- Required at start of each Extraction session
- Fields: no, word, cluster_assignment, session_b_status

### 7.2 Verse Context batch export
- New output directory: `data/exports/verse_context/`
- File naming: `wa-vcb-{batch_id}-extract-{date}.json`
- Produced by Claude Code batch construction logic

### 7.3 Post-patch outputs (updated)
- Final extract now requires both `session_b_status = Analysis Complete` AND `wa_session_b_dimensions` row
- Session D pointers auto-generated from SD_POINTER flags

---

## 8. PROGRAMME STATE QUERIES — Must Update CLAUDE.md

### 8.1 New queries needed
| Query | Purpose |
|-------|---------|
| Verse Context progress by status | `SELECT verse_context_status, COUNT(*)...` |
| Registries where VC complete and DataPrep gate open | Combination check |
| OWNER terms needing Verse Context | No verse_context record yet |
| Pool processing readiness (Stage 2) | Verse context + term_sharing_ratio check |
| XREF coverage for a registry | Unresolved XREF terms |

These are documented in CC-Instructions v3.2 Section 6.6 and VC-Instruction Sections 13–14.

---

## 9. MID-POOL INTERRUPTION HANDLING — NEW

From Analysis Instruction v5.6 Section 4.4:
- Mixed pool states (some words at Pre-Analysis Complete, some at Analysis Complete) = **system failure**
- Stop immediately
- Produce REPAIR mid-pool recovery patch for each word at Analysis Complete
- Reset to Pre-Analysis Complete
- Report to researcher
- Patch naming: `PATCH-{YYYYMMDD}-{nnn}-REPAIR-MIDPOOL-V1`

---

## 10. DOCUMENT REFERENCES — Must Update CLAUDE.md

### 10.1 Section 10 version table needs complete refresh

| Document | Version | Notes |
|----------|---------|-------|
| WA-Implementation-Instruction | v5 | Unchanged |
| WA-Reference | **v5.5** | Schema v3.8.0, Section 18 new |
| WA-Registry-Management-Guide | **v5.6** | Pool IDs, engine-derived fields note |
| WA-SessionB-DataPrep-Instruction | **v5.6** | Failure patch rules, legacy Ready for Analysis |
| WA-SessionB-Analysis-Instruction | **v5.6** | Mid-pool interruption, failure patch rules |
| WA-SessionB-Extraction-Instruction | **v5.6** | SESSIONB-COMPLETE patch, failure patches |
| **WA-SessionB-ClaudeCode-Instructions** | **v3.2** | REPAIR catalogue, failure patches, re-run requirements |
| **WA-VerseContext-Instruction** | **v1.5** | Entire Verse Context stage |
| **WA-VerseContext-SetupInstruction** | **v1.1** | M17/M18 migrations, status resets |
| **patch_specification** | **v1.5** | REPAIR patches, VC patch types, status workflow |

### 10.2 Setup Instruction (v1.1) tasks — all completed
- M17: source_category → dimensions, anchor_verses removed
- M18: verse_context_group, verse_context tables, verse_context_status field
- Status resets: 181 active registries to Verse Context Reset / In Progress
- apply_session_patch.py: updated to exempt VC patch types from session_b_status requirement
- Schema advanced to 3.8.0

---

## 11. ENGINE COMPONENT STATUS — Must Update CLAUDE.md

### 11.1 Engine/script status table (CC-Instructions v3.2 Section 12)

| Component | Status | Notes |
|-----------|--------|-------|
| constants.py | Schema version **3.7.0** | May need update to 3.8.0 — verify |
| migrate.py | M01–**M18** complete | Was M01-M15 in CLAUDE.md |
| apply_session_patch.py | Supports **VERSECONTEXT, VCGROUP, VCVERSE, REPAIR** | New patch types |
| word_export.py | Exports **verse_context data** | Verify |

### 11.2 Additional scripts (new)

| Script | Purpose |
|--------|---------|
| `_batch_extract.py` | Subprocess-isolated batch STEP extraction + audit_word |
| `_produce_final_extract.py` | Final registry extract from database |
| `_generate_programme_report.py` | Comprehensive programme status report |
| `_update_reference_doc.py` | Reference document update utility |

---

## 12. TERM OWNERSHIP — Must Update CLAUDE.md

### 12.1 XREF architecture (not in current CLAUDE.md)
- `wa_term_inventory.term_owner_type`: OWNER or XREF
- OWNER = canonical home, verses active, processed by Verse Context
- XREF = cross-reference copy, verses delete_flagged, verse context derived from OWNER
- Current scale: 5,518 OWNER terms, 1,470 XREF terms, 133,353 active verses

### 12.2 Term sharing fields on word_registry
- `unique_term_count` — engine-derived, Phase 1 state only
- `shared_term_count` — engine-derived, Phase 1 state only
- `term_sharing_ratio` — 0.0 to 1.0, engine-derived, Phase 1 state only
- These are NOT updated by Session B pipeline

---

## 13. CONTROLLED VOCABULARY ADDITIONS — Must Update CLAUDE.md

### 13.1 New flag codes in wa_session_research_flags
`SB_FINDING | SB_DIMENSION | SB_INNER_BEING | SD_POINTER | SD_CLUSTER`

### 13.2 New wa_term_phase2_flags codes
Multiple new codes added: `DIVINE_HUMAN_PARALLEL | ESCHATOLOGICAL_USAGE | WISDOM_LITERATURE_CONCENTRATION | METAPHOR_ROOT | RELATIONAL_DIRECTION | VOLITIONAL_COMPONENT | CROSS_TESTAMENT_SHIFT | ARAMAIC_FORM`

### 13.3 New crosslink type codes
`OVERLAPPING_DOMAIN | CAUSATIVE_CHAIN | THEMATIC_LINK`

### 13.4 New quality flag
`CONCRETE_PHYSICAL` — flagged but not excluded

### 13.5 Dimensional weight vocabulary
`PRIMARY | SECONDARY | PERIPHERAL` — used in final registry extract

### 13.6 Session D observation types expanded
Multiple new `pointer_type` and `pointer_subtype` values

---

## 14. REDUNDANT FIELD WARNINGS — Must Update CLAUDE.md

The Reference v5.5 and CC-Instructions v3.2 document several fields that pipeline stages must NOT write to:

| Field | Table | Note |
|-------|-------|------|
| `god_as_subject` | wa_term_inventory | Superseded by mti_term_flags mechanism |
| `somatic_link` | wa_term_inventory | Superseded by mti_term_flags |
| `status_note` | wa_term_inventory | NULL across all active records, no pipeline purpose |
| `inference_note` | word_registry | Researcher-set only, pipeline must never overwrite |
| `status_note` | mti_terms | Written by Session A engine only (audit_word A10), not by Session B |

---

## 15. CURRENT PROGRAMME STATE — Context Update

From CC-Instructions v3.2 Section 2.6 and RMG v5.6:
- **181** active registries at `Verse Context Reset` / `In Progress`
- **31** excluded registries
- **All v5 implementation tasks complete** (Tasks 1–8)
- **Schema at v3.8.0** (M01–M18)
- **Zero-term registries resolved** — all 6 non-excluded extracted and audited
- **Stage 1 (Verse Context sweep)** is the current priority

---

## SUMMARY — What CLAUDE.md Needs

### Must Add (entirely new):
1. Verse Context pipeline stage (Section 2 above)
2. Verse Context tables in schema (Section 1.3)
3. verse_context_status field and lifecycle (Section 3)
4. Patch specification reference document (Section 4.1)
5. REPAIR patch catalogue (Section 4.3)
6. Failure patch protocol (Section 4.4)
7. Pool-based processing and pool analysis dataset (Section 5)
8. XREF architecture and term ownership (Section 12)
9. Mid-pool interruption handling (Section 9)
10. New programme state queries (Section 8)

### Must Update (content changed):
1. Schema version: 3.7.0 → 3.8.0 (Section 1.1)
2. Migrations: M01-M15 → M01-M18 (Section 1.2-1.3)
3. Document version table (Section 10)
4. session_b_status vocabulary — add Verse Context Reset, note Ready for Analysis as legacy (Section 3.2)
5. Patch types — add VERSECONTEXT, VCGROUP, VCVERSE, REPAIR (Section 4.2)
6. Engine component status table (Section 11)
7. Key Constants — verify EXPECTED_SCHEMA_VERSION (Section 1.4)
8. Controlled vocabulary additions (Section 13)
9. Programme state and current work context (Section 15)
10. audit_word re-run requirements (Section 6)
11. Redundant field warnings (Section 14)

### Must Remove or Correct:
1. Registry Management Guide version listed as "v7" — should be v5.6
2. `anchor_verses` field references (removed in M17)
3. "v5.1/v5.2" references throughout — now v5.5/v5.6

---

*Produced 2026-03-30 by Claude Code for researcher review before CLAUDE.md update*
