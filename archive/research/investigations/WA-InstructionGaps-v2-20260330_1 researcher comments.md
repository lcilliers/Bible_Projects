# WA-InstructionGaps-v2-20260330

Researcher responses is at the end of the document.

**Project:** Framework B — Soul Word Analysis Programme
**Version:** 2.0
**Date:** 2026-03-30
**Purpose:** Complete unified gap register. Every inflection point (DB read and DB write) identified from current instruction documents, assessed against four completeness criteria. Every gap from v1 carried forward with current status. Decisions made 2026-03-29 noted where instruction has not yet been updated.
**Supersedes:** WA-InstructionGaps-v1-20260329.md
**Change note v2:** Complete rebuild from instruction documents. IPs derived fresh from all governing instructions (VerseContext v1.2, DataPrep v5.4, Analysis v5.3, Extraction v5.4, ClaudeCode v3, RMG v5.5, Reference v5.3, patch_specification v1.4). All 30 gaps from v1 carried forward with updated status. New gaps added from IP analysis. Gap and IP registers unified. Cross-gap consistency verified against live documents — corrections applied to G22 (CLOSED — Section 4.3 exists), G25/IP-XP-01 (CLOSED — overwrite behaviour confirmed), G26/G15 (description corrected — bulk_update IS in spec v1.4; issue is operation should be removed from Analysis patch, not that it is undefined), G06 (clarified — Ready for Analysis set by audit_word not VerseContext).
**Produced by:** Claude AI — WA session 2026-03-30

---

## How to Read This Register

### Inflection Point Definition

An inflection point (IP) is any point in the pipeline where data moves between the pipeline and the database:
- **DB Read** — data extracted from the database to construct a JSON or inform a decision
- **DB Write** — a patch applied, status updated, or record inserted/updated in the database

### Completeness Criteria

Each IP is assessed against four criteria:
1. **Operation** — what is being done (read/write, what table, what action)
2. **Method** — how it is executed (patch operation type, SQL query, engine command)
3. **Fields and values** — which fields, what values, what derivation rules
4. **JSON structure** — where JSON is the carrier, is the structure pre-defined in the instruction

A gap exists if the instruction document as it currently stands does not contain complete and correct information for that IP. Decisions made in prior sessions that have not yet been applied to the instruction text do not close the gap — they become the recorded remediation action.

### Severity

| Code | Meaning |
|---|---|
| BLOCKING | Pipeline cannot proceed correctly without resolution |
| MISSING | Output will be incomplete or incorrect |
| AMBIGUOUS | Can proceed but action may be wrong |
| INCONSISTENT | Two documents contradict each other |

### Gap Status

| Code | Meaning |
|---|---|
| CLOSED | Fully specified in current instruction documents — no gap |
| OPEN | Gap exists in current instruction text |
| PENDING UPDATE | Researcher decision recorded in session log; instruction not yet updated — gap remains until document is corrected |

---

## Stage 1 — Verse Context

**Governing documents:** WA-VerseContext-Instruction-v1.2 | WA-SessionB-ClaudeCode-Instructions-v3 Sections 14.1–14.8

---

### IP-VC-01 — DB READ: Batch construction — identify OWNER terms and count unclassified verses

**Direction:** DB → Batch JSON
**Operation:** Claude Code reads mti_terms, wa_term_inventory, wa_verse_records, verse_context to identify eligible OWNER terms and count unclassified verses per term for batch sizing

| Criterion | State |
|---|---|
| Operation | Specified — OWNER terms only, active status, with verses, unclassified first (VerseContext v1.2 Section 5.2; CC v3 Section 14.1) |
| Method | NOT SPECIFIED — no SQL query for counting unclassified verses per term or the accumulation loop to reach the 2,000–2,500 threshold |
| Fields and values | Specified in prose |
| JSON structure | Specified — batch JSON template and source table block in Section 5.3 |

**Gap (G01, G08 partial):** SQL query for batch construction not provided. The join path mti_terms → wa_term_inventory → wa_verse_records → verse_context (to count unclassified verses per term) must be derived by Claude Code from the schema. The source table block in Section 5.3 specifies field-level sources but does not provide the accumulation query.

**Severity:** AMBIGUOUS
**Status:** OPEN
**Remediation:** Confirm by policy that batch construction accumulation queries are CC's responsibility to derive from schema — and state this explicitly in VerseContext Instruction Section 5.2 and CC Instructions Section 14.1. This closes G01 and G08 by policy acknowledgement rather than requiring explicit SQL. Requires researcher decision (Q-C).

---

### IP-VC-02 — DB READ: Batch JSON construction — populate all term and verse fields

**Direction:** DB → Batch JSON
**Operation:** Claude Code populates the full batch JSON structure from database tables

| Criterion | State |
|---|---|
| Operation | Specified |
| Method | Specified — source table mapping added in VerseContext v1.2 Section 5.3 |
| Fields and values | Specified — every field mapped to source table and join |
| JSON structure | Specified — full template in Section 5.3 |

**Status:** CLOSED
**Resolves:** G08 (field-level sources now specified; accumulation query addressed under IP-VC-01)

---

### IP-VC-03 — DB READ: VCGROUP targeted update — input data

**Direction:** DB → JSON input for Claude AI
**Operation:** Claude Code provides current group record with anchor verses before a VCGROUP patch

| Criterion | State |
|---|---|
| Operation | Specified |
| Method | Specified — source table block in VerseContext v1.2 Section 8.1 |
| Fields and values | Specified |
| JSON structure | Specified — input JSON template in Section 8.1 |

**Status:** CLOSED

---

### IP-VC-04 — DB READ: VCVERSE targeted update — input data

**Direction:** DB → JSON input for Claude AI
**Operation:** Claude Code provides verse record, existing verse_context, and available groups before a VCVERSE patch

| Criterion | State |
|---|---|
| Operation | Specified |
| Method | Specified — source table block in VerseContext v1.2 Section 9.1 |
| Fields and values | Specified |
| JSON structure | Specified — input JSON template in Section 9.1 |

**Status:** CLOSED

---

### IP-VC-05 — DB WRITE: VERSECONTEXT patch — verse_context_group and verse_context inserts/updates

**Direction:** Patch JSON → DB
**Operation:** Claude AI produces patch; Claude Code applies inserts and updates to verse_context_group and verse_context

