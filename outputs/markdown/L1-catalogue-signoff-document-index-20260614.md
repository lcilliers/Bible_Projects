# L1 / Catalogue sign-off — document index

> Purpose: pull every document about the **catalogue** and the **L1/L2 verse-processing** back into focus, for the goal: *complete the L1 mechanical work in compliance with the catalogue questions — which first needs the catalogue changes signed off.*
>
> **Verification note:** every path below is real and was cross-checked against `database/file_manifest.json` (my manifest search + two independent reads agreed). The one-line descriptions are summaries from a read — **verify against the files themselves**; I'm flagging where I'm not certain.

---

## 1. The summary doc you're looking for — two candidates

You asked for "the `.md` that summarised the catalogue and the L1/L2 focus." There are **two** that fit, depending on which you remember — confirm which:

| Path | Date | What it summarises |
|---|---|---|
| `Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md` | 2026-06-11 | **The catalogue summary.** Restructures all 189 tier questions into the two-layer model (Layer A = Verse-Extraction VE fields; Layer B = SYNTH). Disposition of every old T-code. Explains the **M/R (mechanical vs read) split that gates L1**. Holds the **D1–D7 sign-off decisions**. |
| `research/investigations/wa-v3_2-l1-l2-architecture-synthesis-v1-20260608.md` | 2026-06-08 | **The L1/L2 summary.** Pulls the prototype work together; reframes the L1/L2 cycle as a multi-angle report pipeline feeding L2 synthesis. |

`[UNCERTAIN which one you mean — likely the first, since it ties the catalogue to the L1 M/R gate.]`

---

## 2. Catalogue changes awaiting your sign-off (the gate before L1)

These hold the decisions that must be ratified before the catalogue is refitted and L1 can run against it:

| Path | Date | Decisions it opens | Status |
|---|---|---|---|
| `Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md` | 2026-06-11 | **D1–D7** (DROP list · origin/from-other-spirits · faculty · constitutional_location + relational_direction · **M/R split** · numbering · approve VE questions) | approved on paper; **DB not modified; D1–D7 open** |
| `research/investigations/wa-catalogue-refit-two-layer-v1-20260609.md` | 2026-06-09 | **D1–D4** (four principles: characteristic = typed-term-in-verse · DROP redundant Qs · de-force forcing Qs · split L1/L2 vs SYNTH) | proposal; **pending markup** |
| `research/investigations/wa-verse-level-extraction-spec-v1-20260609.md` | 2026-06-09 | **D1–D5** (the ~13-field verse-extraction record; tiers computed, not asked) | proposal; **pending markup** |
| `Workflow/Tiers/wa-tier-questions-extract-v1-20260604.md` | 2026-06-04 | — | the live DB extract of the 189 questions (reference key) |
| `memory/feedback_catalogue_refit_four_principles.md` | 2026-06-09 | — | governing principles behind the refit |
| `memory/feedback_verse_level_extraction_feeds_tiers.md` | 2026-06-09 | — | governing: verse feeds the tiers (tiers computed) |

> Per the open-loops register (`outputs/markdown/project-reconstruction/04-…` §1b): the catalogue is "approved on paper, but the DB is not yet modified… D1–D4 + D1–D5 pending researcher markup." `[The §6 D1–D7 list and the proposal blanks I have from a read, not from re-reading every line myself — verify in the files.]`

---

## 3. The documents that "pulled data together" — and were not conclusive

The L1/L2 exploration/synthesis docs (grouped by theme). These are the ones whose own text records an inconclusive / parked / reverted result:

### Diagnosis (the turning point — why you stopped it)
| Path | Date | What it is |
|---|---|---|
| `Workflow/Sessionlogs/wa-sessionlog-20260611-ve-exploration-and-meaning-diagnosis-v1.md` | 2026-06-11 | The VE-01 exploration + the diagnosis that the meaning paragraph **duplicates the dimensions then fabricates** — the point at which the run was stopped. |
| `research/investigations/wa-column-wise-ve-hypothesis-v1-20260611.md` | 2026-06-11 | The row-wise → column-wise reframe proposal (not implemented). |

