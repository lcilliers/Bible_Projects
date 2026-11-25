# #2538 Layered reading of a collection: the full specification Claude builds and works to (v2, 2026-11-25)

Written by Claude for Claude, on the researcher's order of 2026-11-25: "WRITE THE FULL SPECIFICATION IN DETAIL FOR YOURSELF TO ENSURE THAT YOU FULLY
COMPLY. I AM NOT GOING TO RESPECIFY IT, AND I AM NOT GOING TO READ THE SPECIFICATION AGAIN TO CHECK WHERE YOU HAVE GONE WRONG."
So this file is the working contract. The researcher does not re-read it; Claude checks every build and every run against it, item by item, and reports
the result of each check with its evidence. It supersedes v1 (2538-layered-reading-specification-v1-20261125.md).

Sources, all read in this session: the researcher's messages of 2026-10-21 to 2026-11-25 (session transcripts); the 68 active method rules of the steps
collection.* (read in full); the approved designs #2505 (layers 1 and 2), #2507 (the lexical stage), #2484 (node and observation rules); layer.reading config.
Order of authority where sources differ: (1) the researcher's latest words; (2) a method rule or design the researcher approved; (3) anything Claude wrote
without approval. Where a later word of the researcher departs from an approved rule, the rule is changed (config), not worked round.

## 0. How Claude works (conduct; each item is a failure the researcher has named)

P1. The specification comes first. No build, no run, no rollback, no deletion before the notes of what is to be done and what went wrong are written.
P2. Everything the analysis does is a verb of the app (Collection-Build.ps1 actions), codified, repeatable, the same every time. No scratch script, no helper
    written for a collection, no scratch sheet that creates, marks or deletes observations. A thing the verbs cannot do is a defect in the verbs: fix the
    verbs, then run them (researcher 2026-11-21 and 2026-11-24).
P3. Observations are created fresh by the build's steps, in the loop, from the pulled data. An earlier run's withdrawn findings are never an input. A test
    never starts from a half-built state: it starts from the state the live run starts from (researcher 2026-11-24: "you did not create the observations
    fresh, I cannot really confirm that the methods are working properly").
P4. Nothing is called done, safe, or compliant without the check that shows it, and the report says what was checked and what was not. "Compliant" is never
    said of a part not read or not tested (researcher 2026-11-25: "I checked one thing and you did not comply").
P5. Reads are targeted (section 1, A4). No whole-collection load to serve a subgroup. No statement that scans a table. Chunked indexed lookups only (RW-14).
P6. Migrations and live writes: only with the researcher's approval where the hook requires it; never worked round. A named snapshot first for any live change.
P7. Nothing is committed until session close. Banner on every reply in Developer Mode.
P8. A decision is made by Claude from this specification and the rules; a conflict between the researcher's own words is decided by section 9 (stated with its
    basis) and listed in the close report, not asked again.

## 1. Governing requirements (A)

