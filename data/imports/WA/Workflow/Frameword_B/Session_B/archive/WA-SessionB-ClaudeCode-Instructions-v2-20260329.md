# WA-SessionB-ClaudeCode-Instructions-v2-20260329

> Claude Code consolidated instruction document for Framework B v5.
> Version 2 — 2026-03-29.
> Supersedes: WA-SessionB-ClaudeCode-Instructions (undated, last updated 2026-03-29 for schema v3.7.0).
> Change note v2: Section 14 added — full Verse Context operational specification including batch construction, three patch types, registry completion check, re-extraction trigger, integrity validation, and pool analysis dataset export. Section 6 updated with Verse Context monitoring queries. Section 8 updated with new status values and patch types. Section 12 updated to schema v3.8.0. Footer updated.

---

## 0. Document Sources

This document consolidates Claude Code tasks and responsibilities from:

| Source Document | What Was Extracted |
|----------------|-------------------|
| Session-A-v9-Architecture-v4-Final | Data foundation pipeline — STEP extraction, audit_word, JSON export |
| engine/audit_word.py (docstring) | Steps Pre-A1 through A11, flag ownership, classification filters |
| WA-Implementation-Instruction-v5 | Tasks 1-8 (schema, tables, clustering, patches) |
| WA-Reference-v5 | Controlled vocabulary, naming conventions, schema reference |
| WA-Registry-Management-Guide-v5 | Programme state queries, periodic review support |
| WA-SessionB-DataPrep-Instruction-v5 | Patch application, JSON re-export, validation |
| WA-SessionB-Analysis-Instruction-v5 | JSON export for analysis input |
| WA-SessionB-Extraction-Instruction-v5 | Analysis patch application, completion confirmation |

---

## 1. Claude Code's Role — Boundary Definition

Claude Code is the **database engine**. It applies patches, exports JSON, queries the database, runs schema migrations, and validates data integrity. It does **not**:

- Classify terms or make scope decisions
- Assess analytical relevance of terms
- Read verses and judge their significance
- Make synthesis or interpretation claims
- Decide evidential status

All classification, scope judgement, and analytical work belongs to **Claude AI**. Claude Code executes database operations based on validated instructions and patch files.

---

## 2. Data Foundation — Building the Base Layer for Session B

Claude Code's foundational and ongoing responsibility is producing the word JSON export that serves as the starting input for every Session B analysis. This involves four sequential operations, governed by the Session A v9 Architecture Specification (`docs/Session-A-v9-Architecture-v4-Final-20260318.md`) and the engine itself.

### 2.1 The End-to-End Pipeline

```
Register word → Extract STEP data → Audit (populate DB) → Export JSON
                                                             ↓
                                               Session B DataPrep begins
```

Every word must pass through this pipeline before Session B can start. The export is the deliverable — the complete word data package that Claude AI loads for analysis.

### 2.2 Step 1 — Register Word

```bash
python -m engine.engine --register --word="compassion" --source="High Confidence"
```

Creates a `word_registry` row. Write scope: word_registry INSERT only. No biblical data is written. The registry number (`no`) becomes the word's permanent identifier used in all file naming and cross-references.

### 2.3 Step 2 — STEP Data Extraction

```bash
python scripts/word_study_extract.py --word compassion [--anchors H7356,G4698]
```

Queries the local STEP Bible server (`http://localhost:8989`) to pull:
- All Strong's numbers associated with the English word (via `meanings=` endpoint)
- Vocabulary data per term (gloss, meaning, related words, occurrence count)
- Full verse corpus per term (ESV text, with STEP HTML for span filtering)

**Output:** `data/discovery/{nnn}_{word}_step_data_{YYYYMMDD}.json`

**Key technical notes:**
- Uses the `meanings=` API endpoint (not `text=+`) to match STEP's "Related words" panel — catches terms like H2734 that the ESV never translates with the literal English word
- STEP API caps results at 60 per request; the client uses canonical section splits for complete coverage
- The `--anchors` flag adds specific Strong's numbers that should always be included

### 2.4 Step 3 — Audit Word (populate database)

```bash
python -m engine.engine --mode=audit_word --registry=N [--extract-file=PATH]
```

This is the core data population pipeline (steps Pre-A1 through A11):

| Step | What It Does |
|------|-------------|
| Pre-A1 | Lock sentinel + open run log |
| A1 | Registry display + confirmation |
| A2 | DB snapshot + structural completeness check (bypasses STOP if Step 1 JSON available for first-time population) |
| A3 | Load + validate Step 1 JSON (auto-selects latest unless --extract-file given) |
| A4 | Build gap report — compares JSON against DB state (Term / Related / Verse / VTL streams) |
| A5 | Display gap report |
| A6 | Apply changes — single transaction per stream: NEW_TERM inserts, STALE_TERM updates, DB_ONLY_TERM flagging, verse inserts with span filtering |
| A6b | Term classification — data-driven filters (no interpretation): F1-F5 classify NULL-status terms based on verse count and analytical signals |
| A7 | Meaning handler — parse meaning text into wa_meaning_parsed/sense/stem/lsj |
| A8 | Quality flag reset — DATA_COVERAGE group only, then re-derive via flag_engine.py |
| A9 | Audit checks WR-01–WR-20 + write word_run_state |
| A10 | Registry + file index update, close run, set last_automation_run = 'AUDITED' |
| A11 | Full-word JSON export |

