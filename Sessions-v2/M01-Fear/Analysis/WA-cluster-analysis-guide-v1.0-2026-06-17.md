# WA — Cluster / Characteristic Lexical-Analysis Guide (general)

**File:** WA-cluster-analysis-guide-v1.0-2026-06-17.md
**Date:** 2026-06-17 · **Prefix:** WA · **Type:** Methodology / process guide (reusable; markdown)

**Purpose.** A self-standing, cluster-agnostic guide for analysing the inner-being characteristics of any meaning cluster from its verse lexical extract. It encodes the steps, stages, tier framework, and audit process developed on M01 (Fear) so any future session can proceed without re-deriving the method. **Nothing here is specific to fear.**

**Governing companion documents (the hub):**
- Tier framework — `WA-tier-catalogue-current-state-v1-20260617.md` (T0–T7, authoritative DB state).
- Self-audit discipline — `WA-char-self-audit-template-v1.0-2026-06-16.md`.
- T0.4 typology method — `WA-t04-typology-method-v1.0-2026-06-17.md`.

**Standing principle.** Analysis is grounded in the **verse lexical data only**; the lexicon **surfaces and grades**, it does not confirm canonical-theological readings (those route to T7.2). Inferential claims are labelled inferential. No content from outside the lexicon.

---

## 1. Input — the verse lexical extract

A per-cluster JSON (often batched, e.g. `*-b{n}of{m}.json`, plus a full file). Structure:
- `meta` — cluster code, description, counts, **a field data-dictionary**, and a **provenance** note distinguishing mechanically-derived fields from read-resolved fields (cause, location, divine_involvement, object_type, valence). Read the meta first.
- `data[]` — one record per verse (`reference`, `osis_id`, `testament`, `verse_text`) holding `term_occurrences[]`.
- Each occurrence: `term` (strong, translit, gloss, language, **cluster**, **focus_cluster**), `verse_report` (target_word, **morph**, **stem**), and `lexical` (the analysis block).
- **Fan-out layout:** each verse lists *every* inner-being term; `focus_cluster=true` marks the cluster under study; the rest are co-terms (lighter enrichment). **Work from focus terms; use co-terms for synergy.**

Conventions to honour: **absent = NONE** (genuine silence, never imputed); **UNRESOLVED = expected-but-undetermined** (rare). The lexical `mode` field is typically empty — grammar lives in `verse_report.morph`/`stem`.

---

## 2. The pipeline (phases)

```
Stage 0  Extract review / validation        → WA-[cluster]-lexical-extract-review
Step 1   Derive characteristics + senses    → WA-[cluster]-characteristics
         (+ scope decision per characteristic)
Step 2   Preliminary per-characteristic      → v1.0 (first round) → v1.1 (deep dive)
Step 3   Tier enrichment (T0–T7) + self-audit → v1.2 (tier) → v1.3 (final)
[later]  Cross-characteristic synthesis / open T6 / verse-literary (T7.2)
```

The staging exists to manage cognitive load and to produce a **validatable artifact at each stage**. Record each stage as its own version.

---

## 3. Stage 0 — Review and validate the extract

Before analysis: confirm structure and counts; read the meta data-dictionary; note which fields are read-resolved vs mechanical; check integrity (duplicate references, registered-form pairs, homonym/sense noise, membership outliers — terms pulled in on a minority sense); confirm batch ⊂ full. Record observations and any data-quality flags. Data/generator fixes are **CC's domain**, not Claude AI's.

---

## 4. Step 1 — Derive the characteristics (+ scope)

Group the cluster's terms into inner-being **characteristics**, each with its associated **senses** (ESV words) and **glosses/lemmas**. Discipline:
- Derive from the data (lemma_meaning + sense), not from a pre-formed taxonomy. The grouping is the interpretive act — mark it as such.
- Anchor each characteristic on its lemma(s); list the senses under it.
- Separate genuine outliers (minority-sense membership, external-result senses, homonym noise) from the characteristics.
- Note soft boundaries between adjacent characteristics (one term may span several).

**Scope decision (do this at the Step 1 → Step 2 boundary for each characteristic).** Decide whether a characteristic is defined by its **lemma anchor** or by the **data fields** (e.g. a valence/object signature). Run the **convergence test**: cross-tabulate lemma-membership against the field-signature; inspect the disagreement cells (lemma over-includes / under-includes). The divergence is the evidence. *The occurrence set governs Steps 2–3, so settle scope before writing the preliminary analysis.* If undecided, proceed on the lemma anchor and flag the consequence (e.g. N occurrences that would move under a field-based scope).

---

## 5. Step 2 — Preliminary per-characteristic analysis

**v1.0 — first round (orientation).** Occurrence set (terms, counts, testament/language); structural distributions (`type`, `faculty`, `valence` headline, `object_type`, `experiencer`, `location`, `stem`); a descriptive first reading; scope note.

**v1.1 — deep dive.** The verse-read interpretive fields and their **cross-tabs** (esp. `valence` × `object_type`); `divine_involvement` directions; resolved `cause`; the `compound` synergy nexuses; behavioural `immediate_response`; `intensity`; testament/language differences; per-term breakdown; an interpretive synthesis. Distinguish observation / interpretation / reflection.

