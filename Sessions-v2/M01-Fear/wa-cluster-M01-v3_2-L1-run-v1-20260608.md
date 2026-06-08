# M01 — V3_2 L1 run report

> **WRITE-then-report · wa-cluster-M01-v3_2-L1-run-v1-20260608.md · CC.** V3_2 L1 (verse establishment) executed on the live DB (`scripts/v3_2_l1.py`). Cluster status → **In Progress**. Per discipline 2, L1 assigned only single-sense terms; all multi-sense → **residue for L2**.

## Result

- Terms: **83** — single-sense **72**, multi-sense **11**
- Relevant verses touched: **945**
  - **assigned a STEP meaning (single-sense): 482**
  - **residue → L2 (multi-sense): 463** (48% of touched)
- Set-aside verses (left as-is): 81
- Pole distribution (verses): inner 897, physical 48
- Terms flagged `pole_is_metaphor` (heat/tremble/melt): 10 · homonym-filtered terms: 2

## What L1 wrote (per relevant verse_context row)

- single-sense → `step_meaning_applied` (terse STEP sense) + `sense_id` + `sense_multiplicity='single'` + `residue_flag=0`
- multi-sense → `sense_multiplicity='multi'` + `residue_flag=1` (no meaning assigned — deferred to L2)
- all → `pole`, `pole_is_metaphor`, `keywords` (STEP-capture JSON), `step_envelope_note`
- `analysis_note` (existing AI/L3 layer) **preserved, untouched**

## Notes for the L1→L2 gate

- **Morphology capture deferred to L2.** Since L1 assigns only single-sense (multi → L2), the per-verse stem (which *helps resolve* multi-sense) is an L2 input — captured there, not forced into L1. Flagged for your confirmation.
- **`sense_id` is coarse** (points to the term's parsed sense row, not a split sub-sense — the BDB tree is not yet split into stem-branch rows). Precise sub-sense pointing is a refinement.
- **Pole is term-level first-pass** (per-verse pole refines at L2); literal-physical vs metaphor is flagged (`pole_is_metaphor`) not auto-assigned (R6).
- **Next:** run the L1 audit, then the **L1→L2 gate** (researcher review).