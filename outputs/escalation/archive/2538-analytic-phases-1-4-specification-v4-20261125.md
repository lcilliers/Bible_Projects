# Analytic phases 1 to 4 of a collection: the specification, step by step (v4, 2026-11-25)

Written by Claude for Claude on the researcher's orders of 2026-11-25 ("a line by line process by process handle on what analytic phase 1 - 4 should do and deliver", then: the how-to-read and the existing
observations are not one thing, they belong inside each step). It replaces v3, which kept the existing-observation handling in a separate section 3A; here each step carries its own. The researcher does not re-read
this file; Claude works to it, audits the code against it, and shows measured results. Nothing in the code is changed on the strength of it until the step has been audited (the audit register is
2538-code-against-specification-v3-audit-20261125.md; it is re-keyed to v4 in section 9).

## 0. Sources and authority
Read: the researcher's words recorded verbatim in #2509, #2515, #2517, #2526, #2528, #2538, #2545, #2548, #2507, #2463, #2487, #2488; the chat of 2026-10-21 to 2026-11-25; the Programme book extract of 2026-11-21
(approved 2026-11-20 as the single source); the 68 active `collection.*` method rules; the designs #2505, #2507, #2484, #2528 stage 4 design v2 ("Approve D1, D2"), #2538 validation plan v9, #2526 grouping proposal.
Authority, highest first: (1) the researcher's overview of 2026-11-24 (the message beginning "the S1 data pull", its correction, and the two after it); (2) his other words, later over earlier; (3) designs and rules
he approved; (4) what I wrote and he did not approve (never binding). A line marked (derived) is my reading, not his words. "Step 1, Step 2, Step 3" in his words are the steps of the flow; my code's ledger step
called "S1" is the word step of the word step and is a different thing (conflict C1).

## 1. The order of the work, and where your stage numbers fit
The researcher's stage numbers (2026-11-15) are: 1 lexical analysis of the words, 2 grouping of the surfaces, 3 verse-lexical observations, 4 inner-being analysis, 5 claims. They were set before he decided that
the grouping comes first (2026-11-24), so they do NOT give the order of work. This file is laid out in the ORDER OF WORK; his stage number is shown beside each part only as a cross-reference.

