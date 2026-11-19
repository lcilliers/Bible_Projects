# #2510 The inner being's working: what is understood, what is not, and why the methods did not ground (v3, 2026-11-19)

Status: analysis by Claude, for the researcher to correct. It replaces `outputs/escalation/archive/2510-two-contexts-root-cause-v1-20261119.md` after the researcher's correction of 2026-11-19 (recorded on #2510 v12) and v2 (`outputs/escalation/archive/2510-inner-being-working-v2-20261119.md`) after the researcher's second correction (recorded on #2510 v13): section 5 now gives the stages with their elements and focus, section 5.1 is corrected (behaviour is also states and conditions, and it has qualifiers), and the consolidated analysis is in `outputs/escalation/2510-inner-being-definition-lineage-v1-20261119.md`. Statements of cause are inference (B:4). Sources: the project's own record (guides, rules, settings, BUILD, session logs, the archived memory lessons) and read-only queries of `iba.db`.

## 0. The corrections accepted

| Item in v1 | The researcher's correction | What v2 does |
|---|---|---|
| The two contexts (§2) | Partly correct: the what (question, unit, evidence) is understood; the how (can it be checked, consistency, where) is not | Section 1 separates what is understood from what is not |
| Root cause R1 (a unit mismatch) | Not consistent: the unit varies by read, and the reading should trigger different interventions; these are defined but not done (read beyond the verse, reclassify a word, do not force meaning) | Section 4: the interventions as the record defines them, and where they are absent from the current process |
| R2 (one vocabulary on both sides) | More an excuse than a reason: if one understands what to do, the vocabulary can be used in context | Withdrawn |
| R3 (the dependency resolved in one pass) | Not true: the researcher did set the two apart; I did not understand it as such | Withdrawn. The separation was defined (the layers of 14 Nov, the stages of 15 Nov, B:133). The failure was in my application, and the record says so (#2509 v5: "you did not respect the boundaries between lexical work and inner being work") |
| R4 (no settled definition of the working) | A real problem. There have been many attempts to clarify it, none really applied. Each time it is an issue a new definition is derived; the problem is that the definition is not pursued. The only viable test is whether the outcome is sensible, reasonable and defendable | Section 5: the definitions, how far each was applied and why it stopped; the test |
| The surface-group work | It was intended to resolve some of the points raised; the researcher's intent did not ground fully | Section 3, methods b and c |

## 1. The real problem

Neither the researcher nor I know how to depict the working of the inner being systematically. The how is still part of the discovery.

| | Understood | Not known |
|---|---|---|
| **The words used, in the verse** | The question (what does each word mean and do here), the unit (a word occurrence), the evidence (the verse, the structure, the lexicon). It can be checked largely against the text | How far the verse's own words reach before the passage must be read (the verse-bounded rule of 26 Jun and the passage rule of 10 Jun differ) |
| **The inner being's working** | The question (what is the inner being doing here and how do its characteristics interact), the unit (a working, a relation among words, not a word), the evidence (the relations among the words, the partner predicates, the circumstance, the passage) | **How it is depicted systematically; whether and how it can be checked; how to keep it consistent from read to read; where it is read (the verse, the passage, the collection)** |

The record shows that the how was attempted fourteen times (section 5). The test the researcher gives is the only one the study has: whether the outcome is sensible, reasonable and defendable.

## 2. The two contexts (kept short)

The words' context: what the words used say here (sense or face, form, structure, party, movement), checkable against the text, largely stable for a word. The working's context: how characteristics operate and interact in the verse, interpretive, varying by occurrence. A word and its working do not coincide in three ways: an inner-being word with no working in the verse (34% of node rows on `inner_being_state` words are *standalone*, read-only query 2026-11-19, indicative); a working carried by a word that is not an inner-being word (the act as the expression of a characteristic, 24 Jun; analogy vehicles, 14 Jul); a working that arises only from the words together (2 Cor 7:11; qualifiers that route per occurrence).

## 3. The methods the researcher put in place that did not ground

Each method is stated as the record defines it, with what was built and where it did not ground. Where the researcher's note is the evidence, it is quoted by its source.

| | The method as defined | What was done or built | Where it did not ground |
|---|---|---|---|
| a | **Separate observations for verse analysis and for inner-being analysis.** Stages 1 to 3 are lexical and verse-lexical only; no observation of stages 1 to 3 states an inner-being role; stage 4 is the inner-being analysis (B:132, B:133) | A ledger and recorders for stages 1 to 3; stage 4 not built. Of 14,962 live observations, 11 are stage `lexical`; the rest were written under earlier methods that mix the two in one record (tags such as statement, face, link, term, use) | The one stage 1 run restated the dictionary, so it was neither a verse observation nor an inner-being one (BUILD 534, 535). The old observations have not been separated, so the two kinds cannot yet be told apart in the data |
| b | **The surface group is used twice, separately: first in the verse analysis (stage 3), later in the inner-being analysis (stage 4)** (the researcher's account, #2463 v16 and 2026-11-19) | One grouping method, by dictionary meaning (#2509 v2); the use in stage 3 is defined in `layer.reading` (pairings, qualifiers, entities, direction, double meaning); no use in stage 4 is defined | A group made for one use was judged by the other: the run was declared a failure for "changing the meaning of the underlying words" (verse analysis) and for not serving anything (inner-being analysis). The two uses were never given two statements of what a group is |
| c | **The grain for verse analysis differs from the grain for inner-being analysis** | One grain for both in the data: a node is an occurrence of a word (verse, surface, code), and an inner-being observation is applied to the occurrences of the words it covers | An inner-being working is a relation among occurrences. The node model forces it onto single occurrences with a role each (characteristic, qualifier, object, relational target, enactment); how a working is one thing across several nodes is not stated |
| d | **The analysis batch unit** | The work unit is a collection's verses or a subset (B:120); a ledger row per word (stage 1) and per group (steps 1.1 to 2.1); the first run took 197 words and four record files | The record shows twice that the batch unit changes the result: three chapters to a file removed the boundary that kept the Amos reading to the verse (2 Aug); a passage-complete read left 116 of 915 verses unread (14 Jul). What a batch is for the layered reading (a word, a group, a verse, a collection) is not stated, and the guide's working discipline ("trial a few verses and have them checked before running the whole set", by-role guide 5.6) was not applied to the first run |
| e | **Handling of nuances and variances** (the researcher's §3 of the account; the faces; double and triple significance) | The face observation at stage 1 (RG-09); `double-meaning` at step 2.1; the by-role guide v2 added "double and triple significance" and "never close on not X" on 2026-10-19 after the researcher found the analysis "very binary" (#2168) | The face is held for lexical sense only; the working's variance (the same word working differently in different verses) belongs to stage 4, which does not exist. The guide's answer (read outward, §4.0; never close on "not X", §4.9) is not in the layered reading |

## 4. The reading triggers interventions (R1, corrected)

The researcher's point: the working is not one fixed thing; what a read finds decides what to do next. The record defines these interventions. I checked whether the layered reading holds them.

| Intervention | Where the record defines it | In the layered reading (`layer.reading`, `reading.observation_items`, the stage rules)? |
|---|---|---|
| Read beyond the verse: the passage, the genre, the speaker | By-role guide v2 §4.1 ("read the verse in its passage and its genre"); rule of 2026-06-10 (the surrounding verses may ground the meaning); B:116 (read each verse in its passage) | No: the items ground in the lexicon and the stored structure; the words passage, genre and beyond do not occur in `layer.reading` |
| Read outward from the verse, not inward from the item's question | By-role guide v2 §4.0 (#2168) | No |
| Look at the original: the root's range, the rendering, what the English adds or hides | By-role guide v2 §4.6a | Partly: stage 1 reads the lexicon; the check of the rendering against the Hebrew or Greek is not an item |
| Reclassify a word: its role comes from this verse, never from the cluster tag; a word wrongly placed in a collection is moved | By-role guide v2 §4.2; B:89; B:120; B:134 | Placing is defined (the collection change procedure, `Isolate`, `Subgroup`); no step lets a read trigger it |
| Do not force a meaning: a question that does not apply is not answered; a reading beyond the verse is marked "I read"; never close on "not X" | RG-17; RN-06; by-role guide v2 §4.8, §4.9 | RG-17 is a method rule of the reading; the layered items require an answer or a recorded none; "I read" and "never close on not X" are not carried |
| Record a pointer to discovery outside the verse, separately | By-role guide v2 §2, §4.4 | No |

Two readings of this, both inference. First, the interventions are defined, as the researcher says, and not carried into the process that replaced the strand reading: the by-role guide was "in force" from 11 Oct and the layered reading, from 14 Nov, does not mention it. Second, the guide mixes the two contexts in one pass, while the researcher's layering separates them. Set against the layering, the guide's steps divide:

| Belongs to the words' context (stages 1 to 3) | Belongs to the working's context (stage 4) |
|---|---|
| §4.6a look at the original; §4.7 the face; the rendering against the Hebrew or Greek | §4.0 read outward; §4.1 passage and genre; §4.2 the role per occurrence; §4.4 how words work together; §4.5 parties and route; §4.9 never close on "not X"; "I read" |

## 5. The definitions of the working: the stages, their elements and their focus

The researcher's point: the working has been defined many times and not pursued; the definition starts in the programme prose and runs through the dimensions, the catalogues, the definition of what to look for and the configs that set the rules for reading. The full account of each stage (source, what it defined, the elements it added, its focus, what it taught, what it left open) is in `outputs/escalation/2510-inner-being-definition-lineage-v1-20261119.md` section 1. This table is its summary; the elements are followed across the stages in section 2 of that document.

| Stage | Dates | What it defined | Elements it added | Focus | What ended it or what it left open |
|---|---|---|---|---|---|
| L1 The working definition (programme prose, area 1) | Mar to Apr | "Non-physical, internal states, capacities and expressions ... how a person thinks, feels, chooses, relates, orients" | States, capacities, expressions; the five operational dimensions; the non-physical test; the internal test with permeability; spirit and soul together; borderline words in | A filter for deciding whether a word is in scope | Never says how a working is read |
| L2 Tier framework and question catalogue | Mar to Apr | Each word worked through a standing catalogue, in tiers T0 to T7 | The characteristic as a thing with attributes: definition, place in the person, relations to God, others and other characteristics, formation, evidence | The word, then the characteristic behind it | The Fellowship run failed on nine defects (17 Apr); questions fixed before the verses were read |
| L3 Dimensions from the verse groups | Apr to 4 May | About ten to eleven domains (Spiritual/God-ward, Moral/Conscience, Affective, Cognitive, Volitional, Relational/Social, Sin and Vice and others) | The dimension follows the verse; a group has a dominant subject | Classifying verse groups by domain | Dropped 4 May as noise built on wrong assumptions |
| L4 The characteristic as the unit; the verse read for meaning | May to 11 Jun | The characteristic under a cluster; about 14 tier findings per term per verse | The cluster as working collection | The characteristic as an object to fill in | Root cause 10 to 11 Jun: the meaning duplicated the dimensions, then fabricated |
| L5 The reset to what the word does | 19 to 25 Jun | The question changed to "what does it do in the verse" | Antecedent, operation, object, manner, effect, transition, binding, direction, adjacency; seat as presence; discovery lookout; singleton rule | The word's function and relations | The strongest gain of the study; frames the working as doing, with states only as what a transition sets or removes |
| L6 The operation split into dimensions; verse-first lexical | 29 Jun to 3 Jul | D1 to D13: identity, source, seat or bearer, operation, object, manner, process, impact or produced state, coupling, colour, discovery, hidden meaning, cohabitation | The bearer; the produced state; coupling in the verse against cohabitation across the corpus; the verse as unit, genre-aware | One operation in one verse, fully decomposed | The source rule could not tell a driver from a restraint; cohabitation never built |
| L7 Characteristic, candidate, role, lexical cycle | 8 to 11 Jul | Axis A (candidate lemma) and axis B (role per occurrence); 16 per-span dimensions | The qualifier as a role; role is read, never derived | Who is the characteristic in this verse and what the others give it | A role is per word; a working is a relation among words |
| L8 Passage read guidance | 26 Jul to 7 Aug | The operation: subject, "state of, happening in, impacting on, impacted by", source, target; three phases | State or status as a form of operation; parties; a collection as bearer; hidden behind an act; linkage; action-type label | The inner being as the subject of operations | Not carried into the later stages |
| L9 Goal-derived dimensions; the by-role guide | 17 Sep to 19 Oct | Twelve dimensions derived from the definition; role by occurrence; the qualifier's values | Cognitive, affective, volitional, relational, orientational; permeability; embodied expression; science halves; read outward; never close on "not X" | What to look for, derived from the definition | Replaced by the collection reading; science extract not wired at BUILD 268 |
| L10 Analysis_phase_1 items; engagement | 27 Oct to 11 Nov | Eight kinds of finding; nine items; node roles; nuance rules | Polarity, mode, enactment, chain, route | A checkable item set for one verse | Every item is framed as an act; not continued |
| L11 The characteristic as an emergent pattern; surface groups; the layers | 13 to 15 Nov | The characteristic is "not a thing ... process, state, movement", inferred from a collection of behaviours; stages 1 to 5 | The state as a named kind of word (inner_being_state); lexical work split from inner-being work | What a collection gives, then what the working is in it | Stage 4, where the working is read, is not built |

**Each definition was applied to a bounded set and replaced when a problem surfaced; none was refined through its outcomes.** The elements, however, were mostly not refuted. They were renamed and not carried forward (lineage section 2).

### 5.1 The same parts under different names (corrected 2026-11-19; inference)

The first version of this concordance read the working as acts and operations only. The researcher's correction: behaviour is also states and conditions (sin, righteousness, life, death and many more), and it has qualifiers that define it. The record agrees: the definition itself opens with "states" (L1), the Passage guide defines the operation as the state of, or happening in, or impacting on, or being impacted by the inner being (L8), and the glossary says a characteristic is likely to be "a process, state, movement" (L11).

| Part of the working | Under the names |
|---|---|
| The bearer and the seat | the subject (L8); bearer and seat (D3, L6; L7); the party; the faculty as presence (L5) |
| **What the behaviour is, in its three forms** | **Act or operation** (what it does): operation (L5, L6, L8, L10). **State or condition** (what it is: sin, righteousness, life, death, pride, humility, weakness): "states" (L1), "state or status" (L8), D1 and the produced state D8 (L6), inner_being_state (L11). **Movement or transition** (what it becomes: a state set, removed, reversed, transformed): transition (L5), process (D7), movement (L8), chain (L10) |
| **What defines it: the qualifiers** | manner and intensity (L5); D6 manner and D9 coupling (L6); the qualifier role (L7); the qualifier's values: a measure, a strengthening, a ground, a cause, an object, a setting, the bait (L9); polarity and mode (L10); moral colour only where stated (L5, D10) |
| What it comes from, and acts on | source or antecedent (L5, D2, L8); the party and the route, permeability (L9, L10); object or target (L5, L8, L10) |
| What it produces | effect, the produced state (L5, D8); the immediate response (L5) |
| How workings link | the chain, the linkage or its absence (L8, L10); cohabitation across the corpus (D13, L6) |
| How it shows | the enactment, embodied expression, the act or refrained act that hides it (L1, L8, L10) |
| How it is read | the face and double meaning (L10); the passage, genre and speaker (L5, L6, L9); silence as a valid result (L5) |

If the concordance is right, the repeated redefinition was repeated renaming of a stable core, and pursuing one definition would not start from nothing.

### 5.2 How the inner being works, as the stages together support it

Set out in `outputs/escalation/2510-inner-being-definition-lineage-v1-20261119.md` section 3, for the researcher's correction: the inner being is not a list of parts; a working has a bearer and a seat; its behaviour is an act, a state or a movement; qualifiers define it; it stands in relations (source, object, effect, link, party); it is expressed or hidden; it is read in context and the reading varies; and a characteristic is what many such workings, gathered across the verses, give substance to. The critical reading is section 4 of the same document: the definition never excluded states and the instruments narrowed to acts; the working has no place in the programme prose; "characteristic" is used at four levels; two schemes share the D-codes; definitions were written for one stage and not handed on.

## 6. The test

The researcher: the only viable test is whether the outcome is sensible, reasonable and defendable. The record's earlier tests were different: a cold read against the lexical (24 Jun), an acceptance sample against the catalogue rules (14 Jul), the consistency of a reading technique (3 Aug), structural checks (2026-07-21 to 11-15). The first three were mechanical; the structural checks passed while the content was wrong (the stage 1 run). What the researcher names is a test of the outcome read by a person. It has been the test that found every gap (section 1.2 of the learning history), and it has never been written down as a step of the process.

## 7. A proposal, for decision (B:105; nothing is built)

To pursue a definition and not replace it:
1. Take the shape in 5.2 (lineage document section 3) as the working definition once the researcher has corrected it, and add a place for the state or condition of a being, which no item of the present set holds. Its sources: the Passage read guidance (26 Jul) and the by-role guide v2 (19 Oct), both signed off by the researcher, and the node roles. Mark what is not yet defined (how the parts are depicted as one working across nodes, c in section 3).
2. Apply it to one collection (`thought`, already opened) in small batches, as the by-role guide already requires (5.6: trial a few verses and have them checked before running the whole set).
3. Judge each batch by the researcher's test. A batch that fails does not replace the definition; the failure is recorded with the intervention it should have triggered (section 4).
4. Where an intervention recurs, record it as a rule of the reading. The how (what to check, how to keep a read consistent, where to read) is built from these recorded cases, not from a prior design.

This is a recommendation. Whether the by-role guide is in force for the working (stage 4), what the batch is, and whether the two uses of the surface group are to have two statements, are the researcher's decisions.

## 8. Placement of the open questions (researcher, 2026-11-19; #2510 v15)

The researcher's placement: how the inner being must be read belongs in the inner-being observations stage (stage 4); the open questions of the lineage document section 5 (grain, how a state and a transition are recorded and checked, cohabitation, the guides' standing) belong in the claims process (stage 5), where the answers are discovered from the observations. The study's order stands: finish reading the inner-being surface groups into observations, then formulate the claims. The blocks that aid discovery are crafted at stage 4. Detail and my inference of what stage 4 must record: `outputs/escalation/2510-inner-being-definition-lineage-v1-20261119.md` section 6. The proposal in section 7 is to be read in this light; nothing is designed or built.
