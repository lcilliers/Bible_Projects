# wa-claudecode-instruction-v4_4-20260428

> Framework B Soul Word Analysis Programme — Claude Code Operating Guide
> Version: v4_4 | Date: 20260428
> Supersedes: wa-claudecode-instruction-v4_3-20260427.md (adds v2.CC10 citation extraction on initial chapter write + parser format-variant note in v2.CC2)
> Governed by: wa-global-rules-all [current]

---

## Document scope (GR-REF-001 Discipline 5)

This document is the authoritative source for:

- Claude Code's role and boundary of responsibility
- Data foundation pipeline — register, extract STEP data, audit_word, JSON export
- **Session B Architecture v2 — readiness output generation, obslog parser, Phase 2 writer, analytic status generator, anomaly detection** (per Architecture v2 addendum below)
- Schema and implementation tasks (historical record + ongoing)
- JSON export workflow
- Programme state queries (CC-facing)
- Engine and script status
- Periodic review support
- Verse Context operations from CC's perspective (batch construction, consistency validation, anchor integrity)
- Re-run requirements and STALE_TERM mechanism
- Recurring anomaly resolutions

This document is NOT authoritative for (pointers, not copies):

- Patch format, patch application, REPAIR catalogue, failure patches → wa-patch-instruction [current]
- Directive format, directive execution → wa-directive-instruction [current]
- Controlled vocabulary → wa-reference [current] §2–§11
- Schema field definitions → wa-reference [current] §13
- File naming rules → GR-FILE-001 through GR-FILE-009; wa-reference [current] §1
- Programme-wide binding rules → wa-global-general-rules [current]
- Architecture v2 source of truth → research/investigations/db-capture-phase1-results-and-table-architecture-v1-20260427.md

Per GR-REF-001 Discipline 1 (pointer, not copy): content owned by those documents is referenced, not re-stated here.

---

## Architecture v2 — addendum (effective 2026-04-27)

**Source-of-truth:** [research/investigations/db-capture-phase1-results-and-table-architecture-v1-20260427.md](../../../research/investigations/db-capture-phase1-results-and-table-architecture-v1-20260427.md) Parts 10-12 (researcher-locked).

Under Architecture v2, **CC's responsibilities expand significantly**. The old "patch applier" role is replaced by an end-to-end ownership of the readiness phase, the obslog-to-DB capture pipeline, and the analytic status generation.

### v2.CC1 Readiness output generation (ownership)

CC owns the readiness phase entirely. For each registry analytical session:

1. Run `scripts/_pilot_build_readiness_output_v2_*.py --registry {N}` — produces `.md` + `.json` paired outputs in `Sessions/Session_B/09_Analysis_output_logs/words/`.
2. The readiness output is structured per the v2 spec — 14 sections (A through N + M) detailed in `wa-sessionb-analysis-readiness [current]` §v2.R2.
3. **§N "Open Session B Items"** is queried from `wa_session_b_findings WHERE status='open' AND registry_id=?`.
4. **§L Catalogue** embeds the 147 generic universal questions as JSON, plus any registry-specific extensions.
5. Pre-flight integrity checks before writing the `.md`: anchor count consistency, dimension assignment coherence, term-status integrity, group description vs dimension drift.

### v2.CC2 Obslog parser (Phase 1)

After Claude AI submits the comprehensive obslog `.md` for a session:

1. Run `scripts/_pilot_parse_obslog_to_db_v1_*.py --obslog {path} --registry {N}` — produces a structured manifest `.json` + a validation report `.md` in `Sessions/Session_B/09_Analysis_output_logs/words/`.
2. Parser handles 8 categories: Q&A findings, SD pointers, observations, Stage 2c chapters, GAP questions, word-specific questions, review notes, status update, issues.
3. Validators run: declared-vs-parsed counts, required-field checks, duplicate-marker detection, stub-marker detection.
4. Optional comparison mode against any already-applied patches (regression check).

**Format conformance** (per analysis-output `[current]` §v2.8): the parser expects specific obslog markers — `**Q&A-NNN | QNNN**`, `**OBS-NNN-NNN:**`, `**SP-NNN-NNN**`, `## Stage 2c — Chapter N: ...`, `## Session Close`, etc. If AI's obslog uses different markers, the parser silently skips non-conforming sections.

**Format-variant fallback parser:** `scripts/_pilot_parse_obslog_v2_format_v1_*.py` handles the alternative format that emerged in R030 contrition (2026-04-27): `**Q&A NNN** — date` with bullet-list fields, `**OBS-NNN-NNN:**` inline (no register table), `**SP-NNN (NEW)**` blocks, `### CHAPTER N — Title` under `## STAGE 2c — ANALYTIC WORD OUTPUT`. Use this variant only when the standard parser returns 0/0 counts on an obslog known to have content. Going forward under analysis-output `[current]` v1_5+, AI is required to use the canonical markers (§v2.8); the variant should not be needed for new obslogs.

### v2.CC3 Phase 2 obslog-to-DB writer

Reads the manifest from §v2.CC2 and writes to DB:

