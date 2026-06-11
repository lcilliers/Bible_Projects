---
name: project_a1_resolved_rollup_v3_audit_design
description: V3_2 cluster-rollup design COMPLETE as of 2026-06-07 (rollup design v4 = the V3_2 base; A1 corroboration is the GENERATION principle; Phase 1 = mechanical STEP-sense application). All open items resolved (R-series via M01/M02 prototype; only B3/L8b-mechanics carried). NEXT: rebuild from M01 under V3_2 after (1) term dedup, (2) filing archives, (3) schema migration M55.
metadata:
  type: project
---

Working through the `wa-cluster-rollup-design.md` open items one at a time (researcher-led, anchored on that doc as the guide). **A1 done 2026-06-07; researcher resolving A3 next.**

**A1 (verse-meaning corroboration) — RESOLVED as a reframe, not just an audit:**
- Corroboration becomes the **generation principle** — a verse meaning *built from* the term's STEP sense-set cannot diverge from the lexicon. **Phase 1 = mechanical STEP-sense application + residue surfacing**, NOT AI meaning-derivation (the old per-verse AI bias). Validated on M01: 949/949 corroborate, 0 divergent; 97% mechanical, 28 residue read (3-tier triage).
- A term carries a **sense-set**; verses realise different senses → which sense = bounded **sense-selection** (single-sense = mechanical; within-stem multi-sense = light select). See [[feedback_term_corpus_anchors_meaning]], [[feedback_phase_a_light_meaning_at_vcg]].
- **STEP morphology** (per-verse stem) mechanically selects the BDB sense-branch — free disambiguation; neither `morph` nor `wa_meaning_sense.stem_label` is captured today.
- **Dual meaning:** keep the AI `analysis_note` AND add the STEP-applied meaning; never overwrite.
- **T2 surfacing:** STEP-sense overlap surfaces mis-parked Supplementary terms to candidate clusters (`owning_word` agreement = high confidence).

**Live design docs (Workflow/methodology/):** `wa-cluster-rollup-design.md` (**V3**), `wa-phase1-mechanical-meaning-reframe-v1`, `wa-cluster-audit-design-v1`. Evidence in `research/investigations/wa-a1-*`, `wa-step-morphology-*`, `wa-t2-relevance-surface-*`. Scanners: `scripts/_assess_verse_corroboration.py`, `_assess_t2_relevance_surface.py`.

**Rollup V3 spine:** L1 verse establishment (= old Phase 1 incl UT-verse step + A1 mechanical meaning) · L2 VCG formation+meaning · L3 VCG-emergent · L4 sub-group/characteristic · L5 cluster · L6 findings · L7 whole-study. Uniform per-level pattern: **Needs · Does · Updates · Output→next** (+ mop-up Gate); handoff chains rung to rung.

**Audit (A2) DESIGNED:** per-level **compliance check** (PASS/FAIL, NOT remedial; remediation = pointed intervention or re-run v3 instruction). Derived from the rollup pattern: Needs→Precondition, Updates→field-completeness (FC), Does→instruction-adherence spot checks (SC), Gate→mop-up. Full L1 spec done; L2–L7 stubbed. Builds on/ supersedes [[project_v25_audit_tool]]; see [[feedback_audit_must_be_self_critical]], [[feedback_audit_before_prose]].

**Open R-decisions before v3 instruction:** R2 single/multi-sense detector · R3 dual-meaning field layout · R7 capture morphology + parse stem_label (the audit's SC checks need these schema fields). Part of [[project_cluster_rework_phase_started]].

**END OF 2026-06-07 (huge session):** rollup design rewritten to **v4 = the V3_2 base** (sub-group-first spine L1→L8b; A3 gates + A4 finding lifecycle; finding types; schema catalogue §10). R1–R7 RESOLVED via the M01+M02 L1 prototype (`_prototype_l1_mechanical.py`/`_prototype_l1_morph.py`); key prototype finding: **pole can't be lexical-only** (metaphor vs literal vs manifestation → new `pole_is_metaphor` flag). **Governing discipline 2 (NEW): L1 never force-settles ambiguity — double-meaning → L2 deep read** (protects discovery of unique characteristic scenarios). Drafted **V3_2 instruction** (`wa-cluster-rollup-instruction-v3_2-DRAFT`) + **schema migration plan** (`wa-v3_2-schema-migration-plan-v1`, M55, 12 new cols + 2 drops). **Migration control system RECONCILED** (was: migrate.py froze at M39, runner re-ran everything + clobbered version; fixed code-only — history-aware runner, registry backfill, EXPECTED_SCHEMA_VERSION→3.28.0; schema verified intact through M54, restore exonerated; see `wa-migration-control-integrity-v1`). **Row-level completeness checked** (`wa-row-level-completeness-prerebuild-v1`): foundation intact; one pre-rebuild action = **~93-row mti_terms dedup** (restore reverted the lost June-1 dedup). **TOMORROW: rebuild from M01** after Task 1 (term dedup, dry-run+go), Task 2 (filing archives — researcher marks up `wa-archive-decisions-for-guidance-v1`), schema migration M55. Only open design item: **B3** (L8b cross-cluster mechanics, non-blocking). [[project_db_loss_blocker_20260603]] restore exonerated on schema.
