# 2228 — Discovery v3: the sources in scope, how each links to a verse, and the tools

Escalation: #2228 v11. Status: discovery, for your review. Nothing is designed in detail or built
(rule 105). Earlier versions are in `outputs/escalation/archive/` (v1, v2). The numbers come from
read-only queries on `iba/app/db/iba.db` and file scans, 2026-10-22.

What your rulings settle (verbatim on #2228, v9 and v11):
- **A grouping is a verse collection.** Cluster, group, batch and strand are all ways of compiling a
  collection of verses.
- **A bare strong is decomposed to its derivatives.** The collection may focus on some of them. The
  rule is not yet in config: #2233.
- **Pulling in more verses through a narrative or claim is a judgement call.**
- **Excluded:** `_analytics/Bible_Books` (the whole folder, including the phase-1 lexical views),
  `registry`, `essay`, characteristics, cross-cluster-web, dimensions, `outputs/`, `research/`, the
  reading units in `bible_research.db`, and tasks and issues.
- **Lexical:** the parse tables are inactive and excluded; the lexical meaning tables are a source.

---

## 1. Your questions

### (b) Strand hits and faces: a file or the database?

**The database.** The table is `reading_strand_hit` in `iba.db`, one row per strand word in a
verse. It is written by the strand reading (`iba/app/ps/Strand-Reading.ps1`, #2172).

- **The columns:** `verse_id`, `strong`, `surface` (the ESV word), `face`, `parties`, `reason`,
  `observation_id`.
- **The face** is the label the reading gives the hit. For example: "A. God angry with his people as
  a whole", "D01. death notices, lifespans, burial, inheritance (data)". A hit that has no face
  carries a `reason` instead.
- **Four strands, all created today:**

| Strand | Cluster | Hits | Faced | Verses |
|---|---|---|---|---|
| fear | M01 Fear and awe | 1,012 | 1,012 | 916 |
| anger | M02 Anger and wrath | 892 | 892 | 681 |
| life-death | M25 Life and death | 2,218 | 2,218 | 2,005 |
| origin-of-thought | M64 Will and resolve | 358 | 0 | 329 |

- **Where the faces came from:** they were loaded today from the October observation ledgers in
  `_analytics/Clusters` (catch-up B, #2172), so the ledgers' faces are now in the table.
- **The origin-of-thought hits** have no face yet; this is #2217.
- **No hit points to its observation:** `observation_id` is empty on all 4,480 rows.

### (d) Lexical: parse out, meaning in

`cfg_table` confirms that the three parse tables are inactive: `strong_meaning_parsed`,
`strong_lsj_parsed` and `strong_mounce_parsed`. `verse_lexical_note` is inactive too. All four are
excluded.

The meaning tables are live, and each is keyed by the exact strong code. A verse reaches them
through `verse_lexical`:

| Table | What it holds | Coverage of the 15,455 strongs in `verse_lexical` |
|---|---|---|
| `strong_sense` | the sense of each code (the first line of the definition), read constantly | 15,455 of 15,455 |
| `strong_meaning_tree` | the lemma's full range of senses (Hebrew and Greek) | 15,452. Missing: H0430H (God), H1121A (son), H5945H (Most High). These are the spine gaps already on #2205. |
| `strong_lexicon` | the Greek lexicons, LSJ and Mounce | 5,513 Greek codes. LSJ 5,513; Mounce 5,510 (missing G0001G, G4528H, G6094, also on #2205) |
| `strong_related` | related words, from STEP | 15,455 codes |

### (e) The debate digest: is there meaningful analysis in it?

**Very little, and only in Daniel.** What the tables hold:

- **`passage`, `verse_passage`:** 42 passages in Daniel, Jonah, Joel, Obadiah, Micah and Hosea,
  built 27 July to 8 August. These are only boundaries: which verses form a passage.
- **`hib`, `verse_hib`:** 21 "human inner beings" (the persons or groups acting), all in Daniel,
  marked on 235 verses.
- **`phenomenon`:** 121 rows on 48 verses, all in Daniel 1 and Daniel 8. 66 are recorded as
  "silent", meaning there is nothing about the inner being in that verse. 54 are "stated" and 1 is
  "inferred". So 55 rows say something, for example Dan 1:4: "the group's own inner faculties named
  directly as selection criteria: skillfulness, wisdom, knowledge, and understanding".
- **`operation`:** 121 rows, one per phenomenon. 66 are recorded silence and 55 are retained; most
  have no process value.
- **`passage_emergent_question`, `passage_insufficiency`, `passage_linkage`,
  `passage_validation_note`:** 3, 1, 3 and 4 rows.
- **The debate write-ups themselves** are files in `_analytics/Bible_Books` (`WA-*-debate.md`),
  which is excluded.

So the digest holds 55 statements about 2 chapters of Daniel. Its steps are still registered in
`cfg_step` (passage.build, phenomenon.set, report.passage_debate, passage.debate_sync). I propose to
exclude it as a source (D2). Retiring its steps is a separate decision and is not proposed here.

---

## 2. The sources that remain, and how each links to a verse

| # | Source | Where | Link to a verse | Holes, and the preparatory work |
|---|---|---|---|---|
| 1 | Observations | `ib_observation` (7,244 draft) + `ib_node` | `ib_node.verse_reference`; all 16,506 resolve | 63 draft observations have no node: ground or withdraw them. The October dispositions of 717 strand observations are text in `revisit_note`: turn them into a real state. |
| 2 | Strand hits and faces | `reading_strand_hit` (4,480) | `verse_id` | The hit → observation link is empty: back-fill. 358 hits have no face (#2217). |
| 3 | Claims | `narrative_claim` (306 current) + `narrative_claim_source` | `verse_id` on 1,805 verse sources | 13 current claims have no verse source. The source → observation link is empty: back-fill. 40 sources name a study file only. |
| 4 | Narrative blocks | `narrative_section` (404 current) + `narrative_citation` | `verse_id` on 7,408 citations | 39 blocks cite no verse. 37 citations do not resolve. |
| 5 | Open items on threads | `escalation_thread_item` (513) | by kind: verse, cluster, strong, chapter, strand | none |
| 6 | Verse status | `verse_meta.status` (3,643 `analysed`) | `verse_id` | See D1. |
| 7 | Lexical layer | `verse_lexical` | `verse_id` | none |
| 8 | Lexical meaning | `strong_sense`, `strong_meaning_tree`, `strong_lexicon`, `strong_related` | `verse_lexical` → exact strong code | 3 codes with no meaning tree and 3 Greek codes with no Mounce entry (#2205). The spine rule (`governance.base_data_spine`) says what counts as missing. |
| 9 | Cluster readings | `_analytics/Clusters`: 228 files, 6.6 MB, 4,477 sections, in 12 cluster folders and the root | text only: 1,985 sections name a reference in the heading, 1,518 only in the body, 974 none | The ledgers of 4 strands are already in the tables: 717 observations, each naming its file, and the faces above. The rest needs the reading index: pride (M08), humility (M09), desire (M18, 47 files), inner seat (M47, 33), will and resolve (M64, 34), authority (M72), shame (M07), doubt (M20), disgrace (M53), and the root files. |

Everything except 9 is in the database and is cut to a verse collection by joins. Source 9 is the
only file source left.

---

## 3. The tools: a handle for each special situation

1. **Scope resolver.** Turns any request into the verse collection, as JSON. It accepts:
   - a cluster, or any grouping of it: a group of strongs or verses, a batch, a strand
   - a strong, with a bare code decomposed to its derivatives and an optional filter to some of them
   - a verse, a list or a range
   - a narrative chapter or block, a claim, an observation, or a thread item

   Each verse carries its route in, and every reference that cannot be resolved is reported. It is
   built from the routes that exist (`lexicalscope`, `parse_refs`, the citation and source tables)
   behind one entry point, with one set-based query per route.
2. **Cluster reading index.** Splits the 228 cluster reading files into sections, once. Each
   section is recorded with its file, heading, position and hash, and the verses it covers, marked
   by how each was found: heading, body, or the file's title. A file is indexed again only when its
   hash changes. Sections with no verse are listed for review, not guessed.
3. **Verse extract.** For the collection, returns from the index only the paragraph or bullet that
   names each verse, with its heading and file. It never opens a whole file.
4. **Known-for-verses pack.** For the collection, one query per source: observations, strand faces,
   claims, narrative blocks, thread items, verse status, the lexical layer and its meaning, plus the
   verse extract. It returns one record per verse.
5. **Gap report.** Inside the collection only:
   - verses with no observation
   - observations with no claim
   - claims not told in the narrative
   - verses read in the cluster files but not in the tables
   - open thread items on the collection
   - missing meaning, by the spine rule
6. **Neighbour-verse review.** For your judgement call. Lists the verses outside the collection
   that a block or claim on it also rests on, each with the claim text, so you can decide whether
   to pull them in. The decision is recorded.
7. **Link back-fill.** One-off work: strand hit → observation, and claim source → observation.
   Where a link cannot be made mechanically, it is listed rather than guessed.

## 4. Preparatory work before the study restarts, in order

1. The bare-strong rule into config (#2233). The two side corrections, #2231 and #2232.
2. Scope resolver.
3. Cluster reading index, run, with a coverage report; then the verse extract.
4. Link back-fill, with a report of what could not be linked.
5. Known-for-verses pack and gap report.
6. Neighbour-verse review.
7. Turn the October dispositions and the 63 observations with no grounding into real states.

Each step is designed for your review before it is built, and tested on a copy.

---

## Decisions for you

| # | Question | Your choice | Comment |
|---|---|---|---|
| D1 | Excluding Bible_Books also excludes its 918 reading files (July: book, oracle and Psalm readings, 17.9 MB). 1,554 verses are marked `analysed` but have no observation in the tables. Inferential: their reading is in those files. With Bible_Books excluded, should `analysed` on those verses count as read, or as not read (so the gap report shows them)? | | |
| D2 | Exclude the debate digest tables as a source (55 statements, Daniel 1 and 8)? | | |
| D3 | Start with the design of the scope resolver (tool 1)? | | |
