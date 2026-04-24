# wa-versecontext-instruction-v3_4-20260424

**Framework B — Soul Word Analysis Programme
Verse Context Instruction — Integrated Claude AI and Claude Code
Version 3_4 | 20260424 | Status: Active governing instruction**

|**Document**|**Value**|
|-|-|
|Filename|wa-versecontext-instruction-v3_4-20260424.md|
|Supersedes|wa-versecontext-instruction-v3_3-20260424.md|
|Change note|v3_4 (20260424): Resolves A-02 / A-03 / A-04 / A-05 per researcher rulings 2026-04-24. **A-02** — `vc_status` vocabulary simplified: `approved` removed; `complete` renamed `vc_completed` (explicit VC-terminal state). Engine M38 migration; applicator writes `vc_completed`; aggregation checks `vc_completed` only. **A-03** — per-term `.md` freshness is now version-gated. Each per-term `.md` carries `md_version: v{n}` in its header (M38 added `mti_terms.md_version`). Patch `_patch_meta.input_versions` map ({mti_term_id → md_version}) required for VCNEW/VCREVISE; applicator rejects any patch whose declared input_version for any term ≠ current DB md_version. On successful apply, applicator bumps `md_version` — any pre-existing `.md` is stale for the next session. Claude AI reads + acknowledges the version at §6.1 startup; Claude Code stamps it into the header; §7.7 pre-submission validation checks it. **A-04** — session identifier (`batch_id`) no longer operationally required. A patch covers one term or many; the per-term version gate is authoritative for input-output correlation. `batch_id` retained as optional convenience field. **A-05** — cross-term duplicate classifications are not a VC-stage concern; `verse_context_group.mti_term_id` scopes groups per term and the same verse can legitimately appear in multiple term-group rows. Any pattern is discovered during Session B. No instruction change required for A-05. Tooling: engine M38 (schema → 3.16.0); `scripts/apply_session_patch.py` VC-2 helper widened with version gate + version bump + vc_completed write; `scripts/build_session_a_prose.py` stamps md_version into header.<br />**v3_3 (20260424):** Four-patch session output model formalised (resolves A-01 from the v3_1 inspection ambiguity doc). A VC session now produces up to four independently-applied patches — VCNEW (new classifications), VCREVISE (revisions to existing), VCSBFLAGS (Session B observations raised while reading), VCSDPOINTERS (cross-registry pointers for Session D). All four carry the same `batch_id` (session id); each is session_b_status-exempt; each is absent when its output class is empty. A-01 resolved: DataPrep gate = DB state (`word_registry.verse_context_status = 'Complete'`); the full-word JSON re-export is an audit artefact, not a required step. Changes: (1) new §7.9 "Session output — the four-patch model" with full per-patch detail, apply order, and self-check reference to patch instruction [current] §15. (2) §6.2 Step 6 extended: SB observations go into VCSBFLAGS; SD pointers go into VCSDPOINTERS; obslog still captures them as the classifier reads. (3) §6.6 restated: `sessionb-flags.md` is now a companion readable summary of the VCSBFLAGS rows, not the authoritative record; the DB rows are authoritative. (4) §7.2 reframed around the new four-patch structure; existing VERSECONTEXT content retained as legacy-combined patch for backwards compatibility. (5) §7.7 pre-submission validation extended: every SB/SD observation in the obslog must have a corresponding operation in the session's VCSBFLAGS/VCSDPOINTERS patch. (6) §7.8 hand-off updated for four patches; applicator calls the VC-2 helper on VCNEW+VCREVISE only. (7) §13.3 re-written: DB state is the DataPrep gate; full-word JSON re-export is an optional audit artefact. Tooling: patch instruction v2_5 §15 documents the patch formats authoritatively; `scripts/apply_session_patch.py` widened (VC-2 handler triggers on VERSECONTEXT+VCNEW+VCREVISE; `terms_covered` validation widened to match; `sb_exempt_types` extended). v3_2 is archived; its 21-item residue cleanup is preserved in v3_3 (no roll-back).<br />**v3_2 (20260424):** Residue cleanup after Claude AI's v3_1 inspection (obslog `wa-global-vc_review-obslog-v1_0-20260424.md` Entry 009). v3_1 changed the instruction's intent to per-OWNER-term but left stale text carried forward from v2_9/v3_0 that contradicted that intent in 21 places, plus 3 broken internal references and 3 editorial issues. v3_2 addresses them all: (1) §0 "What VC does" bullets, §0 stage-sequence diagram, §0 self-standing-document note — rewritten in term-first voice; CC writes `mti_terms.vc_status` per term; registry advancement + re-render are derived consequences. (2) §1 Two-System Model — Claude Code row corrected ("per-registry" → "per-term" as primary). (3) §5 opening paragraph, §5.1 trigger list, §5.2 input selection criteria — all re-scoped to term-first. §5.4 primary output is per-term `.md`; per-registry `.md` is hybrid secondary. (4) §6.4 file-naming breakpoint identifiers reframed to term/session scope; "batches" replaced with "sessions"; 50-term threshold replaced with 1500-verse threshold; fallback batch-JSON references struck. (5) §6.5 Deferred Flag Protocol — "end-of-batch" → "end-of-session" throughout. (6) §7.1 patch-types table — VERSECONTEXT row reworded for session scope. (7) §7.4 operation ordering — "input document" clarified to "session composition". (8) §8.2 VCGROUP patch and Annexure C template — stale `produced_by` v1.8 strings updated to `{governing_instruction}` placeholder. (9) §13.4 completion report — "next batch id" replaced with "future sessions at researcher discretion". (10) §14 Stage 1 completion — 181/31 registry counts corrected to 184/30 per §0.1; "Batches processed" relabelled "Sessions". (11) Annexure A startup template — rewritten for term-scoped v3_2 model. (12) Annexure C VERSECONTEXT template — produced_by updated; deprecation note strengthened. (13) §0.2 cross-references §14.5 (non-existent) and "completed batch" fixed — now cite §13.1/§13.2 and "completed session". (14) §6.4 references §7.6 (Anchor integrity) where §7.7 (Pre-submission validation) was intended — fixed. (15) Editorial: change-note reformatted as bulleted list (was dense prose); pass-through "batch" usages replaced with "session" where not the VCB identifier; prose-type description field amendment for `prog_instr_verse_context` landed as a separate PROSE patch alongside this instruction. **Five substantive ambiguities (A-01 through A-05 in the review) remain unresolved and are tracked in `outputs/investigations/vc-v3_1-ambiguities-needing-researcher-decision-v1-20260424.md` for researcher ruling; v3_3 will address them.** v3_2 is a correction-only release — no semantic shifts beyond v3_1's intent.<br />**v3_1 (20260424):** Per-OWNER-term input is primary (alignment analysis v4 §7 + §8). (1) Classifier's primary input is now the **per-term Session A `.md`** produced by `scripts/build_session_a_prose.py --term` and stored at `data/exports/session_a/terms/`. The per-registry `.md` is retained as a hybrid secondary view for researcher review and Dimension Review hand-off but is no longer the primary classifier input. (2) §0.1 updated to state per-term as default; registry envelope is a CC-side derived aggregation via `mti_terms.vc_status`. (3) §5 Input Preparation re-scoped: selection is per-term; session scope is researcher-discretionary (1..N terms per session); "never split a term" rule unchanged in substance. (4) §6.1 prior-state posture declaration simplified: per-term binary (FRESH or RE-EVALUATION) with no registry aggregation. (5) §6.1 processing order becomes session-assembly order, not registry-ascending (researcher composes a session's term list). (6) §7.2 adds required `_patch_meta.terms_covered` array of `mti_term_id`s; `batch_id` remains required as the session identifier. (7) §7.8 hand-off updated: Claude Code flips `mti_terms.vc_status` to `complete` per term on successful apply, then derives `word_registry.verse_context_status` as the aggregate of all OWNER + XREF-via-OWNER terms at `complete`/`approved` (per `engine` M37 schema + `scripts/apply_session_patch.py` VC-2 extension). (8) §13 registry completion check re-framed as a derived aggregation read from `mti_terms.vc_status`, not a scan of `verse_context` rows. (9) Annexure C legacy batch JSON noted as deprecated (still readable by the applicator but no longer the primary input form). v3_1 is additive — v3_0's re-evaluation discipline, orphan-group check, and validation rules are all preserved unchanged; the shift is from registry to term as the atomic scope.<br />**v3_0 (20260424):** Session A `.md`-primary input; re-evaluation discipline; streamlining. (1) Classifier's primary input is now the per-registry Session A `.md` produced by `scripts/build_session_a_prose.py`; legacy batch JSON retained as a split-registry fallback. Header Inputs row, §0.1 Pipeline Entry Point, and §5 (renamed "Input Preparation") reflect this. (2) §5.3 large batch-JSON schema moved to Annexure C; §5 now points to `docs/prose-store-architecture.md` and the Session A script as the structural reference. (3) §6.1 Startup adds a mandatory **prior-state posture declaration** — classifier states FRESH (no prior records) or RE-EVALUATION (counts stated; obligations acknowledged) before touching any term. (4) §6.2 Step 6 adds per-term **re-evaluation self-check** (arithmetic balance: confirmed + revised + reassigned = active verses) and **orphan-group check at term close** (every pre-existing active group must be retained/dissolved/documented-retained; no silent pass-through). (5) §7.7 Pre-submission validation gains an **orphan-group validation bullet** — programmatically verifiable from the patch operations. (6) File naming consolidated on `wa-vcb-{batch_id}-...` across all VC session outputs; the earlier proposed per-registry alternative is dropped for consistency. (7) `_patch_meta.batch_id` remains required; `registry` added as optional informational field. (8) §5.2 "never split a term" reworded as "never split a term across input documents". (9) §6.4 Session discipline reworded: primary input is the Session A `.md`; discipline rules (dual-write, progressive observations, versioning) unchanged. Full change rationale in `outputs/investigations/vc-instruction-session-a-md-alignment-v2-20260424.md`.<br />**v2_9 (20260424):** Programme-prose-aware start-up. (1) §6.1 Startup step 1 revised — Claude AI must now also read the programme-prose section `prog_instr_session_a` from the most recent programme-prose extract (`data/exports/reference/wa-programme-prose-extract-{YYYYMMDD}.md`) before beginning work. This carries the Session A content boundary (STEP-sourced data only; no downstream-stage content leaks in either direction) directly into the classifier's working context. (2) §6.1 new step 2 — read `prog_instr_verse_context` from the same programme-prose extract; state the role-of-VC framing aloud before opening the classification input. v2_9 is an Ask (a)-only update; the larger alignment landed as v3_0.<br />**v2_8 (20260418):** GR-REF-002 sweep. (1) Filename migrated to current naming convention (underscored version, compact date, lowercase per GR-FILE-003/GR-FILE-007/GR-FILE-009). (2) Companion documents row updated to `[current]` token per GR-REF-002 for operational references. (3) Governing Rules section pointer migrated to `[current]`. (4) Footer supersession line refreshed. Historical change notes (v2_7, v2_6 etc.) retained below for provenance.<br />**v2_7 (20260414):** Manual changes by researcher: (1) Purpose and Scope: change pipeline stage to between Phase 1 completion and Dimension Review.<br />**v2_6 (20260414):** Global rules integration. (1) Governing Rules header added — mandatory load of the global rules file before session start. (2) Section 3.3 borderline retention paragraph replaced with reference to GR-PROG-004. (3) Section 6.2 Step 2 all-verses-fail principle statement ("individual inspection mandatory and non-waivable") replaced with reference to GR-PROG-005; operational deferred-flag procedure retained. (4) Section 6.4 write-on-discovery principle statement replaced with reference to GR-OBS-001; dual-write rule updated to reference GR-FILE-008. (5) Companion documents updated: DataPrep-Instruction removed (retired); patch\_specification updated to v1.10; SessionB updated to v4.8. All filename examples in output table updated to compact date format per GR-FILE-009.|
|Companion documents|wa-reference [current] │ wa-patch-instruction [current] │ wa-dimensionreview-instruction [current] │ wa-sessionb-analysis-readiness [current] │ wa-sessionb-analysis-output [current]|
|Inputs|**Primary:** per-term Session A `.md` — `wa-{nnn}-{word}-{strongs}-session_a-{date}.md` produced by `scripts/build_session_a_prose.py --term` or `--registry-per-term` from `data/exports/session_a/terms/`. Self-contained per OWNER term; carries all STEP-sourced data for that term + prior verse_context state + a pointer list of other terms in the registry for wrong-face reference. A session may introduce one term or many — the session is the researcher-composed unit. │ **Hybrid secondary:** per-registry Session A `.md` — `wa-{nnn}-{word}-session_a-{date}.md` in `data/exports/session_a/`. Retained for researcher review, Dimension Review hand-off, and human overview. Not the classifier's primary input. │ **Legacy fallback:** Verse Context batch JSON — `wa-vcb-{batch\_id}-extract-{date}.json` — deprecated; retained for rare split-session compatibility; per-term `.md` handles the split-session case natively. │ **Source material (Claude Code internal):** engine `--export-word` JSONs in `data/exports/STEP Extracts/`; live database.|
|Outputs|Verse Context patch — `wa-vcb-{batch\_id}-patch-v{n}-{date}.json` (Claude AI → Claude Code) │ Observations file — `wa-vcb-{batch\_id}-term-observations-v{major}.{minor}-{date}.md` (Claude AI, progressive) │ Session log — `wa-vcb-{batch\_id}-session-log-{scope}-v{n}-{date}.md` (Claude AI, at breakpoints) │ Flags register — `wa-vcb-{batch\_id}-flags-register-v{n}-{date}.md` (Claude AI, end-of-batch flag resolution) │ Session B flags — `wa-vcb-{batch\_id}-sessionb-flags-v{n}-{date}.md` (Claude AI, when Session B flags raised) │ Fresh Session A `.md` re-render per registry on completion (Claude Code → next stage)|
|Claude AI role|Reads programme-prose start-up sections; declares prior-state posture (FRESH or RE-EVALUATION); verse reading; relevance filtering; contextual grouping; anchor designation; per-term re-evaluation self-check + orphan-group check; patch production|
|Claude Code role|Per-term Session A `.md` rendering from database (primary); per-registry hybrid render on demand; patch application; group_code resolution; XREF status propagation; **per-term `mti_terms.vc_status` update on successful apply**; **derived `word_registry.verse_context_status` aggregation from term states**; orphan-group validation; integrity validation; completion reporting at term and registry scope; Session A `.md` re-render on status change|
|Interaction model|Per-term Session A `.md` rendered from current DB state → programme-prose + instruction loaded; per-term prior-state posture declared → Claude AI classifies (session scope = 1..N terms at researcher discretion) → per-term self-check + orphan-group check on re-evaluation terms → VERSECONTEXT patch with `_patch_meta.terms_covered` → Claude Code applies, validates per term, flips `mti_terms.vc_status` per term, derives registry-level `verse_context_status` from the aggregate → Dimension Review gate opens when a registry reaches aggregate completeness|

**File-naming note:** All VC session outputs use the `wa-vcb-{batch\_id}-...` pattern. `batch_id` is a session identifier assigned by Claude Code; it does not imply multi-registry scope. A session can hold one term or many — the patch, observations file, session log, flags register, and Session B flags all carry the same session id. Per-term Session A `.md` inputs use the registry+strongs-scoped pattern `wa-{nnn}-{word}-{strongs}-session_a-{date}.md` (the input is scoped to a term; the session outputs are scoped to the session).

\---

## Governing Rules

This instruction is governed by **wa-global-general-rules [current]**.

Claude AI must confirm the global rules file has been loaded before beginning any work in this session. State aloud per GR-LOAD-001.

Rules stated in the global file are not repeated here. Where a section references a global rule, the rule ID is cited.

\---

## 0\. Purpose and Scope

This document governs the Verse Context stage — the pipeline stage between Phase 1 completion and Dimension Review. Session B analysis follows Dimension Review. It covers the full cycle: Claude Code renders per-term Session A `.md` inputs from the database; Claude AI classifies one or more terms in a session; Claude Code applies the resulting VERSECONTEXT patch, per-term validation, per-term `vc_status` writes, and derived registry-level aggregation.

**What Verse Context does:**

