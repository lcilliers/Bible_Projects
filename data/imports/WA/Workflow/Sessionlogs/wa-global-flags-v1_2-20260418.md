# WA Global Flags

**Filename:** wa-global-flags-v1_2-20260418.md
**Version:** v1_2
**Date:** 2026-04-18
**Status:** Active — supersedes wa-global-flags-v1_1-20260417.md

---

## Purpose

This file holds the open, resolved, obsolete, and standing flags for the WA Soul Word Analysis programme. Flags were migrated out of the global rules JSON in v2_8 of the global rules (2026-04-17) and now live in this standalone file for improved visibility and reviewability. The global rules file defines what is binding; this file tracks what is open.

## Load requirement

Claude AI must read this file in full at the start of every session, immediately after loading the global rules. The load is confirmed by stating aloud: *"Global flags [filename] loaded — [n] open, [n] resolved, [n] obsolete, [n] standing."* This confirmation is part of the session-start ritual alongside GR-LOAD-001.

## Status categories

- **Open** — issue is active; action is pending.
- **Resolved** — issue was worked on and closed with a concrete outcome. Preserved for audit.
- **Obsolete** — flag was raised in a form that is not useful or no longer applies. Set aside without outcome. Preserved for audit.
- **Standing** — standing condition, no action needed but the record is retained.

Open, Resolved, and Standing flags are counted at load. Obsolete flags are retained for history but are not counted at load and are not taken into account in programme state.

## Flag status summary at v1_2

| Status | Count |
|---|---:|
| Open | 7 |
| Resolved | 3 |
| Obsolete | 1 |
| Standing | 0 |
| **Total** | **11** |

**Change from v1_1:** v1_1 had 6 Open, 3 Resolved, 1 Obsolete (total 10). In v1_2: FLAG-011 added Open (retirement of wa-sessionb-cc-instructions-v3_6). No other flag state changes in this revision.

**Change from v1_0:** v1_0 had 6 Open, 2 Resolved, 1 Standing (total 9). In v1_1: FLAG-002 and FLAG-003 moved Open → Resolved; FLAG-009 moved Standing → Obsolete; new FLAG-010 added Open; all other flags updated with refreshed description or action text per researcher direction 2026-04-17. Descriptions and actions were refreshed on FLAG-001, FLAG-006, FLAG-007, FLAG-008 (still Open).

---

## Flag register

### FLAG-001 — Session C instruction — under construction, deferred

- **Status:** Open
- **Raised:** 2026-04-14
- **Last updated:** 2026-04-17
- **Description:** Session C instruction is under construction and not yet ready for project files. Finalisation is deferred until the Analysis_readiness and Analysis_output instructions (which together replace the former Session B instruction) are completed. Until then, Session C work is governed by the prose rule (wa-global-sessionC-prose-rule-v1-20260413.md) and the word study template (wa-word-study-template-v2-20260413.md). *Originally raised as: "Session-C-Instruction-v1_3 referenced in userMemories but not present in project files."*
- **Action needed:** Finalise Session C instruction after Analysis_readiness and Analysis_output are complete. No earlier action required.

### FLAG-002 — Observations log versioning — named boundaries vs every write session — RESOLVED

- **Status:** Resolved
- **Raised:** 2026-04-14
- **Resolved:** 2026-04-17
- **Description:** Dimension Review instruction v3.1 Section 8.2 (and repeat statements in Section 8.6 and Section 15) stated "Every write increments the version by 0.1" for the observations log. Researcher confirmed D-01A: named boundaries is correct — version-increment when resuming a cluster in a new session or at a named batch boundary, not on every file save. The DR instruction text required correction to match this rule (GR-OBS-004).
- **Resolution:** Corrected in `wa-dimensionreview-instruction-v3_2-20260417.md` (2026-04-17). Three locations amended: Section 8.2 (File writing discipline bullet list), Section 8.6 (Per-registry patch protocol — trigger description and step 1), Section 15 (Naming Conventions — Observations log versioning line). All three now reference GR-OBS-004 rather than repeating the rule text inline. No other edits made to the DR instruction in this cycle; a full audit of DR v3.2 against GR v2_8 is scheduled under FLAG-010.

