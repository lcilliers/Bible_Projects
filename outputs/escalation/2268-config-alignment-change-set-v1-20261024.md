# #2268 Config alignment change set (v1): every row assessed against the rulings

**Date:** 2026-10-24 · **Escalation:** #2268 · **Status:** the assessment and the changes, ready to apply. Nothing has been changed yet.

Researcher, chat 2026-10-24 (verbatim): *"rulings-review-v4 is answered and can now be incorporated in the planning. next is to assess and adjust all the configs and rules to align with it."*

**Base documents:**
- the plan: `outputs/escalation/2268-analytic-process-and-reading-plan-v2-20261024.md`, with principles P-1 to P-5, phases, observation record §3, gaps §4, and RO1 to RO12;
- the inventory: `outputs/escalation/2268-analytic-process-config-inventory-v4-20261024.md`.

**Actions:**
- **Keep:** the row stands as it is.
- **Correct:** a fact in the row is wrong.
- **Reword:** the substance stands, and the wording moves to the phases.
- **Replace:** the row's content moves into new rows, and the row is retired.
- **Retire:** the row is set inactive, and its history stays.
- **New:** a row to add.

**How the changes are applied.**
- Every `cfg_*` write goes through `apply_logged` (B:75), tested first on a copy made with `dbsnapshot.copy_db` (B:97), with the result recorded on #2268.
- Code changes are separate build tasks (§9): this file changes config only.
- **Method rules reach a tool through their step:** the hook delivers the method rules of a PS tool's work-package steps (`.claude/hooks/rules_at_point_of_use.py` lines 133 to 141). The new reading rules are therefore method rules on the `reading.*` steps, and they reach `Reading.ps1` at first use with no new mechanism. Quality checks have no delivery yet (§9 B11).

## 1. Summary

| Kind | Keep | Correct | Reword | Replace | Retire | New |
|---|---|---|---|---|---|---|
| Behaviour and escalation rules (57 placed) | 26 | 6 | 15 | 9 | 1 | – |
| Settings | the rows not named in §3 | 4 named | 7 named | 1 named | 4 named, plus the `lexical.llm_*` family | 3 |
| Enums | the rest | – | 2 | – | 2 | 3 |
| Method rules (121) | the 0.B rules | – | carried rules named in §5 by source | – | the rows named in §5 | 47 new keys (§5) |
| Passage quality checks (18) | – | – | 9 carried | – | 9 | 12 new (§6) |
| Control map rows | – | – | 3 | – | – | – |
| Column and table texts | – | 7 | 1 | – | – | 3 |

Behaviour rules are counted per row. The other kinds are listed row by row in their sections.

## 2. Behaviour and escalation rules