**Key behaviours:**
- Auto-approve by default — use `--interactive` to enable per-item gates
- No physical deletes — deletions are flagged with `delete_flagged=1`
- Only engine-derivable flags (DATA_COVERAGE group) are reset and re-derived; Phase 2 flags and session research flags are never touched
- Span filtering: only verses where the queried Strong's number is confirmed in the original-language STEP HTML span are stored

**Flag ownership boundaries (strict):**

| Category | Table | Owner | Engine Touches? |
|----------|-------|-------|----------------|
| A — Engine-derivable | wa_data_quality_flags | Engine (flag_engine.py) | Yes — reset in A8, re-derived |
| B — Term-level analytical | wa_term_phase2_flags | Researcher (Claude AI) | **Never** |
| C — Session research | wa_session_research_flags | Researcher (Claude AI) | **Never** — written by apply_session_patch.py only |

### 2.5 Step 4 — JSON Export (the Session B deliverable)

The export runs automatically as step A11 of audit_word, or manually:

```bash
python -m engine.engine --export-word --registry=N
```

**Output:** `data/exports/{word}_{registry}_full_{YYYYMMDD}_v{N}.json`

The export includes: registry meta, file index, term inventory (with meaning parse, quality flags, phase2 flags, related words, root family, MTI data), verse corpus, cross-registry links, session research flags, patch history, and statistics.

**Version auto-incrementing:** Multiple exports on the same day produce v1, v2, v3, etc. Previous versions are retained.

This JSON file is what Claude AI loads at the start of Session B DataPrep (WA-SessionB-DataPrep-Instruction-v5).

### 2.6 Ongoing Obligations

The data foundation is not a one-time task. Claude Code must:

- **Run audit_word for remaining registries** — 144 words at Ready for Analysis; all have been extracted and audited with current JSON exports
- **Re-export after patches** — every time Claude Code applies a pre-analysis or analysis patch, it must re-export the JSON so Claude AI has current data
- **Zero-term registries** — resolved. All 6 non-excluded zero-term registries have been extracted and audited (consciousness, meekness, resolve, sensuality, energy, resentment)
- **Maintain the STEP client** — the `step_client.py` and `word_study_extract.py` scripts are Claude Code's tools; bugs and enhancements are Claude Code's responsibility

### 2.7 Reference Documents

| Document | Location | What It Covers |
|----------|----------|---------------|
| Session A v9 Architecture Spec | `docs/Session-A-v9-Architecture-v4-Final-20260318.md` | Full specification: governing principles, execution modes, table schemas, step-by-step logic |
| audit_word.py docstring | `engine/audit_word.py` (lines 1-91) | Steps Pre-A1 to A11, flag ownership, classification filters, key behaviours |
| CLAUDE.md Section 4 | `CLAUDE.md` | Engine modes, key flags, audit checks summary |

---

## 3. Implementation Tasks (from WA-Implementation-Instruction-v5)

These are the schema and programme operations Claude Code must execute. They are ordered by dependency — complete earlier tasks before later ones. **Do not execute until researcher approval.**

### Task 1 — Add cluster_assignment to word_registry

```sql
ALTER TABLE word_registry ADD COLUMN cluster_assignment TEXT DEFAULT 'unassigned';
```

**Validation:**
```sql
SELECT COUNT(*) FROM word_registry WHERE cluster_assignment IS NULL;
-- Expected: 0
```

### Task 2 — New Flag Types for Session B JSON Mapping

Insert new flag_code values into the system:

| flag_code | Purpose |
|-----------|---------|
| SB_FINDING | Session B key finding — from key_findings array in Session B JSON |
| SB_DIMENSION | Session B dimensional profile record — one per active dimension |
| SB_INNER_BEING | Session B inner being standing classification |
| SD_POINTER | Session D pointer — cross-registry structural observation from Session B |
| SD_CLUSTER | Session D cluster maturity flag — researcher-triggered when cluster is ready |

**Validation:** Confirm new flag_codes are accepted by the patch applicator by running a test insert for each code type with a dummy registry.

### Task 3 — Create Session D Capture Tables

Four new tables:

