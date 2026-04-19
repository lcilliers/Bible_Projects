# Analysis — CC/CAI Interaction Protocols Across Four Documents

**Filename:** wa-global-ccdir-analysis-v1-20260418.md
**Date:** 2026-04-18
**Prefix:** WA
**Previous output reference:** wa-global-ccdir-consolidation-obslog-v1-20260418.md (session obs log)

## Scope of this analysis

The researcher has asked for analysis of the three documents governing CC/CAI interaction protocols, with a fourth added in this turn:

1. `WA-SessionB-ClaudeCode-Instructions-v3_2-20260330.md` — earlier CC instruction set (added this turn)
2. `wa-sessionb-cc-instructions-v3_6-20260416.md` — current CC instruction set
3. `wa-patch-specification-v1_14-20260416.md` — patch format specification
4. `WA-Reference-v5_5-20260330.md` — controlled vocabulary, naming, schema

The analysis is structured against the six notes the researcher attached to the task:

- **N1** Well-trodden path — no need to re-invent methods
- **N2** Flag duplication and conflicts
- **N3** CC instructions have got out of hand — combination of actual instructions and general conduct — retire with replacement flag
- **N4** CC instructions were drafted by Claude Code as its own understanding of its role
- **N5** Only two methods for CAI → CC: patches and directives; feedback from CC must be specified in these documents
- **N6** CC instructions, interaction protocol, and programme-wide references/lookup must be kept as separate but inter-related documents

---

## 1. Observation on the two CC instruction files (N3 + N4 context)

### 1.1 Relationship between v3_2 and v3_6

The two files are the same lineage. v3.2 was produced 2026-03-30; v3.6 is the current 2026-04-16 version. The v3.6 change note confirms it supersedes v3.5, which itself supersedes v3.4, v3.3, v3.2, v3.1 in date order. Content is progressively refined, not restructured.

### 1.2 Content inventory of v3_6 (authoritative current version)

Breaking v3_6 into its actual content types — this is the "got out of hand" observation made concrete:

| Section | Type of content | Arguably belongs to |
|---|---|---|
| Governing Rules (top table) | CC-role application of global rules | CC instructions |
| §0 Document Sources | History/provenance note | CC instructions |
| §1 Role — Boundary Definition | **Interaction protocol** (what CC is and is not) | Interaction protocol |
| §2 Data Foundation (2.1–2.7) | **Actual CC operations** (register, extract, audit, export) | CC instructions |
| §3 Implementation Tasks (Tasks 1–8) | **Actual CC operations** (schema DDL) — mostly complete historical record | CC instructions |
| §4 Patch Application | **Interaction protocol** (what CC does on receiving a patch) + feedback specs | Interaction protocol (+ patch spec) |
| §5 JSON Export | **Actual CC operations** (post-patch re-export) | CC instructions |
| §6 Programme State Queries | **Actual CC operations** (SQL templates) | CC instructions |
| §7 File Naming Conventions | **Programme-wide reference** — duplicates WA-Reference §1 | WA-Reference |
| §8 Controlled Vocabulary | **Programme-wide reference** — duplicates WA-Reference §2, §3, §3a, §10 | WA-Reference |
| §9 Known Recurring Anomalies | **Interaction protocol** (how CC resolves specific situations) | Interaction protocol |
| §10 Interaction Protocol with Claude AI | **Interaction protocol** (explicit) | Interaction protocol |
| §11 Periodic Review Support | **Actual CC operations** + trigger specification | CC instructions |
| §12 Engine and Script Status | **Operational state** — historical record | CC instructions |
| §13 Schema Additions (13.1–13.6) | **Programme-wide reference** — duplicates WA-Reference §13 | WA-Reference |
| §6.6 Verse Context Monitoring (out of sequence) | **Actual CC operations** (SQL templates) | CC instructions |
| §14 Verse Context Operations | **Actual CC operations** + interaction protocol for VC patches | CC instructions + interaction protocol |
| §15 REPAIR Patch Catalogue | **Actual CC operations** (cascade reset specifications) | CC instructions |
| §16 Failure Patch | **Actual CC operations** + interaction protocol (when to produce) | CC instructions + interaction protocol |

