# T2 (Supplementary) — surfacing mis-parked inner-being terms via STEP sense

> **Investigation · v1 · 2026-06-07 · CC.** Read-only (no DB writes). Tests the researcher's expectation
> that *the STEP-meaning process will surface which parked T2 terms are actually relevant to other clusters.*
> **It does.** Scanner: `scripts/_assess_t2_relevance_surface.py`. Full ranked artifact:
> `wa-t2-relevance-surface-scan-v1-20260607.md`. Feeds the eventual **T2 rework** and the *no-orphans /
> mop-up* discipline (`wa-cluster-rollup-design.md`). Related memory: `feedback_term_is_the_unit_of_movement`,
> `feedback_remediation_is_analysis_not_reassignment`.

---

## What T2 is, and the problem

`T2 = "Supplementary"` is a **parking cluster**: 620 active terms, status *Not started*. Most are genuinely
out of scope (particles "and / not / with", body parts "hand / liver", objects "tower / flask", "to
anoint"). But the `owning_word` column shows a number were **pulled under an inner-life English word and
parked anyway** — so some parked terms are mis-parked inner-being material that belongs in a real cluster.
The task: surface them, mechanically, from the lexicon.

## Method

Same sense-token machinery as A1 corroboration, pointed **cross-cluster**:

1. Build each **named cluster's sense-envelope** = stemmed token-set of `cluster.gloss` (transliterations
   stripped).
2. For each **T2 term**, build its **STEP sense-set** (gloss + `step_search_gloss` + `short_def_mounce` +
   `meaning` + parsed `wa_meaning_sense`).
3. Score term↔cluster overlap, **idf-weighted** (a token shared by many clusters counts less than a
   distinctive one), and rank candidate clusters per term.
4. **Confidence refinement:** cross the surfaced cluster with the legacy `owning_word`. Where they **agree**,
   it is a high-confidence mis-park; where the STEP sense points **elsewhere**, it is a cross-cluster
   reassessment worth a look.

**Candidate ≠ decision.** The score measures token-distinctiveness, not inner-being-ness — so this surfaces
*candidates* the researcher judges, it does not reassign. (And the **term is the unit of movement**: a real
move carries the term's verses/VCGs/findings, and a term with meaning in >1 cluster becomes a finding in
each — `feedback_remediation_is_analysis_not_reassignment`.)

---

## Results

412 of 620 T2 terms overlap some cluster; **121 surface at score ≥ 6.0** (the focused artifact).

### A · High-confidence mis-parks — STEP sense **agrees** with the parked-under word
These belong in the named cluster on two independent signals (lexical sense + the original pull-word):

| Score | T2 term | Gloss | Parked under | → Cluster |
|---|---|---|---|---|
| 12.5 | `fobētron` (G5400) | fearful thing | fear | **M01 (Fear)** |
| 12.5 | `thumoō` (G2373) | to anger | anger | **M02 (Anger)** |
| 8.3 | `ats.tse.vet` (H6094) | injury | grief | **M03 (Grief)** |
| 8.3 | `exischuō` (G1840) | to have power | strength | **M23 (Strength)** |
| 7.9 | `ma.sas` (H4549) | to melt | fear | **M01 (Fear)** *(the "melt with fear" idiom)* |
| 7.9 | `ophthalmos` (G3788) | eye | envy | **M28 (Envy)** *(the "evil eye" = envy)* |
| 7.9 | `enischuō` (G1765) | to strengthen | strength | **M23 (Strength)** |

### B · Cross-cluster reassessments — inner-life parked word, STEP sense points **elsewhere**
The most valuable cases: where the original pull-word was *misleading* and the lexicon corrects it.

| Score | T2 term | Gloss | Parked under | → STEP-surfaced cluster | Note |
|---|---|---|---|---|---|
| 12.1 | `filoneikia` (G5379) | love of dispute | love | **M02 (Anger)** | it is *strife*, not love — pulled under "love" by the English word, correctly re-surfaced to Anger |
| 7.5 | `filoprōteuō` (G5383) | to love to be first | love | **M28 (Envy)** | ambition/rivalry, not love |
| 8.3 | `mar` (H4751) | bitter | anguish | **M03 (Grief)** | bitterness → grief family |
| 8.3 | `anankē` (G0318) | necessity / distress | distress | **M01 (Fear)** | distress↔fear field |
| 7.5 | `ya.tsar` (H3334) | be distressed | distress | **M24 (Weakness)** | distress as being hemmed-in / pressed |
| 16.6 | `a.sham` (H0817) | guilt [offering] | guilt | **M10 (Sin)** | guilt↔sin |
| 8.3 | `latreuō`/`leitourgia`/`latreia`/`sha.rat` | minister / ministry | worship | **M36 (Service)** | worship↔service |

### C · Noise classes to ignore (high score, not inner-being)
The scan also lifts terms that merely *share vocabulary* with a cluster envelope — the researcher filters
these out fast from the matched-token display:
- **Modal/auxiliary verbs:** `ya.khol` "be able", `dunatos`/`dunamai` "able", `echō` "to have" → M23 (share
  "power/able").
- **Divine titles:** `il.lay` "Most High", `tsa.va` "Hosts" → M23/M26 (share "lord/almighty/god").
- **Proper nouns:** `ra.hav` "Rahab" → M08 (the monster connotes arrogance, but it is a name).
- **Generic action verbs:** `a.sah` "to do", `ma.tsa` "to find", `ra.vah` "to multiply".

---

## What this proves

1. **The researcher's expectation holds:** the STEP-meaning process *does* surface mis-parked T2 relevance —
   mechanically, from the lexicon, before any AI reading.
2. **Two signals beat one:** STEP-sense × `owning_word` agreement gives a high-confidence priority list (A);
   disagreement gives the genuinely interesting cross-cluster reassessments (B) — including cases where the
   original English pull-word was *wrong* (`filoneikia` "love of dispute" → Anger).
3. **It is the *no-orphans* discipline for the parked pool:** every T2 term can be scored for a candidate
   home, turning a 620-term "Not started" bucket into a ranked rework worklist.

## Limits

- Token overlap ≠ inner-being relevance; the score ranks distinctiveness, not scope — list C must be filtered
  by judgement.
- `cluster.gloss` is the envelope proxy; a member-term sense-envelope would be richer (and would let the
  surfacing also propose a *sub-group*, not just a cluster).
- Greek/Hebrew homonyms and metaphor (`ophthalmos` "eye"→envy works *because* of the idiom; a literal "eye"
  would mis-fire) — the matched tokens expose this, but a human still adjudicates.

## Recommendation

Adopt this as the **T2 rework entry point**: run the full ranked scan, take list **A** (agreement) as the
priority mis-park set, work list **B** as cross-cluster reassessments, and discard list **C**. Each surfaced
term then enters normal cluster analysis as a **candidate** (term-as-unit-of-movement; meaning-in->1-cluster
→ finding in each), never an automatic reassignment. This is the mechanism that lets the parked T2 pool be
mopped up rather than forgotten — exactly as anticipated.

*Next, if wanted: re-run the surfacing off member-term sense-envelopes (richer than `cluster.gloss`) and add
the `owning_word`-agreement flag directly into the scanner output, so list A/B/C fall out automatically.*
