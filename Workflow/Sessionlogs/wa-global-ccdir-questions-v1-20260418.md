# wa-global-ccdir-questions-v1-20260418

> Questions and clarifications for researcher review
> Companion to: four-document consolidation drafted 2026-04-18
> Session log: wa-global-ccdir-consolidation-obslog-v1-20260418.md

---

Per your instruction *"list all the questions and clarifications together with clear references to where I can find detail. Where you are confident about your judgement, you do not need to ask. Highlight things you do not agree with, where intent is unclear and you cannot figure out what it should be."*

Questions grouped by type. Each has a specific reference to where you can see the detail.

---

## Q1 — Version number for Claude Code instruction: v3_3 vs v3_7

**Where:** wa-claudecode-instruction-v3_3-20260418.md — Change Control section, third paragraph.

**Question:** You specified `v3_3` in the commission. The existing document is `v3_6`. A version bump from v3_6 should normally go to v3_7 (minor) or v4_0 (major) per GR-FILE-003. Going to v3_3 goes backwards in the version series.

**Options I see:**
- **(a)** Accept v3_3 as you specified — treat as a deliberate re-baselining of the v3.x lineage. This is what I have drafted.
- **(b)** Change to v3_7 — minor increment continuing v3_6's lineage, which matches the GR-FILE-003 convention.
- **(c)** Change to v4_0 — major increment, on the argument that this is a substantial restructure with content moved to other documents.

**My judgement:** (c) is the cleanest. The content is materially different from v3_6 — three major sections removed, the document's scope redefined, pointer discipline applied throughout. That is a rewrite, not a minor update. I have drafted v3_3 as instructed but flag this for your decision.

---

## Q2 — Session B instruction status — placeholder references in the patch and reference documents

**Where:** wa-patch-instruction-v2_0-20260418.md §3.2 and Appendix A.3; wa-reference-v5_6-20260418.md §12 Patch Index.

**Context:** FLAG-003 in the global flags records that Session B v4.7 has been retired, to be replaced by Analysis_readiness + Analysis_output. Neither replacement instruction exists yet.

**What I did:** Patch and reference documents cite "wa-sessionb-analysis-readiness (when finalised)" and "wa-sessionb-analysis-output (when finalised)" as the governing documents for PREANALYSIS and SESSIONB patch types.

**Question:** Do you want me to (a) leave these placeholder references as-is until Analysis_readiness and Analysis_output are drafted, or (b) temporarily cite the retired wa-sessionb-instruction v4.8 until the replacements exist?

**My judgement:** (a) is honest about the current state. A user reading the patch instruction in the current state and looking for "wa-sessionb-analysis-readiness" will not find it, but the "(when finalised)" annotation signals the gap. Citing a retired document would be misleading. Not worth redrafting either document over this; flagging for awareness.

---

## Q3 — ClaudeCode filename casing

**Where:** wa-claudecode-instruction-v3_3-20260418.md — filename on disk, and §O-042/O-044 of the session observations log.

**What I did:** You wrote "wa-ClaudeCode-Instruction" with mixed case. GR-FILE-007 requires fully lowercase. I normalised to `wa-claudecode-instruction-v3_3-20260418.md`.

**Not asking for approval** (this is a GR-FILE-007 compliance requirement, not a judgement call). Flagging so you are not surprised by the filename. If you intended the mixed-case form, GR-FILE-007 would need an exception — but this is a filename convention you wrote yourself in v2_10 last turn, so I assume this was a typo.

---

## Q4 — Addendum items NOT absorbed in this batch

**Where:** wa-global-general-rules-v2_10-20260418.json addenda arrays; my O-042 absorption plan.

**What I have absorbed:**
- ADD-REF-001 → wa-reference v5_6 §13.2
- ADD-REF-002 → wa-reference v5_6 §13.2
- ADD-REF-003 → resolved by producing v5_6 with GR-FILE compliance
- ADD-PATCHDIR-001 → wa-patch-instruction v2_0 §7
- ADD-PATCHDIR-002 → resolved by producing wa-directive-instruction v1_0
- ADD-PATCHDIR-003 → wa-directive-instruction v1_0 §7
- ADD-PATCHDIR-004 → wa-patch-instruction v2_0 §5.4
- ADD-PATCHDIR-005 → wa-patch-instruction v2_0 §1 and wa-directive-instruction v1_0 §1
- ADD-PATCHDIR-006 → wa-directive-instruction v1_0 §3
- ADD-PATCHDIR-007 → wa-patch-instruction v2_0 §1
- ADD-PATCHDIR-008 → wa-patch-instruction v2_0 §6 and wa-directive-instruction v1_0 §6
- ADD-PATCHDIR-009 → wa-directive-instruction v1_0 §2

