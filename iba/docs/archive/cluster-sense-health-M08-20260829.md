# Testing the "finite lexical list = valid inner-being descriptives" premise — M08 (Pride, Arrogance and Boasting)

**Date:** 2026-08-29
**Raised by:** researcher, in the #1007 catalogue-quality conversation
**Premise being tested:** the inner-being characteristics/descriptives are all in the lexicals, and
that is a finite list — so a cluster's health can be checked by listing every "sense" tied to its
Strong's numbers and how many verses each sense covers.

Data source: `iba/app/db/iba.db` — `cluster`, `cluster_strong`, `verse_lexical`, `strong`. Read-only
queries, no writes. Full per-sense and per-strong tables are reproducible from the queries logged in
this session; not re-attached here to keep this file focused on the findings, per researcher instruction
to keep this readable rather than dumping raw output.

## 1. The direct answer

M08 = **Pride, Arrogance and Boasting** (`cluster.gloss` lists ~87 English/Strong's glosses).

- **87 Strong's numbers** tied to M08 in `cluster_strong` (all active, none deleted).
- **84 of those 87** have any `verse_lexical` data at all. Zero-coverage: G3166, G7013, G7973.
- **1,192 distinct verses** touched by any M08 Strong's (1,326 total occurrences across those verses —
  84 verses carry more than one M08 Strong's).
- Grouped by `resolved_sense` text (the literal ask — "every inner being sense... with a count of the
  verses it appears in"): **105 distinct sense-strings**, ranging from 363 verses down to 1 verse.

That table exists and I can hand it over in full (CSV or inline) if you want it as a working artefact —
but the more important finding is *what `resolved_sense` actually is*, below, because it changes what
that 105-row list means.

## 2. `resolved_sense` is not a curated sense — it's the raw dictionary text, auto-assembled

Checked directly in code (`iba/app/lib/lexical.py`, `resolve_code()`): for every Strong's/morph-code
combination, `resolved_sense` is built as `"stepGloss: {gloss}"` plus, when a `strong_meaning_parsed`
row exists, the concatenated `strong_meaning_parsed` glosses, plus LSJ and Mounce text appended
verbatim (` | lsj: ... | mounce: ...`). There is no interpretive step — it is a mechanical
concatenation of the lexicon fields, one variant per Strong's/morph-code.

This is confirmed by the shape of the data: **84 of the 87 Strong's numbers produce exactly 1 distinct
`resolved_sense` string** each (a handful — H6965B, H7311A, H7682, H3887, H3932, H1984I, H7426— split
into 2–5 because different inflected forms fall back to slightly different lexicon text). So the
"105 senses" is not 105 independently-identified shades of meaning — it is **~1:1 with the 84 Strong's
numbers themselves**, wearing the dictionary's own wording as a label.

**Implication:** "list every sense and count its verses" and "list every Strong's and count its verses"
are, in this cluster, almost the same query. The lexical layer doesn't currently offer a distillation
of inner-being descriptives finer or coarser than the Strong's list — it just restates each Strong's
own gloss. That's consistent with what you're seeing in the catalogue answers: the "sense" data
available to answer a catalogue question *is* the dictionary entry, so an answer built from it is
close to guaranteed to just restate the dictionary entry.

## 3. A second, sharper problem: the two biggest contributors don't look like Pride at all

Per-Strong's verse counts are extremely top-heavy:

| Strong's | stepGloss | verses | % of M08's 1,192 |
|---|---|---|---|
| H6965B | "to arise: rise" | 370 | 31% |
| H7311A | "to exalt" | 184 | 15% |
| (next 82 Strong's) | — | 638 | 54% |

The top two alone are **46%** of the cluster's entire verse coverage.

I checked `cluster_strong` provenance for both:

- **H6965B** — added by `llm-allocation-v1_3-20260811`, `confidence=medium`, rationale logged as
  *"no precedent; profile suggestion M08:5.9 | accepted"*. Auto-allocated, not manually reviewed
  (`review_flag=0`).
- **H7311A** — `source=old-system-migration`, no confidence/rationale recorded (legacy carry-over).

I pulled a random sample of the actual verse text for both (12 verses for H6965B, 10 for H7311A,
`random.seed` fixed so this is reproducible, not cherry-picked):

- **H6965B sample** — Judg 5:7, Exo 12:31, Nah 1:6, 1Sa 23:4, Judg 7:9, Num 22:13, 2Ch 20:19,
  Isa 28:21, 1Ki 19:8, 1Ki 14:4, 1Ki 1:50, Judg 19:10. Every single one is ordinary narrative "got
  up / arose / stood up" (Balaam rose in the morning, Jeroboam's wife arose and went to Shiloh, the
  Levites stood up to praise God). **None carries any pride/arrogance content.**
- **H7311A sample** — Isa 58:1, Psa 89:13, 2Ki 19:22, Lev 2:9, Psa 27:5, Isa 40:9, Psa 138:6, Eze 31:4,
  Psa 12:8, 2Sa 22:49. Mixed but mostly literal "lift up voice / lift up hand / lift up the memorial
  portion at the altar" — only 2 of 10 (2Ki 19:22 "lifted your eyes to the heights" against the Holy
  One; Psa 138:6 "the haughty") are actually about pride.

**H6965B (qum, "to arise") is a generic, extremely common Hebrew verb** — it is not a pride word in
the great majority of its occurrences. Its presence in M08 appears to be a mis-allocation: an
LLM profiling pass scored it 5.9-ish for M08 based on its overall usage profile (it does occasionally
carry a hostile/exalting sense — "to arise against," "to become powerful" — which the `cluster.gloss`
entry for M08 does list), accepted it at medium confidence with no human check, and it now supplies
roughly a third of the cluster's total verse volume with content that is overwhelmingly not about
pride.

## 4. What this means for the premise

The premise as stated — "the inner-being descriptives are all in the lexicals, and that's a finite
list, so I can test cluster health by listing lexical senses per cluster" — **partially holds and
partially doesn't**, on this one test case:

- **Holds:** the lexical layer is finite and enumerable — you can produce the exact list, which is
  useful.
- **Doesn't hold as a health check on its own:** the "sense" field carries no distillation beyond the
  raw dictionary gloss (§2), so a sense-frequency count mostly just re-measures how common a Strong's
  root is in the whole Bible, not how much pride-content it actually carries in context. And the
  cluster-assignment layer that decides *which* Strong's numbers count toward M08 in the first place
  has at least one clear, well-evidenced false-positive (H6965B) sitting at the top of the frequency
  list, inflating the cluster's apparent verse coverage — which is exactly the "same finding repeated
  a thousand times, no new insight" pattern you described, just showing up one layer earlier than the
  catalogue-question layer.

This overlaps with **escalation #738** (Cluster-Assignment Backfill Exceptions, on-hold pending
analysis-phase start) — that escalation flagged a different symptom (non-T2 clusters with no
word_registry link); this is a same-family problem (unreviewed automated cluster assignment) found a
different way.

## 5. Open question for you

Two directions from here, and I'd rather you pick than guess which is the useful next step:

1. **Widen the same test** — run this Strong's-verse-frequency + provenance check across all clusters
   (or a handful more) to see whether "one or two generic high-frequency roots dominate the cluster and
   don't actually belong" is a one-off (M08 only) or a systemic pattern worth a real cleanup pass.
2. **Go narrow first** — before widening, manually read through M08's full 87-Strong's list against
   its actual verses and decide, cluster by cluster, which Strong's numbers should be pulled/flagged —
   i.e. treat this as the first real instance of #738's backlog rather than a new investigation.

Either way, this is a data judgement call (which Strong's numbers genuinely belong in a cluster) that
needs your read, not something I'd resolve by rule.