| Criterion | State |
|---|---|
| Operation | Specified |
| Method | Specified — patch type VERSECONTEXT; patch_specification v1.4 governs; operation templates in Section 7.3 |
| Fields and values | Specified — table fields in Sections 2.1 and 2.2; consistency rules R1–R4 in Section 2.3 |
| JSON structure | Specified — full patch template in Section 7.2 and Annexure C |

**Gap (G05):** No handling rule for when ALL verses for a term fail the relevance filter. Rule R4 requires every term to have at least one active anchor. If every verse is genuinely non-inner-being, no anchor can legitimately be designated. Three options exist and none is specified: (a) flag to researcher and stop; (b) designate least-irrelevant as anchor with note; (c) treat term as zero-anchor and flag.

**Gap (G02):** term_classification_complete = false does not distinguish "never started" from "partially classified." No guidance on how Claude AI handles partial prior classification in a new batch — whether to continue or treat as fresh.

**Gap (G03):** term_classification_complete = true triggers a review, but "clearly warranted" revision criterion is undefined. Claude AI may re-classify unnecessarily or miss warranted revisions.

**Gap (G04):** No guidance on when minor variations warrant a new group vs expanding an existing group. No maximum group count. Will produce inconsistent grouping across 5,518 OWNER terms.

**Severity:** G05 MISSING | G02 AMBIGUOUS | G03 AMBIGUOUS | G04 MISSING
**Status:** OPEN
**Remediation:**
- G05: Add all-verses-fail handling rule to VerseContext Instruction Section 3 or 6.2. Requires researcher decision (Q-B).
- G02: Add note to Section 5.3 or 6.2: partial classification is treated as incomplete — Claude AI reviews existing records for a term and continues classification from where prior work left off. No re-start from scratch unless revision is warranted.
- G03: Add criterion for "clearly warranted" revision — a revision is warranted when the existing context_description would materially misrepresent the term's inner-being function, or when a clearly stronger anchor verse is available and the current anchor is demonstrably weaker.
- G04: Add grouping discipline note to Section 6.2: prefer fewer, broader groups; create a new group only when the context_description would be genuinely distinct from all existing groups. 5+ groups for a single term is unusual and should be flagged to researcher.

---

### IP-VC-06 — DB WRITE: Consistency rule validation after patch

**Direction:** DB read (validation)
**Operation:** Claude Code runs R1–R3 SQL validation queries after every VERSECONTEXT patch

| Criterion | State |
|---|---|
| Operation | Specified |
| Method | Specified — SQL queries in VerseContext v1.2 Section 11.3 and CC v3 Section 14.3 |
| Fields and values | Specified |
| JSON structure | N/A |

**Status:** CLOSED

---

### IP-VC-07 — DB WRITE: Registry completion — set verse_context_status = Complete

**Direction:** DB → DB (status update)
**Operation:** Claude Code checks OWNER completion and XREF coverage; sets verse_context_status = Complete

| Criterion | State |
|---|---|
| Operation | Specified — completion logic in VerseContext v1.2 Sections 13.1–13.3 and CC v3 Section 14.5 |
| Method | Specified — SQL queries provided in both documents |
| Fields and values | Specified — UPDATE word_registry SET verse_context_status = 'Complete' |
| JSON structure | N/A |

**Gap (G06 — clarified):** VerseContext Instruction Section 13.3 sets verse_context_status = Complete but does not mention session_b_status = 'Ready for Analysis'. Confirmed from patch_specification Section 0: 'Ready for Analysis' is set by audit_word (using COALESCE — only if current status is NULL), not by any Verse Context patch operation. DataPrep Section 4.1 gates on verse_context_status = Complete, not on session_b_status = 'Ready for Analysis'. The current pipeline does not require VerseContext to set this status. However, the status vocabulary includes it and its trigger source (audit_word) is not documented in the VerseContext instruction, creating confusion.

**Severity:** AMBIGUOUS — pipeline functions without this being set by VerseContext; the ambiguity is about documentation clarity only.
**Status:** OPEN
**Remediation:** Add a clarifying note to VerseContext Instruction Section 13.3: "session_b_status is not updated by this process. The value 'Ready for Analysis' in the session_b_status vocabulary is set by audit_word (COALESCE — only if current status is NULL) and is not required for the DataPrep gate. DataPrep gates on verse_context_status = Complete."

---

### IP-VC-08 — DB WRITE: Re-export full word JSON on registry completion

**Direction:** DB → JSON file
**Operation:** Claude Code re-exports full word JSON when registry reaches verse_context_status = Complete

| Criterion | State |
|---|---|
| Operation | Specified |
| Method | Specified — bash command in VerseContext v1.2 Section 13.3 |
| Fields and values | Specified — DataPrep Annexure C documents export structure |
| JSON structure | Specified — DataPrep Annexure C |

**Gap (G07):** No instruction on how Claude Code reports batch-level completion progress — which registries reached Complete in this batch and which remain In Progress. The per-registry completion report template (Section 13.4) covers individual reporting but not the batch-level summary needed for Stage 1 progress tracking.

**Severity:** MISSING
**Status:** OPEN
**Remediation:** Add a batch-level completion summary block to VerseContext Instruction Section 13.4 or CC Instructions Section 14.5: after applying each VERSECONTEXT patch, report total registries in batch, registries that reached Complete this batch (list), registries still In Progress (list), and total unclassified OWNER terms remaining programme-wide.

---

## Stage 2 — DataPrep

**Governing document:** WA-SessionB-DataPrep-Instruction-v5.4

---

### IP-DP-01 — DB READ: Load and validate word JSON export

**Direction:** JSON file → Claude AI session
**Operation:** Claude AI reads post-Verse-Context word export; validates both status fields

| Criterion | State |
|---|---|
| Operation | Specified — gate checks in Sections 4.1 and 4.2 |
| Method | Specified |
| Fields and values | Specified — Annexure C documents export structure and key DataPrep fields |
| JSON structure | Specified — DataPrep Annexure C |

**Status:** CLOSED
**Resolves:** G12 — DataPrep v5.4 Section 7.1 now requires a minimal status-only patch when no term changes are needed, ensuring session_b_status always advances to Pre-Analysis Complete. The "confirm without a patch" path is removed.