Summary of what this table shows:
- **Actual CC operations** (what CC does and how): 8 sections
- **Interaction protocol** (how CC and CAI exchange): 5 sections (some mixed)
- **Programme-wide reference** (vocabulary, naming, schema): 3 sections, all duplicating WA-Reference
- **Operational history** (document sources, engine status): 2 sections

The researcher's diagnosis in N3 is confirmed: the document mixes actual instructions, interaction protocol, and reference content, with significant duplication of WA-Reference.

### 1.3 Origin pattern — N4 context

The researcher notes in N4 that CC instructions were drafted by Claude Code. This shows in two specific patterns in the text:

- **Accumulation without pruning.** Content is added when new work arises (§13 "post-v5 housekeeping" bolted on at the end; §6.6 "Verse Context Stage Monitoring" appears out of sequence between §13 and §14; §15 and §16 are clearly additions rather than integrations). A structured editor would have re-sectioned.
- **Self-referential provenance blocks.** §0 Document Sources reads as a record of what the writer extracted from other documents. It is useful archaeology but it is not an instruction.

Neither of these patterns is wrong in itself — they reflect an organic accretion — but together they produce a document that is hard to read as an instruction and easy to read as a scrapbook.

---

## 2. Duplication and conflict map (N2)

### 2.1 Duplication — content appearing in more than one document

| Topic | CC instructions v3_6 | Patch spec v1_14 | WA-Reference v5_5 |
|---|---|---|---|
| File naming pattern (word-level) | §7.1 | §1 (patch filenames) | §1.1 |
| Patch filename convention | §7.3 (two-identifier table) | §1 | §1.4 |
| Patch ID format (internal vs filename) | §7.3 (distinguished cleanly) | §2 (distinguished cleanly) | §1.4 (does NOT distinguish — stale) |
| `mti_terms.status` vocabulary | §8.1 | Appendix A.4 | §2 |
| `session_b_status` vocabulary | §8.2 | Appendix A.5/A.6 | §3 |
| `verse_context_status` vocabulary | §8.2a | Appendix A.7 | §3a |
| `evidential_status` vocabulary | §8.3 | — | §10 |
| SB_FINDING / SD_POINTER etc. flag codes | §8.4 | — | §5.1 |
| Patch types (controlled vocabulary) | §8.5 | Appendix A.6 + §0.1 | §12 |
| Patch index (governing instruction → patch type) | — | §0.1 | §12 |
| Schema — word_registry columns | §13.1 | — | §13.1 |
| Schema — wa_term_inventory columns | §13.2 | — | §13.3 |
| Schema — wa_verse_records columns | §13.3 | — | §13.6 |
| Housekeeping rules (delete_flagged, CONCRETE_PHYSICAL) | §13.4, §13.5 | — | §13.4 referred; §15 |
| REPAIR patch catalogue | §15 | §3.12 (table + pointer to CC) | — |
| Failure patch | §16 | — | §18.5 (minimum required content) |
| Verse Context patch operations | §14 | §8 | — |
| VC consistency rules (R1–R4) | §14.3 | §8.5 | — |

**Pattern:** the CC instructions duplicate WA-Reference substantially (vocabulary and schema). The patch spec and CC instructions duplicate each other on patch format details but mostly with clean pointer relationships (CC §15 is authoritative for REPAIR specifications; patch spec §3.12 points to it). WA-Reference has its own patch index (§12) that overlaps with the patch spec's patch index (§0.1).

### 2.2 Conflicts — same content, different values or rules

This is the more consequential layer. Where duplication has drifted into contradiction:

**C1. Patch filename convention — WA-Reference §1 is stale**
WA-Reference §1.1 shows the pattern `wa-{nnn}-{word}-{scope}-{YYYYMMDD}.{ext}` — no version component. GR-FILE-001 and GR-FILE-003 require a version component. CC instructions §7.3 and patch spec §1 both correctly include the version. WA-Reference is out of step. This is already flagged in global rules addendum ADD-REF-003.

**C2. Patch ID format capitalisation**
WA-Reference §1.4 shows `PATCH-...V{n}` and does not distinguish this from the filename. Patch spec v1_14 and CC instructions v3_6 both now cleanly distinguish: the internal `patch_id` field retains uppercase `PATCH-...` for applicator compatibility; the filename is lowercase `wa-...-patch-...`. WA-Reference §1.4 needs updating to match, or an explicit note that §1.4 shows the internal field only.

