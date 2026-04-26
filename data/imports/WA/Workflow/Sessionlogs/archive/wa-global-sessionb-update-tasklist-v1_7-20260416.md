# WA — Session B Instruction Update: Task List and Control Document
**Filename:** wa-global-sessionb-update-tasklist-v1_7-20260416.md
**Date:** 2026-04-16
**Version:** v1.7
**Change note (v1.7):** T-POP updated — T-POP-A patch produced (PATCH-20260416-GLOBAL-CATALOGUE-POP-V1.json, 194 rows); T-POP-B and T-POP-C extraction directives produced (DIR-20260416-002). T-POP status updated to IN PROGRESS. Execution sequence clarified. Open items updated.
**Supersedes:** wa-global-sessionb-update-tasklist-v1_6-20260416.md

**Previous output refs:**
- wa-global-sessionb-update-tasklist-v1_6-20260416.md (v1.6)
- PATCH-20260416-GLOBAL-CATALOGUE-POP-V1.json (T-POP-A — 194 rows, awaiting CC application)
- wa-global-dir-20260416-002-popbc-extracts-v1-20260416.md (T-POP-B and T-POP-C extraction directives)

---

## Purpose

Governing control document for this session. Updated and version-incremented at each meaningful change point. No task is actioned without appearing in this register and being confirmed by the researcher.

**Session governance rules:**
1. This task list is updated before any new work is reported or downloaded.
2. Each update is a minor version increment.
3. Each Session B instruction update is a separate minor version increment of that document.
4. No work proceeds without task registration and researcher confirmation.
5. Additional session logs may modify tasks — task list updated when this occurs.

**Target instruction output:** `wa-global-sessionb-instruction-v5_1-20260416.md`

---

## Phase 2 Architecture — Confirmed

**Governing principle:** Stage 1 validates and prepares data. Stage 2 analyses and builds the narrative.

| Stage | Output | Nature |
|---|---|---|
| Stage 2a | Observations log | Full technical narrative — everything the data says |
| Stage 2b | Q&A log | Question-answer pairs; iterative; multi-session capable |
| Stage 2c | Analytic word output | Six Session C chapters; replaces Analytical Brief from v5.0 |

**Six Session C chapters:** Meaning / How it works / Verses (all anchors + full text + Q&A pairs) / Language / Interrelationships / Open questions (all SD pointers)

---

## Source Material Reference

| Document | Role |
|---|---|
| wa-global-sessionb-instruction-v5_0-20260415.md | Target document |
| wa-global-session-log-catalogue-findings-v1-20260415.md | Primary change source |
| wa-global-obs-question-master-catalogue-v2_0-20260415.md | Governing catalogue |
| wa-global-general-rules-v2_2-20260415.json | Global rules |
| wa-global-schema-sessionb-changes-v1_1-20260416.md | Schema design authority |
| wa-global-schema-verify-20260416-001-v1-20260416.md | Schema v3.9.0 confirmed |
| PATCH-20260416-GLOBAL-CATALOGUE-POP-V1.json | T-POP-A patch — 194 rows |
| wa-global-dir-20260416-002-popbc-extracts-v1-20260416.md | T-POP-B/C extraction directives |

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
**Status:** COMPLETE — schema v3.9.0 confirmed

---

### T-POP — Populate flags, pointers, and obs_questions tables
**Status:** IN PROGRESS

**T-POP-A — Populate `wa_obs_question_catalogue`**
**Output:** `PATCH-20260416-GLOBAL-CATALOGUE-POP-V1.json` — 194 insert operations
**Status:** PATCH READY — awaiting researcher approval and CC application
**After application:** CC to run Section 3 of DIR-20260416-002 to populate `source_registry_no` for five source words (Grace 147 / Forgiveness 14 / Love 14 / Mercy 11 / Compassion 8)
**Verification:** Row count = 194; `source_registry_no` populated for all 194 rows

**T-POP-B — Populate `wa_finding_catalogue_links` (pre-mapped links)**
**Output:** DIR-20260416-002 Section 1 — extraction directive for CC
**Status:** DIRECTIVE READY — CC to run after T-POP-A confirmed; return findings + catalogue JSON to Claude AI; Claude AI prepares patch
**Note:** Pre-mapped links carry `status = 'suggested'` only — confirmed during Stage 2b per word

