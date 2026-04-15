# WA Global Rules Audit — Session Log
**Filename:** wa-global-rules-audit-session-log-v1-2026-04-14.md
**Date:** 2026-04-14
**Version:** 1.0
**Prefix confirmed:** WA
**Task:** Cross-reference all instruction files against wa-global-general-rules-v1-2026-04-13.json; isolate rules from instruction files that belong in global rules; remove duplicates and conflicts; global rules take precedence.

---

## Session scope

Files reviewed:
1. wa-global-general-rules-v1-2026-04-13.json (the authority document)
2. WA-SessionB-Instruction-v4_7-2026-04-12.md
3. WA-VerseContext-Instruction-v2_5-20260409.md
4. WA-DimensionReview-Instruction-v1_9-2026-04-09.md
5. wa-global-sessionC-prose-rule-v1-2026-04-13.md (global document — special status)
6. wa-global-pass-close-procedure-v1-2026-04-13.md (global document — special status)
7. patch_specification_v1_10-20260412.md
8. WA-Registry-Management-Guide-v5_8-2026-04-12.md

Files NOT yet reviewed (not in scope for this session — not instruction files in the governing sense):
- WA-SessionD-Orientation-v3_0-2026-04-12.md
- WA-SessionB-ClaudeCode-Instructions-v3_2-20260330.md
- WA-Reference-v5_5-20260330.md
- wa-word-study-template-v2-2026-04-13.md

---

## Step 1 — Inventory of rules already in the global file

The global file (v1) contains 22 rules across seven categories:

| Rule ID | Category | Subject |
|---|---|---|
| GR-FILE-001 | file_naming | Filename structure |
| GR-FILE-002 | file_naming | Short description length (≤30 chars) |
| GR-FILE-003 | file_naming | Version numbering [major].[minor] |
| GR-FILE-004 | file_naming | No overwrites |
| GR-FILE-005 | file_format | Output format by purpose |
| GR-FILE-006 | file_naming | Prefix |
| GR-PASS-001 | pass_close | Pass-close download |
| GR-PASS-002 | pass_close | Write-on-discovery to database |
| GR-OBS-001 | observation_discipline | Write-on-discovery (non-waivable) |
| GR-OBS-002 | observation_discipline | Three-category model (a/b/c/session action) |
| GR-OBS-003 | observation_discipline | Session actions resolve at session close |
| GR-OBS-004 | observation_discipline | Observations on deleted items permitted |
| GR-OBS-005 | observation_discipline | Obsolete marker, not deletion [TRUNCATED — rule inferred from context] |
| GR-DATA-001 | database_pattern | AND mt.status IN ('extracted','extracted_thin') filter |
| GR-DATA-002 | database_pattern | Term ownership — one OWNER per term |
| GR-DATA-003 | database_pattern | XREF root_family artefact |
| GR-DATA-004 | database_pattern | Deprecated meaning fields |
| GR-DATA-005 | database_pattern | mti_term_flags authority over somatic_link |
| GR-DATA-006 | database_pattern | verse_context_record_count semantics |
| GR-DATA-007 | database_pattern | Research flag descriptions are historical |
| GR-PROG-001 | programme_orientation | Human-being study (not theological) |
| GR-PROG-002 | programme_orientation | Dimensions are data-derived |
| GR-PROG-003 | programme_orientation | Cluster assignment is a processing unit |
| GR-PROG-004 | programme_orientation | Borderline verses retained |
| GR-PROG-005 | programme_orientation | No sampling (non-waivable) |
| GR-PROG-006 | programme_orientation | No superlatives without source |
| GR-DIR-001 | claude_code_directive | Plain-language directives |

Note: GR-OBS-005 text was truncated in the file view. Full text not confirmed. This is flagged as an open item.

---

## Step 2 — Analysis of each instruction file

### 2.1 Session B Instruction (v4.7)

#### Rules found in Session B that overlap with or duplicate global rules

**Governing Disciplines section (lines 86–104):**

