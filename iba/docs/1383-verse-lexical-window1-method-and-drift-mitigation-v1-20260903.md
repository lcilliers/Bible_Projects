# Verse-lexical Window 1 — repeatable method and drift-mitigation plan

**Filename:** 1383-verse-lexical-window1-method-and-drift-mitigation-v1-20260903.md
**Escalation:** #1383
**Why this document, not another passage.** Direct researcher correction: redoing individual
passages, and raising a fresh escalation per finding, both fragment the work and miss the actual
point of this session — not five deeply-analysed passages, but **the shape and method that will be
run, unchanged in kind, across the whole corpus**, with the specific failure this session surfaced
(selective attention, narrative-confirming bias) structurally prevented rather than avoided by
trying harder next time. This document is that method. #1442/#1443 are folded in below as evidence,
not left as separate threads needing their own resolution path.

---

## 1. What actually went wrong, stated as a mechanism, not a mistake

The applied-checklist document decided **which codes got full treatment** by reading each verse and
judging what looked interesting. That is the checklist's own forbidden move ("work from the row,
not the gloss") committed one level up — not in how any single row was read, but in which rows were
read at all. Two concrete, evidenced costs, both from the *same* root cause:

- `G1063` ("for," Gal 5:17) was called `inert` in the first pass. It's a causal connective. Missed
  because function words got a fast, un-scrutinised pass while content words got the attention.
- The `G1937`/`G1939` (desire, verb/noun pair) connection got a passing mention instead of the
  escalation it deserved, **and was nearly missed entirely** — it only surfaced because I happened
  to compare two verses by eye. Running the related-words pull for *every* content code (not the
  ones that looked worth it) would have handed it over directly: `G1939` sits in `G1937`'s own
  `strong_related` rows.

**The general failure mode**: any process where "does this code get full treatment" is itself a
judgement call, drifts. It doesn't matter how careful any single pass is — selection happens before
judgement gets a chance to be careful about anything.

## 2. The fix is structural, not disciplinary

Three layers, each with a different guarantee:

### Layer 1 — Mechanical facts. Must be code. Must run on every code, no exceptions, no selection.

Anything answerable **without reading and interpreting the verse** belongs here — a deterministic
function of `strong`/`morph_code`/`role`/`strong_related`, nothing else:

| Check | Deterministic from | Demonstrated below |
|---|---|---|
| Same-code, different-gloss (data quality) | `strong`, compare glosses within the verse | yes |
| Hebrew narrative-morph flag (wayyiqtol) | `morph_code` pattern | yes (existing chain test) |
| Negator flag | a small, explicit, evidence-built lexicon of negator codes | yes |
| Connective type (causal / coordinating / purpose) | a small, explicit, evidence-built lexicon | yes — **this is new**, replaces "read the gloss and guess" |
| Related-words, full pull | `strong_related`, every content-role code | yes |

**The connective lexicon is the key structural change.** The first-pass document tried to classify
`H3588A`/`G1063`-type connectives by reading them in context each time — and got one wrong. A
small, explicit, growable lookup table (seeded from this session's own real evidence:
`H3588A`/`G1063`→causal, `H9002`/`G2532`/`G1161`→coordinating, `G2443`→purpose) turns that into a
mechanical lookup. **An unlisted code is reported `UNCLASSIFIED`, never silently defaulted to
"inert" or skipped** — the lexicon grows by evidence, the same way the negator/wayyiqtol checks
already do, never by guessing in the moment.

**Proof, not assertion** — the script below, run live against Gal 5:16–17 (`iba.db`, unmodified,
read-only):

```python
CONNECTIVE_LEXICON = {
    'H3588A': 'causal', 'G1063': 'causal',
    'H9002': 'coordinating', 'G2532': 'coordinating', 'G1161': 'coordinating',
    'G2443': 'purpose',
}
NEGATOR_LEXICON = {'H0408', 'H3808', 'H3809', 'G3756', 'G3361', 'G3760', 'G3761'}
# ... full script: every span/verse_lexical row for the verse, every content code gets a full
# strong_related pull, every function word gets checked against both lexicons, no selection.
```

Real output (unedited):

