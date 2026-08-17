# Session log — 2026-06-11 · VE exploration, M-vs-R divergence, and the meaning-duplication diagnosis

> Cross-stage log. Covers the full day's arc: the tier-catalogue restructure v2 + DROP soft-deletes (committed
> during the day), then the VE-01 coverage / gap investigation, the M-vs-R divergence analysis, the
> column-wise hypothesis, the engine-timing question, and — the turning point — the diagnosis that the verse-read
> meaning paragraph duplicates-then-fabricates. Ends on a personal checkpoint (despondency / possible sabbatical).

---

## 1. Earlier in the day (already committed)

- **Tier catalogue restructured v2** (`Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md`): each VE
  field reformulated as a single consolidated verse-level question; full originating tier-question text embedded
  under each VE section; M/R workings explained; §5 two-up layout clarified; Appendix A = verbatim DB extract of
  all 189 tiers. (commits 9eeac0d, 40e8499, 42c0dee)
- **§3 DROP executed (D1 approved):** extracted every finding referencing the 16 DROP tier codes by cluster
  (uniform per-family counts = the templated/fabricated tell), then soft-deleted the DROP-code findings + their
  underlying Session B findings + the 16 catalogue questions, all with reasons. Session D layer was empty.
  Pre-change DB backup `backups/bible_research_pre-dropcode-softdelete_20260611.db`. (commits f347742, 2d798a3,
  bb534aa) Governing memory recorded: review-by-statistics is dangerous; legacy findings peppered with fabricated
  data. (afd6eef)

## 2. VE-01 coverage + the gap (this session)

- Confirmed VE-01 (obs 395) is **dual-record** for M01/M02/M15 (100%): a mechanical lexical-range record
  (`l2_mechanical`, cluster-NULL, constant per term) + a verse-specific read record (`l2_api`, cluster-tagged) —
  *not* old/revised re-runs.
- **Excluding T2** (the reference bucket, 12,073 term-in-verses): corpus = **31,420** non-T2 term-in-verses;
  any VE-01 = **28,948 (92%)**; mechanical 28,464 (91%); read 7,014 (22%); both 6,530.
- **Gap investigated = 2,472 (8%).** Not random: **78 distinct terms**, every one with *zero* mechanical
  findings and only partial verse-read. Splits 50/50: **M47 (Constitution, created 2026-06-10)** = 1,236, and
  high-frequency broad framework terms elsewhere = 1,236 (`lev`, `levav`, `nephesh`, `berit`, `mishpat`,
  `chayyim`, `kardia`, `sarx`). These are the constitutional seats + framework terms — exactly where a single
  mechanical lexical sense is meaningless and the read matters most. Not rot; awaiting their verse-read. (We
  agreed to cover these "in a short while".)

## 3. M vs R divergence (this session)

- For VE-01, compared the mechanical gloss-range (M) against the verse-read sense (R) for the 3,702 term-in-verses
  that have both. Script: `scripts/_explore_m_vs_r_divergence.py`. Output:
  `outputs/markdown/m-vs-r-divergence-20260611.md` + `.csv` + interpretation note.
- Crude lexical overlap flags 1,439 (39%) "material" — but **reading the rows proves the count misleads** (exactly
  the standing warning). It decomposes into: (a) **synonym-within-range** noise (wrath≈anger, fury≈rage,
  honour/honor) — the majority, all 367 M02; (b) **empty mechanical gloss** (60 rows / 22 terms — a backfill item);
  (c) **genuine sense-divergence** (the prize): polysemy (`pneuma` wind/breath→Holy-Spirit/human-spirit/ghost),
  homonym (`archō` rule→begin), physical pole (`ka.phar` atone→pitch-coating), morphology stem-sense (Hiphil
  `sha.ma` obey→proclaim; `cha.zaq` strengthen→seize). Lexical overlap cannot isolate "material" — it needs a
  semantic read. Two by-products: 22 empty-gloss terms to backfill; `pneuma`-type polysemy as the confirmed
  divergence class.

## 4. The column-wise hypothesis + engine timing (this session)