**What I have NOT absorbed (and why):**
- ADD-INSTR-001 (GR-PASS-001 pass-close) — targets Session B/C/D instructions which are being rewritten separately; out of scope for this batch.
- ADD-INSTR-002 (GR-PASS-002) — already absorbed into GR-OBS-001 per its obsolete_reason; no action.
- ADD-INSTR-004 through ADD-INSTR-009 (Session B / DR / VC rules) — target specific stage instructions (DR, Analysis_readiness, Analysis_output, VC) which are being rewritten separately.
- ADD-INSTR-010 (GR-PROG-007 relevance filter) — targets VC instruction.
- ADD-INSTR-011 (GR-OBS-006 obs persist to DB) — targets Analysis_output.

**My judgement:** correct scoping. The instruction-addendum items target stage-specific instructions (VC, DR, Analysis_readiness, Analysis_output) and would be addressed when those instructions are next produced or updated. Touching them now would mean reaching into documents that are out of scope for this commission.

**Question:** Do you agree, or would you like me to absorb any of these into the four documents produced this turn?

---

## Q5 — Global rules v2_11 — timing of the addendum cleanup

**Where:** wa-global-general-rules-v2_10-20260418.json addenda; my absorption record in Q4.

**What happens next (not done yet):** Now that the addendum items listed in Q4 have been absorbed into the four documents, the corresponding addendum entries in the global rules should be marked as resolved and removed. This produces wa-global-general-rules-v2_11-20260418.json.

**Question:** Should I produce v2_11 as part of this batch, or wait until you have reviewed the four new documents?

**My judgement:** wait. If you change any of the absorbed content in the four documents, the v2_11 cleanup would need to be redone. Producing v2_11 after your review is cleaner. But flagging for your call.

---

## Q6 — wa-patch-instruction — "SD_POINTERS" versus "SESSIONB" patch_type

**Where:** wa-patch-instruction-v2_0-20260418.md §3.3 (Valid patch_type values).

**Context:** The v1_14 patch spec (v1_10 change note) noted that SDPOINTERS patches carry `session_b_status: null` but the applicator rejects null for non-VERSECONTEXT/VCGROUP/VCVERSE types. My draft lists the valid patch types as: PREANALYSIS | SESSIONB | VERSECONTEXT | VCGROUP | VCVERSE | SESSIOND | CLUSTERING | REPAIR. No SDPOINTERS.

**Question:** Was SDPOINTERS ever a formally-supported patch_type, or is it a term of art for patches that *contain* SD_POINTER flag inserts (which would be a SESSIONB patch)? The v1_10 note implied SDPOINTERS was a patch_type in use. My draft treats SESSIONB as the covering type and leaves SDPOINTERS out.

**My judgement:** SD_POINTER is a flag_code (inside wa_session_research_flags), not a patch_type. Patches containing SD_POINTER inserts are SESSIONB patches. I think the v1_10 "SDPOINTERS" note was ambiguous phrasing, not a statement of a formal patch_type. If I'm wrong, SDPOINTERS needs adding to §3.3 and §3.4 with its valid session_b_status.

---

## Q7 — New category `document_discipline` — only one rule

**Where:** wa-global-general-rules-v2_10-20260418.json — GR-REF-001 introduced `document_discipline` as a new category.

**Context:** The category has only one rule. Usually categories with one rule argue for folding into an existing category.

**What I did:** Introduced the new category anyway, on the argument that future rules about document structure, referencing, and authority would naturally sit here.

**Not asking** — specialist authorship call, already committed. Flagging for awareness in case you disagree.

---

## Q8 — Reference document — what happens to the Chapter Structure language from Framework B?

**Where:** Not in the four documents. Observed in the Framework_B_Spirit_Soul_Body.pdf that is in the project.

**Context:** The Framework B PDF contains a proposed chapter structure, methodology, and gap analysis. It is a planning document rather than an operating instruction. It is not referenced in any of the four documents I produced.