```sql
CREATE TABLE IF NOT EXISTS session_d_verse_links (
  id INTEGER PRIMARY KEY,
  run_id TEXT NOT NULL,
  verse_ref TEXT NOT NULL,
  registry_ids TEXT NOT NULL,
  terms_involved TEXT,
  overlap_count INTEGER,
  threshold_met INTEGER DEFAULT 0,
  gate TEXT NOT NULL,
  raised_date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS session_d_term_links (
  id INTEGER PRIMARY KEY,
  run_id TEXT NOT NULL,
  strongs_id TEXT NOT NULL,
  transliteration TEXT,
  registry_data TEXT NOT NULL,
  status_divergence INTEGER DEFAULT 0,
  gate TEXT NOT NULL,
  raised_date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS session_d_observations (
  id INTEGER PRIMARY KEY,
  run_id TEXT NOT NULL,
  observation_id TEXT NOT NULL UNIQUE,
  observation_type TEXT NOT NULL,
  registries_implicated TEXT NOT NULL,
  terms_implicated TEXT,
  structural_note TEXT,
  source_refs TEXT,
  gate TEXT NOT NULL,
  researcher_flag INTEGER DEFAULT 0,
  raised_date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS session_d_runs (
  id INTEGER PRIMARY KEY,
  run_id TEXT NOT NULL UNIQUE,
  run_date TEXT NOT NULL,
  cluster_ref TEXT,
  registries_in_scope TEXT NOT NULL,
  registries_completed_at_run INTEGER,
  session_b_sources TEXT,
  run_summary TEXT,
  json_filename TEXT
);
```

**Validation:**
```sql
SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'session_d%';
-- Expected: session_d_verse_links, session_d_term_links, session_d_observations, session_d_runs
```

### Task 4 — Registry Clustering Operation

**Claude Code's role in clustering:**
1. Export the full word registry (all 212 words with word label, source_category, phase1_status, session_b_status)
2. Provide export to Claude AI for clustering judgement
3. Receive validated cluster assignments from researcher
4. Apply UPDATE operations to word_registry.cluster_assignment for all 212 words

**Clustering output file:** `wa-clusters-{YYYYMMDD}.json`

**JSON template:**
```json
{
  "meta": {
    "json_template_version": "clusters_v1.0",
    "json_filename": "wa-clusters-{YYYYMMDD}.json",
    "run_date": "{YYYYMMDD}",
    "total_registries": 212,
    "total_clusters": 0
  },
  "clusters": [
    {
      "cluster_id": "C01",
      "cluster_label": "{neutral label}",
      "word_count": 0,
      "words": [
        {"registry_id": 0, "word": "{word}", "session_b_status": "{status}"}
      ]
    }
  ]
}
```

**Database update pattern:**
```sql
UPDATE word_registry SET cluster_assignment = '{cluster_id}' WHERE no = {nnn};
```

### Task 5 — Zero-Term Registry Investigation

Investigate 13 registries with no terms: ambition, consciousness, distress, meekness, pride, resolve, sensuality, sorrow, wisdom, wrath, energy, resentment, being.

**Investigation query:**
```sql
SELECT wr.no, wr.word, wr.phase1_status, wr.phase1_term_count,
       COUNT(ti.id) as actual_terms
FROM word_registry wr
LEFT JOIN wa_file_index fi ON fi.word_registry_fk = wr.id
LEFT JOIN wa_term_inventory ti ON ti.file_id = fi.id
WHERE wr.phase1_term_count = 0 OR wr.phase1_term_count IS NULL
GROUP BY wr.no, wr.word
ORDER BY wr.no;
```

**Resolution options:**
- Data linkage issue — fix wa_file_index.word_registry_fk and re-query
- Phase 1 not run — run Phase 1 extraction
- Genuine gap — confirm as Conceptual Word Register candidate, document in Session D orientation

### Task 6 — PATCH_SPEC Update for New Patch Types

Register new patch_type values:

| patch_type | When used |
|-----------|-----------|
| SESSIONB | Analysis completion patch — from WA-SessionB-Extraction-Instruction-v5 |
| SESSIOND | Session D discovery JSON — from WA-SessionD-Orientation-v2 |
| PREANALYSIS | Pre-analysis classification patch (existing) |
| CLUSTERING | Cluster assignment patch — from Task 4 |

### Task 7 — Session D Discovery JSON Template

The Session D JSON maps to four tables: session_d_runs, session_d_verse_links, session_d_term_links, session_d_observations. Claude Code must be able to ingest and apply these when Session D runs begin.

**File naming:** `wa-{cluster_label}-sessiond-{YYYYMMDD}.json`

### Task 8 — Session B JSON Database Preparation

New fields and tables required before Session B JSON extraction patches can be applied.

**8.2 New fields on wa_term_inventory:**
```sql
ALTER TABLE wa_term_inventory ADD COLUMN evidential_status TEXT DEFAULT NULL;
ALTER TABLE wa_term_inventory ADD COLUMN retention_note TEXT DEFAULT NULL;
```

Valid values for evidential_status: confirmed | plausible | uncertain | instrumental | relational_only

**8.3 New fields on word_registry:**
```sql
ALTER TABLE word_registry ADD COLUMN sb_classification TEXT DEFAULT NULL;
ALTER TABLE word_registry ADD COLUMN sb_classification_reasoning TEXT DEFAULT NULL;
ALTER TABLE word_registry ADD COLUMN carry_forward INTEGER DEFAULT 1;
```

