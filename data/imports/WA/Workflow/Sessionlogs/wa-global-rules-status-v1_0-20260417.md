# WA Global Rules — Status Overview

**Filename:** wa-global-rules-status-v1_0-20260417.md
**Version:** v1_0
**Date:** 2026-04-17
**Subject file:** wa-global-general-rules-v2_9-20260417.json (32 active rules, 23 obsolete retained for audit)
**Prior outputs referenced:** wa-global-rules-audit-v1-20260417.md; wa-global-general-rules-v2_6 / v2_7 / v2_8 / v2_9; wa-global-flags-v1_0 / v1_1; wa-global-preamble-obslog-v1-20260417; wa-global-rules-v2_7-obslog-v1-20260417

**Purpose:** Give the researcher a single-page view of the global rules state after four consecutive minor-version consolidations (v2_6 → v2_9) on 2026-04-17. Identifies what changed, what the active rule set now contains, and what remains to be addressed.

---

## 1. Consolidation journey on 2026-04-17

Starting point: `wa-global-general-rules-v2_5-20260416.json` (53 rules, no preamble).

| Version | Purpose | Outcome |
|---|---|---|
| v2_6 | Add preamble — custodianship framing and three failure mechanisms | 53 rules retained; preamble added; 9 flags standing |
| v2_7 | Add three addendums for migration candidates | 53 rules retained; 15 items placed in three addendums pending dedicated review |
| v2_8 | First consolidation batch | 45 active rules (6 absorbed, 3 migrated, 1 new); 18 addendum items; flags migrated to standalone file |
| v2_9 | Second consolidation batch | 32 active rules (8 retired, 6 migrated, 1 new); 22 addendum items |

Net change in active rule count: 53 → 32. Reduction of 40%. Working-memory load dropped from reference-document weight to rulebook weight.

## 2. Active rules inventory

Total active rules: 32. Distributed across 12 categories.

### Load Requirement (1 rule)

| Rule ID | Version | Subject |
|---|---|---|
| GR-LOAD-001 | 2_1 | Mandatory global rules load at every session start |

### Cadence Discipline (1 rule)

| Rule ID | Version | Subject |
|---|---|---|
| GR-CAD-001 | 1_0 | Write-cadence self-check and present-files milestone |

### File Naming (6 rules)

| Rule ID | Version | Subject |
|---|---|---|
| GR-FILE-001 | 2.0 | Filename structure |
| GR-FILE-002 | 1.0 | Short description length |
| GR-FILE-003 | 3_0 | Version numbering — underscored v[major]_[minor] everywhere, always both components |
| GR-FILE-006 | 1.0 | Prefix and reference conventions |
| GR-FILE-007 | 2.0 | Lowercase filenames |
| GR-FILE-009 | 2.0 | Compact date format in filenames |

### File Format (1 rule)

| Rule ID | Version | Subject |
|---|---|---|
| GR-FILE-005 | 2_0 | Output format by purpose |

### File Output (1 rule)

| Rule ID | Version | Subject |
|---|---|---|
| GR-FILE-008 | 2.0 | Dual-write discipline |

### Observation Discipline (3 rules)

| Rule ID | Version | Subject |
|---|---|---|
| GR-OBS-001 | 2_0 | Observations log — continuous write, log authoritative, pass-close persistence |
| GR-OBS-003 | 2_0 | Observations log vs session log — separate files, different purposes; session log mandatory at close |
| GR-OBS-004 | 2.0 | Observations log version increment at named boundaries |

### Pass Close (1 rule)

| Rule ID | Version | Subject |
|---|---|---|
| GR-PASS-001 | 1.0 | Pass-close download before next pass begins |

### Process Discipline (3 rules)

| Rule ID | Version | Subject |
|---|---|---|
| GR-PROC-001 | 2_0 | Step completion requires validated output existence |
| GR-PROC-002 | 2_0 | Findings rooted in data — traceability required; hypotheses must be supported to become findings |
| GR-PROC-004 | 2.0 | No patch or directive applied without researcher review |

### Data Discipline (5 rules)

