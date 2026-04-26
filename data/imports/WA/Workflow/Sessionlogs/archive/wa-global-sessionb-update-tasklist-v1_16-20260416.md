# WA — Session B Instruction Update: Task List and Control Document
**Filename:** wa-global-sessionb-update-tasklist-v1_16-20260416.md
**Date:** 2026-04-16
**Version:** v1.16
**Change note (v1.16):** Major architectural decision: Session B instruction split into two separate documents. (1) wa-sessionb-analysis-readiness — Stage 1 only; data validation and preparation; produces clean verified extract and Stage 1 Completion Record. (2) wa-sessionb-analysis-output — Stage 2 only; analysis and narrative; reads from clean extract. Stage 1 Completion Record is the formal handoff between them. Target outputs updated accordingly. T-AR added — assemble and finalise Analysis Readiness document from five completed components. T-09 renamed to T-AO (Analysis Output instruction) and T-FC (final close). T-AR actioned and marked COMPLETE this session.
**Supersedes:** wa-global-sessionb-update-tasklist-v1_15-20260416.md

**Previous output refs:**
- wa-global-sessionb-update-tasklist-v1_15-20260416.md (v1.15)
- wa-global-sessionb-analysis-readiness-v1-20260416.md (T-AR output — Analysis Readiness instruction)

---

## Purpose

Governing control document and analytical record for the Session B instruction update. Maintained in detail to enable reconstruction of the analytical journey from any point.

**Target instruction outputs (revised):**
- `wa-sessionb-analysis-readiness-v1-20260416.md` — Stage 1 instruction (Analysis Readiness)
- `wa-sessionb-analysis-output-v1-20260416.md` — Stage 2 instruction (Analysis Output)

---

## Instruction Split — Decision Record

**Decision made:** 2026-04-16

**Rationale:** Stage 1 and Stage 2 are structurally different in every dimension — purpose, inputs, outputs, failure modes, recovery procedures, completion gates, and worker role. Stage 1 is a data engineering process; Stage 2 is an analytical process. They share only the word being studied and the extract. Keeping them in a single instruction creates context noise, wastes context window, and obscures the clean handoff point.

**Handoff mechanism:** The Stage 1 Completion Record (Step 1.6 Part 3) is the formal bridge. Stage 2 (Analysis Output) requires it as a session start input — specifically: extract version, 7-domain checklist pass confirmation, Path 3 notes count, SD pointer count.

**Naming:**
- Stage 1 instruction: `wa-sessionb-analysis-readiness` — making the word ready for analysis
- Stage 2 instruction: `wa-sessionb-analysis-output` — producing the analytical outputs

**Version management:** Each document has its own independent version chain. The split is v1 of both. The prior monolithic instruction (v5.0) is superseded by both together.

---

## Programme Architecture — Confirmed

**Analysis Readiness (Stage 1):** Data validation and preparation. No analytical conclusions. Six steps. Ends with: verified clean extract + Stage 1 Completion Record + Stage 2 Readiness Declaration. Output document: `wa-sessionb-analysis-readiness-v[n]-[date].md`.

**Analysis Output (Stage 2):**

| Stage | Output | Nature |
|---|---|---|
| Stage 2a | Observations log | Full technical narrative — everything the data says |
| Stage 2b | Q&A log | Question-answer pairs; iterative; multi-session |
| Stage 2c | Analytic word output | Six Session C chapters |

Output document: `wa-sessionb-analysis-output-v[n]-[date].md`.

**Six Session C chapters:** Meaning / How it works / Verses (all anchors + full text + Q&A pairs) / Language / Interrelationships / Open questions (all SD pointers)

---

## Source Material Reference