1. Run `scripts/_pilot_capture_obslog_to_db_v1_*.py --manifest {path} --obslog {path} [--live]` — dry-run by default; `--live` commits.
2. Pre-write backup labelled with timestamp.
3. Transactional commit: all-or-nothing per session.
4. Idempotent: re-running on same manifest produces no duplicate rows (existing-row checks per category).
5. Writers per category (see Architecture §10.8):
    - `write_status_update` — `word_registry.session_b_status` UPDATE
    - `write_observations` — `wa_session_b_findings` INSERT (status='open', finding_type='OBSERVATION', session_b_instruction='wa-sessionb-analysis-output-v1_2')
    - `write_chapters` — `prose_section` INSERT (section_type_id codes `sb_s2c_ch1`..`sb_s2c_ch5`)
    - `write_sd_pointers` — `wa_session_research_flags` INSERT (flag_code='SD_POINTER')
    - `write_new_questions` — `wa_obs_question_catalogue` INSERT (auto-allocated obs_id; catalogue_version=`v2.1-R{NNN}`)
    - `write_qa_findings` — `wa_finding_catalogue_links` INSERT (finding_id → source observation; coverage='full|partial|not_applicable') + lifecycle UPDATE on source observation; entity_links (verse + group + dimension) populated
    - `write_catalogue_completeness` — fills `coverage='no_finding'` for unaddressed universal Qs
    - `write_review_notes` — `wa_obs_question_catalogue.review_note` UPDATE (append; `[review note from RNNN]` prefix marker)
    - `write_anchor_verse_analyses` — `verse_context.analysis_note` UPDATE per (verse_record_id, mti_term_id) extracted from Unit 7 prose blocks

### v2.CC4 Analytic Status generator

For revision sessions, CC produces a second input artefact alongside the readiness output:

1. Run `scripts/_pilot_build_analytic_status_v1_*.py --registry {N}` — produces `wa-{NNN}-{word}-analytic-status-v1-{date}.{md,json}`.
2. Captures: lifecycle summary, catalogue coverage breakdown, resolved Q&A pairs, resolved SD pointers, not_relevant findings, Stage 2c chapters, anchor analysis_notes, open items carried forward.
3. AI receives BOTH the readiness `.md` (data) and the analytic status `.md` (analysis) as inputs for revision.

### v2.CC5 Anomaly detection

Post-write validation identifies inconsistencies. CC writes `'open'` findings of type `DATA_ANOMALY_*` to `wa_session_b_findings` for AI to address in the next session:

| finding_type | Trigger |
|---|---|
| `DATA_ANOMALY_ANCHOR_UNCITED` | `is_anchor=1` verse not cited in any chapter prose |
| `DATA_ANOMALY_DIMENSION_DRIFT` | Group dimension contradicts group description content |
| `DATA_ANOMALY_ANSWER_UNGROUNDED` | Q&A answer doesn't reference any anchor verse from the term |
| `DATA_ANOMALY_EMPTY_TERM` | Term `status='extracted'` but 0 active verses |
| `DATA_ANOMALY_ORPHAN_ANALYSIS` | `verse_context.analysis_note` exists but verse no longer `is_anchor=1` |

These appear in the next readiness `.md` §N. Set is expandable as patterns emerge.

### v2.CC6 Schema migrations M40-M43 (live as of 2026-04-27)

| M | Change |
|---|---|
| M40 | `verse_context.analysis_note` (TEXT) — anchor-verse analytical commentary |
| M41 | `wa_prose_section_citations` (table) — chapter↔findings/Q&As/SDs/observations index |
| M42 | `wa_obs_question_catalogue.review_note` (TEXT) — catalogue maintenance notes |
| M43 | `wa_finding_catalogue_links.finding_id` NULL allowed — for `no_finding` and `not_applicable` coverage rows |

Schema version bumped from 3.16.1 → 3.17.0.

### v2.CC7 Lifecycle vocabulary (controlled lists)

CC enforces these controlled vocabularies in the writer:

- `wa_session_b_findings.status`: `open` / `resolved_qa` / `resolved_sd` / `not_relevant` / `superseded`
- `wa_session_b_findings.finding_type`: `OBSERVATION` (CC-written) · `DATA_ANOMALY_*` family (CC-written) · plus all existing analytical types (AI-written via writer)
- `wa_finding_catalogue_links.coverage`: `full` / `partial` / `not_applicable` / `no_finding`
- `wa_finding_entity_links.entity_type`: `term` / `verse` / `group` / `dimension`

### v2.CC8 Pilot status

Architecture v2 piloted on registry 067 (goodness) on 2026-04-27. Outcomes:

- 49 observations written (28 status='open' carried forward; 21 resolved_qa)
- 5 chapters written (~42 KB body)
- 14 new catalogue entries (8 generic gap + 6 Goodness Extensions)
- 61 Q&A catalogue links + 89 entity links + 13 anchor verse analyses
- Post-write analytic status generator output: ~130 KB

Backup: `backups/bible_research_pre_capture_writer_20260427.db`. Pre-migration backup: `backups/bible_research_pre_M40_M43_db_capture_arch_20260427.db`.

### v2.CC9 Prose supersede execution (revision sessions)

**Companion rule:** `wa-sessionb-analysis-output [current]` §v2.7 (prose revision on review).

When a revision-session obslog includes one or more `### SUPERSEDE: sb_s2c_ch{n} — {title}` blocks, CC's writer must:

1. **Detect supersede blocks** during Phase 1 parse — surface as a new manifest category `prose_supersedes` with `{section_type_code, registry_id, body_text, source_file, citations_inline}` per block.
2. **Phase 2 writer — `write_prose_supersedes`:**
   - Locate the existing `prose_section` row by `(registry_id, section_type_id)`.
   - Issue a `supersede` operation: mark the existing row's `is_current=0`, insert a new row with `is_current=1`, `version=prior+1`, `author='claude_ai'`, `source_file={obslog filename}`, body = block content.
   - Extract inline citations (`OBS-{NNN}-OBS-{seq}`, `SP-{NNN}-{seq}`, `Q&A-NNN`, `Q###`, `DIM-NN-NNN`) from the new body.
   - Insert citation rows into `wa_prose_section_citations` linked to the new `prose_section.id`. Resolve FK to `finding_id` / `flag_id` / `question_id` where possible; null FK with token preserved otherwise.
   - Idempotent: if the body of an incoming supersede equals the current body, no new version is written.
3. **Pre-write backup** (mandatory) — supersede operations are non-destructive (prior version remains queryable via `is_current=0`) but the backup makes recovery trivial.
4. **Session-close audit (mandatory):** After all supersedes are written, run a coherence audit and write findings of type `DATA_ANOMALY_*` for any failure (audit table below).
5. **Reporting:** The writer's session-close report includes a "supersede summary" — chapters superseded, prior versions retired, new citation count per chapter, audit outcomes.

**Supersede audit table:**

| Audit | Anomaly type | Trigger |
|---|---|---|
| Finding coverage | `DATA_ANOMALY_FINDING_UNCITED` | A revision-session resolved finding (resolved_qa / resolved_sd / not_relevant) is not cited in any chapter (current `is_current=1`) |
| Chapter completeness | `DATA_ANOMALY_CHAPTER_NOT_SUPERSEDED` | A chapter contains a citation to a finding that was reclassified during the revision (lifecycle change) but the chapter was not superseded |
| Citation FK resolution | `DATA_ANOMALY_CITATION_GAP` | Unresolved citation tokens (FK not populated) exceed 10% of the chapter's total citations |
| Anchor coverage | `DATA_ANOMALY_ANCHOR_UNCITED` (re-run of v2.CC5 audit) | An `is_anchor=1` verse is not cited in any current chapter |

**Citation token format:** Tokens in inline prose use the full finding_id format. Where the obslog uses a short form (e.g. `OBS-002` rather than `OBS-067-OBS-002`), the parser normalises to the full form using the registry context before FK lookup. Unrecognised tokens are written with FK=null and surfaced in the audit.

**Why CC owns this:** AI's job is to write the supersede prose with v2.4 citation discipline. CC's job is the version-discipline plumbing (mark prior `is_current=0`, write new row, populate citation FKs) and the post-write audit (verify finding↔prose bidirectional coverage). Splitting it this way matches the v2 architecture's "AI for analytical content; CC for DB plumbing and audit."

**First application:** R067 goodness obslog v3 (2026-04-27) — five `SUPERSEDE: sb_s2c_ch{1..5}` blocks; superseded versions carry v2.4 citation discipline; prior chapters retained at `is_current=0` for audit-trail provenance.

### v2.CC10 Citation extraction on initial chapter write

**Companion rule:** `wa-sessionb-analysis-output [current]` §v2.9 (chapter citation discipline).

When `write_chapters()` inserts a new `prose_section` row at v=1 (initial write, not supersede), CC **immediately extracts inline citation tokens** from the chapter body and inserts them into `wa_prose_section_citations`. This closes the audit-trail gap that previously existed: under v1_4 and earlier, citations were only extracted on supersede (v2.CC9), so freshly-captured chapters had 0 citation rows even when the prose was citation-rich.

**Token formats recognised** (same set as the supersede extractor in v2.CC9):

| Token | Pattern | FK target |
|---|---|---|
| `OBS-{NNN}-OBS-{seq}` (R067-style finding_id) | `\bOBS-\d{3}-OBS-\d{3}\b` | `wa_session_b_findings.finding_id` |
| `OBS-{NNN}-{seq}` (R030-style finding_id) | `\bOBS-\d{3}-\d{3}\b` | `wa_session_b_findings.finding_id` |
| `SP-{NNN}-{seq}` | `\bSP-\d{3}-\d{3}\b` | `wa_session_research_flags.flag_label` |
| `DIM-{N}-{seq}` (incl. SD-suffix variants) | `\bDIM-\d+-(?:SD)?\d+\b` | `wa_session_b_findings.finding_id` |
| `GAP-N-{seq}` / `GAP-S{n}-{seq}` | `\b(?:GAP-N-\d{3}\|GAP-S\d-\d{3})\b` | `wa_obs_question_catalogue.question_code` (no FK column; stored in `citation_form`) |
| `Q&A-{seq}` / `Q&A {seq}` | `\bQ&A[ -]\d{1,3}\b` | (no FK; stored in `citation_form`) |
| `Q{NNN}` (catalogue question_code) | `\bQ\d{3}\b` | (no FK; stored in `citation_form`) |

**Implementation:** `_extract_and_write_chapter_citations()` helper in `scripts/_pilot_capture_obslog_to_db_v1_*.py`. Called from `write_chapters()` immediately after each `INSERT INTO prose_section`. Idempotent on `(prose_section_id, citation_form)`.

