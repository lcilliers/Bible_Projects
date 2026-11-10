# #2412 — engagement broken into components Ollama can do (design v1, for approval)

Basis: the researcher's direction of 2026-11-10 (below); how the collection build ran (`iba/app/USER-GUIDE.md` 8.13 the one AI route and versioned prompts, 8.14 collections with two judges that must agree, 8.17 long jobs outside the session); `cfg_setting` module ollama; `ai_call` timings read 2026-11-10; plan v2 (`outputs/escalation/2412-engagement-all-collections-plan-v2-20261110.md`) and the test of the existing observations (`outputs/escalation/2412-engagement-from-existing-observations-test-v1-20261110.md`). Nothing is built (B:105). Estimates are mine, inferential (B:4).

## The direction (researcher, verbatim)

> "I abanded to use ollama for the engagement because you said it cannot do the job. I am discovering if we actually break down the work in more doable components, if we can use ollama better. the excercise with creating the collections which are now almost done, seems to have worked reasonably well."

## What worked in the collection build, and what carries over

The build asked the model one narrow closed question at a time (candidate: synonym, opposite or distinct; score; pole check; associated), through one route with versioned prompts, one `ai_call` row per question, a check that refuses an unusable answer, two judges that must agree for an opposite, a halt after repeated failures, and a detached job with progress, stop and resume. 52,605 calls so far, almost all answered; the short questions take about 4 seconds each (candidate 4.56 s over 17,603 calls, score 3.95 s over 12,281).

## The engagement split into small questions

The unit is one surface in one verse (an item): the verse text, the surface, its Strong's code and gloss, and the existing observations of that verse if any. It fits the 4,096-token window with room to spare. Each question has a closed answer and a one-line reason that quotes the words of the verse.

1. **Triage.** In this verse, does the surface name or describe something of the inner being (thought, will, feeling, desire, attitude, perception, disposition), name an outward act of one, or is it ordinary wording (a speech introducer, a movement, a quantity)? Answer: inner_being, outward_act or none. This is the question for `said` and `say`, and the one most of the 64,568 items need.
2. **Role**, asked only where triage is not none: characteristic or qualifier (and what it gives), or bears_on with object, relational target or enactment, as the engagement roles are defined (`engagement.roles`).
3. **Second judge.** Triage asked again in a differently worded prompt; where the two agree the answer stands, where they differ the item goes to a reading by me.
4. **Observation text and grouping** are made by the app from the answers, as Record and Group do now; nothing new is written to the tables except through them.

## Proving it before a bulk run

The six engaged collections hold 4,636 items that I read myself. Run triage and role on those items only, with the prompts versioned, and compare with my result: how often the model's triage agrees, where it errs (inner-being missed, ordinary wording over-read), and how often the two judges agree and are right. `Ai-Control.ps1 -Action Compare` already reports prompt versions side by side. The prompts are corrected on that set and the agreement written down before any other collection is touched. If the agreement is not good enough, the split is changed or the route is dropped, on that evidence.

## Where Claude's reading stays

- Every item where the two judges differ.
- Every item the model puts at inner_being, outward_act or bears_on, in a sample or in full, as the measured agreement allows (decided after the test, not before).
- A sample of the items set at none, to keep measuring the miss rate through the run.
- Anything the check refuses.

## How it runs

As the collection batch does (8.17): a detached job started through Windows' process service, files under `Logs/longrun/` (progress, stop flag, log), resumable without repeating a judged item, halting after three failures in a row, checking the server and the configured model before the first call (B:124). A pass of 64,568 triage calls at about 4 seconds is about 72 hours if the server takes one question at a time, and every second judge doubles that; whether the server answers several at once is not known and is measured in the test, not assumed. The collection build ends about 08:40 today and both use the same server.

## What would be built (developer mode, after approval)

A verse-and-surface item question in `lib/engagement.py` through the existing AI client, two prompt keys in `cfg_ai_prompt`, a job in `Long-Run.ps1`, a writer that turns the answers into the assessment file format of 8.18 (marked `ollama` and the model tag, inferential until confirmed), the comparison of the test, USER-GUIDE and BUILD.md entries, and a test run on a copy of the database.

## Option for the researcher

- **D (new, recommended with the test first):** build the question set above, prove it on the 4,636 items I read, then decide on the bulk run from the measured agreement. Options A, B and C of plan v2 stay available; D can feed A (the verse-keyed pull) later.