### FLAG-003 — Session B pass count inconsistency — RESOLVED by retirement

- **Status:** Resolved
- **Raised:** 2026-04-14
- **Resolved:** 2026-04-17
- **Description:** Session B instruction v4.7 contained inconsistent references to pass count (five vs six). The D-03 resolution called for the document to state six passes consistently.
- **Resolution:** Resolved by retirement of the pass-count concept. The Session B instruction v4.7 is being completely rewritten and split into two separate instructions (Analysis_readiness and Analysis_output) in a format that does not use the pass concept. Correction of v4.7 is no longer required; it is superseded by the new instructions when completed.

### FLAG-004 — GR-PROG-007 (filter at term level) — rule corrected

- **Status:** Resolved
- **Raised:** 2026-04-14
- **Resolved:** 2026-04-14
- **Description:** Rule was too narrow in v2.0. Researcher correction (20260414): corrected to two-condition formulation. GR-PROG-007 updated to v2.1.
- **Resolution:** Applied.

### FLAG-005 — CC Instructions document version currency and audit scope

- **Status:** Resolved
- **Raised:** 2026-04-14
- **Resolved:** 2026-04-14
- **Description:** WA-SessionB-ClaudeCode-Instructions-v3_2-20260330.md had stale references. Updated as wa-sessionb-cc-instructions-v3.3-20260414.md.
- **Resolution:** Applied.

### FLAG-006 — Session D — synthesis output format and naming not yet in global rules

- **Status:** Open (informational — no imminent action expected)
- **Raised:** 2026-04-14
- **Last updated:** 2026-04-17
- **Description:** Session D Orientation v3.0 Section 10.5 specifies a filename pattern using a hyphenated date which conflicts with GR-FILE-009 (compact date). Session D naming convention not fully audited against GR-FILE rules. **Operational note 2026-04-17:** Session D processing is deferred until a considerable number of words have reached status "Analysis Completed". No immediate action required. The naming-convention correction flagged here remains open but can wait until Session D comes into view.
- **Action needed:** When updating Session D Orientation: (1) correct filename example to compact date format; (2) confirm whether a full Session D instruction needs to be drafted before Session D work begins at scale.

### FLAG-007 — SB_FINDING, SB_DIMENSION, SB_INNER_BEING codes — scheduled

- **Status:** Open (scheduled for next Analysis_output work session)
- **Raised:** 2026-04-15
- **Last updated:** 2026-04-17
- **Description:** These three codes in wa_quality_flag_types (ids 145, 146, 147) were placeholder designs from before the dedicated tables existed. The correct destinations for analytical outputs are: wa_session_b_findings (key findings), wa_session_b_dimensions (dimensional profile), and word_registry.sb_classification fields (inner being standing). A CC directive has been produced to mark these three codes as deprecated in wa_quality_flag_types. Researcher confirmed obsolete 2026-04-15. **Scheduling note 2026-04-17:** Resolution of this flag is tied to the next work session on the Analysis_output instruction. At that point, the CC directive DIR-20260415-001 will be applied and the query confirming no rows in wa_data_quality_flags use the deprecated codes will be run.
- **Action needed:** Apply CC directive DIR-20260415-001 to mark the three codes deprecated. Confirm via query that no rows in wa_data_quality_flags use these codes.

### FLAG-008 — Researcher decision discipline — programme-wide rules added

- **Status:** Open (tracked under FLAG-010 audit scope)
- **Raised:** 2026-04-15
- **Last updated:** 2026-04-17
- **Description:** GR-RD-001 through GR-RD-006 added in v2.2 governing the format, gate conditions, presentation, and resolution requirements for researcher decision items. GR-DB-001 added prohibiting DB state assumptions. GR-DIR-001 expanded; GR-DIR-002 through GR-DIR-005 added governing directive and patch distinction, format, and confirmation requirements. All instruction documents that reference the former GR-DIR-001 single-sentence rule should be updated to reflect the expanded directive/patch governance and researcher decision rules. **Note 2026-04-17:** The v2_8 GR update did not change GR-DIR-001, -002, -003, -005, -006, -007 or GR-RD-001 through -006 (the rules this flag is concerned with). The broader instruction audit raised as FLAG-010 covers the scope of this flag; this flag remains Open and will be closed when FLAG-010 confirms each instruction cited here reflects the expanded rule set.
- **Action needed:** Update Session B v5.0 (when drafted — superseded by Analysis_readiness / Analysis_output per FLAG-003 resolution), CC Instructions v3.3, and any other instruction referencing GR-DIR-001 to reflect the expanded directive/patch governance and researcher decision rules. Tracked under FLAG-010.

