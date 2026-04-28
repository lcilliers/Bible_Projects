# WA Global Rules — Audit and Classification

**Filename:** wa-global-rules-audit-v1-20260417.md
**Version:** 1.0
**Date:** 2026-04-17
**Produced by:** Claude AI, conducted in chat session "Fellowship review consolidation and preamble drafting" (2026-04-17)
**Subject file audited:** wa-global-general-rules-v2_6-20260417.json (53 rules, 12 categories, plus preamble)
**Supporting references consulted:** wa-patch-specification-v1_14-20260416.md; WA-Reference-v5_5-20260330.md

**Previous output files in this session:**
- wa-global-general-rules-v2_6-20260417.json (the v2.6 rules file with preamble added)

**Purpose of this document:** To record the audit findings produced in session on 2026-04-17 so that the researcher can review them in a stable document rather than in chat. The audit examines the global rules file for ambiguity, conflict, scope limitation, and volume. It proposes a disposition for every one of the 53 rules. No rule has been moved. No file has been modified. This document is the basis for the researcher's decisions on what changes to approve.

---

## 1. Quantitative overview

### 1.1 Counts

| Metric | Value |
|---|---:|
| Total rules | 53 |
| Total rule text | 3,630 words |
| Average per rule | 68 words |
| Rules exceeding 100 words | 6 |
| Categories | 12 |

### 1.2 Distribution by category

| Category | Rule count |
|---|---:|
| programme_orientation | 9 |
| claude_code_directive | 8 |
| file_naming | 7 |
| observation_discipline | 6 |
| process_discipline | 6 |
| researcher_decision | 6 |
| data_discipline | 5 |
| pass_close | 2 |
| file_format | 1 |
| file_output | 1 |
| database_discipline | 1 |
| load_requirement | 1 |

### 1.3 Distribution by stated scope

| applies_to value | Rule count |
|---|---:|
| all sessions, all phases | 26 |
| all processing instructions | 9 |
| Session B, Session C, Session D instructions | 3 |
| Session B instruction | 3 |
| Session B, Dimension Review, Verse Context instructions | 2 |
| all sessions, all phases — any directive produced by Claude AI | 2 |
| all sessions, all instructions, all phases | 1 |
| Session B instruction, all somatic classification work | 1 |
| all sessions, all phases — any patch produced by Claude AI | 1 |
| Dimension Review, Session B instructions | 1 |
| Session B, Session C instructions | 1 |
| Verse Context, Session B instructions | 1 |
| Verse Context instruction, Session B Stage 1, all relevance filtering decisions | 1 |
| Session B, Session C, Session D, Dimension Review instructions | 1 |

### 1.4 Longest rules (candidates for relocation or compression)

| Rule ID | Word count | Subject |
|---|---:|---|
| GR-DIR-006 | 269 | Patch format self-check — mandatory before submission |
| GR-PROG-007 | 164 | Filter at term level — direct engagement or implication |
| GR-DIR-008 | 148 | Directive self-check — mandatory before submission |
| GR-DIR-001 | 140 | When to use a directive vs a patch — rule and distinction |
| GR-RD-001 | 136 | Researcher decision items — when they may be raised |
| GR-DB-001 | 115 | No DB state assumptions — always verify |

### 1.5 Interpretation

53 rules exceeds the number a human can hold in working memory. Realistic working memory for rules that must be applied conditionally is 10–15 items. The file is currently functioning as a *reference* rather than a *rulebook*: sessions consult it when reminded, rather than binding to it continuously. This is structurally why the rules are reported as ignored. A rule that cannot be recalled is not a rule; it is a reference entry.

---

## 2. Scope limitation findings

The file's own scope test (document.scope_test): *"A rule belongs in this file if it governs the programme's mechanics, conventions, processes, or data artefacts across more than one instruction or phase. A rule that only affects a single instruction and has no impact on any other phase remains in that instruction."*

Rules that appear to fail this test:

