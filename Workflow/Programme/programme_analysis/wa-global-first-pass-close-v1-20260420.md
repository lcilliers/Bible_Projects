# First-Pass Close — Programme Control v1 — 2026-04-20

| Field | Value |
|---|---|
| Filename | wa-global-first-pass-close-v1-20260420.md |
| Purpose | Close out first pass through the 6 pick-up actions (P, Q, S, U, R, T); capture observations + queue for pass 2 |
| Methodology | Per researcher direction 2026-04-20: "complete the first full pass through all the validations and checks … then do another pass if needed … capture the observations and corrections that is necessary to do, before the next pass" |
| Programme control | [wa-global-programme-control-v1-20260420.md](wa-global-programme-control-v1-20260420.md) |
| Produced | 2026-04-20 |

---

## 1. Pass-1 action outcomes

| Code | Action | Pass-1 outcome | Artefact(s) |
|---|---|---|---|
| **P** | Formal banking of 5 BANKED registries | **CLOSED** ✓ | [wa-global-banked-registries-summary-20260420.md](reports/wa-global-banked-registries-summary-20260420.md) + 4 per-registry completion records |
| **Q** | Path 1 remediation patch for 179 items | **CLOSED 2026-04-20 evening** — pivoted to evidence-flag redesign; M29/M30/M31 applied live (schema 3.10.0 → 3.11.0); 12 Q-COV catalogue questions + junction + Session A inlining + wa-reference v5.7 | [coverage-flags-redesign-v1-20260420.md §13-§14](investigations/coverage-flags-redesign-v1-20260420.md) |
| **S** | Session A extract generator | **CLOSED** ✓ | [scripts/generate_session_a_extract.py](../scripts/generate_session_a_extract.py) + 5 generated extracts + [action-s-close-20260420.md](reports/wa-global-action-s-close-20260420.md) |
| **U** | C01 Dimension Review directive + extract handoff | **CC READY — awaiting AI return** | [wa-dim-C01-handoff-kickoff-v1-20260420.md](../Sessions/Session_B/05_Dimension_Review_logs/wa-dim-C01-handoff-kickoff-v1-20260420.md) + 3 C01 extracts |
| **R** | mti_terms deduplication migration design | **DESIGN DRAFTED — awaiting approval** | [mti-terms-dedup-design-v1-20260420.md](investigations/mti-terms-dedup-design-v1-20260420.md) |
| **T** | SUBPROCESS_NEEDED cohort framework (154 registries) | **FRAMEWORK DRAFTED — awaiting approval** | [subprocess-cohort-framework-v1-20260420.md](investigations/subprocess-cohort-framework-v1-20260420.md) |

**Pass-1 coverage:** 6 actions attempted, 2 fully closed, 1 CC-ready/handed-off, 3 in designed-awaiting-approval state (right pattern — these are multi-day executions that need researcher gate approval first).

---

## 2. Observations captured during pass 1

Observations that didn't block pass 1 but need attention before / during pass 2.

### 2.1 Schema + data observations

| # | Observation | Source | Priority | Pass-2 action |
|---|---|---|---|---|
| O-1 | `prose_section_type` Session A seed has chapters 3/4 labels swapped vs approved design | Action S build | LOW | OT-DBR-014 — researcher-approved SQL label swap |
| O-2 | 44 `wa_dimension_index` rows have `dominant_subject='NONE'` (semantic error, should be HUMAN/GOD/etc.) | Action Q investigation | MEDIUM | OT-DBR-012 — subset resolved by Action U (C01); rest via Action T Wave 3 |
| O-3 | Session A advice doc §3 field lists don't match live schema in ~11 places | Action S build | LOW | Optional refresh of advice doc; generator handles reality |
| O-4 | `engine/flag_engine.py` SMALL_VERSE_SAMPLE uses absolute threshold; pilot uses ratio-based check — mismatch | Action Q investigation | ABSORBED into M29 | Fix in M29 coverage redesign |
| O-5 | `wa_term_inventory.evidential_status` sparsely populated (155 of 7,164 rows); judgment-implying vocabulary | Coverage-flag redesign | MEDIUM | Decide retire vs redefine in M29 (question §7.3-3) |

### 2.2 Process / pattern observations