**Not a question I need answered to proceed** — the PDF is in the project as context, not as a document to be absorbed. Flagging for completeness since you mentioned taking source documents into account.

---

## Q9 — Global flags file reference currency

**Where:** wa-global-general-rules-v2_10-20260418.json — `flags_file` block already points to `wa-global-flags-v1_2-20260418.md`.

**Not a question** — this was done when the flags file was updated last turn. Reconfirmed in this batch. Noting for completeness.

---

## Q10 — Session D orientation reference in patch and reference documents

**Where:** wa-patch-instruction-v2_0-20260418.md Appendix A.3; wa-reference-v5_6-20260418.md §12.

**What I did:** Cited "wa-sessiond-orientation v3_0" as the governing document for SESSIOND patches.

**Context:** I am inferring the filename from FLAG-006 which mentions "Session D Orientation v3.0". I have not seen the actual file.

**Question:** Is the current Session D document `wa-sessiond-orientation-v3_0-{YYYYMMDD}.md` (compliant with GR-FILE), or is it still in a pre-GR-FILE filename form? FLAG-006 notes that Session D naming needs GR-FILE alignment. If the current filename is different, the citations in the patch and reference documents need updating.

**My judgement:** leave as drafted; the citation is correct in principle and will be refined when FLAG-006 is resolved.

---

## Things I have NOT asked about — specialist authorship calls made

Per GR-HF-001 specialist-authorship clause, these are recorded for audit rather than raised as questions:

1. **Document ordering:** reference first, patch second, directive third, CC last (production order). Authority flows from reference.
2. **Section numbering in each document:** chosen for readability.
3. **Pointer phrasing:** "per wa-reference v5_6 §13.2" and similar — versioned per GR-REF-001 Discipline 2.
4. **Inline vs appendix placement** — templates and JSON examples inline where they aid reading, appendix where they are reference material.
5. **Removed content that was historical noise** — v3_6 CC instructions §0 "Document Sources" removed (archaeology, not instruction); v3_6 §3 historical tasks moved to Appendix A; v3_6 §6.6 re-integrated into §5 where it belonged.
6. **Cross-references between the four documents** — each cites the others by name, version, and section where appropriate.
7. **The "how to" structure in wa-directive-instruction §5** (step-by-step production workflow) — new content, not absorbed from existing document. Added because directives need it and patches have equivalent in wa-patch-instruction §3–§7.
8. **Retention of wa-patch-instruction §11** (operations not supported by applicator) — kept because it is still operationally relevant.
9. **Wa-reference §18** (Document Preparation and Validation Standard) — retained largely as-is; only §18.5 updated to point to wa-patch-instruction for failure path.
10. **Absence of a §0 "Document sources" in each new document** — the change-control note carries the lineage; a separate sources section is duplication.

---

## Summary

Three questions with real decisions attached:

- **Q1** — version number v3_3 vs v3_7 vs v4_0 for ClaudeCode instruction
- **Q5** — when to produce global rules v2_11 (before or after your review of these four documents)
- **Q10** — Session D instruction filename currency

Seven items flagged for awareness only, where I have made the judgement call and committed to it:

- Q2 placeholder references for Analysis_readiness/Analysis_output
- Q3 lowercase filename normalisation
- Q4 addendum items deliberately not absorbed
- Q6 SDPOINTERS treated as SESSIONB, not separate patch_type
- Q7 new `document_discipline` category with one rule
- Q8 Framework B PDF not absorbed
- Q9 flags_file reference currency

---

## Researcher responses and actions taken — 2026-04-18

Responses received in the chat turn following production of this document. Actions taken to reflect the responses are recorded here.

### Q1 — Version number for CC instruction
**Decision:** Accept recommendation (c) — v4_0 major bump. Researcher confirmed v3_3 was a typo.
**Action taken:**
- Renamed `wa-claudecode-instruction-v3_3-20260418.md` → `wa-claudecode-instruction-v4_0-20260418.md`
- Updated internal version references: title line, header Version field, Change Control section header, footer line, version-number rationale paragraph rewritten to reflect the major bump
- Updated cross-references in `wa-reference-v5_6-20260418.md` and `wa-patch-instruction-v2_0-20260418.md` (directive instruction had no v3_3 reference)
- Removed superseded `wa-claudecode-instruction-v3_3-20260418.md` from outputs

