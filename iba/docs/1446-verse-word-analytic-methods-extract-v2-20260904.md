# Verse/word analytic methods — extract (v2)

**Filename:** 1446-verse-word-analytic-methods-extract-v2-20260904.md
**Escalation:** #1446 (spawned from #1443)
**Supersedes:** v1 (2026-09-04), archived — corrected per direct researcher instruction (this
chat, 2026-09-04): v1 silently excluded methods from five reference documents named explicitly.
This version folds in every verse/word analytic method mentioned in those five documents, plus
everything already in v1. Nothing is summarized past — where a document names a specific rule,
field, or fix, it is named here too, with its own status.

**The five reference documents, checked in full for this version:**
1. `Workflow/methodology/wa-reset-amendments-v1-20260625.md`
2. `outputs/escalation/1383-escalation-history-v2-20260904.md`
3. `Workflow/Catalogue/1383-verse-lexical-window1-validation-applied-v1-20260903.md`
4. `Workflow/methodology/wa-lexical-item-derivation-validation-v1-20260701.md`
5. `Workflow/methodology/wa-ve-lexical-dimension-catalogue-design-v1-20260701.md`

**Status labels used throughout:** LIVE (built, running today) · PROPOSED (designed, awaiting
approval, not built) · CANDIDATE (surfaced by validation, not yet decided or built) · HISTORICAL
(superseded, provenance only) · OPEN (an unresolved question at the time its source document was
written — status as recorded there, not re-adjudicated here).

**★ "T1–T3"/"T2"/"T3" disambiguation, added per direct researcher instruction (2026-09-04) —
escalation #1447 raised to fix this at the glossary level project-wide.** This label is reused for
**three unrelated schemes** in the project's documents; every occurrence below is now tagged with
which one it means:

- **[VRT]** — **Verse Reading Technique v4** (`iba/docs/WA-verse-reading-technique-v4-2026-08-05.md`),
  a 9-step (T1–T9) per-verse analytical technique. T1–T3 = the lexical-meaning half (work from the
  row not the gloss; pull the full lexical range before assigning a sense; let morph decide voice/
  person/aspect) — this is what §1 below actually is.
- **[TC]** — the **tier catalogue** (`Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md`),
  a characteristic-grain catalogue of observation questions, deprecated 2026-07-02. T1 = Definition,
  T2 = Constitutional Location and Boundaries, T3 = The Inner Faculties — this is §4 below, a
  different grain entirely (per-characteristic, not per-verse). **Range discrepancy, not yet
  resolved:** this extract describes the source catalogue as running T0–T9; the live glossary's own
  "Tier" entry (`bible_research.db.prose_section` id 1092, under the real glossary — see below)
  states the canonical range is **T0–T7** ("an earlier T1–T8 document is superseded"). Folded into
  #1447 for the researcher to settle, not adjudicated here.