Valid values for sb_classification: confirmed_characteristic | plausible | uncertain | instrumental | relational_only

**8.4 New table — wa_session_b_dimensions:**
```sql
CREATE TABLE IF NOT EXISTS wa_session_b_dimensions (
  id INTEGER PRIMARY KEY,
  registry_id INTEGER NOT NULL,
  file_id INTEGER,
  relational_environment INTEGER DEFAULT 0,
  relational_environment_note TEXT,
  spirit_soul_body INTEGER DEFAULT 0,
  spirit_soul_body_note TEXT,
  inner_operations INTEGER DEFAULT 0,
  inner_operations_note TEXT,
  being INTEGER DEFAULT 0,
  being_note TEXT,
  raised_date TEXT NOT NULL,
  session_b_instruction TEXT NOT NULL
);
```

**8.5 New table — wa_session_b_findings:**
```sql
CREATE TABLE IF NOT EXISTS wa_session_b_findings (
  id INTEGER PRIMARY KEY,
  finding_id TEXT NOT NULL UNIQUE,
  registry_id INTEGER NOT NULL,
  file_id INTEGER,
  finding_type TEXT NOT NULL,
  finding TEXT NOT NULL,
  anchor_verses TEXT,
  raised_date TEXT NOT NULL,
  session_b_instruction TEXT NOT NULL
);
```

finding_type valid values: etymology | verse_pattern | term_behaviour | theological_note | anomaly

**8.6 Updated database mapping (replaces interim mappings):**

| JSON section | Definitive database target |
|-------------|---------------------------|
| terms — evidential_status | wa_term_inventory.evidential_status |
| terms — retention_note | wa_term_inventory.retention_note |
| dimensions — all fields | wa_session_b_dimensions (new table) |
| inner_being_standing — all fields | word_registry.sb_classification + sb_classification_reasoning + carry_forward |
| key_findings — all fields | wa_session_b_findings (new table) |
| data_flags — all fields | wa_term_phase2_flags or wa_session_research_flags per flag type |
| session_d_pointers — all fields | wa_session_research_flags with flag_code SD_POINTER |

**Validation:**
```sql
SELECT evidential_status, retention_note FROM wa_term_inventory LIMIT 1;
SELECT sb_classification, sb_classification_reasoning, carry_forward FROM word_registry LIMIT 1;
SELECT name FROM sqlite_master WHERE type='table'
  AND name IN ('wa_session_b_dimensions','wa_session_b_findings');
```

**Task dependency order:** Task 1 -> Task 2 -> Task 3 -> Task 8 -> Task 4 -> Task 5 -> Task 6

---

## 4. Patch Application — The Core Operational Loop

Claude Code's most frequent operational role is receiving and applying patches from Claude AI. Two patch types flow through Claude Code:

### 4.1 Pre-Analysis Patches (from DataPrep)

**Trigger:** Claude AI completes data preparation and produces a patch file.

**Handoff format received from Claude AI:**
```
PATCH SUBMISSION TO CLAUDE CODE
Patch file: wa-{nnn}-{word}-patch-{date}.json
Action required: Apply patch, update session_b_status to Pre-Analysis Complete,
  re-export JSON as wa-{nnn}-{word}-extract-{date}.json
Validation: Confirm term statuses updated and verse counts clean in re-export.
```

**Claude Code actions:**
1. Validate patch structure (patch_id not previously applied, all strongs exist, all flag_labels unique, registry_id valid, session_b_status present in _patch_meta)
2. Apply all operations in a single transaction — all or nothing
3. Log patch_id to engine_run_log
4. Update session_b_status on word_registry
5. Re-export JSON: `python -m engine.engine --export-word --registry=N`
6. Confirm completion

**Automated operation types:**
- `update_mti_status` — update status on single term in mti_terms
- `bulk_update_mti_status` — update multiple terms to same status
- `bulk_confirm_candidate_delete` — confirm candidate_delete as delete
- `insert` on wa_session_research_flags — insert research flags
- `update_registry` — update field on word_registry (always final operation)
- `registry_note` — documentation only, no DB action

**Manual operation types (require direct Claude Code intervention):**
- `reassign_verses` — move verse records between term inventories
- `restore_delete_flagged` — restore incorrectly flagged terms
- `add_cross_registry_links` — insert cross-registry link records
- `schema_investigation_note` — investigate data anomaly

**Validation rules (reject entire patch on failure):**
- patch_id must not be previously applied (check engine_run_log)
- All strongs_number values must exist in mti_terms
- All flag_label values must be unique
- All registry_id values must exist in word_registry
- session_b_status must be present in _patch_meta
- All operations in single transaction

### 4.2 Analysis Completion Patches (from Extraction)

**Trigger:** Claude AI completes Session B JSON extraction for a batch of ~5 registries.

