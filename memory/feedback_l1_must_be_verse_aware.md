---
name: feedback_l1_must_be_verse_aware
description: The first V3_2 L1 build FAILED researcher eval (2026-06-08) — a mechanical, per-(verse,term), term-uniform L1 is insufficient. Verse context matters EVEN for single-sense terms. L1 must be verse-aware. Keyword extraction needs whole-words + a self-check.
metadata:
  type: feedback
---

The first V3_2 L1 run on M01 (`scripts/v3_2_l1.py`, 2026-06-08) **failed** researcher evaluation. V3_2
execution was **parked**; the L1 DB writes reverted (M01 to pre-L1; `analysis_note` preserved).

**Why it failed — two classes:**
1. **Keyword extraction technically broken:** over-stemmed fragments (`anxiou`, `terrifi`), stem duplicates
   (`terrify`/`terrifi`), transliteration leakage (`rah`), analytic-method terms (`metonymy`). **No
   self-check.** → keywords must be **whole words** (lemmatise or curate); **the script must validate its own
   keyword output** (dictionary / dedup / translit filter / linguistic-term stop-list).
2. **L1 logic too crude:** it applied a term's head meaning **uniformly to all its verses** and **trusted the
   old `is_relevant`**, so it missed:
   - **verse-level relevance/context** — Song 6:4/6:10: `a.yom` ("terrible/awesome") on *beauty* should be
     **set aside**, not stamped "terrible". **Relevance/pole is per-verse, not per-term.**
   - **multi-term verse arrays** — Psa 55:3: processed as one item; "trouble"/"grudge" not seen (L1 reads each
     `(verse,term)` row independently, never the verse's array of inner-being terms).
   - **sibling-span pairing** — Hab 1:7 "dreaded **and** fearsome": only one of the pair caught (see
     [[feedback_span_pairing_and_reciprocal_findings]]).

**Governing lesson:** **L1 is NOT purely term-level/mechanical — it must be verse-aware** (re-evaluate
relevance in context; see all inner-being terms in a verse together; pair sibling spans). The
"single-sense → assign term meaning uniformly" shortcut is wrong wherever the term is used non-relevantly /
metaphorically in a given verse. This refines [[feedback_term_corpus_anchors_meaning]] and discipline 2 in
[[project_a1_resolved_rollup_v3_audit_design]].

**Re-prototyping plan (read-only, report-before-write):** P1 keyword rebuild + self-check; P2 verse-aware L1
(relevance-in-context, per-verse term array, span pairing), tested against the Song 6 / Psa 55:3 / Hab 1:7
cases. Detail: `research/investigations/wa-l1-test-failure-analysis-v1-20260608.md`. A failing test is the
design working — a real verse read exposed gaps a mechanical shortcut hid.