### FLAG-009 — Preamble edit-lock — OBSOLETE

- **Status:** Obsolete
- **Raised:** 2026-04-17
- **Marked obsolete:** 2026-04-17
- **Description:** Flag was raised to record the preamble edit-lock as a standing condition after v2.6 added the preamble to the global rules document.
- **Reason marked obsolete:** The flag was poorly framed. Preamble edit-lock is implicit in the researcher approval process — the document will not be changed without researcher involvement and approval. A standing flag to record this is not useful; the flag is set aside without outcome. Not counted in programme state. Record retained for audit.

### FLAG-010 — Post-GR-v2_8 instruction audit — GATE ON NEW WORD ANALYSIS

- **Status:** Open — **blocking gate**
- **Raised:** 2026-04-17
- **Description:** Following the major update of the Global Rules to v2_8 (2026-04-17), all instruction sets for the programme must be audited to verify that each correctly applies the updated rules. Rules changed in v2_8: GR-LOAD-001 (amended to load flags file and activate cadence discipline); GR-OBS-001 (consolidated write-on-discovery, log-authoritative, pass-close persistence, chat-to-log); GR-OBS-003 (strengthened to cover session-log-at-close); GR-PROC-001 (trimmed); GR-PROC-002 (consolidated traceability); GR-PROG-002 (edited); GR-PROG-005 (consolidated role separation with TODO marker); GR-FILE-003 (rewritten v3_0 — underscored versioning); GR-FILE-005 (replaced — short formulation); GR-CAD-001 (new — cadence discipline). Six rules marked obsolete and their content absorbed: GR-DIR-004, GR-PROC-003, GR-PROC-005, GR-PASS-002, GR-PROG-008, GR-PROC-006. Instructions citing these by ID must be updated to cite the absorbing rule. Three rules migrated to addendums: GR-OBS-005 (to addendum_patch_directive ADD-PATCHDIR-004); GR-OBS-006 (to addendum_instructions ADD-INSTR-011); GR-DIR-008 (to addendum_patch_directive ADD-PATCHDIR-003). Instructions citing these must be updated accordingly.
- **Instructions in scope:** Verse Context instruction, Dimension Review instruction (v3.2 already has a targeted correction from FLAG-002 — full audit still required), Analysis_readiness instruction (when complete), Analysis_output instruction (when complete), plus several utility instructions — list to be confirmed. The audit may reveal additional documents requiring update.
- **Action needed:** Audit each instruction in scope against GR v2_8. Produce updates where required. Record each updated instruction filename and scope of changes in this flag as progress is made. When all instructions in scope have been confirmed compliant or updated, resolve this flag.
- **Gate:** Analytical processing of any new word is blocked until this flag is resolved.

### FLAG-011 — WA-SessionB-ClaudeCode-Instructions to be retired — REPLACED