**Handoff format:**
```
PATCH SUBMISSION TO CLAUDE CODE
Patch file: wa-{nnn}-{word}-patch-{date}.json
Action required: Apply analysis completion patch. Update session_b_status to
  'Analysis Complete'. Confirm all research flag inserts recorded.
Validation: Confirm session_b_status updated in word_registry.
  Confirm flag records inserted in wa_session_research_flags.
```

**Required operations in analysis patches:**
- `update_registry` — session_b_status = 'Analysis Complete'
- `insert` on wa_session_research_flags — one per key finding (SB_FINDING)
- `insert` on wa_session_research_flags — one per Session D pointer (SD_POINTER)
- `insert` on wa_session_research_flags — dimensional profile records (SB_DIMENSION)
- `registry_note` — recording analysis and JSON filenames

**Patch naming:** `PATCH-{YYYYMMDD}-{nnn}-ANALYSIS-V1`

---

## 5. JSON Export — Providing Data to Claude AI

Claude Code exports word data for Claude AI consumption at two points:

### 5.1 Before Data Preparation
```bash
python -m engine.engine --export-word --registry=N
```
Output: `data/exports/{word}_{registry}_{scope}_{YYYYMMDD}_v{N}.json`

- **Scope**: `full` (pre-analysis) or `final` (v5.2 extraction complete — requires both session_b_status at Analysis Complete AND wa_session_b_dimensions row present)
- **Version**: Auto-increments per day (v1, v2, v3, etc.)

### 5.2 After Patch Application (Re-export)
Same command, producing a fresh export reflecting the patched state. Post-analysis exports automatically use scope `final`.

### 5.3 Post-Patch Outputs (v5.2)

After an analysis completion patch is applied and confirmed, two additional files are produced:

- **Final registry extract**: `data/exports/{word}_{registry}_final_{YYYYMMDD}_v{N}.json` — cross-table view for Session D (produced by Claude AI per WA-SessionB-Extraction-Instruction-v5.2 Section 8.1)
- **Session D pointers**: `data/exports/session_d/wa-{nnn}-{word}-sessiond-pointers-{YYYYMMDD}.json` — auto-generated by apply_session_patch.py from SD_POINTER flags in wa_session_research_flags

The export includes: registry meta, term inventory, verse corpus, existing flags, evidential_status, session_b_status, and session research flags — everything Claude AI needs for analysis and post-patch output production.

---

## 6. Programme State Queries

Claude Code runs these queries to assess programme state (from WA-Registry-Management-Guide-v5 Section 6).

### 6.1 Session B Progress by Status
```sql
SELECT session_b_status, COUNT(*) as count
FROM word_registry GROUP BY session_b_status ORDER BY session_b_status;
```

### 6.2 Words Ready for Analysis
```sql
SELECT no, word FROM word_registry
WHERE session_b_status IN ('Ready for Analysis', 'Pre-Analysis Complete')
ORDER BY no;
```

### 6.3 Words Not Yet Started
```sql
SELECT no, word, phase1_status FROM word_registry
WHERE session_b_status IS NULL ORDER BY no;
```

### 6.4 Zero-Term Registries
```sql
SELECT no, word FROM word_registry
WHERE phase1_term_count = 0 OR phase1_term_count IS NULL ORDER BY no;
```

### 6.5 Cluster Progress
```sql
SELECT cluster_assignment, COUNT(*) as total,
  SUM(CASE WHEN session_b_status = 'Session B Complete' THEN 1 ELSE 0 END) as complete
FROM word_registry GROUP BY cluster_assignment;
```

---

## 7. File Naming Conventions

All files follow these patterns (from WA-Reference-v5):

### 7.1 Word-Level Files
`wa-{nnn}-{word}-{scope}-{YYYYMMDD}.{ext}`

| Scope token | File type |
|------------|-----------|
| analysis | Session B narrative — .docx |
| extract | Word JSON export from database — .json |
| json | Session B structured JSON — .json |
| patch | Patch file for Claude Code — .json |
| final | Final cross-table registry extract (post-patch) — .json |
| sdpointers | Session D pointers file (post-patch, evaluative) — .json |

### 7.2 Programme-Level Files
| Pattern | File type |
|---------|-----------|
| wa-clusters-{date}.json | Clustering run output |
| wa-{cluster}-sessiond-{date}.json | Session D discovery JSON |
| wa-programme-review-{date}.docx | Periodic registry review |

### 7.3 Patch ID Convention
`PATCH-{YYYYMMDD}-{registry_no}-{type}-V{n}`

**Version incrementing:** The `V{n}` suffix tracks multiple patches for the same registry in the same session. First patch is V1. If a correction or follow-up patch is required, increment to V2, V3, etc. The applicator rejects duplicate `patch_id` values — every patch must have a unique ID.

**File naming mirrors patch_id:** `wa-{nnn}-{word}-patch-{YYYYMMDD}.json` for V1. For subsequent versions: `wa-{nnn}-{word}-patch-{YYYYMMDD}-V2.json`, `-V3.json`, etc.