**C3. Governing instruction references in WA-Reference §12**
WA-Reference §12 Patch Index cites governing documents that do not match current state:
- PREANALYSIS → "WA-SessionB-DataPrep-Instruction" — CC instructions v3_6 §0 records DataPrep as retired, superseded by WA-SessionB-Instruction-v4.8 and WA-VerseContext-Instruction-v2.6.
- SESSIONB → "WA-SessionB-Extraction-Instruction" — same retirement status.
- VERSECONTEXT / VCGROUP / VCVERSE → "WA-VerseContext-Instruction-v1" — current version per CC instructions §14 is v2.7.
Patch spec v1_14 §0.1 carries updated governing document references (Session B v4.8, VC v2.7). WA-Reference §12 has not been refreshed.

**C4. Session B v4.7/v4.8/retirement — three positions in one programme**
- WA-Reference §12 cites "WA-SessionB-Extraction-Instruction" as the governing document for SESSIONB patches.
- Patch spec §0.1 cites "wa-sessionb-instruction v4.8" as the governing document.
- Flags file FLAG-003 records that Session B v4.7 is retired and being split into Analysis_readiness + Analysis_output. When that happens, both the above references will become stale.
This is a live in-flight situation; it is not a fault of any one document but it means any consolidation must be aware of it.

**C5. File naming — `wa-sessionb-cc-instructions` scope token is stale**
The filename declares itself a Session B instruction. The content is programme-wide (CC operations across all phases). With Session B v4.7 retired, the filename is doubly stale. Retirement is flagged below in §3.

**C6. Pool vs cluster language**
CC instructions v3_6 §14.8 says *"the pool architecture has been retired (see Registry Management Guide v5.9 Section 5.2). Session B now operates on individual words in cluster order."* But later on the same page in §15.4 it refers to *"re-assemble pool analysis dataset"*. The earlier v3_2 §14 (Verse Context) uses "pool" throughout. The retirement note in v3_6 was added in a late revision but the downstream uses were not purged. Minor but indicative of the accumulation pattern noted in §1.3.

**C7. Engine schema version string**
CC instructions v3_6 §12 says *"Schema at v3.8.0 (migrations M01–M18 complete)"* and *"constants.py | Schema version 3.7.0"*. Internal contradiction: 3.8.0 and 3.7.0 cannot both be right. v3_2 has the same contradiction. This is a CC-internal matter (may be a deliberate state of "constants lags schema") but it is presented without explanation.

**C8. WA-Reference §14 is a stub**
WA-Reference §14 says *"Templates unchanged from v5.2. See v5.2 for full JSON templates."* This creates a reference dependency on a superseded document. Should either be inlined or explicitly point to where the templates now live.

---

## 3. Retirement of the CC instructions document (N3)

### 3.1 What the researcher asked for

> "This instruction need to be retired, but it is referenced in many other places. We need to add a flag about its retirement, and what replaces it."

### 3.2 Where the CC instructions document is referenced

References to the CC instructions document found in the attached materials:

- **Global rules v2_9** — addendum ADD-PATCHDIR-002 cites it: *"The CC instructions document (wa-sessionb-cc-instructions-v3_6) is Session-B scoped by name; directives apply across all phases."*
- **Patch spec v1_14** — §0.1 does not cite it directly, but §3.10 cites "WA-SessionB-Extraction-Instruction-v5.3 Section 6.1" and §3.12 cites "wa-sessionb-cc-instructions-v3_3-20260414.md Section 15–16". The v3_3 reference is stale (current is v3_6).
- **Patch spec v1_14** — change notes reference v3.3, v3.4 etc.
- **WA-Reference v5_5** — §18.5 *"see WA-SessionB-ClaudeCode-Instructions Section 16"* — uses an older filename form (capitalised, hyphens).
- **Global flags v1_1** — FLAG-005 and FLAG-010 both reference it (FLAG-005 records v3.3 as the current update; FLAG-010 lists "CC Instructions v3.3" as in scope for audit).

So the CC instructions document is referenced by: global rules, patch spec, WA-Reference, and global flags. Any retirement must propagate to all four.

