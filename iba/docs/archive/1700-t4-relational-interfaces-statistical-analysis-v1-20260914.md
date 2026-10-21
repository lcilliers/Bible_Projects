# Escalation #1700 — T4 (Relational Interfaces) statistical analysis, pass 1

**Method:** full, unsampled SQL/statistical analysis over every non-deleted finding linked to
every T4 question (28 questions, live-queried against `bible_research.db`) — no LLM reading yet,
per the researcher's own instruction to see what the data itself shows first. Raw per-question
stats: [`1700-t4-relational-interfaces-statistics-v1-20260914.json`](1700-t4-relational-interfaces-statistics-v1-20260914.json).
Cleaned version (fan-out findings separated out, see §2): [`1700-t4-relational-interfaces-statistics-clean-v1-20260914.json`](1700-t4-relational-interfaces-statistics-clean-v1-20260914.json).

## 1. The a/b split codes are completely unexercised

`T4.6.2`/`T4.6.3` exist as BOTH a unified code (with real findings: 110 and 103 respectively) AND
a later mechanical/interpretive split (`T4.6.2a`/`2b`, `T4.6.3a`/`3b` — matching #1444's mechanical/
interpretive split pattern seen elsewhere in this catalogue). **All four split codes have zero
findings, ever.** The split was made in the catalogue but never actually exercised in practice —
every historical answer still lives under the old unified code. Relevant to #1696: these four rows
are among the 98 migration candidates, but carry no evidence of real use.

## 2. A small number of "blob" findings answer many questions at once — a real genericity problem

Of the 2,832 distinct findings linked to T4's original 24 questions, the overwhelming majority
(2,693, ~95%) are clean 1:1 — one finding answers one specific question. But **26 findings are
linked to between 5 and 24 different T4 questions simultaneously**, and two of those (ids `2196`,
`2168`) are each linked to **all 24** of T4's original questions with the same single paragraph.

Example (finding `2196`, cluster `M04`, `level=CLUSTER`, created 2026-05-01 — early in the
project): *"T4 establishes the most precisely articulated relational architecture of any
characteristic in the review set. The God-to-human direction is primary and dominant..."* — a
genuine, well-written paragraph, but a **component-level synthesis statement, not an answer to any
one of T4's 24 individually-worded questions**. Linking it to all 24 inflates every one of their
naive "finding count" stats identically and contributes nothing question-specific. This is a
concrete, historical instance of exactly the "does the answer provide value relative to the
question" problem — not drift (inconsistency across items), but **genericity**: one broad claim
standing in for 24 precise ones.

This is now a small, well-defined, justified target for actual AI reading (26 findings, not
2,832) — worth confirming by inspection whether all 26 are genuinely this kind of blob, or whether
some legitimately touch several closely-related questions.

## 3. A robust, cross-component pattern: the LAST sub-question in each Interface component is answered worse

After removing the 26 "blob" findings above (the `_own_*` columns in the clean JSON — findings
that answer *only* this one question), a clear and **consistent** pattern holds across all six
Divine/Human Interface components:

| Component | Evidentiary sub-qs (mean len / dup%) | Wrap-up sub-q ("...4") (mean len / dup%) |
|---|---|---|
| Divine Interface — God→Human (T4.1) | 670 / 588 / 606 (3–10%) | **190 (18.6%)** |
| Divine Interface — Human→God (T4.2) | 580 / 533 / 582 (2–11%) | **169 (16.3%)** |
| Human Interface — Giving (T4.3) | 567 / 528 / 507 (3–12%) | **194 (21.2%)** |
| Human Interface — Receiving (T4.4) | 536 / 499 / 485 (8–14%) | **195 (19.4%)** |
| Human Interface — Boundaries (T4.5) | 581 / 527 / 515 (10–17%) | **159 (19.4%)** |
| Spiritual Beings Interface (T4.6) | 395 / 429 / 225\* (11–18%) | 503 (18.0%) |

\*T4.6.3's own third evidentiary sub-question is itself already short (225) — this component is
the one exception where the pattern doesn't cleanly hold at the wrap-up question.

Every ".4" question in this catalogue's Interface components is the **interpretive "what does
this show about the relational scope/pattern" wrap-up** (per the question text itself, e.g. T4.5.4:
*"What does the evidence show about the relational scope of the characteristic — who is included
and who is not?"*). Across five of six components, these wrap-up questions get answers **roughly
a third the length** and **1.5–3x the duplication rate** of the evidentiary questions that feed
them. This isn't noise — it's the same shape five times over. It reads as the LLM (or researcher,
historically) treating the wrap-up question as a quick restatement rather than doing fresh
synthesis work, once the harder evidentiary questions were already answered.

## 4. Usage breadth looks healthy, aside from the above

Every populated question was exercised across 13–20 of the corpus's clusters and a similar spread
of distinct dates — broad, not a narrow one-off pattern. This is the "unused vs. inconsistently
used" distinction from the #1700 raise: T4's problem is not non-use, it's **genericity at scale
(finding #2)** and **a specific weak question-type (finding #3)**, not blanket neglect.

## What this suggests for next steps — not decided here

- **Finding #2** (blob answers) is now a small, targeted, justified AI-reading task: 26 findings,
  not 2,832 — read them to confirm the genericity read and see if any should be treated
  differently.
- **Finding #3** (wrap-up question weakness) suggests the "interpretive drift" concern may be less
  about the LLM disagreeing with itself across items, and more about a **specific question
  archetype** (the summary/wrap-up question) being answered shallowly wherever it appears — worth
  checking whether this same "...4-position" pattern holds in other sections (T1, T5 etc. also
  have similarly-shaped components) before deciding it's real, or T4-specific.
- Neither of these needed sampling — the full, unsampled statistical pass surfaced them directly,
  which is itself evidence for continuing this way (full population, one section at a time) rather
  than sampling, before reaching for any AI judgment at all.