| Discipline stated in Session B | Global rule equivalent | Assessment |
|---|---|---|
| "Write on discovery" — every finding written at moment of discovery, nothing accumulated | GR-OBS-001 | DUPLICATE. Exact same rule, restated in prose. Session B should replace this with a reference to GR-OBS-001. |
| "Data is authoritative" — work from JSON only | Not in global rules | CANDIDATE for global rules. This is programme-wide methodology, not Session B-specific. |
| "No assumptions" — null is null, not implicitly populated | Not explicitly in global rules | CANDIDATE for global rules (sub-rule of "data is authoritative"). |
| "All changes through patches" — Claude AI produces, Claude Code executes | GR-DIR-001 partial | PARTIAL DUPLICATE. GR-DIR-001 covers the directive format. The "all changes through patches" principle is broader and not fully captured in GR-DIR-001. |
| "Load only what is needed" | Not in global rules | CANDIDATE — programme-wide discipline. |
| "Session logs at every breakpoint" | Partially GR-PASS-001 | GR-PASS-001 covers downloads at pass close. Session log at breakpoints is related but different. CANDIDATE for global rules or to stay as instruction-specific practice. |

**Step-by-step discipline:**
The "each step is completed before the next begins" principle appears in Session B governing disciplines but is not in global rules. Programme-wide — CANDIDATE.

**Analytical Principles section (lines 948–964):**

| Principle in Session B | Global rule equivalent | Assessment |
|---|---|---|
| "Cross-registry vision is always active" | Not in global rules | Session B-specific — do not lift to global. |
| "The data is authoritative" | GR-DATA (various) + programme-wide | CANDIDATE — already noted above. |
| "Emergence, not imposition" | GR-PROG-002 partial | Partial duplicate. GR-PROG-002 covers dimensions. The emergence principle is broader (covers somatic, semantic picture, all classifications). CANDIDATE to extend GR-PROG-002 or add new GR-PROG rule. |
| "Session C documents are not sacred" | Not in global rules | Session-specific — do not lift. |
| "Correlation signals confirm; they do not explain" | Not in global rules | Session B-specific — do not lift. |
| "Inferential is not confirmed — label as such" | Not in global rules | CANDIDATE for programme-wide rule. This is about analytical honesty, not Session B-specific. |
| "Phase 2 flags are recommendations, not conclusions" | Not in global rules | Session B-specific — do not lift. |
| "Somatic evidence is observational, not interpretive" | Not in global rules | Session B-specific — do not lift. |

**Integrity Rules table (lines 970–988):**

SB-3: "No patch is applied without researcher review" — not in global rules. CANDIDATE — programme-wide.
SB-6: "Observations log governs over session log in conflict" — not in global rules. CANDIDATE — applies to all sessions.

**Somatic evidence / mti_term_flags note (line 607):**
"Do NOT update wa_term_inventory.somatic_link — this is a redundant field per WA-Reference Section 13.3" — DUPLICATE of GR-DATA-005. Should be replaced by reference to GR-DATA-005.

**Naming Conventions (lines 992–1006):**
File naming pattern in Session B follows the GR-FILE-001 structure. Consistent — no conflict. The specific examples are instruction-specific and should remain. However, the note "All filenames lowercase" at line 1006 is a rule not captured in the global file. CANDIDATE for GR-FILE-006 extension or new GR-FILE rule.

#### Rules found in Session B that conflict with global rules

No direct conflicts identified. One potential tension:
- Session B line 608 says "Do NOT update wa_term_inventory.somatic_link" and cites "WA-Reference Section 13.3" as the authority. Global rule GR-DATA-005 is the current programme-wide authority. The Session B instruction should reference GR-DATA-005 directly (or both), not only WA-Reference.

#### Summary for Session B:
- DUPLICATES to remove (replace with reference to global rules): write-on-discovery discipline, somatic_link prohibition
- CANDIDATES to lift to global rules: "data is authoritative" principle, "no assumptions" sub-rule, "all changes through patches" / no direct DB manipulation, "load only what is needed", "session logs at every breakpoint", step-by-step discipline, "inferential is not confirmed", "no patch without researcher review", "observations log governs over session log in conflict", lowercase filenames
- CONFLICTS: None (one reference inconsistency — WA-Reference vs GR-DATA-005)

---

### 2.2 Verse Context Instruction (v2.5)

#### Rules found that overlap with or duplicate global rules

**Write-on-discovery / file writing discipline (Dimension Review Section 6.2 — observed first in DimReview but also present in VC):**

