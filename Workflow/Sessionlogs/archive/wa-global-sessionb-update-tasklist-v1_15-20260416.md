# WA — Session B Instruction Update: Task List and Control Document
**Filename:** wa-global-sessionb-update-tasklist-v1_15-20260416.md
**Date:** 2026-04-16
**Version:** v1.15
**Change note (v1.15):** T-02E added and marked COMPLETE — Stage 1 opening section produced (wa-global-sessionb-stage1-opening-v1-20260416.md). Covers: Stage 1 outputs table; tracking document structure with four named sections in observations log and their update triggers; session start protocol (S1–S6); position marker register; fallback protocol for six failure modes; session close protocol (C1–C4). Stage 1 instruction now complete across five components (T-02A, T-02C, T-02D, T-02E plus retained Step 1.1). Status summary and dependency map updated.
**Supersedes:** wa-global-sessionb-update-tasklist-v1_14-20260416.md

**Previous output refs:**
- wa-global-sessionb-update-tasklist-v1_13-20260416.md (v1.13)
- wa-global-sessionb-step1-2-v2-20260416.md (T-02C output)
- wa-global-sessionb-stage1-completion-v1-20260416.md (T-02D output)

---

## Purpose

Governing control document and analytical record for the Session B instruction update. Maintained in detail to enable reconstruction of the analytical journey from any point.

**Target instruction output:** `wa-global-sessionb-instruction-v5_1-20260416.md`

---

## Programme Architecture — Confirmed

**Stage 1:** Data validation and preparation only. No analytical conclusions. Completes with a verified fresh extract and a formal Stage 2 readiness declaration.

**Stage 2:**

| Stage | Output | Nature |
|---|---|---|
| Stage 2a | Observations log | Full technical narrative — everything the data says about the word |
| Stage 2b | Q&A log | Question-answer pairs; iterative; multi-session |
| Stage 2c | Analytic word output | Six Session C chapters; replaces Analytical Brief |

**Six Session C chapters:** Meaning / How it works / Verses (all anchors + full text + Q&A pairs) / Language / Interrelationships / Open questions (all SD pointers)

---

## Source Material Reference

| Document | Role | Status |
|---|---|---|
| wa-global-sessionb-instruction-v5_0-20260415.md | Target document | Active |
| wa-global-obs-question-master-catalogue-v2_0-20260415.md | Governing catalogue | Active |
| wa-global-general-rules-v2_2-20260415.json | Global rules | Active |
| database-schema-20260416.json | Schema v3.9.0 | Active |
| wa-global-sessionb-stage1-draft-v1-20260416.md | T-02A — Steps 1.3a–1.5 v1.0 | Active — researcher review |
| wa-global-sessionb-step1-2-v2-20260416.md | T-02C — Step 1.2 v2.0 (full rewrite) | Active — researcher review |
| wa-global-sessionb-stage1-completion-v1-20260416.md | T-02D — Step 1.5 update + Step 1.6 new | Active — researcher review |
| wa-103-love-step1-2-audit-v1_1-20260416.md | Love extract audit | Active — reference |
| wa-global-sessionlog-sessionb-redesign-v1-20260416.md | Phase 2 architecture reasoning | Active |
| wa-global-sessionlog-sessionb-redesign-v2-20260416.md | Step 1.2 correction history | Active |

---

## Task Register

---

### T-00 — Schema analysis
**Status:** COMPLETE

---

### T-01 — Structural insertion point decision
**Status:** CONFIRMED

---

### T-SC — Schema directive and CC execution
**Status:** COMPLETE — schema v3.9.0

---

### T-POP — Populate tables
**Status:** COMPLETE

---

### T-02A — Stage 1 Part A: Steps 1.3a, 1.3b, 1.3c, 1.4
**Output:** wa-global-sessionb-stage1-draft-v1-20260416.md
**Status:** COMPLETE — awaiting researcher review and confirmation

**What was produced:**
- Step 1.3a: `wa_term_phase2_flags` — four-step decision sequence; confirmed/rejected/irrelevant/thin; patch for rejected flags
- Step 1.3b: `wa_session_b_findings` — data preparation only; three-outcome catalogue link assignment; no analytical reframing
- Step 1.3c: `wa_session_research_flags` B-target — four resolution types (A=data correction / B=research completed / C=Session D / D=researcher decision); hard gate with CC count verification
- Step 1.4: Type (a) patch — consolidated from all 1.3 sub-steps; includes field corrections, catalogue links, flag resolutions; B-target flag hard gate verification after application
- RESEARCHER_DECISION block: positioned after all three sub-steps, before patch construction
- Integrity rules: SB-20 (findings readiness gate), SB-21 (no analysis in Stage 1)

---

