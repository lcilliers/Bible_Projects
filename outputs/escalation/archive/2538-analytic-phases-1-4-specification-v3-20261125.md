# Analytic phases 1 to 4 of a collection: the collated specification, process by process (v3, 2026-11-25)

Written by Claude for Claude on the researcher's order of 2026-11-25: "you cannot build a system from a single sentence. you will have to collate my guidance across multiple escalations, check it
against your multiple attempts to draft certain parts of it, then decide which guidance survived. Check it again [with] the final complete overview I wrote yesterday. until you have a line by
line process by process handle on what analytic phase 1 - 4 should do and deliver there is no sense or reason to try and fix anything."
This supersedes v2 (2538-layered-reading-specification-v2-20261125.md, built from the chat of one day and the method rules only). Nothing in the code is fixed on the strength of this file until each
process below has been audited against it (section 12). The researcher does not re-read this file; Claude works to it and shows results.

## 0. How the collation was done, and what rules the collation

Sources read in full or in the parts named: the researcher's words recorded verbatim in #2509, #2515, #2517, #2526, #2528, #2538, #2545, #2548, #2507, #2463, #2487, #2488 (escalation comment
fields); the chat of 2026-10-21 to 2026-11-25 (session transcripts); the Programme book extract of 2026-11-21 (approved 2026-11-20 "as the single source", sections Word selection, Programme flow, Data
architecture, Instruction corpus: The collection reading / grouping / recording observations); the 68 active method rules `collection.*`; the designs #2505 (layers 1-2), #2507 (lexical stage), #2484 (node and
observation rules), #2528 stage 4 design v2 (the researcher: "Approve D1, D2"; D3-D5 stand), #2538 validation plan v9 (the researcher: "Yes, build it" / "Yes, promote it"), #2526 grouping proposal.
Not re-read in full: #2463 earlier entries before 2026-11-11, #2329/#2319/#2318 (the older Analysis_phase_1 specification, superseded by the collection method), the 2412 engagement run.
Authority, highest first: (1) the researcher's final overview of 2026-11-24 (the message beginning "the S1 data pull" and its corrections, and the two messages after it); (2) the researcher's other
words in date order, later over earlier; (3) designs and rules the researcher approved; (4) anything I wrote that the researcher did not approve (never binding; listed only to show what changed).
Collision to remember: the researcher's "Step 1, Step 2, Step 3" (2026-11-24) are the steps of the flow. My code's ledger step called "S1" (word-sense) is something else. The two must never again be
confused (conflict C1).

## 1. The thread (what exists before the analysis; the analysis does not rebuild it)

T1. Base data: every verse with its Hebrew/Greek words; `verse_lexical` = the mechanical structural reading of each verse, built once, before any collection exists, complete before a collection is read; it
    records structure and nothing of what a word does for the inner being (researcher 2026-11-15, 2026-11-20 Q1; Programme "Base_data").
T2. Surfaces (ESV words/phrases) sorted into four groups: behaviour, inner_being_state, entity, other; "roughly 90% correct, with an acceptable margin"; wrongly sorted items are "picked up during the
    deeper analysis, and compensate for" (2026-11-20).
T3. Collections: surfaces of groups 1 and 2 collated by likeness/relatedness of behaviour (about 169). Each surface through its base Strong's is connected with its verses. A collection carries the verses
    that are read, is the unit through which the stages are gated, and becomes a narrative chapter (Programme).