Examples:

- `PATCH-20260327-097-PREANALYSIS-V1` — first pre-analysis patch
- `PATCH-20260327-097-PREANALYSIS-V2` — correction to first patch
- `PATCH-20260327-097-ANALYSIS-V1` — analysis completion patch (different type, resets to V1)
- `PATCH-20260327-CLUSTERS-V1` — programme-level patch

---

## 8. Controlled Vocabulary Quick Reference

### 8.1 mti_terms.status
| Value | When to use |
|-------|-------------|
| extracted | Term is genuine vocabulary for this registry |
| extracted_thin | Relevant but data is thin — include with caution |
| extracted_theological_anchor | Primary theological anchor for this registry |
| delete | Confirmed bleed, peripheral, or non-registry vocabulary |
| candidate_delete | Likely bleed, not yet confirmed — flag for researcher |
| excluded | Excluded from programme scope |
| xref_{word} | Belongs primarily to another registry |
| phase2_enrichment | Needs deeper research before classification |

### 8.2 word_registry.session_b_status
| Value | Meaning |
|-------|---------|
| NULL | Phase 1 excluded or not yet audited |
| Verse Context Reset | Prior Session B work superseded — reprocess through Verse Context and pool-based Session B |
| Ready for Analysis | Verse Context complete + term inventory clean — ready for DataPrep |
| Pre-Analysis Complete | Pre-analysis patch applied |
| Analysis Complete | Session B narrative complete, analysis patch applied |
| Session B Complete | Full Session B cycle done |

### 8.2a word_registry.verse_context_status
| Value | Meaning |
|-------|---------|
| NULL | Phase 1 excluded or zero-term registry — outside Verse Context scope |
| In Progress | Verse Context pending or underway for this registry |
| Complete | All OWNER terms with verses classified — registry may proceed to DataPrep |

### 8.3 Evidential Status (wa_term_inventory.evidential_status)
| Value | Meaning |
|-------|---------|
| confirmed | Clear inner-being vocabulary with direct verse evidence |
| plausible | Relevant but evidence is indirect |
| uncertain | Genuine uncertainty — retain with note |
| instrumental | Acts on inner being from outside |
| relational_only | Operates only in relational/social contexts |

### 8.4 Session B Flag Codes
SB_FINDING | SB_DIMENSION | SB_INNER_BEING | SD_POINTER | SD_CLUSTER

### 8.5 Patch Types
PREANALYSIS | SESSIONB | SESSIOND | CLUSTERING | VERSECONTEXT | VCGROUP | VCVERSE | REPAIR

Note: VERSECONTEXT, VCGROUP, VCVERSE carry `session_b_status: null` in _patch_meta. The applicator must not reject these. See WA-Reference-v5.3 Section 12 (Patch Index) and Section 14 of this document.

---

## 9. Known Recurring Anomalies

From WA-SessionB-DataPrep-Instruction-v5 Section 10:

| Anomaly | Claude Code Resolution |
|---------|----------------------|
| HFA particles incorrectly extracted in Phase 1 | Accept delete classification from Claude AI. Apply bulk_update_mti_status. |
| update_registry ops in PREANALYSIS patches not executing | Verify session_b_status present in _patch_meta. Check applicator version. |
| Verses substantially exceeding occurrence_count | Accept bleed term classifications. Re-export after patch. Use reassign_verses only if contamination persists. |
| delete_flagged=1 with mti_status=extracted | Await researcher decision. Apply restore_delete_flagged or update mti_status per decision. |

---

## 10. Interaction Protocol with Claude AI

### 10.1 What Claude Code Receives from Claude AI
- Patch files — complete and validated before submission
- Schema investigation notes — specific anomalies to investigate
- Re-export requests — after patch application

### 10.2 What Claude Code Does NOT Receive
- Classification opinions or scope judgements
- Requests to read verses and assess relevance
- Analytical questions about term meaning
- Instructions to make decisions about the data

### 10.3 Sequence of Operations

```
Claude AI produces patch  ->  Claude Code validates & applies  ->
Claude Code re-exports JSON  ->  Claude AI loads & verifies  ->
Claude AI confirms readiness  ->  proceed to next phase
```

---

## 11. Periodic Review Support

Approximately every 25 completed Session B analyses, Claude Code supports a periodic review by:

1. Running all programme state queries (Section 5)
2. Investigating zero-term registries (Task 5 query)
3. Reporting cluster progress
4. Flagging registry anomalies (inconsistent status, incorrect data)

**Output file:** `wa-programme-review-{YYYYMMDD}.docx`

The review does **not**: remove words, reclassify completed analyses, or make synthesis claims.

---

## 12. Engine and Script Status (v3.8.0)

All v5 implementation tasks complete. Schema at v3.8.0 (migrations M01–M18 complete).