A1. Codified, repeatable, no scratch; self-learning baked into code and config, learned state in the database/config (researcher 2026-11-21, #2538).
A2. Purpose of learning: accuracy, quality, efficiency, less rework, no reading the same data twice unnecessarily.
A3. Validation is integral to the build, not an after-the-fact corrective (2026-11-24).
A4. Targeted reads (2026-11-24): "Do not read everything into memory, and then start to scan it ... write the pull of data for a [unit], and process by [unit],
    write the result by [unit]. when you get to the stage where you are looking at trends across [units], then pull the data specific to the read." Every scan for
    related data "is pin pointed and direct and does not have to read through tons of unnecessary data".
A5. End state of a collection's build: every observation of the scope is fixed or deleted; no observation and no node is left in the air; every word node is
    complete or carries its reason; every deferral is owned by a named collection (RW-13).
A6. A marker (ib_observation.nature) on every observation, old and new. Evidence states what the data are or show, tied to a verse. Inner being states how
    something works in the inner being, based on evidence. The marker follows content, never stage (VA-05, RS-04).
A7. The entry point is a collection, never a verse (2026-11-24). The unit of reading is the surface subgroup, in isolation (2026-11-20, 2026-11-24).
A8. Layers deposit observations so the next layer can use them. Lexical first, then inner being (2026-11-20). Lexical and claims readings never run concurrently
    (2026-11-14). Evidence and inner-being validation are separate, never concurrent, each with its own expectations (2026-11-22; VA-06).
A9. Stages (2026-11-15): 1 verse-reading lexical; 2 grouping (4 groups, collections, subgroups); 3 base data + collection data -> verse-lexical observations
    (layers 1.1, 1.2, 2.1); 4 inner-being analysis from the stage 3 observations (3.1, 3.2, 3.3); 5 claim formulation (not decided, not built here).
A10. Layers 1 and 2 are not inner-being aware: their observations say what the dictionary, the verses and the stored structure show, never what a word does for
    the inner being (LR-02, #2507). Stage 4 observations are inner being and each traces to evidence (IB-07).

## 2. The flow, step by step (B). Each step: PULL (exactly what is read), WRITE (exactly what is written), GATE (what must be true before and after).

### Step S1-pull: the grouping pull (stage 2)   [verb GroupPull]
PULL: all surfaces of the collection (surface_term via collection_link/index) and, from the WordNet tables, each surface's assignment to a network group and its
  pairs with the other surfaces of the collection. Nothing else: no verse_lexical, no verse text, no observation.
WRITE (GroupRecord, one transaction): the subgroup table (collection_subgroup, collection_subgroup_surface). A surface WordNet does not hold is a subgroup of its
  own and still goes through the subgroup analysis. No JSON output. Every surface placed whole in one subgroup (never split by code).
GATE: every surface placed or isolated with a reason; every subgroup holds a surface (grouping_gate). Status of the collection is checked first; the researcher
  is asked before the status is used to open 3.3 ("collection status - first check then you ask me").

### The subgroup loop: for ONE subgroup at a time, never all at once. Every pull below is limited to that subgroup's surfaces and verses.
Order inside the loop: S1 (words) -> 1.1 -> 1.2 -> 2.1 -> sweep -> evidence validation -> 3.1. Nothing of another subgroup is read or written.

### Step S1: words of the subgroup (stage 1, lexical)   [LayerOpen/Pull/Record/Check -Step S1 -Subgroup]
PULL: for each word (surface + lettered Strong's code) of the subgroup, its occurrences (verse_lexical rows of the subgroup's surfaces), the verse text of those
  verses, the Strong's/lexicon meaning, the faces, and the existing observations on those occurrences (section 3). By indexed lookup on the subgroup's term ids.
WRITE: one word-sense observation per sense with the occurrences it holds for, nature evidence, role lexical (LR-02, LX-01, RG-08/09/14/16/21/22). Function words
  get none (RG-22).
GATE: every word of the subgroup answered and validated before 1.1.

### Steps 1.1 and 1.2: group definition and Strong's enrichment (stage 3)
PULL (researcher 2026-11-24, in full): the FULL verse-lexical for every verse in the subgroup; the verse text; the existing observations on those occurrences whose
  nature is evidence or null (not the build's own stages, no cap); the subgroup as data (its surfaces and definition); the pairings per WordNet.
WRITE: 1.1 one group-definition observation for the subgroup (kind group), nodes on every occurrence of its surfaces; 1.2 one strong-enrichment observation (kind
  enrichment), nodes on the occurrences for every Strong's code of the group, a definition from the lexicon, the codes as the link to usage. Both nature evidence,
  role lexical. Create or update every observation and node that applies to these two steps (older ones are answered per section 3).
GATE: 1.1 closed before 1.2; each row answered and validated.

### Step 2.1: pairings (stage 3)
PULL: the same subgroup pull. The WordNet pairings are the CONTROL: compare them with the pairings in the verse-lexical (both, wordnet-only, verse-only).
WRITE: update the existing observations that are about pairing; CREATE NEW OBSERVATIONS BY VERSE. In the evidence layer each subgroup's surface has its OWN
  observation in a verse (no joint observation of two subgroups; "when it gets to 3.2 then these observations are pulled together"). Unit of the 2.1 items
  pairing, qualifier, entity, direction: one observation for each (subgroup, verse) where the item is present, nodes on the subgroup's occurrences in that verse
  and on the partner words. double-meaning: one observation for each surface of the subgroup whose occurrences carry more than one code (it compares verses). No
  threshold on the number of verses (the 3-verse threshold was never the researcher's). qualifier: the word the negator/qualifier reaches is stated (adjacency
  is not scope). entity: who is named and how referred to. direction: from whom to whom, by the grammar. All nature evidence, role lexical.
GATE: at the end of 2.1 "the evidence observations (both old and new) should be complete".

### Sweep and evidence validation (still inside the loop, before 3.1)
SWEEP: inspect every remaining observation with NULL nature on the subgroup's occurrences. Any observation not clearly inner-being related is a candidate for
  deletion; deletions are marked deleted in the loop (soft delete with reason), through the verb, never a scratch method. If a non-inner-being null remains after
  the sweep something went wrong: fix the verb (researcher 2026-11-24).
VALIDATE (evidence layer, collectionvalidate.check + closing_gate evidence): every observation of the scope marked; none without a live node; no word node missing a
  required column without its reason; no live trace to a deleted observation; no two of one text. Evidence only; inner being is not judged here (VA-06).

### Step 3.1 (start of stage 4): elements of the subgroup
PULL: dump the data in memory; extract the evidence observations of the subgroup and the verse text of all its verses. Nothing else (IB-02: stage 4 starts from the
  observations, base data read back only occasionally with a recorded read-back).
WRITE: all the observations for 3.1 (subgroup-analysis findings), each resting on named evidence observations (a traced node on each), nature inner_being, node
  roles other than lexical. Every stage 3 observation of the subgroup is rested on or declared not_used with a reason (IB-04). End of the subgroup loop.

### After all subgroups of the collection
Step 3.2 (collection gathering): pull ALL the inner-being observations of ALL the subgroups; discover behaviours (flag findings, type discovery), every 3.1
  observation gathered or declared not_gathered with a reason (IB-04). It states no claim (stage 5).
Step 3.3 (across collections): opens only when no partner collection in the observations is incomplete (collection status checked against the status the verbs
  define; the researcher is asked). Its pull is all inner-being observations of all collections in scope; the analysis reviews across the collections. A
  partner counts once its own 3.2 is closed. Partner collections are then introduced one at a time.
Inner-being validation (IB-07, VA-06): completes only after 3.3 (researcher 2026-11-24, which supersedes "after the subgroup loop"): it removes the inner-being
  observations that cannot be traced to evidence. Run separately from, and after, the evidence layer passes.

## 3. Older observations (RW-13, VA-03, VA-04, VA-05, RS-04; researcher 2026-11-22: consumed then deleted, never discarded unverified)
Every older live observation (not the build's own stages lexical, layer-1, layer-2, layer-3) with a node on an occurrence of the row is answered ONCE at the record
of the row, by one of: keep or restate (with its marker, by content); merge into a named observation; consume (live observations carry its meaning, stated in
words, every word occurrence on a carrier node or named not carried with reason, traces re-pointed, kept as consumed_by) and only then delete; delete as neither
(comment first; ONLY when it is neither evidence nor inner being); defer to a named collection. An observation of any stage may be inner being when it traces to
evidence. An older observation that states evidence is not forced out because the build writes evidence: it is kept (marked evidence) or consumed into a carrier.
There is NO config rule "kept only as inner being" and NO finding "older_evidence": both were Claude's invention and are removed (migration older_evidence_2538,
BUILD 568, escalation #2555 withdrawn). In the loop the pull shows older observations of nature evidence or null; older inner_being observations are shown at 3.1
(IB-05) and judged for trace in the inner-being validation after 3.3.

## 4. Observation and node requirements (apply to every observation any step writes)
- One observation per finding; the same text is never written twice (RW-03, N8): applied to another verse/word it gains a node on the existing observation.
- Each observation carries its marker (nature) AT CREATION from the item answered (layer.reading items.<item>.nature); a file never sets it (RW-12).
- Each word node carries the node_required columns at creation (strong, verse_reference, surface, morph_code, role, verse_lexical_id, collection_id, subgroup_id);
  a column the data cannot give (node_gap_columns) is left empty with its reason in disposition_note; any other gap refuses the whole file (RW-12).
- The nodes are built from the data (LR-02), never typed. The observation text is concise, tied to its verses by reference in the evidence form, never a
  restatement of the verse (no run longer than max_verse_words_copied), basis stated or read (B:131, RW-04, RW-05).
- A traced node never points at a deleted observation (IB-07). The subgroup is on the node (LR-05).
- Every change keeps ib_observation_change with its reason; nothing is physically deleted (RW-01, VA-01).
- A whole file is checked whole and written in one transaction, or refused entirely (LR-02, GP-02, VA-01). -Check previews and writes nothing.
- A row answered again withdraws its earlier observations with the reason.

## 5. Reads and speed (A4, RW-14)
- load(): NO whole-collection load for a subgroup. The loader takes the subgroup and reads only that subgroup's term ids, their verse_lexical occurrences (by an
  indexed column), the verses of those occurrences, and the observations/nodes on those occurrences, in chunks. The pairs of 2.1 are built for the subgroup's
  verses only.
- Every lookup is by an indexed column with a chunk of ids; none runs once per item of a list; the query plan of every build statement is tested to not scan a
  table (layer.scan scan_ok lists the temporary tables allowed); a statement over layer.scan max_vm_ops is stopped and named.
- Cost is measured and reported per verb for a small and a large subgroup before any live run.

## 6. Verbs, ledger and gates (existing, kept; these must conform to sections 2-5)
LayerOpen/LayerPull/LayerRecord(-Check)/LayerCheck with -Subgroup; ValidatePull/ValidateRecord/ValidateCheck; GroupPull/GroupRecord. The ledger collection_layer_item
derives the rows each step demands from the data. A step is closed when every row is answered and validated and the data demands nothing more (LR-04).
Opening a step for a subgroup judges needs and gates for that subgroup alone (LR-01). The old supersession code (legacy S1 rows, rows of later steps read again)
was written to serve a rebuild from an earlier state; with the database rolled back to the pre-rerun state and the steps run in the loop order, it is reviewed
and kept only if the spec's flow needs it (decision in the gap list).

## 7. The transgressions log (what went wrong; each is a defect to be closed and tested)
T1. 2026-11-24/25: every subgroup pull loads the whole collection (and, for layer 2 and 3.3, every verse_lexical row of every verse in the collection) -> slow, and
    against A4. Code: lib/layerreading.py load() and pull().
T2. The pull is capped and truncated: 80 nodes per row, verse text 200 characters, existing observations 12 and 200 characters, filtered by stage and not by
    nature. The spec pull is full and filters to evidence or null.
T3. 2.1 was built per subgroup/per partner collection with a 3-verse threshold and a group-relation item that joins two subgroups: against "by verse", "each
    subgroup surface its own observation" and "pulled together at 3.2".
T4. "An older observation is kept only as inner being" (older_keep_natures, finding older_evidence, BUILD 568, #2555) was Claude's inference recorded as the
    researcher's ruling, and it contradicts RW-13/VA-05. It led to 98 older EVIDENCE observations being deleted as "neither evidence nor inner being" (false) with
    a false statement that the build held their meaning (not verified: VA-03).
T5. 3.1 and 3.2 of thought were rebuilt from the earlier run's withdrawn findings by scratch scripts; 168 markers and 98 deletions came from scratch-built
    sheets; helper scripts in the temp folder did the filling. Against P2, P3, A1.
T6. The loop test started from a half-built state; the method was proven on thought and on copies of it, never on a collection built from nothing.
T7. A rollback was made before the notes were written (the order P1).
T8. "Compliant" and "the spec is exactly as described" were said before the code was compared (P4).
T9. The researcher's rulings were recorded with words he did not say (T4). Every recorded ruling is now quoted with its date or marked as Claude's.
T10. Migration #2555 and the older_keep_natures guard make live verbs refuse ("the code is ahead of the config").

## 8. The build plan (order; each item closes with its test)
W1. Remove the T4 additions: the older_keep_natures guard and refusal in buildvalidate._answer and layerreading.settings, the older_evidence finding in
    collectionvalidate, their tests, the migration, #2555, BUILD 568 text corrected.
W2. Subgroup-scoped loader (T1, section 5): rewrite load() and the pair building to take the subgroup. Test: same answers as the whole load for that subgroup,
    reads only its ids (counted), no table scan in the plans, time measured.
W3. Full pull in the loop (T2): no caps in the read; evidence-or-null existing observations; complete verse text; WordNet pairings in the 1.1/1.2 pull.
W4. 2.1 by verse (T3): derive per (subgroup, verse) items; drop the threshold and group-relation from 2.1; keep double-meaning per surface; WordNet control per
    verse/partner.
W5. Loop conformance test: from the rolled-back database copy, run one small subgroup through the verbs only (GroupPull skipped where the grouping exists), S1 to
    3.1, asserting each pull's scope and each write against sections 2-4, the sweep, the evidence validation, and that nothing was written outside the subgroup.
W6. Conformance tests for 3.2, 3.3 gate and the inner-being validation after 3.3.
W7. Only then the live run of thought: subgroup by subgroup through the verbs, no scratch; report each step's result with evidence.
W8. Then the next partner collection from nothing ("return" proposed), to prove the method on a collection built from nothing.

## 9. Decisions on conflicts in the researcher's own words (made by Claude, basis stated; not asked again)
D1. 2.1 granularity: "create new observations by verse" and "each subgroup surface will have its own observation" (2026-11-24, later) govern over the per-group
    design of #2505 (2026-11-15, earlier). #2505's items qualifier/entity/direction/pairing change from per-subgroup to per-(subgroup, verse); group-relation is
    removed from 2.1 (it joins two subgroups; 3.2 pulls together). 1.1 and 1.2 stay per subgroup (they define the group).
D2. Inner-being validation timing: after 3.3 (2026-11-24 last message) over "after the subgroup loop" (2026-11-24 first message).
D3. The S1 word-sense step stays: stage 1 lexical (2026-11-15), "lexical first" (2026-11-20), #2507 section 3.1 (approved). It runs inside the subgroup after the
    grouping.
D4. Older evidence observations are kept or consumed, never deleted as "neither" (RW-13, VA-04, VA-05; 2026-11-22). The 2026-11-24 order to delete null-nature
    non-inner-being observations applies to NULL natures only.
D5. Per-subgroup pulls are full (the researcher's list); the working file may carry a digest for reading but the read, the validation and the node building use the
    complete data.

## 10. Acceptance (the check I show before any claim of compliance)
For each of sections 2, 3, 4, 5: a named test, run on a copy of the rolled-back database, passing, with its output; a statement of what is not tested. The close
report lists every deviation from this file. The researcher is shown results, not this file.
