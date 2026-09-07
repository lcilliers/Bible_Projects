# M10b (Wickedness) — remedial run log v2 (post-recovery redo)

**Cluster:** M10b · **Date:** 2026-06-03 · per the remediation playbook. Redo on the recovered
clean baseline after FLAG rescue + cluster_link. Researcher-approved (proceed 1→2→3, 2026-06-03).

## Baseline (programme audit v2)
GATE fails: **2** — A7 (1 stray SB finding), B7 (2 uncited anchors). A6 was **already 0** (the
cluster_link/orphan-set-aside work cleared M10b's SD_POINTER A6 items). A2 advisory-review (4 synthesis
rows) — documented false-positive, non-gating.

## Verification before apply
- A6: 0 flags (cleared upstream). A7: exactly **finding id=101** (`DIMENSION_REVIEW`, pending) —
  matches the committed disposition.

## Applied
`_apply_pointer_dispositions_v1 --file …/wa-cluster-M10b-pointer-dispositions-v1-20260601.json --apply`:
| Item | Action | Result |
|---|---|---|
| finding 101 (`DIMENSION_REVIEW`, reg-57) | set_aside (superseded registry-scope note) | `status='set_aside'` |
| cluster_finding A2 (19474,19485,19506,19626) | review — no action | no-op |
| B7 anchors Hos 10:13 (H7562), 2Ch 24:7 (H4849) | surface — analytical residual | no-op (do NOT fabricate citations) |

Citation extractor re-run (`--cluster M10b --live`) as part of the programme sweep — did **not**
clear B7: the two anchors are genuinely not cited in any M10b finding (confirmed: a coverage gap,
not an extraction gap, exactly as the 06-01 disposition recorded).

## Re-audit (v3)
- A7 → **0** ✓ (finding 101 set_aside).
- **B7 = 1 gate still failing** (2 anchors uncited).
- Verdict: **A7 closed; B7 OPEN — analytical residual pending researcher call.**

## Open item for researcher (B7) — carried from 06-01
Two strongly-relevant anchors of VCG M10b-A-VCG-11 (char 47 "Wickedness as settled person-identity")
are not used in any finding:
- **Hos 10:13** (H7562 resha) — "wickedness is the inward soil that produces injustice and lies".
- **2Ch 24:7** (H4849 mirshaath, Athaliah) — "wickedness expressed as religious violation".
Resolution is analytical, not mechanical: **(a)** extend the char-47 finding to use these two
exemplars (preferred — both genuinely evidence the characteristic), or **(b)** de-anchor
(`is_anchor=0`, keep `is_relevant=1`) if the VCG's findings rest on other exemplars. Do not fabricate
a citation. M10b stays one-gate-open until you decide.
