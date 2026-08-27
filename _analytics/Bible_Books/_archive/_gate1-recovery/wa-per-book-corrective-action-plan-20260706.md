# Per-book corrective-action methodology (researcher's plan, 2026-07-06)

> Captured from the researcher's direction, for review/correction before any execution. This is the governing plan for repairing the study's integrity. Nothing here is executed yet.

## Governing principles

1. **Work strictly by book.** One book fully corrected before the next.
2. **No fix across books.** No global/cross-book operations; each book is completed and validated on its own.
3. **The role dimension cannot be fixed standalone** — it depends on the reading unit (passage vs verse) being correct first. So reading units precede role.
4. **No reading starts until the reading units are confirmed and captured in the tables.**
5. **Forward and backward tracking must be by indexed FK links, not by scanning text.** The chain must be traversable both directions: master index (`verse_span_index`, term-span-verse) ↔ passage ↔ lexical (`ve_lexical`) ↔ verse(s).

## The per-book pipeline (ordered)

### (a) Scope: one book
Select the book. Everything below is confined to it.

### (b) Reading units — confirm or rework, and CAPTURE in the tables *(gate: nothing proceeds until done)*
- Confirm each verse's reading unit: **if it belongs to a passage, the passage is the reading unit; if not, the verse is.**
- Where the passage grouping is missing or inaccurate, **rework it** (the prophets are largely un-passaged today — Ezekiel/Jeremiah/Psalms/Isaiah hold ~61k lexicals on verses with no `passage_id`).
- Ensure the reading units are **captured in the tables** with **forward + backward, indexed** links:
  - `verse_span_index` (master) → `verse` → passage
  - passage → its verses (reverse)
  - `ve_lexical` → span → verse → passage, and back
- **Fix these tables where the links are missing/broken.**

### (c) Role dimension — re-assess, fix if needed
- With the correct reading unit known, **read the passage (or verse) and assign each span one of three roles**, in order:
  1. **characteristic** — by its use and meaning in this context it says/does something about the inner being;
  2. else **qualifier** — it operates with (supports) a characteristic in the reading unit;
  3. else **standalone**.
- Definition anchor: a characteristic is decided by **the word's meaning in context**, *not* by any existing term list (`mti_terms` is a record of what's already in, incomplete by definition, so it cannot be the test).

### (d) Gate 1 completeness — a STEP action
- For **all characteristic spans**, ensure the DB is complete:
  - the **term is recorded**,
  - its **verses are pulled** (via STEP),
  - **all links are built and intact**.
- This catches characteristic spans that have no term/verse-record yet and completes them.

### (e) Validate — full integrity on book completion
- The lexicals exist for the book.
- **No orphans** anywhere in the chain.
- **Forward and backward tracking intact and indexed** (never dependent on text-scanning).

## Open decisions to confirm before starting (execution-affecting)

1. **The "passage table."** Today the passage is a *column* (`verse.passage_id`, the mechanical 3,650-run grouping the lexical build used) — *plus* a separate `segment_unit` table (the narrative reading units, GEN-01…, forward/backward linked). Step (b) needs one canonical, FK-linked passage table. **Decision:** make `segment_unit` the canonical reading-unit table for every book (rebuild per book), or formalise/repair `verse.passage_id` into a linked table? (My read: `segment_unit` already has the forward/backward structure; `passage_id` is just a column.)
2. **First book.** Which book is the pilot for the pipeline? (Isaiah is where we've been testing; a smaller prophet or a clean book may be a better first run.)
3. **STEP source for (d).** Confirm Gate-1 verse-pulling uses the STEP local server (`http://localhost:8989`) as the authoritative occurrence source, per the existing `step_client`.
4. **Global term registry vs by-book.** `mti_terms` is one-row-per-Strong's programme-wide (inherently cross-book). Under "no cross-book fix," the intent is presumably: the registry stays global, but a book's characteristic terms are *registered/completed as that book is processed* — not pre-populated across books. Confirm. (Note: the recovered-term onboarding done earlier this week was a cross-book action and may need to be re-examined under this discipline.)

*Filed 2026-07-06 as the governing corrective plan. Awaiting the researcher's confirmation/correction and the four decisions above before any book is started.*
