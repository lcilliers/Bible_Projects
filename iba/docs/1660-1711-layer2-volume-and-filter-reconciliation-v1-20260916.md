# #1660 reconsidered for Layer 2's stage 5 — volume, filters, and why the two aren't the same question

**Escalation:** #1660 (reopened for this specific question) / #1711 · **Date:** 2026-09-16

**Researcher's framing this turn:** *"1660 was trying to think through the volume impact of the
lexical data into the next analytic phase — however, at that stage it was not yet conceptualised
to have layer 2 answering the questions. perhaps 1660 must be approached with new eyes, and also
think through volume and filters for the layer 2 llm process."* Correct chronology: #1660 closed
2026-09-10, five days before the researcher's own 2026-09-15 instruction that first described
stage 5 as producing "an observation (linked to a question)." #1660 could not have weighed a design
that didn't exist yet — it was a real, standalone objection to a different, undirected use.

## 1. What #1660 actually objected to, re-read precisely

Not "lexicon data is bad" — the objection was **shape and cost**: *"trying to generate a lexical
with this information for every word is of no value, because it is completely overwhelming for
any analysis process."* Two separable complaints packed into one sentence:

- **Cost/overwhelm** — a volume problem, checkable directly.
- **No value** — a *shape* problem: **undirected, exhaustive documentation** ("generate a lexical...
  for every word") produces noise because nothing tells the reader which of the many facts
  generated actually matters. The determination's own remedy names the shape that *would* have
  value: *"the only time this depth of word analysis would have any value is when the word is
  considered in context and there is doubt or different meaning options need to be considered."*

Stage 5, as it now stands, already answers the shape half by construction, not by argument:
it produces **slant-answers to a specific catalogue question**, not free-form lexical documentation.
"Which of the many facts about this word matter" is answered by the question itself — that's a
structurally different task from what #1660 rejected, not the same task on a new source table.
**But the cost half is still a live, checkable question** — and it hadn't been checked. Now it has.

## 2. The volume, checked live (not estimated)

| Scope | Distinct strongs | `vw_strong_meaning_raw` rows | Total characters (≈ tokens ÷ 4) |
|---|---:|---:|---:|
| **Corpus-wide** (every `cluster_strong`-tagged strong) | 15,706 | 56,687 | 22,498,104 (~5.6M tokens) |
| **M-code strongs only** | 3,101 | 11,878 | 5,151,807 (~1.3M tokens) |

**Scoping to M-code strongs cuts the read by ~78% before any other filter.** This is not a new
idea invented for this reconciliation — it is **already the live precedent**: #1527 (completed,
2026-09-10) restricted `resolved_sense` computation to M-code cluster members only, `NULL` for
T-code-only members, for exactly this reason (T-code-only strongs — particles, negators, party
markers, the T2 catch-all — are grammatical/referent-identity tags, not characteristic-relevant
vocabulary; 12,700 of the 15,706 tagged strongs are T-code-only). Stage 5 inheriting the same scope
is not a new design decision, it's applying an existing one consistently.

**Within the M-code set, checking #1660's own stated trigger** ("doubt or different meaning options"):

| | Count | % of M-code strongs with any `strong_meaning_tree` coverage |
|---|---:|---:|
| M-code strongs with `strong_meaning_tree` rows at all | 2,961 | 100% |
| — of those, >1 listed sense (candidate "doubt") | 2,098 | 70.9% |
| — of those, exactly 1 listed sense | 863 | 29.1% |

**This filter is real but modest** — most M-code vocabulary genuinely is multi-sense (matching what
this whole study is about: words whose meaning shifts by context). A sense-count filter would cut
volume by ~29% on top of the M-code scoping, not the order-of-magnitude cost#1660 was worried about
— that reduction already happened at the M-code scoping step. **Recommendation: don't gate
*whether* a strong gets a stage-5 pass on sense-count** (it would exclude real characteristic
vocabulary for a modest saving) — instead use it to calibrate *how much* work the pass does per
strong (§3).

## 3. Proposed reconciliation — three concrete design inputs for #1711, not decided here

1. **Scope: M-code strongs only (3,101), not corpus-wide (15,706).** Matches #1527's existing
   precedent exactly. Resolves the bulk of #1660's cost objection by construction — 78% volume cut
   before any other measure.
2. **Task shape stays question-directed, not documentation-directed** — already true of stage 5's
   design (§1 stage 5: "slant-answers to the catalogue's term-scoped questions"). This is the
   structural difference from what #1660 rejected; worth stating explicitly in #1711's own design
   doc so the reconciliation is on record, not implicit.
3. **Depth calibration, not a pre-filter, for the single-sense minority.** For the 863 M-code
   strongs with exactly one listed sense, the answer to a lexical catalogue question is expected to
   be short and settled (there's no real ambiguity to explore) — the LLM should be free to answer
   tersely for these, matching the calibration #1700's own review already confirmed as a *virtue*,
   not a defect, elsewhere in this catalogue (e.g. T0.3.2's *"terse, confident negatives... brevity
   here is calibration, not genericity"*). This isn't a new mechanism — it falls out naturally from
   asking a specific question rather than requesting exhaustive documentation; flagged here so it's
   a deliberate expectation, not an accident of prompt wording.

## 4. What this does NOT resolve — still #1711's own open items

Volume/filter is one input to #1711, not the whole design. Still open, per #1706 §4A: the stage's
own name/value, whether it batches per-cluster or corpus-wide in one pass (§5 below adds a data
point), and exactly which catalogue question(s) beyond the T1.1/T7.1 candidates it answers.

**New data point for the scope-grain question (§4A item 2):** 84 M-clusters carry the 3,101
M-code strongs, averaging ~37 strongs each (range 2–213, e.g. M24=213, M67=2). Per-cluster batching
(already the pattern process (a)/(c) use) would keep each stage-5 run to a few hundred strongs at
most, not a single 1.3M-character pass — a practical argument toward per-cluster batching, though
§4A's own countervailing point stands (T1.1/T7.1 want term-grain output, and a term's full
occurrence picture may span clusters) — not fully settled by this alone.

## 5. Bottom line

#1660 and stage 5 are not the same question re-litigated — #1660 rejected an undirected, exhaustive
documentation exercise; stage 5 is a directed, question-answering pass. But #1660's cost concern
was real and unchecked until now. Checked: scoping to M-code strongs (already precedented by #1527)
resolves the volume problem to within the range every other stage in this pipeline already operates
at (~1.3M characters, not 22.5M). Recommend closing this reconciliation as: **stage 5 inherits the
M-code-only scope, answers a specific question per strong (not open documentation), and calibrates
depth to the strong's own sense-count** — three concrete, checked design inputs for #1711 to build
against, not a new open question.
