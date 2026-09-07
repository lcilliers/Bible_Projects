# M10c (Defilement) — remedial run log v2 (post-recovery redo)

**Cluster:** M10c · **Date:** 2026-06-03 · per the remediation playbook
(`Workflow/methodology/wa-cluster-remediation-playbook-v1`). Redo of the 06-01 remediation
(v1 log in this folder) on the recovered clean May-28 baseline, after the FLAG rescue +
cluster_link redo. Researcher-approved 2026-06-03.

## Baseline (programme audit v2, post-rescue)
M10c GATE fails: **2** — A6 (1 flag), A7 (1 stray SB finding). B1a/B1b/B3/B5/**B7** all PASS
(the 05-26 citation state is intact in the recovered DB, so the v1 citation-extractor step was
**not** needed). A2 advisory-review (5 synthesis rows) — documented false-positive, non-gating.

## Verification before apply (IDs confirmed against current DB)
Reproduced the auditor's A6/A7 predicates for M10c (registries 41, 86, 115):
- **A6** flagged exactly **flag id=364** (`SB_FINDING`, reg 115, unresolved).
- **A7** flagged exactly **finding id=55** (`DIMENSION_REVIEW`, status `pending`, reg 115).
Both match the committed 06-01 disposition record exactly — the evaluation maps cleanly onto the
recovered DB.

## Applied
`scripts/_apply_pointer_dispositions_v1_20260601.py --file …/wa-cluster-M10c-pointer-dispositions-v1-20260601.json --apply`
(guarded, transactional, rowcount-asserted):
| Item | Action | Result |
|---|---|---|
| finding 55 (`DIMENSION_REVIEW`, reg-115) | set_aside (superseded registry-scope note) | `status='set_aside'` + reason |
| flag 364 (`SB_FINDING`, G3392 miaino Joh 18:28) | resolve | `resolved=1` + resolved_note |
| cluster_finding A2 (20385,20412,20450,20568,20571) | review — no action | documented no-op, skipped |

Pre-write backup: `C:\Users\lerouxc\db_recovery\bible_research_pre_M10c_remediation_20260603.db`.

## Re-audit (targeted; avoids clobbering the committed v1 per-cluster audit file)
- A6 gating flags: **0** ✓
- A7 stray findings: **0** ✓
- finding 55 status = `set_aside`; flag 364 resolved = 1; integrity ok.

## Verdict — CLOSED (redo)
M10c has **0 GATE fails**, consistent with its `Analysis Completed` status (no status flip needed —
already Completed in the recovered DB). First cluster re-driven through the loop post-recovery; the
process was predictable and matched the 06-01 record exactly.

## Note
A2-on-cluster_synthesis remains a known auditor false-positive (refinement: exclude
`finding_status='cluster_synthesis'`); non-gating, left as-is.