T4. WordNet network held in iba.db (2026-11-24, #2548): `surface_relation`, `surface_network_group`: every surface's WordNet group and pairs (same_base, both, ...), 154 no-pair surfaces, 23 not in WordNet.
T5. Entity and other surfaces are not collection members; they enter only as words standing with a member surface, as nodes of the observation that covers them (Programme "Fallout").
T6. Verse-level analysis is not an entry point (2026-11-24): "setting a verse as an entry point is not feasible nor correct"; the entry is a collection; the smallest unit within it is a surface (in a subgroup).
T7. The five stages (2026-11-15): 1 verse-reading lexical; 2 grouping of surfaces; 3 verse-lexical observations from base data + collection data; 4 inner-being analysis from the stage 3 observations (first step of
    claims); 5 claims (not decided, out of scope). "Phase 3 and 4" and "phase 4" in the researcher's words are stages 3 and 4. Engagement (assessing each member surface in each verse by the role it takes) is
    described in the Programme as run on a collection before it is read; its status is a gap (G2).

## 2. Cross-cutting requirements (apply to every process below)

X1 Codified and repeatable: every operation is a verb of the app, same result every time, no scratch helper per collection; learning lives in code, database and config, never in scratch (2026-11-21).
X2 Purpose: accuracy, quality, efficiency, less rework, no reading the same data twice unnecessarily (2026-11-21).
X3 Targeted reads (2026-11-24): never read everything into memory and then scan; pull for the unit, process by the unit, write the result by the unit; pull data specific to the read when looking at trends
   across units; every lookup is pinpointed (indexed, chunked, none per item; RW-14).
X4 Validation is part of the build, not after-the-fact repair (2026-11-24).
X5 Nothing is left in the air (2026-11-15, 2026-11-24): at the end every observation of the scope is fixed or deleted, no observation or node left unfixed, every word node complete or with its reason, every
   deferral owned by a named collection (RW-13).
X6 Two markers only (2026-11-22): evidence (observations about the data, verse-based by definition) and inner_being (observations about the working of the inner being based on evidence; building blocks of
   stage 5, not claims). The marker follows content and purpose, never stage and never the node's role. An observation that is neither is deleted (comment first). Set when the observation is created by the
   item answered; a file never sets it (RW-12, VA-05).
X7 Repair first, delete last (2026-11-22): restate so it is true and founded (a restatement that changes meaning is checked against the base data); complete node columns; consolidate duplicates; delete a node only
   when it cannot be referenced and another node carries the context; delete an observation only when meaningless and not repairable (comment first). Nothing is physically deleted (soft delete with reason).
X8 No older observation is discarded without verified consumption (2026-11-22; VA-03): the mapping is stated in words, every word occurrence is on a carrier node or named not carried with a reason, traces re-pointed,
   `consumed_by` recorded, then deleted. An observation that holds more than one finding is split first. An older observation may be kept (with its marker), merged, consumed, deleted as neither, or deferred to a
   named collection (RW-13). An observation of any stage may be inner_being when it traces to evidence.
X9 Observation rules (RO11, RG-01..25, RW-01..14, RS-02/04/05/08/10, B:130-134, 2484 N1-N15): one observation per finding; same text never twice (a second subject gains a node); concise, tied to the verse by
   reference, never a restatement (no run longer than max_verse_words_copied); basis stated or read; kinds and parts per item; node roles per occurrence from the verse (never from the cluster); lexical layers
   state what the dictionary, the verses and the stored structure show and never what a word does for the inner being (nodes role `lexical`, no route).
X10 Node rules: a node cannot exist without a live observation; a live observation has at least one live node; a node has one surface; each word node carries verse_reference, verse_lexical_id, surface, strong,
    morph_code, role, collection_id, subgroup_id (from the step where the grouping exists), source_stage, seq; a column the data cannot give is left empty with its reason in disposition_note (2484 section 3; RW-12).
    A trace to a deleted observation is refused (IB-07). The subgroup is on the node (LR-05).
X11 Every change is kept in ib_observation_change with its reason; a whole file is checked whole and written in one transaction or refused entirely; -Check previews and writes nothing.
X12 A step closes only when every row it demands is answered (observation with nodes, or a recorded none with a permitted reason) and validated by the check; the next step does not open before it (LR-04). A stage
    that finds an earlier observation wrong returns to the earlier stage: the row is answered again and withdraws the earlier observation with its reason.
X13 Lexical and inner-being readings never run together (2026-11-14, Programme); evidence and inner-being validation are separate, never concurrent, each with its own completeness check and its own
    expectations (2026-11-22, VA-06).
X14 AI decides in the majority of cases; the researcher scrutinises; the researcher sees only what the evidence could not settle (2026-11-14). A result is tested as sensible, reasonable, defensible.
X15 The Claude conduct rules: P1-P8 of v2 stand (specification before work; no scratch; fresh creation; nothing called compliant without the check that shows it; targeted reads; approval where the hook requires;
    commit only at close; decide from the spec and state the basis).

## 3. The processes, in order. Each: PURPOSE, INPUT (exactly what is read), OUTPUT (exactly what is written), GATES, SOURCES (dated), DRAFTS (what I tried and changed), SURVIVOR, GAP.

### P1. Step 1: the grouping pull
PURPOSE: collect what the grouping needs. INPUT: all surfaces of the collection (surface_term via the collection index) and, from the WordNet tables, each surface's network group and its pairs with the other
surfaces of the collection. Nothing else: no verse_lexical, no verse text, no observation, no verse. OUTPUT: a working set (file or memory) with one row per surface.
SOURCES: 2026-11-24 "the S1 data pull ... get all the surfaces of the collection, and to get the assignment of the surfaces to groups from the new tables. It is not necessary to pull the entire verse-lexical at this
stage"; 2026-11-15 #2509 "the surface groups has nothing to do with the inner being. it is about the meaning of the surface words"; 2026-11-21 Q3-Q6 (#2526): meaning in context, hidden meaning in the different Strong's
codes, concepts only in stage 4.
DRAFTS: #2509 v1 grouping by dictionary meaning (rejected 2026-11-15: "grouping is not a skill you have ... overengineered"); the 2026-11-21 rebuild reading verses (GP-01 "reads verses"); the 2026-11-24 rebuild
(GroupPull reads no verse; WordNet seed). SURVIVOR: the 2026-11-24 form. GAP: none known in the spec; code audit pending (the seed grouping proposes, Claude amends by meaning).

### P2. Step 2: the subgroups
PURPOSE: form the unit of reading. INPUT: the P1 set. OUTPUT: the subgroup tables (collection_subgroup, collection_subgroup_surface); no JSON. A surface WordNet does not hold is a subgroup of its own and still goes
through the subgroup analysis. A surface is placed whole in one subgroup (never split by Strong's code); a surface plainly not a member in meaning is set aside with its reason (change procedure moves it out of the
collection); an uncertain placement is marked uncertain and listed; a small collection is one subgroup by default (GP-01..04). Every change is a surface_event with its reason.
SOURCES: 2026-11-24 "step 2 correction. the output is updating the sub group table. no json required. missing wordnet item - treat them as a subgroup on their own"; 2026-11-21 Q4 "exactly what the surface subgroup
are"; GP-01..04. GATE (grouping_gate): every surface placed or isolated with a reason, every subgroup holds a surface; the researcher's Subgroup instruction corrects a placement and wins (GP-04).
GAP G5: "collection status - first check then you ask me": there is no recorded field that says a collection is complete (see P12).

### The subgroup loop (P3 to P8): for ONE subgroup at a time, in isolation. The pull of each step is limited to that subgroup's surfaces and verses. Nothing of another subgroup is read or written.

### P3. Lexical reading of the words of the subgroup (stage 1)  [my ledger step "S1"; see conflict C1]
PURPOSE: the lexical meaning of each word in its verses ("each collection must be digested into observations for lexical meaning first", 2026-11-20; "complete the verse-lexical observations for the underlying
surfaces and verses"). INPUT (per #2507/Programme): each word (surface with lettered Strong's) of the subgroup, its occurrences in verse_lexical, verse text, lexicon meaning, faces, prompts, existing observations.
OUTPUT: one observation per sense the verses give the word, with the occurrences it holds for (kind term/face, stage lexical, nature evidence, node role lexical). Function words get none (RG-22).
SOURCES: 2026-11-15 stage 1 definition; 2026-11-20 Q4-7; #2507 section 3.1 (approved "I will approve for the build"); Programme stage table (the redesigned step: one observation per sense).
DRAFTS: #2505 had no word step; #2507 v4 added it; code built it as a collection-wide ledger step, then (2026-11-24) read after grouping inside the subgroup.
SURVIVOR: kept. It is the stage 1 reading of the researcher's own 2026-11-15/20 definitions and #2507. GAP G1: the 2026-11-24 overview does not mention it; its place relative to P4 (before, as "lexical first", or
inside "1.1 and 1.2") is not stated by the researcher. Decision made here: it is the first step of the loop, closed before 1.1, because 2026-11-20 says lexical first; the researcher is told it is the one point of
the flow his overview does not name. The code calls it S1 and must be renamed "words" in every message to end the collision with Step 1.

### P4. Steps 1.1 and 1.2 (stage 3, layer 1)
PURPOSE: 1.1 what the subgroup's words mean as a group ("place the words into groups of what it is or does ... words that has no inner being role is isolated" 2026-11-14 as read by the later rulings: layers 1 and 2
are not inner-being aware, 2026-11-15); 1.2 enrich the group by studying the Strong's codes, validate the grouping, a short definition from the lexicon, the codes as the link to usage (2026-11-14).
INPUT (2026-11-24, in full): the FULL verse_lexical for every verse in the subgroup; the verse text; the existing observations on those occurrences whose nature is evidence or NULL; the subgroup as data (its
surfaces); the pairings per WordNet. OUTPUT: 1.1 one group-definition observation (kind group) with nodes on every occurrence of the group's surfaces; 1.2 one enrichment observation with a node for every Strong's code
of the group; both evidence, lexical, role lexical; "create or update every observation / node that applies to these two steps" (older ones are answered per X8). Never a none.
GATE: P3 closed for the subgroup; 1.1 before 1.2.
DRAFTS: #2505 design (group-definition judged "what does each word do for the inner being" - later corrected to lexical by 2026-11-15 "did not respect the boundaries between lexical and inner being"). SURVIVOR: lexical.