### Q2 — Placeholder references and new current-version rule
**Decision:** Leave the "(when finalised)" placeholders in patch and reference documents. Add a new GR rule applying to all instructions that when a document references another document, it should reference the `[current]` version rather than a specific version. Add a flag for a cross-instruction reference cleanup sweep.
**Action taken:**
- Added new rule **GR-REF-002** to the `document_discipline` category in `wa-global-general-rules-v2_11-20260418.json`. The rule establishes the `[current]` reference convention for operational cross-references in the instruction corpus. Specific versions remain appropriate for provenance references (Supersedes, observation logs, patch `_patch_meta.produced_by`).
- Produced `wa-global-flags-v1_3-20260418.md` with **FLAG-012** — cross-instruction reference cleanup sweep, sequenced to run after FLAG-013.
- Placeholders for Analysis_readiness / Analysis_output left as-is in the patch and reference documents, to be resolved in the FLAG-012 sweep.

### Q3 — Lowercase filename
**Decision:** Accept — GR-FILE-007 compliance required.
**Action taken:** Filename was already lowercase in the v3_3 draft; v4_0 renamed filename also lowercase. No additional action needed.

### Q4 — Addendum items not absorbed
**Decision:** Agree with all. INSTR-series addenda out of scope for this batch.
**Action taken:** None required.

### Q5 — Global rules v2_11 timing
**Decision:** Wait on the full addendum cleanup until researcher has reviewed the five documents.
**Action taken:** v2_11 produced with **only** the Q2 rule addition (GR-REF-002). Addendum cleanup remains deferred to v2_12. Sequencing recorded in v2_11 change note.

### Q6 — SD_pointers vs SESSIONB patch_type
**Decision:** Leave as-is for now. Researcher clarified SD_pointers and SessionB pointers are different datatypes. Will review in detailed pass.
**Action taken:** None required. My Q6 judgement overridden — preserving for future revision.

### Q7 — New `document_discipline` category
**Decision:** Accept. Flag that the next global rules revision should review classification completeness. Classification review runs **before** the reference cleanup sweep (Q2).
**Action taken:** Added **FLAG-013** to `wa-global-flags-v1_3-20260418.md` — document_discipline category classification review, gating FLAG-012.

### Q8 — Framework B PDF
**Decision:** Original study, superseded by current programme. May be rewritten later. No action in the four documents.
**Action taken:** None required.

### Q9 — Session D reference currency
**Decision:** Session D has anchors in the current phase via SD pointers generated through patches. Specification correct.
**Action taken:** None required.

### All specialist authorship calls
**Decision:** Accepted — no changes required.
**Action taken:** None required.

---

## Files updated in this action pass

1. `wa-global-general-rules-v2_11-20260418.json` — new rule GR-REF-002 added to document_discipline category
2. `wa-global-flags-v1_3-20260418.md` — FLAG-012 and FLAG-013 added (13 flags total)
3. `wa-claudecode-instruction-v4_0-20260418.md` — renamed from v3_3, internal version references updated, footer updated, Governed-by reference updated to v2_11
4. `wa-reference-v5_6-20260418.md` — cross-reference to CC instruction updated to v4_0, Governed-by and scope pointer updated to v2_11
5. `wa-patch-instruction-v2_0-20260418.md` — cross-reference to CC instruction updated to v4_0, Governed-by and one operational citation updated to v2_11 (footer provenance citation to v2_10 preserved)
6. `wa-directive-instruction-v1_0-20260418.md` — cross-reference to CC instruction updated to v4_0, Governed-by and all operational citations updated to v2_11

## Pending / deferred

- **Global rules v2_12** — addendum cleanup (removal of absorbed ADD-REF-001/002/003 and ADD-PATCHDIR-001/-002/-003/-004/-005/-006/-007/-008/-009). Deferred per Q5 until researcher accepts the five-document set.
- **FLAG-013 resolution** — document_discipline category classification review (before FLAG-012).
- **FLAG-012 resolution** — cross-instruction reference cleanup sweep replacing specific versions with `[current]` across the instruction corpus (after FLAG-013).
- **FLAG-011 resolution** — retirement of `wa-sessionb-cc-instructions-v3_6-20260416.md` once replacement set is accepted.

---

*Questions document closed.*