**Why this is on initial write rather than a separate AI pass:** AI is already required to cite inline by §v2.4; the analytical pass produces citation-rich prose organically (R030 contrition produced ~73 inline tokens in 5 chapters without any separate citation step). CC's job is mechanical token extraction — no second AI pass is needed for citations. **Supersede (v2.CC9) is reserved for content refresh on revision sessions**, not for citation backfill.

**Critical regex bug fixed (2026-04-28):** the prior `OBS-(\d+)` pattern in the qa_findings resolver greedy-captured the registry digits (e.g. "030") and never reached the seq, causing every Q&A citation to resolve to the same finding (whichever observation seq numerically equalled the registry number). Fixed to `OBS-\d+(?:-OBS)?-(\d+)\b` which captures only the trailing seq and works for both R067 and R030 formats. R030 contrition was the registry where the bug manifested; pre-fix capture rolled back from backup; re-ran with corrected logic.

**First application:** R030 contrition (2026-04-28). Backfill script for chapters captured under v1_4 pre-citation-extraction: `scripts/archive/_apply_r030_chapter_citation_backfill_v1_20260428.py` (one-off; not needed going forward since v2.CC10 now extracts on write). 73 citations extracted across 5 chapters.

---

## Governing Rules

Per GR-REF-001, rules stated in the global rules file are not repeated here — rule IDs are the authoritative reference. CC-role application notes are added only where CC's specific behaviour requires clarification.

| Rule | CC application |
|---|---|
| GR-PROG-005 | CC executes; does not initiate database changes independently |
| GR-PROC-004 | CC does not apply any patch or directive until researcher approval confirmed |
| GR-DATA-001 (per wa-reference [current] §13.2) | All CC queries against `mti_terms` for active terms include `AND mt.status IN ('extracted', 'extracted_thin')` |
| GR-DATA-003 (per wa-reference [current] §13.2) | `mti_term_flags` is the authoritative field for somatic classification, not `wa_term_inventory.somatic_link` |
| No physical deletion (per wa-patch-instruction [current] §5.4) | CC never executes DELETE statements against analytical records; `delete_flagged = 1` only |
| Patch format self-check (per wa-patch-instruction [current] §7) | CC may reject patches that fail the self-check on receipt — reports which of the six points failed |
| Directive five elements (per wa-directive-instruction [current] §3) | CC may reject directives missing any of the five required elements — reports which are missing |
| Completion confirmation (per wa-patch-instruction [current] §6 and wa-directive-instruction [current] §6) | CC returns the specified confirmation before the operation is considered closed |

---

## Change Control — v4_4

| Change | Section |
|---|---|
| Added §v2.CC10 — **citation extraction on initial chapter write**: `write_chapters()` now extracts inline citation tokens into `wa_prose_section_citations` immediately after each `prose_section` insert, closing the audit-trail gap that previously left freshly-captured chapters with 0 citation rows. Token-format table matches v2.CC9. Idempotent. | New section after v2.CC9 |
| Updated v2.CC2 (parser) with **format-conformance reference** to analysis-output `[current]` §v2.8 + note on the format-variant fallback parser (`scripts/_pilot_parse_obslog_v2_format_v1_*.py`) that handled the R030 contrition obslog convention drift | v2.CC2 |
| Citation regex bug fix documented (was greedy-capturing registry digits in the OBS-NNN-NNN form) — fixed pattern: `OBS-\d+(?:-OBS)?-(\d+)\b` which captures only the trailing seq and works for both R067 and R030 formats | v2.CC10 |
| Banner version + filename + Supersedes refreshed | Frontmatter |

## Change Control — v4_3

| Change | Section |
|---|---|
| Added §v2.CC9 — **prose supersede execution + audit** for revision sessions; companion to wa-sessionb-analysis-output [current] §v2.7 | New section after v2.CC8 |
| Defines parser detection of `### SUPERSEDE: sb_s2c_ch{n}` blocks, Phase 2 `write_prose_supersedes` writer behaviour, mandatory pre-write backup, and four-audit session-close coherence check | v2.CC9 |
| Citation token normalisation rule for short-form (`OBS-NNN`) vs full-form (`OBS-{registry:03d}-OBS-{seq:03d}`) | v2.CC9 |
| First application: R067 goodness obslog v3 (five chapter supersedes) | v2.CC9 |
| Banner version + filename + Supersedes refreshed | Frontmatter |

## Change Control — v4_2

| Change | Section |
|---|---|
| Architecture v2 addendum applied (substantial new CC responsibilities) — readiness output generation, obslog parser, Phase 2 writer, analytic status generator, anomaly detection, M40-M43 schema migrations, lifecycle vocabulary, pilot status | v2.CC1–v2.CC8 |

## Change Control — v4_1

| Change | Section |
|---|---|
| Operational cross-references migrated to `[current]` token per GR-REF-002 — frontmatter, Governing Rules table, §2/§3/§4/§6/§9 inline references | Throughout |
| Registry-management-guide and versecontext-instruction pointers now use `[current]` | §9, §11 |
| Provenance preserved: v4_0 Change Control describing document consolidation (§Change Control — v4_0 below) | — |
| v4_0 Change Control retained below for provenance | — |

### Prior change control — v4_0