Section 6.2 of Dimension Review (write-on-discovery principle stated as "absolute") is a direct restatement of GR-OBS-001. DUPLICATE.

In Verse Context, Section 6.4 (observations file write discipline):
- "Write to disk after every individual observation" — GR-OBS-001 equivalent. DUPLICATE.
- "Dual-write: working directory and /mnt/user-data/outputs/" — not explicitly in global rules but implied by programme practice. CANDIDATE for global rules.
- "Version-increment the observations log filename on every new write session" — this is GR-FILE-003/GR-FILE-004 applied to the observations log specifically. Consistent with global rules, not conflicting.

**Governance of OWNER/XREF distinction:**
Section 0.2 and 5.2 in VC define the OWNER/XREF term handling pattern — this matches GR-DATA-002 and GR-DATA-003 exactly. The detailed operational rules in VC go beyond what GR-DATA-002/003 cover and should remain in the instruction. No conflict.

**No sampling rule:**
VC Section 6.2 Step 2 all-verses-fail rule: "individual inspection is mandatory and non-waivable regardless of corpus size" — this directly matches GR-PROG-005. DUPLICATE (but appropriate to keep the operational detail in VC; the principle statement should reference GR-PROG-005 or be removed from inline prose).

**Borderline verses retained:**
Section 3.3: "retain (is_relevant = 1) and record the uncertainty in the notes field. The cost of a missed inclusion is higher than the cost of retaining an uncertain verse." — matches GR-PROG-004 exactly. DUPLICATE.

**Relevance filter at term level, not verse level:**
Section 3, warning box: "Apply the filter to the term's specific use in this verse — not to the verse's general theme." — this is an important methodological principle not currently in global rules. CANDIDATE for GR-PROG.

**Step-by-step (complete before moving on):**
Instruction line 1 of Section 6.2: "For each term — complete this sequence before moving to the next term." This is the same step-by-step discipline as Session B. CANDIDATE already identified.

**Filename convention:**
Section 6.4 (output file naming) uses the wa-vcb-{batch_id}-{scope}-{version}-{date}.{ext} pattern. Consistent with GR-FILE-001 structure — no conflict. The batch-specific scope (vcb-{batch_id}) is instruction-specific and should remain.

**Fix-or-stop principle (from Dimension Review, but also relevant here):**
VC does not explicitly state "fix-or-stop" but the partial completion rule (stop for structural data integrity failures) is related. DR has "fix-or-stop" as an explicit governing principle. CANDIDATE for global rules if agreed across all instructions.

#### Summary for Verse Context:
- DUPLICATES to remove (replace with reference): write-on-discovery, no sampling, borderline verses retained
- CANDIDATES to lift to global rules: dual-write discipline (/home/claude + /mnt/user-data/outputs/), filter at term level (not verse level)
- CONFLICTS: None

---

### 2.3 Dimension Review Instruction (v1.9)

#### Rules found that overlap with or duplicate global rules

**Write-on-discovery principle (Section 0 foundational principles):**
"Every analytical decision... is written to the observations log immediately on discovery. Nothing is accumulated in memory for later transcription." — exact duplicate of GR-OBS-001. DUPLICATE.

**Fix-or-stop principle (Section 0 foundational principles):**
"When a quality problem is identified, the Dimension Review follows whatever sub-process is necessary to fix it. If a fix cannot be completed within the Dimension Review session, the session stops and issues a formal return instruction. A group with an unresolved quality problem does not advance to Phase C." — not in global rules but has programme-wide applicability. CANDIDATE.

**All changes through patches (Section 1.6):**
"No corrections to group descriptions, dimension assignments, or any database field are made by direct database manipulation. Every change is encoded in a patch file, reviewed by the researcher, and applied by Claude Code." — DUPLICATE of the "all changes through patches" principle in Session B. CANDIDATE already identified for global rules.

**Dimensions are data-derived (Section 1.3, 1.1):**
Matches GR-PROG-002 exactly. DUPLICATE. Section 5.7 contains the operational vocabulary; GR-PROG-002 states the governing principle. The operational vocabulary list belongs in the instruction — the governing principle should reference GR-PROG-002.