### The L1 prototype + the L1 failure
| Path | Date | What it is |
|---|---|---|
| `research/investigations/wa-l1-test-failure-analysis-v1-20260608.md` | 2026-06-08 | **First V3_2 L1 run on M01 FAILED; DB writes reverted; "L1 as built is not ready."** |
| `research/investigations/wa-l1-prototype-findings-and-r-decisions-v1-20260607.md` | 2026-06-07 | L1 mechanical prototype M01+M02; R-decisions; homonym filter; residue classes. |
| `research/investigations/wa-l1-prototype-m01-m02-comparison-v1-20260607.md` | 2026-06-07 | M01 vs M02 prototype run comparison. |
| `research/investigations/wa-l1-prototype-r7-morph-m01-m02-v1-20260607.md` | 2026-06-07 | Morphology (R7) as a *partial* aid — does not remove the within-stem residue. |
| `Sessions-v2/M01-Fear/wa-cluster-M01-v3_2-L1-run-v1-20260608.md` | 2026-06-08 | The actual M01 L1 run record. |

### Architecture / method synthesis (held / re-design)
| Path | Date | What it is |
|---|---|---|
| `research/investigations/wa-v3_2-l1-l2-architecture-synthesis-v1-20260608.md` | 2026-06-08 | L1/L2 as a multi-angle report pipeline — iteration designed in; held pending prototyping. |
| `research/investigations/wa-method-checkpoint-does-l1-change-the-approach-v1-20260608.md` | 2026-06-08 | Checkpoint: build on V3_2, evolve not replace; held pending cross-cluster roll-up. |
| `research/investigations/wa-l1-sweep-prelaunch-state-and-rollback-v1-20260608.md` | 2026-06-08 | Pre-sweep snapshot + rollback state; L2 synthesis HELD. |
| `Workflow/Sessionlogs/wa-sessionlog-20260608-l1-sweep-launch-v1.md` | 2026-06-08 | L1 sweep launch log (validate-on-hard-case recommendation). |

### Catalogue ↔ L2 coverage (the data-pull on what L2 covers)
| Path | Date | What it is |
|---|---|---|
| `research/investigations/wa-l2-findings-catalogue-coverage-v1-20260609.md` | 2026-06-09 | Which catalogue questions L2 covers; DIRECT/EVIDENCE/BEYOND split of the questions. |
| `research/investigations/wa-l2-findings-view-M15-M10-M26-v1-20260609.md` / `…-v2-…` | 2026-06-09 | L2 per-verse findings samples (old vs new). |

### Governing design / methodology (the L1/L2 frame)
| Path | Date | What it is |
|---|---|---|
| `Workflow/methodology/wa-cluster-rollup-design.md` | 2026-06-07 | The L1–L8 roll-up design (verse → cluster → study); several `〔CONSULT〕` open calls. |
| `Workflow/methodology/wa-phase1-mechanical-meaning-reframe-v1-20260607.md` | 2026-06-07 | Phase 1 meaning as **mechanical STEP application** (R1–R7 open). |
| `Workflow/methodology/wa-verse-analysis-methodology.md` | 2026-06-06 (v4 DRAFT) | Span-focal verse-analysis methodology; §7 open questions. |
| `Workflow/Sessionlogs/wa-sessionlog-20260609-verse-read-meaning-M01-M15-v1.md` | 2026-06-09 | The verse-read = meaning live run (M01 + M15). |

---

## What I am *not* doing here

I'm only surfacing the real documents and where the decisions sit — no fix, no recommendation, no patch. The full live-state of the L1/L2 data (the NULL-clustered mechanical layer, the partial `l2_api` coverage) is a separate thing I can lay bare *as evidence for you to verify* whenever you want it — it is not folded into this index.

> There are also ~25 `research/investigations/wa-l2-write-*-dryrun/live-*` execution logs (per-cluster L2 write runs, 2026-06-09). I left them out as run logs rather than the "pulled-data-together" synthesis docs you asked for — say if you want those listed too.