Major restructure from v3_6. The document has been rescoped per the researcher direction in the 2026-04-18 session:
1. Patch-related content (§4 Patch Application, §15 REPAIR catalogue, §16 Failure patch, patch-handoff formats) moved to wa-patch-instruction v2_0
2. Vocabulary duplication (§8 Controlled Vocabulary, §13 Schema Additions) removed; pointers to wa-reference v5_6 added in their place
3. File naming conventions (§7) reduced to pointers; authority moved to wa-reference v5_6 §1 and GR-FILE rules
4. Governing rules section rebuilt — inline restatements replaced with rule-ID citations per GR-REF-001 Discipline 1
5. Document scope statement added at top per GR-REF-001 Discipline 5

Content that was in v3_6 and is now authoritatively elsewhere is removed from this document; pointers are provided where useful for CC workflow navigation.

Version number note: major bump v3_6 → v4_0. The content is materially different from v3_6 — three major sections removed (patch application workflow, REPAIR catalogue, failure patch — all moved to wa-patch-instruction), vocabulary and schema duplication removed (moved to wa-reference), Governing Rules section rebuilt to point-not-copy discipline. That scope of change is a rewrite, not a minor update, and a major version number reflects this honestly.

Change list:
- New document scope section (top)
- Governing Rules table — rule IDs only, CC-role application notes
- §1 — Role and boundary (from v3_6 §1)
- §2 — Data foundation pipeline (from v3_6 §2, retained with reference updates)
- §3 — Implementation tasks historical record (from v3_6 §3 — ongoing items only; historical tasks moved to Appendix A)
- §4 — JSON export workflow (from v3_6 §5)
- §5 — Programme state queries (from v3_6 §6 and §6.6)
- §6 — Verse Context operations — CC perspective (from v3_6 §14)
- §7 — Engine and script status (from v3_6 §12)
- §8 — Periodic review support (from v3_6 §11)
- §9 — Re-run requirements and STALE_TERM mechanism (from v3_6 §2.4)
- §10 — Recurring anomalies (from v3_6 §9)
- §11 — Interaction protocol with Claude AI (from v3_6 §10)
- Appendix A — Historical implementation tasks

Removed (now in other documents):
- Patch application workflow → wa-patch-instruction [current] §3–§7
- REPAIR patch catalogue → wa-patch-instruction [current] §9
- Failure patch → wa-patch-instruction [current] §10
- Controlled vocabulary tables → wa-reference [current] §2–§11
- Schema additions and housekeeping rules → wa-reference [current] §13, §15
- File naming convention table → wa-reference [current] §1

---

## 1. Claude Code's Role — Boundary Definition

Claude Code is the **database engine**. It applies patches, exports JSON, queries the database, runs schema migrations, and validates data integrity. It does **not**:

- Classify terms or make scope decisions
- Assess analytical relevance of terms
- Read verses and judge their significance
- Make synthesis or interpretation claims
- Decide evidential status

All classification, scope judgement, and analytical work belongs to **Claude AI**. Claude Code executes database operations based on validated instructions — patch files (wa-patch-instruction [current]) and directive files (wa-directive-instruction [current]).

---

## 2. Data Foundation Pipeline

Claude Code's foundational and ongoing responsibility is producing the word JSON export that serves as the starting input for every Session B analysis.

### 2.1 End-to-end pipeline

```
Register word → Extract STEP data → Audit (populate DB) → Export JSON
                                                             ↓
                                               Verse Context begins
                                                             ↓
                                               Session B pipeline
```

Every word passes through this pipeline before Session B can start.

### 2.2 Step 1 — Register word

```bash
python -m engine.engine --register --word="compassion" --source="High Confidence"
```

Creates a `word_registry` row. Write scope: `word_registry` INSERT only. No biblical data is written. The registry number (`no`) becomes the word's permanent identifier used in all file naming and cross-references.

### 2.3 Step 2 — STEP data extraction

```bash
python scripts/word_study_extract.py --word compassion [--anchors H7356,G4698]
```

Queries the local STEP Bible server (`http://localhost:8989`) to pull:
- All Strong's numbers associated with the English word (via `meanings=` endpoint)
- Vocabulary data per term (gloss, meaning, related words, occurrence count)
- Full verse corpus per term (ESV text, with STEP HTML for span filtering)

**Output:** `research/discovery/{nnn}_{word}_step_data_{YYYYMMDD}.json`

**Key technical notes:**
- Uses the `meanings=` endpoint (not `text=+`) to match STEP's "Related words" panel — catches terms like H2734 that the ESV never translates with the literal English word
- STEP API caps results at 60 per request; the client uses canonical section splits for complete coverage
- `--anchors` flag adds specific Strong's numbers that should always be included

### 2.4 Step 3 — Audit word (populate database)

```bash
python -m engine.engine --mode=audit_word --registry=N [--extract-file=PATH]
```

Core data population pipeline (Pre-A1 through A11):

| Step | What it does |
|---|---|
| Pre-A1 | Lock sentinel + open run log |
| A1 | Registry display + confirmation |
| A2 | DB snapshot + structural completeness check (bypasses STOP if Step 1 JSON available for first-time population) |
| A3 | Load + validate Step 1 JSON (auto-selects latest unless --extract-file given) |
| A4 | Build gap report — compares JSON against DB state (Term / Related / Verse / VTL streams) |
| A5 | Display gap report |
| A6 | Apply changes — single transaction per stream: NEW_TERM inserts, STALE_TERM updates, DB_ONLY_TERM flagging, verse inserts with span filtering |
| A6b | Term classification — data-driven filters (no interpretation): F1–F5 classify NULL-status terms based on verse count and analytical signals |
| A7 | Meaning handler — parse meaning text into wa_meaning_parsed/sense/stem/lsj |
| A8 | Quality flag reset — DATA_COVERAGE group only, then re-derive via flag_engine.py |
| A9 | Audit checks WR-01–WR-20 + write word_run_state |
| A10 | Registry + file index update, close run, set last_automation_run = 'AUDITED' |
| A11 | Full-word JSON export |