---

### IP-DP-02 — DB WRITE: Pre-analysis patch — mti_terms status, research flags, session_b_status

**Direction:** Patch JSON → DB
**Operation:** Claude AI produces patch; Claude Code applies: update_mti_status per term, insert wa_session_research_flags (PH2 flags), update_registry setting session_b_status = Pre-Analysis Complete

| Criterion | State |
|---|---|
| Operation | Specified |
| Method | Specified — operation types in Sections 7.4 and 7.5; patch_specification v1.4 governs |
| Fields and values | Specified — operation templates with all fields |
| JSON structure | Specified — patch template in Section 7.2 and Annexure A |

**Gap (G28):** patch_specification Section 3.1 explicitly states update_mti_status "matches on strongs_number only." If two registries share a Strong's number (OWNER in one, XREF in another), a DataPrep update_mti_status targeting that term by strongs_number would affect the mti_terms record shared by both — including any XREF. However: (a) DataPrep only produces one patch per registry, so the registry_id context is clear; (b) mti_terms holds one record per strongs_number programme-wide, so updating it updates the shared record. The risk is real if two different registries' DataPrep patches classify the same Strong's number differently. The instruction does not address this.

**Gap (G13):** The distinction between update_mti_status (writes mti_terms.status — programme-wide term classification) and update_evidential_status (writes wa_term_inventory.evidential_status — word-specific analytical assessment on a different table) is never explained in either instruction. Both operations appear in templates and a reader unfamiliar with the schema could conflate them.

**Gap (G30):** DataPrep Section 6 classification list does not include extracted_theological_anchor. Reference v5.3 Section 2 lists it as a valid mti_terms.status value. If a term arrives in DataPrep with this status, Claude AI has no instruction for handling it — whether to leave it, treat it as extracted, or reclassify it.

**Severity:** G28 AMBIGUOUS | G13 MISSING | G30 MISSING
**Status:** OPEN
**Remediation:**
- G28: Add a note to DataPrep Section 7.4 update_mti_status: "update_mti_status matches on strongs_number programme-wide. For XREF terms in this registry, do not produce update_mti_status operations — their mti_terms.status reflects the OWNER registry's classification and must not be overwritten by a DataPrep patch targeting a different registry." This closes the risk for DataPrep. The broader patch_specification clarification (whether term_inv_id should be an additional match key) remains an open architecture question.
- G13: Add a one-line note to DataPrep Section 7.4 and Extraction Section 6.1: update_mti_status writes mti_terms.status (programme-wide, shared across registries). update_evidential_status writes wa_term_inventory.evidential_status (per-registry, per-word analytical record on a different table). These are distinct and non-overlapping operations.
- G30: Add extracted_theological_anchor to DataPrep Section 6 with handling rule. Requires researcher decision (Q-F).

---

### IP-DP-03 — DB READ (monitoring): Pool readiness check

**Direction:** DB → status report
**Operation:** Claude Code checks whether all words in a pool have reached Pre-Analysis Complete; reports to researcher when ready

| Criterion | State |
|---|---|
| Operation | Specified — Sections 9.1–9.3 |
| Method | Specified — SQL queries provided |
| Fields and values | Specified |
| JSON structure | N/A — report template in Section 9.3 |

**Gap (G10):** Section 9.1 uses cluster_assignment as a proxy for pool membership. The note immediately after states that for multi-cluster pools, Claude Code must reference the pool definition in RMG Section 7 directly. RMG v5.5 Section 7a now provides a complete pool_id controlled vocabulary table with explicit word membership for each pool. Pool membership is therefore derivable from RMG Section 7a — but the DataPrep instruction does not state this explicitly, and Section 9.2 query still requires `{list of registry_no values in this pool}` to be resolved manually.

**Gap (G11 — CLOSED):** pool_id controlled vocabulary is now fully defined in RMG v5.5 Section 7a. This gap is closed.

**Severity:** G10 AMBIGUOUS
**Status:** OPEN
**Remediation — G10:** Update DataPrep Section 9.1 note and CC Instructions Section 14.8 to state explicitly: "Pool membership is defined in WA-Registry-Management-Guide Section 7a. For multi-cluster pools, Claude Code derives the list of registry_no values from the pool_id controlled vocabulary table in Section 7a. No database column is required — the RMG table is the authoritative source." This closes G10 by documentation without requiring a schema change. Researcher decision Q-D is now answerable from the documents themselves: RMG 7a is sufficient.

---

### IP-DP-04 — DB WRITE: Re-export JSON after pre-analysis patch

**Direction:** DB → JSON file
**Operation:** Claude Code re-exports word JSON after applying pre-analysis patch

| Criterion | State |
|---|---|
| Operation | Specified — Section 8 step 8; handoff in Section 10.1 |
| Method | Specified |
| Fields and values | Specified |
| JSON structure | Specified — same export format, Annexure C |

**Status:** CLOSED

---

## Stage 3 — Pool Analysis Dataset Assembly

**Governing documents:** WA-SessionB-ClaudeCode-Instructions-v3 Section 14.8 | WA-SessionB-Analysis-Instruction-v5.3 Annexure B

---

### IP-PA-01 — DB READ: Construct pool analysis dataset

**Direction:** DB → Pool analysis JSON
**Operation:** Claude Code assembles pool analysis dataset from multiple tables for all words in the pool

| Criterion | State |
|---|---|
| Operation | Specified |
| Method | Specified — source tables listed in CC v3 Section 14.8 |
| Fields and values | Specified — source table mapping provided |
| JSON structure | Specified — full template in Analysis Instruction Annexure B |

**Gap (G10 continuation):** CC Section 14.8 says "pool membership: word_registry (cluster_assignment + pool processing sequence from WA-Registry-Management-Guide-v5.5 Section 7)" — a prose reference, not a queryable mechanism. Same resolution as IP-DP-03: add explicit statement that pool membership is derived from RMG Section 7a controlled vocabulary table.

**Gap (IP-PA-01a):** No SQL query provided for the pre-construction check (confirm verse_context_status = Complete for all pool words before assembling the dataset). The check is required but not specified.