* Classifies every verse for every active OWNER term in a session, term by term
* Filters each verse: does the term, in this verse, engage the inner being?
* Groups relevant verses by the inner-being characteristic they engage (characteristic-perspective)
* Designates anchor verses — the canonical citation and primary Session B analysis input per group
* Produces a session patch (`VERSECONTEXT`) covering all terms classified in the session; the patch declares `_patch_meta.terms_covered`
* On apply, writes `mti_terms.vc_status = 'complete'` per term — the atomic unit of VC progress is the term

**What Verse Context does NOT do:**

* Analyse the meaning of terms in depth — that is Session B Analysis
* Draw conclusions about the word being studied — that is Session B Analysis
* Produce cross-registry synthesis — that is Session D
* Assign evidential status to terms — that is Session B Analysis
* Classify XREF terms directly — XREF status is derived from OWNER classification (see Section 0.2)
* Advance `word_registry.verse_context_status` itself — that value is a **CC-side derived aggregation** from the per-term `vc_status` states (see §13)
* Re-render or re-export any artefact itself — per-term `.md` regeneration and the optional per-registry hybrid `.md` are CC-side operations triggered on demand or as downstream stages require

**Stage sequence:**

```text
Phase 1 complete (session_b_status, audit_word COMPLETE)
     │
     ▼
Verse Context (this document)
  ├── Claude Code: per-term Session A `.md` rendering from the database
  ├── Claude AI: per-term classification session (researcher composes 1..N terms)
  ├── Claude AI: VERSECONTEXT patch with _patch_meta.terms_covered
  ├── Claude Code: patch application + per-term R1–R4 / orphan-group / coverage validation
  ├── Claude Code: write mti_terms.vc_status = 'complete' per term on successful validation
  ├── Claude Code: derive affected registries (OWNER + XREF-via-OWNER)
  ├── Claude Code: aggregate check → word_registry.verse_context_status = 'Complete' where all qualify
  └── loop until every OWNER + XREF-via-OWNER term of every registry reaches complete
     │
     ▼
Session B DataPrep (word_registry.verse_context_status = 'Complete' opens the gate)
     │
     ▼
Session B Analysis → Session B Extraction → Session D
```

|This document is self-standing. It does not rely on session memory. Claude Code requires this document and access to the database. Claude AI requires this document, the latest `prog_instr_session_a` and `prog_instr_verse_context` sections of the programme-prose extract, and the per-term Session A `.md` inputs for the session.|
|-|

\---

## 0.1 Pipeline Entry Point — What Already Exists

**Before any Verse Context work begins, the following is already in place:**

Session A has run for every non-excluded registry (currently 184 of 214 registries; the 30 excluded carry `phase1_status = 'Excluded'` and no verse data). Each processed registry has:

* All OWNER terms extracted into `wa_term_inventory` and `mti_terms`; verse records populated in `wa_verse_records`; `mti_term_id` links present
* Audited by `audit_word` (WR-01 through WR-20) with outcome `COMPLETE`
* `session_b_status` set per programme state (commonly `Verse Context Reset` when a re-run is expected)
* `verse_context_status` set per programme state (varies — `Complete` for registries already classified in the prior cycle; `In Progress` or `NULL` for those awaiting a fresh classification)
* `verse_context_group` and `verse_context` tables: populated where prior classification occurred; empty where classification has not yet begun

**Classifier input — the per-term Session A `.md`:** Claude Code renders one `.md` per OWNER term via `scripts/build_session_a_prose.py --term` (or `--registry-per-term` to fan out an entire registry) from the current database state. Each per-term `.md` is the classifier's input for that term's portion of a session. It is self-contained — it carries the term's STEP-sourced data (meaning, verses, lexical layer), any existing `verse_context_group` rows for the term (active and dissolved), per-verse prior classification state where records exist, and a pointer list of other terms in the registry for wrong-face reference. It states a per-term **prior-state posture** (FRESH or RE-EVALUATION) in its header based on counts of prior groups for that single term. See §5 for input preparation details and `docs/prose-store-architecture.md` for the underlying prose-store model.

**Session composition is researcher-driven.** A session can introduce one per-term `.md` or several. There is no registry-level bundling requirement at the input layer — the atomic unit of VC is the term, and sessions compose from that unit. The per-registry Session A `.md` is still available as a hybrid secondary view for humans and downstream stages (Dimension Review reads registry-scoped state); it is not the classifier's primary input.

**Registry-level signal is CC-side derived.** The programme still needs a registry-level Complete signal — DataPrep (and, thereafter, Dimension Review) reads `word_registry.verse_context_status`. But that signal is no longer produced by VC itself. VC operates per term, writing `mti_terms.vc_status = 'vc_completed'` on each successful per-term apply. Claude Code then aggregates: once all OWNER terms (with verses) and all XREF terms' OWNERs for a registry are at `vc_completed`, Claude Code advances the registry's `verse_context_status` to Complete. See §13 and `scripts/apply_session_patch.py` (VC-2 extension) for the derivation logic.

**Legacy batch JSON — deprecated:** the `wa-vcb-{batch_id}-extract-{date}.json` format that preceded the `.md` renderer is retained in Annexure D for historical reference but is no longer a primary or fallback input form. The per-term `.md` handles both small-session and large-term cases natively; there is no split-registry use case the `.md` cannot serve directly.

**Database sources Claude Code reads to produce the per-term `.md`:**

* `word_registry` — registry identity, status, synopsis, inference_note
* `wa_file_index` — file provenance per registry
* `wa_term_inventory` — OWNER and XREF terms (`term_owner_type`, `delete_flagged = 0`)
* `mti_terms` — canonical term records (`status IN ('extracted', 'extracted_thin')`)
* `wa_verse_records` — verse records for each OWNER term (`delete_flagged = 0`)
* `wa_meaning_parsed` / `_sense` / `_stem` / `wa_lsj_parsed` — lexical layer
* `wa_term_related_words` / `_root_family` — lexical neighbourhood
* `wa_data_quality_flags` — informational flags (post-M29)
* `verse_context_group` / `verse_context` — existing classifications (shown as Prior state)
* `wa_cross_registry_links` — structural pointers
* `wa_obs_question_catalogue` + `wa_flag_type_question_link` — open catalogue questions

\---

## 0.2 XREF Terms — How They Are Handled

XREF terms are not classified by Claude AI. Their verse\_context status is derived from the OWNER term's completed classification. This section specifies exactly what Claude Code does with XREF terms.

**Background:** A XREF term is a Strong's number that appears in a registry's term inventory but whose primary analytical home (OWNER) is in a different registry. XREF verse records are delete\_flagged — they are excluded from all analysis. The term identity (`mti\_terms.id`) is shared across OWNER and XREF.

**Because verse\_context uses `mti\_term\_id` (FK to `mti\_terms.id`) as its key — not the term inventory id — the OWNER's verse\_context records are automatically visible to any registry that shares that term.** There is no separate XREF verse\_context record to create. The OWNER's classification is the programme-wide classification for that term.

**What Claude Code must do after every VERSECONTEXT patch:**

For each XREF term whose OWNER term appears in the completed session's patch:

1. Check whether the OWNER term now has `verse_context` records (i.e. has been classified in this or a prior session)
2. If yes: the XREF term is considered covered — no verse_context insert needed. The XREF term's registry can query verse_context via `mti_term_id` and will see the OWNER's groups and classifications
3. Include this coverage in the registry completion aggregation (§13.1 and §13.2): a registry is complete when all its OWNER terms are at `vc_status = 'vc_completed'` AND every XREF term's OWNER is at the same

**What this means for the completion check:**
A registry's `verse\_context\_status` advances to Complete only when:

* All its OWNER terms (with verses) have `verse\_context` records; AND
* All its XREF terms have an OWNER term that has `verse\_context` records

This second condition ensures that Session B Analysis, when it reads the pool analysis dataset, will find complete contextual profiles for every term — both OWNER and XREF.

**Claude Code query to check XREF coverage for a registry:**

```sql
-- XREF terms in this registry whose OWNER has not yet been classified
SELECT DISTINCT mt.strongs\_number, mt.owning\_registry\_fk, wr2.word as owner\_word
FROM wa\_term\_inventory ti
JOIN wa\_file\_index fi ON fi.id = ti.file\_id
JOIN word\_registry wr ON wr.id = fi.word\_registry\_fk
JOIN mti\_terms mt ON mt.strongs\_number = ti.strongs\_number
JOIN word\_registry wr2 ON wr2.id = mt.owning\_registry\_fk
WHERE wr.no = {registry\_no}
  AND ti.term\_owner\_type = 'XREF'
  AND ti.delete\_flagged = 0
  AND NOT EXISTS (
    SELECT 1 FROM verse\_context vc WHERE vc.mti\_term\_id = mt.id AND vc.delete\_flagged = 0
  );
-- If any rows returned: XREF terms unresolved — registry cannot advance to Complete yet
-- If zero rows: all XREFs covered — combine with OWNER check for complete assessment
```

**Reporting:** When Claude Code reports completion status, it must distinguish: "Registry {nnn} — {word}: OWNER classification complete, XREF coverage complete → verse\_context\_status set to Complete" vs "OWNER complete, {n} XREF terms pending OWNER classification in registries {list}".

\---

## 1\. The Two-System Model

|**System**|**Role**|
|-|-|
|Claude AI|Reads verse text. Applies the relevance filter. Produces contextual meaning descriptions. Groups verses. Designates anchors. Identifies dual-context. Produces the patch file.|
|Claude Code|Renders the per-term Session A `.md` from the live database (primary input for the classifier). Renders a per-registry hybrid `.md` on demand for researcher review and Dimension Review hand-off. Applies VERSECONTEXT patches. Resolves group_code to integer id. Handles XREF coverage. On successful per-term validation, writes `mti_terms.vc_status = 'complete'` + `vc_instruction_version` + `vc_status_updated_at`. Derives `word_registry.verse_context_status` from the aggregate of OWNER + XREF-via-OWNER term states. Re-renders any affected per-term `.md`s on demand. Validates consistency rules (R1–R4) including orphan-group validation. Runs integrity checks. Reports completion at term and registry scope. Does not assess verse relevance or produce contextual descriptions.|

|**⚠ Claude Code does not assess verse relevance, produce contextual meaning descriptions, or designate anchors. All classification is Claude AI's responsibility.**|
|-|

\---

## 2\. Database Tables

### 2.1 `verse\_context\_group`

|Field|Type|Notes|
|-|-|-|
|id|INTEGER PK|Used for all joins — never use group\_code as join key|
|mti\_term\_id|INTEGER FK|→ mti\_terms.id — programme-wide term identifier, not registry-specific|
|group\_code|TEXT UNIQUE|`{mti\_term\_id}-{serial}` — human-readable, patch-constructable, never a join key|
|context\_description|TEXT|Brief phrase — inner-being engagement of the term in this group|
|notes|TEXT|Optional qualification|
|delete\_flagged|INTEGER|0 = active; 1 = dissolved (no physical deletes)|

### 2.2 `verse\_context`

|Field|Type|Notes|
|-|-|-|
|id|INTEGER PK||
|verse\_record\_id|INTEGER FK|→ wa\_verse\_records.id|
|mti\_term\_id|INTEGER FK|→ mti\_terms.id|
|group\_id|INTEGER FK|→ verse\_context\_group.id — NULL if is\_relevant = 0|
|is\_anchor|INTEGER|1 = anchor verse for its group|
|is\_relevant|INTEGER|0 = set aside; 1 = inner-being relevant|
|is\_related|INTEGER|1 = shares group meaning with anchor|
|set\_aside\_reason|TEXT|NULL if is\_relevant = 1. Controlled vocabulary when is\_relevant = 0 — see below.|
|notes|TEXT|Dual-context flags, borderline notes, revision reasons|
|delete\_flagged|INTEGER|0 = active; 1 = excluded (no physical deletes)|

**`set\_aside\_reason` controlled vocabulary** (applies when `is\_relevant = 0` only):

|Value|Meaning|
|-|-|
|`no\_inner\_being`|The term carries no inner-being content in this verse — the verse as a whole may or may not have inner-being content but this term does not carry it here|
|`physical\_only`|The term refers to a physical process, body part, or material object with no inner-being engagement|
|`spatial\_only`|The term is used in a locational or geographical sense with no inner-being engagement|
|`wrong\_face`|The verse contains inner-being content, but that content is carried by a different term — not by the term being classified. This verse belongs to another registry's analytical face. See Section 3.6 for the rediscovery procedure.|
|`other`|The set-aside reason does not fit the above categories. The `notes` field must explain.|

**Rule:** `set\_aside\_reason` must be populated for every `is\_relevant = 0` record from VCB-032 onward. It must be `NULL` for every `is\_relevant = 1` record. The `wrong\_face` value is the vertical-pass-enabling value — it marks verses that have analytical significance for a different registry's perspective, preserving that information for future rediscovery without re-reading the full corpus. Pre-VCB-031 set-aside records with `set\_aside\_reason = NULL` are a known gap; they will be populated in a future programme-wide audit if needed.

**Uniqueness:** UNIQUE on (verse\_record\_id, mti\_term\_id, group\_id). Same verse may appear under two groups for the same term (dual-context). Never twice in the same group.

**Programme-wide key:** `mti\_term\_id` is the same integer regardless of which registry views the term. OWNER and XREF registries query the same verse\_context records via this key.

### 2.3 Logical consistency rules

|Rule|Condition|
|-|-|
|R1|is\_relevant = 0 → group\_id IS NULL, is\_anchor = 0, is\_related = 0|
|R2|is\_anchor = 1 → is\_relevant = 1, is\_related = 0, group\_id NOT NULL|
|R3|is\_related = 1 → is\_relevant = 1, group\_id references a group with at least one active anchor|
|R4|Every term must have at least one active anchor before Session B may proceed|

\---

## 3\. The Governing Filter

Every verse is assessed against one question:

> \*\*Does this verse, through the use of this term, say something about the inner being — understood as the non-physical, internal states, capacities, and expressions that constitute a person's invisible life: how a person thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God?\*\*

**If yes:** classify the contextual meaning (Section 6).
**If no:** set aside (is\_relevant = 0). No further work for this verse.

### 3.1 What passes the filter

A verse passes when the term's use engages one or more of:

* An internal state — emotion, feeling, disposition, attitude
* A capacity of the inner life — will, intention, thought, belief, desire
* A relational orientation — how the person is oriented toward God, others, or themselves inwardly
* A moral or character quality of the whole person
* A spiritual characteristic — responsiveness to God, spiritual condition, worship disposition

### 3.2 What does not pass the filter

* **Purely physical use** (`physical\_only`) — the term refers to a body part, physical process, or material object with no inner-being engagement
* **Purely social or narrative** (`no\_inner\_being`) — external conduct or events with no window into the inner life through this term
* **Purely positional or geographical** (`spatial\_only`) — locating something in space or time
* **Wrong face** (`wrong\_face`) — the verse contains inner-being content, but that content is carried by a different term, not by the term being classified. See Section 3.6.

When setting a verse aside, record the appropriate `set\_aside\_reason` value from Section 2.2 in the patch. Do not leave `set\_aside\_reason` null for any set-aside record from VCB-032 onward.

|**⚠ Apply the filter to the term's specific use in this verse — not to the verse's general theme. A verse about covenant renewal may use the term in a purely legal sense with no inner-being engagement for this specific term. Filter at term level, not verse level.**|
|-|

### 3.3 Borderline cases

Per GR-PROG-004: where the filter decision is genuinely uncertain, retain (is\_relevant = 1) and record the uncertainty in the notes field. Accumulate uncertainty questions and resolve them at the end of each term's classification — do not stop mid-term.

### 3.4 Expressions as inner-being evidence

Where a term names a human act of expression — vocal, physical, or behavioural — the relevance filter is satisfied if the act plausibly originates in an inner state rather than being purely mechanical or reflexive. The direction of travel (inner state → outward expression) is itself inner-being data. The inner state need not be named explicitly in the verse; its presence may be inferred from the nature and force of the expression.

**What this means in practice:**

* A cry, call, or shout that carries urgency, distress, longing, outrage, or devotion passes the filter — even if the verse does not name an inner state explicitly. The force and character of the expression implies its inner origin.
* A groan, gesture, or act of worship passes when the expression plausibly reflects an inward disposition rather than a trained reflex or mechanical procedure.
* Administrative, liturgical, or physical acts with no personally engaged human agent (a procedure to be followed, a reflex without agent) do not pass on this basis alone.

