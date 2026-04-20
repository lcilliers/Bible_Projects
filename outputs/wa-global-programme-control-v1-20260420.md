# Programme Control — v1 — 2026-04-20

| Field | Value |
|---|---|
| Filename | wa-global-programme-control-v1-20260420.md |
| Purpose | Single source of truth for programme macro sequence + active action queue |
| Opened | 2026-04-20 (day after DB-wide review completion) |
| Discipline | Updated at each action close; version increment at session boundary |
| Governs | CC near-term queue (6 pick-up actions) + macro programme roadmap |

---

## 1. Macro programme sequence (researcher direction — 2026-04-20)

The programme advances through seven macro steps, executed in dependency order. Step 1 is the foundation (now complete or near-complete); steps 2–3 are remediation runs across the registry cohort; steps 4–7 build the analytical output layer (Session A → B → D → C).

| # | Macro step | Responsibility | Status 2026-04-20 |
|---:|---|---|---|
| M1 | Clear all database integrity and consistency issues | CC-led (mechanical) + researcher approvals | **Mostly complete.** DB-wide review done (schema 3.10.0). Open: Path 1 remediation (179 items), OT-DBR-009 (mti_terms dedup). |
| M2 | Rerun / complete all outstanding Verse Context runs | CC-orchestrated directives → Claude AI classifies → CC applies VC patches | **Pending.** 32 registries VC not Complete (30 UNPROCESSED + 2 In Progress). |
| M3 | Complete all outstanding Dimension Reviews | CC directive → Claude AI reviews → CC applies DIMREVIEW patch | **Partially in progress.** C17 complete. 20 clusters still to process. C01 is next (U). |
| M4 | Populate Session A prose | CC builds `generate_session_a_extract.py` → PROSE patches; researcher authors `word_synopsis` | **Pending — tooling gap.** S is the unblocker. |
| M5 | Use Session A as substrate for Session B prose | Claude AI consumes Session A extract; produces Session B Stage 2a/2b/2c prose; CC applies PROSE + SESSIONB patches | **Blocked on M4.** |
| M6 | Use Session B + finding pool to generate Session D prose | Claude AI performs cross-registry synthesis (pointer clustering); CC applies SESSIOND patches | **Blocked on M5.** |
| M7 | Use Session B + D as substrate for Session C (reader-facing final articulation) | Claude AI produces 6-chapter word study; CC applies PROSE patches | **Blocked on M6.** Note: despite the letter-sequence C ahead of D, C comes LAST — it is the final reader-articulation built on both Session B (per-word analytical output) and Session D (cross-registry synthesis). |

**Key dependency:** M4 (Session A) is the bottleneck. Once `generate_session_a_extract.py` exists, the 5 BANKED + 12 STRUCTURALLY_CLEAN registries can flow immediately through M5 → M6 → M7.

---

## 2. Active action queue — pick-up points from 2026-04-19 day report

These are the six CC-executable actions carried forward from end-of-day 2026-04-19. Ordered by estimated effort (ascending). Execute in sequence unless blocked.

| Code | Action | Serves macro step | Effort | Status |
|---|---|:---:|---|---|
| **P** | Formal sweep completion records for the 5 BANKED registries | M1 close-out | ~30 min | **CLOSED — 2026-04-20** ✓ |
| **Q** | Build Path 1 remediation patch for 179 items across affected registries | M1 | half-day | **PAUSED — 2026-04-20.** Investigation found all 179 are pilot misclassifications; broader issue surfaced: coverage/volume flag family needs programme-level redesign per researcher principle (volume ≠ value). Design note: [coverage-flags-redesign-v1-20260420.md](outputs/investigations/coverage-flags-redesign-v1-20260420.md). Q blocked pending §7 decisions on redesign. OT-DBR-011 absorbed; OT-DBR-012 independent. |
| **U** | Claude AI Dimension Review on C01 (r112 mind, r183 heart) — directive + extract handoff | M3 | CC build ~1h then handoff | **CC READY — 2026-04-20** — handoff kickoff + 3 extracts produced; awaiting Claude AI Phase A/B/C + DIMREVIEW patches back to CC |
| **S** | Build `generate_session_a_extract.py` | M4 unblocker | ~1 day engineering | **CLOSED — 2026-04-20** ✓ |
| **R** | Design OT-DBR-009 mti_terms deduplication migration (tentatively M32) | M1 | ~2–3 days | **DESIGN DRAFT — 2026-04-20.** Design produced: [mti-terms-dedup-design-v1-20260420.md](outputs/investigations/mti-terms-dedup-design-v1-20260420.md). Strategy: 6-phase migration (canonical map → FK repoint → integrity verify → hard-delete ~3,616 rows → UNIQUE index → status stamp). 7 §9 decisions queued for researcher. Execution awaiting approval. |
| **T** | Process SUBPROCESS_NEEDED cohort (154 registries, starting with span-failure batch of 86) | M2 + M3 | multi-day ongoing | **FRAMEWORK — 2026-04-20.** Design produced: [subprocess-cohort-framework-v1-20260420.md](outputs/investigations/subprocess-cohort-framework-v1-20260420.md). 1,361 P2 findings across 3 directive families (A span-failure 902; B zero-extraction 254; C DimReview 205). All unblocked. Three-wave rollout proposed; pre-drafted pilot directive for r188 weeping. 6 §10 decisions queued. |

