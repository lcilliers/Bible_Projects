# M10b (Wickedness) — remedial run log

**Cluster:** M10b · **Date:** 2026-06-01 (B7 closed 2026-06-02) · **Status:** `Analysis Complete` (CLOSED 2026-06-02 — B7 residual resolved) · per the remediation playbook. Audit snapshot: `wa-cluster-M10b-audit-v1-20260601.md` (this folder, now **PASS**). Dispositions: `wa-cluster-M10b-pointer-dispositions-v1-20260601.json`; B7 citation extension: `wa-cluster-M10b-b7-citation-extension-v1-20260602.json` (this folder).

## Baseline (audit before remediation)
GATE fails: A7 (1 stray SB), B7 (4 uncited anchors). B1a/B1b/B3/B5 PASS. No new terms, no pointers. (No A6.)

## Fixes applied
| Handler | Aspect | Action | Result |
|---|---|---|---|
| citation extractor (`--cluster M10b --live`) | B6/B7 | idempotent re-extract — 6,616 citations | **B7 4 → 2 uncited** (2 were citation-gap, now cited) · B6 PASS |
| dispositions applier (`_apply_pointer_dispositions_v1`, `--apply`) | A7 | finding 101 (`DIM-57-001`) → `set_aside` (verified persisted) | **A7 → PASS** (gate fails 2 → 1) |

## Dispositions (content-evaluated — `wa-cluster-M10b-pointer-dispositions-v1-20260601.json`)
| Item | Action | Reason |
|---|---|---|
| **A7** finding 101 (`DIM-57-001`, registry 57 'evil') | **set aside** (applied) | Phase-C dimension note about the OLD registry model (reg-57 breadth / framing-particle container); its own link is M15,T2, surfaced under M10b via a non-exclusive term→sub-group link. Superseded by the term-anchor re-clustering. Same class as M10c finding 55. Set aside globally (correct — superseded for every cluster). |
| **A2** 4 `cluster_synthesis` rows (19474/19485/19506/19626) | **review — no action** | False positives: legitimate synthesis essays discussing the cluster's silences/gaps (the layer's job). Heuristic over-triggered on *silent/gap/has-not-addressed*. Advisory (INFO), non-gating. |
| **B7** anchors `Hos 10:13` (H7562), `2Ch 24:7` (H4849) | **surface — analytical residual** (no DB change) | Both are valid, strongly-relevant anchors of VCG M10b-A-VCG-11 / sub-group 156, characteristic 47 ('Wickedness as settled person-identity'), yet **no M10b finding cites either** (extractor already run — not a citation gap). A genuine Phase-D coverage gap. **Will NOT fabricate** a citation (extractor would delete a text-unbacked citation). |

## B7 resolution — researcher decision **(a)**, applied 2026-06-02
Researcher chose **(a)**: the two anchors are genuine settled-wickedness exemplars and should be cited. Each was added to the host char-47 finding whose existing claim it directly evidences — faithful to the verse's `verse_context.analysis_note`, in house style, VCG-tagged — then the citation extractor re-derived `finding_citation` from the extended text (no fabricated citation rows). Spec: `wa-cluster-M10b-b7-citation-extension-v1-20260602.json`; reusable applier `scripts/_apply_finding_citation_extension_v1_20260602.py` (idempotent, anchor-unique guarded, dry-run default).

| Anchor | Host finding | Extension (faithful to analysis_note) |
|---|---|---|
| **Hos 10:13** (H7562 re.sha, VCG-11) | 18414 ('internally-generated state overflowing outward as social harm') | "…wickedness is *the inward soil that produces injustice and lies* — a settled inner orientation… whose outward harvest is injustice and deceit." |
| **2Ch 24:7** (H4849 mir.sha.at, VCG-11) | 18412 ('the wicked extend their characteristic outward as harm/profanation') | new exemplar (e) 'sacral desecration' alongside the existing Eze 7:21 profanation exemplar — settled wicked character channelled into desecrating sacred space. |

Extractor: 6616 → **6618** citations (the two new refs). Re-audit: **B7 → PASS**, all gates clear (gate_fails=0).

## Verdict — **CLOSED** (`Analysis Complete`, 2026-06-02)
Full loop completed: audit → handlers (citation extractor B6/B7; dispositions applier A7; B7 citation-extension applier) → re-audit PASS → `_close_cluster_analysis_v1 --apply`. A2 advisory/no-action (false positives). M10b is the **second** cluster through the systematic loop after M10c.
