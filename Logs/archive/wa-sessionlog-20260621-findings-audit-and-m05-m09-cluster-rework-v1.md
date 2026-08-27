# Session log — Findings audit framework + M05–M09 cluster rework

- **File:** wa-sessionlog-20260621-findings-audit-and-m05-m09-cluster-rework-v1.md · **Date:** 2026-06-21
- **Scope:** the cluster-rework run from M05 through M09, and the new **findings-audit gate** built to govern capture/essay from here on. (Commit also sweeps in accumulated, previously-uncommitted findings from 2026-06-19/20 for M01–M05.)

## 1. Headline — the Findings Audit gate (new governance)

A **findings audit** is now the required pre-step before (a) capturing a cluster's findings into the DB and (b) producing the cluster essay.

- **Spec:** `Workflow/Instructions/wa-findings-audit-spec-v1_0-20260621.md` — policy RESOLVED. Two gates, 23 checks (FA-01…FA-23). STOP is researcher-**releasable** after reporting; REVIEW blocking depends on the corrective action (CA-1 accept · CA-2 CC in-file fix · CA-3 researcher file/DB fix · CA-4 set aside & redo in Chat). Report must be self-explanatory (plain language, no code lookup). Added FA-23 (unsubstantiated superlatives) per researcher request.
- **Script:** `scripts/_audit_findings_v1_20260621.py --cluster MNN` (read-only; writes `Sessions-v2/{CLUSTER}/findings/wa-findings-audit-{CLUSTER}-{date}.md`).
- **Retro-baseline (M03–M06):** all ran with **no STOPs**. The run shook out two real bugs in the audit itself (a cursor-reuse defect in FA-14; book-code variants tripping FA-18 — both fixed). Material catches: FA-11 stale-extract reconciliation (M03 835 vs 595), FA-14 gloss↔sense (chesed H2617B "shame"→"steadfast love"; M04 nichoach), FA-21 essay grounding (statements without citations), FA-23 scope-superlatives.
- **FA-21 changed** from a verse-coverage % to a **statements-without-citation** test (the meaningful grounding check).
- Memory recorded: `project_findings_audit_gate_live`.

## 2. Corrected cluster overview

`Workflow/Clusters/wa-cluster-overview-20260621.md` (generator `_generate_cluster_overview_v2_20260621.py`). The prior "Verses" column counted `verse_context` rows (term-in-verse **occurrences**) and ignored set-asides — doubly inflated (M08 read 680 where the in-scope corpus is 253). v2 reports **distinct in-scope verses** + separate **Set-aside** and **Occ** columns. Programme: 32,291 in-scope verses · 3,669 set aside · 40,640 occurrences. Old overview archived.

## 3. Silent-answer coverage audit

`outputs/markdown/wa-silent-answers-by-cluster-char-v1-20260621.md` and `…-why-expected-v1-…`. Isolated every silent tier-question per characteristic (M03–M06), classified each into six expected causes (faculty-not-engaged · data-shape · register · defining · lexical-fit · thin-evidence). Finding: silence is overwhelmingly **expected**; no surprising gaps; the one lever is the uniform data-shape band (recoverable only by a verse-narrative pass). Surfaced that the "Silent" marker is **not standardised** across clusters (four conventions).

## 4. Cluster work

- **M05 (Love):** flags 5 (chesed A/B split — confirmed disambiguation artifact) and 6 (corporate no-faculty band) verified against the DB. Essay restructured (v2 per-characteristic, then v3 with the compound-vocabulary finding); separate **interactions essay** "How Love Orders the Inner Life" (.md/.pdf). M05 findings + 6 characteristics captured earlier in the run.
- **M06 (Hate):** findings captured (6 characteristics A–F); essay **"The Two Edges of Hatred"** (.md/.docx/.pdf, captured). Bivalence finding (commanded hatred of evil vs sinful hatred; cruelty alone has no divine instance).
- **M07 (Shame) — first cluster through the new gate.** Gate-1 readiness check caught the self-audit-vs-files discrepancy (resolved: Phase-2 verse-read complete for all 12). **Captured A–H (9 characteristics)**; **set aside J/K/RESID** (23 occurrences — innocence antonym, silencing/casting terms, the 2 non-shame ka.lam) via `_apply_m07_setaside_jkresid_20260621.py`; M07 in-scope now 283 verses. Essay **"The Covered Face"** (.md/.docx/.pdf, captured; Gate-2 clean of STOPs — all cited verses verified). Combined `fg`/`hjkr` findings files handled by a bespoke capture.
- **Extracts generated:** M06, M07, M08 (Pride), M09 (Humility) — all with corrected provenance (`build_ve_lexical_extract.py` fixed: real `extract_version` + dynamic generation date; documents the T2-noise filter + set-aside honouring).

## 5. Scripts added/changed (key)

- `_audit_findings_v1_20260621.py` (audit) · `_generate_cluster_overview_v2_20260621.py` · `_apply_m06_findings_capture_20260620.py` · `_apply_m07_findings_capture_20260621.py` · `_apply_m07_setaside_jkresid_20260621.py` · `_render_essay_to_docx_v2_20260620.py` · `build_ve_lexical_extract.py` (provenance + version fix).

## 6. Open / carried forward

- **M07 interpret-phase flags** (in its synthesis): D vicarious sub-band; F↔M09 humility seam (sha.phel); G axis-vs-characteristic. Decisions deferred.
- **M05 flags 5/6/7** (chesed re-gloss; corporate set-aside; intra-verse duplication) — verified, DB corrections still pending researcher direction.
- **M03 extract stale** (regenerate if reused as a Chat input).
- **Marker standardisation** (M06-style "X of Y per tier") — recommended (FA-09 WARN), not yet mandated.
- **Next:** M09 distillation (Chat) → audit → capture → essay; M08 distillation still to come.