**Severity:** G10 AMBIGUOUS | IP-PA-01a AMBIGUOUS
**Status:** OPEN
**Remediation:**
- G10: Add to CC Instructions Section 14.8: pool membership is derived from RMG Section 7a. Same fix as IP-DP-03.
- IP-PA-01a: Add SQL pre-construction check to CC Section 14.8: `SELECT no, word, verse_context_status FROM word_registry WHERE no IN ({pool_registry_nos}) AND verse_context_status != 'Complete';` — if any rows returned, halt and report to researcher.

---

## Stage 4 — Session B Analysis

**Governing document:** WA-SessionB-Analysis-Instruction-v5.3

---

### IP-AN-01 — DB READ: Load pool analysis dataset at session start

**Direction:** JSON file → Claude AI session
**Operation:** Claude AI loads pool analysis dataset; validates status fields per word; determines session approach

| Criterion | State |
|---|---|
| Operation | Specified — startup sequence in Section 4.3; status validation in Section 4.4 |
| Method | Specified |
| Fields and values | Specified — Annexure B documents dataset structure |
| JSON structure | Specified — Annexure B |

**Gap (G14):** Section 4.2 specifies simultaneous vs word-by-word fallback based on "manageable session scope" — but no numeric threshold is given. Two different AI sessions on the same dataset may make different decisions. This is the primary session design decision and has no specified criterion.

**Gap (G17):** The pool dataset includes quality_flags and phase2_flags arrays on each OWNER term. The Analysis instruction says "note any significant data quality issues" but gives no guidance on which flags change analytical approach, which affect evidential status decisions, and which warrant SD pointers.

**Gap (G18):** Step 4 (Root and etymology) instructs Claude AI to note root family, but root_family data is absent from the pool dataset structure (Annexure B has no root_family field). Claude AI cannot complete Step 4 from the data as provided. The step either relies on Claude AI's prior knowledge (violating data-first principle) or is silently skipped.

**Severity:** G14 BLOCKING | G17 MISSING | G18 AMBIGUOUS
**Status:** OPEN
**Remediation:**
- G14: Add numeric threshold to Analysis Instruction Section 4.2. Requires researcher decision (Q-A).
- G17: Add a quality flag handling table to Section 7 (ten-step protocol, Step 2 or Step 1): specify which flag types warrant a caution note in the analysis (PH2_VOLUME_LIMITATION, THIN_DATA, HIGH_FREQUENCY_ANCHOR), which trigger an SD pointer (PH2_CROSS_REGISTRY_REQUIRED, PH2_BOUNDARY_QUESTION), and which are for information only (CONCRETE_PHYSICAL, SPAN_FILTER_APPLIED).
- G18: Add a note to Section 7 Step 4: root_family data is not currently included in the pool dataset. If root data is absent, note this in the narrative and proceed — do not draw on prior knowledge external to the dataset. Where etymology is relevant and root data is missing, flag as a Session D enrichment item.

---

### IP-AN-02 — DB WRITE: Analysis closing patch — registry_note and update_registry

**Direction:** Patch JSON → DB
**Operation:** Claude AI produces closing patch; Claude Code applies: registry_note, update_registry setting session_b_status = Analysis Complete

| Criterion | State |
|---|---|
| Operation | Partially specified — Section 12.1 describes intent |
| Method | Specified — patch type ANALYSIS; template in Section 12.3 |
| Fields and values | INCORRECT — current patch template contains bulk_update on mti_terms.status_note |
| JSON structure | INCORRECT — current Section 12.3 template contains an operation that should be removed |

**Gap (G15, G26 — decision made, instruction not yet updated):** The current Analysis Instruction Section 12.3 patch template includes a bulk_update operation writing mti_terms.status_note. Note: bulk_update IS a defined operation in patch_specification v1.4 Section 3.10a — it is not undefined. However, the decision made 2026-03-29 was to remove this operation entirely from the Analysis closing patch. The reason: writing mti_terms.status_note in the Analysis session is premature — the full evidential assessment belongs in the Extraction patch. The instruction has not been updated to reflect this decision. The current Section 12.3 template is inconsistent with the agreed design.

**Severity:** BLOCKING — patch as currently specified produces an operation that should not exist, and the session design intent is not correctly documented.
**Status:** PENDING UPDATE → Analysis Instruction v5.3 to v5.4
**Remediation:** Update Analysis Instruction Section 12 to: (a) remove bulk_update and mti_terms.status_note write entirely; (b) update patch template to contain only registry_note + update_registry; (c) add a researcher checkpoint rule: if a situation arises requiring bulk field updates not covered by standard patch operations, Claude AI must surface a field-level proposal to the researcher before constructing any patch; (d) update _patch_summary block to reflect 2 operations only. Decision recorded in WA-SessionLog-FieldAnalysis-v1-20260329 Section 3.1.

---

### IP-AN-03 — DB WRITE: Claude Code applies analysis closing patch and re-exports

**Direction:** DB write + re-export
**Operation:** Claude Code applies ANALYSIS patch; confirms session_b_status = Analysis Complete; re-exports word JSON; reports pool ready for Extraction

| Criterion | State |
|---|---|
| Operation | Specified — handoff template in Section 12.4 |
| Method | Specified |
| Fields and values | Specified |
| JSON structure | N/A |

**Status:** CLOSED (contingent on IP-AN-02 correction)

---

## Stage 5 — Session B Extraction

**Governing document:** WA-SessionB-Extraction-Instruction-v5.4

---

### IP-EX-01 — DB READ: Load word JSON exports — obtain term_inv_ids and file_ids

**Direction:** JSON file → Claude AI session
**Operation:** Claude AI reads post-analysis word JSON exports to obtain term_inv_ids and file_ids for patch operations

| Criterion | State |
|---|---|
| Operation | Specified |
| Method | Specified — Section 1: term_inv_id from mti.id; file_id from files[0].id (Phase 1 entry, most recent produced_date) |
| Fields and values | Specified |
| JSON structure | Specified — DataPrep Annexure C |

**Status:** CLOSED
**Resolves:** G24 — file_id selection rule added in v5.4.

---

### IP-EX-02 — DB READ: Load word_registry.json for cross-registry resolution

**Direction:** File → Claude AI session
**Operation:** Claude AI loads word_registry.json to resolve also_in_registries to {registry_id, word} pairs

