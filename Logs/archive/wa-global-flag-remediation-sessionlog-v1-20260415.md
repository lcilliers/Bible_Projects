# Session Log — Flag Remediation and Resolution Loop Design
## wa-global-flag-remediation-sessionlog-v1-20260415.md
**Date:** 2026-04-15
**Status:** Breakpoint — directives produced, awaiting researcher approval and CC execution
**Supersedes:** wa-global-sessionb-session-log-v1.1-20260414.md (for this design thread)

---

## What was accomplished this session

### 1. Full context review

All related documents were read before any design work began:
- wa-global-flagtable-remediation-plan-v1.0-20260414.md
- wa-global-sessionb-session-log-v1.1-20260414.md
- wa-global-obs-schema-v2_2-20260414.md (key document — most current specification)
- All five table assessments (session_d_tables, session_research_flags, session_b_findings, cross_registry_links, term_phase2_flags)
- flag-tables-listing-20260414.md and flag-tables-extract-joins-20260415.md
- Session B instruction v4.8, CC instructions v3.3, global rules v2.1
- Patch specification v1.11

### 2. Key decisions confirmed by researcher

**Q2 — SB_FINDING, SB_DIMENSION, SB_INNER_BEING codes:**
These three codes in `wa_quality_flag_types` (ids 145, 146, 147) are obsolete. Session B analytical outputs route to dedicated tables (`wa_session_b_findings`, `wa_session_b_dimensions`, `word_registry.sb_classification`). The codes were placeholder designs that predate these tables. They have never been used (zero rows in `wa_data_quality_flags`). Confirmed deprecated 2026-04-15. DIR-20260415-001 produced to execute.

**Q3 — wa_term_phase2_flags handling:**
Phase2 flags on individual terms are advisory, not evidential. They are not to be bulk-deleted. Session B Stage 1 audit must review each term's phase2 flags against the verse evidence — confirming, correcting, or marking irrelevant (where the term is deleted) on a term-by-term basis. This must be built into the Session B v5.0 Stage 1 process design. No directive needed — this is an instruction design decision.

**Q1 — Obs schema and resolution loop:**
The obs schema document describes what gets written and where. It does not describe how flags are encountered, evaluated, and formally closed within Session B. The missing piece is the resolution loop — the sequential process by which Session B ingests inherited flags at session start and closes them through the six analytical passes. Points 1, 2, 4, and 5 from the analysis (when flags are encountered, what constitutes resolution, what triggers marking resolved, what happens when Session B cannot resolve a flag) must be built into Session B v5.0 Stage 1. Point 3 (RESEARCHER_DECISION format) is addressed by the new GR-RD rules.

### 3. Resolution loop problem diagnosed

The researcher identified a structural problem with how decision items have been raised throughout the programme:
- Questions arrive without sufficient information for the researcher to decide
- Questions are raised without evidence that Claude AI exhausted its own resources first
- Questions have no numbering or referencing, making responses difficult
- The same questions recur because resolutions are partial and not formally closed
- Resolutions produce no concrete outcome — the conversation IS treated as the resolution

**Root cause:** No governed format or gate condition existed for researcher decision items.

**Resolution:** GR-RD-001 through GR-RD-006 added to global rules v2.2, governing the complete lifecycle of a researcher decision item programme-wide.

Additional rule added: GR-DB-001 — Claude AI never assumes DB state. Checks chat first; requests from CC if not present; asks for refresh if currency is in doubt.

GR-DIR-001 expanded from a single sentence to five rules (GR-DIR-001 through GR-DIR-005) governing: when to use directive vs patch, directive format, patch specification reference, role separation, and completion confirmation requirements.

### 4. Obs schema reconciliation

The remediation plan (v1.0-20260414) was found to be substantially answered by the obs schema document (v2.2-20260414). Specific findings:
- Steps 1–2 of the plan (schema extract, architecture decision): answered — same table architecture confirmed
- Steps 3–4 (govern reference table, RESEARCHER_DECISION fields): addressed by DIR-20260415-002 and new GR-RD rules
- Step 5 (SB outcome codes): resolved — codes deprecated, obs schema routes confirmed
- Steps 6–7 (export format, data cleanup): DIR-20260415-003, DIR-20260415-004, DIR-20260415-006 address the data cleanup; export format is a separate item not yet addressed
- Step 8 (instruction updates): Session B v5.0 is the vehicle — deferred until directives are confirmed

### 5. Documents produced this session

| File | Purpose | Status |
|------|---------|--------|
| wa-global-general-rules-v2.2-20260415.json | Updated global rules — new GR-RD, GR-DB, expanded GR-DIR rules | Produced — requires upload to project files |
| wa-global-flag-remediation-directives-v1-20260415.md | Six CC directives for flag table remediation and schema migration | Produced — requires researcher approval before CC executes |
| wa-global-flag-remediation-sessionlog-v1-20260415.md | This file | Produced |

---

## What is confirmed and decided

