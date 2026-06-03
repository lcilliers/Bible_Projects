# v2_4 → v2_5 change summary (DRAFT — for researcher approval)

**Status:** DRAFT FOR APPROVAL. Not loaded as current. Awaiting researcher review and explicit instruction to apply.
**Draft file:** [wa-sessionb-cluster-instruction-v2_5-DRAFT-20260518.md](wa-sessionb-cluster-instruction-v2_5-DRAFT-20260518.md)
**Base:** [wa-sessionb-cluster-instruction-v2_4-20260517.md](../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_4-20260517.md)

This revision incorporates the three Q1/Q2/Q3 directives from the 2026-05-18 review: dispositions consolidated, co-occurrence simplified, BOUNDARY resolution moved before findings.

---

## What v2_5 changes — quick map

v2_5 is **cluster-agnostic**. It embeds three structural corrections into the instruction for all future cluster work, plus a post-closure compliance flow for bringing pre-v2_5 clusters into alignment without re-opening them.

| # | Change | Theme | Section(s) |
|---|---|---|---|
| 1 | **Scope clarification §1.1** — inner being = entire human inner life, no theological narrowing. Explicit in-scope examples spanning vertical/horizontal/self-directed/circumstantial/moral-positive/moral-negative/illicit/sensory/volitional/evaluative registers. | Scope | NEW §1.1 |
| 2 | **§2.8 No-spiritualisation contamination guard** — bias correction in the operating-principle block, alongside the cross-cluster (§2.2) and inherited-structure (§2.3) guards. | Scope | NEW §2.8 |
| 3 | **Phase 1 forbidden SET_ASIDE grounds** — UT classifier rubric must NOT use "no theological framing" / "not God-directed" / "not spiritual" as grounds for set_aside. Only "no inner-being state evidenced" is valid. Explicit pure-human example set added to the rubric. | Scope | §4.2, NEW §4.5.1 |
| 4 | **Phase 3 disallowed BOUNDARY reasons** — constitution debate cannot BOUNDARY a term solely because its corpus lacks God-directed framing. Three valid BOUNDARY reasons listed; disallowed grounds enumerated. | Scope + BOUNDARY | NEW §6.3.1 |
| 5 | **Phase 5 BOUNDARY-is-not-a-parking-lot discipline** — pure-human inner-being content (parental delight, marital joy, refined luxury, illicit pleasure, predatory exultation, cheerful-heart-from-circumstance) belongs in substantive sub-groups, not BOUNDARY. BOUNDARY at Phase 5 carries only verses of BOUNDARY-verdict terms. | Scope + BOUNDARY | NEW §8.4.1 |
| 6 | **Phase 8.5 NEW — BOUNDARY resolution pass (between Phase 8 and Phase 9)** — every BOUNDARY-pending decision resolves to exactly one of three outcomes before catalogue findings author: SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP. Researcher-approved. Gate: 0 pending `BOUNDARY_DECISION_PENDING` flags before Phase 9. Findings then run against the structurally-final corpus. | BOUNDARY + ordering | NEW §11.5 |
| 7 | **Phase 4 co-occurrence simplified to informational discipline** — CC produces a simple "co-occurring terms at this verse_record_id" list when packaging the Phase 4 transfer directive. No AI-driven structured assessment, no `[XCO-...]` notes. The list informs the transfer rationale; cross-cluster relationship findings remain T6's responsibility at Phase 9. | Co-occurrence | NEW §7.3.1 (rewritten) |
| 8 | **§18 NEW — Disposition vocabulary canonical reference** — replaces the previous standalone co-occurrence section. Defines all three disposition vocabularies in one place: term-level (Phase 3), verse-level (Phase 8.5 + audit-fix), inherited-finding-level (Phase 10). Each phase references §18 rather than redefining inline. Cross-cluster co-occurrence is a discipline reminder embedded in the §18.2 ROUTE-TO-CLUSTER definition — informational input only, not a structured workflow. | Disposition consolidation | NEW §18 (replaces old §18) |
| 9 | **Phase 12 closure simplified** — by v2_5 ordering, all checks that can impact findings happen by Phase 8.5. Phase 12 pre-flight reduces to two substantive checks: **§15.2 check 1 (evidence-grounding)** — every E-coded `cluster_finding` row has ≥1 verse / VCG / anchor reference; **§15.2 check 2 (completeness)** — every prompt × scope cell from the catalogue has a row (silent prompts recorded explicitly). "Flagged-for-decision" exit removed. | BOUNDARY + closure | §15 (rewritten) |
| 10 | **NEW §17 Post-closure compliance audit and surgical fix** — when the instruction evolves, closed clusters are NOT re-opened. An audit script reads the cluster's DB state and the current instruction, produces a read-only compliance report, researcher approves a fix list, CC builds targeted fix directives. Cluster status stays `Analysis Completed`. Specific findings, verse routings, and Session C sections are surgically updated. | Post-closure | NEW §17 |