| Criterion | State |
|---|---|
| Operation | Specified |
| Method | Specified — Section 1: engine --export-registry command; re-export at start of each session |
| Fields and values | Specified — minimum required fields: no, word, cluster_assignment, session_b_status |
| JSON structure | Sufficient — minimum fields specified for the resolution purpose |

**Status:** CLOSED
**Resolves:** G23 — export command and required fields specified in v5.4.

---

### IP-EX-03 — DB WRITE: Analysis completion patch — evidential status, dimensions, inner being standing, findings, SD pointers, session_b_status

**Direction:** Patch JSON → DB
**Operation:** Claude AI produces analysis completion patch; Claude Code applies: update_evidential_status per OWNER term, insert wa_session_b_dimensions, update_registry (sb_classification, carry_forward), insert wa_session_b_findings, insert wa_session_research_flags (SD_POINTER), update_registry (session_b_status = Analysis Complete)

| Criterion | State |
|---|---|
| Operation | Specified — six operation groups in Section 6.1 |
| Method | Specified — patch type SESSIONB; operation types in Annexure B |
| Fields and values | PARTIALLY SPECIFIED — OWNER-only rule missing; dimensions and description updates missing |
| JSON structure | Specified — Annexure B patch template |

**Gap (G16 — decision made, instruction not updated):** The OWNER-only rule for update_evidential_status is not explicitly stated in Section 6.1 Group A or Annexure B. Section 4.3a states "XREF terms: no patch operations" but does not explicitly state this applies to update_evidential_status. patch_specification v1.4 Section 3.10 confirms update_evidential_status matches on term_inv_id — so targeting an XREF term_inv_id would incorrectly write evidential_status to a XREF record. The decision made 2026-03-29 confirmed OWNER-only targeting. The instruction has not been updated.

**Gap (G29 — decision made, instruction not updated):** word_registry.dimensions and word_registry.description are not written by any operation in the current Extraction patch template. The field mapping table (Section 5) maps dimension booleans to wa_session_b_dimensions but omits word_registry.dimensions (comma-delimited multi-value) and word_registry.description. The decision made 2026-03-29 was that Extraction must write both via update_registry. The instruction has not been updated.

**Gap (G21):** The pool_observations block in the final registry extract Annexure C has no corresponding database table. It is a file-only artefact. The instruction does not state this explicitly, creating uncertainty about whether Session D can query this data programmatically.

**Severity:** G16 MISSING (PENDING UPDATE) | G29 MISSING (PENDING UPDATE) | G21 AMBIGUOUS (OPEN)
**Status:** PENDING UPDATE (G16, G29) | OPEN (G21)
**Remediation:**
- G16: Add explicit statement to Extraction Instruction Section 6.1 Group A: "update_evidential_status targets OWNER records only. One operation per active OWNER term. XREF terms inherit evidential status from their OWNER registry — no update_evidential_status operation is produced for XREF term_inv_ids." Also add to Annexure B patch template note. Decision recorded in WA-SessionLog-FieldAnalysis-v1-20260329 Section 3.2. → Extraction v5.5
- G29: Add two update_registry operations to Extraction Instruction Section 6.1 (new Group F) and Annexure B patch template: (1) word_registry.dimensions — comma-delimited string derived from Session B dimensional analysis, using the valid dimension values from WA-Reference Section 4.3; (2) word_registry.description — Session B confirmed description replacing the Phase 1 preliminary value. Add derivation rules to Section 8.1. → Extraction v5.5
- G21: Add a note to Extraction Section 8.1 and Annexure C: pool_observations is a file-only artefact in the final registry extract. It is not persisted to the database. If Session D requires programmatic query of intra-pool observations, a database table will need to be designed at that stage. → Extraction v5.5

---

### IP-EX-04 — DB WRITE: Session B Complete status patch

**Direction:** Patch JSON → DB
**Operation:** After all four outputs per word confirmed, produce and apply SESSIONB-COMPLETE patch setting session_b_status = Session B Complete

| Criterion | State |
|---|---|
| Operation | Specified |
| Method | Specified — patch template in Section 9 |
| Fields and values | Specified |
| JSON structure | Specified — template in Section 9 |

**Status:** CLOSED
**Resolves:** G27 — Session B Complete trigger and patch template added in Extraction v5.4.

---

### IP-EX-05 — DB WRITE: Re-export JSON after analysis completion patch

**Direction:** DB → JSON file
**Operation:** Claude Code re-exports word JSON after applying analysis completion patch

| Criterion | State |
|---|---|
| Operation | Specified — handoff in Section 6.3 step 7 |
| Method | Specified |
| Fields and values | Specified |
| JSON structure | N/A |

**Status:** CLOSED

---

## Cross-Pipeline Issues

---

### IP-XP-01 — Two SESSIONB patches — naming and idempotency

**Documents:** Analysis Instruction v5.3 Section 12.2 | Extraction Instruction v5.4 Section 6.2 | patch_specification v1.4 Section 6
**Issue (G25):** v5.3 resolved the naming conflict by using -ANALYSIS- infix for the Analysis patch (PATCH-{date}-{nnn}-ANALYSIS-V1.json) vs Extraction's PATCH-{date}-{nnn}-SESSIONB-V1.json. Both set session_b_status = Analysis Complete when applied in sequence.

**Confirmed from patch_specification Section 6:** "apply_session_patch.py overwrites session_b_status from _patch_meta.session_b_status." There is no idempotency check on the status value itself — the applicator simply overwrites. Applying Analysis Complete twice overwrites with the same value. No error is raised.

**Status:** CLOSED
**Resolves:** G25 — naming conflict resolved in v5.3; double status write confirmed as harmless by patch_specification overwrite behaviour.

---

### IP-XP-02 — Broken cross-reference — WA-Reference Section 4.3

**Documents:** Extraction Instruction v5.4 Section 8.1 | WA-Reference v5.3 Section 4.3
**Issue (G22):** Extraction Section 8.1 says the comma-delimited dimensions value is derived per "WA-Reference-v5.3 Section 4.3."

**Confirmed from WA-Reference v5.3:** Section 4.3 DOES exist. It contains the dimensions vocabulary — 14 valid comma-delimited values (Affective/Emotional, Anthropological/Structural, Character/Disposition, Cognitive/Mind, Identity/Selfhood, Inner Life, Moral/Conscience, Relational/Social, Sin & Vice, Spiritual/God-ward, Volitional/Capacity, Volitional/Will, Theological/Divine-Human, Somatic/Embodied). The cross-reference is correct.

