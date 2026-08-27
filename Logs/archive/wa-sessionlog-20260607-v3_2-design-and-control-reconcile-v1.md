# Session log — V3_2 design, prototyping, control-system reconcile (2026-06-07)

**Type:** end-of-day session log / restart record · **Author:** CC. Everything committed + pushed (HEAD
`1fadd0e` + the archive-decisions/this-log commit). **No DB writes today** (design + read-only analytics +
code-only engine reconciliation). DB integrity **ok** (schema 3.28.0, intact). Continues from
`wa-sessionlog-20260606-verse-meaning-reshape-v1.md`.

---

## TL;DR — where to pick up

A very large day. We took **A1 (verse-meaning corroboration)** from "an audit idea" all the way to a
**complete V3_2 base design + a draft instruction + a schema plan**, validated by an **M01+M02 prototype**,
then **reconciled the migration control system** and **checked row-level data completeness** before the
rebuild. **Tomorrow: rebuild from M01 under V3_2.**

Two things are parked **awaiting the researcher** before the rebuild:
1. **Task 1 — term dedup** (~93 mti_terms rows; needs a dry-run eyeball + go).
2. **Task 2 — filing archives** (mark up `wa-archive-decisions-for-guidance-v1-20260607.md`).
Then: **apply schema migration M55** (backup + dry-run) → **run M01 through L1**.

---

## The arc (what happened)

1. **A1 corroboration — built + validated.** `_assess_verse_corroboration.py`; M01 = **949/949 meanings
   corroborate to the STEP sense-set, 0 divergent**; a **3-tier triage** (97% mechanical, 28 residue read).
2. **The reframe.** Corroboration becomes the **generation principle**: **Phase 1 = mechanical STEP-sense
   application**, not AI meaning-derivation. Dual meaning (AI note preserved). `wa-phase1-mechanical-meaning-
   reframe-v1`.
3. **STEP morphology finding.** The per-verse **stem** selects the BDB sense-branch (free disambiguation);
   neither `morph` nor `stem_label` is captured today. `wa-step-morphology-sense-disambiguation-v1`.
4. **T2 surfacing.** STEP-sense overlap surfaces mis-parked Supplementary terms to candidate clusters.
   `wa-t2-relevance-surface-v1`.
5. **Rollup design → V3 → resequenced → V4 (the V3_2 base).** Sub-group-first spine (L1 mechanical → L2
   provisional sub-group → L3–L5 per sub-group → L6 closure → L7 synthesis+science → L8a/L8b);
   **A3 gates + A4 finding lifecycle**; completeness checks; uniform per-level pattern; then a full **clarity
   rewrite** as the authoritative V3_2 base. `wa-cluster-rollup-design.md` (v4).
6. **Audit design.** A per-level **compliance check** (PASS/FAIL, not remedial), *derived from* the rollup
   pattern (Needs→precondition / Updates→FC / Does→SC / Gate→mop-up). `wa-cluster-audit-design-v1`.
7. **All open items resolved.** A1–A4, B1–B3 (B3 the one carried), C1/C2, D1–D3, E1–E9, F1/F2, and the
   **R1–R7 schema decisions via the M01+M02 L1 prototype** (`_prototype_l1_mechanical.py` + `_prototype_l1_
   morph.py`; findings `wa-l1-prototype-findings-and-r-decisions-v1`). Headline prototype findings:
   multi-sense load is verse-weighted + cluster-variable (M01 49% / M02 64%); **pole can't be assigned by
   lexicon alone** (metaphor vs literal vs manifestation → new `pole_is_metaphor` flag); morphology is a
   **partial** resolver (~14–22%). The **9 §12 CONSULT items** were then settled (key: **discipline 2 — L1
   never force-settles ambiguity; double-meaning → L2**, to protect discovery of unique characteristic
   scenarios).
8. **V3_2 instruction draft + schema migration plan.** `wa-cluster-rollup-instruction-v3_2-DRAFT`;
   `wa-v3_2-schema-migration-plan-v1` (12 new cols + 2 drops; ready-to-register M55).
9. **Migration control-system integrity — investigated + reconciled.** The registry/history drift was real:
   `migrate.py` froze at M39 (one-off scripts applied M40–M54); the runner re-ran **every** migration with
   unconditional version-bumps (would have reset 3.28.0→3.16.1). **Schema verified intact through M54;
   restore exonerated.** Fixed code-only: **history-aware runner**, M39 bug removed, **registry backfilled**
   (now ⊇ history), `EXPECTED_SCHEMA_VERSION → 3.28.0`. `wa-migration-control-integrity-v1`.
10. **Row-level completeness check.** Foundation intact; the restore reverted a **~93-row mti_terms dedup**
    (term layer, the rebuild reads it) — the one pre-rebuild action. The 296 verse_context ghosts are
    **superseded by the rebuild** (re-forms VCGs); the big lost June 1–2 work (cluster closures, remediation
    tooling) is **moot under V3_2**. `wa-row-level-completeness-prerebuild-v1`.

## Key deliverables (all committed)

- **Design (Workflow/methodology/):** `wa-cluster-rollup-design.md` **(v4 — the V3_2 base)** ·
  `wa-phase1-mechanical-meaning-reframe-v1` · `wa-cluster-audit-design-v1` · `wa-v3_2-schema-migration-plan-v1`.
- **Instruction (Workflow/Instructions/):** `wa-cluster-rollup-instruction-v3_2-DRAFT`.
- **Filing (Workflow/):** `wa-archive-decisions-for-guidance-v1` (awaiting markup).
- **Investigations (research/investigations/):** `wa-a1-*` (3) · `wa-step-morphology-*` · `wa-t2-relevance-*`
  (2) · `wa-l1-prototype-*` (3) · `wa-migration-control-integrity-v1` · `wa-row-level-completeness-prerebuild-v1`.
- **Scripts:** `_assess_verse_corroboration.py` · `_assess_t2_relevance_surface.py` ·
  `_prototype_l1_mechanical.py` · `_prototype_l1_morph.py`.
- **Engine:** `migrate.py` (history-aware runner + M16/17/40–54 backfill; M39 fix) · `constants.py` (version).

## Open / next (the rebuild runway)

1. **Task 1 — term dedup** (~51 duplicate + ~42 delete-status ghost mti_terms; leave ~50 FLAG parked). CC to
   produce a **dry-run row list + backup**, then soft-delete on the researcher's go.
2. **Task 2 — filing archives.** Researcher marks up `wa-archive-decisions-for-guidance-v1`; CC sweeps +
   generates the fresh `database-schema-v3.28.0` snapshot + updates the cleanup register.
3. **Schema migration M55** — register the V3_2 fields (per the migration plan), apply via the now-safe
   runner, **backup + `--migrate --dry-run` first**. Then run the **stem_label + homonym** population passes.
4. **Run M01 through L1 under V3_2** — the first real execution (morphology populates here) → audit →
   researcher review gate.

**Still-open design:** **B3** (L8b cross-cluster ordering/dependency mechanics — study-level, non-blocking) ·
a few schema `〔CONSULT〕` details (`sense_id` FK vs code; homonym-detection rule).

---

*End of session. State consistent on disk + git (pushed), DB intact (3.28.0) and untouched, migration
control reconciled, backups live. The V3_2 design is settled; execution begins tomorrow with M01. Rest well.*
