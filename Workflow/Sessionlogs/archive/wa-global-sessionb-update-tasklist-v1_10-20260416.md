# WA — Session B Instruction Update: Task List and Control Document
**Filename:** wa-global-sessionb-update-tasklist-v1_10-20260416.md
**Date:** 2026-04-16
**Version:** v1.10
**Change note (v1.10):** T-02 split into Part A (Steps 1.3a–1.3c, 1.4, 1.5 — ready for review) and Part B (Step 1.2 — requires correction). Three problems identified by researcher in Step 1.2: (1) incoherent Phase 2 deferrals, (2) no terms of reference for field checks, (3) incomplete field coverage. T-02B added as formal correction task. T-2A blocked until T-02A and T-02B both confirmed. Session log v2 produced.
**Supersedes:** wa-global-sessionb-update-tasklist-v1_9-20260416.md

**Previous output refs:**
- wa-global-sessionb-update-tasklist-v1_9-20260416.md (v1.9)
- wa-global-sessionlog-sessionb-redesign-v2-20260416.md (session close log — Step 1.2 correction items)
- wa-global-sessionb-stage1-draft-v1-20260416.md (T-02 draft — Part B requires correction)

---

## Purpose

Governing control document for this session. Updated and version-incremented at each meaningful change point. No task actioned without appearing in this register and being confirmed by the researcher.

**Session governance rules:**
1. This task list is updated before any new work is reported or downloaded.
2. Each update is a minor version increment.
3. Each Session B instruction update is a separate minor version increment of that document.
4. No work proceeds without task registration and researcher confirmation.
5. Additional session logs may modify tasks — task list updated when this occurs.

**Target instruction output:** `wa-global-sessionb-instruction-v5_1-20260416.md`

---

## Phase 2 Architecture — Confirmed

| Stage | Output | Nature |
|---|---|---|
| Stage 2a | Observations log | Full technical narrative — everything the data says |
| Stage 2b | Q&A log | Question-answer pairs; iterative; multi-session |
| Stage 2c | Analytic word output | Six Session C chapters; replaces Analytical Brief |

**Six Session C chapters:** Meaning / How it works / Verses (all anchors + full text + Q&A pairs) / Language / Interrelationships / Open questions (all SD pointers)

---

## Source Material Reference

| Document | Role |
|---|---|
| wa-global-sessionb-instruction-v5_0-20260415.md | Target document |
| wa-global-obs-question-master-catalogue-v2_0-20260415.md | Governing catalogue |
| wa-global-general-rules-v2_2-20260415.json | Global rules |
| wa-global-schema-verify-20260416-001-v1-20260416.md | Schema v3.9.0 confirmed |
| database-schema-20260416.json | Schema v3.9.0 — required for Step 1.2 rebuild |
| wa-global-sessionb-stage1-draft-v1-20260416.md | T-02 draft — Part A ready, Part B needs correction |
| wa-global-sessionlog-sessionb-redesign-v1-20260416.md | Phase 2 architecture reasoning |
| wa-global-sessionlog-sessionb-redesign-v2-20260416.md | Step 1.2 correction items |

---

## Task Register

### T-00 — Schema analysis — COMPLETE
### T-01 — Structural insertion point decision — CONFIRMED
### T-SC — Schema directive and CC execution — COMPLETE
### T-POP — Populate tables — COMPLETE

---

### T-02A — Stage 1 Part A: Steps 1.3a, 1.3b, 1.3c, 1.4, 1.5
**Output:** wa-global-sessionb-stage1-draft-v1-20260416.md (these sections)
**Status:** COMPLETE — awaiting researcher review and confirmation

---

### T-02B — Stage 1 Part B: Step 1.2 correction and rebuild
**Source:** Researcher review of T-02 draft — three problems identified
**Depends on:** T-SC ✓; schema v3.9.0 available
**Status:** PENDING — correction required before next session proceeds

**Three problems to correct:**