**Status:** CLOSED
**Resolves:** G22 — Section 4.3 exists and contains the required vocabulary. No update needed.

---

### IP-XP-03 — extracted_theological_anchor not handled in DataPrep

**Documents:** WA-SessionB-DataPrep-Instruction-v5.4 Section 6 | WA-Reference v5.3 Section 2
**Issue (G30):** DataPrep Section 6 classification list omits extracted_theological_anchor. If a term arrives with this status, Claude AI has no instruction for handling it.

**Severity:** MISSING
**Status:** OPEN
**Remediation:** Add extracted_theological_anchor to DataPrep Section 6 with a handling rule. Requires researcher decision (Q-F).

---

### IP-XP-04 — Redundant fields not documented

**Documents:** WA-Reference v5.3 | WA-Registry-Management-Guide v5.5
**Issue (GAP-B, GAP-C, GAP-K, GAP-L):** Four fields exist in the database that are redundant relative to the pipeline:
- wa_term_inventory.god_as_subject — duplicated by mti_term_flags flag_id 1 (GOD_AS_SUBJECT)
- wa_term_inventory.somatic_link — duplicated by mti_term_flags flag_id 3/4 (SOMATIC_INNER_LINK, BODY_INNER_EXPRESSION)
- word_registry.inference_note — no pipeline stage writes to it; contains researcher-set pre-existing content that must be preserved
- wa_term_inventory.status_note — NULL across all records; no documented purpose

No pipeline operation writes to these fields. Their presence in export JSON may cause confusion.

**Severity:** MISSING (documentation gap — no pipeline impact)
**Status:** PENDING UPDATE → Reference v5.4 and RMG v5.6
**Remediation:** Add a redundant fields note to WA-Reference Section 13 and RMG: document that these fields exist but are not written by any pipeline stage; note that inference_note may contain researcher-set content that must not be overwritten; note that god_as_subject and somatic_link are superseded by the mti_term_flags mechanism. Decision recorded in WA-SessionLog-FieldAnalysis-v1-20260329 Sections 3.6 and 3.7.

---

### IP-XP-05 — Engine-derived fields not documented as Phase 1 only

**Documents:** WA-Reference v5.3 | WA-Registry-Management-Guide v5.5
**Issue (GAP-E through GAP-J):** word_registry fields phase1_term_count, phase1_verse_count, unique_term_count, shared_term_count, term_sharing_ratio are engine-derived at Phase 1 and not updated by any subsequent pipeline stage. Instructions do not document this constraint. Risk: pipeline stages may read these fields expecting current counts.

**Severity:** MISSING (documentation gap)
**Status:** PENDING UPDATE → Reference v5.4
**Remediation:** Add a note to WA-Reference Section 13.1 (word_registry fields): these five fields reflect Phase 1 extraction state only and are not updated by the Session B pipeline. Live counts must be derived from queries against mti_terms and wa_term_inventory. Decision recorded in WA-SessionLog-FieldAnalysis-v1-20260329 Section 3.5.

---

## Researcher Decisions Required

These gaps cannot be closed by instruction update alone.

| # | Question | Impacts | Severity |
|---|---|---|---|
| Q-A | What is the numeric threshold (total anchor verses across all pool words) for simultaneous vs word-by-word analysis in Session B? | Analysis Instruction v5.4 Section 4.2 | BLOCKING |
| Q-B | What should Claude AI do when ALL verses for a term fail the relevance filter? Options: (a) flag to researcher and stop; (b) designate least-irrelevant as anchor with note; (c) treat term as zero-anchor and flag for researcher decision post-batch. | VerseContext Instruction v1.3 Section 3 or 6.2 | MISSING |
| Q-C | Are batch construction SQL accumulation queries Claude Code's responsibility to derive from the schema? If yes, add a policy statement to VerseContext Instruction Section 5.2 confirming this — which closes G01 and G08 without requiring explicit SQL in the instruction. | VerseContext Instruction v1.3 Section 5.2; CC Instructions Section 14.1 | AMBIGUOUS |
| Q-F | How should DataPrep handle a term with mti_status = extracted_theological_anchor — leave unchanged (treat as extracted), reclassify to extracted, or flag for researcher decision? | DataPrep Instruction v5.5 Section 6 | MISSING |

**Note — Q-D and Q-G removed as no longer open:** Q-D (pool membership) is resolved — RMG Section 7a is confirmed as the authoritative source; instruction update is sufficient without a schema change. Q-G (Reference Section 4.3) is resolved — Section 4.3 exists and contains the dimensions vocabulary. Q-E (idempotency) is resolved — patch_specification confirms overwrite behaviour is silent.

---

## Complete Gap Status Register

