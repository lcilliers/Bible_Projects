# #2463 What the thought evidence report lacks as the foundation for layer 2 (v1, 2026-11-14)

Status: findings for the researcher to correct; read-only; nothing built or changed. Prompted by the researcher (#2463, 2026-11-14, verbatim): "i think the md and the excel is missing or not sufficiently showing the foundation work for layer 2, which causes us to stumble. layer 2 base data is in the verse-lexical, and the observations around faces is sort of moving in the right direction, and you analysis §3 in the md also flirts around it, but there is nothing that truely teases out the significance of surfaces living together in the verses, it seems there is mostly a lack of clarity and quite a bit of cherry picking taking place."

Read first (B:123): `cfg_table.use` for `verse_lexical` ("L4b, derived, version-aware: the mechanical reading, role classification and sense per code; read by report.verse_lexical and downstream, never by re-deriving from span/strong"), and `cfg_column.use` for its columns: `position` (span.position, mechanical), `surface` (the English of this code; with `surface_kind`, `unit_surface`, `unit_size`, `unit_role` for multi-term units), `morph_code`, `role` (since 2026-09-16 a JSON array of the cluster codes of the strong, history), `is_negator` (1 if the code is in the T5 lexicon, else NULL), `party_kind` (divine, human or non_human, only where the code is itself a name in the T4, T7, T8 or T9 lexicons), `gloss_consistent_in_verse`, `status`. 544,667 live rows. Counts below are my own read-only queries on 2026-11-14 (method in section 6); readings are inferential (B:4).

## 1. What layer 2 step 1 asks, and where each answer would come from

| Layer 2 question (researcher, v16) | Base data it needs | Held in `verse_lexical`? |
|---|---|---|
| Which words pair with which group | the other surfaces of the same verse, each with its own group or collection | the other rows of the verse are there (surface, strong, morph, position); the group or collection of each is a lookup on its surface |
| Which other words stand out | the words of the verse that carry an inner-being role or are entities, negators or qualifiers, against the rest | `party_kind` (entity), `is_negator`, `unit_role`; the inner-being role of a neighbour is its own collection membership |
| What does a word do with or for the group | the order and distance of the words in the verse, and how they are joined | `position` gives the order and distance; the morph slice gives person, number, case and tense. **No stored relation** (subject, object, what modifies what) is in the table; I have not checked other tables for one |
| Are groups related or interchangeable | the same pairing across verses, by group | derived from the rows above across all the group's verses |
| Qualifiers and their significance | which neighbour qualifies the group's word, and how it reads | `is_negator` and the T-coded neighbours; the qualifier role is node-level and empty on 14,065 of 68,406 live nodes |
| Multiple entities, entity by group, direction of travel | the entities of the verse and which acts on which | `party_kind` names the entity words; direction is not stored (see the relation row) |

## 2. What the md and the workbook show

- **Section 3 of the md is organised by Strong's code, not by verse.** Each section (3.1 to 3.105) is one code: its stored meaning, its related terms, clusters and counts, the member words that carry it, then one table row for each occurrence: reference, member word, morph, engagement, "other observations" (observation ids only, "-" where none), catalogue observations (a count) and the verse text with the member word in bold. It answers "where does this code occur and what is recorded for it". It does not answer "what lives with this word in its verse".
- **The other words of the verse appear only as ESV text.** The neighbours' Strong's codes, collections, entities, negators and positions are not listed.
- **The workbook sheet `Occurrences`** (395 rows, 25 columns: scope, tiers, word, reference, vl_id, Strong's code, native word, transliteration, STEP gloss, morph, position, surface_kind, kind, unit word, unit role, unit size, role (clusters), negator, party, status, engagement, other observations, catalogue observations, live nodes on withdrawn observations, verse text) holds the member occurrence's own attributes. Its `negator` and `party` columns are those of the member word itself, which is rarely a negator or entity; they are not the verse's.
- **"Other observations"** is the list of observation ids with a live node on that member occurrence (`collectionevidence.py` selects observations by the member occurrence's `verse_lexical_id`). An observation on a neighbouring word of the same verse is not listed, and the id carries no text in the md.

## 3. How much is missing (measured for the thought collection)

Thought's member surfaces under the export tiers (core, synonym, opposite, gathered) are 27 surfaces with 387 occurrences in 346 verses; the report's 33 words and 394 occurrences also include 6 phrases with 7 occurrences, which my count leaves out.

| Measure | Result |
|---|---|
| `verse_lexical` rows in those 346 verses | 6,507 (average 18.8 a verse); the report lists 387 of them |
| Verses holding an occurrence of another collection's surface | 304 of 346; 915 such occurrences |
| Verses holding an entity code (`party_kind`) | 187 of 346 |
| Verses holding a negator | 105 of 346 |
| Verses holding two or more different thought surfaces | 5 of 346 |
| Collections most often in the same verses (verses) | know 34, heart 31, wise 25, evildoer 25, fear 20, live 17, profess 16, labor 16, search 15, serve 15 |
| Thought occurrences with a live node | 131 of 387 |
| Other-collection occurrences in these verses with a live node | 290 of 915 |

My reading: almost every verse where thought occurs also holds another collection's word (88 per cent), and the report shows none of those words as data. That is the "surfaces living together" the layer 2 work starts from, and it is not in the md or the workbook. The 5 verses with two thought surfaces show the pairing inside a collection is rare, so the pairing that matters is across collections (know, heart, wise, evildoer, fear).

A worked verse (`verse_lexical` rows of 1Sa 25:25, "Let not my lord regard this worthless fellow, Nabal..."): `regard` (H3820A, the thought word) sits with the negator `not` (H3808), the entity words `lord`, `fellow`, `Nabal`, `young men` (party_kind human), `worthless` (collection pride) and `folly` (collection folly), in a stated order (positions 0 to 17). The report row for `regard` shows the verse text and the word's own morph; it shows none of these as a pairing.

## 4. Where the selection is hidden (the "cherry picking")

These are the places the report decides what the reader sees without saying so. I cannot say from the data who or what chose, only what is shown:

1. **The unit is the member occurrence.** Everything is anchored on the 387 member occurrences; a neighbour is shown or hidden by whether it is a member of this collection.
2. **Observations are tied to the member occurrence, not the verse.** An observation on `worthless` or `not` in the same verse is not shown, so the report appears more or less supported depending on which word carried the node.
3. **The report orders by Strong's code and frequency (3.1 first, 39 own occurrences).** Codes with one occurrence come last (from 3.50); an interchange between two groups does not show, because their codes sit in different sections.
4. **Occurrences with no node.** 256 of the 387 occurrences have no live node, so no observation of any kind stands behind them. They are listed as rows with a dash. The report does not distinguish "not yet read" from "read and nothing found".
5. **Claims** are reached by verse or observation (the earlier finding on #2463, the claim C-114 case); a claim in the report is not shown with whether it uses the pairing.

## 5. What would make layer 2 evidence visible (a proposal; nothing built, B:105)

For the researcher to correct, keep or reject. Each would be read-only and built from `verse_lexical` and the collections, with no new stored value:

| # | Addition | Shows |
|---|---|---|
| 1 | A verse view: for each verse where the collection occurs, every `verse_lexical` row in word order (position), with its surface, Strong's code, morph, collection (or none), entity (`party_kind`), negator, unit role, and a mark for the member word | the verse as the base data, in order, so pairing and distance can be read |
| 2 | A pairing table for the collection: for each other collection, the verses it shares with each group (layer 1 group, later), the surfaces that meet, the order (before or after) and the distance | which words pair with which group; interchangeability across the groups |
| 3 | A neighbour table of the words with no collection but a role in the pairing (negators, entities, T-coded qualifiers) | the qualifiers and the entities of the verse |
| 4 | For each occurrence the observations on all words of its verse, with their text and node surfaces, not ids only | what is recorded around the member word, not only on it |
| 5 | A "read or not read" status for each occurrence and each neighbour (live node, none) | the difference between "nothing found" and "not read" |
| 6 | The same for the Excel as sheets (verse view, pairings, neighbours), keeping the existing sheets | one workbook that carries the foundation for layer 2 |

Not covered by `verse_lexical`: the relation between words (subject, object, modifier). The layer 2 questions on direction of travel and "what a word does to or from an entity" need it. I have not checked whether any other table holds a relation; this is a decision for the researcher, whether to build one at the lexical stage or to read it by hand in layer 2.

## 6. Method and limits

- Surfaces of each collection: the live `collection_link` rows of the export tiers (`cfg_setting collection.export_tiers`: core, synonym, opposite, gathered), the term itself and the terms whose base it is, as `collectionevidence.py` does (functions `_terms` and `_own_terms`). Occurrences: live `verse_lexical` rows whose lower-cased, trimmed surface is one of them.
- Co-occurrence: every other live `verse_lexical` row of the same verse whose surface is a member of any live collection.
- A node counts when it is live, on a live observation, with that `verse_lexical_id`.
- Not checked: tables other than `verse_lexical` for a word relation; the 256 occurrences without a node were not examined; collections that share surfaces by the "shared" flag were counted once each per verse; the counts are mine and were not re-run on a second route.
- The script is not kept in the project; if the researcher wants the pairing sheets built, it is the starting point of that build.