| Document | Role | Status |
|---|---|---|
| wa-global-sessionb-instruction-v5_0-20260415.md | Prior monolithic instruction — superseded | Reference only |
| wa-global-obs-question-master-catalogue-v2_0-20260415.md | Governing catalogue | Active |
| wa-global-general-rules-v2_2-20260415.json | Global rules | Active |
| database-schema-20260416.json | Schema v3.9.0 | Active |
| wa-global-sessionb-stage1-opening-v1-20260416.md | T-02E — Stage 1 opening section | Incorporated into T-AR |
| wa-global-sessionb-step1-2-v2-20260416.md | T-02C — Step 1.2 v2.0 | Incorporated into T-AR |
| wa-global-sessionb-stage1-draft-v1-20260416.md | T-02A — Steps 1.3a–1.4 | Incorporated into T-AR |
| wa-global-sessionb-stage1-completion-v1-20260416.md | T-02D — Step 1.5 + Step 1.6 | Incorporated into T-AR |
| wa-global-sessionb-analysis-readiness-v1-20260416.md | T-AR output — Analysis Readiness instruction | Active — researcher review |
| wa-103-love-step1-2-audit-v1_1-20260416.md | Love extract audit | Active — reference |
| wa-global-sessionlog-sessionb-redesign-v1-20260416.md | Phase 2 architecture reasoning | Active — load for T-AO |

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

### T-02A — Stage 1: Steps 1.3a, 1.3b, 1.3c, 1.4
**Output:** wa-global-sessionb-stage1-draft-v1-20260416.md
**Status:** COMPLETE — incorporated into T-AR

---

### T-02B — Stage 1: Step 1.2 v1.0 (first rebuild)
**Status:** COMPLETE — superseded by T-02C

---

### T-02C — Stage 1: Step 1.2 v2.0 (full rewrite with resolution framework)
**Output:** wa-global-sessionb-step1-2-v2-20260416.md
**Status:** COMPLETE — incorporated into T-AR

---

### T-02D — Stage 1: Step 1.5 update + Step 1.6 new
**Output:** wa-global-sessionb-stage1-completion-v1-20260416.md
**Status:** COMPLETE — incorporated into T-AR

---

### T-02E — Stage 1 opening section: tracking documents, session management, fallback protocol
**Output:** wa-global-sessionb-stage1-opening-v1-20260416.md
**Status:** COMPLETE — incorporated into T-AR

---

### T-AR — Assemble and finalise Analysis Readiness instruction
**Output:** wa-sessionb-analysis-readiness-v1-20260416.md
**Status:** COMPLETE — awaiting researcher review and confirmation

**What was assembled:** Five components integrated into a single coherent instruction document:
1. Stage 1 opening section (T-02E): purpose, outputs, tracking document structure, session start protocol, fallback protocol, session close protocol
2. Step 1.1: confirm extract version (retained from v5.0 unchanged)
3. Step 1.2 v2.0 (T-02C): full audit with resolution framework, Sections A.0 through H
4. Steps 1.3a, 1.3b, 1.3c, 1.4 (T-02A): flag preparation, findings preparation, B-target clearance, Type (a) patch
5. Step 1.5 updated + Step 1.6 new (T-02D): sub-process triggers, fresh extract, completion verification, handoff

**Editorial work at assembly:**
- Unified voice and tense throughout
- Cross-references between steps resolved (e.g. patch accumulator references consistent throughout)
- Integrity rules consolidated into a single section at the document end (SB-1, SB-18 through SB-24)
- Companion documents section updated: Analysis Readiness loads only what Stage 1 needs; Analysis Output not referenced
- Change log written: supersedes v5.0 Stage 1; principal changes listed
- Header, version, and companion document list aligned to programme conventions
- Step 1.2 resolution path references harmonised with Steps 1.3 and 1.4 (paths named consistently throughout)

---

### T-2A — Draft Stage 2a: Comprehensive analysis → Observations log
**Depends on:** T-AR confirmed by researcher
**Status:** PENDING — ready on researcher confirmation

**What to load at T-2A session start:**
- wa-global-general-rules-v2_2-20260415.json
- wa-global-sessionb-update-tasklist-v1_16-20260416.md
- wa-global-sessionlog-sessionb-redesign-v1-20260416.md (Phase 2 architecture reasoning)
- wa-global-sessionb-analysis-readiness-v1-20260416.md (to understand what Stage 1 provides)

**Content to draft:**
- Session start inputs: Stage 1 Completion Record (required — contains extract version, 7-domain pass, Path 3 notes, SD pointer count); fresh extract; master catalogue JSON extract
- Load sequence: what to read first and why
- Comprehensive analysis process: all data read; free-form; comprehensive; nothing withheld; covers existing 171 findings as input material; thin-evidence flags from Step 1.3a; all existing SD pointers; correlation signals; Path 3 notes from Stage 1
- Observations log structure and conventions
- Sign-off condition: observations log complete, downloaded, confirmed
- Session management: multi-session capable; each session adds to the log; log is fixed after Stage 2a closes

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