### 3.3 What replaces it — observation, not decision

The researcher has stated the structure in N6:
> "Claude code instructions guidance, interaction protocol, and program wide references and lookup must be kept as separate, but inter related documents."

This names three distinct documents:
1. **Claude Code instructions/guidance** — what CC does operationally (register, extract, audit, export, apply patches, run state queries, produce REPAIR patches)
2. **Interaction protocol** — how CC and CAI exchange (the two methods, the feedback required, the role boundaries)
3. **Programme-wide reference/lookup** — controlled vocabulary, naming conventions, schema (this is WA-Reference's existing role)

The CC instructions document is currently all three of these mixed together. Retirement means splitting its content into the three natural homes.

**I am not proposing specific structure beyond this naming.** That is the main consolidation task we have not yet begun.

### 3.4 Draft flag entry for the global flags file

For researcher review. Not yet applied.

> **FLAG-011 — WA-SessionB-ClaudeCode-Instructions to be retired — REPLACED**
>
> - **Status:** Open — pending consolidation
> - **Raised:** 2026-04-18
> - **Description:** The document currently named `wa-sessionb-cc-instructions-v3_6-20260416.md` (lineage from v3.0 through v3.6) is to be retired. The document contains three distinct content types that belong in separate documents per the researcher's structural direction: (a) Claude Code instructions and operational guidance, (b) interaction protocol between CAI and CC, (c) programme-wide references and lookup. The current document mixes all three and duplicates WA-Reference in its vocabulary and schema sections. The filename is also stale: the "sessionb" scope token does not match the document's programme-wide content, and will be further mismatched when Session B v4.7 is retired per FLAG-003.
> - **Replacement:** Three documents (filenames to be confirmed in consolidation work):
>   - `wa-cc-instructions-v1_0-{YYYYMMDD}.md` — Claude Code operational instructions: register, extract, audit, export, apply patches, run state queries, produce REPAIR patches
>   - `wa-cc-cai-interaction-v1_0-{YYYYMMDD}.md` — interaction protocol: the two methods (patches and directives), feedback requirements, role boundaries, handoff formats
>   - `WA-Reference` (existing) — absorbs any vocabulary, naming, and schema content from the retired document that is not already present
> - **References to update on retirement:** global rules v2_9 (addendum ADD-PATCHDIR-002, ADD-INSTR items that cite the CC instructions); patch spec v1_14 (§3.12 references Section 15–16; §3.10 reference; change notes); WA-Reference v5_5 (§18.5); global flags v1_1 (FLAG-005 and FLAG-010 both reference the document).
> - **Action needed:** (1) Produce the three replacement documents. (2) Update all references in the four documents above. (3) Mark `wa-sessionb-cc-instructions-v3_6` as superseded with a pointer to the new document set. (4) Resolve this flag once all references are updated.
> - **Relationship to FLAG-010:** FLAG-010 is a programme-wide audit of instructions against GR v2_8. This flag is a specific retirement-and-replacement within that audit scope. The work on this flag contributes to resolving FLAG-010 for the CC instructions entry.

---

## 4. CAI → CC methods and feedback specification (N5)

### 4.1 The two methods, as stated across the documents

The two methods are consistently named across global rules and patch spec:

- **Patches** — JSON format, governed by `wa-patch-specification-v1_14`
- **Directives** — plain language, five required elements (ID, motivation, scope, outcome, confirmation)

The patch method has a dedicated specification document. **The directive method does not.**

Global rules v2_9 addendum ADD-PATCHDIR-002 records this explicitly:
> "Three rules govern directive format, filename, and self-check. They are not patch rules. No peer specification for directives exists. The CC instructions document (wa-sessionb-cc-instructions-v3_6) is Session-B scoped by name; directives apply across all phases."

The options recorded in the addendum: (a) retain directive rules in global rules; (b) create `wa-directive-specification` as a peer to the patch specification.

The researcher's direction in N5 adds weight to option (b): if *"only two methods... are acceptable, and the feedback required from CC must be specified in these documents"* (plural), that implies two specification documents — one for each method.

### 4.2 Feedback specification — current state

#### 4.2.1 In the patch specification (v1_14)
- **§3.10 `update_evidential_status`** — describes what the operation does but does not specify the CC confirmation output.
- **§5 Validation Rules** — lists pre-application validation (what CC rejects) but not post-application confirmation.
- **§6 Post-Application Behaviour** — "On success: patch_id logged to engine_run_log, patch file moved to archive/patches/. On failure: full rollback, patch file remains in place." This is CC behaviour, not the confirmation format returned to CAI.
- **GR-DIR-005 (migrated to addendum ADD-PATCHDIR-008)** — *"Every patch and every directive must specify the completion confirmation that Claude Code must return to close the operation. The confirmation is a specific query result, row count, or field state check — not a general acknowledgement."*

So the global rules (via the addendum) say feedback must be specified, but the patch specification does not itself carry a template or standard for what that feedback looks like per patch type.

#### 4.2.2 In the CC instructions v3_6
- **§4.1 "Handoff format received from Claude AI"** — shows the handoff format but not the feedback format.
- **§4.1 step 6** — "Confirm completion." One word.
- **§4.2** — same pattern. "Confirm session_b_status updated in word_registry. Confirm flag records inserted in wa_session_research_flags." This is closer to specification but still narrative, not structured.
- **§14 Verse Context** — describes consistency checks (§14.3) and integrity checks (§14.4, §14.7) that CC runs, but does not say *these results are the feedback to CAI*.

#### 4.2.3 Gap diagnosis
The programme has stated the rule (feedback must be specified — GR-DIR-005), but neither document carries the operational implementation. Every patch type and every directive type should have a defined feedback template. Currently:

- Patch spec has the patch format but not the feedback format.
- CC instructions have some feedback language but scattered and non-uniform across patch types.
- No directive specification exists, so no directive feedback format exists.

This is a specific gap that a consolidation must close. The researcher's N5 names exactly this gap.

### 4.3 What the two method specifications should contain (observation, not draft)

Extracted from the six notes and the documents:

Each of the two method-specification documents (patch spec, directive spec) would need to carry, per method/operation type:

- Purpose — what the method is used for
- Who produces it — CAI
- Who applies it — CC
- Format — JSON structure for patches; plain-language structure for directives
- Pre-application validation — what CC checks before executing
- Application behaviour — what CC does
- **Feedback required from CC** — the specific query result, row count, or state check returned to CAI and the researcher
- Rejection handling — what CC does if validation fails

The patch spec already has most of these but is not consistent on feedback (per §4.2.1 above). The directive spec does not exist yet.

---

## 5. Well-trodden path (N1) — what exists that should not be re-invented

N1 says: "the methods and contents is a well trodden path — there is no need to re-invent new methods."

What is well-established and must be preserved through any consolidation:

### 5.1 The two-method model
Patches and directives. Established across all four documents. Any consolidation must keep these as the only two methods. No third method introduced.

### 5.2 The role boundary
CC instructions §1 names it: CC is the database engine; CAI does analysis and judgement. Global rules GR-PROG-005 is the authoritative statement. Repeated in CC instructions §1, §10. Patch spec §7 item 4 *"Use `update_mti_status`... — this is the workhorse operation"*. This is settled architecture.

### 5.3 The patch format
Patch spec v1_14 is a mature document. Three top-level keys, operation types enumerated, validation rules stated, idempotency via patch_id, applicator behaviour documented. This format does not need redesigning.

### 5.4 The status workflow
Verse Context → DataPrep → Analysis → Extraction, with session_b_status values. Patch spec §0 and §0.1 carry this; CC instructions §8.2 repeats it; WA-Reference §3 carries it. The model is stable; what varies is which document is authoritative for which part.

### 5.5 The REPAIR patch concept
Cascade resets for each pipeline re-run scenario. CC instructions §15 specifies four REPAIR patches; patch spec §3.12 refers to them. This is an established pattern.

### 5.6 The failure patch concept
CC instructions §16; WA-Reference §18.5 minimum required content. This is an established pattern.

### 5.7 The flag-ownership boundary
CC instructions §2.4 — *"Category A engine-derivable flags... Category B term-level analytical flags... Category C session research flags... Engine never touches B or C."* This is settled.

Summary: the methods, role boundaries, patch format, status workflow, REPAIR pattern, failure pattern, and flag-ownership rules are all well-established. Consolidation is about **where they are documented**, not about changing how they work.

---

## 6. Separate but inter-related documents (N6) — structural observation

The researcher named three document types in N6:

1. **CC instructions / guidance** — operational (what CC does, how it does it)
2. **Interaction protocol** — governance of exchange (methods, feedback, role)
3. **Programme-wide references and lookup** — shared reference material (vocabulary, naming, schema)

### 6.1 Inter-relationships observable in the current material

| Relationship | Currently expressed as | Observation |
|---|---|---|
| CC instructions cite reference material | §7, §8, §13 of CC instructions duplicate WA-Reference | Should be pointer references, not duplicates |
| CC instructions cite interaction protocol | §1, §10, §14 sections of CC instructions are interaction protocol | Should be in a separate interaction protocol document |
| Interaction protocol cites patch format | Currently absent as separate doc — patch spec stands alone | Interaction protocol would cite patch spec and directive spec |
| Global rules cite all three | GR-PROG-005, GR-DIR-001..008 (now in addendum) | Global rules remain the authority layer above all three |

### 6.2 The fourth document — patch specification

The patch spec is already a peer reference in the existing structure. It is cited by CC instructions (§7.3, §15), by WA-Reference (§12), and by global rules. It is not part of the three-document set the researcher named because it is method-specific (one of the two methods). Per N5, a directive specification would be its peer.

So the full document set after retirement looks like this (observational, not a design proposal):

| Layer | Document | Role |
|---|---|---|
| Authority | Global rules | Programme-wide binding rules |
| Authority | Global flags | Open issues, resolved items |
| Method specification | Patch specification | JSON patch format + applicator rules |
| Method specification | Directive specification (new) | Plain-language directive format + CC receipt rules |
| Interaction protocol | CC/CAI interaction document (new) | How CAI gives instructions to CC, how CC responds, feedback templates |
| Operational instruction | CC instructions (new) | What CC does and how: register, extract, audit, export, apply, query, REPAIR, failure |
| Reference | WA-Reference | Controlled vocabulary, naming, schema |

Any content from `wa-sessionb-cc-instructions-v3_6` must land in one of the top five of these (it cannot go into global rules, global flags, or WA-Reference wholesale).

### 6.3 What each document would NOT contain

Stated as boundaries to resist the accumulation pattern (N3, N4):

- **CC instructions** does not contain vocabulary, naming, or schema. Points to WA-Reference.
- **CC/CAI interaction** does not contain patch JSON structure. Points to patch spec.
- **CC/CAI interaction** does not contain directive format. Points to directive spec.
- **Patch spec** does not contain CC operational routines (what CC does after applying). Points to CC instructions.
- **Directive spec** does not contain CC operational routines. Points to CC instructions.
- **WA-Reference** does not contain operational instruction or interaction protocol. Holds only vocabulary, naming, schema.

---

## 7. Summary — what this analysis has established

1. The two CC instruction files are one lineage; v3_6 is current.
2. The CC instructions document mixes three distinct content types (operations, interaction, reference) and duplicates WA-Reference substantially.
3. Significant duplications identified (table in §2.1); eight named conflicts (C1–C8 in §2.2), most of which are staleness rather than contradiction in intent.
4. The document's retirement is appropriate. Draft flag `FLAG-011` prepared for researcher review (§3.4).
5. Directive specification does not exist; patch specification exists but feedback format is incomplete per method. Both gaps confirmed by the material.
6. The well-trodden methods, role boundaries, and patterns do not need redesign — only rehousing.
7. The three-document structure the researcher named (operations / interaction / reference), with the patch spec and directive spec as method peers, is consistent with the existing material's natural seams.

---

## 8. Holding

No rules applied. No consolidation work started. This is analysis only, per researcher's instruction to "analyse the three files... and note the following".

**One-line flag per GR-HF-001 judgement edge:** C4 (Session B v4.7 retirement) and C3 (stale governing document references) are live issues already flagged elsewhere (FLAG-003, ADD-REF-003). They should be resolved together with this consolidation rather than piecemeal.

Waiting for direction on next step.

---

*End of analysis — 2026-04-18. Previous output: wa-global-ccdir-consolidation-obslog-v1-20260418.md.*
