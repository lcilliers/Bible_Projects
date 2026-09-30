# Instructions folder — archival proposal & action log (2026-07-08)

> Cleanup of `Workflow/Instructions/`. Every classification is grounded in the **written record** (each doc's own status banner, or an explicit "retired by" in a present successor), not inference. Archive target per file-org-rules §3.10: `Workflow/Instructions/archive/`. **Batch A moved this session; Batch B awaits researcher confirmation.**

## Batch A — ARCHIVED THIS SESSION (self-declared superseded/retired; successor present)
These need no judgement — the documents (or a present successor) explicitly retire them.

| file | written-record basis |
|---|---|
| `wa-passage-completeness-rule-v1-20260707.md` | self-banner: "SUPERSEDED 2026-07-08 by v2" |
| `wa-audit-framework-design-v0_1-20260526.md` | self-banner: "SUPERSEDED (2026-06-14) by wa-cluster-audit-design-v1"; was DRAFT, never ratified |
| `wa-v3-publication-pipeline-design-v1-20260527.md` | retired by `wa-cluster-publishing-instruction-v1_0` §9 |
| `wa-sessionc-cluster-style-method-v1_1-20260512.md` | retired by `wa-cluster-publishing-instruction-v1_0` §9 |
| `wa-sessionc-cluster-ch1-instruction-v1_0-20260512.md` | retired by `wa-cluster-publishing-instruction-v1_0` §9 |
| `wa-sessionc-cluster-ch2-instruction-v1_0-20260512.md` | " |
| `wa-sessionc-cluster-ch3-instruction-v1_0-20260512.md` | " |
| `wa-sessionc-cluster-ch4-instruction-v1_0-20260512.md` | " |
| `wa-sessionc-cluster-ch5-instruction-v1_0-20260512.md` | " |
| `wa-sessionc-cluster-ch6-instruction-v1_0-20260512.md` | " |
| `wa-sessionc-cluster-ch7-instruction-v1_0-20260512.md` | " |
| `wa-sessionc-cluster-appendices-instruction-v1_0-20260512.md` | retired by `wa-cluster-publishing-instruction-v1_0` §9 |

## Dimension-authority resolution (2026-07-08, researcher-decided)
The reset doc was pulled from Batch B and investigated (see chat + docs). Outcome:
- **Authoritative dimension source = `wa-ve-lexical-catalogue-v1-20260702`** (07-02 catalogue) + the 07-02 method that drives it. Not the reset.
- **Option (A) taken:** the cycle §3 now **cites** the catalogue; the catalogue gained a **ve_nr master list (§9)** completing it with `specifier(110)` + `locus(116)`; the reset's governing **principles P0–P8 + discovery-lookout** were folded into the cycle as **§3A**.
- **`wa-lexical-analysis-rules-reset-v1` → CLOSED & ARCHIVED** (content morphed into current docs; provenance banner added). Moved to `Workflow/Instructions/archive/`.
- **`wa-synthesis-B-spec-reset-v1` → KEEP** (researcher: still relevant, albeit stale) — the assembly half. Removed from any archive consideration.

## Batch B — ✅ ARCHIVED 2026-07-08 (researcher approved: "yes Batch B can be archived")
All 20 files below moved to `Workflow/Instructions/archive/`. The three caution-flagged docs (`wa-sessionc-cluster-overview`, `wa-findings-audit-spec`, `wa-word-study-template`) were archived **with caution** per explicit blanket approval — recoverable in one `git mv` from archive if any proves still-live. Active Instructions folder now holds **only Batch C** (13 docs). Archive holds 35.

## Batch B — the archived set (was: recommend-archive)
Made legacy by the **2026-06-25 RESET** (characteristics→movements) and the **2026-07-02 verse-first / 2026-07-08 authoritative-cycle** shift, which closed the characteristic/faculty/tier/logical-unit framing and the Session A/B/C/D + cluster-publication pipeline. They are **not** self-declared superseded and some are still name-referenced in the (lagging) CLAUDE.md §10, so I have not moved them.

| file | why legacy | caution |
|---|---|---|
| `wa-sessionb-cluster-instruction-v3_0-20260527.md` | self-banner "SUPERSEDED (2026-06-14)… Archiving pending" | its §7 assembler-interface pointer is cited by others |
| `wa-cluster-rollup-instruction-v3_2-DRAFT-20260607.md` | DRAFT, never ratified; the v3_2 rollup is an open draft item | — |
| `wa-cluster-publishing-instruction-v1_0-20260530.md` | publication parked (finding-centric model) | it is the successor that retires Batch A — keep until Batch A is archived, then archive |
| `wa-cluster-dos-and-donts-v1_2-20260621.md` | cluster-essay era | — |
| `wa-cc-cluster-essay-style-template-v1_0-20260620.md` | cluster-essay era | — |
| `wa-sessionc-cluster-overview-v1_0-20260513.md` | cluster publication | **kept as assembler interface** per sessionb-cluster §7 — confirm before archiving |
| `wa-findings-audit-spec-v1_0-20260621.md` | pre-reset finding audit | memory `project_findings_audit_gate_live` — audit gate may still apply; **lean KEEP** |
| `wa-sessionb-analysis-output-v1_8-20260430.md` | Session B per-word pipeline (legacy) | — |
| `wa-sessionb-analysis-readiness-v1_10-20260501.md` | Session B per-word pipeline (legacy) | — |
| `wa-sessiond-orientation-v3_2-20260418.md` | Session D moot (memory `project_session_d_moot`) | — |
| `wa-dimensionreview-instruction-v3_3-20260418.md` | dimension review eliminated 2026-05-04 (CLAUDE.md §10) | — |
| `wa-versecontext-instruction-v3_10-20260425.md` | verse_context legacy, not used by new cycle (linkage map §8) | verse_context table still exists |
| `wa-sessiona-prose-instruction-v1_0-20260427.md` | prose publication parked | — |
| `wa-global-sessionc-prose-rule-v1_1-20260414.md` | draft rule for Session C (parked) | — |
| `wa-global-readiness-sweep-instruction-v1_0-20260419.md` | pre-cluster readiness sweep | — |
| `wa-v2_9-vs-v3_0-cycle-comparison-v1-20260527.md` | v3_0 design-phase analysis (historical) | — |
| `wa-v3_0-final-review-v1-20260527.md` | v3_0 design-phase analysis (historical) | — |
| `wa-v3_0-phase-b-control-design-v1-20260527.md` | v3_0 design-phase analysis (historical) | — |
| `wa-Session-A-Instruction-v8-final.docx` | Session A (legacy); also a stray `.docx` in a `.md` folder | — |
| `wa-word-study-template-v2.1-20260414.md` | word-study output template | onboarding may still use it — **confirm** |

## Batch C — KEEP (current live method + operational infrastructure)
| file | role |
|---|---|
| `wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md` | ★ live lexical cycle |
| `wa-passage-completeness-rule-v2-20260708.md` | ★ live passage rule (Stage 0) |
| `wa-per-book-corrective-method-authoritative-v1-20260707.md` | ★ live per-book pipeline |
| `wa-gate1-span-orphan-audit-method-rule-v1-20260705.md` | ★ live gate-1 audit |
| `wa-verse-analysis-method-v1-20260702.md` | ★ live verse-first method |
| `wa-narrative-style-instruction-v1-20260702.md` | live narrative style |
| `01b-VE-field-reliability-and-rules.md` | canonical VE generation (SETTLED 2026-06-16) |
| `01c-T2-treatment-and-API-governance.md` | canonical T2/API governance (SETTLED 2026-06-17) |
| `wa-lexical-analysis-rules-reset-v1-20260624.md` | RESET decomposition spec — method substrate (confirm vs 07-08 supersession) |
| `wa-synthesis-B-spec-reset-v1-20260624.md` | RESET assembly spec — method substrate |
| `wa-patch-instruction-v2_11-20260507.md` | operational — patches still applied |
| `wa-directive-instruction-v1_4-20260506.md` | operational — directives still used |
| `wa-claudecode-instruction-v4_5-20260514.md` | operational — CC responsibilities (cluster-era content dated) |
| `wa-operational-governance-v1_0-20260614.md` | operational governance |

## Open questions for the researcher
1. **Confirm Batch B** for archiving (or flag any to keep). Special cases flagged: `wa-sessionc-cluster-overview` (assembler interface), `wa-findings-audit-spec` (audit gate may be live), `wa-word-study-template` (onboarding).
2. `wa-lexical-analysis-rules-reset` / `wa-synthesis-B-spec-reset` (Batch C) — are these still live, or superseded by the 2026-07-08 authoritative cycle? If superseded, they move to B.
3. CLAUDE.md §10 lists several Batch B docs as "authoritative" — it lags the resets and should be refreshed once B is settled.

*Filed 2026-07-08. Batch A moved to `Workflow/Instructions/archive/`; Batch B/C pending.*