### 2.1 Pick-up → macro step mapping

```
M1 (DB integrity) ─┬─ P  close out 5 BANKED (housekeeping)
                   ├─ Q  Path 1 remediation patch
                   └─ R  mti_terms dedup migration

M2 (VC runs)      ─── (subset of T)
M3 (Dim reviews)  ─┬─ U  C01 dim review (first non-C17 cluster)
                   └─ T  programme cohort via directives
M4 (Session A)    ─── S  extract generator
M5 (Session B)    ─── requires M4 + AI
M6 (Session D)    ─── requires M5 + AI
M7 (Session C)    ─── requires M5 + M6 + AI
```

### 2.2 Stop-the-line rules

- **Any action that would modify >10 rows** stops for researcher approval before commit (per auto-mode §5).
- **Any unresolved OT finding that could cause data corruption** stops the queue (as OT-DBR-009 is currently gating further Path 1 XREF operations until the dedup migration lands).

---

## 3. Quick status — as at 2026-04-20 morning

- Schema version: 3.10.0 (stable since 2026-04-19)
- Outstanding tasks: 1 HIGH open (OT-DBR-009), 3 LOW open (OT-DBR-005, 007, 008)
- Banking scorecard: 5 BANKED, 12 STRUCTURALLY_CLEAN, 9 P1_REMEDIATION, 154 SUBPROCESS_NEEDED, 30 UNPROCESSED
- Day report referenced: [outputs/reports/wa-global-day-report-20260419.md](outputs/reports/wa-global-day-report-20260419.md)
- Scorecard v2 referenced: [outputs/reports/wa-global-readiness-scorecard-v2-20260419.md](outputs/reports/wa-global-readiness-scorecard-v2-20260419.md)
- Outstanding tasks register: [outputs/wa-global-outstanding-tasks-v1-20260419.md](outputs/wa-global-outstanding-tasks-v1-20260419.md)

---

## 4. Action close register

Each action, on close, produces (a) a completion record or patch artefact, (b) an entry in this register, and (c) an update to the relevant macro-step status line in §1.