- **[CC]** — live `cluster_code` rows literally named `T2`/`T3` in the `cluster` table (iba.db only —
  confirmed live bible_research.db's own `cluster` table has a T2 row but no T3 row): T2 =
  "Supplementary" (particles/objects/no-IB-relation strongs, also surfaces as a Scope-focus bucket
  label and in `verse_coverage`'s `n_T2`/`n_study_nonT2` counts), T3 = "Operations" (a strong
  considered a human operation/movement not tied to one IB cluster) — **but confirmed live, zero
  `mti_terms` rows actually carry `cluster_code='T3'`; the row exists in the lookup table as a
  defined tier, never as an actual term assignment.** Not otherwise referenced in this document,
  named here only so the tag set is complete.

**The real glossary, corrected understanding (researcher, 2026-09-04):** lives at
`prose_section_type` (the section-type row identifies it, e.g. id 109 `glossary_programme` /
book_label "Word Index and Glossary"), with content in `prose_section` rows carrying that
`section_type_id` — **not** `prose_section` id 64 (a different, older Session-B-pipeline vocabulary
section this extract's first correction round mistook for "the glossary"). The real glossary
**already has entries for T2 (id 1046), T3 (id 1069), and "Tier" (id 1092)** — [CC]/[TC] are
already reasonably covered; the genuine gaps are a missing T1 entry and no entry at all for [VRT]'s
own T1–T9 scheme. Full correction on record: escalation #1447.

A fourth, unresolved case is noted at its own occurrence below (§3.4) rather than silently forced
into one of the three.

---

## 0. ★ THE WINDOW 1 / WINDOW 2 SPLIT — the pivotal strategy finding from #1383

**Added 2026-09-04, corrected twice the same day** — first from "detect vs. interpret" to
subject/perspective, then to the sharper definitional rule below once the first correction's own
FK-link/rollup treatment turned out still wrong.

**Per direct researcher instruction:** #1383 fixed a strategy question this document must state
explicitly, not leave implicit — because every method in this document sits on one side of a line
that must never be crossed in either direction.

**★ Correction (researcher, same day): the split is by SUBJECT/PERSPECTIVE, not by DEPTH.** An
earlier version of this section described Window 1 as "detect only" and Window 2 as "interpret" —
**wrong**. Window 1 already does real judgement work on the verse itself (idiom recognition,
structural-pattern recognition and labelling, connective classification, related-word sorting —
§§2b/2c/2d below are genuine interpretive findings, not mechanical detection). The actual line:

- **Window 1 = the word/verse/passage analysed in its own terms.** Both the mechanical facts (Layer
  1, §2a) and the judgement-bearing findings (Layer 2, §2b) about what the verse's own language,
  grammar, and rhetoric are doing — idiom, structural pattern, chain, connective type, related
  words, and every candidate/deferred refinement in §§2c–2d. All of it stays Window 1 as long as the
  question being asked is about the verse/passage itself.
- **Window 2 = the SAME underlying verse/word/passage data, looked at through a different lens: the
  human inner being.** `operations-ingest` (HIB/`phenomenon`/`operation`) asks what these
  already-established facts mean **for or about the human inner being** — a different question put
  to the same material, not a deeper or more interpretive pass over it.
- **The bridge, sourced verbatim from #1379's own scope statement:** *"This is Window 1: understanding
  the words in a single verse, everything derivable from its own span/morph/lexicon data — full stop.
  It is NOT Window 2 (identifying HIBs, phenomena, operations — `operations-ingest`'s job, which also
  reads adjacent verses). The one and only bridge between them: where this checklist finds something
  it cannot resolve from the verse's own data, it records that explicitly as unresolved, never
  guesses, and never reaches into another verse to settle it itself."* Read correctly: this bounds
  Window 1 to the verse's *own* data (vs. reaching into other verses, or asking an inner-being
  question), not to "mechanical only."

**How this was actually decided (#1383's own record), re-read under the corrected framing:**
- **#1443 is still the concrete precedent, for the right reason.** The structural-pattern finding
  (merism/chiasm/antithetic-parallelism/paired-image) splits on subject, not depth: *recognising that
  a structural pattern exists, labelling its kind, and naming which spans it covers* is a fact about
  the verse's own rhetoric — Window 1 (`structural_pattern` note_type, §2b), and a genuine judgement
  call, not mechanical. *What that pattern means for the human inner being* is a question about the
  inner being specifically — Window 2, **parked**, not designed or decided in #1383 at all.
- **The HIB-candidacy correction (#1383 v11).** HIB candidacy is about named/implicit **parties**,
  answered by asking the HIB-specific question "is this party human." Window 1's
  `pronoun_resolution`/`entity_link` tests (§2b) already supply the grammatical fact (who/what a
  word points to) — that fact is reused by Window 2, which then asks its own HIB-specific question
  of it. Window 1 is not barred from producing HIB-*useful* facts (see `party_kind`, §2a — a
  mechanical, lexicon-derived fact about the verse that Window 2 will clearly draw on); what Window 1
  never does is ask the HIB question itself.
- **The `phenomenon`/`operation` FK link is Window 2 work, not a deferred Window 1 item — corrected
  a second time, researcher, same day.** A structural pointer from Window 2's free-text fields back
  to the specific Window-1 finding that warranted them was recommended (#1383 v11, v18), and this
  document previously described it as "deferred, not built this round," as though it were paused
  Window 1 scope. **It was never Window 1 scope to defer.** `phenomenon`/`operation` are themselves
  inner-being objects; a link from them into `verse_lexical`/`verse_lexical_note` is Window 2 reaching
  into Window 1's data — the link's design belongs entirely to Window 2's own build cycle, mentioned
  in §2d only because it references Window 1's tables.

**★ The definitional rule, stated plainly (researcher, 2026-09-04): `verse_lexical`/
`verse_lexical_note` can never carry an inner-being concept, by definition — and nothing in Window 1
ever determines whether something is a phenomenon.** #1383's own record has repeatedly mis-drawn this
line as a *mechanical* boundary (Layer 1 "mechanical" vs. Layer 2 "judgement," with anything not
cleanly on one side of that treated as ambiguous or "adjacent"). That framing is the actual error,
not a detail — Layer 1 and Layer 2 are **both** Window 1, whether mechanical or judgement-bearing;
the real boundary is definitional (does this table/field ever assert or decide something about the
inner being), and it does not bend for how the work is executed.

**Applying the corrected split to this document's own sections:** §§1–2 (the live T1–T3 baseline and
the full proposed Window 1 Stage 1 checklist, mechanical AND judgement-bearing alike) **are** Window
1, entirely — nothing in §2 is excluded from Window 1 for being interpretive, and §2d's two
non-reporting items are excluded not for being "deferred" but for genuinely belonging to Window 2.
§3 (VE-lexical, historical) is the same kind of work at an earlier stage of the same project line —
per-term lexical/rhetorical facts about the verse, some already close to what became `party_kind`-
style facts; not flagged as a discipline violation under the corrected framing. §4 (the tier
catalogue) is characteristic-grain, asking questions that are themselves about the inner being
(definition, faculties) rather than about a verse's own language — closer to Window 2's subject
matter, included for genealogy only. §5 (the 2026-06-25 cluster/movement apparatus) likewise asks
what per-verse signals mean for an assembled inner-being "movement" — Window 2's own historical
ancestor, not Window 1's — kept only because the researcher named that source document explicitly.
Each of those sections carries its own short pointer back to this section.

**★ Anticipated build characteristic, researcher, same day (not yet decided or designed):** the
verse-lexical full analysis — **both Layer 1 and Layer 2** — is anticipated to need an actual API
call (not pure deterministic Python) to execute. This cuts against the full build spec's own current
framing of Layer 1 as "mechanical, no judgement, run at scale" (§2a) — if even Layer 1 needs an API
trip, that changes cost, latency, and error-handling assumptions #1383 v22 doesn't yet address.
Recorded here as the researcher's own anticipation, not a decision — a real open item for #1383's own
build design, not resolved in this document.

---

## 1. LIVE today (`iba.db`, unchanged, in production) — `verse_lexical` T1–T3 **[VRT]**

**Source:** `1383-verse-lexical-window1-full-build-specification-v1-20260904.md` §B.4 (unchanged
from v1 of this extract), which implements Verse Reading Technique v4's **[VRT]** T1–T3 exactly (per
the #1383 design-propose doc: "its T1-T3 is already exactly `lexical.build`").

| Field | Method |
|---|---|
| `role` | classifies the code `content` vs `function` (grammar-only) |
| `resolved_sense` | stem/voice-selects the operative STEP sense for a `content` code |
| `status` | `resolved` or `unregistered` |
| `ambiguity_note` | flags same-base sibling ambiguity, never resolves it silently |

**Known live defect, being root-fixed (not yet applied):** `role` misclassifies `H0853` (the
Hebrew direct-object marker) as `content` — confirmed live at least 6 times across the #1383
validation run (Deut 6:5, Exod 14:31 ×2, Exod 15:1) on top of the original Hos 2:4 find. Fix
designed in #1383 §4 (an explicit exception set on `classify_role`, starting with `H0853`, plus a
one-time UPDATE on the ~10,521 pre-existing affected rows) — not yet built.

**Caveat raised then resolved:** #1383 v11 flagged that `resolved_sense` hit STEP's `stepGloss`
fallback on every single code across the 19-verse validation run — possibly a live gap in T1-3
**[VRT]** baseline quality. **Resolved in v18**: a false alarm caused by Claude's own em-dash display
truncation, not the field's real content — checked at full scale (551,797 live rows), 99.999%
carry a genuine per-stem narrowed sense (proven on H1288 bless/kneel, narrowing correctly by stem).

---

## 2. PROPOSED, not yet built (`iba.db`, escalation #1383, in propose stage — v22, not approved)

**§0 applies directly here: this whole section is Window 1, end to end** — mechanical facts (§2a)
and genuine judgement-bearing findings about the verse's own language and rhetoric (§§2b–2d) alike.
Nothing below asks or answers what a finding means for the human inner being — that HIB-specific
question is Window 2's separate, later job, applied to the same underlying data.

**Sources:** `1379-verse-lexical-enrichment-checklist-v1-20260902.md`,
`1383-verse-lexical-window1-full-build-specification-v1-20260904.md`, and the full #1383 escalation
history (v1–v21) for the refinements and candidates below.

### 2a. Layer 1 — mechanical, no judgement (new columns on `verse_lexical`)

| Field | Method |
|---|---|
| `position` / `surface` | straight copy from `span.position` / `span.surface` |
| `language` | straight copy from `strong.language` |
| `testament` | derived from `cfg_book_order.ordinal` (≤38 → OT, else NT) |
| `is_negator` | looked up in `cfg_lexical_code_class` (class=`negator`) |
| `narrative_morph` | Hebrew-only; regex-matches `morph_code` for wayyiqtol **and** `az`+imperfect narrative-opening markers (the second pattern added specifically because the validation run's Exod 15:1 pivot verse uses `az`+imperfect, not wayyiqtol, for its primary narrative verb — see 2c) |
| `gloss_consistent_in_verse` | data-quality check — does the same (strong, morph_code) pair carry >1 distinct `resolved_sense` in this verse |
| `party_kind` | looked up in `cfg_lexical_code_class` (party_divine/human/angelic → divine/human/non_human) |

**Lexicon build status behind `is_negator`/`party_kind` (per #1383 v21):** negator, connective
(see 2b), and divine-name lexicons are seeded and verified live; **human-name and angelic-name
lexicons are NOT built yet** — `T4.3.1`/`T4.4.1`/`T4.6.1` stay unanswerable until they are.

### 2b. Layer 2 — judgement, one `verse_lexical_note` row per (code, test)

11 `note_type` values, each a distinct analytic test:

| note_type | What it tests |
|---|---|
| `idiom` | is this span part of a multi-code compound whose combined gloss diverges from a literal code-by-code reading |
| `pronoun_resolution` | same-verse antecedent resolution for a pronoun (person/number/gender agreement) — `unresolved` if not resolvable from this verse alone |
| `noun_relational` | does a noun name another party engaged in the verse's action (target/source/addressee) |
| `noun_severity` | does a noun sharpen the weight of an object/action without naming a party |
| `chain` | narrative-sequencing marker (Hebrew wayyiqtol/`az`+imperfect) linking this operation to another as "and then" — no Greek equivalent built yet |
| `connective` | logical/causal connective linking two clauses by reason, not narrated order — classified against `cfg_lexical_code_class`'s **three** connective classes: `connective_causal`, `connective_coordinating`, `connective_purpose` (the coordinating/purpose classes were surfaced by the Gal 5:17 calibration pass, #1383 v9, alongside a correction to the causal call itself — G1063 "for" was first wrongly marked inert, then correctly reclassified causal) |
| `related_word` | mechanical pull of `strong_related` links for content-role codes — recorded raw, sorting left as a judgement field |
| `polarity` | is this row a negation/modifier attached to a declared operation |
| `entity_link` | ties an operative verb/noun back to its named subject (possessive suffix, proper name, person/number match) |
| `inert` | positive confirmation that a function-word row contributes nothing beyond grammar |
| `structural_pattern` | detects a verse-level rhetorical relationship (merism/chiasm/antithetic-parallelism/paired-image) spanning multiple codes — **detection only**; interpreting what it means is Stage 2's job (#1443's own resolution) |

**`genre` — its own explicit method, not a note_type.** Set manually as this integrated read's own
first move, before any Layer 2 note is written (`one-integrated-read-genre-first`) — free text this
round, no controlled vocabulary yet. Written to `passage.genre`.

**Demonstrated capability, live-tested (not yet built into schema):** `pronoun_resolution` and
`entity_link` are *specified* as same-verse-only, but the #1383 validation run demonstrated they
resolve correctly at **passage-block** scope in practice — 6 confirming instances across 3 passages
and both languages (Deut 6:8–9 ×2, Prov 3:6, John 1:2, Gal 5:17), the single strongest, most
repeated result of that run. This validates the "one integrated read per passage" model directly,
not just as a design argument.

**Data-quality check promoted into Layer 1:** "same code, different gloss" (`gloss_consistent_in_verse`,
§2a) started as a manual note-layer item, then was promoted to a mechanical column once proven — it
never needed to be a judgement call.

### 2c. Candidate refinements — surfaced by the validation run, NOT yet decided or built

| Candidate | Source finding |
|---|---|
| `az`+imperfect as an explicit second chain-test signal | Exod 15:1's primary narrative verb ("sang") is Qal imperfect + `az`, not wayyiqtol — the chain test still fires, but on the verse's *other* verb ("saying," which does carry wayyiqtol), not the one a reader would point to first. Already folded into `narrative_morph`'s field description (§2a) but the checklist's own `chain` rule has not been formally rewritten to name it |
| Same-code-recurrence-with-shifting-rhetorical-role | `G3056` (John 1:1, "Word") and `G2222` (John 1:4, "life") recur identically in code/morph but shift grammatical role (subject → object → predicate) across occurrences in one verse — no checklist slot exists for this as its own observable pattern |
| Different-lemma-same-English-gloss | `G1937` (Gal 5:17) vs `G1939` (Gal 5:16) — two genuinely distinct Greek roots both glossed "desire" — the inverse of the existing same-code/different-gloss data-quality check; not covered by any current item |
| Language-aware "related word" note | Hebrew related-word families skew toward root-sharing (triliteral roots); Greek families skew toward compound-morphology relationships (e.g. God-hating/God-fighting/God-breathed compounds on `G2316`) — a genuine difference in what "related" means by language, not yet written into the checklist as a rule |
| Boundary judgement calls remain genuinely open in places | Prov 3:5–6 vs extending to 3:7 — a real, honestly-recorded ambiguity (thematically continuous, but the couplet's own result clause closes cleanly at v6) — left as-is, not resolved mechanically |

### 2d. NOT Window 1 — items #1383 discusses that don't belong to this method at all

**★ Corrected, researcher, 2026-09-04: #1383 has consistently mis-drawn this line as a mechanical
boundary** (Layer 1 "mechanical" vs. Layer 2 "judgement," with these two items sitting somewhere
"adjacent" to that boundary). That framing is wrong. The real rule is definitional, not about depth
or mechanism: **`verse_lexical`/`verse_lexical_note` — Window 1's own tables — can never carry an
inner-being concept, and nothing in Window 1 determines whether something is a phenomenon.** Under
that rule, two of the three items below are not "deferred Window 1 work" at all — they are Window 2
work, full stop, mentioned only because they reference Window 1's data:

- **Aggregation/rollup layer — Window 2, not Window 1.** A cross-verse rollup that would use Window
  1's per-verse raw material (related-words, testament/language columns, morph capture) to answer
  characteristic-level catalogue questions (#1383 v12/v13: ~20 of 181 catalogue questions land here)
  is answering a question about the inner being/characteristic, not about a verse's own language —
  it belongs with Window 2's own apparatus, not scoped as part of this method.
- **FK link, `phenomenon`/`operation` → `verse_lexical`/`verse_lexical_note` — Window 2 work, not a
  deferred Window 1 item.** `phenomenon` and `operation` are themselves inner-being objects; a link
  from them back to a Window 1 finding is Window 2 reaching into Window 1's data, which is fine —
  but the link's design, and any decision about it, belongs entirely to Window 2's own build cycle.
  It was previously described here as "deferred, not built this round" as if it were paused Window 1
  scope (#1383 v11, v18) — corrected: it was never Window 1 scope to defer.

**The "Layer 3 reporting" item removed from this list — a category error, not a mechanism.** A prior
round of this document described a per-run exception report (implemented as
`report.lexical_exceptions`) as "Layer 3," alongside Layer 1 and Layer 2 as if it were a third
data-derivation layer. It is not: it is a **report** that reads Layer 1's and Layer 2's own
already-written rows and tallies them — no new field, no new derivation, nothing decided that Layer
1/2 didn't already decide. Its one real content point stays worth keeping, without the confusing
"layer" framing: the report must never be framed as "confirms"/"validates"/"closes the gap" — the
bias the researcher corrected out of the first-pass validation summary (#1383 v9/v10) — just a plain
tally against Layer 1's own complete count.

---

## 3. HISTORICAL — VE-lexical per-term dimensions (`bible_research.db`, catalogue v1, 2026-07-02)

**§0 applies here:** this predecessor model is the same kind of work as §2 — per-term facts about
the verse's own language, some already close to what became `party_kind`-style facts (D5 target's
object-type classification, D3 seat/bearer) — Window 1 territory throughout, at an earlier stage of
the same project line, not a discipline violation under the corrected split.

**Sources:** `Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md` (the authoritative item
list, already used in v1 of this extract) plus its own design/validation predecessors,
`wa-ve-lexical-dimension-catalogue-design-v1-20260701.md` and
`wa-lexical-item-derivation-validation-v1-20260701.md` (both 2026-07-01, one day earlier — the
working documents the catalogue itself was written from).

### 3.1 The model

Each dimension value is a **PAIR** (`element1 → element2`, an ordered edge with a resolution state),
an **EVENT** (a predicate/chain, not a two-node edge), or a **FLAG**.

**Direction convention (confirmed): semantic flow**, not a uniform counterpart→term rule — the
arrow follows meaning: **into** the term for source/seat/operation/process (`cause → term`), **out
of** the term for target/effect (`term → object`).

**Resolution states, every pair value:** `span` (element1 is an actual span in the verse) ·
`inferred` (deduced, not present in the verse) · `unknown` (a value is expected but undeterminable —
the open worklist) · `none/silent` (the verse genuinely has none — never impute).

### 3.2 Per-term items

| dim | item | shape | definition | reliability at time of writing |
|---|---|---|---|---|
| D1 | sense | value | per-occurrence STEP subgloss | ✅ reliable |
| D1 | type | value | action/status/quality (from POS) | ✅ reliable |
| D2 | source | PAIR | driver/antecedent → term | ⚠ must distinguish DRIVER vs RESTRAINT |
| D3 | seat | PAIR | constitutional seat (heart/soul/spirit…) → term, via construct chain | ✅ reliable (construct-gated) |
| D3 | bearer | PAIR | who bears it (experiencer/subject) → term | ❌ not yet derived (gap) |
| D4 | operation | EVENT | the governing predicate | ✅ reliable |
| D5 | target | PAIR | term → object (+ object-type: person/God/group/thing/abstract/spiritual-being) | ⚠ partial |
| D6 | manner | PAIR | qualifier span → term (+ intensity: me'od/kol) | ✅ reliable |
| D7 | process | EVENT | the escalation chain of the passage's affect/vice operations (prose narrative only) | passage-level |
| D8 | effect | PAIR | term → produced-state (Piel/Hiphil result verb, adjacent, prose only) | ✅ narrative / ⚠ poetry |
| D9 | coupling | PAIR | the morphological weld only (construct/preposition binding) — NOT every co-occurrence | ✅ reliable (no explosion) |
| D10 | prohibition | FLAG | mechanical negation/prohibition particle (moral framing) | ⚠ proximity-based |
| D11 | discovery | FLAG (verse) | the uncertainty/discovery-notes channel — also the span-completeness lookout (flags spans not yet tagged to any term) | ✅ reliable + valuable |
| D14 | passage | verse-level | consecutive-run membership; anchor = first verse | (see §3.4) |

**Dropped by researcher decision:** D10 valence (99.3% AI-interpreted, all soft-deleted — only the
mechanical prohibition signal, above, was kept); D12 hidden meaning (not lexical-level); D13
cohabitation (implicit in the multi-term-in-verse principle); `related_tier` (T0–T7, superseded by
this whole catalogue).

### 3.3 The underlying technique: argument-structure parse

D2/D3/D5/D6/D9 all depend on one shared parsing mechanism, not five independent ones: identifying
**which word governs which** — the governing verb, the construct/suffix owner, the preposition
complement. Confirmed **not yet reliably in the data** at the time of the 2026-07-01 validation
(the reason D9's "kernel" recommendation — keep only the morphological weld — could be stated but
not yet fully implemented).

### 3.4 Derivation rules, per dimension, and their round-by-round fix history

(Source: `wa-lexical-item-derivation-validation-v1-20260701.md`, rounds 1–3; harness scripts
`_probe_lexical_derivation_harness_v1/v2_20260701.py`.)

| dim | Round 1 finding (broken) | Round 2/3 fix | Status at time of writing |
|---|---|---|---|
| D2 source | `cause`/`cause_clause` = a bag of every verse word, identical on every term; `from-source` fired in the wrong direction | fires only on a causal particle (`ki`) | OPEN — over-fires: doesn't yet distinguish causal `ki` from complementiser `ki` (the latter marks the object of perception, not a cause) |
| D3 seat | smeared onto ALL terms in a verse (Gen 6:5: "heart" attached even to "every"/"saw"/"man") | attaches only via construct chain | ✅ fixed |
| D5 target | mixed/wrong; `object-type` defaulted to "impersonal" | object = the noun governed to the right of the verb | OPEN (round 3) — still grabs a preposition-marked manner-noun instead of the real `et`-marked/suffixed object in some cases |
| D6 manner | not captured — fell into the `operation`/`how` field instead | a preposition-marked noun (be-/ke-) is adverbial manner on the governing verb | ✅ fixed |
| D9 coupling | exploded — every co-term in the verse listed with an arbitrary role | only the morphological weld (construct/preposition binding); loose co-occurrence → NONE | ✅ fixed |
| D7 process | not captured (round 1); round 3 demo (Exod 1:11–14) recovers the escalation chain correctly | must filter to IB-relevant operations only — drop response-verbs ("built"/"multiplied"/"spread"), keep afflict/oppress/dread/enslave/embitter | OPEN (round 3) — filter rule stated, not yet applied generally |
| D8 effect | not captured (round 1); round 3 demo picks the operation verb, not the produced state | must skip the operation verb and take the produced-state (e.g. "embittered," not "made") | OPEN (round 3) — fix identified, not yet applied |
| D4 operation | conflates the term's own action with an action done *to* it (Psa 34:4: `how=delivered` for *fear*, but God removes the fear — that's not the fear's own operation) | separate "the term's own verb" from "a verb acting on the term" | OPEN — unresolved as of round 3 |
| "T2 qualifiers" *(label as-is in source — unresolved, see note)* | derived as standalone items (every/saw/man/only) | should **inform** other terms' derivation, not be analysed standalone | OPEN — noted, not yet implemented |

**Note on "T2 qualifiers":** `wa-lexical-item-derivation-validation-v1-20260701.md` uses this exact
label without defining it, and it fits **none** of the three schemes disambiguated at the top of
this document ([VRT]'s T2 is "pull the full lexical range"; [TC]'s T2 is "Constitutional Location";
[CC]'s T2 is "Supplementary") — a **fourth, unresolved** use of the label, quoted as-is rather than
guessed into one of the three. Folded into escalation #1447 for the researcher to identify or
retire.

**Passage-awareness is mandatory, not optional (Round 3 finding):** `source`, `effect`, and
`process` **do not exist** at single-verse scope — isolated per-verse evaluation is systematically
impoverished for these three dimensions specifically (demonstrated on Exod 1:13 read isolated vs.
as its passage, Exod 1:11–14).

### 3.5 Passage determination — five rounds to a definitive rule

1. **Rounds 1–2** — no explicit passage mechanism; derivation run per-verse.
2. **Round 3** — passage-aware derivation demanded; discovered the existing `isolable` marker
   under-detects (missed Exod 1:13–14 despite clear textual continuation).
3. **Round 4 — two startup validators built:** **Validator A** (passage membership, forward+backward
   walk from the start verse; links classified `confirmed` vs `candidate`, candidates flagged for
   review, never silently trusted) and **Validator B** (every passage verse must have
   `verse_morphology`; a missing verse is a BLOCKER). Anchor = first verse; read all passage
   morphology together before deriving.
4. **Round 5 — process-marker + batch resilience:** `verse.process_marker` and
   `verse.is_passage_anchor` fields; per-verse batch loop runs Validator A then B, writes a marker
   on failure and moves on (`ANCHOR:<ref>` / `MEMBER:<anchor>` / `A-REVIEW:<n>v-candidate-boundary` /
   `B-BLOCKED:<refs>`). **Finding: the boundary SIGNAL itself was the real problem** — a dry-run on
   Exodus 1 sent 14 of 16 verses to `A-REVIEW`, because the "continuation opener" heuristic
   (and/so/but/therefore) fires on almost every verse in Hebrew narrative, where *waw* is simply the
   default connector, not a boundary signal. Live-write held as not useful state.
5. **Round 6 — DEFINITIVE, supersedes rounds 3–5's boundary machinery.** Researcher ruling: a
   passage is purely mechanical — sort verses by book/chapter/verse_num; **any maximal run of
   consecutive verse numbers (length ≥2) is a passage**; runs break at chapter boundaries; no
   `isolable`, no opener heuristics, no paragraph markers, no semantic detection, no reading to
   establish boundaries. Rebuilt live: 3,650 passages, 22,209 verses linked. This is what
   `verse.passage_id`/`is_passage_anchor` hold today, and is the direct ancestor of the current
   "passage = a maximal run of consecutive verses" definition (§3.6 below) and of #1383's own
   `passage` table. Validator A collapses to a plain lookup once this rule is adopted; Validator B
   (spans-present) and the process-marker/anchor design stay unchanged.

### 3.6 The processing algorithm (researcher-stated verbatim, 2026-07-01)

1. **Select verse.** Is it part of a passage? If yes, handle as a passage — take the passage's
   **first verse**. If the selected verse *is* the first verse, proceed; else **skip** (cross-
   referencing the selected verse to its passage).
2. **Analyse verse morphology** — isolate all spans that require lexical treatment (the
   span-completeness pre-pass — the same mechanism D11 discovery flags for).
3. **Perform the full lexical analysis** on that term-list.

### 3.7 Storage design

- `ve_lexical` (`verse_context_id · ve_nr · ve_label · value · notes · source_provenance`) plus the
  pair columns `from_span · to_span · direction · resolution · pair_kind`.
- **Structure pivot, confirmed needed** (predicted by the researcher, then confirmed against live
  data): `ve_lexical` was keyed only to `verse_context` (per-term), but verse-level facts
  (`isolable`, `discovery`) were being **duplicated per term-context** — `isolable` on 2,775 verses,
  1,445 with >1 copy; `discovery` on 19,128 verses, 10,862 with >1 copy. Fix: a genuine verse-level
  tier alongside the per-term rows (a `scope` column, or a separate table) — this is exactly the
  per-term/verse-level split the current `ve_lexical` catalogue (§3.2 above) reflects.
- Verse-level tier (per-term/verse split) sits above passage (passage-level, on the first verse
  only) — three genuine grains, not two.

### 3.8 Known caveats on this whole layer

- **Term-grounding noise**: the `mti`/`owning_word` term label a lexical item's cluster comes from
  is often the wrong sense — a homonym artifact, not a real classification (Gen 6:5: "every"→*evil*,
  "man"→*kindness*, "saw"→*experience*; Exo 1:13: `abad` "enslave" tagged under "worship"/M36). Any
  item reading the term's cluster/label inherits this noise; the per-verse *sense* value is
  unaffected.
- **Backtrack test, proposed but not confirmed run**: pick 2–3 verses sharing a feature and confirm
  the completed item-set reconstructs the shared meaning between them — proposed as the validation
  gate for "does this item-set actually support cross-verse synthesis," status at time of writing:
  awaiting researcher confirmation to run.

### 3.9 Legacy flat-field model this catalogue itself superseded

**Source:** `wa-ve-lexical-dimension-catalogue-design-v1-20260701.md` §3 (the "converges legacy"
mapping) — an even earlier layer, the flat single-value `ve_lexical` model (the "01b-VE-field-
reliability-and-rules" scheme the 2026-07-02 catalogue's own header names as superseded). Each old
numbered item folded into one of the D-dimensions above:

| legacy item (number) | folded into |
|---|---|
| `sense`(1) | D1 sense |
| `type`(2) | D1 type |
| `compound`(3), qualifier-role | D6 manner (qualifier half) / D9 coupling (weld half) |
| `location`(5) | D3 seat |
| `immediate-response`(11) | D8 effect |
| `intensity`(19) | D6 manner |
| `experiencer`(20) | D3 bearer |
| `valence`(21) | D10 (dropped — see §3.2) |
| `cause`(17), `cause_clause`(22), `from-source`(23) | D2 source (three legacy items converged into one) |
| `how`(18), `operation`(27) | D4 operation (two legacy items converged into one) |
| `object`/`object-type`(16) | D5 target |
| `isolable`(28), `read_with` | D14 passage |
| `discovery`(29) | D11 discovery |

Each convergence was required to **reproduce the old item's result** before being trusted (a
convergence-validation gate) — per-pair, not a blanket rule, since (researcher, verbatim) "each
pairs convergence rules must be set individually, the same rule does not apply for every pair."

---

## 4. HISTORICAL — tier catalogue T1–T3 **[TC]** (`bible_research.db`, pre-2026-07-02, DEPRECATED)

**§0 applies here as a boundary marker:** this was never Window 1. Its questions are themselves about
the inner being (definition, faculties, constitutional location) rather than about a verse's own
language — Window 2/Stage 2 subject matter (or beyond), included here only for the genealogy, not as
a method to be read alongside §§1–2.

**Source:** `Workflow/Tiers/wa-tier-catalogue-restructured-v2-20260611.md`. Superseded by §3 above
(its own deprecation note). Characteristic-level catalogue questions answered from verse evidence,
not per-code mechanical tests — included because §3's own source document names it directly as what
it replaced.

- **T1 — Definition:** name/naming, kind, boundary, modes of operation, immediate response,
  sustained effect, conditions of reception.
- **T2 — Constitutional Location and Boundaries:** spirit-level location, body-direction,
  origin/source, constitutional movement.
- **T3 — The Inner Faculties:** perception, cognition, memory, affect, creativity, volition,
  agency, moral evaluation, conscience, conscientiousness, relational capacity.

(T0 and T4–T9 exist in the same catalogue but operate at the characteristic/theological-synthesis
grain, out of scope for this extract — omitted as out of scope, not overlooked. One live discipline
carried forward from this layer, per the reset amendments below: T0–T7 areas are meant as a
**completeness checklist** for describing a movement, never a classification grid.)

---

## 5. HISTORICAL — cluster/movement-level apparatus built on per-verse lexical data (2026-06-25)

**§0 applies here as the clearest case of all:** this section asks what per-verse signals mean for an
assembled inner-being "movement" — Window 2's own subject matter, not a verse's own language. It is
**not** Window 1, and not a precedent for anything in §§1–2; kept only because the researcher named
this source document explicitly.

**Source:** `Workflow/methodology/wa-reset-amendments-v1-20260625.md` — the "Characteristics →
Movements" reset amendment pack (v1.1). This sits **chronologically between** the tier catalogue
(§4) and the VE-lexical catalogue (§3) — one week before VE-lexical's own D1–D14 model — and is
itself part of the reset that CLAUDE.md's 2026-06-25 banner records as later closed/reopened. Not a
per-word test like §§1–3; it operates on **per-verse relation signals** to assemble cluster-level
"movements," so it is included here per the instruction not to omit anything the reference documents
name. Where this document names fields from its own predecessor (`wa-lexical-analysis-rules-reset-v1
§3`, not one of the five documents supplied), those field names are quoted as cited, not verified
independently against that source.

### 5.1 Governing principle — P0, measurement informs, never decides

Quantitative facts (occurrence count, co-occurrence, distribution, association strength) are
descriptive only. They never gate **existence** (a once-attested phenomenon exists), **inclusion**,
**exclusion**, or **validity** (real dynamic vs. linguistic/genre artifact — always a qualitative
read).

### 5.2 The singleton rule

- A movement of one is a movement — cardinality is recorded *about* a movement, never the criterion
  *for* being one.
- Clustering groups verses by shared functional shape and emits **every distinct shape**, cardinality
  1..n; no group discarded for low cardinality.
- **Validity, read qualitatively, is the only screen** against spurious (artifact) movements — never
  rarity: a rare shape that reads as real is kept; a frequent shape that reads as artifact is
  discarded despite its count.

### 5.3 Cluster formation & status

- A cluster (of the ~3,500 STEP terms, loosely coupled by gloss into 47 clusters) is an
  **operational partition, not an ontological claim** — a workspace for batching analysis, nothing
  about the inner being asserted by where a verse is filed.
- **Term mobility** — a term can be moved to a better-fitting cluster; the initial gloss-coupling is
  correctable.
- **Focus-time boundary-collapse** — verses are analysed when their cluster comes into focus; at
  that moment the lexical analysis binds the verse to *other* clusters too, dissolving the
  partition for that specific verse. The partition holds for batching only; it dissolves at the
  point of analysis.
- **Boundary-permeability** — driven by the "binding-web" field (co-occurring inner-being terms +
  their relation, per verse); co-terms routinely belong to other clusters, so a verse's home cluster
  is one fact about it, its cross-cluster edges are equally real facts.

### 5.4 Related-verse relation signals

A verse is related to a movement under focus by a **relation signal**, not by frequency. Six
signals, each read off an "L1 edge-record" already produced per verse:

| Relation signal | Source field (as cited) | What it relates |
|---|---|---|
| shared shape | (operation, object-kind, effect, transition, valence) configuration | verses enacting the same movement, any cluster |
| binding-web tie | relational web / binding field | verses whose head term co-occurs with/binds to the focus term |
| shared object-kind | object/target field | verses directed at the same kind of object (e.g. toward-God) |
| pole-opposition | transition/becomes; binding pole-opposite role | verses naming the movement's opposite/boundary |
| shared seat addressed | faculty/seat addressed field | verses addressing the same seat when the movement runs |
| cognate/root tie | bedrock lemma + family | act↔state↔identity of one root across clusters |

(Compare §3.2's D2/D3/D5/D8/D9/D10 — the same conceptual territory, named slightly differently a
week before the VE-lexical catalogue settled its own field names. `transition` here does not appear
under that name in §3's D1–D14 list; it is quoted as cited by this document, not independently
verified.)

### 5.5 The B+D pointer mechanism

A **pointer** is a deferred observation recorded against a verse/cluster, re-surfacing when that
verse/cluster next comes into focus — raising something now, resolving it later, without holding
the whole relational web in one pass. Records: the observation + the D1 relation signal that
occasioned it + its origin. **B-pointers** (cluster scope, Session B) vs. **D-pointers**
(cross-cluster scope, Session D). The **discovery-lookout** (§3.2's D11) is the raiser; the pointer
is the carrier; focus is the trigger.

### 5.6 Assembly models — an open researcher decision at the time of writing

How a movement is assembled once related verses are in focus:
- **(i) Recognise-then-attach** *(recommended default)* — recognise the movement from verses rich
  enough to show its shape; attach sparser single-edge verses to the named movement by their D1
  signal; nothing force-merged.
- **(ii) Fragment-stitch** — reconstruct a movement never wholly present in any one verse, combining
  fragments across verses; only permitted with an explicit, non-lemma join key (else the term
  silently re-becomes the unit).

### 5.7 Measurement instruments — revealing, never deciding

| Instrument | What it reveals | Non-deciding constraint |
|---|---|---|
| Co-occurrence heat-map (term×term, term×cluster, shape×cluster) | graded association density | a cold cell never excludes; a hot cell never auto-includes |
| Association/affinity matrix (movement×movement) | how movements bind/trigger/oppose | strength shown, never thresholded into membership |
| Distribution histogram (term/shape/movement × book/genre/cluster) | spread & concentration | a tall bar is emphasis; a single bar is a singleton, kept |
| Edge/network view (nodes=terms/movements, weighted edges=co-occurrence) | emergent areas without hard lines | dense regions observed, never drawn as boundaries |

No instrument output is ever stored as a finding or membership — only a candidate related-verse set,
a candidate movement-association, or a spread description recorded *on* a movement.

### 5.8 Standing evaluation rules

- **Tiered clustering key** — cluster primarily on dense fields (operation, object-kind); sparse
  fields (effect, transition) only subdivide/enrich a candidate where present; never cluster on
  shared absence (two NONEs is not a similarity).
- **Validity gate** — a named step distinct from the emergence test; screens found artifacts;
  neither test ever uses count.
- **Areas-checklist, not a grid** — the T0–T7 areas (§4) are a completeness checklist for describing
  a movement, not classification bins; if every emergent movement maps cleanly onto an old tier,
  that is itself a signal the checklist is steering, and the emergence test should be re-run.

---

## Summary — the full genealogy, six layers

| Layer | Grain | Window (§0) | Status | Location |
|---|---|---|---|---|
| `verse_lexical` T1–T3 **[VRT]** | per-code | **Window 1** — the verse's own language | **LIVE** (one known bug, fix designed not built) | iba.db |
| Window 1 Stage 1 (Layer 1 + Layer 2, 11 note_types, + candidates/deferred items) | per-code, per-span | **Window 1** — mechanical facts AND judgement-bearing findings about the verse itself | **PROPOSED** (#1383, awaiting approval) | iba.db |
| VE-lexical D1–D11/D14 (+ legacy flat-field predecessor) | per-term / per-verse | **Window 1** — same subject, earlier stage of the same line | historical, superseded | bible_research.db |
| Tier catalogue T1–T3 **[TC]** | per-characteristic (different grain) | **Window 2 subject matter** — the questions are themselves about the inner being | historical, deprecated | bible_research.db |
| Cluster/movement apparatus (reset amendments) | per-cluster, built on per-verse relation signals | **Window 2's historical ancestor** — asks what verse signals mean for an inner-being movement | historical (2026-06-25 reset, later closed/reopened) | bible_research.db |

**The one line that matters most (§0, corrected):** the split is by subject/perspective, not by
depth — the first three rows analyse the verse/word/passage in its own terms (mechanical AND
judgement-bearing alike); the last two ask what that same material means for the human inner being.
Window 1 is not "the shallow half" of the work — it carries real interpretive judgement of its own,
just never the HIB question itself.

No new decision is made in this document beyond what its five source documents already state, each
with the status recorded there at the time. Open items (D2/D5/D7/D8/D4 derivation fixes, the
assembly-model choice, the human/angelic-name lexicons, the FK link, the aggregation/rollup layer)
are named as open, not resolved here.
