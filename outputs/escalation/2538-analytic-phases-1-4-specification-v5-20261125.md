# Analytic phases 1 to 4 of a collection: the complete specification (v5, 2026-11-25)

Written by Claude for Claude on the researcher's orders of 2026-11-25. It supersedes v4. It carries the researcher's rulings of 2026-11-25 (B1 and B2 granularity; the scope and routing of existing observations;
senses; the lifecycle of the subgroup dataset) and states every remaining point as a decision with its basis, so that no question is left open in it. The researcher does not re-read it; Claude works to it,
audits the code against it and shows measured results. Where a line is marked (derived) it is my decision from his words and the approved designs, not his words.

## 0. Sources and authority
Read: the researcher's words recorded verbatim in #2509, #2515, #2517, #2526, #2528, #2538, #2545, #2548, #2507, #2463, #2487, #2488; the chat of 2026-10-21 to 2026-11-25; the Programme book (approved 2026-11-20
as the single source); the 68 active `collection.*` method rules; the designs #2505, #2507, #2484, #2528 v2, #2538 validation plan v9, #2526. Authority, highest first: (1) his rulings of 2026-11-25 and his overview
of 2026-11-24; (2) his other words, later over earlier; (3) designs and rules he approved; (4) what I wrote and he did not approve (never binding). His "Step 1, Step 2" of 2026-11-24 are the steps of the flow.