| Order | Part | His stage | What it is, and the unit it works on |
|---|---|---|---|
| before | base data | none | verse_lexical, the surfaces, the four groups, the collections, the WordNet tables: complete before a collection is read; nothing here is rebuilt |
| A | Steps 1 and 2: the grouping | 2 | the collection's surfaces become subgroups, the unit of reading. Unit: the surface |
| the loop | for ONE subgroup at a time, in isolation: B1, B2, B3, B4, B5, then C1 | | |
| B1 | the word step (ledger step "S1") | 1 | what ONE WORD (a surface with its lettered Strong's code) is and how it is used in EACH VERSE it stands in. ONE OBSERVATION FOR EACH SURFACE IN A VERSE (2026-11-25). Unit: the word in a verse. Example: "departed" (H3318G) in Exod 35:20 means going out from the presence |
| B2 | steps 1.1 and 1.2 | 3, layer 1 | what each SENSE (concept) of the subgroup means (1.1) and what its Strong's codes say (1.2). ONE OBSERVATION FOR EACH SENSE; a subgroup with several senses has several; each is TRACED back to the B1 observations it covers (2026-11-25). Unit: the sense. Example: depart, departed and departs, one sense, going away from a place |
| B3 | step 2.1 | 3, layer 2 | what stands with the subgroup's word IN EACH VERSE: the words beside it, negation, qualifiers, entities, direction. One observation per verse and item, built on B2 (and sometimes B1) and TRACED to them. Unit: the subgroup in a verse. Example: in Exod 35:20 "presence" stands after it and Moses is named as an entity |
| B4 | the sweep | 3 | what is still NULL after B1 to B3 |
| B5 | the evidence validation | 3 | the gate before C1 |
| C1 | step 3.1 | 4 | the elements of a behaviour, from the subgroup's evidence. Ends the loop for the subgroup |
| after the loop | C2 step 3.2, C3 step 3.3, C4 the inner-being validation | 4 | the behaviours of the collection; across collections; the validation that completes the collection |
| not built | claims | 5 | not decided and not specified here |

The difference between B1, B2 and B3 in one line: B1 reads each WORD in each verse for what it is and how it is used there; B2 gathers those readings into the SENSES of the subgroup and traces each sense back to them; B3 reads what STANDS WITH it in each verse, building on B2 and sometimes B1, with traces. None of the three
says what a word does for the inner being; that begins at C1.
Why B1 is placed first in the loop although it is his stage 1 and the grouping (his stage 2) comes before it: the words are read inside the subgroup of their surface (2026-11-24: for each subgroup "pull the full
verse-lexical ... then do 1.1 and 1.2"), and 2026-11-20 says lexical meaning comes first. His overview of 2026-11-24 does not name B1 (gap G1); it is the one step placed on the strength of his earlier words only.

## 2. Rules that hold in every step (stated once; each step says how it applies them)
X1 Codified and repeatable: every operation is a verb of the app, the same result every time; no scratch helper per collection; learning lives in code, database and config (2026-11-21).
X2 Targeted reads (2026-11-24): never read everything into memory and then scan; pull for the unit, process by the unit, write the result by the unit; pull data specific to the read when looking across units;
   every lookup is pinpointed, indexed and chunked (RW-14).
X3 Validation is part of the build, not after-the-fact repair (2026-11-24). A step closes only when every row it demands is answered by an observation with nodes, or by a recorded none with its reason, and the
   check has validated it (LR-04); the next step does not open before it. A whole file is checked whole and written in one transaction, or refused entirely; -Check previews and writes nothing.
X4 Nothing is left in the air (2026-11-15, 2026-11-24): at the end every observation of the scope is fixed or deleted, every word node complete or with its reason, every deferral owned by a named collection.
X5 Two markers only (2026-11-22): evidence (states what the data are or show, tied to a verse) and inner_being (states how something works in the inner being, based on evidence; a building block of stage 5,
   not a claim). The marker follows content, never stage and never the node's role; it is set when an observation is created, by the item answered (a file never sets it).
X6 Observation rules: one observation per finding, the same text never twice; concise; tied to its verses by reference; never a restatement of the verse (no run of more than max_verse_words_copied words); basis
   stated or read; node roles chosen per occurrence from the verse, never from the cluster; the lexical phases (1 and 3) say what the dictionary, the verses and the stored structure show and never what a word does
   for the inner being (node role lexical, no route) (RG, RW, RS, RO11, B:130-134).
X7 Node rules: a node cannot exist without a live observation, nor a live observation without a live node; a node has one surface; each word node carries verse_reference, verse_lexical_id, surface, strong,
   morph_code, role, collection_id, subgroup_id (from stage 3 on), source_stage, seq; a column the data cannot give is left empty with its reason in disposition_note; a trace to a deleted observation is refused.
X8 Every change keeps its reason in ib_observation_change; nothing is physically deleted.
X9 Claude's conduct: the specification before work; no scratch; observations created fresh by the verbs; nothing called compliant without the check that shows it; approval where the hook requires it; nothing
   committed before session close.

## 2A. The answers an existing observation can receive (defined once; each step below says which apply to which observations, and when)
An existing observation is live, has a live node on an occurrence the step reads, and was not written by this build. These are the only things that may be done with one (RS-04, RW-13, VA-02 to VA-05, v9):
- ACCEPT: it stays as it is, with its marker set by content. - SPLIT: it holds more than one finding, so it becomes one observation per finding first (v9 section 5).
- RESTATE: it says more than the verse shows or something the data contradict; its wording is made true and the new wording is checked against the base data. If it cannot be made true it is DELETED, with the reason.
- ADOPT: it states what the step's item asks; it is kept in place, the nodes it lacks for the demanded occurrences are added, a node without a role gets the item's role, and its marker is set (RS-04, #2507 section 9).
- CONSUME: a new observation of this build already says it. Every word occurrence of it is on a live node of a carrier or is named as not carried with its reason; the mapping is stated in words; the traces to it
  are re-pointed; `consumed_by` is recorded; only then is it deleted. It is never discarded without that verification (2026-11-22).
- MERGE: the same text as another live observation; its nodes move to the one kept.
- DELETE AS NEITHER: by content it states neither evidence nor inner being. Comment first with the reason and the occurrences no other live observation holds; then deleted. Refused for one that is already marked or
  that another observation traces (repair that trace first), and for one that another subgroup or collection also holds (see DEFER).
- DEFER: another subgroup or collection holds it. It is marked now and the finding is left to that named collection, recorded; or it is answered where all its holders are read (v9 principle 14).
- COMPLETE A NODE: a node of a kept observation that lacks a required column is completed from the data where the data give it (collection from the surface; surface and strong from the occurrence; verse from the
  verse table); where they cannot (the role an older word had, say) the reason is written on the node.
Each answer is made once, by one step, with its reason.
WHICH STEP ANSWERS AN EXISTING OBSERVATION is decided by READING WHAT IT STATES, not by its kind, stage or question code (RS-04: the stage never filters). Measured on 2026-11-25 on the rolled-back database: the older
observations on thought's occurrences are 211: 156 prior-capture statements with no question code, 32 strand-reading key-statements, 4 prior-capture faces, 3 verse-reading no-impact, 2 engagement statements, 2
engagement silences, 1 link, 1 reading statement (9 carry a marker already); on depart's occurrences 37 (34 prior-capture statements, 2 links, 1 verse-reading). Kind and question code therefore cannot route them: each
is read, and by what it states it belongs to B1 (one word in one verse), B2 (a sense or the Strong's meaning), B3 (what stands with the word in a verse), or the inner-being layer (C1). A single observation may state
several of these: it is split first. The step lists below say what each step looks for; they do not say which kinds belong to it.

## A. THE GROUPING (his stage 2): Steps 1 and 2

### Step 1: the grouping pull  [GroupPull]
- Gate in: the collection's index is complete (every member surface has a row).
- Pull: all surfaces of the collection and, from the WordNet tables, each surface's network group and its pairs with the other surfaces of the collection. Nothing else: no verse_lexical, no verse text, no
  observation, no verse (2026-11-24: "It is not necessary to pull the entire verse-lexical at this stage").
- Existing observations: none are read here; none are answered here.
- Reading: group by meaning in context, using the WordNet grouping as the basis the pull prepares: surfaces joined by a same_base or both pair are one seed group; a surface WordNet does not hold is a subgroup of its
  own. The grouping states nothing of the inner being (2026-11-15: "the surface groups has nothing to do with the inner being. it is about the meaning of the surface words").
- Write: a working set with one row per surface (file or memory).
- Checks: one row per member surface; the seed grouping equals the WordNet grouping computed from the tables. Gate out: Step 2.
- Sources: 2026-11-24 overview and its correction; 2026-11-15 #2509; 2026-11-21 Q3 to Q6 (#2526); GP-01. Replaces the dictionary-meaning method the researcher rejected on 2026-11-15.

### Step 2: the subgroups  [GroupRecord]
- Pull: the Step 1 set. Existing observations: none read or answered here.
- Reading: place every surface WHOLE in one subgroup, never split by Strong's code (its codes are its hidden meanings, recorded in the word step and step 1.2); name each subgroup and define in a sentence the meaning
  its surfaces share; a surface plainly not a member in meaning is set aside with its reason (the change procedure moves it out of the collection); an uncertain placement is marked uncertain and says what is open;
  a small collection is one subgroup by default (GP-01 to GP-04). The researcher's Subgroup instruction wins over mine.
- Write: the subgroup tables (collection_subgroup, collection_subgroup_surface); no JSON; every change a surface_event with its reason; the nodes of a placed surface take its subgroup.
- Checks (GroupRecord): every surface answered once; each subgroup named once, defined, holding a surface; a surface answered by code refused; the whole file or nothing. Gate out: every surface placed or set aside
  with a reason, every subgroup holding a surface (the grouping gate). Before 3.3 uses a collection's status the status is checked and the researcher is asked (G5).
- Sources: 2026-11-24 ("the output is updating the sub group table. no json required. missing wordnet item - treat them as a subgroup on their own"); 2026-11-21 Q4.
- NOTE for thought: its 7 subgroups were made on 2026-11-21 by the earlier verse-reading method; they were never made by this step and must be (researcher 2026-11-20 Q3).

### THE SUBGROUP LOOP (B1 to B5 and C1): ONE subgroup at a time, in isolation. Every pull is limited to that subgroup's surfaces and the verses they stand in; nothing of another subgroup is read.

## B1. THE WORD STEP (his stage 1; the first step of the loop; ledger step "S1")
Settled by the researcher on 2026-11-25: B1 is ONE OBSERVATION FOR EACH SURFACE IN A VERSE; B2 is one observation for each SENSE (concept) of the subgroup; both are needed, and B2 is traceable back to B1 by traced nodes.

### B1. The word step: one observation for each surface in a verse
- Gate in: the grouping is finished (every surface placed or set aside, every subgroup holding a surface).
- Pull: the ONE SUBGROUP DATASET, pulled once and used by B1 to C1 alike: the subgroup's surfaces with their lettered Strong's codes; every verse they stand in, with the full verse text and the full verse_lexical of
  each verse; the lexicon for each code (strong_meaning_tree, the lexicons LSJ and Mounce); the existing observations with a live node on those occurrences; the WordNet pairings.
- Existing observations MET HERE: the older observations on a single surface in a verse (whatever of any kind or stage states what one word is and how it is used in one verse; typically verse-reading M0.1, M0.4, M0.5 readings, face observations, and the single-word statements among the prior-capture ones), of
  nature evidence or NULL. Each is matched to the occurrence it is about (its node's verse_lexical_id; RS-02). Ask: does it state what THIS word is and how it is used HERE? Then ADOPT it in place as that
  occurrence's observation (given the role lexical, the marker evidence, its node completed), RESTATE it if it overstates, CONSUME it if a new observation of this occurrence already says it, SPLIT it if it holds
  several findings (an older observation that covers several occurrences becomes one per occurrence), DELETE AS NEITHER, COMPLETE its nodes. An older observation about a pairing, a group's meaning, a qualifier or
  an entity, or about how the inner being works, is NOT answered here: it waits for its own step and stays visible.
- Reading, how: the unit is a word (surface with lettered code) read in the verse of THIS occurrence (RG-21, never the bare lemma, never aggregated across codes). Evidence in this order (RG-08, #2507 3.1): the
  verse text and the occurrence's stored structure (morph read, not carried: RG-14); the three meaning sources for the code read together; the ESV rendering across the word's verses, whether the English adds or
  hides, the literal sense beside the rendering; the M0.1, M0.4, M0.5 questions as prompts, a question that does not apply is not answered (RG-17). A function word in every occurrence has no observation except a
  negator and a connective (RG-22).
- Write: ONE observation for each occurrence of a content word of the subgroup (kind term; face where the sense departs from the usual gloss, RG-09; stage lexical; nature evidence) with ONE node on that
  occurrence (role lexical). Text: what the word is and how it is used in THIS verse, naming the verse; concise; neither restating the dictionary range nor the verse; never what it does for the inner being. The
  different codes of one surface are its possible hidden meanings: recorded here as evidence (2026-11-21 Q3). A homonym or a name is recorded as such; a data error is flagged, not fixed (RG-16).
- Checks (code): one observation for each occurrence of each content word of the subgroup (from the data); the node columns; every existing observation of this step answered. Reading only: that each is true.
- Gate out: every occurrence of every content word has its observation, validated, before B2.
- Sources: 2026-11-14 ("I expect an observation for the surface in the verse (that is lexical work, and layer 1 will build on it)"); 2026-11-25 ("B1 = one per surface in a verse"); #2507 section 3.1 ("per verse
  and per member occurrence"); RS-02.
- NOTE: the code's word step writes one observation for each SENSE of a word with a list of occurrences. That is the shape of B2, not of B1 (D7).

## B2 to B5. GROUP AND STRUCTURE OBSERVATIONS (his stage 3; the loop continues)

### B2. Steps 1.1 and 1.2: one observation for each SENSE (concept) of the subgroup, traced back to B1
Settled 2026-11-25: "B2 = one per sense (concept) or sub group (some sub groups have multiple senses)"; "the inner being workings will be working more with the senses than the individual surfaces"; "B2 must not
forget to use the nodes to capture the traces for the senses to ensure that B2 is traceable back to B1".
- Gate in: B1 closed for the subgroup.
- Pull: the same subgroup dataset, with the B1 observations just written.
- Existing observations MET HERE: older observations that state the meaning of a group of surfaces or a concept the subgroup now holds, or the Strong's meaning of its codes, of nature evidence or NULL. Ask: does it
  state what this sense is, as the dictionary gives it? ADOPT (kept as the sense's observation, traced to the B1 observations of its occurrences), RESTATE, CONSUME into the sense observation that says the same,
  SPLIT, DELETE AS NEITHER. An older observation that says what the sense does for the inner being is an inner-being observation: it is marked so and waits for C1. Concept observations of the retired concept
  method: consumed or deleted (concepts were replaced by collections, 2026-11-20 Q5).
- Reading, how (1.1): read the B1 observations of the subgroup together and form its senses: the occurrences whose B1 observations state the same meaning are one sense. A subgroup with one meaning has one sense;
  one with several (the same word used in different ways, or surfaces of a family that part in meaning) has several. A sense is named for its meaning, in words the Strong's meaning of the codes supports. A surface
  that does not fit any sense goes back to Step 2 with its reason; it is not forced in. Never what the sense does for the inner being.
- Reading, how (1.2): for each sense, what the Strong's codes of its occurrences say: a short definition from the lexicon entries (for example what meditation means); the codes named as the link from the sense to
  its usage; what the different codes of one surface add (the hidden meaning).
- Write: for each SENSE of the subgroup, ONE observation (1.1: kind group; stage layer-1; evidence) and ONE observation (1.2: kind enrichment; stage layer-1; evidence). Each carries (a) a TRACED NODE on EACH B1
  observation of the occurrences the sense covers (the trace back to B1), and (b) occurrence nodes (role lexical) on those occurrences; the enrichment has a node for every Strong's code of the sense. Every B1
  observation of the subgroup is carried by exactly one sense (none left out, none in two); a surface occurrence that no sense carries is a refusal. Never a none.
- Checks (code): every B1 observation of the subgroup is traced by exactly one 1.1 sense; each sense's nodes equal the occurrences of the B1 observations it traces; every code of a sense has a node.
  Reading only: that a sense is true and that the senses are the right ones.
- Sources: 2026-11-14 (layer 1 step 1 and 2: "each grouping becomes an observation with the surfaces as the nodes"; "each enrichment becomes an observation with the related strongs as the nodes"); 2026-11-24
  ("do 1.1 and 1.2 and create or update every observation / node that applies"); 2026-11-25 (above); #2505.
- NOTE: the code writes ONE 1.1 and ONE 1.2 observation for the whole subgroup with nodes on every occurrence and no traced nodes to B1. That is the single-sense case without the trace (D7).

### B3. Step 2.1: the pairings, by verse
- Gate in: 1.2 closed for the subgroup.
- Pull: as 1.1, with the WordNet pairings as the CONTROL: for each partner collection, the verses where the verse-lexical shows it beside the subgroup and the verses where only WordNet relates it (both, WordNet
  only, verse only).
- Existing observations MET HERE: older observations of the structure of the verse around the subgroup's word: pairings with other words, negation and the word it reaches, qualifiers, entities and pronoun
  reference, direction, connectives, chains, double meaning (the structural verse-reading observations, M0.6.x, and the like), of nature evidence or NULL. Ask of each, per verse: does it state a structure the
  data show? ADOPT or RESTATE it into that verse's observation (the nodes added, the verse named), CONSUME it into the new observation of that verse (an older observation that spans several verses is SPLIT, or
  consumed by several), DELETE AS NEITHER, and mark as inner-being (waiting for stage 4) any that says how the inner being works rather than what the structure is. This is "update existing observations that is
  about pairing, and create new observations by verse" (2026-11-24).
- Reading, how (from verse_lexical, which holds the structure; nothing is evaluated that is not stored): the words that stand with the subgroup's surface and where each stands (side and distance, from the stored
  positions); which belong to another collection and which stand out; the WordNet control against them (a WordNet-only pairing is one to look for, a verse-only pairing has no control); negators and the word each
  reaches (adjacency is not scope: the observation names the word reached); qualifiers and what each gives the word by the grammar (what it gives the behaviour is stage 4); entities named or referred to, by name
  or pronoun, and whether they differ from verse to verse; the direction of travel by the grammar. Double meaning: a surface that carries more than one Strong's code, compared across its verses.
- Builds on: the B2 sense observations (and, where an observation is about one surface in one verse, that B1 observation). Every B3 observation carries a TRACED NODE on each B2 sense observation (and each B1
  observation) it builds on, so it can be followed back (2026-11-25: "B3 will build on B2, and sometimes B1 - again the traces are captured in the nodes").
- Write: ONE observation for each (subgroup, verse) and item present (pairing, qualifier, entity, direction), kind pairing, qualification, party or relation as the item says, stage layer-2, nature evidence, role
  lexical, nodes on the subgroup's occurrences in that verse and on the partner words of that verse; ONE double-meaning observation (kind face) for each surface of the subgroup carrying more than one code. Each
  subgroup's surface has its own observation in a verse; none joins two subgroups (they are pulled together at 3.2). No minimum number of verses.
- Checks (code): the rows equal the verses where the item is present in the data; the nodes are exactly the subgroup's occurrences and partner words of that verse. Reading only: that each is true.
- Sources: 2026-11-14 (layer 2 step 1); 2026-11-24 (by verse; WordNet as control; "each subgroup surface will have its own observation"); #2505, #2507 section 3.1 (the structure items); decision D1 (section D).

### B4. The sweep: what is left with nature NULL
- Pull: the older observations that still have nature NULL and a live node on the subgroup's occurrences after the word step, 1.1, 1.2 and 2.1. Reading: judge each by content (answers above): by now an
  older observation that states a sense, a group meaning or a verse structure has been answered by its own step. What remains is judged: evidence, inner being (mark it), neither (DELETE AS NEITHER, in the loop),
  held by another subgroup or collection (DEFER). 2026-11-24: "inspect all the remaining observations with null nature and any observations that is not clearly inner being related ... candidates for deletion";
  "All non-inner-being observations with null nature should now be deleted. If not, then something went wrong that need to be fixed, not just to perform a scratch method".
- Write: deletions and markers, each with its reason; no observation of nature NULL is left on the subgroup's occurrences except one deferred to a named collection. If one cannot be answered by the verbs, a verb is
  missing: it is fixed in the code, not removed by a scratch route.

### B5. The evidence validation (the gate before 3.1)
- Scope: the subgroup's observations (a live node on its occurrences or its verses). Checks (VA-06, plan v9 section 6, the evidence column): every observation marked; none without a live node; no word node missing a
  required column without its reason; no trace to a deleted observation; no two observations of one meaning; every word has its word-step observations; the subgroup its stage 3 ones; every finding closed or deferred to a
  named collection. Inner being is not judged here. 3.1 does not open until it passes. Evidence and inner-being validation are never run together.
- Reading only (gap G7): that each observation is true, founded and coherent with the others (2026-11-22 (c)); I read and record.

## C. INNER-BEING ANALYSIS (his stage 4)

### C1. Step 3.1: the elements of the subgroup  (the end of the loop for the subgroup)
- Gate in: the evidence validation of the subgroup passes.
- Pull: the same subgroup dataset; "dump the data in memory and extract the evidence observations + verse text for all the verses in the subgroup" (2026-11-24): the evidence observations of the subgroup by MARKER (the build's and the older
  ones kept as evidence), the verse text of ALL its verses, the subgroup's definition and Strong's meaning by code. The base data is read back only occasionally, each time recorded with the verse and why (#2528 E3).
- Existing observations MET HERE: the older observations marked inner_being (or judged so now) on the subgroup's occurrences. Ask: does it state how something works in the inner being, based on evidence? It needs
  a trace to a live evidence observation or is self-evidencing (it quotes its verse in full and holds a node for every word it relies on) (IB-07). ACCEPT it with its traces, RESTATE it if stronger than the evidence,
  CONSUME it into a 3.1 finding that says the same, MERGE, SPLIT a compound one first, DELETE AS NEITHER (cannot be made true or founded), DEFER if another collection holds it. It counts for nothing in the check
  and nothing is demanded of it (IB-05), but it is answered, not left.
- Reading, how: what the evidence shows of the elements of a behaviour of the inner being: what is done and its mode (the operation, with its chain), whether a refusal or a pursuit, what it is directed at, the
  outward act, the other party with the route, the circumstance, and what a qualifier or a variation of the word gives the working (the dimension). The role of each occurrence is chosen from the verse, never from the
  cluster (RG-03); a word that holds nothing for the inner being takes standalone, so a word not read can be told from one read and found empty.
- Write: findings on the items role, polarity, object, enactment, party (with route), circumstance, operation, chain, flag (never meaning, which is the word step); each finding is one observation, kind per item, stage
  layer-3, nature inner_being, resting on named evidence by a TRACED node on each (the B2 sense observations first, because the inner-being workings work with the senses more than with the individual surfaces; the B3 and B1 observations where the finding needs them) and carrying occurrence nodes with a role other than lexical that lie within the occurrences of the evidence it rests on (or are
  read back with the verse and the reason). Every stage 3 observation of the subgroup is rested on or declared not_used with its reason. A finding is a building block, never a claim.
- Checks (code): the above, from the tables. Sources: 2026-11-24; 2026-11-21 Q7; #2528 design v2; IB-01 to IB-07.

### C2. Step 3.2: the behaviours of the collection  (after all the subgroups)
- Pull: "pull all the observations of all the subgroups for inner being" (2026-11-24): every inner_being observation of every subgroup of the collection, by marker (the build's 3.1 and the older ones kept).
- Existing observations MET HERE: older inner-being observations of the collection not yet answered: answer by the same list as 3.1.
- Reading, how: discover the behaviours from the element observations: a behaviour may be one subgroup, part of one, or gather elements from several; a subgroup may form none. It states no claim about what the
  behaviour is.
- Write: each behaviour is a finding of the item flag, type discovery, that names it and gathers its element observations by traced nodes, saying which elements belong together and why; findings of operation, chain,
  party, circumstance or role that relate elements across subgroups. Every 3.1 observation is gathered or declared not_gathered with its reason; at least one behaviour or a recorded none with its reason.

### C3. Step 3.3: across collections
- Gate in: no partner collection in the observations is incomplete: "check against the collection status"; "collection status - first check then you ask me" (2026-11-24). It does not open before.
- Pull: "a pull of all the inner being observations for all the collections in scope" (2026-11-24): this collection's and its partner collections', by marker.
- Existing observations MET HERE: the partner collections' inner-being observations are input, not answered here; this collection's remaining older inner-being observations by the 3.1 list.
- Reading, how: how the workings of this collection's subgroups and of the partner collection relate in the verses they share; where the shared verses show no working together, none, with the reason.
- Write: findings that rest on named inner-being observations of both sides (a traced node on each) and carry nodes of both sides in the shared verses. Rows: one for each subgroup and partner collection that share a
  verse (the 3-verse minimum is withdrawn: never the researcher's).
- Gate out: 3.3 closes on the evidence layer passing (the inner-being validation is not required to have finished: it completes after 3.3).

### C4. The inner-being validation
- Starts after the loop, completes after 3.3 ("inner being validation can only complete after step 3.3 to remove the inner-being observations that cannot be traced", 2026-11-24). Checks (v9 section 6, IB-07): every
  inner-being observation traced to live evidence or self-evidencing; no reference to deleted evidence; every observation marked; no two of one meaning; no consumed deletion without its verified record; every
  finding closed or deferred. Repair first: find the evidence and trace it, create an evidence observation only when none states the fact and it earns its place, restate; delete last, with the reason.

### Completion of a collection, and the next partner
- A collection is complete when every step above is closed and validated, both validation layers pass, and every deferral to it has been taken up. There is no recorded completion status (G5). "Which partner
  collection should be introduced next" is the researcher's; the proof of the method is a collection built from nothing.

## D. Conflicts between the researcher's sources, and what survived
C1 "Step 1" (flow) vs my ledger step "S1" (words): the code and messages say "words" for mine. C2 stage numbering vs the order of the layers: resolved by the 2026-11-24 order (section 1).
C3 2.1 granularity: by verse (2026-11-24) over per group (2026-11-14, #2505). C4 3-verse thresholds: never his; removed. C5 inner-being validation timing: starts after the loop, completes after 3.3.
C6 older evidence observations: kept, restated or consumed after verification; only NULL nature is swept (2026-11-22 over my invented rule "kept only as inner being", withdrawn). C7 entry point: a collection.
C8 grouping method: WordNet seed plus meaning in context, no verse reading, over the dictionary-meaning method rejected 2026-11-15. C9 concepts: replaced by collections (2026-11-20 Q5).
D1 decision: 2.1 is by verse, group-relation removed; basis: his later 2026-11-24 words over the earlier per-group design. D3: the word step stays, first in the loop.
D7 (the researcher, 2026-11-25): B1 is one observation for each surface in a verse; B2 is one for each sense (concept), a subgroup having one or several; B2 traces to B1 and B3 to B2 (and sometimes B1) by traced
nodes. Supersedes my earlier design of a word step that wrote one observation per sense of a word, and of one 1.1 and one 1.2 for the whole subgroup.
D6 decision (derived): an older observation is answered by the step whose new observation carries what it says, not at the first row that touches it.

## E. Gaps (not settled by his words, or not built)
G1 the word step's place in his flow; G2 engagement (a precursor in the Programme; run #2412 withdrawn; not checked); G3 the shape of the 3.3 rows beyond the pull; G5 no collection completion status; G6 the order of
collections and the size of a sitting; G7 no code check of content (only my reading, recorded); G8 the by-verse volume (470 rows and 1,681 nodes for one subgroup of a 6-surface collection, measured); G9 the node
columns of older pipelines (hundreds of nodes lack role or collection); G10 the per-surface observation of a verse that holds surfaces of two subgroups, not verified in code; G-i the code demands every older
observation at the first row that touches it (the word step), not at the step that carries it.

G13 older observations are mostly free-text prior-capture statements and cannot be routed by kind: each must be read, by me, one by one (thought 211, depart 37), and the code has no help for that beyond the pull; G11 how the senses of a subgroup are fixed when the B1 readings are mixed (a judgement of reading, recorded with its reason); G12 volume: one observation for each surface in a verse is about as many observations as content-word occurrences of the collection.

## F. Status of the code against this file
Audited by running the verbs on a copy (register: 2538-code-against-specification-v3-audit-20261125.md). Its labels map to this file as follows: its P1 and P2 are Steps 1 and 2 (A); its P3 is B1 (the word
step); P4 is 1.1 and 1.2 (B2); P5 is 2.1 (B3); P6 is the sweep (B4); P7 the evidence validation (B5); P8 is 3.1 (C1); P9 the inner-being validation (C4); P10 is 3.2 (C2); P11 is 3.3 (C3); P12 completion.
Result, corrected after the researcher's rulings of 2026-11-25 (D7): the code conforms on Steps 1 and 2, and on B3 as to what is pulled and written (but B3 carries no traced nodes to B2 or B1). It does NOT
conform on B1 (it writes one observation for each SENSE of a word with a list of occurrences; the specification is one for each surface in a verse) nor on B2 (it writes one 1.1 and one 1.2 for the whole
subgroup, with no traced nodes to B1; the specification is one for each sense of the subgroup, traced to B1). It also does not conform on: the existing-observation handling in every step (G-i, and the loop's
missing verbs for older observations already marked whose nodes are incomplete and for another collection's unmarked observations); C1 (12 verse texts; older kept evidence not offered; it does not rest on B2
senses); C2 (an inner-being observation of another build not offered); C3 (partner collections never read, a 3-verse threshold, closes on both layers); no completion status; no single subgroup dataset (each step
pulls its own slice). Nothing is repaired on the strength of this file until the researcher has seen it.