---

## 6. Step 3 — Tier enrichment (T0–T7) + self-audit

**v1.2 — tier coverage.** Reorganise the findings through T0–T7 with a **coverage map** (which tiers the lexicon populates richly / sparsely / silently — the map is itself a finding). Use the field→tier map (§8). Note silences explicitly rather than filling them.

**v1.3 — final + self-audit.** Add the **field-completeness self-audit table** (every field: fill, tier home, status) and the final synthesis + reflection (including impact for different reading communities; application held lightly). Confirm cross-tabs / multi-value / boundary / integrity angles were taken.

---

## 7. The self-audit gate (non-negotiable)

Before presenting any per-characteristic analysis, prove that **every lexical field of every verse in the set has been examined** — each field yields a reported value **or a noted silence**. Build the completeness table *first*. "All angles" = each populated field read by distribution, cross-tabulation, direction, within-term vs across-term, by testament/language, in its multi-value cases, and at its boundary/contrast. The `compound` field and the `morph/stem` layer are always read; integrity anomalies are surfaced. This is Claude AI's own responsibility, run proactively — not deferred to review.

---

## 8. Field → Tier map (general)

| Lexical field | Primary tier home(s) |
|---|---|
| sense, lemma_meaning | T1.1 (Name), T7.1 (Lexical) |
| morph / stem (mode empty) | T1.4 (Modes), T7.1 |
| type (act/status/quality) | T1.2 (Kind) |
| valence | T0.2 (design vs fallen), T1.3 (Boundary), T1.7 (Conditions) |
| object / object_type | T4 (Relational interfaces) |
| divine_involvement (object/agent/giver/addressee) | T0.1 (God's role), T4.1 / T4.2 |
| cause | T4, T1.7 |
| location (spirit/soul/heart/mind/flesh) | T2 (.1/.2/.3/.4/.6) |
| origin | T2.9 |
| faculty (+ blends) | T3 (.1 Perception … .4 Affect … .6 Volition …) |
| compound | operational co-terms → T1/T3/T4; other-characteristic partners → **T6 (held)** |
| immediate_response | T1.5 (Immediate Response) |
| (sustained / produces) | T1.6 (Sustained Effect) |
| experiencer (self/other/addressed) | T1 stance, T4 |
| intensity (magnitude vs totality vs durative) | T1.2, T1.6 |
| how (governing predicate) | T1.4, T2 |
| relational | T4 |
| cross-testament / NT-divine-act / eschat cause / covenant co-term | **T0.4** candidates (inferential → T7.2) |
| VE `purpose` / `typology` fields | excluded by design (≠ the T0.2 / T0.4 *questions*) |

**Key relocations to remember:** `immediate_response` is **T1.5 (Definition)**, not the Formative tier; the Formative tier (**T5**) is the developmental *arc* (transformation, sequence, suffering, sanctification, eschatology) — usually near-silent in the lexicon. T0 (Divine Image) is assessed largely from `divine_involvement` (is the characteristic ever attributed to God as experiencer?) and `valence` (created design vs fallen response).

---

## 9. Special methods and policies

- **T0.4 (Typological Significance):** candidate-surfacing, not a field. Covenantal → compound co-terms; eschatological → cause/object + reference distribution; christological → NT + verse_text referencing the divine instance. Label inferential; route confirmation to T7.2; record graded silence where absent. (See the T0.4 method doc.)
- **T6 (Structural Relationships with Other Characteristics):** typically **held silent** until explicitly opened. While held, report the `compound` field's *operational* co-terms (routed to T1/T3/T4) but **park** co-terms that are themselves other characteristics. Do **not** name legacy cluster codes under the current terms of reference.
- **Silence handling:** distinguish a genuine **noted silence** (field empty → record it) from **excluded-by-design** (VE purpose/typology fields). Both are stated, never confused.

---

## 10. Grounding, integrity, and output discipline

- Ground every claim in a field value, a count, or a verbatim `verse_text`. Inferential ≠ confirmed (label it).
- Surface integrity issues (duplicates, registered-form pairs, homonym noise, membership outliers); do not silently absorb them. Generator/data fixes are CC's domain.
- **Outputs by purpose:** internal reusable analysis → markdown (.md); tabular/patch/itemised → JSON; visualisation/reader documents → docx, converted to PDF for finals. Convert docx→md when it improves working efficiency.
- **File naming:** `WA-[short description ≤30 chars]-v[major]_[minor or .]-[YYYY-MM-DD]`. Version maintained docs; minor for updates, major for a from-scratch redo or a re-base onto a changed framework. Each output references its filename, date, and a one-line pointer to the prior output.
- **Two-AI division:** Claude AI decides/analyses/authors; Claude Code executes all database/generator operations. Claude AI never writes the DB.

---

## 11. Stop / handoff

Produce a **session log** at natural breakpoints and at close — capturing the debate and reasoning, decisions, conclusions, open items, and next steps, plus a list of files produced. The session log is the handoff record; this guide is the standing method.

---

*End of v1.0. Generalise further as new clusters surface method gaps; bump version on change.*