### P5. Step 2.1: pairings (stage 3, layer 2)
PURPOSE: what stands with the subgroup's surfaces in the verses (2026-11-14 layer 2 step 1: which words pair with the grouping; which other words stand out; qualifiers and their significance; entities and whether
they differ; direction of travel; double meanings; are groups related or interchangeable). INPUT: the P4 pull; the WordNet pairings as the CONTROL, compared with the pairings in the verse-lexical (both / WordNet only /
verse only). OUTPUT (2026-11-24): "update existing observations that is about pairing, and create new observations by verse"; "each subgroup surface will have its own observation, when it gets to 3.2 then these
observations are pulled together". So the unit is the verse: one observation per (subgroup, verse) for each of pairing, qualifier, entity, direction present in that verse, nodes on the subgroup's occurrences in that verse and
the partner words; double-meaning stays per surface (it compares verses). No observation joins two subgroups. No minimum number of verses. All evidence, lexical.
SURVIVOR and conflict C3: the 2026-11-14 text and #2505 design are per group; the 2026-11-24 text is by verse; the later governs. Consequence: far more observations (thought: about 118 rows for one mid subgroup of 43 verses).
GAP G8: the volume this makes for a whole collection is not budgeted anywhere; the researcher has not seen it.
Removed: the group-relation item (it joined two subgroups: against "each subgroup surface its own observation") and the 3-verse threshold (never the researcher's; the Programme lists it as "not yet defined").

### P6. The sweep: remaining observations with NULL nature
PURPOSE: "inspect all the remaining observations with null nature and any observations that is not clearly inner being related at this point is candidates for deletion" (2026-11-24); "All non-inner-being observations with
null nature should now be deleted. If not, then something went wrong that need to be fixed, not just to perform a scratch method for the deletion" (2026-11-24). INPUT: the older observations with a node on the subgroup's
occurrences and nature NULL, not yet judged. OUTPUT: each answered by X8 (kept with a marker, merged, consumed, deleted as neither, deferred); deletions are marked deleted in the loop through the verb with a comment first.
An observation that also holds nodes outside the subgroup is answered where all its holders are read. END STATE: after the sweep and P3-P5 no observation on the subgroup's occurrences has nature NULL unless deferred to a
named collection; a non-inner-being NULL left over is a defect of the verbs, not something to delete by a scratch route.
CONFLICT C6: older observations that state evidence. 2026-11-22 (v9) and the rules say they are kept as evidence, merged, or consumed after verification; the deletion order applies to NULL, not to marked evidence.

### P7. Evidence-layer validation (inside the loop, before 3.1)
INPUT: the observations of the subgroup. CHECKS (2026-11-22 expectations, VA-06, 2538 v9 section 6, evidence column): every observation of the scope marked; none without a live node; no word node missing a required
column without its reason; no live trace to a deleted observation; no two observations of one meaning; every word has its stage 1 observations; every subgroup its stage 3; every in-scope occurrence a node with a role;
every finding closed or deferred to a named collection. Inner being is not judged here. 3.1 does not open until this passes (open_gate).
GAP G7: the Programme records that no content check exists ("the structural checks have passed while the content was wrong"). Content (is the observation true, founded, coherent) is judged by reading, by me, and
is recorded; no code tests it. The specification therefore requires my reading of each observation written to be recorded against its evidence, and says so in the close report.

### P8. Step 3.1 (start of stage 4): elements of the subgroup
PURPOSE: "start of phase 4. dump the data in memory and extract the evidence observations + verse text for all the verses in the subgroup. prepare and write out all the observations for 3.1 this is the end of sub
group loop" (2026-11-24). INPUT: the evidence (stage 3 and stage 1) observations of the subgroup and the verse text; read back to base data only occasionally, recorded (#2528 E3). OUTPUT: findings on the nine items
(role, polarity, object, enactment, party with route, circumstance, operation with chain, flag; never meaning), kind per item, nature inner_being, each resting on named evidence by a traced node and carrying
occurrence nodes with roles other than lexical; every stage 3 observation of the subgroup rested on or declared not_used with a reason (IB-04). A finding is a building block, not a claim.
SOURCES: 2026-11-21 Q7; #2528 design v2 (D1, D2 approved, D3-D5 no objection); IB-01..06.

### After the loop (all subgroups of the collection)
### P9. Inner-being validation
CONFLICT C5. 2026-11-24 first message: "On completion of all the subgroups [do] the validation checks for inner being element observations." 2026-11-24 last message: "inner being validation can only complete after step
3.3 to remove the inner-being observations that cannot be traced." SURVIVOR: it starts after the loop and completes after 3.3. CHECKS (v9 section 6, IB-07): every inner-being observation traced to live evidence
or self-evidencing; no reference to deleted evidence; every in-scope observation marked; no two of one meaning; no consumed deletion without its verified record; every finding closed or deferred; inner-being
observations that cannot be traced are removed (repair first: find evidence and trace it, create evidence only when none states the fact and it earns its place, restate; delete last, with the reason).
A created evidence observation must earn its place (v9 section 4).

### P10. Step 3.2: behaviours of the collection
INPUT: "pull all the observations of all the subgroups for inner being" (2026-11-24). OUTPUT: behaviours discovered as flag findings of type discovery that name them and gather the 3.1 observations by traced nodes (a
behaviour may be one subgroup, part of one, or several; a subgroup may form none); findings of operation, chain, party, circumstance, role relating elements across subgroups; every 3.1 observation gathered or declared
not_gathered with a reason; at least one behaviour or a recorded none with reason. No claim.

### P11. Step 3.3: across collections
GATE: "dependent on the completion of all partner collections. This step check if there are any partner in the observations where the partner collection is not completed (check against the collection status)"; "collection
status - first check then you ask me" (2026-11-24). INPUT: "a pull of all the inner-being observations for all the collections in scope. the analysis then review the observations across the collections." OUTPUT: findings
resting on 3.1/3.2 observations with nodes on both sides in the shared verses. The existing design (#2528 E5: rows per subgroup and partner collection) survives by the researcher's no-objection; its threshold of
shared verses was never the researcher's. DECISION: no minimum (a row for any subgroup and partner collection that share a verse), with a none and reason where the shared verses show no working together (the item allows
none). GAP G3: whether rows per subgroup-partner is how the researcher wants "review across the collections" is not stated beyond the pull; the design is carried by no-objection.

### P12. Completion of a collection and the next partner
A collection is complete when P1-P11 are closed, its validation passes in both layers, and every deferral to it by another collection has been taken up. GAP G5: no field records completion, and 3.3 reads a
status. The researcher is asked before the status is used. "Which partner collection should be introduced next" (2026-11-24) is open and is the researcher's; the proof of the method is a collection built from nothing.

## 3A. How to read, and what to do with the existing observations, process by process (added 2026-11-25 after the researcher found P3 silent on both)

Sources: RG-01..RG-25, RW-01..RW-14, RS-04, RS-05, VA-03 to VA-05, IB-01 to IB-07; the approved design #2507 (sections 2, 3.1 and 9); #2538 validation plan v9 (principles 2, 4, 5, 7, 10, 13, 14 and section 5); the researcher's words of 2026-11-14, 2026-11-15, 2026-11-22 and 2026-11-24 quoted in section 3. Where a line below is my own derivation and not the researcher's, it is marked (derived).

### A. The procedure for an existing (older) observation, the same in every process
An existing observation is one that is live, has a live node on an occurrence the step reads, and was not written by this build. It is shown in the pull whole (nature evidence or NULL at stages 1 to 3; inner_being at stage 4). It is answered ONCE, by the step whose NEW observation carries what it says (derived from "update existing observations that is about pairing" and "create or update every observation / node that applies to these two steps", 2026-11-24). The test, for each, in this order (RS-04; v9 section 5):
1. Read its wording against the verse and the stored data (verse text, verse_lexical, the lexicon). The stage never decides what it is (RS-04).
2. Does it hold more than one finding? Split it first, one finding per observation (v9 section 5).
3. Is it true and founded? If it says more than the verse shows, or something the data contradicts, restate it to what the data show and check the restatement against the base data (a restatement that changes the meaning is validated against the base data). If it cannot be made true, delete it with the reason (repair first, delete last, X7).
4. What does it say, by content? Evidence: states what the data are or show, tied to a verse. Inner being: states how something works in the inner being, based on evidence. Both: split. Neither: delete (principle 13: comment first with the reason, and the occurrences no other live observation holds). The marker follows content, never stage or the node's role.
5. Does a NEW observation of this build already say it? Then it is CONSUMED: every word occurrence of the old observation is on a live node of a carrier or is named as not carried with its reason, the mapping is stated in words (what the old says, which carrier states each part), the traces to it are re-pointed, `consumed_by` is recorded, and only then is it deleted. Never discarded without that verification (2026-11-22).
6. Does it say something the step's new observation lacks and that the step may hold? Then it is ADOPTED: kept in place, the nodes it lacks for the demanded occurrences added, a node without a role given the item's role, the marker set by content; or merged into the new observation (the nodes move, same text only).
7. Is it held also by another subgroup or collection? It is not deleted from here: it is deferred to the named collection (marked now, only the finding left to that collection) or answered where all its holders are read (v9 principle 14; found necessary by the audit of 2026-11-25).
8. Every answer keeps its reason in ib_observation_change. A node of a kept observation that lacks a required column is completed from the data where the data gives it (collection from the surface, surface and strong from the occurrence, verse from the verse table), and where it cannot (the role of an older word, say) its reason is written on the node.

Which step answers which (derived): word-level lexical observations (kinds term or face; the M0.1, M0.4, M0.5 questions; senses of a word) at P3; observations of the group's meaning or the Strong's enrichment of the group at P4; observations of pairing, qualifier, negation and its reach, entity, direction, connective, relation, double meaning at P5, by verse; anything still NULL after P3 to P5 at P6 (the sweep); older inner-being observations at P8 and P10. THE CODE DOES NOT DO THIS: it demands every older observation on the occurrences at the first row that touches them, which is the word step (audit gap G-i).

### P3. How to read the words of the subgroup
- The unit is a word: the surface with its lettered Strong's code (RG-21, B:113), read in each verse it stands in, never the bare lemma and never aggregated across codes. A word that is a function word in every occurrence has no row of its own except a negator and a connective (RG-22).
- Evidence, in this order (RG-08, #2507 section 3.1): (1) the verse text and the occurrence's stored structure (morph read, not carried: RG-14; the unit and gloss in verse_lexical); (2) the three meaning sources for the code read together, none picked and the others dropped (strong_meaning_tree, the lexicons LSJ and Mounce); (3) the ESV rendering of the word across its verses, whether the English adds or hides, the literal sense beside the rendering; (4) the question list M0.1, M0.4, M0.5 as prompts for the areas to explore (RG-17): a question that does not apply is not answered and no answer is manufactured.
- What is written: one observation for each sense the verses give the word, with the occurrences it holds for (together every occurrence, none left out). A sense that departs from the usual gloss is a face (RG-09), recorded as it appears in these verses. A homonym or a name with no meaningful context is recorded as such, a data error is flagged and not fixed (RG-16). Several readings open: each is recorded and the choice marked "I read" (RG-08).
- What it says: what the word means in these verses as the verses and the stored data show it, naming the verses by reference; concise; no restatement of the verse text or of the dictionary range; a transliteration never without its gloss (RW-04). It never says what the word does for the inner being. The different Strong's codes of one surface are its possible hidden meanings: they are evidence and are recorded here (researcher 2026-11-21 Q3; GP-03).
- Existing observations: the older ones of the lexical kinds on these occurrences (the verse-reading term and face observations, prior-capture, engagement and the like) are treated by procedure A: adopted where they already state a sense, restated where untrue or stronger than the verse, consumed where the new sense observation says the same, deleted where neither evidence nor inner being. The older observations about pairings, groups or inner-being workings are NOT answered here (they wait for their own step).

### P4. How to read for 1.1 and 1.2
- 1.1: what the subgroup's surfaces mean together as the dictionary gives their meaning: the one meaning, or the one kind of meaning, they share, in words the Strong's meaning of their codes supports; the group is named for it. Validate the grouping against the words as read in P3: a surface that does not fit goes back to the grouping with its reason (set aside by the change procedure), it is not forced in. It never says what the group does for the inner being.
- 1.2: what the Strong's codes of the group say: a short definition from the lexicon entries (for example what meditation means), every code of the group named as the link to the group's usage, and what the different codes of one surface add (hidden meaning). A node for every code.
- Existing observations: older observations that state the meaning or enrichment of the group (any stage), by procedure A.

### P5. How to read for 2.1, by verse
- For each verse of the subgroup, from verse_lexical (which holds the structure; nothing is evaluated that is not stored): the words that stand with the subgroup's surface and where each stands (side and distance from the stored positions); which of them belong to another collection and which stand out; the WordNet pairings compared with these (both, WordNet only, verse only), the WordNet-only ones as pairings to look for and the verse-only ones as pairings with no control; the negators and the word each reaches (adjacency is not scope: the observation names the word reached); the qualifiers and what each gives the word by the grammar (what it gives the behaviour is stage 4); the entities named or referred to, by name or pronoun, and whether they differ from verse to verse; the direction of travel by the grammar. Double meaning: a surface that carries more than one code, compared across its verses.
- One observation for each (subgroup, verse) and item present; the subgroup's surface has its own observation in the verse and none joins two subgroups (they are pulled together at 3.2).
- Existing observations: the older observations on pairing, qualifier, negation, entity, direction and connective structure on these verses are updated (restated or adopted) or consumed into the verse's new observation, by procedure A; an older observation that spans several verses is split or consumed by several.

### P6. The sweep
After P3 to P5 every older observation of nature NULL on the subgroup's occurrences has been marked, deleted, deferred or consumed. What remains is judged by procedure A, steps 3 to 7. A non-inner-being NULL that cannot be answered by the verbs means a verb is missing (fix the verb); it is not removed by a scratch route (2026-11-24).

### P8. How to read for 3.1
- Input: the evidence observations of the subgroup (by marker) and the verse text of all its verses; the base data is read back only occasionally and the verse and reason are recorded (#2528 E3).
- What is read: what the evidence shows of the elements of a behaviour of the inner being: what is done and its mode (the operation, with its chain), whether a refusal or a pursuit, what it is directed at, the outward act, the other party with the route, the circumstance, and what a qualifier or a variation of the word gives the working (the dimension).
- What is written: findings on the nine items (never meaning, which is stage 1), each resting on named evidence by a traced node and carrying occurrence nodes with a role other than lexical, chosen from the verse and never from the cluster (RG-03, RG-24). Every stage 3 observation of the subgroup is rested on or declared not_used with its reason. A word that holds nothing for the inner being takes the role standalone, so a word not read can be told from one read and found empty.
- Existing observations: the older inner-being observations on the occurrences are shown and answered by procedure A (accepted, modified, merged, deleted, or consumed into a 3.1 finding that says the same), each with a trace to evidence or self-evidencing (IB-07, IB-05).

### P10 and P11
- 3.2: read the element observations of all the subgroups and discover the behaviours: a flag finding of type discovery that names a behaviour and gathers its elements by traced nodes; findings that relate elements across subgroups; every element gathered or declared not_gathered; no claim. Existing: older inner-being observations of the collection by procedure A.
- 3.3: read the inner-being observations of all the collections in scope and how the subgroup's and the partner collection's workings relate in the verses they share; each finding rests on named observations of both sides and carries nodes of both sides in the shared verses; none with its reason where the shared verses show no working together. Existing: the partner collections' inner-being observations are part of the input.

### Gap added
G-i (code): older observations are demanded at the first row that touches their occurrences (the word step), not at the step whose new observation carries them; the pairing observations of the verse-reading stage are answered before any new pairing observation exists to carry them.

## 4. Conflicts between the sources, and what survived
C1 Step 1 (flow) vs "S1" (my ledger step for words): rename mine; keep the word step (P3, G1).
C2 Stage numbering of the configuration vs the order of the layers (Programme "alignment ... is open"): resolved by the 2026-11-24 overview: grouping (stage 2) first, then the loop with stages 1, 3, 4 steps inside the subgroup.
C3 2.1 granularity: by verse (2026-11-24) over per group (2026-11-14, #2505): P5. C4 Thresholds of 3 verses: none given by the researcher; removed from 2.1, none in 3.3.
C5 Inner-being validation timing: starts after the loop, completes after 3.3 (P9). C6 Older evidence observations: kept or consumed after verification, never deleted as neither (X8); only NULL natures are swept (P6).
C7 Entry point: collection (T6). C8 Grouping method: WordNet seed plus meaning in context, no verse reading (P1), over the dictionary-meaning method of #2509 which the researcher rejected on 2026-11-15.
C9 Concepts: replaced by collections (2026-11-20 Q5); concept observations are not a stage 3 product.
C10 My invented rule "an older observation is kept only as inner being": removed (v2 section 7, T4); not a source.

## 5. Gaps disclosed (things the researcher's words do not settle, or the system does not hold)
G1 the place of the word step in the 2026-11-24 flow; G2 engagement (precursor in the Programme; withdrawn run #2412; status not checked here); G3 3.3 row definition beyond the pull; G5 no completion status field;
G6 the order of collections and the size of a sitting (Programme: not set); G7 no code check of content; G8 the by-verse volume; G9 the node/observation columns of older pipelines not all complete (Programme "Node");
G10 the per-surface unit of the evidence layer when a surface is in several verses together with another subgroup's surface (handled by "own observation", not verified in code); G11 role of observation as
"claim input" vs evidence beyond the marker (2026-11-22 question, answered: two markers only).

## 6. Status of the code against this file
Not audited process by process. Changes made on 2026-11-25 before this file existed (subgroup-scoped loads, the full pull, 2.1 by verse, removal of the invented rule) are provisional: each is to be checked against P1-P11
and is retained only where it matches. The by-verse migration stays unapplied. The next work, in order: audit P1 through P11 against the code, one process at a time, recording for each: conforms / does not conform /
not built, with the evidence; then the researcher sees the gap register; then repairs, process by process, each with a test that starts from the state the live run starts from.
