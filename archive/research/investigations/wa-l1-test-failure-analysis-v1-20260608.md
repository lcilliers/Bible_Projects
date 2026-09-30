# L1 test on M01 — failure analysis + re-prototyping plan

> **Investigation · v1 · 2026-06-08 · CC.** The first V3_2 L1 run on M01 (`scripts/v3_2_l1.py`,
> 2026-06-08) was evaluated by the researcher and **failed**. V3_2 execution is **parked**; the L1 DB writes
> were **reverted** (M01 back to pre-L1 state, `analysis_note` preserved). This records the specific failures
> (as test cases) and the plan for explicit prototyping/testing of the **keyword** and **L1** process before
> any re-attempt. Honest verdict: **L1 as built is not ready.**

---

## 1. Keyword extraction — technically broken (no self-check)

| Defect | Examples | Cause |
|---|---|---|
| **Over-stemmed fragments** | `anxiou` (anxious), `terrifi` (terrified) | naive suffix-stripping truncates real words |
| **Stem duplicates** | `terrify` **and** `terrifi` as separate keywords | inconsistent stemming → dupes |
| **Transliteration leakage** | `rah` (and more) | translit fragments not filtered |
| **Analytic-method terms** | `metonymy` (also `metaphor` etc.) | linguistic-analysis words in `sense_text` leak through |

**Required:** rebuild keyword extraction so keywords are **real, whole words** (no naive stemming — use a
lemmatiser or a curated inner-being vocabulary), and add a **self-check** that rejects: non-dictionary
fragments, duplicates, transliterations (dot-notation / Hebrew-translit patterns), and linguistic-analysis
terms (metonymy/metaphor/synecdoche…). *The script must validate its own keyword output.*

## 2. L1 logic — too crude conceptually (the real failure)

L1 applied a term's head meaning **uniformly to all its verses** and **trusted the old relevance flags**. The
researcher's examples show this misses three real classes of verse:

### Test case A — verse-level relevance/context (term used non-relevantly)
- **Song 6:4 & Song 6:10** — `a.yom` ("terrible / awesome") applied to the woman's **beauty** ("awesome as an
  army with banners"). **This is not fear/terror — it should be SET ASIDE** (or at least a different
  sense/pole). L1 blindly applied "terrible" because the old `is_relevant=1` said so. **L1 must re-evaluate
  relevance in context, not trust the legacy flag and stamp the term meaning.**

### Test case B — multi-term verse arrays (processed as a single item)
- **Psa 55:3** — a **complex array of fear/distress terms**; "**trouble**" and "**grudge**" were not picked
  up; the verse was processed as one item. **L1 processes each `(verse, term)` row independently, so it never
  sees the verse's other inner-being terms** — it can't read the array.

### Test case C — sibling-span pairing (only one of a pair caught)
- **Hab 1:7** — "they are **dreaded and fearsome**" — **two paired terms**, only one captured. **Span/sibling
  pairing (T1/T2) is not handled** (cf. `feedback_span_pairing_and_reciprocal_findings`).
- *"…and there are many more of these examples."*

**Root:** the build skipped real parts of the design — **relevance re-evaluation** and **span/multi-term
handling** — and over-trusted the "single-sense → uniform term meaning" shortcut. Verse context matters
**even for single-sense terms.** A mechanical, per-`(verse,term)`, term-uniform L1 is insufficient.

## 3. What this means for the design

- **L1 is not purely term-level/mechanical.** It must be **verse-aware**: re-evaluate relevance in context,
  see all inner-being terms in a verse together (the array), and pair sibling spans. This may move some work
  the build deferred (or shortcut) back into L1 — to be settled in the design, not papered over.
- The "assign single-sense uniformly" rule (discipline-2-compliant on *ambiguity*) is **still wrong when the
  single-sense term is used non-relevantly or metaphorically in a given verse** (Song 6). Relevance/pole is
  per-verse, not per-term.

## 4. Re-prototyping plan (explicit; before any L1 re-attempt)

**P1 · Keyword extraction + self-check** *(read-only prototype):*
- Rebuild the keyword source (whole words; lemmatise or curate); add the self-check (dictionary, dedup,
  translit filter, analytic-term stop-list). Run on M01+M02, report keyword quality + the self-check results.

**P2 · L1 logic, tested against the cases** *(read-only prototype):*
- Build the verse-aware pieces: (a) **relevance-in-context re-eval**; (b) **per-verse term array** (group a
  verse's inner-being terms); (c) **sibling-span pairing**. Evaluate against test cases A/B/C + a sample, and
  report — *no DB writes* until the logic is validated.

**Sequencing:** P1 first (bounded, clear), then P2 (the harder rethink). Each is a read-only prototype that
**reports**; the researcher evaluates with full information before the design/L1 is changed.

---

## 5. State

- **V3_2 execution parked.** M01 L1 writes **reverted** (verse_context L1 fields NULL; status back to
  "Analysis Completed (Terms Added)"; `analysis_note` preserved). Backup
  `backups/bible_research_pre_L1_M01_20260608.db` retained.
- The flawed L1 report (`Sessions-v2/M01-Fear/wa-cluster-M01-v3_2-L1-run-v1`) is kept as the **failing
  evidence** these test cases came from.
- `scripts/v3_2_l1.py` retained but **not ready** — superseded by the prototyping above.

*The test failing here is the design working as intended: a real verse-level read exposed gaps a mechanical
shortcut hid. Fix the design, then re-run.*
