# Data Preparation Pipeline

> Framework B — Soul Word Analysis Programme
> Reference document | April 2026

This document describes the five-stage data preparation pipeline that takes a raw English word from initial registration through to Session B readiness. Each stage must complete before the next begins.

```
Stage 1: Registry Creation
    |
Stage 2: STEP Data Extraction
    |
Stage 3: Database Population (audit_word)
    |
Stage 4: Verse Context Classification
    |
Stage 5: Dimension Review
    |
    v
Session B (Data Audit, Analysis, Word Articulation)
```

---

## Stage 1: Registry Creation

Register the English word in `word_registry`, establishing it as a programme-scoped research target.

**Command:**
```bash
python -m engine.engine --register --word="<word>" --source="<source_list>"
```

**What happens:**
- Assigns a sequential registry number (`no`) — the human-readable identifier used in all file naming and cross-references
- Sets `phase1_status = 'Pending'`, `automation_eligible = 1`
- Records `source_list` (High Confidence, Low Confidence / Inferred, Missing Inner Being Words, or Programme Addition)
- Optional `category_hint` for broad semantic navigation

**Key fields set:**
| Field | Value |
|-------|-------|
| `no` | Next sequential number (MAX + 1) |
| `phase1_status` | Pending |
| `automation_eligible` | 1 |
| `source_list` | As specified |
| `cluster_assignment` | Set later (C01–C22) |

**Output:** A new row in `word_registry`. No data extraction yet.

---

## Stage 2: STEP Data Extraction

Pull lexical and verse data from the local STEP Bible API for all Strong's numbers associated with the word.

**Command:**
```bash
python scripts/word_study_extract.py --word <word> [--anchors H1234,G5678]
```

