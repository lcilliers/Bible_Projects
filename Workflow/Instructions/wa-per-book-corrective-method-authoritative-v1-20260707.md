# Per-book corrective method — AUTHORITATIVE INSTRUCTION (v1)

> This is the governing method for correcting each book, set by the researcher. It is recorded **verbatim** so it cannot be paraphrased into drift. Where any of my earlier documents restate or "tidy" this (e.g. `Workflow/methodology/wa-per-book-corrective-pipeline-spec-v1-20260706.md`), **this document is authoritative and they are subordinate to it.** Set 2026-07-05 05:12 UTC; recorded 2026-07-07.

## The instruction (researcher's exact words — do not reword)

> "to me it looks like corrective action to fix all the issues is going to be a **by book operation**, and that **no fix should be done accross books**. the last question and answer also indicates that the **role cannot be fixed as a stand alone item**. It seems that we need
>
> **a)** to work by book
>
> **b)** confirm, or rework if not accurate the **passage/verse reading units** - ensure it is captured in the tables. **no reading should start before this is done.** these tables must allow **forward and backward tracking from the master index (term-span-verse) through the passage table to the lexican and to the verse(s)** - fix these table where necessary
>
> **c)** **re-assess the role dimension**, fix if needed
>
> **d)** go back to **gate 1** and check that the DB is **complete for all characteristic span** - the term must be recorded, the verses pulled, and all the links must be built and be in tact - **this is a STEP action**.
>
> **e)** on completion of the book, **validate that the DB is full integrity**, that the lexicals exists, there are no orphans and forward and backward tracking is in tact (and **indexed, tracking by scanning text should be discouraged**)"

## Order is fixed
**b → c → d → e**, per book. Roles (c) are re-assessed **before** span/gate-1 completeness (d) — because the role decides which spans are characteristic, which is what determines what must be recorded. Reading (any of c onward) does **not** start before the reading units (b) are confirmed/reworked.

## Supporting principles the researcher has stated (hold these)
- A word's **role** is assessed in the context of the verse/passage, in strict order: **characteristic → else qualifier (operates with a characteristic) → else standalone**. "the order of evaluation is important."
- **`mti_terms` is NOT the definition of primary inner-being.** It is a record of terms already in the study and is **incomplete by definition**. A word is characteristic by its **use and meaning in the context of the verse/passage** and that it does/says something about the inner being — never by a lookup table.
- Tracking is by **index/FK, forward and backward**; **text-scanning is discouraged**.
- Fixes are **strictly per book; nothing across books.**

## My operating discipline under this instruction (agreed 2026-07-07)
The researcher will not trust my memory and will not let me drift far before spotting and correcting it. Accordingly:
1. **I follow a → e in order. I do not reorder or skip steps.** (The Proverbs error was jumping to a d/e-type backfill with no (c).)
2. **No improvising in gaps.** When the instruction does not literally cover a case (ambiguous term, tangle, choice of validation method, a resolution heuristic), I **halt and surface it, and do nothing**, until the researcher decides. Filling a gap with my own invention is defined as a **failure**, not helpfulness.
3. **I narrate before acting** — which step I am on and exactly what I am about to do — so drift is visible immediately.
4. **No cross-book operations.** Index-based tracking only.
5. Every write is **integrity-gated**, and every completeness/correctness claim must be **independently (non-circular) verifiable** — I will not report existence as correctness (see `wa-backfill-completeness-claim-CORRECTION-20260706.md`).

## Marker convention — `SPAN_UNRESOLVED` (step-b residual that step-c MUST resolve)
When a verse-record's link to its master-index span is **ambiguous** (the term repeats in the verse with differing forms and nothing — including `target_word` — singles out the occurrence), step (b) does **not** guess. Instead it marks the record and **both/all** candidate spans, deferring resolution to the step-c lexical read:
- **`wa_verse_records.analysis_marker = 'SPAN_UNRESOLVED'`** on the record (its `verse_span_id` stays NULL).
- **`ve_lexical.notes` contains `SPAN_UNRESOLVED_VR:<record_id>`** on every ve_lexical item of **each candidate span** — because if the right span is unknown, **all candidates need revision**.

**Step (c) obligation:** when the role/lexical of a marked span is (re)assessed, the process MUST (1) revise the candidate spans' lexical, (2) bind each `SPAN_UNRESOLVED` verse-record to the correct span (set `verse_span_id`), and (3) clear both markers. Until then these records trace to a passage (verse_id set) but not to the master index — a known, tracked residual, never silently linked. (First applied to Proverbs' 34 residuals, 2026-07-07.)

*Recorded 2026-07-07. This is the reference to read before any corrective work on any book.*
