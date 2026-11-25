# #2538 Layered reading of a collection: specification (v1, 2026-11-25)

Source: the researcher's own words, from the session of 2026-11-21 (recorded in #2538) and the session of 2026-11-24.
Nothing here is Claude's design. Where the researcher's words stop, the text says "not stated" and the point goes to the
researcher; it is not filled by Claude. The quotes are verbatim; the numbered requirements restate them step by step.

## A. Governing requirements

A1. Codified, repeatable, no scratch. "the analysis process must be codified in such a way that it can run 169 times over
many days and even months and every process and output will work exactly the same ... the self learning must be baked into
the code and not live at all in scratch folders." "I definetely do not want you to re-create any helpers each time an
analysis is done." (2026-11-21, #2538)

A2. Purpose of learning: "to ensure accuracy, quality output, efficiency, and to reduce rework or reading the same data
multiple times unneccesary." (2026-11-21)

A3. Validation is part of the build: "all the validation work you did previously are built into the collection build code
to ensure that the validation steps are an integral part of the build, and not a after the fact corrective action."

A4. Targeted reads: "code is written to protect against long running scanning operations through large quantities of data,
and ... every scan for related data is pin pointed and direct and does not have to read through tons of unneccessary data."
"the read of the base data must be done as targeted as possible. Do not read everything into memory, and then start to scan
it ... write the pull of data for a verse [now: for a subgroup], and process by [unit], write the result by [unit]. when you
get to the stage where you are looking at trends across [units], then pull the data specific to the read."

A5. End state: "all the observations for the collection are fixed or deleted and no observations or nodes are left in the air."

A6. A marker (nature) against each observation, old and new.

A7. The entry point is a collection, never a verse: "the smallest unit as entry point is a surface, but this can only apply
for collections that already have gone through a surface subgroup creation process ... the initial analysis run must be a
collection." (This replaces the earlier by-verse idea.)

A8. The researcher must be able to confirm the methods analytically: "because you did not create the observations fresh, I
cannot really confirm that the methods are working properly from an analytic perspective." So a run creates its observations
fresh through the build's own steps; it does not rebuild them from an earlier run's withdrawn findings, and it uses no scratch
deletion: "If not, then something went wrong that need to be fixed, not just to perform a scratch method for the deletion."

## B. The steps (researcher, 2026-11-24, "the S1 data pull" message and its correction)

B1. Step 1 (S1), pull. "the objective is to pull data about surfaces of the collection to create the grouping. It is not
necessary to pull the entire verse-lexical at this stage. I suggest the grouping use the wordnet data prepare the groups.
therefore the query of data in Step 1 should be to get all the surfaces of the collection, and to get the assignment of the
surfaces to groups from the new tables."

B2. Step 2, subgroups. "the output is updating the sub group table. no json required. missing wordnet item - treat them as a
subgroup on their own - still require going through the subgroup analysis." (A surface that is odd, or missing from WordNet,
is a subgroup on its own.)

B3. Steps 1.1 and 1.2, by subgroup. "for each subgroup in isolation (not all subgroups at once) pull the full verse-lexical
for every verse in the subgroup + verse text + existing observations (where nature is evidence or null) + json of surface
subgroup + pairings per wordnet - then do 1.1. and 1.2 and create or update every observation / node that applies to these
two steps."

B4. Step 2.1, same subgroup. "comparing the pairings in wordnet as a control mechanism with the pairings in the
verse-lexical. update existing observations that is about pairing, and create new observations by verse. at this stage the
evidence observations (both old and new) should be complete."
Verse share: "in terms of evidence layer - each subgroup surface will have its own observation, when it gets to 3.2 then
these observations are pulled together."

B5. Clean-up inside the loop. "now inspect all the remaining observations with null nature and any observations that is not
clearly inner being related at this point is candidates for deletion." "deletions - they can be marked as deleted in the loop."
Ruling of 2026-11-24 (last): "All non-inner-being observations with null nature should now be deleted."

B6. Evidence-layer validation, in the loop: "complete all the validation checks for evidence layer compliance."

B7. Step 3.1 (start of phase 4), same subgroup. "dump the data in memory and extract the evidence observations + verse text for
all the verses in the subgroup. prepare and write out all the observations for 3.1 this is the end of sub group loop."

