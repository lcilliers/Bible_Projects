# #2510 The study's learning history: the change events in sequence, and what two streams of trial and error taught (v1, 2026-11-19)

Status: analysis by Claude from the record, for the researcher to correct. It replaces `outputs/escalation/archive/2510-characteristics-battleground-review-v1-20261119.md` (the first review, built from the BUILD history alone) and the section 5 and 6 tables of the project map v2. Built after the researcher's note of 2026-11-19: catalogue every change event in sequence, look for the changeovers the first pass missed, and separate the learning into two streams, (a) the subject matter and (b) the process. The researcher's own account of the characteristics battleground (recorded on #2510 v8) and the two streams are taken as the frame.

Sources: the project's own reconstruction of 2026-06-14 (`outputs/markdown/project-reconstruction/01` and `02`), the June to July methodology documents (`Workflow/methodology/`, `Workflow/Instructions/archive/`), the archived session logs (`Logs/`, `Logs/archive/`), the archived memory lessons (`memory/archive/`, 241 files), `iba/app/BUILD.md` (540 entries), `CHARTER.md`, `outputs/escalation/2509-escalation-history-v1-20261119.md`, and read-only queries of `iba.db`. Stream tags: **S** subject matter, **P** process, **B** both. An inference is marked as one (B:4). The first review had missed the whole period before 2026-07-17; this one does not.

## 0. The summary

1. **The study did not move in a line; it oscillated between two views of its subject and each swing was forced by a finding.** The subject was first modelled as a list of named characteristics (Feb), then as clusters of terms that each carried characteristics (May), then, after a cold-read validation found that 70 to 85% of the analytical claims imported meaning the verses do not carry (24 Jun), as movements and a relational web with "identify, name and describe characteristics" set aside (25 Jun, "the reset"), then again as characteristics, this time read from the verse and typed there (the authoritative cycle of 8 Jul), and now as the collation of characteristics on surfaces read in context (Nov). The October to November design is a third synthesis, not the first.
2. **There are two roots under almost every failure, named by the project itself on 2026-06-14: over-structuring an integrated subject, and drift between what was decided and what the live artefacts say.** They are the two streams: the first is the subject stream, the second the process stream.
3. **In the subject stream the lesson is always about grain.** The wrong grain was repeated six times: the registry word, the dimension, the term-similarity cluster, the lemma, the Strong's code, the single word out of its verse. The right grain moved each time toward the occurrence in its verse: the verse in its context, the sense and not the lemma (2 Jul), the surface and not the code (28 Oct to 7 Nov).
4. **In the process stream the lesson is always about verification.** Discretion in instructions drifted (Apr), an AI was the sole quality gate (Mar), an audit checked one direction and enforced fabrication (Jun), "completeness" was circular or passage-level while the foundation reached 9% of spans (Jun to Jul), validators checked structure while the values were wrong (Jul 21 and Nov 15). The response each time was to move a rule from a document or a person into a mechanism that checks the content.
5. **Each stream hid the other.** Process failures (a fabrication loop, circular completeness checks) hid what the verses say; subject changes (the reset, the sense grain, the surface) invalidated the process built on the earlier subject view and forced the rebuilds.
6. **Every gap was found by the researcher reading one concrete case by hand**, never by the app's own checks. The app's checks have repeatedly passed while the content was wrong.
7. **The failure that runs through both streams, and that this summary first missed, is the difference between the verse context of the words used and the verse context of the inner being's working, and above all that no one knows how to depict the working systematically.** The what is understood (the question, the unit, the evidence); the how (whether it can be checked, how to keep a read consistent, where it is read) is still part of the discovery. The study has defined the working in eleven stages (`outputs/escalation/2510-inner-being-definition-lineage-v1-20261119.md`) and pursued none of the definitions: each was applied to a bounded set and replaced when a problem surfaced, while the elements were mostly renamed and not carried forward. The methods the researcher put in place did not ground (separate observations for verse analysis and inner-being analysis; the surface group used twice; two grains; an undefined batch unit; nuances and variances), and the reading interventions the record defines (read beyond the verse, reclassify a word, do not force meaning) are not carried into the layered reading. The `thought` grouping of 15 November failed at this point. See `outputs/escalation/2510-inner-being-working-v3-20261119.md`; read it first.
8. **What is not yet tested:** the current design has not been run through a stage on any collection, so it has not met the test where the 3 August 2026 verse-reading method failed (consistency at scale).

## 1. Catalogue of change events in sequence

Each row is an event that changed what the study does or how. Routine fixes are left out. The number is the event's place in the sequence.

### 1.1 January to April 2026: the framework documents and the per-word programme

| # | Date | Event | Trigger or finding | S/P | Source |
|---|---|---|---|---|---|
| 1 | Jan | Framework A (the Holy Spirit) and Framework B (Spirit, Soul and Body) begun | A wish to understand spirit, soul and body, and the Spirit's relation to the human inner life | S | Programme prose, Mission |
| 2 | Feb | Scope extended from Framework B's overview: an in-depth study of the soul within the inner being; a registry of about 200 words | A cursory overview counted some 28 characteristics, an order of magnitude short | S | Programme prose, Scope |
| 3 | Mar | A per-word STEP extraction engine (Session A, v9, signed off 18 Mar); the STEP API reverse-engineered; span-based verse filtering | The need for a structured text source | P | Reconstruction 01 |
| 4 | 7 Mar | Session C (full verse-context extraction) retired from Phase 1; multi-part logic removed from Session A | Production burden; the required array never populated; duplicated Session B | P | Reconstruction 02 |
| 5 | 15 Mar | The AI recognised as unfit to be the sole quality gate: inconsistent formats, an incomplete verse search, registry numbers fabricated from memory, a file claimed compliant that was not | Format drift across sessions | P | Reconstruction 02 |
| 6 | 22 to 25 Mar | The audit engine redesigned to treat STEP as master; seven engine bugs; a destructive reset that deleted researcher flags; duplicate term rows | Engine and schema re-migration | P | Reconstruction 02 |
| 7 | 23 to 24 Mar | H2734 (anger, 91 occurrences) found entirely missed by a text search; the search moved to the `meanings=` semantic endpoint | The ESV never renders it "anger" | S | Reconstruction 02 |
| 8 | 29 Mar | A pool-based design and a Verse Context stage added (classify each verse per term as anchor, related or set aside) to cut the volume of verse reading | The volume of verses to read | S/P | Reconstruction 01 |
| 9 | 30 Mar | 42 gaps found in the instruction register in one day: "the gap between decisions made and instructions updated is where pipeline failures live" | Drift between decisions and instructions | P | Reconstruction 02 |
| 10 | 5 to 8 Apr | Verse Context complete for 181 registries, 3,469 groups; a bulk delete wrongly removed the heart's anchor term | Bulk clean-up hit a term whose own note said keep | P | Reconstruction 02 |
| 11 | 6 Apr | Dimension review: 40% of groups unclassified, keyword matching unreliable | Broad keyword matches | S | Reconstruction 02 |
| 12 | **8 Apr** | **Grouping corrected from term-centric to characteristic-perspective: groups must say what the verse is about, not what the term does** | Groups described the term, not the verse | S | Reconstruction 02 |
| 13 | 9 Apr | A patch corrupted the wrong IDs and the database was restored from backup | A sequential-ID assumption broke after a version bump | P | Reconstruction 02 |
| 14 | 14 to 17 Apr | Flag tables put under governance (six directives); Session B's Step 1.2 rewritten; the Fellowship Stage 2a run failed on nine defects | Discretionary instruction language let the session decide otherwise; the rule adopted: remove discretion, make every step mechanical | P | Reconstruction 02 |
| 15 | 19 Apr | A join bug found to have inflated findings by 48% (14,284 to 7,411); vocabularies moved into the database as the single source | Pointing at a deprecated duplicate | P | Reconstruction 02 |
| 16 | 28 to 29 Apr | The tier framework revised: soul as seat of faculties, heart and mind as subsets | A conceptual revision | S | Reconstruction 02 |

### 1.2 May to mid-June 2026: clusters, the verse-read, the database loss

| # | Date | Event | Trigger or finding | S/P | Source |
|---|---|---|---|---|---|
| 17 | **4 May** | **Three things dropped at once: the registry as the grouping driver, dimension review, and verse groups as a clustering input; replaced by term-similarity clustering into 45 M-clusters** | Registry dominance only 50.6%; dimensions "created noise, built on wrong assumptions" | S | Reconstruction 01, 02 |
| 18 | 9 May | Preference recorded for the smallest atomic chunks, run in chat, while the method is not settled | A $0.50 big-picture API run produced nothing; M26 attempts cost $5.66 | P | Memory `small_chunks_over_elaborate_pipelines` |
| 19 | 17 May | **Scope-bias correction: inner being means the whole human inner life, no spiritualisation filter; "boundary-pending" ruled an invalid resolution; co-occurrence across clusters to be checked before routing** | M04 had 322 boundary verses; prompts had all been God-directed | S | Reconstruction 02 |
| 20 | 18 May | The characteristic model added: cluster, characteristic, sub-group, verse group, verse | The cluster level alone did not carry the characteristic | S | Reconstruction 01 |
| 21 | **26 May** | **M11 parked: a characteristic's "legs" are scattered across clusters; the open question whether the inner being is too integrated to force into structures** | Term-similarity clustering is not characteristic neighbourhoods | S | Reconstruction 02 |
| 22 | 27 May | v3_0 pipeline: 14 phases to 6; Session C retired (it re-read the verse corpus seven times); two governing principles: verse meaning rules all analytics, record every observation | Cost and rework | P/S | Reconstruction 01, 02 |
| 23 | 29 May | The first full v3_0 cluster (M38): prose sentence-by-sentence, 177 hygiene items | A functional but unfinished pipeline | P | Reconstruction 02 |
| 24 | **3 Jun** | **The live database truncated to 0 bytes (cloud-sync corruption); recovery to a copy six weeks old; the project moved off the cloud drive to NAS and git** | Handler-based work was not replayable | P | Reconstruction 01, 02 |
| 25 | 4 Jun | The "remediation, audit to zero" frame declared the wrong frame; the study re-grounded: verse meaning rules all analytics, every finding anchored | A frame that audited without a purpose | S/P | Reconstruction 01 |
| 26 | 7 Jun | The manual verse-group and sub-group iteration abandoned (about 40 days per cluster) for an L1 to L8 rollup | Cascading rework | P | Reconstruction 02 |
| 27 | 8 to 9 Jun | "Verse-read = meaning" goes live: each verse read once, about 14 findings per term; clusters M01 and M15 complete | The need to read verses once and accumulate | S/P | Reconstruction 01 |
| 28 | **10 to 11 Jun** | **Root cause of the four-month rework loop found: the meaning paragraph duplicated the 14 dimensions and then fabricated, and the audit checked only field to paragraph; the fix: dimensions primary, meaning derived and unable to invent; legacy findings with templated counts removed; faculty induced per cluster removed** | One tool defect behind months of rework | B | Reconstruction 02 |
| 29 | 10 Jun | The M47 "Constitution" cluster created for the seats and faculties (heart, soul, spirit, mind, flesh, conscience) | A single mechanical sense is meaningless for these words | S | Reconstruction 01 |
| 30 | 14 Jun | The project reconstructed from its own written record for the first time; summaries had drifted from reality; governance layers (filing, git, backups, scripts) found omitted from the first pass | Drift between summaries and the live state | P | Reconstruction 01, 02 |

### 1.3 Mid-June to mid-July 2026: the reset, the sense grain, the book re-reads

| # | Date | Event | Trigger or finding | S/P | Source |
|---|---|---|---|---|---|
| 31 | 19 to 23 Jun | M10 (sin) analysed in logical units; the cluster found to be largely not characteristics but object-kinds; "giving is not a characteristic; it is the expression of one" | The characteristic frame visibly did not fit | S | Reset baseline document, section 2 |
| 32 | **24 Jun** | **Cold-read validation: about 70 to 85% of the analytical claims imported meaning the verses do not carry; "faculty" and "type" were lemma constants relabelled as per-verse discoveries** | Validating against the lexical | S | Reset baseline; memory `superstructure_eisegesis_validation` |
| 33 | **25 Jun** | **The reset: the aim to identify, name and describe individual characteristics is set aside for movements, associations, interlocking and emergence; the inner being modelled as a process and relational web; rules for the lexical reset (functional first; measurement informs and never decides; a movement of one is a movement)** | The superstructure was eisegesis; the object of study changed, not only its organising key | S | Reset baseline; lexical rules reset; synthesis-B spec |
| 34 | **26 Jun** | **Valence, origin and faculty overlays quarantined or reversed; the rule: the lexical captures only what the verse says; the verse-meaning foundation found to reach about 9% of spans, the earlier completeness "largely illusory"** | A fan-out index over the verse spans | B | Session log 2026-06-26 |
| 35 | 27 Jun | The verse fan-out operating model; a questions-first method; scripture as the data source | Rebuilding on verse evidence | S | Methodology documents of 26 to 28 Jun |
| 36 | 1 to 2 Jul | A verse-first VE-lexical catalogue becomes the authority; 14 dimensions validated; span completeness pre-pass | Rebuilding the lexical item list | S | Methodology documents of 1 to 2 Jul |
| 37 | **2 Jul** | **"A term is a sense (a span), not a lemma": `abad` (H5647) pulled 261 verses of worship, ministry, labour and enslavement together** | The ruthlessness passages carried one sense of a four-sense lemma | S | Methodology, term-is-sense issue |
| 38 | 3 to 4 Jul | The earlier verse-analysis state declared defunct | Replaced by the new model | P | Archive `verse-analysis-state-20260704` |
| 39 | **6 to 7 Jul** | **Completeness for Psalms and Proverbs reported complete and correct; the researcher rejected it: the check was near-circular, matched on base Strong's and leaned on unverified heuristics; a reset of the working method followed** | The records were created and then checked for existence | P | Session log 2026-07-06/07 |
| 40 | **8 Jul** | **The authoritative cycle: characteristic, candidate, role, lexical; it supersedes the qualifier-as-a-role framing, the per-span role reassessment and the Strong's-list and 277-table candidate attempts** | Several earlier attempts at the same sub-process | S | Authoritative cycle document |
| 41 | 10 to 14 Jul | Psalms (150 of 150) and Proverbs (59 cycles) read to the new standard, one passage at a time with checks each cycle | The new cycle proven on two books | P | Session logs 2026-07-11, 14 |
| 42 | **14 Jul** | **The Proverbs audit found the read passage-complete but not verse-complete: 116 of 915 verses had no passage and were never read; the "100%" corrected; the qualifier reconsidered as a typed relationship (analogy, causation, condition, comparison) after analogy was found structurally lost** | A scored audit (G0 to G10); the researcher's remark that qualifiers were underestimated | B | Session log 2026-07-14; qualifier reconsideration |

### 1.4 July to September 2026: the IBA app, the debate, the clusters in the app

| # | Date | Event | Trigger or finding | S/P | Source |
|---|---|---|---|---|---|
| 43 | **17 Jul** | **The IBA app begun as a complete rebuild of the database and its dependencies, config-driven** | Process control had never been consolidated | P | BUILD 1 to 4; `CHARTER.md` |
| 44 | 22 to 23 Jul | Config governance and the escalation workflow; the candidate system retracted pending a replacement | Orphan configs; a candidate system load-bearing but unproven | P | BUILD 13, 14; session logs |
| 45 | **24 Jul** | **A classifier of inner-being relevance by the term's own meaning built and concluded: word-level classification hits a hard ceiling; the next phase should analyse spans directly** | Testing the limit of pre-classification | S | BUILD 15 |
| 46 | 25 to 26 Jul | The span model corrected (combined-code tags); the lexicon parse layer; the meaning-tree defect; the passage system retired | A tag carried several codes; a base-collapse bug | S/P | BUILD 16 to 26 |
| 47 | 27 to 30 Jul | The passage debate method baked into the app (Daniel), then run for Jonah, Joel, Obadiah, Hosea, Micah; the book narrative generated by API | A per-passage reading with the beings in each verse | S/P | BUILD 27 to 54 |
| 48 | 29 to 30 Jul | Config-system remediation and a recorded non-compliance; a doc-archaeology rule | Past precedent reconstructed in place of live config | P | BUILD 37 to 53 |
| 49 | **2 Aug** | **The Amos debate drifted to general textual phenomena, "trying to arrive at some sort of story", enabled by three chapters to a file; a three-phase method: phenomena per verse first, operations second, validation third** | A wider file scope removed a natural boundary | B | Session log 2026-08-02 |
| 50 | **3 Aug** | **Training on beings: a six-type typology for human beings and a two-layer method (mark what the text decides, resolve the open referents separately); the same day the verse-reading technique v3 was tested on Jonah 3 and the researcher judged it failed: "the central unresolved problem since the study started, seven months in"** | A specification cannot be made specific enough for consistency at scale | B | Session logs 2026-08-03 |
| 51 | 5 Aug | `verse_lexical` as a mechanical engine (T1 to T3) replacing the verse-span-meaning report; the HIB, phenomenon and operation schema; passages redefined on HIB continuity | The layering lesson turned into a mechanism | S/P | BUILD 56 to 66 |
| 52 | 10 Aug | The `receive` build rolled back: 79% of its occurrences came from nine basic verbs matched through a buried sense; relevance "has always been a human curation step" | STEP's discovery was never checked against inner-being relevance | S/P | BUILD 99 |
| 53 | 11 to 13 Aug | The cluster model adopted into the app; allocation by an LLM; a keyword crossmatch rejected for allocation grounded in verse-context analysis | The researcher's correction of 13 Aug | S | BUILD 103 to 111 |
| 54 | **15 Aug** | **`CHARTER.md`: the app is the single driver; the history of 69 session logs, 113 BUILD sections and 43 GOVERNANCE sections "never once added up to a single statement of what the whole was for"** | The same drift the reconstruction found in June | P | `CHARTER.md` |
| 55 | 16 to 21 Aug | The escalation system reset and rebuilt after a cutover rolled back; `wa_rule_registry` retired; the content index cleared when `iba.db` reached 8.06 GB | Redesign after a failed cutover | P | BUILD 113, 137, 152 to 167 |
| 56 | 22 to 26 Aug | The resolution_kind axis (a decision goes to the researcher; a slip against a settled design is corrected); the module-blocking gate disabled | Routing around the gate had become the normal response | P | BUILD 172, 177 |
| 57 | 31 Aug | Developer Mode and App Mode defined as a property of the session, chosen by the researcher: "you should not be allowed to swap between developer mode and standard mode on the fly" | A session spent routing ordinary fixes through the per-row approval gate | P | `CHARTER.md` section 4 |
| 58 | 4 to 6 Sep | Strong's classification moved from a config table to the cluster tables; T5 to T9 clusters; the M-cluster taxonomy rebuilt from 47 to 85 with hundreds of duplicate tags ruled on | Multi-tagged codes; clusters naming different concepts than in May | S | BUILD 228 to 248 |
| 59 | **10 Sep** | **The three parse tables retired: all 194 occurrences of G3551 read in context gave at least six senses, one in no dictionary entry; "the entire approach and method to arrive at meaningful meaning will be revised"** | A hand-read of one lemma at scale | S | BUILD 262 |
| 60 | 15 to 18 Sep | The full lexical-stack rebuild (Layer 1); the five-stage cluster-reading pipeline built and run on cluster M67 | Rebuilding the data layer then reading on it | S/P | BUILD 267 to 298 |
| 61 | **17 Sep** | **"Gloss is a strong-level entity" (the cluster gloss column dropped); reading must be progressive and relational: 2 Cor 7:11 gave 21 observations about one of seven words** | The researcher took one verse apart by hand | S | BUILD 277, 280 |
| 62 | 20 to 24 Sep | The observation enhancer; stage 1 tuned (tags, windows, span-grounding enforced); `bible_research.db` retired to prose-only with 4.9 million rows cleared; `session.close` built | Governance of the reading pipeline | P | BUILD 299 to 331 |
| 63 | 21 Jul, with its consequences in the audits of Aug to Oct (placed here out of date order) | Every validator in the app found to check structure only and none to check value quality | A parser bug in the most-read field, two enums no code enforced, dirty labels behind "valid" tables | P | Memory `structural_validation_is_not_value_quality`; BUILD 221, 304 |

### 1.5 October 2026: control reform, threads, the reading process

| # | Date | Event | Trigger or finding | S/P | Source |
|---|---|---|---|---|---|
| 64 | 4 Oct | The narrative copied to the learning4comfort inbox; direct GitHub publishing refused | A never-committed publishing workflow retired | P | BUILD 335 |
| 65 | 12 to 22 Oct | The open-threads register (OT-nn); the narrative claim register in the database; the chapter table as the authority | Open items and claims living outside the database (inference) | P | BUILD 336 to 351, 384 |
| 66 | **20 to 22 Oct** | **The control reform: start and close rebuilt, the control map, `CLAUDE.md` and memory cut to pointers, replaced history moved out of the read path, every script not in a utility retired, rules delivered at the point of use** | Rules, documents and memory each held their own version of the rules (inference from the entries; the researcher's own words are on #2177) | P | BUILD 353 to 375 |
| 67 | 22 to 24 Oct | The strand reading, then `Reading.ps1` with three gates; the strand steps retired; the reading method held as config (#2268) | A gated path from scope to narrative | S/P | BUILD 386, 398, 406 to 408 |
| 68 | 25 to 30 Oct | Surface subgroups within clusters; the capture of prior documents (19,112 lines into 6,709 observations); Analysis_phase_1 (522 observations) | Folding prior study into the observation record | S | BUILD 409 to 435 |
| 69 | **28 Oct** | **The surface shown for a code in a multi-code span was the span's word, not STEP's ("still", not "alive")** | The researcher: "I have noticed that you regularly have the wrong surface for multi-span items" | S | BUILD 428 |
| 70 | 31 Oct to 1 Nov | Local-model pilots; the concept grouping (domains as chapters, concepts as sub-chapters) built as tables | A local model grouped 190 of 200 surfaces into one group | S | BUILD 436 to 442 |

### 1.6 November 2026: surfaces, collections, the layered reading

| # | Date | Event | Trigger or finding | S/P | Source |
|---|---|---|---|---|---|
| 71 | **2 to 4 Nov** | **Surface judging: the first design judged each (code, surface) pair and judged the code's gloss, not the English; the researcher: "why are you not using the list of surfaces and apply the test to it"; a per-surface judgement into behaviour, state, entity or other** | A pilot of seven surfaces | S | BUILD 446, 447 |
| 72 | 3 to 4 Nov | How the Ollama server is reached held in config; long jobs started outside the Claude session | Services and jobs depended on the session | P | BUILD 450 to 453; rule B:124, B:125 |
| 73 | 6 Nov | The surface cycle in five modules over tables; files demoted to working files | A prototype run by scripts and files | S/P | BUILD 455 to 466 |
| 74 | 7 Nov | The group of things that exist renamed `entity`; multi-term units kept visible in `verse_lexical` | "The use of the term being is confusing"; the meaning of a unit confused with one code's surface | S | BUILD 468, 469 |
| 75 | 9 to 11 Nov | Engagement: what each surface does for the inner being per verse; running it on all collections withdrawn and folded into the study of each collection; the evidence report | The collection as the unit of study | S | BUILD 475 to 484; #2412 |
| 76 | **12 to 13 Nov** | **The collections rebuilt in batches and verified by lists; the phrase rule retired; the collection placed on every node; clusters retired from nodes and observations** | One surface in one collection; cluster and subgroup history | S | BUILD 497 to 527 |
| 77 | 14 to 15 Nov | The layered reading built: stages, a ledger, boundaries between lexical and inner-being work | The researcher's definition of the layers | S/P | BUILD 528 to 531 |
| 78 | **15 Nov** | **The first run of stage 1 on `thought` removed: it passed every structural check and restated the dictionary sense, against the observation rules ("I guess you never looked at the observation rules"); the recorders audited; "not confirmed as first built"** | The researcher read the observations | P | BUILD 534 to 538 |
| 79 | **15 Nov** | **The grouping of `thought` by dictionary meaning declared a failure: it "changed the meaning of the underlying words"; "you have not even considered what the groups are being used for"** | The researcher read the groups | B | #2509 v6, v7 |
| 80 | 15 Nov | Rule 135: a column added to an existing data table is registered and made in one unit of work | A migration gap | P | BUILD 532 |
| 81 | 19 Nov | The programme prose found to describe a method no longer in use; the project map and this history begun (#2510) | The researcher: the previous session showed no grip on how the project is put together | P | #2510 |

Events 4, 8, 12, 17, 21, 32, 33, 37, 45, 50, 59, 61, 69, 71 and 79 are the ones that moved the subject; events 5, 9, 14, 24, 28, 34, 39, 42, 54, 57, 63, 66 and 78 are the ones that moved the process.

### 1.7 Changeovers the first pass missed

The first review began in July. The record before it adds these changeovers, none of which was in the earlier list: the word-by-word programme and its retirement (events 3 to 27); the term-centric to characteristic-perspective grouping of 8 April (12); the spiritualisation-bias correction of 17 May (19); the scattered legs of a characteristic (21); the cold-read finding that most of the superstructure was eisegesis (32); **the reset of 25 June, which set the study's central aim aside** (33); the coverage failure of 26 June (34); the sense, not the lemma (37); the circular completeness claim (39); the authoritative cycle of 8 July and the book re-reads (40, 41); and the passage-complete-not-verse-complete gap (42).

## 2. Stream A: the subject matter. Findings and progressive learning

### 2.1 The learning path

| Stage | What the study believed or did | What was found | What the stage added | The gap it left |
|---|---|---|---|---|
| A1 Feb to Apr | The inner being is a set of characteristics found in the soul and spirit words; collect the words (Framework B, then the registry), read each word's verses | The list was an order of magnitude short; the discovery of terms by English text missed words the ESV never renders as the English (H2734) | A bounded, flagged scope; the STEP discovery of related terms; a first classification of verses per term | Registry and STEP discovery gave candidates, not relevance |
| A2 Apr | Group a term's verses by what the term does | The groups described the term, not the verse (8 Apr) | **Grouping by what the verse is about: the first context-driven step** | Dimensions gave 40% unclassified; the grouping stayed per term |
| A3 May | Cluster terms by similarity (M-clusters); add the characteristic below the cluster | The registry and dimensions miscut the data; a spiritualisation bias had narrowed the inner being to the God-directed; a characteristic's legs scatter across clusters; the whole subject may be too integrated to force into structures | The whole inner life as scope; clusters as a working grouping | Clusters hold terms, not characteristics; the integration question left open |
| A4 Jun 8 to 11 | Read each verse once and derive about 14 findings per term | A tool defect (meaning duplicating then fabricating) explained four months of rework | Dimensions primary, meaning derived | The grain was still the term in a cluster |
| A5 Jun 19 to 26 | Read clusters as sets of named characteristics, object-kinds and faculties | The sin cluster was object-kinds; "giving is the expression of a characteristic"; most of the superstructure was eisegesis; faculty and type were lemma constants; the foundation reached 9% of spans | **The lexical captures only what the verse says; characteristics are not given by the lemma** | The aim itself (name the characteristics) put in doubt |
| A6 Jun 25 | The reset: study movements and a relational web, not named characteristics | The inner being does not decompose into clean parts; meaning lives on the edges | **Movement and edge as the unit of synthesis; measurement informs and never decides** | The pull back to characteristics three weeks later suggests this alone did not answer "what is a characteristic" |
| A7 Jul 2 to 14 | A term is a sense; the characteristic is a typed term in its verse; the cycle characteristic, candidate, role, lexical; qualifiers as typed relationships | A lemma pulls many senses; analogy, causation, condition and comparison were lost as standalone qualifiers | **Sense as the owner; the occurrence as the unit; the qualifier a typed relationship** | The cycle was proven on two books by hand; it had not been made repeatable by mechanism |
| A8 Jul 24 to Aug 7 | Judge relevance by the word; read verses for the beings in them; debate each passage | Word-level relevance has an accuracy ceiling; the debate drifts to a story; one instruction cannot be made specific enough | **Layering: what the text decides before what judgement decides; the mechanical `verse_lexical`** | The method stayed per passage and per book |
| A9 Aug 10 to Sep | Discover terms from STEP by English word; allocate Strong's codes to clusters | Discovery pulls basic verbs by buried senses (`receive`); keyword allocation rejected; multi-tag duplicates; mechanical meaning-distillation cannot capture context (G3551); reading in isolation misses the relation (2 Cor 7:11) | **The meaning is decided by the occurrence in its verse, read in relation to the other words of the verse** | The cluster remained a Strong's-level tag showing one face of a word |
| A10 Oct 22 to Nov 7 | Read by strand and subgroup; map surfaces inside clusters; judge surfaces | The surface shown could be the span's word; a pair judged the code's gloss; one term's meaning confused with a multi-term unit | **The English surface as the reader meets it is the unit; the Strong's code the lens on it** | The universe of surfaces was bounded by the cluster allocation of codes |
| A11 Nov | Collections of like surfaces; the layered reading; lexical and inner-being kept apart | A stage 1 that restated the dictionary; a grouping that changed the meaning of the words | **The collection as the unit that has its verses and tells a story; lexical meaning separate from inner-being meaning** | Stage 4 (what is a characteristic) not built; the purpose of the surface groups not settled |

### 2.2 The findings of the stream

1. **Context decides.** Meaning, relevance and role are decided by the occurrence in its verse, read with the other words of the verse (8 Apr; 24 Jun; 2 Jul; 10 and 17 Sep). Neither the dictionary entry, nor the lemma, nor the tag, nor the cluster can decide it.
2. **The grain keeps moving toward the occurrence.** The wrong grain was the registry word, the dimension, the term-similarity cluster, the faculty, the lemma and the Strong's code; the working grain is the surface in its verse.
3. **Completeness and preselection conflict, and every attempt to preselect failed.** The 28 characteristics, the registry, the STEP candidates, the clusters, the classifier and the surface groups each preselected and each left a gap. The only mechanisms that exposed gaps were comparisons against an independent source (the primary lexica, the lemma inventory) and a human reading of one case.
4. **The subject is integrated.** Boundaries do not hold (26 May; 25 Jun); a characteristic's legs scatter across clusters; some words are behavioural only in combination. The study has answered this by relations (movements, qualifiers as typed relationships, pairings) and not by parts.
5. **Separate what the text decides from what judgement decides.** Layering worked in August and again in November.
6. **A characteristic is not given in advance: it is read from the verse.** The 25 June reset set it aside; the 8 July cycle brought it back as a typed term in its verse; the November design collates characteristics on surfaces. The question "what is and is not a characteristic" is the one question that has not yet been answered in a way that has held.

### 2.3 What stands unsolved in this stream

- Stage 4 of the collection reading (the inner-being analysis, where the characteristic is established) is not built.
- The surface groups are again a word-level gate. The data shows a third of the node rows on `inner_being_state` words with no inner-being role in their verse, and 563 distinct `other` words read as characteristic or qualifier somewhere; these roles were written under earlier methods, so the sign is indicative (inference).
- The judged universe is 6,225 of 18,254 surfaces. The 12,099 outside it hold 204,620 of 544,609 occurrence rows (37.6%), all on codes allocated only to T-clusters. These enter only as qualifiers of verses of member surfaces.
- No collection has completed a stage, so the layered design has not met the 3 August test (consistency at scale).
- The purpose of the surface groups in stages 3 and 4 is not written down.

## 3. Stream B: the process. Findings and progressive learning

### 3.1 The learning path

| Stage | What the process was | What failed or was found | What the stage added | The gap it left |
|---|---|---|---|---|
| B1 Mar | Instruction documents executed by Claude sessions, with the AI as a quality gate | The AI fabricated numbers, drifted formats, claimed compliance falsely; a reset deleted researcher flags; schemas and instructions drifted (42 gaps) | STEP as master; backups; dry-run then apply | Discretion in instructions |
| B2 Apr | Instruction language left choices to the session | The Fellowship run failed on nine defects: "the instruction said something else in each case, the session decided otherwise" | **Remove discretion; every step mechanical** | Mechanical steps still checked by the same author |
| B3 May to Jun | A fourteen-phase pipeline; API runs for classification | Costs with no output; Session C re-read the corpus seven times; the database lost on 3 June; handler-based work not replayable | Smaller chunks; six phases; backups to NAS and git; all work replayable in the database | The audit design |
| B4 Jun 11 | An audit that checked field to paragraph | It enforced duplication and left fabricated prose unaudited; "review by statistics is dangerous" | **An audit must check the direction that can fail** | Verification was still by the author |
| B5 Jun 14 | Summaries and memory as the guide | They had drifted from the live state; the reconstruction itself omitted governance layers | Manifest-first reading; a reconstruction from the record | No single surface for what is current and what is superseded |
| B6 Jun 26 to Jul 14 | Completeness claimed by counting what was created | The foundation reached 9% of spans; the check created the records and then checked they exist; 116 of 915 verses were never read | **Completeness measured against an independent source, at the unit that matters (the verse)**; scored gates G0 to G10; snapshots each cycle | Gates written for one book at a time |
| B7 Jul 17 to Aug | A rebuild as an app: config rows for rules, registered steps, a dispatcher, escalations | Rules in documents; past precedent reconstructed in place of config; a gate routed around (disabled 26 Aug); a session routing fixes through approval (31 Aug) | **Rules are config rows; a decision goes to the researcher and a slip against a settled design is corrected; mode is the researcher's choice** | The app's validators checked structure |
| B8 Jul 21 to Oct | The app's validators passed | None checked value quality: a parser bug sat in the most read field; unenforced config; hand-rolled checks | Value-quality checks; `context_delivered` and enforcement status; the Oct 20 to 22 reform: CLAUDE.md and memory as pointers, one home for each kind of control, rules delivered at the point of use, compliance restated at start, close checks | Rules delivered did not guarantee rules built into the recorders |
| B9 Sep | A pipeline of many fixes | Stage 1 needed about thirty BUILD entries of fixes between 18 and 23 Sep (BUILD 299 to 327); a compliance self-audit found five gaps; relevance cost reading volume (36% of observations carry no finding) | Batch resume, progress, tag definitions, span-grounding | Effort went into the pipeline rather than the question |
| B10 Oct to Nov | Reading gates; an open-item register; local model pilots; services configured | A local model's grouping was unusable; long jobs ended with the session; unindexed scans; questions put that the record answers; a breach of a recorded sequence | Long jobs outside the session; service access in config; query plans checked first; the record as the memory | Claude's own repeated failures keep surfacing at the point of work |
| B11 Nov 15 | Stage 1 and the grouping built to design and checked structurally | Both passed the checks and both were wrong; the rules existed and the recorder did not enforce them; the groups were made without settling what they serve | Audit of the recorders against the rules; a boundary check for stages | The check that would have caught it is a content read by the researcher |

### 3.2 The findings of the stream

1. **A rule that is not built into the mechanism is not a rule.** The same failure at 15 March (the AI claimed compliance), 17 April (discretion), 7 July (a circular check), 21 July (structure-only validators) and 15 November (rules existed, the recorder did not enforce them).
2. **Verification must be independent of the maker and measured at the unit that matters.** A check that creates what it checks, or checks existence and not content, proves nothing.
3. **The only reliable detector of a content gap has been the researcher reading one case by hand.** The app's checks passed in the cases of 2 Cor 7:11, `receive`, Jonah 3, Gen 43:27, G3551, the stage 1 run and the `thought` groups.
4. **Drift between decision and artefact is a standing hazard**, named on 30 March, 14 June and 15 August and answered each time by consolidating the home of each kind of content. The control map and the point-of-use rules are the latest answer.
5. **Infrastructure is existential.** The loss of 3 June cost six weeks and was unrecoverable because the work was not replayable; it is why the work lives in the database.
6. **Elaborate pipelines built before the method is known are paid for twice.** The record states it on 9 May and shows it again in September and November.
7. **Claude's own recurring failures are a process finding in their own right:** over-reach, copying a prior unreviewed pass, overclaiming completeness, building ahead of a decision (B:105), putting questions the record answers. They are recorded in the session logs and the rules answer them; they have not stopped.

### 3.3 What stands unsolved in this stream

- A content-level check before a stage closes does not exist; the structural checks pass while the content is wrong.
- No independent completeness control now operates on the study's universe: the registry's lexica comparison, the lemma inventory and the candidate net were each built and retired.
- The recorders were not audited against the rules before the November runs; the audit was done after the failure.
- The consistency test of 3 August has not been run against the layered design.

## 4. How the streams interact

- **Subject findings invalidated the process built on the earlier view.** The reset (25 Jun) and the sense grain (2 Jul) made the earlier readings and the per-word pipeline obsolete; the move to surfaces and collections retired the cluster pipeline and the strand and concept work. Each time the process had to be rebuilt, which is why the history shows so many rebuilds.
- **Process failures hid subject truths.** The meaning-duplicates-then-fabricates loop and the circular completeness checks stood between the study and what the verses say for months.
- **The same remedy fits both streams: make the context and the check explicit and independent of the maker.** Reading the occurrence in its verse (subject) and verifying by an independent comparison at the unit that matters (process) are two forms of one discipline.
- **A critical reading of where this leaves the present design** (inference unless stated): the split of the problem relocates the circularity of "what is a characteristic" to stage 4; the surface groups are again a word-level relevance gate, the approach that hit a ceiling on 24 July; the universe of surfaces is bounded by a Strong's-level allocation, which the surface premise rejects; the definition of the inner being already said that context decides (weeping qualifies, walking does not), so the repeated failures may be one failure, a test meant for occurrences applied to words; and the design is untested at the point where earlier designs failed.

## 5. Gaps, and a proposed way to close each (for discussion; none is built or decided)

| Gap | Stream | Evidence | A way to close it |
|---|---|---|---|
| G1 Stage 4, the inner-being analysis | A | Not built (B:132); the circularity lives here | A design for how a characteristic is established from stage 3 observations, taken to the researcher first |
| G2 The universe boundary | A | 37.6% of occurrence rows outside, by Strong's code | Read a sample of T-only surfaces in their verses; the researcher decides whether the boundary stays or widens |
| G3 A word-level gate | A | Section 2.3; event 45 | Test the groups against occurrence evidence for a sample of `inner_being_state` and `other` surfaces before stage 1 runs on further collections |
| G4 The purpose of the surface groups | A | Event 79; two statements in the record | The researcher states what stages 3 and 4 take from the groups; the method follows |
| G5 No independent completeness control | B | Section 3.3 | Re-establish a check against an independent source (the lexicon, the full surface list) |
| G6 No content-level check | B | Events 63, 78, 79 | A read sample of each stage's output by the researcher before the stage closes |
| G7 Consistency at scale untested | A/B | Event 50; no collection through a stage | Take one collection through stages 1 to 3 as the pilot and judge it on the 3 August criterion |
| G8 Recorders not audited against rules before use | B | Event 78 | Audit each recorder against its rules before a stage runs |
| G9 The narrative's structure against the collections | A | Map section 8 | Decision on #2486 |

Everything in sections 2.3, 3.3 and 5 is for the researcher to accept, correct or reject. None of it changes any rule, table or document.
