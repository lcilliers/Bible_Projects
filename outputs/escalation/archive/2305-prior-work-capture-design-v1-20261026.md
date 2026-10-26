# #2305 Design (v1): capturing prior reading work, what is recorded and how

**Date:** 2026-10-26 · **Escalation:** #2305 · **Status:** design for the researcher's decision. Nothing has been
built or captured. **Input:** `outputs/escalation/2305-prior-work-document-index-v1-20261026.json` (235 documents).

Researcher, chat 2026-10-26 (verbatim): *"the partly document must be included.  The parts already recorded can be
skipped, but the remaining parts must be recorded.  the important thing to work out and be very clear, is what need
to be recorded and how.  This capture process is about capturing any material observation about a verse.  When a
verse is identified in the document, then every observation made in the document for the verse must be captured.
There is no expectation to re-analyse the verse for new or further observations, or validate the observations made.
The wording of the observations must be adjusted to fit into the observation structure already agreed upon. an
observation that does not fit in the structure must get a new type to allow for these observations to be separately
identified.  The rules for splitting the classification of an observation between different handles must be adhered
(e.g. the same observation applying to multiple verses, or multiple strongs or clusters or sub clusters are all
matters for the node.  separate observations should not be created for essencially the same observation."*

This is a migration. It is not part of the standard analytic process. It writes into the observation record already
agreed and built (B2: `outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md` §1
and §3; `cfg_method_rule` RO11, RW-02 to RW-10) and changes none of it, except for the new type (§2.4) and the
stage (Q1).

---

## 1. What is captured

**The unit is the document line that names a verse.** The reading index already holds every such line
(`reading_ref`): 19,034 lines in the 235 documents, naming 11,121 verses (10,277 bullets, 5,228 table rows, 1,900
headings, 1,629 paragraphs).

Of the 51,765 references on those lines, 1,594 resolve to no single verse:
- **1,002 name a whole chapter.** A finding on a chapter gets nodes on the verses it quotes or names. Where it names
  none, it gets one node on the chapter's first verse, with the chapter in `disposition_note`.
- **592 resolve to nothing** (a chapter the book does not have, a verse past the chapter's end, a verse with no row
  by design). They are listed in the run with the line, never guessed (RW-11), and the observation is captured on
  the verses that do resolve.

**What is captured: every material observation the document makes about a verse it names.** An observation is
material when it says something about what the verse shows: what a word means or how it is used there, who acts or
undergoes, what leads to what, what a qualifier gives, how a face differs, or that a word has no inner-being bearing
there. All of it is captured as written, whether the document states it from the verse or reads it ("I read").

**What is not done:** the verse is not read again; no observation is added, checked, corrected or rejected. Whether
an observation is right is not this task's question (RO3; the rules check is the work of #2260 to #2267).

**Not an observation** (the line is answered and passed over, with its reason, §4):
- a heading, a reference list, a hit count, a surface or gloss table that only lists;
- a scope, method, process or test record: what was read, how, in what order, what was decided about the reading;
- a pointer with no content: "carried from M09", "see unit 3", "in Ch 10.6";
- a weave or quote-check record, a next-steps list.

A heading or table cell that carries the finding (a face named in a faces table, a bold statement heading its
evidence) is part of the observation it heads, not passed over.

## 2. How it is recorded

### 2.1 One finding, one observation; everything it applies to is a node

RO11, RW-03 and B:121 govern this, along with the researcher's ruling above. How they apply to the capture:

- **A finding's evidence belongs to it.** The quotations and the verse list that support one thing said do not
  make further observations.
- **Verses, words, clusters, subgroups and roles are nodes.** The same finding over six verses, three Strong's
  numbers or two clusters is one observation with that many nodes.
- **The same finding in another document** (an overview restating a ledger, a batch reading repeating a group
  reading) gets nodes on the observation already captured, never a second observation. Whether two passages say
  essentially the same thing is judged by reading them, not by matching text. The later line is answered
  `already recorded` with the observation's id.
- **A split is made only where the document says two different things:** two findings about one verse, or two
  readings of one verse set side by side (RW-08).
- **A finding about other findings** (a "what differs between the faces" table, a pairing across faces) is its own
  observation, applied to the findings it compares through `ib_node.traced_observation_id`.

### 2.2 The observation (`ib_observation`)

| Column | Written | From the document |
|---|---|---|
| `obs_text` | the finding, restated concisely in the B2 shape (§2.5) | its substance and its quotations |
| `meaning`, `implication` | where the document states them | as stated; left empty where it does not |
| `basis` | `stated` or `read` | `stated` where it is what the verse says; `read` for "I read", "I take", "inferential" |
| `tag` | the kind (§2.4) | from what the finding is |
| `route` | A, B or C, on a party or link finding | Ch 13 / other beings is A, HIB is B, "data" is C, where the document routes it |
| `stage` | `prior-capture` (decision Q1) | marks the row as migrated, not read in a standard reading |
| `status` | `draft` | |
| `stable_key` | the document's own id where it has one (`fear:FE-50`, the October form), else `<reading_file_id>:L<line>` | lets a later run see what is already captured |
| `revisit_note` | `Captured from <full path> lines <a>-<b> (#2305)` | the October import's form, so the reading index's count and the collation pick it up |
| `run_id` | the capture run | |

Not written on the observation, as B2 sets: `strong`, `cluster_code`, `cluster_subgroup_id`, `question_code`,
`window`, `setting`, `chain`, `parties`. `meaning_source` keeps its enum use (`verse-text` for a stated finding,
`observations` for a finding about findings); the citation is in `revisit_note`.

### 2.3 The nodes (`ib_node`)

| Column | Written |
|---|---|
| `verse_reference` | each verse the finding applies to, resolved fresh from the line (RW-06) |
| `verse_lexical_id`, `strong`, `surface`, `morph_code` | the word occurrence the finding is about, found in `verse_lexical` for that verse (the document names the English word, the Strong's number, or both) |
| `cluster_code`, `cluster_subgroup_code` | the word's own M-code (or T-code) and subgroup, from `cluster_strong` and the surface map, never from the document |
| `role` | characteristic, qualifier or standalone |
| `traced_observation_id` | for a finding about findings |
| `disposition`, `disposition_note` | where the document says the verse went (decision Q4); the document's chapter pointer ("touches 10.1") goes in the note |
| `source_stage` | `prior-capture` |

A finding that names a verse but no word gets a node on the verse alone. A word the document names that cannot be
placed on one occurrence gets a node with its verse and Strong's and no `verse_lexical_id`, and goes to the cluster's
anomaly group (B:121).

### 2.4 The kind, and the new type

What the documents hold fits the eight kinds (RW-02) almost everywhere:

| In the documents | Kind (`tag`) |
|---|---|
| a faces table row; "the word describes …"; "Face K: terror that comes upon" | `face` |
| what a measure word, an object, a cause or a setting gives the characteristic | `qualification` |
| who bears, causes, receives; God, a spirit, nature acting or acted on | `party` |
| a bold statement with its verses; "Fear leads to hiding"; "Pride deceives the one who has it" | `statement` |
| "X, then Y"; "set against"; "joined to"; one characteristic giving rise to another | `link` |
| one phrase put to different ends; a speaker's purpose; one word in two senses | `use` |
| one root rendered many ways; surface variants; related words | `term` |
| "data", "no inner-being bearing", "used of a pot" | `silence` |

**The new type: tag `unfitted`** (decision Q2). A material observation about a verse that is none of the eight is
captured as it stands with tag `unfitted`, so these rows can be found and sorted later. The run reports every one
with its line. Candidates seen in the sampling: a note on the text or translation itself, a literary or structural
point about a passage, a comparison with a verse outside the study's verse set.

### 2.5 The wording

The researcher's ruling is that the wording is adjusted to the structure and the substance is kept:
- concise and tied to the verse (RW-04): the finding first, then the quotations it rests on, in the ESV words as the
  document quotes them;
- a transliteration keeps its gloss (*paḥad*, "dread");
- the document's own frame is removed where it is about the reading, not the verse ("This is the clearest single
  pattern in the batch" becomes the pattern itself);
- nothing is added, softened or corrected. Where the document reads beyond the verse, it stays, with `basis` `read`.

## 3. The parts already recorded

662 live observations name 19 of the documents (the October catch-up, #2266). They are skipped as follows, and are
not changed (their restatement is #2266's work):
- **A ledger with ids** (the 19 documents are all ledgers): an id with a live observation whose `stable_key` is that
  id is already recorded. Example: in `_analytics/Clusters/M01 - fear-awe/fear-observation-ledger-unit2-v1-20261001.md`,
  28 of the ids FE-47 to FE-85 are in the table; FE-50, FE-56, FE-63, FE-64, FE-67, FE-70, FE-72 and FE-78 to FE-81
  are not, and are captured.
- **The parts of those ledgers October did not take** are captured in full: the faces table (§A), the
  change-of-character table (§C), and any finding in the other sections.
- **An observation already recorded** is answered `already recorded`, with its id. When another document says the
  same thing, its verses are added as nodes to that observation (§2.1). This adds nodes to an October row and
  changes nothing else on it.

## 4. Every line answered

Each document is captured whole, in one run, and no line naming a verse passes unanswered. Each line gets one of:

| Answer | Meaning |
|---|---|
| `captured` | the observation(s) it gave, by id |
| `already recorded` | the observation that already holds it, by id |
| `not an observation` | with its reason, one of the classes in §1 |

The answers are kept with the run, so what was taken from each document, and why the rest was passed over, can be
checked line by line. The document's `capture_status` in the index is set to `captured`, or `nothing to capture`
when every line is passed over.

## 5. Order

Cluster by cluster. Within a cluster: the ledgers and readings first, by date; then the syntheses and overviews,
which mostly restate them and so mostly answer `already recorded` or add nodes; then the data and process documents,
which are read and mostly passed over. The five admin files and the ten documents with no cluster come last.

## 6. Worked examples (real lines; not written)

**a) A ledger finding October did not take.** `fear-observation-ledger-unit2-v1-20261001.md`, FE-50, "Dread before
God's presence, voice, word and act", with seven sub-bullets of evidence:
- one observation, tag `statement`, basis `stated`, stable_key `fear:FE-50`. obs_text: *Dread and trembling arise
  before God's presence, voice, word and act: "I am terrified at his presence; when I consider, I am in dread of
  him" (Job 23:15–16); "At this also my heart trembles" at the thunder (Job 37:1); "all the people in the camp
  trembled" at Sinai (Exo 19:16); "they turned trembling to one another, saying, 'What is this that God has done to
  us?'" (Gen 42:28)*, and the other three bullets in the same way;
- the seven sub-bullets are evidence, not seven observations;
- nodes on every word the quotations name, for example Job 23:15 *terrified* (H0926, M24) and *dread* (H6342, M01),
  both role characteristic; Exo 19:16 *trembled* (H2729, M01); Gen 42:28 *trembling* (H2729, M01) and *hearts*
  (H3820A, M47, role standalone, the seat the verse names). One observation, three clusters on its nodes;
- disposition: the ledger's `W` and "touches 10.9, 10.2" (decision Q4).

**b) A ledger finding October took.** FE-47 is observation 11762 (`fear:FE-47`): answered `already recorded`.

**c) A face in a reading.** `M18 - desire-longing/m18-group-D-reading-v1-20261009.md` §1, the row "Consumes the one
who has it": one observation, tag `face`: *Zeal consumes the one who has it: lit by insult to God's house and by the
forgetting of God's words, it draws God's reproach onto the zealous one*; nodes on Psa 69:9 *zeal* (H7068, M18,
characteristic), with *reproaches* (H2781, M07) and *reproach* (H2778A, M53), the words the finding names, and on
Psa 119:139 and Joh 2:17. The paragraph after the table, "**I read:** … not a strength the zealous one holds but a
fire that uses him up", is the same face read further: it goes into this observation's `meaning`, not into a second
observation.

**d) One finding, two clusters; and a second finding beside it.** `M08 - pride-arrogance/m08-batch2-reading-v1-20261015.md`,
"Pride deceives the one who has it" (Obd 3; Jer 49:16, "The horror you inspire has deceived you, and the pride of
your heart"): one `statement`; nodes on Jer 49:16 *pride* (H2087, M08), *deceived* (H5377, M14), *inspire* (H8606,
M01) and *heart* (H3820A, M47). The document's "The fear others feel feeds the self-deception" says something else
(fear leading to self-deception): a `link`, basis `read`, its own observation.