- **Hypothesis (le Roux):** reorganise the verse-read from **row-wise** (read a verse, answer all 14 VE
  dimensions + meaning, per verse; ~1 day/cluster, ~40 days left, errors on every review) to **column-wise**
  (answer each *isolable* VE question across the whole corpus as one focused pass; one stable rubric). Drives
  consistency (one rubric, reviewable in one view) and cuts time (mechanical dimensions leave the metered read).
- **Three lanes:** A mechanical/term-level (no read, scripted) · B sense-application spine (one read pass) ·
  C interdependent cause/effect/relationship core (stays *grouped* — guardrail: never column-split it, or you
  re-read each verse N times). A+B ≈ 9–10 of 14; C is the gap-flagged dynamics cluster.
- **Engine timing question:** the engine *cannot* currently break a batch into read / dimensions / meaning /
  write. Logs are coarse wall-clock; dimensions **and** meaning are produced in **one streamed model call** (so
  inseparable). Output-token proxy across 8,367 records: **14 dimensions ~40% of generation, meaning paragraph
  ~60%** — the meaning costs more than all the dimensions combined.
- Working note: `research/investigations/wa-column-wise-ve-hypothesis-v1-20260611.md`.

## 5. The turning point — meaning duplicates, then fabricates

- le Roux's diagnosis, confirmed by evidence (not asserted): the meaning paragraph **duplicates** the 14
  dimensions and **fabricates**. The system prompt *orders* it to reflect every non-null field; the audit checks
  field→paragraph **only** (no paragraph→field), so duplication is enforced and extra prose is unaudited.
- Three real M02 records show the three patterns: **Mat 2:16 `thumoō`** = pure duplication (restates faculty
  tags verbatim); **Mar 3:5 `orgē`** = observation-only-in-meaning (anger-grief fusion + co-terms `sullupeō`/
  `pōrōsis`, in no dimension); **Rom 1:18 `orgē`** = imported filler ("gospel backdrop" pulled from 1:16-17, not
  the verse; `origin=within-person` for God's wrath is also a dimension error the prose smooths over).
- **Why it is the 4-month variation circle:** the meaning is a *generative free-prose step*; free prose abhors a
  vacuum, so it invents to fill gaps and imports synthesis. Each re-read notices/imports different things →
  meaning differs → reads inconsistent → re-do. It also **falsifies** the prior premise that value is "safely
  mirrored as ~14 queryable findings" — value is prose-locked in the meaning.
- **Structural fix — reverse the primacy:** dimensions become PRIMARY (disciplined, option-list, silence-valid,
  column-wise, stable against complete inputs ⇒ re-read returns the same answer); meaning becomes DERIVED (a
  deterministic roll-up that *cannot* invent; cross-verse synthesis → SYNTH layer); genuine meaning-only
  observations get *promoted to new dimensions* (paired/fused-with, key co-terms, cause→effect). Column-wise is
  the mechanism that breaks the circle because it separates disciplined extraction from generative prose.

## 6. Personal checkpoint

le Roux is despondent — ~15 redo rounds, doubts it can ever be "right", considering a sabbatical (gardening,
dioramas). Noted honestly: everything is durably stored (DB + git + NAS + memory) and safe to set down; today
diagnosed a *cause* (a tool defect) rather than proposing another angle, which is a different category of
finding; and "right" — per his own governing principles (scaffolding-not-reality, infinitely-variable,
allow-ambiguity, milestones-replace-completion-pressure) — may be a target he had already, on paper, let go of.
No decision forced. He said he enjoyed (some of) the journey, learnt a lot, and will bank that.

## 7. Artefacts this session

- New scripts: `scripts/_explore_m_vs_r_divergence.py`.
- New outputs: `outputs/markdown/m-vs-r-divergence-20260611.{md,csv}`,
  `outputs/markdown/m-vs-r-divergence-interpretation-20260611.md`.
- New note: `research/investigations/wa-column-wise-ve-hypothesis-v1-20260611.md`.
- New memory: `project_meaning_duplicates_then_fabricates`, `project_column_wise_ve_hypothesis` (+ MEMORY.md
  index); earlier `feedback_no_stats_trends_review_fabricated_data`, `project_verse_extraction_cause_side_gap`.
- No schema change this session. DROP soft-deletes (earlier) are reversible.