| Rule ID | Subject | Stated scope | Audit finding |
|---|---|---|---|
| GR-DATA-002 | Extract is authoritative for Session B | Session B instruction | Single instruction. Belongs in Session B. |
| GR-DATA-003 | mti_term_flags authoritative for somatic | Session B instruction, all somatic classification work | Somatic classification happens within Session B. Single instruction in effect. Alternatively belongs in WA-Reference Section 13. |
| GR-DATA-004 | Complete word data export version confirmation | Session B instruction | Single instruction. Belongs in Session B. |
| GR-DATA-005 | god_as_subject and somatic_link verification | Session B instruction | Single instruction. Belongs in Session B. |
| GR-DATA-001 | Active terms filter — SQL | all sessions, all phases | Scope statement is too broad. The filter is only relevant where mti_terms queries are issued — Session B, Verse Context, Dimension Review analytical work. Belongs in WA-Reference Section 13.2 (mti_terms schema). |
| GR-PROG-003 | Dimensions are data-derived | Dimension Review, Session B | Two-instruction. Borderline by letter of the test. |
| GR-PROG-004 | Session C primary, Session B deepens | Session B, Session C | Two-instruction. Borderline. |
| GR-PROG-006 | Characteristic-perspective grouping | Verse Context, Session B | Two-instruction. Mostly Verse Context. |
| GR-PROG-007 | Term-level relevance filter (164 words) | Verse Context, Session B Stage 1, all relevance filtering decisions | Two-instruction. 164 words. Heaviest where it is used (Verse Context). |

---

## 3. Redundancy findings

Rules that restate the same discipline in different words.

### 3.1 Write-on-discovery / observations-log-governs — three rules say it three times

- **GR-OBS-001:** *"Every finding … is written to the observations log at the moment it is determined."*
- **GR-PROC-005:** *"The observations log is the authoritative record … if something is not in the observations log, it has not been done."*
- **GR-PASS-002:** *"Claude AI writes all analytical workings to the observations log continuously within a pass (per GR-OBS-001)."*

These are three restatements of one principle: *the log is the record; if it is not there, it did not happen; write as you go.* GR-OBS-001 is the authoritative formulation.

**Proposed merge:** Retain GR-OBS-001 (cover log as record, write-on-discovery, memory not authoritative). Delete GR-PROC-005 (fully subsumed). Delete GR-PASS-002 (the pass-close write-to-database point is separable — see disposition for GR-PASS-002 below).

### 3.2 Two-AI role separation — two rules say it

- **GR-PROG-005:** *"Claude AI handles all analysis, interpretation, and document production. Claude Code handles all database operations … These roles are strictly separated."*
- **GR-DIR-004:** *"Claude AI determines what should be done and why … Claude Code determines how to execute it and executes it."*

Identical principle, two rules. Risk: future edits drift apart, creating a conflict.

**Proposed merge:** Retain GR-PROG-005 (universal statement). Fold GR-DIR-004's directive-specific wording into GR-DIR-001 (which already discusses the boundary).

### 3.3 Evidence-to-finding traceability — two rules

- **GR-PROC-002:** *"Every analytical finding must be traceable to a specific verse record, term entry, lexical source, correlation signal, or extract field in the current working data. Findings not traceable to a data source are not findings — they are hypotheses."*
- **GR-PROG-008:** *"All analytical outputs must emerge from the verse evidence … No classification is assigned in advance and evidence then selected to support it."*

Close but not identical. GR-PROC-002 is about traceability (every finding must cite its source). GR-PROG-008 is about direction of inference (evidence to finding, not the reverse). Both have value.

**Proposed disposition:** Retain both, but tighten both to prevent confusion. GR-PROC-002 = traceability. GR-PROG-008 = emergence (no back-fitting).

### 3.4 Patch and directive self-checks — two enormous checklists

- **GR-DIR-006** (269 words) — six-point patch self-check.
- **GR-DIR-008** (148 words) — five-point directive self-check.

These are operational checklists, not rules. Their length alone signals they are in the wrong place. The patch specification already has a Section 7 ("Producing Patches — Guidelines for Claude.ai") that is their natural home. The directive equivalent has no home; see Complication 2 below.

**Proposed disposition:**
- GR-DIR-006 → move to wa-patch-specification Section 7 (expanding the 10-item guideline into 10 + 6-point self-check). Retain in global rules a single sentence: *"Before presenting any patch, Claude AI must pass the patch self-check defined in wa-patch-specification Section 7."*
- GR-DIR-008 → retain in global rules for now; no directive specification document exists.

---

## 4. Ambiguity findings

### 4.1 Serious (require resolution before the file can stabilise)

**A5 — GR-OBS-004 contradicts Dimension Review v1.9.**
FLAG-002 in the rules file already records this. GR-OBS-004 states version increment at named session boundaries; DR v1.9 Section 6.2 states increment on every new write session. Unresolved for three days.