**Key behaviours:**
- Auto-approve by default — use `--interactive` for per-item gates
- No physical deletes (per wa-patch-instruction [current] §5.4) — deletions flagged with `delete_flagged=1`
- Only engine-derivable flags (DATA_COVERAGE group) are reset and re-derived; Phase 2 flags and session research flags never touched
- Span filtering: only verses where the queried Strong's is confirmed in the original-language STEP HTML span are stored

**Flag ownership boundaries (strict):**

| Category | Table | Owner | Engine touches? |
|---|---|---|---|
| A — Engine-derivable | `wa_data_quality_flags` | Engine (flag_engine.py) | Yes — reset in A8, re-derived |
| B — Term-level analytical | `wa_term_phase2_flags` | Researcher (Claude AI) | **Never** |
| C — Session research | `wa_session_research_flags` | Researcher (Claude AI) | **Never** — written by apply_session_patch.py only |

### 2.5 Step 4 — JSON export

Runs automatically as A11, or manually:
```bash
python -m engine.engine --export-word --registry=N
```

**Output:** `data/exports/{word}_{registry}_{scope}_{YYYYMMDD}_v{N}.json`

- Scope: `full` (pre-analysis) or `final` (post-analysis, requires both `session_b_status = Analysis Complete` AND `wa_session_b_dimensions` row present)
- Version auto-increments per day (v1, v2, v3, …). Previous versions retained.

Export includes: registry meta, file index, term inventory (with meaning parse, quality flags, phase2 flags, related words, root family, MTI data), verse corpus, cross-registry links, session research flags, patch history, statistics.

### 2.6 Ongoing obligations

- **Run audit_word for remaining registries** — as new registries are added
- **Re-export after patches** — every time CC applies a pre-analysis or analysis patch, re-export JSON so Claude AI has current data
- **Maintain the STEP client** — `step_client.py` and `word_study_extract.py` are CC's tools; bugs and enhancements are CC's responsibility

---

## 3. Implementation Tasks — Ongoing

All v5 schema implementation tasks are complete. Schema v3.8.0 (migrations M01–M18). Historical record in Appendix A.

Any future schema changes are produced as migration scripts (`migrate.py`) and executed by CC with researcher approval. New tables or columns introduced after this document's date should be added to wa-reference [current] §13.

---

## 4. JSON Export Workflow

CC exports word data for Claude AI consumption at defined points:

### 4.1 Before data preparation
```bash
python -m engine.engine --export-word --registry=N
```
Output: `data/exports/{word}_{registry}_{scope}_{YYYYMMDD}_v{N}.json`

### 4.2 After patch application (re-export)
Same command — produces fresh export reflecting patched state. Post-analysis exports automatically use scope `final`.

### 4.3 Post-patch output files
After an analysis completion patch is applied and confirmed, two additional files are produced per wa-patch-instruction [current] §8:
- Final registry extract (produced by Claude AI)
- Session D pointers (auto-generated by apply_session_patch.py)

---

## 5. Programme State Queries

CC runs these queries to assess programme state. Vocabulary values per wa-reference [current] §3, §3a.

### 5.1 Session B progress by status
```sql
SELECT session_b_status, COUNT(*) as count
FROM word_registry GROUP BY session_b_status ORDER BY session_b_status;
```

### 5.2 Words ready for analysis
```sql
SELECT no, word FROM word_registry
WHERE session_b_status IN ('Ready for Analysis', 'Pre-Analysis Complete')
ORDER BY no;
```

### 5.3 Words not yet started
```sql
SELECT no, word, phase1_status FROM word_registry
WHERE session_b_status IS NULL ORDER BY no;
```

### 5.4 Zero-term registries
```sql
SELECT no, word FROM word_registry
WHERE phase1_term_count = 0 OR phase1_term_count IS NULL ORDER BY no;
```

### 5.5 Cluster progress
```sql
SELECT cluster_assignment, COUNT(*) as total,
  SUM(CASE WHEN session_b_status = 'Session B Complete' THEN 1 ELSE 0 END) as complete
FROM word_registry GROUP BY cluster_assignment;
```

### 5.6 Verse Context stage monitoring

```sql
-- Progress by verse_context_status
SELECT verse_context_status, COUNT(*) as count
FROM word_registry GROUP BY verse_context_status;

-- Registries where VC complete and DataPrep gate is open
SELECT no, word, cluster_assignment
FROM word_registry
WHERE verse_context_status = 'Complete'
  AND session_b_status NOT IN ('Ready for Analysis','Pre-Analysis Complete','Analysis Complete','Session B Complete')
ORDER BY no;

-- OWNER terms needing VC (no verse_context record yet)
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

### 5.7 Term sharing and ownership

```sql
-- Not-shared words
SELECT no, word, cluster_assignment, unique_term_count, phase1_term_count, phase1_verse_count
FROM word_registry
WHERE term_sharing_ratio = 0.0 AND phase1_status != 'Excluded' AND phase1_term_count > 0
ORDER BY no;