### T-02B — Stage 1 Part B: Step 1.2 first rebuild
**Output:** wa-global-sessionb-step1-2-corrected-v1-20260416.md + wa-103-love-step1-2-audit-v1_1-20260416.md
**Status:** COMPLETE — superseded by T-02C

**Key findings from love extract audit:** 7 instruction corrections (IC-01 through IC-07) and 3 structural weaknesses (W1–W3) identified.

---

### T-02C — Step 1.2 full rewrite with resolution classification framework
**Output:** wa-global-sessionb-step1-2-v2-20260416.md
**Status:** COMPLETE — awaiting researcher review and confirmation

**What was produced:** Complete clean rewrite of Step 1.2 incorporating all corrections. The governing change is the Resolution Classification Framework — four named paths (Type (a) patch / Process re-run directive / Stage 2a verification note / RESEARCHER_DECISION) with explicit decision rules, applied consistently to every check throughout the document.

**Structural additions:**
- Section A.0: Statistics pre-read — reads `statistics` section first as orientation signal; flags internal discrepancies before section-by-section work
- Section A.1: Audit_word history — reads `patch_history.word_run_states`; dispositions all inherited REVIEW flags
- Section B restructured by term type: OWNER / XREF / deleted — different checks per population
- Cross-check B1: Three-number verse diagnostic (`span_match_count` / `total_verse_records` / `delete_flagged_count`) — distinguishes span filter failure from genuine extraction gap
- Section C: Verse record quality checks including NULL `span_strong_match` handling
- Section D: Set-aside verse NULL reason check; `dominant_subject` correction logic
- Section E: Hardcoded dimension vocabulary removed; NULL and AUTOMATED only checked; DR instruction is authority
- Section H: Hard gate extended with three additional stopping conditions

**Key principles applied:**
- Every anomaly action specifies: which path; which table/field/value OR which process/scope/sequence; what to record in observations log
- Path 1 = Claude AI fixes — no researcher needed
- Path 2 = Process re-run — CC executes; Claude AI verifies; Session B paused
- Path 3 = Deferred to Stage 2a — non-blocking; recorded only
- Path 4 = RESEARCHER_DECISION — human judgement required; formal format; gate holds

---

### T-02D — Stage 1 completion: Step 1.5 update + Step 1.6 new
**Output:** wa-global-sessionb-stage1-completion-v1-20260416.md
**Status:** COMPLETE — awaiting researcher review and confirmation

---

### T-02E — Stage 1 opening: tracking documents, session management, fallback protocol
**Output:** wa-global-sessionb-stage1-opening-v1-20260416.md
**Status:** COMPLETE — awaiting researcher review and confirmation

**What was produced:**

**Stage 1 outputs table:** Four outputs named and initiated at Stage 1 start — observations log, session log, Type (a) patch, CC directives. All initiated before Step 1.1.

**Tracking document structure:** The observations log has four named sections created at start: Type (a) Patch Accumulator, RESEARCHER_DECISION Accumulator, Path 3 Verification Notes, Stage 1 Progress Record. Each section has a defined format and a defined trigger for when it is updated. Every step in Stage 1 knows which section to write to and when.

**Session start protocol (Steps S1–S6):** Defined sequence for every session start — whether first session or resumption. Confirms: global rules loaded; current position from progress record; extract version currency; patch accumulator state; directive state. States resumption position in observations log before proceeding.

**Position marker register:** The Stage 1 Progress Record functions as the position marker register. Its sign-off statements are the recovery instrument. The resumption table maps each last-completed step to the exact next step — deterministic, no reconstruction needed.

**Fallback protocol:** Six named failure modes with defined fallback states: session interrupted mid-step; patch partially applied; sub-process interrupted; stale extract; RD item unresolvable within session; Path 2 directive not confirmed within session. Each fallback is a known clean state, not a partial state.

**Session close protocol (Steps C1–C4):** Defined sequence for every session end — reach a clean stopping point; verify observations log completeness; produce session log; produce downloads. Always ends with the current position recorded and the next session's entry point explicit.

**What was produced:**

**Step 1.5 updated:** Extended to cover all five Path 2 sub-process triggers from the Step 1.2 resolution framework:
- Trigger 1: Span filter failure — re-extraction + audit_word + VC re-run (targeted)
- Trigger 2: Zero-verse extraction gap — re-extraction + audit_word (with occurrence_count check before raising directive)
- Trigger 3: OWNER terms with no groups — Verse Context sub-process (targeted)
- Trigger 4: NULL dimension or AUTOMATED confidence groups — Dimension Review sub-process
- Trigger 5: Groups with no anchor verse — targeted VC anchor pass
Session B pauses at Step 1.5 until all triggered processes complete and are confirmed.

