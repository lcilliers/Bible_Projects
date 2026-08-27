---
name: project_registry_words_not_all_lexically_grounded
description: Finding (2026-06-08, corrected). The corpus keyword vocabulary is built from TERM GLOSSES, so an anchor word is a keyword only if a term's gloss uses that exact word. Testing each registry word against its OWN terms: of 215 rows, 164 GROUNDED-LEXICAL, 21 GROUNDED-COGNATE (has terms, relates by synonym — brokenness→shaber, consciousness→conscience, loyalty→chesed, vulnerability→nakedness), 30 EMPTY (no terms — ~26 distinct: awareness, intuition, identity, personality, emotion, cowardice, blamelessness…; mostly modern psychological abstractions). 4 EMPTY are duplicate rows whose twin is grounded (deadness/resentment/transformation/vulnerability). So ~86% of anchors ARE grounded; ~26 genuinely have no terms.
metadata:
  type: project
---

**Why some registry words aren't in the keyword list (researcher 2026-06-08; corrected after pushback).** The
keyword vocabulary is built from **term glosses/senses**, not the registry — an anchor is a keyword only if a
term's gloss literally uses that English word. My first cut wrongly checked anchors against the *cluster*
keyword vocabulary and mislabelled grounded words as "absent abstractions." **Corrected test**
(`scripts/_assess_registry_grounding.py`, report `research/investigations/wa-registry-grounding-v1-20260608.md`)
checks each registry word against its OWN terms (`word_registry.strongs_list`/`phase1_term_count`):

**215 rows → GROUNDED-LEXICAL 164 (76%) · GROUNDED-COGNATE 21 (10%) · EMPTY 30 (14%).**
- **GROUNDED-COGNATE (21):** has terms, but the anchor isn't the gloss token — relates by synonym:
  `brokenness→shaber (break)`, `consciousness→suneidesis (conscience)`, `loyalty→chesed`,
  `vulnerability→ervah (nakedness)`, `whoredom→taznut`, `sorcery→pharmakeia`, `yearning→machmad`,
  `will/might/meaning` (have terms — though those mappings look loose: will→thumos/wrath, meaning→dunamis/power
  — worth a later glance). The researcher's expectation (≥1 related term) **holds** for these.
- **EMPTY (~26 distinct, the real gap):** no terms at all — `assent, awareness, blamelessness, commitment,
  communion, conformity, cowardice, determination, emotion, hopelessness, identity, image of god, ingratitude,
  intuition, laziness, manipulation, personality, personhood, reliability, self-awareness, sensitivity,
  sexuality, spiritual powers, stupor, darkening, betrayal`. Kinds: modern psychological abstractions the
  lexicon has no word for (awareness/self-awareness/intuition/identity/personality/emotion/sensitivity),
  `-ness` nominalisations grounded elsewhere (blamelessness/hopelessness), concepts covered under another
  anchor (cowardice→`deilia` under Fear), compounds (image of god, spiritual powers).
- **Data hygiene:** 4 EMPTY are **duplicate rows whose twin is grounded** — `deadness, resentment,
  transformation, vulnerability` each have two `word_registry` rows (one populated, one empty); 215 rows for
  ~214 words.

**So ~86% of anchors are grounded (lexical or cognate); ~26 genuinely have no terms.** Bears on
[[feedback_ontology_typed_relationships]] (a few anchors are constructs with no lexical thing behind them) and
the scaffolding-not-reality principle. Note: keyword vocab is per-CLUSTER; registry↔cluster linkage is loose
(`mti_terms.owning_registry_fk` mostly NULL). Earlier whole-word/no-stemming choice also hides inflected
anchors (FORM-VARIANT). The 3 "filtered" words (will/might/meaning) are NOT just filter casualties — they have
terms (grounded-cognate), though a global filter does still drop them as modals/metalinguistic.