| # | Observation | Source | Priority | Pass-2 action |
|---|---|---|---|---|
| O-6 | 3 pilot Path 1 misclassifications found in 2 days (OT-DBR-010 + OT-DBR-011 + OT-DBR-012) | Action Q | MEDIUM | OT-DBR-013 — systematic audit of pilot Path 1 emitters |
| O-7 | Directive format is CC→Claude-AI centric; Action U needed a CC→Claude-AI "handoff kickoff" that doesn't fit the 5-element directive template | Action U | LOW | Consider adding a "handoff-kickoff" type alongside the directive type in wa-directive-instruction |
| O-8 | Style lint warnings (MD060 table alignment) appear across most outputs today; lint is consistent but noisy | All actions | LOW | Optional: fix table style programme-wide; or suppress MD060 per project |
| O-9 | Session A extract regeneration creates large `.md` files (~10-20k words each). Reading flow is good; FTS5 search will be the primary machine entry point | Action S validation | INFORMATIONAL | None — expected |

### 2.3 User-raised observations (captured for reference)

| # | Observation | Raised | Status |
|---|---|---|---|
| O-10 | Session A "raises more questions in my mind" | User 2026-04-20 afternoon | Open — user will communicate questions at their pace |
| O-11 | Coverage flags should inform approach, not gate inclusion (volume ≠ value) | User 2026-04-20 morning | ABSORBED — GR-EVIDENCE-001/002/003 drafted for next `wa-global-general-rules` version |
| O-12 | Absence of expected evidence is itself a research signal | User 2026-04-20 | ABSORBED — core reframe of NO_VERSES → VERSE_EVIDENCE_MINIMAL + Q-COV-01..04 |
| O-13 | Term introduction-source is not tracked; missed analytical signal | User 2026-04-20 | ABSORBED — M30 design in coverage-flags-redesign-v1 §4.8 |
| O-14 | Flag-triggered research routes should exist | User 2026-04-20 | ABSORBED — M29 design §4.7 research actions |
| O-15 | Evidence-triggered questions should flow into question catalogue | User 2026-04-20 | ABSORBED — M31 design §4.9 junction table |

---

## 3. Outstanding tasks register — state after pass 1

Updated from OT register 2026-04-19 baseline + pass-1 additions.

| ID | Status | Priority | Source | Note |
|---|---|---|---|---|
| OT-DBR-001 | RESOLVED (2026-04-19) | — | audit_word rewrite | |
| OT-DBR-002 | RESOLVED (2026-04-19) | — | audit.py cleanup | |
| OT-DBR-003 | RESOLVED (2026-04-19) | — | apply_session_patch PROSE ops | |
| OT-DBR-004 | RESOLVED (2026-04-19) | — | build_dimension_extract post-DBR joins | |
| OT-DBR-005 | OPEN | LOW | word_full_extract.py update | Pass-2 optional |
| OT-DBR-006 | PARTIAL | — | Script archival | Mostly done |
| OT-DBR-007 | OPEN | LOW | create_tables.sql consumer validation | Pass-2 optional |
| OT-DBR-008 | OPEN | LOW | M26b CHECK constraint application | Pass-2 optional |
| **OT-DBR-009** | **DESIGN (Action R)** | **HIGH** | mti_terms dedup | **Pass-2 execution after §9 approval** |
| OT-DBR-010 | RESOLVED (2026-04-19) | — | Pilot XREF join fix | |
| OT-DBR-011 | OPEN → **ABSORBED into M29** | MEDIUM | SMALL_VERSE_SAMPLE classifier mismatch | Resolved in M29 design |
| OT-DBR-012 | OPEN | MEDIUM | dominant_subject='NONE' misclassification | Partly resolved by Action U; rest via Action T |
| OT-DBR-013 | OPEN | LOW | Full audit of pilot Path 1 classifier sites | Pass-2 preventative |
| OT-DBR-014 | OPEN | LOW | prose_section_type Session A seed label swap | Pass-2 researcher-approved SQL UPDATE |

**End-of-pass-1 profile:** 1 HIGH (designed), 3 MEDIUM (2 absorbed, 1 in-progress), 4 LOW (optional), 5 RESOLVED.

---

## 4. Pass-2 queue — prioritised

Pass 2 is the execution / decision loop over items designed in pass 1. Organised by what unblocks what.

### 4.1 Decisions needed from researcher (unblocks execution)

**All require researcher review of the linked design docs.**