**Step 1.6 (new) — Stage 1 Completion Verification and Handoff:**
Three parts:
- Part 1: Targeted verification of every correction against the fresh extract — every Path 1 patch operation confirmed present; every Path 2 sub-process outcome confirmed. Failures block until resolved.
- Part 2: Stage 1 Completion Checklist — 7 domains checked: registry state / term data / verse context groups / dimension assignments / flags and findings / catalogue readiness / process history. Every item must pass. Corrective action specified for each failure.
- Part 3: Stage 1 Completion Record and Stage 2 Readiness Declaration — formal structured summary of all steps; explicit declaration that Stage 2 may begin; extract version recorded as authoritative reference.

**New integrity rules added:** SB-22 (Stage 1 Completion Record required), SB-23 (Stage 2 works from confirmed fresh extract), SB-24 (Path 2 directive not complete until CC execution AND extract verification confirmed).

**Why Step 1.6 is necessary:** Without it, Stage 1 ends with a fresh extract version number but no verification that the extract contains the corrections. Patches can fail silently. Sub-processes can complete without their output reaching the extract. Step 1.6 closes that gap — it verifies the data, not just the process.

---

### T-02 — Overall Stage 1 instruction status

The Stage 1 instruction is now structurally complete across all components:

| Component | Document | Status |
|-----------|----------|--------|
| Stage 1 opening (outputs, tracking, sessions, fallback) | wa-global-sessionb-stage1-opening-v1-20260416.md | Complete — researcher review |
| Step 1.2 v2.0 | wa-global-sessionb-step1-2-v2-20260416.md | Complete — researcher review |
| Steps 1.3a, 1.3b, 1.3c, 1.4 | wa-global-sessionb-stage1-draft-v1-20260416.md | Complete — researcher review |
| Step 1.5 (updated) + Step 1.6 (new) | wa-global-sessionb-stage1-completion-v1-20260416.md | Complete — researcher review |
| Integrity rules | Distributed across T-02A, T-02C, T-02D | Complete — researcher review |

When all components are confirmed, they will be assembled into the single instruction document as part of T-09.

---

### T-2A — Draft Stage 2a: Comprehensive analysis → Observations log
**Depends on:** T-02A CONFIRMED AND T-02C CONFIRMED AND T-02D CONFIRMED
**Status:** PENDING — ready on researcher confirmation of all T-02 components

**What Stage 2a must cover:**
- Load all data at start: complete fresh extract; all existing findings (as input material, not pre-completed outputs); thin-evidence phase2 flags carried from Step 1.3a; all SD pointers for this registry from `wa_session_research_flags` (session_target = 'D'); Path 3 notes from Step 1.2; correlation signals
- Produce the observations log: full technical narrative; free-form; comprehensive; no structure imposed; no conclusion withheld
- Observations log is fixed after Stage 2a — it does not change in Stage 2b or 2c
- Output filename: `wa-[nnn]-[word]-sessionb-observations-v[n]-[date].md`
- Sign-off: observations log downloaded and confirmed complete

---

### T-2B — Draft Stage 2b: Q&A partitioning → Q&A log + patches
**Depends on:** T-2A CONFIRMED
**Status:** PENDING

---

### T-2C — Draft Stage 2c: Structured output → Analytic word output
**Depends on:** T-2B CONFIRMED
**Status:** PENDING

---

### T-CL — Draft Stage 2 Closure: checklist and final patch
**Depends on:** T-2C CONFIRMED
**Status:** PENDING

---

### T-GATE — Draft schema readiness gate at Stage 1/Stage 2 transition
**Depends on:** T-SC ✓
**Status:** PENDING

---

### T-08 — Nine gap candidates (C-1 through C-9)
**Nature:** Researcher decision — independent
**Status:** PENDING — researcher decision required

| Code | Proposed direction |
|------|-------------------|
| C-1 | Does the word's vocabulary construct meaning primarily through negation? |
| C-2 | Does the word's corpus contain the signature of another word as its structural answer? |
| C-3 | Does the word name a creational baseline — a pre-fall condition — with a before/after structure? |
| C-4 | Does any verse place the same inner-being faculty on both sides of the divine-human boundary simultaneously? |
| C-5 | Does the word describe a corporate or communal inner-being condition as well as an individual one? |
| C-6 | Does the word have a static form (condition held) and a dynamic form (process of becoming)? |
| C-7 | Does the word's vocabulary hold moral and affective dimensions as linguistically undivided? |
| C-8 | Does the word include the inner person addressing, observing, or commanding their own inner state? |
| C-9 | Does any verse within the word's corpus name this inner act as greater than another inner act? |

---

### T-09 — Final instruction close
**Depends on:** All other tasks CONFIRMED
**Status:** PENDING