**Problem 1 — Incoherent Phase 2 deferrals:**
Fields `god_as_subject` and `somatic_link` currently say "do not trust — verify in Stage 2." This is incoherent in a step that validates data before Stage 2 begins. Must be replaced with a concrete Stage 1 action — a reasonability check that can be completed from the extract, with a note that full verification happens in Stage 2a when verses are read.

**Problem 2 — No terms of reference:**
Every field check must state: what the field should contain, what to compare it against, and what constitutes a gap or anomaly. Currently the checks say "check field X" without specifying what correct looks like or how to determine it.

**Problem 3 — Incomplete field coverage:**
Step 1.2 must be rebuilt against schema v3.9.0. The governing rule is: ALL data for the word must be validated. Every table in the extract requires field-level checks. Cross-field consistency checks required (e.g. `status = 'extracted'` → verse count > 0). Cross-table correlation checks required (e.g. `somatic_link = 1` → at least one group in Somatic/Embodied dimension).

**Action for next session:**
1. Read the full schema v3.9.0 against the extract structure
2. For each table in the extract: list all fields; specify the check, terms of reference, and action for each
3. Identify all cross-field and cross-table consistency checks
4. Rewrite Step 1.2 with complete field coverage and explicit terms of reference
5. Present corrected Step 1.2 for researcher review

---

### T-2A — Draft Stage 2a: Comprehensive analysis → Observations log
**Depends on:** T-02A CONFIRMED AND T-02B CONFIRMED
**Status:** PENDING — blocked until both T-02A and T-02B confirmed

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

### T-GATE — Draft schema readiness gate
**Depends on:** T-SC ✓
**Status:** PENDING

---

### T-08 — Nine gap candidates (C-1 through C-9)
**Nature:** Researcher decision — independent
**Status:** PENDING — researcher decision required

| Code | Proposed direction |
|---|---|
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

## Task Dependency Map

```
T-00/T-01/T-SC/T-POP ── ALL COMPLETE
    │
T-02A (Steps 1.3a–1.5) ── COMPLETE — under researcher review
T-02B (Step 1.2 rebuild) ── PENDING — correction required
    │
    ▼ (both T-02A AND T-02B confirmed)
T-2A (Stage 2a: observations log)
    │
    ▼
T-2B (Stage 2b: Q&A partitioning)
    │
    ▼
T-2C (Stage 2c: analytic word output)
    │
    ▼
T-CL (closure)

T-GATE — independent (T-SC done)
T-08 — independent (researcher decision)
T-09 — depends on all
```

---

## Open Items

| Ref | Item | Owner | Blocking |
|---|---|---|---|
| T-02B | Step 1.2 correction — 3 problems | Claude AI (next session) | T-2A |
| T-02A | Researcher review of Steps 1.3a–1.5 | Researcher | T-2A |
| T-08 | Nine gap candidates C-1–C-9 | Researcher | Catalogue supplementary rows |

---

## Status Summary

| Task | Description | Depends on | Status |
|---|---|---|---|
| T-00 | Schema analysis | — | COMPLETE |
| T-01 | Structural insertion point | — | CONFIRMED |
| T-SC | Schema directive + CC | T-00, T-01 | COMPLETE |
| T-POP | Populate tables | T-SC | COMPLETE |
| T-02A | Stage 1: Steps 1.3a–1.5 | T-01, T-SC, T-POP | COMPLETE — researcher review |
| T-02B | Stage 1: Step 1.2 rebuild | T-SC | PENDING — correction required |
| T-2A | Stage 2a: observations log | T-02A+B | PENDING — blocked |
| T-2B | Stage 2b: Q&A partitioning | T-2A | PENDING |
| T-2C | Stage 2c: analytic word output | T-2B | PENDING |
| T-CL | Closure checklist | T-2C | PENDING |
| T-GATE | Schema readiness gate | T-SC | PENDING |
| T-08 | Nine gap candidates | — | PENDING — researcher decision |
| T-09 | Final instruction close | All | PENDING |

---

*End of wa-global-sessionb-update-tasklist-v1_10-20260416.md*
*Supersedes wa-global-sessionb-update-tasklist-v1_9-20260416.md*
*Target instruction output: wa-global-sessionb-instruction-v5_1-20260416.md*
