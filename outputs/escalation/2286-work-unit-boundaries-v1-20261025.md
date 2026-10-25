# #2286 prototype step 2: the boundaries of the work unit step

Date: 2026-10-25. Escalation #2286 v5. This is a working paper for discussion. It builds nothing and
decides nothing.

## 1. The boundaries as the researcher set them

| boundary | state |
|---|---|
| Trigger: a request, from the accepted sources (cluster, subgroup, strand, word, Strong's code, verses, chapter or block, claim, observation, thread item, thread) | agreed |
| Output: a JSON | agreed |
| Expected outcome: what the JSON must achieve | unclear |
| Process: how the request becomes the JSON, which varies widely with the request | unclear |

The researcher's point: until this step is clear, any later work is in complete darkness.

## 2. The expected outcome: what the JSON must be fit for

The output is clear in form (a JSON) but not in purpose. One way to pin the purpose down is to ask
what the next step needs to be able to rely on when it receives the JSON. The questions below are
the ones I can see. Each needs your answer; none is settled by the rules as they stand.

| # | question | why it matters | your answer |
|---|---|---|---|
| O1 | Does a work unit carry its **objective**: the question the reading is to answer? Is the objective part of the request, or is it worked out during 0.C? | Rules RM-01, RM-02 and RO10 make the objective the home of what a reading records. The resolver takes no objective; only Reading Open does. | |
| O2 | **Completeness:** must the unit hold every verse that bears on the objective, or only what the request names? | B:94 (scan glosses across all codes before setting a scope) implies the first. The resolver gives the second. | |
| O3 | **Size:** is there a size a single cycle can work properly? Is it set by a number, by the objective, or case by case? | RM-03 says a cluster is not read whole. The only limit in code is 2,500 verses, which is a review trigger, not a working size. | |
| O4 | **Coherence:** must the verses in a unit hang together (one face of a word, one theme, one passage), or may a unit be a mixed set? | A mixed set makes the claims step harder. Segmenting (RM-03) suggests coherence is expected. | |
| O5 | **Exclusions at 0.C:** are verses taken out at this step (a homonym, a name, a word used of nature only), or does every resolved verse go forward and get dealt with in the reading? | B:116 says reading is never held back. RG-16 records homonyms in the reading. Either way the step has to say which. | |
| O6 | **Passage context:** does the unit name the passage each verse is read in, or is that left to the reading? | RG-02 reads the verse in its passage. A chapter or claim scope gives only the verses it cites (`versescope.py` lines 17 and 18). | |
| O7 | **What is already known:** does the unit say what work exists for its verses, or is that the next step's job (0.GAP pre, the collation)? | RM-04 says gather, don't redo. The code puts this in the collation, after the scope. | |
| O8 | **Done:** what makes a work unit finished, so that the cycle can start? | Without this, the step cannot be checked. | |

## 3. The process: why it varies with the request

The requests are not alike in how much has to be decided to get from the request to the verses.
Grouped by that (my grouping, inferential):

| kind of request | sources | what is decided on the way | difficulty |
|---|---|---|---|
| **Given set** | verses, an observation, a claim | almost nothing: the verses are named. What is open is context (O6) and whether the set is complete for the objective (O2). | low |
| **Lexical** | Strong's code, word | which derivatives (grains) are in (B:113, RG-21); homonyms and names (RG-16); whether related words belong (B:94) | medium |
| **Grouping** | cluster, subgroup, strand | the set is wide. It needs an overview and cutting into units (RM-03), and the units need an order. | high |
| **Derived from earlier work** | chapter or block, thread or thread item | the set comes from earlier readings, which may have been done outside the rules (#2260, #2265 to #2267). Is it taken as it stands, or re-checked? | high |

One more case to check: **a theme or question with no selector**, such as "what the bosom shows of
anger". It is not in the list of sources, yet it is how the `anger-bosom` scope arose (M02 Anger &
Wrath narrowed to H3708A, vexation). Translating a theme into selectors may be where most of the
judgement sits. Is a theme a kind of request?

| your answer on the theme request | |
|---|---|

## 4. How to get clarity: a suggestion

Defining the outcome and the process in the abstract has failed before. One practical alternative is
to take two or three real requests of different kinds and walk each one from request to JSON by hand
here, together. We would write down every decision taken on the way and who took it. The outcome
(section 2) and the process (section 3) would then be drawn from what actually happened, not from
a design.

For example: one lexical request, one grouping request (a cluster), and one derived request (a
thread or a chapter block).

| do this? which requests? | |
|---|---|