| Gap ID | Stage | Description | v1 Severity | Current Status |
|---|---|---|---|---|
| G01 | Verse Context | Batch construction accumulation query not specified | BLOCKING | OPEN — see IP-VC-01. Requires Q-C decision. |
| G02 | Verse Context | term_classification_complete logic undefined for partial classification | AMBIGUOUS | OPEN — see IP-VC-05. Remediation identified. |
| G03 | Verse Context | "Clearly warranted" revision criterion undefined | AMBIGUOUS | OPEN — see IP-VC-05. Remediation identified. |
| G04 | Verse Context | No grouping discipline guidance; no maximum group count | MISSING | OPEN — see IP-VC-05. Remediation identified. |
| G05 | Verse Context | No handling rule for all-verses-fail | MISSING | OPEN — see IP-VC-05. Requires Q-B decision. |
| G06 | Verse Context | session_b_status = Ready for Analysis transition unspecified in VerseContext | INCONSISTENT | OPEN — see IP-VC-07. Remediation identified: note that Ready for Analysis is set by audit_word, not VerseContext. |
| G07 | Verse Context | No batch-level completion progress reporting format | MISSING | OPEN — see IP-VC-08. Remediation identified. |
| G08 | Verse Context | Batch JSON population queries not specified | BLOCKING | PARTIALLY CLOSED — field-level sources specified in v1.2 (IP-VC-02 CLOSED). Accumulation query addressed under IP-VC-01 (requires Q-C). |
| G09 | Extraction | intra_pool column does not exist in schema | MISSING | CLOSED — resolved in Extraction v5.4: finding_type = pool_observation. |
| G10 | DataPrep | Pool membership not queryable from database | BLOCKING | OPEN — see IP-DP-03, IP-PA-01. Remediation identified: RMG Section 7a is sufficient; instruction update needed to state this explicitly. No schema change required. |
| G11 | DataPrep | pool_id values never defined | AMBIGUOUS | CLOSED — resolved by RMG v5.5 Section 7a controlled vocabulary. |
| G12 | DataPrep | No-patch path leaves session_b_status unadvanced | AMBIGUOUS | CLOSED — resolved in DataPrep v5.4 Section 7.1: minimal status-only patch always required. |
| G13 | DataPrep | Relationship between update_mti_status and update_evidential_status unexplained | MISSING | OPEN — see IP-DP-02. Remediation identified. |
| G14 | Analysis | Simultaneous threshold undefined | BLOCKING | OPEN — see IP-AN-01. Requires Q-A decision. |
| G15 | Analysis | Analysis closing patch template should not contain bulk_update on mti_terms | MISSING | PENDING UPDATE — bulk_update IS defined in patch_specification v1.4 Section 3.10a, but the decision made 2026-03-29 is to remove it from the Analysis patch entirely. Analysis Instruction v5.3 → v5.4. See IP-AN-02. |
| G16 | Extraction | OWNER-only rule for update_evidential_status not stated | AMBIGUOUS | PENDING UPDATE — decision made 2026-03-29. Extraction v5.4 → v5.5. See IP-EX-03. |
| G17 | Analysis | Quality flag handling in analysis undefined | MISSING | OPEN — see IP-AN-01. Remediation identified. |
| G18 | Analysis | Root data absent from pool dataset; Step 4 cannot be completed from data | AMBIGUOUS | OPEN — see IP-AN-01. Remediation identified. |
| G19 | Analysis | pool_id format and valid values not defined | MISSING | CLOSED — resolved by RMG v5.5 Section 7a. |
| G20 | Extraction | intra_pool column (duplicate of G09) | BLOCKING | CLOSED — same resolution as G09. |
| G21 | Extraction | pool_observations block not persisted to database; not documented as file-only | AMBIGUOUS | OPEN — see IP-EX-03. Remediation identified. |
| G22 | Extraction | Broken cross-reference to Reference Section 4.3 | MISSING | CLOSED — Section 4.3 confirmed to exist in WA-Reference v5.3. Cross-reference is correct. |
| G23 | Extraction | word_registry.json source undefined | AMBIGUOUS | CLOSED — resolved in Extraction v5.4 Section 1. |
| G24 | Extraction | file_id selection rule unspecified | MISSING | CLOSED — resolved in Extraction v5.4 Section 1. |
| G25 | Cross-doc | Two SESSIONB patches naming conflict and idempotency | INCONSISTENT | CLOSED — naming fixed in v5.3; idempotency confirmed: patch_specification overwrites session_b_status silently. |
| G26 | Cross-doc | Analysis closing patch contains bulk_update that should be removed | BLOCKING | PENDING UPDATE — bulk_update is defined in spec, but the decision is to remove it from Analysis patch. Analysis v5.3 → v5.4. See IP-AN-02. Same document update as G15. |
| G27 | Cross-doc | Session B Complete trigger undefined | MISSING | CLOSED — resolved in Extraction v5.4 Section 9. |
| G28 | Cross-doc | update_mti_status matches on strongs_number only — XREF risk | AMBIGUOUS | OPEN — see IP-DP-02. Remediation identified: add note that DataPrep must not produce update_mti_status for XREF terms. |
| G29 | Cross-doc | word_registry.dimensions and description not written by any pipeline operation | MISSING | PENDING UPDATE — decision made 2026-03-29. Extraction v5.4 → v5.5. See IP-EX-03. |
| G30 | Cross-doc | extracted_theological_anchor not handled in DataPrep | MISSING | OPEN — see IP-DP-02. Requires Q-F decision. |
| GAP-B | Cross-doc | inference_note — redundant field not documented | MISSING | PENDING UPDATE — Reference v5.3 → v5.4. See IP-XP-04. |
| GAP-C | Cross-doc | wa_term_inventory.status_note — redundant field not documented | MISSING | PENDING UPDATE — Reference v5.3 → v5.4. See IP-XP-04. |
| GAP-E–J | Cross-doc | Engine-derived fields not documented as Phase 1 only | MISSING | PENDING UPDATE — Reference v5.3 → v5.4. See IP-XP-05. |
| GAP-K | Cross-doc | god_as_subject — redundant field not documented | MISSING | PENDING UPDATE — Reference v5.3 → v5.4. See IP-XP-04. |
| GAP-L | Cross-doc | somatic_link — redundant field not documented | MISSING | PENDING UPDATE — Reference v5.3 → v5.4. See IP-XP-04. |
| IP-PA-01a | Pool Assembly | Pre-construction check query not provided | NEW | OPEN — see IP-PA-01. Remediation identified. |

---

## Summary Counts

### By Status

| Status | Count |
|---|---|
| CLOSED | 16 |
| OPEN | 12 |
| PENDING UPDATE | 6 |
| **Total gaps** | **34** |

### Open and pending gaps by severity

| Severity | Count |
|---|---|
| BLOCKING | 2 (G14/IP-AN-01; G15+G26/IP-AN-02) |
| MISSING | 9 |
| AMBIGUOUS | 7 |
| **Total open + pending** | **18** |

### Document Updates Required