**Rationale:** The inner being is the origin of human expression. Separating the expression from its inner origin would remove part of the causal chain from view. Every human act of expression originates somewhere in the person; the nature of that origination is significant inner-being data.

**Boundary:** This principle applies where the term itself names the act of expression, not merely a verse that happens to contain an expressive act. The term must carry the expression for Section 3.4 to apply.

**Where the distinction is uncertain:** retain (Section 3.3 applies).

*Programme note: This principle was established as RD-PC-001 during VCB-003 patch construction, arising from classification of H7121I (qa.ra call-out). It applies from VCB-004 onward and was applied retrospectively to H7121I in VCB-003.*

\---

### 3.5 Grammatical and functional particles

Where a term is a grammatical or functional particle — including pronouns, quantifiers, interrogatives, conjunctions, adverbs, particles of entreaty, and similar grammatical elements — the relevance filter requires an explicit assessment of how the particle functions in the specific verse, not merely whether the verse contains inner-being content.

**A grammatical particle passes the filter if it:**

* **Directs** inner-being content — orients a question, command, or assertion toward an inner-being subject (e.g. an interrogative pronoun framing a question about inner identity or moral worth)
* **Intensifies** an inner-being state or act — amplifies, sharpens, or emphasises the force of an inner-being expression
* **Qualifies the scope** of an inner-being condition — universalises, restricts, or otherwise shapes what an inner-being statement covers (e.g. a quantifier applied to a moral condition)
* **Discloses an inner orientation** through the manner in which it frames inner-being content — e.g. a particle of entreaty that reveals the posture of the speaker before God

**A grammatical particle does not pass the filter if it is:**

* **Purely syntactic** — present as a grammatical requirement with no semantic contribution to inner-being content
* **A social register marker** — indicating politeness, courtesy, or social function without inner-being implication
* **A temporal connector** — linking events or states in time without contributing to the inner-being dimension
* **Procedural filler** — serving a formal function in legal, liturgical, or administrative text with no personal inner-being engagement

**The test:** Remove the particle from the verse mentally. Does the inner-being content change meaningfully in how it engages the inner being? If the particle's presence shapes, frames, or intensifies that engagement, it passes. If the inner-being content is identical with or without the particle, it does not.

**Where the distinction is uncertain:** retain (Section 3.3 applies).

*Programme note: This section was added in v2.2, arising from programme flags PF-VCB007-001. It applies from VCB-008 onward. Applicable retrospectively to VCB-007 classifications of H4310 mi and H3605 kol, which were classified under this criterion during VCB-007 processing even before it was formally codified.*

\---

### 3.6 Wrong-face set-asides

A verse is a **wrong-face set-aside** when it contains genuine inner-being content — but that content is carried by a different term in the verse, not by the term currently being classified. The verse is analytically significant; it simply does not belong to this term's classification face.

**Examples:**

* Jer 7:24: "they walked in the stubbornness of their evil hearts" — when classifying *sha.ma* (hear/listen), the inner-being content is carried by *lev* (heart) and *she.ri.rut* (stubbornness), not by *sha.ma*. The refused hearing is a consequence of the stubborn heart, not the inner-being subject. Set aside for *sha.ma* with `set\_aside\_reason = 'wrong\_face'`.
* A verse about forgiveness where *ne.phesh* (soul) carries the inner-being content but the term being classified is a grammatical particle present in the same verse.

**When to use `wrong\_face`:**

* The verse passes the general relevance question ("does this verse contain inner-being content?") — yes
* The term-specific relevance question ("does this term carry the inner-being content?") — no
* The inner-being content in the verse is identifiably carried by a different term with its own registry

**When not to use `wrong\_face`:**

* The verse simply has no inner-being content at all — use `no\_inner\_being`, `physical\_only`, or `spatial\_only`
* The term partially carries the inner-being content (even weakly) — retain rather than set aside (Section 3.3)

**Patch treatment:**
Set aside normally (is\_relevant = 0, group\_id = null). Set `set\_aside\_reason = 'wrong\_face'`. In the `notes` field, identify which term carries the inner-being content and which registry it belongs to, where known: e.g. `"wrong\_face: inner-being content carried by lev (H3820A, Reg 183)"`.

**Rediscovery procedure:**
When a future analytical session (vertical pass, Session B cross-registry review, or programme audit) examines a verse across multiple registry faces, wrong-face set-asides are queryable:

```sql
SELECT vc.verse\_record\_id, vc.mti\_term\_id, vc.notes, vr.verse\_text
FROM verse\_context vc
JOIN wa\_verse\_records vr ON vr.id = vc.verse\_record\_id
WHERE vc.set\_aside\_reason = 'wrong\_face'
  AND vc.mti\_term\_id = {target\_mti\_term\_id};
```

This returns all verses set aside as wrong-face for a given term — i.e. verses where the term is present but the inner-being content belongs to a different face. The `notes` field identifies which term carries the content, enabling cross-registry analysis.

*Programme note: This section was added in v2.5, arising from VCB-031 vertical pass experiment. The `wrong\_face` value enables the vertical pass model to be applied to the existing VC classification corpus without re-reading every verse. Applies from VCB-032 onward.*

\---

**Dual purpose:**

1. **Efficiency instrument** — Session B Analysis reads anchor verses, not the full verse corpus. Verse Context reduces 133,353 active verses to a small set of anchors that carry the essential inner-being content for each term.
2. **Citation instrument** — anchor verses appear in Session B narratives and Session D synthesis as the evidential foundation for claims about the term

**Selection criteria:**

* Makes the contextual meaning evident without requiring surrounding context
* The term's inner-being function is unambiguous in the verse
* Stands alone as evidence — does not depend on interpretation of adjacent passages

**Minimum requirement:** every term must have at least one active anchor across all its groups (Rule R4). A term with no anchor cannot proceed to Session B Analysis. This is an absolute gate — Claude Code enforces it in the completion check.

**Quantity:** 1–2 anchors per group. Where two are designated, they represent distinct aspects of the group's meaning. Do not designate more than 2 unless a third genuinely adds something the first two do not.

**When no clear anchor exists:** if a group's verses are all contextually dependent (require surrounding passage to make sense), designate the least dependent one as the anchor and note the limitation. Do not leave a group without an anchor.

\---

## 5\. Claude Code — Input Preparation

The classifier's primary input is the **per-term Session A `.md`**. Claude Code renders one `.md` per OWNER term from the live database via `scripts/build_session_a_prose.py --term` (or `--registry-per-term` to fan out a whole registry). Each per-term `.md` is self-contained, carries STEP-sourced data for that single term plus any prior `verse_context` state, and is human- and AI-readable. A session is researcher-composed from one or more per-term `.md`s. The per-registry `.md` is produced on demand as a hybrid secondary view (researcher review, Dimension Review hand-off). The legacy batch JSON format is deprecated (see Annexure D).

### 5.1 Trigger

Claude Code renders (or refreshes) per-term Session A `.md`s:

* At the start of every classification session — for each term the researcher includes in the session
* After a VERSECONTEXT patch is applied — refresh the affected terms' `.md`s to reflect new DB state
* When researcher instructs a fresh render (e.g. after an `audit_word` re-run adds verses to specific terms, or a directive flips terms to `to_revise`)
* When a per-registry hybrid view is needed for a downstream stage (Dimension Review hand-off) — rendered via `--registry-per-term` composed into the registry view

### 5.2 Input selection criteria

**Per-term selection (the default):**

* **OWNER terms only** — `wa_term_inventory.term_owner_type = 'OWNER'`, `delete_flagged = 0`
* **Active terms only** — `mti_terms.status IN ('extracted', 'extracted_thin')`
* **Terms with verses only** — at least one `wa_verse_records` row where `delete_flagged = 0`
* **Existing `verse_context` state rendered per term** — this term's `verse_context_group` rows (active and dissolved) and its `verse_context` per-verse records included so the classifier can review and revise; drives the per-term posture declaration at §6.1
* **Term identifier scope** — the `.md` filename carries the registry number, word, and Strong's: `wa-{NNN}-{word}-{strongs}-session_a-{date}.md`

**Multi-term session composition (researcher-composed):**

* A session can cover one term or many — the researcher composes the session's term list based on analytical priority, verse-count budget, clustering, or any other criterion
* **Never split a term across input documents** — all verses for a single term must appear in one per-term `.md`
* **Session identifier** — Claude Code assigns a sequential `VCB-{nnn}` session id; that id names all session output artefacts (patch, observations, session log, flags register, Session B flags). `batch_id` is retained as the field name for the session id
* **Session budget guide (soft)** — when the composed session's verse count across its terms exceeds ~1,500, consider splitting into successive sessions. This is a practical soft limit, not a rule

**SQL policy:** SQL query construction is Claude Code's responsibility. This section provides all criteria, field names, derivation rules, and expected outcomes required. Claude Code derives the query from these specifications and the current schema. An "unclassified verse" is any `wa_verse_records` row (`delete_flagged = 0`) for an OWNER term that has no corresponding `verse_context` row for the matching `mti_term_id`.

### 5.3 Input document structure — the per-term Session A `.md`

Each per-term Session A `.md` is scoped to a single OWNER term and organised under six section families parallel to the seeded `prose_section_type` handles (`sa_s1_d1` … `sa_s1_d6`): Word Summary (registry identity + this term's posture), Meaning (this term's lexical layer), Verses (this term's verses only), Terms (other terms in the registry — pointer list for wrong-face reference, §3.6), Pointers (cross-registry links + XREF matches for this term), Questions (catalogue questions linked to this term's flags). The header carries a **per-term Prior-state posture** block (FRESH or RE-EVALUATION with counts) and a **Method reminder** quoting the §3 filter and §6.2 Step 3 grouping model. The Verses section carries full ESV verse text, target word form, span-match indicator, and any Prior classification state (with group_code, is_relevant, is_anchor, is_related, set_aside_reason, notes, delete_flagged). Existing `verse_context_group` rows for the term — active and dissolved — are rendered in the header's posture block.

The per-registry hybrid `.md` (optional, researcher-discretionary) composes per-term blocks with a registry-level header for registry-scoped review; it is not the classifier's input.

The authoritative structural reference is `docs/prose-store-architecture.md` §5 (prose store stages) and the renderer source `scripts/build_session_a_prose.py`. Rendering is deterministic — running the renderer twice on unchanged DB state produces byte-identical output (modulo the generation timestamp).

**Source-table mapping** — the fields rendered in the per-term `.md` derive from the database tables listed in §0.1. Full mapping with derivation rules is in **Annexure D** (retained for historical reference to the deprecated batch JSON format that preceded the `.md` renderer).

### 5.4 Output file

**Primary output:** `data/exports/session_a/terms/wa-{NNN}-{word}-{strongs}-session_a-{date}.md` — the per-term Session A `.md`. Regenerated on demand per term; same-day regenerations overwrite (deterministic content). Handed to the Claude AI classification session as the classifier's input for that term.

**Hybrid secondary output:** `data/exports/session_a/wa-{NNN}-{word}-session_a-{date}.md` — the per-registry view composed of the registry's per-term blocks. Produced on request for researcher review and Dimension Review hand-off; not used by the classifier.

**Legacy batch JSON (deprecated):** `data/exports/verse_context/wa-vcb-{batch_id}-extract-{date}.json`. Retained in Annexure D for historical reference; not produced under v3_2.

\---

## 6\. Claude AI — Classification Workflow

### 6.1 Startup

On receiving one or more per-term Session A `.md` inputs that together compose the session:

1. Read this instruction document in full (or confirm it is already loaded for this session). Then read the programme-prose section `prog_instr_session_a` from the most recent programme-prose extract at `data/exports/reference/wa-programme-prose-extract-{YYYYMMDD}.md` (or the `.json` equivalent where only metadata+body is needed). State aloud: *"Session A content boundary understood: Session A carries STEP-sourced data only; no downstream-stage content is read from it or written into it."* This read is mandatory — the Session A boundary is part of the classifier's working contract, not a footnote.
2. Read the programme-prose section `prog_instr_verse_context` from the same programme-prose extract. State aloud: *"Verse Context's role understood — classify verses by term-level inner-being engagement; produce anchors; defer all interpretation to Session B."* This pairs the input-discipline statement (step 1) with the stage-role statement before the classifier opens any verse.
3. Load and parse the per-term Session A `.md` inputs for this session (one or more). The session-composition is researcher-driven; the classifier classifies whichever terms are presented.
4. **Version acknowledgement — mandatory, once per term (A-03 version gate).** For each per-term `.md` in the session, read the `md_version` from the header's version line and state verbatim:
    > *"Term {strongs} mti_id={n} loaded at md_version=v{n}. This is the version that will be declared in the patch's `_patch_meta.input_versions[{n}]`. If the DB's md_version for this term has changed by the time the patch is submitted, the patch will be rejected as stale."*
    Record the (mti_term_id, md_version) pair into the session's running versions map; this map becomes `_patch_meta.input_versions` in the VCNEW/VCREVISE patches (§7.2). If any `.md` is missing the `md_version:` header line, stop and request a fresh render — the input pre-dates the version-gate discipline and cannot be used under v3_4.
5. **Prior-state posture declaration — mandatory, once per term.** For each per-term `.md` in the session, read its "Prior-state posture (this term)" block in the About section and state verbatim one of the two templates below.
    * **FRESH posture** (no prior `verse_context` records for this term):
        > *"Prior-state posture for {strongs} ({transliteration}) mti_id={n}: FRESH. No `verse_context` records exist for this term. First-time classification. No orphan-group disposition required at term close."*
    * **RE-EVALUATION posture** (any prior records exist for this term):
        > *"Prior-state posture for {strongs} ({transliteration}) mti_id={n}: RE-EVALUATION. {m} active `verse_context_group` rows and {d} dissolved rows are present for this term. Every prior classification will be reviewed against the current filter and grouping model. Every pre-existing active group will be accounted for at term close — either retained with verses, dissolved, or carried without verses with a documented reason. No silent pass-through."*
    Per-term posture is binary (no registry aggregation). A session that covers four FRESH terms and three RE-EVALUATION terms declares seven separate postures, one per term, each at the point that term is opened for classification.
    If the counts `m / d` in the posture block do not match the counts visible in the input document's Existing verse_context groups table, stop and flag — the input may be mis-rendered.
6. State the startup summary (Annexure A template) — now term-scoped: list the terms in the session with their `mti_term_id`, Strong's, registry, `md_version`, and posture.
7. Note any term whose active verse_context state is fully in place and internally consistent (R1–R4) — review without re-classifying unless a revision is clearly warranted (see revision rule in Section 6.2 Step 2).
8. Note any term with existing `verse_context` records but incomplete coverage (some verses classified, others not) — flag to researcher before continuing (partial completion rule in Section 6.2 Step 2).
9. **Processing order:** Terms are processed in the order they appear in the session's input list, which is the researcher's session-composition order. Registry-ascending order is no longer an imposed discipline at the input layer — the researcher composes the session, the classifier follows its order.

### 6.2 For each term — complete this sequence before moving to the next term

**Step 1: Read all verses**
Read every verse in the term's verse array. Do not skip. Do not begin classifying while reading. Note the term's gloss and any existing\_groups before beginning. Understand what the term means before filtering verses.

**Step 2: Apply the relevance filter**
For each verse, apply the governing filter (Section 3).

* If an existing verse\_context record is present, review it — but do not assume it is correct. You may revise prior classifications if a revision is clearly warranted (see revision rule below).
* Mark each verse: Relevant (is\_relevant = 1) or Set aside (is\_relevant = 0).

**All-verses-fail rule:** Per GR-PROG-005 (non-waivable): if every verse for a term fails the relevance filter, individual inspection of every verse is mandatory before reaching this finding — no sampling regardless of corpus size. Once full individual inspection is complete, the all-verses-fail finding is treated as a deferred flag under the Deferred Flag Protocol (Section 6.5). Do not stop mid-classification. Accumulate the finding, record it in the flags register, and continue classifying. The finding must be documented with: term identity, verse count, the basis for the finding, and confirmation that individual inspection was completed for all verses.

