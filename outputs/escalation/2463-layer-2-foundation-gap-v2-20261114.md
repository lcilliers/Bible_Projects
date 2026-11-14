# #2463 What the thought evidence report lacks as the foundation for layer 2 (v2, 2026-11-14)

Status: findings for the researcher to correct; read-only; nothing built or changed. Prompted by the researcher (#2463, 2026-11-14, verbatim): "i think the md and the excel is missing or not sufficiently showing the foundation work for layer 2, which causes us to stumble. layer 2 base data is in the verse-lexical, and the observations around faces is sort of moving in the right direction, and you analysis §3 in the md also flirts around it, but there is nothing that truely teases out the significance of surfaces living together in the verses, it seems there is mostly a lack of clarity and quite a bit of cherry picking taking place."

Second input (researcher, #2463 v24, verbatim): "another input in your analysis, is that the work is mostly done on a strong level, and not on a concept level, which make the actual comparative trends much more difficult.  regarding your 6 points.  verse-lexical provide the data so each surface co-existance can be plotted, pairings can be teased out using the positions, but also differentiation of different types of pairings, the real impact and relation of the pairings only come to life in context reading.  this must be done at different levels, not only strong level, but moving toward concept level - the data should be prepared to speak much more for itself that it is doing at the moment." Section 3a and section 5 answer it.

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

## 3a. The same pairings at four levels (measured for thought; the researcher's second input)

For each thought occurrence (387), every other word of its verse that is an entity (`party_kind`), a negator, or a member of another collection, with its distance in positions and its side (before or after). Links are counted for each thought occurrence, so a verse with two thought words counts its neighbours twice. T-coded qualifiers other than negators and function words are not in this count.

**Typed pairings (1,558 links):**

| Neighbour type | Links | Adjacent (1 position) | Near (2 to 3) | Far (4 or more) |
|---|---|---|---|---|
| Member of another collection | 1,010 | 147 | 275 | 588 |
| Entity, human | 231 | 36 | 50 | 145 |
| Entity, divine | 161 | 11 | 37 | 113 |
| Negator | 156 | 31 | 43 | 82 |

The neighbour is after the thought word in 882 links and before it in 676.

**The same links counted at each level:**

| Level the pair is counted at | Distinct pairs | Seen once | Seen 5 or more times |
|---|---|---|---|
| Strong's code (thought code with neighbour code) | 1,167 | 941 | 19 |
| Surface (thought surface with neighbour surface) | 916 | 613 | 42 |
| Collection or type (the neighbour's collection, or entity or negator) | 141 | 14 | 77 |

My reading: at the Strong's level 81 per cent of the pairs (941 of 1,167) are seen once, so no trend can show; at the collection level 77 of 141 partners recur five times or more, and the pattern is visible: entity (human 231, divine 161), negator 150 (of 156 links; the other six sit in a collection and are counted there), then know 47, heart 41, evildoer 35, wise 28, fear 28. That is the researcher's point, shown for one collection. It also shows what a Strong's-level view hides: the strongest Strong's pair is H0559 (to say, carried by the member word thought) with the negator H3808, 14 times, a use that is about saying, not thinking.

**Which levels exist today, from the tables (2026-11-14):**

| Level | Held? |
|---|---|
| Strong's code | yes: `verse_lexical.strong` |
| Surface | yes: `verse_lexical.surface` |
| The layer 1 group inside a collection (starting, weighing, the types) | no: not built (layer 1) |
| Collection | yes: 169 confirmed collections (86 merged, 23 retired) |
| Concept above the collection | no: `collection.concept_id` is empty on all 169 live collections; the `concept` rows (101) group subgroups, not collections |

So comparison is possible today at the code, surface and collection levels only; the group level comes from layer 1, and the concept level needs the roll-up of collections into concepts that the `collection` table describes as not yet done.

## 4. Where the selection is hidden (the "cherry picking")

These are the places the report decides what the reader sees without saying so. I cannot say from the data who or what chose, only what is shown:

1. **The unit is the member occurrence.** Everything is anchored on the 387 member occurrences; a neighbour is shown or hidden by whether it is a member of this collection.
2. **Observations are tied to the member occurrence, not the verse.** An observation on `worthless` or `not` in the same verse is not shown, so the report appears more or less supported depending on which word carried the node.
3. **The report orders by Strong's code and frequency (3.1 first, 39 own occurrences).** Codes with one occurrence come last (from 3.50); an interchange between two groups does not show, because their codes sit in different sections.
4. **Occurrences with no node.** 256 of the 387 occurrences have no live node, so no observation of any kind stands behind them. They are listed as rows with a dash. The report does not distinguish "not yet read" from "read and nothing found".
5. **Claims** are reached by verse or observation (the earlier finding on #2463, the claim C-114 case); a claim in the report is not shown with whether it uses the pairing.

## 5. What would make layer 2 evidence visible (a proposal; nothing built, B:105)

For the researcher to correct, keep or reject. The principle from the researcher's second input: the data is prepared to speak for itself, at several levels; what a pairing means and does for the inner being is read in context (layer 2 reading), not computed. So each addition is read-only, built from `verse_lexical` and the collections, shows a typed and counted pairing, and leaves the meaning column for the reading.

| # | Addition | Shows | Levels |
|---|---|---|---|
| 1 | Verse view: every `verse_lexical` row of each verse in word order (position), with surface, Strong's code, morph, collection (or none), entity, negator, unit role, and the member word marked | the verse as base data, so pairing and distance are readable | row level |
| 2 | Pairing table: one row for each pair of (member word, neighbour), with the neighbour's type (collection, entity divine or human, negator, other), side, distance, and the verse | the pairings, typed and positioned | surface and code |
| 3 | Pairing summary at each level: the same pairs counted by Strong's code, by surface, by collection or type (and later by group and by concept), each with its count and verses, and the typed split (adjacent, near, far; before, after) | the comparative trends, which the code level hides | code, surface, collection, later group and concept |
| 4 | Neighbours with no collection but a role in the pairing (negators, entities, T-coded qualifiers) listed with the pairs they join | the qualifiers and entities of the verse | row level |
| 5 | Observations on every word of the verse with their text and node surfaces, not ids only; and a read or not-read mark for each member occurrence and neighbour | what is recorded around the word, and the gap between "nothing found" and "not read" | row level |
| 6 | An empty "reading" column on the pairing rows and summary rows, for the context reading to fill and for layer 2 observations to cite | the place where the meaning and impact are recorded, kept apart from the prepared data | each |
| 7 | The same as workbook sheets next to the existing ones; the md gives the summary and a count per level, with the detail in the sheets | one report that carries the foundation | each |

Order of the levels: code and surface and collection can be built now; the group level follows layer 1; the concept level waits for the collection roll-up. The build is a change to `lib/collectionevidencereport.py` and `lib/collectionevidence.py` and is Developer Mode work, tried on a copy, with the report's test plan updated in the same unit (B:46); it is not started.

Not covered by `verse_lexical`: the relation between words (subject, object, modifier). The layer 2 questions on direction of travel and "what a word does to or from an entity" need it. I have not checked whether any other table holds a relation; this is a decision for the researcher, whether to build one at the lexical stage or to read it by hand in layer 2.

## 6. Method and limits

- Surfaces of each collection: the live `collection_link` rows of the export tiers (`cfg_setting collection.export_tiers`: core, synonym, opposite, gathered), the term itself and the terms whose base it is, as `collectionevidence.py` does (functions `_terms` and `_own_terms`). Occurrences: live `verse_lexical` rows whose lower-cased, trimmed surface is one of them.
- Co-occurrence: every other live `verse_lexical` row of the same verse whose surface is a member of any live collection.
- A node counts when it is live, on a live observation, with that `verse_lexical_id`.
- Not checked: tables other than `verse_lexical` for a word relation; the 256 occurrences without a node were not examined; collections that share surfaces by the "shared" flag were counted once each per verse; the counts are mine and were not re-run on a second route.
- Section 3a: a second query of the same kind (neighbour types from `party_kind`, `is_negator` and collection membership; distance is the difference of `position`, which is span order, not syntax). Collections counted: `collection` rows with deleted = 0 and status confirmed (169); merged (86) and retired (23) are not counted as live.
- The scripts are not kept in the project; if the researcher wants the pairing sheets built, they are the starting point of that build.