| Document | Current | Target | Changes required |
|---|---|---|---|
| WA-SessionB-Analysis-Instruction | v5.3 | v5.4 | Section 12: remove bulk_update and mti_terms.status_note write; patch template to registry_note + update_registry only; add researcher checkpoint rule; update _patch_summary |
| WA-SessionB-Extraction-Instruction | v5.4 | v5.5 | Section 6.1 Group A: OWNER-only rule for update_evidential_status; new Group F: update_registry for dimensions and description; Section 8.1: derivation rules for dimensions and description; Annexure B: updated patch template; note on pool_observations as file-only artefact |
| WA-Reference | v5.3 | v5.4 | Section 13.1: engine-derived fields note; Section 13.3: redundant fields note (god_as_subject, somatic_link, status_note); Section 13.1: inference_note note; Section 13.2: status_note note |
| WA-Registry-Management-Guide | v5.5 | v5.6 | Section 2: add engine-derived fields note |
| WA-VerseContext-Instruction | v1.2 | v1.3 | Section 13.3: clarify session_b_status/Ready for Analysis; Section 13.4: batch completion summary format; Section 5.2 and 6.2: partial classification guidance (G02, G03, G04, G07); Section 3 or 6.2: all-verses-fail rule after Q-B |
| WA-SessionB-DataPrep-Instruction | v5.4 | v5.5 | Section 6: add extracted_theological_anchor after Q-F; Section 7.4: update_mti_status XREF note; Section 9.1: pool membership from RMG 7a; add G13 note on update_mti_status vs update_evidential_status |

### Dry Run Gate Assessment — Gratitude (single not-shared word)

**BLOCKING — must resolve before dry run:**

| Gap | Action needed |
|---|---|
| IP-AN-02 / G15, G26 | Produce Analysis Instruction v5.4 (remove bulk_update from closing patch) |
| IP-AN-01 / G14 | Researcher decision on simultaneous analysis threshold (Q-A) |

**Does NOT block the gratitude dry run:**
G05/Q-B (all-verses-fail — unlikely for gratitude), G10/IP-DP-03 (pool membership — gratitude is not-shared, no pool), IP-PA-01 (pool dataset — not needed for not-shared word), IP-XP-03/G30 (extracted_theological_anchor — unlikely), G02/G03/G04 (batch guidance — low risk for single word), G17/G18 (quality flag and root guidance — low risk for one well-known word), G28 (XREF risk — not-shared word has no XREFs).

**Assessment:** Two items required before dry run. All other open gaps are either post-analysis stage, low probability for gratitude, or inapplicable to a not-shared single-word analysis.

---

*WA-InstructionGaps-v2-20260330 | Supersedes WA-InstructionGaps-v1-20260329 | 34 gaps total: 16 closed, 12 open, 6 pending update | 27 inflection points | 2 BLOCKING | Cross-gap consistency verified against live documents*


Researcher comments:

**Gap (G01, G08 partial):**   this reply applies to multiple GAPS

The Claude ai instructions is not expected to have the SQL queries or scripts. It is Claude Code's responsibility.  It is Claude ai responsibility to include all the details that is necessary to prepare the queries (field names, table names, rules for arriving at the desired result, definition of what the expected outcome should be).  Therefore, when something that is currently defined as Gap has all the relevant instructions and a clear hand over statement to Claude Code, then it is no longer a gap.

other GAPS related G07,G08, G10

### IP-VC-05 — DB WRITE:

**Gap (G05):** No handling rule for when ALL verses for a term fail the relevance filter. Rule R4 requires every term to have at least one active anchor. If every verse is genuinely non-inner-being, no anchor can legitimately be designated. Three options exist and none is specified: (a) flag to researcher and stop; (b) designate least-irrelevant as anchor with note; (c) treat term as zero-anchor and flag.

(a)  this scenario should never happen.

**Gap (G02):** term_classification_complete = false does not distinguish "never started" from "partially classified." No guidance on how Claude AI handles partial prior classification in a new batch — whether to continue or treat as fresh.

partial completion must be flagged to the researcher with reasons why it did not complete. The submission must be fixed and re-submitted.

**Gap (G03):** term_classification_complete = true triggers a review, but "clearly warranted" revision criterion is undefined. Claude AI may re-classify unnecessarily or miss warranted revisions.

the reasons for 'clearly warranted' must be updated in the notes and feedback to researcher

**Gap (G04):** No guidance on when minor variations warrant a new group vs expanding an existing group. No maximum group count. Will produce inconsistent grouping across 5,518 OWNER terms.

this is a concern, and it a judgement call.  I am not sure what the criteria for a group is set at but a variation is warranted when a group is evaluated against the criteria, and any one of the criteria is materially different. Materially different means an analysis of the verses may arrive at a differential conclusion.  The criteria is : it serves as a inner being characteristics; the context of the verse is different that the other, and the variation of the context changes or further enhance how the characteristic operate in or around the inner being. this could be related to the parties involved, what the characteristic is doing, what influences the characteristic, the involvement of other characteristics.

### IP-VC-07 — DB WRITE:

**Gap (G06 — clarified):** VerseContext Instruction Section 13.3 sets verse_context_status = Complete but does not mention session_b_status = 'Ready for Analysis'. Confirmed from patch_specification Section 0: 'Ready for Analysis' is set by audit_word (using COALESCE — only if current status is NULL), not by any Verse Context patch operation. DataPrep Section 4.1 gates on verse_context_status = Complete, not on session_b_status = 'Ready for Analysis'. The current pipeline does not require VerseContext to set this status. However, the status vocabulary includes it and its trigger source (audit_word) is not documented in the VerseContext instruction, creating confusion.

**Severity:** AMBIGUOUS — pipeline functions without this being set by VerseContext; the ambiguity is about documentation clarity only.
**Status:** OPEN
**Remediation:** Add a clarifying note to VerseContext Instruction Section 13.3: "session_b_status is not updated by this process. The value 'Ready for Analysis' in the session_b_status vocabulary is set by audit_word (COALESCE — only if current status is NULL) and is not required for the DataPrep gate. DataPrep gates on verse_context_status = Complete."

 the pipeline status setting is materially important because it would determine the overall status of processing of a word.  I can see from the gap that there are not a full understanding of the how the pipeline moves through, what set it, what happens with it in each process if it fails and how and when it is updated.  this gap may relate to other gaps also so this need to be handled holistically by first digging out all the pipeline updates, evaluate it against what should happen and is it complete and deals with all the pipeline change scenarios, and then the gaps can again be updated.

G13 - this was dealt with replies yesterday.  Get the replies and update the gaps,  should be closed.

| IP-AN-01 / G14 | Researcher decision on simultaneous analysis threshold (Q-A) |  

The threshold is not yet known.  We will keep on pushing the limits, but it is AI capability dependent.  It is likely to be in the region of approx. 9 words.