| Queue item | Document | Open questions | Unblocks |
|---|---|---:|---|
| D1. Coverage-flag redesign (M29/M30/M31) | [coverage-flags-redesign-v1-20260420.md](investigations/coverage-flags-redesign-v1-20260420.md) §7.2 + §7.3 | 9 | M29 migration execution + Action Q resolution |
| D2. mti_terms dedup (M32) | [mti-terms-dedup-design-v1-20260420.md](investigations/mti-terms-dedup-design-v1-20260420.md) §9 | 7 | M32 migration execution (Action R close) |
| D3. SUBPROCESS cohort rollout | [subprocess-cohort-framework-v1-20260420.md](investigations/subprocess-cohort-framework-v1-20260420.md) §10 | 6 | Wave 1 pilot directive execution (Action T kickoff) |
| D4. prose_section_type seed label fix | OT-DBR-014 (in register) | 1 | Clean seed consistency |
| D5. Word synopsis authoring for 5 BANKED | Session A §1.2 placeholders | 5 (1 per BANKED word) | BANKED cohort Stage 1 entry |

### 4.2 CC-executable once decisions received

| Queue item | Dependent on | Effort |
|---|---|---|
| E1. M29 migration implementation + dry-run + live | D1 | ~2 days |
| E2. M30 migration (term_introduction_source) | D1 | ~0.5 day (migration only; backfill is separate) |
| E3. M31 migration (flag-question junction) | D1 + researcher catalogue questions authored | ~0.5 day |
| E4. M32 migration (mti_terms dedup) | D2 | ~2-3 days |
| E5. Apply 5 Session A patches to DB | D5 (word_synopsis authored) | ~10 min |
| E6. OT-DBR-014 seed label swap | D4 | ~2 min (single UPDATE with backup) |
| E7. Wave 1 pilot directive execution (r188) | D3 | ~0.5 day |

### 4.3 Claude AI → CC returns awaited

| Queue item | State | Effort on receipt |
|---|---|---|
| A1. C01 DimReview patches (r112 + r183) | Handoff complete; awaiting Claude AI Phase A/B/C | CC applies patches + validates + status-stamp (~30 min) |

### 4.4 Pass-2 observations already absorbed

Six user-raised observations O-11 through O-15 are already captured in pass-1 design docs. No separate pass-2 action needed — they surface when the respective design docs execute.

---

## 5. Recommended pass-2 opening sequence

If the researcher wants a sequenced kickoff for tomorrow or next session:

1. **Review one Session A extract** (r62 fellowship) to validate pass-1 S output — already suggested but not formally confirmed
2. **Approve D4** (OT-DBR-014 seed swap) + execute E6 — 5 minute close-out
3. **Approve D2** (mti_terms dedup §9 decisions) — R is the biggest cleanup and clears OT-DBR-009 HIGH
4. **Parallel: approve D1** (coverage-flag redesign) — bigger design space; can absorb async
5. **Approve D3 + execute E7** (Wave 1 pilot) — validates the directive pattern end-to-end
6. **Await A1** (C01 DimReview returns) — no CC action needed until Claude AI returns patches
7. **Author D5** (5 word synopses) when researcher has bandwidth — enables E5 and M4 close for BANKED cohort

This sequence sets up pass 2 to run 5-7 working days and close all HIGH+MEDIUM items in the register.

---

## 6. Programme state at end of pass 1

**Schema:** 3.10.0 (stable since 2026-04-19)

**Banking scorecard:** 5 BANKED (formally), 12 STRUCTURALLY_CLEAN, 9 P1_REMEDIATION (about to collapse under M29), 154 SUBPROCESS_NEEDED (framework queued), 30 UNPROCESSED

**Open HIGH items:** 1 (OT-DBR-009 — designed; pending approval)

**Macro step readiness:**

| Macro | State | Blocker |
|---|---|---|
| M1 DB integrity/consistency | 95% (M29 + M32 pending approval) | Researcher decisions D1 + D2 |
| M2 VC reruns | Queued (T Wave 2) | D3 approval |
| M3 DimReviews | In progress (Action U handoff + T Wave 3) | Claude AI cycle + D3 approval |
| M4 Session A prose | **Unblocked.** Generator works; patches ready | D5 researcher authoring |
| M5 Session B prose | Blocked on M4 + AI | — |
| M6 Session D prose | Blocked on M5 + AI | — |
| M7 Session C prose | Blocked on M5+M6 + AI | — |

**The programme is in an unusually good state.** Every macro step has either moved forward or has a clear, scoped unblocker.

---

## 7. Close of pass 1

All 6 pick-up actions processed. Observations captured. Pass-2 queue organised by decision / execution / handoff. Control document updated.

Pass 2 waits on researcher decisions D1–D5 (plus the one already-flagged A1 Claude AI return).

---

*First-pass close — 2026-04-20.*