| Decision | Status |
|----------|--------|
| SB_FINDING / SB_DIMENSION / SB_INNER_BEING codes — deprecated | Confirmed. DIR-20260415-001 ready. |
| VOLUME_LIMITATION → PH2_VOLUME_LIMITATION consolidation | Confirmed. DIR-20260415-003 ready. |
| Same table architecture for wa_session_research_flags (four purposes, governed by flag_code category) | Confirmed by obs schema. |
| 15 missing reference rows needed in wa_quality_flag_types | Confirmed. DIR-20260415-002 ready. |
| 9 missing fields needed on wa_session_b_findings | Confirmed by obs schema G-4. DIR-20260415-004 ready. |
| wa_finding_entity_links new table | Confirmed by obs schema G-5. DIR-20260415-005 ready. |
| finding_type normalisation to UPPER_SNAKE_CASE | Confirmed. DIR-20260415-006 ready. |
| wa_term_phase2_flags — term-by-term verification in Session B Stage 1 audit (not bulk delete) | Confirmed. Instruction design work required. |
| Resolution loop for Session B — must be built into Session B v5.0 Stage 1 | Confirmed. Instruction design work required. |
| RESEARCHER_DECISION format — GR-RD-001 through GR-RD-006 | Confirmed. Added to global rules v2.2. |
| GR-DB-001 — no DB state assumptions | Confirmed. Added to global rules v2.2. |
| GR-DIR-001 through GR-DIR-005 — directive/patch distinction and confirmation | Confirmed. Added to global rules v2.2. |

---

## What remains open

| Item | Nature | Next action |
|------|--------|-------------|
| DIR-20260415-001 through DIR-20260415-006 | CC execution pending researcher approval | Researcher approves → CC executes in sequence |
| wa-global-general-rules-v2.2-20260415.json | Needs to replace v2.1 in project files | Upload to project |
| Session B v5.0 Stage 1 — flag resolution loop design | Instruction design work | Begin after directives confirmed |
| Session B v5.0 Stage 1 — wa_term_phase2_flags review sub-process | Instruction design work | Incorporate into Stage 1 audit design |
| wa_session_b_dimensions table — retire or retain? | Open obs schema decision (researcher decision needed) | Raise as RD item when drafting Session B v5.0 with full context |
| Verse annotation home (obs schema G-7) | Three options presented in obs schema | Raise as RD item with full option/consequence specification |
| finding_type C22 rows — mapping confirmation | DIR-20260415-006 notes CC should flag if uncertain | CC flags; researcher confirms before execution |
| FLAG-001 (Session C instruction missing) | Unresolved from v2.1 | Carry forward |
| FLAG-002 (DR instruction versioning correction) | Unresolved from v2.1 | Carry forward |
| FLAG-003 (Session B pass count correction) | Unresolved from v2.1 | Carry forward |
| FLAG-006 (Session D naming convention) | Unresolved from v2.1 | Carry forward |
| Export format for complete word data (remediation plan Step 6) | Not yet addressed | After schema directives confirmed |
| Programme-wide backward validation sweep DIM-187-SD001 | HIGH priority, pre-existing | Not in scope this session — remains open |

---

## Where to resume

**Immediate next steps (in order):**

1. Researcher reviews and approves DIR-20260415-001 through DIR-20260415-006
2. CC executes directives in sequence, returning confirmation for each
3. Claude AI reviews confirmations — if any anomalies, raises as new directives
4. Upload wa-global-general-rules-v2.2-20260415.json to project files (replaces v2.1)
5. Begin Session B v5.0 Stage 1 design — flag resolution loop and phase2 flag review sub-process

**Files to attach when resuming Session B v5.0 design:**
- wa-global-general-rules-v2.2-20260415.json (updated global rules)
- wa-global-obs-schema-v2_2-20260414.md (observation storage specification)
- wa-global-sessionb-instruction-v5.0-20260414.md (sections 1–5 already drafted)
- wa-global-sessionb-schema-gaps-v1.0-20260414.md
- This session log
- CC confirmation outputs from DIR-20260415-001 through DIR-20260415-006

---

## Analytical notes for Session B v5.0 Stage 1 design

The following points were established this session and must be incorporated:

**Flag resolution loop — what Session B Stage 1 must do:**
1. At session start — retrieve all `wa_session_research_flags` for this registry where `session_target = 'B'` and `resolved = 0`. These are the inherited flags requiring resolution within Session B. Present count and list before Stage 2 begins.
2. During Stage 1 audit — for each term, check `wa_term_phase2_flags` for existing flags. For each flag found: assess against verse evidence. If supported — note confirmed in observations log (flag stands). If not supported — note rejection with reason (flag to be marked for correction in patch). If term is deleted — flag is irrelevant, note in observations log.
3. During the six analytical passes — flags in `wa_session_research_flags` with `session_target = 'B'` are encountered during the relevant pass and resolved. Resolution means: a finding written to `wa_session_b_findings`, a correction applied via patch, or an escalation to SD_POINTER or RESEARCHER_DECISION. The flag is marked `resolved = 1` with `resolved_date` and `resolved_note` pointing to the resolving action.
4. At session close — zero open `wa_session_research_flags` with `session_target = 'B'` for this registry. This is a hard gate on session close.
5. RESEARCHER_DECISION items raised during Stage 1 are presented as a discrete block using the GR-RD-002 format before Stage 2 begins. Stage 2 does not begin until all RD items are resolved.

**wa_term_phase2_flags — advisory status:**
- These flags are prior-session hypotheses, not confirmed analytical facts
- 99% have no provenance description — the verification must come from reading the verses
- Flags on deleted terms are irrelevant — noted in observations log, no patch needed
- Flags on function words are irrelevant — noted in observations log, no patch needed
- Confirmed flags require no patch — they stand as-is
- Rejected flags require a patch to mark them (per GR-OBS-005 — no physical deletion)