- **Status:** Open — pending consolidation
- **Raised:** 2026-04-18
- **Description:** The document currently named `wa-sessionb-cc-instructions-v3_6-20260416.md` (lineage from v3.0 through v3.6) is to be retired. The document contains three distinct content types that belong in separate documents per the researcher's structural direction: (a) Claude Code instructions and operational guidance, (b) interaction protocol between CAI and CC, (c) programme-wide references and lookup. The current document mixes all three and duplicates WA-Reference in its vocabulary and schema sections. The filename is also stale: the "sessionb" scope token does not match the document's programme-wide content, and will be further mismatched when Session B v4.7 is retired per FLAG-003. Full diagnosis and content inventory in `wa-global-ccdir-analysis-v1-20260418.md` §1–§3.
- **Replacement:** Three documents (filenames to be confirmed in consolidation work):
  - `wa-cc-instructions-v1_0-{YYYYMMDD}.md` — Claude Code operational instructions: register, extract, audit, export, apply patches, run state queries, produce REPAIR patches
  - `wa-cc-cai-interaction-v1_0-{YYYYMMDD}.md` — interaction protocol: the two methods (patches and directives), feedback requirements, role boundaries, handoff formats
  - `WA-Reference` (existing) — absorbs any vocabulary, naming, and schema content from the retired document that is not already present
  - Additionally: `wa-directive-specification-v1_0-{YYYYMMDD}.md` to be produced as peer to the patch specification, closing the gap recorded in addendum ADD-PATCHDIR-002 of the global rules.
- **References to update on retirement:** global rules (addendum ADD-PATCHDIR-002 and ADD-INSTR items citing the CC instructions); patch spec v1_14 (§3.10 reference; §3.12 references Section 15–16; change notes); WA-Reference v5_5 (§18.5); global flags v1_2 (FLAG-005 and FLAG-010 both reference the document).
- **Action needed:** (1) Produce the replacement documents using GR-REF-001 v1_0 discipline throughout. (2) Update all references in the four documents above. (3) Mark `wa-sessionb-cc-instructions-v3_6` as superseded with a pointer to the new document set. (4) Resolve this flag once all references are updated.
- **Relationship to FLAG-010:** FLAG-010 is a programme-wide audit of instructions against GR v2_8. FLAG-011 is a specific retirement-and-replacement within that audit scope. Work on FLAG-011 contributes to resolving FLAG-010 for the CC instructions entry.
- **Relationship to new rules:** The consolidation work governed by this flag is expected to produce documents compliant with GR-REF-001 v1_0 (single-authority referencing, pointer-not-copy, versioned references, consistency checks, scope discipline) — introduced in wa-global-general-rules v2_10-20260418 specifically to govern this and subsequent consolidation work.

---

## Change register

**v1_2 (2026-04-18):** FLAG-011 added — retirement of `wa-sessionb-cc-instructions-v3_6-20260416.md` with replacement by three separate documents per researcher structural direction (CC instructions, CC/CAI interaction protocol, WA-Reference absorption). Session record: `wa-global-ccdir-consolidation-obslog-v1-20260418.md` O-018 (draft) and O-037 (finalised). Paired with wa-global-general-rules v2_10-20260418 which introduced GR-REF-001 governing the discipline for the replacement documents. No other flag state changes in this revision.

**v1_1 (2026-04-17):** Flag updates applied per researcher direction in session 2026-04-17 (see obslog entries O-031 through O-036):
- FLAG-001 — description and action refreshed (remains Open); Session C deferred until Analysis_readiness and Analysis_output complete.
- FLAG-002 — Open → **Resolved**. DR instruction correction applied in `wa-dimensionreview-instruction-v3_2-20260417.md`.
- FLAG-003 — Open → **Resolved** by retirement of the pass-count concept (Session B rewrite into Analysis_readiness and Analysis_output).
- FLAG-006 — description refreshed with operational note about Session D deferral (remains Open, informational).
- FLAG-007 — description refreshed with scheduling note for Analysis_output work (remains Open, scheduled).
- FLAG-008 — description refreshed; tracked under FLAG-010 scope (remains Open).
- FLAG-009 — Standing → **Obsolete** per researcher direction (flag was poorly framed; preamble edit-lock is implicit in approval process).
- **FLAG-010 added** — post-GR-v2_8 instruction audit, blocking gate on new word analysis.

New status category introduced in this version: **Obsolete** — for flags set aside without outcome; not counted in programme state.

**v1_0 (2026-04-17):** File created. All 9 flags migrated verbatim from `wa-global-general-rules-v2_7-20260417.json` `flags` array. Content unchanged; container changed. Flag IDs, descriptions, dates, and resolved states preserved as they were in v2.7. Migration authorised by researcher in session 2026-04-17 (see obslog entry O-020, D1 decision).