**A7 — GR-DIR-001 patch-vs-directive test rests on AI self-assessment.**
*"A patch is used when Claude AI is certain of the field names, FK keys, table structure, and exact operations required … A directive is used when Claude AI knows the outcome required but is not certain of the exact execution path."* The test is self-reported certainty. A session that feels certain but is wrong produces a patch that fails. The preamble specifically identifies this failure mode as the reason the preamble exists.

Proposed objective test: *use a patch when the operation uses only tables and fields explicitly named in the patch specification Section 3 (Supported Operation Types); use a directive otherwise.*

### 4.2 Tidy-up (cosmetic but worth fixing in the same cycle)

| Item | Rule | Issue |
|---|---|---|
| A1 | GR-FILE-003 | Rule says major.minor; filename examples elsewhere show v1, v2 (major only). Does a filename use v1 or v1.0? Settled in practice as v1, not stated in rule. |
| A2 | GR-FILE-005 | Contains a permission clause (docx may be converted to markdown) mixed with a format rule. Unclear whether the converted markdown or the original docx is then the "final deliverable" for GR-FILE-004 (no-overwrites) purposes. |
| A3 | GR-OBS-002 | Category (d) "Session action" is a catch-all with five example types. An observation that fits none cleanly has no procedure — should it be category (d), or raised as a researcher decision? |
| A4 | GR-PROC-001 vs preamble | GR-PROC-001 prohibits step skipping; preamble states analytical freedom is unrationed. Resolution exists (procedural steps are governed; analytical scope is not), but must be inferred. |
| A6 | GR-PROG-002 | "Divine characteristics are retained as reference material … but are not the programme's primary subject." Ambiguous — retained from what, at what priority? Session D genuinely handles divine material. |

---

## 5. Conflict findings

| Ref | Rules in conflict | Description | Status |
|---|---|---|---|
| C1 | GR-OBS-004 vs DR v1.9 §6.2 | Named-boundary vs every-save version increment | Already flagged as FLAG-002; unresolved 3 days |
| C2 | GR-FILE-004 (no overwrites) vs GR-FILE-008 (dual-write) | Neither rule addresses whether the second destination in a dual-write counts as a separate save requiring its own version; GR-OBS-004 adds a special case for logs | Silent conflict; needs clarifying sentence in GR-FILE-008 |
| C3 | GR-DIR-004 vs GR-PROG-005 | Duplication, not conflict, but future drift risk | Merge proposed (see 3.2) |
| C4 | GR-RD-003 (decision block) vs GR-RD-002 (6-element format) at scale | At 15+ decision items (conceivable for Registry 103 'love' with 120+ Q&A pairs), the decision block becomes 1,500+ words | Latent scaling problem; no immediate action needed |

---

## 6. Complete classification table — proposed disposition for all 53 rules

**Legend:**
- **KEEP** — remains in global rules as-is or with light edit
- **KEEP (merge)** — remains but absorbs another rule
- **MOVE → WA-Reference** — relocated to WA-Reference-v5_5 (target section specified)
- **MOVE → Patch spec** — relocated to wa-patch-specification Section 7 or similar
- **ADDENDUM** — placed in a new `addendum` key at the back of the global rules file, awaiting migration to the relevant instruction document