| Closed | Code | Artefact(s) | Macro step advanced |
|---|---|---|---|
| 2026-04-20 | **P** | Summary: [wa-global-banked-registries-summary-20260420.md](outputs/reports/wa-global-banked-registries-summary-20260420.md); per-registry: wa-035, wa-134, wa-206, wa-207 sweep-completion-20260420.md (r62 completed 2026-04-19) | M1 close-out: 5 registries formally banked (51 OWNER, 10 XREF, 367 verses) — first cohort ready for M4→M5 pilot |
| 2026-04-20 | **Q** | Investigation: [action-q-path1-investigation-20260420.md](outputs/investigations/action-q-path1-investigation-20260420.md); design expansion: [coverage-flags-redesign-v1-20260420.md](outputs/investigations/coverage-flags-redesign-v1-20260420.md); OT-DBR-011/012/013 raised | M1: Q paused — 179 "Path 1" items found to be pilot misclassifications; triggered broader evidence-flag redesign per researcher principle (volume ≠ analytical value). M29/M30/M31 migrations scoped. |
| 2026-04-20 | **S** | Script: `scripts/generate_session_a_extract.py` (~1,105 lines); 5 Session A extracts generated (r35, r62, r134, r206, r207 — total ~76k words); close record: [wa-global-action-s-close-20260420.md](outputs/reports/wa-global-action-s-close-20260420.md); OT-DBR-014 raised | **M4 unblocked.** Generator produces 6 sections per registry from live DB; outputs PROSE_SECTION-marker .md + optional JSON PROSE patch. BANKED cohort now one step (researcher-authored `word_synopsis`) from flowing into Stage 1. |
| 2026-04-20 | **U** | CC portion complete. Kickoff doc: [data/imports/WA/Session_B_Dimension_Review/wa-dim-C01-handoff-kickoff-v1-20260420.md](data/imports/WA/Session_B_Dimension_Review/wa-dim-C01-handoff-kickoff-v1-20260420.md); 3 C01 extracts in `data/exports/dimension_review/` (275 cluster groups, 29 SB findings, 37 SD pointers, 61 roots). Awaiting Claude AI Phase A/B/C + 2 DIMREVIEW patches (r112, r183). | M3: C01 DimReview kicked off. Targets r112 mind (73 groups) + r183 heart (59 groups). Remaining 4 C01 registries already Complete. No blockers. |
| 2026-04-20 evening | **U Phase A** | Phase A observations received from Claude AI (`wa-dim-c01-observations-v1_0-20260420.md`). Incoming analysis: [dim-c01-phase-a-incoming-analysis-20260420.md](outputs/investigations/dim-c01-phase-a-incoming-analysis-20260420.md). Bundle regenerated via new `build_dimension_extract.py --bundle` (adds DV-1..DV-5 pre-checks + override block + handoff production). OT-DBR-015 (vocabulary vintage, 265/275 legacy labels) + OT-DBR-016 (rootfamily false-positive reporting) raised. | M3: Phase A clean. Phase B+C await next Claude AI session. Generator enhanced for standard handoff production. |
| 2026-04-20 late | **U Phase C r112** | r112 patch applied (v2 — OP-075 removed pre-apply per FF-11 schema-compat check — targeted dropped column `wa_dimension_index.context_description`). All 73 r112 groups now on current §7.7 vocabulary; 4 new SB findings + 5 SD pointers inserted; registry stamped Complete. FF-1..FF-11 all PASS. Applicator library fix: `record`/`values` key acceptance harmonised. Verification: [wa-dim-C01-reg112-post-apply-verification-20260420.md](outputs/reports/wa-dim-C01-reg112-post-apply-verification-20260420.md). Directive DIR-20260420-001 executed — r183 verse-extract results in [wa-183-heart-dirresult-001-phaseb-verify-v1-20260420.md](outputs/wa-183-heart-dirresult-001-phaseb-verify-v1-20260420.md) — **halt condition engaged for group 2763 (0 surviving verses)**. r183 Phase C blocked pending researcher disposition of group 2763. | M3 partial: r112 DR=Complete; r183 awaits. OT-DBR-015 now concrete — Option 1/2/3 decision pending. DV-6..DV-9 pre-check candidates captured. |
| 2026-04-20 | **R** | Design: [mti-terms-dedup-design-v1-20260420.md](outputs/investigations/mti-terms-dedup-design-v1-20260420.md) — 6-phase migration plan, 7 open decisions for researcher. Tentatively M32. Not executed. | M1: OT-DBR-009 scoped and designed. Clears the only remaining HIGH-priority open OT. |
| 2026-04-20 | **T** | Framework: [subprocess-cohort-framework-v1-20260420.md](outputs/investigations/subprocess-cohort-framework-v1-20260420.md) — 3-directive-family taxonomy, 3-wave rollout plan, pre-drafted pilot directive for r188 weeping. 6 open decisions for researcher. Not executed. | M2 + M3: 154-registry cohort scoped. All three families unblocked. ~8-10 working days of tractable work queued. |

---

## 5. Next session / day planning

Opens the day by validating (a) the previous close register; (b) whether any stop-the-line condition is active; (c) selecting the next PENDING action by dependency order.

---

*v1 opened 2026-04-20. Will increment to v1.1 at session close.*
