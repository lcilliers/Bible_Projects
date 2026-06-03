# Cluster Audit Interpretation — 2026-06-03

Companion to [wa-programme-cluster-audit-20260603.md](../../Workflow/Programme/Program_reports/wa-programme-cluster-audit-20260603.md).
Read-only audit of all 19 started clusters on the recovered **2026-05-28** DB.

## Headline must not be misread

**0 PASS / 19 FAIL** does **not** mean the published analysis is broken. The auditor
(`audit_cluster_v1_20260601.py`) enforces the **06-01 v3_0 / Phase-F gate spec**, which is
*newer* than most of the recovered data. The substantive analytical aspects pass broadly:
A1 (findings present), A3 (every characteristic has findings), B4 (per-characteristic findings),
B6 (citation traceability) all PASS on every closed cluster. The FAILs are overwhelmingly
**recovery-gap** or **newer-gate-vs-older-convention** artefacts.

## The failures, grouped by cause

### Cause 1 — Schema lost in recovery (auditor/DB mismatch, NOT data)
- **D2 `ERR: no such column: cluster_link` on all 19.** The 06-01 "pointer `cluster_link` schema + population" migration is not in the May-28 DB. Non-gating (auditor marks it PASS). Resolves automatically once the 06-01 schema work is redone.

### Cause 2 — The lost 06-01/06-02 remediation (the core redo)
- **A6 (gating flags) + A7 (stray SB findings) FAIL on most clusters.** This is precisely the COMMENT_EVALUATION remediation the 06-02 session performed. On the May-28 DB those SD_POINTER / SB_FINDING rows are still open. Magnitudes track remediation state: **M10b (2/2), M10c (1/1)** are near-clean (partially remediated pre-snapshot — their disposition JSONs are present); **M05 (183/338), M39 (166/219), M09 (66/186)** are untouched.
- **C1 old-format VCGs not dissolved** on older clusters (M05 123, M26 56, M39/M46 34) — the Phase-C dissolution step, also part of the redo.

### Cause 3 — Audit gates newer than the older clusters' completion convention
- **B1b KEYWORDS FAIL on 17 of 19** ("0/N have keywords"). Keywords-in-Pass-A dates from **2026-05-23**; only M10/M10b/M10c/M11/M38 (analysed after) pass. The 06-02 B1b backfill isn't in this DB.
- **B1a MEANINGS missing on the oldest clusters** (M26 0/869, M39 1/718, M46 1/197, M15 545 short, M05 1264 short, M06 280 short, M20 56 short). Meaning-on-`analysis_note` convention postdates their completion. Newer clusters (M01/M02/M04/M07/M08/M09/M10/M10b/M10c) pass B1a.

### Cause 4 — Real, pre-existing, already-documented open items
- **A5 BOUNDARY_DECISION_PENDING** — M03 (28), M01 (7), M02 (4). These are the pre-v2_5 BOUNDARY-pending closures flagged in the 2026-05-17 methodology pivot; they need the §11.5 resolution pass. Genuinely open, but known and tracked (see [[feedback_boundary_resolution_required]]).
- **B7 anchor-not-cited / B5 VCG-no-anchor / B3 one-subgroup-unlinked / B2 ungrouped** — small structural residuals (B7 is an analytical-coverage gap, not a mechanical citation fix; see the M10b disposition workings in the report).

### Cause 5 — Known empty state (not a defect)
- **M11 & M38 = 0 findings (A1/A3/B6 FAIL).** Phase D was created *after* the snapshot cut-off; their published essays exist on disk but the findings aren't in this DB. M38's disposition JSON is an unfilled REVIEW-REQUIRED template (blank rows in the report).

## One genuine auditor refinement (cosmetic, non-gating)
- **A2** over-triggers on `cluster_synthesis` rows that legitimately discuss the cluster's silences/gaps (that is the synthesis layer's job). Confirmed false-positive in the M10b & M10c dispositions. Fix: exclude `finding_status='cluster_synthesis'` or tighten the gap-pattern. INFO/REVIEW only.

## Conclusion
The audit is a precise map of the **recovery gap**, not an indictment of the analysis. The redo
worklist it produces (143 items) is the same June 1-2 remediation, plus the meaning/keyword
backfill that the newer convention now expects on the older clusters. Recommended sequence
unchanged: redo the 06-01 schema work (restores `cluster_link`, clears D2), then re-drive the
remediation handlers per cluster (A6/A7/C1), then backfill B1a/B1b on the older clusters.