| Rule ID | Version | Subject |
|---|---|---|
| GR-DATA-001 | 2.0 | Active terms filter — mandatory for all mti_terms queries |
| GR-DATA-002 | 2.0 | Extract is authoritative for Session B — not prior session outputs |
| GR-DATA-003 | 2.0 | mti_term_flags authoritative field for somatic classification |
| GR-DATA-004 | 2.0 | Complete word data export carries a version number — confirm before proceeding |
| GR-DATA-005 | 2.0 | god_as_subject and somatic_link fields — verify before setting |

### Database Discipline (1 rule)

| Rule ID | Version | Subject |
|---|---|---|
| GR-DB-001 | 1.0 | No DB state assumptions — always verify |

### Researcher Decision (1 rule)

| Rule ID | Version | Subject |
|---|---|---|
| GR-RD-007 | 1_0 | Researcher feedback process — obs log as detail carrier, chat as alert, follow-up recorded |

### Programme Orientation (8 rules)

| Rule ID | Version | Subject |
|---|---|---|
| GR-PROG-001 | 2.0 | Verse always leads |
| GR-PROG-002 | 2_0 | Programme governing question — human inner being (spirit, soul, body) |
| GR-PROG-003 | 2.0 | Dimensions are data-derived |
| GR-PROG-004 | 2.0 | Session C is primary — Session B deepens it |
| GR-PROG-005 | 2_0 | Two-AI division of responsibility — Claude AI decides, Claude Code executes; patches and directives as sole DB-change mechanisms |
| GR-PROG-006 | 2.0 | Characteristic-perspective grouping model |
| GR-PROG-007 | 2.1 | Filter at term level — direct engagement or implication in an inner-being characteristic |
| GR-PROG-009 | 2.0 | Inferential is not confirmed — label accurately |

## 3. Obsolete rules retained for audit

Total obsolete entries: 23. Retained in the array with `obsolete: true` and a `superseded_by` or `migrated_to` pointer. No rule is ever physically deleted.

| Rule ID | Retired date | Superseded by / Migrated to |
|---|---|---|
| GR-DIR-001 | 20260417 | addendum_patch_directive ADD-PATCHDIR-005 |
| GR-DIR-002 | 20260417 | addendum_patch_directive ADD-PATCHDIR-006 |
| GR-DIR-003 | 20260417 | addendum_patch_directive ADD-PATCHDIR-007 |
| GR-DIR-004 | 20260417 | GR-PROG-005 |
| GR-DIR-005 | 20260417 | addendum_patch_directive ADD-PATCHDIR-008 |
| GR-DIR-006 | 20260417 | addendum_patch_directive ADD-PATCHDIR-001 |
| GR-DIR-007 | 20260417 | addendum_patch_directive ADD-PATCHDIR-009 |
| GR-DIR-008 | 20260417 | addendum_patch_directive ADD-PATCHDIR-003 |
| GR-FILE-004 | 20260417 | GR-FILE-003 v3_0 and GR-OBS-004 |
| GR-OBS-002 | 20260417 | GR-OBS-001 v2_0 and GR-OBS-003 v2_0 |
| GR-OBS-005 | 20260417 | addendum_patch_directive ADD-PATCHDIR-004 |
| GR-OBS-006 | 20260417 | addendum_instructions ADD-INSTR-011 |
| GR-PASS-002 | 20260417 | GR-OBS-001 |
| GR-PROC-003 | 20260417 | GR-PROG-005 |
| GR-PROC-005 | 20260417 | GR-OBS-001 |
| GR-PROC-006 | 20260417 | GR-OBS-003 |
| GR-PROG-008 | 20260417 | GR-PROC-002 |
| GR-RD-001 | 20260417 | GR-RD-007 v1_0 |
| GR-RD-002 | 20260417 | GR-RD-007 v1_0 |
| GR-RD-003 | 20260417 | GR-RD-007 v1_0 |
| GR-RD-004 | 20260417 | GR-RD-007 v1_0 |
| GR-RD-005 | 20260417 | GR-RD-007 v1_0 |
| GR-RD-006 | 20260417 | GR-RD-007 v1_0 |

## 4. Addendum items pending dedicated review

Addendum items hold content for dedicated review sessions. Each item carries a `researcher_comment` node (empty until populated) and a `migration_status` field.

### Addendum Instructions (10 items)

