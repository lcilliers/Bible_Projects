# #2268 The role-reading guide v2, plotted into the config (v2)

**Date:** 2026-10-24 · **Escalation:** #2268 · **Status:** findings only. Nothing has been changed.

**v2.** Two additions follow the researcher's correction of 2026-10-24 (on the overlay v2). §6 sets the guide's per-verse record against the observation record as it is (`ib_observation`, `ib_node`), column by column. §7 links the guide's hand-over checks to gap discovery. The overlay is now `outputs/escalation/2268-config-overlay-on-reading-process-v2-20261024.md`. v1 of this file is in `outputs/escalation/archive/`.

Researcher, chat 2026-10-24 (verbatim): *"and one more exercise before we start to work on closing the gaps and re-align the rules.  Take Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md and make sure you plot it into the config analysis. this instruction should all be captured in configs and should not live on its own."*

**The source:** `Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md` (161 lines; approved #1995, v2 #2168).

**What was checked:** each statement of the guide against:
- `cfg_behaviour_rule`, `cfg_method_rule`, `cfg_quality_check`, `cfg_setting` and `cfg_enum`;
- the columns of `ib_observation`, `ib_node`, `reading_strand_hit` and `verse_lexical` (`cfg_column`);
- the glossary entries the guide cites (the `bible_research.db` prose store, allowed by B:67);
- the steps of the reading process (N0 to N10, from the overlay file).

**What each column means:**
- **Held:** a live config row carries the statement.
- **Partly:** a row carries some of it, or carries it in era wording, or on a route the reading does not use.
- **Not held:** no config row carries it.
- **Delivered:** whether the holding row reaches `Reading.ps1`.
- **Candidate home:** the kind of config row the statement would fit, offered for the design. It is not a decision.

## 1. In short

| | Statements | Held | Partly | Not held |
|---|---|---|---|---|
| §1 What the reading is for | 6 | 1 | 5 | 0 |
| §2 Terms | 12 | 0 | 11 | 1 |
| §3 Before reading a collection | 5 | 2 | 3 | 0 |
| §4 Reading one verse | 13 | 1 | 10 | 2 |
| §5 Reading a collection | 10 | 4 | 4 | 2 |
| §6 Worked cases | 4 | 0 | 0 | 4 |
| §7 Checks before hand-over | 7 | 0 | 0 | 7 |
| **Total** | **57** | **8** | **33** | **16** |

**Where it stands.** Of the 57 statements, only 8 are carried whole by a config row. Only 2 of those 8 act inside a reading:
- 3.4: open items are matched at Open, in code;
- 4.8b: the record's `basis` field, where `read` means "I read".

The other 6 rules are not delivered to `Reading.ps1`. 33 are carried in part. Mostly that is B:73, which compresses §1, §4 and §5 into one paragraph worded for strands, delivered only on `_analytics/**`, and pointing back to the guide. 16 are carried nowhere:
- the reading sequence's record (§4.8);
- the T-code and untagged-row reading (§4.6);
- the faculty (§5.5);
- the trial-first discipline (§5.6);
- the worked cases (§6);
- all seven hand-over checks (§7).

The guide itself is held in config only as a file path in B:73's text, and B:73's `enforced_by` names the earlier v1 (overlay C5).

## 2. The guide's front matter and sources

| Item | In config | Note |
|---|---|---|
| Audience: "Claude, when reading strand verses and weaving them" | – | Era: strands and weaves (overlay W12) |
| "Where this guide and a source differ, the source wins" | – | so the guide is a derived document. Its sources are the authority, and several of them are not config (below) |
| Source: the glossary (prose 1089, 1047, 1043, 1066, 1048, 1046, 1069) | Partly | all seven entries exist, at status `draft`. Only *inner being* has a `cfg_prose_concept` pointer (`inner_being_definition`), and none is delivered at a reading |
| Source: `wa-verse-analysis-method-v1-20260702.md` §13 and §14 | Not held | a July Workflow file, itself a method held in a document |
| Source: `iba/docs/1704-role-driven-reading-sequence-design-v1-20260915.md` | Not held | **moved** to `iba/docs/archive/`, so the guide's link is broken |
| Source: `iba/docs/1706-progressive-relational-verse-reading-v1-20260917.md` | Not held | live engineering doc |
| Sources: rules 69, 70, 71, 72 | Held | B:69 to B:72, all era-worded (overlay W13 to W15) and not delivered |
| Sources cited by memory name (`feedback_surface_is_the_sensitivity_lens`, `feedback_narrative_citation_is_verse_level_not_word_coverage`, `feedback_read_verse_for_inner_act_not_event_template`, `feedback_weave_with_meaning_not_quote_lists`) | Held, by rule | the memory files are retired (#2184, archived). #2184 mapped them to B:110, B:93, B:91 and B:90/B:91. The guide still names the retired files |
| Sources: the M18 correction re-read and the redraft trail under `_analytics/Clusters/M18 …` | – | history, not method |

## 3. The statements, one by one

Steps: N0 anchor and purpose · N1 scope · N2 what is known · N3 gap JSON · N4 read and record · N5 gate 1 · N6 synergy · N7 apply · N8 gate 2.

### §1 What the reading is for

| # | The guide says (in short) | Step | In config | Coverage | Delivered | Candidate home |
|---|---|---|---|---|---|---|
| 1.1 | The study's question: what Scripture reveals about the characteristics, operations and interrelationships of the human inner being | N0 | `cfg_prose_concept inner_being_definition` (pointer to glossary 1089) | Held | no (a concept pointer is not delivered) | delivery of the concept at Open |
| 1.2 | The inner being is a web; a strand is one thread; a verse is where threads cross | N0 | B:84 | Partly: era (strand as the unit) | no | B:84 reworded |
| 1.3 | A characteristic is not predefined; known by inference from what the inner being does; a lemma, gloss, surface or tag is not a characteristic | N4 | glossary 1047 (draft); B:73 ("an M-code tag does not make a word the verse's characteristic"); B:89 ("never taken from its cluster tag") | Partly | no | a reading method rule |
| 1.4 | The same word changes character with circumstance; faces are a key discovery | N4, N7 | B:89 | Partly: era; faces have no home (overlay P10) | no | B:89 reworded; a face field |
| 1.5 | The focus is the HIB; other beings for what they are and do and how they act with the HIB | N4 | B:72 | Partly: era (ledger) | no | B:72 reworded |
| 1.6 | So a verse is read for what the inner being is doing in it and how its words work together, never as "a verse about the strand's word" | N4 | B:73 | Partly: era | no | a reading method rule; the gap guide for `not_read` |

### §2 The terms

| # | Term | In config | Coverage | Candidate home |
|---|---|---|---|---|
| 2.1 | M-code cluster: a loose grouping, an anchor, no re-tagging | glossary 1043; B:70 | Partly: B:70 era (ledger) | B:70 reworded; concept pointer |
| 2.2 | role: characteristic, qualifier / process-element, standalone, decided per occurrence | glossary 1066; B:73 | Partly: no enum, no field (`verse_lexical.role` is the cluster-code list, not this role) | `cfg_enum` of roles; a record field |
| 2.3 | qualifier: gives value in place, no own account; **except a qualifier whose usage varies may earn its own reading later** | B:73 (no own account) | Partly: the exception is not held | method rule |
| 2.4 | main IB operation: the inner-being activity the verse is about | B:73 names it | Partly: no definition, no field | concept; record field |
| 2.5 | operation: what an inner-being activity is doing and how, to or from others | glossary 1048; method rule 20 *four-parts* (passage route, `operation.set`) | Partly: on route D3 only | concept pointer; method rule for the reading |
| 2.6 | relational observation: two M-code words working together in the verse | B:73; method rule 122 (M0.6.5, route D1) | Partly: no field or tag for the reading | record field or tag |
| 2.7 | pointer observation: always separate; points outside the verse | B:73 ("pointers outside the verse kept separate") | Partly: no field or tag | record field or tag |
| 2.8 | party-kind T-codes: T4, T7, T8, T9, T11 | `cluster` T-codes; `verse_lexical.party_kind` | Partly: `party_kind` covers T4, T7, T8 and T9, **not T11**; a reading is given no T-codes (overlay P7) | collation; method rule |
| 2.9 | T3 operations: inner-being action words not tied to one cluster | glossary 1069; `cluster` T3 | Partly: not given to a reading | collation |
| 2.10 | T2 and other referent T-codes (T5, T6, T10, T12, T13, T14) | glossary 1046; `cluster`; `verse_lexical.is_negator` (T5) | Partly: not given to a reading | collation |
| 2.11 | faculty / where: reflected on at the end, over the collection | – | **Not held** (only #1704 decision 4, archived) | method rule |
| 2.12 | face; route A, B, C | B:89 (face), B:72 (route); `reading_strand_hit.face` | Partly: face lives only on a table of superseded strands; route has no enum or field | `cfg_enum` of routes; record fields |

### §3 Before reading a collection

| # | The guide says | Step | In config | Coverage | Delivered | Candidate home |
|---|---|---|---|---|---|---|
| 3.1 | Use what is extracted; the set-based M-code link; add the T-codes from the same join | N2 | B:71 | Partly: era (strand folder pulls); the T-codes are not collated | no | B:71 reworded; collation |
| 3.2 | The surface table per Strong's, both ways; a surface is a pointer to a verse, never a meaning | N1, N2 | B:110 | Partly: era; no tool (#2235, overlay P5) | no | B:110 reworded; collation |
| 3.3 | Earlier readings of the same verses; a narrative citation is verse-level, not word coverage; build on, don't re-derive | N2 | B:93 (citation is verse-level), B:71(3), B:114 | Partly: collation shows only `draft` observations (overlay C4) | B:114 yes | B:114 extended |
| 3.4 | The open threads: items whose trigger the collection meets | N2, X | B:74, E:16; collation matches items | Held, in function; the guide names the register file, which is now generated (era) | yes (match at Open) | – |
| 3.5 | Filters and buckets are working aids, never a standing decision | N1 | B:111 | Held | no | – |

### §4 Reading one verse

| # | The guide says | Step | In config | Coverage | Delivered | Candidate home |
|---|---|---|---|---|---|---|
| 4.i | The sequence says what to notice and in what order, not a frame of fixed answers; follow a discovery path; the rejected M64 §2a event template | N4 | B:91 ("no reading framework laid over it") | Partly | no | a reading method rule |
| 4.0 | Read outward: write down everything the verse carries, each with where it bears (chapter, thread, signpost); two or three significances; none dropped; the item's question last | N4 | B:73 (1) | Partly: no field for the significances or where each bears | no | method rule; record field |
| 4.1 | Read in passage and genre; name genre and speaker; explore figures; take paired and opposite acts together | N1, N4 | B:73, B:91 (passage, figures) | Partly: the scope gives no passage (overlay C3); paired and opposite acts are not held | no | method rule; scope |
| 4.2 | Find the main IB operation and every M-coded word's role; what each qualifier gives (a measure, strengthening, ground, cause, object, setting, bait); the role is from the verse, never the tag | N4 | B:73 | Partly: the list of what a qualifier gives is not held; no field | no | method rule; `cfg_enum`; record field |
| 4.3 | Only then the strand word, in its role: the characteristic is the focal point; a qualifier gets no own account and is carried as a face and an interrelationship | N4 | B:73 | Partly: era (strand word) | no | method rule |
| 4.4 | The M-code words together: a relational observation; a pointer recorded separately, not resolved inline | N4 | B:73; method rule 93 (a difference is its own observation, route D2) | Partly: no field | no | method rule; record field or tag |
| 4.5 | The parties: bearer, cause, acted on; source, target, impact, purpose; route A, B or C (may be A and B) | N4 | B:72; `ib_observation.parties` (free text); method rule 20 (route D3) | Partly: route has no field; source, target, impact and purpose have no field on route D4 | no | record fields |
| 4.6 | The action words and other referents: T3 operations, movement and force, negators (a refusal is an act), connectives, descriptive words, body parts, places, objects, nature; **read every row, untagged ones too** | N2, N4 | – | **Not held**: no rule; the collation gives M-code rows only | – | method rule; collation |
| 4.6a | Look at the original: the root's range (`strong_meaning_tree` and the ESV renderings across its verses); does the English add or hide; the literal sense beside the rendering; more than one reading marked "I read" | N2, N4 | B:73 (2); method rules 70, 88, 113 (three meaning sources, routes D1 and D2); 42, 43 (full lexical weight, route D3); 92 (alternatives, route D2); `ib_observation.basis` | Partly: renderings across verses are not given (overlay P7); the method rules are on other routes | no | method rule for the reading; collation |
| 4.7 | Note the face: how the word appears here, the circumstance, why it differs; where the sense departs from the general gloss | N4 | B:89; tags `surface-gloss-divergence`, `alternative-meaning` (`ib_observation.tag_guidance`) | Partly: no face field (overlay P10); tag guidance not given to a reading (P11) | no | record field |
| 4.8 | Record per verse: main IB operation; each M-coded word's role and what each qualifier gives; the strand word's role and face; relational and pointer observations; parties and route; the home, following the main operation | N4 | – (`ib_observation` holds text, meaning, setting, implication, chain, basis, parties) | **Not held** (overlay P9) | – | record fields; `cfg_column` |
| 4.8b | Mark a reading beyond the verse "I read"; join no verses into a pattern no verse states | N4, N7 | `ib_observation.basis` (`read` = "I read"); B:69 | Held | B:69 no | B:69 reworded |
| 4.9 | Never close on "not X"; a role label is never a verdict; the close records what the verse **is** and where each significance goes; route C is a finding with its reason | N4, N5 | B:73 (3); method rule 91 (every instance states what it is, route D2) | Partly: gate 1 accepts any reason of 10 characters (overlay P13); the `not_read` guide asks for "the reason it holds nothing" | no | quality check at gate 1; gap guide reworded |

### §5 Reading a collection

| # | The guide says | Step | In config | Coverage | Delivered | Candidate home |
|---|---|---|---|---|---|---|
| 5.1 | Progressive: a verse with several M-codes is read once for each strand that reaches it; each sees what earlier ones found; the question shifts | N2, N4 | B:84; B:73 ("progressive reading across strands") | Partly: era; earlier readings are shown only as `draft` observations (overlay C4) | no | method rule reworded to readings |
| 5.2 | Group by the main operation, not the entry word; a qualifier's verses go to the characteristic's account and to a short table in the word's own section | N6, N7 | B:73 ("collections are grouped by main operation") | Partly: the qualifier table is not held; synergy has no grouping step | no | method rule; synergy |
| 5.3 | One account per phenomenon: what it is, its forms, why they differ; narrate by probing; never verse lists; other sections point back | N7 | B:90, B:91 | Held (era: ledger) | no | B:90 reworded |
| 5.4 | Interrelationships and faces are findings, feeding Ch 11 §4 and the change-of-character file; never thrown away | N7 | B:89 | Partly: the change-of-character file is an `_analytics` ledger (era) | no | B:89 reworded; a face home |
| 5.5 | Faculty last: heart, soul, spirit, mind, reflected on once over the collection | N6, N7 | – | **Not held** | – | method rule |
| 5.6a | Trial a few verses and have them checked before the whole set | N4 | – | **Not held** | – | method rule; a step in the reading |
| 5.6b | Read the verses; don't ask what a reading would answer | N4 | B:109 | Held (era: "belongs in a strand") | no | – |
| 5.6c | Don't hold items unnecessarily | N4, N7 | B:92 | Held (era: "while the strand is busy") | no | – |
| 5.6d | No dedicated audit of the existing narrative; correct placements in each read-back | N7 | B:73, B:72 | Partly: era (each strand's read-back) | no | reworded to readings |
| 5.6e | Weave, don't fit; every reading gets a placement; "does not fit" means the structure must change | N7 | B:88 | Held (era: strand) | no | – |

### §6 Worked cases

| # | Case | In config | Coverage |
|---|---|---|---|
| 6.1 | 2Pe 2:13 (#1993): five M-codes; pleasure is the measure of the reveling; the home follows the main operation | – | **Not held** |
| 6.2 | 2Cor 7:11 (#1706): seven M-codes read by three strands in turn; a pointer to 7:2; an untagged word (G0627) carries an operation | – | **Not held** |
| 6.3 | Lam 4:6 (#2168, OT-07.2): read inward, nearly closed as "not a fear face"; read outward, four significances | – | **Not held** |
| 6.4 | Psa 1:1, 1:5 (method §14): role is per occurrence | – | **Not held** |

No config table holds a worked example. They are the guide's teaching material, so their home needs your ruling (R10 below).

### §7 Checks before a reading is handed over

None is held. `cfg_quality_check` has no row for any `reading.*` step (overlay P13). Each would sit at gate 1 (N5) or gate 2 (N8).

| # | Check | Candidate home |
|---|---|---|
| 7.1 | Every M-coded word, and every untagged row that carries the operation, given a role | `cfg_quality_check` at gate 1 |
| 7.2 | The strand word read in its role in the verse, not by its tag | gate 1 |
| 7.3 | Every verse's home follows its main operation | gate 1 |
| 7.4 | Qualifier bindings and relational observations recorded, pointers kept separate | gate 1 |
| 7.5 | Earlier readings of the same verses used, not re-derived | gate 1 |
| 7.6 | Every reading beyond the verse marked "I read", with no imputed pattern | gate 1 and gate 2 |
| 7.7 | Parties and route recorded | gate 1 |

## 4. What this adds to the overlay

- **More gaps, beyond overlay P1 to P15:**
  - P16: the faculty (§2.11, §5.5)
  - P17: reading every row, untagged ones too, and the T-code reading (§4.6)
  - P18: the trial-first discipline (§5.6a)
  - P19: the qualifier exception and what a qualifier gives (§2.3, §4.2)
  - P20: paired and opposite acts (§4.1)
  - P21: the qualifier table in a word's own section (§5.2)
  - P22: the T11 party kind is not in `verse_lexical.party_kind` (§2.8)
- **A further conflict.** C15: the `not_read` gap guide ("the reason it holds nothing") and gate 1's 10-character reason, against §4.9 (a close records what the verse *is*).
- **Further era wording.** W32: the guide's own audience line and its §5.1 and §5.6d are worded for strands. W33: the guide cites retired memory files and a design document now in `archive/`.

## 5. Decisions this adds to R1 to R8

| # | Decision |
|---|---|
| R9 | Where the study's terms live (role, characteristic, operation, main IB operation, qualifier, relational, pointer, face, route, faculty): `cfg_prose_concept` pointers to the glossary (now all `draft`), or `cfg_enum` and `cfg_column` definitions, or both |
| R10 | Where the worked cases live once the guide is retired: a config table of examples, the glossary, or kept as a teaching document that config points to |
| R11 | The July method file (`wa-verse-analysis-method-v1-20260702.md` §13 and §14), the guide's own source: carried into config with the guide, or retired |
| R12 | The guide itself once its content is in config: archived (B:96), with B:73 pointing to the cfg rows instead of the file |

## 6. The guide's record against the observation record

The guide (§4.8) asks for a record per verse. The observation record has one row per observation (`ib_observation`) and one grounding row per verse and strong it rests on (`ib_node`). The table below shows, for each part of the guide's record, where it could sit today and where nothing holds it. Role and face are per occurrence (per verse and word), so their natural grain is `ib_node`, not the observation. That grain is offered for the design, not decided.

| The guide's record (§4.8, §4.5 to §4.7) | Grain | Today | Held? |
|---|---|---|---|
| main IB operation of the verse | verse | none | no |
| role of each M-coded word (characteristic, qualifier, standalone) | occurrence (verse + strong) | none: `ib_node` has verse, strong, surface, morph, cluster, subgroup, question; `verse_lexical.role` is the list of cluster codes | no |
| what each qualifier gives, and to which characteristic | occurrence pair | none; `ib_node.traced_observation_id` links observations, not words | no |
| the word's face, and its circumstance | occurrence | `reading_strand_hit.face` (superseded strands only); tags `surface-gloss-divergence`, `alternative-meaning` | partly |
| relational observation (two M-code words together) | observation over two or more nodes | `ib_observation.window` `relational`; catalogue M0.6.5 (route D1); several `ib_node` rows on one observation | partly (route D1 only) |
| pointer observation, kept separate | observation | none: no tag or window; checklist §2 item 15 names "pointer observations" with no tag chosen | no |
| parties: bearer, cause, acted on; source, target, impact, purpose | observation | `ib_observation.parties` (free text); `verse_lexical.party_kind` (T4, T7, T8, T9) | partly |
| route A, B, C | verse | none | no |
| home (follows the main operation) | verse | `ib_observation.cluster_code` = the reading's `home_cluster` (overlay C24) | no (conflicts) |
| the original: root range, renderings, literal sense | observation | `ib_observation.meaning_source` (three sources; the reading does not fill it) | partly |
| "I read" | observation | `ib_observation.basis` `read` | yes |
| setting, meaning, implication, chain | observation | `ib_observation` columns (October ledger shape, overlay W36) | yes, era-worded |
| what the verse carries and where each significance bears (§4.0) | verse | none | no |

## 7. The guide's checks and gap discovery

The guide's §7 checks are what "read" should mean for one verse. None is held (§3 §7 above), and none feeds any measure of "read" in §2.GAP of the overlay. Collation presence, `verse_meta` `analysed`, Stage 1 coverage and `cluster.status` all count a verse as read without asking whether its roles, home, parties and route were recorded. If the §7 checks become quality checks (P13), they are also the measure a gap analysis needs (overlay P23 to P25, R13).