**e) Lines passed over.** In the same M18 document, the heading "## 4. God's jealousy (13.1 *Jealousy*)" and the
note "Isa 37:32 carried": `not an observation` (heading; pointer). The route the heading gives (13.1, other beings)
is carried to the findings under it as route A.

## 7. How it runs

Per document, three steps, in the pattern of the #2304 prototype (its D7 b: the capture is judgement, not pattern
matching):
1. **Prepare** (a tool): the document's sections and every line naming a verse, the verses resolved, the M- and
   T-coded occurrences in each verse (`verse_lexical` with `cluster_strong` and the surface map), and the
   observations already naming the document or its ids. One JSON per document.
2. **Fill** (Claude, reading the document): the findings in the §2 shape, and an answer for every line.
3. **Record** (a tool): refuses the run unless every line is answered, every enum is valid and every node resolves;
   writes the observations, nodes and line answers in one transaction; sets the document's `capture_status`.

The tool and the new config (stage `prior-capture`, tag `unfitted`, a write grant for the recorder, its step) are a
Developer Mode build. It is tested first on a copy (B:97) with two documents, one partly imported ledger
(`fear-observation-ledger-unit2-v1-20261001.md`) and one reading (`m18-group-D-reading-v1-20261009.md`), and the
results are shown before the live run.