B8. After all subgroups: "the validation checks for inner being element observations." (Ruling of 2026-11-24, later and so
governing: "inner being validation can only complete after step 3.3 to remove the inner-being observations that cannot be
traced.")

B9. Step 3.2. "pull all the observations of all the subgroups for inner being then do 3.2."

B10. Step 3.3. "dependent on the completion of all partner collections. This step check if there are any partner in the
observations where the partner collection is not completed (check against the collection status) [if] none, step 3.3 can be
completed. this step start with a pull of all the inner being observations for all the collections in scope. the analysis then
review the observations across the collections." Collection status: "first check then you ask me."
Ruling of 2026-11-24: "step 3.3 cannot yet open" while partners are open; the partner collections are then introduced one at a
time ("which partner collection should be introduced next").

## E. Earlier instructions found on 2026-11-25 (added after the researcher asked whether the whole phase 1-4 method was checked)

Sources: the researcher's messages in the session transcripts of 2026-10-25 to 2026-11-22 (dates below). Quoted in part; the
full text is in the transcripts.

E1. Stages (2026-11-15, session 58e035fd): "Stage 1 verse-reading lexical ... contains the relational base data but does not
analyse the relations. Stage 2: ... grouping surfaces in 4 groups, then ... collections for group 1 and 2, then creating surface
subgroups with collections. Stage 3 reading base data and collection data and preparing verse-lexical analysis observations
(layer 1.2 and layer 2 (verse lexical only)). Stage 4 using the observations from stage 3 - perform inner being analysis ...
Stage 5 ... claim formulation ... not yet decided." Lexical work and claims "are two processes that should not run concurrent"
(2026-11-14).

E2. Layer 1 step 1 (2026-11-14): "what does the words do for the inner being. place to words into groups ... words that has no
inner being role is isolated ... Each grouping becomes an observation with the surfaces as the nodes."
Layer 1 step 2: "enrich each word grouping by studying the strongs. Validate step 1 grouping ... place the strongs for each
grouping as this will become the link to the usage of the grouping ... short definition ... Each enrichment becomes an
observation with the related strongs as the nodes."
Layer 2 step 1: "which words pair with which grouping; which other words stand out ... are groupings related, are they being
used interchangably ... give special attention to qualifyers, capture the qualifyer signifance; does the group have multiple
entities, does the entities differ from group to group, does the direction of travel change. Each observation for each group
or word becomes a ib_observation with nodes for verse, surface, strong, related surface (entity), role, etc filled in."

E3. Unit of reading (2026-11-20, session 19e3337e): "the surfaces in the collection are further grouped in surface subgroups.
The subgroups becomes the unit of reading. the reading then takes place in layers - each layer deposits its findings as
observations, so it can be available for the next layer ... lexical meaning first, and then the inner being working next ...
then ... across sub groups and collections."

E4. Housekeeping (2026-11-15): "layer 1 step 1 should be in place before the next step, ensure the rules define it, the methods
is in place to do it, that it is all recorded and validated. dont let things hang in the air." "if the claims need to
reference a group it should be able to discover it" (a group column on the node where needed).

E5. Validation (2026-11-22, session 604473ee): "The validation of the evidence observations and claims observations must be
separated, and not run concurrent. both ... must go through a completeness check ... claims observations should not reference
deleted evidence ... the validation for each layer is different."

E6. Older observations (2026-11-22): an observation that is not stage 4 may be classified inner being "as long as it has
evidence traces"; "most of the older observations will be consumed into the new observations and then be deleted as a
duplicate ... under no circumstances should the old observations just be discarded without a clear verification that they
have been consumed."

## C. Not stated (to the researcher; Claude does not decide these)

C1. The thought rerun's starting point: the researcher has now ordered the database rolled back and the run started again.
C2. How a surviving older observation of nature inner_being is handled in B3/B4 (the pull takes evidence or null only;
inner-being observations are read at 3.1 and later). The 2026-11-24 ruling says an older observation is kept only as inner
being.
C3. Which partner collection follows thought (asked 2026-11-24; unanswered).

## D. Conformance check (to be run before any step is called built)

Each step B1-B10 has a test that runs on a copy, from an unwritten state, through the build's own verbs only, and asserts the
pull is the stated pull (what is read, what is not), the writes are the stated writes, and A5 holds at the end of the step.
No test or run may read the earlier run's withdrawn observations as its input (A8).