| Rule ID | Subject | Proposed disposition | Target location if moving | Notes |
|---|---|---|---|---|
| GR-LOAD-001 | Mandatory global rules load | KEEP | — | The gate. Top of file. |
| GR-FILE-001 | Filename structure | KEEP | — | Master pattern. |
| GR-FILE-002 | Short description ≤30 chars | KEEP | — | Atomic. |
| GR-FILE-003 | Version numbering major.minor | KEEP (clarify filename uses major only) | — | See A1. |
| GR-FILE-004 | No overwrites — new versioned file | KEEP | — | — |
| GR-FILE-005 | Output format by purpose | KEEP (separate permission clause) | — | See A2. |
| GR-FILE-006 | Prefix and reference conventions | KEEP | — | — |
| GR-FILE-007 | Lowercase filenames | KEEP | — | — |
| GR-FILE-008 | Dual-write discipline | KEEP (add clarifying sentence) | — | See C2. |
| GR-FILE-009 | Compact date YYYYMMDD | KEEP | — | — |
| GR-PASS-001 | Pass-close download | ADDENDUM | Target: Session B, Session C, Session D instructions | Pass-level; not all phases have passes. |
| GR-PASS-002 | Write-on-discovery at pass close | ADDENDUM | Target: Session B, Session C, Session D instructions | Subsumed analytically by GR-OBS-001; pass-close write-to-db is specific. |
| GR-OBS-001 | Write-on-discovery — non-waivable | KEEP (merge: absorb GR-PROC-005) | — | Load-bearing. |
| GR-OBS-002 | Obs log classification categories | ADDENDUM | Target: Session B, Dimension Review, Verse Context instructions | See A3. |
| GR-OBS-003 | Session log vs observations log | KEEP | — | Universal distinction. |
| GR-OBS-004 | Version increment at named boundaries | KEEP (resolve FLAG-002 conflict) | — | See C1. |
| GR-OBS-005 | No physical deletion — flag only | KEEP | — | Data integrity universal. |
| GR-OBS-006 | All observations return to database | KEEP | — | Universal. |
| GR-PROC-001 | Step-by-step completion | KEEP (clarify vs preamble) | — | See A4. |
| GR-PROC-002 | Findings traceable to source | KEEP | — | See 3.3 — kept distinct from GR-PROG-008. |
| GR-PROC-003 | All DB changes via patch/directive | KEEP | — | Universal. |
| GR-PROC-004 | No patch/directive without review | KEEP | — | Universal. |
| GR-PROC-005 | Obs log governs, not memory | MERGED INTO GR-OBS-001 | — | See 3.1. |
| GR-PROC-006 | Session logs at breakpoints | KEEP | — | Universal. |
| GR-DATA-001 | Active terms SQL filter | MOVE → WA-Reference | Section 13.2 (mti_terms schema) | Schema-specific. |
| GR-DATA-002 | Extract authoritative for Session B | ADDENDUM | Target: Session B instruction | — |
| GR-DATA-003 | mti_term_flags authoritative for somatic | MOVE → WA-Reference | Section 13.2 or 15.4 | Schema field authority. |
| GR-DATA-004 | Export version confirmation | ADDENDUM | Target: Session B instruction | — |
| GR-DATA-005 | god_as_subject/somatic_link verification | ADDENDUM | Target: Session B instruction | — |
| GR-DB-001 | No DB state assumptions | KEEP | — | Universal. |
| GR-DIR-001 | Patch vs directive choice | KEEP (revise test per A7) | — | See A7. |
| GR-DIR-002 | Directive format — 5 elements | KEEP | — | No directive-spec document exists. |
| GR-DIR-003 | Patch format per patch spec | KEEP (pure pointer) | — | Could be compressed to a single sentence; remains in global as a pointer. |
| GR-DIR-004 | CC executes, AI decides | MERGED INTO GR-PROG-005 and GR-DIR-001 | — | See 3.2. |
| GR-DIR-005 | Completion confirmation mandatory | KEEP | — | Universal. |
| GR-DIR-006 | Patch format self-check (269w) | MOVE → Patch spec | Section 7 | Operational checklist. See 3.4. |
| GR-DIR-007 | Directive filename convention | KEEP | — | No directive spec. |
| GR-DIR-008 | Directive self-check (148w) | KEEP | — | No directive spec. See 3.4. |
| GR-RD-001 | When to raise a researcher decision | KEEP | — | Universal. |
| GR-RD-002 | Researcher decision item format | KEEP | — | Universal. |
| GR-RD-003 | Decision items not embedded in analysis | KEEP | — | Universal. |
| GR-RD-004 | Resolution produces concrete outcome | KEEP | — | Universal. |
| GR-RD-005 | Same question may not be raised twice | KEEP | — | Universal. |
| GR-RD-006 | Decision items do not accumulate | KEEP | — | Universal. |
| GR-PROG-001 | Verse always leads | KEEP | — | Universal principle. |
| GR-PROG-002 | Governing question | KEEP (clarify A6) | — | See A6. |
| GR-PROG-003 | Dimensions are data-derived | ADDENDUM | Target: Dimension Review, Session B instructions | Two-instruction. |
| GR-PROG-004 | Session C primary, Session B deepens | ADDENDUM | Target: Session B, Session C instructions | Two-instruction. |
| GR-PROG-005 | Two-AI role separation | KEEP (absorb GR-DIR-004) | — | Universal. |
| GR-PROG-006 | Characteristic-perspective grouping | ADDENDUM | Target: Verse Context instruction primarily | Verse Context construct. |
| GR-PROG-007 | Term-level relevance filter (164w) | ADDENDUM | Target: Verse Context instruction | The filter rule. Heaviest where used. |
| GR-PROG-008 | Emergence — classifications from evidence | KEEP | — | See 3.3. |
| GR-PROG-009 | Inferential is not confirmed | KEEP | — | Universal. |

### 6.1 Projected counts after proposed dispositions