Plus: §16 BOUNDARY lifecycle table updated (Phase 8.5 row); §20 directives table updated (Phase 8.5 row replaces Phase 11.5; audit-fix row); §21 pre/post controls table updated (Phase 8.5 row inserted; Phase 12 row tightened with the two finding-quality checks); §24 change history carries the v2_5 entry.

---

## What v2_5 does NOT change

- **No schema changes.** Phase 8.5 and audit-fix use existing tables (`cluster_subgroup`, `mti_term_subgroup`, `verse_context_group`, `vcg_term`, `verse_context`, `cluster_finding`).
- **No Pass A (Phase 2) rework.** Verse meanings are NEUTRAL by design and remain valid; the bias lived in the synthesis layer only.
- **No Phase 9 (catalogue) restructure.** T6 prompts continue to capture cross-cluster relationship findings. They now author against a structurally-final corpus (Phase 8.5 having resolved BOUNDARY first).
- **No reopening of the 40% distribution gate (§8.6).** v2_4's gate stays as-is.
- **No changes to Phase 7 staged write-out (§10.7), no-sampling checklist (§10.8), or CC validation (§10.9).**
- **No retroactive auto-rerun of closed clusters.** The §17 audit-and-fix flow is researcher-triggered per cluster.
- **No re-opening of closed clusters.** §17 keeps `cluster.status = 'Analysis Completed'` throughout.
- **No structured co-occurrence mechanism.** The previous draft's §18 (AI-driven JOINED_MEANING / STRUCTURAL_SIGNIFICANCE / NO_SECONDARY_ROLE assessment with `[XCO-...]` notes) is dropped. Cross-cluster relationships are captured by T6 catalogue prompts at Phase 9 in both clusters' findings.

---

## Open questions — all resolved

**[OPEN-Q-1]** Phase 8.5 directive packaging — **resolved 2026-05-18: one bundled directive per cluster**, to be tested in practice on M04. If bundling causes overload or quality deterioration (oversized review surface, slow apply, hook timeouts), the researcher may direct a split for subsequent clusters.

*(Earlier open questions were resolved during the refactor: OPEN-Q-2 §18 storage convention dropped with the §18 redesign — no XCO notes mechanism exists. OPEN-Q-3 re-examination sequence dropped with the §17 audit-and-fix redesign — sequence is per-researcher direction at audit time. OPEN-Q-4 cluster_finding revision dropped — defaults to in-place UPDATE with audit prefix in `finding_text`; append-and-supersede available per-directive. OPEN-Q-5 Phase 11.5 timing resolved by the Q3 directive — BOUNDARY resolution moves to Phase 8.5, before findings.)*

---

## Apply path (after approval)

1. **Researcher reviews this summary + the full draft.** Resolves OPEN-Q-1. Marks accepted / amended / rejected for line-level changes.
2. **CC integrates approved amendments** into a clean v2_5 file at `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_5-20260518.md`. The abbreviated `(Unchanged from v2_4)` sections are expanded back to full v2_4 text.
3. **CC archives v2_4** to `Workflow/archive/wa-sessionb-cluster-instruction-v2_4-20260517.md`.
4. **Manifest rebuild + commit + push.**

Once v2_5 is live, downstream activities are separate workstreams — each researcher-directed:

- **M04 finalisation under v2_5** — Phase 8.5 runs on M04's BOUNDARY queue (M04 is currently paused at end of Phase 9; under v2_5 this means M04 needs a re-routed flow: Phase 8.5 fires first on its 322 BOUNDARY verses, then Phase 9 re-authors against the resolved structure, then Phase 10 → 11 → 12. The "Phase 9 already exists" wrinkle for M04 is operational, not instructional.)
- **Audit-and-fix script design** — `scripts/_audit_cluster_against_instruction_v25_*.py` written and tested.
- **Closed-cluster audits** — researcher directs which clusters to audit and in what order.

---

*End of changes summary. Open the [full draft](wa-sessionb-cluster-instruction-v2_5-DRAFT-20260518.md) for line-level review.*