---

## Instruction Correction Register

| Code | Source | Section | Issue | Status |
|------|--------|---------|-------|--------|
| IC-01 | Love extract audit | Step 1.2 Section E | Hardcoded dimension vocabulary | Resolved in T-02C |
| IC-02 | RD-S1-001 + G1516 | Step 1.2 Section C + Step 1.5 | Span filter failure not distinguished | Resolved in T-02C + T-02D |
| IC-03 | Love extract audit | Step 1.2 Section B | XREF NULL mti_status vs OWNER NULL | Resolved in T-02C |
| IC-04 | Love extract audit | Step 1.2 deleted terms | delete_flagged inconsistency | Resolved in T-02C |
| IC-05 | Love extract audit | New Section A.1 | audit_word REVIEW flags not read | Resolved in T-02C |
| IC-06 | Love extract audit | Step 1.2 Section D | Set-aside NULL reason | Resolved in T-02C |
| IC-07 | Love extract audit | New Section A.0 | Statistics not read first | Resolved in T-02C |
| W1 | Structural assessment | Step 1.2 throughout | No resolution framework | Resolved in T-02C |
| W2 | Structural assessment | Step 1.2 throughout | Method of fixing underspecified | Resolved in T-02C |
| W3 | Structural assessment | Step 1.2 Section H | Hard gate incomplete | Resolved in T-02C + T-02D |

All instruction corrections resolved. No open items in this register.

---

## Task Dependency Map

```
T-00/T-01/T-SC/T-POP ── ALL COMPLETE
    │
T-02A (Steps 1.3a–1.4) ── COMPLETE — researcher review
T-02B (Step 1.2 v1.0) ── COMPLETE — superseded
T-02C (Step 1.2 v2.0) ── COMPLETE — researcher review
T-02D (Step 1.5 update + Step 1.6) ── COMPLETE — researcher review
T-02E (Stage 1 opening — tracking/sessions/fallback) ── COMPLETE — researcher review
    │
    ▼ (all T-02 components confirmed)
T-2A (Stage 2a: observations log) ◄── NEXT after confirmation
    │
    ▼
T-2B (Stage 2b: Q&A partitioning)
    │
    ▼
T-2C (Stage 2c: analytic word output)
    │
    ▼
T-CL (closure checklist + final patch)

T-GATE — independent (T-SC done)
T-08 — independent (researcher decision)
T-09 — depends on all
```

---

## Open Items

| Ref | Item | Owner | Blocking |
|---|---|---|---|
| T-02A | Researcher review of Steps 1.3a–1.4 | Researcher | T-2A |
| T-02C | Researcher review of Step 1.2 v2.0 | Researcher | T-2A |
| T-02D | Researcher review of Step 1.5 update + Step 1.6 | Researcher | T-2A |
| T-02E | Researcher review of Stage 1 opening section | Researcher | T-2A |
| T-08 | Nine gap candidates C-1–C-9 | Researcher | Catalogue rows |

---

## Status Summary

| Task | Description | Depends on | Status |
|------|-------------|-----------|--------|
| T-00 | Schema analysis | — | COMPLETE |
| T-01 | Structural insertion point | — | CONFIRMED |
| T-SC | Schema directive + CC | T-00, T-01 | COMPLETE |
| T-POP | Populate tables | T-SC | COMPLETE |
| T-02A | Stage 1: Steps 1.3a–1.4 | T-01, T-SC, T-POP | COMPLETE — researcher review |
| T-02B | Stage 1: Step 1.2 v1.0 | T-SC | COMPLETE — superseded |
| T-02C | Stage 1: Step 1.2 v2.0 full rewrite | T-02B | COMPLETE — researcher review |
| T-02D | Stage 1: Step 1.5 update + Step 1.6 | T-02C | COMPLETE — researcher review |
| T-02E | Stage 1: opening section — tracking/sessions/fallback | T-02D | COMPLETE — researcher review |
| T-2A | Stage 2a: observations log | T-02A+C+D+E | PENDING — ready on confirmation |
| T-2B | Stage 2b: Q&A partitioning | T-2A | PENDING |
| T-2C | Stage 2c: analytic word output | T-2B | PENDING |
| T-CL | Closure checklist + final patch | T-2C | PENDING |
| T-GATE | Schema readiness gate | T-SC | PENDING |
| T-08 | Nine gap candidates | — | PENDING — researcher decision |
| T-09 | Final instruction close | All | PENDING |

---

*End of wa-global-sessionb-update-tasklist-v1_14-20260416.md*
*Supersedes wa-global-sessionb-update-tasklist-v1_13-20260416.md*
*Target instruction output: wa-global-sessionb-instruction-v5_1-20260416.md*