**What happens:**
- Queries the local STEP Bible server (`localhost:8989`) for all Strong's numbers tagged to the English word in the ESV
- For each Strong's number, fetches:
  - Lexical data: gloss, detailed meaning text, related words, root family
  - All ESV verse occurrences (paginated — STEP caps at 60 per request, client splits by canonical sections)
  - Raw STEP HTML per verse (for span filtering / Strong's confirmation)
- Expands term clusters: sub-glosses, related terms, root family members

**Output:**
```
data/discovery/{nnn}_{word}_step_data_{YYYYMMDD}.json   (structured data)
data/discovery/{nnn}_{word}_step_data_{YYYYMMDD}.md     (human-readable summary)
```

The discovery JSON is the input for Stage 3. No database writes occur at this stage.

---

## Stage 3: Database Population (audit_word)

Ingest the STEP discovery data into the database, creating term records, verse records, and all supporting structures in a single atomic pass.

**Command:**
```bash
python -m engine.engine --mode=audit_word --registry=N
```

**What happens (steps A1–A11):**

| Step | Action |
|------|--------|
| Pre-A1 | Lock sentinel set, run log opened |
| A1 | Registry display and confirmation |
| A2 | DB snapshot and structural completeness check |
| A3 | Load and validate the latest Step 1 JSON |
| A4 | Build gap report: what's new, stale, missing, or orphaned across terms, related words, verses, and verse-term links |
| A5 | Display gap report |
| A6 | Apply all changes in one transaction per stream: insert new terms, update stale terms, flag DB-only terms, insert/update verses and verse-term links |
| A6b | Term classification (data-driven filters: candidate_delete, extracted, extracted_thin) |
| A7 | Meaning parse: structured breakdown of meaning text into senses, stems, LSJ entries |
| A8 | Quality flag reset and re-derivation (DATA_COVERAGE group only — 7 flag codes) |
| A9 | Audit checks WR-01 through WR-20, write word_run_state |
| A10 | Registry and file index update, close run, set `last_automation_run = 'AUDITED'` |
| A11 | Full-word JSON export for downstream consumption |

**Tables populated:**
- `wa_file_index` — one row per imported JSON
- `wa_term_inventory` — per-term metadata (OWNER or XREF classification)
- `mti_terms` — one record per Strong's number programme-wide
- `wa_verse_records` — one row per term-in-verse occurrence
- `wa_verse_term_links` — verse-to-term cross-references
- `wa_term_related_words` — lexical relatives
- `wa_term_root_family` — root family membership
- `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem` — structured meaning parse
- `wa_data_quality_flags` — engine-derived quality indicators

**Key concepts:**
- **OWNER vs XREF:** Each Strong's number has exactly one OWNER registry (canonical analytical home) and may have XREF copies in other registries. XREF verse records are delete-flagged — analysis runs on OWNER data only.
- **No physical deletes:** Removals use `delete_flagged = 1`.
- **Phase 2 and research flags are untouched** — the engine only manages DATA_COVERAGE flags.

**Output:**
- Database fully populated for this registry
- `phase1_status = 'Complete'`
- Full word JSON export at `data/exports/`

---

## Stage 4: Verse Context Classification

Classify all active OWNER-term verses by inner-being relevance, group them by contextual meaning, and designate anchor verses. This stage sits between Phase 1 completion and Session B.

**Governed by:** WA-VerseContext-Instruction-v2.5

### 4a. Batch Construction (Claude Code)

Claude Code queries the database and builds batch JSONs for Claude AI:
- **Scope:** OWNER terms only (`term_owner_type = 'OWNER'`, `mti_terms.status IN ('extracted', 'extracted_thin')`)
- **Size:** 2,000–2,500 unclassified verses per batch (never splits a term across batches)
- **Priority:** Unclassified terms first, ordered by `owning_registry_fk` ascending
- **Batch ID:** Sequential VCB-001, VCB-002, etc.
- **Output:** `data/exports/verse_context/wa-vcb-{batch_id}-extract-{date}.json`

### 4b. Verse Classification (Claude AI)

For each verse, Claude AI determines:
- **Relevance:** Does this verse engage the inner being through this term? (yes/no, with `set_aside_reason` for no)
- **Contextual grouping:** Relevant verses grouped by the inner-being characteristic they engage (characteristic-perspective, not term-centric)
- **Anchor designation:** One or more canonical citations per group — the primary Session B analysis input

### 4c. Patch Application (Claude Code)

- Applies VERSECONTEXT patch: resolves `group_code` to integer IDs, inserts `verse_context_group` and `verse_context` records
- Validates consistency rules (R1–R4): set-aside rows clean, anchor rows clean, related rows have active anchors
- Propagates XREF coverage: XREF terms share `mti_term_id` with their OWNER — no separate records needed

### 4d. Registry Completion

After each patch, Claude Code checks per affected registry:
1. All OWNER terms (with verses) have `verse_context` records
2. All XREF terms have an OWNER that has `verse_context` records
3. If both satisfied: `verse_context_status = 'Complete'`
4. Re-export full word JSON — this opens the DataPrep gate

**Scale:** 133,353 active OWNER-term verses across 182 registries, processed in 34+ batches.

---

## Stage 5: Dimension Review

Review contextual meaning groups at cluster level, discern what dimensions emerge from the data, assign dominant subjects, and capture Session B/D pointers.

**Governed by:** WA-DimensionReview-Instruction-v2.2

### 5a. Extract Construction (Claude Code)

Three extracts built per cluster:
```bash
python scripts/build_dimension_extract.py --cluster C17          # cluster extract
python scripts/build_dimension_extract.py --rootfamily C17       # root family extract
python scripts/build_dimension_extract.py --pointers C17         # existing pointers extract
```

### 5b. Analytical Session (Claude AI)

Three phases, run per cluster:

| Phase | Purpose |
|-------|---------|
| **A — Cluster Assignment Review** | Validate that words are correctly assigned to this cluster |
| **B — Group Quality Review** | Assess contextual meaning group descriptions; screen for term-centric framing (QA-TERMCENTRIC); correct to characteristic-perspective where needed; verify anchor verse data |
| **C — Dimension Discernment** | Read groups, name what dimensions emerge, assign `dominant_subject` per group, progressively refine dimension assignments from hypothesis to confirmed |

**Foundational principle:** The dimension always follows the verse. Read the group. Name what you see. Never fit a group into a dimension that does not genuinely describe it.

### 5c. Per-Registry Patch (Claude AI + Claude Code)

- Produced immediately after each registry's Phase C completes
- Populates `wa_dimension_index`: dimension labels, confidence levels, dominant_subject
- Locks confirmed dimensions via `manual_override` flag
- Captures Session B/D observations as `SD_POINTER`, `SB_FINDING`, `SB_DIMENSION` flags in `wa_session_research_flags`
- Final registry patch includes cluster stamp

### 5d. Completion

- All registries in the cluster stamped
- Cluster stamp set in `wa_dim_review_cluster_log`
- Session B DataPrep gate is now open for all registries in the cluster

---

## Status Tracking Summary

Two parallel status tracks on `word_registry` govern pipeline progress:

| Track | Field | Values |
|-------|-------|--------|
| Session B | `session_b_status` | NULL → Verse Context Reset → Ready for Analysis → Pre-Analysis Complete → Analysis Complete → Session B Complete |
| Verse Context | `verse_context_status` | NULL → In Progress → Complete |

Additional status indicators:
| Field | Table | Purpose |
|-------|-------|---------|
| `phase1_status` | `word_registry` | Phase 1 extraction: Pending → Complete / Excluded |
| `mti_terms.status` | `mti_terms` | Per-term: NULL → extracted / extracted_thin / candidate_delete / delete |
| `dim_review_status` | `wa_dimension_index` | Per-group dimension confidence |
| `last_automation_run` | `word_registry` | Lock sentinel (IN_PROGRESS) or completion marker (AUDITED) |

---

## Programme Scale (April 2026)

| Metric | Count |
|--------|-------|
| Total registries | 214 |
| Active registries (Phase 1 Complete) | 183 |
| OWNER terms | 5,518 |
| XREF terms | 1,470 |
| Active verses (OWNER) | 133,353 |
| Clusters | C01–C22 |
| VC batches processed | 34+ |