**Cluster assignment is a processing unit:**
Not explicitly restated in the DR instruction but consistent with GR-PROG-003.

**Session log discipline (Section 6.3):**
DR states session logs must be produced at natural breakpoints. Matches Session B discipline. CANDIDATE already noted.

**Observations log governs (Section 6.2):**
"The observations log is the input to the patch session. The patch session does not perform analytical work..." — this does not directly duplicate GR-OBS rule but is related to the principle that the observations log is the primary analytical artefact. Consistent with Session B SB-6 (observations log governs over session log in conflict). CANDIDATE already noted.

**No pre-formed dimension categories imposed (Section 1.1):**
Matches GR-PROG-002 (dimensions are data-derived). DUPLICATE.

**Dual-write discipline (Section 6.2 file writing):**
"Dual-write: working directory (/home/claude/) and /mnt/user-data/outputs/" — same as Verse Context. CANDIDATE already noted.

#### Specific conflict identified:
DR Section 6.2 states observations log should be "version-incremented on every new write session for the same cluster." This is consistent with GR-FILE-003/004 (no overwrites, versioning). No conflict.

DR companion documents list references "WA-SessionB-Analysis-Instruction-v5.7" — but the current instruction is v4.7. This is a stale reference in the DR companion documents table, not a rule conflict. OBSERVATION: companion document references in DR are out of date (v5.7 does not exist; current is v4.7). FLAG for correction.

#### Summary for Dimension Review:
- DUPLICATES to remove: write-on-discovery, dimensions are data-derived / no imposition
- CANDIDATES to lift to global rules: fix-or-stop principle, all changes through patches (already noted)
- FLAG: Stale companion document reference (WA-SessionB-Analysis-Instruction-v5.7 should be v4.7)
- CONFLICTS: None

---

### 2.4 Global Session C Prose Rule (v1)

This is itself a global document, but it is a draft for incorporation into the Session C instruction. It references GR-OBS-006 which does NOT appear in the current global rules file. This is a forward reference — GR-OBS-006 is proposed but not yet defined in the rules file.

OBSERVATION: The prose rule file cites GR-OBS-006 as the rule being operationalised, but GR-OBS-006 does not exist in wa-global-general-rules-v1. This is a gap: the global rules file needs GR-OBS-006 added.

Content of GR-OBS-006 (inferred from prose rule document):
"Session C reader-facing prose must derive from (b) observations in the database. No new analytical claims may be introduced at the writing stage."

Also cites GR-PROG-006 (no superlatives without source) — this exists in global rules. Consistent.

#### Summary for Session C Prose Rule:
- Gap in global rules: GR-OBS-006 is referenced but not defined — needs to be added to the global rules file
- No conflicts with existing global rules

---

### 2.5 Pass-Close Procedure (global, v1)

This is a global document intended for incorporation into Session B. It references:
- GR-PASS-001 ✓ exists
- GR-PASS-002 ✓ exists
- GR-OBS-001 ✓ exists
- GR-OBS-002 ✓ exists
- GR-OBS-003 ✓ exists
- GR-OBS-005 ✓ referenced (obsolete marker, not deletion)
- GR-FILE-004 ✓ exists

No conflicts identified. This document operationalises existing global rules — it is correctly positioned as a procedure, not a rule file.

One observation: Section 8 ("Open items for incorporation into the Session B instruction") lists items needed in the next Session B revision. This is a programme action, not a rule issue.

---

### 2.6 Patch Specification (v1.10)

The patch specification is a technical reference document, not an instruction file governing analytical behaviour. It defines the patch format, applicator rules, and status workflow.

Rules relevant to global governance:

**"All changes through patches" principle:**
The entire document operationalises this principle. The principle is already a CANDIDATE for the global rules file. The operational patch format itself belongs in this document.

**"No patch without researcher review":**
Not explicitly stated in patch_specification but implied by the process (researcher reviews patches before Claude Code applies). This is Session B integrity rule SB-3 — already a CANDIDATE for global rules.

**Status management rules:**
The `session_b_status` workflow is programme-specific and belongs in this document. Consistent with Registry Management Guide.

No conflicts with global rules identified.

---

### 2.7 Registry Management Guide (v5.8)