| State | Rule count in global |
|---|---:|
| Current (v2.6) | 53 |
| After MOVEs (to WA-Reference and patch spec) | 50 |
| After MERGES (2 merges: PROC-005 into OBS-001; DIR-004 into PROG-005) | 48 |
| After ADDENDUM extraction (10 rules moved to addendum block) | 38 in main rules section + 10 in addendum |

Addendum rules are visibly separate from main rules. A session reading the file sees the main rules as the active binding set; the addendum is marked as *pending migration to instructions*.

---

## 7. Material complications

### 7.1 Complication 1 — WA-Reference Section 1 is stale

WA-Reference-v5_5 Section 1 (File Naming Conventions) shows patterns that predate the current GR-FILE rules:
- Pattern `wa-{nnn}-{word}-{scope}-{YYYYMMDD}.{ext}` — omits the version component required by GR-FILE-001 and GR-FILE-003.
- Instruction document names in Section 1.3 use capital "WA-" prefix; GR-FILE-007 requires all lowercase.
- Patch ID Convention in Section 1.4 uses `PATCH-...V{n}` (uppercase, capital V); current practice is lowercase.

**Impact on this audit:** Moving GR-DATA-001 and GR-DATA-003 to WA-Reference places content into a document that already contradicts the current file-naming rules. A session reading WA-Reference for the active-terms filter is also reading stale file-naming guidance in the same document.

**Options:**
- (a) Update WA-Reference Section 1 in the same cycle as these moves (produce WA-Reference v5.6).
- (b) Add a note in the global rules that GR-FILE-001 through GR-FILE-009 are authoritative over WA-Reference Section 1 until the reference is updated.
- (c) Pause all moves into WA-Reference until WA-Reference is updated.

### 7.2 Complication 2 — No directive specification document exists

GR-DIR-002 (directive format), GR-DIR-007 (directive filename), and GR-DIR-008 (directive self-check) have no natural reference-doc home. The CC instructions document (`wa-sessionb-cc-instructions-v3_6`) is Session-B scoped by name; directives apply across all phases.

**Options:**
- (a) Keep GR-DIR-002, GR-DIR-007, GR-DIR-008 in global rules for now. Revisit when a directive specification is drafted.
- (b) Create `wa-directive-specification-v1-YYYYMMDD.md` alongside the patch specification as a peer document.

Recommendation from audit: (a). Directive rules are not growing fast enough to justify a new specification document at present.

---

## 8. Open questions requiring researcher decision

Four decisions are required before any rule is moved:

**Q1 — Rule-by-rule approval.** The classification table in Section 6 proposes dispositions for all 53 rules. The researcher reviews this table and objects to any disposition they disagree with, by rule ID. No rule will be moved without explicit approval of its disposition.

**Q2 — Complication 1 (stale WA-Reference Section 1).** Choose (a), (b), or (c) as listed in Section 7.1.

**Q3 — Complication 2 (directive rules without a reference home).** Choose (a) keep in global, or (b) create a directive specification. Audit recommends (a).

**Q4 — Addendum structure.** Proposed structure: a new top-level key `addendum` at the end of the JSON file, containing the addendum rules with their original text unchanged plus two new fields per rule: `migration_target` (naming the instruction(s) where the rule needs to land) and `migration_status` (pending | confirmed-covered | migrated). The addendum is reviewed at intervals; when all items are confirmed-covered, the addendum is emptied and a version increment records the completion. Confirm or propose alternative.

---

## 9. Audit disposition summary

- 33 rules KEEP in main rules section (unchanged or lightly revised)
- 2 merges within the kept set (GR-PROC-005 into GR-OBS-001; GR-DIR-004 absorbed by GR-PROG-005 and GR-DIR-001)
- 3 rules MOVE to reference documents (GR-DATA-001 and GR-DATA-003 to WA-Reference; GR-DIR-006 to patch specification)
- 10 rules ADDENDUM (pending migration to stage-specific instructions)
- 7 ambiguity and conflict items requiring revision text

Expected outcome if all dispositions are approved: the main rules section of the global rules file drops from 53 rules to approximately 38 rules, with 10 more in a visibly-separate addendum. The file becomes readable as a rulebook rather than a reference.

---

## 10. What this audit is NOT

This audit does not modify any file. No rule has been moved, deleted, or merged. No reference document has been updated. This document is the basis for the researcher's decisions. Execution of any change happens only after the four open questions in Section 8 are answered.

---

*End of audit — wa-global-rules-audit-v1-20260417.md*