| Rule | Action | Why | New text, or where its content goes |
|---|---|---|---|
| B:2, B:4, B:19, B:21, B:24, B:34, B:36, B:40, B:61, B:66, B:76, B:78, B:80, B:83, B:107, B:111, B:112, B:113, B:115, B:52, B:53, B:55, E:4, E:5, E:16, E:18 | Keep | fit the phases as worded | – |
| B:7, B:8, B:9 | Correct `enforced_by` | the call site it names (`narrative.generate`) is retired, and no study step calls the API after R3c | "No live call site after #2268 R3c; applies to any future API call." |
| B:13 | Correct | C12, R8 | "…bible_research.db (prose only: the programme and glossary prose) and iba.db (process control, base data and all analysis tables)…" |
| B:67 | Correct `enforced_by` | it names retired memory files | "Delivered at session start (rule 81) and at first use of sqlite (cfg_rule_scope)." |
| B:77 | Correct `enforced_by` | it names the retired `-Action Record` and a one-off script | "Checked at the reading's claim step (0.GAP post gap types: claim on verses only; verse cited with nothing behind it)." |
| B:37 | Reword | R1 | "New analytical work is derived from the config rows that govern it, never from a prior run's unreviewed output used as a template." |
| B:69 | Reword | W14, R4 | "Observation, claim and narrative text states what a cited verse or passage says, and may set related verses side by side. It never joins verses into a pattern, mechanism or 'what this shows' that no verse states, and never uses an uncounted most/often/always. A new insight found while writing goes to an observation first. A researcher 'not in the way you portrayed it' means withdraw the portrayal. When in doubt: quote, and stop." |
| B:70 | Reword | W15 | "…A reading that finds a word associated with another cluster records that association in an observation (the term's cluster relation), for cross-cluster analysis. It never proposes … a re-tag of a single word…" (the rest as now) |
| B:71 | Reword | W8, P-3 | "Before any query for a reading, use what is already gathered: the scope's collation (0.GAP pre) first. The verse to M-code link is verse_lexical.strong joined to cluster_strong (cluster_code LIKE 'M%', deleted=0), read with ONE set-based query over the verse set, never per verse. Results already recorded (observations, claims, faces) are gathered, not re-derived. A query that does not return within seconds means the approach is wrong: stop and re-plan." |
| B:72 | Reword | W13, R4 | "The study's primary focus is the human inner being (HIB). Each verse read is routed by what it shows, and the route is recorded in its observation: (A) another being in its own right, routed to Ch 13 (13.1 Divine, 13.2 Angels, 13.3 Other spirits, 13.4 Nature); (B) another being interacting with the HIB, fully in HIB scope; (C) no inner-being and no other-being bearing: assessed and recorded as data, not in the narrative. A verse may take A and B." (The last two sentences, on dedicated passes and the researcher's direction for routing, are removed under R4.) |
| B:74 | Reword | W28 | "…A thread is not worked as a task: its items are matched when a reading opens on a scope and settled in the reading's claim step… Before a reading opens, the threads that bear on its scope are matched (Escalation.ps1 -Action Match …); unresolved gaps and gaps needing further work are raised as open items (R13a)…" (the rest of the mechanics as now) |
| B:89 | Reword | R18 | "How the meaning or application of the same word or concept changes in different circumstances is a key discovery and is built upon, never set aside. Every reading records each word's face in its observation, with the circumstance that differs and why (the ledger face and the catalogue's term for it are one concept). A word's meaning is never taken from its cluster tag. Ch 11 §4 ('What changes the character') is the cross-cutting account the faces feed." |
| B:92 | Reword | W22 | "Items are not held unnecessarily: verses or items that bear on the scope are read while the reading is open. A gap unresolved, or needing further work, goes to an open item, not parked behind another step." |
| B:93 | Reword | W6 | "When a scope includes M47 (inner seat) words, its verses are checked for dropped observations by word, not by citation (a narrative citation is verse-level, not word coverage); a dropped one is a 0.GAP pre gap." |
| B:94 | Reword | W5 | "Before a scope is set, the glosses of its theme are scanned across all cluster codes, M and T alike (0.C): words for the theme may sit in T-codes no earlier reading pulled." |
| B:95 | Reword | W4 | "A scope's verse sets come only through the app's raw layer and the scope resolver (Verse-Scope.ps1), never through an inline STEP call." |
| B:109 | Reword | W17 | "A question a verse reading could answer is answered by reading the verses, never passed to the researcher." |
| B:110 | Reword | W7, R13a | "For every term in a verse read, verse_lexical.surface is analysed per Strong's first: the surface shows the different interpretations of the root that the gloss or suffix alone can miss. Surface variants and related terms found are recorded in observations." |
| B:114 | Reword | phases, RO12 | "Study work runs in phases: the scope with its objective (0.C); the gaps recorded for it (0.GAP pre), processed into the tables before the next gate; the verses read in context (D4); then claims finalised and gaps rechecked against them (0.GAP post), and the narrative written. Claims and narrative are done only from the tables, never from memory. A session may break between phases." |
| B:116 | Reword | R14, RO2 | "…Study work starts by reading each verse in its passage, with all its observations already recorded read into focus, and letting it say what it says…" (the rest as now) |
| B:73 | Replace | R1, R12 | the role guide's content becomes the method rules of §5 on the `reading.observe` step |
| B:79 | Replace, then retire | R5 | the tables record where a verse ends up (`observation_disposition`, §4). B:79 stays active only for the October files not yet gathered, and retires when they are |
| B:84 | Replace | R2 | §5 rules RM-01 to RM-04 (web, scope objective, segmentation, gathering) |
| B:85 | Replace | R4 | RN-01: "Programme prose (the DB prose store) is the researcher's, and Claude writes it only on instruction. The narrative is written by Claude from the claims, to the narrative style rows, with no approval before publishing; the researcher reads the published chapters and corrects through Claude." |
| B:86 | Replace | R4, C9 | §5 narrative rules RN-02 and RN-03; governance.narrative_home stays the home |
| B:87 | Replace | R4 | RN-04 (quotes checked; science chapters later; the Spirit and Jesus in 13.1, the human side in Ch 10) |
| B:88 | Replace | R4 | RN-05 (weave, not fit; every reading's claims get a placement; 'does not fit' changes the structure; key characteristics get a Ch 10 sub-chapter) |
| B:90 | Replace | R4 | RN-06 (one account per phenomenon; interpretation required; verses not listed; 'I read') |
| B:91 | Replace | R4, R1 | its reading half becomes RO-guide rules (§5 RG-02); its narration half becomes RN-07 |
| B:68 | Retire | R6 | its lasting point goes into RW-01 (§5) |

## 3. Settings

| Setting | Action | Why | New value |
|---|---|---|---|
| `governance.*` (15 in FRAME) except below; `spine.*`, `raw.*`, `step.*`, `lexicon.*`, `discovery.*`, `registry.*`, `cluster.assign.*`; `verse_scope.*`; `verse_collate.*`; `open_item.*`; `narrative.*` paths; the escalation report paths | Keep | fit | – |
| `governance.scope_iba_db` | Correct | R8 | drop "a few analysis tables (debate/passage control) are expected to migrate back to research_db" |
| `ib_observation.tag_guidance` | Correct | #2263, W19 | add `key-statement`: "a statement of what the verse says about the inner being, with its parts (the October ledger form, gathered work)". `use` becomes "the definition of each tag, given to every reading" |
| `ib_observation.tag_stage_excluded` | Correct `use` | W19 | "per stage, the tags it may not offer" (without "generator") |
| `reading.gap_types` | Reword | R13 | the gap types of plan §4, each with its expectation and its phase: `term_cluster`, `meaning_missing`, `base_missing`, `term_reading_missing`, `read_in_files_only`, `face_not_gathered`, `open_item`, `not_read`, `observation_part_missing`, `observation_unsupported` (D4); `observed_no_claim`, `claim_not_told`, `claim_without_observation`, `citation_without_record` (0.GAP post). The guides say "measured against what is expected; presence of something that is not the right thing is not a resolved gap". `hit_unread` is replaced by `face_not_gathered` |
| `reading.output_dir` | Reword | R7 | `"_analytics/Clusters/{home}/readings"` (the home cluster's folder, named per `report.cluster_folder_naming_convention`) |
| `reading_index.roots` | Reword, with a new exclusion | C27 | new `reading_index.exclude`: `["*/readings/*"]`, so a reading's own files are not indexed as earlier file readings |
| `report.cluster_folder_naming_convention` | Reword | R7 | add: "A reading homed in a cluster keeps its files in that cluster's `readings/<label>/`." |
| `escalation.worked_strand_escalations` | Reword | W29 | key unchanged; `use`: "per cluster, the escalations whose readings worked it (formerly its strand)" |
| `governance.study_status` | Reword when the study re-opens | phases | name the phases instead of "Open, Record, Check, Synergy, Apply, Publish, Account" (after the build of §9) |
| `session_close.reading_scope`, `reading_file_pattern`, `placement_kinds` | Keep, then retire | R5 | stay only while October files remain to be gathered |
| `narrative.inner_being_style_guide_path` | Replace | R4, R1 | the style guide's rules become narrative method rules (RN-*); this setting retires when they are in (§8 W-2) |
| `method.passage_read_guidance_path`, `method.interpretation_questions_path` | Retire | R3 (passage retired), R1 | their live content is carried in §5 |
| `strand_reading.output_dir` | Retire | W21 | the work package is inactive |
| `cluster.recording_similarity_threshold` | Retire | R6 | the API recording pass is retired |
| `ib_observation.meaning_source_aliases` | Retire | R3c | it maps LLM spellings |
| `lexical.llm_*` (9), `lexical.meaning_max_verses_per_batch`, `lexical.relational_max_verses_per_batch`, `report.stage1_coverage_validation_pattern` | Retire | R3c | the API steps are retired |
| `reading.whole_cluster_reading_start` | New | R2 | "A cluster is not read whole by default. A scope on a cluster starts with an overview of its subgroups and the spread of its verses, from which the scope is segmented." |
| `reading.observation_parts` | New | R13a | `["face","role","operation","parties","route","home"]`: the parts every verse observation holds, per M-code in focus and per relevant T-code |
| `glossary.currency_check` | New | R9, P33 | the controlled values whose glossary entries must exist and be current (role, route, face, gap types, dispositions); checked at session start |

## 4. Enums

| Enum | Action | Change |
|---|---|---|
| `ib_observation.stage` | Reword | add `reading` for observations written by a reading from now on. `strand-reading` stays for the gathered ledger rows (R14 B: meanings by stage) |
| `reading_gap_type` | Reword | the values of `reading.gap_types` above |
| `observation_role` | New | characteristic, qualifier, standalone (glossary 1066) |
| `observation_route` | New | A, B, C (B:72) |
| `observation_disposition` | New | told, claim, held, data, context, withdrawn (R5) |
| `word_status`, `party_kind`, `cluster.status` | Keep | `cluster.status` advances only on the retired Stage 1 coverage: see §9 B9 |
| `reading_strand_item_source`, `reading_strand_state` | Retire | the strands are superseded |
| all other enums in the inventory | Keep | |

## 5. Method rules

**Kept on their 0.B steps (15):** 44 to 48 (`lexical.build`), 68 (`raw.verses`), 69 (`lexical.readiness`), 126 (`spine.check`), and 77/118 (`strongs-reassigned-detection`, re-homed to `cluster.assign`). Each stays.

**Retired (64).** Their steps are retired, or they force answers to catalogue questions (R17):
- `lexical.meaning` and `lexical.relational`: 72, 73, 75, 115, 117, 122, 123, 125;
- `cluster.reading`: 100;
- `cluster.answer`: 101, 105, 106, 107;
- the passage method: 13, 17, 19, 24, 25, 28 to 35, 40, 41;
- the rest of the API steps' rules that only restate their batching, model or JSON contract.

**Carried (42).** Restated below onto the new homes:
- **`reading.observe`**: the D4 reading;
- **`word.read`**: D1, in a session;
- **`cluster.read`**: D2, in a session.

`word.read` and `cluster.read` are new steps (§9 B3). Their sources are given in brackets.

**New rules (47).** These carry the role guide (R1, R12), the reading rules RO1 to RO12, the observation record (plan §3) and the narrative (R4).

### 5.1 Reading and scope (step `reading.open` unless marked)

| Key | Rule |
|---|---|
| RM-01 | The inner being is a web of interrelated activity. A reading takes one scope with a clear objective, and the fan-out follows from what it finds. Cluster codes are anchors, not goals. (from B:84) |
| RM-02 | A scope's objective defines the home of what it records (RO10). A verse may come into several scopes from different angles, each adding the observations its objective calls for. |
| RM-03 | A cluster is not read whole by default (`reading.whole_cluster_reading_start`). |
| RM-04 | Work already done is gathered, not redone, unless it is incomplete or needs revision (RO3). |
| RO-1 to RO-12 | As in the plan §5, one row each, on the step of the phase they govern: RO1, RO2, RO11 on `reading.observe`; RO4, RO5, RO12 on `reading.open`; RO7 on `reading.check`; RO9 on `reading.apply`. |

### 5.2 Reading a verse (step `reading.observe`): the role guide

| Key | Rule (source) |
|---|---|
| RG-01 | Read outward from the verse, not inward from the scope's question. First record everything the verse carries, each with where it bears (chapter, thread, signpost); answer the scope's question last. A verse often has two or three significances, and none is dropped. (guide §4.0) |
| RG-02 | Read the verse in its passage and genre; name the speaker; explore figures for what they say about the inner being; take paired and opposite acts together; restating a verse is not reading it. (§4.1, B:91) |
| RG-03 | Find the main inner-being operation and give every M-coded word, and every T-code word that turns out relevant, its role: characteristic, qualifier / process-element, or standalone. The role comes from this verse, never the cluster tag. (§4.2) |
| RG-04 | A qualifier gets no own account from the verse. It is recorded with what it gives the characteristic it binds to (a measure, strengthening, ground, cause, object, setting, bait) and as an interrelationship. A qualifier whose usage varies across contexts may earn its own reading later. (§2, §4.3) |
| RG-05 | Record how the M-code words work together (relational observation). Record any pointer outside the verse separately, without resolving it inline. (§4.4, checklist §0.5a) |
| RG-06 | Record the parties: who bears the act, who causes it, who is acted on (source, target, impact, purpose), and the route A, B or C. A non-human being is never itself a HIB; a collective stays one HIB; an implied party is named as referential, never asserted. (§4.5, method rules 1 to 4) |
| RG-07 | Read the T3 operations, movement and force, negators (a refusal is an act), connectives, body parts, places, objects and nature for what they carry here; read every row, untagged ones too. (§4.6) |
| RG-08 | For every word that names an inner or bodily act, look at the original: the root's range in all three meaning sources, read together, never one picked and the others dropped; the ESV renderings across its verses; whether the English adds or hides; the literal sense beside the rendering. Where more than one reading is open, record each, and mark the choice "I read". (§4.6a; method rules 42, 43, 70, 88, 92, 113) |
| RG-09 | Record each word's face: how it appears here, the circumstance, and why it differs from its other occurrences; and where the sense departs from the general gloss. (§4.7, B:89, R18) |
| RG-10 | Never close a verse or item on "not X". A role label is never a verdict; the close records what the verse is. Silence about the inner being is a finding, recorded as data with its reason. (§4.9; method rules 18, 91) |
| RG-11 | A hidden phenomenon behind a stated or refrained act may be named, with the verb, clause or stated silence that grounds it, and whether it is stated or read. (method rules 14, 15) |
| RG-12 | A literary or structural pattern is not an inner-being observation; log it as an open question instead. A human/divine comparison is recorded only where the text's own wording anchors it. (method rules 16, 23) |
| RG-13 | Keep the source of an interior state apart from the source of an enablement to act. (method rule 21) |
| RG-14 | Morph is read, not carried: where occurrences of a word show different stems or voices, record whether the subject does, undergoes or causes the act. (method rule 95) |
| RG-15 | A difference, or a specific inference, is its own observation, never folded into another. (method rule 93) |
| RG-16 | A word that is only a homonym or a name, with no meaningful context, is recorded as such (tag `no-human-context`) and left. Data errors found while reading are flagged (tag `data-error`), not fixed in the reading. (method rules 97, 98) |
| RG-17 | The catalogue's questions are prompts for the areas to explore. A question that does not apply is not answered, and no answer is manufactured beyond what the verse shows. (R17) |
| RG-18 | Faculty (heart, soul, spirit, mind) is reflected on at the end, over the scope, not per word. (§2, §5.5) |
| RG-19 | Before reading the whole scope, read a few verses and have them checked. (§5.6) |

### 5.3 The observation record (steps `reading.observe`, `reading.record`)

| Key | Rule (source) |
|---|---|
| RW-01 | No observation is changed except by a reading, and every change is recorded with its reason. An observation no longer supported by the verse is soft-deleted, with the reason. (R6, R15) |
| RW-02 | Per M-code in focus, and per T-code found relevant, the verse's observations hold `reading.observation_parts` (face, role, operation, parties, route, home). The term reading results (meaning in context, surface variants, related terms) are observations too. (R13a) |
| RW-03 | One observation row per M-code or relevant T-code in focus, with no duplicate rows. An observation applying to several verses or terms carries several nodes. (R16) |
| RW-04 | Observation text is concise and tied to this verse's content, never a restatement of the word's dictionary sense. A transliteration is never given without its gloss. (method rules 108 to 111, 119, 120) |
| RW-05 | An observation about a word can be answered only by consulting this occurrence's verse, span and morph. (method rules 112, 121) |
| RW-06 | Verse references are resolved fresh at write time, never taken from the text written. Relations are recorded only on evidence. (checklist §0.5, §0.8) |
| RW-07 | A flag raised in reading (needs adjacent context, a pointer) states its reason and what the follow-up must establish, and is carried to an open item, not resolved inline. Can't-resolve is recorded, never guessed (tag `could-not-resolve`). (method rules 74, 104, 116; checklist §0.5a, §0.5b, §0.6) |
| RW-08 | Where the evidence points to more than one reading, each is its own observation with its own evidence. (method rule 102) |
| RW-09 | A re-read includes the observations already recorded for the verse, so the reading sees prior findings and builds on them. (method rule 99, RO2) |
| RW-10 | Where a verse ends up is recorded as an `observation_disposition` (told, claim, held, data, context, withdrawn). (R5) |
| RW-11 | Missing data in the base extract is named as a gap, never substituted from memory or outside knowledge. (method rule 37, RO4) |

### 5.4 D1 and D2 in a session (steps `word.read`, `cluster.read`)

These are carried from method rules 78 to 90 and 94 (subgroups), adapted from "the LLM" to Claude in a session.

| Key | Rule (source) |
|---|---|
| RC-01 | For a cluster, every member word's glosses and surfaces are read before any is placed in a subgroup. (78) |
| RC-02 | Subgroups group by shared meaning, not similar wording; at most 10 real subgroups, FLAG excluded; a label names the essence, not a word list; a singleton is valid; each word sits in exactly one subgroup. (79 to 82, 86) |
| RC-03 | A word goes to FLAG only with a reason (no inner-being implication, belongs to another cluster, or another anomaly); any placement may carry a note. (83, 84) |
| RC-04 | A subgroup's anchor verse is the one that best shows its shared characteristic, chosen by reading, not by a count. (85) |
| RC-05 | Read every occurrence; grouping similar verses never excuses skipping one. (89, 90) |
| RC-06 | Compare the subgroup's words against each other: where they share meaning and where they diverge. (94) |
| RC-07 | Every occurrence of a word read in D1 is cited by at least one observation, checked after the write. (96) |

### 5.5 The narrative (steps `reading.apply`, `narrative_register.*`)

| Key | Rule (source) |
|---|---|
| RN-01 | Programme prose is the researcher's. The narrative is Claude's to write from the claims, to the style rows, with no approval before publishing; the researcher reads and corrects through Claude. (R4, from B:85) |
| RN-02 | The narrative is *Inner Being in Operation*, kept as blocks in iba.db (`governance.narrative_home`). Each block fits the flow and context of its chapter's story, and the chapters follow a story. A chapter's purpose (`narrative_chapter`) is read before material is placed in it. (R4, from B:86) |
| RN-03 | The original adjusts to the new, not the reverse; each unfounded claim is checked and restated; each later reading adds to the narrative. The researcher's own pictures are not narrative terms: the verses' own phrases are used. (from B:86) |
| RN-04 | Quote wording is checked against the ESV text in iba.db. Science chapters come later. The Spirit's own acts are placed in 13.1; Jesus's own acts get their 13.1 face, and Ch 10 keeps the human side. (from B:87) |
| RN-05 | A reading's claims are woven into the narrative knowing more is to come, never fitted where they support the current story. "Does not fit" means the structure must change. A key characteristic gets its own Ch 10 sub-chapter, with its angles woven into the chapters they belong to. (from B:88) |
| RN-06 | A phenomenon gets one account: what Scripture says it is, its forms from the words themselves, and why they differ. Other sections carry only what belongs to their activity and point back to it. Saying what a verse means in its setting is required; verses are not listed. Readings beyond what a verse states are marked "I read". (from B:90) |
| RN-07 | Narration is from the inner being's workings: probe (compare, ask why, ask what lies behind it, whether a relationship makes a difference); explore figures; never restate a verse as narration. (from B:91) |
| RN-08 onward | The narrative style guide's rules, carried in by work unit W-2 (§8). |

## 6. Quality checks

These are new rows in `cfg_quality_check`, on the reading's gates.

**Carried and adapted from the passage method (9):**
- is-genuinely-human;
- verse-actually-supports-it;
- genuinely-inner-being;
- not-a-literary-pattern;
- warrant-is-specific;
- full-lexical-range;
- stated-or-inferred-honest;
- source-target-not-invented;
- insufficiency-genuinely-absent.

The other 9 passage checks retire with the method.

**New (12):**

| Gate | Check |
|---|---|
| `reading.check` (observe) | every M-coded word, and every relevant T-code word, has a role |
| | every observation holds its parts (`reading.observation_parts`) |
| | every verse's home follows the scope's objective (RO10) |
| | bindings and relational observations are recorded, and pointers are kept separate |
| | earlier observations were read into focus, not re-derived |
| | every reading beyond the verse is marked "I read", with no imputed pattern |
| | parties and route are recorded |
| | no duplicate observation rows |
| `reading.check` (claims) | every claim rests on observations, not on verses alone |
| | every block fits its chapter's story and the style rows |
| any | every gap is resolved against what is expected, not by presence |
| any | every unresolved gap has an open item |

## 7. Control map, columns and tables

| Row | Action | New text |
|---|---|---|
| `cfg_control_home` study_method | Reword (R1) | home: "cfg_method_rule (steps reading.*, word.read, cluster.read), cfg_quality_check, cfg_setting reading.*, with cfg_prose_concept pointers to the glossary"; "A Workflow file is the authority only for the programme and inner-being definitions, through cfg_prose_concept." |
| `cfg_control_home` study_state | Reword (W2) | "escalation (reading escalations, thread items), the reading and reading_verse tables, narrative_chapter, the claim register tables, the narrative blocks" |
| `cfg_control_home` study_output | Reword (W3, R7) | "_analytics/Clusters/<cluster>/ (readings in readings/<label>/), the exported narrative chapters" |
| `cfg_table ib_observation` use | Correct (W35) | writers: reading.record, reading.apply, observation_enhancer.apply; gathered rows from the retired API stages and the October ledgers |
| `cfg_table ib_node` use | Correct (W34) | "the grounding of every observation: one row per verse, term, cluster, subgroup or observation it rests on" |
| `cfg_column ib_node.source_stage` | Correct (C16) | the stage of the observation it grounds |
| `cfg_column ib_observation.stage` | Correct (C17) | the six values plus `reading` |
| `cfg_column ib_observation` setting, meaning, implication, run_id, revisit_note | Reword (W36) | without "October ledger part" or "Strand-Reading run": the reading's record |
| `cfg_column verse_meta.status` | Correct (C20) | "set by a reading (analysed at its observe gate, citated when a block cites the verse) or by VerseMeta.ps1" |
| `cfg_table wa_obs_question_catalogue`, `cfg_column` question_code | Correct (C21) | 116 rows; the catalogue is the reading's prompts (R17); the FK is a design point |
| `cfg_status_flow` for `ib_observation` | New (R14) | one flow per stage, stating who sets each status |
| `cfg_prose_concept` | New (R9) | pointers for role, characteristic, operation, main IB operation, qualifier, relational, pointer, face, route, faculty |
| `cfg_method_example` (new table) | New (R10) | worked examples, each with the rule key it illustrates, the verse, what the reading found and why; the four guide cases restated or replaced |

## 8. Work units this change set cannot finish by itself

| Unit | What | Why separate |
|---|---|---|
| W-1 | Carry the July method file into config (R11) | it needs reading section by section; the relevant parts become RG or RW rows |
| W-2 | Carry the narrative style guide into config (R4, R1) | the guide (`Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md`) has not been read for this change set; its rules become RN-08 onward |
| W-3 | Gather the ledger faces (R18) and restate #2260 to #2267 (R19) | data work, after the rules are in |
| W-4 | The generated guide (R12) | built from the rows once all are in; you review it |

## 9. Code to build after the config is in

Each item is its own escalation task, built and tested on a copy (B:97).

| # | Build |
|---|---|
| B1 | `Reading.ps1` on the phases: 0.C with an objective; 0.GAP pre gathering; the gap JSON processed into the tables before each gate (RO12); D3 claims read before observe; D4 observe, claims with 0.GAP post, narrate |
| B2 | the observation record shape: the parts (face, role, operation, route) as fields; stage `reading`; dispositions; soft delete with reason |
| B3 | `word.read` and `cluster.read` (D1, D2 in a session); retire the API work packages `verse-lexical` steps `lexical.meaning` / `lexical.relational` and `cluster-reading` |
| B4 | the collation reads all observations of a verse, not only `draft` (C4); it gives the passage, T-codes, meaning text and renderings |
| B5 | the hard-coded rules into config (C25) |
| B6 | the gap types and their checks (§3 `reading.gap_types`) |
| B7 | the reading output folder and the index exclusion (R7, C27) |
| B8 | the faces gathered into the record (R18) |
| B9 | `cluster.status`: its advance depends on Stage 1 coverage; it is redesigned or retired |
| B10 | the glossary currency check (P33) and the worked-examples table (R10) |
| B11 | the quality checks delivered and checked at the gates (§6) |

## 10. The order of work

1. **Config rows:** §2 to §7, in one tested `configmaint` run on a copy, then live.
2. **W-1 and W-2:** they add RN and RG rows.
3. **Builds B1 to B11:** each with its test.
4. **W-3:** gathering the faces and restating the findings.
5. **W-4:** the generated guide, for your review.