## 1. The order of the work (his stage numbers are cross-references only)
| Order | Part | His stage | Unit and output |
|---|---|---|---|
| before | base data | none | verse_lexical, surfaces, the four groups, collections, the WordNet tables: complete before a collection is read; nothing here is rebuilt |
| A | Steps 1 and 2: grouping | 2 | the surface; every surface of the collection is allocated to a subgroup, and every surface through its Strong's codes has its verses |
| loop | for ONE subgroup at a time, in isolation: B1, B2, B3, B4, B5, C1, all on the SAME subgroup dataset (section 1A) | | |
| B1 | the word step | 1 | the surface (with its Strong's code): one observation for each distinct finding about it, with ONE NODE FOR EACH OCCURRENCE it holds in; the same surface in several verses is several nodes of one observation, not several observations |
| B2 | steps 1.1, 1.2 | 3 | the sense (concept): ONE OBSERVATION FOR EACH SENSE (a subgroup has one or several), traced to B1 |
| B3 | step 2.1 | 3 | what stands with the subgroup in the verses: one observation for each distinct finding of an item, with one node for each occurrence it holds in (several verses are several nodes of one observation), built on B2 and sometimes B1, traced |
| B4 | the sweep | 3 | marks or deletes what is still NULL |
| B5 | the evidence validation | 3 | the gate before C1 |
| C1 | step 3.1 | 4 | the elements of a behaviour, from the evidence (B2 senses first); ends the loop for the subgroup |
| after the loop | C2 step 3.2; C3 step 3.3; C4 the inner-being validation | 4 | the behaviours of the collection; across collections; the validation that completes the collection |
| not built | claims | 5 | not decided, not specified here |
B1 to B4 create EVIDENCE observations; C1 to C3 create INNER-BEING observations from the evidence (researcher 2026-11-25). Each of B1 to B4 produces very specific observations from the same data (section 3).
B1 reads each word in each verse for what it is and how it is used there. B2 gathers those readings into senses and traces each sense back to them. B3 reads what stands with the subgroup in each verse. None of
B1 to B3 says anything about the inner being; that begins at C1. B2 and B3 are about what the BASE DATA say about meaning and the differences in meaning, which cannot rest on the English surface alone: it
involves the Strong's code (researcher 2026-11-25).

## 1A. The scope, the subgroup dataset and the ledger

### The scope (researcher 2026-11-25; 2026-11-22)
"all observations that can be related to the collection and its verses is in scope." An observation is related to the subgroup if (a) a live node of it is on one of the subgroup's occurrences or carries the
collection, (b) it refers to a verse of the subgroup's verses, (c) it refers to a surface of the subgroup or a Strong's code of its words, or (d) its meaning relates (judged by reading). Deleted observations and
nodes are excluded. The loop works on the NODES of the subgroup: an observation that also holds nodes of another subgroup or another collection keeps those nodes; only the nodes of this subgroup are dealt with
here, and the observation is deleted when its last live node goes (a live observation has at least one live node) (derived: from "Deletion includes the node" and the rule that a node cannot outlive its observation).

### The subgroup dataset and its lifecycle (researcher 2026-11-25: "Lifecycle of the subgroup dataset: B1 - C1")
It is pulled ONCE at the start of B1 and used unchanged by B1, B2, B3, B4, B5 and C1; it is released when C1 closes for the subgroup. It holds:
1. the base data: the subgroup's surfaces with their Strong's codes; every verse they stand in with the full verse text and the full verse_lexical of each; the lexicon for each code (strong_meaning_tree, LSJ,
   Mounce); the WordNet pairings of the subgroup;
2. the old set: every old observation in scope as it stands at the start of B1, each with its fate tracked in the loop (re-applied, corrected, carried to B2/B3, kept with its marker, deleted);
3. NOT in it: the observations the loop itself writes. B2 reads B1's observations, B3 reads B2's, C1 reads the evidence, each live from the tables as the earlier steps record them.
If the grouping or the base data changes during the loop the dataset is discarded and the loop restarts for the subgroup. It is held as a working file under layer.working_dir (derived).

### The ledger: a record of processing, kept up to date as the work goes (researcher 2026-11-25)
The researcher will observe this table as the work proceeds. It is a tracking record, valuable for that: it is updated AT EVERY EVENT, never written at the end. A row is created when its step opens; it is updated when the
row is pulled, when it is answered, when it is checked and validated, when it is withdrawn and answered again, when the grouping retires or revives it; and each old observation in scope is itself tracked there (item
old-observation, one row for each, state: open, re-applied, corrected, carried forward, marked, deleted, deferred) so its fate is visible while the loop runs. Every update carries its run and its time.

### The ledger (what it is, answering the researcher's question of 2026-11-25)
The ledger is the table `collection_layer_item`, the app's control list of work. A ledger row is ONE UNIT OF WORK a step demands, derived from the data when the step is opened (never typed). It has a state
(open; observed; none, with its reason; retired), points to the observation or observations that answer it, and has a `validated` flag that only the check sets. It exists to meet the researcher's rule of
2026-11-15, "dont let things hang in the air": a step closes only when every one of its rows is answered and validated, and the next step does not open before. When the grouping changes, the rows the data no
longer demand are retired and the new ones added. The rows of each step in this specification:
- A: none (the grouping gate). B1: one row for each word of the subgroup (a surface with its Strong's code; a function word has none, except a negator and a connective), answered by the LIST of its observations, each naming the occurrences it holds in; the check demands that every occurrence of the word is in some observation. B2: one row for the subgroup's senses at 1.1 and
  one at 1.2, each answered by the LIST of sense observations, because the number of senses is a result of reading and cannot be derived beforehand; the check demands that every B1 observation of the subgroup is
  traced by exactly one sense. B3: one row for each (subgroup, item) and, for the pairing, each partner collection (so the rows come from the data), and one for each surface of the subgroup carrying more than one code; each row is answered by the LIST of its findings, each naming the verses (occurrences) it holds in, and the check demands that every occurrence the data show for the row is in some finding. No minimum number of verses. B4: one row for the subgroup (the sweep outcome). B5:
  none (a check). C1: one row for the subgroup. C2: one row for the collection. C3: one row for each unique match across the observations that reference more than one collection (section C3).

## 2. Rules that hold in every step
X1 Codified and repeatable: every operation is a verb of the app; no scratch helper; learning lives in code, database and config (2026-11-21).
X2 Targeted reads (2026-11-24): pull for the unit, process by the unit, write the result by the unit; every lookup indexed and chunked (RW-14); nothing read whole and then scanned.
X3 Validation is part of the build (2026-11-24). A step closes only when every row is answered and validated (LR-04). A file is checked whole and written in one transaction or refused; -Check writes nothing.
X4 Nothing is left in the air (2026-11-15, 2026-11-24): at the end every observation in scope is fixed or deleted, every word node complete or with its reason, every deferral owned by a named collection.
X5 Two markers (2026-11-22): evidence (states what the data are or show, tied to a verse) and inner_being (states how something works in the inner being, based on evidence; a building block of stage 5, not a claim).
   The marker follows content, never stage or role; set when the observation is created by the item answered.
X6 Observation rules: one observation for each finding, the same text never twice; concise; tied to its verses by reference; never a restatement of the verse (no run longer than max_verse_words_copied);
   basis stated or read; B1 to B3 say what the dictionary, the verses and the stored structure show and never what a word does for the inner being (node role lexical, no route) (RG, RW, RS, RO11, B:130-134).
X7 Node rules: a node cannot exist without a live observation nor a live observation without a live node; a node has one surface; each word node carries verse_reference, verse_lexical_id, surface, strong,
   morph_code, role, collection_id, subgroup_id, source_stage, seq; a column the data cannot give is left empty with its reason in disposition_note; a TRACED node (traced_observation_id set, no word columns)
   names the observation it rests on and never points at a deleted one.
X8 Every change keeps its reason in ib_observation_change; nothing is physically deleted (soft delete).
X9 Conduct: the specification before work; no scratch; observations created fresh by the verbs; nothing called compliant without the check that shows it; approval where the hook requires it; nothing committed before session close.

## 2A. The answers an existing observation can receive (defined once; each step says which apply and when)
ACCEPT (stays, marker set by content); SPLIT (more than one finding: one observation per finding first); RESTATE (said more than the verse shows or something the data contradict: made true and checked against the
base data; if it cannot be made true it is deleted with the reason); ADOPT (it states what the step's item asks: kept in place as that step's observation, nodes it lacks added, a node without a role given the
item's role, marker set); CONSUME (a new observation already says it: every word occurrence of it is on a live node of a carrier or named not carried with the reason, the mapping stated in words, the traces
re-pointed, `consumed_by` recorded, then deleted; never discarded without that verification); MERGE (same text as another live observation: its nodes move); DELETE (see below); CARRY FORWARD (a complex
observation that B1 cannot settle stays, still NULL, flagged to B2/B3, and B2 and B3 consider it first); COMPLETE A NODE (a missing column is filled from the data where the data give it; where they cannot, the
reason is written on the node). Each answer is made once, by one step, with its reason.
DELETE: an old observation in scope that is not re-applied or corrected and is still nature NULL, or is a duplicate, is marked deleted TOGETHER WITH ITS NODES (comment first, with the reason). Refused for one that is
already marked evidence or inner_being, and for one that another observation traces (that trace is repaired first). Where it holds nodes of another subgroup or collection, only the nodes of this subgroup go
and the observation is deleted when its last live node goes.
HOW OLD OBSERVATIONS ARE ROUTED (researcher 2026-11-25), replacing my earlier by-kind routing: B1 clears all the old observations in scope that have a verse, a surface or a Strong's code about the in-scope data.
At the end of B1 every old observation in scope that was not re-applied or corrected, and is still nature NULL or a duplicate, is deleted with its node. B1-scope observations usually have a single node; a complex
observation is carried forward to B2 and B3. B2 and B3 first consider the existing observations for correction, rather than creating new ones; this sets further old observations to evidence. The B4 sweep then
evaluates what is still NULL and deletes it. Measured 2026-11-25: thought has 211 older observations on its occurrences (156 prior-capture statements with no question code, 32 strand-reading key-statements,
others), depart 37; kind and question code cannot route them, so each is READ for what it states.

## 3. KINDS, NODES AND ROLES: exactly what each step writes
Kinds are the values of cfg_enum ib_observation.tag; roles of observation_role. A node role of `lexical` records that the word was read lexically and its inner-being role was not assessed.
| Step | kind | stage | nature | nodes | roles |
|---|---|---|---|---|---|
| B1 | term; face where the sense departs from the usual gloss | lexical | evidence | ONE word node for EACH occurrence the observation holds in (collection, subgroup, the occurrence's columns) | lexical |
| B2 1.1 (for each sense) | group | layer-1 | evidence | a word node on every occurrence the sense covers; a TRACED node on each B1 observation it covers (one B1 observation may hold occurrences of two senses: it is then traced by both) | lexical |
| B2 1.2 (for each sense) | enrichment | layer-1 | evidence | a word node on an occurrence carrying each Strong's code of the sense; a traced node on the sense's 1.1 observation | lexical |
| B3 pairing (a row for each partner collection), qualifier, entity | pairing (the configuration's kind for all three; the 2505 design's qualification and party kinds are inner-being and not used in B3) | layer-2 | evidence | word nodes on the subgroup's occurrences in the verse and on the partner words (partner collection on the node, or this one); a traced node on each B2 sense it builds on and, for one surface in a verse, its B1 | lexical |
| B3 direction | relation | layer-2 | evidence | as above | lexical |
| B3 double meaning (a surface with more than one code) | face | layer-2 | evidence | a node on each occurrence of the surface; traced to the B2 senses | lexical |
| B4 | none written | | | nodes of deleted observations are deleted | |
| C1 (the items role, polarity, object, enactment, operation, circumstance, flag; chain; party) | qualification or statement; statement; statement; statement; statement; statement; statement; link; party (route required) | layer-3 | inner_being | occurrence nodes within the occurrences of the evidence it rests on (or read back with verse and reason); a traced node on each evidence observation it rests on, B2 senses first | characteristic, qualifier, object, relational_target, enactment or standalone, chosen per occurrence from the verse |
| C2 behaviour | statement (the flag item, type discovery); relating findings: statement, link, party | layer-3 | inner_being | a traced node on each C1 observation it gathers; an occurrence node on the occurrences where it shows (IB-02) | as C1 |
| C3 | statement, link or party | layer-3 | inner_being | a traced node on the inner-being observations of both sides; occurrence nodes of both sides in the shared verses (partner nodes carry the partner collection) | as C1 |
The trace chain: C1 to B2 (and B3, B1); B3 to B2 (and sometimes B1); B2 to B1; C2 to C1; C3 to C1 and C2 of both collections. A node column the data cannot give is explained on the node.

## A. THE GROUPING (his stage 2): Steps 1 and 2
### Step 1: the grouping pull  [GroupPull]
- Pull: all surfaces of the collection and, from the WordNet tables, each surface's network group and its pairs with the other surfaces of the collection. Nothing else: no verse_lexical, no verse text, no
  observation (2026-11-24). Existing observations: none read or answered.
- Reading: group by meaning in context on the WordNet grouping the pull prepares (surfaces joined by a same_base or both pair are one seed group; a surface WordNet does not hold is a subgroup of its own). The
  grouping states nothing of the inner being (2026-11-15). The subgroups are INDICATIVE of words that may relate to each other and may differentiate or accentuate senses (2026-11-25); they are not the senses.
- Write: a working set, one row per surface. Checks: one row for each member surface; the seed grouping equals the WordNet grouping computed from the tables.
### Step 2: the subgroups  [GroupRecord]
- Place every surface WHOLE in one subgroup, never split by Strong's code (its codes are evidence of different senses, recorded in B1 and B2); name and define each subgroup in a sentence; a surface plainly not a member
  in meaning is set aside with its reason; an uncertain placement says what is open; a small collection is one subgroup by default (GP-01 to GP-04). The researcher's Subgroup instruction wins.
- Write: the subgroup tables; no JSON; each change a surface_event with its reason. Gate out: every surface placed or set aside with a reason, every subgroup holding a surface; then every surface through its
  Strong's codes has its verses (outcome of A, researcher 2026-11-25).
- NOTE for thought: its 7 subgroups were made on 2026-11-21 by the older verse-reading method, never by this step; they must be made by it (2026-11-20 Q3).

## THE SUBGROUP LOOP: ONE subgroup at a time, in isolation, all steps on the same subgroup dataset (section 1A)

## B1. THE WORD STEP: one observation for each distinct finding about a surface, with a node for each occurrence
- Gate in: the grouping is finished.
- Pull: the subgroup dataset (section 1A), pulled now.
- Existing observations (ruling 2026-11-25): B1 CLEARS all the old observations in scope that have a verse, a surface or a Strong's code about the in-scope data. For each: RE-APPLY it as the observation of its
  occurrence (adopt in place: role lexical, marker evidence, node completed), or CORRECT it (restate, checked against the base data), or CONSUME it into a new B1 observation, SPLIT a compound one, or DELETE it with its
  node(s) if it is not re-applied or corrected and is still NULL or is a duplicate. A complex observation (several nodes, or stating a group's meaning, a structure or an inner-being working) is CARRIED FORWARD to
  B2/B3, flagged. An observation already marked evidence or inner_being is not deleted here. When B1 is complete, no in-scope old observation is left that B1 could have settled.
- Reading, how: the unit is the surface with its lettered Strong's code, read in the verse of THIS occurrence (RG-21), never the bare lemma. Evidence in this order (RG-08, #2507 3.1): the verse text and the
  occurrence's stored structure (morph read: RG-14); the three meaning sources for the code read together, none picked; the ESV rendering across the word's verses, whether the English adds or hides, the literal
  sense beside the rendering; the M0.1, M0.4, M0.5 questions as prompts, a question that does not apply is not answered (RG-17). The meaning is judged in context from the Strong's code and the verse, not from the
  English surface alone. A function word in every occurrence has no observation except a negator and a connective (RG-22).
- Write: ONE observation for each distinct finding about the word (a surface with its Strong's code): the occurrences where it is used in the same way are NODES of one observation; an occurrence used differently, or a face, is
  its own observation (RW-03, RW-08) (kind and nodes: section 3). Text: what the word is and how it is used in THIS verse, naming the verse; concise; neither the dictionary range nor the
  verse restated; never what it does for the inner being. A different Strong's code of the same surface is a possible different sense: recorded here. A homonym or a name is recorded as such; a data error flagged,
  not fixed (RG-16).
- Checks (code): every occurrence of every content word is a node of some observation of its word (from the data); node columns; every old observation in scope answered or carried forward. Reading only: that each is true.
- Gate out: every occurrence is in an observation, validated; the clearing of the simple old observations is complete.

## B2. Steps 1.1 and 1.2: one observation for each SENSE (concept), traced to B1
- Ruling 2026-11-25: B2 is one per sense (concept) or subgroup, a subgroup having one or several senses; the inner-being workings will work more with the senses than with the surfaces; B2 uses traced nodes so it is
  traceable back to B1.
- Gate in: B1 closed for the subgroup. Pull: the subgroup dataset and the B1 observations just written.
- Existing observations: the old observations carried forward from B1 and any other that states what a sense is, or the Strong's meaning of its codes. CONSIDER THEM FIRST for correction rather than creating a new one:
  ADOPT or RESTATE the old observation AS the sense's observation (traced to B1, nodes completed); CONSUME where a new one says the same; DELETE what is left NULL and not applied. Adopted ones are set to evidence.
  An old observation stating what a sense does for the inner being is marked inner_being and waits for C1.
- Reading, how (1.1): SENSES ARE DRIVEN BY MEANING IN CONTEXT. Read the B1 observations of the subgroup and gather them into senses: the occurrences, of any surface and any Strong's code of the subgroup, whose meaning in
  context is the same are one sense. The same surface may carry different senses (it then has occurrences in several senses); different surfaces may carry one sense. It is vitally important to group the different
  senses of the surfaces by meaning in context, and the grouping rests on what the base data say about the meaning and the differences in meaning, that is on the Strong's code, the lexicon and the verse, not on
  the English surface alone. The subgroup is indicative of words that may relate to each other and differentiate or accentuate senses. Each sense is named for its meaning. A surface that fits no sense goes back to
  Step 2 with its reason. Never what the sense does for the inner being.
- Reading, how (1.2): for each sense, what the Strong's codes of its occurrences say: a short definition from the lexicon entries; the codes named as the link from the sense to its usage; what the different codes
  of one surface add.
- Write: for each sense, ONE group observation (1.1) and ONE enrichment observation (1.2); nodes and traces: section 3. Every B1 observation of the subgroup is carried by exactly one sense; a B1 observation no sense
  carries, or two senses carry, is a refusal. Never a none.
- Checks (code): the coverage and exactly-one rule; each sense's nodes equal the occurrences of the B1 observations it traces; every code of a sense has a node. Reading only: that the senses are the right ones.

## B3. Step 2.1: what stands with the subgroup in each verse
- Gate in: B2 closed. Pull: the subgroup dataset, with the WordNet pairings as the CONTROL (both, WordNet only, verse only) and the B2 and B1 observations.
- Existing observations: those carried forward from B1 and any other about the structure around the subgroup's word in a verse (pairings, negation and its reach, qualifiers, entities, direction, connectives,
  chains, double meaning). CONSIDER THEM FIRST for correction: ADOPT or RESTATE the old observation as the verse's observation (traced to B2/B1, the verse named), SPLIT one that spans several verses, CONSUME where a new
  one says the same; this sets them to evidence. An old observation stating how the inner being works is marked inner_being and waits for C1.
- Reading, how (from verse_lexical, which holds the structure; nothing evaluated that is not stored): the words that stand with the subgroup's surface and where each stands (side, distance from the stored
  positions); which belong to another collection; the WordNet control against them (a WordNet-only pairing is one to look for; a verse-only pairing has no control); negators and the word each reaches (adjacency is
  not scope: name the word reached); qualifiers and what each gives the word by the grammar; entities named or referred to, by name or pronoun; the direction of travel by the grammar; double meaning across verses.
  Differences in meaning are read from the base data (the Strong's code, the morph, the construction), not from the English alone.
- Write: ONE observation for each distinct finding of an item, with a node for each occurrence (each verse) it holds in; the same finding in several verses is several nodes of one observation (researcher 2026-11-25: "the
  same applies to B3"); a verse that shows something different is its own finding. One double-meaning observation for each surface of the subgroup with more than one code (section 3). Each subgroup's surface has its own
  observation; none joins two subgroups (they are pulled together at C2). No minimum number of verses. Traced to the B2 sense(s) it builds on and, for one surface in a verse, its B1.
- Checks (code): the rows equal the verses where the item is present in the data; nodes are the subgroup's occurrences and that verse's partner words only. Reading only: that each is true.

## B4. The sweep
- Pull: the old observations of the subgroup's scope that still have nature NULL after B1 to B3 (anything B1 carried forward and B2 and B3 did not take up).
- Reading: judge each by content: evidence, then it is marked; inner being, then it is marked and waits for C1; neither, then it is DELETED with its nodes (comment first); held by another collection, then
  its nodes here go and the observation is deferred to the named collection for the rest.
- Write: markers and deletions only, each with its reason. End state: no observation of nature NULL on the subgroup's scope except one deferred to a named collection (2026-11-24: if a non-inner-being NULL cannot be
  removed by the verbs, a verb is missing and is fixed; no scratch route).

## B5. The evidence validation (gate before C1)
- Scope: the subgroup's observations (section 1A). Checks (VA-06, v9 section 6, evidence column): every observation marked; none without a live node; no word node missing a required column without its reason; no
  live trace to a deleted observation; no two of one meaning; every B1 observation traced by a sense; every sense traced by the B3 observations built on it where there are any; every finding closed or deferred.
  Inner being is not judged here; the two validations are never run together.
- Reading only (limitation of the code: no content check exists): that each observation is true, founded and coherent with the others; I read and record it.

## C1. Step 3.1: the elements of the subgroup (the end of the loop for the subgroup)
- Gate in: B5 passes. Pull: the subgroup dataset; the evidence observations of the subgroup BY MARKER (the loop's own and the old ones kept as evidence), the verse text of ALL its verses; the definition and Strong's
  meaning by code. The base data is read back only occasionally, each time recorded with the verse and why (#2528 E3).
- Existing observations: the old observations marked inner_being (or judged so) on the subgroup's occurrences: each needs a trace to a live evidence observation or is self-evidencing (IB-07); ACCEPT with its traces,
  RESTATE if stronger than the evidence, CONSUME into a C1 finding that says the same, MERGE, SPLIT a compound, DELETE (cannot be made true or founded).
- Reading, how: what the evidence shows of the elements of a behaviour: what is done and its mode (the operation, with its chain), whether a refusal or a pursuit, what it is directed at, the outward act, the other
  party with the route, the circumstance, and what a qualifier or a variation of the word gives the working (the dimension). The inner-being workings work with the senses more than with the surfaces, so the B2
  senses are what findings rest on first. The role of each occurrence is chosen from the verse, never from the cluster (RG-03); a word holding nothing for the inner being takes standalone.
- Write: findings on the nine items (never meaning); kinds, nodes, roles and traces: section 3. Every B2 sense and every other evidence observation of the subgroup is rested on or declared not_used with its reason.
  A finding is a building block, never a claim.

## C2. Step 3.2: the behaviours of the collection (after all the subgroups)
- Pull: every inner_being observation of every subgroup of the collection, BY MARKER. Existing: older inner-being observations of the collection not yet answered, by the C1 list.
- Reading: discover the behaviours from the element observations; a behaviour may be one subgroup, part of one, or gather elements from several; a subgroup may form none; no claim.
- Write: each behaviour a flag finding of type discovery that names it and gathers its elements by traced nodes; findings relating elements across subgroups; every C1 observation gathered or declared not_gathered
  with its reason; at least one behaviour or a recorded none with its reason.

## C3. Step 3.3: across collections (RULED by the researcher 2026-11-25, replacing the earlier text of this section)
- What it does: it reads ALL the observations whose nodes reference more than one collection (any nature; the ones 3.2 and B3 recorded across collections) and creates ONE NEW OBSERVATION FOR EACH UNIQUE MATCH across all
  those observations. The match is the basis for a deeper analysis of the verses, to explore what the pairing means. Many matches will have no inner-being significance; that is known only later, so nothing is dropped
  or floored here: no minimum number of shared verses, no cap, no judgement of significance in 3.3.
- Critical dependency: the nodes of every underlying observation must reference BOTH (all) the collections the observation concerns, so that the 3.3 data can be extracted. 3.3 depends on 3.2 (and B3) recording the pairings
  correctly on the nodes (collection_id on each node, the partner's collection on the partner's node). A gate before 3.3 checks this and refuses with the observations whose nodes do not carry the collections.
- A match can span MANY verses (researcher 2026-11-25): the pairing of two surfaces across collections is one observation whose nodes are all those verses; the verses are inspected to observe whether they show a variety of implications or a single behaviour, and the observation says which. (Two words count as paired in a verse where nodes of one observation place them together; the match is then every such verse.)
- Volume: not quantifiable at this stage and its effect on the observations is not decided now (the researcher). The ledger row therefore follows the match, not a floor; the earlier "one row for each (subgroup, partner
  collection) that share a verse" is withdrawn.
- My decision where the ruling leaves the word open ("unique match"): a match is one distinct combination of the collections' surfaces (with Strong's codes) that nodes of one or more observations place together; the observation
  of a match carries, as traced nodes, each underlying observation it comes from, and the shared verses as occurrence nodes. If the researcher means a coarser unit (subgroup against partner collection), it is a change of the row derivation only.
- Gate in (2026-11-24): no partner collection in the observations is incomplete. The collection status is CHECKED FIRST; where it does not show a partner as complete, the researcher is ASKED and his answer is recorded.
- Gate out: C3 closes on the evidence layer passing; the inner-being validation completes after it.

## C4. The inner-being validation
- Starts after the loop, completes after C3 ("inner being validation can only complete after step 3.3 to remove the inner-being observations that cannot be traced", 2026-11-24). Checks (v9 section 6, IB-07): every
  inner-being observation traced to live evidence or self-evidencing; no reference to deleted evidence; every observation marked; no two of one meaning; no consumed deletion without its record; every finding
  closed or deferred. Repair first (find the evidence and trace it; create an evidence observation only when none states the fact and it earns its place; restate); delete last, with the reason.

## Completion of a collection, and the next partner
A collection is complete when every step is closed and validated, both validation layers pass, and every deferral to it has been taken up. "Which partner collection to introduce next" is decided by me with the
basis stated (the proof of the method is a collection built from nothing; return, then depart, profess); the researcher may overrule.

## D. Conflicts between his sources and what survived
C1 "Step 1" (flow) vs my ledger step "S1": the code and messages say "words" or B1. C2 stage numbering vs order of layers: the order of work (section 1). C3 2.1 granularity: by verse. C4 the 3-verse thresholds:
never his; removed. C5 inner-being validation timing: starts after the loop, completes after C3. C6 older evidence observations: kept, restated or consumed after verification; deletion only for NULL, duplicate, or
neither (his 2026-11-22 over my invented rule, withdrawn). C7 entry point: a collection. C8 grouping method: WordNet seed plus meaning in context, no verse reading. C9 concepts are replaced by collections.
D7 (his 2026-11-25): B1 one observation for each distinct finding about a surface, a node for each occurrence; B2 one per sense, traced to B1; B3 traced to B2 and sometimes B1. D8 (his 2026-11-25): old observations are routed by B1 clearing the in-scope ones, carrying complex
ones to B2/B3, B2 and B3 correcting first, B4 sweeping the rest. D9 (derived): kinds for B3 follow the configuration (pairing for pairing, qualifier and entity; relation for direction; face for double meaning).
D10 (derived): 1.1 and 1.2 are each one observation for each sense (his 2026-11-14 defines the two observation types). D11 (derived): an observation held by another subgroup or collection loses only the nodes of
this subgroup. D12 (derived): engagement is not a step of this specification; its observations, if present, are old observations like any other.

## E. Limitations that remain (stated, not open questions)
L1 No code check of content exists; I read and record each judgement (the Programme records this as unsolved). L2 Volume: the same surface in several verses is several nodes of one observation, not several observations (researcher 2026-11-25), in B1 and B3 alike; the number of observations is then the number of distinct findings, a result
of reading. (The by-verse rows of the first B3 audit, 470 rows for one subgroup, are not the design.) L3 The older observations (thought 211, depart 37) must each be read by me. L4 Thought's subgroups predate this
method and are regrouped by Step 2 before the loop runs on it.

## F. Status of the code against this file
Audited by running the verbs on a copy (register: 2538-code-against-specification-v3-audit-20261125.md, "FINAL MEASURED STATE"; its P3 is B1, P4 is B2, P5 is B3, P6 B4, P7 B5, P8 C1, P9 C4, P10 C2, P11 C3).
Code now written to this specification (2026-11-25): A grouping; B1 per-surface observations with a node per occurrence; B2 senses with traced nodes; B3 findings (rows per subgroup, item and partner collection, no minimum) with traces; old-observation answers including
carry, with node deletion; one subgroup dataset B1 to C1; continuous ledger (pulled_at, answered_at, checked_at, old-observation rows); C1 to C3 input by marker with partner collections read; 3.3 closes on the evidence layer; partner status checked then asked (`partner_complete`).
Measured: group 10/10; after phase 5 pass, 0 fail, 2 blocked; loop 120 pass with 3 harness-fixture failures not rerun. NOT shown: P9 closing order and P11.2 rows (need complete partner collections), content truth, thought regrouped, a completion status procedure (not built),
and nothing is applied live: the config/ledger migration awaits the researcher's approval. In this file "rows" always means ledger rows (collection_layer_item); a finding is an observation; an occurrence it applies to is a node.