| Component | Status |
|-----------|--------|
| constants.py | Schema version 3.7.0 |
| migrate.py | Migrations M01-M18 complete (M17: dimensions rename + anchor_verses removal; M18: verse_context tables + verse_context_status field) |
| apply_session_patch.py | Supports SESSIONB, SESSIOND, CLUSTERING, update_evidential_status, SD pointers auto-report |
| audit_word.py | A2 first-time population bypass, scope-aware A11 export |
| flag_engine.py | All flag codes recognised |
| word_export.py | Exports evidential_status, retention_note, sb_classification, carry_forward, term_owner_type |

### Additional Scripts

| Script | Purpose |
|--------|---------|
| _batch_extract.py | Subprocess-isolated batch STEP extraction + audit_word |
| _produce_final_extract.py | Final registry extract (wa-{nnn}-{word}-final-{date}.json) from database |
| _generate_programme_report.py | Comprehensive programme status report |

---

*WA-SessionB-ClaudeCode-Instructions  |  20260327  |  Consolidation of Claude Code responsibilities from v5 document suite*

## 13. Schema Additions (post-v5 housekeeping, 2026-03-28)

### 13.1 word_registry — new columns

| Column | Type | Purpose |
|--------|------|---------|
| unique_term_count | INTEGER | Count of terms unique to this registry. Engine-derived. |
| shared_term_count | INTEGER | Count of terms shared with other registries. Engine-derived. |
| term_sharing_ratio | REAL | 0.0 (all unique) to 1.0 (all shared). Engine-derived. |

### 13.2 wa_term_inventory — new columns