-- Ownership distribution
SELECT term_owner_type, COUNT(*) as terms
FROM wa_term_inventory WHERE delete_flagged = 0
GROUP BY term_owner_type;
```

---

## 6. Verse Context Operations — CC Perspective

Full integrated instruction for both Claude AI and Claude Code: wa-versecontext-instruction [current]. This section contains CC's operational rules. Patch format for all three VC patch types per wa-patch-instruction [current] §12.

### 6.1 Batch construction rules

- OWNER terms only (`term_owner_type = 'OWNER'`)
- Active terms only (`mti_terms.status IN ('extracted', 'extracted_thin')`) per GR-DATA-001
- Terms with verses only (`COUNT(wa_verse_records WHERE delete_flagged = 0) > 0`)
- Target: 2,000–2,500 unclassified verses per batch
- Never split a term across batches
- Priority: terms with no existing `verse_context` records first, ordered by `mti_terms.owning_registry_fk` ascending
- Batch ID format: VCB-001, VCB-002, …
- Output filename: `wa-vcb{nnn}-extract-v{n}-{YYYYMMDD}.json` per wa-reference [current] §1.2

**SQL policy:** SQL query construction for batch assembly is CC's responsibility. The governing instruction (wa-versecontext-instruction) provides all criteria, field names, and derivation rules. An unclassified verse is any `wa_verse_records` record (`delete_flagged = 0`) for an OWNER term that has no corresponding `verse_context` record for that `mti_term_id`.

### 6.2 Consistency rule validation

Run after every Verse Context patch. Per wa-patch-instruction [current] §12.6.

### 6.3 Anchor integrity check

After any patch affecting anchor status, for each affected term:

```sql
SELECT COUNT(*) as active_anchors FROM verse_context
WHERE mti_term_id = {mti_term_id} AND is_anchor = 1 AND delete_flagged = 0;
-- If 0: flag to researcher — term has no anchor and cannot proceed to Session B
```

### 6.4 Registry completion check

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

### 6.5 Re-extraction trigger

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

### 6.6 Integrity validation

After every patch cycle:

```sql
SELECT mt.strongs_number, mt.status, COUNT(vc.id) as active_vc_rows
FROM mti_terms mt
JOIN verse_context vc ON vc.mti_term_id = mt.id
WHERE mt.status IN ('delete','excluded') AND vc.delete_flagged = 0
GROUP BY mt.id;
-- Expected: zero rows. Any result is an integrity violation — report to researcher.
```

### 6.7 Cluster analysis dataset export

Produced on researcher instruction after cluster registries reach Pre-Analysis Complete. Pool architecture has been retired (see wa-registry-management-guide [current] §5.2); Session B operates on individual words in cluster order. Retained here for dataset construction mechanics.

**Filename:** `wa-{cluster}-analysis-v{n}-{YYYYMMDD}.json` per wa-reference [current] §1.3.

**Pre-construction check:**
1. Determine all `registry_no` values in the cluster (from `cluster_assignment`)
2. Query `word_registry` to verify `verse_context_status = 'Complete'` for all
3. If any not Complete: halt, report to researcher listing which are not Complete
4. If all Complete: proceed

**Source tables for construction:**
- Pool membership: `word_registry` (cluster_assignment + processing sequence from wa-registry-management-guide [current])
- Per-word registry meta: `word_registry` (core fields)
- OWNER terms per word: `wa_term_inventory` (`term_owner_type = 'OWNER'`, `delete_flagged = 0`) → `mti_terms` → `wa_quality_flag_types` → `mti_term_flags` / `wa_term_phase2_flags`
- Contextual groups per OWNER term: `verse_context_group` (`mti_term_id = mt.id` AND `delete_flagged = 0`)
- Anchor verses per group: `verse_context` (`group_id = vcg.id` AND `is_anchor = 1` AND `delete_flagged = 0`) → `wa_verse_records`
- XREF terms per word: `wa_term_inventory` (`term_owner_type = 'XREF'`, `delete_flagged = 0`) → `mti_terms` → `word_registry`
- XREF contextual groups: `verse_context_group` (shared via `mti_term_id`)
- XREF anchor references: `verse_context` (reference only, no verse text)
- Cross-word map: derived — terms appearing in more than one word in the pool

After construction: provide to Claude AI for analysis.

---

## 7. Engine and Script Status

Schema at v3.8.0 (migrations M01–M18 complete).

| Component | Status |
|---|---|
| constants.py | Schema version 3.7.0 (constants lag schema by one — not a defect) |
| migrate.py | M01–M18 complete (M17: dimensions rename + anchor_verses removal; M18: verse_context tables + verse_context_status field) |
| apply_session_patch.py | Supports SESSIONB, SESSIOND, CLUSTERING, update_evidential_status, SD pointers auto-report |
| audit_word.py | A2 first-time population bypass, scope-aware A11 export |
| flag_engine.py | All flag codes recognised |
| word_export.py | Exports evidential_status, retention_note, sb_classification, carry_forward, term_owner_type |

### 7.1 Additional scripts

| Script | Purpose |
|---|---|
| `_batch_extract.py` | Subprocess-isolated batch STEP extraction + audit_word |
| `_produce_final_extract.py` | Final registry extract from database |
| `_generate_programme_report.py` | Comprehensive programme status report |

### 7.2 Applicator gaps — flagged for implementation

Per wa-patch-instruction [current] §11.6:
- `insert` on `wa_dimension_index` — not supported; manual application required
- `update` on `wa_session_research_flags` — not supported; manual application required
- `session_b_status: null` on SDPOINTERS-type patches — rejected by applicator

---

## 8. Periodic Review Support

Approximately every 25 completed Session B analyses, CC supports a periodic review:

1. Run all programme state queries (§5)
2. Investigate zero-term registries (§5.4)
3. Report cluster progress (§5.5)
4. Flag registry anomalies (inconsistent status, incorrect data)

**Output file:** `wa-programme-review-v{n}-{YYYYMMDD}.docx`

The review does NOT: remove words, reclassify completed analyses, or make synthesis claims.

---

## 9. Re-run Requirements and STALE_TERM Mechanism

When audit_word detects it is re-running for a registry that already has `wa_term_inventory` records, the routine enforces:

### 9.1 REPAIR patch verification (mandatory gate)

Before any re-run processing begins, CC checks the patch history for a `REPAIR-AUDITWORD-RERUN` patch on this registry (query `engine_run_log` for a `patch_id` matching `PATCH-*-{nnn}-REPAIR-AUDITWORD-RERUN-*`).

If no such patch is found: halt with an error message to the researcher. Do not proceed.

A re-run without the preceding REPAIR patch risks leaving analytical outputs in an inconsistent state relative to the new verse corpus. REPAIR patch specifications are in wa-patch-instruction [current] §9.

### 9.2 wa_term_inventory update mechanism

The STALE_TERM mechanism at Step A6 is the authoritative path for updating `wa_term_inventory` on re-run. It compares the incoming STEP JSON against existing DB records and applies only the delta — updating changed fields, inserting new terms, flagging removed terms with `delete_flagged = 1`.

CC must NOT implement a separate delete/re-insert approach for `wa_term_inventory`. The REPAIR patch will have already delete_flagged `verse_context` and `verse_context_group` records; audit_word handles term inventory update through the existing gap analysis mechanism.

### 9.3 Post-run check for NULL-status terms

After A6b classification runs, check for any terms in this registry with `mti_terms.status = NULL`. These are new terms added by the re-run that the engine's classification filters did not resolve. Report these to the researcher — DataPrep must re-run before Verse Context can proceed for this registry.

---

## 10. Recurring Anomalies

| Anomaly | CC Resolution |
|---|---|
| HFA particles incorrectly extracted in Phase 1 | Accept delete classification from Claude AI. Apply `bulk_update_mti_status`. |
| `update_registry` ops in PREANALYSIS patches not executing | Verify `session_b_status` present in `_patch_meta`. Check applicator version. |
| Verses substantially exceeding `occurrence_count` | Accept bleed term classifications. Re-export after patch. Use `reassign_verses` only if contamination persists. |
| `delete_flagged=1` with `mti_status=extracted` | Await researcher decision. Apply `restore_delete_flagged` or update `mti_status` per decision. |

---

## 11. Interaction Protocol with Claude AI

### 11.1 What CC receives from Claude AI

- Patch files (wa-patch-instruction [current] format) — complete, validated before submission
- Directive files (wa-directive-instruction [current] format) — complete, validated before submission
- Schema investigation requests — specific anomalies to investigate
- Re-export requests — after patch application

### 11.2 What CC does NOT receive

- Classification opinions or scope judgements
- Requests to read verses and assess relevance
- Analytical questions about term meaning
- Instructions to make decisions about the data

### 11.3 Sequence of operations

```
Claude AI produces patch/directive  →  Researcher approves  →
Claude Code validates & applies  →  Claude Code re-exports / runs confirmation →
Claude AI reviews confirmation  →  operation closed
```

### 11.4 Feedback from CC

Per wa-patch-instruction [current] §6 and wa-directive-instruction [current] §6. CC returns the completion confirmation as specified in the patch or directive. Not a general acknowledgement — the specific query result or state check.

---

## Appendix A — Historical Implementation Tasks (v5 schema build, completed)

Preserved for audit. All tasks complete as of 2026-03-30.

### A.1 Task 1 — Add cluster_assignment to word_registry (complete)
### A.2 Task 2 — New flag types for Session B JSON mapping (complete)
### A.3 Task 3 — Create Session D capture tables (complete)
### A.4 Task 4 — Registry clustering operation (complete)
### A.5 Task 5 — Zero-term registry investigation (complete — all 6 non-excluded resolved)
### A.6 Task 6 — PATCH_SPEC update for new patch types (complete)
### A.7 Task 7 — Session D discovery JSON template (complete)
### A.8 Task 8 — Session B JSON database preparation (complete — schema v3.8.0 achieved)

Full task specifications preserved in the v3_6 document archive. This summary retained for reference; historical detail not migrated.

---

*wa-claudecode-instruction-v4_1-20260418 | Supersedes wa-claudecode-instruction-v4_0-20260418 | Prior (v4_0): superseded wa-sessionb-cc-instructions-v3_6-20260416 and its lineage; patch and directive content moved to dedicated instructions; vocabulary and schema duplication removed via GR-REF-001 pointers | v4_1 applies GR-REF-002 `[current]` to operational cross-references*