| Item ID | Rule / origin | Subject |
|---|---|---|
| ADD-INSTR-001 | GR-PASS-001 | Pass-close download — all internal outputs made available for download at end of pass |
| ADD-INSTR-002 | GR-PASS-002 | Within-pass write discipline — workings to obs log continuously; pass-close write to database |
| ADD-INSTR-004 | GR-DATA-002 | Extract is authoritative for Session B analysis |
| ADD-INSTR-005 | GR-DATA-004 | Complete word data export — version confirmation at session start |
| ADD-INSTR-006 | GR-DATA-005 | god_as_subject and somatic_link verification against verse evidence |
| ADD-INSTR-007 | GR-PROG-003 | Dimensions are data-derived — grounded in at least one verse |
| ADD-INSTR-008 | GR-PROG-004 | Session C primary; Session B deepens and corrects |
| ADD-INSTR-009 | GR-PROG-006 | Characteristic-perspective grouping model — groups describe what a verse is about, not what a term does |
| ADD-INSTR-010 | GR-PROG-007 | Inner-being relevance filter — term-level two-condition formulation (164 words) |
| ADD-INSTR-011 | GR-OBS-006 | Observations persist to database before session close — Session C/D read from DB only |

### Addendum Patch Directive (9 items)

| Item ID | Rule / origin | Subject |
|---|---|---|
| ADD-PATCHDIR-001 | GR-DIR-006 | Patch format self-check — six-point mandatory check (269 words) |
| ADD-PATCHDIR-002 | audit finding | No directive specification document exists — GR-DIR-002, GR-DIR-007, GR-DIR-008 have no natural reference home |
| ADD-PATCHDIR-003 | GR-DIR-008 | Directive self-check — five-point check before submission (148 words) |
| ADD-PATCHDIR-004 | GR-OBS-005 | No physical database deletion — delete_flagged pattern |
| ADD-PATCHDIR-005 | GR-DIR-001 | When to use a patch vs a directive |
| ADD-PATCHDIR-006 | GR-DIR-002 | Directive format — five required elements |
| ADD-PATCHDIR-007 | GR-DIR-003 | Patch format per patch specification (pointer rule) |
| ADD-PATCHDIR-008 | GR-DIR-005 | Completion confirmation mandatory for every patch and directive |
| ADD-PATCHDIR-009 | GR-DIR-007 | Directive filename convention |

### Addendum Reference (3 items)

| Item ID | Rule / origin | Subject |
|---|---|---|
| ADD-REF-001 | GR-DATA-001 | Active terms SQL filter — AND mt.status IN ('extracted', 'extracted_thin') |
| ADD-REF-002 | GR-DATA-003 | mti_term_flags is authoritative for somatic classification (not wa_term_inventory.somatic_link) |
| ADD-REF-003 | audit finding | WA-Reference §1 (File Naming Conventions) is stale against current GR-FILE rules |

## 5. Flags state (from wa-global-flags-v1_1-20260417.md)

| Status | Count |
|---|---:|
| Open | 6 |
| Resolved | 3 |
| Obsolete | 1 |
| Standing | 0 |
| **Total** | **10** |

**FLAG-010 is a blocking gate on new word analysis.** It requires an audit of every governing instruction against GR v2_9. Until resolved, no new word enters analysis.

## 6. What remains to be addressed

### 6.1 Structural observations surfaced during the consolidation

- **GR-PROG-005 TODO.** The consolidated role-separation rule contains an in-line TODO: *"complying with [TODO: consolidated patch/directive instruction — reference to be inserted when the document is produced]"*. This TODO will be backfilled when the patch/directive instruction exists.
- **GR-CAD-001 and GR-FILE-008 relationship.** GR-CAD-001 governs cadence (self-check, present_files) but does not itself mandate dual-write. GR-FILE-008 is retained as the dual-write rule. A future review could consolidate these into a single cadence-and-dual-write rule; flagged for consideration but not scheduled.
- **Addendum_patch_directive heaviness.** 9 items now sit in this addendum — it is the largest by far. When the patch/directive instruction review session runs, this is where the bulk of work concentrates.
- **No active GR-DIR rules in main array.** All directive-related governance has moved to the addendum. Any live use of directives in current practice relies on the addendum items and on GR-PROG-005 v2_0 which describes the patch/directive request mechanism at high level. The patch/directive instruction consolidation is now the single point of truth for directive mechanics until produced.