**T-POP-C — Align `wa_session_research_flags` B-target flags**
**Output:** DIR-20260416-002 Section 2 — extraction directive for CC
**Status:** DIRECTIVE READY — CC to run after T-POP-A confirmed; return 9 B-target flag rows to Claude AI; Claude AI reviews and prepares alignment patch if corrections required

**Execution sequence for CC:**
1. Apply T-POP-A patch → confirm 194 rows
2. Run Section 3 registry lookup → confirm with Claude AI → apply source_registry_no updates → confirm counts
3. Run Section 1 T-POP-B extract → return JSON to Claude AI
4. Run Section 2 T-POP-C extract → return JSON to Claude AI

---

### T-02 — Draft Stage 1: Steps 1.3a, 1.3b, 1.3c
**Depends on:** T-01 ✓; T-SC ✓; T-POP COMPLETE
**Status:** PENDING

**Step 1.3a — Clear `wa_term_phase2_flags`** (data validation only)
**Step 1.3b — Prepare `wa_session_b_findings` for Stage 2** (question linking + status setting; no analytical reframing)
**Step 1.3c — Clear B-target `wa_session_research_flags`** (hard gate)
**Step renumbering:** Old 1.5 → 1.4; Old 1.6 → 1.5

---

### T-2A — Draft Stage 2a: Comprehensive analysis → Observations log
**Depends on:** T-02 CONFIRMED
**Status:** PENDING

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
**Affects:** T-POP-A count (if adopted, add rows to catalogue patch); T-2B universal question handling
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
T-00 ── COMPLETE
T-01 ── CONFIRMED
T-SC ── COMPLETE
    │
    ▼
T-POP ── IN PROGRESS
  ├── T-POP-A: patch ready → CC applies → source_registry_no updated
  ├── T-POP-B: directive ready → CC extracts → Claude AI patches
  └── T-POP-C: directive ready → CC extracts → Claude AI reviews
    │
    ▼ (T-POP COMPLETE)
T-02 (Stage 1: Steps 1.3a/b/c)
    │
    ▼
T-2A (Stage 2a: observations log)
    │
    ▼
T-2B (Stage 2b: Q&A partitioning + patches)
    │
    ▼
T-2C (Stage 2c: analytic word output)
    │
    ▼
T-CL (closure checklist + final patch)

T-GATE (schema readiness gate) — depends on T-SC only
T-08 (gap candidates) — independent
T-09 (final instruction close) — depends on all
```

---

## Open Items

| Ref | Item | Owner | Blocking |
|---|---|---|---|
| T-POP-A | Researcher approval of PATCH-20260416-GLOBAL-CATALOGUE-POP-V1.json | Researcher | T-POP-B/C |
| T-POP-B/C | CC execution of DIR-20260416-002 after T-POP-A confirmed | CC | T-POP completion |
| T-08 | Nine gap candidates C-1–C-9 | Researcher | T-POP-A supplementary rows |
| T-02 | Researcher confirmation to begin instruction drafting | Researcher | T-2A onward |

---

## Status Summary

| Task | Description | Depends on | Status |
|---|---|---|---|
| T-00 | Schema analysis | — | COMPLETE |
| T-01 | Structural insertion point | — | CONFIRMED |
| T-SC | Schema directive + CC execution | T-00, T-01 | COMPLETE |
| T-POP | Populate tables | T-SC | IN PROGRESS |
| T-02 | Stage 1: Steps 1.3a/b/c | T-01, T-SC, T-POP | PENDING |
| T-2A | Stage 2a: observations log | T-02 | PENDING |
| T-2B | Stage 2b: Q&A partitioning | T-2A | PENDING |
| T-2C | Stage 2c: analytic word output | T-2B | PENDING |
| T-CL | Closure checklist + final patch | T-2C | PENDING |
| T-GATE | Schema readiness gate | T-SC | PENDING |
| T-08 | Nine gap candidates | — | PENDING — researcher decision |
| T-09 | Final instruction close | All | PENDING |

---

*End of wa-global-sessionb-update-tasklist-v1_7-20260416.md*
*Supersedes wa-global-sessionb-update-tasklist-v1_6-20260416.md*
*Target instruction output: wa-global-sessionb-instruction-v5_1-20260416.md*