**Size.** 19,034 lines in 235 documents. At one or a few documents per run, this is many sessions. The index records
where it stands, so the capture can stop and resume at any document.

## 8. Decisions sought

| # | Question | Options | Recommend |
|---|---|---|---|
| Q1 | The `stage` of a captured observation | a) `prior-capture`, new; b) `reading`, as a standard reading | a: the rows stay identifiable as migrated, and the collation reads every stage anyway (#2276) |
| Q2 | The new type for an observation that fits none of the eight kinds | a) tag `unfitted`; b) another name | a, or the researcher's name |
| Q3 | A finding about a word with no verse named ("one root, many renderings") | a) captured, nodes on the Strong's with no verse (B2 allows this for a term finding); b) not captured, since the task is observations about a verse | a: B2 already provides for it, and the documents usually list the verses anyway |
| Q4 | The document's own disposition (the ledgers' `W` woven, `held`, `data`) | a) carried onto the node: W to `told`, held to `held`, data to `data`, none left empty, the chapter pointer in `disposition_note`; b) left empty for a later reading to set | a: it records where the verse went, already decided |
| Q5 | Flags and open questions in the documents ("needs the next verse", "to check") | a) captured with the observation they belong to, in `revisit_note`, no open item raised; b) an open item raised for each (RW-07) | a: raising items is analysis, not capture; the run lists every flag |
| Q6 | The admin, data and process documents | a) read and answered line by line like the rest (mostly `not an observation`); b) left out | a: some process documents hold findings (scope rulings, test readings) |
| Q7 | The pilot | the two documents in §7, on a copy | as named |