### 6.2 Outstanding flags

- **FLAG-001** (Open) — Session C instruction finalisation, deferred.
- **FLAG-006** (Open, informational) — Session D naming conventions, deferred.
- **FLAG-007** (Open, scheduled) — SB_FINDING/SB_DIMENSION/SB_INNER_BEING deprecation at next Analysis_output session.
- **FLAG-008** (Open, tracked under FLAG-010) — instruction updates for expanded rule set.
- **FLAG-010** (Open, blocking gate) — post-GR-v2_9 instruction audit. Blocks new word analysis.

### 6.3 Audit items from the v2_7 audit now fully addressed

- §3.1 redundancy cluster 1 (write-on-discovery triple) — consolidated into GR-OBS-001 v2_0 (v2_8).
- §3.2 redundancy cluster 2 (role separation duplication) — consolidated into GR-PROG-005 v2_0 (v2_8).
- §3.3 redundancy cluster 3 (evidence traceability) — consolidated into GR-PROC-002 v2_0 (v2_8).
- §3.4 redundancy cluster 4 (two self-checks) — both migrated to addendum (v2_8 / v2_9).
- §4.1 A5 / FLAG-002 (DR v1.9 vs GR-OBS-004 conflict) — resolved by DR v3_2 correction (O-037).
- §4.1 A7 (GR-DIR-001 self-assessment test) — dissolved by migration of GR-DIR-001 to addendum (v2_9).
- §4.2 A1 (version numbering) — GR-FILE-003 v3_0 (v2_8).
- §4.2 A2 (GR-FILE-005 format ambiguity) — GR-FILE-005 v2_0 (v2_8).
- §4.2 A3 (GR-OBS-002 category (d) catch-all) — dissolved by retirement of GR-OBS-002 (v2_9).
- §4.2 A4 (GR-PROC-001 vs preamble) — GR-PROC-001 v2_0 trim (v2_8).
- §4.2 A6 (GR-PROG-002 divine-characteristics) — GR-PROG-002 v2_0 edit (v2_8).
- §5 C1 (GR-OBS-004 vs DR v1.9) — resolved via FLAG-002 resolution.
- §5 C2 (GR-FILE-004 vs GR-FILE-008 dual-write conflict) — dissolved by retirement of GR-FILE-004 (v2_9). GR-FILE-008 retained.
- §5 C3 (GR-DIR-004 / GR-PROG-005 duplication) — resolved in v2_8 absorption.
- §5 C4 (decision-block scaling) — dissolved by retirement of GR-RD-001 through -006 in favour of new interactive GR-RD-007 (v2_9).

## 7. Suggested next steps

1. **Resolve FLAG-010 instruction audit.** This is the blocking gate. Start with whichever instruction is nearest to next use: VerseContext instruction and the Dimension Review v3_2 full audit are natural first candidates. Analysis_readiness and Analysis_output are on the horizon but not yet produced.
2. **Patch/directive instruction consolidation.** When next available, the 9 items in addendum_patch_directive give a ready-made scope for producing a unified patch/directive instruction. The TODO in GR-PROG-005 resolves when this document exists.
3. **WA-Reference Section 1 update.** ADD-REF-003 flags this (stale file-naming patterns). Schedule as part of the Reference review session.
4. **Session C, Session D, Analysis_output instruction drafts.** Several flags (FLAG-001, FLAG-006, FLAG-007) wait on these. None is blocking current work.

## 8. Current state — one sentence each

- **Global rules:** v2_9, 32 active rules across 12 categories; preamble binding since v2_6; obsolete rules retained for audit.
- **Flags:** v1_1, 10 flags (6 open, 3 resolved, 1 obsolete).
- **Dimension Review:** v3_2, observations-log versioning corrected; full audit against v2_9 pending under FLAG-010.
- **Addendums:** 22 items (10 instructions, 9 patch/directive, 3 reference) pending dedicated review sessions.
- **Blocking gate:** FLAG-010 — no new word analysis until all governing instructions are audited against GR v2_9.

---

*End of status overview — wa-global-rules-status-v1_0-20260417.md*