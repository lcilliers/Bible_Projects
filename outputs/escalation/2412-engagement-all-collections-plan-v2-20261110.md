# #2412 — engagement on all collections: read each verse once (plan v2, replaces v1)

Basis: the researcher's correction of 2026-11-10 (below); read-only counts from `iba/app/db/iba.db` on 2026-11-10 (scripts in the session scratchpad); the engagement process as run so far (`iba/app/USER-GUIDE.md` 8.18, `iba/app/lib/engagement.py`). Cost figures are my estimates from character counts and file sizes, inferential (B:4). Nothing below is built (B:105).

## The correction (researcher, verbatim)

> "if you have 64000 verse items to read, then it means you are reading a verse multiple times, and passing in a large set of tokens repeatedly. that does not make sense. is there a more optimal mechanism to achieve the objective. also, any surface with more than roughly 1000 verses is highly suspect that it has a large number of verses that has no inner being bearing."

## What the counts show

- The 64,568 items still to assess lie in **24,896 distinct verses**: 2.59 items a verse. The pull is built per collection and per surface, so a verse that holds several member surfaces is written into the file once for each, and read once for each. The verse text alone is 9.3 million characters read per item, against 3.3 million if each verse is read once (2.8 times less). The existing observations of the verse are repeated with it, and they are the larger part of the pull (call: 806 observations on 833 items; 1.1 MB for the pull).
- Surfaces with 1,000 or more items still to assess: **two**, `said` (4,304) and `say` (1,097), 8.4% of all items. The next are know (997), heart (852), saying (825), great (802). The collection saying (7,122 items) is large because it holds many speech words, not because one surface is.
- The researcher's expectation matches the shape of these words: most occurrences of said or say introduce speech and have no bearing; the inner-being cases are the exceptions (said in his heart, the speech that expresses an inner state).

## Proposed mechanism: assess by verse, not by collection

1. **One pull of verses.** For all collections to be engaged, one working file per batch of verses: each distinct verse once, with its ESV text, each member surface it contains (with the collections each belongs to and its draft group), and the existing observations of that verse (any stage) once. Nothing repeats.
2. **One reading of each verse.** I read the verse once and assess all its member surfaces together, which also settles the roles against each other (the characteristic and its qualifier are in the same verse, so the observation is written once, not rediscovered per collection). Output is compact: per verse, an entry for each surface with bearing (role, gives, test, observation); the surfaces with no bearing are listed as a group with one reason for the verse. Each recorded item still carries a reason, expanded by the app from that line.
3. **Record per collection, unchanged.** The app splits the verse assessments back into one assessment per collection and writes them through the existing Record, Group, Review, Close and Check, so the tables, the group rule, the one-escalation-per-collection rule and the checks stay as they are.
4. **Review of the no-bearing verses** (ruling B of #2411) is made on the same verse file, by verse, so a verse is not read a third time per surface.
5. **Large surfaces first screened by verse, not by surface.** For `said`, `say` and any other surface of 1,000 or more items, each verse is still read, because the surface is assessed in every verse it occurs in (the process, and the check refuses a surface not assessed everywhere). What changes is the cost: a verse where `said` is the only member surface needs only the verse text and a one-line reason, and the exceptions (said in his heart, the speech that expresses an inner state) are picked out in reading. I do not propose a rule that sets a surface aside without reading its verses, because that is a new decision on the process (R1 to R4, 2026-11-09) and is the researcher's.

## Estimated effect (inferential)

Reading falls from about 20 million tokens (per item, with repeated observations) to about 3 to 4 million (each verse once, its observations once); writing from about 7 million to about 2 to 3 million. The run is still large, but about five times smaller, and one reading covers every collection that shares the verse.

## What needs building (developer mode, not started)

A verse-keyed pull, a split of the verse assessments into per-collection assessment files, and the compact entry format with its expansion into reasons. These are new Engagement.ps1 actions and a change to `iba/app/lib/engagement.py`; the USER-GUIDE, BUILD.md entries and a test run on a copy of the database follow the same stages as #2406.

## Options for the researcher

- **A (my recommendation):** build the verse-keyed mechanism, then run all collections through it.
- **B:** run per collection as now, with a leaner pull file (observations only for the verses with a relevant one). Nothing to build; saves part of the reading, not the repeated verses.
- **C:** A, with the surfaces of 1,000 or more items done first, as the test of the compact format on a large, mostly no-bearing case.

## Open point on the build job

The collection build ends about 08:40 today; writes while it runs may collide with its own (`database is locked`, as on 2026-11-08). With A, building takes the time until then.