### T-GATE — Draft schema readiness gate at Analysis Output session start
**Depends on:** T-SC ✓
**Status:** PENDING
**Note:** Now belongs in the Analysis Output instruction, not Analysis Readiness.

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

### T-AO — Draft and finalise Analysis Output instruction
**Depends on:** T-2A, T-2B, T-2C, T-CL, T-GATE all CONFIRMED
**Nature:** Assemble Stage 2 components into wa-sessionb-analysis-output-v1-[date].md
**Status:** PENDING

---

### T-FC — Final close: update companion documents, global rules references, register both instructions
**Depends on:** T-AR confirmed + T-AO complete
**Nature:** Programme hygiene — register new instructions in programme documentation; update any cross-references; retire v5.0
**Status:** PENDING

---

## Instruction Correction Register

All items resolved. No open items.

| Code | Issue | Status |
|------|-------|--------|
| IC-01 through IC-07 | Seven Step 1.2 corrections from love extract audit | Resolved in T-02C |
| W1–W3 | Three structural weaknesses in Step 1.2 | Resolved in T-02C |

---

## Task Dependency Map

```
T-00/T-01/T-SC/T-POP ── ALL COMPLETE
T-02A/T-02C/T-02D/T-02E ── ALL COMPLETE (incorporated into T-AR)
    │
T-AR (Analysis Readiness instruction assembled) ── COMPLETE — researcher review
    │
    ▼ (T-AR confirmed)
T-2A (Stage 2a: observations log)
    │
    ▼
T-2B (Stage 2b: Q&A partitioning)
    │
    ▼
T-2C (Stage 2c: analytic word output)
    │
    ▼
T-CL (closure checklist + final patch)
    │
    ▼
T-GATE (schema readiness gate — belongs in Analysis Output)
    │
    ▼
T-AO (Analysis Output instruction assembled)
    │
    ▼
T-FC (final close — programme registration)

T-08 (gap candidates) — independent; researcher decision
```

---

## Open Items

| Ref | Item | Owner | Blocking |
|---|---|---|---|
| T-AR | Researcher review and confirmation | Researcher | T-2A |
| T-08 | Nine gap candidates C-1–C-9 | Researcher | Catalogue rows |

---

## Status Summary

| Task | Description | Depends on | Status |
|---|---|---|---|
| T-00 | Schema analysis | — | COMPLETE |
| T-01 | Structural insertion point | — | CONFIRMED |
| T-SC | Schema directive + CC | T-00, T-01 | COMPLETE |
| T-POP | Populate tables | T-SC | COMPLETE |
| T-02A | Stage 1: Steps 1.3a–1.4 | — | COMPLETE — incorporated |
| T-02B | Stage 1: Step 1.2 v1.0 | — | COMPLETE — superseded |
| T-02C | Stage 1: Step 1.2 v2.0 | — | COMPLETE — incorporated |
| T-02D | Stage 1: Step 1.5 + Step 1.6 | — | COMPLETE — incorporated |
| T-02E | Stage 1 opening section | — | COMPLETE — incorporated |
| T-AR | Analysis Readiness instruction | T-02A+C+D+E | COMPLETE — researcher review |
| T-2A | Stage 2a: observations log | T-AR | PENDING — ready on confirmation |
| T-2B | Stage 2b: Q&A partitioning | T-2A | PENDING |
| T-2C | Stage 2c: analytic word output | T-2B | PENDING |
| T-CL | Closure checklist + final patch | T-2C | PENDING |
| T-GATE | Schema readiness gate | T-SC | PENDING |
| T-AO | Analysis Output instruction | T-2A–T-CL+T-GATE | PENDING |
| T-FC | Final close + programme registration | T-AR+T-AO | PENDING |
| T-08 | Nine gap candidates | — | PENDING — researcher decision |

---

*End of wa-global-sessionb-update-tasklist-v1_16-20260416.md*
*Supersedes wa-global-sessionb-update-tasklist-v1_15-20260416.md*
*Target outputs: wa-sessionb-analysis-readiness-v1-20260416.md + wa-sessionb-analysis-output-v1-20260416.md*