| Column | Type | Purpose |
|--------|------|---------|
| term_owner_type | TEXT | OWNER (canonical home for this Strong's) or XREF (cross-reference copy). |

**XREF handling:** XREF term records remain active for cross-registry linkage queries. Their verse records are delete_flagged — excluded from all standard queries and exports.

### 13.3 wa_verse_records — new columns

| Column | Type | Purpose |
|--------|------|---------|
| mti_term_id | INTEGER | Direct FK to mti_terms.id — one-hop path from verse to master term. |

### 13.4 wa_quality_flag_types — new flag

| Flag Code | Description |
|-----------|-------------|
| CONCRETE_PHYSICAL | Term denotes a concrete physical object (sand, hand, stork). Flagged, not excluded. Verse analysis may reveal inner-being usage in context. |

### 13.5 Housekeeping rules

- Particle terms (ki, asher, al, im, etc.) are delete_flagged across all registries
- mti_status=delete is synced to wa_term_inventory.delete_flagged
- Verse records under delete_flagged terms are also delete_flagged
- XREF verse records are delete_flagged (OWNER verses only in active set)
- CONCRETE_PHYSICAL is a queryable filter, not an exclusion — terms remain active

### 13.6 Programme state queries — additions

**Term sharing (not-shared words):**
```sql
SELECT no, word, cluster_assignment, unique_term_count, phase1_term_count, phase1_verse_count
FROM word_registry
WHERE term_sharing_ratio = 0.0 AND phase1_status != 'Excluded' AND phase1_term_count > 0
ORDER BY no;
```

**Ownership distribution:**
```sql
SELECT term_owner_type, COUNT(*) as terms
FROM wa_term_inventory WHERE delete_flagged = 0
GROUP BY term_owner_type;
```

---

### 6.6 Verse Context Stage Monitoring (new v2)

```sql
-- Progress by verse_context_status
SELECT verse_context_status, COUNT(*) as count
FROM word_registry GROUP BY verse_context_status;

-- Registries where Verse Context complete and DataPrep gate is open
SELECT no, word, cluster_assignment
FROM word_registry
WHERE verse_context_status = 'Complete'
  AND session_b_status NOT IN ('Ready for Analysis','Pre-Analysis Complete','Analysis Complete','Session B Complete')
ORDER BY no;

-- OWNER terms needing Verse Context (no verse_context record yet)
SELECT mt.strongs_number, mt.gloss, mt.owning_word,
       COUNT(vr.id) as verse_count
FROM mti_terms mt
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
  AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
WHERE mt.status IN ('extracted','extracted_thin')
  AND NOT EXISTS (SELECT 1 FROM verse_context vc
                 WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0)
GROUP BY mt.id
ORDER BY mt.owning_registry_fk, mt.strongs_number;
```

---

## 14. Verse Context Operations (new v2 — schema v3.8.0)

Full integrated instruction for both Claude AI and Claude Code: WA-VerseContext-Instruction-v1-20260329.md. This section contains Claude Code's specific operational rules.

### 14.1 Batch Construction Rules

- OWNER terms only (`term_owner_type = 'OWNER'`)
- Active terms only (`mti_terms.status IN ('extracted', 'extracted_thin')`)
- Terms with verses only (`COUNT(wa_verse_records WHERE delete_flagged = 0) > 0`)
- Target: 2,000–2,500 unclassified verses per batch
- Never split a term across batches
- Priority: terms with no existing `verse_context` records first, ordered by `mti_terms.owning_registry_fk` ascending
- Batch ID format: VCB-001, VCB-002 etc.
- Output file: `wa-vcb-{batch_id}-extract-{date}.json`

### 14.2 Patch Application — Three Verse Context Patch Types

All three types carry `session_b_status: null` in `_patch_meta`. The applicator must not reject these.

**VERSECONTEXT** (`PATCH-{YYYYMMDD}-VCB{nnn}-VERSECONTEXT-V1`):
- Process `verse_context_group` inserts before `verse_context` inserts
- After each group insert: capture `last_insert_rowid()` as the integer id for this group
- Resolve group_code strings (e.g. `"142-001"`) to captured integer ids for verse_context inserts
- Single transaction — all or nothing

**VCGROUP** (`PATCH-{YYYYMMDD}-VCGROUP{group_id}-V1`):
- Update operations on `verse_context_group` only
- Reinstatement (delete_flagged 1→0): verse_context rows are NOT automatically reinstated — separate VCVERSE patch required

**VCVERSE** (`PATCH-{YYYYMMDD}-VCVERSE{verse_record_id}-V1`):
- Insert or update on `verse_context`; may include a group insert if new group needed

### 14.3 Consistency Rule Validation

Run after every Verse Context patch:

```sql
-- R1: set-aside rows clean
SELECT COUNT(*) FROM verse_context
WHERE is_relevant=0 AND (group_id IS NOT NULL OR is_anchor=1 OR is_related=1);
-- Expected: 0

-- R2: anchor rows clean
SELECT COUNT(*) FROM verse_context
WHERE is_anchor=1 AND (is_relevant=0 OR is_related=1 OR group_id IS NULL);
-- Expected: 0

-- R3: related rows have an anchor in their group
SELECT COUNT(*) FROM verse_context vc
WHERE is_related=1 AND NOT EXISTS (
  SELECT 1 FROM verse_context a
  WHERE a.group_id=vc.group_id AND a.is_anchor=1 AND a.delete_flagged=0);
-- Expected: 0
```

### 14.4 Anchor Integrity Check

After any patch affecting anchor status, for each affected term:

```sql
SELECT COUNT(*) as active_anchors FROM verse_context
WHERE mti_term_id = {mti_term_id} AND is_anchor = 1 AND delete_flagged = 0;
-- If 0: flag to researcher — term has no anchor and cannot proceed to Session B
```

### 14.5 Registry Completion Check

After each VERSECONTEXT patch, for each registry whose OWNER terms appear in the batch:

```sql
SELECT COUNT(*) as unclassified
FROM wa_term_inventory ti
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
WHERE wr.no = {registry_no}
  AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
  AND mt.status IN ('extracted','extracted_thin')
  AND EXISTS (SELECT 1 FROM wa_verse_records vr
              WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0)
  AND NOT EXISTS (SELECT 1 FROM verse_context vc
                 WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0);
```

If 0: `UPDATE word_registry SET verse_context_status = 'Complete' WHERE no = {registry_no};`

### 14.6 Re-extraction Trigger

After every audit_word re-run:

```sql
-- Find OWNER terms with new verses not in verse_context
SELECT DISTINCT mt.id, mt.strongs_number, mt.owning_registry_fk
FROM wa_verse_records vr
JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
JOIN mti_terms mt ON mt.id = vr.mti_term_id
WHERE ti.term_owner_type = 'OWNER' AND vr.delete_flagged = 0
  AND NOT EXISTS (SELECT 1 FROM verse_context vc
                 WHERE vc.verse_record_id = vr.id AND vc.mti_term_id = mt.id);
```

For each term returned: set owning registry `verse_context_status = 'In Progress'`.

Cascade delete_flag from verse records to verse_context:
```sql
UPDATE verse_context SET delete_flagged = 1
WHERE verse_record_id IN (SELECT id FROM wa_verse_records WHERE delete_flagged = 1)
  AND delete_flagged = 0;
```

### 14.7 Integrity Validation

After every patch cycle:

```sql
SELECT mt.strongs_number, mt.status, COUNT(vc.id) as active_vc_rows
FROM mti_terms mt
JOIN verse_context vc ON vc.mti_term_id = mt.id
WHERE mt.status IN ('delete','excluded') AND vc.delete_flagged = 0
GROUP BY mt.id;
-- Expected: zero rows. Any result is an integrity violation — report to researcher.
```

### 14.8 Pool Analysis Dataset Export

When Stage 2 Session B Analysis begins, produce pool analysis datasets.

File naming: `wa-pool-{pool_id}-analysis-{date}.json`

Content: all words in the pool batch, OWNER term anchor verses grouped by contextual meaning group, XREF term profiles (group descriptions and anchor references from OWNER registries). Full specification: WA-SessionB-Analysis-Instruction v5.2 (pending).

---

*WA-SessionB-ClaudeCode-Instructions-v2  |  Updated 20260329  |  Schema v3.8.0  |  Supersedes undated prior version*
