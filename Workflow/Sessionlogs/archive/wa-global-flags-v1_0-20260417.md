# WA Global Flags

**Filename:** wa-global-flags-v1_0-20260417.md
**Version:** v1_0
**Date:** 2026-04-17
**Status:** Active — supersedes flags array inside wa-global-general-rules-v2_7-20260417.json

---

## Purpose

This file holds the open, resolved, and standing flags for the WA Soul Word Analysis programme. Flags were previously held in the `flags` array of the global rules JSON. In v2_8 of the global rules (2026-04-17), the array was removed from the JSON and migrated to this standalone file to improve visibility, reviewability, and separation of concerns — the global rules file defines what is binding; this file tracks what is open.

## Load requirement

Claude AI must read this file in full at the start of every session, immediately after loading the global rules. The load is confirmed by stating aloud: *"Global flags wa-global-flags-v[version]-[date].md loaded — [n] open, [n] resolved, [n] standing."* This confirmation is part of the session-start ritual alongside GR-LOAD-001.

## Flag status summary at migration

| Status | Count |
|---|---:|
| Open | 6 |
| Resolved | 2 |
| Standing condition | 1 |
| **Total** | **9** |

---

## Flag register

### FLAG-001 — Session C instruction — full document missing from project files

- **Status:** Open
- **Raised:** 2026-04-14
- **Description:** Session-C-Instruction-v1_3-2026-04-11.md is referenced in userMemories as an active governing instruction but is not present in the project files. The project contains only the prose rule (wa-global-sessionC-prose-rule-v1-2026-04-13.md) and the word study template (wa-word-study-template-v2-2026-04-13.md). It is unclear whether: (a) the instruction exists but was not uploaded to the project, (b) the Session C instruction was intentionally replaced by the prose rule plus template, or (c) the instruction needs to be created. All GR rules apply to Session C via GR-LOAD-001 but the specific Session C workflow cannot be audited or updated without the full instruction.
- **Action needed:** Confirm whether Session-C-Instruction-v1_3 exists and should be added to project files, or whether the prose rule + template constitute the current Session C governing documents.

### FLAG-002 — Observations log versioning — named boundaries vs every write session

- **Status:** Open
- **Raised:** 2026-04-14
- **Description:** Dimension Review instruction v1.9 Section 6.2 states "version-increment on every new write session for the same cluster." Researcher confirmed D-01A: named boundaries is correct — version-increment when resuming a cluster in a new session, not on every file save. The DR instruction text requires correction to match this confirmed rule. Decision has been confirmed; this flag tracks the pending instruction update.
- **Action needed:** Update Dimension Review v1.9 Section 6.2 file writing discipline to state: "Version-increment the observations log filename when resuming work on the same cluster in a new session — not on every file save within the same session."

### FLAG-003 — Session B pass count inconsistency — five vs six passes

- **Status:** Open
- **Raised:** 2026-04-14
- **Description:** Session B instruction v4.7 contains inconsistent references to pass count. Several overview sections and section headers reference "five passes" but the instruction body defines six passes (Pass 1–5 analytical, Pass 6 Correlation Audit). The session close confirmation template and integrity rules correctly reference six passes. Researcher confirmed D-03: the document defines 6 passes and Session B instruction must be updated to state six passes consistently throughout.
- **Action needed:** Update Session B v4.7: replace all references to "five passes" and "five-pass analysis" with "six passes" and "six-pass analysis". Confirm that the change note for v4.8 documents this correction.

### FLAG-004 — GR-PROG-007 (filter at term level) — rule corrected

- **Status:** Resolved
- **Raised:** 2026-04-14
- **Resolved:** 2026-04-14
- **Description:** Rule was too narrow in v2.0. Researcher correction (20260414): corrected to two-condition formulation. GR-PROG-007 updated to v2.1.
- **Action needed:** None — resolved.

### FLAG-005 — CC Instructions document version currency and audit scope

- **Status:** Resolved
- **Raised:** 2026-04-14
- **Resolved:** 2026-04-14
- **Description:** WA-SessionB-ClaudeCode-Instructions-v3_2-20260330.md had stale references. Updated as wa-sessionb-cc-instructions-v3.3-20260414.md.
- **Action needed:** None — resolved.

### FLAG-006 — Session D — synthesis output format and naming not yet in global rules

- **Status:** Open
- **Raised:** 2026-04-14
- **Description:** Session D Orientation v3.0 Section 10.5 specifies a filename pattern using a hyphenated date which conflicts with GR-FILE-009 (compact date). Session D naming convention not fully audited against GR-FILE rules.
- **Action needed:** When updating Session D Orientation: (1) correct filename example to compact date format; (2) confirm whether a full Session D instruction needs to be drafted before Session D work begins at scale.

### FLAG-007 — SB_FINDING, SB_DIMENSION, SB_INNER_BEING codes — deprecated

- **Status:** Open
- **Raised:** 2026-04-15
- **Description:** These three codes in wa_quality_flag_types (ids 145, 146, 147) were placeholder designs from before the dedicated tables existed. The correct destinations for Session B analytical outputs are: wa_session_b_findings (key findings), wa_session_b_dimensions (dimensional profile), and word_registry.sb_classification fields (inner being standing). A CC directive has been produced to mark these three codes as deprecated in wa_quality_flag_types. Researcher confirmed obsolete 2026-04-15.
- **Action needed:** Apply CC directive DIR-20260415-001 to mark the three codes deprecated. Confirm via query that no rows in wa_data_quality_flags use these codes.

### FLAG-008 — Researcher decision discipline — programme-wide rules added

- **Status:** Open
- **Raised:** 2026-04-15
- **Description:** GR-RD-001 through GR-RD-006 added in v2.2 governing the format, gate conditions, presentation, and resolution requirements for researcher decision items. GR-DB-001 added prohibiting DB state assumptions. GR-DIR-001 expanded; GR-DIR-002 through GR-DIR-005 added governing directive and patch distinction, format, and confirmation requirements. All instruction documents that reference the former GR-DIR-001 single-sentence rule should be updated to reference the expanded GR-DIR-001 through GR-DIR-005 set.
- **Action needed:** Update Session B v5.0 (when drafted), CC Instructions v3.3, and any other instruction referencing GR-DIR-001 to reflect the expanded directive/patch governance and researcher decision rules.

### FLAG-009 — Preamble edit-lock — custodianship

- **Status:** Standing condition
- **Raised:** 2026-04-17
- **Description:** The preamble in the document header was added in v2.6 as the binding behavioural frame for all sessions. Edits to the preamble require explicit researcher approval and a version increment. A session proposing to improve, shorten, or restructure the preamble without researcher authorisation is exhibiting the exact pattern the preamble forbids. This flag records the edit-lock for audit.
- **Action needed:** None — standing condition. Future edits to the preamble must cite explicit researcher approval in the change note.

---

## Change register

**v1_0 (2026-04-17):** File created. All 9 flags migrated verbatim from `wa-global-general-rules-v2_7-20260417.json` `flags` array. Content unchanged; container changed. Flag IDs, descriptions, dates, and resolved states are preserved as they were in v2.7. Migration authorised by researcher in session 2026-04-17 (see obslog entry O-020, D1 decision).