Reference guide, not an operational instruction. Contains definitions and rules relevant to programme-wide understanding.

**One OWNER per Strong's number (Section 3a):**
Matches GR-DATA-002 exactly. No conflict.

**Engine-derived fields are Phase 1 only (Section 2):**
Not in global rules. CANDIDATE — this affects how any session reads registry fields. Programme-wide relevance.

**Runtime-computed fields in overview exports must check exported_date (Section 2a):**
Not in global rules. Procedural — probably instruction-specific rather than global.

No conflicts with global rules identified.

---

## Step 3 — Consolidated findings

### 3.1 Missing rules to add to global file

The following rules are either referenced in global documents but not defined, or are genuinely programme-wide rules currently only appearing in individual instructions:

| Proposed Rule ID | Content | Source | Priority |
|---|---|---|---|
| GR-OBS-006 | Session C prose derives from (b) observations only; no new analytical claims at writing stage | wa-global-sessionC-prose-rule-v1 (references it but doesn't define it) | HIGH — referenced but missing |
| GR-FILE-007 | Filenames are lowercase | Session B naming conventions | MEDIUM |
| GR-FILE-008 | Dual-write: all output files written to /home/claude/ (working) and /mnt/user-data/outputs/ (outputs) | VC Section 6.4, DR Section 6.2 | HIGH — appears in multiple instructions |
| GR-PROC-001 | Step-by-step: each step is completed and confirmed before the next begins | Session B governing disciplines, VC Section 6.2 | HIGH — fundamental programme discipline |
| GR-PROC-002 | Data is authoritative: all analysis grounded in the JSON/database only; no imported general knowledge to fill gaps | Session B governing disciplines | HIGH |
| GR-PROC-003 | All changes through patches: no database field is updated by assertion; all corrections are encoded in a patch reviewed and applied by Claude Code | Session B, DR Section 1.6 | HIGH — appears in multiple instructions |
| GR-PROC-004 | No patch is applied without researcher review | Session B SB-3 | HIGH |
| GR-PROC-005 | Observations log governs over session log in conflict (SB-6) | Session B integrity rule | MEDIUM |
| GR-PROC-006 | Session logs at every natural breakpoint | Session B, DR | MEDIUM |
| GR-PROC-007 | Fix-or-stop: when a quality problem is identified, the relevant sub-process is followed to fix it before advancing; a group/term/registry with an unresolved quality problem does not advance | DR Section 0 | MEDIUM |
| GR-PROG-007 | Filter at term level: the inner-being relevance filter is applied to the term's specific use in the verse, not to the verse's general theme | VC Section 3 warning box | HIGH |
| GR-PROG-008 | Emergence applies beyond dimensions: the spirit-soul-body classification, somatic signature, semantic picture, and connection characterisations must emerge from the evidence; no classification is assigned and evidence then selected to support it | Session B analytical principles | MEDIUM |
| GR-PROG-009 | Inferential is not confirmed: where a connection is theologically plausible but not supported by data, it is labelled inferential; it may not be upgraded to confirmed | Session B analytical principles | HIGH |
| GR-DATA-008 | Engine-derived Phase 1 fields (phase1_term_count, phase1_verse_count, unique_term_count, shared_term_count, term_sharing_ratio) are not updated by the Session B pipeline; live queries must be used for current counts | Registry Management Guide Section 2 | MEDIUM |

### 3.2 Duplicates to remove from instructions (replace with reference to global rule)

| Instruction | Inline text | Global rule | Action |
|---|---|---|---|
| Session B v4.7 (governing disciplines) | "Write on discovery" paragraph | GR-OBS-001 | Replace inline paragraph with: "Write on discovery — per GR-OBS-001 (non-waivable)." |
| Session B v4.7 (Pass 4, somatic_link note) | "Do NOT update wa_term_inventory.somatic_link — this is a redundant field per WA-Reference Section 13.3" | GR-DATA-005 | Replace with: "Do NOT update wa_term_inventory.somatic_link — redundant field per GR-DATA-005." |
| Dimension Review v1.9 (foundational principles) | Write-on-discovery principle paragraph | GR-OBS-001 | Replace with reference to GR-OBS-001. |
| Dimension Review v1.9 (Section 1.3 and 1.1) | "No dimension category is assumed correct before group content has been read; automated labels are a starting map, not a conclusion" | GR-PROG-002 | Replace with reference to GR-PROG-002. |
| Verse Context v2.5 (Section 3.3) | Borderline cases retention rule | GR-PROG-004 | Replace with reference to GR-PROG-004. |
| Verse Context v2.5 (Section 6.2 Step 2, all-verses-fail) | "individual inspection is mandatory and non-waivable regardless of corpus size" | GR-PROG-005 | Replace principle statement with reference to GR-PROG-005; keep operational procedure detail. |

### 3.3 Stale reference to correct

| Document | Stale reference | Correct reference |
|---|---|---|
| DimensionReview v1.9 companion documents | WA-SessionB-Analysis-Instruction-v5.7 | WA-SessionB-Instruction-v4.7 |

### 3.4 Conflicts (none identified)

No rule in any instruction file directly conflicts with the global rules. The global rules file states it is authoritative; no instruction contradicts this.

One reference inconsistency found: Session B cites WA-Reference Section 13.3 for somatic_link prohibition; the current programme-wide authority is GR-DATA-005. This is an inconsistency in citation, not a conflict in substance.

---

## Step 4 — Proposed updates

### Priority 1 (must do before work proceeds):

**4.1 Add GR-OBS-006 to global rules file**
GR-OBS-006 is referenced in wa-global-sessionC-prose-rule-v1 but is not defined anywhere. The global file is incomplete without it.

### Priority 2 (recommended before next Session B):

**4.2 Add GR-FILE-007 (lowercase filenames), GR-FILE-008 (dual-write)**
Both appear as practices in multiple instructions. Making them global prevents inconsistency.

**4.3 Add GR-PROC-001 through GR-PROC-007**
Programme-wide operational disciplines currently scattered across instructions.

**4.4 Add GR-PROG-007 (filter at term level), GR-PROG-008 (emergence beyond dimensions), GR-PROG-009 (inferential is not confirmed)**
These are analytical rules with programme-wide applicability.

### Priority 3 (at next instruction revision):

**4.5 Remove duplicates from Session B, Verse Context, Dimension Review**
Replace inline restatements of global rules with references. This reduces maintenance burden and prevents future divergence.

**4.6 Correct stale companion document reference in Dimension Review**
WA-SessionB-Analysis-Instruction-v5.7 → WA-SessionB-Instruction-v4.7.

---

## Open items requiring researcher decision

**OI-001 (HIGH):** GR-OBS-005 text is truncated in the global rules file view (line 150 onward not captured). Researcher should confirm the full text of GR-OBS-005 is correctly present in the file.

**OI-002 (MEDIUM):** Fix-or-stop principle (GR-PROC-007 candidate). This principle governs Dimension Review explicitly. The researcher should confirm: does this apply programme-wide (lift to global), or is it Dimension Review-specific?

**OI-003 (MEDIUM):** GR-PROC-006 (session logs at every natural breakpoint). This is stated in multiple instructions. The researcher should confirm it belongs in global rules, or whether the session log discipline is instruction-specific.

**OI-004 (LOW):** Dual-write path. The Dimension Review specifies /home/claude/ as the working directory. The pass-close procedure and Verse Context also reference /mnt/user-data/outputs/. Is /home/claude/ the correct working directory name for all sessions, or does it vary? Confirm before writing GR-FILE-008.

---

## Next steps

1. Researcher reviews this analysis and confirms candidates and open items.
2. Produce updated wa-global-general-rules-v2 (JSON) incorporating confirmed new rules.
3. Produce updated versions of each instruction file that: (a) reference the global file at the top; (b) remove duplicated rule text; (c) replace with references to relevant GR rule IDs.
4. Correct stale reference in Dimension Review.
5. Session log finalized and delivered for download.

---

## Session state

**Current stage:** Analysis complete — awaiting researcher confirmation of candidates and resolution of open items before producing updated files.
**Files read:** 7 instruction/global files (see scope above)
**Files NOT yet read:** WA-SessionD-Orientation, WA-SessionB-ClaudeCode-Instructions, WA-Reference, wa-word-study-template
**Next session action:** Researcher response → produce updated global rules v2 JSON + updated instruction files