```
=== Gal.5.16 ===
  p0    G1161 CONJ       role=function | gloss_consistent=YES CONNECTIVE=coordinating
  p5    G3756 PRT-N      role=function | gloss_consistent=YES NEGATOR
  p5    G3361 PRT-N      role=function | gloss_consistent=YES NEGATOR
  p7    G1939 N-ASF      role=content  | gloss_consistent=YES related_pull=[8] ['G0120','G1937','G1938','G2114','G2115','G4288']...

=== Gal.5.17 ===
  p0    G1063 CONJ       role=function | gloss_consistent=YES CONNECTIVE=causal
  p1    G1937 V-PAI-3S   role=content  | gloss_consistent=YES related_pull=[10] ['G0120','G1909','G1938','G1939','G2114','G2115']...
  p13   G2443 CONJ       role=function | gloss_consistent=YES CONNECTIVE=purpose
```

Both real problems from the first pass are gone here, mechanically, not by me being more careful:
`G1063` gets `CONNECTIVE=causal` automatically; `G1939` appears in `G1937`'s own `related_pull`
(and vice versa) without anyone comparing verses by eye. **This is what "structural" means** — the
same script run against verse 40,000 in the corpus behaves identically to verse 1, because there is
no attention to allocate.

### Layer 2 — Judgement-bearing calls. Still per-code, but now impossible to silently skip.

Idiom sense-selection, related-word sorting (same-concept vs. coincidental), pronoun/entity
resolution, structural-pattern naming, genre determination — these genuinely need reading and
thought, and stay manual (or Claude-assisted, chat-driven, per the researcher's own already-decided
process model — not mechanized). **What changes**: Layer 1's output is the input to this layer, not
something re-derived by hand each time. Every code already has a row, a related-words list, a
connective classification, before judgement starts — so there is no "row I didn't get to," only
"row I looked at and made a call on." The completeness guarantee moves from *discipline* ("remember
to check everything") to *structure* ("the table already has every row; fill in the judgement
column or mark it not-applicable").

### Layer 3 — Reporting. Symmetric, not curated.

The first-pass document's summary was a highlights reel — "confirms," "closes the gap,"
"validates." That framing itself is what let real misses (the `G1063` error, the near-missed
`G1937`/`G1939` link) sit alongside genuine wins without anyone weighing them differently. Going
forward, a run's report is a **tally against Layer 1's complete enumeration** — how many codes
processed, how many connectives found and of what type, how many negators, how many
related-words pulls returned zero results, how many `UNCLASSIFIED` connectives (a number that
should point at the lexicon needing growth, not get glossed over) — plus a plain list of judgement
calls made, each labelled resolved / genuine-open-question / correction-to-prior-item. No "wins"
section, no framing that the checklist is being proven.

## 3. What this means for the build plan (§8 of the main design doc) — a recommendation, not a decision

**Layer 1 should be the first real build increment**, ahead of schema for `verse_lexical_note`:
it needs no schema change (it reads `span`/`verse_lexical`/`strong`/`strong_related`, all live
today), it's read-only, and it directly converts the failure mode this session found into something
that cannot recur mechanically. Concretely: a small `lexical_qa` support module — given a verse or
passage, returns the complete Layer-1 table for every code — used as the mandatory first step
before any Layer-2 judgement work starts, by me or by the researcher. Registration (cfg_utility,
etc.) follows the normal governed path if and when this is approved for real; nothing here has been
built into the live app.

## 4. Why this is what makes the scale problem tractable, not worse

The researcher's own standing concern (#1379 v1: 66 books, ~40,000 verses, "I don't have enough
years in my lifetime") is real, and exhaustive-by-hand treatment (the calibration doc's single
verse, which took substantially longer than its share of 19) makes it worse, not better, if every
verse needs that. **The point of Layer 1 is that it removes the mechanical share of the work from
the per-verse manual burden entirely** — related-words pulls, connective classification, negator/
recurrence checks all happen once, automatically, at whatever scale is needed. What's left for
manual, one-at-a-time, chat-driven judgement (per the researcher's own already-decided process
model) is genuinely just the judgement-bearing surface: idiom sense, related-word sorting, pronoun/
entity resolution, structural-pattern naming, genre. That's a smaller, boundeder task than
re-deriving everything by hand each time — and it's the same shape of split #1383's own schema
design already proposed for the DB (cheap mechanical columns vs. judgement-bearing notes),
extended here to the *process*, not just the storage.

## 5. Explicit scope note

#1442 (desire noun/verb pair) and #1443 (recurring verse-structure gap) stand as the **evidence**
this method answers — #1442 by showing Layer 1's related-words pull finds it automatically; #1443
is *not* resolved by this document (verse-level structural findings are a different grain than any
per-code layer, mechanical or judgement) and stays a genuine open question, but doesn't need a
third escalation to say so. No further passages, no further individual-finding escalations this
session — this document is the deliverable.
