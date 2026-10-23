# 2228 — Discovery v2: each resource, how its link to a verse resolves, and the tools

Escalation: #2228 v9. Status: discovery, for your review. Nothing is designed in detail or built
(rule 105). v1 is at `outputs/escalation/archive/2228-discovery-scope-and-known-v1-20261022.md`.
The numbers come from read-only queries on `iba/app/db/iba.db` and a read-only scan of the files,
2026-10-22.

Your answers to v1 (verbatim on #2228 v9) settle these points:
- **A grouping is a verse collection.** A cluster, a group of its strongs or verses, and a batch of
  a group are all just ways of compiling a collection of verses.
- **A bare strong is always decomposed to its derivatives.** The collection may then focus on a
  subset of them. The rule is not in config: raised as #2233.
- **Pulling in more verses through a narrative or claim is a judgement call, not mechanical.** It
  depends on the nature of the claim.
- **`registry` and `essay` are excluded.**
- **Bible_Books is the big issue.** A tool must extract exactly the verse, without reading whole
  books.

---

## 1. The finding that changes the size of the problem

Bible_Books is 1,740 files and 236 MB, but most of that is not reading. It splits three ways:

| Part of Bible_Books | Files | Size | What it is | Treatment |
|---|---|---|---|---|
| Database extracts: whole-book `verse-lexical`, `verse-span-meaning`, `fanout`, `lexical-exceptions`, coverage and state diagnostics | 187 | 206 MB | Generated from `verse_lexical` and `span` ("generated from verse_lexical, never an independent write"). The tables hold it. | **Exclude.** It can be regenerated, so it holds nothing to look up. |
| Phase-1 lexical views (`phase1-views/…-lexical-view`) | 635 | 12.7 MB | Per-verse lexical drafts from July, for 21 books (Psalms 300, Isaiah 66, Jeremiah 52, Ezekiel 48, Job 42, …). Each verse has its own heading (`## Psa 117:1`). | **A source.** The fields they carry (sense, type, operation, target, intensity, bearer) are in no `iba.db` column registered in `cfg_column`. So these files are the only home of that lexical model. Inferential: a retired table may once have held them. |
| Readings | 918 | 17.9 MB | Book, unit and oracle readings, Psalm chapter readings, unit and scene syntheses, passage debates, re-read cycle logs, catch-up units, whole-book reads | **The real knowledge.** It needs a verse index. |

So the file problem is about 1,800 files and 37 MB, not 2,700 files and 263 MB: 918 reading
files, 635 lexical views and 228 cluster readings.

---

## 2. Each resource: how its link to a verse will resolve

| # | Resource | Link today | How the link will resolve | Preparatory work before the study restarts | Tool |
|---|---|---|---|---|---|
| 1 | Observations (`ib_observation`, 7,244 draft) | `ib_node.verse_reference`. All 16,506 resolve to `verse`. | A join on the collection | 63 draft observations have no node at all: ground them or withdraw them. The October dispositions (to weave, stays in data, …) of 717 strand observations sit only in `revisit_note` text: turn them into a real state. | known-for-verses pack |
| 2 | Strand hits and faces (`reading_strand_hit`, 4,480) | `verse_id` | A join | The hit → observation link is empty on all 4,480 rows: fill it where the observation's own nodes show it. 358 hits have no face (#2217). | link back-fill |
| 3 | Claims (306 current) | `narrative_claim_source.verse_id` | A join. Pulling in a claim's other verses is your judgement call. | The claim source → observation link is empty on all 1,851 rows. 13 current claims have no verse source. 40 sources name a study file: point each one at the file section through the reading index. | link back-fill; neighbour-verse review |
| 4 | Narrative blocks (404 current) | `narrative_citation.verse_id` | A join. Pulling in a block's other verses is a judgement call. | 39 blocks cite no verse. 37 citations do not resolve. | neighbour-verse review |
| 5 | Open items: thread items (513) | by kind: `verse`, `cluster`, `strong`, `chapter`, `strand` | Through the scope resolver, per kind | none | scope resolver |
| 6 | Open items: tasks and issues | free text only | A structured scope on the item, in the same kinds as thread items | Give each open task and issue that is about study content a scope (8 of the 25 open ones name verses). New items carry it from the start. | scope resolver |
| 7 | Verse status (`verse_meta.status`, 3,643 `analysed`) | `verse_id` | A join | none. The reading index will show where the readings of the 1,554 analysed verses with no observation are. | known-for-verses pack |
| 8 | Lexical base data (`verse_lexical`, meaning and parse tables) | `verse_id`, then strong | A join. Missing meaning or parse comes from the spine rule (`governance.base_data_spine`). | none | gap report |
| 9 | Debate digest (`phenomenon`, `operation`, `hib`, `verse_hib`, `passage`, `verse_passage`) | `verse_id` or passage | A join | Decision D4 | known-for-verses pack |
| 10 | Bible_Books readings (918 files, 13,334 sections) | text only | **Reading index:** each section is entered once with the verses it covers | Build and run the index. Of the 13,334 sections, 6,284 name a reference in the heading (e.g. `## MIC-theophany-judgment · Mic 1:2–16`) and 2,393 only in the body (often `vv.2–7`, with book and chapter from the title). 4,655 name none; mostly Contents, process control and logs, which are listed for review, not guessed. | reading index; verse extract |
| 11 | Phase-1 lexical views (635 files) | text only, one heading per verse | The reading index: each verse heading is one entry | Build and run the index; it is mechanical here | reading index; verse extract |
| 12 | Clusters readings (228 files, 4,477 sections) | text only | The reading index. The October ledgers of 4 strands (anger, fear, life-death, origin of thought) are already in `ib_observation`: 717 rows, each naming its file. | Index the rest: the pride, humility and desire batch readings, validation registers and worksheets, phenomena, no-seat observations and overviews. 1,985 sections name a reference in the heading, 1,518 only in the body, and 974 none. | reading index; verse extract |
| 13 | characteristics (22), cross-cluster-web (23), dimensions (5) | text, organised by characteristic or cluster, not by verse | Of 374 sections, 9 name a reference in the heading. cross-cluster-web also holds design hand-overs (e.g. `escalation-2000-build-handoff`). | Decision D3 | — |
| 14 | `outputs/escalation`, `outputs/strand-reading`, `research/discovery` (280 files) | text | The verse-heavy files are copies of the tables: context packs (`2172-catch-up-b-…-context`), the anger gather, and escalation history exports. The one reading among them, the anger inner-seat basis, is recorded in `ib_observation` (#2172). | **Exclude.** Inferential: nothing else in them is unique; only the 19 files with 20 or more references were looked at. | — |
| 15 | Reading units (`segment_unit`, `segment_unit_verse`) | in `bible_research.db`, inactive: 877 units → 10,330 verses (`cfg_table`) | They would resolve a unit name in a reading heading (MIC-theophany-judgment) to its verses | Decision D5. Not queried, because it is inactive and in `bible_research.db` (rules 61, 67). | reading index |
| — | `registry`, `essay` | — | — | excluded by you | — |

---

## 3. The tools: a handle for each special situation

1. **Scope resolver.** Turns any request into the verse collection, as JSON. It accepts:
   - a cluster, or any grouping of it: a group of strongs or verses, a batch, a strand
   - a strong, with a bare code decomposed to its derivatives and an optional filter to some of them
   - a verse, a list of verses or a range
   - a narrative chapter or block
   - a claim, an observation, or an open item (through the item's kind or scope)

   Each verse in the JSON carries why it is in (the route), and every reference that cannot be
   resolved is reported, never dropped. It is built from the routes that already exist (`lexicalscope`,
   `parse_refs`, the citation and source tables) behind one entry point, with one set-based query per
   route.
2. **Reading index.** Splits the reading files (Bible_Books readings, phase-1 views, Clusters
   readings) into sections, once. Each section is recorded with its file, heading, position and a
   hash, and the verses it covers, each marked by how it was found: heading, body, or the file's
   title. Book and chapter context comes from the title and the unit heading. A file is indexed
   again only when its hash changes. Sections with no verse are listed for review.
3. **Verse extract.** Given the collection, returns from the index exactly the passages that speak
   of each verse: the paragraph or bullet naming it, under its section heading, with the file and
   position. It never opens a whole book.
4. **Known-for-verses pack.** For the collection, pulls what is known from every table source, one
   query per source: observations, strand faces, claims, narrative blocks, open items, verse status,
   the lexical layer, the debate digest. It adds the verse extract, and returns one record per verse.
5. **Gap report.** Within the collection only: verses with no observation, observations with no
   claim, claims not told, verses read in files but not in the tables, open items on the
   collection, and missing meaning or parse by the spine rule.
6. **Neighbour-verse review.** For the judgement call. Lists the verses outside the collection that
   a block or claim on the collection also rests on, each with the claim text, so the call can be
   made to pull them in or not. The decision is recorded.
7. **Link back-fill.** One-off preparatory work: strand hit → observation, claim source →
   observation, and the claim sources that name a study file → the file section. Where a link
   cannot be made mechanically, it is listed rather than guessed.

---

## 4. Preparatory work before the study can restart, in order

1. The bare-strong rule into config (#2233). The two side corrections, #2231 and #2232.
2. Build the scope resolver.
3. Bring in the reading units, if decided (D5).
4. Build the reading index and run it over the reading sources. Report its coverage: sections
   with verses, without verses, and references that do not resolve.
5. Build the verse extract on the index.
6. Run the link back-fill and report what could not be linked.
7. Give the open tasks and issues a scope, and change the Raise action so new ones carry one (D6).
8. Build the known-for-verses pack and the gap report.
9. Build the neighbour-verse review.
10. Turn the October dispositions and the 63 observations with no grounding into real states.

Each is designed for your review before it is built, and each is tested on a copy.

---

## Decisions for you

| # | Question | Your choice | Comment |
|---|---|---|---|
| D1 | Exclude the 187 database-extract files (206 MB) from Bible_Books, since the tables hold them? | | |
| D2 | Treat the 635 phase-1 lexical views as a source and index them, since their fields are in no table today? | | |
| D3 | characteristics, cross-cluster-web and dimensions (50 files): exclude, or index by cluster or characteristic rather than by verse? | | |
| D4 | The debate digest tables (`phenomenon`, `operation`, `hib`, `passage`…): part of "what is known", or retired method? | | |
| D5 | Bring the reading units (`segment_unit`, `segment_unit_verse`, 877 units) from `bible_research.db` into `iba.db` as the unit map for the reading index? | | |
| D6 | Tasks and issues get a structured scope in the same kinds as thread items? | | |
| D7 | Start with the design of the scope resolver (tool 1)? | | |