**The only condition that triggers an immediate stop** is a structural data integrity failure that would prevent correct classification of subsequent verses — for example, a partial completion anomaly in the input (some verses already classified but the term's classification state is not complete). In all other cases, including all-verses-fail and all borderline classification decisions, proceed and defer to the end-of-session flag session.

**Partial completion rule:** If a term has existing verse_context records (some verses already classified) but the term's active verse_context rows do not cover every active verse, this indicates a prior session was not completed correctly. This is an error condition. Stop for this term. Flag to the researcher with: the term details, which verses are classified, which are unclassified, and the reason for incompleteness if discernible. Await researcher instruction. The session's patch must not proceed for this term until the researcher has confirmed how to resolve it.

**Revision criterion for term\_classification\_complete = true:** A revision is clearly warranted when: (a) the existing context\_description would materially misrepresent the term's inner-being function in light of the full verse set now visible; or (b) a clearly stronger anchor verse is available and the designated anchor is demonstrably weaker. When a revision is made, Claude AI must: record the reason for the revision in the verse\_context notes field; and include a clear description of what changed and why in the per-term classification summary (Annexure B) so the researcher can review the change.

**Step 3: Group relevant verses**
Ask for each relevant verse: **does this verse engage the same inner-being characteristic through this term as verses already assigned to a group?**

* If yes → assign to that group
* If no → check existing\_groups first; assign to an existing group if appropriate; only create a new group if no existing group fits

**Characteristic-perspective grouping model:**

Groups must be formed from the perspective of the inner-being characteristic the verse cluster is primarily about — not from the perspective of what the term does. This distinction matters because:

* **Characteristic terms** name an inner-being state directly (e.g. *lev* = heart, *ne.phesh* = soul, *pistis* = faith). Their groups are naturally characteristic-centred.
* **Property terms** describe how inner-being characteristics operate — their mechanism, condition, expression, or channel (e.g. *sha.ma* = hear/listen, *o.zen* = ear, *akoē* = hearing). Property terms can serve different characteristics across their verse corpus, and can serve the same characteristic in opposite ways (e.g. receptive hearing as the channel of faith; refused hearing as the expression of heart-stubbornness).

**For property terms especially:** the group description must name the characteristic being served — not just the term's function. A group called "refusing to hear God" is term-centric. A group called "heart-stubbornness expressed through refusal of God's word" is characteristic-perspective. The difference is analytically significant: Session B analyses characteristics, and group descriptions must map to that analysis correctly.

**Forming context\_description:** A brief phrase (one sentence maximum) capturing what the group says about the inner being. It must:

* Name the inner-being characteristic the verse cluster primarily engages
* State the term's role accurately relative to that characteristic (as seat, expression, channel, mechanism, obstacle, or counterpart)
* Be grounded in what the verses show — not in prior theological knowledge
* Be sufficient to distinguish this group from others for this term

Examples of well-formed descriptions under the characteristic-perspective model:

* *Term names the inner seat of the emotion of fear — the place where fear arises and is registered* (characteristic: fear; term's role: seat)
* *Term serves as the channel through which faith arrives — hearing as the mechanism of faith reception* (characteristic: faith; term's role: channel)
* *Term expresses the stubbornness of the heart — refusal to hear as the outward form of inner resistance* (characteristic: stubbornness; term's role: expression)
* *Term names the cognitive capacity of the inner person — the faculty by which wisdom is received and held* (characteristic: wisdom/understanding; term's role: faculty)

Examples of descriptions to avoid (term-centric, not characteristic-perspective):

* <i>~~Term describes an act of refusing to listen~~</i> — names what the term does, not what the verse is about
* <i>~~Term is used when God addresses people~~</i> — describes context, not the inner-being characteristic
* <i>~~Term indicates active, engaged hearing~~</i> — describes the term's behaviour, not the characteristic served

**Grouping criterion — when a new group is warranted:** A new group is warranted when the inner-being characteristic being engaged is materially different from all existing groups, or when the same characteristic is engaged in a materially different way. Materially different means: an analysis of the verses in the candidate group, evaluated against the existing groups, would arrive at a differential conclusion about the characteristic. The following factors indicate material difference: (1) a different inner-being characteristic is the primary subject; (2) the term serves the same characteristic in a distinguishably different role (e.g. seat vs. channel vs. expression); (3) the same characteristic appears in a materially different orientation (e.g. toward God vs. against God; positive vs. negative register). Minor variations in emphasis or tone within the same essential characteristic engagement do not warrant a new group. Where 5 or more groups emerge for a single term, pause and assess whether consolidation better serves the criterion before adding further groups. Note the count in the per-term summary.

**Step 4: Designate anchors**
For each group: designate 1–2 anchor verses meeting the criteria in Section 4.

If revising prior classification: a verse previously marked is\_related may be promoted to is\_anchor. A verse previously marked is\_anchor may be demoted if a better anchor is found — but ensure the group retains at least one anchor.

**Step 5: Identify dual-context verses**
Where a verse plainly operates at two distinct inner-being levels through the same term — assign to two groups. This is the exception, not the norm. Record the reason for dual-context in the notes field on both verse\_context rows.

**Step 6: Per-term classification summary and observations file write**
Before moving to the next term, state the summary (Annexure B template) and write the term's Classification blocks to the observations file immediately. This produces a readable record and the machine-parseable record simultaneously.

**v3_3 note — Session B / Session D observations raised during this term:** If while reading the term's verses the classifier noticed any analytical signal worth flagging for Session B or Session D (see §7.9.3), record each as a deferred flag in the observations file — tagged `session_target = 'Session B'` for SB observations, `session_target = 'Session D'` with the other registry's number for SD pointers. These accumulate into the session's VCSBFLAGS and VCSDPOINTERS patches at end-of-session (§7.9, §7.9.1, §7.9.4). Do not interrupt classification to resolve them; record and continue.

**Re-evaluation self-check — mandatory for every term that had prior `verse_context` records at session start:**

Before writing the Classification block to the observations file, state the self-check verbatim:

> *"Re-evaluation self-check for {strongs} ({transliteration}) mti_id={n}:*
> *— Active verses: N*
> *— Prior classifications reviewed: N (every active verse — mandatory)*
> *— Confirmed unchanged (is_relevant + group + is_anchor all unchanged): X*
> *— Revised is_relevant: Y*
> *— Revised group assignment: Z*
> *— Promoted to anchor: P*
> *— Demoted from anchor: D*
> *— Check: X + Y + Z = N? {yes/no}"*

If the arithmetic does not balance, every active verse was not accounted for. Stop and correct before proceeding. The balance-check is the numerical proof that "review every prior record" was performed. Terms with no prior records (FRESH terms in a RE-EVALUATION session) do not require the self-check — the standard Annexure B summary is sufficient.

**Orphan-group check — mandatory for every term that had prior `verse_context_group` records at session start:**

For every pre-existing active group for this term (from the Existing verse_context groups table in the input), after re-classification:

1. Count the active verses (`is_relevant = 1`, `delete_flagged = 0`) now assigned to the group.
2. If the count is zero, the group is an orphan.
3. Dispose of each orphan explicitly in the patch:
    * **Dissolve** (default) — emit an `update` operation on the group setting `delete_flagged = 1` and `notes = "dissolved — all verses reassigned in re-evaluation"` (or more specific reason).
    * **Retain** (rare) — only where the group is structurally meaningful and expected to carry verses from future work. Record a retention note in the observations file explaining why; emit no patch operation for the group; the group stays `delete_flagged = 0` with zero active verses.

State the check in the observations file immediately after the re-evaluation self-check:

> *"Orphan-group check for {strongs} mti_id={n}:*
> *— Pre-existing active groups: G*
> *— Active verse counts per group after re-classification: {group_code: count, ...}*
> *— Orphan groups (0 active verses): [list of group_codes] or NONE*
> *— Disposition per orphan: {group_code}: dissolved | retained ({reason})"*

No orphan may be left undisposed. Silent orphans are a pre-submission validation failure (§7.7).

**⚠ Classification block integrity rules — these govern the observations file as a machine-parseable source document:**

**Unique group codes:** Every Classification block written for a term must carry a unique `{mti\_id}-{serial}` group code. Once a code is written to the file (e.g. `235-001`), that code is permanently bound to the group it was first assigned to. It must not be reused for a different group in the same term entry, even if the original group is revised or abandoned.

**Mid-stream revision protocol:** If, during classification of a term, a group is revised or abandoned and replaced with a different group, the following steps are mandatory:

1. Mark the original Classification block explicitly as superseded by prepending `\~\~SUPERSEDED\~\~` to that block.
2. Assign the revised group a new sequential code (e.g. if `235-001` is superseded, the revision becomes `235-004` — the next available serial for that term).
3. Write the revised block with the new code immediately after the superseded block.
4. Update the SUMMARY line to reflect the final count of active (non-superseded) groups only.

**Why this matters:** The patch builder parses Classification blocks by group code. Duplicate codes for different groups cause the patch builder to conflate or dissolve correct groups along with incorrect ones. The superseded-block marking ensures the patch builder identifies and skips abandoned draft groups without ambiguity. This failure mode occurred in VCB-006 (H7451A group 235-001) and caused correct verses to be incorrectly set aside in the patch.

### 6.3 After all terms are classified

Review the full session classification summary. Then, before producing the VERSECONTEXT patch:

**Step 1 — End-of-session flag resolution (mandatory if any flags were deferred):**
Produce the flags register (Section 6.5) and present it to the researcher for decisions. Do not begin patch preparation until all flags are resolved. After the researcher provides decisions, update the observations file to reflect any classification changes arising from those decisions, increment the observations file version, and dual-write.

**Step 2 — Session B flags document (mandatory if any Session B flags were raised during flag resolution):**
Produce the Session B flags document (Section 6.6). This document must be completed before the patch construction session begins, as it forms part of the handoff chain to Session B.

**Step 3 — Produce the VERSECONTEXT patch (Section 7).**

### 6.4 Session discipline — file writing, session logs, and memory management

**⚠ This section governs how Claude AI manages its working process throughout a Verse Context session. These rules exist because context window exhaustion is the primary operational risk in large sessions.**

**Continuous file writing — observations file (per GR-OBS-001, non-waivable):**
The per-session observations file must be written progressively to disk during the session, not accumulated in memory and written at the end. Per GR-FILE-008 (dual-write): every write goes to both `/home/claude/` and `/mnt/user-data/outputs/`. The write discipline is as follows:

* **After every term** (Step 6 of Section 6.2): write that term's Classification blocks and SUMMARY line to the observations file immediately. Do not defer. Do not accumulate multiple terms before writing.
* **On every write**: increment the minor version number in the filename and in the file header (e.g. `v1.2` → `v1.3`). The version number is the only reliable differentiator between saves.
* **Version confirmation**: before each write, state aloud: *"Writing observations file — current version: v{n}. Incrementing to v{n+1}."* This confirms the save is occurring and makes the version progression visible in the session transcript.
* **Session log version reference**: every session log must state the current observations file version at the time of writing (e.g. *"Observations file at time of this log: wa-vcb-006-term-observations-v1.7-20260331.md"*). This creates a recoverable link between session logs and the observations file state they describe.
* **Continued-session startup**: at the start of every session that continues an existing VCB-{nnn} session id, Claude AI must confirm the observations file version it is reading before doing any work. State: *"Observations file loaded: {filename} version {v}. This is the most recent version and will be the base for continued writes."*

If the session is interrupted, the observations file must contain a complete record of every term classified up to that point, and the version number must reflect the last completed write.

**Unified file naming convention — all Claude AI outputs:**

All files produced by Claude AI during a Verse Context classification or patch construction session must follow this pattern:

```
wa-vcb-{batch\_id}-{scope}-{version}-{date}.{ext}
```

|Component|Rule|
|-|-|
|`wa-vcb`|Fixed prefix — always lowercase, always present|
|`{batch\_id}`|Session identifier (field name preserved as `batch_id` for backwards compatibility) — e.g. `003` for VCB-003|
|`{scope}`|Short descriptor of the file's content — see table below|
|`{version}`|Version string — see versioning rules below|
|`{date}`|Creation date in `YYYYMMDD` format — does not change on update|
|`{ext}`|File extension — `.md`, `.json`|

**Scope values for Claude AI outputs:**

|File type|Scope value|Example|
|-|-|-|
|Observations file|`term-observations`|`wa-vcb-003-term-observations-v1.2-20260331.md`|
|Session log|`session-log-{breakpoint}`|`wa-vcb-003-session-log-R19-v1-20260331.md`|
|Final session log|`session-log-final`|`wa-vcb-003-session-log-final-v1-20260331.md`|
|Flags register|`flags-register`|`wa-vcb-015-flags-register-v1-20260403.md`|
|Session B flags|`sessionb-flags`|`wa-vcb-015-sessionb-flags-v1-20260403.md`|
|Patch file|`patch`|`wa-vcb-003-patch-v1-20260331.json`|

**Breakpoint identifiers for session logs** — use the term-completion state of the session at that breakpoint:

* Single term: `mti142`, `mti1097` etc.
* Multiple terms in one log: `mti142-143-187`, or `terms1-4` where the ordering is session-composition order
* Final log covering all terms in the session: `final`

(Registry-range identifiers — `R19`, `R20-R23` — are obsolete under the per-term session model; they remain valid for pre-v3_2 historical session logs but should not be used going forward.)

**Versioning rules:**

* `{version}` always starts at `v1` for a new file
* For the observations file, which is updated progressively within a session, increment the minor version on each save: `v1`, `v1.1`, `v1.2`, etc. The version number is the only reliable differentiator between saves — do not rely on file size or timestamp
* For session logs and flag resolution files, which are written once per breakpoint, use `v1` unless a correction is issued, in which case increment: `v2`, `v3`, etc.
* `{date}` is the creation date and does not change when the file is updated

**Sorting behaviour:** All session outputs sort together under `wa-vcb-{batch\_id}-` when listed alphabetically, making the full session file set visible at a glance.

**Example — complete set for VCB-015:**

```
wa-vcb-015-flags-register-v1-20260403.md
wa-vcb-015-patch-v1-20260403.json
wa-vcb-015-session-log-classA-v1-20260403.md
wa-vcb-015-session-log-classB-v1-20260403.md
wa-vcb-015-session-log-classC-v1-20260403.md
wa-vcb-015-session-log-final-v1-20260403.md
wa-vcb-015-sessionB-flags-v1-20260403.md
wa-vcb-015-term-observations-v4.6-20260403.md
```

This convention applies from VCB-003 onward. Files produced before this version of the instruction are not retroactively renamed. **Mixed-case or non-standard prefixes (e.g. `WA-SessionLog-VCB003-...`) are a naming violation — do not use them.**

**Session logs at natural breakpoints:**
A session log must be produced at every natural breakpoint — completion of a term (or a group of terms), a researcher checkpoint, a context window warning, or a session close. Do not wait until the end of the session. Session logs must capture: terms classified, groups and anchors per term, all researcher decisions made, any open flags, and the work order for the next session. If the session ends unexpectedly, the most recent session log is the recovery point.

**No large in-memory accumulation:**
Do not hold growing data structures in memory across many terms. The observations file and session logs are the durable record. Patch operations should be derived from these files in a separate dedicated patch construction step, not accumulated in the classification session. When a session's cumulative verse count exceeds approximately **1,500 verses across all terms in the session**, treat patch construction as a separate session that reads the observations file and the per-term `.md` inputs as its source — not a continuation of the classification session. See deferred patch construction below. (A 1,500-verse threshold replaces the earlier 50-term threshold under the per-term model; for single-term sessions on very large OWNER terms, the same threshold applies.)

**Deferred patch construction — valid workflow:**
When a session is large enough that accumulating patch operations during classification would fill the context window, classification and patch construction are performed in separate sessions. This is the expected workflow for sessions covering many terms or a single very large term. Requirements for the deferred path:

* The observations file must contain a **Classification block** for every active term, in structured format: `{mti\_id}-{serial}: \*{context\_description}\* | Anchor: {ref} | Related: {ref, ...}`. This structured block is what the patch builder reads — prose-only entries cannot be reliably parsed. Write the Classification block for every term at classification time, even for terms with a single verse. The observations file provided to the patch construction session must be the most recent version (highest version number).
* The final session log before patch construction must contain a complete per-term table showing: mti\_id, Strong's, verse count, relevant count, group count, and anchor references. This table is the reconciliation check for the patch.
* The patch construction session must verify every anchor reference against the actual verse\_record\_ids in the per-term input before producing any operations. Anchor references that do not match the term's verse set must be corrected — they are typically reference format variants (e.g. `Jude 3` vs `Jud 1:3`) or verses assigned to a different term.
* The patch construction session must run programmatic pre-submission validation (Section 7.7) before producing the output file.

**Instruction document size awareness:**
This instruction document is long. When loading it alongside large per-term Session A `.md` inputs and an observations file, the combined context load is significant. Claude AI should read the instruction once at session start and not reload it unless a specific section is needed. For patch construction sessions, load only the observations file, the relevant per-term `.md` inputs, and Sections 7–7.7 of this instruction — not the full document.

\---

## 6.5 Deferred Flag Protocol

**⚠ This section replaces the previous per-term stop rule for all-verses-fail findings and borderline classification decisions. Flags that do not block the classification of other verses are accumulated during classification and resolved in a single interactive exchange at end-of-session, before patch preparation begins.**

### 6.5.1 What is a deferred flag

A deferred flag is any classification finding or question that:

* Does not prevent correct classification of the remaining verses in the session
* Requires researcher judgement before the patch can be correctly produced
* Would, under the previous protocol, have caused a mid-classification interruption

**Examples of deferred flags:**

* All-verses-fail findings (all verse counts, all term types)
* Borderline relevance judgements where the filter decision is genuinely uncertain
* Classification boundary questions (e.g. where a term's inner-being connection is indirect)
* Homograph split observations (informational flags, no decision required)
* Analytical observations that require researcher input before a Session B note can be formed

**The only condition that still triggers an immediate stop** is a structural data integrity issue that would prevent correct classification of subsequent verses — specifically, a partial completion anomaly where some verses for a term already have verse_context records but the term's active rows do not cover every active verse. This indicates a prior session was not completed correctly and must be resolved before continuing.

### 6.5.2 During classification — flag accumulation

While classifying, when a deferred flag arises:

1. Record the flag identifier (DF-{nnn}, sequential within the session) in the running flags list maintained in working memory or in the observations file notes
2. Make a working classification decision (typically: classify as best you can on current evidence, note the assumption made, continue)
3. For all-verses-fail findings: record the term identity, verse count, basis for the finding, and confirmation that individual inspection was completed for all verses
4. Do not interrupt the session. Do not present the flag to the researcher until the end-of-session flag exchange

### 6.5.3 End-of-session — producing the flags register

After all terms are classified, produce the flags register before the patch. The flags register is a structured document (not a prose summary) with one entry per flag.

**File:** `wa-vcb-{batch\_id}-flags-register-v1-{date}.md`

**Each flag entry must contain:**

1. **Flag identifier** — DF-{nnn} | term identity (Strong's, transliteration, gloss, mti\_id, registry)
2. **The verse(s) under consideration** — full verse text for every verse relevant to the flag. Do not use references alone. The researcher cannot make a sound judgement from references alone.
3. **The specific issue** — what was found and why a decision is required
4. **What each option means for the patch** — concrete patch consequence of each option: which verses will be classified as relevant or set aside, whether a group will exist or not, whether an all-verses-fail record will be produced
5. **Claude AI's own assessment** — state which option is analytically stronger and why, grounded in the verse texts, the filter criteria, and programme precedent. Label explicitly: *"Claude AI assessment: \[option/finding] is \[stronger/correct] because \[reason]."* Do not present options as equally weighted when one is clearly more consistent with programme criteria

**Format:**

```
### DF-{nnn} | {strongs} ({transliteration}) — {gloss} | mti\_id={n} | Registry {nnn} ({word})
\*\*Verse count:\*\* {n}
\*\*Finding / Issue:\*\* {description}

\*\*The verse(s):\*\*
vid={n} {ref}: \*"{full verse text}"\*
\[repeat for all relevant verses]

\*\*Option A:\*\* {description} — patch consequence: {what happens}
\*\*Option B:\*\* {description} — patch consequence: {what happens}
\[or: CONFIRM / OVERRIDE for all-verses-fail findings]

\*\*Claude AI assessment:\*\* {which option/finding, and why}

→ \*\*Your decision:\*\*
```

The register closes with a summary table listing all flags, their type, and Claude AI's recommendation. This allows the researcher to see the full scope before making decisions.

### 6.5.4 Receiving researcher decisions

The researcher returns the flags register with decisions recorded against each flag. On receiving it:

1. **Parse all decisions** before making any changes
2. **Update the observations file** — for each decision that changes a classification (e.g. moving verses to set-aside, confirming all-verses-fail), append a clearly marked decisions section to the observations file. Do not edit inline — append after the last term entry under the heading `## FLAG RESOLUTION DECISIONS — {date}`. This preserves the full classification record and makes the decision trail visible
3. **Record Session B flags** — for any flag where the researcher's decision includes an analytical observation or question for Session B exploration (see Section 6.6), record it in the Session B flags list
4. **Increment the observations file version** (e.g. v4.5 → v4.6) and dual-write after all decision updates are complete
5. **Proceed to Session B flags document** (Section 6.6) if any Session B flags were raised, then proceed to patch construction

### 6.5.5 All-verses-fail — patch treatment

For any term confirmed as all-verses-fail:

* No verse\_context records are inserted for this term
* The term proceeds to Session B with no anchor. Rule R4 (every term must have at least one active anchor before Session B may proceed) is noted as not applicable for this term
* The all-verses-fail finding is documented in the final session log

\---

## 6.6 Session B Flags

> **v3_3 framing change (A-01 resolution):** Under v3_3 the authoritative record of Session B observations raised during VC is the set of `wa_session_research_flags` rows written by the session's **VCSBFLAGS** patch (see §7.9). The `.md` file described below is now a **companion readable summary** of those rows, produced alongside the patch for human review — not the authoritative record. Session B loads its input set by querying the DB, not by reading the `.md`. See §7.9.6 for the query.

**Purpose:** The Session B flags document carries analytical insights and questions that emerge during Verse Context classification — from the researcher's flag decisions, from unexpected term behaviour, or from verse engagement that raises questions beyond the scope of the filter decision — into the Session B Analysis stage. Verse Context intentionally defers interpretation; this document is the formal channel through which Verse Context observations inform Session B.

**When to produce:** The **VCSBFLAGS patch** is produced at end-of-session whenever any SB-targeted flag was raised during classification (the authoritative record). The companion `.md` summary is produced alongside for human review.

**Files:**
- **Authoritative:** VCSBFLAGS patch — `wa-vcb-{batch_id}-patch-vcsbflags-v1-{date}.json` (see patch instruction [current] §15.4).
- **Companion readable summary:** `wa-vcb-{batch_id}-sessionB-flags-v1-{date}.md` — same content as the patch's rows, rendered for human review. Not used by the applicator or by Session B's DB reads.

### 6.6.1 What qualifies as a Session B flag

A Session B flag is raised when:

* The researcher's decision on a flag includes an explicit analytical question or observation for Session B to explore
* A term's classification raises an interpretive question that goes beyond the filter decision (e.g. the term behaves in a way that may reveal a previously unidentified inner-being dynamic)
* A researcher comment on a flag suggests a connection between terms, registries, or clusters that Session B should investigate

Session B flags are not corrections or errors. They are analytical starting points.

### 6.6.2 Content of each Session B flag entry

Each entry must contain:

1. **Flag identifier** — SBF-{batch\_id}-{nnn} (e.g. SBF-VCB015-001)
2. **Term and registry** — Strong's, transliteration, gloss, mti\_id, registry number and word
3. **Source** — which deferred flag triggered this Session B flag (DF-{nnn})
4. **The analytical question** — the question or observation the researcher raised, expanded with analytical context grounded in the verse corpus
5. **Suggested Session B exploration** — concrete lines of inquiry for Session B Analysis, including which group codes carry the most relevant verses, any cross-registry connections, and what the question implies for the programme's understanding of the inner being
6. **Relevant group codes** — the group codes in the observations file most directly relevant to this exploration

### 6.6.3 Position in the handoff chain

The Session B flags document must be provided to the Session B DataPrep and Analysis sessions alongside the re-exported full word JSON for each affected registry. It is not a replacement for the Session B instructions — it is supplementary analytical context that enriches how the analyst approaches those terms.

When Session B begins for a registry that has Session B flags, Claude AI must load the flags document alongside the standard Session B instructions and explicitly acknowledge each flag at the start of analysis for the affected term.

**⚠ Session B flags must not be lost between sessions.** The patch construction session should note in its handoff that Session B flags exist for specific registries. Claude Code's completion report for a registry should flag whether a sessionB-flags file exists for that session.

\---

## 7\. Patch Production

### 7.1 Patch types

|Type|Purpose|When to use|
|-|-|-|
|VERSECONTEXT|Full session — all terms classified in the session|After completing all terms in the session and passing pre-submission validation|
|VCGROUP|Targeted group update|When revising a single group description or dissolving/reinstating a group outside a full session|
|VCVERSE|Targeted verse update|When a single verse changes state (new verse added after audit\_word re-run, verse removed, reclassification needed)|

### 7.2 VERSECONTEXT patch — structure

Produced once per session after all terms in the session are complete and pre-submission validation passes. A session can cover one term or many; the patch captures whichever terms the session classified.

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-VCB{nnn}-VCNEW-V1",
    "batch_id": "VCB-{nnn}",
    "terms_covered": [142, 143, 187, 892],
    "input_versions": { "142": 1, "143": 1, "187": 2, "892": 1 },
    "governing_instruction": "wa-versecontext-instruction-v3_4-20260424.md",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "wa-versecontext-instruction-v3_4",
    "session_b_status": null,
    "description": "Verse context classification — session VCB-{nnn}, {n} terms, {n} verses"
  },
  "operations": [],
  "_patch_summary": {
    "total_operations": 0,
    "group_inserts": 0,
    "group_updates": 0,
    "verse_context_inserts": 0,
    "verse_context_updates": 0,
    "relevant_verses": 0,
    "set_aside_verses": 0,
    "anchor_verses": 0,
    "dual_context_verses": 0,
    "revisions_to_prior": 0
  }
}
```

**Required fields in `_patch_meta`:**

* `patch_id` — uppercase identifier; used as the applicator's idempotency key.
* `batch_id` — optional (A-04 ruling): the session identifier (VCB-{nnn}) is retained as a convenience field for human audit grouping but is no longer operationally required. The per-term version gate (`input_versions`) is the authoritative correlation between input `.md`s and the patch.
* **`terms_covered`** — array of integer `mti_term_id`s — **every term the patch operates on** (VCNEW/VCREVISE). The applicator cross-checks this against the `mti_term_id`s referenced by operations: missing term_ids (operations reference a term not declared) fail the patch; extra declared ids are accepted. The applicator uses `terms_covered` to know which terms to flip to `vc_status = 'vc_completed'` after the patch applies.
* **`input_versions` (A-03 version gate — required for VCNEW and VCREVISE)** — a map of `{mti_term_id: md_version}` carrying the `md_version` stamped in the per-term `.md` header the classifier worked from. The applicator compares each declared version to the current `mti_terms.md_version` in the DB; **any mismatch rejects the whole patch as stale** (the DB state changed since the `.md` was rendered). On successful apply, the applicator **bumps** `md_version` for every term in `terms_covered` — any pre-existing `.md` is now stale for the next session on that term. Keys may be JSON numbers or strings; the applicator normalises. VCSBFLAGS and VCSDPOINTERS do not require `input_versions` (they touch only `wa_session_research_flags` and do not change classification state).
* `governing_instruction` — filename of the VC instruction version under which the session classified. The applicator writes this to `mti_terms.vc_instruction_version` on apply.
* `session_b_status` — always `null` for VC patches; applicator must not reject.

**`_patch_summary` field definitions:**

* `dual_context_verses` — count of *verses* (not verse_context rows) that appear in more than one group for the same term. A verse assigned to two groups contributes 1 to this count regardless of how many verse_context rows it generates.

### 7.3 Operation types

#### Insert new group

```json
{
  "op\_id": "OP-001",
  "operation": "insert",
  "table": "verse\_context\_group",
  "record": {
    "mti\_term\_id": 142,
    "group\_code": "142-001",
    "context\_description": "{brief phrase — inner-being engagement}",
    "notes": null,
    "delete\_flagged": 0
  },
  "description": "New group for {strongs\_number}: {context\_description}"
}
```

**Claude Code:** after inserting, capture `last\_insert\_rowid()` as the integer id for this group. Use this integer in all subsequent verse\_context inserts that reference this group in the same patch.

#### Update existing group

```json
{
  "op\_id": "OP-002",
  "operation": "update",
  "table": "verse\_context\_group",
  "match": { "id": 47 },
  "set": {
    "context\_description": "{revised phrase}",
    "notes": "{reason for revision}",
    "delete\_flagged": 0
  },
  "description": "Revised context description for group {group\_code}: {reason}"
}
```

Only fields being changed appear in `set`. `delete\_flagged = 1` dissolves a group. When dissolving: check that affected anchor verses are reassigned or that the term retains at least one anchor from another group — include those operations in the same patch.

#### Insert new verse\_context record — anchor

```json
{
  "op\_id": "OP-003",
  "operation": "insert",
  "table": "verse\_context",
  "record": {
    "verse\_record\_id": 4821,
    "mti\_term\_id": 142,
    "group\_id": "142-001",
    "is\_anchor": 1,
    "is\_relevant": 1,
    "is\_related": 0,
    "notes": null,
    "delete\_flagged": 0
  },
  "description": "{Book Ch:V} — anchor, group 142-001: {context\_description}"
}
```

#### Insert new verse\_context record — related

```json
{
  "op\_id": "OP-004",
  "operation": "insert",
  "table": "verse\_context",
  "record": {
    "verse\_record\_id": 4822,
    "mti\_term\_id": 142,
    "group\_id": "142-001",
    "is\_anchor": 0,
    "is\_relevant": 1,
    "is\_related": 1,
    "notes": null,
    "delete\_flagged": 0
  },
  "description": "{Book Ch:V} — related, group 142-001"
}
```

#### Insert new verse\_context record — set aside

```json
{
  "op\_id": "OP-005",
  "operation": "insert",
  "table": "verse\_context",
  "record": {
    "verse\_record\_id": 4823,
    "mti\_term\_id": 142,
    "group\_id": null,
    "is\_anchor": 0,
    "is\_relevant": 0,
    "is\_related": 0,
    "set\_aside\_reason": "{no\_inner\_being | physical\_only | spatial\_only | wrong\_face | other}",
    "notes": null,
    "delete\_flagged": 0
  },
  "description": "{Book Ch:V} — set aside ({set\_aside\_reason}), no inner-being engagement for {strongs\_number}"
}
```

**`set\_aside\_reason` is required** for every set-aside record from VCB-032 onward. Use the controlled vocabulary from Section 2.2. For `wrong\_face`, populate the `notes` field with the term and registry carrying the inner-being content where known: e.g. `"wrong\_face: inner-being content carried by lev (H3820A, Reg 183)"`. For `other`, the `notes` field must explain the reason. `NULL` is not acceptable from VCB-032 onward.

```

#### Update existing verse\_context record

```json
{
  "op\_id": "OP-006",
  "operation": "update",
  "table": "verse\_context",
  "match": { "id": 892 },
  "set": {
    "group\_id": 47,
    "is\_anchor": 1,
    "is\_relevant": 1,
    "is\_related": 0,
    "notes": "{reason for revision}",
    "delete\_flagged": 0
  },
  "description": "{Book Ch:V} — reclassified: promoted to anchor, group {group\_code}"
}
```

**All corrections are UPDATE operations. Never delete and reinsert.** Use `delete\_flagged = 1` to flag a record out of the active set without physical deletion.

**Note on group\_id references:** In operations within the same patch, `group\_id` may be a group\_code string (e.g. `"142-001"`) for groups being inserted in the same patch. Claude Code resolves these to the captured integer id at apply time. For existing groups from prior patches, use the integer id directly.

### 7.4 Operation ordering within patch

For each term, order operations as follows:

1. All `verse\_context\_group` inserts for the term (new groups — so integer ids are available for subsequent rows)
2. All `verse\_context\_group` updates (revisions to existing groups)
3. All `verse\_context` inserts — anchors first, then related, then set-aside
4. All `verse\_context` updates (revisions to prior classifications)

Across terms: process terms in the order the session composition specifies — the order in which the per-term Session A `.md` inputs were introduced to the session by the researcher.

### 7.5 Decision context requirement — researcher decisions during patch construction

When Claude AI identifies an issue during patch construction that requires a researcher decision (anchor missing, group dissolution, cross-term assignment, ambiguous reference, or any other unresolvable condition), it must present the decision with the following elements. A bare option list is not acceptable.

**Required elements for every researcher decision:**

1. **The affected term and group** — Strong's number, transliteration, gloss, mti\_id, group code, and group description.
2. **The specific issue** — what was found and why it cannot be resolved automatically.
3. **Full verse text for every verse under consideration** — not just references. The researcher cannot make a sound judgement from references alone.
4. **What each option means for the patch** — spell out the concrete consequence of each choice: which verses will be classified, which will be set aside, whether a group will exist in the database.
5. **Claude AI's own assessment** — state which option is analytically stronger, and why, grounded in the verse texts and the group description. Claude AI must not present options as equally weighted when one is clearly more consistent with the programme's classification criteria. Label this explicitly: *"Claude AI assessment: \[option] is stronger because \[reason]."*

**Rationale:** During VCB-006 patch construction, 10 decisions were presented to the researcher as option lists with minimal verse context. The researcher noted that in 90% of cases the decision required a judgement call without sufficient information. This instruction corrects that discipline. The researcher's role is to make an informed decision, not to guess.

**Format template:**

```
Decision D-NNN | mti\_id={n} | {strongs} ({transliteration}) — {gloss}
Group {code}: {description}

Issue: {what was found and why it cannot be auto-resolved}

Verses under consideration:
  {ref} vid={n}: "{full verse text}"
  {ref} vid={n}: "{full verse text}"
  \[repeat for all relevant verses]

Options:
  A. {description of option A} — patch consequence: {what happens}
  B. {description of option B} — patch consequence: {what happens}

Claude AI assessment: Option {A/B} is analytically stronger because {reason grounded in verse text and group description}.

→ Your decision:
```

### 7.6 Anchor integrity rule

Any operation that removes, dissolves, or reclassifies the last anchor for a term must be accompanied in the same patch by a promotion operation ensuring the term retains at least one active anchor. This rule is absolute. Claude AI is responsible for ensuring it. Claude Code validates after application.

### 7.7 Pre-submission validation

Before submitting any patch, verify (per-patch rules that apply to VCNEW + VCREVISE or to the legacy VERSECONTEXT):

* Every verse in the session has exactly one verse_context row, except dual-context verses (exactly two)
* Every new group has at least one anchor insert in this patch or an existing anchor in the database
* Every is_related = 1 row references a group that has an anchor (in this patch or existing)
* Every is_relevant = 0 row has group_id = null
* No row has is_anchor = 1 and is_related = 1 simultaneously
* **Orphan-group validation** — for every pre-existing active `verse_context_group` for every term in the session's input, either (a) at least one `verse_context` operation in this session's VCNEW or VCREVISE patch leaves the group with ≥ 1 active verse (`is_relevant = 1`, `delete_flagged = 0`), or (b) a VCREVISE `update` operation on the group sets `delete_flagged = 1`. A pre-existing active group reaching zero active verses with no dissolve operation is a validation failure. See §6.2 Step 6 orphan-group check.
* `_patch_summary` counts match the actual operation counts

**v3_3 addition — session-level cross-patch consistency:** Under the four-patch model (§7.9), the session's observations file must reconcile with the session's patch set:

1. **Obslog-to-patch SB consistency** — every deferred flag in the obslog tagged `session_target = 'Session B'` must have a corresponding `insert` on `wa_session_research_flags` in the session's **VCSBFLAGS** patch. An obslog SB flag with no corresponding operation is a validation failure.
2. **Obslog-to-patch SD consistency** — every deferred flag tagged `session_target = 'Session D'` must have a corresponding operation in the session's **VCSDPOINTERS** patch. Same failure rule.
3. **Four-patch batch_id consistency** — every patch of the session carries the same `_patch_meta.batch_id` (the VCB-{nnn} session id).
4. **Terms-covered union** — the union of `terms_covered` across VCNEW and VCREVISE must equal the set of terms the session classified (per the session log's per-term table).

**Programmatic validation — required for large sessions (>1500 verses or >50 terms):** When the patch is produced in a deferred patch construction session (see Section 6.4), validation must be performed programmatically against the input document before the patch file is written. Specifically:

1. **Anchor reference verification** — every anchor reference in the classification data must be resolved to an actual verse_record_id in the term's verse set. References that do not resolve must be corrected before operations are generated. Silent failure (generating a patch with unresolved anchors) is not acceptable.
2. **Duplicate key check** — verify no (verse_record_id, mti_term_id, group_id) combination appears more than once. This catches the case where a verse appears in both the anchor and related lists for the same group.
3. **Coverage check** — every verse_record_id in the input for every term must appear in exactly one verse_context insert (or two for dual-context verses). No verse may be missed.
4. **R1–R4 pre-check** — apply the consistency rules (Section 11.3) to the proposed operations before writing the file, not only after application.
5. **Orphan-group programmatic check** — compute, for each pre-existing active group on every term in the input, the net active-verse count after the proposed patch operations are applied. Flag any group reaching zero with no dissolve operation. This catches §6.2 Step 6 orphan-group discipline failures before the patch leaves the construction session.
6. **Four-patch set integrity** — if VCNEW, VCREVISE, VCSBFLAGS, or VCSDPOINTERS is missing despite the obslog indicating its output class was produced, raise a validation failure before any patch writes.

### 7.8 Handoff to Claude Code

```text
PATCH SUBMISSION TO CLAUDE CODE

Patch file: wa-vcb-{batch_id}-patch-{date}.json
Patch type: VERSECONTEXT

Action required (per v3_1 per-term model — scripts/apply_session_patch.py VC-2 extension):
  1. Apply patch — insert/update verse_context_group and verse_context records
     (all operations run in a single SQLite transaction; failure rolls back).
  2. Resolve group_code strings to integer ids for new groups in this patch.
  3. Validate consistency rules R1–R4 after application, per term.
  4. Run integrity validation including orphan-group validation (§7.7 bullet).
  5. For each mti_term_id in _patch_meta.terms_covered, where the term's
     operations passed R1–R4 + orphan-group + coverage checks:
       UPDATE mti_terms
          SET vc_status = 'complete',
              vc_instruction_version = {governing_instruction},
              vc_status_updated_at = {now()},
              vc_status_note = NULL
        WHERE id = {mti_term_id};
  6. Derive affected registries:
       - OWNER path: SELECT DISTINCT owning_registry_fk FROM mti_terms
                     WHERE id IN ({terms_covered}).
       - XREF path:  registries that reference any covered term's strongs_number
                     via wa_term_inventory.term_owner_type = 'XREF'.
  7. For each affected registry, run the derived completion aggregation:
       - All active OWNER terms (with verses) at vc_status = 'vc_completed'?
       - All XREF terms' OWNER at vc_status = 'vc_completed'?
     If both, UPDATE word_registry SET verse_context_status = 'Complete' and trigger
     the Session A .md re-render (per-term files for any terms whose data changed;
     per-registry hybrid view on demand).
  8. Report: terms marked complete, registries advanced to Complete, any term-level
     validation failures, orphan-group dispositions applied.
```

\---

### 7.9 Session output — the four-patch model

A VC session produces up to **four independently-applied patches**, one per output class. All four carry the same `batch_id` (VCB-{nnn} — the session id), so the four trace to one session. Each is applied in its own transaction; a failure in one does not roll back others from the same session. A session may produce fewer than four — empty classes produce no patch. This model formalises the four output types a VC session generates as the classifier reads the verses.

**Authoritative structural reference:** `wa-patch-instruction` [current] §15. That section documents the patch structure, required `_patch_meta` fields, supported operations, applicator behaviour, example `_patch_summary`, and self-check rules per type. This section describes the **workflow** — what each patch is for and how the classifier produces it.

#### 7.9.1 The four output classes

| Patch | Output class | Produced when | Tables written |
|---|---|---|---|
| **VCNEW** | (b) New VC data — first-time classifications | Any term in the session is being classified for the first time (inserts on `verse_context_group` or `verse_context`) | `verse_context_group` + `verse_context` (inserts) |
| **VCREVISE** | (a) Changes to existing VC data | Any revision is made to existing classifications — group description edits, dissolves, verse reassignments, anchor promotions/demotions | `verse_context_group` + `verse_context` (updates, including `delete_flagged = 1`) |
| **VCSBFLAGS** | (c) Session B observations raised while reading | The classifier notices an analytical signal that should be examined at Session B | `wa_session_research_flags` (inserts, `session_target = 'Session B'`) |
| **VCSDPOINTERS** | (d) Session D cross-registry pointers | The classifier notices a signal connecting this term or verse to another term or registry | `wa_session_research_flags` (inserts, `session_target = 'Session D'`, `cross_registry_id` populated) |

#### 7.9.2 Apply order

`VCNEW` → `VCREVISE` → `VCSBFLAGS` → `VCSDPOINTERS`.

Reason: VCNEW may insert groups that VCREVISE references (by integer id post-resolution). Flag patches are independent of the classification patches and independent of each other, but the SB-before-SD convention is kept for reading consistency.

#### 7.9.3 Producing each patch during the session

The session's **observations file** is the working paper where all four patches accumulate. As the classifier proceeds term by term through §6.2 Steps 1–6:

- **New classifications** (insert operations) accumulate as Classification blocks in the observations file. These become the VCNEW patch.
- **Revisions** to prior classifications (update operations) are recorded alongside, marked as revisions with the rationale. These become the VCREVISE patch.
- **Session B observations** the classifier notices while reading — e.g. a verse that reveals a previously-unidentified inner-being connection, a theological question worth examining, a cross-reference worth enriching Session B with — are recorded as DF-{nnn} flag entries with `session_target = 'Session B'`. These become the VCSBFLAGS patch.
- **Cross-registry / cross-term signals** — e.g. Col 1:9's use of a term that parallels a term in another registry, a thematic link that's analytically material — are recorded as DF-{nnn} flag entries with `session_target = 'Session D'` and `cross_registry_id` specified. These become the VCSDPOINTERS patch.

At the end of the session (§6.3 Steps 1–3), the classifier partitions the observations file into the four patches and produces each as a separate JSON file. Any patch whose operation list would be empty is not produced.

#### 7.9.4 Output file names (per patch instruction [current] §3.6 and §15)

```text
data/imports/WA/Patches/
├── wa-vcb-{batch_id}-patch-vcnew-v1-{date}.json
├── wa-vcb-{batch_id}-patch-vcrevise-v1-{date}.json
├── wa-vcb-{batch_id}-patch-vcsbflags-v1-{date}.json
└── wa-vcb-{batch_id}-patch-vcsdpointers-v1-{date}.json
```

(The legacy combined `wa-vcb-{batch_id}-patch-versecontext-v1-{date}.json` is retained for backwards compatibility with pre-v3_3 sessions; new v3_3 sessions do not produce it.)

#### 7.9.5 Applicator behaviour — what happens on apply

Per `scripts/apply_session_patch.py`:

- **VCNEW**: applies operations → validates per-term R1–R4 + orphan-group + coverage for every `mti_term_id` in `terms_covered` → writes `mti_terms.vc_status = 'complete'` + `vc_instruction_version` + `vc_status_updated_at` → derives affected registries and runs the aggregate check (§13).
- **VCREVISE**: applies operations → validates per-term invariants → bumps `vc_status_updated_at` for every term in `terms_covered`; does not downgrade `vc_status`. The aggregate check re-runs.
- **VCSBFLAGS**: applies `wa_session_research_flags` inserts → no `vc_status` change → no registry aggregation.
- **VCSDPOINTERS**: same as VCSBFLAGS.

**A-01 resolution (v3_3):** the DataPrep gate is `word_registry.verse_context_status = 'Complete'`, written by the VC-2 handler's aggregate check when VCNEW or VCREVISE applies. The full-word JSON re-export is an optional audit artefact — the DB state is the gate. DataPrep reads the DB, not a file.

#### 7.9.6 What replaces the `sessionb-flags.md` file

Pre-v3_3, Session B observations raised during VC were captured only in the end-of-session `wa-vcb-{batch_id}-sessionb-flags-v{n}-{date}.md` file — a file-only artefact that Session B had to load separately.

Under v3_3, **the authoritative record is the VCSBFLAGS patch's DB rows in `wa_session_research_flags`**. The `.md` file becomes a companion **readable summary** of those rows, produced alongside the patch for human review. It is not the authoritative record; the DB is. Session B loads its input set by querying:

```sql
SELECT * FROM wa_session_research_flags
WHERE session_target = 'Session B'
  AND registry_id = {N}
  AND resolved = 0
ORDER BY raised_date;
```

#### 7.9.7 Self-check (pre-submission, per §7.7 + patch instruction [current] §15.6)

The classifier's end-of-session check must verify, for the session's four patches:

1. Every deferred flag in the obslog with `session_target = 'Session B'` has a corresponding operation in VCSBFLAGS.
2. Every deferred flag in the obslog with `session_target = 'Session D'` has a corresponding operation in VCSDPOINTERS.
3. Every orphan-group disposition noted in §6.2 Step 6 is reflected in VCREVISE (as a dissolve update) — or documented as retained with rationale.
4. `_patch_meta.batch_id` is identical across the four patches (proving they belong to one session).
5. `_patch_meta.terms_covered` is present on VCNEW and VCREVISE; the union matches the terms the session classified.

No observation is left without a corresponding operation. The obslog and the patch set must be consistent.

\---

## 8\. VCGROUP Patch — Targeted Group Update

Use when revising a single `verse\_context\_group` record outside a full classification session — for example, when a context\_description needs refinement after researcher review, or when a group is dissolved because its verses belong better in another group.

### 8.1 Input required from Claude Code

Before producing a VCGROUP patch, Claude Code must provide:

```json
{
  "group": {
    "id": 0,
    "mti\_term\_id": 0,
    "strongs\_number": "{H/Gnnnn}",
    "group\_code": "{text}",
    "context\_description": "{current text}",
    "notes": null,
    "delete\_flagged": 0,
    "anchor\_count": 0,
    "related\_count": 0,
    "anchor\_verses": \[
      {
        "verse\_record\_id": 0,
        "reference": "{Book Ch:V}",
        "verse\_text": "{text}"
      }
    ]
  }
}
```

**Source tables for VCGROUP input:**

|Field|Source|
|-|-|
|group.id|verse\_context\_group.id|
|group.mti\_term\_id|verse\_context\_group.mti\_term\_id|
|group.strongs\_number|mti\_terms.strongs\_number (JOIN via verse\_context\_group.mti\_term\_id → mti\_terms.id)|
|group.group\_code|verse\_context\_group.group\_code|
|group.context\_description|verse\_context\_group.context\_description|
|group.notes|verse\_context\_group.notes|
|group.delete\_flagged|verse\_context\_group.delete\_flagged|
|group.anchor\_count|COUNT(verse\_context WHERE group\_id = vcg.id AND is\_anchor = 1 AND delete\_flagged = 0)|
|group.related\_count|COUNT(verse\_context WHERE group\_id = vcg.id AND is\_related = 1 AND delete\_flagged = 0)|
|group.anchor\_verses|verse\_context (WHERE group\_id = vcg.id AND is\_anchor = 1 AND delete\_flagged = 0) → wa\_verse\_records (verse\_record\_id, reference, verse\_text)|

### 8.2 Patch structure

```json
{
  "\_patch\_meta": {
    "patch\_id": "PATCH-{YYYYMMDD}-VCGROUP{group\_id}-V1",
    "group\_id": 0,
    "produced\_date": "{yyyy-mm-dd}",
    "produced\_by": "{governing\_instruction — e.g. wa-versecontext-instruction-v3\_2-20260424.md}",
    "session\_b\_status": null,
    "description": "Targeted group update — group {group\_code}: {reason}"
  },
  "operations": \[
    {
      "op\_id": "OP-001",
      "operation": "update",
      "table": "verse\_context\_group",
      "match": { "id": 0 },
      "set": {
        "context\_description": "{revised text}",
        "notes": "{reason if applicable}",
        "delete\_flagged": 0
      },
      "description": "Revised group {group\_code}: {reason}"
    }
  ],
  "\_patch\_summary": {
    "total\_operations": 1,
    "group\_updates": 1
  }
}
```

**Reinstatement note:** If `delete\_flagged` is reset from 1 to 0 (reinstating a dissolved group), the verse\_context rows that were flagged when the group was dissolved are NOT automatically reinstated. A separate VERSECONTEXT or VCVERSE patch is required to reinstate those verses.

\---

## 9\. VCVERSE Patch — Targeted Verse Update

Use when a single verse changes state: a new verse was added after audit\_word re-run, a verse was removed, or a reclassification is needed outside a full classification session.

### 9.1 Input required from Claude Code

```json
{
  "verse": {
    "verse\_record\_id": 0,
    "reference": "{Book Ch:V}",
    "verse\_text": "{current text}",
    "target\_word": "{text}",
    "span\_strong\_match": 1,
    "verse\_delete\_flagged": 0,
    "mti\_term\_id": 0
  },
  "existing\_verse\_context": {
    "id": 0,
    "group\_id": 0,
    "group\_code": "{text}",
    "is\_anchor": 0,
    "is\_relevant": 0,
    "is\_related": 0,
    "notes": null,
    "delete\_flagged": 0
  },
  "available\_groups": \[
    {
      "id": 0,
      "group\_code": "{text}",
      "context\_description": "{text}",
      "anchor\_count": 0,
      "delete\_flagged": 0
    }
  ]
}
```

`existing\_verse\_context` is null if no record exists yet.

**Source tables for VCVERSE input:**

|Field|Source|
|-|-|
|verse.verse\_record\_id|wa\_verse\_records.id|
|verse.reference|wa\_verse\_records.reference|
|verse.verse\_text|wa\_verse\_records.verse\_text|
|verse.target\_word|wa\_verse\_records.target\_word|
|verse.span\_strong\_match|wa\_verse\_records.span\_strong\_match|
|verse.verse\_delete\_flagged|wa\_verse\_records.delete\_flagged|
|verse.mti\_term\_id|wa\_verse\_records.mti\_term\_id|
|existing\_verse\_context|verse\_context WHERE verse\_record\_id = vr.id AND mti\_term\_id = {mti\_term\_id} (NULL object if no row exists)|
|existing\_verse\_context.group\_code|verse\_context\_group.group\_code (JOIN via verse\_context.group\_id → verse\_context\_group.id)|
|available\_groups|verse\_context\_group WHERE mti\_term\_id = {mti\_term\_id} AND delete\_flagged = 0|

### 9.2 Three scenarios

**Scenario A — New verse, first-time classification:**
Use `insert` operation. Assign to an existing group if it fits; insert new group first if needed.

**Scenario B — Verse removed (`wa\_verse\_records.delete\_flagged` set to 1):**

```json
{
  "op\_id": "OP-001",
  "operation": "update",
  "table": "verse\_context",
  "match": { "id": 0 },
  "set": { "delete\_flagged": 1 },
  "description": "{Book Ch:V} — verse removed from active set, flagging verse\_context record"
}
```

If the verse was an anchor: include a second operation promoting another related verse in the same group to anchor status. If no related verses remain active in the group, include a note flagging that the group has no anchor — researcher decision required before Session B proceeds.

**Scenario C — Reclassify existing verse:**
Use `update` operation on the existing verse\_context id. Include notes explaining the reason for reclassification. Maintain anchor integrity.

### 9.3 Patch naming

`PATCH-{YYYYMMDD}-VCVERSE{verse\_record\_id}-V1`

\---

## 10\. Researcher Compliance Rules

|**⚠ Do not make assumptions or guesses. When uncertain about whether a verse passes the relevance filter, retain the verse, note the uncertainty, and proceed. Do not stop the session for borderline filter decisions — accumulate uncertainty questions at the end of each term's classification and present them together.**|
|-|

Additional rules:

* Do not develop analytical conclusions about terms during Verse Context — that is Session B
* Do not draw cross-registry connections during Verse Context — that is Session D
* Do not assign evidential status — that is Session B DataPrep and Analysis
* Context descriptions must be grounded in what the verses show — not in prior theological knowledge about the term
* Dual-context is rare — only when two distinct inner-being engagements are plainly evident. Do not use it to resolve interpretive difficulty
* All corrections are UPDATE operations — never produce delete + reinsert
* The anchor integrity rule is absolute — a term must retain at least one active anchor at all times

\---

## 11\. Claude Code — Patch Application Protocol

### 11.1 Apply in single transaction

All operations in a VERSECONTEXT patch apply as one transaction — all or nothing.

### 11.2 Group\_code resolution

For each `verse\_context\_group` insert: after the insert executes, capture `last\_insert\_rowid()`. Store this mapping: `group\_code → integer id`. Apply this mapping to all subsequent `verse\_context` inserts in the same patch that reference this group\_code as their group\_id value.

### 11.3 Consistency rule validation

Run after every patch application:

```sql
-- R1: set-aside rows clean
SELECT COUNT(\*) FROM verse\_context
WHERE is\_relevant=0 AND (group\_id IS NOT NULL OR is\_anchor=1 OR is\_related=1);
-- Expected: 0

-- R2: anchor rows clean
SELECT COUNT(\*) FROM verse\_context
WHERE is\_anchor=1 AND (is\_relevant=0 OR is\_related=1 OR group\_id IS NULL);
-- Expected: 0

-- R3: related rows have an active anchor in their group
SELECT COUNT(\*) FROM verse\_context vc
WHERE is\_related=1 AND NOT EXISTS (
  SELECT 1 FROM verse\_context a
  WHERE a.group\_id=vc.group\_id AND a.is\_anchor=1 AND a.delete\_flagged=0);
-- Expected: 0
```

Any violation: report to researcher. Do not advance registry status until violations resolved.

### 11.4 Anchor integrity check

After any patch affecting anchor status, for each affected term:

```sql
SELECT COUNT(\*) as active\_anchors FROM verse\_context
WHERE mti\_term\_id = {mti\_term\_id} AND is\_anchor = 1 AND delete\_flagged = 0;
-- If 0: flag to researcher — term has no anchor and cannot proceed to Session B
```

### 11.5 Re-extraction trigger and reset requirement

**Pre-extraction REPAIR patch required:** Before any audit\_word re-run for a registry, a REPAIR patch must be applied to reset the registry state. This patch must be applied and confirmed before audit\_word runs. No re-extraction may proceed without it.

The REPAIR patch resets:

* `word\_registry.session\_b\_status` → `Verse Context Reset`
* `word\_registry.verse\_context\_status` → `In Progress`
* All `verse\_context` records for this registry's OWNER terms → `delete\_flagged = 1`
* All `verse\_context\_group` records for this registry's OWNER terms → `delete\_flagged = 1`
* All Session B analytical outputs (wa\_session\_b\_dimensions, wa\_session\_b\_findings, wa\_session\_research\_flags SD\_POINTER records, wa\_term\_inventory.evidential\_status) for this registry → cleared

The REPAIR patch naming convention: `PATCH-{YYYYMMDD}-{nnn}-REPAIR-AUDITWORD-RERUN-V1`
Full patch specification: WA-PipelineStatusReview-v2-20260330 Section 3.2.

**Claude Code expectation — audit\_word routine:** Claude Code must build the following into the audit\_word re-run routine. When audit\_word detects it is re-running for a registry that already has data (i.e. wa\_term\_inventory records exist for this registry), the routine must:

1. Verify the REPAIR patch has been applied (check patch history for REPAIR-AUDITWORD-RERUN on this registry). If not applied: halt with error — do not proceed.
2. On re-run, the STALE\_TERM mechanism (Step A6) handles wa\_term\_inventory updates — it compares the incoming JSON against existing records and applies only the delta. This is the authoritative mechanism for updating term inventory on re-run. No separate delete/re-insert of wa\_term\_inventory records is required.
3. After audit\_word completes, re-export the full word JSON (Step A11). The re-export confirms the updated state for the next pipeline stage (Verse Context).

**Post-audit\_word detection (existing check retained):**

After every audit\_word re-run, check for OWNER terms with verse records that have no corresponding verse\_context entry:

```sql
SELECT DISTINCT mt.id, mt.strongs\_number, mt.owning\_registry\_fk
FROM wa\_verse\_records vr
JOIN wa\_term\_inventory ti ON ti.id = vr.term\_inv\_id
JOIN mti\_terms mt ON mt.id = vr.mti\_term\_id
WHERE ti.term\_owner\_type = 'OWNER' AND vr.delete\_flagged = 0
  AND NOT EXISTS (
    SELECT 1 FROM verse\_context vc
    WHERE vc.verse\_record\_id = vr.id AND vc.mti\_term\_id = mt.id
  );
```

For each term returned: set owning registry `verse\_context\_status = 'In Progress'`. Report to researcher.

Cascade delete\_flag from verse records to verse\_context when a verse is flagged:

```sql
UPDATE verse\_context SET delete\_flagged = 1
WHERE verse\_record\_id IN (SELECT id FROM wa\_verse\_records WHERE delete\_flagged = 1)
  AND delete\_flagged = 0;
```

**Claude Code expectation — Verse Context input preparation after a reset:** When Claude Code prepares per-term Session A `.md` inputs for a registry that previously had verse_context records and has since been reset, the preparation routine must:

1. Confirm that all verse_context and verse_context_group records for this registry's OWNER terms are delete_flagged (the REPAIR patch should have done this — verify before rendering the input).
2. Render the input reflecting only active (delete_flagged = 0) verse_context_group rows — which after the reset will be empty. Dissolved groups may still be shown to the classifier (they inform the re-run) but are labelled as dissolved. The `.md` will consequently state **FRESH** prior-state posture for this registry per §6.1.
3. Re-assess the wa_term_inventory records for this registry: confirm that mti_terms.status values are still appropriate (extracted/extracted_thin) after the audit_word re-run. If any terms now have NULL status (new terms added by the re-run), flag these to researcher for DataPrep re-classification before Verse Context proceeds.

\---

## 12\. Claude Code — Integrity Validation

Run after every patch application cycle:

```sql
-- Terms with delete/excluded status should have no active verse\_context rows
SELECT mt.strongs\_number, mt.status, COUNT(vc.id) as active\_vc\_rows
FROM mti\_terms mt
JOIN verse\_context vc ON vc.mti\_term\_id = mt.id
WHERE mt.status IN ('delete','excluded') AND vc.delete\_flagged = 0
GROUP BY mt.id;
-- Expected: zero rows. Any result is an integrity violation — report to researcher.
```

\---

## 13\. Claude Code — Registry Completion Check (derived from term states)

Run after every VERSECONTEXT patch, for each registry affected by the patch (OWNER path + XREF-consumer path). Under v3_1 the check reads from `mti_terms.vc_status` — no longer a scan of `verse_context` rows.

### 13.1 OWNER term completion — aggregated from term states

```sql
-- Count OWNER terms (with verses) NOT at complete/approved for this registry.
SELECT COUNT(DISTINCT mt.id) AS owner_terms_incomplete
FROM mti_terms mt
JOIN word_registry wr ON wr.id = mt.owning_registry_fk
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
     AND ti.term_owner_type = 'OWNER'
     AND ti.delete_flagged = 0
     AND ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = wr.id)
WHERE wr.no = {registry_no}
  AND mt.delete_flagged = 0
  AND mt.status IN ('extracted', 'extracted_thin')
  AND EXISTS (SELECT 1 FROM wa_verse_records vr
               WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0)
  AND mt.vc_status != 'vc_completed';
-- If 0: all OWNER terms are at complete or approved.
```

### 13.2 XREF coverage — aggregated from OWNER term states

```sql
-- Count XREF terms in this registry whose OWNER is NOT at complete/approved.
SELECT COUNT(DISTINCT mt.id) AS xref_owners_incomplete
FROM wa_term_inventory ti
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
WHERE wr.no = {registry_no}
  AND ti.term_owner_type = 'XREF'
  AND ti.delete_flagged = 0
  AND mt.vc_status != 'vc_completed';
-- If 0: every XREF term's OWNER is classified.
```

Both queries are performed by `scripts/apply_session_patch.py` inside the VERSECONTEXT patch transaction via the VC-2 extension. The applicator derives the registries to check from the patch's `_patch_meta.terms_covered` (OWNER path + XREF-consumer path); operators do not need to loop manually.

### 13.3 Advancing status

When both counts are zero for a registry:

```sql
UPDATE word_registry SET verse_context_status = 'Complete' WHERE no = {registry_no};
```

The applicator logs each advancement in its final summary (`registries_advanced_to_complete` counter).

**A-01 resolution (v3_3 — authoritative):** The **DataPrep gate is the DB state** `word_registry.verse_context_status = 'Complete'`. DataPrep reads the DB — not a file. Once the applicator writes the status to Complete, the gate is open. No file re-export is required to open the gate.

**The full-word JSON re-export** (previously "the trigger") is now **optional audit artefact** only. Researchers may still produce it for human review, diff, or offline analysis, but it is not in the critical path:

```bash
# Optional — audit artefact, not a gating step
python -m engine.engine --export-word --registry={registry_no}
```

The per-term Session A `.md`s are similarly researcher-discretionary re-renders — they regenerate the same data from the canonical DB state; the state is already written by the applicator.

**Double-check verification (G06-F):** Before committing the status write, run both §13.1 and §13.2 in the same transaction. The VC-2 applicator does this by computation (the `owner_incomplete` and `xref_incomplete` values must be 0 before the UPDATE fires). If either is non-zero the UPDATE is not executed and no status flip occurs — the registry remains at its current status until subsequent patches bring the remaining terms to complete.

**Note on session_b_status:** This process does not update `session_b_status`. The value `Ready for Analysis` in the session_b_status vocabulary is set by `audit_word` (using COALESCE — only when current status is NULL), not by any Verse Context operation. The DataPrep gate check (wa-sessionb-analysis-readiness [current] Section 4.1) gates on `verse_context_status = Complete` — it does not require `session_b_status = Ready for Analysis`. No session_b_status write is needed here.

### 13.4 Completion report to researcher

For each registry reaching Complete, report:

```
Registry {nnn} — {word}:
  OWNER terms classified: {n} / {total}
  XREF terms covered: {n} (via OWNER classifications in registries: {list})
  verse\_context\_status: Complete
  Re-export: wa-{nnn}-{word}-extract-{date}.json produced
  Ready for: Session B DataPrep
```

For each registry that remains incomplete after this session (i.e. has OWNER terms the session did not classify), report:

```text
Registry {nnn} — {word}:
  OWNER terms classified this session: {n}
  OWNER terms remaining: {n} (to be classified in future sessions at researcher discretion)
  verse_context_status: In Progress — continuation expected
```

After all per-registry reports for this session, produce a session-level summary:

```text
SESSION {batch_id} COMPLETION SUMMARY

Registries affected by this session: {n}
  Reached Complete this session: {n} — {list: nnn—word}
  Still In Progress: {n} — {list: nnn—word, reason}
    Of which: terms remaining for future session: {n}
    Of which: all-verses-fail or other pending decision: {n}

Programme-wide Stage 1 progress:
  verse_context_status = Complete: {n} / 184 registries
  verse_context_status = In Progress: {n} registries
  Unclassified OWNER terms remaining: {n}
```

\---

## 14\. Stage 1 Completion

Stage 1 is complete when all 184 active registries have `verse_context_status = Complete` (the 30 registries at `phase1_status = 'Excluded'` are outside VC scope).

### 14.1 Monitoring query

```sql
SELECT verse_context_status, COUNT(*) as count
FROM word_registry
WHERE session_b_status IS NOT NULL
GROUP BY verse_context_status;
-- Target: Complete = 184, In Progress = 0, NULL = 30 (excluded)
```

### 14.2 Stage 1 completion report

When the monitoring query shows Complete = 184, Claude Code produces the Stage 1 completion report:

```text
STAGE 1 — VERSE CONTEXT SWEEP COMPLETE

Date: {yyyy-mm-dd}
Sessions: {n} (VCB-001 through VCB-{nnn})

Summary:
  Registries classified: 184 / 184
  verse_context_group records created: {n}
  verse_context records created: {n}
    - Anchor verses: {n}
    - Related verses: {n}
    - Set aside: {n}
  OWNER terms classified: {n}
  XREF terms covered: {n}

All 184 registries are now at verse_context_status = Complete.
Per-term and per-registry Session A .md renders are available on demand.

Programme state:
  verse_context_status = Complete: 184 registries
  DataPrep gate: OPEN for all 184 registries

Stage 2 — Session B Analysis may now begin.
Processing sequence: per pool/cluster order in wa-registry-management-guide [current] Section 7.
```

### 14.3 What happens next

After Stage 1 completion, the programme moves to Stage 2 — Session B Analysis. Processing proceeds in pool/cluster order as defined in wa-registry-management-guide [current] Section 7. The governing instruction for each stage is:

|Stage|Governing instruction|
|-|-|
|Session B Analysis Readiness|wa-sessionb-analysis-readiness [current]|
|Session B Analysis Output|wa-sessionb-analysis-output [current]|
|(Session B Extraction — retired, content folded into Analysis Output)|—|

DataPrep is triggered per registry as registries reach `verse_context_status = Complete`. It does not wait for all 184 to complete — registries that complete Verse Context early can begin DataPrep immediately.

\---

## Annexure A — Startup Summary Template

```text
Verse Context v3_2 startup complete.
Session: {batch_id}
Governing instruction: wa-versecontext-instruction-v3_2-20260424.md
Programme prose extract: wa-programme-prose-extract-{YYYYMMDD}.md
  prog_instr_session_a loaded — Session A content boundary understood.
  prog_instr_verse_context loaded — VC role understood.

Terms in session: {n}
Total verses across terms: {n} | Previously classified verses: {n}

Term inventory (session composition order):
  {strongs_number} ({transliteration}) — {gloss} — {n} verses | mti_term_id={id}
    OWNER registry: {owning_word} ({owning_registry_no})
    Existing groups: {n_active} active / {n_dissolved} dissolved
    Prior-state posture for this term: {FRESH | RE-EVALUATION}
  [repeat for each term in the session]

Per-term posture declarations:
  {one FRESH or RE-EVALUATION posture block per term, verbatim per §6.1 step 4}

Notes on terms with prior classification:
  {list any terms where prior verse_context coverage is complete; whether
   revision seems warranted under re-evaluation}

Ready to proceed. Beginning with {first_strongs_number} ({transliteration})
  — the first term in the session's composition order.
```

\---

## Annexure B — Per-Term Classification Summary Template

```
Term: {strongs\_number} ({transliteration}) — {gloss}
mti\_term\_id: {integer}
OWNER for: {owning\_word} (registry {owning\_registry\_id})
Total verses: {n} | Relevant: {n} | Set aside: {n}

Groups:
  {group\_code} \[{new / existing}]: "{context\_description}"
    Anchors: {verse reference(s)}
    Related: {n} verses
    \[repeat for all groups]

Revisions to prior classifications: {n}
  {describe each: what changed and why}
Dual-context verses: {n}
  {describe each: what two engagements are present}
Borderline retained: {n}
  {list references and note uncertainty}
Anchor integrity: confirmed — {n} active anchors across {n} groups

Ready for patch.
```

\---

## Annexure C — VERSECONTEXT Patch Template

> **Note:** The authoritative structure for VERSECONTEXT patches is **§7.2** of this instruction (which includes the required `_patch_meta.terms_covered` array). This Annexure was preserved from earlier versions for continuity but is effectively superseded by §7.2; consult §7.2 for the canonical current template. Annexure D (separate) covers the deprecated legacy batch JSON input format.

File naming: `wa-vcb-{batch\_id}-patch-{YYYYMMDD}.json`

```json
{
  "\_patch\_meta": {
    "patch\_id": "PATCH-{YYYYMMDD}-VCB{nnn}-VERSECONTEXT-V1",
    "batch\_id": "VCB-{nnn}",
    "terms\_covered": \[0, 0, 0],
    "governing\_instruction": "wa-versecontext-instruction-v3\_2-20260424.md",
    "produced\_date": "{yyyy-mm-dd}",
    "produced\_by": "{governing\_instruction — e.g. wa-versecontext-instruction-v3\_2-20260424.md}",
    "session\_b\_status": null,
    "description": "Verse context classification — session VCB-{nnn}, {n} terms, {n} verses"
  },
  "operations": \[
    {
      "op\_id": "OP-001",
      "operation": "insert",
      "table": "verse\_context\_group",
      "record": {
        "mti\_term\_id": 0,
        "group\_code": "{mti\_term\_id}-001",
        "context\_description": "{brief phrase}",
        "notes": null,
        "delete\_flagged": 0
      },
      "description": "Group 1 for {strongs\_number}: {context\_description}"
    },
    {
      "op\_id": "OP-002",
      "operation": "insert",
      "table": "verse\_context",
      "record": {
        "verse\_record\_id": 0,
        "mti\_term\_id": 0,
        "group\_id": "{mti\_term\_id}-001",
        "is\_anchor": 1,
        "is\_relevant": 1,
        "is\_related": 0,
        "notes": null,
        "delete\_flagged": 0
      },
      "description": "{Book Ch:V} — anchor, group {mti\_term\_id}-001: {context\_description}"
    },
    {
      "op\_id": "OP-003",
      "operation": "insert",
      "table": "verse\_context",
      "record": {
        "verse\_record\_id": 0,
        "mti\_term\_id": 0,
        "group\_id": "{mti\_term\_id}-001",
        "is\_anchor": 0,
        "is\_relevant": 1,
        "is\_related": 1,
        "notes": null,
        "delete\_flagged": 0
      },
      "description": "{Book Ch:V} — related, group {mti\_term\_id}-001"
    },
    {
      "op\_id": "OP-004",
      "operation": "insert",
      "table": "verse\_context",
      "record": {
        "verse\_record\_id": 0,
        "mti\_term\_id": 0,
        "group\_id": null,
        "is\_anchor": 0,
        "is\_relevant": 0,
        "is\_related": 0,
        "notes": null,
        "delete\_flagged": 0
      },
      "description": "{Book Ch:V} — set aside, no inner-being engagement for {strongs\_number}"
    }
  ],
  "\_patch\_summary": {
    "total\_operations": 4,
    "group\_inserts": 1,
    "group\_updates": 0,
    "verse\_context\_inserts": 3,
    "verse\_context\_updates": 0,
    "relevant\_verses": 2,
    "set\_aside\_verses": 1,
    "anchor\_verses": 1,
    "dual\_context\_verses": 0,
    "revisions\_to\_prior": 0
  }
}
```

\---

## Annexure D — Legacy Batch JSON Schema (deprecated)

> **Status under v3_1:** **deprecated**. The per-term Session A `.md` is the primary VC input; it handles split-session cases natively (the session's term list is the split). This schema is retained for historical continuity — it documents the input format that preceded the `.md` renderer (v2_8 §5.3) and can still be read by the applicator if a legacy batch JSON is encountered. Do not produce new batch JSONs. If a situation appears that seems to require one, it is almost certainly solvable by composing a session's per-term `.md` list differently.

### C.1 Schema

```json
{
  "batch_id": "VCB-{nnn}",
  "produced_date": "{yyyy-mm-dd}",
  "produced_by": "Claude Code — WA-VerseContext-Instruction v3_0",
  "governing_instruction": "wa-versecontext-instruction-v3_0-20260424.md",
  "total_verse_count": 0,
  "total_term_count": 0,
  "unclassified_verse_count": 0,
  "verse_context_summary": {
    "total_verses_in_batch": 0,
    "previously_classified": 0,
    "unclassified": 0,
    "set_aside_in_prior_batches": 0,
    "anchor_verses_existing": 0
  },
  "terms": [
    {
      "mti_term_id": 0,
      "strongs_number": "{H/Gnnnn}",
      "transliteration": "{text}",
      "gloss": "{text}",
      "language": "{Hebrew or Greek}",
      "mti_status": "{extracted or extracted_thin}",
      "term_owner_type": "OWNER",
      "owning_registry_id": 0,
      "owning_registry_word": "{word}",
      "registry_verse_context_status": "{NULL or In Progress or Complete}",
      "term_classification_complete": false,
      "total_verses": 0,
      "unclassified_count": 0,
      "existing_groups": [
        {
          "id": 0,
          "group_code": "{mti_term_id}-{serial}",
          "context_description": "{text}",
          "notes": null,
          "delete_flagged": 0,
          "anchor_count": 0,
          "related_count": 0
        }
      ],
      "verses": [
        {
          "verse_record_id": 0,
          "reference": "{Book Ch:V}",
          "verse_text": "{full ESV text}",
          "target_word": "{the specific word form occurring in this verse}",
          "span_strong_match": 1,
          "verse_delete_flagged": 0,
          "verse_context": {
            "id": 0,
            "group_id": 0,
            "group_code": "{mti_term_id}-{serial}",
            "is_anchor": 0,
            "is_relevant": 0,
            "is_related": 0,
            "notes": null,
            "delete_flagged": 0
          }
        }
      ]
    }
  ]
}
```

### C.2 Source-table mapping

Fields are identical to those rendered in the Session A `.md`; the mapping carries for both forms.

|Field|Source|
|-|-|
|mti_term_id|mti_terms.id|
|strongs_number|mti_terms.strongs_number|
|transliteration|mti_terms.transliteration|
|gloss|mti_terms.gloss|
|language|mti_terms.language|
|mti_status|mti_terms.status|
|term_owner_type|wa_term_inventory.term_owner_type (WHERE delete_flagged = 0)|
|owning_registry_id|mti_terms.owning_registry_fk|
|owning_registry_word|word_registry.word (JOIN via mti_terms.owning_registry_fk → word_registry.id)|
|registry_verse_context_status|word_registry.verse_context_status (JOIN via owning_registry_fk)|
|total_verses|COUNT(wa_verse_records WHERE term_inv_id = ti.id AND delete_flagged = 0)|
|unclassified_count|COUNT(wa_verse_records WHERE term_inv_id = ti.id AND delete_flagged = 0 AND NOT EXISTS (SELECT 1 FROM verse_context WHERE verse_record_id = vr.id AND mti_term_id = mt.id))|
|existing_groups|verse_context_group WHERE mti_term_id = mt.id (ALL rows including delete_flagged = 1)|
|existing_groups.anchor_count|COUNT(verse_context WHERE group_id = vcg.id AND is_anchor = 1 AND delete_flagged = 0)|
|existing_groups.related_count|COUNT(verse_context WHERE group_id = vcg.id AND is_related = 1 AND delete_flagged = 0)|
|verses|wa_verse_records WHERE term_inv_id = ti.id (ALL rows including delete_flagged = 1 for revision history)|
|verses.verse_context|verse_context WHERE verse_record_id = vr.id AND mti_term_id = mt.id (NULL object if no record)|
|term_classification_complete|true if COUNT(wa_verse_records WHERE term_inv_id = ti.id AND delete_flagged = 0 AND NOT EXISTS (SELECT 1 FROM verse_context WHERE verse_record_id = vr.id AND mti_term_id = mt.id AND delete_flagged = 0)) = 0|

### C.3 Field population notes

* `verse_context` field on each verse: set to `null` as a JSON object if no verse_context record exists for this `verse_record_id` + `mti_term_id` combination. Populate all fields when a record exists, including `delete_flagged` — Claude AI needs to see the full history including dissolved records.
* `existing_groups`: include ALL groups for the term regardless of `delete_flagged` — Claude AI needs to see dissolved groups to avoid duplicating their meaning in a new group.
* `term_classification_complete`: set to `true` only if every verse for this term already has a non-flagged verse_context record. If `true`, Claude AI should review rather than re-classify from scratch.
* `verses`: include ALL verse records for the term, classified and unclassified alike — Claude AI may revise prior classifications.

### C.4 When the fallback is used

The fallback is triggered when Claude Code determines that a registry cannot be classified from a single Session A `.md` within a practical session-context budget. The trigger conditions and the split policy are the responsibility of Claude Code; the classifier sees either a `.md` or a batch JSON and treats each according to this instruction. The prior-state posture declaration in §6.1 applies to both forms; the re-evaluation self-check and orphan-group check in §6.2 Step 6 apply to both forms.

\---

*wa-versecontext-instruction-v3_4-20260424 | Supersedes wa-versecontext-instruction-v3_3-20260424 | v3_4: Resolves A-02/A-03/A-04/A-05. vc_status vocab simplified (A-02: approved dropped; complete renamed vc_completed; M38 migration). Per-term .md freshness version-gated (A-03: mti_terms.md_version column; patch's _patch_meta.input_versions required for VCNEW/VCREVISE; applicator rejects stale mismatches and bumps on apply). Session id no longer operationally required (A-04: batch_id optional; per-term version gate is the correlation). Cross-term duplicate classifications are not a VC concern (A-05: handled at Session B). Engine M38; applicator VC-2 helper widened; renderer stamps md_version into per-term .md header.*

*Historical: wa-versecontext-instruction-v3_3-20260424 | Supersedes wa-versecontext-instruction-v3_2-20260424 | v3_3: Four-patch session output model (VCNEW, VCREVISE, VCSBFLAGS, VCSDPOINTERS) formalised in new §7.9. A-01 resolved at §13.3 — DataPrep gate = DB state (`word_registry.verse_context_status = 'Complete'`); full-word JSON re-export is optional audit artefact. §6.2 Step 6 extended for SB/SD obslog routing. §6.6 restated — sessionb-flags.md is companion summary; DB rows (VCSBFLAGS patch) are authoritative. §7.7 pre-submission adds session-level obslog-to-patch consistency checks. §7.8 hand-off updated for four patches. Patch instruction [current] §15 is authoritative structural reference. Applicator (`scripts/apply_session_patch.py`) widened: VC-2 handler + terms_covered validation both cover VERSECONTEXT + VCNEW + VCREVISE; sb_exempt_types extended.*

*Historical: wa-versecontext-instruction-v3_2-20260424 | Supersedes wa-versecontext-instruction-v3_1-20260424 | v3_2: Residue cleanup — 21 stale-text items from v2_9/v3_0 fixed (§0 bullets, §0 stage diagram, §1 Claude Code role, §5 opening/triggers/criteria/output, §6.4 breakpoints + thresholds, §6.5 end-of-batch→end-of-session, §7.1/§7.4, §8.2/Annexure C produced_by, §13.4/§14 registry counts, Annexure A startup template, Annexure C/D renaming). No semantic shifts beyond v3_1's intent. v2_9 residual lint unchanged.*

*Historical: wa-versecontext-instruction-v3_1-20260424 | Supersedes wa-versecontext-instruction-v3_0-20260424 | v3_1: Per-OWNER-term as primary VC input unit (alignment analysis v4 §7 + §8). Per-term Session A `.md` replaces the per-registry `.md` as the classifier's primary input; per-term posture at §6.1; `_patch_meta.terms_covered` required at §7.2; registry completion check at §13 re-framed as derived aggregation from `mti_terms.vc_status`; Annexure D (legacy batch JSON) marked deprecated. v3_0's re-evaluation discipline and orphan-group checks are preserved unchanged.*

*Historical: wa-versecontext-instruction-v3_0-20260424 | Supersedes wa-versecontext-instruction-v2_9-20260424 | v3_0: Session A `.md`-primary input; re-evaluation discipline (prior-state posture at §6.1; per-term self-check + orphan-group check at §6.2 Step 6; orphan-group validation at §7.7); file naming consolidated on `wa-vcb-{batch_id}-...`; legacy batch JSON schema moved to Annexure C*

*Historical: wa-versecontext-instruction-v2_8-20260418 | Supersedes wa-versecontext-instruction-v2_7-20260414 | v2_8: GR-REF-002 sweep — filename current-conventions, operational cross-refs migrated to `[current]`*

*Historical: WA-VerseContext-Instruction-v2.2-20260401 | Supersedes v2.1-20260401 | v2.2: (1) Section 3.5 added: Relevance filter for grammatical and functional particles — pass criteria (directs/intensifies/qualifies scope/discloses inner orientation) and fail criteria (purely syntactic/social register/temporal connector/procedural) stated explicitly; (2) Section 6.2 Step 1: All-verses-fail rule rewritten — individual inspection is now explicitly non-waivable for all terms regardless of corpus size; researcher confirmation no longer required for full-corpus grammatical particles or confirmed homographs where individual inspection is complete*

